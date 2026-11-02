# Eval fixture 03
*Iteration-9 run, 2026-11-01, blind generation by fresh-context agent (model: Opus), against SKILL.md @ e61616f plus the notice-spacing edit.*

**Verdict: Pursue with conditions.** It is worth more diligence: the disclosed credit terms hold up and no standalone RED fired, but nothing yet shows that the 9% net comes from the loan book alone, after every GP layer.

*Screening output only, not investment advice.*

Tags: 🟢 stated or from a reference, 🟡 inferred, 🔴 assumed or unverifiable.

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Hard Money / Bridge Loan 🟢 |
| Deal type | Hard money / bridge debt fund, senior secured 🟢 |
| Sponsor | Not stated |
| Geography | 12 states, no single metro over 15% 🟢 |
| Minimum | Not stated |
| Hold / fund term | Not stated (category norm is 6–18 months per loan, 3–5 years at fund level 🟢) |
| Raise | Not stated |
| Claimed return | 9% net target to LPs 🟢 (a target, not a realized figure) |
| LTV | 68% average on as-is value, 72% on ARV 🟢 |
| Credit history | 3.1% default rate, 92% realized recovery, including 2020 and 2022–23 🟢 (unaudited in what I have 🔴) |
| Loan grading | A–D, mix described as disclosed; the actual distribution is not in what I received |
| Stated fees | 1.5% management fee, stepping down to 1.0% after the investment period 🟢 |

Against the category norm: 9% sits mid-range of 8–10% net, the LTV is inside the 65–75% typical band, and the risk tier is Low-Med 🟢.

## 2. Return Stress-Test

The lock-up is not stated, so the comparison uses 4 years, the midpoint of the 3–5 year fund norm 🔴. These scenarios are mine, not the GP's. They assume no fund-level leverage 🔴, because leverage is undisclosed and would widen every outcome.

| Case | Swing assumptions | Net to LP | Over HYG (4.83% 10yr) | Over 3mo / 2yr Treasury (4.24% / 4.87%) | Read at ~300–400bps hurdle |
|---|---|---|---|---|---|
| Bull 🔴 | Book yield at the top of the category; losses at the historical rate | 10.0% | 517bps | 576 / 513bps | Clears comfortably |
| Base 🟢 | GP's target, taken as stated | 9.0% | 417bps | 476 / 413bps | Clears, 17bps above the top of the band |
| Bear 🔴 | Defaults triple to 9.3% a year, recovery falls to 80% | ≈7.4% | 256bps | 315 / 252bps | Thin / fails the hurdle |

Swing factors: default rate, loss severity, and whether fund leverage or undisclosed layers sit behind the target.

**Does it clear the lock-up?** On the stated target, yes. 9% exceeds HYG by ≈417bps. For a 4-year lock-up the hurdle is ~300–400bps, so the deal clears the bar 🟡. The answer depends on the lock-up: at 1 year or less (~200bps hurdle) it clears easily, and at 7 years (~400–600bps) it is thin. Clearing is necessary, not sufficient.

**How much cushion there is 🟡:**
- The net return can fall to 7.83% before it reaches the bottom of the hurdle band. That is a 117bps cushion.
- The 2yr Treasury (4.87%) is currently a slightly tighter floor than HYG. On that measure the LP is paid ≈413bps for credit and illiquidity together.
- If the 3.1% is annual, historical losses cost about 25bps a year (3.1% × 8% loss). If it is cumulative, they cost less.
- Credit losses could rise to about 142bps a year before the hurdle fails. That equals a 17.7% annual default rate at today's 8% severity, or 7.1% at 20% severity. On the disclosed history this is a wide margin, and severity is what erodes it fastest.

**The payoff is asymmetric.** The upside is about 100bps, capped by the coupon, because debt has no equity kicker. The bear case costs about 160bps. Even so, the bear case damages the premium rather than LP principal, provided the fund is unlevered 🔴.

