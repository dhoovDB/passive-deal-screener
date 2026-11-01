# Eval fixture 10
*Iteration-7 run, 2026-11-01, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 181fdd7.*

# Deal A Screen (Comparison Mode: Deal B Not Yet Received)

**Verdict (Deal A): Pass as presented, insufficient disclosure.** The distribution shape is the one thing this deal gets right on paper. Nearly everything needed to underwrite the 14% is missing.

*Screening output only, not investment advice.*

**Comparison status:** you asked me to compare this deal to "the next one," but only Deal A was included. Below is the full screen of Deal A, plus a comparison frame already filled in on Deal A's side. Paste Deal B and I'll screen it the same way and complete the head-to-head. The comparison turns mainly on distribution timing (J-curve). Two deals with the same headline IRR are not equal if one holds its return back until the exit.

---

## 1. Deal Snapshot

| Field | Deal A |
|---|---|
| Asset class | Multifamily 🟢. Strategy (value-add vs core/core-plus) is **not stated**. A 14% projection fits the value-add band (`01`: 12–18% target) and sits above the core band (8–12%) 🟡 |
| Deal type | Equity syndication (inferred from "multifamily" plus cash-on-cash distributions) 🟡 |
| Sponsor | Not stated |
| Geography / submarket | Not stated |
| Minimum investment | Not stated |
| Hold period | Not stated |
| Raise size / capitalization | Not stated |
| Claimed return | 14% projected IRR 🟢. **Gross or net to LP: not stated.** |
| Distributions | 7% cash-on-cash, paid quarterly from Year 1 🟢. "Capital returns progressively over the hold" 🟢, but the mechanism (operations, refinance, partial sales) is not stated |
| Fees / waterfall / pref | Not stated |
| Debt | Not stated |
| Exit cap / going-in cap | Not stated |
| Track record / co-invest | Not stated |

---

## 2. Return Stress-Test

**Gross vs net is unknown, which is the first problem.** The skill never compares gross to gross, and "14% IRR" with no basis can't be benchmarked as given. I ran it both ways.

**Benchmark (`scripts/benchmark_comparator.py`, VNQ 4.92% 10yr, `05`):**

| Reading of "14%" | Net-to-LP IRR | Premium over VNQ | Illiquidity hurdle | Read |
|---|---|---|---|---|
| Already net to LP (best case) | 14.00% 🔴 | ≈908 bps | 5-yr hold: ~300–400 bps · 7-yr hold: ~400–600 bps | Clears comfortably at either hold |
| Gross, with a typical `02` equity stack (see §4) | ≈9.71% 🔴 | ≈479 bps | 7-yr hold: ~400–600 bps | **Clears, but thinly** (lower half of the hurdle band) |

- **Treasury floor (`05`, 10yr ≈5.18%):** 14% net would be ≈882 bps over risk-free. A 9.71% net would be ≈453 bps. Right now the risk-free bond out-yields VNQ's trailing decade, so the Treasury is the tighter floor.
- **Hold is not stated (🔴), so the hurdle is a range.** I modeled 5 and 7 years from the `01` value-add band (5–7 yrs). A core plan (7–10 yrs) would push the hurdle to the top of the ~400–600 bps band.
- **Dispersion caveat (`05`):** clearing the spread is necessary, not sufficient. The median deal lands below the marketed figure, and `01` notes that realized multifamily value-add clusters at 12–15% net, below the 14–18% marketing range.

**Scenarios.** No pro forma, exit cap, rent growth or debt terms were disclosed, so the scenarios below are a frame for testing, not a model:

| Case | What it would take | Swing assumptions |
|---|---|---|
| Bull | 14% is net. The 7% yield is funded entirely by property operations. Capital comes back through operations or sales, not through a refinance. | Rent growth meets plan; exit cap at or above going-in |
| Base | 14% is gross. A market fee stack brings net to ≈9.7–10% 🔴. The 7% holds. | Exit cap flat; refi not required |
| Bear | The Year-1 7% is funded from reserves or raised equity rather than NOI. The "progressive capital return" depends on a refinance that is unavailable or comes in at worse terms (the 2022–24 pattern). Distributions get cut and capital return slips to the exit. | **(1) Exit cap**, **(2) refi availability/terms**, **(3) rent growth vs submarket supply** |

The three swing assumptions follow `01` (multifamily key LP risks: exit cap, rent growth, refi). None of them is disclosed.

---

## 3. Where LP Returns Come From

