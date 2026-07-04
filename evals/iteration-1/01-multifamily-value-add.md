# Eval fixture 01 — Sun Belt value-add multifamily syndication

*Iteration-1 run, 2026-07-03, against SKILL.md @ cddc52d (9.07KB body). Fixture prompt: evals.json id 1.*

---

**Verdict: Pursue with conditions** — category-normal return target on a classic value-add thesis, but the exit cap is underwritten *below* going-in (baked-in compression), the debt is floating-rate bridge with no rate-cap disclosure, and the "30% IRR track record" is unverified as stated. The biggest swing factor is the exit cap: if the deal can't clear its pref at a flat 5.5% exit, this is a financing story, not an asset story.

## 1. Deal Snapshot
- **Asset class:** Multifamily — value-add 🟢
- **Deal type:** Equity syndication (single asset, 280 units) 🟢
- **Sponsor:** Not stated (name/entity not given)
- **Geography:** Sun Belt (metro not stated) 🟡
- **Minimum investment:** Not stated
- **Hold:** 5 years 🟢
- **Raise:** $50M equity 🟢
- **Claimed return:** 16% IRR / 2.0x EM 🟢 — *gross vs net-to-LP not stated* 🔴
- **Structure:** 8% pref, 20% promote, deal-by-deal (American) waterfall 🟢
- **Debt:** Bridge, floating rate; term, maturity, rate cap all not stated 🔴

## 2. Return Stress-Test
Baseline (`01`): value-add multifamily targets 12–18% net IRR; realized vintages cluster 12–15%. The claimed 16% sits inside the target band but above the realized cluster 🟡.

Swing assumptions (the 2–3 that move this deal):
1. **Exit cap** — underwritten at 5.0% vs 5.5% going-in. Reversing that to a flat 5.5% removes the baked-in appreciation; on a 5-year value-add, that typically costs several hundred bps of IRR. Bear case must be run at ≥5.5%.
2. **Renovated-rent premium** — the entire operational thesis. No rent roll or T-12 provided to validate the delta 🔴.
3. **Rate path / refi** — floating bridge debt over a 5-year plan means at least one refinance or sale into an unknown rate market.

Benchmark (`05`): assuming the 16% is gross, estimated net-to-LP ≈ 11.5–12% (see §4). VNQ 10yr = 6.47% → premium ≈ 500–550bps. For a 5-year lock-up the hurdle is ~300–400bps → **clears the illiquidity hurdle** 🟡 — but see §3: the unlevered overlay says much of that premium is leverage, not alpha.

- Base: ~11.5–12% net (fees applied to claimed gross) 🟡
- Bull: claimed case holds, cap compression materializes → ~13%+ net 🟡
- Bear: flat 5.5% exit cap + elevated rates at refi → mid-single-digit net or pref impairment; not computable from disclosure — that is itself the finding 🔴

## 3. Where LP Returns Come From
Not decomposable from the disclosure — no cash-flow vs exit split given (`GEN-11` fires; see §5). Structural read 🟡: a 2.0x in 5 years with exit-cap compression underwritten means the return is weighted toward exit value, not in-place cash flow. Unlevered overlay (`05`): NCREIF NPI unlevered private RE returned ~4.9% (2025), almost all income — so a 16% levered projection is carrying ~10+ points of leverage and assumed appreciation. **Probable financing-story cluster** (`GEN-07` + `EQUITY-06`, with `GEN-08` unconfirmed pending the Q-DS-01 split). Demand the decomposition before committing.

## 4. Fee Stack Summary
Per `02` (equity syndication inventory), all disclosed fees are in-range; drag on a 5-year hold:

| Fee | Rate | Frequency | Annualized drag |
|---|---|---|---|
| Acquisition | 2% of equity | One-time | ~40bps |
| Asset management | 1.5% annual | Recurring | ~150bps |
| Disposition | 1% | One-time at sale | ~20bps |
| Promote | 20% over 8% pref | Contingent | ~200–220bps at 16% gross |

**Total estimated drag ≈ 410–430bps → net-to-LP ≈ 11.5–12% on the claimed 16%** 🟡 (verify with `scripts/fee_drag_calculator.py`). Not disclosed: loan placement/refi fees (bridge debt makes a refi event likely), admin/IR fees, catch-up rate on the promote. The waterfall's catch-up structure changes the promote drag materially and is unstated 🔴.

## 5. Red Flags
**RED**
- `EQUITY-06` — Exit cap (5.0%) below going-in (5.5%): unproven cap compression baked into the headline IRR. Exposure: the IRR is partly a market-timing bet the LP can't underwrite.
- `GEN-05` — "30% IRR track record" with no basis stated: almost certainly project-level or GP-level, not net-to-LP; fees and promote mean LP realized returns were materially lower. Exposure: the record may not survive restatement.
- `GEN-10` — Floating-rate bridge debt with **no rate-cap disclosure**: the 2022–24 failure pattern (cap expires → rates elevated → refi frozen → debt service erases distributions) cannot be ruled out. Exposure: distribution suspension / capital call.
- `GEN-09` — Bridge debt on a 5-year plan: bridge terms are typically 2–3 years, implying maturity inside the hold. Term not stated — treat as maturity-inside-plan until shown otherwise. Exposure: forced refi/sale into whatever market exists.

