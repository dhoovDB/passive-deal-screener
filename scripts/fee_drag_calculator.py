#!/usr/bin/env python3
"""Estimate net-to-LP IRR and total fee drag from a private deal's fee stack.

Screening tool, not underwriting. Given a gross deal IRR, the fee stack, the
hold period, and the promote terms, it estimates the LP's net IRR and decomposes
the gross-to-net drag into recurring fees, one-time fees, and promote.

The model mirrors `references/02-fee-stack-library.md` (the "Total-drag
framework"), which treats drag *additively* in annual basis points:

    net LP IRR  ~=  gross IRR
                  - recurring fees   (annual %, paid every year)
                  - one-time fees    (% spread across the hold: fee / hold_years)
                  - promote          (waterfall on profit, annualized below)

Two deliberate simplifications, consistent with `02`'s screening stance:
  * Drag is additive. Fees and promote are each computed against the gross
    return rather than compounding on one another's residual. This is how `02`'s
    worked examples are built; it slightly overstates total drag versus a full
    sequential waterfall, which is the conservative direction for screening.
  * Promote uses a single bullet distribution at exit (no J-curve / interim
    distribution schedule). Distribution timing is a separate LP risk surfaced
    by the skill (`03` -> GEN-11), not a fee-drag input.

For the precise per-deal answer, replace the inputs with the real fee schedule
and waterfall from the PPM. stdlib-only by design (no pip installs).
"""

import argparse
import json
import sys


# --------------------------------------------------------------------------- #
# Pure calculation core (same input -> same output, no side effects)
# --------------------------------------------------------------------------- #

def recurring_drag_bps(annual_fee_pct):
    """Annual drag in bps from recurring fees. A fee charged every year drags
    the IRR by its own rate: 1.5%/yr == 150 bps/yr."""
    return annual_fee_pct * 100.0


def one_time_drag_bps(one_time_fee_pct, hold_years):
    """Annual drag in bps from one-time fees, spread across the hold. A 2%
    one-time fee over 7 years is ~28.6 bps/yr; over 3 years, ~66.7 bps/yr."""
    if hold_years <= 0:
        return 0.0
    return (one_time_fee_pct / hold_years) * 100.0


def promote_drag(gross_irr_pct, hurdle_pct, carry_pct, hold_years, catch_up_pct=100.0):
    """Promote drag in bps via a bullet-exit waterfall on $1 of LP capital.

    Tiers: (1) return of capital + a simple preferred-return accrual to the LP,
    (2) a GP catch-up toward its carry share of distributed profit, scaled by
    `catch_up_pct`, (3) residual profit split (1-carry)/carry LP/GP.

    Returns (drag_bps, detail) where detail carries the LP/GP profit split and
    whether the deal clears the hurdle. Note: with a 100% catch-up the pref
    governs distribution *timing*, not the final split — the GP still ends with
    exactly `carry` of total profit. The pref only changes the LP's share when
    the catch-up is below 100%.
    """
    g = gross_irr_pct / 100.0
    pref = hurdle_pct / 100.0
    carry = carry_pct / 100.0
    catch_up = catch_up_pct / 100.0

    detail = {
        "clears_hurdle": g > pref,
        "gp_profit_share_pct": 0.0,
        "lp_profit_share_pct": 100.0,
        "note": "",
    }

    if hold_years <= 0 or carry <= 0.0:
        return 0.0, detail

    total_profit = (1.0 + g) ** hold_years - 1.0
    if total_profit <= 0.0:
        return 0.0, detail

    pref_accrual = pref * hold_years            # simple pref on $1 (per `02`)
    profit_above_pref = max(0.0, total_profit - pref_accrual)

    # Full catch-up target: the GP take that makes GP == carry of (pref + take).
    if carry < 1.0:
        full_catch_up = carry * pref_accrual / (1.0 - carry)
    else:
        full_catch_up = profit_above_pref
    catch_up_target = catch_up * full_catch_up

    catch_up_taken = min(catch_up_target, profit_above_pref)
    residual = profit_above_pref - catch_up_taken
    gp_profit = catch_up_taken + carry * residual

    lp_terminal = 1.0 + (total_profit - gp_profit)
    lp_net_irr = lp_terminal ** (1.0 / hold_years) - 1.0
    drag_bps = max(0.0, (g - lp_net_irr) * 10000.0)  # promote drag is never negative

    detail["gp_profit_share_pct"] = round(gp_profit / total_profit * 100.0, 2)
    detail["lp_profit_share_pct"] = round((1.0 - gp_profit / total_profit) * 100.0, 2)
    if not detail["clears_hurdle"]:
        detail["note"] = ("Gross IRR is at or below the preferred return - no "
                          "promote is earned, but the LP may not realize the full pref.")
    elif catch_up_pct >= 100.0:
        detail["note"] = (f"With a 100% catch-up, the {hurdle_pct:g}% pref governs "
                          "distribution timing, not the final split - the GP still "
                          f"takes {carry_pct:g}% of total profit.")
    else:
        detail["note"] = (f"Catch-up below 100% lets the {hurdle_pct:g}% pref lift the "
                          "LP's share above the residual split.")
    return drag_bps, detail