**On its face, Deal A is front-loaded, which is the right shape for a comparison.** 🟡
- A 7% cash-on-cash yield paid from Year 1 means that, if it is sustained, roughly half of a 14% IRR arrives as in-period cash rather than at exit. Add progressive capital return, and less capital stays at risk until the terminal sale.
- That runs against the exit-dependent pattern (`GEN-08`, >60% from terminal value). On the stated terms, **`GEN-08` does not fire**, and I'm not inventing it. But I can't verify the split until the GP decomposes the IRR (`Q-DS-01`).
- `GEN-07` (financing story) is untested. `05`'s unlevered overlay puts institutional private real estate at ≈5.00% (NCREIF NPI, trailing 4Q to Q2 2026), almost all income, with residential at 5.3% for 2025. At 14% levered, **roughly 9 points would have to come from leverage, value-add execution or appreciation** rather than in-place unlevered income 🟡. That is normal for levered equity, but the deal has to show which source it is (`Q-DS-02`).

**Two mechanisms could make the front-loaded shape misleading. I'm treating both as must-asks, not flags, because they rest on unstated terms:**
1. **How is the Year-1 7% funded?** `01` puts multifamily value-add cash-on-cash at 5–8% *after stabilization*. Paying 7% from Year 1, before any value-add plan has stabilized, is possible only if in-place NOI supports it. Otherwise the payout comes from a distribution reserve or from LP equity, which is your own capital handed back and labeled as yield. That would lower the real yield and weaken the J-curve advantage. → `Q-DIST-01`, `Q-RISK-03`.
2. **How does capital "return progressively"?** In multifamily that usually means a cash-out refinance or a partial sale. If it's a refinance, the capital-return schedule is a bet on the debt market (`EQUITY-07`, not fired, not confirmed) and adds leverage partway through the hold. → `Q-EXIT-02`, `Q-RISK-01`.

---

## 4. Fee Stack Summary

**The gross-to-net drag cannot be computed from what was disclosed. That is the finding.** No acquisition, asset-management, disposition, financing or admin fee, promote, pref or waterfall was stated (`GEN-16`).

`scripts/fee_drag_calculator.py`, two runs at 14% gross over 7 years (hold ASSUMED 🔴):

| Run | Inputs | Net LP IRR | Total drag |
|---|---|---|---|
| Disclosed fees only (every fee passed as 0) | Nothing disclosed | 14.00% | **0 bps (not a real result; it only shows that nothing was disclosed)** |
| Illustrative `02` market stack (all ASSUMED 🔴) | 2% acquisition, 1.5%/yr asset mgmt, 1% disposition, 0.3%/yr admin, 20% promote over 8% pref, 100% catch-up | ≈9.71% | **≈429 bps/yr** (recurring 180 + one-time 43 + promote 206) |

- **If the 14% is gross and the fee stack is ordinary, the LP's net drops by about 430 bps**, from inside the value-add band to the low end of the core band.
- Every input in the second run is an ASSUMED gap (§6), not a disclosed term.
- Still unknown: whether affiliated parties earn property-management or loan-placement fees (`GEN-06`), and whether the deal sits inside a feeder or fund-of-funds wrapper, which per `02` adds another 50–150 bps a year.

---

## 5. Red Flags

**RED:** none fired on the stated facts. Every candidate RED depends on terms that weren't disclosed, so each is a must-ask (§8), not a finding.

**YELLOW–RED (treat as RED until answered):**
- **`GEN-16`: no fee or waterfall disclosure.** There is no fee schedule, pref, promote, catch-up or clawback, so gross-to-net drag is unknowable. The §4 illustration shows about 430 bps at stake. → `Q-FEE-01`. The waterfall terms that should be probed (`EQUITY-01`, `EQUITY-02`, `EQUITY-03`, `EQUITY-04`, `EQUITY-05`) are all unassessable. → `Q-FEE-03`, `Q-FEE-04`.
- **`GEN-15`: missing financials.** There is no rent roll, no T-12 and no debt terms, so the Year-1 7% can't be tied to in-place NOI. → `Q-RISK-03`.

**YELLOW:**
- **`GEN-17`: essential multifamily disclosures absent** (`01`: rent roll, T-12, exit cap with sensitivity, debt structure and maturity, refi assumptions, record on prior multifamily exits). Even the strategy (value-add vs core) is unstated, and that sets which return band and hold apply. → `Q-RISK-03`, `Q-DS-01`, `Q-RISK-01`.
- **`GEN-13`: no sensitivity or downside case.** The 14% is a single number. → `Q-DS-03`.

