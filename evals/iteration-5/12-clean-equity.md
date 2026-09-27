# Eval fixture 12 — Clean multifamily value-add syndication
*Iteration-5 run, 2026-09-27, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 7712624.*

**Verdict: Pursue.** It's worth more diligence. On every term disclosed, the structure protects LP capital: 10% cash co-invest pari-passu, a whole-of-fund waterfall with a secured clawback, an 8% cumulative compounding pref, in-range fees, five realized exits reported net-to-LP, fixed-rate debt that matures after the planned exit, and a flat exit cap. None of these facts fires a RED or YELLOW flag. The biggest swing factor is the target return itself, which isn't stated. Even the full-fee stack clears the illiquidity hurdle only if the property delivers about 12% gross or better. Get the target gross/net IRR, the hold and the leverage in the next round. These are diligence items, not structural defects.

---

## 1. Deal Snapshot

| Field | Value | Tag |
|---|---|---|
| Asset class | Multifamily — value-add | 🟢 |
| Deal type | Equity syndication | 🟢 |
| Sponsor | Not stated | — |
| Geography / submarket | Not stated | — |
| Minimum investment | Not stated | — |
| Hold period | Not stated. Category norm is 5–7 yrs (`01`). | 🟡 |
| Raise / equity size | Not stated | — |
| Claimed return (gross or net IRR, multiple, CoC) | Not stated | — |
| Pref / promote | 8% cumulative, compounding / 20% | 🟢 |
| Waterfall | Whole-of-fund, secured clawback | 🟢 |
| Fees | 1% acquisition, 1.5% asset mgmt (annual), 1% disposition | 🟢 |
| GP co-invest | 10% of equity, cash, pari-passu | 🟢 |
| Debt | Fixed rate. Matures 2 yrs after the planned exit. LTV, amortization and prepayment terms not stated. | 🟢 / gaps |
| Exit cap | Equal to going-in cap | 🟢 |
| Financials | Full T-12, rent roll, downside sensitivity provided | 🟢 |
| Track record | 5 fully exited deals, net-to-LP IRRs disclosed | 🟢 |

## 2. Return Stress-Test

No target IRR was given, so there is no headline to test. The scenarios below use the `01` category norms as placeholder gross returns. **Every return figure in this section is 🔴 ASSUMED until the GP supplies the pro forma.** The disclosed fee terms are the only inputs taken from the deal.

**Swing assumptions:** (1) NOI lift from the value-add program (rent growth and renovation premiums), (2) exit cap versus going-in (already underwritten flat, so the obvious lever is neutralized), (3) hold length versus the debt maturity (2 yrs of slack before the loan becomes a forced event).

| Case | Gross IRR (assumed) | Hold (assumed) | Net-to-LP IRR (script) | vs VNQ 4.92% (10yr) | Illiquidity hurdle | Read |
|---|---|---|---|---|---|---|
| Bull | 15% | 5 yr | 11.67% | +675 bps | ~300–400 bps | Clears comfortably |
| Base | 15% | 7 yr | 11.04% | +612 bps | ~400–600 bps | Clears (just above the top of the band) |
| Bear | 12% | 7 yr | 8.37% | +345 bps | ~400–600 bps | **Thin / fails** — the lock-up goes uncompensated |

(All three cases assume a 100% catch-up, the conservative case, because the catch-up rate is not stated. With no catch-up, base net rises to 11.80%.)

- **Treasury floor (`05`):** the 10yr Treasury is 5.18%, so base net is about 586 bps over risk-free and bear is only about 319 bps. At this snapshot the Treasury is a tighter floor than VNQ.
- **Category check (`01`):** value-add multifamily realized returns cluster at 12–15% net blended. The base case (about 11% net at 15% gross) sits below that band, so the GP's pro forma has to show a gross return high enough to land in it. 🟡
- **Downside:** a downside sensitivity was provided. Check that its bear case actually stresses rent growth, exit cap *above* going-in, and a hold that runs past plan (Q-DS-03).
- Clearing the spread is necessary, not sufficient. Single-asset concentration and Preqin dispersion (`05`) argue for sitting at the upper end of the hurdle, not the floor.

## 3. Where LP Returns Come From

