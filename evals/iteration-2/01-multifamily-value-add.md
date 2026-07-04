# Eval fixture 01 — Sun Belt value-add multifamily syndication
*Iteration-2 run, 2026-07-04, blind generation by fresh-context agent, against SKILL.md (post S1–S3 fixes).*

**Verdict: Pass as presented — insufficient disclosure, and what *is* disclosed is a financing story: the exit cap is underwritten below going-in (`EQUITY-06`), the debt is floating-rate bridge with no cap or maturity disclosed, and the "30% IRR track record" has no stated basis (`GEN-05`).**

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Multifamily — value-add 🟢 |
| Deal type | Equity syndication 🟢 |
| Sponsor | **Not stated** |
| Geography | Sun Belt (metro/submarket **not stated**) 🟢 |
| Minimum investment | **Not stated** |
| Hold | 5 years 🟢 |
| Raise | $50M equity, 280 units 🟢 |
| Claimed return | 16% IRR / 2.0x equity multiple — **gross or net-to-LP not stated** 🔴 |
| Structure | 8% pref, 20% promote, American (deal-by-deal) waterfall 🟢 |
| Debt | Bridge, floating rate — amount, maturity, rate cap all **not stated** |

Routing: `01` multifamily value-add baseline (target net 14–18%, realized cluster 12–15%, hold 5–7 yrs); `02` equity syndication + waterfall; `03` `GEN-`/`EQUITY-` prefixes; `05` VNQ comparator + NCREIF unlevered overlay.

## 2. Return Stress-Test

Swing assumptions: **(a) exit cap** (5.0% underwritten vs 5.5% going-in — ~9% of exit value is assumed cap compression), **(b) rent growth** post-reno in a Sun Belt submarket whose supply pipeline is undisclosed, **(c) floating-rate debt cost / refi** (bridge debt on a 5-year plan almost certainly requires a refi inside the hold 🟡).

- **Base:** 16% as claimed. If 16% is gross, the disclosed fee stack nets to **≈11.4%** (`scripts/fee_drag_calculator.py`, §4). If 16% is already net, the fee schedule implies a gross near 20–21% — top-decile for the category (`01`) and itself a question 🟡.
- **Bull:** rents hit pro forma and compression materializes → 16–18% territory 🟡.
- **Bear:** exit at a flat 5.5% cap removes ~9% of terminal value; on levered equity that plausibly takes several hundred bps off the IRR — and if the bridge refi prices wide or freezes, distributions stop first (the 2022–24 pattern, `GEN-10` mechanism) 🟡. No sensitivity was provided to check any of this (`GEN-13`).

**Benchmark (`05`):** net ≈11.4% vs VNQ 6.47% (10yr) ≈ **+490bps**; the 5-year lock-up hurdle is ~300–400bps → clears numerically 🟡. But the NCREIF NPI unlevered baseline is **4.9%** (2025, almost all income) — roughly 11 points of this deal's claimed return come from leverage and assumed appreciation, not operations. The premium is a leverage-and-exit bet, which is exactly what the unlevered overlay exists to expose (`GEN-07`).

## 3. Where LP Returns Come From

Value-add CoC of 5–8% post-stabilization is the category norm (`01`); no pro-forma cash-flow split is disclosed here. A 2.0x in 5 years with an interior-reno thesis and baked-in cap compression is, by construction, mostly exit-driven — likely above the 60% exit-dependence threshold, but **not decomposable from this disclosure** 🟡 → `GEN-08` suspected, demand the split (`Q-DS-01`). Combined with floating bridge debt and a below-going-in exit cap, the return story is leverage + cap compression, not operations: **financing-story cluster `GEN-07` + `GEN-08` (suspected) + `EQUITY-06`**.

## 4. Fee Stack Summary

| Fee | Stated | `02` range | Read |
|---|---|---|---|
| Acquisition | 2% | 1–2% of equity | Top of range 🟢 |
| Asset management | 1.5%/yr | 1–2% annual | In range 🟢 |
| Disposition | 1% | 0.5–1% of sale price | Top of range 🟢 |
| Promote | 20% over 8% pref | 15–30% over 6–10% | In range 🟢 |
| Loan placement / refi fees | **Not stated** — bridge debt implies at least one financing event, likely a refi | 0.5–1.5% / 0.5–1% per event | Undisclosed layer 🟡 |
| Admin / IR | **Not stated** | 0.1–0.5% | Undisclosed 🟡 |
| Catch-up rate | **Not stated** | — | Ask (`EQUITY-03` probe) |

