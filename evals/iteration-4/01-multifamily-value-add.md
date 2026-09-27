# Eval fixture 01 — Sun Belt value-add multifamily syndication
*Iteration-4 run, 2026-09-27, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 1c7faff.*

**Verdict: Pass as presented. This is a financing story. The 16% IRR depends on 50bps of exit-cap compression under floating-rate bridge debt, and nothing about the rate cap is disclosed. At a flat exit cap, the estimated net-to-LP return falls below the illiquidity hurdle for a 5-year lock-up.** Enough is disclosed to underwrite the core return story, so this is a verdict on the merits, not "insufficient disclosure." The deal can be re-opened if the conditions in §10 are met.

Confidence tags: 🟢 stated in the offering or taken from a reference · 🟡 inferred · 🔴 assumed or unverifiable.

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Multifamily, value-add (280 units) 🟢 |
| Deal type | Equity syndication 🟢 |
| Sponsor | **Not stated** |
| Geography | "Sun Belt." **Metro and submarket not stated** |
| Minimum investment | **Not stated** |
| Hold | 5 years 🟢 (bottom of the 5–7 yr category norm, `01`) |
| Raise | $50M equity 🟢 (≈$179k equity per unit). **Purchase price, total capitalization, and renovation budget not stated** |
| Claimed return | 16% IRR / 2.0x equity multiple 🟢. **Gross vs net-to-LP not stated** |
| Structure | 8% pref, 20% promote, American (deal-by-deal) waterfall 🟢. Catch-up, clawback, and whether the pref is cumulative or compounding: **not stated** |
| Caps | Going-in 5.5%, exit 5.0% 🟢 (**exit cap is 50bps below going-in**) |
| Debt | Floating-rate bridge 🟢. LTV/LTC, spread, maturity, extensions, and rate cap (strike, term, expiry): **not stated** |
| Fees | 2% acquisition (basis not stated), 1.5% annual asset management (basis not stated), 1% disposition 🟢 |
| Track record | "30% IRR track record across prior deals." Basis, realized vs unrealized, and deal count **not stated** 🔴 |

## 2. Return Stress-Test

The three assumptions that move this return the most are **(1) the exit cap**, **(2) the floating rate and rate cap on the bridge loan**, and **(3) rent growth from the renovation premium**. The GP gave no sensitivity analysis (`GEN-13`).

To build the table below, I used an illustrative cash-flow shape that reproduces the sponsor's 2.0x / ~16% (15.7% modeled). The inputs are 🔴 assumed because the GP disclosed neither leverage nor a distribution schedule:
- about 65% leverage on a ~$143M capitalization,
- back-loaded operating distributions of ~$12.5M over 5 years,
- the remainder paid at exit.

Only the exit cap changes between rows. I then ran each project-level result through `fee_drag_calculator.py` using the disclosed fee stack. Assumptions in that step: 100% catch-up 🔴, admin fee 0, loan placement fee 0.

| Case | Exit cap | Illustrative deal IRR / multiple | Est. net-to-LP IRR | vs VNQ (4.92%) | 5-yr illiquidity hurdle (300–400bps) |
|---|---|---|---|---|---|
| **Bull (sponsor base)** | 5.0% (50bps compression) | ~16% / 2.0x | **11.36%** if 16% is gross; 16% if already net | +644bps / +1108bps | Clears |
| **Base (flat cap)** | 5.5% (= going-in) | ~11.5% / 1.67x | **7.46%** | +254bps | **Thin / fails** |
| **Bear** | 6.0% (+50bps over going-in) | ~7.4% / 1.40x | **4.86%** | −6bps | **Fails outright.** Below the 10yr Treasury (5.18%) |
| Severe | 6.5% | ~3.4% / 1.17x | below the risk-free rate | — | Fails |