- **Cap-rate compression: none underwritten.** 🟢 Exit cap equals going-in, so any appreciation has to come from NOI growth the business plan creates. That is an asset story, not a financing story. `EQUITY-06` does not fire, and the `GEN-07` precondition (cap compression) is absent.
- **Leverage: size unknown.** The unlevered overlay (`05`): NCREIF NPI trailed 5.00% (residential 5.3% in 2025), almost all of it income. At a 15% gross levered IRR, roughly 10 points would come from leverage plus the value-add NOI lift. That is normal for value-add equity, but the split between the two can't be measured without the LTV and the unlevered pro forma (Q-DS-02). 🟡
- **Exit share: unmeasured.** A value-add plan realizes much of its NOI uplift at sale, so an exit-weighted return is structurally expected here. With a flat exit cap that is not the >60% cap-compression bet that `GEN-08` targets. Still, the cash-flow versus exit split isn't disclosed, so `GEN-08` stays **unmeasured, not fired**. Route to Q-DS-01. 🟡
- **Refi: none apparent.** Fixed-rate debt maturing after exit implies the plan does not need a refinance. `EQUITY-07` looks absent (🟡 inferred; confirm with Q-EXIT-02).

## 4. Fee Stack Summary

| Fee | Disclosed | `02` range | Aggressive threshold | Read |
|---|---|---|---|---|
| Acquisition | 1% (basis not stated) | 1–2% of equity / 0.5–1.5% of price | >2.5% equity / >2% price | Low end of market 🟢 |
| Asset management | 1.5% annual (basis not stated) | 1–2% of equity, annual | >2.5% | Mid-market 🟢 |
| Disposition | 1% | 0.5–1% of sale price | >1.5% | Top of range but in-market 🟢 |
| Promote | 20% over 8% pref | 15–30% over 6–10% | >30%, pref <6% | Market 🟢 |
| Pref | Cumulative, compounding | Cumulative standard; compounding is LP-favorable | Non-cumulative / simple-only | Better than typical 🟢 |
| Catch-up | Not stated | — | 100% → `EQUITY-03` | Gap (§6) |
| Loan placement / refi | Not stated | 0.5–1.5% of loan | >2% | Gap (§6) |
| Admin / IR / K-1 | Not stated | 0.1–0.5% of equity or $1–3k/LP | >$5k/LP | Gap (§6) |
| Affiliate property / construction mgmt | Not stated | — | — | Gap (§6); `GEN-06` probe |

**Gross-to-net drag: ≈396 bps/yr** (base case: 15% gross, 7-yr hold, 100% catch-up). The breakdown is about 150 bps from recurring fees, about 29 bps one-time and about 217 bps promote. The range across the cases in §2 is **320–431 bps/yr**, depending on hold and catch-up. Undisclosed fees were entered as 0, so the true drag is *at least* this. Gross IRR, hold and catch-up are ASSUMED inputs (§6).

Two caveats on the computed figure:
- The calculator applies the disposition fee to equity. Disclosed as 1% of *sale price* on a levered asset, it lands at a multiple of that on LP equity (for example, about 2.5–3% of equity at roughly 60–65% LTV). 🟡 That adds perhaps 20–30 bps/yr on a 7-yr hold. Confirm the basis.
- The calculator models a simple pref. The compounding pref and the whole-of-fund timing both push promote later and modestly *reduce* promote drag compared with the script's figure. 🟡

## 5. Red Flags

**RED: none.** **YELLOW: none fired on disclosed facts.**

This is a sound structure, and no flag is being manufactured against it. The flags checked and cleared on 🟢 stated facts, cited so the clearance is auditable:

- `GEN-01` (zero co-invest): cleared. 10% cash, pari-passu.
- `GEN-05` / `GEN-14` (GP-IRR divergence / unrealized record): cleared. Five realized exits, reported net-to-LP.
- `EQUITY-01` / `EQUITY-02` (deal-by-deal, no clawback): cleared. Whole-of-fund with a secured clawback.
- `EQUITY-04` / `EQUITY-05` (low or non-cumulative pref): cleared. 8% cumulative, compounding.
- `EQUITY-06` (exit cap below going-in): cleared. Flat.
- `GEN-07` (financing story): precondition absent (no cap compression). Leverage share unmeasured (§3).
- `GEN-09` (maturity inside hold): cleared *for the planned hold*. The 2-yr buffer is the margin if the hold slips.
- `GEN-10` (rate-cap expiry): not applicable. Fixed-rate debt.
- `EQUITY-07` (refi-dependent): absent by inference (🟡).
- `GEN-12` / `GEN-15` (no T-12 / missing financials): cleared. T-12 and rent roll provided.
- `GEN-13` (no downside case): cleared. Sensitivity provided.
- `GEN-16` (no fee/waterfall disclosure): cleared on the core stack. Residual line items in §6.

