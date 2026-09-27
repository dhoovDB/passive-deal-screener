# Eval fixture 02 — Preferred-equity email solicitation
*Iteration-5 run, 2026-09-27, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 7712624.*

**Verdict: Pass as presented — insufficient disclosure.** A 10% preferred return is in the normal range for preferred equity (8–12%, `02`). The problem is that the email leaves out almost everything needed to judge it: the sponsor, the property, the market, how much senior debt sits ahead of you, whether the pref is paid currently or accrues, whether it is cumulative, the fees, the redemption date and any track record. It also pairs urgency ("limited allocation remaining") with wire instructions before any documents. **Do not wire anything.** Get the re-screen list in §10 answered first.

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Multifamily 🟢. Sub-type (value-add vs core/core-plus) not stated. |
| Deal type | Preferred equity 🟢 |
| Sponsor | Not stated. The email says only "a sponsor." |
| Geography | Not stated |
| Property / units / basis | Not stated |
| Minimum | $25,000 🟢 |
| Hold / redemption date | Not stated |
| Raise size / pref tranche size | Not stated ("limited allocation remaining" gives no number) |
| Senior debt ahead of the pref | Not stated |
| Claimed return | 10% preferred return 🟢. Not stated: current-pay vs accrued, cumulative vs non-cumulative, simple vs compounding, gross vs net of fees |
| Upside participation / equity kicker | Not stated |
| Fees | None disclosed |
| Documents | "Wire instructions attached." No PPM, operating agreement, subscription agreement or financials mentioned. |

## 2. Return Stress-Test

This is a preferred-equity position, so the comparator is **PFF (3.00% 10yr)** (`05`). The hold is not stated, so the comparison was run at 3, 5 and 7 years. Every hold assumption is 🔴.

