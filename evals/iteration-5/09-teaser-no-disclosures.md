# Eval fixture 09 — Multifamily fund teaser ("15%+ returns")
*Iteration-5 run, 2026-09-27, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 7712624.*

**Verdict: Pass as presented (insufficient disclosure).** What you pasted is a teaser, not a deal. The one number in it ("15%+") can't be tested: it doesn't say whether it's gross or net, IRR or cash-on-cash, or over what hold. It also names no sponsor, no fees, no waterfall, no debt terms and no track record. Nothing here gives you a reason to wire $100k. Whether it's worth a call depends on whether the GP's first reply includes the re-screen list in §10.

---

## 1. Deal Snapshot

| Field | Value | Confidence |
|---|---|---|
| Asset class | Multifamily. Strategy (value-add vs core/core-plus) not stated | 🟢 class / 🟡 strategy |
| Deal type | Fund, with equity vs preferred vs debt not stated. Treated as a **multifamily equity fund** | 🟡 inferred |
| Sponsor | Not stated | 🟢 |
| Geography | Not stated | 🟢 |
| Minimum | $100,000 | 🟢 |
| Eligibility | Accredited investors only | 🟢 |
| Hold / fund term | Not stated | 🟢 |
| Raise / fund size | Not stated | 🟢 |
| Claimed return | "15%+". Metric (IRR / cash-on-cash / multiple), basis (gross / net-to-LP) and horizon not stated | 🟢 claim / 🔴 meaning |
| Fees / waterfall / pref | Not stated | 🟢 |
| Leverage / debt terms | Not stated | 🟢 |
| Track record | Not stated | 🟢 |

The strategy inference: 15%+ sits above the multifamily core/core-plus range (8–12% net) and at the top of the value-add target range (14–18% target; realized nearer 12–15% blended). If it's an equity fund, it's pitched as **value-add or higher-risk**, not core (`01`). 🟡

## 2. Return Stress-Test

Everything here is conditional, because the one input doesn't say what it measures. The script runs below assume a **7-year hold** 🔴, since no hold was stated and 5–7 years is the value-add norm (`01`).

| Case | Reading of "15%+" | Net to LP | vs VNQ (4.92% 10yr) | 7-yr illiquidity hurdle ~400–600 bps | Confidence |
|---|---|---|---|---|---|
| Bull | 15% is **net-to-LP IRR** | 15.0% | +1008 bps | **Clears comfortably** | 🔴 assumes net |
| Base | 15% is **gross**, with a market-typical stack (2% acq, 1.5% AM, 1% dispo, 0.3% admin, 20% promote over 8% pref, 100% catch-up) | ≈10.6% | +568 bps | **Clears (thin)**, lower half of the band | 🔴 assumes gross and the `02` demo stack |
| Bear | Can't be modeled. The swing assumptions that drive a multifamily bear case (**exit cap**, **rent growth**, **refi availability / rate-cap expiry**) are all undisclosed | — | — | — | 🔴 |

- **The gross-vs-net ambiguity is worth ~440 bps/yr.** The same "15%" is either a strong deal or a thin one, depending on a word the teaser leaves out. Never compare gross to anything. Demand the net-to-LP figure (skepticism rule 2; `GEN-16`).
- **Treasury floor.** The 10yr Treasury is ≈5.18%, which currently out-yields VNQ's trailing 10yr. The base case at ≈10.6% is only ≈540 bps over a risk-free bond, locked up for years (`05`). 🟢/🟡
- **Dispersion.** Even the bull case only clears the bar at the *marketed* number. Realized value-add returns cluster at 12–15% net blended, below the 14–18% marketing range (`01`), and the median private-RE fund earns well below top-quartile (`05`). "15%+" is a top-of-range pitch. 🟢
- **No downside case is offered.** It's a single-point claim (`GEN-13`).

## 3. Where LP Returns Come From

**Can't tell from this.** 🔴 The teaser says nothing about cash flow vs exit vs leverage. The benchmark overlay still frames the question:

- Unlevered institutional private RE (NCREIF NPI) returned **5.00%** over the trailing four quarters. That was almost all income (1.17% income vs 0.12% appreciation in the latest quarter). Residential returned 5.3% in 2025 (`05`). 🟢
- A 15% multifamily return against a ~5% unlevered in-place baseline means **~10 points have to come from leverage and assumed appreciation (exit cap, rent growth), not operations**, if the 15% is levered. 🟡 That doesn't fire the financing-story flag by itself, because leverage and exit assumptions are undisclosed. It is exactly what `Q-DS-01` / `Q-DS-02` must resolve: the >60%-from-exit test (`GEN-08`) and the leverage/cap-compression test (`GEN-07`, `EQUITY-06`).