**Unmeasured, to watch (not fired):**
- `GEN-08`: exit share of return not disclosed.
- `EQUITY-03`: catch-up rate not stated.
- `GEN-06`: affiliate providers not stated.
- `GEN-11`: no distribution schedule. There is also no quoted IRR yet, so the trigger isn't met; it becomes live once a target IRR arrives.
- `GEN-18`: rent-growth assumption and submarket not stated.

A bad answer to the matching §8 question converts any of these into a fired flag.

## 6. Missing Disclosures

Against the `01` value-add multifamily baseline and the `02` equity fee inventory:

1. **Target return.** Gross and net IRR, equity multiple, projected cash-on-cash. This is the most material gap: §2 runs on norms, not the deal.
2. **Hold period.** Needed to size the illiquidity hurdle and to confirm how much slack the debt maturity actually gives.
3. **Debt terms beyond rate type and maturity.** LTV, amortization/IO period, and **prepayment terms**. Fixed-rate debt sold two years before maturity usually carries yield maintenance or defeasance, or depends on buyer assumption; that exit cost belongs in the pro forma.
4. **Catch-up rate** (feeds the promote drag and `EQUITY-03`).
5. **Fee bases.** Acquisition fee on equity or on price; asset management fee on equity raised or invested capital.
6. **Admin / IR / K-1 fees, loan-placement fee, and any construction-management fee** (common in value-add).
7. **Affiliate service providers** (property management, construction management).
8. **Distribution schedule / J-curve.**
9. **Track-record detail.** Are the five exits multifamily, and what are their realized IRRs and multiples versus underwriting? `01` specifically asks for the GP's record on *prior multifamily exits*.
10. **Sponsor identity, geography/submarket, minimum, raise size.**

Nothing on this list blocks underwriting the core return story. They are next-round diligence items.

## 7. GP Alignment

- **Co-invest:** strong. 10% of equity in cash, pari-passu 🟢. Before the verdict hardens, confirm it's real cash and not a fee waiver or deferred-fee rollover (Q-GP-01).
- **Track record:** realized, net-to-LP, five exits 🟢 stated. It is **unverified** until the per-deal figures are in hand and reconcile to the PPM and distribution records (🔴 until checked). Five is a modest sample, so check the dispersion across the five, not just the average.
- **Waterfall alignment:** among the most LP-protective structures `02` describes. Whole-of-fund (European) with a *secured* clawback means the GP earns nothing until LPs have all capital back plus a compounding 8%. In a single-asset deal this mainly means no interim promote on operating cash flow or partial capital events (🟡 inferred; confirm in the PPM).
- **Affiliate fees:** not disclosed either way. Probe with Q-FEE-02.

## 8. Questions for the GP

**Must-ask**

