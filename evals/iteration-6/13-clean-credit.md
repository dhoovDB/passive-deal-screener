# Eval fixture 13
*Iteration-6 run, 2026-11-01, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 436a76b.*

**Verdict: Pursue with conditions.** A sound structure with no RED flags: leverage, diversification, loss history and both return bases are disclosed. The conditions are the numbers and terms your summary describes but does not give.

*Screening output only, not investment advice.*

Confidence tags: 🟢 stated or from a reference, 🟡 inferred or arithmetic on stated facts, 🔴 assumed or unverifiable.

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Private credit (fund) 🟢 |
| Deal type | Private credit, BDC-style 🟢 |
| Sponsor | Not stated |
| Geography | Not stated |
| Minimum | Not stated |
| Hold / lock-up | Not stated (`01` norm for the class: 3–7 yrs) |
| Raise | Not stated ("large") |
| Claimed return | Net IRR stated levered, with the unlevered figure also shown 🟢. **Neither value was in the material provided.** |
| Management fee | 1.5% of gross assets; 1.0% on assets below the 200% asset-coverage threshold 🟢 |
| Incentive fee | Two-part, with a hurdle and a high-water mark 🟢. Rates and hurdle level not stated. |
| Leverage | ~1.1x debt to equity, about 191% asset coverage (2.1 / 1.1) 🟢/🟡 |
| Portfolio | 400+ loans across sectors 🟢 |
| Loss history | Through-cycle default and recovery rates disclosed 🟢. Values not provided. |

## 2. Return Stress-Test

The stated net IRR was not provided, so these cases use the `01` range for the class (8–12% net) as a placeholder. 🔴 Replace the base case with the fund's figure. No verdict rests on these placeholder returns.

**Swing assumptions, per 100 bps, on a book of 2.1x NAV** 🟡
- Annual credit loss on assets: -210 bps of pre-fee return on NAV.
- Asset yield (spread compression or lower base rates on floating loans): -210 bps.
- Cost of the fund's debt: -110 bps per +100 bps.

| Case | Net to LP | How it is built | Over HYG (4.83%) | 5-yr lock-up (hurdle ~300–400 bps) | 7-yr lock-up (hurdle ~400–600 bps) | Over 2yr Treasury (4.87%) |
|---|---|---|---|---|---|---|
| Bull 🔴 | 12.0% | Top of `01` range | +717 bps | Clears comfortably | Clears comfortably | +713 bps |
| Base 🔴 | 10.0% | Midpoint of `01` range | +517 bps | Clears comfortably | Clears, thin | +513 bps |
| Low end 🔴 | 8.0% | Bottom of `01` range | +317 bps | Clears, thin | Thin / fails | +313 bps |
| Bear 🔴 | ~6.3% | Base, less 150 bps more annual credit loss on assets (-315 bps; for example 5% defaults at 70% recovery, inside the `01` 60–80% band), less 50 bps more debt cost (-55 bps), before any incentive-fee relief | +147 bps | Thin / fails | Thin / fails | +143 bps |

(`benchmark_comparator.py`, private-credit type; lock-up assumed at both lengths because none was stated.)

**The pass lines, once you have the number** 🟢/🟡
- Lock-up of 5 years or less: stated net IRR must reach **7.83–8.83%**.
- 7-year lock-up: **8.83–10.83%**.
- At this snapshot the Treasury is the tighter floor: the 2yr (4.87%) and 10yr (5.18%) both out-yield HYG's trailing 10yr return. `05` places the true 3–7yr floor between those two points.

**Comparator mismatch** 🟡
HYG is an unlevered basket; this fund carries 1.1x on top of its loans. A levered net IRR against HYG flatters the fund. The cleaner test is the **unlevered** figure against HYG and the Treasury (§3).

