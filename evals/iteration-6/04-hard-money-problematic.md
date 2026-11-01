# Eval fixture 04
*Iteration-6 run, 2026-11-01, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 436a76b.*

# Bridge Fund Screen (Phoenix fix-and-flip)

**Verdict: Pass as presented — insufficient disclosure.** Four sentences of pitch cannot show how the 11% is earned, what it is net of, or what protects LP capital when a flip fails.

*Screening output only, not investment advice.*

**Biggest swing factor:** the as-is LTV together with realized default and recovery history. The re-screen list is in Section 10.

Confidence tags: 🟢 stated or from a reference, 🟡 inferred, 🔴 assumed or unverifiable.

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Hard money / bridge loan 🟢 |
| Deal type | Hard money / bridge debt fund, fix-and-flip lending 🟢 |
| Sponsor | Not stated. The team is described only as "experienced" and no principal is named |
| Geography | Phoenix metro only 🟢 |
| Minimum | Not stated |
| Hold / fund term | Not stated (category norm: 6–18 months per loan, 3–5 year fund 🟢) |
| Raise / fund size | Not stated |
| Claimed return | "Target 11% net" 🟢. A target, not a realized figure. IRR or yield not stated; what "net" deducts not stated |
| LTV | 70% 🟢. Basis (as-is or ARV) not stated; average or maximum not stated |
| Lien position | Not stated. The norm is senior secured, but this pitch doesn't say so 🔴 |
| Loss history | "Never had a loss" 🔴 unverified, no figures or time period given |

---

## 2. Return Stress-Test

**Comparator:** HYG, 4.83% trailing 10yr, plus the duration-matched Treasury (returns to 2026-06-30, Treasury closes 2026-09-24). 🟢

**The claim against the category:** 11% net sits 100 bps above the top of the 8–10% net norm for this deal type. 🟢 It is also only a target, and nothing in the pitch explains the excess.

Exit cap and rent growth don't drive a loan book. The swing assumptions here are:
1. **Realized credit loss:** default rate × (1 − recovery).
2. **As-is LTV:** this sets recovery when a flip fails.
3. **What "net" means, and any fund-level leverage:** this sets how much of the 11% is real and how much risk produced it.

| Case | Net to LP | What has to be true | Over HYG | Read at a 3–5 yr lock-up (~300–400 bps hurdle) |
|---|---|---|---|---|
| **Bull** (GP target) | 11.00% | Target is met, net of all fees and losses; loss experience stays near zero | 617 bps | Clears comfortably |
| **Base** (category norm, `01`) | 8–10% | The fund performs like its category rather than above it | 317–517 bps | 8%: clears, thin. 9–10%: clears comfortably |
| **Bear** (breakevens, no loss data exists to model) | Below 7.83–8.83% | Annual realized losses or undisclosed fees exceed 217–317 bps | Below 300–400 bps | Lock-up is uncompensated |
| **Severe** | Below 4.83% | Drag exceeds 617 bps | Negative | Trails a liquid index outright |

- **Lock-up is my input, not the deal's.** 🔴 I ran 1, 3 and 5 years because the term is undisclosed. The 11% clears at all three (hurdle ~200 bps at 1 year, ~300–400 bps at 3–5 years).
- **Treasury floor:** 11% is 676 bps over the 3mo (4.24%) and 613 bps over the 2yr (4.87%). At the norm, 8–10% is 376–576 bps over the 3mo. 🟢 HYG's trailing return currently sits below the 2yr Treasury, so the Treasury is the tighter floor for a multi-year lock-up.
- **How much loss the cushion absorbs:** 🔴 illustrative only, using the `03` example of 40% recovery. A 217–317 bps cushion is used up by annual defaults of about 3.6–5.3% of capital. The same library shows why both numbers are needed: 2% default at 40% recovery loses 120 bps, while 5% default at 90% recovery loses 50 bps. Neither is this fund's data.