**Two credit figures don't reconcile yet:**
- **LTV basis.** ARV is normally at or above as-is value, so on the same loan balance the ARV LTV should be at or below 68%. Instead it is 72%. The two figures therefore can't share a balance 🟡. The likely explanation is initial funding on as-is versus total commitment including rehab draws on ARV 🟡. If so, a fully drawn loan sits above 68% of as-is value before the rehab adds value, and 68% understates peak exposure. This is a question, not a defect (`Q-RISK-04`).
- **Recovery versus cushion.** A loan at 68% of as-is value recovers only 92% if net proceeds come to about 62.6% of as-is, roughly 37% below the value it was underwritten on 🟡. That assumes defaulted loans were at average LTV and that 92% is measured on principal 🔴. The possible explanations are that defaulted loans carried higher LTVs, that as-is appraisals ran high, or that workout costs were heavy. Each leads to a different view of the 68% (`Q-RISK-05`).

## 3. Where LP Returns Come From

- **Cash flow, on the structure of the asset.** Hard-money return is contractual coupon and origination points, with no terminal-value bet 🟡. `GEN-08` (exit-dependent IRR) does not fire. The relevant exit is the borrower's sale or refinance, which repays the loan, and that risk appears in the default and recovery figures.
- **The split is not disclosed.** I can't tell how much comes from coupon, points, or default interest and late fees 🔴 (`Q-DS-01`).
- **Leverage is the open question.** The summary is silent on fund-level leverage. I can't tell whether 9% is the book's yield or a levered version of it. `GEN-07` (financing story) is not fired because that would require assuming a leverage figure, and it stays a must-ask (`Q-DS-02`, `Q-RISK-06`). `CREDIT-01` is outside this deal type's routing but is the same mechanism.

Can't determine from this whether more than 60% of the return is leverage-driven. Nothing stated suggests exit-driven return.

## 4. Fee Stack Summary

**Gross-to-net drag: 150bps a year on what is disclosed, stepping down to 100bps after the investment period. The full figure is not computable, and that is the finding: no gross yield and no complete fee schedule were given 🟢.**

| Fee (`02` hard money inventory) | Norm | This deal | Read |
|---|---|---|---|
| Fund management fee | 1–2% annual, aggressive >2.5% | 1.5%, then 1.0% 🟢 | In range, with a step-down. Fee base not stated |
| Servicing | 0.25–0.5% of balance, aggressive >1% | Not stated | Standard fee, usually flows to the GP |
| Performance fee / carry | 10–20% over a 5–8% hurdle, aggressive >25% or no hurdle | Not stated | Largest possible hidden layer |
| Origination points | 1–3 points, borrower-paid | Not stated | Should flow to fund yield; confirm the GP doesn't keep them |
| Late fees / default interest | Should go to the fund | Not stated | Confirm no GP "workout fee" |
| Wind-down fee | 0.5–1% of remaining AUM, absent in most short-duration funds | Not stated | Ask |
| Admin / IR | 0.1–0.5% or a fixed amount per LP | Not stated | Ask |
| Feeder wrapper, if any | Additional 50–150bps | Not stated | Check whether access is through a feeder |

**What the target implies:**
- **Implied gross 🟡.** A 9% net target plus 150bps of disclosed fee means gross of at least 10.5% (calculator: 10.5% gross less 150bps gives 9.00% net). If gross stays at 10.5% after the step-down, net would be 9.5%. I can't tell whether the 9% target already blends this in.
- **Unexplained gap 🟡.** The category's common gross is 11–13%. At that level, the gap to 9% net is 200–400bps, of which the management fee explains 150bps. That leaves 50–250bps for losses and undisclosed layers.
- **Stress test on the stack 🔴.** At 12% gross, with servicing of 0.5%, admin of 0.3%, and 20% carry over an 8% hurdle with full catch-up on a 4-year hold, the drag is 440bps (230bps recurring, about 210bps carry) and net is 7.60%. All those inputs are assumptions, listed in §6. The result shows that this full stack and a 9% net can't both be true at 12% gross. Either some of these layers are absent or gross is higher, and the schedule will show which.

