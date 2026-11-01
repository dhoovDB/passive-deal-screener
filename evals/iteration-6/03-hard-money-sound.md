# Eval fixture 03
*Iteration-6 run, 2026-11-01, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 436a76b.*

**Verdict: Pursue.** Yes, this fund is worth more diligence: the numbers that decide a bridge fund are disclosed and sound, and no RED flag fires. Nothing here is verified yet, and the open items in §10 should be cleared before any capital goes in.

*Screening output only, not investment advice.*

Tags: 🟢 stated by the fund or from a reference, 🟡 inferred, 🔴 assumed or unverifiable. "Stated" means the fund said it, not that anyone has checked it.

---

## 1. Deal Snapshot

| Field | Detail |
|---|---|
| Asset class | Hard money / bridge loan 🟢 |
| Deal type | Senior-secured debt fund 🟢 |
| Sponsor | Not stated |
| Geography | 12 states, no single metro over 15% 🟢 |
| Collateral / borrower type | Not stated |
| Minimum | Not stated |
| Fund term / lock-up | Not stated (category norm: 6–18 months per loan, 3–5 year fund) |
| Raise | Not stated |
| Claimed return | 9% net target to LPs 🟢 (a target, not a realized figure) |
| LTV | 68% as-is, 72% ARV, portfolio averages 🟢 |
| Credit history | 3.1% default rate, 92% realized recovery, including 2020 and 2022–23 🟢 |
| Loan grades | A–D; the fund says the mix is disclosed, but the figures aren't in what you shared |
| Fees | 1.5% management fee, 1.0% after the investment period 🟢 |

---

## 2. Return Stress-Test

**Benchmark.** 9% net sits inside the 8–10% category range. The fund's term isn't stated, so I tested three lock-ups. The result clears the hurdle in all three.

| Lock-up tested | Illiquidity hurdle | Premium over HYG (4.83% 10yr) | Read |
|---|---|---|---|
| 1 year or less | ~200 bps | 417 bps | Clears comfortably |
| 4 years (category norm) 🟡 | ~300–400 bps | 417 bps | Clears comfortably, but only 17 bps above the top of the band |
| 7 years | ~400–600 bps | 417 bps | Clears, thin |

Spread over the duration-matched Treasury: about 476 bps over the 3-month (4.24%) and 413 bps over the 2-year (4.87%) 🟢. The 2-year currently out-yields HYG's trailing 10-year return, so the Treasury is the tighter floor, and the fund still clears it. Comparator data is as of the 2026-09-27 snapshot.

Clearing the bar is necessary, not sufficient. It rests on a target, and a single fund carries manager and concentration risk that HYG diversifies away.

**Scenarios.** The swing assumptions are (1) default rate times loss severity, (2) coupon and origination yield as short loans roll over, and (3) idle cash between loans. Stressed inputs below are my illustrations, not fund disclosures, and the verdict does not rest on them.

| Case | Assumptions | Net to LP | Premium over HYG | At a 4-year lock-up |
|---|---|---|---|---|
| Bull | Top of category range; fully deployed, losses at history 🔴 | 10.0% | 517 bps | Clears comfortably |
| Base | Fund target, with historic losses already inside it 🟢/🔴 | 9.0% | 417 bps | Clears comfortably |
| Base, if losses are not inside the target | 9.0% less about 25 bps of historic loss 🔴 | 8.75% | 392 bps | Inside the band, no longer above it |
| Bear | Defaults triple to 9.3%, recovery falls to 80%, 50 bps of coupon and cash drag 🔴 | ~6.9% | 207 bps | Fails the hurdle |

**What the numbers say:**

- **Historic loss is small.** 3.1% default × 8% severity is about 25 bps 🟡, if the 3.1% is annual and by dollars. The fund's statement doesn't say. This compares well with the library's own reference point of 5% default with 90% recovery, about 50 bps.
- **There is room to miss.** The target can fall about 117 bps before it drops below the low end of the 4-year hurdle (7.83%) 🟡. That is more than five times the historic loss rate, if the target already includes that loss.
- **The bear case is a pay-cut, not a capital loss.** LP return stays positive, but at about 6.9% the lock-up is no longer paid for. This assumes no fund-level leverage, which is undisclosed and would amplify every line.