**Read:** clearing the hurdle at a target proves little, since any pitch can state a target. Beating the spread is necessary, not sufficient, and this fund's single-metro concentration is a risk HYG diversifies away. An amplifier like that raises the premium an LP should demand. 🟢

---

## 3. Where LP Returns Come From

**Can't tell from this.** No decomposition is given.

- **Cash flow:** a debt fund should earn its return from coupon and borrower-paid points, with late fees and default interest flowing to the fund. 🟢 (category structure) None of these rates are disclosed, so the mix is unknown.
- **Exit:** `GEN-08` as defined doesn't apply, because there is no terminal-value assumption. The exit risk moves to the borrower instead: repayment depends on each flip selling or refinancing. 🟡 Not computable against the 60% test, and not fired.
- **Leverage:** undisclosed. `GEN-07` and `CREDIT-01` are **not fired** because firing them would need an assumption. They are must-asks because the unexplained 100+ bps over the norm has to come from somewhere.

The excess has four possible sources, and the pitch rules out none of them: 🟡
1. Higher coupons or points, which may mean weaker borrowers. Points above 5 are flagged as predatory in `02`.
2. A fund-level credit line levering the book.
3. Loss assumptions set near zero because losses have been near zero so far.
4. A "net" that excludes some fees.

---

## 4. Fee Stack Summary

**Total gross-to-net drag: not computable. That is the finding.** 🟢 No fee, no gross return and no waterfall is disclosed. Running the calculator on what was disclosed returns 0 bps, which is an artifact of having no inputs, not evidence of a free fund.

| Fee (`02`, hard money / bridge) | Typical range | This deal |
|---|---|---|
| Origination points (borrower-paid, flow to yield) | 1–3 points | Not stated |
| Fund management fee | 1–2% of AUM, annual | Not stated |
| Servicing fee | 0.25–0.5% of balance, annual | Not stated |
| Performance fee / carry | 10–20% above a 5–8% hurdle | Not stated |
| Late fees / default interest | Should go to the fund, not the GP | Not stated |
| Wind-down fee | 0.5–1% of remaining AUM | Not stated |
| Admin / IR / K-1 | 0.1–0.5% or fixed per LP | Not stated |
| Affiliate fees | No norm; the test is disclosure and benchmarking | Not stated |
| Feeder / fund-of-funds wrapper, if any | Additional 50–150 bps annually | Not stated |

**What 11% net would require.** 🔴 These stacks are `02` range points I supplied, not this deal's terms. They assume a 5-year hold and exclude admin, wind-down and wrapper fees.

| Illustrative stack | Drag | Gross needed for 11% net | Against the 11–13% gross norm |
|---|---|---|---|
| Low: 1% mgmt, 0.25% servicing, no carry | 125 bps | 12.25% | Inside |
| Mid: 1.5% mgmt, 0.375% servicing, 15% carry over 6.5%, no catch-up | ≈296 bps | ≈14.0% | Above |
| High: 2% mgmt, 0.5% servicing, 20% carry over 5%, full catch-up | ≈505 bps | ≈16.0% | Well above |

**Read:** 🟡 11% net fits inside the normal gross range only with a low fee load and no carry. With a mid or high stack, the book must out-earn the category gross range, which brings back the question in Section 3 of what risk is producing the yield.

---

## 5. Red Flags

YELLOW–RED flags are treated as RED until an answer moves them down, per `03`.

**RED**
- `HML-01` **LTV with no as-is value.** 🟡 The basis is unstated; ARV is inferred because this is fix-and-flip lending and ARV is the category norm. On an ARV basis, 70% LTV exceeds 100% of current value whenever the as-is value is below 70% of ARV. If the renovation thesis fails, the LP has no equity cushion, even though 70% reads as conservative.
- `GEN-14` **No realized exits cited.** 🟢 "Never had a loss" comes with no realized loans, no net-to-LP figures and no time period. The LP has no validated record to rely on.

