# Eval fixture 02 — Preferred-equity email solicitation
*Iteration-2 run, 2026-07-04, blind generation by fresh-context agent, against SKILL.md (post S1–S3 fixes).*

**Verdict: Pass as presented — insufficient disclosure. This is a wire solicitation, not a deal disclosure: three sentences, urgency language, and wire instructions before a single fee, term, sponsor name, or document. Do not wire anything.**

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Multifamily (subtype, asset(s), market — **not stated**) 🟢 |
| Deal type | Preferred equity 🟢 |
| Sponsor | **Not stated** — the email doesn't identify the GP entity |
| Geography | **Not stated** |
| Minimum investment | $25,000 🟢 |
| Hold / maturity | **Not stated** |
| Raise | **Not stated** |
| Claimed return | 10% preferred return — cumulative? compounding? current-pay vs accrued? **Not stated** |
| Position in capital stack | **Not stated** — senior debt above? common equity cushion below? |

Routing: `01` multifamily (subtype unknown) + preferred-equity norms; `02` preferred equity fee inventory; `03` `GEN-`, `PREF-`, `EQUITY-04/05`; `05` PFF comparator.

## 2. Return Stress-Test

- The 10% pref sits inside the `02` typical range (8–12%; <7% under-compensated, >15% likely distressed) 🟢 — the *rate* is unremarkable for the structure.
- **Benchmark (`05`):** 10% vs PFF 3.72% (10yr) ≈ **+630bps** — well above the ~230bps a 6% pref would carry, and above the 3–5yr lock-up hurdle of ~300–400bps *if* the term is in that range 🟡. On paper, generous.
- But a stress-test needs the stack: pref-equity downside is governed by the common-equity cushion beneath it, the senior leverage above it, and whether the pref is current-pay or accrued. **None disclosed** → the bull case is "the coupon pays"; the bear case (senior lender forecloses, pref is wiped behind the mortgage) cannot be sized from this email 🔴. A 10% pref that ends up effectively last-dollar exposure is common equity risk at a capped return.

## 3. Where LP Returns Come From

Contractual preferred coupon — capped upside, no stated equity kicker. 100% of the return is the coupon actually being paid and the principal actually being returned at maturity, which depends entirely on the underlying asset's cash flow and refinance/exit — none of which is described. Whether there is a promote sitting above the pref (which would make it equity dressed as preferred, `PREF-01`) is unknown → ask.

## 4. Fee Stack Summary

**Nothing disclosed.** The `02` preferred-equity inventory expects: origination/placement (1–2%), servicing (0.5–1%/yr), possible exit/maturity fee (0.5–1%), possible equity kicker. Zero of these appear.

**Gross-to-net drag: not computable — that is the finding (`GEN-16`).** A 10% headline pref with a 2% origination and 1% annual servicing on a 3-year term is materially less than 10% net; without the schedule the real number is unknowable.

## 5. Red Flags

**YELLOW–RED**
- `GEN-16` — no fee or waterfall/priority disclosure at all; undisclosed fees are still paid → `Q-FEE-01`.
- `GEN-15` — no financials of any kind (no asset, no NOI, no debt terms); the deal can't be underwritten — the absence is a choice → `Q-RISK-03`.

**YELLOW**
- `GEN-03` — marketing-heavy, substance-light: "Exclusive," "limited allocation remaining" urgency, and **wire instructions attached before any diligence document** — urgency standing in for underwriting. The wire-first pattern is also the classic shape of investment-solicitation fraud; treat identity and account verification as a precondition, not a formality → `Q-FEE-01` / demand the PPM (mechanism per `GEN-03`).
- `GEN-17` — essential category disclosures absent across the board (see §6).
- `EQUITY-05` (probe) — cumulative/compounding status of the pref unstated; non-cumulative would be a flag on its own (`02`) → `Q-FEE-04`.
- `PREF-01` (probe) — whether any promote sits above the pref is unstated → `Q-FEE-04`.