**Probed, not fired (cited so the gaps are visible):**
- **`GEN-08` / `GEN-07` / `EQUITY-06` (the financing-story family):** the stated distribution shape argues against exit dependence. The exit cap, leverage and an unlevered return are all undisclosed. → `Q-DS-01`, `Q-DS-02`, `Q-EXIT-01`.
- **`EQUITY-07`: refi-dependent plan.** "Capital returns progressively" may mean a cash-out refinance. → `Q-EXIT-02`.
- **`GEN-09` / `GEN-10`: debt maturity inside the hold; rate-cap expiry.** No debt terms at all. → `Q-RISK-01`, `Q-RISK-02`.
- **`GEN-11`: J-curve not disclosed.** *Not fired.* Deal A does state a shape (7% quarterly from Year 1, progressive capital return). That puts it ahead of a deal quoting a bare IRR. The milestones, the funding source and what gates the distributions are still unstated. → `Q-DIST-01`.
- **`GEN-01`, `GEN-05` / `GEN-14`, `GEN-02`: sponsor alignment and record.** No sponsor named, no co-invest, no track record of any kind (so it is unverified, not "unrealized"). → `Q-GP-01`, `Q-GP-02`, `Q-GP-03`.
- **`GEN-06`: affiliate fee stacking.** → `Q-FEE-02`.
- **`GEN-18`: rent growth in a soft submarket.** No geography, so no supply check is possible. → `Q-MKT-01`.

**Cluster note:** `GEN-16` + `GEN-15` + `GEN-17` + `GEN-13` together mean the core return story can't be underwritten. Per `03`, a cluster of YELLOWs reads as a RED, and that cluster drives the verdict.

---

## 6. Missing Disclosures

What `01` and `02` say a multifamily equity syndication normally discloses that Deal A omits:

1. **Whether the 14% is gross or net to LP**, and the equity multiple
2. **Strategy:** value-add vs core/core-plus (sets the `01` return band and hold)
3. **Hold period** (ASSUMED at 5 and 7 years in §2 and §4)
4. **Sponsor identity and track record** on *realized* multifamily exits, net to LP
5. **GP co-investment:** amount, cash, pari-passu
6. **Full fee schedule:** acquisition, asset management, disposition, loan placement/refinance, admin/IR (all ASSUMED in §4)
7. **Waterfall:** pref rate, cumulative/compounding, promote, catch-up, deal-by-deal vs whole-of-fund, clawback
8. **Rent roll and T-12 actuals**
9. **Debt:** amount/LTV, fixed vs floating, rate cap and its expiry, maturity, extension options
10. **Going-in cap, exit cap and sensitivity**
11. **Source of the Year-1 7% distributions** (NOI vs reserve vs return of equity) and whether "7% cash-on-cash" is measured on original or remaining capital as capital is returned
12. **Mechanism and schedule of the "progressive" capital return** (refinance, partial sale, operations)
13. **Geography / submarket, supply pipeline and rent-growth assumption**
14. **Minimum investment, raise size, LP liquidity / transfer provisions**

---

## 7. GP Alignment

- **Co-invest:** not stated. Unverified. (`GEN-01`)
- **Track record:** none cited. **There is no validated record**, and per the skepticism contract nothing can be credited until realized, net-to-LP figures are produced. (`GEN-05`, `GEN-14`)
- **Waterfall alignment:** unknown. Whether the GP earns promote before LPs get capital back is the key alignment question, and progressive capital return makes it sharper. If capital comes back partway through, does the promote also start partway through? (`EQUITY-01`, `EQUITY-02`)
- **Affiliate fees:** unknown. (`GEN-06`)
- **Regulatory history:** unknown. The sponsor isn't even named. (`GEN-02`)

---

## 8. Questions for the GP

**Must-ask**

