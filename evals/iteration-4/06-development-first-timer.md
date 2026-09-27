# Eval fixture 06 — Ground-up development, first-time sponsor
*Iteration-4 run, 2026-09-27, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 1c7faff.*

**Verdict: Pass.** Every return in this deal comes from the exit (GEN-08), and the exit assumes cap-rate compression (EQUITY-06), so it's a leverage-and-exit bet, not an operating one (GEN-07). The sponsor has never built from the ground up and has no realized development exits (GEN-14). There is no downside case (GEN-13). The fees stack a development fee and a construction-management fee on the same work (GEN-06). Filling the disclosure gaps would not fix the main problem, which is a sponsor with no development history. **Biggest swing factor: the exit cap. It sets the headline return, and this sponsor has never proven it can deliver it.**

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Development (ground-up). Product type (multifamily, industrial, etc.) not stated 🟢 |
| Deal type | Development (equity) 🟡 inferred. No pref-equity or debt position described |
| Sponsor | Not stated. Disclosed only as "first ground-up project" 🟢 |
| Geography / submarket | Not stated |
| Minimum investment | Not stated |
| Hold | 3 years 🟢. That is the **short end** of the `01` development norm of 3–5 years, and it has to cover entitlement/permit, construction, lease-up, and sale |
| Total raise / project cost / capital stack | Not stated |
| Claimed return | 25% IRR / 2.5x equity multiple 🟢. **Gross or net-to-LP not stated.** That is above the `01` development *target* of 18–22% net, and `01` notes realized returns "often below" that target |
| Downside / sensitivity case | None shown 🟢 |
| Exit cap | Underwritten below the going-in basis 🟢. Numbers not stated |
| Fees disclosed | 5% development fee; 4% construction management 🟢. Fee basis (total project cost vs hard costs vs equity) not stated |
| Pref / promote / waterfall | Not stated |
| Debt (construction loan, takeout) | Not stated |
| Entitlement / permit status | Not stated |
| GP co-invest | Not stated |

## 2. Return Stress-Test

**Swing assumptions:** (1) the **exit cap**, (2) **construction cost and schedule**: overruns, and lease-up delays that push the hold past 3 years, and (3) **construction-loan takeout / rate path**. Rent levels at lease-up are a fourth, but they can't be tested because the product and submarket aren't disclosed.

**A 2.5x in 3 years implies a very large development margin or very high leverage** 🟡 (illustrative arithmetic, 🔴 assumed capital stacks):
- At 65% loan-to-cost, 2.5x on equity needs exit value ≈ **1.5× total project cost**, a ~50% margin on cost.
- At 75% loan-to-cost, it needs ≈ **1.28× cost**, a ~28% margin. That's more plausible, but only because more debt is doing the work.

In both cases the multiple depends on leverage and on the exit price. Neither is something the sponsor has shown it can deliver.

| Case | Assumptions (🔴 illustrative, 75% LTC, construction interest ignored) | Approx. outcome (gross, before fees and promote) |
|---|---|---|
| **Bull / sponsor pro forma** | On budget, on schedule, exit at the underwritten (compressed) cap | 25% IRR / 2.5x as claimed |
| **Base (realistic)** | Exit cap +50bps over underwritten (≈ −9% value), on budget, 3-yr exit | Equity proceeds ≈ 1.6x → **~18% gross IRR** |
| **Bear** | Exit cap +50bps, 10% hard-cost overrun funded by LP capital call, 12-month lease-up delay (4-yr hold) | ≈ 1.3x over 4 yrs → **~6% gross IRR**. Exit cap +100bps puts the LP at **roughly 1.0x (return of capital, or a loss after fees)** |

Development returns are the most sensitive in private real estate to small changes in assumptions. The asset produces no income during construction, so any slip goes straight to the equity at the exit.

**Versus the public comparator** (`05`: VNQ 4.92% 10yr; `scripts/benchmark_comparator.py`, `development`, 3-yr lock-up → illiquidity hurdle ~300–400bps):

| Net-to-LP IRR tested | Premium over VNQ | Read |
|---|---|---|
| 25.0% (if the headline is already net) | ≈2008bps | Clears easily on paper |
| 18.7% (headline treated as gross, typical equity stack assumed; §4 Scenario C) | ≈1374bps | Clears |
| 6.0% (bear case above, before fees) | ≈108bps | **Thin / fails.** Only ~80bps over the 10yr Treasury (5.18%) |

