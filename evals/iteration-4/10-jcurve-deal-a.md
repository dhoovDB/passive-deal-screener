# Eval fixture 10 — J-curve pair, Deal A (front-loaded distributions)
*Iteration-4 run, 2026-09-27, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 1c7faff.*

**Verdict (Deal A, standalone): Pass as presented — insufficient disclosure.** The distribution profile is the strongest thing disclosed and will carry real weight in the comparison. But with no sponsor, no hold, no fees, no debt terms and no statement of whether the 14% is gross or net, the core return story can't be underwritten yet. Re-screen list is in §10.

**Comparison mode.** Deal A is screened below and held for the side-by-side. When you send Deal B, the contrast will centre on **distribution timing / J-curve** (`GEN-11`): two equal headline IRRs are not equal if one back-loads its return to the exit. Deal A is the front-loaded side of that pair, *if its 7% is operating cash flow*. §3 shows it is still more exit-dependent than the phrase "front-loaded" suggests.

---

## 1. Deal Snapshot

| Field | Deal A |
|---|---|
| Asset class | Multifamily. Strategy (value-add vs core/core-plus) **not stated** 🔴 |
| Deal type | Equity syndication (inferred from "multifamily" + cash-on-cash language) 🟡 |
| Sponsor / GP | Not stated |
| Geography / submarket | Not stated |
| Minimum investment | Not stated |
| Hold period | Not stated ("capital returns progressively over the hold" gives no hold length) |
| Raise size | Not stated |
| Claimed return | 14% projected IRR. **Gross or net-to-LP not stated** 🔴 |
| Distributions | 7% cash-on-cash, quarterly, starting Year 1 🟢. Capital returned progressively over the hold 🟢 (mechanism not stated) |
| Debt | Not stated (amount, rate type, maturity, rate cap) |
| Fees / waterfall | Not stated |

## 2. Return Stress-Test

The comparison hinges on whether the 14% is net or gross, so both readings are run. Hold is unstated, so the multifamily-equity norm (5–7 yrs, `01`) is used and marked ASSUMED.

| Reading | Net-to-LP IRR | vs VNQ (4.92% 10yr) | Illiquidity hurdle | Read |
|---|---|---|---|---|
| 14% is **net** to LP | 14.00% | ≈908 bps | 5-yr: ~300–400 bps · 7-yr: ~400–600 bps | **Clears comfortably** 🟢 (script) |
| 14% is **gross**, market-typical stack (`02` worked-example fees, 20% over 8% pref, 100% catch-up) | ≈9.71% 🔴 assumed stack | ≈479 bps | 7-yr: ~400–600 bps | **Clears (thin)**, lower half of the band 🔴 |

- **Treasury floor** (`05`): the 10yr Treasury is 5.18%. A 9.71% net is only ≈450 bps over a risk-free bond, for single-asset illiquid equity.
- **Against the `01` baseline:** value-add multifamily targets 14–18% net, and realized returns cluster at 12–15%. A 14% net sits at the realized top, which is plausible. At 14% gross the net is ≈9.7%, which is the **core/core-plus** range (8–12%). That would mean value-add risk for a core-level net return.
- **Scenarios (ranges only, because no pro forma was provided, `GEN-13`):**
  - **Base.** 14% as marketed. Hurdle clears if the figure is net.
  - **Bull.** Rent growth and exit cap hold or improve. Upside mostly flows through the exit (§3).
  - **Bear.** The three swing assumptions are (1) **exit cap** expansion vs underwriting, (2) **rent growth** below pro forma, and (3) **whether the 7% Year-1 yield is covered by operations**, or instead comes from reserves, return of capital, or a refi (§5). If the yield is not operating cash, the front-loaded profile is cosmetic. It hands LPs their own capital back early.
- **Dispersion caveat** (`05`): clearing the spread is necessary, not sufficient. A single-asset deal carries concentration that VNQ's basket diversifies away.

## 3. Where LP Returns Come From

