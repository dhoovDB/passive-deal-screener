# Eval fixture 10 — J-curve pair, Deal A (front-loaded distributions)
*Iteration-3 run, 2026-07-04, blind generation by fresh-context agent, against SKILL.md (post S1b/S2b fixes).*

**Verdict: Pass as presented — insufficient disclosure (no sponsor, fees, waterfall, debt, or financials), but with the LP-favorable return *shape* on full display: 7% cash-on-cash from Year 1 with progressive capital return means the 14% IRR is mostly realized cash, not a terminal-value bet. Comparison against Deal B follows in the Deal B screen (fixture 11).**

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Multifamily (sub-strategy not stated) 🟡 |
| Deal type | Equity (syndication vs fund not stated) 🟡 |
| Sponsor | Not stated |
| Geography | Not stated |
| Minimum investment | Not stated |
| Hold | Not stated (a multi-year hold implied by "progressively over the hold") 🟡 |
| Raise | Not stated |
| Claimed return | 14% projected IRR — gross or net not stated 🔴 |
| Distributions | 7% cash-on-cash, quarterly, starting Year 1; capital returns progressively over the hold 🟢 |

## 2. Return Stress-Test

Swing assumptions: **durability of the 7% CoC**, **the exit assumption behind the residual**, **whatever debt sits under it (undisclosed)**.

- **Base.** 14% IRR sits inside the `01` multifamily value-add band (12–18% target) and at the top of core-plus (8–12%) — plausible either way, but the sub-strategy is unstated 🟡.
- **Shape.** A 7% CoC paid quarterly from Year 1 plus progressive return of capital means a large share of the IRR is banked as cash along the way — the deal de-risks itself as it goes. If the exit disappoints, the LP has already recovered a meaningful fraction of capital plus income; the bear case erodes the IRR rather than vaporizing it 🟡.
- **Credibility check:** immediate 7% CoC requires genuinely in-place cash flow — `01` puts stabilized value-add CoC at 5–8% *after* stabilization, so 7% from day one implies an already-performing asset (or distribution support from reserves/subscription — verify; distributions funded from capital rather than operations are the classic dressing-up of this profile 🟡).
- **Benchmark (`05`, benchmark_comparator, 5-yr hold assumed 🔴):** 14% vs VNQ 6.47% = **≈753bps premium**, vs a ~300–400bps hurdle → clears comfortably *if net and if delivered*. Basis unstated, so the comparison is conditional.

## 3. Where LP Returns Come From

The disclosed schedule implies: roughly half or more of total return from realized quarterly cash flow and progressive capital return, with the residual at exit — i.e., **below** the 60% exit-dependence threshold, so GEN-08 does *not* fire on the disclosed shape 🟡 (subject to verifying the CoC is from operations, not reserves). GEN-11 does not fire either — the distribution schedule is exactly the disclosure that flag exists to force. Leverage and cap assumptions are undisclosed, so GEN-07 cannot be assessed (unresolved, not fired).

## 4. Fee Stack Summary (`02`)

**Nothing disclosed — GEN-16.** Expect the `02` equity inventory (acquisition 1–2%, asset mgmt 1–2% annual, disposition 0.5–1%, promote 15–30% over 6–10% pref, admin). Whether the 14% and the 7% CoC are before or after that stack changes the LP outcome by hundreds of bps (`02` worked example: a standard stack costs ≈450bps/yr). **Drag not computable — that is the finding.**

## 5. Red Flags (`03`)

**YELLOW / YELLOW–RED**
- **GEN-16** (YELLOW–RED) — no fee or waterfall disclosure.
- **GEN-15** (YELLOW–RED) — no financials: no T-12, rent roll, or debt terms to substantiate a day-one 7% CoC.
- **GEN-17** — `01` essentials absent (§6).
- **GEN-13** — single-point 14%; no downside case.
- Distribution-source risk 🟡 — a schedule this clean invites the question of whether early distributions are operations or return *of* capital dressed as yield (routes to Q-DIST-01/Q-RISK-03).

Affirmatively not fired: **GEN-11** (schedule disclosed) and **GEN-08** (shape is front-loaded, below the 60% threshold on disclosed terms).

## 6. Missing Disclosures (`01` multifamily essentials)

- Rent roll and T-12 (the substantiation for the 7% CoC)
- Debt structure, maturity, rate profile; refi assumptions
- Exit cap with sensitivity; sub-strategy and business plan
- Fee schedule and waterfall (pref, promote, clawback)
- Sponsor identity and realized net-to-LP track record
- Hold period, raise, minimum; gross-vs-net basis of both quoted figures

## 7. GP Alignment

Unassessable 🔴: sponsor unnamed, co-invest unstated (GEN-01 unresolved), track record absent (GEN-05/GEN-14 unresolved), waterfall undisclosed.

## 8. Questions for the GP (`04`)

**Must-ask**
1. **Q-DIST-01** (GEN-11) — confirm the schedule contractually: what gates the 7%, and are early distributions from operations or from reserves/capital? *Bad answer:* distributions are return of capital relabeled as yield; "we'll distribute when the deal supports it."
2. **Q-RISK-03** (GEN-15, GEN-12) — T-12 and rent roll substantiating day-one 7% CoC; complete debt terms. *Bad answer:* withheld; T-3/T-6 only.
3. **Q-FEE-01** (GEN-16) — complete fee schedule and waterfall; are the 14%/7% net of it? *Bad answer:* "standard fees"; basis stays vague.
4. **Q-DS-01** (GEN-08) — decompose the 14%: how much is the quarterly cash vs the exit residual, and the IRR at a flat exit cap. *Bad answer:* can't decompose.
5. **Q-DS-03** (GEN-13) — bear case: flat rents, higher exit cap. *Bad answer:* none.
6. **Q-GP-02** (GEN-05, GEN-14) — realized net-to-LP record. *Bad answer:* project-level IRR only.
7. **Q-FEE-03 / Q-FEE-04** (EQUITY-01/02, EQUITY-04/05) — waterfall type, clawback, pref mechanics. *Bad answer:* deal-by-deal, high promote, no clawback; pref <6% or non-cumulative.
8. **Q-GP-01** (GEN-01) — co-invest. *Bad answer:* sweat equity.

**Nice-to-ask:** Q-RISK-01 (GEN-09 — once debt terms surface), Q-MKT-01 (GEN-18), Q-LIQ-01.

## 9. Diligence Checklist

- PPM: fee stack, waterfall, distribution mechanics (and any right to suspend)
- T-12 + rent roll vs the 7% CoC claim; distribution history if the asset is seasoned
- Debt documents: service coverage at current rates (the quiet threat to a quarterly schedule)
- Sponsor background and realized-track-record verification

## 10. Verdict

**Pass as presented — insufficient disclosure** — the `01` essentials (financials, debt, fees, sponsor) are substantially absent, so the 14% cannot be underwritten yet. But the disclosure that *was* made is the one that usually gets withheld: a concrete distribution schedule showing a front-loaded, self-de-risking return shape (GEN-11 satisfied, GEN-08 not fired). Biggest swing factor: whether the 7% CoC is real operating cash flow, net of fees. **Re-screen list:** T-12/rent roll, debt terms, full fee stack and waterfall, sponsor's realized net-to-LP record, gross/net basis. If those verify, this profile is the LP-preferred way to earn 14%. **Comparison with Deal B — same headline IRR, opposite timing — is in the fixture-11 screen.**