| ID | Question | Bad-answer signal (the specific dodge) |
|---|---|---|
| `Q-FEE-01` (`GEN-16`) | "Can you provide the complete fee schedule and the full distribution waterfall?" | "Standard market fees"; a partial list; "the PPM has it" without producing it |
| `Q-FEE-04` (`EQUITY-04`, `EQUITY-05`) | "What preferred return do LPs receive before the GP earns promote, and is it cumulative and compounding?" | Pref below 6% or absent; non-cumulative |
| `Q-FEE-03` (`EQUITY-01`, `EQUITY-02`) | "Is the waterfall deal-by-deal or whole-of-fund, and is there a clawback?" | Deal-by-deal with high promote and no clawback; can't explain the catch-up; "you get paid when we get paid" |
| `Q-DIST-01` (`GEN-11`) | "What is the projected distribution schedule, and at what milestones does LP capital start returning?" Also ask: *is the Year-1 7% covered by in-place NOI, or by a reserve or LP equity?* | "We'll distribute when the deal supports it"; no milestones; won't say what funds the Year-1 payout |
| `Q-RISK-03` (`GEN-15`, `GEN-17`) | "Can you provide trailing-twelve-month actuals, the rent roll, and complete debt terms?" | T-3/T-6 only; rent roll withheld; "confidential until you commit" |
| `Q-EXIT-02` (`EQUITY-07`) | "Does the business plan depend on a refinance, and what happens to distributions if the refi isn't available on the assumed terms?" Ask this specifically about the *progressive capital return*. | Capital return requires a refi at lower rates; no fallback; "the refi market will reopen" |
| `Q-DS-01` (`GEN-08`, `EQUITY-06`) | "What share of projected LP IRR comes from in-place cash flow versus the exit, and what's the IRR at a flat exit cap?" | Can't or won't decompose the IRR; "real estate always appreciates"; IRR falls below the pref at a flat exit cap |
| `Q-DS-02` (`GEN-07`) | "Strip out leverage and cap-rate compression: what is the unlevered, in-place return?" | No unlevered view exists; "leverage is just how the deal works" |
| `Q-DS-03` (`GEN-13`) | "What is the return under a bear case: flat rents, higher exit cap, no refinance?" | Single-point pro forma; "we underwrite conservatively" with nothing to show |
| `Q-RISK-01` (`GEN-09`) | "When does the debt mature relative to the projected hold, and what's the refinance or extension plan?" | Maturity inside the hold; "we'll refinance" with no terms |
| `Q-RISK-02` (`GEN-10`) | "When does the rate cap expire relative to debt maturity, and what's the cost to extend it at current pricing?" (if floating) | Cap expires before maturity; extension cost not modeled; "rates should be lower by then" |
| `Q-EXIT-01` (`EQUITY-06`) | "Why is the exit cap below the going-in cap, and what's the IRR at an exit cap equal to or above going-in?" (if it is below) | "Cap rates will compress"; IRR breaks at a flat exit cap; no sensitivity |
| `Q-GP-02` (`GEN-05`, `GEN-14`) | "Can you restate your track record as net-to-LP IRR on fully-realized, exited deals only?" | Only project-level or GP-level IRR; "most deals are still performing" |
| `Q-GP-01` (`GEN-01`) | "How much of your own capital is in this deal, on the same terms as LPs?" | "Our sweat equity is our investment"; co-invest is a fee waiver, not cash |
| `Q-GP-03` (`GEN-02`) | "Have you or your principals faced any regulatory action, enforcement, or investor litigation?" | "Nothing material"; a search turns up something undisclosed |
| `Q-FEE-02` (`GEN-06`) | "Which service providers are GP-affiliated, what do they charge, and are those rates third-party-benchmarked?" | "All arm's-length" without naming providers; no benchmark |
| `Q-MKT-01` (`GEN-18`) | "What submarket supply pipeline and absorption data support the rent-growth assumption?" | Metro-level optimism in place of submarket data; no supply pipeline acknowledged |
| `Q-LIQ-01` | "What are my options if I need to exit before the hold period ends?" | "A secondary market may develop"; "we'll try to accommodate" |

**Nice-to-ask**

| ID | Question | Bad-answer signal |
|---|---|---|
| `Q-DIST-02` | "When are capital calls expected, and what's the consequence of a missed or late call?" | "Calls as needed" with no notice period; punitive dilution buried in the docs |
| `Q-LIQ-02` | "When will K-1s be delivered each year, and have you historically delivered them before the filing deadline?" | "As soon as we can"; a history of extensions |
| `Q-GP-04` (`GEN-04`) | "How have your headcount and deal-monitoring capacity grown alongside AUM?" | "We're lean and efficient" as the whole answer |

---

## 9. Diligence Checklist