**Failure mode: marks, not coupons** 🟡
- At 1.1x, a 10% markdown on assets takes NAV down 21% and leverage to 1.39x.
- A 12.7% markdown takes leverage to 1.5x, the `02` line for compounded credit risk.
- A 2008-scale fall matching HYG's worst drop (-34%) would take NAV down about 71% and leverage to about 3.85x. That is a tail case, and a senior loan book may behave differently from HYG. It does show what the leverage does to the LP's position in a credit-market break.
- `05` also warns that private-credit vehicles report smoothed marks, so reported volatility understates this risk.

## 3. Where LP Returns Come From

| Source | Read |
|---|---|
| Cash flow | Loan coupon income is the likely primary driver for a lending book. 🟡 The split between coupon, fees and gains is not stated. |
| Exit / terminal value | No cap-rate or sale thesis in a diversified loan book. `GEN-08` does not fire on the facts given. 🟡 |
| Leverage | Material by construction, and **measurable here because both bases are shown**. |

**Test for the >60% rule** 🟡
Leverage share = (levered net − unlevered net) / levered net. It trips 60% only if the unlevered figure is below 40% of the levered figure. At a 10% levered net, that means an unlevered net below 4%, which is under both HYG and the 2yr Treasury. This takes one line to check once you have the two numbers. Fire `GEN-07` and `CREDIT-01` if it trips; do not fire them before then.

**Check that the unlevered figure is on the same basis** 🔴
It must be net of fees too, or the comparison is gross against net. An unlevered fund would pay 1.5% of NAV, not about 3.1%, so ask how the fee was restated.

**What leverage must earn** 🟡
Each borrowed dollar pays debt cost plus a 1.5% management fee on the first 1.0x (1.0% above it). It adds to LP return only if asset yield less credit losses exceeds that combined cost, before the incentive fee. The debt cost is not disclosed. The `05` NCREIF overlay is real-estate data and is not used here; the fund's own unlevered figure is the correct baseline.

## 4. Fee Stack Summary

**Gross-to-net drag: about 490 bps/yr of NAV (illustrative). Only 310 bps of that is computable from disclosure.** The incentive rate, hurdle level and catch-up were not given, so the total is an estimate and that gap is the finding.

| Fee | Terms | Against `02` | Drag on NAV |
|---|---|---|---|
| Management fee | 1.5% on gross assets; 1.0% tier below 200% coverage 🟢 | Headline in the 1–2% range, but `02` quotes that range on committed or invested capital, not gross assets | **310 bps/yr** 🟡: 2.0x NAV × 1.5% + 0.1x NAV × 1.0% |
| Incentive fee | Two-part; hurdle and high-water mark 🟢; rates not stated | `02`: 10–20% over a 5–7% hurdle; aggressive above 25% or hurdle below 5%; soft hurdle with 100% catch-up is aggressive | 77–241 bps/yr 🔴 (see below) |
| Time-based step-down | Not stated | `02`: absence is a flag | Unknown |
| Servicing | Not stated | 0.25–0.5% of loan balance | Passed as 0; a gap |
| Admin / IR | Not stated | $1–3k per LP or 0.1–0.3% of capital | Passed as 0; a gap |
| Fund debt cost | Not stated | *Variable* | Treated as already inside the pre-fee return; a gap |
| Feeder / wrapper | Not stated | 50–150 bps/yr if present | Verify separately |

**The fee-base finding** 🟡
The 1.5% headline is about 3.1% of the LP's equity. On assets it blends to about 148 bps, which is in range. Measured on the LP's capital it sits above the 2% aggressive line, though that line is set on a different base, so this is a real cost rather than an automatic breach. The 1.0% tier is LP-favorable because it reduces the pay for the last slice of leverage. The fee still grows with borrowed assets, so the manager is paid more for adding leverage whether or not it adds to LP return.

**Illustrative runs** (`fee_drag_calculator.py`: 15% pre-fee return on NAV 🔴, 5-yr hold 🔴, unstated fees passed as 0, incentive terms 🔴 from the `02` ranges)

| Incentive terms | Promote | Total drag | Net to LP |
|---|---|---|---|
| Not counted (the disclosed floor) | 0 bps | 310 bps/yr | 11.90% |
| 10% over 7%, no catch-up | 77 bps | 387 bps/yr | 11.13% |
| **15% over 6%, full catch-up** | **179 bps** | **489 bps/yr** | **10.11%** |
| 20% over 5%, full catch-up | 241 bps | 551 bps/yr | 9.49% |

