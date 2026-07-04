# Eval fixture 11 — J-curve pair, Deal B (bullet at exit) + A-vs-B comparison
*Iteration-2 run, 2026-07-04, blind generation by fresh-context agent, against SKILL.md (post S1–S3 fixes).*

*Compare-two-deals mode: Deal B screened below; the pairwise contrast with Deal A (fixture 10) is in the Comparison section, per the pair instruction.*

**Verdict: Pass as presented — insufficient disclosure — and structurally inferior to Deal A at the identical 14% headline: zero distributions until a Year-5 sale makes the return 100% exit-dependent (`GEN-08`, RED), a single-date bet on the exit market. Equal IRRs are not equal returns.**

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Multifamily (subtype **not stated**) 🟡 |
| Deal type | Equity (syndication presumed 🟡 — structure not stated) |
| Sponsor | **Not stated** |
| Geography | **Not stated** |
| Minimum investment | **Not stated** |
| Hold | 5 years (sale in Year 5) 🟢 |
| Raise | **Not stated** |
| Claimed return | 14% IRR — gross or net **not stated** 🔴 |
| Distributions | **None until the Year-5 sale; entire return realized at exit** 🟢 |
| Fees / waterfall / debt | **Not stated** |

Routing: `01` multifamily; `02` equity syndication; `03` `GEN-`, `EQUITY-`; `05` VNQ + NCREIF unlevered overlay.

## 2. Return Stress-Test

Swing assumptions: **(a) the exit cap / terminal value** — the *only* source of return, so every point of exit-cap movement passes straight through to the LP's entire outcome; **(b) the Year-5 transaction market** — the deal must sell (or refi) in one specific window; **(c) the undisclosed debt** — five years of zero distributions implies either negative/reinvested cash flow or a structure that accrues to exit; either way the leverage terms carry the deal to Year 5 or don't.

- **Base:** 14% as claimed, all at exit — a 5-year zero-coupon position; ~1.9x implied multiple if 14% is IRR-true 🟡.
- **Bull:** strong Year-5 market → 14%+ arrives in one payment.
- **Bear:** the defining fragility — a soft exit market in the *one year that matters* doesn't dent the return, it *is* the return. A one-point exit-cap widening or a frozen transaction market converts 14% into low single digits or an extended hold with the LP having received **nothing** along the way; realized IRR is quasi-binary 🟡. No sensitivity is provided (`GEN-13`).
- **Benchmark (`05`):** same arithmetic as Deal A (14% net vs VNQ 6.47% ≈ +750bps; ~10% net-of-assumed-fees ≈ +350bps vs a ~300–400bps 5yr hurdle) — but the *quality* of the premium is worse: `05`'s concentration amplifier says a premium must be discounted for idiosyncratic risk, and here the idiosyncratic risk is concentrated further onto a single future date. The illiquidity is also strictly worse than A's: five years with zero interim cash is the maximal lock-up for the stated hold 🟡.

## 3. Where LP Returns Come From