**Readings**
- **The sponsor's return exists only if cap rates compress.** Under this illustrative structure, keeping the exit cap flat at the going-in cap cuts about 4 points of project IRR and removes 0.33x of multiple. After fees, the LP's premium over REITs falls to about 254bps. That is below the ~300–400bps a 5-year lock-up requires (`05` framework). 🟡
- **Treasury floor.** The 10yr Treasury currently yields 5.18%, which is more than VNQ's 4.92% 10-year return (`05`). The flat-cap case earns about 228bps over a risk-free bond while carrying single-asset, floating-rate, illiquid equity risk. 🟢/🟡
- **The table leaves out rate stress.** If the rate cap expires before the exit, debt service rises. That cuts the operating distributions, which are already the smaller share of the return (§3). Rising rates also usually push exit caps up. Both effects hit together, so the bear case is not unlikely. 🟡
- **Which figure is net?** The offering does not say. If 16% is gross, the estimated net of 11.36% is **below** the 12–15% realized range for value-add multifamily (`01`). If 16% is net, it sits in the upper half of the 14–18% *target* band, above what the category usually realizes. Either way, the number depends on the exit cap. 🟢 (`01` ranges)
- **Per-case benchmark results** come from `benchmark_comparator.py`: CLEARS at 16.00% and 11.36% net, THIN/FAILS at 7.46%, FAILS at 4.86%.
- **Dispersion.** Clearing the hurdle is necessary but not sufficient. Private-RE dispersion means the median outcome falls well below the marketed figure, and a single asset carries concentration risk that VNQ diversifies away (`05`).

## 3. Where LP Returns Come From

- **Exit vs cash flow:** In the illustrative model that matches the sponsor's 2.0x, about **75% of total profit ($37.5M of $50M) arrives at exit**. That exceeds the 60% threshold, so the return is exit-dependent (**`GEN-08`**, 🟡 inferred because no distribution schedule was provided, `GEN-11`). A 5-year value-add hold with renovation downtime early on almost always back-loads distributions. The 2.0x / 16% pairing fits that shape.
- **Exit cap:** A 5.0% exit against a 5.5% going-in cap adds roughly 10% to exit value (5.5 / 5.0) before any NOI growth. With leverage, that is a much larger share of exit *equity*. **`EQUITY-06` fires on stated facts** 🟢.
- **Leverage vs operations:** The unlevered overlay in `05` shows NCREIF NPI earning **5.00% trailing total return (income 1.17% of the latest 1.29% quarter; appreciation ≈0)**, and residential **5.3%** in 2025. The sponsor's 16% levered IRR is therefore about **11 points above the unlevered, in-place baseline for institutional real estate**. Those 11 points must come from floating-rate leverage, the renovation premium, and cap compression. Only the renovation premium is operational, and the GP has provided nothing that would size it (no rent roll, T-12, or renovation budget). **`GEN-07` fires** 🟡.
- **Cluster:** `GEN-07` + `GEN-08` + `EQUITY-06` together, plus unhedged floating debt (`GEN-10`), make up the financing-story family that `03` says should be named in the verdict. It is named there.

## 4. Fee Stack Summary

| Fee | Stated | `02` norm | Read |
|---|---|---|---|
| Acquisition | 2%, **basis not stated** | 1–2% of equity, or 0.5–1.5% of purchase price. Aggressive above 2.5% of equity or above 2% of price | Top of range if charged on equity (~$1.0M). **If charged on purchase price, it reaches the aggressive threshold** (2% of an assumed ~$135–145M ≈ $2.7–2.9M, about 5.6% of equity) 🟡 |
| Asset management | 1.5% annual, **basis not stated** | 1–2% of equity annually | In range. ≈$750k/yr and **≈$3.75M over the hold** on $50M raised 🟢. Charging it on invested capital instead would lower it |
| Disposition | 1% of sale price | 0.5–1% of sale price | Top of range. On an illustrative ~$180M exit value that is ~$1.8M, about 3.6% of equity 🟡. Check that it is not charged in addition to a brokerage commission |
| Promote | 20% over 8% pref | 15–30% over 6–10% pref | Mid-market 🟢. **Catch-up not stated.** It moves the drag by about 95bps/yr (see below) |
| Loan placement | **Not stated** | 0.5–1.5% of loan | Bridge debt is being placed, so this fee is probably charged somewhere. **Not disclosed** |
| Refinance | **Not stated** | 0.5–1% of new loan | Likely relevant if the bridge loan is refinanced before exit (§5) |
| Construction management | **Not stated** | 3–5% of hard costs | Typical for heavy value-add. The renovation budget is also not disclosed |
| Admin / IR | **Not stated** | 0.1–0.5% of equity or $1–3k/LP | Not disclosed |

