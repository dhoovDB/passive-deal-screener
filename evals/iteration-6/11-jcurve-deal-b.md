# Eval fixture 11
*Iteration-6 run, 2026-11-01, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 436a76b.*

**Verdict: both deals, Pass as presented — insufficient disclosure. The 14% IRRs match, but the deals don't: Deal B is 100% exit-dependent (`GEN-08`, RED), while Deal A pays cash along the way but hasn't shown where its return of capital comes from. If both resubmit, screen Deal A first.**

*Screening output only, not investment advice.*

Confidence tags: 🟢 stated or from a reference, 🟡 inferred, 🔴 assumed or unverifiable.

---

## 1. Deal Snapshot

| Field | Deal A | Deal B |
|---|---|---|
| Asset class | Multifamily 🟢; subtype not stated. 14% fits value-add, not core (8–12%) 🟡 | Same 🟢 / 🟡 |
| Deal type | Equity syndication 🟡 (inferred) | Equity syndication 🟡 (inferred) |
| Claimed return | 14% projected IRR; gross or net not stated 🟢 | Same 🟢 |
| Distributions | 7% cash-on-cash, quarterly, from Year 1 🟢 | None until sale 🟢 |
| Capital return | "Progressively over the hold"; no schedule or source 🟢 | All at exit 🟢 |
| Hold | Not stated | 5 years 🟢 |
| Sponsor, geography, minimum, raise | Not stated | Not stated |
| Fees, waterfall, debt, exit cap | Not stated | Not stated |

## 2. Return Stress-Test

**Against the public hurdle (`05`, `benchmark_comparator.py`).** The comparator is VNQ at 4.92% over 10 years. The illiquidity hurdle is about 300–400 bps for a 5-year lock-up and about 400–600 bps for 7 years. Deal A's hold is unstated, so it needs both.

| If the 14% is... | LP net IRR | Premium over VNQ | Read |
|---|---|---|---|
| Already net to LP | 14.00% | 908 bps | Clears comfortably at 5 or 7 years |
| Gross, 5-year hold, `02` worked-example fee stack 🔴 | 9.32% | 440 bps | Clears at 5 years, but only 414 bps over the 10-year Treasury (5.18%) |
| Gross, 7-year hold (Deal A only), same stack 🔴 | 9.71% | 479 bps | Clears thinly |

- **Gross or net is the first unknown.** The comparison is only valid net to LP, so the GP has to state the net figure. 14% is the bottom of the value-add target range (14–18%) and inside the realized range (12–15%) 🟢. If it is gross, a norm-level fee stack puts the net below that realized range 🔴.
- **Both trail SPY.** SPY returned 15.39% over the same 10 years 🟢. Neither deal pays more than the liquid equity anchor even at face value, so each owes a diversification or downside rationale. That decade was exceptional and isn't a forward promise.
- **Single-asset risk.** Clearing the hurdle is necessary, not sufficient. A single asset carries concentration risk that VNQ diversifies away, and private-RE dispersion is wide (`05`).

**Base / bull / bear.** Neither deal gives a leverage figure, exit cap or capital-return schedule, so this stresses exit equity proceeds directly instead of inventing property-level inputs. The grid assumes a 5-year hold for both deals and treats the 14% as LP-level. Deal A's two columns bracket its unstated shape 🔴:

- **A-slow:** 7% a year on original capital, nothing else until exit.
- **A-fast:** 7% a year plus 10% of capital returned each year.

Each A column solves for the exit proceeds that produce 14%. All figures below are illustrative 🔴.

| Measure | Deal B | A-slow | A-fast |
|---|---|---|---|
| Bull: exit equity +25% | 19.2% IRR | 18.5% | 17.1% |
| **Base: as projected** | **14.0%** | **14.0%** | **14.0%** |
| Bear: exit equity −25% | 7.6% | 8.6% | 10.5% |
| Bear premium over VNQ | 271 bps, below hurdle | 364 bps, thin | 557 bps, clears |
| Severe: exit equity −50% | −0.8% (loses capital) | 1.6% | 6.3% |
| Exit miss that drops IRR below the 5-year hurdle (7.9–8.9%) | 20–24% | 24–28% | 35–41% |
| Exit miss that drops IRR below the 10-year Treasury | 33% | 38% | 56% |
| Exit miss that loses capital | 48% | 55% | 80% |

