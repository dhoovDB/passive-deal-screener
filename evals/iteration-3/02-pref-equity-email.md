# Eval fixture 02 — Preferred-equity email solicitation
*Iteration-3 run, 2026-07-04, blind generation by fresh-context agent, against SKILL.md (post S1b/S2b fixes).*

**Verdict: Pass as presented — insufficient disclosure. This is a solicitation, not an offering: no sponsor identity, no asset, no terms, no fees, no financials — and wire instructions attached to a cold email is itself a warning sign. Do not wire anything. Re-screen only against a full package (list in §10).**

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Multifamily (sub-strategy not stated) 🟢 |
| Deal type | Preferred equity 🟢 |
| Sponsor | Not stated |
| Geography | Not stated |
| Minimum investment | $25,000 🟢 |
| Hold / maturity | Not stated |
| Raise | Not stated ("limited allocation remaining" is urgency copy, not a number) |
| Claimed return | 10% preferred return — cumulative/compounding, current-pay vs accrued: not stated |
| Capital-stack position | Not stated |

Nearly every snapshot field is "Not stated" — that is the finding; it all feeds §6.

## 2. Return Stress-Test

There is nothing to stress: no asset, no senior debt figure, no attachment/detachment point in the capital stack, no coverage. What can be said:

- The 10% pref sits inside the `02` typical band for preferred equity (8–12%) 🟢 — not distressed-high (>15%), not under-compensated (<7%).
- **Benchmark (`05`):** 10% vs PFF 3.72% (10yr) = **≈628bps premium** — comfortably above the ~300–400bps illiquidity hurdle for a typical 3–5-year pref hold 🟡 *if the coupon is real, paid, and the position is where "preferred" implies*. None of that is verifiable from this email 🔴.
- Downside: preferred equity fails when the common cushion below it is thin and property cash flow can't cover the accrual. Cushion, coverage, and senior leverage are all undisclosed, so the loss case is unbounded from this disclosure 🔴.

## 3. Where LP Returns Come From

Contractually: a 10% preferred accrual paid from property cash flow ahead of common equity, with return of capital at a refinance or sale. Actually: unknowable — whether this is current-pay or accrued, whether there is an equity kicker, and what takeout event returns capital are all undisclosed. A pref that accrues (rather than pays current) and depends on a future refi for repayment is a materially riskier instrument than the email implies (EQUITY-07 family, unresolved).

## 4. Fee Stack Summary (`02`)

No fee is disclosed — **GEN-16**. Per `02`, preferred equity typically carries: origination/placement 1–2%, servicing 0.5–1% annual, sometimes an exit/maturity fee 0.5–1% and an equity kicker. **Gross-to-net drag is not computable from this disclosure — that is the finding.** A 10% headline pref with a 2% origination and 1% annual servicing is a materially different net.

## 5. Red Flags (`03`)

**YELLOW–RED**
- **GEN-16** — no fee or waterfall/structure disclosure: undisclosed fees are still paid; the net is unknowable.
- **GEN-15** — no financials of any kind: no property, no T-12, no senior debt terms; the deal cannot be underwritten.

**YELLOW**
- **GEN-03** — marketing-heavy, substance-light: "exclusive," "limited allocation remaining," and **wire instructions attached before any diligence materials** — urgency and payment mechanics standing in for underwriting. This pattern (unsolicited, urgency, wire-first) also matches common solicitation-fraud fact patterns 🟡; treat with elevated caution beyond the flag's nominal severity.
- **GEN-17** — essential category disclosures absent across the board (see §6).
- **EQUITY-05 / PREF-01 (unresolved)** — cumulative/compounding status and whether anything sits above the pref are undisclosed; per `02`, non-cumulative pref is a flag on its own, and a promote above a pref means equity risk dressed as preferred.

## 6. Missing Disclosures (`01`/`02` baseline)

Everything the category normally discloses:
- Sponsor identity and track record (realized, net-to-LP)
- Property: asset, location, sub-strategy, T-12, rent roll
- Capital stack: senior debt amount/terms, position of this pref, common equity cushion below it
- Pref mechanics: cumulative? compounding? current-pay vs accrued? maturity/takeout event?
- Fees: origination, servicing, exit fee, any kicker (`02` pref inventory)
- Hold/maturity, total raise, use of proceeds
- Offering documents: PPM, subscription agreement (an email with wire instructions is not an offering package)

## 7. GP Alignment

Nothing to assess: sponsor unnamed, co-invest unstated (GEN-01 unresolved), track record absent (GEN-05/GEN-14 unresolved). **Alignment is entirely unverified 🔴.**

## 8. Questions for the GP (`04`)

All must-ask — this deal is 100% questions:
1. **Q-FEE-01** (GEN-16) — complete fee schedule and structure documents. *Bad answer:* "standard market fees"; "the PPM has it" without producing it.
2. **Q-RISK-03** (GEN-15) — T-12, rent roll, complete senior debt terms. *Bad answer:* "confidential until you commit."
3. **Q-FEE-04** (EQUITY-04, EQUITY-05, PREF-01) — is the 10% pref cumulative and compounding, and does anything sit above it? *Bad answer:* non-cumulative; a promote above the pref.
4. **Q-GP-02** (GEN-05, GEN-14) — realized, net-to-LP track record. *Bad answer:* project-level IRR only; unrealized marks.
5. **Q-GP-03** (GEN-02) — regulatory/enforcement/litigation history. *Bad answer:* "nothing material" deflection.
6. **Q-GP-01** (GEN-01) — GP cash in the deal, same terms. *Bad answer:* "our sweat equity is our investment."
7. **Q-EXIT-02** (EQUITY-07) — does repayment of the pref depend on a refinance? *Bad answer:* "the refi market will reopen."
8. **Q-DIST-01** (GEN-11) — is the pref current-pay, and on what schedule? *Bad answer:* no timing; accrual-only with no milestone.
9. **Q-LIQ-01** — exit options before maturity. *Bad answer:* vague secondary-market promises.

## 9. Diligence Checklist

- Obtain the PPM and subscription docs before any further conversation — no wire on any timeline until then
- Independent sponsor verification: identity, SEC/FINRA/state registration and enforcement search, litigation search
- Verify the underlying property exists and its capital stack (title, senior lender)
- Confirm the offering is a registered exemption (Form D on EDGAR) — a legitimate 506(b)/(c) raise leaves a paper trail
- Counsel review of pref mechanics (cumulative, compounding, remedies on missed pref)

## 10. Verdict

**Pass as presented — insufficient disclosure.** The essential disclosures for this category are *substantially* absent — there is no sponsor, asset, capital stack, fee, or document to underwrite; the only hard facts are a coupon, a minimum, and wire instructions, and the urgency-plus-wire-first pattern is itself the strongest signal here (GEN-03). Biggest swing factor: whether a real offering package exists at all. **Re-screen list:** PPM with full fee schedule and pref mechanics; property-level financials (T-12, rent roll) and senior debt terms; capital-stack position and common cushion; sponsor identity with realized net-to-LP track record and clean regulatory history; maturity/takeout terms. If that package arrives, this re-screens as an ordinary preferred-equity deal — the 10% coupon itself is in market range. Until then, no funds move.
