# Eval fixture 11 — J-curve pair, Deal B (all-at-exit) + A/B comparison
*Iteration-3 run, 2026-07-04, blind generation by fresh-context agent, against SKILL.md (post S1b/S2b fixes).*

**Verdict: Pass as presented — insufficient disclosure, and structurally inferior to Deal A at the identical 14% headline: 100% of the return arrives at a Year-5 sale (GEN-08 at its maximum), so the LP carries full capital at full risk for five years against a single terminal event. Equal IRRs are not equal deals — the comparison below is the point.**

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Multifamily (sub-strategy not stated) 🟡 |
| Deal type | Equity (syndication vs fund not stated) 🟡 |
| Sponsor | Not stated |
| Geography | Not stated |
| Minimum investment | Not stated |
| Hold | 5 years (sale in Year 5) 🟢 |
| Raise | Not stated |
| Claimed return | 14% projected IRR — gross or net not stated 🔴 |
| Distributions | **None until the Year-5 sale; entire return realized at exit** 🟢 |

## 2. Return Stress-Test

Swing assumptions: **the exit price (cap rate) — effectively the only assumption that matters**, plus whatever rent growth and debt structure (undisclosed) feed it.

- **Base.** 14% inside the `01` value-add band — but here the IRR is a single number resting on a single future transaction. Zero distributions for five years means the *entire* claim is the Year-5 sale price 🟢.
- **Bear.** With no interim cash, the downside has no floor from banked distributions: if the Year-5 exit market is soft (cap decompression, frozen transactions — the 2022–24 pattern), the LP's options are sell weak or extend with no income; a 100–150bps exit-cap miss can take a back-loaded 14% into single digits or principal loss, whereas a front-loaded deal has already returned cash. The deal also implies negative or fully-retained operating cash flow for five years — where does operating cash go? (Debt service? Reinvestment? Undisclosed.) 🟡
- **Benchmark (`05`, benchmark_comparator, 5-yr):** 14% vs VNQ 6.47% = ≈753bps over a ~300–400bps hurdle → clears *arithmetically* 🔴 — but an all-at-exit private position is strictly more exposed than the comparator on timing risk: VNQ pays continuous distributions and can be sold any day, while this position pays nothing and cannot be exited. The illiquidity premium demanded here should sit at the top of the band or above (per `05`, concentration and timing amplify the required premium).

## 3. Where LP Returns Come From

**100% from terminal value — GEN-08 fires at its maximum (100% > the 60% threshold).** This is disclosed, not hidden — GEN-11's *disclosure* demand is technically met — but what the disclosure reveals is the maximum-risk timing profile: five years of full capital exposure to one sale, with the exit cap (undisclosed → EQUITY-06 unresolved), leverage (undisclosed → GEN-07 unresolved), and the 2031 transaction market all sitting between the LP and the first dollar back.

## 4. Fee Stack Summary (`02`)

**Nothing disclosed — GEN-16.** Same as Deal A: expect the full `02` equity inventory; whether 14% is gross or net swings the outcome by ≈450bps/yr (`02` worked example). One structure-specific addition: in a back-loaded deal, watch whether the pref *accrues* (cumulative, compounding) across the five distribution-free years — a non-cumulative pref in this shape is worth almost nothing (EQUITY-05 probe). **Drag not computable — that is the finding.**

## 5. Red Flags (`03`)

**RED**
- **GEN-08** — exit-dependent IRR at 100%: the return is entirely a future-sale bet; no operating income reaches the LP at any point.

**YELLOW / YELLOW–RED**
- **GEN-16** (YELLOW–RED) — no fee or waterfall disclosure.
- **GEN-15** (YELLOW–RED) — no financials, debt terms, or exit-cap disclosure (EQUITY-06 unresolved: the assumption carrying 100% of the return is not shown; GEN-07 unresolved on leverage).
- **GEN-17** — `01` essentials absent (§6).
- **GEN-13** — no downside case, on the shape most punished by a downside.
- **GEN-11 (mechanism note)** — timing disclosed, so the flag's disclosure demand is met; the *risk* it screens for is present at maximum and is scored via GEN-08 above.

## 6. Missing Disclosures (`01` multifamily essentials)

- Exit cap assumption and sensitivity — carries the entire return here; its absence is the single loudest omission
- Rent roll, T-12; where operating cash flow goes for five years
- Debt structure, maturity vs the 5-year plan, rate profile
- Fee schedule and waterfall; pref mechanics (cumulative/compounding — decisive in this shape)
- Sponsor identity and realized net-to-LP track record
- Raise, minimum, gross-vs-net basis of the 14%