**The swing assumptions:**
1. **Exit cap** is the largest swing in most pro formas (`01`), and it hits Deal B on every dollar. Neither deal states one, so `EQUITY-06` can't be tested.
2. **Rent growth** drives exit NOI, and through it exit value, for both deals (`GEN-18`). Deal A also needs it to sustain the 7%.
3. **Refi** is the swing specific to Deal A. If "progressive" capital return means a refinance, a frozen refi market pushes A-fast's capital back to exit and takes the 14% with it (`EQUITY-07`). Deal B states no refi, but its debt maturity is unknown, and a loan maturing before Year 5 forces one anyway (`GEN-09`, `GEN-10`).

These are equity misses. Leverage makes an exit-price miss a larger equity miss, and neither deal gives the debt terms needed to convert one to the other.

## 3. Where LP Returns Come From

| Source | Deal A | Deal B |
|---|---|---|
| Cash before exit | 7% a year stated 🟢; about 25% (A-slow) to 61% (A-fast) of present value 🔴 | 0% 🟢 |
| Exit | **39–75% of present value, depending on the unstated shape** 🔴 | **100%** 🟢 |
| Equity multiple at plan | 1.59x–1.79x 🔴 | 1.93x (1.14^5, if the 5-year bullet holds) 🟡 |
| Cash back by end of Year 3 | 21–51% of capital 🔴 | 0% 🟢 |

**Deal B fires `GEN-08` on its own stated terms.** "The entire return is realized at exit" is well past the >60% line. No part of the 14% is earned until a sale closes in Year 5, at whatever cap rate and credit market exist that year.

**Deal A can't be cleared on `GEN-08` yet.** Its exit share straddles the 60% line depending on a schedule it hasn't given, so this stays a must-ask rather than a fired flag (`Q-DS-01`). A 7% yield supplies roughly half of a 14% IRR. The rest has to come from a capital event, and "progressively" doesn't say which:
- **Refi or partial sale:** the exit share falls, but the deal becomes refi-dependent (`EQUITY-07`).
- **Part of the 7% relabeled as return of capital:** nothing extra comes back early, and Deal A looks like A-slow, over the 60% line at 75% (`GEN-08`).
- **Reserves or investor capital funding Year 1 payments:** the yield isn't earned yet.

**The Year 1 start needs its own check, because 7% is high against the baseline.** The `01` cash-on-cash norm of 5–8% applies *after stabilization* 🟢. Unlevered institutional income is about 4.8% (NPI 2025) and the 10-year Treasury is 5.18% 🟢, so debt likely costs at least that and leverage is unlikely to lift the cash yield 🟡. A 7% payment from Year 1 therefore needs an unusually high going-in yield or a non-operating source. Deal A has to show which.

**Deal B's zero needs an explanation too.** A multifamily asset normally produces cash. Five years of no distributions means operating cash is going elsewhere: renovation, debt service, reserves, or thin coverage 🟡. The deal doesn't say which, and each answer tells you something different about the risk.

**Leverage overlay, both deals (`05`).** Unlevered private RE returned about 5.0%, nearly all income, with appreciation near zero 🟢. That leaves about 9 points of the 14% coming from leverage and assumed appreciation rather than in-place operations 🟡. This doesn't fire `GEN-07` as a fact because leverage and cap terms aren't disclosed, but the burden is on both GPs to show otherwise (`Q-DS-02`).

## 4. Fee Stack Summary

**Gross-to-net drag: not computable for either deal, and that is the finding (`GEN-16`).** Neither deal discloses a single fee, a pref, or a promote.

- **On disclosure alone:** `fee_drag_calculator.py` with `0` for every undisclosed fee returns 0 bps. That reflects missing data, not a free deal.
- **Illustrative, all inputs assumed 🔴:** the `02` worked-example stack on a 14% gross, 5-year hold gives **about 468 bps** (9.32% net). That is 180 recurring, 60 one-time and 228 promote, using 2% acquisition, 1.5% asset management, 1% disposition, 0.3% admin, and a 20% promote over an 8% pref with 100% catch-up. A low-end stack gives about 272 bps (11.28% net). At 7 years (Deal A only), the worked-example stack gives about 429 bps.
- **Model limit:** the calculator's promote assumes a single bullet at exit. That matches Deal B and only approximates Deal A.

**The same fee terms would treat these deals differently:**
- **Who gets paid first:** if asset-management fees are paid currently, Deal B's GP collects for five years while LPs receive nothing 🟡. Ask how those fees are funded.
- **Pref terms matter far more in Deal B.** Five years of pref accrue unpaid. Non-cumulative means it is lost outright. At an illustrative 8% 🔴, simple accrues 40% against 46.9% compounding. A 100% catch-up can then hand that protection's value to the GP at a single exit (`EQUITY-03`, `EQUITY-04`, `EQUITY-05`).

## 5. Red Flags

