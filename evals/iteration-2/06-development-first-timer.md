# Eval fixture 06 — Ground-up development, first-time sponsor
*Iteration-2 run, 2026-07-04, blind generation by fresh-context agent, against SKILL.md (post S1–S3 fixes).*

**Verdict: Pass as presented — insufficient disclosure — and the disclosed facts are independently disqualifying: a first-time developer projecting 25% IRR (above the `01` 18–22% category *target*), an exit cap underwritten below going-in (`EQUITY-06`), a 9-point development+CM fee split (`02` aggressive threshold), and a single pro forma with no downside (`GEN-13`) on the asset class where realized returns most often miss target.**

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Development — ground-up (property type **not stated**) 🟢 |
| Deal type | Equity (development) 🟢 |
| Sponsor | **Not stated**; first ground-up project 🟢 |
| Geography | **Not stated** |
| Minimum investment | **Not stated** |
| Hold | 3 years 🟢 (short end of the `01` 3–5yr norm — aggressive for entitle-build-lease-exit) |
| Raise | **Not stated** |
| Claimed return | 25% IRR / 2.5x — gross or net **not stated** 🔴 |
| Fees | 5% development fee + 4% construction management 🟢 |
| Structure | Pref, promote, waterfall — **none stated** |
| Debt | **Not stated** (construction loan? takeout?) |

Routing: `01` development (target net 18–22%, realized often below; high risk); `02` equity + development variations; `03` `GEN-`, `EQUITY-`; `05` VNQ — *discount the target premium heavily* per the routing table.

## 2. Return Stress-Test

Swing assumptions: **(a) exit cap** — underwritten below going-in basis, so the headline bakes in cap compression on top of development risk; **(b) hard-cost budget and contingency** — undisclosed; construction-cost overrun is the canonical development miss (`01`); **(c) lease-up pace / absorption** — undisclosed, no comp evidence; a 3-year hold leaves no slack for a slow lease-up.

- **Base:** 25% as claimed — **above the `01` category target range of 18–22%**, from a sponsor with zero development exits. The claim exceeds what experienced developers target 🟡.
- **Bull:** on-budget, on-schedule, exit into compression → 25% conceivable; this is the only case shown.
- **Bear:** `01` is explicit that realized development returns come in *below* target on cost overruns, financing spikes, or lease-up misses — and this deal's buffer is negative: the pro forma already needs cap compression to hit its number. Flat exit cap + 10% cost overrun + 6-month lease-up slip on a 3-year clock plausibly takes 2.5x toward capital-impairment territory; **no sensitivity exists to check** (`GEN-13`) 🔴.

**Benchmark (`05`):** 25% vs VNQ 6.47% ≈ **+1,850bps** *target* premium — beyond even the spread table's development row (≈1,150–1,550bps target), which itself carries the warning: *largest target premium **and** widest dispersion — discount heavily for realized-below-target.* Preqin dispersion (opportunistic IQR ~13pts, `05`) means the median outcome sits far below the marketing number; for a first-timer, below-median is the base case to price, not the tail 🟡.

## 3. Where LP Returns Come From

Ground-up development is structurally exit-loaded: no meaningful cash flow until lease-up, then the entire return at sale. Effectively ~100% of the 2.5x is terminal-value dependent → **`GEN-08` fires by construction** (well past the 60% threshold), resting on an exit cap already flagged as aggressive (`EQUITY-06`). With the debt structure undisclosed, whether leverage is also doing the work is unknowable (`GEN-07` probe) → `Q-DS-01`, `Q-DS-02`.

## 4. Fee Stack Summary

| Fee | Stated | `02` range | Read |
|---|---|---|---|
| Development fee | 5% (of project cost, presumed — base not stated) | 3–5% of total project cost | Top of range 🟡 |
| Construction management | 4% (of hard costs, presumed) | 3–5% of hard costs | In range alone — **but** |
| **The split** | 5% + 4% together | `02`: aggressive = *">6% or split across both a development fee and construction management fee"* | **Aggressive — fires on the split itself**, ~9 points of fee against project cost before any promote 🟢 |
| Contingency reserve | **Not stated** | 5–10% of hard costs standard; <5% under-reserved, >15% padding | Undisclosed — a first-order development disclosure |
| Promote / pref / acquisition / admin | **Not stated** | 15–30% over 6–10% pref etc. | Undisclosed → `GEN-16` partial |