**Gross-to-net drag: ≈464bps/yr** (16.00% gross → 11.36% net). This is the `fee_drag_calculator.py` result using the disclosed fees on an equity basis: recurring 150bps, one-time 60bps, promote 254bps.

- **The figure is a floor.** It assumes a 100% catch-up 🔴 and a zero charge for every undisclosed fee.
- **Catch-up sensitivity:** with no catch-up, drag falls to ≈369bps (net 12.31%).
- **Fee-basis sensitivity:** if acquisition is charged on purchase price and disposition on sale price, drag rises to **≈588bps/yr (net 10.12%)** 🔴. That calculation used illustrative 5.6% and 3.6% equity-equivalents.
- **Drag cannot be computed exactly** until the GP discloses the catch-up, the fee bases, and the missing fee lines (`GEN-16`, partial).

## 5. Red Flags

**RED**
- **`EQUITY-06` — exit cap (5.0%) below going-in cap (5.5%).** The headline IRR assumes 50bps of cap compression that has not happened. LP exposure: at a flat cap, estimated net falls to about 7.5%, below the 5-yr illiquidity hurdle (§2). 🟢
- **`GEN-07` — financing story.** The return sits about 11 points above the ~5% unlevered NPI baseline (`05`), and floating leverage plus cap compression, not demonstrated operations, would have to supply most of that gap. LP exposure: the return depends on the rate path and on exit-market pricing. 🟡
- **`GEN-08` — exit-dependent IRR.** An estimated ~75% of profit arrives at exit, above the >60% threshold. LP exposure: the LP is betting on a year-5 sale price, not collecting income. 🟡
- **`GEN-10` — rate cap on the floating bridge loan is undisclosed.** This is the 2022–24 failure pattern: the cap expires, rates stay high, the refi market freezes, debt service rises, distributions stop, and capital calls follow. A floating bridge loan with no disclosed cap strike or expiry cannot be cleared. LP exposure: loss of distributions, then dilution or a capital call. 🔴 (unverifiable until disclosed; treat as RED until answered)
- **`GEN-05` — "30% IRR track record" is an unverified headline.** The offering does not say whether it is project-level, GP-level, or net-to-LP. A 30% figure is well above the 12–15% realized range for this category (`01`), which suggests it is gross, project-level, or cherry-picked. LP exposure: the sponsor's claimed skill is unproven. 🔴
- **`GEN-14` — realized vs unrealized not distinguished.** "Across prior deals" may include deals still marked at estimated value. Together with `GEN-05`, this forms the RED cluster `03` describes: no validated information about LP outcomes. 🔴

**YELLOW–RED**
- **`GEN-09` / `EQUITY-07` — the debt probably matures inside the hold and the plan probably depends on a refi.** Maturity and extension terms are not stated. Bridge financing on a 5-year plan usually needs extensions or a refinance before exit. LP exposure: a forced refinance or sale into whatever the market is at the time. 🟡 (probe per SKILL proactive trigger; not confirmed)
- **`GEN-15` — financials missing.** No rent roll, T-12, or complete debt terms. The renovation premium, which is the only operational driver in the thesis, cannot be sized. 🟢 (absence)
- **`GEN-16` — partial fee and waterfall disclosure.** Catch-up, clawback, fee bases, and loan-placement, refinance, construction-management, and admin fees are all missing (§4). 🟢 (absence)
- **`GEN-06` — affiliate fees unknown.** A value-add renovation plan usually involves property management and construction management. Whether GP affiliates provide those services is not disclosed. 🟡