**Fired on stated facts or absences**

| ID | Severity | Deal | Mechanism and LP exposure |
|---|---|---|---|
| `GEN-08` | RED | **B** 🟢 | All return comes from terminal value. One sale in one year decides the whole outcome, with no cash banked if it slips. |
| `GEN-16` | YELLOW–RED, treat as RED until answered | A, B 🟢 | No fee or waterfall disclosure. Undisclosed fees still get paid, and net return can't be calculated. |
| `GEN-15` | YELLOW–RED, treat as RED until answered | A, B 🟢 | No rent roll, T-12 or debt terms, so neither return can be underwritten. |
| `GEN-11` | YELLOW | A, B 🟢 | **A:** cadence given, but no capital-return milestones or source. **B:** timing is stated, so nothing is hidden, but the mechanism applies in full: back-loading concentrates all return risk at exit. |
| `GEN-13` | YELLOW | A, B 🟡 | One IRR figure with no sensitivity or downside shown. |
| `GEN-17` | YELLOW | A, B 🟢 | Multifamily essentials are absent (§6). |

**Cluster note.** For each deal, the YELLOW and YELLOW–RED disclosure flags together act as a RED. In Deal B, `GEN-08` is one leg of the financing-story family (`GEN-07` + `GEN-08` + `EQUITY-06`). The other two legs are untested, so I'm not calling it a financing story yet.

**Open: raised by this analysis, not fired, because they would need assumed facts**

| ID | Severity if confirmed | Why it's open | Sharper for |
|---|---|---|---|
| `GEN-07` | RED | About 9 points above the unlevered baseline; leverage unknown | Both |
| `EQUITY-06` | RED | Exit cap not stated | B (all return rides on it) |
| `EQUITY-07` | YELLOW–RED | "Progressively" may mean a refi | A |
| `GEN-08` (Deal A) | RED | 39–75% of present value, depending on the shape | A |
| `GEN-09` / `GEN-10` | RED | Debt maturity, rate type and any cap not stated | Both; B has no earlier cash if one bites |
| `GEN-18` | YELLOW | Rent growth assumption not stated | Both |
| `GEN-12` | YELLOW–RED | No financials of any window provided (covered by `GEN-15`) | Both |
| `GEN-01`, `GEN-02`, `GEN-05`, `GEN-14` | RED | Sponsor unnamed; no co-invest or track record given | Both |
| `GEN-06` | YELLOW–RED | Affiliates not disclosed | Both |
| `EQUITY-01`–`EQUITY-05` | RED to YELLOW | Waterfall and pref not disclosed. Single-asset, so the deal-by-deal risk in `EQUITY-01`/`EQUITY-02` is limited unless these sit in a fund. | B on `EQUITY-03`–`EQUITY-05` (§4) |

## 6. Missing Disclosures

**Missing from both (per `01` and `02`):**
- Net-to-LP IRR and equity multiple
- Multifamily subtype and business plan
- Rent roll and T-12 actuals
- Pro forma exit cap with sensitivity
- Debt structure: amount, rate type, maturity, any rate cap, prepayment
- Refi assumptions
- GP track record on **prior multifamily exits**
- Full fee schedule: acquisition, asset management, disposition, loan placement, refinance, construction management, admin
- Waterfall: pref rate, cumulative or not, compounding or simple, catch-up, splits, clawback
- Affiliate providers
- GP co-invest
- Sponsor identity, geography, minimum, raise size
- Liquidity and transfer terms

**Specific to Deal A:** hold period, capital-return schedule and its source, whether the 7% is on original or remaining capital, and what portion of the 7% is earned versus returned capital.

**Specific to Deal B:** where operating cash goes for five years, how fees are funded in the meantime, how shortfalls are funded with no distribution buffer (reserves or capital calls), and whether Year 5 is a target or a commitment, including extension rights.

## 7. GP Alignment

Unverified for both deals: nothing is disclosed.

| Item | Status |
|---|---|
| Co-invest (cash, pari-passu?) | Not stated (`GEN-01` open) |
| Realized net-to-LP track record | None given. Unverified, not weak (`GEN-05`, `GEN-14` open). |
| Waterfall alignment | Not stated |
| Affiliate fees | Not stated (`GEN-06` open) |

**One structural difference.** Current distributions make Deal A's GP report and pay against operating results every quarter, which gives LPs an early read on underperformance. Deal B gives LPs no cash signal until the sale, so reporting quality and promote terms carry more of the alignment burden 🟡.

## 8. Questions for the GP

**Must-ask: the questions that separate these two deals**