**Gross-to-net drag: not fully computable — the finding.** The two stated fees alone are ~9% of project cost; on a 3-year hold that is roughly 300bps/yr of drag against project cost before promote, and more against LP *equity* once the capital stack is known 🟡. Whether the 25% is before or after this load is unstated — demand the net (skepticism rule 2).

## 5. Red Flags

**RED**
- `EQUITY-06` — exit cap underwritten below the going-in basis: unproven cap compression baked into a development exit, stacking a market-timing bet on top of construction and lease-up risk → `Q-EXIT-01`.
- `GEN-08` — return ~100% exit-dependent (structural to ground-up, but this deal adds an aggressive cap to it; cluster with `EQUITY-06`, `GEN-07` probe pending debt disclosure) → `Q-DS-01`.
- `GEN-14` (mechanism) — first ground-up project = **zero realized development track record**. `01` is explicit: development experience is not fungible with acquisition experience, and the essential disclosure is "the GP's last three development exits" — which cannot exist → `Q-GP-02`.

**YELLOW–RED**
- Fee stacking per `02` — development fee at top-of-range **plus** a separate CM fee is the library's named aggressive pattern; if the CM flows to a GP affiliate this is also `GEN-06` (probe) → `Q-FEE-02`, `Q-FEE-01`.
- `GEN-16` — no pref, promote, waterfall, or remaining fee disclosure → `Q-FEE-01`, `Q-FEE-03`, `Q-FEE-04`.
- `GEN-15` — no budget, no debt terms, no absorption data; the deal can't be underwritten → `Q-RISK-03` (budget/debt form).

