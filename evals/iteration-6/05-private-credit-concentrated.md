# Eval fixture 05
*Iteration-6 run, 2026-11-01, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 436a76b.*

**Verdict: Pursue with conditions.** The 12% clears its public hurdle on paper, but it is a levered number on a concentrated book, so it earns more diligence and not a commitment until the unlevered return, the loss history and the credit facility terms are on the table.

*Screening output only, not investment advice.*

Confidence tags: 🟢 stated or from a reference, 🟡 inferred, 🔴 assumed or unverifiable.

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class / deal type | Private credit fund 🟢 |
| Sponsor | Not stated |
| Geography | Not stated |
| Minimum | Not stated |
| Hold / fund term | Not stated (category norm 3–7 years) |
| Raise / fund size | Not stated |
| Claimed return | 12% net IRR to investors 🟢; whether target or realized is not stated |
| Fund leverage | ~2.5x 🟢; basis not stated (debt-to-equity or assets-to-equity) |
| Concentration | ~60% of the loan book in one sector 🟢; sector not named |
| Management fee | 2% 🟢; fee base not stated |
| Loan position | Senior secured 🟢 |

## 2. Return Stress-Test

**Against the public hurdle.** The 12% net IRR exceeds HYG's 4.83% 10-year return by about 717 bps. For a 3–7 year lock-up the illiquidity hurdle is about 300–600 bps, so the headline clears at every hold in the range (`benchmark_comparator.py`). 🟢 The spread over Treasuries is about 680–715 bps (10-year 5.18%, 2-year 4.87%). The 12% also sits at the very top of the 8–12% category range. 🟢

**Why that test flatters this fund.** HYG is unlevered and diversified, and this fund is neither, so the 717 bps is not a like-for-like premium. A fairer test asks what the loan book earns before fund debt.

The arithmetic, reading 2.5x as debt-to-equity (assets are 3.5x equity):

`Net to LP = 3.5 × book return after losses − 2.5 × facility cost − fee`

The facility cost is not disclosed. I used 7% as a placeholder, tested 6–8%, and treated the 2% fee as charged on equity with no carry. 🔴

| Case | Swing assumptions | Net to LP | Over HYG | Against the hurdle |
|---|---|---|---|---|
| Bull | Credit losses 25 bps lower, facility 50 bps cheaper | ~14.1% | ~929 bps | Clears |
| Base (as quoted) | Book earns ~9.0% after losses, facility 7% | 12.0% | ~717 bps | Clears |
| Bear | Credit losses 100 bps higher per year, facility 100 bps dearer | ~6.0% | ~117 bps | Fails |
| Same book, no fund leverage | Back-solved book return (8.3–9.7%) less the 2% fee | ~6.3–7.7% | ~146–288 bps | Fails ~300–400 bps |

These swings need no exit assumption and are large because of the multiplier: each 100 bps of credit loss costs LPs 350 bps, and each 100 bps of facility cost costs them 250 bps. 🟡

If 2.5x means assets-to-equity (1.5x debt-to-equity), the unlevered line becomes ~7.2–8.4%, or ~237–357 bps over HYG, which only touches the bottom of the hurdle. Either way, **the premium looks like it comes mostly from leverage rather than from getting paid for illiquidity.** That reading rests on the assumed facility cost, so it is a must-ask and not a finding. 🔴

**Loss math, using only the stated terms and the 60–80% recovery norm:** 🟡

| Event | Hit to LP equity (2.5x debt-to-equity) | On the 1.5x reading |
|---|---|---|
| 3.4% loss on total assets (5.7% on the concentrated sector) | Erases one full year's 12% | 4.8% of assets (8.0% of the sector) needed |
| 14–29% of sector loans default at 60–80% recovery | Same: one year's return gone | 20–40% of sector loans |
| 30% of sector loans default at 60% recovery (7.2% of assets) | About −25% | About −18% |
| 28.6% decline in asset value | Equity at zero | 40% decline needed |

For scale, HYG's worst peak-to-trough drop was −34% in 2008. 🟢 That is a price move on a different book and not a realized loss, but it shows a credit-wide mark can exceed the 28.6% cushion. `05` also warns that private-credit marks are smoothed, so any low reported volatility understates this risk.

**Likely failure mode.** Defaults cluster in the 60% sector and marks fall. That trips the facility's coverage test, the lender cuts its advance rate or sweeps cash, and distributions stop while the fund sells loans into the same weak market. 🔴 Facility terms are unseen, so this needs confirming.

## 3. Where LP Returns Come From