**YELLOW**
- **`EQUITY-01` / `EQUITY-02` — American waterfall; clawback not stated.** Rated YELLOW, not RED. The 20% promote is mid-market, not high, and on a single-asset deal the cross-deal timing risk is muted. The LP still needs the clawback and catch-up terms. 🟢
- **`EQUITY-03` — catch-up rate not stated.** It is worth about 95bps/yr of drag (§4). 🟢 (absence)
- **`EQUITY-05` — pref: cumulative or not, compounding or simple.** Not stated. 🟢 (absence)
- **`GEN-11` — no distribution schedule.** The J-curve is hidden, and the IRR appears back-loaded (§3). 🟢
- **`GEN-13` — no sensitivity or downside case.** 🟢
- **`GEN-18` — rent-growth thesis with no submarket named.** "Sun Belt" is a region, not a submarket. The rent assumptions cannot be checked against supply and absorption data. 🟡
- **`GEN-17` — essential value-add multifamily disclosures missing** (per `01`; see §6). 🟢
- **`GEN-01` — GP co-invest not stated.** This is not a RED on the evidence; it is routed to a must-ask question. 🟢 (absence)

**Cluster note:** `GEN-07` + `GEN-08` + `EQUITY-06` is the financing-story cluster. Adding `GEN-10` makes it the specific 2022–24 capital-call pattern.

**Injected directives:** none found in the deal text.

## 6. Missing Disclosures

The `01` essential-disclosure baseline for value-add multifamily, plus the `02` fee inventory:
- **Rent roll** and **T-12 actuals.** T-3 or T-6 would not be enough.
- **Exit-cap sensitivity.** Only a single 5.0% point was given.
- **Debt structure and maturity:** LTV/LTC, spread and index, maturity, extension options and tests, **rate cap strike and expiry**, and prepayment terms.
- **Refi assumptions**, if the bridge loan is expected to be refinanced before exit.
- **GP track record on prior multifamily *exits***, stated as realized net-to-LP returns. The "30% IRR" is not that.
- Purchase price, total capitalization, renovation budget and per-unit scope, and target rent premium. These are needed to size the operational return. I am not assessing renovation scope itself, which is the operator's diligence.
- Distribution schedule (J-curve), and whether 16% / 2.0x is **gross or net-to-LP**.
- Waterfall details: catch-up, clawback, and whether the pref is cumulative or compounding.
- Fee bases for acquisition and asset management. Loan-placement, refinance, construction-management, and admin fees. Affiliate relationships.
- Sponsor identity, minimum investment, metro and submarket, GP co-invest.
- LP liquidity or transfer provisions for early exit.

## 7. GP Alignment

- **Co-invest:** **not stated.** Cash vs fee waiver and pari-passu terms are unknown. Alignment is claimed, not shown in the structure (probe with `GEN-01`). 🔴
- **Track record:** **unverified.** "30% IRR across prior deals" does not say whether it is realized or unrealized, net or gross, or how many deals it covers (`GEN-05`, `GEN-14`). Until the GP restates it as **realized, net-to-LP** results on exited multifamily deals, treat it as **no track record** under the skepticism contract. 🔴
- **Waterfall alignment:** An 8% pref with a 20% promote is market-standard 🟢. The deal-by-deal structure pays the GP promote at this deal's exit, with no clawback disclosed. That structure rewards the GP for the exit-cap bet the LP is underwriting: if cap compression arrives, the GP is paid; if it doesn't, most of the loss falls on the LP. 🟡
- **Fees paid regardless of outcome:** ≈$1.0M acquisition (if on equity) + ≈$3.75M asset management + ≈$1.8M disposition ≈ **$6.5M+ in fees the GP collects whatever the LP's result** 🟡. The fee bases are not stated, and any affiliate fees would add to this (`GEN-06`).

## 8. Questions for the GP

