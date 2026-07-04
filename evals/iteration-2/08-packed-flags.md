# Eval fixture 08 — Multifamily syndication, stacked structural REDs
*Iteration-2 run, 2026-07-04, blind generation by fresh-context agent, against SKILL.md (post S1–S3 fixes).*

**Verdict: Pass. Six independent RED flags fire on the stated facts alone — zero GP co-invest (`GEN-01`), a prior SEC action (`GEN-02`), a 50% promote in a deal-by-deal waterfall (`EQUITY-01`) with no clawback (`EQUITY-02`), a rate cap expiring ~2 years before loan maturity (`GEN-10`, the 2022–24 wipeout pattern), and an all-unrealized track record (`GEN-14`). Any one is pass-or-resolve; together they are not resolvable by better answers.**

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Multifamily (subtype **not stated**; value-add presumed 🟡) |
| Deal type | Equity syndication, single asset 🟢 |
| Sponsor | **Not stated** by name; zero co-invest; one principal named in a prior SEC action 🟢 |
| Geography | **Not stated** |
| Minimum investment | **Not stated** |
| Hold | **Not stated** (loan matures 2028 → business plan runs at least ~2 more years 🟡) |
| Raise | **Not stated** |
| Claimed return | **Not stated** — "projections show only an upside case" |
| Structure | American (deal-by-deal) waterfall, **50% promote**, no clawback; pref **not stated** 🟢 |
| Debt | Floating rate; rate cap expires in ~12 months (≈ mid-2027); loan matures 2028 🟢 |
| Track record | All current, unrealized marks 🟢 |

Routing: `01` multifamily; `02` equity + waterfall; `03` `GEN-`, `EQUITY-`; `05` VNQ + NCREIF unlevered overlay.

## 2. Return Stress-Test

No return figure, hold, or pro forma is disclosed, so no base case exists to stress — only an "upside case" is shown, which is `GEN-13` by definition. The stress that *can* be run is on the debt, because those facts are stated:

- **The cap-expiry gap:** the rate cap dies ~12 months out; the loan matures in 2028 — roughly a 2-year window of uncapped floating exposure 🟢. This is the exact 2022–24 sequence in `03` (`GEN-10`): *cap expires → rates stay elevated → refi frozen → debt service spikes and erases distributions*. In the bear case the LP's first losses arrive as suspended distributions and a capital call **before** any exit math matters.
- **Waterfall asymmetry:** at a 50% promote in a deal-by-deal structure with no clawback, the GP's share of any upside is extreme, and in the downside the GP — with zero capital in — loses nothing it ever had at risk. The LP return distribution is truncated on top and unprotected on the bottom 🟢.
- **Benchmark (`05`):** no claimed return to compare, which is itself the finding. For orientation: the category's realized net band is 12–15% (`01`) vs VNQ 6.47% — but a 50% promote makes reaching even the category net band arithmetically hostile: the gross required for the LP to net 12–15% through a 50/50 residual split is far above what multifamily produces (NPI unlevered 4.9%, `05`) 🟡. The structure, not the asset, caps the LP.

## 3. Where LP Returns Come From

Not determinable — no cash-flow or exit split is disclosed (`GEN-11`; only an upside case exists). Structurally: single-asset equity behind floating-rate debt whose cap expires mid-plan means the *loss* side is financing-driven even if the *return* side were operational — the LP is short the rate market for ~2 years without a hedge (`GEN-10`; `GEN-07` probe pending the actual pro forma) → `Q-DS-01`, `Q-DS-02`.

## 4. Fee Stack Summary

**No fees disclosed** (`GEN-16`) — acquisition, asset management, disposition, financing, admin: all unstated against the `02` inventory. What *is* disclosed is the waterfall economics, and it is off the chart:

| Item | Stated | `02` range | Read |
|---|---|---|---|
| Promote | **50%** | 15–30% typical; **>30% = aggressive threshold** | ~1.7x the top of the aggressive line 🟢 |
| Preferred return | **Not stated** | 6–10%; pref <6% or none = `EQUITY-04` | Unknown — if none, YELLOW–RED on its own |
| Catch-up | Not stated | 100% catch-up = `EQUITY-03` | Unknown |
| Waterfall type | Deal-by-deal, no clawback | Clawback absence in deal-by-deal = major flag | Fired (`EQUITY-01` + `EQUITY-02`) |

**Gross-to-net drag: not computable (no fee schedule, no pref, no gross figure) — that is the finding.** Directionally, a 50% promote alone is the largest single drag element the `02` framework contemplates; at any plausible gross, the LP keeps a minority of the profit above the (unstated) pref.

## 5. Red Flags

**RED**
- `GEN-01` — zero GP co-investment; "our expertise is our investment" is verbatim the `Q-GP-01` bad-answer signal, offered unprompted. Fees and 50% promote with no capital at risk → `Q-GP-01`.
- `GEN-02` — a principal named in a prior SEC action; pattern-of-harm risk that no deal term offsets → `Q-GP-03`.
- `EQUITY-01` — deal-by-deal waterfall **with** a 50% promote (well past the `02` >30% aggressive threshold); per `03` notes, deal-by-deal is RED precisely when paired with high promote and no clawback — both present → `Q-FEE-03`.
- `EQUITY-02` — no clawback in that deal-by-deal structure: the GP keeps promote even if the LP is later impaired (single-asset here, but the same one-way ratchet) → `Q-FEE-03`.
- `GEN-10` — rate cap expires ~12 months out, loan matures 2028: ~2 years of uncapped floating exposure, the named 2022–24 failure mode → `Q-RISK-02`.
- `GEN-14` — track record is entirely current, unrealized marks: self-reported, unproven; the GP has never demonstrated an exit that returned LP capital → `Q-GP-02`. (If those marks are also project-level rather than net-to-LP, `GEN-05` joins it as the RED cluster named in `03`/`04` notes — basis unstated, so probe.)

**YELLOW–RED**
- `EQUITY-04` (probe) — preferred return unstated; with a 50% promote, a low or absent pref removes the LP's only priority cushion → `Q-FEE-04`.
- `GEN-16` — no fee schedule → `Q-FEE-01`.
- `GEN-15` — no financials, no rent roll, no full debt terms → `Q-RISK-03`.

**YELLOW**
- `GEN-13` — upside case only; no downside or sensitivity → `Q-DS-03`.
- `GEN-11` — no distribution schedule → `Q-DIST-01`.
- Single-asset concentration — no `03` ID; scored via the `05` illiquidity-framework amplifier (idiosyncratic risk vs a diversified comparator) → factored into the verdict.

**Cluster notes:** `GEN-01` + `EQUITY-01` + `EQUITY-02` + 50% promote = the GP holds a free option on the deal — all upside participation, no capital exposure, no give-back. `GEN-14` (+ `GEN-05` probe) = no validated record. `GEN-10` + floating single-asset = the 2022–24 distress profile. Three independent RED clusters.

## 6. Missing Disclosures

Against `01` multifamily essentials (`GEN-17`) and the `02` baseline:
- Return target, equity multiple, and the pro forma itself (only an upside case shown).
- Hold period; raise size; minimum; market/submarket.
- Preferred return, catch-up, tiers — the waterfall below the 50% headline.
- Complete fee schedule.
- Rent roll, T-12 actuals, debt amount/rate/spread, cap strike and replacement cost.
- Refi assumptions for the 2028 maturity.
- Realized track record (none exists — the absence is the disclosure).
- GP co-invest terms (disclosed as zero — adverse, not absent).
- Distribution schedule; the SEC action's docket, allegations, and resolution.

## 7. GP Alignment