## 4. Fee Stack Summary

**Gross-to-net drag computable from disclosure: none. The drag is unknowable, and that's the finding.** 🟢 (`GEN-16`)

- With every undisclosed fee passed as 0, the calculator returns **0 bps/yr**. That isn't "no fees". The inputs are simply blank. Undisclosed fees are still paid (`03` → `GEN-16`).
- For scale, a market-typical equity-syndication stack from `02` (acquisition 2%, asset management 1.5%/yr, disposition 1%, admin 0.3%/yr, 20% promote over an 8% pref with 100% catch-up) costs **≈440 bps/yr** at a 15% gross, 7-year hold (≈180 recurring, ≈43 one-time, ≈217 promote). Every input in that figure is **ASSUMED** 🔴 and a §6 gap.
- **Fund-specific layers to surface:**
  - Whether there's a fund-level management fee on top of asset-level fees.
  - Whether affiliates collect property-management, construction or loan-placement fees (`GEN-06`, probed).
  - Whether this is a **feeder / fund-of-funds**. A wrapper typically adds another 50–150 bps/yr and is rarely disclosed alongside the underlying stack (`02`).
- **Waterfall structure matters more in a fund.** Deal-by-deal (American) vs whole-of-fund (European), and whether there's a clawback, decide whether the GP can bank promote on early exits while later assets lose (`EQUITY-01`, `EQUITY-02`, probed).

## 5. Red Flags

**Fired (on stated facts / clear absences):**

- 🔴 **`GEN-16` No fee or waterfall disclosure (YELLOW–RED, treated as RED until answered).** No fee, pref, promote or waterfall term at all, so gross-to-net drag can't be known and the headline can't be converted to net-to-LP. Exposure: the whole ~0–440+ bps/yr range sits on the LP. 🟢 → `Q-FEE-01`
- 🔴 **`GEN-15` Missing financials (YELLOW–RED, treated as RED).** No debt terms, T-12, rent rolls, asset list or fund size. For a blind or undisclosed pool, the LP can't underwrite a single asset. 🟢 → `Q-RISK-03`
- 🟡 **`GEN-17` Essential category disclosure absent (YELLOW).** Multifamily normally discloses rent roll, T-12, exit cap with sensitivity, debt structure and maturity, refi assumptions, and the GP's track record on **prior multifamily exits** (`01`). None is present. 🟢 → `Q-RISK-03`, `Q-EXIT-01`, `Q-GP-02`
- 🟡 **`GEN-03` Marketing-heavy, substance-light (YELLOW).** An open-ended "15%+" plus "contact us to learn more" stands in for underwriting. 🟡 → nearest `04` probe `Q-DS-03` (the full model / downside case)
- 🟡 **`GEN-13` Projections with no sensitivity or downside case (YELLOW).** A single-point "15%+" with no bear case. 🟢 → `Q-DS-03`
- 🟡 **`GEN-11` Distribution timing / J-curve not disclosed (YELLOW).** A return target with no distribution schedule. It can't tell current income from a back-loaded exit. 🟢 → `Q-DIST-01`
- 🟡 **`GEN-14` No realized track record cited (RED on its own terms, held at "unverified").** No exits, no track record of any kind. Under rule 5, a GP with no realized net-to-LP record has **no verified record**. It's cited because the teaser offers none. It gets confirmed or cleared by the first answer to `Q-GP-02`, not assumed to be bad. 🟡 → `Q-GP-02`

**Cluster:** `GEN-15` + `GEN-16` + `GEN-17` together make this **unscreenable**. It isn't a bad deal. It isn't a deal yet.

**Probed, not fired (would need a 🔴 assumption; each routes to a must-ask):**
- `GEN-07` / `GEN-08` / `EQUITY-06`: financing-story family, via the ~10-point gap to the unlevered baseline (§3) → `Q-DS-01`, `Q-DS-02`, `Q-EXIT-01`
- `GEN-09` / `GEN-10` / `EQUITY-07`: debt maturity, rate-cap expiry, refi dependence (the 2022–24 multifamily failure mode) → `Q-RISK-01`, `Q-RISK-02`, `Q-EXIT-02`
- `EQUITY-01` / `EQUITY-02`: fund waterfall type and clawback → `Q-FEE-03`
- `EQUITY-04` / `EQUITY-05`: pref existence, level and cumulative status → `Q-FEE-04`
- `GEN-01`: GP co-invest → `Q-GP-01`
- `GEN-05`: GP-/project-level IRR substituted for net-to-LP → `Q-GP-02`
- `GEN-06`: affiliate fee stacking → `Q-FEE-02`
- `GEN-02`: regulatory / litigation history, since the sponsor isn't even named → `Q-GP-03`
- `GEN-18`: rent-growth assumption vs submarket supply (geography unstated) → `Q-MKT-01`