- [ ] PPM and operating agreement: fee schedule, waterfall, pref, clawback, distribution policy (including whether distributions can be paid from reserves or capital)
- [ ] Sponsor background: SEC/FINRA/state records, litigation search, principals' prior entities
- [ ] Rent roll and T-12 reconciled to bank statements or a third-party audit; check in-place NOI against a 7% Year-1 payout
- [ ] Rent and sale comps for the submarket; supply pipeline from a third-party source
- [ ] Appraisal or broker opinion of value at the going-in basis
- [ ] Lender term sheet and loan documents: rate, fixed/floating, cap expiry, maturity, extensions, prepayment, refi assumptions behind the capital-return schedule
- [ ] Realized track record verified from prior LPs' K-1s or distribution statements, not the sponsor deck
- [ ] Wrapper check: is the offering a direct LP interest or a feeder/fund-of-funds?

---

## 10. Verdict

**Pass as presented, insufficient disclosure.**

*Screening output only, not investment advice.*

**Reasoning.** Deal A states three things: multifamily, a 14% projected IRR, and a front-loaded distribution shape (7% quarterly from Year 1 plus progressive capital return). It omits the essentials `01` lists for multifamily: whether the return is gross or net, strategy, hold, sponsor, fees and waterfall, debt, financials, exit cap and track record. Those omissions mean the core return story can't be underwritten (`GEN-16` + `GEN-15` + `GEN-17` + `GEN-13`). That is a disclosure verdict, not a merits verdict. No RED fired on the stated facts.

**Biggest swing factor:** *what funds the early distributions and the progressive capital return.* If the 7% comes from in-place NOI and capital returns through operations or sales, Deal A is a genuinely lower-risk return shape. Less of the 14% rides on the exit, and that is its best argument against a back-loaded deal. If the 7% is paid from reserves or LP equity, or the capital return depends on a cash-out refinance, the front-loading is cosmetic and the risk sits back at the exit and the debt market (`EQUITY-07`, `GEN-09`, `GEN-10`). The second factor is gross vs net: ≈430 bps of plausible fee drag (§4) separates "clears comfortably" (≈908 bps over VNQ) from "clears thinly" (≈479 bps).

**Who it would suit, if it checks out:** an income-oriented LP who values early cash and wants capital back before the exit, and who accepts a single-asset, illiquid multifamily position for an as-yet-unstated hold.

**What would have to be true to re-screen as Pursue / Pursue with conditions:**
1. 14% confirmed as **net to LP**, or a fee stack and waterfall disclosed so net can be computed and still clears the 7-yr ~400–600 bps hurdle over VNQ (`Q-FEE-01`, `Q-FEE-03`, `Q-FEE-04`)
2. Year-1 7% shown to be covered by T-12 NOI (`Q-DIST-01`, `Q-RISK-03`)
3. The capital-return mechanism shown not to depend on a refinance, or a credible fallback if it does (`Q-EXIT-02`)
4. Debt maturity at or beyond the hold, with rate-cap coverage if floating (`Q-RISK-01`, `Q-RISK-02`)
5. An IRR decomposition showing the return is mostly cash flow, plus a bear case that preserves LP capital (`Q-DS-01`, `Q-DS-02`, `Q-DS-03`)
6. Realized net-to-LP track record and cash co-invest (`Q-GP-02`, `Q-GP-01`)

---

## Comparison Frame: Deal A vs Deal B (awaiting Deal B)

Paste Deal B and I'll screen it fully and fill in its column. Here is what the comparison will test:

| Axis | Deal A | Deal B |
|---|---|---|
| Headline IRR / basis | 14%, gross-vs-net **not stated** | — |
| Net-to-LP after fees | ≈9.7% (illustrative `02` stack) to 14% (if already net) 🔴 | — |
| Distribution start | Year 1, quarterly 🟢 | — |
| Current yield | 7% cash-on-cash 🟢 (funding source unverified) | — |
| Capital return | Progressive over the hold 🟢 (mechanism unstated) | — |
| Exit dependence (`GEN-08`) | Likely below 60% on stated shape 🟡; unconfirmed | — |
| Refi dependence (`EQUITY-07`) | Possible, since the capital-return mechanism is unstated | — |
| Hold / illiquidity hurdle | Not stated (5–7 yr → ~300–600 bps) | — |
| Premium over VNQ | ≈479–908 bps depending on gross/net | — |
| Disclosure sufficiency | Insufficient | — |

**How the J-curve will be read:** if Deal B quotes a similar IRR but pays little or nothing until a sale or refinance, its return is concentrated at the exit (`GEN-11`, and possibly `GEN-08`). Deal A's stated shape would then carry less timing risk, *provided* its early cash is real operating cash flow. Equal IRRs do not mean equal risk, and the comparison will rank the two on net-to-LP return, timing of capital back, and what each return depends on (operations vs exit vs refinance).

*Screening output only, not investment advice.*