## 5. Red Flags

**RED:** none fired as a standalone flag.

**YELLOW–RED:**
- `GEN-16` No full fee or waterfall disclosure (fires on everything beyond the management fee) 🟢. Undisclosed layers are still paid, so the LP can't confirm 9% is truly net. Under the library's rule this is treated as RED until the schedule arrives. → `Q-FEE-01`

**YELLOW:**
- `GEN-11` Net target with no distribution schedule 🟢. Monthly income and back-loaded payouts look identical at 9%, and the LP can't see when capital returns. → `Q-DIST-01`
- `GEN-13` Single-point target with no fund-level downside case 🟢. The through-cycle credit history partly offsets this, but it doesn't show the LP's return in a stress period. → `Q-DS-03`
- `GEN-17` Essential disclosures absent 🟢: foreclosure process, and sponsor identity and downturn history beyond the aggregate statistics. Workouts are a craft skill, and the LP's realized loss rests on them. → `Q-RISK-05`; `04` has no question citing this flag directly, so the `03` response is asked alongside it

**Cluster:** these four share one root, a summary-level disclosure, and one document request can largely cure them. A YELLOW cluster counts as RED under the library, so treat them as pass-or-resolve. That is why this is "with conditions" rather than a clean Pursue.

**Checked and not fired:**
- `HML-01` As-is LTV is disclosed. The 68%/72% basis question stays open (§2).
- `HML-02` 12 states and a 15% metro cap are real diversification 🟢. State-level concentration is not stated.
- `HML-03`, `HML-04` Both default and recovery are disclosed, including the stress periods 🟢. At 3.1%/92% they beat the 5%/90% profile the library uses as its better example, subject to definitions.
- `HML-05` The fee steps down 🟢.

**Can't fire without assuming facts, so routed to questions instead:**
- `GEN-01` co-invest (`Q-GP-01`)
- `GEN-02` regulatory history (`Q-GP-03`)
- `GEN-04` AUM growth versus team (`Q-GP-04`)
- `GEN-05`, `GEN-14` track-record basis (`Q-GP-02`)
- `GEN-06` affiliate fees (`Q-FEE-02`)
- `GEN-07` financing story (`Q-DS-02`)
- `GEN-08` exit-dependent return (`Q-DS-01`)
- `GEN-09`, `GEN-10` fund-level debt, if any (`Q-RISK-01`, `Q-RISK-02`)
- `GEN-15` missing financials (`Q-RISK-03`)
- `GEN-19` office collateral, if any (`Q-MKT-02`)

## 6. Missing Disclosures

**Essential disclosures for this class (`01`):**

| Item | Status |
|---|---|
| Average LTV, as-is and ARV | Disclosed 🟢, basis unclear |
| Default rate history | Disclosed 🟢, definition unclear |
| Recovery rate | Disclosed 🟢, definition unclear |
| Foreclosure process | **Absent** |
| Geographic mix | Disclosed 🟢 |
| Sponsor history through a downturn | **Partial**: aggregate statistics only, sponsor unnamed |

Enough is disclosed to underwrite the core credit story, so this gets a merits verdict and the absences below become conditions.

**Fees (`02`):** gross yield, fee base (committed, invested, or AUM), length of the investment period, servicing, carry and hurdle, treatment of points and default interest, wind-down, admin. In the §4 stress test, the carry, hurdle, catch-up, servicing, admin, and gross inputs were all assumed, and the 4-year hold there and in §2 was assumed too.

**Portfolio:**
- Fund-level leverage
- Loan count and average loan size. Metro limits say nothing about single-loan concentration
- Collateral type, including any office or commercial exposure, and the share of fix-and-flip versus purchase bridge loans
- The grade A–D distribution, and default experience by grade
- Whether the 3.1% and 92% cover this fund or the sponsor's whole platform; whether they are annual or cumulative, and by count or by dollars; what recovery is measured on; and how long workouts took

**Terms:** sponsor, minimum, raise, fund term, redemption rights, capital-call mechanics, distribution schedule.