**YELLOW–RED (treat as RED)**
- `HML-03` **Default rate not disclosed.** 🟢 "No losses" is not "no defaults". Extended, modified or foreclosed loans can all sit outside that claim, so the LP can't see how often borrowers failed.
- `HML-04` **Recovery rate not disclosed.** 🟢 Workout skill sets the LP's realized loss, and a fund with no recorded losses may never have tested it. `04` lists "we've never had a loss" as a bad-answer signal on `Q-RISK-05`, so the pitch opens with the dodge.
- `GEN-16` **No fee or waterfall disclosure.** 🟢 Undisclosed fees are still paid, and the 11% can't be tested without knowing what "net" deducts.
- `GEN-15` **Missing financials.** 🟢 No loan tape, fund financials or debt terms, so nothing can be underwritten.

**YELLOW**
- `HML-02` **Single-metro concentration.** 🟢 One Phoenix-wide fall in resale prices hits collateral values and borrower exits at the same time, across the whole book, with no diversification offset. The book is also all fix-and-flip, the same correlated-default mechanism as `CREDIT-02` (outside this deal type's routing).
- `GEN-17` **Essential category disclosures absent.** 🟢 See Section 6.
- `GEN-11` **Return with no distribution schedule.** 🟢 Timing of income and capital return is unknown.
- `GEN-13` **Single-point target, no downside case.** 🟢 One number and no sensitivity to loss rates or a resale slowdown.
- `GEN-03` **Substance-light pitch.** 🟡 "Experienced team" and "never had a loss" stand in for underwriting detail and actuals.

**Cluster:** `HML-01` + `HML-03` + `HML-04` + `GEN-14` is one problem seen from four angles: the fund's capital protection is asserted, and none of it can be measured. The YELLOWs would also read as RED on their own, per the `03` cluster rule.

**Probed, not fired (undisclosed is not the same as adverse):** `GEN-01` co-invest, `GEN-02` regulatory history, `GEN-04` AUM growth, `GEN-05` GP-level vs LP-level IRR (no IRR was cited to test), `GEN-06` affiliate fees, `GEN-07` and `CREDIT-01` leverage, `GEN-08` exit dependence, `GEN-09` and `GEN-10` fund-level debt terms if a credit line exists, `GEN-18` submarket supply, `HML-05` fee step-down. Each has its question in Section 8.

---

## 6. Missing Disclosures

**Hard money essentials (`01`):**

| Essential disclosure | Status |
|---|---|
| Average loan LTV, as-is and ARV | Partial: one number, no basis |
| Default rate history | Absent |
| Foreclosure process and recovery rate | Absent |
| Geographic mix | Stated at metro level only; no submarket breakdown |
| Sponsor history through a downturn | Absent: "experienced" only; nothing on 2020 or 2022–23 |

**Also absent (`01` / `02`):**
- Sponsor and principal names, firm age, loans originated
- Fund size, loan count, average loan size, largest-loan exposure
- Lien position
- Gross yield, coupon and points
- Full fee schedule, carry, hurdle, waterfall and step-down
- Fund term, redemption rights and lock-up
- Distribution schedule
- GP co-invest
- Fund-level leverage
- Minimum investment

**Assumed inputs that are gaps:** every fee, the gross return and the hold used in Sections 2 and 4.

---

## 7. GP Alignment

- **Co-invest:** Not stated. Cash, pari-passu status and amount all unknown. Not treated as zero.
- **Realized net-to-LP track record:** None provided. **"Never had a loss" is unverified.** 🔴 It also has no denominator: a young fund, a rising market or a book of mostly unresolved loans could each produce a true statement that says little. 🟡 Loans of 6–18 months mean the record only tests the market conditions it lived through, so 2020 and 2022–23 are the periods to ask about. 🟢
- **Waterfall alignment:** Not stated. Whether the GP earns carry, over what hurdle, and with what catch-up is unknown.
- **Affiliate fees:** Not stated.
- **Sponsor identity:** Not stated, so background and regulatory checks can't begin.

---

## 8. Questions for the GP

**Must-ask**

| ID (flag) | Question | Bad-answer signal |
|---|---|---|
| `Q-RISK-04` (`HML-01`) | "What is the average portfolio LTV on as-is value, not just ARV?" Add: is the 70% an average or a maximum, and is it on the initial advance or fully drawn? | Quotes only LTV-on-ARV; can't produce as-is LTV; "our borrowers always complete." |
| `Q-RISK-05` (`HML-03`, `HML-04`) | "What is your historical default rate and realized recovery rate, including through 2020 and 2022–23?" Add: how many loans were extended, modified or taken back as REO, and what is the workout timeline? | "We've never had a loss" (already given); default rate without recovery, or the reverse; silence on 2022–23. |
| `Q-GP-02` (`GEN-14`, `GEN-05`) | "Can you restate your track record as net-to-LP IRR on fully-realized, exited deals only?" | Only project- or GP-level IRR; "most deals are still performing"; can't separate realized from unrealized. |
| `Q-FEE-01` (`GEN-16`, `HML-05`) | "Can you provide the complete fee schedule and the full distribution waterfall?" Add: what exactly does "11% net" deduct, is it an IRR or a yield, and does the management fee step down? | "Standard market fees"; partial list; "the PPM has it" without producing it. |
| `Q-FEE-02` (`GEN-06`) | "Which service providers are GP-affiliated, what do they charge, and are those rates third-party-benchmarked?" Add: do late fees and default interest go to the fund? | "All arm's-length" without naming providers; no benchmark; default interest routed to a GP "workout fee". |
| `Q-FEE-03`, `Q-FEE-04` (`EQUITY-01`, `EQUITY-02`, `EQUITY-04`, `EQUITY-05`; apply if carry exists) | "Is the waterfall deal-by-deal or whole-of-fund, and is there a clawback?" and "What preferred return do LPs receive before the GP earns promote, and is it cumulative and compounding?" | "You get paid when we get paid"; can't explain the catch-up; hurdle absent or below 5–6%. |
| `Q-DS-01` (adapted; `GEN-08`) | What share of the 11% comes from coupon, points, late and default fees, and leverage? | Can't or won't decompose it. |
| `Q-DS-02` (`GEN-07`) | "Strip out leverage… what is the unlevered, in-place return?" | Treats the levered figure as the only one; "leverage is just how the deal works." |
| `Q-RISK-06` (`CREDIT-01`), `Q-RISK-01` (`GEN-09`), `Q-RISK-02` (`GEN-10`) | "What is the fund's leverage ratio, and is the quoted LP IRR levered or unlevered?" If a credit line exists: when does it mature, and is any floating rate capped? | Won't disclose; "leverage is conservative" with no number; "we'll refinance" with no terms. |
| `Q-DS-03` (`GEN-13`) | Bear case, adapted: what is the LP return if Phoenix resale prices fall and flips stall? | Single-point target; "we underwrite conservatively" with nothing to show; the bear case is still a gain. |
| `Q-RISK-03` (adapted; `GEN-15`, `GEN-17`) | Can you provide the current loan tape, trailing-twelve-month fund actuals and audited financials? | "Confidential until you commit." |
| `Q-DIST-01` (`GEN-11`) | "What is the projected distribution schedule, and at what milestones does LP capital start returning?" | "We'll distribute when the deal supports it"; a target quoted with no timing. |
| `Q-LIQ-01` | "What are my options if I need to exit before the hold period ends?" | "We'll try to accommodate"; lock-up undisclosed. An honest "there is none" is a good answer. |
| `Q-GP-01` (`GEN-01`) | "How much of your own capital is in this deal, on the same terms as LPs?" | "Our sweat equity is our investment"; a fee waiver instead of cash. |
| `Q-GP-03` (`GEN-02`) | "Have you or your principals faced any regulatory action, enforcement, or investor litigation?" | "Nothing material"; a search surfaces something undisclosed. |
| `Q-MKT-01` (adapted; `GEN-18`), with the `HML-02` response (no `04` row) | "What is the geographic distribution of the loan book?" Add: what submarket supply and absorption data support the resale assumptions behind your ARVs? | Metro-level optimism standing in for submarket data; no supply pipeline acknowledged. |
| `GEN-03` response (no `04` row) | "Can you provide the full underwriting model and the historical actuals behind these projections?" | More narrative about experience, no actuals. |

**Nice-to-ask**

| ID (flag) | Question | Bad-answer signal |
|---|---|---|
| `Q-GP-04` (`GEN-04`) | "How have your headcount and deal-monitoring capacity grown alongside AUM?" | "We're lean and efficient" as the whole answer; no named asset manager. |
| `Q-DIST-02` | "When are capital calls expected, and what's the consequence of a missed or late call?" | "Calls as needed"; punitive dilution buried in the docs. |
| `Q-LIQ-02` | "When will K-1s be delivered each year, and have you historically delivered them before the filing deadline?" | "As soon as we can"; a history of extensions. |

---

## 9. Diligence Checklist

Third-party verification still needed, if the GP answers:

- [ ] **PPM and subscription documents:** fee schedule, waterfall, lock-up and redemption terms, and whether the 11% is a promise or only a target.
- [ ] **Background and regulatory:** SEC, FINRA and state records and litigation searches on the sponsor and each principal, once named. Form ADV if the manager is an RIA.
- [ ] **Audited fund financials:** to check realized losses, reserves, loans held at carrying value and any REO.
- [ ] **Loan tape sample:** confirm default, extension, modification and payoff history against the "no loss" claim.
- [ ] **Appraisals and comps:** sampled third-party as-is values and ARVs, with ARVs checked against sold comps.
- [ ] **Title and lien:** confirm first-lien position on sampled loans.
- [ ] **Lender:** credit-line agreement, if any, covering size, maturity, covenants and priority over LP capital.
- [ ] **Prior LP references:** chosen by you rather than the GP, ideally from before 2022.
- [ ] **Your own counsel and tax adviser:** legal and tax review of the documents.

---

## 10. Verdict

**Pass as presented — insufficient disclosure.**

*Screening output only, not investment advice.*

**Reasoning.** This is a disclosure call, not a judgment that the fund is bad. 11% clears the comparator on paper (617 bps over HYG against a ~300–400 bps hurdle at 3–5 years), but it is an unverified target 100 bps above the category norm. Of the five essential disclosures for this deal type, default history, recovery history and downturn history are absent, and LTV has no basis. The core return story can't be underwritten, so a merits verdict isn't available. The sponsor's one piece of evidence, "never had a loss", is the bad-answer signal the question bank warns about.

**Biggest swing factor:** as-is LTV and realized loss history. If as-is LTV is well below 100% and loss history holds up through 2020 and 2022–23, this could be a real candidate. If 70% is on ARV with thin as-is equity, and the record hasn't been tested, the "no loss" claim offers no protection.

**Re-screen list (a fresh screen needs all of these):**
1. Sponsor and principals named.
2. Average and maximum LTV on both as-is and ARV, plus lien position.
3. Default, extension, REO and recovery history by year, through 2020 and 2022–23, with workout timelines.
4. Realized net-to-LP returns by year.
5. Full fee schedule and waterfall, and a definition of "net" (IRR or yield, and what it deducts).
6. Gross yield decomposition and fund-level leverage.
7. Fund term, lock-up, redemption rights and distribution schedule.
8. GP co-invest in cash, on pari-passu terms.
9. Loan count, average size, largest loan and Phoenix submarket mix.

**Who it would suit, if it passes re-screen:** an LP seeking short-duration income who accepts single-metro, single-strategy credit risk and the fund's lock-up, and holds it as a concentrated satellite position. It would not suit anyone who needs liquidity on demand.

**What would have to be true for 11% to be worth the lock-up:**
- It is net of all fees and realized losses, without leverage doing the work.
- There is a real as-is equity cushion.
- The record includes actual defaults worked out at known recoveries.
- Realized losses and any fee surprises stay inside the 217–317 bps cushion above the hurdle.