**Must-ask**

| # | Question (`04` ID) | Bad-answer signal |
|---|---|---|
| 1 | **Q-EXIT-01** (EQUITY-06): Why is the exit cap below the going-in cap, and what is the IRR at an exit cap equal to or above 5.5%? | "Cap rates will compress"; the IRR breaks at a flat cap; no sensitivity offered. |
| 2 | **Q-DS-01** (GEN-08, EQUITY-06): What share of projected LP IRR comes from in-place cash flow vs the exit, and what is the IRR at a flat exit cap? | Can't or won't split the IRR; "real estate always appreciates"; the IRR falls below the 8% pref at a flat cap. |
| 3 | **Q-DS-02** (GEN-07): Strip out leverage and cap compression. What is the unlevered, in-place return? | Treats the levered IRR as the only relevant number; "leverage is just how the deal works." |
| 4 | **Q-RISK-02** (GEN-10): When does the rate cap expire relative to debt maturity, and what does it cost to extend at current pricing? | Cap expires before maturity; extension cost not modeled; "rates should be lower by then." |
| 5 | **Q-RISK-01** (GEN-09): When does the bridge loan mature relative to the 5-year hold, and what is the refinance or extension plan? | Maturity falls inside the hold; "we'll refinance" with no terms; no plan if the refi market is shut. |
| 6 | **Q-EXIT-02** (EQUITY-07): Does the plan depend on a refinance, and what happens to distributions if the refi isn't available on the assumed terms? | Capital return requires a refi at lower rates; no fallback; "the refi market will reopen." |
| 7 | **Q-GP-02** (GEN-05, GEN-14): Restate the "30% IRR" as net-to-LP IRR on fully realized, exited deals only. | Offers only project-level or GP-level IRR; "most deals are still performing"; can't separate realized from unrealized. |
| 8 | **Q-GP-01** (GEN-01): How much of your own cash is in this deal, on the same terms as LPs? | "Our sweat equity is our investment"; co-invest is a fee waiver; a token amount on better terms. |
| 9 | **Q-FEE-03** (EQUITY-01, EQUITY-02): Deal-by-deal waterfall. Is there a clawback, and what is the catch-up? | No clawback; can't explain the catch-up; "you get paid when we get paid." |
| 10 | **Q-FEE-04** (EQUITY-05): Is the 8% pref cumulative, and does unpaid pref compound? | Non-cumulative; simple only, with no carry-forward. |
| 11 | **Q-FEE-01** (GEN-16): Provide the complete fee schedule, including fee bases, loan-placement, refinance, construction-management, and admin fees, and the full waterfall. | "Standard market fees"; "the PPM has it" without producing it. |
| 12 | **Q-FEE-02** (GEN-06): Which providers (property management, construction management, loan placement) are GP-affiliated, what do they charge, and are the rates benchmarked? | "All arm's-length" without naming providers; no benchmark. |
| 13 | **Q-RISK-03** (GEN-12, GEN-15): Provide the T-12, current rent roll, and complete debt terms. | T-3/T-6 only; "financials are confidential until you commit." |
| 14 | **Q-DS-03** (GEN-13): What is the return under a bear case with flat rents, a 6.0% exit cap, and no refinance? | A single-point pro forma; "we underwrite conservatively" with nothing to show. |
| 15 | **Q-DIST-01** (GEN-11): What is the projected distribution schedule, and when does LP capital start coming back? | "We'll distribute when the deal supports it"; no milestones. |
| 16 | **Q-MKT-01** (GEN-18): Which submarket is this, and what supply-pipeline and absorption data support the rent-growth assumption? | Metro or "Sun Belt" optimism instead of submarket data; no supply pipeline acknowledged. |
| 17 | **Q-LIQ-01**: What are my options if I need to exit before year 5? | "A secondary market may develop"; vague promises of liquidity. |

**Nice-to-ask**

