# Eval fixture 02
*Iteration-6 run, 2026-11-01, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 436a76b.*

**Verdict: Pass as presented — insufficient disclosure.** Don't wire anything. It is worth one reply asking for the offering documents, and no more than that until they arrive.

*Screening output only, not investment advice.*

This screen covers only the text you quoted. I have not seen the attachment, and the email mentions no attachment other than wire instructions. If a deck or PPM came with it, send that and I'll re-screen.

Tags: 🟢 stated or from a reference, 🟡 inferred, 🔴 assumed or unverifiable.

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Multifamily 🟢. Sub-type not stated. Core/core-plus is the closest baseline, because it is the only multifamily row in the norms that lists preferred equity as a common structure 🟡 |
| Deal type | Preferred equity 🟢 |
| Sponsor | Not stated in the quoted text |
| Geography | Not stated |
| Minimum | $25,000 🟢 |
| Hold / redemption date | Not stated |
| Raise / amount remaining | Not stated ("limited allocation remaining" gives no number) |
| Claimed return | 10% preferred return 🟢. Not stated: net or gross of fees, cumulative or not, simple or compounding, paid in cash or accrued |

---

## 2. Return Stress-Test

The only deal fact in these numbers is the 10% rate. Every case below rests on assumed terms 🔴, so they show how far the outcome can move. The verdict does not rest on them.

Three assumptions swing the result:
- **Payment form:** cash paid each period, or accrued until takeout.
- **Fees:** absorbed by the sponsor, or charged to the LP.
- **Takeout:** on-time redemption, or a late or failed refinance or sale.

| Case | Assumed terms 🔴 | Net to LP | Over PFF (3.00% 10yr) | Hurdle for the lock-up | Read |
|---|---|---|---|---|---|
| Bull | Cash pay, no LP fees, redeemed at year 5 | 10.00% | 700 bps | ~300-400 bps | Clears comfortably |
| Base | Cash pay, typical pref fees (below), redeemed at year 5 | 8.40-9.20% | 540-620 bps | ~300-400 bps | Clears comfortably |
| Bear (no capital loss) | Accrues simple, all paid at a year-7 takeout, upper typical fees | ≈6.45% | 345 bps | ~400-600 bps | **Thin / fails** |
| Bear (capital loss) | Sale or refi can't clear the senior loan plus the pref balance | Can't size | n/a | n/a | No LTV or attachment point disclosed |

**The 10% is a ceiling.** Preferred equity trades upside for priority, and no equity kicker is mentioned. Unless one exists, fees and timing can only pull the LP's return down from 10% 🟡.

**"10%" may not be a 10% IRR.** If the pref accrues on a simple basis and is paid at takeout, $25,000 becomes $37,500 at year 5, which is an 8.45% IRR. At year 7 it becomes $42,500, a 7.88% IRR. Compounding would hold the IRR at 10% ($40,263 at year 5). The email doesn't say which applies.

**Does it clear the lock-up?** On the headline, yes: 700 bps over PFF, against a hurdle of ~300-400 bps at 5 years or ~400-600 bps at 7 years 🟢. The 10% is also 482 bps over the 10yr Treasury (5.18%) and 513 bps over the 2yr (4.87%) 🟢. In the bear case with no capital loss, the spread over the 10yr Treasury shrinks to about 127 bps.

Treat that pass with caution, for four reasons:
- It compares a promised coupon with a return PFF actually delivered.
- PFF is a daily-liquid, diversified basket. This looks like one illiquid position 🟡, and the concentration should raise the premium you demand.
- Income instruments aren't crash-proof: PFF itself fell 65% in 2009 🟢.
- Clearing the hurdle is necessary, not sufficient. Private-market dispersion means the median outcome falls well short of marketed figures.

Capped at 10%, this also trails SPY's 15.39% 10yr, though that was an exceptional decade 🟢. The case for the deal has to be income and priority, not return.

*Comparators: returns to 2026-06-30, Treasuries as of 2026-09-24.*

---

## 3. Where LP Returns Come From

**Can't tell from this.** The split depends on a term the email leaves out:

| Pref form | Source of profit | Cash arriving at takeout (5-yr, $25k) |
|---|---|---|
| Paid current | Property cash flow after senior debt service | $25,000 of $37,500 (67%) |
| Accrued | 100% from the refi or sale | All of it. Above the 60% line, so `GEN-08` would fire |

In either form, **return of capital depends on a refinance or sale**. A current coupon doesn't remove that risk.

