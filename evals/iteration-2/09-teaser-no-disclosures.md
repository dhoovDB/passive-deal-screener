# Eval fixture 09 — Multifamily fund teaser ("15%+ returns")
*Iteration-2 run, 2026-07-04, blind generation by fresh-context agent, against SKILL.md (post S1–S3 fixes).*

**Verdict: Pass as presented — insufficient disclosure. Four sentences and one unanchored number: "15%+ returns" with no basis (IRR? cash-on-cash? gross or net?), no sponsor, no fees, no term, no track record. A teaser this sparse scores almost entirely on what it withholds — which is everything the `01`/`02` baselines require.**

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Multifamily (subtype **not stated** — "15%+" implies value-add or higher risk 🟡) |
| Deal type | Fund (blind pool? number of assets? **not stated**) 🟢 |
| Sponsor | **Not stated** |
| Geography | **Not stated** |
| Minimum investment | $100,000 🟢 |
| Hold | **Not stated** |
| Raise / fund size | **Not stated** |
| Claimed return | "15%+ returns" — metric undefined (IRR? multiple? CoC?), gross-or-net unstated 🔴 |
| Structure / fees / debt | **Not stated** |
| Investor gate | Accredited only 🟢 (a regulatory posture, not a diligence signal) |

Routing: `01` multifamily (value-add band as the closest analog 🟡); `02` equity/fund; `03` `GEN-`; `05` VNQ + NCREIF overlay. Thin input is the missing-disclosures case per the SKILL — screened in full, not bailed on.

## 2. Return Stress-Test

There is nothing to stress — no metric definition, no hold, no leverage, no fee stack. What the number *permits* as screening arithmetic:

- If "15%+" means **net IRR**: it sits at the top of the `01` value-add target band (12–18% target; realized clusters 12–15%) — i.e., the marketing quotes the top of the category's realized experience as its floor 🟡.
- If it means **gross IRR**: a market-norm fee stack (`02` worked example: ~400–465bps drag) nets it to ~10–11% — inside but not above the ordinary category outcome 🟡.
- If it means cash-on-cash or "average annual return," it is not comparable to anything without a schedule (`GEN-11`).
- **Benchmark (`05`):** taken at face as 15% net vs VNQ 6.47% ≈ +850bps — clears any lock-up hurdle *if real*; taken as ~10.5% net-of-fees vs VNQ ≈ +400bps — clears a 5–7yr hurdle (~400–600bps) only at the low edge. The claim's entire benchmark meaning depends on the undisclosed basis 🔴. NPI overlay: unlevered RE earned 4.9% in 2025 — any 15% figure is predominantly leverage/appreciation, so the financing-story question (`GEN-07`) is open until the pro forma exists.

## 3. Where LP Returns Come From

Unknowable — no cash-flow split, no leverage, no business plan (`GEN-11`; `GEN-07`/`GEN-08` unassessable). "Targeting 15%+" with no distribution schedule is precisely the pattern the proactive trigger list flags: IRR with no distribution schedule → `GEN-11` → `Q-DIST-01`.

## 4. Fee Stack Summary

**Nothing disclosed.** Against the `02` inventory (acquisition 1–2%, asset mgmt 1–2%/yr, disposition 0.5–1%, promote 15–30% over 6–10% pref, financing and admin fees — plus fund-level layers if this is a fund-of-deals wrapper, +50–150bps/yr):

**Gross-to-net drag: not computable — that is the finding (`GEN-16`).** "15%+ returns" is unfalsifiable until the fee schedule and waterfall define what an LP would actually keep.

## 5. Red Flags

**YELLOW–RED**
- `GEN-16` — no fee or waterfall disclosure of any kind → `Q-FEE-01`.
- `GEN-15` — no financials, assets, or debt terms; there is nothing to underwrite → `Q-RISK-03`.

**YELLOW**
- `GEN-03` — marketing-heavy, substance-light: an unanchored "15%+," an accreditation gate as social proof, and "contact us to learn more" in place of any underwriting detail → `Q from GEN-03`: full underwriting model and historical actuals.
- `GEN-17` — every `01` essential disclosure absent (see §6).
- `GEN-11` — return quoted with no distribution schedule → `Q-DIST-01`.
- `GEN-13` — no scenarios of any kind (a single marketing number is less than a single-point pro forma) → `Q-DS-03`.