**The LTV pair needs reconciling.** On the same loan, as-is LTV should be higher than ARV LTV, because ARV is the larger value. Here it's lower: 68% vs 72% implies as-is value about 6% above ARV, which doesn't make sense for a renovation loan 🟡. The likely explanation is different bases, such as initial advance over as-is and fully drawn commitment over ARV, or the two averages covering different loans. That reading would be ordinary, but it changes the cushion. If 68% is the initial advance only, as-is LTV rises as rehab draws fund, and the protection on a half-finished project is thinner than 68% suggests. Ask for both figures on one basis (`Q-RISK-04`).

**Recovery against LTV.** If defaulted loans sat at the 68% average, 92% recovery means net proceeds of about 63% of as-is value (0.92 × 0.68) 🟡. So either defaulted loans carried above-average LTV, or sale costs and value declines took about 37% of value. A 92% figure with visible losses is more believable than a claimed 100%, but it also shows the 32-point cushion isn't as thick as it looks.

---

## 3. Where LP Returns Come From

- **Cash flow: nearly all of it** 🟡. A loan book earns interest and origination points. The split isn't disclosed, but this is the structure of the asset class.
- **Exit: no terminal-value bet** 🟡. There's no exit cap or appreciation assumption, so `GEN-08` doesn't apply. Principal does depend on borrowers repaying through a sale or refinance, and when that market freezes the usual result is extensions, not immediate defaults. That's the mechanism to test in the default definition (`Q-RISK-05`).
- **Leverage: can't tell** 🔴. Fund-level leverage isn't disclosed, so I can't apply the >60% test to it. On the stated facts this doesn't read as a financing story: 9% net is reachable from the 11–13% gross common in the category with no leverage. `GEN-07` doesn't fire, but the question stays open (`Q-DS-02`, `Q-RISK-06`).

---

## 4. Fee Stack Summary

**Gross-to-net drag: at least 150 bps/yr on disclosed fees alone, falling to 100 bps/yr after the step-down.** The true total can't be computed from this disclosure, and that is the finding.

| Fee | Disclosed? | Terms | Library norm | Drag |
|---|---|---|---|---|
| Fund management fee | Yes 🟢 | 1.5%, then 1.0% | 1–2%, aggressive above 2.5%; step-down is LP-friendly | 150, then 100 bps |
| Fee base (AUM, committed, or invested) | No | Not stated | Matters most if on committed capital | Unknown |
| Servicing fee | No | Not stated | 0.25–0.5% of loan balance | Passed as 0 |
| Performance fee / carry | No | Not stated | 10–20% above a 5–8% hurdle, in some funds | Passed as 0 |
| Origination points | No | Not stated | 1–3 points; should flow to fund yield | Confirm who keeps them |
| Late fees / default interest | No | Not stated | Should go to the fund, not the GP | Confirm no GP "workout fee" |
| Admin / fund expenses | No | Not stated | 0.1–0.5% | Passed as 0 |
| Wind-down fee | No | Not stated | 0.5–1%, absent in most short-duration funds | Passed as 0 |

Calculator inputs: gross 10.5% (9% net plus the one disclosed fee, a floor rather than a stated figure 🟡), all undisclosed fees 0. Investment-period length isn't stated, so a blended figure isn't computable.

**Why the gaps matter.** Gross isn't stated either. If this fund earns the 11–13% gross common in the category, the gap to 9% net is 200–400 bps, against only 150 bps of disclosed fees. The other 50–250 bps goes to credit losses, idle cash, or fees not yet shown.

**Illustrative only, not a finding** 🔴: a top-of-norm stack (1.5% management, 0.5% servicing, 0.3% admin, 20% carry over 8% with full catch-up) would leave about 7.6% net at 12% gross and 8.45% at 13%. So that stack and a 9% net target together would require gross above the common range. The likelier reading is that the stack is lighter 🟡, which is what the full schedule should confirm.