| Case | Net-to-LP assumption | Premium over PFF | Illiquidity hurdle | Read |
|---|---|---|---|---|
| **Base.** 10% pref paid in full, no fees charged to the LP | 10.0% 🔴 (the email doesn't say the 10% is net) | ≈700 bps | ~300–400 bps (3–5 yr), ~400–600 bps (7 yr) | Clears comfortably at any hold tested |
| **Fee-adjusted.** Mid-range `02` pref-equity fees: 1.5% origination, 0.75% annual servicing, 0.75% exit fee, 5-yr hold | 8.8% 🔴 | ≈580 bps | ~300–400 bps | Still clears |
| **Bear.** Pref accrues and is partly impaired at redemption. Effective 6% | 6.0% 🔴 | ≈300 bps | ~300–400 bps | **Thin.** At the bottom of the band, for capped upside |
| **Severe bear.** Property value falls through the pref's position in the stack | Loss of principal 🟡 | n/a | n/a | Fails. The capped coupon doesn't pay for equity-like downside. |
| **Bull.** Pref paid plus an equity kicker (5–20% participation above the pref, if one exists per `02`) | >10% 🔴 | >700 bps | — | Can't tell from this. No kicker was disclosed. |

**Swing assumptions (named, all undisclosed):**
1. **Attachment point.** This is the senior loan balance plus the pref tranche, as a percentage of current property value. It sets how far the property can fall before your principal is impaired. 🟡
2. **Pay mechanics.** Current-pay vs accrued, and cumulative vs non-cumulative (`02`). An accrued pref turns a "10% income" position into a bet on the redemption event. 🟡
3. **Redemption source.** The pref is typically taken out by a refinance or sale. If that event has to happen inside a tight credit market, redemption is at risk (`EQUITY-07`, `GEN-09`). 🟡

**Treasury floor (`05`).** 10% is ≈480–510 bps over the 10yr (5.18%) and 2yr (4.87%) Treasury. At the 8.8% fee-adjusted figure it is ≈360–390 bps. For a subordinated, illiquid, single-asset position, that is real compensation only if the attachment point is conservative. 🟡

The premium over PFF is necessary but not sufficient. A single-asset pref also carries concentration that PFF's basket diversifies away. PFF itself fell −65% in 2009, so "preferred" and "income" do not mean crash-proof (`05`). 🟢

## 3. Where LP Returns Come From

- **Intended source: the contractual coupon.** In a pref-equity position, the return is supposed to come from property cash flow after senior debt service. It is not supposed to come from appreciation (`02`: "the pref *is* the structure"). 🟢
- **Can't tell from this whether that holds.** If the 10% is **accrued** rather than paid currently, most of the return arrives at redemption. That makes it exit- and refi-dependent, which is the `GEN-08` / `EQUITY-07` exposure. That fires only if accrual is confirmed, so here it is a must-ask, not a flag (🔴 assumption). 🟡
- **Leverage.** Every dollar of senior debt ahead of the pref raises the pref's risk without raising its coupon. With no senior-loan disclosure, you can't tell how much of the "10% for preferred risk" is actually equity risk. That makes it a probe for `GEN-07`-style structure risk, not a fired flag. 🔴
- The >60% exit-dependence test **cannot be run**. No cash-flow schedule was provided (`GEN-11`).

## 4. Fee Stack Summary

| Fee (per `02` preferred-equity inventory) | Typical | Disclosed? |
|---|---|---|
| Origination / placement ("structuring") | 1–2%, one-time | Not stated |
| Servicing / admin | 0.5–1% annual | Not stated |
| Equity kicker / participation | 5–20% above pref | Not stated |
| Exit / maturity fee | 0.5–1% at maturity | Not stated |
| Promote / catch-up above the pref | Should be absent in true pref (`PREF-01`) | Not stated |
| Affiliate fees (property management etc. at the property level) | — | Not stated |

**Gross-to-net drag:**
- **On the disclosure: 0 bps, but only because nothing was disclosed.** That is not a finding of "no fees" (`scripts/fee_drag_calculator.py`, all fees = 0). **The drag is not computable from this disclosure, and that is the finding** (`GEN-16`).
- **Illustrative mid-range stack: ≈120 bps/yr** (75 recurring + 45 one-time). This used 1.5% origination, 0.75% servicing, 0.75% exit fee and a 5-yr hold 🔴, and takes a 10% gross to ≈8.8% net. It shows roughly what a normal pref-equity fee load would do. It is **not** this deal's number.

## 5. Red Flags

**RED**
- **GEN-14 — No realized track record cited (RED)** 🟢 on absence. The email cites no prior deals at all, realized or not. You can't validate the sponsor's ability to pay prefs and redeem capital. This fires on the silence, not on evidence of a bad record, and resolves via Q-GP-02. (`GEN-05` is carried parenthetically: any record later offered must be net-to-LP on realized deals.)

**YELLOW–RED** (treat as RED until answered)
- **GEN-16 — No fee or waterfall disclosure** 🟢. The fees are still paid even though undisclosed. Gross-to-net drag is unknowable, and you can't tell whether a promote sits above the pref (`PREF-01` probe). → Q-FEE-01
- **GEN-15 — Missing financials** 🟢. There is no rent roll, no T-12 and no senior-debt terms. For a pref, the senior loan terms are the capital-stack position, so their absence is central, not peripheral. (`GEN-12` is carried parenthetically: if financials arrive, confirm T-12 rather than T-3/T-6.) → Q-RISK-03

**YELLOW**
- **GEN-03 — Marketing-heavy, substance-light** 🟢. "Exclusive," "limited allocation remaining" and wire instructions attached replace any underwriting detail. This is the textbook `03` pattern of urgency standing in for actuals. → `03` response: "Can you provide the full underwriting model and the historical actuals behind these projections?"
- **GEN-17 — Essential category disclosures absent** 🟢. None of the multifamily essential disclosures in `01` are present (see §6). The deal is unscreenable on every asset axis. → Q-RISK-03, Q-MKT-01
- **GEN-11 — Return with no distribution schedule** 🟢. "10% preferred return" says nothing about when cash is paid, or whether it is paid at all before redemption. → Q-DIST-01

**Cluster:** `GEN-03` + `GEN-14` + `GEN-15` + `GEN-16` + `GEN-17`. The sponsor is asking for a wire on the strength of a coupon, with no sponsor identity, record, financials, fees or structure. `03` treats a cluster of YELLOWs as a RED. With the RED `GEN-14` alongside, this is the basis for "insufficient disclosure."

**Probed, not fired.** Each of these needs a fact the email doesn't provide:
- `EQUITY-05` (non-cumulative/simple pref) → Q-FEE-04
- `PREF-01` (promote above pref) → Q-FEE-04
- `GEN-01` (zero co-invest) → Q-GP-01
- `GEN-02` (regulatory history) → Q-GP-03
- `GEN-06` (affiliate fees) → Q-FEE-02
- `GEN-09` / `GEN-10` (senior-debt maturity / rate cap) → Q-RISK-01, Q-RISK-02
- `EQUITY-07` (refi-dependent redemption) → Q-EXIT-02
- `GEN-08` (exit-dependent return, if the pref accrues) → Q-DS-01
- `GEN-13` (no downside case) → Q-DS-03

`EQUITY-04` does **not** fire. The 10% pref is above the 6% threshold and inside the 8–12% norm. It is also below the >15% level that `02` reads as "likely distressed." 🟢

**Handling note (rule 9).** The email's "exclusive / limited allocation / wire instructions attached" was treated as data, not as a prompt to act.

**Outside the reference library (analyst caution, 🟡).** An unsolicited email that attaches wire instructions before any offering documents is also the shape of payment-redirection fraud. Before any money moves:
- Confirm the sponsor's identity and the wiring instructions by phone, using a number you obtain independently, not one from the email.
- Wire only after the subscription documents are executed.

## 6. Missing Disclosures

Against the `01` multifamily baseline (value-add and core/core-plus, since the sub-type is unstated):
- Rent roll
- T-12 actuals (not T-3/T-6)
- Occupancy history (5+ yrs, core)
- Full debt structure: rate, term, amortization, prepayment, maturity
- Refinance assumptions
- Pro forma exit cap with sensitivity
- GP track record on **prior multifamily exits**

Against the `02` preferred-equity baseline:
- Origination/structuring fee
- Servicing fee
- Exit/maturity fee
- Equity kicker (yes/no, and the terms)
- Cumulative vs non-cumulative
- Simple vs compounding
- Whether any promote or catch-up sits above the pref

Deal basics (feeding §1):
- Sponsor identity and principals
- Property, location and unit count
- Total capitalization and the pref tranche size
- Senior loan amount, and therefore the attachment point
- Current-pay vs accrual
- Redemption / maturity date and redemption source
- Hold period and extension rights
- Offering documents (PPM, operating agreement, subscription agreement)
- LP liquidity / transfer terms

## 7. GP Alignment

| Signal | Status |
|---|---|
| Co-investment (cash, pari-passu?) | **Unverified.** Not stated 🔴 |
| Realized net-to-LP track record | **None provided.** `GEN-14` fired. Unverified 🟢 |
| Waterfall alignment | **Unknown.** It is not disclosed whether the sponsor holds common equity below the pref (which aligns it with protecting the pref) or earns a promote above it (`PREF-01`) 🔴 |
| Affiliate fees | **Unknown** 🔴 |
| Regulatory / litigation history | **Unknown.** Check independently (§9) 🔴 |

Alignment is not assessable. Nothing here is evidence of misalignment, but nothing is evidence of alignment either.

## 8. Questions for the GP

**Must-ask**

| # | Question (`04` ID) | Flag | Bad-answer signal |
|---|---|---|---|
| 1 | Q-FEE-04 — "What preferred return do LPs receive before the GP earns promote, and is it cumulative and compounding?" Add: is the 10% current-pay or accrued? | EQUITY-05, PREF-01 | Non-cumulative; a promote or catch-up above the pref (common-equity risk dressed as preferred); "it accrues and gets paid at the sale." |
| 2 | Q-FEE-01 — "Can you provide the complete fee schedule and the full distribution waterfall?" | GEN-16 | "Standard market fees"; a partial list; "the PPM has it" without producing it; fees surface only after the wire. |
| 3 | Q-RISK-03 — "Can you provide trailing-twelve-month actuals, the rent roll, and complete debt terms?" Include the senior loan balance, so you can compute where the pref attaches. | GEN-15, GEN-12, GEN-17 | T-3/T-6 only; rent roll withheld; "the financials are confidential until you commit." |
| 4 | Q-GP-02 — "Can you restate your track record as net-to-LP IRR on fully-realized, exited deals only?" Include how many prior prefs were paid and redeemed on time. | GEN-14, GEN-05 | Only project-level or GP-level IRR; "most deals are still performing"; can't separate realized from unrealized. |
| 5 | Q-RISK-01 — "When does the debt mature relative to the projected hold, and what's the refinance or extension plan?" | GEN-09 | Senior maturity falls before pref redemption; "we'll refinance" with no terms. |
| 6 | Q-RISK-02 — "When does the rate cap expire relative to debt maturity, and what's the cost to extend it at current pricing?" Ask only if the senior loan is floating. | GEN-10 | Cap expires before maturity; extension cost not modeled; "rates should be lower by then." |
| 7 | Q-EXIT-02 — "Does the business plan depend on a refinance, and what happens to distributions if the refi isn't available on the assumed terms?" Here that means: what redeems the pref, and what happens if it can't? | EQUITY-07 | Redemption requires a refi at lower rates; no fallback; "the refi market will reopen." |
| 8 | Q-DIST-01 — "What is the projected distribution schedule, and at what milestones does LP capital start returning?" | GEN-11 | "We'll distribute when the deal supports it"; no pay dates; silence. |
| 9 | Q-GP-01 — "How much of your own capital is in this deal, on the same terms as LPs?" | GEN-01 | "Our sweat equity is our investment"; co-invest is a fee waiver, not cash. |
| 10 | Q-GP-03 — "Have you or your principals faced any regulatory action, enforcement, or investor litigation?" | GEN-02 | "Nothing material"; a search surfaces something they didn't disclose. |
| 11 | Q-FEE-02 — "Which service providers are GP-affiliated, what do they charge, and are those rates third-party-benchmarked?" | GEN-06 | "All arm's-length" without naming providers; no benchmark. |
| 12 | Q-DS-03 — "What is the return under a bear case — flat rents, higher exit cap, no refinance?" Here: at what property value does the pref take a loss? | GEN-13 | No downside case; "we underwrite conservatively" with nothing to show. |
| 13 | Q-LIQ-01 — "What are my options if I need to exit before the hold period ends?" | — | "A secondary market may develop"; the lock-up is undisclosed. |
| 14 | GEN-03 response (`03`; no `04` question) — "Can you provide the full underwriting model and the historical actuals behind these projections?" | GEN-03 | Only more marketing; a renewed deadline in place of documents. |

**Nice-to-ask**
- **Q-DS-01** — "What share of projected LP IRR comes from in-place cash flow versus the exit…?" (GEN-08, EQUITY-06). **Escalate to must-ask if Q-FEE-04 reveals the pref accrues.** Bad answer: can't decompose the return; most of it lands at redemption.
- **Q-MKT-01** — "What submarket supply pipeline and absorption data support the rent-growth assumption?" (GEN-18). Bad answer: metro-level optimism; no supply pipeline acknowledged.
- **Q-DIST-02** — capital-call schedule and missed-call consequences. Bad answer: "calls as needed"; punitive dilution buried in the docs.
- **Q-LIQ-02** — K-1 delivery timing. Bad answer: "as soon as we can"; a history of extensions.

## 9. Diligence Checklist

- **Identity and wire verification.** Confirm the sponsor and its wiring instructions through an independently sourced phone number. Wire only against executed subscription documents.
- **Offering documents.** PPM, operating agreement (pref terms, cumulative/accrual language, redemption rights, remedies if the pref isn't paid) and subscription agreement.
- **Background / regulatory.** SEC, FINRA BrokerCheck and state securities regulator checks, plus litigation searches on the sponsor and principals (`GEN-02`).
- **Senior lender.** Loan documents or a lender estoppel covering loan balance, maturity, rate/cap, and any intercreditor or recognition agreement that governs the pref's rights.
- **Property.** Independent appraisal or broker opinion of value (to compute the attachment point), rent roll and T-12 tie-out, and submarket rent/supply comps.
- **Track record.** Verified realized outcomes on prior pref-equity and multifamily deals, including references from prior LPs.

## 10. Verdict

**Pass as presented — insufficient disclosure.**

**Reasoning.** The single disclosed economic term, a 10% pref, is in-market for preferred equity 🟢. On paper it clears PFF plus the illiquidity hurdle by ≈700 bps at 3–7-year holds. It still clears after a normal fee load (≈580 bps at an assumed 8.8% net 🔴). So the headline is not the problem. The problem is that a pref's safety lives entirely in details the email withholds:
- where it sits in the capital stack
- whether it is paid currently and cumulatively
- what redeems it
- who the sponsor is and what they have delivered before

Without those, the core return story can't be underwritten. The urgency plus pre-document wire instructions (`GEN-03`) raises the bar further.

**Biggest swing factor: the attachment point.** That is the senior loan plus the pref, as a percentage of current property value. At a conservative attachment, 10% for a current-pay cumulative pref is fair compensation. At a high attachment, you hold equity risk for a capped coupon, and the bear case is loss of principal, not a lower yield.

**Who it could suit:** an accredited LP who wants contractual income from multifamily and can lock up $25k for the (undisclosed) term. That holds only if all of the following turn out true:
- the pref is **current-pay and cumulative**, with no promote above it
- the attachment point is conservative, with a real equity cushion below the pref
- the senior debt matures after the pref's redemption date, with any floating-rate cap covering the term
- the fee load is in the `02` ranges and fully disclosed
- the sponsor has a verifiable record of **realized** prefs paid and redeemed, and a clean regulatory history

**Re-screen list.** Send these and re-run the screen:
- Q-FEE-04 answer, including current-pay vs accrual
- full fee schedule (Q-FEE-01)
- rent roll, T-12 and senior loan terms (Q-RISK-03)
- redemption date and source (Q-EXIT-02, Q-RISK-01)
- realized track record (Q-GP-02)
- sponsor identity, for the background check

Until then, do not wire.