The model is additive and uses a bullet exit, so it slightly overstates drag against a fee paid on income quarterly. Every 🔴 input above is a §6 gap.

## 5. Red Flags

**RED: none.**

**YELLOW**
- **`GEN-11` Distribution timing not disclosed.** 🟢 A net IRR is quoted with no distribution schedule. The LP cannot tell how much arrives as current income versus at the end, or whether two funds at the same IRR are comparable.
- **`GEN-17` Essential category disclosure absent.** 🟢 `01` lists seniority position and average loan size for this class; neither is stated. "400+ loans" does not say where those loans sit in the capital stack. A second-lien book at 1.1x fund leverage is a different risk from a first-lien one, and the `01` Low-Med risk tier and 60–80% recovery band assume senior secured.

These two are unrelated and do not form a cluster.

**Fee-stack finding with no library ID:** the gross-asset fee base (§4). It is reported as a cost and an incentive issue, not as a flag.

**Checked and did not fire**

| ID | Read |
|---|---|
| `CREDIT-01` Fund leverage stacked on loan leverage | 1.1x is below the `02` 1.5x line, and the IRR is labeled levered with the unlevered figure shown. 🟢 This is the good answer to the flag's question. Re-opens only if the §3 test trips. |
| `GEN-07` Financing story | No cap-compression thesis; leverage is disclosed and measurable. 🟡 Same §3 test. |
| `GEN-08` Exit-dependent IRR | Lending income, no terminal-value thesis. 🟡 |
| `CREDIT-02` Sector concentration | 400+ loans across sectors. 🟢 Largest-sector share still worth getting. |
| `HML-03`, `HML-04` Default / recovery not disclosed | Both disclosed, through-cycle. 🟢 Values and the 2020 and 2022–23 periods still to be read. |
| `GEN-16` No fee or waterfall disclosure | Structure is disclosed; rates are missing. Partial gap handled as a condition, not fired. |

**Open: cannot tell from this, so not fired** (each is a §8 must-ask)
- `GEN-01` co-invest
- `GEN-02` regulatory or litigation history
- `GEN-05`, `GEN-14` whether the net IRR is realized and net-to-LP
- `GEN-06` affiliate fees
- `GEN-09`, `GEN-10` maturity and rate terms on the fund's own debt
- `HML-05` time-based fee step-down

`HML-01` applies only if the book lends against real estate; the summary does not say.

## 6. Missing Disclosures

**Provided against the `01` private-credit baseline:** loan count, sector diversification (at summary level), fund leverage ratio, through-cycle default and recovery rates.

**Omitted from the `01` baseline**
- Seniority position
- Average loan size

**Omitted from the `02` fee stack**
- Incentive rate on each of the two parts
- Hurdle level, soft or hard, and catch-up rate
- Whether the high-water mark covers both parts
- Any time-based management-fee step-down
- Servicing, admin and affiliate fees
- Cost of the fund's debt

**Described but values not provided**
- Levered and unlevered net IRR, and their fee basis
- Default and recovery rates

**Other**
- Sponsor, geography, minimum, raise, vintage
- Lock-up and redemption terms
- Distribution schedule
- Maturity and fixed or floating mix of fund debt
- GP co-invest and realized track record

**ASSUMED inputs in this report, each from the gaps above:** net IRR, lock-up, pre-fee return, incentive terms.

## 7. GP Alignment

- **Co-invest:** Not stated. Unverified. 🔴
- **Track record:** Not stated. The net IRR is **unverified** until shown as realized and net-to-LP. A figure resting on marks counts as no track record, and this class's marks are smoothed (`05`). 🟢/🔴
- **Incentive alignment:** A hurdle and a high-water mark are the LP-favorable features, and `02` treats the high-water mark as usual for this class. 🟢 Whether they bite depends on terms not given. If the high-water mark or a lookback does not cover the income part, the manager can collect income incentive on accrued interest while credit losses reduce NAV. 🟡
- **Fee-base alignment:** Mixed. A gross-asset base pays for size and leverage; the 1.0% tier moderates this. 🟡
- **Affiliate fees:** Not stated. Origination, servicing or structuring income kept by the manager rather than the fund would be a layer the §4 drag misses. 🔴