| ID | Question | Bad-answer signal | `03` ref |
|---|---|---|---|
| Q-DS-01 | What share of projected LP IRR comes from in-place cash flow versus the exit? What's the IRR at a flat exit cap? | Can't or won't decompose the IRR; "real estate always appreciates." | GEN-08, EQUITY-06 |
| Q-DS-02 | Strip out leverage — what is the unlevered, in-place return (and the LTV)? | Treats the levered IRR as the only figure; "leverage is just how the deal works." | GEN-07 |
| Q-DS-03 | Does the provided downside case stress flat rents, an exit cap *above* going-in, and a longer hold? | The "downside" is still a comfortable gain; only one variable stressed. | GEN-13 |
| Q-FEE-01 | Full fee schedule and waterfall, including catch-up rate, fee bases, admin/IR, loan placement, construction management? | "Standard market fees"; "the PPM has it" without producing it. | GEN-16 |
| Q-FEE-02 | Which providers are GP-affiliated, what do they charge, and is it benchmarked? | "All arm's-length" without naming providers. | GEN-06 |
| Q-FEE-03 | Confirm whole-of-fund mechanics for this single-asset deal and how the clawback is secured (escrow/guarantee). | Can't explain the clawback security; "you get paid when we get paid." | EQUITY-01, EQUITY-02 |
| Q-FEE-04 | Confirm the pref is cumulative *and* compounding in the operating agreement. | Marketing says compounding, the PPM says simple. | EQUITY-04, EQUITY-05 |
| Q-RISK-01 | Debt matures 2 yrs after planned exit — what is the plan if the hold extends? What's the prepayment penalty or yield maintenance at the planned sale date, and is the loan assumable? | "We'll refinance" with no terms; prepayment cost not modeled. | GEN-09 |
| Q-RISK-03 | Complete debt terms (LTV, IO period, amortization, prepayment). | Terms withheld until commitment. | GEN-12, GEN-15 |
| Q-EXIT-02 | Confirm no part of capital return depends on a refinance. | A mid-hold cash-out refi is quietly in the plan. | EQUITY-07 |
| Q-GP-01 | Is the 10% co-invest cash at close, pari-passu, with no fee offset? | Co-invest funded by fee waiver or acquisition-fee rollover. | GEN-01 |
| Q-GP-02 | Share the five exits deal by deal: asset type, realized net-to-LP IRR and multiple versus underwritten. | Only an average; project-level IRR substituted; the exits aren't multifamily. | GEN-05, GEN-14 |
| Q-GP-03 | Any regulatory action or investor litigation? | "Nothing material" without a direct yes/no. | GEN-02 |
| Q-MKT-01 | What submarket supply and absorption data support the rent-growth and renovation-premium assumptions? | Metro-level optimism; no supply pipeline acknowledged. | GEN-18 |
| Q-DIST-01 | Projected distribution schedule — when do distributions start, and what gates them? | "When the deal supports it"; no milestones. | GEN-11 |
| Q-LIQ-01 | What are my options if I need to exit before the hold ends? | "A secondary market may develop." (An honest "none" is a good answer.) | — |

**Nice-to-ask**

| ID | Question | Bad-answer signal | `03` ref |
|---|---|---|---|
| Q-GP-04 | How has the team scaled alongside AUM? | AUM multiplied while the team stayed flat. | GEN-04 |
| Q-DIST-02 | Any capital calls expected, and what's the penalty for a missed call? | Punitive dilution buried in the docs. | — |
| Q-LIQ-02 | K-1 delivery timing and history? | A history of extensions. | — |

## 9. Diligence Checklist

- [ ] PPM and operating agreement: waterfall language (whole-of-fund, compounding pref, catch-up), clawback security, the full fee schedule and fee bases.
- [ ] Track record: per-deal realized net-to-LP IRRs reconciled to distribution records or K-1s, and confirmation that the exits are multifamily.
- [ ] Background and regulatory checks on principals: SEC/FINRA/state records, litigation search.
- [ ] Rent and sale comps supporting the renovation premium and the going-in cap (T-12 and rent roll already provided — tie them to the pro forma).
- [ ] Appraisal or BOV versus purchase price.
- [ ] Lender term sheet or loan docs: LTV, IO, amortization, prepayment/yield maintenance, assumability, extension options.
- [ ] Downside model: rerun it with an exit cap 50–100 bps above going-in and a hold extended to the debt maturity.
- [ ] Confirm the co-invest is funded in cash at close.

## 10. Verdict

**Pursue.**

- **Why:** the disclosed structure answers almost every question this screen asks about how LP capital is protected. The GP has cash at risk on LP terms. Promote is deferred until LPs are whole plus a compounding 8%, and a secured clawback backs it. Fees are in-market with no aggressive line. The return story rests on operations, with no cap compression underwritten. The debt can't force a sale or refi inside the plan. The track record is realized and net-to-LP. The underwriting package (T-12, rent roll, downside) is complete. Not one RED or YELLOW flag fires on a stated fact.
- **Biggest swing factor:** the **target return versus fee drag**. At about 4% of annual gross-to-net drag, the property must earn about 12% gross or better for the LP's net to clear the 7-yr illiquidity hurdle over VNQ (bear case: 8.37% net, thin). The GP's pro forma has to show a gross IRR that lands net in the `01` 12–15% realized band.
- **What would have to be true:** the target net IRR clears roughly 400–600 bps over VNQ for the actual hold, and a hold slip still fits inside the 2-yr debt buffer. The five exits hold up deal by deal. No undisclosed affiliate or ancillary fees materially widen the drag. A bad answer on the target return, the prepayment cost or the track-record detail would move this to Pursue with conditions or Pass.
- **Who it suits:** an LP comfortable with a single-asset, 5–7-yr illiquid position (🟡 inferred hold) who wants value-add multifamily exposure with institutional-grade LP protections, and doesn't need liquidity before exit.