**Gross-to-net drag ≈ 464bps/yr** on the disclosed stack (16% gross, 5-yr hold, 100% catch-up assumed 🔴): recurring 150bps + one-time 60bps + promote 254bps → **net ≈ 11.4%**. Any refi fee, admin fee, or affiliate layer widens this — those layers are undisclosed, which is itself the finding (`GEN-16` partial).

## 5. Red Flags

**RED**
- `EQUITY-06` — exit cap 5.0% underwritten below the 5.5% going-in cap: unproven cap compression is baked into the headline IRR; at a flat cap the exit price drops ~9% → `Q-EXIT-01`.
- `GEN-07` — financing story: the return rests on leverage (floating bridge) plus cap compression rather than operational value creation; collapses if rates stay up or credit tightens (cluster with `EQUITY-06`, `GEN-08`) → `Q-DS-02`.
- `GEN-05` — "30% IRR track record" with no basis: project- or GP-level IRR presented as a track record; net-to-LP realized is materially lower after fees and promote 🟡 (basis inferred) → `Q-GP-02`. Whether it is realized or marks is also undisclosed (`GEN-14` probe).

**YELLOW–RED**
- `GEN-10` (probe) — floating-rate bridge debt with no rate cap disclosed; if a cap exists and expires before maturity this is the 2022–24 wipeout pattern; treat as RED until answered → `Q-RISK-02`.
- `GEN-09` (probe) / `EQUITY-07` — bridge terms are typically 2–3 years vs a 5-year hold: maturity almost certainly falls inside the plan, making it refi-dependent 🟡 → `Q-RISK-01`, `Q-EXIT-02`.
- `GEN-15` — no rent roll, no T-12, no debt terms: the deal cannot be underwritten from this disclosure → `Q-RISK-03` (`GEN-12` subsumed — trailing financials of any window are absent).

**YELLOW**
- `EQUITY-01`/`EQUITY-02` (probe) — American waterfall disclosed; 20% promote is mid-range so not RED on its own (`03` notes), but clawback is undisclosed — deal-by-deal with no clawback would escalate → `Q-FEE-03`.
- `GEN-13` — single-point projection, no downside case shown → `Q-DS-03`.
- `GEN-11` — 16% IRR quoted with no distribution schedule; can't tell if capital returns before exit → `Q-DIST-01`.
- `GEN-18` — rent-growth thesis in the Sun Belt, where the supply pipeline has been heaviest; no submarket absorption data offered → `Q-MKT-01`.

**Cluster note:** `GEN-07` + `EQUITY-06` (+ suspected `GEN-08`) is the financing-story family firing together — the verdict names it explicitly per `03` notes.

## 6. Missing Disclosures

Against the `01` multifamily value-add essential-disclosure baseline (`GEN-17`):
- Rent roll and **T-12 actuals** — absent.
- Exit-cap **sensitivity** — absent (single-point 5.0% only).
- **Debt structure and maturity** — "bridge, floating" is all we get; no amount, rate, spread, cap terms, maturity, extension options.
- **Refi assumptions** — absent, despite a bridge-debt/5-year-hold mismatch that makes a refi nearly certain.
- GP track record on **prior multifamily exits** (realized, net-to-LP) — absent; a basis-free "30% IRR" is not this.
- Plus (`02` baseline): clawback, catch-up rate, admin/financing fees, distribution schedule, GP co-investment, and whether 16% is gross or net.

## 7. GP Alignment

- **Co-investment:** not stated → `Q-GP-01`; zero co-invest would be `GEN-01` RED.
- **Track record:** "30% IRR across prior deals" — unverified, basis unknown, realized-vs-marked unknown. Under the skepticism contract this is **no validated track record** until restated as realized net-to-LP (`GEN-05`, `GEN-14` probe) 🔴.
- **Waterfall alignment:** deal-by-deal pays the GP per-asset; combined with unknown clawback, GP economics can front-run LP outcomes.
- **Affiliate fees:** property management / construction management arrangements undisclosed → `Q-FEE-02` (`GEN-06` probe).

## 8. Questions for the GP