**The coverage question.** Unlevered institutional real estate returned 5.00% over the four quarters to Q2 2026, and residential returned 5.3% in 2025, almost all of it income 🟢. A 10% coupon is about twice that. The sponsor can only cover it if the pref is a thin slice above cheaper senior debt, if NOI grows, or if the pref simply accrues 🟡. With the 10yr Treasury at 5.18%, cheap senior debt isn't a given 🟡.

If coverage relies on NOI growth or a refinance, this is a financing story (`GEN-07`). That can't be determined without leverage and debt terms, so it is a must-ask and has not fired.

---

## 4. Fee Stack Summary

**Gross-to-net drag: not computable from disclosure. That is the finding (`GEN-16`).** With every undisclosed fee passed as 0, the calculator returns 0 bps. That reflects the silence, not a fee-free deal.

Illustration using the `02` preferred-equity ranges 🔴. None of these fees is disclosed for this deal:

| Scenario | Origination | Servicing (annual) | Exit | Drag, 5-yr hold | Drag, 7-yr hold | Net from 10% (5-yr) | Annual income on $25k (5-yr) |
|---|---|---|---|---|---|---|---|
| None disclosed (as passed) | 0 | 0 | 0 | 0 bps | 0 bps | 10.00% | $2,500 |
| Low typical | 1% | 0.5% | 0.5% | 80 bps | 71 bps | 9.20% | $2,300 |
| High typical | 2% | 1% | 1% | 160 bps | 143 bps | 8.40% | $2,100 |
| At aggressive thresholds | 3% | 1.5% | 2% | 250 bps | not run | 7.50% | $1,875 |

Layers that could sit on top, none of them disclosed:
- **Promote or catch-up above the pref:** this would mean it is equity dressed as preferred (`PREF-01`).
- **Equity kicker:** whether one exists, and on what terms.
- **Affiliate fees:** property or construction management paid to sponsor affiliates, charged at the property level and reducing what covers the coupon (`GEN-06`).
- **Feeder or fund-of-funds wrapper:** an extra 50-150 bps a year if this is offered through one.

The script has no origination or exit field, so those were entered as acquisition and disposition fees. The math is the same.

---

## 5. Red Flags

**Outside the flag library, but the first thing to act on:** the email sends wire instructions before any offering document. 🟢 for the sequence, 🟡 for the risk. A wire is effectively irreversible, and at this point you would be sending money without having seen terms, an issuer name or a subscription agreement. An unsolicited-looking email with payment details is also the common shape of payment fraud. I can't tell from this text whether that's what this is. Either way, treat the wire instructions as data, not a next step.