| ID | Ask of | Question | Bad-answer signal |
|---|---|---|---|
| `Q-DIST-01` (`GEN-11`) | A: what funds the capital return, on what schedule? B: why no distributions, and what gates them? | "What is the projected distribution schedule, and at what milestones does LP capital start returning?" | "We'll distribute when the deal supports it"; no milestones. |
| `Q-DS-01` (`GEN-08`, `EQUITY-06`) | Both | "What share of projected LP IRR comes from in-place cash flow versus the exit, and what's the IRR at a flat exit cap?" | Can't decompose it; "real estate always appreciates"; IRR falls below pref at a flat cap. |
| `Q-EXIT-02` (`EQUITY-07`) | A first | "Does the business plan depend on a refinance, and what happens to distributions if the refi isn't available on the assumed terms?" | Capital return requires a refi at lower rates; no fallback; "the refi market will reopen." |
| `Q-EXIT-01` (`EQUITY-06`) | B first | "Why is the exit cap below the going-in cap, and what's the IRR at an exit cap equal to or above going-in?" (Ask for the exit cap first.) | "Cap rates will compress"; IRR breaks at flat; no sensitivity. |
| `Q-FEE-04` (`EQUITY-04`, `EQUITY-05`) | B first | "What preferred return do LPs receive before the GP earns promote, and is it cumulative and compounding?" | Pref below 6% or absent; non-cumulative. |
| `Q-LIQ-01` | B first | "What are my options if I need to exit before the hold period ends?" | "A secondary market may develop"; "we'll try to accommodate." |

**Must-ask: both deals equally**

| ID | Question | Bad-answer signal |
|---|---|---|
| `Q-DS-02` (`GEN-07`) | "Strip out leverage and cap-rate compression. What is the unlevered, in-place return?" | "Leverage is just how the deal works"; no unlevered view exists. |
| `Q-DS-03` (`GEN-13`) | "What is the return under a bear case: flat rents, higher exit cap, no refinance?" | "We underwrite conservatively" with nothing to show; the bear case is still a gain. |
| `Q-FEE-01` (`GEN-16`) | "Can you provide the complete fee schedule and the full distribution waterfall?" | "Standard market fees"; "the PPM has it" without producing it. |
| `Q-FEE-02` (`GEN-06`) | "Which service providers are GP-affiliated, what do they charge, and are those rates third-party-benchmarked?" | "All arm's-length" without naming providers. |
| `Q-FEE-03` (`EQUITY-01`, `EQUITY-02`, `EQUITY-03`) | "Is the waterfall deal-by-deal or whole-of-fund, and is there a clawback?" Also ask the catch-up rate. | Can't explain the catch-up; "you get paid when we get paid." |
| `Q-RISK-01` (`GEN-09`) | "When does the debt mature relative to the projected hold, and what's the refinance or extension plan?" | Maturity inside the hold; "we'll refinance" with no terms. |
| `Q-RISK-02` (`GEN-10`), if floating | "When does the rate cap expire relative to debt maturity, and what's the cost to extend it at current pricing?" | Cap expires before maturity; "rates should be lower by then." |
| `Q-RISK-03` (`GEN-12`, `GEN-15`) | "Can you provide trailing-twelve-month actuals, the rent roll, and complete debt terms?" | T-3 or T-6 only; "the financials are confidential until you commit." |
| `Q-GP-01` (`GEN-01`) | "How much of your own capital is in this deal, on the same terms as LPs?" | "Our sweat equity is our investment"; co-invest is a fee waiver. |
| `Q-GP-02` (`GEN-05`, `GEN-14`) | "Can you restate your track record as net-to-LP IRR on fully-realized, exited deals only?" | Only project-level or GP-level IRR; "most deals are still performing." |
| `Q-GP-03` (`GEN-02`) | "Have you or your principals faced any regulatory action, enforcement, or investor litigation?" | "Nothing material"; a search surfaces something undisclosed. |
| `Q-MKT-01` (`GEN-18`) | "What submarket supply pipeline and absorption data support the rent-growth assumption?" | Metro-level optimism in place of submarket data; no supply pipeline acknowledged. |

**Nice-to-ask**

| ID | Question | Bad-answer signal |
|---|---|---|
| `Q-DIST-02` (no flag; matters more in B, which has no cash buffer) | "When are capital calls expected, and what's the consequence of a missed or late call?" | "Calls as needed"; punitive dilution buried in the docs. |
| `Q-LIQ-02` | "When will K-1s be delivered each year, and have you historically delivered them before the filing deadline?" | "As soon as we can"; a history of extensions. |
| `Q-GP-04` (`GEN-04`) | "How have your headcount and deal-monitoring capacity grown alongside AUM?" | "We're lean and efficient" as the whole answer. |