**Must-ask**
1. `Q-EXIT-01` — Why is the exit cap below going-in, and what's the IRR at a flat exit cap? *Bad answer:* "cap rates will compress" / IRR breaks at a flat cap / no sensitivity offered.
2. `Q-DS-01` — What share of LP IRR is in-place cash flow vs exit, and the IRR at a flat exit cap? *Bad answer:* can't decompose; "real estate always appreciates."
3. `Q-DS-02` — Strip out leverage and cap compression — what's the unlevered in-place return? *Bad answer:* "leverage is just how the deal works"; no unlevered view.
4. `Q-GP-02` — Restate the track record as net-to-LP IRR on fully-realized exits only. *Bad answer:* only project/GP-level IRR; "most deals are still performing."
5. `Q-RISK-01` — When does the bridge debt mature vs the 5-year hold, and what's the refi/extension plan? *Bad answer:* maturity inside the hold with "we'll refinance" and no terms.
6. `Q-RISK-02` — Is there a rate cap, when does it expire vs maturity, and what does extending cost today? *Bad answer:* cap expires before maturity; "rates should be lower by then."
7. `Q-RISK-03` — Provide T-12, rent roll, and complete debt terms. *Bad answer:* T-3/T-6 only; "confidential until you commit."
8. `Q-FEE-03` — Deal-by-deal or whole-of-fund, and is there a clawback? *Bad answer:* deal-by-deal, high promote, no clawback; "you get paid when we get paid."
9. `Q-DIST-01` — Projected distribution schedule and the milestones that gate it. *Bad answer:* "we'll distribute when the deal supports it."
10. `Q-GP-01` — How much GP cash is in, on LP terms? *Bad answer:* "our sweat equity is our investment."
11. `Q-MKT-01` — What submarket supply/absorption data supports the rent growth? *Bad answer:* metro-level optimism; no pipeline acknowledged.
12. `Q-DS-03` — Return under a bear case (flat rents, higher exit cap, no refi)? *Bad answer:* single-point pro forma; "we underwrite conservatively" with nothing shown. *(Escalated from the fired `GEN-13`.)*
13. `Q-EXIT-02` — Does the plan depend on a refinance, and what happens to distributions without it? *Bad answer:* "the refi market will reopen."

**Nice-to-ask:** `Q-FEE-02` (affiliate providers, benchmarked?), `Q-GP-04` (team scale vs AUM), `Q-LIQ-01` (exit options before year 5), `Q-DIST-02` (capital-call mechanics), `Q-LIQ-02` (K-1 timing).

## 9. Diligence Checklist

- PPM / operating agreement: waterfall, clawback, catch-up, full fee schedule.
- Background + regulatory search on the sponsor and principals (SEC/FINRA/state, litigation).
- Independent verification of the claimed track record: settlement statements or audited realized net-to-LP figures.
- Third-party rent comps for post-reno rents; submarket supply pipeline data.
- Appraisal and going-in cap verification; lender term sheet for the bridge (rate, cap, maturity, extensions).
- Sensitivity model: flat exit cap, zero rent growth, refi at current market.

## 10. Verdict

**Pass as presented — insufficient disclosure.** Essential `01` disclosures (T-12, rent roll, debt maturity, refi assumptions, realized track record, exit-cap sensitivity) are absent, so no merits verdict is available. Worse, the disclosed facts already form a financing-story cluster (`GEN-07` + `EQUITY-06`, with `GEN-08` suspected): the biggest swing factor is the **exit cap** — the deal manufactures ~9% of terminal value by assuming compression, financed on floating bridge debt whose cap and maturity you aren't shown. The "30% IRR" track record has no basis and screens as no track record (`GEN-05`).

**Re-screen list:** T-12 + rent roll; full bridge terms (amount, rate, cap expiry, maturity, extensions); refi assumptions; flat-exit-cap sensitivity; realized net-to-LP track record; clawback/catch-up terms; gross-vs-net basis of the 16%; GP co-invest; distribution schedule. **What would have to be true to pursue:** the deal clears its pref at a 5.5% exit cap, the debt survives the hold without a refi at lower rates, and the sponsor shows realized net-to-LP exits in this asset class. Suits no LP as presented; even re-screened, it suits only an LP explicitly underwriting a rate/exit-cap bet, not an income story.