This is the section that matters for the J-curve comparison. **A 7% annual yield alone cannot produce a 14% IRR. The other ~7 points have to come from the exit or from the capital-return mechanism.** 🟡 (Illustrative arithmetic, not the GP's model. It assumes a flat 7% on original equity with the balance paid at exit.)

| Hold (assumed) | PV share of LP distributions from the 7% yield | Exit share of LP *profit* | Implied equity multiple |
|---|---|---|---|
| 5 yrs | ≈24% | ≈57% | ≈1.81x |
| 7 yrs | ≈30% | ≈61% | ≈2.24x |

- **Exit dependence sits right at the `GEN-08` 60% line** 🟡. Front-loaded yield still leaves this deal mostly an exit bet on a present-value basis. The yield is a better *shape* than a pure back-loaded deal, not a different *kind* of return.
- **"Capital returns progressively"** can shift that balance materially, but only if the capital comes back from operations or partial sales. In a single-asset multifamily deal, progressive capital return usually means either **a refinance** (`EQUITY-07`) or **distributions that are characterized as return of capital**. Both are financing mechanics, not operating ones. The mechanism is unstated 🔴.
- **Leverage vs operations** (`05` unlevered overlay): NCREIF NPI is 5.00% trailing (residential 5.3% in 2025), almost entirely income. A 14% levered return therefore has ~9 points coming from leverage and assumed appreciation. That's normal for RE equity, but it is the financing bet the LP is taking. Whether it reaches `GEN-07` (financing story, RED) depends on the exit cap vs going-in cap (`EQUITY-06`) and the debt terms. Neither was disclosed, so this is **probed, not fired**.

## 4. Fee Stack Summary

**Gross-to-net drag: not computable from the disclosure.** That is the finding (`GEN-16`).

- With every undisclosed fee passed as 0, the script returns **0 bps**. That is not a real answer, because undisclosed fees are still paid.
- On a market-typical `02` equity-syndication stack (2% acquisition, 1.5% annual asset management, 1% disposition, 0.3% admin, 20% promote over an 8% pref with 100% catch-up), a 14% gross becomes **≈429 bps/yr drag → ≈9.71% net**. That breaks down as ≈180 bps recurring, ≈43 bps one-time and ≈206 bps promote. 🔴 Every input is ASSUMED and becomes a §6 gap.
- Layers to surface: acquisition, asset management, disposition, loan placement / refinance fees (especially relevant if the progressive capital return is refi-driven), admin/IR, promote/waterfall, affiliate property management (`GEN-06`), and any feeder/platform wrapper (+50–150 bps, `02`).

## 5. Red Flags

**Fired (disclosure-driven):**
- 🟡→🔴 **`GEN-15` Missing financials (YELLOW–RED).** No rent roll, no T-12, no debt terms. You can't verify that the 7% Year-1 yield is covered by in-place NOI. → `Q-RISK-03`
- 🟡→🔴 **`GEN-16` No fee or waterfall disclosure (YELLOW–RED).** Drag is unknowable, and gross vs net on the 14% is unknown. → `Q-FEE-01`, `Q-FEE-04`, `Q-FEE-03`
- 🟡 **`GEN-17` Essential multifamily disclosures absent (YELLOW).** Strategy, exit cap with sensitivity, debt structure/maturity, refi assumptions, and GP multifamily exit record are all missing (`01`). No track record is cited at all, so it is unverified (`GEN-14` / `GEN-05` cannot be cleared). → `Q-GP-02`
- 🟡 **`GEN-13` No sensitivity or downside case (YELLOW).** A single-point 14%. → `Q-DS-03`
- 🟡 **`GEN-08` Exit-dependent IRR (RED threshold; borderline, inferred).** On §3 arithmetic, ≈57–61% of LP profit comes from the exit, depending on hold. The "progressive capital return" mechanism could move it either way. → `Q-DS-01`

**Probed, not fired (can't be assessed from what was disclosed):**
- **`EQUITY-07` Refi-dependent plan (YELLOW–RED).** Progressive capital return in a single asset often means a refi, and the 2022–24 frozen-refi pattern applies. → `Q-EXIT-02`
- **`GEN-07` / `EQUITY-06` financing-story cluster (RED).** The ~9-point gap over the unlevered NPI baseline has to be explained by operations, not by cap compression. → `Q-DS-02`, `Q-EXIT-01`
- **`GEN-09` / `GEN-10` debt maturity and rate-cap expiry (RED).** Debt terms are unstated, and a Year-1 7% payout is exactly what a cap expiry erases. → `Q-RISK-01`, `Q-RISK-02`
- **`GEN-01` co-invest, `GEN-06` affiliate fees, `EQUITY-01`/`02`/`03`/`04`/`05` waterfall terms.** All unstated. → §8
- **`GEN-11` J-curve.** **Largely addressed** 🟢. Deal A does disclose a distribution shape (quarterly from Year 1, progressive capital return), which is its comparative strength. The milestones that gate capital return are still missing. → `Q-DIST-01`

**Cluster note.** `GEN-15` + `GEN-16` + `GEN-17` + `GEN-13` together mean the deal is marketed on its distribution *shape* while withholding everything needed to verify the shape is funded by operations.

## 6. Missing Disclosures

Against `01` (multifamily) and `02` (equity syndication):
- Sponsor identity and **realized, net-to-LP** multifamily exit record
- Strategy (value-add vs core/core-plus). This sets the baseline: 14–18% vs 8–12% net
- **Gross vs net** basis of the 14% IRR; equity multiple
- Hold period
- Rent roll, **T-12 actuals**, going-in cap and pro forma exit cap with sensitivity
- Debt: amount/LTV, fixed vs floating, maturity, rate cap and its expiry, refi assumptions
- **Source of the 7% Year-1 distribution** (operating cash vs reserves vs return of capital)
- **Mechanism and schedule of "progressive" capital return** (refi, partial sale, or distribution characterization)
- Full fee schedule, waterfall (pref rate, cumulative?, catch-up, splits, deal-by-deal vs whole-of-fund, clawback), affiliate providers
- GP co-invest (cash, pari passu?)
- Minimum, raise, LP liquidity provisions, K-1 timing

## 7. GP Alignment

**Unverified on every axis.** 🔴
- Co-invest: not stated (`GEN-01` unassessable).
- Track record: none cited. Unrealized or absent = no track record (`GEN-14`, `GEN-05` unassessable).
- Waterfall alignment: not stated. One alignment question is specific to this deal. If the GP earns promote on the quarterly 7% distributions before LP capital is returned, the front-loaded shape benefits the GP as much as the LP (`EQUITY-01`, `EQUITY-03`).
- Affiliate fees: not stated (`GEN-06`).

## 8. Questions for the GP

**Must-ask**

| ID | Question (short) | Bad-answer signal |
|---|---|---|
| `Q-DIST-01` | Projected distribution schedule, and the milestones at which LP capital returns? | "We'll distribute when the deal supports it"; no milestones; can't say what funds Year-1 distributions. |
| `Q-EXIT-02` *(escalated: EQUITY-07 probe)* | Does the progressive capital return depend on a refinance, and what happens if the refi isn't available? | Capital return requires a refi at lower rates; no fallback; "the refi market will reopen." |
| `Q-RISK-03` | T-12 actuals, rent roll, complete debt terms? | T-3/T-6 only; rent roll withheld; "confidential until you commit." |
| `Q-FEE-01` | Complete fee schedule and full waterfall? And **is the 14% gross or net to LP?** | "Standard market fees"; partial list; "the PPM has it" without producing it. |
| `Q-FEE-04` | Pref rate, cumulative, compounding? | Pref below 6% or absent; non-cumulative. |
| `Q-FEE-03` | Deal-by-deal or whole-of-fund, and is there a clawback? | Deal-by-deal with high promote and no clawback; "you get paid when we get paid." |
| `Q-DS-01` | Share of LP IRR from in-place cash flow vs exit; IRR at a flat exit cap? | Can't decompose; "real estate always appreciates"; IRR falls below pref at a flat exit cap. |
| `Q-DS-02` | Unlevered, in-place return? | "Leverage is just how the deal works"; no unlevered view exists. |
| `Q-DS-03` | Bear case: flat rents, higher exit cap, no refi? | No downside; "we underwrite conservatively" with nothing to show. |
| `Q-EXIT-01` | Exit cap vs going-in cap; IRR at an equal-or-higher exit cap? | Exit cap below going-in with "cap rates will compress." |
| `Q-RISK-01` | Debt maturity vs hold; refi/extension plan? | Maturity inside the hold; "we'll refinance" with no terms. |
| `Q-RISK-02` | Rate-cap expiry vs maturity; extension cost at current pricing? | Cap expires before maturity; "rates should be lower by then." |
| `Q-GP-01` | Your own cash in the deal, pari passu? | "Our sweat equity is our investment"; co-invest is a fee waiver. |
| `Q-GP-02` | Track record as net-to-LP IRR on realized exits only? | Project- or GP-level IRR only; "most deals are still performing." |
| `Q-GP-03` | Regulatory action or investor litigation? | "Nothing material"; a search surfaces something undisclosed. |
| `Q-FEE-02` | GP-affiliated providers, their fees, benchmarked? | "All arm's-length" without naming providers. |
| `Q-MKT-01` | Submarket supply/absorption behind rent growth? | Metro-level optimism; no supply pipeline acknowledged. |
| `Q-LIQ-01` | Exit options before the hold ends? | "A secondary market may develop"; silence. |

**Nice-to-ask:** `Q-DIST-02` (capital-call schedule and missed-call penalties; bad answer: "calls as needed," punitive dilution buried in the docs), `Q-GP-04` (team scale vs AUM), `Q-LIQ-02` (K-1 timing).

## 9. Diligence Checklist

- PPM and operating agreement: waterfall, fees, capital-return mechanics, distribution-characterization language
- Sponsor background: SEC/FINRA/state records and litigation search (`Q-GP-03`)
- Independent T-12 and rent-roll review; reconcile Year-1 NOI against 7% of equity
- Lender term sheet: maturity, rate type, rate-cap expiry, extension options
- Submarket rent and cap-rate comps vs going-in and exit cap
- Appraisal or broker opinion of value
- Realized-deal references from prior LPs

## 10. Verdict

**Pass as presented — insufficient disclosure.**

- **Reasoning.** Three facts are disclosed: asset class, headline IRR and distribution shape. The `01` essential multifamily disclosures are substantially absent. The core return story (gross vs net, leverage, exit cap, fees) can't be underwritten. This is not a merits Pass. Nothing disclosed is itself disqualifying.
- **Biggest swing factor.** **Is the 14% net or gross, and is the 7% Year-1 yield funded by operating cash flow?**
  - Net plus operating-funded: a strong, front-loaded multifamily deal that clears the 7-yr hurdle by ≈300–500 bps above its top.
  - Gross plus reserve- or refi-funded: roughly a 9.7% net with cosmetic early distributions and a refi dependency.
- **Who it suits (if it re-screens well).** An income-oriented LP who values early cash return and a shorter effective exposure to exit risk, and who can accept a 5–7 yr lock-up.
- **What would have to be true.** (1) The 14% is net to LP. (2) T-12 NOI covers the 7% payout after debt service. (3) The progressive capital return does not depend on a refi at assumed terms. (4) The exit cap is ≥ the going-in cap. (5) The GP has realized, net-to-LP multifamily exits and cash co-invested pari passu.
- **Re-screen list.** Sponsor + realized track record; gross/net basis; hold; T-12 + rent roll; debt terms incl. rate-cap expiry; going-in/exit cap with sensitivity; full fee schedule + waterfall; capital-return mechanism and schedule.

**For the comparison.** Send Deal B with the same fields if you have them: IRR basis, distribution start and rate, capital-return timing, and hold. On shape alone, Deal A's quarterly-from-Year-1 profile beats a deal that back-loads to exit at the same IRR. It moves part of the return out of the exit-risk window, though (per §3) not most of it. The comparison will test whether that advantage is **real (operating cash) or engineered (return of capital or refi)**. If Deal B is back-loaded, it will carry `GEN-11` and a higher `GEN-08` exposure.

---

*Scripts run (screening, not underwriting):*
- `benchmark_comparator.py --deal-type multifamily-equity --net-irr 14 --hold-years 7` → 908 bps, clears.
- Same with `--hold-years 5` → 908 bps, clears.
- `fee_drag_calculator.py --gross-irr 14 --hold-years 7` with all fees 0 → 0 bps (undisclosed, not real).
- Same with the `02` typical stack (`--carry 20 --hurdle 8 --catch-up 100 --acquisition-fee 2 --disposition-fee 1 --mgmt-fee 1.5 --admin-fee 0.3`) → 429 bps, 9.71% net.
- `benchmark_comparator.py --net-irr 9.71 --hold-years 7` → 479 bps, thin.
