# Eval fixture 04
*Iteration-7 run, 2026-11-01, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 181fdd7.*

# Passive Deal Screen: Phoenix Fix-and-Flip Bridge Fund

**Verdict: Pass as presented (insufficient disclosure).** What the GP has given you is three claims, none of them checkable. Re-screen when the items in the list at the end are disclosed.

*Screening output only, not investment advice.*

Biggest swing factor: the **as-is LTV** behind the "70% LTV". It decides whether the LP has a real equity cushion. If the 70% is measured on after-repair value (ARV), the loans can sit at or above current value (HML-01).

---

## 1. Deal Snapshot

| Field | Value | Confidence |
|---|---|---|
| Asset class | Hard Money / Bridge Loan | 🟢 stated ("bridge fund", "we lend on fix-and-flip") |
| Deal type | Hard money / bridge debt fund (pooled, senior-secured short-duration loans) | 🟢 "fund" stated; 🟡 senior-secured position inferred from the category, not stated |
| Sponsor | Not stated (no name, entity, or principals) | 🟢 |
| Geography | Phoenix metro, one market | 🟢 |
| Loan strategy | Fix-and-flip only, one strategy | 🟢 |
| Leverage | "70% LTV", basis not stated (ARV or as-is?) | 🟢 figure stated; basis unknown |
| Minimum investment | Not stated | 🟢 |
| Hold / fund term / lock-up / redemption terms | Not stated | 🟢 |
| Raise / fund size / AUM | Not stated | 🟢 |
| Claimed return | "Target 11% net". No IRR-vs-yield definition, no distribution schedule, no gross figure | 🟢 stated; 🔴 unverified |
| Fees / waterfall | Not stated | 🟢 |
| Track record | "Experienced team, we've never had a loss". No figures, no time period, no loan count | 🟢 stated; 🔴 unverifiable |

The `01` category baseline (Hard Money / Bridge Loan) is: 6–18 months per loan, 3–5 year fund commitment, **8–10% net to LP** (11–13% gross is common), senior secured, 65–75% LTV typical **on ARV**, risk tier Low-Med.

---

## 2. Return Stress-Test

**Headline vs category.** 🟢 The 11% net target sits **100 bps above the top of the category's 8–10% net range** (`01`). It also equals the *bottom* of the 11–13% *gross* range. There are four possible explanations, and the deal tells you nothing that separates them:
1. The fund charges unusually low fees. Plausible but not disclosed.
2. The loans are riskier: higher LTV on as-is value, weaker borrowers, or longer or troubled loans. This links to HML-01.
3. Fund-level leverage (a credit line on the loan book) is lifting LP yield. That is the CREDIT-01 mechanism; see §5.
4. "Net" is really a gross or loan-coupon figure. This links to GEN-16.

**Illustration of what 11% net implies** (`scripts/fee_drag_calculator.py`, 3-year hold ASSUMED). Every fee input here is 🔴 ASSUMED, so these runs illustrate the problem and do not support a finding:
- 13% gross (top of the common band), a 2% fund management fee, no carry → **11.00% net** (200 bps drag). To deliver 11% net, the loan book has to earn at the top of the gross band every year with zero credit losses, *and* the fund can carry no performance fee.
- 13% gross, a 1.5% management fee, 0.5% servicing, and 20% carry over an 8% hurdle (all within `02` ranges) → **9.93% net** (307 bps drag). An ordinary in-range fee stack on a top-of-band gross yield lands *inside* the 8–10% category baseline, not at 11%.

**Scenarios** (`scripts/benchmark_comparator.py`, deal type `hard-money`, comparator HYG 4.83% 10yr, 3-month T-bill 4.24%, 2-year Treasury 4.87%; the hold is not stated, so the 3-year lock-up is 🔴 ASSUMED from the `01` fund-commitment range):