**YELLOW**
- `GEN-13` — single pro forma, no downside case — per `03` notes, a cycle-exposed asset with a single-point pro forma is a sharper flag than either alone → `Q-DS-03`.
- 25% target vs the 18–22% `01` band — out-of-norm claim from the least-proven sponsor type 🟡 (scored under `01`'s out-of-range discipline; routes to `Q-GP-02`, `Q-DS-03`).
- `GEN-11` — no distribution schedule (development = long J-curve by nature; when does any capital return?) → `Q-DIST-01`.

## 6. Missing Disclosures

Against the `01` development essential-disclosure baseline (`GEN-17`) — **every essential is absent:**
- **Entitlement and permit status** — entitled-but-not-permitted vs shovel-ready is a different deal; unstated.
- **Hard-cost budget with contingency %** — unstated.
- **Debt structure including takeout assumptions** — construction loan terms, recourse, takeout/refi at completion: unstated.
- **Market absorption assumptions with comp evidence** — unstated.
- **GP's last three development exits** (timing, budget vs underwritten) — none exist; the disclosure gap is structural.
- Plus: property type, market, capital stack, pref/waterfall, GP co-invest, raise size, gross-vs-net basis of the 25%.

## 7. GP Alignment

- **Co-investment:** not stated → `Q-GP-01`; for a first-time developer, meaningful GP cash at risk is the *only* available alignment substitute for a track record.
- **Track record:** none in this strategy, by the deal's own admission. Any record offered from other strategies (flips, acquisitions) does not transfer per `01` 🟢-cited / 🔴 as evidence of development capability.
- **Fee alignment:** the GP collects ~9 points of development+CM fees largely **during construction — i.e., regardless of outcome** — while the LP's entire return waits on a Year-3 exit at a compressed cap. Fees-before-outcome plus zero realized exits is the misalignment pattern the fee flags exist to catch 🟡.
- **Affiliates:** is the construction manager (or the GC) GP-affiliated? Undisclosed → `Q-FEE-02` (`GEN-06` probe).

## 8. Questions for the GP

**Must-ask**
1. `Q-GP-02` — Realized, net-to-LP track record — and specifically: what development-adjacent execution have you completed? *Bad answer:* acquisition-deal IRRs offered as development credentials; "our GC has done this before" substituting for sponsor experience.
2. `Q-EXIT-01` — Why is the exit cap below going-in, and what's the IRR/multiple at a flat or higher exit cap? *Bad answer:* "cap rates will compress"; no sensitivity offered.
3. `Q-DS-03` — Return under a bear case: 10–15% cost overrun, 6–12 month lease-up slip, flat exit cap? *Bad answer:* the single pro forma is re-presented; "we underwrite conservatively" with nothing shown.
4. Entitlement status (per `01` essentials, via `GEN-17`/`Q-RISK-03` form) — Entitled? Permitted? What approvals remain and on what timeline? *Bad answer:* "entitlements are basically done."
5. `Q-RISK-03` (budget/debt form) — Hard-cost budget with contingency %, GMP contract status, and full construction-debt terms including the takeout. *Bad answer:* no GMP; contingency <5% (`02` under-reserved); "we'll refinance at completion" with no takeout terms.
6. `Q-FEE-01` — Complete fee schedule and waterfall: pref, promote, catch-up, and why both a 5% development fee *and* a 4% CM fee. *Bad answer:* "standard for development"; the split defended without a scope breakdown.
7. `Q-FEE-02` — Is the CM/GC GP-affiliated, and are its rates third-party-benchmarked? *Bad answer:* "all arm's-length" without naming entities.
8. `Q-GP-01` — GP cash co-invest on LP terms. *Bad answer:* the development fee "reinvested" counted as co-invest.
9. `Q-MKT-01` — Submarket supply pipeline and absorption comps behind the lease-up and exit assumptions. *Bad answer:* metro-level optimism; no pipeline acknowledged.
10. `Q-DIST-01` — When does any LP capital return — and what happens at month 36 if the asset isn't stabilized? *Bad answer:* "we'll extend"; no milestone schedule.

**Nice-to-ask:** `Q-GP-03` (regulatory/litigation), `Q-DIST-02` (capital-call mechanics — development deals call capital in tranches), `Q-LIQ-01` (exit options during construction — realistically none; an honest "none" is the good answer), `Q-GP-04` (who on the team has personally delivered a ground-up project).

## 9. Diligence Checklist

- PPM/LPA: full fee schedule, waterfall, capital-call and dilution mechanics.
- Entitlement/permit documentation from the municipality, not the sponsor's summary.
- Hard-cost budget vs a third-party cost estimate; GMP contract and GC financials/bonding.
- Construction lender term sheet: rate, recourse, completion guaranties, takeout conditions.
- Third-party market study: absorption, competitive pipeline, rent comps.
- Background/regulatory search on principals; verify any claimed prior projects (county records).

## 10. Verdict

**Pass as presented — insufficient disclosure.** Every `01` development essential (entitlement status, budget/contingency, debt + takeout, absorption evidence, development exits) is absent, so no merits verdict is available — and the merits that *are* visible each independently point to pass: above-target IRR from a first-timer, compression baked into the exit (`EQUITY-06`), the `02`-flagged dev+CM fee split, and a single-scenario pro forma (`GEN-13`) in the asset class with the widest realized dispersion (`05`). Biggest swing factor: **execution risk with no track record to price it** — the exit cap is the biggest *modeled* swing, but the unmodeled one is whether a first-time developer delivers on budget at all.

**Re-screen list:** entitlement/permit status; budget with contingency; construction-debt and takeout terms; downside sensitivity; full fee/waterfall schedule; affiliate disclosure; GP co-invest; absorption comps; gross-vs-net basis of the 25%. **What would have to be true to pursue:** shovel-ready entitlements, a GMP contract with ≥5–10% contingency, an exit underwritten at or above going-in cap, real GP cash, and a team member with personally-attributable development exits. **Who it suits:** as presented, no passive LP — first-time-developer risk is venture risk, and this deal prices it as if it were a proven operator's.