No GP-behavior flags can even be evaluated (`GEN-01`, `GEN-02`, `GEN-05` — sponsor unidentified), which is itself the problem.

## 6. Missing Disclosures

Effectively everything the `01`/`02` baselines expect:
- Sponsor identity, entity, and track record (realized, net-to-LP).
- The underlying asset(s): market, unit count, occupancy, T-12, business plan.
- Capital stack: senior debt amount/terms above the pref; common equity below it; the pref's dollar size and attachment point.
- Pref mechanics: cumulative? compounding? current-pay or accrued? maturity/term? redemption and forced-sale rights?
- Fee schedule (origination, servicing, exit) and any kicker or promote above the pref.
- Documents: PPM, subscription agreement, org chart — none referenced.
- GP co-investment; distribution schedule (`GEN-11` subsumed under the general absence).

## 7. GP Alignment

**Unassessable.** The sponsor is not identified, so co-investment, realized track record, waterfall alignment, and affiliate arrangements are all unknown 🔴. An unnamed counterparty requesting a $25k wire is an alignment finding in itself: every alignment question below is a precondition.

## 8. Questions for the GP

**Must-ask**
1. `Q-FEE-01` — Complete fee schedule and full distribution priority. *Bad answer:* "standard market fees"; "the PPM has it" without producing it.
2. `Q-RISK-03` — T-12 actuals, rent roll, and complete debt terms on the underlying asset. *Bad answer:* "financials are confidential until you commit."
3. `Q-FEE-04` — Is the pref cumulative and compounding, and does anything (promote/catch-up) sit above it? *Bad answer:* non-cumulative; a promote above the pref (`PREF-01` confirmed — equity risk dressed as preferred).
4. `Q-GP-02` — Realized, net-to-LP track record on exited deals. *Bad answer:* project-level IRR only; "most deals are still performing."
5. `Q-GP-03` — Any regulatory action, enforcement, or investor litigation? *Bad answer:* "nothing material" deflection; a search surfaces what they didn't disclose.
6. `Q-GP-01` — GP cash in the deal, on what terms? *Bad answer:* "our sweat equity is our investment."
7. `Q-LIQ-01` — Exit options before maturity? *Bad answer:* "a secondary market may develop."
8. `Q-DIST-01` — When does the pref pay — current monthly/quarterly, or accrued to exit? *Bad answer:* no schedule; "when the deal supports it."

**Nice-to-ask:** `Q-LIQ-02` (K-1 timing), `Q-GP-04` (team vs AUM).

## 9. Diligence Checklist

- **Identity first:** verify the sponsor entity exists, who the principals are, and that the wire coordinates belong to a real escrow/fund account — before any other step.
- PPM and subscription docs; state/SEC filing check (Form D).
- Background and regulatory search on principals.
- Underlying-asset verification: title, senior loan terms, appraisal.
- Independent confirmation of the capital stack and the pref's attachment point.

## 10. Verdict

**Pass as presented — insufficient disclosure.** No essential disclosure from the `01`/`02` baselines is present — no sponsor, no asset, no stack position, no fees, no term — so no merits verdict is possible; the 10% coupon is a number floating free of anything that secures it. The solicitation pattern (urgency + wire instructions before documents, `GEN-03`) independently warrants treating this as unverified until the counterparty is proven real.

**Re-screen list:** sponsor identity + realized net-to-LP track record; PPM; capital-stack diagram with senior debt terms and common cushion; pref mechanics (cumulative/compounding/current-pay, maturity); full fee schedule; underlying-asset T-12 and rent roll. **What would have to be true:** a named, verifiable sponsor with realized exits, a pref attaching below ~75% of verified value with a real common cushion, cumulative compounding coupon, and fees that leave the net near the headline. Until then this suits no LP — the only correct action on a wire-instructions-first email is to not wire.
