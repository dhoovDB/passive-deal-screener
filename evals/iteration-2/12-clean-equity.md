# Eval fixture 12 — Multifamily value-add syndication (LP-aligned structure)
*Iteration-2 run, 2026-07-04, blind generation by fresh-context agent, against SKILL.md (post S1–S3 fixes).*

**Verdict: Pursue with conditions — this is what LP-aligned structure looks like against every `02`/`03` baseline (10% cash co-invest pari-passu, whole-of-fund waterfall with secured clawback, 8% cumulative compounding pref, flat exit cap, fixed debt maturing after the exit, realized net-to-LP track record, T-12 + rent roll + downside case provided). The conditions exist because the deal, as pasted, states no target return, hold, or distribution schedule, and the track-record figures still need third-party verification.**

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Multifamily — value-add 🟢 |
| Deal type | Equity syndication 🟢 |
| Sponsor | **Not stated** by name (track record described: five fully-exited deals, net-to-LP IRRs disclosed) |
| Geography | **Not stated** |
| Minimum investment | **Not stated** |
| Hold | **Not stated** ("planned exit" referenced; debt matures 2 years after it) |
| Raise | **Not stated** |
| Claimed return | **Not stated** — no target IRR/multiple given in the materials as pasted 🔴 |
| Structure | Whole-of-fund waterfall, secured clawback; 8% cumulative **compounding** pref; 20% promote 🟢 |
| Fees | 1% acquisition, 1.5% annual asset management, 1% disposition 🟢 |
| Debt | Fixed-rate, matures 2 years **after** the planned exit 🟢 |
| Underwriting | Exit cap = going-in cap; full T-12, rent roll, downside sensitivity provided 🟢 |

Routing: `01` multifamily value-add (target net 14–18%, realized 12–15%, hold 5–7yrs); `02` equity + waterfall; `03` `GEN-`, `EQUITY-`; `05` VNQ + NCREIF unlevered overlay.

## 2. Return Stress-Test

The materials provide the *inputs* for a stress-test (T-12, rent roll, downside sensitivity, flat exit cap) but the pasted summary states **no target return and no hold** — so the test below runs on category norms, flagged accordingly:

Swing assumptions: **(a) rent growth / reno premium capture** — the only major lever left, since the exit cap is flat and the debt is fixed; **(b) exit-year transaction market** (mitigated: no forced event — debt runs 2 years past plan); **(c) expense inflation vs the T-12 baseline**.

- **Base 🔴 (assumed):** at the `01` category target (14–18% gross-ish), the disclosed fee stack nets roughly 11.5–12% (see §4 script run at an assumed 16%/6yr: **net ≈ 11.8%**, drag ≈ 423bps).
- **Bull:** premium capture above plan → mid-teens net.
- **Bear:** the deal's engineering shows here — flat exit cap means no baked-in compression to unwind; fixed-rate debt kills the rate/refi failure modes (`GEN-10`, `EQUITY-07` structurally absent); maturity 2 years post-exit means a soft Year-5 market can be waited out rather than sold into (`GEN-09` clear). The provided downside sensitivity should be checked against `Q-DS-03`'s bar (flat rents, higher exit cap): LP capital should survive it 🟡 (sensitivity referenced but its cases not shown in the paste).
- **Benchmark (`05`):** at an assumed ~12% net 🔴 vs VNQ 6.47% ≈ **+550bps** — clears the 400–600bps hurdle for a 5–7yr lock-up. NPI overlay: unlevered RE at 4.9% means roughly half-plus of any mid-teens gross is still leverage + value-creation rather than in-place income — normal for value-add, and this deal's fixed-rate, no-compression structure is how that leverage is responsibly carried 🟡. Condition: rerun this section with the actual target and hold.

## 3. Where LP Returns Come From

Value-add returns split between (a) NOI growth from the reno program cashing out at a **flat** exit cap and (b) in-place cash flow. With no compression assumed, exit-value growth must be *earned* through NOI — an asset story, not a financing story: `GEN-07`/`EQUITY-06` affirmatively clear 🟢. The precise cash-flow-vs-exit split and the distribution schedule are not stated → confirm below the 60% exit-dependence line via `Q-DS-01` (`GEN-08` probe — likely fine for the category, unverified here 🟡).