GP-behavior flags (`GEN-01`, `GEN-02`, `GEN-05`, `GEN-14`) are unassessable — the sponsor is unnamed. For a $100k-minimum commitment, that is the loudest absence on the page.

## 6. Missing Disclosures

Effectively the entire `01` multifamily baseline (`GEN-17`):
- Sponsor identity and **realized net-to-LP track record**.
- Fund structure: blind pool vs identified assets; number of deals; diversification.
- Subtype and strategy (core-plus? value-add? development exposure?) — the risk tier is unknowable.
- Hold period / fund term / lock-up.
- Return metric definition and gross-vs-net basis.
- Complete fee schedule and waterfall (pref, promote, catch-up, clawback).
- Leverage policy; debt terms; rate-hedging approach.
- Rent rolls / T-12s for any seeded assets.
- Target markets and submarket data.
- Distribution schedule; capital-call mechanics; redemption/liquidity terms.
- PPM or any offering document.

## 7. GP Alignment

**Unassessable** — the GP is anonymous in the teaser. Co-investment, track record basis, waterfall alignment, affiliates: all unknown 🔴. Screening discipline: an unnamed sponsor soliciting $100k minimums has provided no alignment evidence at all; every `04` GP question below is a precondition, not a follow-up.

## 8. Questions for the GP

**Must-ask**
1. `Q-FEE-01` — Complete fee schedule and full distribution waterfall. *Bad answer:* "standard market fees"; "the PPM has it" without producing it.
2. `Q-GP-02` — Track record as net-to-LP IRR on fully-realized, exited deals only. *Bad answer:* project-level or GP-level IRR; "most deals are still performing."
3. What does "15%+" mean — net-to-LP IRR? Over what hold? (basis question required by skepticism rule 2, routed via `Q-FEE-01`/`Q-DS-01`). *Bad answer:* the metric keeps shifting (IRR in one breath, "average annual" in the next).
4. `Q-RISK-03` — T-12s, rent rolls, and complete debt terms for current/seeded assets. *Bad answer:* "confidential until you commit."
5. `Q-GP-01` — GP cash co-invested, on LP terms? *Bad answer:* "our sweat equity is our investment."
6. `Q-GP-03` — Regulatory action, enforcement, or investor litigation? *Bad answer:* "nothing material."
7. `Q-DS-03` — The downside case behind the 15%+. *Bad answer:* no downside exists; "we underwrite conservatively" with nothing to show.
8. `Q-DIST-01` — Projected distribution schedule and the milestones gating it. *Bad answer:* "we'll distribute when the fund supports it."
9. `Q-LIQ-01` — Exit options before fund end. *Bad answer:* "a secondary market may develop."

**Nice-to-ask:** `Q-GP-04` (team vs AUM), `Q-DIST-02` (capital-call mechanics), `Q-LIQ-02` (K-1 timing), `Q-MKT-01` (submarket data — escalates once target markets are named).

## 9. Diligence Checklist

- Obtain the PPM before any further engagement — no document, no conversation of substance.
- Identify the sponsor entity and principals; background + regulatory search (SEC/FINRA/state; Form D filings).
- Verify any claimed track record against realized, third-party-verifiable exits.
- Fee schedule and waterfall review against the `02` inventory.
- Asset-level financials for anything already in the fund.
- Confirm fund administration, audit, and custody arrangements.

## 10. Verdict

**Pass as presented — insufficient disclosure.** Every essential disclosure in the `01` baseline is absent; the single number offered has no defined metric, basis, or term, so it cannot even be benchmarked honestly (§2 runs both readings and they land in different decisions). This is the canonical teaser: it exists to start a funnel, not to inform a commitment — screen it as withholding, per the missing-disclosures contract.

**Re-screen list:** PPM; sponsor identity + realized net-to-LP record; metric/basis/hold behind "15%+"; full fee schedule and waterfall; leverage policy and debt terms; asset-level financials; distribution schedule; liquidity terms. **What would have to be true to pursue:** a named sponsor with verified realized exits, a defined net-to-LP target with its downside case, and a fee stack whose drag leaves the net clearing VNQ + a 400–600bps lock-up premium. **Who it suits:** no one at this stage — the correct next step costs nothing: request the PPM and re-screen.
