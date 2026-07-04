# Eval fixture 01 — Sun Belt value-add multifamily syndication
*Iteration-3 run, 2026-07-04, blind generation by fresh-context agent, against SKILL.md (post S1b/S2b fixes).*

**Verdict: Pursue with conditions — this is a financing story until proven otherwise (GEN-07 + GEN-08 + EQUITY-06 cluster), and the "30% IRR" track record is unusable as stated (GEN-05); the exit-cap assumption is the biggest swing factor.**

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Multifamily — value-add (Sun Belt) 🟢 |
| Deal type | Equity syndication 🟢 |
| Sponsor | Not stated |
| Geography | Sun Belt (metro/submarket not stated) |
| Minimum investment | Not stated |
| Hold | 5 years 🟢 |
| Raise | $50M equity, 280 units 🟢 |
| Claimed return | 16% IRR / 2.0x equity multiple — **gross or net to LP not stated** 🔴 |
| Structure | 8% pref, 20% promote, American (deal-by-deal) waterfall 🟢 |
| Debt | Bridge, floating rate; maturity, rate cap, and LTV not stated |

Unstated fields feed §6.

## 2. Return Stress-Test

Swing assumptions: **exit cap**, **rent growth on renovated units**, **floating-rate path / refi availability**.

- **Base.** If the 16% is gross deal IRR, the disclosed fee stack nets to LP **≈11.4%** (fee-drag model: 464bps/yr total drag — §4). Within the `01` value-add target band (12–18% target; realized clusters 12–15%) only at the claimed gross 🟡.
- **Bear.** The pro forma bakes in 50bps of cap compression (5.5% in → 5.0% out). At a flat 5.5% exit cap, terminal value drops ≈9% before any NOI shortfall 🟡 — on a 5-year, exit-heavy profile that plausibly pushes LP net toward or below the 8% pref. No sensitivity was provided (GEN-13), so this is the LP's math, not the sponsor's.
- **Bull.** Renovation premium achieved plus further compression — this is what 16% already assumes; there is little upside left that isn't in the headline.
- **Benchmark (`05`).** Est. net 11.4% vs VNQ 6.47% (10yr) = **≈490bps premium**; the 5-year lock-up hurdle is ~300–400bps → **clears, if the deal delivers gross** 🟡. Unlevered overlay: NCREIF NPI 2025 total return was 4.9%, nearly all income — so roughly two-thirds of this deal's claimed return is leverage plus assumed appreciation, not in-place operations (grounds GEN-07).

## 3. Where LP Returns Come From

2.0x over 5 years with value-add cash-on-cash typically 5–8% post-stabilization (`01`) implies cumulative distributions of perhaps 0.25–0.35x, leaving **~65–75% of total profit at exit** 🟡 — over the 60% threshold → **GEN-08 fires**. The exit itself rests on a compressed cap (**EQUITY-06**) and the capital structure is floating-rate bridge debt (**GEN-07** — leverage + cap compression, not operations). This is the financing-story cluster; the verdict names it.

## 4. Fee Stack Summary (`02`)

| Fee | Deal | `02` norm | Read |
|---|---|---|---|
| Acquisition | 2% | 1–2% of equity | Top of range 🟢 |
| Asset management | 1.5%/yr | 1–2% annual | In range 🟢 |
| Disposition | 1% | 0.5–1% of sale price | Top of range 🟢 |
| Promote | 20% over 8% pref | 15–30% over 6–10% | In range 🟢 |
| Loan placement | Not disclosed | 0.5–1.5% typical on debt-financed deals | Absent or undisclosed 🟡 |
| Catch-up / tiers / clawback | Not disclosed | — | Feeds §6 |

**Total drag (fee_drag_calculator, 16% gross, 5-yr hold): ≈464bps/yr — 150 recurring + 60 one-time + 254 promote → est. net-to-LP ≈11.4%.** If 16% is already net, the sponsor must show the gross and the bridge from one to the other (skepticism rule: never gross-to-gross).

## 5. Red Flags (`03`)

**RED**
- **EQUITY-06** — exit cap (5.0%) below going-in (5.5%): 50bps of unproven cap compression is baked into the headline IRR; LP eats the gap if the market doesn't oblige.
- **GEN-07** — financing story: with the unlevered private-RE baseline at ~4.9% (`05` overlay), the bulk of the 16% is leverage and assumed appreciation; it collapses if rates stay up or credit tightens.
- **GEN-08** — exit-dependent IRR: est. 65–75% of profit arrives at sale 🟡; the return is a future-sale bet, not income. (GEN-07 + GEN-08 + EQUITY-06 = the financing-story cluster.)
- **GEN-05** — "30% IRR track record across prior deals": no basis stated — project-level or GP-level IRR is not net-to-LP, and realized vs unrealized is unstated (GEN-14 unresolved until answered).
- **GEN-09 / GEN-10 (unresolved, treat as RED until answered)** — floating-rate *bridge* debt on a 5-year hold: bridge terms typically run well short of 5 years, so maturity almost certainly sits inside the business plan 🟡, and no rate cap is disclosed at all. This is the 2022–24 failure pattern's exact setup.

**YELLOW**
- **GEN-15 / GEN-12** (YELLOW–RED) — no rent roll, no T-12, no debt terms disclosed.
- **EQUITY-02** — clawback not disclosed in a deal-by-deal waterfall (RED if confirmed absent alongside the promote).
- **EQUITY-05** — pref stated but cumulative/compounding status not disclosed.
- **GEN-11** — 16% IRR quoted with no distribution schedule.
- **GEN-13** — single-point pro forma; no downside case.
- **GEN-18** — Sun Belt value-add rent-growth assumption with no submarket supply/absorption support; several Sun Belt metros carry heavy delivery pipelines 🟡.