| Question | Bad-answer signal |
|---|---|
| **Q-GP-04** (GEN-04): How has your team grown alongside AUM? | AUM multiplied while the team stayed flat; no named asset manager. |
| **Q-DIST-02**: When are capital calls expected, and what happens if one is missed? This is more relevant than usual given `GEN-10`. | "Calls as needed"; punitive dilution buried in the documents. |
| **Q-LIQ-02**: When are K-1s delivered? | A history of filing extensions. |
| **Q-GP-03** (GEN-02): Any regulatory action or investor litigation? This is asked as a must-ask in practice because the sponsor is unnamed and cannot be background-checked yet. | "Nothing material"; a search turns up something they didn't disclose. |

## 9. Diligence Checklist

Third-party verification still needed:
- [ ] **PPM and operating agreement.** Check the waterfall text (catch-up, clawback, whether the pref is cumulative), every fee with its basis, and affiliate disclosures.
- [ ] **Loan documents / term sheet.** Check maturity, extension tests, rate cap confirmation (strike, notional, expiry), and required rate-cap replacement reserves.
- [ ] **Sponsor background check.** Search SEC/FINRA/state actions and litigation on the principals (the sponsor is unnamed).
- [ ] **Track record verification.** Get deal-level realized results (net-to-LP) on prior multifamily exits, with investor references from exited deals.
- [ ] **Independent comps.** Check submarket cap rates and recent trades to test the 5.0% exit cap, and submarket rent comps and supply pipeline to test the renovation premium.
- [ ] **Appraisal / purchase price.** Reconcile the price to the 5.5% going-in cap using T-12 NOI rather than pro forma NOI.
- [ ] **Lender confirmation** of loan terms and any lender-required reserves.

## 10. Verdict

**Pass as presented. This is a financing story.**

**Reasoning.** The sponsor's 16% / 2.0x depends on three assumptions all holding at once:
1. cap-rate compression from 5.5% to 5.0% (`EQUITY-06`),
2. an exit-weighted return profile (`GEN-08`),
3. floating-rate bridge debt with no disclosed rate cap or maturity (`GEN-10`, `GEN-09`).

Against a ~5% unlevered NPI baseline, most of the headline comes from leverage and assumed cap compression, not demonstrated operations (`GEN-07`).

With the exit cap held at going-in, the estimated net-to-LP return is about 7.5%. That is ~254bps over VNQ and ~228bps over the 10yr Treasury, which **does not clear** the ~300–400bps illiquidity hurdle for a 5-year lock-up. A 50bps cap *expansion* puts the LP at REIT-level returns (about 4.9%) with single-asset, floating-rate, illiquid risk. The only evidence of sponsor skill is an unverified "30% IRR" (`GEN-05`, `GEN-14`).

**Biggest swing factor.** The exit cap, and the rate environment at exit that drives it. A 50bp move in exit cap moves the illustrative project IRR by about 4 points.

**Who it could suit.** An LP who holds a specific view that Sun Belt multifamily cap rates will compress by 2031, is fine with a back-loaded, exit-weighted return, and can absorb a capital call. That LP should size the investment as a rate bet, not an income allocation.

**What would have to be true to re-open (re-screen conditions).**
1. The GP re-underwrites at an exit cap ≥5.5%, and the net-to-LP IRR still clears ~9–10%. That means ≥400bps over VNQ, at the top of the 5-year hurdle.
2. The rate cap covers the full loan term through maturity, or extension costs are funded in reserves. Debt maturity plus extensions reaches past the planned exit.
3. The GP confirms whether 16% is net or gross and provides a distribution schedule.
4. The track record is restated as **realized, net-to-LP** results on exited multifamily deals.
5. GP cash co-invest is pari-passu with LPs. The catch-up is disclosed. The pref is cumulative.
6. The full fee schedule, with bases and affiliate relationships, is disclosed so drag can be computed exactly. The current screening figure is ≈464bps/yr, and that is a floor.

If conditions 1–2 come back favorably, this could move to **Pursue with conditions**, with conditions 3–6 remaining as the conditions.