## 9. Diligence Checklist

For both deals, all still to verify:
- **PPM and operating agreement:** check fees, waterfall, pref terms and transfer limits against the marketing.
- **Background and regulatory:** search SEC, FINRA, state records and litigation on the GP and principals.
- **Financials:** review the rent roll and T-12 against bank statements or audited figures where available.
- **Comps and market:** check sale comps for the exit cap, and rent comps plus submarket supply for rent growth.
- **Appraisal:** get an independent value for the going-in basis.
- **Lender:** review loan documents for maturity, extensions, covenants and any rate cap.
- **Track record:** tie claimed exits to LP statements or K-1s.

**Deal A:** tie Year 1 distributions to projected NOI less debt service, and check the documents on how distributions are classified (income or return of capital).

**Deal B:** obtain the 5-year cash flow showing where operating cash goes, and read the extension and sale-timing provisions.

## 10. Verdict

**Deal A: Pass as presented — insufficient disclosure.**
**Deal B: Pass as presented — insufficient disclosure, with `GEN-08` (RED) already fired on its stated terms.**

*Screening output only, not investment advice.*

**Reasoning.** Each deal is one sentence: asset class, an IRR and a distribution shape. Sponsor, net return, fees, debt, exit cap and financials are all missing, so the core return story can't be underwritten for either. These are passes on what is missing, not on the merits. Deal B's flag doesn't kill it, but it must be resolved before committing.

**Biggest swing factor.**
- **Deal B:** exit equity at Year 5. A miss of about 20–24% takes it below the illiquidity hurdle, and about 48% loses capital 🔴.
- **Deal A:** the source of its capital return. That decides whether it behaves like A-fast or looks close to Deal B with a coupon.

**Who each could suit, if it clears diligence.**
- **Deal A:** an LP who needs income or wants less riding on one exit, and accepts a lower multiple and the job of reinvesting distributions.
- **Deal B:** an LP who needs no cash for five years, can absorb a delayed or weak exit, and wants the higher multiple without reinvestment drag.

**What would have to be true to re-screen.**

Both deals:
1. Net-to-LP IRR and multiple are stated, and clear VNQ plus the lock-up hurdle and the Treasury floor.
2. A complete fee schedule and waterfall are provided, so drag can be calculated.
3. Rent roll, T-12 and full debt terms are provided, with debt maturing at or after the planned exit and any rate cap covering it.
4. The exit cap is at or above going-in, or the compression is specifically justified, and the IRR at a flat cap and in a bear case is shown.
5. There is a meaningful pari-passu cash co-invest and a realized net-to-LP track record on multifamily exits.

Deal A also needs:

6. A hold period and capital-return schedule, with the 7% shown to be funded by operations from Year 1 and capital return not dependent on a refi.

Deal B also needs:

7. A credible reason for five years of no distributions, a cumulative pref (ideally compounding), and an IRR at a flat exit cap that still clears the hurdle.

## Contrast: same IRR, different deals

| | Deal A | Deal B |
|---|---|---|
| Exit dependence | 39–75% 🔴, unresolved | 100% 🟢, `GEN-08` |
| J-curve | Cash from Year 1 | Flat to Year 5, then one payment |
| Capital at risk over time | Declines if capital really returns | Fully at risk until sale |
| If exit equity falls 50% | Stays positive (1.6–6.3% IRR) 🔴 | Loses capital (−0.8%) 🔴 |
| Multiple at plan | 1.59x–1.79x 🔴 | 1.93x 🟡 |
| Year 5 wealth, reinvesting distributions at 5.18% | 1.71x–1.84x 🔴 | 1.93x 🔴 |
| Main open question | Where does capital return come from? | Why is there no cash, and what is the exit cap? |

**IRR hides the trade.** It treats early cash as if it were reinvested at 14%. Deal A's distributions probably won't earn that, so if both deals hit plan, Deal B leaves you with more money at Year 5. That is the real case for Deal B.

**The crossover is about an 18–19% exit equity miss** 🔴. Assume both deals miss their exit by the same percentage and Deal A's cash earns the 10-year Treasury rate. Above that miss, Deal A leaves you wealthier at Year 5. Below it, Deal B does. Deal A is the better structure only if you believe a miss of that size is a real possibility, and for a single levered asset with an undisclosed exit cap, it has to be treated as one.

**Deal A's advantage is conditional.** It rests entirely on those distributions being earned from operations. If they turn out to be reserves or relabeled capital, the gap between the deals narrows sharply, and Deal A then has the lower multiple without the safety that justified it.