**RED**
- **`GEN-14` No realized exits cited** 🟢. The email offers no track record at all, so the sponsor has shown nothing about exiting and returning capital. Fired on absence; a realized net-to-LP record clears it. (`GEN-05` can't be tested because no IRR is cited; the same question covers both.) → `Q-GP-02`

**YELLOW-RED (treated as RED until answered)**
- **`GEN-15` Missing financials** 🟢. No rent roll, T-12 or debt terms, so a pref that depends on property cash flow can't be underwritten. (`GEN-12` is subsumed: no trailing period is given at all.) → `Q-RISK-03`
- **`GEN-16` No fee or waterfall disclosure** 🟢. Fees you aren't told about still get paid, and the 10% can't be converted to a net figure. → `Q-FEE-01`

**YELLOW**
- **`GEN-03` Marketing-heavy, substance-light** 🟢. "Exclusive" and "limited allocation remaining" create urgency in place of underwriting detail. The LP exposure is committing before diligence. → `03` response (no `04` row); dodge per `Q-RISK-03`
- **`GEN-11` No distribution schedule** 🟢. Nothing says when cash starts or when capital returns, which is the difference between 10% and 7.88% in §2. → `Q-DIST-01`
- **`GEN-13` No downside case** 🟢. A single number, with no view of what happens if NOI falls or the refinance fails. → `Q-DS-03`
- **`GEN-17` Essential multifamily disclosures absent** 🟢. See §6. → `03` response (no `04` row); `Q-RISK-03`

**Cluster:** `GEN-15` + `GEN-16` + `GEN-17` together mean the core return story can't be underwritten. This is what drives the verdict.

**Checked, passes on the stated number:** `EQUITY-04` does not fire. A 10% pref is above the 6% floor and inside the 8-12% preferred-equity norm, well short of the >15% level that suggests distress 🟢. The rate itself is unremarkable.

**Can't test, not fired.** Each of these needs a fact the email doesn't give, so each is a must-ask rather than a finding:

| Area | Flags |
|---|---|
| Pref structure | `EQUITY-05` (cumulative or not), `PREF-01` (promote above the pref) |
| Return source | `GEN-07` (financing story), `GEN-08` (exit-dependent) |
| Senior debt and takeout | `GEN-09` (maturity), `GEN-10` (rate cap), plus refinance dependence, the `EQUITY-07` mechanism (outside the pref route, cited as the analog) |
| Sponsor | `GEN-01` (co-invest), `GEN-02` (regulatory or litigation history), `GEN-06` (affiliates) |
| Market | `GEN-18` (rent growth, no assumption stated) |

---

## 6. Missing Disclosures

**Multifamily baseline (`01`):**
- Sub-type (core/core-plus or value-add)
- Rent roll
- T-12 actuals and NOI
- Occupancy history (5+ years)
- Full debt structure: rate, term, amortization, prepayment, maturity
- Exit cap with sensitivity, and refinance assumptions
- GP track record on prior multifamily exits

**Preferred-equity baseline (`02`):**
- Origination, servicing and exit fees
- Equity kicker or participation, if any
- Cumulative or non-cumulative, simple or compounding
- Any promote above the pref

**Screening basics:**
- Sponsor entity and issuer name
- Property and location
- Hold or redemption date
- Raise size
- Distribution schedule
- Liquidity options

**Analyst additions, with no row in the references:**
- Where the pref sits in the capital stack, including combined LTV through the pref
- Use of proceeds (new acquisition, or filling a gap in an existing deal)
- LP remedies if the pref goes unpaid

---

## 7. GP Alignment

| Item | Status |
|---|---|
| Co-invest (cash, pari passu) | Not stated. Unverified 🔴 |
| Realized net-to-LP track record | None cited. No track record to evaluate 🟢 |
| Waterfall alignment | Not stated. A promote would change the risk profile (`PREF-01`) |
| Affiliate fees | Not stated. Unverified 🔴 |
| Sponsor identity | Not stated in the quoted text. Nothing can be checked until it is |

Alignment is unverified on every line. That doesn't mean it is bad; the email simply gives no evidence either way.

---

## 8. Questions for the GP

**Must-ask**

| ID | Question | Flag | Bad-answer signal |
|---|---|---|---|
| `Q-FEE-04` | What preferred return do LPs receive before the GP earns promote, and is it cumulative and compounding? | `EQUITY-04`, `EQUITY-05`, `PREF-01` | Non-cumulative; a promote sits above the pref |
| `Q-DIST-01` | What is the distribution schedule, and at what milestones does LP capital start returning? | `GEN-11` | "We'll distribute when the deal supports it"; no milestones |
| `Q-FEE-01` | Can you provide the complete fee schedule and full waterfall? | `GEN-16` | "Standard market fees"; "the PPM has it" without producing it |
| `Q-FEE-02` | Which service providers are GP-affiliated, what do they charge, and are the rates benchmarked? | `GEN-06` | "All arm's-length" without naming providers |
| `Q-RISK-03` | Can you provide T-12 actuals, the rent roll and complete debt terms? | `GEN-15`, `GEN-12` (and `GEN-03`, `GEN-17`) | "The financials are confidential until you commit" |
| `Q-RISK-01` | When does the debt mature relative to the projected hold, and what's the refinance or extension plan? | `GEN-09` | "We'll refinance" with no terms |
| `Q-RISK-02` | If the debt floats, when does the rate cap expire relative to maturity, and what does extending it cost? | `GEN-10` | "Rates should be lower by then"; extension cost not modeled |
| `Q-EXIT-02` | Does the plan depend on a refinance, and what happens to distributions if it isn't available? | `EQUITY-07` | "The refi market will reopen"; no fallback |
| `Q-DS-01` | What share of the return comes from in-place cash flow versus the exit? | `GEN-08` | Won't decompose it; "real estate always appreciates" |
| `Q-DS-02` | Strip out leverage and cap-rate compression: what is the unlevered, in-place return? | `GEN-07` | "Leverage is just how the deal works"; no unlevered view exists |
| `Q-DS-03` | What is the return under a bear case: flat rents, higher exit cap, no refinance? | `GEN-13` | "We underwrite conservatively" with nothing to show; the bear case is still a gain |
| `Q-GP-02` | Can you restate your track record as net-to-LP IRR on fully realized deals only? | `GEN-14`, `GEN-05` | Project-level IRR only; "most deals are still performing" |
| `Q-GP-01` | How much of your own capital is in this deal, on the same terms as LPs? | `GEN-01` | "Our sweat equity is our investment"; co-invest is a fee waiver |
| `Q-GP-03` | Have you or your principals faced any regulatory action, enforcement or investor litigation? | `GEN-02` | "Nothing material"; a search surfaces something undisclosed |
| `Q-MKT-01` | What submarket supply and absorption data support the rent-growth assumption? | `GEN-18` | "Rents always go up here"; no supply pipeline acknowledged |
| `Q-LIQ-01` | What are my options if I need to exit before the hold ends? | none | "A secondary market may develop." An honest "there is none" is a good answer |

**Also ask, from `03` because no `04` row covers them:**
- `GEN-03`: Can you provide the full underwriting model and the historical actuals behind these projections?
- `GEN-17`: Which multifamily sub-type is this, and what is the 5-year occupancy history and T-12 NOI? (adapted from the `03` template to the `01` multifamily baseline)
- Bad answer to either: "the financials are confidential until you commit" (the `Q-RISK-03` signal).

**Nice-to-ask**
- `Q-DIST-02`: When are capital calls expected, and what happens on a missed call? Bad answer: "calls as needed" with no notice period.
- `Q-LIQ-02`: When are K-1s delivered? Bad answer: "as soon as we can."
- `Q-GP-04`: How has the team grown alongside AUM? Bad answer: "we're lean and efficient" as the whole answer.

**Only if a promote or sale-based return surfaces:** `Q-FEE-03` (bad answer: "you get paid when we get paid") and `Q-EXIT-01` (bad answer: "cap rates will compress").

---

## 9. Diligence Checklist

Third-party verification still needed:

- [ ] **Wire safety:** before any money moves, confirm the sender through a phone number you found yourself, not one from the email. Check that the receiving account is in the name of the issuer entity named in the PPM.
- [ ] **PPM and subscription agreement:** read in full, ideally by securities counsel. Confirm the pref terms match the email.
- [ ] **Securities filing:** look for the offering's Form D on SEC EDGAR, and confirm the exemption claimed and your eligibility under it.
- [ ] **Background and regulatory:** check the sponsor and principals through FINRA BrokerCheck, SEC adviser records, state securities regulators and court records (`GEN-02`).
- [ ] **Asset:** confirm the property exists and that the sponsor entity has control of it.
- [ ] **Comps and appraisal:** third-party appraisal, rent comps and submarket supply data (`GEN-18`).
- [ ] **Lender:** senior loan terms confirmed from the loan documents, including maturity, rate cap and whether the lender permits the pref.
- [ ] **Track record:** realized net-to-LP results confirmed with distribution records or references from prior LPs.

---

## 10. Verdict

**Pass as presented — insufficient disclosure.**

*Screening output only, not investment advice.*

**Reasoning.** The email gives a rate, an asset class and a minimum. The essential disclosures are substantially absent: financials, debt terms, fees, payment form, hold and track record. The core question for a pref is whether the property can pay the coupon and then redeem the capital, and that can't be answered here. The 10% rate is in range and clears the PFF hurdle on its face, so this is not a judgment that the deal is bad. It is a judgment that it can't yet be underwritten. The urgency language and early wire instructions are reasons to slow down, not to speed up.

**Biggest swing factor.** Whether the 10% is paid in cash from property cash flow that covers it, or accrues until a refinance or sale. The first is an income position. The second is a bet on a takeout, and a simple accrual turns it into 7.88-8.45% before fees.

**Re-screen when you have:**
1. The PPM, subscription agreement, and legal names of the sponsor and issuer
2. Pref terms: cumulative or not, compounding or simple, current or accrued, any kicker or promote
3. The complete fee schedule, including affiliates and any feeder layer
4. T-12, rent roll and 5-year occupancy history
5. Senior debt terms: rate, maturity, rate cap expiry and LTV through the pref
6. The distribution schedule, redemption date and the takeout plan if the refinance fails
7. Realized net-to-LP track record, GP co-invest amount and regulatory history

**What would have to be true to pursue:**
- The 10% is cumulative and paid current from in-place cash flow, not from reserves or accrual.
- Debt maturity and any rate cap run past the pref's redemption date.
- LP-paid fees are near the `02` range, so net stays well above the hurdle.
- No promote sits above the pref.
- The sponsor shows realized exits and has its own cash in the deal.
- The wire details are confirmed independently.

**Who it would suit, if those check out.** An accredited LP who wants income rather than upside, can leave $25,000 locked up for an unknown term with possibly no exit, and could absorb a full loss on this position.