## 8. Questions for the GP

**Must-ask**

| ID | Question | Bad-answer signal |
|---|---|---|
| `Q-FEE-01` (`GEN-16`) | Provide the complete fee schedule, including both incentive parts, hurdle, catch-up, and servicing and admin. | "Standard market fees"; a partial list; "the PPM has it" without producing it. |
| `Q-FEE-04` | What is the hurdle rate, and does a shortfall carry forward? | Hurdle below the `02` range or absent; shortfalls that don't carry forward. |
| `Q-FEE-03` | What protects LPs if later losses follow incentive already paid: does the high-water mark cover both parts, and is there a clawback? | Can't explain the catch-up; "you get paid when we get paid." |
| `Q-RISK-06` (`CREDIT-01`) | Answered as described. Confirm the leverage ratio and show both IRR bases on the same net-of-fee footing. | "Leverage is conservative" with no number; the unlevered figure turns out to be gross. |
| `Q-DS-02` (`GEN-07`) | What is the unlevered return, in numbers, with the debt cost? | Treats the levered IRR as the only relevant figure; "leverage is just how the deal works." |
| `Q-DS-01` (`GEN-08`) | What share of net IRR is coupon income versus gains, fees and marks? | Can't or won't decompose the IRR. |
| `Q-DS-03` (`GEN-13`) | What is the return in a bear case: higher defaults, lower recoveries, costlier debt? | A single-point projection; "we underwrite conservatively" with nothing to show; a bear case that is still a gain. |
| `Q-RISK-05` (`HML-03`, `HML-04`) | Answered as described. Show default and realized recovery with workout timelines, through 2020 and 2022–23. | One number without the other; "we've never had a loss"; silence on 2022–23. |
| `Q-RISK-01` (`GEN-09`) | When does the fund's debt mature against its loan book, and what is the refinance or extension plan? What covenant or asset-coverage minimum applies, and how much cushion is there? | "We'll refinance" with no terms; no plan if credit markets are shut. |
| `Q-RISK-03` (`GEN-15`) | Provide complete debt terms and trailing-twelve-month fund financials. Adapted: no rent roll in a loan fund. | Trailing 3- or 6-month only; "confidential until you commit." |
| `GEN-17` question, per `01` | What is the seniority mix, first-lien share and average loan size? | "Senior" with no first-lien / second-lien split; an average that hides a few large positions. Inferred dodge; `04` has no row for this. |
| `HML-05` question, per `02` | Does the management fee step down over time? | Treats the leverage tier as if it were the step-down. Inferred dodge; `04` has no row for this. |
| `Q-DIST-01` (`GEN-11`) | What is the distribution schedule, and how much of it is covered by income? | "We'll distribute when the deal supports it"; an IRR quoted with no timing. |
| `Q-LIQ-01` | What are my options if I need out before the lock-up ends? Is there a gate or a cap on redemptions? | "A secondary market may develop"; "we'll try to accommodate." An honest "there is none" is a good answer. |
| `Q-GP-01` (`GEN-01`) | How much of your own capital is in, on LP terms? | "Sweat equity"; a fee waiver presented as cash; a token amount on better terms. |
| `Q-GP-02` (`GEN-05`, `GEN-14`) | Restate the record as net-to-LP on realized investments only. | Project-level figures only; "most loans are still performing"; can't separate realized from marked. |
| `Q-GP-03` (`GEN-02`) | Any regulatory action, enforcement or investor litigation? | "Nothing material"; a search surfaces something undisclosed. |
| `Q-FEE-02` (`GEN-06`) | Which providers are affiliated, what do they charge, and who keeps origination fees? | "All arm's-length" without naming providers; no benchmark. |