## 6. Missing Disclosures (`01` value-add essentials + `02`)

- Rent roll and T-12 actuals (essential per `01`)
- Exit-cap sensitivity (essential per `01`; doubly so given EQUITY-06)
- Debt structure: maturity, LTV, rate-cap terms and expiry, refi assumptions (essential per `01`)
- GP track record on **prior multifamily exits**, realized, net-to-LP (essential per `01`)
- Whether 16% is gross or net to LP
- Waterfall detail: catch-up rate, split tiers, clawback; pref cumulative/compounding
- Loan placement fee; any affiliate fees (GEN-06 unverified)
- Distribution schedule; GP co-invest; minimum; sponsor identity

## 7. GP Alignment

- **Co-invest:** not stated → GEN-01 unresolved; ask Q-GP-01.
- **Track record:** "30% IRR" with no basis is marketing, not evidence — not net-to-LP, not confirmed realized (GEN-05; GEN-14 pending). **Unverified.**
- **Waterfall alignment:** deal-by-deal with undisclosed clawback tilts GP-favorable if clawback is absent (EQUITY-01/EQUITY-02 pending).
- **Affiliate fees:** no disclosure either way (GEN-06 pending).

## 8. Questions for the GP (`04`)

**Must-ask**
1. **Q-DS-01** (GEN-08, EQUITY-06) — share of IRR from exit vs cash flow; IRR at a flat exit cap. *Bad answer:* can't decompose; "real estate always appreciates"; IRR collapses below pref at flat cap.
2. **Q-EXIT-01** (EQUITY-06) — why exit cap below going-in; IRR at exit cap ≥ going-in. *Bad answer:* "cap rates will compress"; no sensitivity offered.
3. **Q-DS-02** (GEN-07) — unlevered, in-place return. *Bad answer:* "leverage is just how the deal works"; no unlevered view exists.
4. **Q-RISK-01** (GEN-09) — debt maturity vs the 5-year hold; extension/refi plan. *Bad answer:* maturity inside the hold with "we'll refinance" and no terms.
5. **Q-RISK-02** (GEN-10) — rate cap expiry vs maturity; cost to extend at current pricing. *Bad answer:* cap expires before maturity; "rates should be lower by then."
6. **Q-GP-02** (GEN-05, GEN-14) — track record restated as net-to-LP on realized exits only. *Bad answer:* only project-/GP-level IRR; "most deals are still performing."
7. **Q-RISK-03** (GEN-12, GEN-15) — T-12, rent roll, complete debt terms. *Bad answer:* "confidential until you commit."
8. **Q-FEE-03** (EQUITY-01, EQUITY-02) — deal-by-deal confirmed; clawback and how secured. *Bad answer:* deal-by-deal, high promote, no clawback.
9. **Q-FEE-04** (EQUITY-04, EQUITY-05) — pref cumulative and compounding? *Bad answer:* non-cumulative.
10. **Q-DS-03** (GEN-13) — bear case: flat rents, higher exit cap, no refi. *Bad answer:* "we underwrite conservatively," nothing to show.
11. **Q-MKT-01** (GEN-18) — submarket supply pipeline and absorption behind the rent-growth assumption. *Bad answer:* metro-level optimism.
12. **Q-GP-01** (GEN-01) — GP cash co-invest, same terms. *Bad answer:* "our sweat equity is our investment."
13. **Q-DIST-01** (GEN-11) — distribution schedule and capital-return milestones. *Bad answer:* IRR with no timing.
14. **Q-LIQ-01** — early-exit options. *Bad answer:* vague "a secondary may develop."

**Nice-to-ask:** Q-FEE-02 (GEN-06 — affiliate providers, escalate if any surface), Q-DIST-02, Q-LIQ-02.

## 9. Diligence Checklist

- PPM: full waterfall (catch-up, tiers, clawback), complete fee schedule, loan placement fee
- Loan documents / term sheet: maturity, extensions, rate-cap confirmation and expiry
- Third-party: sponsor background + SEC/FINRA/state check; verify the "30% IRR" against realized deal records
- Market: submarket rent comps, supply pipeline, absorption (independent of sponsor materials)
- Appraisal / cap-rate comps for going-in 5.5% and the exit assumption

## 10. Verdict

**Pursue with conditions.** The fee stack is in market range and the estimated net (~11.4%) clears the VNQ-plus-illiquidity hurdle *if the gross is real* — but the return quality is the problem: the headline depends on 50bps of assumed cap compression, high floating-rate leverage, and a mostly-at-exit profit profile (GEN-07/GEN-08/EQUITY-06 — a financing story), and the track-record claim is unusable as stated. **Biggest swing factor: the exit cap.** Conditions before any commitment: (1) IRR holds above the pref at a flat-to-higher exit cap; (2) debt maturity/rate-cap terms shown to survive the hold; (3) track record restated as realized net-to-LP; (4) T-12 + rent roll + waterfall detail delivered. Suits an LP who wants levered Sun Belt value-add beta and can absorb an exit miss; it must be true that the submarket keeps absorbing supply and the 2027–31 exit market pays a 5.0% cap. A bad answer on Q-DS-01 or Q-EXIT-01 converts this to Pass.