- **Cash flow:** Presumably loan interest, which is what a senior secured book should produce. The split between cash and accrued interest is not stated. 🔴
- **Exit:** There is no cap-rate or terminal-value story here, so `GEN-08` does not fire on what's disclosed. No distribution schedule was given, so this can't be fully confirmed (`GEN-11`).
- **Leverage:** About 36–48% of the 12 points on the placeholder 6–8% facility cost, or 30–40% on the 1.5x reading. 🔴 That is below the 60% line, but the input is assumed, so I can't call this a financing story (`GEN-07`) either way. Leverage is clearly doing real work: at 7%, the lender takes 17.5 of the 31.5 points of book income on LP equity. 🟡

**"Senior secured" describes the loans, not your position.** The facility lender sits ahead of you, and you hold the equity beneath it. The Low-Med risk tier that `01` gives senior secured credit does not carry over to an LP behind this much fund debt. 🟡

## 4. Fee Stack Summary

**Gross-to-net drag: 200 bps disclosed. That is a floor, and the true total can't be computed from this disclosure, which is itself the finding.** (`fee_drag_calculator.py`: 14% implied gross, undisclosed fees passed as 0, 5-year hold assumed. Hold has no effect here because no one-time fees are disclosed.)

| Layer | Status | Norm (`02`) | Drag or note |
|---|---|---|---|
| Management fee | 2% stated 🟢 | 1–2%; aggressive above 2% | 200 bps if charged on equity. Top of range, not over the line |
| Fee base | Not stated | Committed, then invested capital | **If on gross assets, 2% × 3.5 = ~700 bps of equity** and implied gross is 19% 🟡 |
| Step-down | Not stated | Industry standard after the investment period | Absence is a flag (`HML-05`) |
| Performance fee / carry | Not stated | 10–20% over a 5–7% hurdle | Illustration only: 15% over 6% with full catch-up adds ~190 bps, for ~390 bps total on ~16% gross 🔴 |
| Hurdle type | Not stated | Hard is LP-favorable; soft with 100% catch-up is aggressive | Unknown |
| Servicing | Not stated | 0.25–0.5% of loan balance | On a loan book 3.5x equity, ~88–175 bps of equity if charged 🟡 |
| Fund leverage cost | Not stated | Variable; compounded credit risk above 1.5x equity | The largest unknown line in the return |
| Admin / IR | Not stated | $1–3k per LP or 0.1–0.3% | Unknown |
| Feeder wrapper | Not stated | Adds 50–150 bps if accessed through one | Confirm how you would be investing |

Also confirm that the 12% is net of all of the above. A "net" figure that excludes carry or fund expenses would not be net.

## 5. Red Flags

**RED**
- **`CREDIT-01` Fund leverage stacked on the loan book.** ~2.5x is above the 1.5x level `02` treats as compounded credit risk (on the assets-to-equity reading it is 1.5x, right at the line). LP exposure: losses reach equity at 2.5–3.5x, and the 12% is by construction a levered figure. 🟢 (`GEN-07` financing-story family: cited, not fired on its own, because measuring it needs the undisclosed facility cost and unlevered return.)

**YELLOW–RED (treated as RED until answered)**
- **`HML-03` / `HML-04` Default and recovery rates not disclosed.** Applies through `Q-RISK-05`. LP exposure: with this much leverage, realized loss is the whole question, and neither input is given. 🟢
- **`GEN-16` Fee and waterfall disclosure incomplete.** Only the management fee is given, so drag is unknowable. 🟢
- **`GEN-15` Financials missing.** No loan tape, fund financials or facility terms. 🟢

**YELLOW**
- **`CREDIT-02` Sector concentration.** ~60% in one unnamed sector means correlated defaults, which diversification was supposed to dampen. 🟢
- **`HML-05` No step-down disclosed.** A flat 2% through wind-down drags net as the book runs off. 🟡
- **`GEN-11` IRR with no distribution schedule.** Timing of capital return is hidden. 🟢
- **`GEN-13` No downside case.** A single-point 12% conceals fragility, and leverage makes that fragility worse. 🟢
- **`GEN-17` Essential category disclosure absent.** Loan count and average loan size are missing. 🟢

**Cluster:** `CREDIT-01` + `CREDIT-02` is the core problem. Each is manageable alone, but together one sector downturn can reach LP equity at a multiple. I read the pair as RED.

**Not fired, still open (nothing disclosed either way):** `GEN-01` co-invest, `GEN-02` regulatory history, `GEN-05` / `GEN-14` track record, `GEN-06` affiliate fees, `GEN-09` facility maturity, `GEN-10` rate hedging, `HML-01` LTV basis (only relevant if the book is real-estate-backed), `HML-02` geographic mix. `GEN-08` does not apply on the stated terms.

The 2% fee and the senior secured position are not flags in themselves.