**Nice-to-ask**

| ID | Question | Bad-answer signal |
|---|---|---|
| `Q-GP-04` | How has the team grown against AUM, given 400+ loans to monitor? | AUM multiplied with a flat team; "lean and efficient" as the whole answer. |
| `Q-RISK-02` (`GEN-10`) | If the fund's debt is floating and hedged, when do hedges expire against maturity? | Hedges expire first; "rates should be lower by then." |
| `Q-DIST-02` | If capital is called, what are the schedule and the penalty for a missed call? | "Calls as needed"; punitive dilution buried in the docs. |
| `Q-LIQ-02` | When do K-1s arrive? | "As soon as we can"; a history of extensions. |

Not applicable to a diversified lending fund: `Q-MKT-01`, `Q-MKT-02`, `Q-EXIT-01`, `Q-EXIT-02`. `Q-RISK-04` applies only if the book is real-estate-secured.

## 9. Diligence Checklist

- [ ] Offering document: read the fee, incentive and high-water-mark sections directly and recompute §4.
- [ ] Audited financials: confirm leverage, income versus gains, and non-accruals.
- [ ] Valuation policy: who marks the book, and how much is third-party-valued.
- [ ] Credit facility and note agreements: maturity, covenants, coverage minimums, rate terms.
- [ ] Loan schedule: seniority, largest positions, largest sector, average loan size.
- [ ] Default and recovery data: rebuild from the fund's own records through 2020 and 2022–23.
- [ ] Track record: realized net-to-LP, ideally from an administrator or auditor.
- [ ] Form ADV and regulatory filings: fee disclosures, affiliates, disciplinary history.
- [ ] Background and litigation search on the manager and principals.
- [ ] Tax review: K-1 timing, and how the fund's income is treated in your situation.

## 10. Verdict

**Pursue with conditions.**

*Screening output only, not investment advice.*

**Reasoning.** The risks that usually sink a BDC-style fund are addressed here. Leverage is disclosed and under the `02` 1.5x line. The IRR is labeled levered and shown unlevered, which is the good answer to `Q-RISK-06`, so `CREDIT-01` does not fire. 400+ loans address concentration. Default and recovery are both disclosed through-cycle. Hurdle and high-water mark are the LP-favorable features. Enough is disclosed to underwrite the core story, so this is a merits verdict, and the absences below are conditions rather than a reason to pass.

**Biggest swing factor: the unlevered net figure.** It shows whether the loans pay for the risk on their own or whether 1.1x leverage, carrying about 310 bps/yr of management fee on NAV, is producing the spread.

**What would have to be true (the conditions)**
1. Levered net IRR reaches at least 7.83–8.83% for a lock-up of 5 years or less, or 8.83–10.83% at 7 years. Below the lower number, the lock-up is uncompensated.
2. Unlevered net IRR, on a true net-of-fee basis, beats HYG (4.83%) and the Treasury floor (4.87–5.18%), and leverage supplies no more than 60% of the return. If either fails, `GEN-07` and `CREDIT-01` fire as RED.
3. Incentive terms fall inside the `02` limits: no more than 25% on either part, hurdle of at least 5%, and an explained catch-up. The high-water mark covers both parts. Recompute §4 on the real terms.
4. The book is predominantly senior secured, which is the premise of the `01` risk tier and recovery band (`GEN-17`).
5. Realized net-to-LP track record and meaningful cash co-invest are produced (`Q-GP-01`, `Q-GP-02`).
6. Debt maturity and covenant cushion hold under a markdown of roughly 13% (§2), and redemption terms are known and acceptable (`Q-RISK-01`, `Q-LIQ-01`).
7. Distribution schedule is provided and covered by income (`GEN-11`).

**Who it suits.** An income-oriented LP who can hold through the lock-up, accepts that this is levered credit exposure rather than bond-like stability, and has liquidity elsewhere. It does not suit an LP who may need the capital back on demand, or one relying on reported low volatility as evidence of low risk.