**YELLOW**
- `EQUITY-07` (YELLOW–RED) — The renovate-and-raise-rents plan on bridge debt implies a refi to permanent financing; refi terms unstated.
- `GEN-11` — No distribution schedule: 16% IRR with unknown J-curve.
- `EQUITY-01/-02` context — Deal-by-deal waterfall with 20% promote: on a single-asset deal the deal-by-deal vs whole-of-fund distinction is less consequential, and 20%/8% is market-standard (`02`), so not RED here — but clawback status should still be asked.

**Cluster note:** `EQUITY-06` + floating bridge + implied refi = the financing-story family (`GEN-07`). Two confirmed and one probable member — treat the cluster as RED.

## 6. Missing Disclosures
Per `01` (multifamily value-add essential disclosures), this deal omits:
- Rent roll and **T-12 actuals** (`GEN-15` risk; must-ask)
- Exit-cap **sensitivity** (single-point pro forma → `GEN-13`)
- Debt structure detail: term, maturity date, rate cap and its expiry, spread
- Refi assumptions
- GP track record on **prior multifamily exits** (realized, net-to-LP)
- GP co-investment (`GEN-01` unresolvable as disclosed)
- Distribution schedule (`GEN-11`)
- Whether 16%/2.0x is gross or net to LP

## 7. GP Alignment
- **Co-invest:** Not stated 🔴 — must resolve (Q-GP-01).
- **Track record:** "30% IRR across prior deals" — basis unstated; treated as **unverified** per the contract (`GEN-05`; possibly `GEN-14` if it includes unrealized marks). A 30% claim in a category whose realized net clusters 12–15% (`01`) demands restatement, not acceptance.
- **Waterfall alignment:** 8% pref / 20% promote is market (`02`); catch-up and clawback unstated.
- **Affiliate fees:** No disclosure either way — ask (Q-FEE-02).

## 8. Questions for the GP
**Must-ask**
1. **Q-DS-01** — IRR split: in-place cash flow vs exit, and IRR at a *flat 5.5%* exit cap. *Bad answer:* can't decompose; "real estate always appreciates"; IRR collapses below pref at flat cap. (`GEN-08`/`EQUITY-06`)
2. **Q-RISK-02** — Rate cap expiry vs debt maturity, and current cost to extend. *Bad answer:* cap expires before maturity; "rates should be lower by then." (`GEN-10`)
3. **Q-RISK-01** — Debt maturity vs the 5-year hold; refinance/extension plan. *Bad answer:* maturity inside hold with "we'll refinance" and no terms. (`GEN-09`)
4. **Q-GP-02** — Restate track record as net-to-LP on realized exits only. *Bad answer:* only project-level IRR; "most deals are still performing." (`GEN-05`/`GEN-14`)
5. **Q-GP-01** — GP cash co-invest, pari-passu. *Bad answer:* "sweat equity is our investment." (`GEN-01`)
6. **Q-RISK-03** — T-12, rent roll, complete debt terms. *Bad answer:* T-3/T-6 only; "confidential until you commit." (`GEN-12`/`GEN-15`)
7. **Q-DS-03** — Bear case: flat rents, 5.5%+ exit cap, no refi. *Bad answer:* "we underwrite conservatively" with nothing to show. (`GEN-13`)
8. **Q-DIST-01** — Distribution schedule and first-capital-return milestone. *Bad answer:* "we'll distribute when the deal supports it." (`GEN-11`)

**Nice-to-ask** (escalate if the matching flag fires)
- **Q-FEE-03** — Clawback status on the deal-by-deal waterfall; catch-up rate.
- **Q-FEE-02** — Affiliate service providers and benchmarking.
- **Q-LIQ-01** — Early-exit options over the 5-year lock-up.

## 9. Diligence Checklist
- [ ] PPM: full waterfall (catch-up, clawback), complete fee schedule
- [ ] Third-party: rent comps for renovated units in the submarket
- [ ] Lender term sheet: rate, spread, cap terms, maturity, extension options
- [ ] Background/regulatory search on sponsor principals (`GEN-02` unprobed)
- [ ] Appraisal with as-is and post-reno values
- [ ] Sponsor's realized-deal case studies, verified net-to-LP

## 10. Verdict
**Pursue with conditions.** The thesis is category-standard and the disclosed fee stack is in-range; the claimed 16% sits inside the `01` target band and, at estimated ~11.5–12% net, clears the VNQ + illiquidity hurdle for a 5-year lock-up. But the deal as presented leans on unproven cap compression and undisclosed floating-rate debt mechanics — the exact 2022–24 multifamily failure pattern. **Conditions:** (1) IRR still clears the 8% pref at a flat 5.5% exit cap; (2) rate cap covers the debt term or extension is budgeted, and maturity/extension mechanics survive a frozen refi market; (3) track record restated net-to-LP on realized exits. A bad answer on any of the three converts this to **Pass**. Suits an LP who can tolerate a back-loaded, exit-weighted return; wrong for an LP needing early distributions. **Biggest swing factor: the exit cap.**