The spread only clears if the sponsor's own pro forma turns out right. `05` flags development as having the "largest *target* premium **and** widest dispersion — discount heavily for realized-below-target." For a first-time ground-up sponsor, the headline should be discounted more than usual. A bear case that returns ~1x over four years pays nothing for the lock-up, and the LP could have held Treasuries for that period with no risk.

## 3. Where LP Returns Come From

- **Cash flow: ~0%** 🟡. Ground-up construction produces no in-place income. Across a 3-year hold, most of the time goes to construction and lease-up.
- **Exit: ~100%** 🟡. The whole 2.5x arrives at sale. That is well past the >60% exit-dependence threshold → **GEN-08 (RED)**.
- **Leverage and cap compression.** The underwriting assumes an exit cap below the going-in basis → **EQUITY-06 (RED)**. The multiple only works at high loan-to-cost (§2). The `05` unlevered overlay puts institutional private real estate at **~5.0% total return, almost all income, with appreciation near zero** (NCREIF NPI, trailing four quarters to Q2 2026). About 20 of the 25 claimed points therefore depend on leverage, development margin, and an assumed lower exit cap, none of which this sponsor has delivered before → **GEN-07 (RED)**.

**Cluster:** GEN-07 + GEN-08 + EQUITY-06 all fire. Per `03`, when two or three fire together the deal should be called a **financing story**, and this one is.

*Development nuance:* some spread between a development's yield-on-cost and its exit cap is the legitimate development thesis (you build at a higher yield than the market pays for stabilized assets). EQUITY-06 is flagged here because the deal describes the exit cap as below the *going-in basis*. That wording suggests the underwriting also assumes the market cap rate itself compresses between now and exit. That is a second bet stacked on the development spread. Q-EXIT-01 separates the two.

## 4. Fee Stack Summary

| Fee (`02` development variations) | Disclosed | `02` norm | Read |
|---|---|---|---|
| Development fee | 5% (basis not stated) 🟢 | 3–5% of total project cost, one-time; aggressive >6% **or split across both a development fee and construction management fee** | Top of range, and **stacked** with CM |
| Construction management | 4% (basis not stated) 🟢 | 3–5% of hard costs; aggressive >6% | In range alone, but charged on top of the development fee |
| Combined development + CM | ~9% headline 🟢 | `02` names this exact split as the aggressive pattern | **Aggressive per `02`.** Possibly both paid to GP affiliates (GEN-06) |
| Construction contingency | Not stated | 5–10% of hard costs | Can't tell if under-reserved (<5%) or padded (>15%, which inflates the fee base) |
| Acquisition / land fee | Not stated | 1–2% of equity | Unknown |
| Asset management | Not stated | 1–2% of equity, annual | Unknown |
| Loan placement (construction + takeout) | Not stated | 0.5–1.5% of loan per event | Likely two financing events. Unknown |
| Disposition | Not stated | 0.5–1% of sale price | Unknown |
| Pref / promote / catch-up / waterfall | Not stated | 15–30% over 6–10% pref | **Unknown. The largest line in the gross-to-net drag** |
| Admin / IR | Not stated | 0.1–0.5% of equity | Unknown |

**Gross-to-net drag: can't be computed from what's disclosed. That is the finding (GEN-16).** `scripts/fee_drag_calculator.py` runs (gross 25%, 3-yr hold):

| Scenario | Inputs | Drag | Net LP IRR |
|---|---|---|---|
| A: disclosed fees only, assumed inside the project budget | All undisclosed fees = 0 | **0bps/yr** (floor; almost certainly understated) | 25.0% |
| B: development + CM charged on top, converted to equity basis 🔴 | 5% of cost + 4% × hard costs (assumed ~70% of cost), at 60% LTC ≈ 19.5% of equity one-time; others 0 | **≈650bps/yr** | 18.5% |
| C: development + CM inside budget, typical equity stack for the undisclosed fees 🔴 | 20% promote / 8% pref / 100% catch-up, 1.5% AM, 1% disposition, 0.3% admin | **≈634bps/yr** (420 promote, 180 recurring, 33 one-time) | 18.7% |

Development and CM fees are usually paid from the project budget, so they are often already inside a project-level IRR. That makes the key question **whether the 25% is project-level, before the fees, or net to LP**. If it's project-level and the undisclosed promote looks like Scenario C, the LP nets ~18.7%, below the headline and within the `01` target range. The short 3-year hold makes one-time fees heavier: `02` notes a one-time fee spread over 3 years costs roughly three times as much per year as over 10. **Every input in Scenarios B and C is ASSUMED, so each is a §6 gap.**