## 6. Missing Disclosures

Against the multifamily baseline (`01`) and the equity / fund fee inventory (`02`):

1. **Sponsor identity** and principals.
2. **Return definition.** Metric (IRR / CoC / equity multiple), **gross vs net-to-LP**, horizon.
3. **Hold / fund term**, investment period, extension options.
4. **Strategy.** Value-add vs core/core-plus vs development.
5. **Fee schedule.** Acquisition, asset management, disposition, loan placement / refinance, admin/IR, any fund-level management fee, and affiliate fees.
6. **Waterfall.** Pref rate and whether it's cumulative / compounding, promote %, catch-up rate, deal-by-deal vs whole-of-fund, clawback.
7. **Debt.** Leverage, fixed vs floating, maturity vs hold, rate-cap terms and expiry, refi assumptions.
8. **Portfolio.** Assets identified or blind pool, geography / submarkets, fund size.
9. **Financials.** Rent rolls and T-12 actuals per asset, pro forma exit cap with sensitivity.
10. **Track record.** Realized, exited multifamily deals, net-to-LP.
11. **Distribution schedule** and capital-call mechanics.
12. **GP co-invest.** Amount, cash vs fee waiver, pari-passu.
13. **Liquidity / transfer** terms and K-1 timing.
14. **Script inputs used as ASSUMED:** 7-year hold, and the entire `02` demo fee stack in the §2 base case and §4 illustration.

## 7. GP Alignment

**Unverified on every axis.** 🔴
- **Co-invest:** not stated. Unknown whether cash, how much, or pari-passu (`GEN-01`, probed).
- **Track record:** none cited. Unverified. Only realized, exited, net-to-LP figures count. Marks or project-level IRRs won't substitute (`GEN-14`, `GEN-05`).
- **Waterfall alignment:** unknown. No pref, promote, catch-up or clawback terms (`GEN-16`, `EQUITY-01`/`02`).
- **Affiliate fees:** unknown (`GEN-06`).

## 8. Questions for the GP

**Must-ask, the first five, and the teaser doesn't earn a second call without them:**

| # | Question | Bad-answer signal (the dodge) |
|---|---|---|
| `Q-FEE-01` | "Can you provide the complete fee schedule and the full distribution waterfall?" | "Standard market fees"; a partial list; "the PPM has it" without producing it. |
| `Q-GP-02` | "Can you restate your track record as net-to-LP IRR on fully-realized, exited deals only?" | Only project-level or GP-level IRR; "most deals are still performing"; can't separate realized from unrealized. |
| `Q-DS-01` | "What share of projected LP IRR comes from in-place cash flow versus the exit, and what's the IRR at a flat exit cap?" (And: is "15%+" gross or net-to-LP, and IRR or cash-on-cash?) | Can't or won't decompose the IRR; "real estate always appreciates"; IRR falls below the pref at a flat exit cap. |
| `Q-FEE-03` | "Is the waterfall deal-by-deal or whole-of-fund, and is there a clawback?" | Deal-by-deal with high promote and no clawback; can't explain the catch-up; "you get paid when we get paid." |
| `Q-GP-01` | "How much of your own capital is in this deal, on the same terms as LPs?" | "Our sweat equity is our investment"; co-invest is a fee waiver, not cash; a token amount on better terms. |

**Must-ask, next:**