## 4. Fee Stack Summary

| Fee | Stated | `02` range | Read |
|---|---|---|---|
| Acquisition | 1% | 1–2% of equity | Low end 🟢 |
| Asset management | 1.5%/yr | 1–2% annual | In range 🟢 |
| Disposition | 1% | 0.5–1% of sale price | Top of range 🟢 |
| Promote | 20% over 8% cumulative compounding pref | 15–30% over 6–10%; compounding pref is the more LP-favorable variant most deals don't offer (`02`) | In range, LP-favorable pref mechanics 🟢 |
| Waterfall | Whole-of-fund + secured clawback | The materially-better-LP-protection structure per `02`; rare in retail syndications | 🟢 |
| Catch-up rate / tiers | **Not stated** | 100% catch-up = `EQUITY-03` | Ask 🟡 |
| Admin / financing fees | **Not stated** | 0.1–0.5% / 0.5–1.5% | Confirm none lurk |

**Gross-to-net drag ≈ 423bps/yr** at an assumed 16% gross over an assumed 6-year hold 🔴 (`scripts/fee_drag_calculator.py`: recurring 150 + one-time 33 + promote 240 → **net ≈ 11.8%**). The stack is at or below the `02` worked-example norm (~465bps); the whole-of-fund + clawback structure further protects the *realization* of that net. Residual disclosure gap: catch-up rate, admin fees, any loan-placement fee.

## 5. Red Flags

The category's kill-list is affirmatively **clear**, each against its `03` ID: `GEN-01` clear (10% cash co-invest, pari-passu); `EQUITY-01`/`EQUITY-02` clear (whole-of-fund + **secured** clawback); `EQUITY-04`/`EQUITY-05` clear (8%, cumulative, compounding); `EQUITY-06` clear (flat exit cap); `GEN-07`/`GEN-08` no financing story (§3); `GEN-09` clear (maturity 2yrs past exit); `GEN-10`/`EQUITY-07` structurally inapplicable (fixed rate, no refi dependence); `GEN-12`/`GEN-15` clear (full T-12 + rent roll); `GEN-13` clear (downside sensitivity provided); `GEN-05`/`GEN-14` clear (realized, net-to-LP, five exits).

What still fires:

**YELLOW**
- `GEN-11` — no distribution schedule or capital-return milestones stated → `Q-DIST-01`.
- `GEN-18` (probe) — the rent-growth/premium-capture assumption is the deal's one live lever, and no submarket supply/absorption data appears in the paste → `Q-MKT-01`.
- `EQUITY-03` (probe) — catch-up rate unstated; a 100% catch-up would be the standard-but-aggressive lever inside an otherwise LP-friendly waterfall → `Q-FEE-03`/`Q-FEE-04` follow-through.
- `GEN-06` (probe) — affiliate relationships (property management, construction management for the reno) undisclosed → `Q-FEE-02`.
- `GEN-17` (residual) — target return, hold, raise, market: basic snapshot fields absent from the paste (see §6).

No RED or YELLOW–RED flags fire 🟢.

## 6. Missing Disclosures

The `01` value-add essentials are substantially present (rent roll ✓, T-12 ✓, exit cap with sensitivity ✓, debt structure and maturity ✓, refi assumptions moot ✓, prior-exit track record ✓). Remaining gaps:
- **Target net-to-LP return, equity multiple, and hold period** — the deal describes structure but, as pasted, never states what it projects to earn or for how long.
- The **actual five net-to-LP IRR figures** (described as disclosed; not shown here) and deal names/dates for verification.
- Distribution schedule and capital-return milestones (`GEN-11`).
- Catch-up rate and any promote tiers; admin/financing fees.
- Market/submarket and the supply-pipeline data behind rent growth.
- Sponsor name, raise size, minimum; affiliate service providers.

## 7. GP Alignment