## 6. Missing Disclosures

**Essential for private credit (`01`):**
- Loan count and average loan size
- Which sector holds the 60%, and the rest of the sector mix
- Historical default and recovery rates, preferably through-cycle

Fund leverage, seniority and part of the sector mix were disclosed, which is why this gets a merits verdict and not an insufficient-disclosure Pass.

**Fees (`02`):** Fee base, step-down, carry, hurdle type and catch-up, servicing, admin, fund expenses.

**Needed to read the return:**
- Leverage basis, facility cost, maturity, covenants and recourse
- Unlevered and gross return
- Whether 12% is a target or realized
- Distribution schedule, fund term, redemption or exit rights

**Sponsor:** Identity, track record, co-invest, regulatory history.

**Assumed inputs in this report, all replaced once disclosed:** 5-year hold in the scripts (tested 3 and 7), 7% facility cost (tested 6–8%), 2% fee charged on equity, 2.5x as debt-to-equity (other reading shown), and the illustrative carry in §4.

## 7. GP Alignment

Can't tell from this. All of it is unverified. 🔴

- **Co-invest:** Not stated. Cash and pari-passu are the test.
- **Track record:** None presented. A quoted 12% is not a realized net-to-LP record, and until one is shown there is no validated record.
- **Waterfall:** Not stated.
- **Affiliate fees:** Not stated.
- **Incentive to watch:** If the 2% is charged on gross assets, the GP earns more by adding leverage, whatever LPs end up with. 🟡

## 8. Questions for the GP

**Must-ask**

| ID | Question | Bad-answer signal |
|---|---|---|
| `Q-RISK-06` | What is the fund's leverage ratio, and is the quoted LP IRR levered or unlevered? (Add: debt-to-equity or assets-to-equity?) | Won't disclose it; presents a levered IRR as if unlevered; "leverage is conservative" with no number. |
| `Q-DS-02` | Strip out leverage: what is the unlevered, in-place return on the loan book? | Treats the levered IRR as the only relevant figure; no unlevered view exists; "leverage is just how the deal works." |
| `Q-RISK-05` | What is your historical default rate and realized recovery rate, including through 2020 and 2022–23? (Add: for this sector specifically.) | Default without recovery or the reverse; "we've never had a loss"; silence on 2022–23. |
| `CREDIT-02` response (no `04` entry) | What is the sector breakdown of the portfolio, and your single-largest-sector exposure? Is there a cap? | Analyst-written signal: won't name the sector, or describes a broad label such as "specialty finance" that hides the underlying exposure. |
| `Q-DS-03` | What is the return under a bear case? (Adapted: higher sector defaults, lower recovery, facility repriced or not renewed.) | A single-point pro forma; "we underwrite conservatively" with nothing to show; the bear case is still a gain. |
| `Q-RISK-01` | When does the debt mature relative to the fund's term, and what's the refinance or extension plan? (Add: what happens on a covenant breach?) | Maturity falls inside the term; "we'll refinance" with no terms; no plan if the market is shut. |
| `Q-RISK-03` | Can you provide trailing-twelve-month actuals and complete debt terms? (Adapted: loan tape in place of a rent roll.) | Partial periods only; tape withheld; "the financials are confidential until you commit." |
| `Q-FEE-01` | Can you provide the complete fee schedule and the full distribution waterfall? (Add: what is the 2% charged on?) | "Standard market fees"; a partial list; "the PPM has it" without producing it. |
| `Q-FEE-03` | Is the waterfall deal-by-deal or whole-of-fund, and is there a clawback? | Can't explain the catch-up; "you get paid when we get paid." |
| `Q-FEE-04` | What return do LPs receive before the GP earns carry, and is it cumulative and compounding? (Adapted: hurdle in place of pref.) | Below market or absent; non-cumulative. |
| `HML-05` response (no `04` entry) | Does the management fee step down after the investment period? | Analyst-written signal: "the fee is competitive" with no yes or no; a step-down that only moves the base. |
| `GEN-17` response (no `04` entry) | How many loans are in the book, what is the average size, and what are the largest positions? | Analyst-written signal: gives a count of borrowers' facilities without position sizes. |
| `Q-DIST-01` | What is the projected distribution schedule, and at what milestones does LP capital start returning? | "We'll distribute when the deal supports it"; an IRR with no timing. |
| `Q-GP-01` | How much of your own capital is in this deal, on the same terms as LPs? | "Our sweat equity is our investment"; a fee waiver instead of cash; token amount on better terms. |
| `Q-GP-02` | Can you restate your track record as net-to-LP IRR on fully-realized deals only? | Only project- or GP-level IRR; "most deals are still performing"; can't separate realized from marked. |
| `Q-GP-03` | Have you or your principals faced any regulatory action, enforcement, or investor litigation? | "Nothing material"; blames the regulator; a search finds what they didn't mention. |
| `Q-FEE-02` | Which service providers are GP-affiliated, what do they charge, and are those rates third-party-benchmarked? | "All arm's-length" without naming anyone; no benchmark. |
| `Q-LIQ-01` | What are my options if I need to exit before the hold period ends? | "A secondary market may develop"; "we'll try to accommodate." An honest "there is none" is a good answer. |