## 5. Red Flags

**RED**
- **GEN-08. Exit-dependent IRR.** ~100% of return comes from the exit; there is no in-place income during construction. **LP exposure:** the whole 2.5x rides on one sale at an assumed price and date. → Q-DS-01
- **EQUITY-06. Exit cap below going-in basis.** Cap compression is built into the headline. **LP exposure:** +50bps on exit cap costs ~9% of value, which is ~36% of equity at 75% LTC. → Q-EXIT-01
- **GEN-07. Financing story.** About 20 of 25 points depend on leverage, development margin, and compression, against a ~5% unlevered income-driven baseline (`05` NPI). **LP exposure:** the return breaks if rates or the exit cap move. → Q-DS-02
  - *Cluster: GEN-07 + GEN-08 + EQUITY-06 = financing story.*
- **GEN-14. No realized development track record.** This is the sponsor's first ground-up project, so there are no realized development exits to check. `01`: "development experience is not fungible with acquisition experience." **LP exposure:** the LP pays for the sponsor to learn how to handle entitlements, GCs, cost overruns, and lease-up. (GEN-05 can't be assessed: we don't know if their prior track record, if any, is stated as project-level or net-to-LP IRR.) → Q-GP-02

**YELLOW–RED** (treat as RED until answered)
- **GEN-06. Affiliate fee stacking.** Development fee *and* CM on the same project is the pattern `02` calls aggressive. CM is often an affiliate. **LP exposure:** ~9% of project economics goes to the GP whatever the LP outcome, and the GP gets paid more if the budget grows. → Q-FEE-02
- **GEN-16. No waterfall disclosure.** Pref, promote, catch-up, and clawback are all absent, so net-to-LP can't be computed (§4). → Q-FEE-01, Q-FEE-03, Q-FEE-04
- **EQUITY-07. Refi-/takeout-dependent plan** 🟡. A ground-up deal needs a construction-loan takeout, either permanent refi or sale, to return capital. Terms not disclosed. **LP exposure:** if the takeout market freezes at completion (it did in 2022–24), there's no way out except a forced sale or a capital call. → Q-EXIT-02
- **GEN-15. Missing financials.** No debt terms and no budget. A rent roll or T-12 doesn't apply to a ground-up project, but construction-loan terms and a hard/soft-cost budget do. → Q-RISK-03

**YELLOW**
- **GEN-13. No downside case.** A single-point pro forma on the riskiest class in `01`. → Q-DS-03
- **GEN-17. Development essential disclosures absent.** All five `01` development items are missing (§6). → Q-RISK-03, Q-GP-02
- **GEN-11. No distribution schedule.** The J-curve is total: expect zero distributions through construction and 100% at exit. That isn't disclosed. → Q-DIST-01