**100% from exit — disclosed outright.** This is far past the `GEN-08` >60% threshold: the return is a terminal-value bet, not income (RED; skepticism rule 3). Whether leverage amplification also sits inside it (`GEN-07`) is unknowable without the debt terms → `Q-DS-02`. Credit where due: the deal *discloses* its back-loading rather than hiding it — `GEN-11` (timing not disclosed) does not fire; the timing is disclosed and is the problem (`GEN-11`'s mechanism — identical IRRs, different risk timing — cited as the analytical frame, not as a fired flag).

## 4. Fee Stack Summary

**Nothing disclosed.** Same `02` inventory gap as Deal A: **gross-to-net drag not computable — that is the finding (`GEN-16`).** One B-specific note: in a back-loaded deal the waterfall crystallizes entirely at the Year-5 event — pref accrual (cumulative? compounding?) across five distribution-free years, catch-up mechanics, and any clawback all bind at once at exit; the LP's protection lives or dies on those undisclosed terms → `Q-FEE-03`, `Q-FEE-04`.

## 5. Red Flags

**RED**
- `GEN-08` — >60% (here 100%) of the return from terminal value: the entire LP outcome rides on the Year-5 exit cap and transaction market → `Q-DS-01` (cluster candidate with `EQUITY-06`/`GEN-07` — both probes pending disclosure of the exit cap and debt).

**YELLOW–RED**
- `GEN-16` — no fee or waterfall disclosure; in a bullet structure the waterfall terms are worth more than in A, and they're absent → `Q-FEE-01`.
- `GEN-15` — no rent roll, T-12, or debt terms — with zero interim distributions the LP can't even watch cash flow as a monitoring signal; the financials are the only window and they're not offered → `Q-RISK-03`.

**YELLOW**
- `EQUITY-06` (probe) — exit-cap assumption undisclosed; in a 100%-exit deal this is *the* number → `Q-EXIT-01` (escalated to must-ask: its flag family already fired via `GEN-08`).
- `GEN-07` (probe) — leverage share of the terminal value unknown → `Q-DS-02`.
- `GEN-13` — no downside case → `Q-DS-03`.
- `GEN-17` — `01` essentials absent (see §6).
- Five years of accrued (undisclosed-mechanics) pref with no cash — pref structure risk scored under `EQUITY-05` (probe): simple-only or non-cumulative accrual would quietly strip the LP's time-value protection exactly where it matters most → `Q-FEE-04`.

## 6. Missing Disclosures

Against the `01` multifamily baseline (`GEN-17`): rent roll, T-12, exit cap with sensitivity, debt structure and maturity (does the loan even reach Year 5?), refi assumptions, GP realized-exit track record — all absent. Plus: fee schedule and waterfall (`GEN-16`), pref mechanics across the distribution-free years, sponsor identity, co-invest, raise, minimum, market. B-specific: what happens if the Year-5 sale doesn't clear — extension terms, forced-sale provisions, and who decides.

## 7. GP Alignment

**Unassessable** — sponsor, co-invest, track record, waterfall, affiliates all undisclosed (→ `Q-GP-01`, `Q-GP-02`, `Q-FEE-02`). Structure-level note: a bullet deal aligns GP and LP *timing* (everyone waits for exit) but concentrates the GP's promote incentive on maximizing the single exit print — including stretching the hold or exit-cap assumptions — while the LP bears five years of uncompensated interim risk. Clawback and pref-accrual terms are the alignment safeguards here, and none are disclosed.

## 8. Questions for the GP

**Must-ask**
1. `Q-DS-01` — Confirm the return decomposition (stated: 100% exit) and the IRR at a flat exit cap. *Bad answer:* the IRR collapses below the pref at a flat cap; "real estate always appreciates."
2. `Q-EXIT-01` — Exit cap vs going-in, and the sensitivity table. *Bad answer:* exit cap below going-in with "cap rates will compress." *(Escalated: `GEN-08` fired.)*
3. `Q-DS-03` — Bear case: flat rents, higher exit cap, no refi, Year-5 market shut. *Bad answer:* single-point pro forma; no extension plan.
4. `Q-RISK-01` — Debt maturity vs the Year-5 exit; extension options if the sale slips. *Bad answer:* maturity at or inside Year 5 with no extensions — the forced-seller scenario.
5. `Q-FEE-04` — Pref rate, and is it cumulative and **compounding** across the five distribution-free years? *Bad answer:* simple-only or non-cumulative accrual (`EQUITY-05` confirmed).
6. `Q-FEE-03` — Waterfall structure and clawback at the single crystallization event. *Bad answer:* "you get paid when we get paid."
7. `Q-FEE-01` — Complete fee schedule. *Bad answer:* "standard market fees."
8. `Q-RISK-03` — T-12, rent roll, debt terms. *Bad answer:* withheld until commitment.
9. `Q-GP-02` — Realized net-to-LP track record, specifically deals that *exited on schedule*. *Bad answer:* marks; extended holds recharacterized as wins.
10. `Q-LIQ-01` — Exit options during five distribution-free years. *Bad answer:* "a secondary market may develop." *(Sharper here than in A: an LP in B has no cash flow to soften an emergency.)*
11. `Q-DS-02` — Unlevered, in-place return. *Bad answer:* only the levered exit story exists.

**Nice-to-ask:** `Q-GP-01`, `Q-GP-03`, `Q-MKT-01`, `Q-DIST-02`, `Q-LIQ-02`.

## 9. Diligence Checklist

- PPM/LPA: waterfall, pref accrual mechanics, clawback, extension/forced-sale provisions.
- Debt documents: maturity vs Year 5, extension tests, sweep triggers.
- Exit-cap sensitivity model; third-party submarket cap-rate evidence.
- T-12/rent roll; sponsor background and realized-exit verification (on-schedule exits specifically).
- Model the LP outcome at Year 6/7 extended holds — the realistic bear case.

## 10. Verdict — and the A-vs-B comparison

**Deal B standalone: Pass as presented — insufficient disclosure**, with `GEN-08` already fired RED on the disclosed structure. Biggest swing factor: the Year-5 exit cap — it isn't the largest input, it is effectively the *only* input.

### Comparison: Deal A vs Deal B — same 14%, opposite risk timing

| Dimension | Deal A (fixture 10) | Deal B |
|---|---|---|
| Headline IRR | 14% | 14% — identical |
| Cash to LP, Years 1–4 | ~7%/yr quarterly + progressive capital return | **Zero** |
| Exit dependence | ~half the return 🟡 (below the 60% line) | **100%** — `GEN-08` RED |
| Bear-case shape | Degrades gracefully — coupon and returned capital already banked | Quasi-binary — one soft exit window impairs the entire return |
| Capital at risk over time | Declining through the hold | 100% for 5 years |
| Effective illiquidity | Softened by quarterly cash | Maximal — no interim cash, no exit (`Q-LIQ-01`) |
| Reinvestment/optionality | Quarterly cash redeployable; self-monitoring signal | None; and no cash-flow signal to monitor |
| What must be true to hit 14% | In-place NOI covers the coupon; ordinary exit | An exit at the assumed cap, in one specific year |

**The SKILL's compare-mode principle applied: equal headline IRRs are not equal when one back-loads to exit.** A dollar of IRR earned as Year-1 cash and a dollar promised at a Year-5 sale carry different risk, and B's version is strictly riskier: same expected return, greater variance, all of it concentrated on one date. For B to be the rational choice it would need a *premium* over A — visibly better basis, lower leverage, or a higher net IRR — and it offers none; it offers the same 14% with more ways to miss.

**Pairwise verdict: prefer Deal A.** Neither deal is commitable on current disclosure (both: `GEN-15`/`GEN-16`; re-screen lists in each file), but if both re-screen clean at the same terms, A dominates B for any LP who values realized cash over promised cash — which, from the LP's recovery perspective, should be every LP. **Who B suits:** only an LP with zero liquidity needs, explicit conviction in the Year-5 exit market, and a demanded return premium over A that this deal, as presented, does not pay.