**Nice-to-ask**

| ID | Question | Bad-answer signal |
|---|---|---|
| `Q-RISK-02` | If the facility floats, what hedge is in place, when does it expire, and what does it cost to extend? | Expires before maturity; cost not modeled; "rates should be lower by then." |
| `Q-DS-01` | What share of LP IRR comes from current cash versus the end of the fund? (Adapted: cash versus accrued interest.) | Can't or won't decompose the IRR. |
| `Q-GP-04` | How have headcount and monitoring capacity grown alongside AUM? | AUM multiplied while the team stayed flat; no named owner. |
| `Q-DIST-02` | When are capital calls expected, and what's the consequence of a missed call? | "Calls as needed"; punitive dilution buried in the docs. |
| `Q-LIQ-02` | When will K-1s be delivered each year? | "As soon as we can"; a history of extensions. |

## 9. Diligence Checklist

Third-party verification still needed:

- [ ] PPM and LPA: fee base, carry, step-down, term, redemption rights, and whether the LP can face a capital call to cure a facility breach
- [ ] Credit facility agreement: advance rates, coverage tests, cash sweep, maturity, recourse, lender's rights on default
- [ ] Audited fund financials and the valuation policy, including who independently marks the loans
- [ ] Loan tape: position sizes, lien position, collateral value, non-accruals, amended or extended loans
- [ ] Independent read on the named sector's default outlook
- [ ] Background and regulatory checks on the GP and principals, including Form ADV Part 2 if the manager is an RIA
- [ ] Reference call with an existing LP in a fund that has fully returned capital
- [ ] Confirmation from the lender or administrator of the current leverage figure

## 10. Verdict

**Pursue with conditions.**

*Screening output only, not investment advice.*

**Reasoning.** The headline is not unreasonable: 12% is within the category range and clears HYG plus the illiquidity hurdle by a wide margin, and the 2% fee is in range. Enough is disclosed to see the risk shape, so this isn't an insufficient-disclosure Pass. But the two most important stated terms work against each other. About 2.5x leverage (`CREDIT-01`) means a loss of about 3.4% on assets costs a year of return, and 60% in one sector (`CREDIT-02`) makes that size of loss more plausible. With no default or recovery history, no unlevered return and no facility terms, nothing shown yet says the 12% survives a sector downturn.

**Biggest swing factor:** the loan book's return after losses and before fund debt. On placeholder inputs it looks like 6.3–7.7% net unlevered, which would not clear HYG plus the hurdle. If that holds up with real numbers, the premium is mostly leverage.

**Conditions (a refusal or bad answer on 1–3 turns this into a Pass):**
1. **Unlevered net return is shown and clears the hurdle:** roughly 7.8–8.8% for a lock-up up to 5 years (HYG plus 300–400 bps), and 8.8–10.8% at 7 years (`Q-DS-02`).
2. **Through-cycle default and recovery data are provided, including 2020 and 2022–23 and the named sector.** The fund should credibly stay well short of 14–29% sector defaults at 60–80% recovery, the band that erases a year of return (`Q-RISK-05`).
3. **Facility terms are clean:** leverage basis confirmed, maturity beyond the fund term, and a coverage test that a downturn in one sector doesn't trip into forced selling or an LP capital call (`Q-RISK-06`, `Q-RISK-01`).
4. **Full fee schedule is delivered:** fee not charged on gross assets, a step-down exists, carry has a real hurdle, and 12% is confirmed net of all of it (`Q-FEE-01`).
5. **Realized net-to-LP record, cash co-invest and a clean regulatory check are confirmed** (`Q-GP-01`, `Q-GP-02`, `Q-GP-03`).

**What would have to be true.** The book earns about 9% or better after real losses, the sector's loss history is benign through stress, and the lender can't force a sale at the bottom. If so, 12% is fair pay for the risk.

**Who it suits.** An LP who would size this as levered, equity-like credit risk, doesn't need the money for the full term, and has little other exposure to that sector. It does not suit someone looking for a bond-like income holding because of the "senior secured" label.

---
Benchmarks: ETF returns to 2026-06-30, Treasury closes 2026-09-24 (`05`, stamped 2026-09-27).