## 7. GP Alignment

Unassessable 🔴 (sponsor unnamed, co-invest unstated — GEN-01 unresolved; track record absent — GEN-05/GEN-14 unresolved). Structure note: in an all-at-exit deal the GP's promote and the LP's outcome both hang on the same sale — superficially aligned, but if the GP collects fees through five distribution-free years, the GP is paid to wait while the LP is not (fee schedule undisclosed; Q-FEE-01).

## 8. Questions for the GP (`04`)

**Must-ask**
1. **Q-DS-01** (GEN-08, EQUITY-06) — the IRR at a flat exit cap, since 100% of return is the exit. *Bad answer:* collapses at flat cap; "real estate always appreciates."
2. **Q-EXIT-01** (EQUITY-06) — the exit cap vs going-in. *Bad answer:* compression assumed with no defense.
3. Where does five years of operating cash flow go? (Debt service? Capex? GP fees?) *Bad answer:* it's consumed by debt service — i.e., the asset can't afford distributions (routes to Q-DS-02 / GEN-07).
4. **Q-DS-02** (GEN-07) — unlevered, in-place return. *Bad answer:* no unlevered view.
5. **Q-FEE-04** (EQUITY-04, EQUITY-05) — pref rate; cumulative and compounding across the no-distribution years? *Bad answer:* non-cumulative or simple-only in a back-loaded deal.
6. **Q-FEE-01** (GEN-16) — full fee schedule and waterfall; fees taken during the distribution-free years. *Bad answer:* "standard fees."
7. **Q-RISK-01** (GEN-09) — debt maturity vs the Year-5 sale; what if 2031 is a bad year to sell? *Bad answer:* no extension plan.
8. **Q-DS-03** (GEN-13) — bear case at a higher exit cap. *Bad answer:* none exists.
9. **Q-RISK-03** (GEN-15) — T-12, rent roll, debt terms. *Bad answer:* withheld.
10. **Q-GP-02** (GEN-05, GEN-14) + **Q-GP-01** (GEN-01) — realized record; co-invest. *Bad answers:* marks-only; sweat equity.
11. **Q-LIQ-01** — five years, zero cash: what if the LP needs out in Year 3? *Bad answer:* vague secondary promises.

## 9. Diligence Checklist

Same base list as Deal A (PPM, T-12/rent roll, debt documents, sponsor verification), plus:
- Exit-cap sensitivity table — demand it in writing; it *is* this deal
- Pref accrual mechanics in the LPA (cumulative/compounding through Year 5)
- Debt maturity/extension tests vs a delayed sale

---

## Comparison — Deal A vs Deal B (compare-two-deals mode)

**Identical 14% headline IRRs; nowhere near identical deals.** This pair is the textbook GEN-11 lesson: IRR is timing-blind, and the LP is not.

| Axis | Deal A | Deal B |
|---|---|---|
| Distribution timing | 7% CoC quarterly from Year 1 + progressive capital return | Nothing until Year-5 sale |
| Exit dependence | Minority of return at exit — GEN-08 not fired | **100% at exit — GEN-08 RED** |
| Capital at risk over time | Declines steadily as capital returns | Full principal exposed all five years |
| Bear-case behavior | IRR erodes; cash already banked | Return can vaporize on one bad exit window |
| Sequence/reinvestment | LP redeploys cash along the way | LP compounds nothing for five years |
| Verification burden | Is the 7% CoC real operating cash? | Is the exit cap defensible? (heavier: one assumption carries everything) |

At equal headline IRR, **Deal A dominates on risk timing** — to be *equivalent*, Deal B would need a materially higher projected return as compensation for concentrating all risk in a single terminal event (per `05`, the demanded premium scales with what the position makes the LP bear). Both deals fail disclosure identically today (no fees, sponsor, debt, or financials — the re-screen lists mirror), so neither is investable as presented; but if both return with equally clean full packages at the same net 14%, **advance Deal A and price Deal B down — or demand Deal B pay visibly more.**

## 10. Verdict

**Pass as presented — insufficient disclosure**, with the structural finding on top: even fully disclosed, this shape carries GEN-08 at 100% — a five-year, zero-distribution bet on one exit assumption that the materials don't even state. Biggest swing factor: the Year-5 exit cap. **Re-screen list:** exit-cap assumption with sensitivity; T-12/rent roll and the five-year cash-flow story; debt terms and maturity vs the sale; full fee stack and pref accrual mechanics; sponsor's realized net-to-LP record. Relative verdict: at the same 14%, Deal A is the better-shaped claim on the same headline — Deal B must out-pay it to deserve the allocation, and as presented it doesn't try.