def compute_fee_drag(params):
    """Orchestrate the drag estimate from a params dict. Pure: returns a result
    dict, prints nothing."""
    hold = params["hold_years"]

    recurring_pct = (params["mgmt_fee"] + params["admin_fee"]
                     + params["servicing_fee"] + params["fund_mgmt_fee"])
    one_time_pct = (params["acquisition_fee"] + params["disposition_fee"]
                    + params["loan_placement_fee"] + params["refinance_fee"])

    recurring_bps = recurring_drag_bps(recurring_pct)
    one_time_bps = one_time_drag_bps(one_time_pct, hold)
    promote_bps, carry_detail = promote_drag(
        params["gross_irr"], params["hurdle"], params["carry"], hold, params["catch_up"]
    )

    total_bps = recurring_bps + one_time_bps + promote_bps
    net_irr = params["gross_irr"] - total_bps / 100.0

    return {
        "inputs": params,
        "gross_irr_pct": round(params["gross_irr"], 4),
        "net_irr_pct": round(net_irr, 2),
        "total_drag_bps": round(total_bps, 1),
        "total_drag_pct": round(total_bps / 100.0, 2),
        "drag_breakdown_bps": {
            "recurring_fees": round(recurring_bps, 1),
            "one_time_fees": round(one_time_bps, 1),
            "promote": round(promote_bps, 1),
        },
        "carry_analysis": carry_detail,
    }


# --------------------------------------------------------------------------- #
# I/O boundary (argument parsing, formatting, printing)
# --------------------------------------------------------------------------- #

def parse_args(argv):
    p = argparse.ArgumentParser(
        description="Estimate net-to-LP IRR and gross-to-net fee drag for a private deal.",
        epilog="Run with no arguments to reproduce the 02-fee-stack-library worked "
               "example (15 percent gross multifamily, 7-year hold, full stack, ~10.6 percent net).",
    )
    # Defaults reproduce the `02` worked example so a bare run is a live demo.
    p.add_argument("--gross-irr", type=float, default=15.0, help="Gross deal IRR, %% (default: 15)")
    p.add_argument("--hold-years", type=float, default=7.0, help="Hold period in years (default: 7)")
    p.add_argument("--carry", type=float, default=20.0, help="GP promote / carry, %% (default: 20)")
    p.add_argument("--hurdle", type=float, default=8.0, help="Preferred return / hurdle, %% (default: 8)")
    p.add_argument("--catch-up", type=float, default=100.0,
                   help="GP catch-up, %% (100 = full catch-up to carry share; 0 = none)")
    # One-time fees
    p.add_argument("--acquisition-fee", type=float, default=2.0, help="One-time, %% (default: 2)")
    p.add_argument("--disposition-fee", type=float, default=1.0, help="One-time, %% (default: 1)")
    p.add_argument("--loan-placement-fee", type=float, default=0.0, help="One-time, %% (default: 0)")
    p.add_argument("--refinance-fee", type=float, default=0.0, help="One-time, %% (default: 0)")
    # Recurring (annual) fees
    p.add_argument("--mgmt-fee", type=float, default=1.5, help="Annual asset-mgmt fee, %% (default: 1.5)")
    p.add_argument("--admin-fee", type=float, default=0.3, help="Annual admin/IR fee, %% (default: 0.3)")
    p.add_argument("--servicing-fee", type=float, default=0.0, help="Annual servicing fee, %% (default: 0)")
    p.add_argument("--fund-mgmt-fee", type=float, default=0.0, help="Annual fund mgmt fee, %% (default: 0)")
    p.add_argument("--json", action="store_true", help="Emit JSON instead of a human-readable summary")
    p.add_argument("--self-check", action="store_true", help="Run internal checks against `02` and exit")
    return p.parse_args(argv)