---

## 5. Red Flags

**RED: none fired.**

**YELLOW:**

- **`GEN-16` (partial): incomplete fee schedule.** The library rates this YELLOW–RED. The headline fee, step-down, and a net target are given, so this is not the full "no fee disclosure" flag. The carry, servicing, and expense lines are missing, though, and an undisclosed carry could change how the 9% is earned. It must be resolved before committing, but it doesn't block diligence. (`Q-FEE-01`)
- **`GEN-11`: no distribution schedule.** A 9% target with no payment frequency or statement of whether it is an IRR or a cash yield. Exposure is low for an income fund, but it hides early cash drag during ramp-up and any wind-down lag. (`Q-DIST-01`)
- **`GEN-17`: essential disclosures partly absent.** The category baseline includes the foreclosure process and sponsor history through a downturn. Neither is described, and neither is a workout timeline. A 12-state book diversifies collateral risk but means running workouts under many states' foreclosure processes 🟡, and workouts are a craft skill. (`Q-RISK-05`)

**Cluster check.** The library treats a cluster of YELLOWs as a RED. These three don't compound that way: they're all gaps in a short summary, not separate structural problems, and one document set could close them. If the PPM doesn't close them, that reading changes.

**Checked and not fired:**

| ID | Why not |
|---|---|
| `HML-01` LTV on ARV only | As-is LTV is disclosed. The basis still needs reconciling (§2). |
| `HML-02` Geographic concentration | 12 states, 15% metro cap. |
| `HML-03` Default rate hidden | Disclosed, including stress periods. Definition still open. |
| `HML-04` Recovery hidden | Disclosed as realized. Workout timeline still open. |
| `HML-05` No step-down | Step-down disclosed. |
| `GEN-07` Financing story | Nothing stated points to it. Leverage unknown, so asked rather than fired. |
| `GEN-08` Exit-dependent IRR | No terminal-value assumption in a loan book. |
| `GEN-09` Debt maturity inside horizon | No fund debt disclosed. Asked, not assumed. |
| `GEN-13` No downside case | No forward sensitivity given, but through-cycle history is real downside evidence. Asked. |
| `GEN-01` Zero co-invest, `GEN-06` affiliate stacking, `GEN-05` / `GEN-14` track-record presentation, `GEN-02` regulatory history | Nothing stated either way, and silence isn't evidence of the flag. Each is a must-ask. |

No directives were embedded in the pasted text.

---

## 6. Missing Disclosures

**Category essentials (`01`).** Four of the five are at least partly there: LTV on both bases, default history, recovery rate, and geographic mix. That is why this gets a merits verdict.

Still missing from that baseline:

- Foreclosure process and workout timeline
- Sponsor identity and history through a downturn

**Normally disclosed for this type (`02`):**

- Full fee schedule: fee base, servicing, carry and hurdle, expenses, and who keeps points and default interest
- Gross yield and investment-period length

**Needed to rely on what was disclosed:**

- Definition behind the 3.1%: annual or cumulative, dollars or loan count, and whether extended or modified loans count
- Default and recovery by year, since an average can hide a spike in 2023, and a fast-growing book flatters the rate with new loans that haven't had time to default 🟡
- Actual A–D grade mix, plus how grades are assigned and how the mix has changed
- LTV on a single consistent basis
- Fund-level leverage or credit lines
- Loan count, average size, and largest borrower; lien position; property and borrower type
- Term, redemption rights, minimum, and raise size
- Whether the 9% is a target with any realized history behind it

---

## 7. GP Alignment

- **Co-invest:** not stated. Unverified.
- **Realized net-to-LP track record:** not provided. The 3.1% and 92% describe loan performance, not what LPs actually received, and both are self-reported. Unverified until tied to audited financials.
- **Waterfall:** none disclosed. If there is no carry, the GP earns on assets, not on results, which makes co-invest the main alignment test.
- **Affiliate fees:** not stated. In a lending platform, origination and servicing often sit with the sponsor 🟡, so this needs a direct answer.
- **Positives in what was shared:** a fee step-down, a realized recovery figure rather than marks, and explicit reference to the stress periods. Those are the right things to volunteer, but they don't substitute for verification.