| Case | Swing assumptions | Net to LP | Premium over HYG | Over 3mo / 2yr Treasury | vs illiquidity hurdle (3–5 yr: ~300–400 bps) |
|---|---|---|---|---|---|
| Bull | Target delivered: gross at top of band, low fees, no material defaults | 11.0% (🔴 GP's own target) | ≈617 bps | ≈676 / ≈613 bps | Clears comfortably |
| Base | Category realized norm: in-range fee stack, normal defaults with full recovery | ≈9.5% (mid of `01` 8–10%) | ≈467 bps | ≈526 / ≈463 bps | Clears comfortably |
| Bear | Category floor: higher fees or carry, some loans default and recovery comes in below par | 8.0% (bottom of `01` range) | ≈317 bps | ≈376 / ≈313 bps | **Clears, thin**, in the lower half of the hurdle band |
| Tail (not modeled) | Phoenix resale prices fall while loans are mid-renovation. If the 70% is on ARV, as-is LTV can be 100%+, so foreclosed collateral covers less than the loan | **Principal loss**, size unknowable without as-is LTV, default history, and recovery rate | n/a | n/a | Fails |

The three swing assumptions:
1. **As-is LTV**, which sets loss severity when a flip stalls (HML-01).
2. **Default × recovery rate** through a downturn (HML-03, HML-04).
3. **Fee load**, which sets the gross-to-net gap (GEN-16).

A fourth swing is **capital deployment**: cash waiting between short loans earns T-bill yield, not 11%.

**Read.** At the stated target the fund clears HYG plus the illiquidity premium. That result is necessary, not sufficient. 🟢 It also rests entirely on an unverified target. The bear case still clears, but thinly. The real downside for a fix-and-flip book is the tail row, a loss of principal, which no yield comparison captures. Because all 11% comes from loan interest and fees, the return is income-driven, so the equity-style exit test does not apply (§3). The risk sits in collateral coverage.

---

## 3. Where LP Returns Come From

- **Cash flow (loan interest + borrower points):** 🟡 roughly all of the return. In a debt fund the LP is paid from coupons and origination points, not from an exit valuation. Rules 3 and 4 of the skepticism contract (exit-dependent IRR, financing story: GEN-08, GEN-07) **do not fire**: there is no exit cap or terminal value.
- **Leverage:** unknown. The deal does not say whether the fund borrows against its loan book. If it does, part of the 11% is fund leverage, which amplifies losses the same way it amplifies yield. That is the CREDIT-01 mechanism (§5, probe via Q-RISK-06). 🔴 Unstated.
- **The hidden exit dependence:** each borrower's repayment depends on *selling the flipped house at ARV* (or refinancing out). The LP's principal is therefore exposed to Phoenix resale pricing loan by loan, even though the LP's yield is not. 🟡 Inferred from the fix-and-flip strategy (`01`: "senior secured short-duration debt … typically for fix-and-flip … borrowers").

---

## 4. Fee Stack Summary

| Fee (`02`, hard money / bridge) | Typical | Aggressive | This deal |
|---|---|---|---|
| Origination points (borrower-paid) | 1–3 pts | <1 or >5 pts | Not stated. Also not stated whether the points go to the fund or to the GP |
| Fund management fee | 1–2% of AUM, annual | >2.5% | Not stated |
| Servicing fee | 0.25–0.5% of loan balance, annual | >1% | Not stated |
| Performance fee / carry | 10–20% above 5–8% hurdle | >25%, or no hurdle | Not stated |
| Late fees / default interest | *Variable*. Should go to the fund | Siphoned into a GP "workout fee" | Not stated |
| Wind-down / liquidation fee | 0.5–1% of remaining AUM | >2% | Not stated |
| Admin / IR / K-1 | 0.1–0.5% or a fixed $/LP | >$5k/LP | Not stated |

**Gross-to-net drag: not computable from what was disclosed.** Running `scripts/fee_drag_calculator.py` with every undisclosed fee passed as `0` returns **0 bps of drag**. That figure is not a result. It shows that nothing was disclosed (🟢). Every fee input is a §6 gap. An illustrative in-range stack (§2) produces **≈200–307 bps/yr** of drag (🔴 ASSUMED). At that level, an 11% *net* would need a gross yield at or above the top of the 11–13% band.

Undisclosed fees still get paid (GEN-16). One point is specific to bridge funds: borrower-paid points and default interest either raise fund yield or flow to the GP. Which way they go can move LP net by more than the management fee does.

---

## 5. Red Flags

No embedded directives in the pasted text. All three sentences are marketing claims, and they are treated as data.

**RED / YELLOW–RED (treated as RED until answered)**

- **HML-01: LTV quoted with no as-is value. RED.** 🟢 The deal states "70% LTV" with no basis and no as-is figure. 🟡 It is probably ARV-based, since `01` notes that fix-and-flip LTVs are typically quoted on ARV. Mechanism: per `01`, "an ARV-based 70% LTV can be 100%+ on current value". If renovations stall or Phoenix resale prices fall, the collateral covers less than the loan and the LP loses principal. → Q-RISK-04.
- **GEN-14: unrealized / unevidenced track record. RED** (with GEN-05 cited parenthetically). 🔴 "We've never had a loss" is an assertion with no realized net-to-LP figures, no loan count, no time window, and no definition of "loss". The GEN-05 mechanism applies: the claim is pitched at a level other than net-to-LP. It could mean no principal write-downs at the loan level while LPs still absorbed suspended distributions, extended workouts, or capitalized interest. Taken together, this is no validated LP-outcome data. → Q-GP-02.
- **HML-03: default rate not disclosed. YELLOW–RED.** 🟢 Absent. "Never had a loss" is not a default rate; a fund can have defaults and still claim no loss through foreclosure and resale. → Q-RISK-05.
- **HML-04: recovery rate not disclosed. YELLOW–RED.** 🟢 Absent. Recovery rate and workout timeline decide the LP's realized loss. `04` names *"we've never had a loss"* as the **bad-answer signal** for this exact question, and the GP has led with it unprompted. → Q-RISK-05.
- **GEN-16: no fee or waterfall disclosure. YELLOW–RED.** 🟢 Not one fee line is given, and there is no hurdle or carry. Gross-to-net drag cannot be known (§4), and the "net" label cannot be verified. → Q-FEE-01.

**YELLOW**

- **HML-02: geographic concentration.** 🟢 One metro (Phoenix) and one strategy (fix-and-flip). A local housing-price decline hits every loan's exit, the borrower's sale at ARV, at the same time. Diversification offers no offset. → Q-RISK-05 (stress-period history) and the geographic-distribution question attached to HML-02.
- **GEN-17: essential category disclosures absent.** 🟢 Per `01`, a hard money fund normally discloses average LTV on both as-is and ARV, default history, foreclosure process and recovery rate, geographic mix, and sponsor history through a downturn. This fund disclosed none of them. GEN-15 is cited parenthetically: the debt-fund equivalent of missing financials (loan tape, loan-level terms, fund financials) is also absent. → Q-RISK-03, Q-RISK-04, Q-RISK-05.
- **GEN-13: no sensitivity or downside case.** 🟢 A single-point "target 11%" with no bear case. For a single-metro credit book, the missing downside is a price-decline scenario. → Q-DS-03.
- **GEN-11: distribution timing not disclosed.** 🟢 A target return with no distribution schedule, payment frequency, or reinvestment / DRIP terms, and no word on whether "net" is an IRR or a current yield. → Q-DIST-01.
- **GEN-03: marketing-heavy, substance-light.** 🟢 "Experienced team" and "never had a loss" replace underwriting data. → Q-GP-02 and a request for the full underwriting model and historical actuals.

**Clusters**
- **HML-01 + HML-03 + HML-04 + HML-02** form the debt-fund loss-severity cluster. There is no evidence of the collateral cushion, the default history, or the recovery competence, and all the loans sit in one market. Together these are a RED: the fund's downside cannot be bounded.
- **GEN-14 (+ GEN-05) + GEN-03** form the unvalidated-sponsor cluster. Per `03`, this pairing is a RED cluster, not two separate soft flags.

**Probed, not fired** (the facts needed to fire them are 🔴 unknown, so each is a must-ask rather than a flag):
- **GEN-01**, co-investment: unstated. → Q-GP-01.
- **GEN-02**, regulatory history: unstated. → Q-GP-03.
- **GEN-06**, affiliate servicing: unstated. → Q-FEE-02.
- **CREDIT-01**, fund-level leverage: unstated, though the above-baseline 11% makes it a live question. → Q-RISK-06.
- **HML-05**, management-fee step-down: the fund term is unstated. → Q-FEE-01.

---

## 6. Missing Disclosures

Against the `01` Hard Money / Bridge baseline and the `02` fee inventory:

**Category-essential items (`01`), all missing:**
1. Average portfolio LTV on **as-is** value *and* on ARV, plus the maximum single-loan LTV and loan-to-cost.
2. Historical **default rate**, including through 2020 and 2022–23.
3. **Foreclosure process and recovery rate**, with the average workout timeline.
4. **Geographic mix**: Phoenix submarkets, plus any loans outside the metro.
5. **Sponsor history through a downturn**: when the team started lending, and which cycles they have actually lent through.

**Fund structure, all missing:**
6. Sponsor name, principals, and the regulatory status of the manager.
7. Fund size / AUM, loan count, average and largest loan size.
8. Fund term, hold, lock-up, redemption / withdrawal rights and gates.
9. Minimum investment and accreditation requirement.
10. Whether the fund uses leverage at fund level.
11. Lien position: first-lien only? Personal guarantees?

**Fees and economics (`02`), all missing:**
12. Every fee line in §4, including who keeps borrower points and default interest.
13. Hurdle, carry, and catch-up, if a performance fee exists.

**Return definition, all missing:**
14. Whether the 11% net is an IRR or a cash yield, the distribution frequency, and the reinvestment option.
15. The realized net-to-LP history behind the target.

**Track record, all missing:**
16. Realized net-to-LP returns by year.
17. Loans originated, repaid, defaulted, and foreclosed, with outcomes.

This deal omits essentially *every* item its category normally discloses. That is why the verdict is "insufficient disclosure" and not a merits call.

---

## 7. GP Alignment

- **Co-investment:** not stated, so it is 🔴 unknown whether the GP has any cash in the fund, or on pari-passu terms. Must-ask (Q-GP-01).
- **Realized net-to-LP track record:** **unverified.** "We've never had a loss" is not a track record. It has no period, no volume, and no definition of "loss", and it gives no net-to-LP return (GEN-14, GEN-05). "Experienced" is also unverified: there is no team, no years, and no AUM history.
- **Waterfall alignment:** unknown. There is no hurdle or carry disclosure, so it cannot be judged whether the GP earns economics before LPs receive their target (GEN-16).
- **Affiliate fees:** unknown. In bridge lending the GP often originates and services the loans itself, which means it can earn points and servicing fees on volume regardless of credit outcomes. That is an origination-volume incentive that can work against LP credit discipline. 🟡 Inferred from the `02` fee structure; not stated for this fund. Must-ask (Q-FEE-02).

---

## 8. Questions for the GP

**Must-ask**

| # | ID | Question | Bad-answer signal (the specific dodge) | Fired flag |
|---|---|---|---|---|
| 1 | Q-RISK-04 | "What is the average portfolio LTV on as-is value, not just ARV?" | Quotes only LTV-on-ARV; can't produce an as-is LTV; "our borrowers always complete." | HML-01 |
| 2 | Q-RISK-05 | "What is your historical default rate and realized recovery rate, including through 2020 and 2022–23?" | A default rate without recovery (or the reverse); **"we've never had a loss"** (already given unprompted); silence on 2022–23. | HML-03, HML-04, HML-02 |
| 3 | Q-GP-02 | "Can you restate your track record as net-to-LP IRR on fully-realized, exited deals only?" (For this fund: realized net-to-LP returns by year, on repaid and foreclosed loans.) | Offers only loan-level or GP-level figures; "most loans are still performing"; can't separate realized from unrealized. | GEN-14, GEN-05, GEN-03 |
| 4 | Q-FEE-01 | "Can you provide the complete fee schedule and the full distribution waterfall?" Include who keeps borrower points and default interest, and whether the management fee steps down. | "Standard market fees"; a partial list; "the PPM has it" without producing it; fees surface only after you commit. | GEN-16 (HML-05 probe) |
| 5 | Q-RISK-03 | "Can you provide trailing-twelve-month actuals, the rent roll, and complete debt terms?" For a debt fund: the current loan tape (balance, rate, LTV as-is and ARV, maturity, status by loan) and the fund financials. | Only summary statistics; the loan tape withheld; "the financials are confidential until you commit." | GEN-17, GEN-15 |
| 6 | Q-DS-03 | "What is the return under a bear case?" For this fund: Phoenix home prices fall during the renovation window, and defaults rise. | A single-point pro forma with no downside; "we underwrite conservatively" with nothing to show; the bear case still shows a gain. | GEN-13 |
| 7 | Q-DIST-01 | "What is the projected distribution schedule, and at what milestones does LP capital start returning?" | "We'll distribute when the deal supports it" with no milestones; a target quoted with no distribution timing. | GEN-11 |
| 8 | Q-GP-01 | "How much of your own capital is in this deal, on the same terms as LPs?" | "Our sweat equity is our investment"; co-invest is a fee waiver, not cash; a token amount on better terms than LPs. | GEN-01 (probe) |
| 9 | Q-GP-03 | "Have you or your principals faced any regulatory action, enforcement, or investor litigation?" | Deflects to "nothing material"; blames the LP or the regulator; a search turns up something they didn't disclose. | GEN-02 (probe) |
| 10 | Q-FEE-02 | "Which service providers are GP-affiliated, what do they charge, and are those rates third-party-benchmarked?" (origination, servicing, workout, any construction-draw inspection) | "All arm's-length" without naming providers; affiliate fees undisclosed; no benchmark offered. | GEN-06 (probe) |
| 11 | Q-RISK-06 | "What is the fund's leverage ratio, and is the quoted LP IRR levered or unlevered?" Escalated from conditional because 11% net is above the 8–10% category baseline. | Won't disclose leverage; presents a levered return as if unlevered; "leverage is conservative" with no number. | CREDIT-01 (probe) |
| 12 | Q-LIQ-01 | "What are my options if I need to exit before the hold period ends?" (redemption notice, gates, suspension rights) | "A secondary market may develop"; "we'll try to accommodate"; silence, meaning the fund is illiquid and the lock-up is undisclosed. | — |

**Nice-to-ask**

| ID | Question | Bad-answer signal | Flag |
|---|---|---|---|
| Q-FEE-04 | "What preferred return do LPs receive before the GP earns promote, and is it cumulative and compounding?" Asked if a performance fee exists. | Hurdle below 6% or absent; non-cumulative. | EQUITY-04 / EQUITY-05 (only if a carry exists) |
| Q-FEE-03 | "Is the waterfall deal-by-deal or whole-of-fund, and is there a clawback?" Asked if carry is crystallized periodically. | Carry paid on interim income with no clawback if later losses come; "you get paid when we get paid." | EQUITY-01 / EQUITY-02 (only if a carry exists) |
| Q-GP-04 | "How have your headcount and deal-monitoring capacity grown alongside AUM?" | AUM multiplied while the team stayed flat; no named person runs asset management or workouts. | GEN-04 (not fired) |
| Q-DIST-02 | "When are capital calls expected, and what's the consequence of a missed or late call?" | "Calls as needed" with no notice period; punitive dilution. | — |
| Q-LIQ-02 | "When will K-1s be delivered each year, and have you historically delivered them before the filing deadline?" | "As soon as we can"; a history of extensions. | — |

---

## 9. Diligence Checklist (third-party verification)

1. **PPM, operating agreement, and subscription docs.** Confirm the fee schedule, the hurdle and carry, redemption gates, fund-leverage permissions, and who receives points and default interest.
2. **Background / regulatory search** on the sponsor entity and principals: SEC IAPD / Form ADV (if an RIA), FINRA BrokerCheck, Arizona Corporation Commission and state lending/mortgage licensing (Arizona Department of Insurance and Financial Institutions), and court records for investor or borrower litigation.
3. **Loan tape audit.** A sample of loans checked against recorded deeds of trust in the Maricopa / Pinal County recorder: lien position, recorded amounts, and foreclosure filings (trustee's sale notices). This tests "never had a loss" against public foreclosure records.
4. **Independent valuation check.** Sample as-is appraisals or BPOs against the stated LTVs, and ARV comps against recent Phoenix resale data.
5. **Fund financials.** Audited statements (who the auditor is), any loan-loss reserve, and whether non-accrual or extended loans are disclosed.
6. **Fund-level lender** (if any). Credit facility terms, advance rate, and covenants that could force loan sales in a downturn.
7. **LP references.** Ideally LPs invested through 2022–23, asked about distribution consistency and any suspended or reduced payouts.

---

## 10. Verdict

**Pass as presented (insufficient disclosure).**

*Screening output only, not investment advice.*

**Reasoning.** For a hard money / bridge fund, the core return story is *coupon minus credit losses minus fees*, and none of those three is disclosed in a form you can underwrite:
- **The coupon side** is a target that sits 100 bps above the category's 8–10% net range, with no explanation.
- **The credit-loss side** has no as-is LTV, default rate, recovery rate, or downturn history (HML-01, HML-03, HML-04). It is backed only by "we've never had a loss", which is the exact bad-answer signal `04` names for Q-RISK-05.
- **The fee side** is entirely absent (GEN-16), so the "net" label is unverified.

On the stated target, the benchmark math (≈617 bps over HYG, ≈676 bps over the 3-month bill) clears comfortably. That is necessary, not sufficient: it is a comparison against the GP's own unverified number, and the bear case at the category floor (8%) is already thin for a 3–5 year lock-up.

**Biggest swing factor:** as-is LTV. At a real 70% as-is LTV with a demonstrated recovery process, this could be a sound senior-secured income fund. At 70% of ARV in a falling single-metro market, the LP is lending at or near current value, and the 11% coupon does not pay for that tail.

**Who it could suit (if it re-screens well):** an accredited LP who wants short-duration real-estate income, accepts single-metro and single-strategy concentration, has no need for liquidity during the fund term, and sizes the position as a satellite holding, not core fixed income.

**What would have to be true to Pursue:**
- Portfolio as-is LTV is disclosed and sits inside the 65–75% category norm on an **as-is** basis, or the ARV-based figure has a defined as-is cap.
- A loan-level history is provided, ideally including 2020 and 2022–23, with default rate, recovery rate, and workout timelines that hold up against the county foreclosure record.
- A full fee schedule shows how 11% net is reached from the gross loan yield, and fund-level leverage, if any, is disclosed.
- GP cash co-investment is pari passu, and the regulatory search comes back clean.

**Re-screen list** (send these; re-run the screen on receipt):
1. Portfolio LTV on as-is and on ARV (average and maximum), plus loan-to-cost.
2. Default rate, recovery rate, and workout timeline by year, including 2020 and 2022–23.
3. Full fee schedule and waterfall, including who keeps points and default interest.
4. Fund leverage, if any, and whether the 11% is levered.
5. Realized net-to-LP returns by year, and a definition of "loss".
6. Current loan tape: count, sizes, lien position, status, and Phoenix submarket mix.
7. Fund term, lock-up, redemption rights and gates; minimum investment; distribution frequency.
8. Sponsor identity, principals, co-investment amount, and regulatory history.