def args_to_params(args):
    return {
        "gross_irr": args.gross_irr,
        "hold_years": args.hold_years,
        "carry": args.carry,
        "hurdle": args.hurdle,
        "catch_up": args.catch_up,
        "acquisition_fee": args.acquisition_fee,
        "disposition_fee": args.disposition_fee,
        "loan_placement_fee": args.loan_placement_fee,
        "refinance_fee": args.refinance_fee,
        "mgmt_fee": args.mgmt_fee,
        "admin_fee": args.admin_fee,
        "servicing_fee": args.servicing_fee,
        "fund_mgmt_fee": args.fund_mgmt_fee,
    }


def format_human(r):
    b = r["drag_breakdown_bps"]
    c = r["carry_analysis"]
    lines = [
        "Fee-drag estimate (screening, not underwriting)",
        "=" * 48,
        f"  Gross deal IRR        {r['gross_irr_pct']:>8.2f}%",
        f"  Estimated net LP IRR  {r['net_irr_pct']:>8.2f}%",
        f"  Total fee drag        {r['total_drag_pct']:>8.2f}%  ({r['total_drag_bps']:.0f} bps/yr)",
        "",
        "  Drag breakdown (bps/yr)",
        f"    Recurring fees      {b['recurring_fees']:>8.1f}",
        f"    One-time fees       {b['one_time_fees']:>8.1f}",
        f"    Promote             {b['promote']:>8.1f}",
        "",
        "  Carry / waterfall",
        f"    Clears hurdle       {'yes' if c['clears_hurdle'] else 'no':>8}",
        f"    LP share of profit  {c['lp_profit_share_pct']:>7.1f}%",
        f"    GP share of profit  {c['gp_profit_share_pct']:>7.1f}%",
        f"    {c['note']}",
    ]
    return "\n".join(lines)


def _self_check():
    """Validate the model against `02-fee-stack-library.md` anchor points."""
    ok = True

    # Full worked example (total-drag section): ~10.5-11% net.
    full = compute_fee_drag(args_to_params(parse_args([])))
    if not (10.4 <= full["net_irr_pct"] <= 11.0):
        ok = False
        print(f"FAIL worked example: net {full['net_irr_pct']}% not in 10.4-11.0%")
    else:
        print(f"ok   worked example net IRR = {full['net_irr_pct']}% (expected ~10.5-11%)")

    # Promote-only anchors from the waterfall example: ~150 bps @ 12%, ~200 bps @ 15%.
    for gross, lo, hi in ((12.0, 150.0, 220.0), (15.0, 180.0, 250.0)):
        bps, _ = promote_drag(gross, 8.0, 20.0, 7.0, 100.0)
        if not (lo <= bps <= hi):
            ok = False
            print(f"FAIL promote @ {gross:g}%: {bps:.0f} bps not in {lo:.0f}-{hi:.0f}")
        else:
            print(f"ok   promote @ {gross:g}% gross = {bps:.0f} bps")

    print("PASS" if ok else "FAILED")
    return 0 if ok else 1


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    args = parse_args(argv)
    if args.self_check:
        return _self_check()
    result = compute_fee_drag(args_to_params(args))
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(format_human(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