| # | Question | Bad-answer signal |
|---|---|---|
| `Q-FEE-04` | "What preferred return do LPs receive before the GP earns promote, and is it cumulative and compounding?" | Pref below 6% or absent; non-cumulative. |
| `Q-DS-02` | "Strip out leverage and cap-rate compression — what is the unlevered, in-place return?" | Treats the levered IRR as the only figure; "leverage is just how the deal works." |
| `Q-DS-03` | "What is the return under a bear case — flat rents, higher exit cap, no refinance?" | Single-point pro forma; "we underwrite conservatively" with nothing to show. |
| `Q-RISK-03` | "Can you provide trailing-twelve-month actuals, the rent roll, and complete debt terms?" | T-3/T-6 only; rent roll withheld; "confidential until you commit." |
| `Q-RISK-01` | "When does the debt mature relative to the projected hold, and what's the refinance or extension plan?" | Maturity inside the hold; "we'll refinance" with no terms. |
| `Q-RISK-02` | "When does the rate cap expire relative to debt maturity, and what's the cost to extend it at current pricing?" | Cap expires before maturity; extension cost not modeled; "rates should be lower by then." |
| `Q-EXIT-01` | "Why is the exit cap below the going-in cap, and what's the IRR at an exit cap equal to or above going-in?" | "Cap rates will compress"; no sensitivity. |
| `Q-EXIT-02` | "Does the business plan depend on a refinance, and what happens to distributions if the refi isn't available on the assumed terms?" | Capital return requires a refi at lower rates; "the refi market will reopen." |
| `Q-DIST-01` | "What is the projected distribution schedule, and at what milestones does LP capital start returning?" | "We'll distribute when the deal supports it"; no milestones. |
| `Q-FEE-02` | "Which service providers are GP-affiliated, what do they charge, and are those rates third-party-benchmarked?" | "All arm's-length" without naming providers; no benchmark. |
| `Q-GP-03` | "Have you or your principals faced any regulatory action, enforcement, or investor litigation?" | "Nothing material"; a search surfaces something undisclosed. |
| `Q-MKT-01` | "What submarket supply pipeline and absorption data support the rent-growth assumption?" | Metro-level optimism; "rents always go up here"; no supply pipeline acknowledged. |
| `Q-LIQ-01` | "What are my options if I need to exit before the hold period ends?" | "A secondary market may develop"; silence, i.e. illiquid with the lock-up undisclosed. |

**Nice-to-ask:** `Q-DIST-02` (capital-call schedule and missed-call penalties, relevant if this is a commitment fund), `Q-GP-04` (team growth vs AUM), `Q-LIQ-02` (K-1 delivery timing).

## 9. Diligence Checklist

- [ ] **PPM / LPA / subscription docs.** Verify every fee, the waterfall, the clawback and the pref against the GP's verbal answers.
- [ ] **Sponsor background / regulatory search** on the entity and principals. If the manager is an RIA, check the fee schedule in SEC Form ADV Part 2 (`02` provenance).
- [ ] **Realized track record.** Exit-level statements for prior multifamily deals, net-to-LP, ideally LP-verifiable.
- [ ] **Asset-level:** rent rolls, T-12s, rent and sale comps, appraisals for identified assets.
- [ ] **Lender / debt docs:** maturity, rate cap and expiry, extension conditions.
- [ ] **Structure check:** whether this is a direct fund or a feeder / fund-of-funds, and both fee layers if a feeder.

## 10. Verdict

**Pass as presented (insufficient disclosure).** 🟢

- **Reasoning.** The essential multifamily disclosures (`01`) are *substantially* absent: no sponsor, fees, waterfall, debt, hold or track record. The core return story can't be underwritten, not even to the point of knowing whether "15%+" is gross or net. This is a teaser, not an offering. That isn't evidence of a bad deal, but it isn't evidence of anything else either.
- **Biggest swing factor: gross vs net.** Read as net-to-LP IRR over ~7 years, 15% clears VNQ plus the illiquidity hurdle comfortably (+1008 bps). Read as gross with a market-typical stack, it nets ≈10.6% and clears only thinly (+568 bps vs a ~400–600 bps hurdle), about 540 bps over a risk-free 10yr Treasury. 🔴 Behind that sits the leverage question: ~10 of the 15 points exceed the ~5% unlevered private-RE baseline (§3).
- **Re-screen list.** Re-run this screen when the GP provides:
  1. Sponsor identity plus a realized, net-to-LP multifamily track record (`Q-GP-02`).
  2. The return defined as net-to-LP IRR, with hold / fund term and distribution schedule (`Q-DS-01`, `Q-DIST-01`).
  3. The full fee schedule and waterfall: pref, promote, catch-up, deal-by-deal vs whole-of-fund, clawback (`Q-FEE-01`, `Q-FEE-03`, `Q-FEE-04`).
  4. Leverage and debt terms, including maturity and rate-cap expiry (`Q-RISK-01`, `Q-RISK-02`).
  5. GP co-invest amount and terms (`Q-GP-01`).
  6. A downside case: flat rents, higher exit cap, no refi (`Q-DS-03`).
- **Who it could suit, if it checks out.** An accredited LP who can lock up $100k for an undisclosed multi-year term with no liquidity. It could become a **Pursue-with-conditions** only if all of these hold:
  - the 15% is net-to-LP;
  - most of it isn't exit- or leverage-driven;
  - the waterfall is whole-of-fund, or deal-by-deal with a clawback, over a cumulative pref of at least 6%;
  - the GP has real co-invest;
  - the GP has *realized* multifamily exits to show.