The strongest alignment picture in this eval set, on stated terms:
- **Co-invest:** 10% of equity, **cash, pari-passu** — the exact good-answer profile of `Q-GP-01` 🟢; meaningful skin at deal scale.
- **Track record:** five **fully-realized** exits with **net-to-LP** IRRs — the precise standard `GEN-05`/`GEN-14` demand 🟢; verification still required (self-reported until documents confirm) 🟡.
- **Waterfall:** whole-of-fund with a **secured** clawback — the GP cannot keep promote the LP's final outcome didn't earn (`02`) 🟢.
- **Fees:** low-end acquisition fee suggests economics weighted to the promote — i.e., to performance — rather than to closing 🟡 (inference).
- **Open items:** affiliate fees (`Q-FEE-02`), catch-up rate, and how co-invest scales across the sponsor's other deals.

## 8. Questions for the GP

**Must-ask**
1. State the target: net-to-LP IRR, equity multiple, hold — and the distribution schedule with milestones (`Q-DIST-01`). *Bad answer:* a gross figure with the net dodged; "we'll distribute when the deal supports it."
2. `Q-DS-01` — Share of return from in-place cash flow vs exit, and IRR at the (already flat) exit cap under the downside case. *Bad answer:* can't decompose.
3. `Q-MKT-01` — Submarket supply pipeline and absorption behind the rent-growth/premium assumption. *Bad answer:* metro-level optimism; no pipeline acknowledged.
4. `Q-GP-02` (verification form) — The five exits: names, dates, and documentation for the net-to-LP figures; any deals *not* in the five (losers omitted?). *Bad answer:* cherry-picked list; "those were different market conditions" for exclusions.
5. `Q-FEE-03` — Catch-up rate and tier structure above the pref; confirm clawback security mechanics (escrow? guarantee?). *Bad answer:* 100% catch-up brushed off as standard; "clawback's in the docs" without the security terms.
6. `Q-FEE-02` — GP-affiliated service providers (property mgmt, construction), their rates, third-party benchmarks. *Bad answer:* "all arm's-length" without names.
7. `Q-DS-03` (confirmation) — Walk through the provided downside case: flat rents, higher exit cap — does LP capital survive with the pref intact? *Bad answer:* the "downside" still shows a gain on every assumption.
8. `Q-RISK-03` (confirmation) — Deliver the T-12, rent roll, and debt terms referenced. *Bad answer:* friction on what was advertised as available.

**Nice-to-ask:** `Q-GP-03` (regulatory/litigation), `Q-GP-04` (team vs AUM), `Q-LIQ-01` (early-exit options), `Q-DIST-02` (capital-call mechanics), `Q-LIQ-02` (K-1 timing), admin/financing fee confirmation (`Q-FEE-01` residual).

## 9. Diligence Checklist

- Verify the five realized exits: closing statements, K-1s, or fund audits — not the sponsor's summary table.
- PPM/LPA: confirm whole-of-fund waterfall, clawback security, pref compounding language, catch-up, full fee schedule.
- Background/regulatory search on sponsor and principals.
- T-12/rent roll audit against the pro forma; third-party rent comps for post-reno premiums.
- Loan documents: confirm fixed rate, maturity date, no springing provisions.
- Submarket study: supply pipeline, absorption, comp deliveries.

## 10. Verdict

**Pursue with conditions.** Every structural failure mode the `03` library screens for is affirmatively engineered out: alignment is cash and pari-passu, the waterfall is the LP-protective variant with a secured clawback, the pref compounds, the exit assumes no cap-rate help, and the debt cannot force a bad-market sale. The essentials of the `01` disclosure baseline are met, so a merits verdict is warranted — and the merits are good. Biggest swing factor: **rent growth / renovation-premium capture** — with compression and rate risk stripped out, it is the one assumption the return genuinely rides on; the submarket data behind it is the key open item.

**Conditions:** (1) the stated target — net-to-LP IRR, multiple, hold — plus distribution schedule; (2) third-party verification of the five realized exits (including confirming there are no omitted losers); (3) submarket supply/absorption support for the rent assumption; (4) catch-up rate, clawback security mechanics, and affiliate-fee disclosure; (5) confirmation the downside case shows a genuine downside. **Who it suits:** an LP wanting classic value-add multifamily exposure with institutional-grade LP protections, at a likely ~11–12% net (assumption-based 🔴) for a 5–7yr lock-up — comfortably clearing VNQ + the illiquidity hurdle if the target confirms. **What would have to be true:** the verification matches the marketing — the structure already does its job.