The alignment section *is* the deal's problem:
- **Co-invest:** zero, by their own framing (`GEN-01` RED). The GP participates in upside at 50% past the (unstated) pref and bears no downside.
- **Track record:** unrealized marks only (`GEN-14` RED) — no demonstrated ability to exit and return capital; basis (net-to-LP vs project-level) unstated (`GEN-05` probe).
- **Conduct:** prior SEC action against a principal (`GEN-02` RED) — obtain the order/docket; undisclosed detail compounds it.
- **Waterfall alignment:** deal-by-deal + 50% + no clawback is the least LP-aligned combination in the `02` waterfall taxonomy.
- **Affiliates:** undisclosed → `Q-FEE-02` (`GEN-06` probe) — in this alignment picture, assume affiliate fees until shown otherwise.

## 8. Questions for the GP

These are listed for completeness of process; per §10, no answers rehabilitate this structure.

**Must-ask**
1. `Q-GP-03` — Full detail of the SEC action: allegations, resolution, bars or undertakings. *Bad answer:* "nothing material"; blaming the regulator; details differing from the public record.
2. `Q-GP-01` — Any GP cash in the deal, on LP terms? *Bad answer:* already given — "our expertise is our investment."
3. `Q-GP-02` — Track record restated as **realized**, net-to-LP IRR. *Bad answer:* "most deals are still performing"; marks re-presented as returns.
4. `Q-FEE-03` — Why a 50% promote, deal-by-deal, with no clawback? *Bad answer:* "you get paid when we get paid"; "standard for our deals."
5. `Q-FEE-04` — What pref, and is it cumulative/compounding? *Bad answer:* pref <6% or none (`EQUITY-04` confirmed).
6. `Q-RISK-02` — Cost today to extend the rate cap to 2028, and is it budgeted/escrowed? *Bad answer:* "rates should be lower by then"; extension unbudgeted.
7. `Q-RISK-01` — Refinance/extension plan for the 2028 maturity. *Bad answer:* "we'll refinance" with no terms.
8. `Q-DS-03` — The downside case: flat rents, higher exit cap, cap-extension cost paid, no refi. *Bad answer:* only the upside case exists (already the disclosure).
9. `Q-FEE-01` — Complete fee schedule. *Bad answer:* "standard market fees."
10. `Q-RISK-03` — T-12, rent roll, complete debt terms. *Bad answer:* withheld until commitment.

**Nice-to-ask:** `Q-DIST-01` (distribution schedule), `Q-FEE-02` (affiliates), `Q-MKT-01` (submarket data), `Q-GP-04` (team vs AUM), `Q-LIQ-01` (exit options).

## 9. Diligence Checklist

(For the record — §10 recommends against spending it.)
- Pull the SEC action: EDGAR/litigation releases, state records; check FINRA/IAPD for related bars.
- PPM/LPA: confirm the 50%/no-clawback waterfall in the documents, pref, fee schedule.
- Loan documents: cap strike/expiry, maturity, extension tests, guaranties.
- Independent verification of the marks (appraisals vs the GP's own valuations).
- Background search on all principals, not just the one named.

## 10. Verdict

**Pass.** This is a merits pass on stated facts, not an insufficient-disclosure pass — although disclosure is also grossly incomplete (no return figure, no pref, no fees: `GEN-15`/`GEN-16`). Six REDs fire from the deal's own description, and they compound: a sponsor with a regulatory history and no capital at risk, holding a 50% no-clawback promote, on a single asset carrying uncapped floating-rate exposure for the last ~2 years of the loan, marketed on unrealized marks and an upside-only projection. Biggest swing factor: none worth naming — the structure fails before the real estate is reached; even a strong asset delivers the LP a truncated share of the upside and the whole downside.

**Who it suits:** no passive LP. **What would have to be true to pursue:** a different sponsor, a different waterfall, hedged or fixed debt, and a realized track record — i.e., a different deal. The only follow-up worth an LP's time is pulling the SEC docket to calibrate every other claim this sponsor makes elsewhere.