---

## 8. Questions for the GP

**Must-ask**

| ID | Question | Bad-answer signal | Fired by |
|---|---|---|---|
| `Q-RISK-05` | "What is your historical default rate and realized recovery rate, including through 2020 and 2022–23?" Get it by year, in dollars, with workout timelines. Ask whether extended or modified loans count, and whether unsold foreclosed property is excluded from "realized." | "We've never had a loss"; silence on 2022–23; one number without the other; a blended since-inception figure with no annual view | `HML-03`, `HML-04`, `GEN-17` |
| `Q-RISK-04` | "What is the average portfolio LTV on as-is value, not just ARV?" Add: why is as-is below ARV, and what is as-is LTV on fully drawn balances? | Can't produce as-is on a consistent basis; "our borrowers always complete" | `HML-01` (basis) |
| `Q-FEE-01` | "Can you provide the complete fee schedule and the full distribution waterfall?" | "Standard market fees"; a partial list; "the PPM has it" without producing it | `GEN-16` |
| `Q-FEE-02` | "Which service providers are GP-affiliated, what do they charge, and are those rates third-party-benchmarked?" Include origination, servicing, and any workout fees. | "All arm's-length" without naming providers; no benchmark offered | `GEN-06` |
| `Q-GP-02` | "Can you restate your track record as net-to-LP IRR on fully-realized, exited deals only?" For this fund: realized net returns by year. | Offers only loan-level yield or GP-level IRR; "most deals are still performing" | `GEN-05`, `GEN-14` |
| `Q-GP-01` | "How much of your own capital is in this deal, on the same terms as LPs?" | "Our sweat equity is our investment"; a fee waiver rather than cash; a token amount on better terms | `GEN-01` |
| `Q-GP-03` | "Have you or your principals faced any regulatory action, enforcement, or investor litigation?" | "Nothing material"; a search surfaces something they didn't disclose | `GEN-02` |
| `Q-RISK-06` | "What is the fund's leverage ratio, and is the quoted LP IRR levered or unlevered?" (Bank label is credit-fund; the exposure is the same here, including a credit line.) | Won't disclose it; "leverage is conservative" with no number; a levered IRR shown as unlevered | `CREDIT-01` (off-route), `GEN-07` |
| `Q-DS-02` | "Strip out leverage — what is the unlevered, in-place return?" (Cap-rate language doesn't apply to a loan book.) | Treats the levered figure as the only one; no unlevered view exists | `GEN-07` |
| `Q-RISK-01` | If the fund borrows: "When does the debt mature relative to the projected hold, and what's the refinance or extension plan?" | Line matures inside the fund term; "we'll refinance" with no terms | `GEN-09` |
| `Q-DS-03` | "What is the return under a bear case?" For this fund: defaults and severity stressed, with no refinance market for borrowers. | "We underwrite conservatively" with nothing to show; the bear case is still 9% | `GEN-13` |
| `Q-DIST-01` | "What is the projected distribution schedule, and at what milestones does LP capital start returning?" | "We'll distribute when the deal supports it"; a target with no timing | `GEN-11` |
| `Q-LIQ-01` | "What are my options if I need to exit before the hold period ends?" Include redemption gates. | "We'll try to accommodate"; a vague promise of liquidity. An honest "there is none" is a good answer. | — |

**Must-ask only if a carry exists**

| ID | Question | Bad-answer signal | Fired by |
|---|---|---|---|
| `Q-FEE-04` | "What preferred return do LPs receive before the GP earns promote, and is it cumulative and compounding?" Library norm for this type: a 5–8% hurdle; no hurdle is aggressive. | Hurdle absent; non-cumulative | Off-route (`EQUITY-04`, `EQUITY-05`); norm from `02` |
| `Q-FEE-03` | "Is the waterfall deal-by-deal or whole-of-fund, and is there a clawback?" | Can't explain the catch-up; "you get paid when we get paid" | Off-route (`EQUITY-01`, `EQUITY-02`) |

**Nice-to-ask**

| ID | Question | Bad-answer signal |
|---|---|---|
| `Q-GP-04` | "How have your headcount and deal-monitoring capacity grown alongside AUM?" Workout staffing across 12 states is the part that matters. | "We're lean and efficient" as the whole answer; no named asset manager |
| `Q-DIST-02` | "When are capital calls expected, and what's the consequence of a missed or late call?" | "Calls as needed"; punitive dilution buried in the documents |
| `Q-LIQ-02` | "When will K-1s be delivered each year, and have you historically delivered them before the filing deadline?" | "As soon as we can"; a history of extensions |

---

## 9. Diligence Checklist

Third-party verification still needed:

- [ ] **PPM, LPA, and subscription documents:** full fees, fee base, term, redemption terms, and investment-period length
- [ ] **Audited fund financials, several years:** tie out the 3.1%, the 92%, and LP distributions; check how foreclosed property is valued
- [ ] **Loan tape:** LTV by loan on both bases, grade, state and metro, lien position, maturity, extensions, and largest borrowers
- [ ] **Appraisal sample:** who orders them, whether they're independent, and how as-is and ARV values compare with actual sale prices
- [ ] **Lien and title sample:** confirm "senior-secured" means first lien on the sampled loans
- [ ] **Background and regulatory:** principals, SEC filings and Form ADV if registered, state lending licenses, and litigation search
- [ ] **Fund lender:** credit-line agreement, if any, including covenants and maturity
- [ ] **Workout files:** two or three completed foreclosures from 2022–23, with timeline, cost, and final recovery
- [ ] **Tax and legal review:** your own advisers, including state filing exposure from a 12-state book

---

## 10. Verdict

**Pursue.**

*Screening output only, not investment advice.*

**Reasoning.** On the stated facts this looks like a properly built bridge fund:

- **Cushion:** 68% as-is LTV, with both bases disclosed. That avoids the main way debt funds mislead, which is quoting ARV only.
- **Loss history:** about 25 bps a year if the 3.1% is annual, with stress periods included.
- **Diversification:** 12 states and a 15% metro cap.
- **Fees:** 1.5% is mid-range and steps down.
- **Return:** 9% net is in the category range and clears the illiquidity hurdle at every lock-up tested.

No RED fired, and the three YELLOWs are gaps in a summary, not structural defects. The return is modest by design. This is a credit-income position, so there's no upside to rescue it if credit goes wrong.

**Biggest swing factor: whether the 3.1% and 92% hold up under their definitions.** The whole case rests on them. If extended or modified loans are excluded, or unsold foreclosed property is left out of "realized," or the 2023 figure is far above the average, the real loss rate could be several times what it appears. At 4 years, the fund's spread over the hurdle is thin enough to matter: about 117 bps of slippage takes it below the low end of the band.

**Conditions before committing capital.** These are residual gaps, not reasons to pass. Any one of them failing should reopen the verdict:

1. Default and recovery data ties to audited financials by year, with extensions and foreclosed property treated honestly.
2. The LTV pair reconciles, and as-is LTV on fully drawn balances still leaves a real cushion.
3. The full fee schedule shows how 9% net is reached, with any carry above a hurdle and points and default interest flowing to the fund.
4. Fund-level leverage is none or modest (the library's private-credit warning line is above 1.5× equity), and the 9% isn't dependent on it.
5. The GP has cash co-invested on the same terms and a clean background check.
6. Realized net-to-LP returns exist and are near the target, not just a forward target.
7. Term and redemption rights fit your liquidity. At about 7 years or longer, the premium no longer clears comfortably.

**Who it suits.** An income-focused LP who can leave capital locked for the full fund term, wants senior-secured real estate credit, and accepts capped upside. It doesn't suit anyone who may need the money early, or who expects equity-like returns. Over the trailing decade SPY returned 15.39%, so this position is for income and downside protection, not for growth.

**What would have to be true:** the book performs near its stated history, the 9% is earned from loan yield rather than leverage, and the GP's records match its summary.
