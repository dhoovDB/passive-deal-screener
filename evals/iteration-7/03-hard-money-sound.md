# Eval fixture 03
*Iteration-7 run, 2026-11-01, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 181fdd7.*

# Passive Deal Screen: Senior-Secured Bridge Loan Fund (Hard Money)

**Verdict: Pursue with conditions.** This is a better-disclosed hard-money fund than most. It gives LTV on both an as-is and an ARV basis, a default rate and a recovery rate through 2020 and 2022–23, diversification limits, and a fee step-down. A 9% net target beats HYG by about 417 bps, which clears the hurdle for a 3–5 year lock-up. The open items are the fee layers you can't see, whether the fund uses leverage, and whether the GP's own record is verified. They are conditions to resolve, not reasons to pass.

*Screening output only, not investment advice.*

Confidence tags: 🟢 stated in the deal or taken from a reference · 🟡 inferred · 🔴 assumed or unverifiable.

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Hard Money / Bridge Loan (`01`) 🟢 |
| Deal type | Hard money / bridge **debt fund**, senior secured 🟢 |
| Sponsor | Not stated |
| Geography | 12 states; no single metro over 15% 🟢 |
| Collateral / loan type | Not stated (fix-and-flip residential vs commercial bridge; property-type mix not given) |
| Portfolio LTV | 68% as-is / 72% ARV (average) 🟢 (see the basis anomaly in §5/§6) |
| Credit grading | Loans graded A–D; the deal says the grade mix is disclosed, but **the mix itself was not in the material provided** |
| Loss history | 3.1% historical default rate; 92% realized recovery, including 2020 and 2022–23 🟢 (unverified) |
| Minimum investment | Not stated |
| Hold / fund term | Not stated. There is an "investment period", which implies a closed-end fund, but its length and the fund term are not given. `01` norm: 3–5 yr fund commitment, 6–18 mo per loan |
| Raise / fund size | Not stated |
| Fees | 1.5% management fee, stepping down to 1.0% after the investment period 🟢. All other fees not stated |
| Claimed return | **9% net target to LPs** 🟢. It is a *target*, not a realized figure |
| Distribution schedule | Not stated |
| Fund-level leverage | Not stated |
| GP co-invest | Not stated |

---

## 2. Return Stress-Test

**Benchmark (from `scripts/benchmark_comparator.py`, `05` figures as of 2026-09-27):**