## 7. GP Alignment

- **Co-invest:** not stated. Cash amount and pari-passu terms are unknown 🔴.
- **Realized net-to-LP track record:** none given. The 3.1% and 92% are loan-level credit statistics, and "realized" is a good sign, but they aren't LP returns. **The 9% is a target, and the record behind it is unverified 🔴.**
- **Waterfall:** not stated, including whether any carry exists.
- **Affiliate fees:** not stated. In this structure the servicing fee, points, and any workout fees are the places to look.
- **Stated positive:** the fee step-down lowers GP take as the book winds down 🟢.

## 8. Questions for the GP

**Must-ask**

| ID | Question | Bad-answer signal |
|---|---|---|
| `Q-RISK-04` (`HML-01`) | What is average LTV on as-is value? Why is the ARV figure higher than the as-is figure: are they on funded balance versus total commitment? What is fully drawn loan balance to as-is? | Quotes only LTV on ARV; can't produce as-is on a consistent basis; "our borrowers always complete" |
| `Q-RISK-05` (`HML-03`, `HML-04`, `GEN-17`) | What are your default and realized recovery rates through 2020 and 2022–23, shown by year and by grade? Annual or cumulative, by count or dollars? Recovery on what balance, what workout timeline, and what foreclosure process, run by whom? What were the LTVs on the defaulted loans? | One number without the other; "we've never had a loss"; silence on 2022–23 |
| `Q-GP-02` (`GEN-05`, `GEN-14`) | Can you restate your track record as net-to-LP IRR on fully realized funds or periods only? | Offers only project- or GP-level IRR; "most deals are still performing"; can't separate realized from marked |
| `Q-FEE-01` (`GEN-16`) | Can you provide the complete fee schedule and full distribution waterfall, and the gross yield behind the 9%? | "Standard market fees"; a partial list; "the PPM has it" without producing it |
| `Q-FEE-02` (`GEN-06`) | Which service providers are GP-affiliated, what do they charge, and are rates benchmarked? Who keeps points, late fees, and default interest? | "All arm's-length" without naming providers; no benchmark |
| `Q-FEE-03`, `Q-FEE-04` (if carry exists; `EQUITY-01`, `EQUITY-02`, `EQUITY-04`, `EQUITY-05`) | Is there carry? Over what hurdle, is it cumulative, and on what catch-up and clawback terms? | Can't explain the catch-up; "you get paid when we get paid"; hurdle absent |
| `Q-DS-02` (`GEN-07`), `Q-RISK-06` (borrowed from credit funds; `CREDIT-01`) | What is fund-level leverage, and what is the unlevered return on the loan book? Is the 9% levered? | Treats the levered figure as the only one; won't disclose leverage; "leverage is conservative" with no number |
| `Q-RISK-01` (`GEN-09`) | If the fund has a credit line, when does it mature relative to fund term, and what's the extension plan? | "We'll refinance" with no terms; no plan if the line isn't renewed |
| `Q-DS-01` (`GEN-08`) | How much of the 9% comes from coupon, how much from points, and how much from default interest or other items? | Can't or won't decompose it |
| `Q-DS-03` (`GEN-13`) | What was LP net return in 2020 and 2022–23, and what is your bear case? | "We underwrite conservatively" with nothing to show; the bear case is still a gain |
| `Q-DIST-01` (`GEN-11`) | What is the distribution schedule, and at what milestones does capital come back? | "We'll distribute when the deal supports it"; no timing |
| `Q-GP-01` (`GEN-01`) | How much of your own cash is in this fund, on the same terms as LPs? | "Sweat equity"; a fee waiver instead of cash; a token amount on better terms |
| `Q-GP-03` (`GEN-02`) | Have you or your principals faced any regulatory action, enforcement, or investor litigation? | "Nothing material"; a search turns up something they didn't disclose |
| `Q-RISK-03` (`GEN-15`), adapted | Can you provide audited fund financials, a current loan tape, and complete debt terms? | "Confidential until you commit"; partial periods only |
| `Q-LIQ-01` | What are my options if I need to exit before the fund term ends? Are there redemption gates? | "A secondary market may develop"; "we'll try to accommodate" |
| `Q-MKT-02` (if the book includes office or other variable assets; `GEN-19`) | How does underwriting reflect post-2020 physical occupancy and sublease overhang? | Pre-2020 baseline; leased occupancy only |