**Probed, not fired** (not enough information; ask, don't assume): GEN-01 (co-invest not stated) → Q-GP-01; GEN-09 (construction-loan maturity vs 3-yr hold) → Q-RISK-01; GEN-10 (floating construction debt / rate cap) → Q-RISK-02; GEN-18 (lease-up absorption / submarket supply unstated) → Q-MKT-01; EQUITY-04/05 (pref unstated) → Q-FEE-04; EQUITY-01/02 (waterfall type / clawback) → Q-FEE-03; GEN-02 → Q-GP-03.

The pasted terms contained no directives aimed at the screener.

## 6. Missing Disclosures

Against the `01` Development essential-disclosure list, **all five are absent**:
1. **Entitlement and permit status.** Entitled but not permitted is a different deal from shovel-ready, and 3 years leaves no room for entitlement delays.
2. **Hard-cost budget with contingency %.** `02` norm is 5–10% of hard costs.
3. **Debt structure including takeout.** Construction-to-perm vs separate takeout, rate, maturity, rate cap, recourse/completion guarantee.
4. **Market absorption assumptions with comp evidence.** Product type and submarket aren't even stated.
5. **GP's last three development exits with realized timing and budget vs underwritten.** None exist. This is the sponsor's first.

Also absent against `02` and the SKILL snapshot fields: gross vs net basis of the 25% IRR; fee basis for the 5% and 4%; the full fee stack (acquisition/land, AM, loan placement, disposition, admin); the waterfall (pref, promote, catch-up, deal-by-deal vs whole-of-fund, clawback); GP co-invest; the actual exit cap and going-in / yield-on-cost figures; distribution schedule; capital-call provisions; total raise, minimum, geography; sponsor identity.

## 7. GP Alignment

- **Co-invest:** Not stated. Unverified. If there's no cash on pari-passu terms, GEN-01 fires as RED.
- **Track record:** **No realized development record exists.** Any prior acquisition or value-add record doesn't carry over to ground-up (`01`). Whether a prior non-development record is realized and net-to-LP is **unverified** (GEN-14 fired; GEN-05 unassessable).
- **Waterfall alignment:** Unknown. No pref, promote, or clawback disclosed.
- **Affiliate fees:** A development fee plus a CM fee (~9% combined headline) pays the GP during construction, before any LP return. Both are typically calculated on cost, so **the GP earns more if the budget grows**, which works against the LP in a cost overrun. It's unverified who performs CM or whether their rates are benchmarked (GEN-06).
- **Net read:** Fees pay the GP whatever happens. The LP's return depends on an exit this sponsor has never executed. On the disclosed facts, alignment is weak.

## 8. Questions for the GP

**Must-ask**

| ID | Question | Bad-answer signal | Flag |
|---|---|---|---|
| Q-GP-02 | "Restate your track record as net-to-LP IRR on fully-realized, exited deals only, and separately, what ground-up development have you or your principals completed?" | Offers only project-level or GP-level IRR; "most deals still performing"; presents acquisition experience as development experience | GEN-14, GEN-05 |
| Q-DS-01 | "What share of projected LP IRR comes from in-place cash flow vs the exit, and what's the IRR at a flat exit cap?" | Can't decompose the IRR; "real estate always appreciates"; IRR collapses below the pref at a flat exit cap | GEN-08, EQUITY-06 |
| Q-EXIT-01 | "Why is the exit cap below the going-in basis, and what's the IRR at an exit cap equal to or above going-in?" | "Cap rates will compress"; the IRR breaks at a flat cap; no sensitivity. *Also: can't separate the yield-on-cost spread from assumed market compression* | EQUITY-06 |
| Q-DS-02 | "Strip out leverage and cap-rate compression. What is the unlevered return?" | Levered IRR treated as the only figure; "leverage is just how the deal works" | GEN-07 |
| Q-DS-03 | "What is the return under a bear case: cost overrun, lease-up delay, higher exit cap, no refinance?" | Single-point pro forma; "we underwrite conservatively" with nothing to show; the bear case is still a gain | GEN-13 |
| Q-FEE-01 | "Provide the complete fee schedule and the full distribution waterfall. Is the 25% gross or net to LP?" | "Standard market fees"; "the PPM has it" without producing it | GEN-16 |
| Q-FEE-02 | "Which service providers are GP-affiliated, including the CM, what do they charge, and are those rates benchmarked? Why both a development fee and a CM fee?" | "All arm's-length" without naming providers; no benchmark; no answer on the double fee | GEN-06 |
| Q-FEE-03 | "Is the waterfall deal-by-deal or whole-of-fund, and is there a clawback?" | Can't explain the catch-up; "you get paid when we get paid" | EQUITY-01, EQUITY-02 |
| Q-FEE-04 | "What preferred return do LPs receive before promote, and is it cumulative and compounding?" | Pref <6% or absent; non-cumulative | EQUITY-04, EQUITY-05 |
| Q-EXIT-02 | "Does the plan depend on a construction-loan takeout or refinance, and what happens to LP capital if it isn't available on the assumed terms?" | Capital return requires a refi at lower rates; no fallback; "the refi market will reopen" | EQUITY-07 |
| Q-RISK-01 | "When does the construction loan mature relative to the projected 3-year hold, and what are the extension options?" | Maturity inside the hold; "we'll refinance" with no terms | GEN-09 |
| Q-RISK-02 | "Is the construction debt floating? When does the rate cap expire, and what does it cost to extend?" | Cap expires before maturity; extension cost not modeled; "rates should be lower by then" | GEN-10 |
| Q-RISK-03 | "Provide the full hard/soft-cost budget with contingency %, entitlement/permit status, and complete debt terms." | Budget withheld; "confidential until you commit"; contingency <5% | GEN-15, GEN-17 |
| Q-GP-01 | "How much of your own capital is in this deal, on the same terms as LPs?" | "Our sweat equity is our investment"; co-invest is a fee waiver, not cash | GEN-01 |
| Q-GP-03 | "Have you or your principals faced any regulatory action, enforcement, or investor litigation?" | "Nothing material"; a search turns up something undisclosed | GEN-02 |
| Q-DIST-01 | "What is the projected distribution schedule, and at what milestones does LP capital start returning?" | "We'll distribute when the deal supports it"; no milestones | GEN-11 |
| Q-MKT-01 | "What submarket supply pipeline and absorption data support the lease-up and rent assumptions?" | Metro-level optimism instead of submarket data; no supply pipeline acknowledged | GEN-18 |
| Q-LIQ-01 | "What are my options if I need to exit before the hold ends?" | "A secondary market may develop"; vague accommodation promises | — |

**Nice-to-ask, escalated to must-ask**
- **Q-DIST-02**: "When are capital calls expected, and what's the consequence of a missed or late call?" *Escalated:* the bear case depends on an LP-funded cost-overrun call, and a first-time developer makes that more likely. **Bad answer:** "calls as needed" with no notice period; punitive dilution buried in the docs.

**Nice-to-ask**
- **Q-GP-04**: team headcount and development-monitoring capacity. **Bad answer:** no named construction or development lead; "we're lean and efficient."
- **Q-LIQ-02**: K-1 delivery timing. **Bad answer:** "as soon as we can"; a history of extensions.

## 9. Diligence Checklist

- **PPM / operating agreement:** confirm the fee basis for the 5% and 4%, the full waterfall, clawback, capital-call and dilution mechanics, and removal-for-cause rights.
- **Background / regulatory:** SEC, FINRA, and state searches on the sponsor and principals; litigation search; check whether the principals have *any* prior role on a ground-up project (as an employee of another developer, for example).
- **Entitlement verification:** confirm zoning, site plan approval, and permit status with the municipality independently.
- **Third-party cost review:** an independent construction consultant's review of the hard-cost budget, GC contract type (GMP vs cost-plus), contingency %, and GC bonding.
- **Lender:** construction-loan term sheet, including maturity, extensions, rate/cap, recourse, and completion guarantee (who is guaranteeing, and can they actually cover it?).
- **Market comps:** independent rent and sale comps and submarket supply pipeline for the exit, plus current market cap rates for stabilized comparables vs the underwritten exit cap.
- **Appraisal:** as-complete / as-stabilized appraisal vs pro forma exit value.

## 10. Verdict

**Pass.**

**Reasoning.** This is a **merits Pass**, not an insufficient-disclosure Pass. What's disclosed is enough to see how the deal makes its money, and that is the problem:
1. **It's a financing story (GEN-07 + GEN-08 + EQUITY-06).** 100% of the return arrives at exit, at an exit cap below the going-in basis, on a multiple that only works with high leverage or a ~30–50% development margin.
2. **Nobody has checked the one skill the deal depends on (GEN-14).** Development is the highest-risk class in `01`. Realized returns there "often" land below target even for experienced developers, and this sponsor has no realized development exits.
3. **No downside case (GEN-13).** In a realistic bear case (§2: +50bps exit cap, 10% overrun, 12-month delay), the LP is at ~6% gross over 4 years before fees, or ~1.0x with +100bps on the exit cap. Neither pays for the lock-up against VNQ plus a ~300–400bps hurdle, or even against the 5.18% 10yr Treasury.
4. **The GP gets paid regardless (GEN-06).** A development fee plus CM (~9%) pays the GP during construction and grows with the budget.

The five missing essential disclosures (§6) make this worse but aren't the reason for the verdict. Even full disclosure can't give this sponsor a development track record.

**Biggest swing factor:** the exit cap, together with whether a first-time developer can finish on budget and on schedule so the exit happens in year 3 and not year 4 or 5.

**Who it would suit.** Only an LP who is sizing this as a small, fully-expendable position; who can meet an overrun capital call; who can tolerate zero distributions for the full hold and possibly longer; and who has a specific reason to back this sponsor's move into development.

**What would have to be true to re-screen.**
- A principal, co-GP, or JV partner with **three or more realized ground-up exits**, with budget and timing vs underwritten documented, and an actual economic role in this project (not just an advisory title).
- An exit cap **at or above** current market cap for stabilized comparables, with the IRR still clearing roughly the `01` development range at that cap.
- A real downside case where LP capital survives an overrun, a delay, and a +50–100bps exit cap.
- The 25% confirmed as net to LP, or a full waterfall that lets the net be calculated.
- One of the development or CM fees dropped or credited against the other, and fee basis capped (not tied to budget growth).
- Meaningful GP cash co-invest on pari-passu terms.
- Entitled and permitted site; contingency ≥5% of hard costs; construction-loan maturity and extensions covering the hold with room to spare; takeout not dependent on lower rates.