| Case | Net to LP | Premium over HYG (4.83% 10yr) | Illiquidity hurdle (3–5 yr lock-up) | Result |
|---|---|---|---|---|
| Bull | 10.0% (top of `01`'s 8–10% range) | ≈517 bps | ~300–400 bps | Clears comfortably |
| **Base** | **9.0% (stated target)** 🟢 | **≈417 bps** | ~300–400 bps | **Clears**, by roughly 17–117 bps |
| Bear | 7.5% 🔴 | ≈267 bps | ~300–400 bps | **Thin / fails**: the lock-up isn't paid for |
| Severe | 6.0% 🔴 | ≈117 bps | ~300–400 bps | Fails |

- **Lock-up is assumed** 🔴. The fund term isn't stated, so I used `01`'s 3–5 yr fund commitment. The comparator puts the same ~300–400 bps hurdle on 3, 4 and 5 years. If the effective lock-up is ≤1 yr (open-ended with redemptions), the hurdle falls to ~200 bps and the base case clears easily.
- **Treasury floor, the credit-lens view in `05`:** 9% net is ≈476 bps over the 3-month bill (4.24%) and ≈413 bps over the 2-year (4.87%). That sits inside `05`'s hard-money band of ≈315–575 bps, so the LP is paid for both credit risk and illiquidity, though not lavishly.
- **The base case has little room.** Its margin over the hurdle is at most ~117 bps, and only ~17 bps against the top of the hurdle range. Net returns about 150 bps below target (7.5%) fail the illiquidity test. Clearing the bar is necessary but not sufficient: per `05`'s dispersion note, the median fund underperforms marketed targets.

**The 2–3 swing assumptions (debt-fund equivalents of exit cap, rent growth and refi):**

1. **Loss severity in the next downturn** 🟡. The stated history implies an expected loss of roughly 3.1% × (1 − 0.92) ≈ **25 bps of principal**. That is per year only if the 3.1% is an annual, dollar-weighted rate; if it is cumulative or counted by loan, it is lower per year. The bear case does not need a disaster. Losses of about 150 bps a year take the net from 9% to ~7.5%, for example defaults roughly doubling while recovery falls toward 75% 🔴 (illustrative, not a forecast). At 68% average as-is LTV, collateral can fall about 32% before principal is impaired, *before* foreclosure, carry and legal costs. How competent the GP is at workouts decides where losses land inside that cushion. The workout timeline is not disclosed.
2. **Fund-level leverage** 🔴. If a credit line sits behind the 9%, part of the return is leverage, and the same leverage amplifies the bear case (`CREDIT-01` logic, see §3).
3. **Reinvestment yield and cash drag** 🟡. Loans of 6–18 months (`01`) mean the book re-prices to current coupons within a year or two. Lower short rates or more competition for loans compress the coupon, and idle capital between payoffs drags the realized net below the target.

---

## 3. Where LP Returns Come From

- **Almost entirely current income** 🟡. Loan interest plus borrower-paid origination points, which `02` says flow into fund yield (whether they actually do is unverified; see §4 and §7), minus credit losses. There is no terminal value or exit cap. **`GEN-08` (exit-dependent IRR) does not apply**, and **`GEN-07` (financing story) does not fire on the asset side**: return comes from coupon, not cap-rate compression.
- **Leverage is the open question, and it would be fund-level.** The deal is silent on whether the fund borrows. In a debt fund, a credit facility is how a modest loan-book yield gets levered into a marketable LP number (`03` notes, `CREDIT-01` → `GEN-07` family). **Not fired**, because the facts are unknown. It is a must-ask (Q-RISK-06).
- **Implied-gross gap** 🔴/🟡. `01` puts common gross yield at 11–13%. With only the disclosed management fee, that gross would net about 9.5–12% to LPs. The 9% target sits *below* that range. Either the book's gross yield is lower (about 10–10.5%) or 50–300 bps of drag is undisclosed (carry, servicing, fund expenses, credit losses, cash drag). Section 4 quantifies one plausible version.

---

## 4. Fee Stack Summary

| Fee (`02` → Hard money / bridge) | This deal | `02` norm / aggressive threshold | Read |
|---|---|---|---|
| Fund management fee | 1.5% → 1.0% after the investment period 🟢 | 1–2% of AUM; >2.5% aggressive; no step-down is a flag | **In range; the step-down is present** (`HML-05` clear). Basis (committed vs invested vs AUM) not stated |
| Performance fee / carry | **Not stated** | 10–20% above a 5–8% hurdle; >25% or no hurdle is aggressive | Unknown, and the biggest drag line that could be hiding |
| Servicing fee | **Not stated** | 0.25–0.5% of loan balance; >1% aggressive | Unknown; usually charged by a GP affiliate |
| Origination points | **Not stated** (rate, and who keeps them) | 1–3 pts; <1 or >5 is a flag | If the GP keeps the points rather than the fund, that is a fee layer |
| Late fees / default interest | **Not stated** | Should go to the fund, not the GP | Verify they aren't diverted into a GP "workout fee" |
| Admin / fund expenses | **Not stated** | 0.1–0.5% or $1–3k/LP | Unknown |
| Wind-down / liquidation fee | **Not stated** | 0.5–1% of remaining AUM; >2% aggressive | Unknown |

**Gross-to-net drag (`scripts/fee_drag_calculator.py`, 12% gross and 4-yr hold ASSUMED 🔴, undisclosed fees entered as 0):**

- Disclosed fees only: **≈125 bps/yr** (150 bps during the investment period, 100 bps after; blended 1.25%). That gives about 10.75% net at a 12% gross.
- **Total drag: not computable from the disclosure. That is the finding.**
- Illustrative only 🔴: add a typical `02` servicing fee (0.5%) and a 20% carry over an 8% hurdle to the 1.5% management fee, and the calculator gives **≈291 bps of drag → 9.09% net**. That is almost exactly the stated target. The 9% is consistent with an undisclosed carry and servicing layer of about that size. Get the actual schedule.

---

## 5. Red Flags

**YELLOW–RED (treat as RED until the answer moves it down)**
- **`GEN-16`: incomplete fee disclosure** 🟢. Only the management fee is disclosed. The performance fee/hurdle, servicing, points retention, expenses and wind-down are all absent, so gross-to-net drag can't be calculated, and §4 shows roughly 150–200 bps of drag unexplained by what is disclosed. LP exposure: the 9% is presented net, but there is no way to check what it is net *of*, or how it behaves if gross yield falls (a carry above a hurdle cushions the LP; a flat servicing fee does not). → Q-FEE-01

**YELLOW**
- **`GEN-11`: no distribution schedule behind the net target** 🟢. Proactive trigger. For an income fund, distributions are normally monthly or quarterly, but frequency, reinvestment default and any lag are not stated. LP exposure: a "9% target" with accrued-but-unpaid or reinvested income has different risk timing from cash paid monthly. → Q-DIST-01
- **`GEN-17`: one essential category disclosure absent** 🟢. `01` lists "foreclosure process and recovery rate". The recovery rate is given (92%), but the foreclosure/workout process and timeline are not. LP exposure: a 92% recovery that took 24 months has a very different IRR effect than one that took 6, because principal sits idle and stops earning through the workout. → Q-RISK-05

**Anomaly to resolve (not a flag, a must-clarify)** 🟡
- **The two LTV figures don't reconcile on a like-for-like basis.** ARV should exceed as-is value, so LTV on ARV should be *lower* than LTV on as-is. Here it is higher (72% vs 68%). The usual benign explanation is different numerators: as-is LTV on the initial advance, LTARV on the full commitment including rehab holdbacks. If so, the fully-drawn as-is exposure is above 68%. `HML-01` does **not** fire, because as-is LTV *is* disclosed, but the basis needs a written definition. → Q-RISK-04

**Checked, not fired** (disclosed favorably or not applicable; cited per the output contract)
- `HML-01` (ARV-only LTV): as-is is disclosed (subject to the anomaly above).
- `HML-02` (geographic concentration): 12 states, no metro over 15% 🟢.
- `HML-03` / `HML-04` (default/recovery not disclosed): both disclosed, including 2020 and 2022–23 🟢. The basis is still unverified (Q-RISK-05).
- `HML-05` (no step-down): a step-down to 1.0% is disclosed 🟢.
- `CREDIT-01` (fund-level leverage): **unknown, not fired**. Leverage is undisclosed, so it is a must-ask (Q-RISK-06), not a finding.
- `GEN-01` (zero co-invest), `GEN-05` / `GEN-14` (GP-level / unrealized record), `GEN-02` (regulatory), `GEN-06` (affiliate stacking): **not stated, so they can't be scored**. They are routed to must-asks (§8) rather than fired on assumption.
- `GEN-07` / `GEN-08`: not applicable on the asset side (income return, no exit dependence; §3).
- `GEN-13` (no downside case): only the target is quoted, but the through-cycle loss history partly answers it. Not fired; Q-DS-03 is a nice-to-ask.

No cluster pattern. The flags sit in disclosure, not in the credit story.

---

## 6. Missing Disclosures

Against `01` (Hard Money essentials) and `02` (hard-money fee inventory):

**Core credit story (asked for by `01`)**
- Foreclosure/workout process and **average workout timeline** (the one `01` essential not covered).
- **Basis of the 3.1% default rate**: annual or cumulative, by dollar or by count, and the default definition (60/90+ days, maturity default, REO).
- Basis of the **92% recovery**: principal only or including accrued interest and costs, gross or net of legal/REO costs.
- **LTV definitions and valuation source**: numerator (initial advance vs total commitment), appraisal vs BPO vs internal, and the reconciliation of 68% as-is vs 72% ARV.
- **The A–D grade mix itself** (claimed disclosed, not in the material provided), and default/loss by grade.
- Loan count, average and largest loan size, top-borrower concentration, property-type mix (residential vs commercial; fix-and-flip vs stabilization bridge), lien position on every loan, loan term profile, fixed vs floating coupons, average coupon and points.

**Fees and structure (asked for by `02`)**
- Performance fee/carry and hurdle (hard vs soft, catch-up, high-water mark).
- Servicing fee; who keeps origination points, extension fees, late fees and default interest.
- Management-fee basis (committed vs invested vs AUM) and the **length of the investment period**.
- Admin/fund expenses; wind-down fee.
- **Fund-level leverage** and the facility terms.

**Fund and sponsor**
- Sponsor identity, AUM, years lending, team size.
- Fund term, lock-up, redemption terms/gates (if open-ended), minimum, raise size.
- Distribution frequency and reinvestment default.
- GP co-invest (amount, pari-passu?).
- **Realized net-to-LP returns** on prior funds/vintages.
- Auditor and fund administrator.

---

## 7. GP Alignment

- **Co-invest:** not stated 🔴. Unverified. → Q-GP-01
- **Track record:** the 3.1% default and 92% recovery through 2020 and 2022–23 are *realized loan-level* statistics, which is stronger evidence than marks. But they are self-reported and unaudited as presented 🔴. There is **no realized net-to-LP fund return**; the 9% is a forward target. Treat the record as **unverified** until there are audited, realized LP returns by vintage (`GEN-05` / `GEN-14` logic, not fired). → Q-GP-02
- **Waterfall alignment:** unknown. If there is a performance fee, how aligned the GP is depends on the hurdle (`02`: a no-hurdle promote is aggressive) and on whether it is calculated across the whole fund with a high-water mark. → Q-FEE-01, Q-FEE-04 (adapted)
- **Affiliate fees:** in hard-money funds, servicing, points and extension/workout fees often go to GP affiliates. Fee stacking through affiliates (`GEN-06`) can't be assessed from this disclosure. → Q-FEE-02
- **Positive alignment signals** 🟢: the management-fee step-down after the investment period, and voluntary disclosure of as-is LTV and stress-period loss data. A GP hiding a weak record usually doesn't volunteer 2022–23 numbers.

---

## 8. Questions for the GP

**Must-ask**

| ID | Question (adapted to this deal) | Bad-answer signal | Flag |
|---|---|---|---|
| Q-FEE-01 | "Send the complete fee schedule: performance fee and hurdle, servicing, who keeps origination/extension/late fees, fund expenses, wind-down, and the management-fee basis and investment-period length." | "Standard market fees"; a partial list; "the PPM has it" without producing it; the carry surfaces only in the LPA. | `GEN-16` (fired), `HML-05` (confirm step-down mechanics) |
| Q-RISK-04 | "Define your LTV numerators and valuation source. Why is LTV on ARV (72%) higher than LTV on as-is (68%)? What is fully-drawn as-is LTV including holdbacks?" | Can't reconcile the two figures; quotes only LTV on ARV when pressed; "our borrowers always complete." | `HML-01` (clarification; not fired) |
| Q-RISK-05 | "Is the 3.1% default rate annual or cumulative, by dollar or by count, and how do you define default? Is the 92% recovery net of legal/REO costs and inclusive of accrued interest? What is the average workout timeline, and the numbers for 2020 and 2022–23 separately?" | Recovery quoted gross of costs; no timeline; one blended number with no 2022–23 breakout; "we've never had a loss." | `HML-03`, `HML-04`, `GEN-17` (fired) |
| Q-RISK-06 | "Does the fund use a credit facility or other leverage? If so, what ratio, and is the 9% target levered or unlevered?" | Won't give a number; "leverage is conservative"; a levered target presented as if unlevered. | `CREDIT-01` (not fired, undisclosed) |
| Q-DIST-01 | "How often are distributions paid, is reinvestment the default, and what is the lag from loan interest to LP distribution?" | "We distribute when the book supports it"; target quoted with no schedule; reinvestment on by default without disclosure. | `GEN-11` (fired) |
| Q-GP-01 | "How much of your own capital is in this fund, on the same terms as LPs?" | Co-invest is a fee waiver, not cash; a token amount on better terms. | `GEN-01` |
| Q-GP-02 | "Restate your track record as realized net-to-LP returns by fund or vintage, audited." | Offers only loan-level yields or gross portfolio yield; "most loans are still performing"; can't separate realized from accrued. | `GEN-05`, `GEN-14` |
| Q-GP-03 | "Have you or your principals faced any regulatory action, enforcement, or investor litigation?" | "Nothing material"; a search turns up something they didn't disclose. | `GEN-02` |
| Q-FEE-02 | "Which service providers (servicer, appraiser/BPO, title, workout/REO management) are GP-affiliated, what do they charge, and are the rates benchmarked?" | "All arm's-length" without naming providers; points or extension fees kept by the GP undisclosed. | `GEN-06` |
| Q-LIQ-01 | "What is the lock-up, and what are my options to exit early: redemption windows, gates, notice periods, secondary?" | "We'll try to accommodate"; gates that can be imposed at will; lock-up length vague. | — |

**Nice-to-ask**

| ID | Question | Bad-answer signal | Flag |
|---|---|---|---|
| Q-FEE-04 *(if a performance fee exists)* | "What hurdle sits under the performance fee? Is it hard or soft, with what catch-up, and is there a high-water mark?" | No hurdle; a soft hurdle with 100% catch-up; carry on recouped losses. | `02` threshold (>25% or no hurdle) |
| Q-DS-03 | "What is the net return to LPs if defaults double and recoveries fall to 75%? What happened to LP distributions in 2020 and 2022–23?" | "We underwrite conservatively" with no numbers; distributions were cut but this wasn't disclosed. | `GEN-13` |
| Q-GP-04 | "How have origination, servicing and asset-management headcount grown alongside AUM?" | Loan count multiplied while the servicing team stayed flat. | `GEN-04` |
| Q-DIST-02 | "Are there capital calls, or is it fully funded at subscription? What are the consequences of a missed call?" | "Calls as needed" with no notice period. | — |
| Q-LIQ-02 | "When are K-1s delivered, and have you met the filing deadline historically?" | "As soon as we can"; a history of extensions. | — |

---

## 9. Diligence Checklist

- [ ] **PPM, LPA and subscription docs**: confirm the full fee schedule, performance-fee mechanics, management-fee basis, investment-period length, fund term, redemption/gate terms and leverage limits.
- [ ] **Background and regulatory**: SEC IAPD / Form ADV (fee schedule, disciplinary history), FINRA BrokerCheck, state securities regulators, state lending/broker licenses in the 12 states, and court and lien searches on the principals (`GEN-02`).
- [ ] **Audited financials**: a named, credible auditor and a third-party fund administrator. Tie the 3.1% / 92% figures to audited loss data.
- [ ] **Loan tape**: a current tape showing LTV (both bases), grade, state/metro, coupon, points, maturity and status, so you can check the 68%/72% averages, the ≤15% metro cap and the A–D mix yourself.
- [ ] **Valuation sample**: pull a handful of appraisals/BPOs and compare them against independent comps for as-is value.
- [ ] **Workout files**: a sample of resolved defaults from 2020 and 2022–23, with timeline, costs and net recovery.
- [ ] **Lender / facility**: if leveraged, the credit agreement terms (advance rate, covenants, maturity, recourse).
- [ ] **LP references**: existing investors from a prior vintage, asked about distribution consistency and redemption experience.
- [ ] **Custody and title**: who holds the original notes, and confirm lender's title policies and hazard insurance naming the fund.

---

## 10. Verdict

**Pursue with conditions.**

*Screening output only, not investment advice.*

**Reasoning.** This fund discloses the things that usually sink hard-money screens. It gives LTV on an as-is basis, not just ARV, so `HML-01` does not fire. It reports a default rate *and* a recovery rate, and its loss history explicitly covers 2020 and 2022–23 (`HML-03`/`HML-04` clear). Its geography is diversified (`HML-02` clear), and the management fee steps down (`HML-05` clear). The stated history implies an expected loss of about 25 bps of principal, and 68% average as-is LTV leaves about 32 points of collateral cushion before costs. A 9% net target clears HYG by about 417 bps against a ~300–400 bps hurdle for a 3–5 year lock-up, and sits about 413–476 bps over short Treasuries. The core return story can be underwritten, so this is a merits verdict, not an "as presented" one.

**Biggest swing factor:** the drag you can't see. The disclosed management fee explains only part of the gap between a typical 11–13% gross loan-book yield and the 9% net. An undisclosed carry and servicing layer (illustratively ~291 bps total drag) or a fund credit line could fill the rest. Either one changes how the 9% holds up in a bad year. With at most ~117 bps of margin over the illiquidity hurdle, a ~150 bps shortfall (to 7.5% net) means the lock-up is no longer paid for.

**Conditions to commit:**
1. A full written fee schedule (Q-FEE-01). Any performance fee needs a hard hurdle at or above 5–8% with no 100% catch-up, and the total drag must reconcile the book's gross yield to the 9% net.
2. Written disclosure of fund leverage (Q-RISK-06). Unlevered, or modest and covenant-light, with the 9% stated on a known basis.
3. A written reconciliation of the 68% as-is vs 72% ARV LTV figures, plus fully-drawn as-is LTV (Q-RISK-04).
4. Default and recovery definitions, a workout timeline, and 2020 and 2022–23 broken out separately (Q-RISK-05), tied to audited financials.
5. Audited, realized net-to-LP returns by vintage (Q-GP-02), meaningful pari-passu GP co-invest (Q-GP-01), and a clean regulatory search (Q-GP-03).
6. A lock-up and redemption structure the LP can live with (Q-LIQ-01), and a stated distribution schedule (Q-DIST-01).

**Who it suits.** An income-seeking LP who wants senior-secured, short-duration real-estate credit, can accept a 3–5 year lock-up (assumed) and moderate credit risk, and wants regular current income rather than appreciation. It does not suit an LP who needs liquidity within the term, or who is comparing it against equity-RE upside.

**What would have to be true.** Gross book yield minus the full fee stack has to arrive at about 9% without leverage doing the work, and the 2020 and 2022–23 recoveries have to hold up as audited, net-of-cost figures. If fees or leverage explain the gap, or recoveries turn out gross of costs, re-screen with the corrected net. Below about 7.5–8% net, the fund no longer clears the illiquidity hurdle against HYG.