**Nice-to-ask**

| ID | Question | Bad-answer signal |
|---|---|---|
| `Q-RISK-02` (`GEN-10`) | If the credit line floats, is rate exposure capped, and when does the cap expire? | Cap expires before maturity; "rates should be lower by then" |
| `Q-GP-04` (`GEN-04`) | How have headcount and monitoring capacity grown with AUM? | Team flat while AUM multiplied; no named asset manager |
| `Q-DIST-02` | When are capital calls expected, and what happens on a missed call? | "Calls as needed"; punitive dilution buried in the docs |
| `Q-LIQ-02` | When are K-1s delivered each year? | "As soon as we can"; a history of extensions |

## 9. Diligence Checklist

- **PPM and subscription documents:** confirm fees, fee base, waterfall, leverage limits, concentration limits, redemption terms.
- **Audited fund financials:** tie them to the stated 9%, the default rate, and realized losses.
- **Loan tape:** recompute LTV on one basis, grade mix, property-type mix, single-loan concentration, state concentration.
- **Default and REO log:** recompute 3.1% and 92% loan by loan, including timelines and costs.
- **Appraisals:** sample as-is and ARV values, who orders them, and how they compare with liquidation outcomes.
- **Lien and title sample:** confirm the senior position on a selection of loans.
- **Background and regulatory:** SEC, FINRA, and state records for the sponsor and principals, litigation search, Form ADV Part 2 if the manager is an RIA.
- **Lender:** credit-line agreement and covenants, if the fund has one.
- **Investor references:** LPs who were invested through 2022–23.

## 10. Verdict

**Pursue with conditions.**

*Screening output only, not investment advice.*

**Why it earns more diligence:** the disclosures that usually sink a hard-money fund are here and within norm: as-is LTV of 68%, default and recovery through both stress periods, real geographic spread, a management fee in range with a step-down. The 9% target is mid-range and ≈417bps over HYG, which clears a 3–5 year lock-up 🟡.

**Why it isn't a clean Pursue:** the case rests on summary figures nobody has verified, and the cost side is incomplete. The 9% has no realized net-to-LP record, no gross yield, and no statement on leverage or carry behind it.

**Biggest swing factor:** whether 9% is produced by an unlevered loan book after all GP layers. If it is, this is a reasonably paid senior-credit position. If fund leverage gets it there, the 68% LTV and the historical loss figures no longer describe the LP's actual risk.

**Conditions to keep going:**
1. A complete fee schedule and gross yield that reconcile to 9% net.
2. Fund-level leverage stated, with the unlevered return shown.
3. Realized net-to-LP returns, including 2020 and 2022–23.
4. The 3.1% and 92% defined and tied to a loan-level log, and the 68%/72% LTV reconciled on one basis.
5. Cash co-invest on LP terms, a clean background check, and the sponsor named.
6. Fund term, redemption rights, and distribution schedule in writing.

**What would turn this into a Pass:**
- The GP won't supply any of the above.
- Carry with no hurdle, or above 25%.
- Servicing above 1%.
- Undisclosed leverage or a levered figure shown as unlevered.
- A loan-level default log that doesn't support the stated figures.
- A lock-up long enough that 417bps no longer clears (~400–600bps at 7–10 years).

**Who it suits:** an LP who wants income from senior-secured real estate credit, accepts capped upside, and can leave the capital locked for the full term, assuming the conditions clear. It doesn't suit someone who needs liquidity or wants equity-style appreciation.

**What would have to be true:** credit losses stay well under about 142bps a year, the realized record supports the target, and no layer outside the disclosed stack cuts into the 9%.
