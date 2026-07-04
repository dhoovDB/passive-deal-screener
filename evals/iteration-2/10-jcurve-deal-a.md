# Eval fixture 10 — J-curve pair, Deal A (front-loaded distributions)
*Iteration-2 run, 2026-07-04, blind generation by fresh-context agent, against SKILL.md (post S1–S3 fixes).*

*Compare-two-deals mode: this file screens Deal A; the head-to-head contrast with Deal B lives in fixture 11 per the pair instruction.*

**Verdict: Pass as presented — insufficient disclosure for a commitment (no sponsor, fees, debt, or market disclosed) — but structurally this is the distribution profile an LP should prefer: 7% cash-on-cash from Year 1 with progressive capital return means roughly half the 14% IRR is realized cash, not a terminal-value bet.**

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Multifamily (subtype **not stated**; 14% IRR + 7% CoC profile reads value-add/core-plus 🟡) |
| Deal type | Equity (syndication presumed 🟡 — structure not stated) |
| Sponsor | **Not stated** |
| Geography | **Not stated** |
| Minimum investment | **Not stated** |
| Hold | **Not stated** ("over the hold"; Deal B's Year-5 exit suggests a comparable ~5yr frame 🟡) |
| Raise | **Not stated** |
| Claimed return | 14% IRR — gross or net **not stated** 🔴 |
| Distributions | 7% cash-on-cash, quarterly, starting Year 1; capital returns progressively over the hold 🟢 |
| Fees / waterfall / debt | **Not stated** |

Routing: `01` multifamily; `02` equity syndication; `03` `GEN-`, `EQUITY-`; `05` VNQ + NCREIF unlevered overlay.

## 2. Return Stress-Test

Swing assumptions: **(a) durability of the 7% CoC** — is it covered by in-place NOI from day one, or does it depend on a rent-growth ramp?; **(b) the exit assumptions behind the residual** ~half of the IRR (exit cap undisclosed); **(c) the undisclosed debt** — a 7% Year-1 CoC on levered multifamily implies either strong in-place yield or aggressive leverage; which one matters enormously.

- **Base:** 14% as claimed — inside the `01` value-add target band (12–18%); if gross, a market-norm fee stack (`02`, ~400–465bps) nets ~9.5–10% 🟡; demand the basis (skepticism rule 2).
- **Bull:** rent growth on top of covered distributions → 14–16%.
- **Bear:** the deal's structural virtue shows here — if the exit disappoints, the LP has already banked ~7%/yr and partial capital back; realized IRR degrades gracefully rather than collapsing. The bear case is a mediocre single-digit outcome, not a zero — *provided* the 7% CoC is real NOI coverage and not return **of** capital dressed as yield 🟡 → verify.
- **Benchmark (`05`):** at 14% net vs VNQ 6.47% ≈ **+750bps**, clearing the ~300–600bps hurdle for a 5–7yr lock-up; at ~10% net-of-assumed-fees ≈ +350bps, thin but passing at a 5yr lock-up 🟡. NPI overlay: unlevered RE runs ~4.9% (income-dominant) — a real 7% cash yield from Year 1 is above unlevered sector income, so either the basis is genuinely good or leverage is amplifying the coupon; the undisclosed debt decides which (`GEN-07` probe) → `Q-DS-02`.

## 3. Where LP Returns Come From

The deal's defining strength: **distribution timing is disclosed and front-loaded.** 7% CoC against a 14% IRR puts roughly half the return in periodic cash flow with capital returning progressively — comfortably below the `GEN-08` 60% exit-dependence threshold 🟡 (split not exactly stated; confirm via `Q-DS-01`). `GEN-11` does **not** fire — this is what the flag's good case looks like. Residual exit dependence (~half) still warrants the flat-exit-cap question, and the leverage question is open until the debt is disclosed.

## 4. Fee Stack Summary

**Nothing disclosed.** Against the `02` equity-syndication inventory (acquisition 1–2%, asset mgmt 1–2%/yr, disposition 0.5–1%, promote 15–30% over 6–10% pref, financing/admin):

**Gross-to-net drag: not computable — that is the finding (`GEN-16`).** Note the interaction with the headline: if 14% is gross, the norm-stack drag (~400–465bps, `02` worked example) lands the LP near 9.5–10% net — a different decision than 14% net. The distribution profile also interacts with the waterfall: with progressive capital return, whether the pref is cumulative and how the promote crystallizes (deal-by-deal vs whole-of-fund is moot for a single asset, but catch-up timing isn't) shapes who keeps the early cash → `Q-FEE-01`, `Q-FEE-04`.

## 5. Red Flags

**YELLOW–RED**
- `GEN-16` — no fee or waterfall disclosure → `Q-FEE-01`.
- `GEN-15` — no rent roll, T-12, or debt terms; the 7% CoC's coverage can't be verified → `Q-RISK-03`.

**YELLOW**
- `GEN-17` — `01` multifamily essentials absent (see §6).
- `GEN-13` — no downside case shown → `Q-DS-03`.
- `GEN-07` (probe) — undisclosed leverage behind an above-unlevered-income cash yield → `Q-DS-02`.
- `EQUITY-06` (probe) — exit cap assumption undisclosed for the exit-dependent residual → `Q-EXIT-01`.
- Return-of-capital ambiguity — "capital returns progressively" is LP-favorable if it's amortization/refi-lite return alongside a covered coupon, but "7% CoC" funded by returning the LP's own capital would overstate yield; not a `03`-listed flag by ID, scored under `GEN-11`'s mechanism (timing transparency) and routed to `Q-DIST-01` 🟡.

No RED flags fire on the stated facts 🟢 — the stated facts are simply few.

## 6. Missing Disclosures

Against the `01` multifamily baseline (`GEN-17`):
- Rent roll and T-12 — absent (is the 7% CoC covered by in-place NOI?).
- Exit cap with sensitivity — absent.
- Debt structure and maturity; refi assumptions — absent.
- GP track record on prior exits — absent.
- Subtype/strategy, market, hold length, raise, minimum.
- Fee schedule, pref, promote, waterfall, clawback (`GEN-16`).
- Whether "capital returns progressively" means amortization, refi proceeds, or asset sales — the mechanics matter.
- Sponsor identity; GP co-invest.

## 7. GP Alignment

**Unassessable on this disclosure** — sponsor unnamed, co-invest unstated (`Q-GP-01`), track record unstated (`Q-GP-02`), waterfall unstated, affiliates unstated (`Q-FEE-02`). One alignment-adjacent positive: a GP that structures and *discloses* early, progressive distributions is at least selling the LP-favorable risk shape rather than a back-loaded IRR story 🟡 — but that is marketing posture until the documents confirm who the waterfall pays first.

## 8. Questions for the GP

**Must-ask**
1. `Q-DS-01` — Exact split of the 14% between in-place cash flow and exit, and the IRR at a flat exit cap. *Bad answer:* can't decompose; the residual turns out to be mostly exit after all.
2. `Q-RISK-03` — T-12, rent roll, complete debt terms — specifically: does in-place NOI cover the 7% CoC from day one? *Bad answer:* the 7% needs Year-2 rent growth; "confidential until you commit."
3. `Q-DIST-01` — Mechanics of "capital returns progressively": amortization, refi, or partial sales — and is any of the 7% return **of** capital? *Bad answer:* the coupon and capital return blur together; no milestone schedule.
4. `Q-FEE-01` — Complete fee schedule and waterfall. *Bad answer:* "standard market fees."
5. `Q-FEE-04` — Pref rate; cumulative and compounding? *Bad answer:* pref <6% or none.
6. `Q-DS-02` — Unlevered, in-place return. *Bad answer:* "leverage is just how the deal works."
7. `Q-GP-02` — Realized net-to-LP track record. *Bad answer:* project-level IRR; unrealized marks.
8. `Q-GP-01` — GP cash co-invest on LP terms. *Bad answer:* "sweat equity."
9. `Q-DS-03` — Bear case: flat rents, higher exit cap, no refi. *Bad answer:* single-point pro forma.
10. `Q-RISK-01` — Debt maturity vs hold. *Bad answer:* maturity inside the hold, "we'll refinance."

**Nice-to-ask:** `Q-EXIT-01` (exit-cap vs going-in — escalates if compression is baked in), `Q-MKT-01` (submarket data), `Q-LIQ-01` (early-exit options), `Q-GP-03` (regulatory), `Q-LIQ-02` (K-1s).

## 9. Diligence Checklist

- PPM/LPA: waterfall, pref mechanics, fee schedule, distribution policy (coupon vs return-of-capital accounting).
- T-12 + rent roll: verify Year-1 CoC coverage from in-place NOI.
- Debt documents: leverage level, rate structure, maturity, amortization.
- Sponsor background/regulatory search; realized-exit verification.
- Exit-cap sensitivity model; submarket comps.

## 10. Verdict

**Pass as presented — insufficient disclosure** — the `01` essentials (T-12, rent roll, debt terms, refi assumptions, track record) are absent, so no commitment-grade verdict is available. But the screen's structural finding stands: a 14% IRR delivered as 7% quarterly cash from Year 1 with progressive capital return is the **front-loaded** risk shape — return realized as it accrues, exit dependence roughly half, graceful degradation in the bear case. Biggest swing factor: **whether in-place NOI actually covers the 7% from day one** — if yes, this profile is as good as the category offers; if the coupon is return-of-capital or rent-growth-dependent, the shape is cosmetic.

**Re-screen list:** T-12/rent roll, debt terms, fee schedule + waterfall, exit-cap sensitivity, capital-return mechanics, sponsor track record, co-invest. **Who it suits (if re-screened clean):** an income-oriented LP who wants current yield and declining capital-at-risk over the hold. **See fixture 11 §Comparison for the head-to-head against Deal B — same headline IRR, opposite risk timing.**
