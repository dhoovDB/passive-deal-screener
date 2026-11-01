# Eval fixture 01
*Iteration-7 run, 2026-11-01, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 181fdd7.*

# Deal Screen: Sun Belt Value-Add Multifamily Syndication ($50M raise, 280 units)

**Verdict: PASS.** Most of the 16% / 2.0x comes from the sale, and the sale assumes a lower cap rate than the purchase (5.0% exit vs 5.5% going in). The deal also carries floating-rate bridge debt and a track-record claim nobody can check. Together, `GEN-07` + `GEN-08` + `EQUITY-06` make this a financing story, and the financing is the 2022–24 failure shape (`GEN-09`, `GEN-10` open).

*Screening output only, not investment advice.*

> **Not investment advice.** This screen decides whether the deal deserves more diligence. It is not financial, legal or tax advice, and the verdict is not a recommendation to invest.

Confidence tags: 🟢 stated in the deal or taken from a reference · 🟡 inferred · 🔴 assumed or unverifiable.

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Multifamily, value-add 🟢 |
| Deal type | Equity syndication 🟢 |
| Sponsor | **Not stated** |
| Geography | "Sun Belt". **Metro and submarket not stated** |
| Units | 280 🟢 |
| Equity raise | $50M 🟢 |
| Purchase price / total capitalization | **Not stated** |
| Minimum investment | **Not stated** |
| Hold | 5 years 🟢 (the `01` norm for this class is 5–7 years) |
| Claimed return | 16% IRR / 2.0x equity multiple 🟢. **It is not stated whether these are gross or net to LP** |
| Pref / promote / waterfall | 8% pref, 20% promote, American (deal-by-deal) 🟢. **Catch-up, cumulative vs non-cumulative, and clawback not stated** |
| Caps | Going-in 5.5%, exit 5.0% 🟢 |
| Debt | Bridge, floating rate 🟢. **Loan amount/LTV, spread, maturity, extensions and rate cap not stated** |
| Fees | 2% acquisition, 1.5% annual asset management, 1% disposition 🟢. **The base each fee is charged on is not stated** |
| Track record | "30% IRR across prior deals" 🟢 as stated, 🔴 unverified |
| Distribution schedule / cash-on-cash | **Not stated** |

---

## 2. Return Stress-Test

**The three assumptions that swing the result:** (1) **the exit cap**, 5.0% against 5.5% going in; (2) **the floating rate and the bridge takeout**, meaning whether the debt can be refinanced or extended inside a 5-year hold; (3) **rent growth after renovation**, i.e. the Sun Belt rent premiums that make the NOI growth happen.

| Case | What's assumed | Deal-level IRR (on the sponsor's quoted basis) |
|---|---|---|
| **Bull** | Renovation premiums are achieved, the rate cap and extensions hold, and buyers pay the sponsor's 5.0% cap | ~16% / 2.0x as marketed 🟢 |
| **Base (mine)** | Same NOI path, but the exit cap is flat at the 5.5% going-in cap | **~11–12%, ~1.6–1.7x** 🔴 illustrative |
| **Bear** | Exit cap 6.0% (+50bps over going-in). No relief on debt cost | **~6–8.5%, ~1.3–1.5x** 🔴 illustrative. That is below the 8% pref |

How the cases were built: holding NOI fixed, a flat 5.5% exit cap cuts the sale price by **9.1%** (5.0/5.5) 🟢 arithmetic. To turn that into equity returns I had to assume leverage of 60–70% LTV and level ~5%/yr distributions, because the deal discloses neither (🔴, illustration only). Leverage multiplies the 9.1% price cut into a ~19–26% cut in exit equity. **The verdict does not rest on these figures.** They show the direction and rough size of the risk. The fact that decides it is stated: the headline return assumes 50bps of cap-rate compression (🟢).

**Gross or net is unknown.** The deal doesn't say whether 16% is net to LP. If it is *gross*, `fee_drag_calculator.py` (16% gross, 5-year hold, 8% pref, 20% promote, 2% / 1.5%/yr / 1% fees; admin, loan placement and refi fees passed as 0 because they are undisclosed) estimates:

- **Net LP IRR ≈ 12.3%** with no catch-up (369 bps/yr drag)
- **Net LP IRR ≈ 11.4%** with a 100% catch-up (464 bps/yr drag). The catch-up isn't disclosed, so both are shown

**Benchmark (`benchmark_comparator.py`, VNQ 10-year 4.92%, 5-year lock-up → illiquidity hurdle ~300–400bps):**

| LP net IRR scenario | Premium over VNQ | Read |
|---|---|---|
| 16.0% (if the headline is already net) | 1108 bps | Clears comfortably |
| 12.3% / 11.4% (headline is gross; no catch-up / 100% catch-up) | 739 / 644 bps | Clears comfortably |
| ~11.7% (flat exit cap, quoted basis) | 678 bps | Clears |
| ~7.6% (exit cap 6.0%, quoted basis) | 268 bps | **Thin / fails** the hurdle |

Two more checks from `05`. First, the **10-year Treasury is 5.18%** 🟢, so this deal's underwritten **5.0% exit cap is below the risk-free rate at the snapshot date**. Second, on the headline the deal clears its benchmark, but the margin depends almost entirely on whether a buyer pays the sponsor's 5.0% cap. Move the cap 50bps above going-in and the deal falls below both the pref and the illiquidity hurdle. **The lock-up is only paid for if the cap compression actually happens.**

Dispersion matters too (`05`). Value-add multifamily targets 14–18% net, but realized results cluster at 12–15% blended (`01`) 🟢. A 16% claim sits in the upper half of the *marketed* range.

---

## 3. Where LP Returns Come From

**Exit-dependent: ~70–75% of the profit comes from the sale** 🟡. A 2.0x over 5 years means 1.0x of profit. Reaching a 16% IRR at that multiple requires average distributions of only about 5–6% a year (≈0.25–0.30x in total), so the sale has to supply the remaining ~0.70–0.75x. Even at 8% a year in distributions, the top of `01`'s stabilized cash-on-cash range of 5–8% and a level this renovation business plan won't reach in years 1–2, the exit still supplies 60% of the profit. That is above the >60% line → **`GEN-08`**.

**Leverage and cap compression, not operations** 🟡. `05`'s unlevered baseline: NCREIF NPI returned **5.00%** over the trailing four quarters, almost all of it income (residential 5.3% in 2025) 🟢. A 16% levered IRR against a ~5% unlevered in-place baseline means **~11 points come from leverage and assumed appreciation**. Part of that appreciation is cap-rate compression the sponsor assumed rather than earned (`EQUITY-06`). The leverage is also floating-rate bridge debt: the debt cost is a floating base (the 3-month bill is 4.24% at snapshot, used here as a proxy) plus an *undisclosed* spread. Any spread above ~125bps makes the all-in debt cost higher than the 5.5% going-in cap, so the debt would cost more than the property yields (**negative leverage**) from day one 🟡. → **`GEN-07`**.

**Cluster:** `GEN-07` + `GEN-08` + `EQUITY-06` fire together. Per `03`, the deal is a **financing story**: the return is a bet on rates and exit pricing, not on in-place cash flow.

---

## 4. Fee Stack Summary

| Fee | Stated | Base | `02` norm | Read |
|---|---|---|---|---|
| Acquisition | 2% | **Not stated** | 1–2% of equity, or 0.5–1.5% of purchase price. Aggressive above 2% of purchase price | At the top of the equity range. If it is 2% of *purchase price*, it is past the typical band and well above 2% of equity 🟡 |
| Asset management | 1.5%/yr | **Not stated** (equity raised vs invested vs revenue) | 1–2% of equity/yr | In range 🟢 |
| Disposition | 1% | **Not stated** (presumably sale price) | 0.5–1% of sale price | Top of range. On a levered sale price it is a multiple of 1% of equity. Check that it doesn't also pay the broker commission (double charge) |
| Promote | 20% over 8% pref | Deal-by-deal | 15–30% over 6–10% | In range 🟢 |
| Catch-up | **Not stated** | – | 50/80/100% are all seen | Swings drag by ~95 bps/yr (calculator) |
| Loan placement (bridge) | **Not stated** | – | 0.5–1.5% of loan | Bridge debt nearly always involves one. An absence here is a gap |
| Refinance (bridge takeout) | **Not stated** | – | 0.5–1% of new loan | Likely if the bridge is refinanced (`EQUITY-07`) |
| Construction management (renovation) | **Not stated** | – | 3–5% of hard costs | Heavy interior renovation usually carries one |
| Admin / IR / K-1 | **Not stated** | – | 0.1–0.5% of equity or $1–3k/LP | Gap |
| Affiliate property management | **Not stated** | – | – | `GEN-06` probe |

**Gross-to-net drag: ~369–464 bps/yr** (`fee_drag_calculator.py`: recurring fees 150 bps, one-time fees 60 bps, promote 159–254 bps depending on the undisclosed catch-up). **This is a floor.** Undisclosed fees (loan placement, refi, construction management, admin, affiliates) were passed as 0, and the one-time fees were modeled as % of equity, while their actual bases may be purchase and sale price. Each ASSUMED or zeroed input is a §6 gap.

---

## 5. Red Flags

**RED**

- **`EQUITY-06` Exit cap below going-in** 🟢. The 5.0% exit vs 5.5% entry builds 50bps of cap compression into the headline. A flat cap removes 9.1% of sale value before leverage, and the 5.0% exit cap sits below the 5.18% 10-year Treasury. LP exposure: the IRR depends on the exit price. → `Q-EXIT-01`.
- **`GEN-08` Exit-dependent IRR** 🟡. ~70–75% of profit comes from the sale (§3). LP exposure: the return is a single sale-price bet in year 5. → `Q-DS-01`.
- **`GEN-07` Financing story** 🟡. ~11 points of IRR above the ~5% unlevered NPI baseline come from leverage and assumed appreciation, on floating bridge debt that is likely negatively levered at entry. LP exposure: the return collapses if rates stay high or credit tightens. → `Q-DS-02`.
- **`GEN-09` Debt maturity inside the hold** 🟡. Bridge debt is short-duration by design (`01`), and the hold is 5 years. A takeout refinance or an early sale is forced into whatever market exists at maturity. Maturity and extensions are not disclosed. → `Q-RISK-01`.
- **`GEN-05` GP-IRR vs LP-IRR divergence** 🔴 unverified. "30% IRR track record across prior deals" doesn't say whether it is project-level, GP-level or net-to-LP. Until it is restated, treat it as project/GP-level. → `Q-GP-02`.
- **`GEN-14` Unrealized track record** 🔴 unverified. The claim doesn't separate realized exits from marks. Paired with `GEN-05`, that is a RED cluster: there is no validated LP-outcome data. `01` specifically requires prior **multifamily exits**. → `Q-GP-02`.

**YELLOW–RED**

- **`EQUITY-07` Refinance-dependent plan** 🟡. Bridge debt implies either a refinance into permanent debt or a sale before maturity. If the refi isn't available on the assumed terms, distributions and the 5-year path break. → `Q-EXIT-02`.
- **`GEN-10` Rate-cap expiry risk (open, not yet fired)** 🔴. The deal has floating debt, but the cap's term, strike and expiry vs maturity are undisclosed. This is the specific 2022–24 pattern (cap expires → debt service spikes → refi frozen). It is treated as RED until answered. → `Q-RISK-02`.
- **`GEN-15` Missing financials** 🟢. No rent roll, T-12 or full debt terms. → `Q-RISK-03`.
- **`GEN-16` Incomplete fee/waterfall disclosure** 🟢. Fee bases, catch-up, pref mechanics, financing/admin/construction fees are all missing, so drag can only be bounded. → `Q-FEE-01`.
- **`GEN-06` Affiliate fee stacking (probe)** 🔴. Property management, construction management and loan placement are undisclosed, and this business plan typically uses all three. → `Q-FEE-02`.

**YELLOW**

- **`GEN-11` No distribution schedule** 🟢. An IRR is quoted with no distribution timing. Combined with `GEN-08`, the return is back-loaded to the exit. → `Q-DIST-01`.
- **`GEN-13` No sensitivity or downside case** 🟢. A single-point 16% / 2.0x. → `Q-DS-03`.
- **`GEN-18` Rent-growth assumption without submarket data** 🟡. The renovate-and-raise plan depends on Sun Belt rent premiums, and no submarket supply or absorption is given. → `Q-MKT-01`.
- **`GEN-17` Essential category disclosures absent** 🟢. These are missing against the `01` value-add multifamily list: T-12, rent roll, exit-cap sensitivity, debt structure/maturity, refi assumptions, and prior multifamily exits. → `Q-RISK-03`, `Q-GP-02`.

**Considered, not fired:** (`EQUITY-01`) The deal-by-deal waterfall is standard for retail syndications, and a 20% promote is not "high" (the threshold is >30%). For a single asset, deal-by-deal vs whole-of-fund matters little. (`EQUITY-02`) Clawback is undisclosed, but with one asset there are no "later deals" to lose on. Confirm anyway. (`EQUITY-03`, `EQUITY-05`) Catch-up and cumulative status are unknown, so they become questions rather than flags. (`EQUITY-04`) The 8% pref is at market. (`GEN-01`) Co-invest is unknown and becomes a must-ask.

**Clusters:** the financing story is `GEN-07` + `GEN-08` + `EQUITY-06`. The debt-failure chain is `GEN-09` + `GEN-10` + `EQUITY-07`. Unvalidated sponsor is `GEN-05` + `GEN-14`.

---

## 6. Missing Disclosures

Measured against the `01` essential disclosures for value-add multifamily and the `02` equity-syndication fee inventory:

1. **Gross vs net basis** of the 16% IRR / 2.0x.
2. **Rent roll and T-12 actuals**, plus current occupancy.
3. **Exit-cap sensitivity**: IRR at 5.5% and 6.0%.
4. **Debt structure**: loan amount/LTV, spread, maturity, extension options and their tests, **rate cap (strike, term, expiry, cost to replace)**, recourse, reserves.
5. **Refi / takeout assumptions**: rate, proceeds, timing.
6. **Business-plan inputs the return rests on**: renovation premium per unit, rent-growth assumption, purchase price.
7. **Distribution schedule** and projected cash-on-cash by year.
8. **Fee bases** (acquisition, asset management, disposition), plus loan placement, refinance, construction management, admin/IR, and any affiliate property-management fee.
9. **Waterfall detail**: catch-up rate, cumulative/compounding pref, clawback.
10. **Sponsor identity**, GP co-invest (amount, cash, pari-passu), and the **track record as realized, net-to-LP, prior multifamily exits**.
11. **LP terms**: minimum, capital-call provisions, transfer/liquidity rights, K-1 timing.

Calculator inputs that are ASSUMED or zeroed because of these gaps: catch-up (run at 0% and 100%), and admin, loan placement and refi fees (0).

---

## 7. GP Alignment

- **Co-invest:** **Not stated.** Amount, whether it's cash or fee waivers, and whether it's pari-passu are all unknown (`GEN-01` probe).
- **Track record:** "30% IRR across prior deals" is **unverified** 🔴. The deal doesn't say whether it is realized or marked, net-to-LP or project-level, or how many deals and which vintages. A 30% figure from a 2010s–2021 multifamily vintage would be consistent with cap-rate compression rather than skill. That is the same tailwind this deal assumes will continue. Treat it as **no track record** until restated (`GEN-05`, `GEN-14`).
- **Waterfall alignment:** an 8% pref with a 20% promote is market 🟢. The undisclosed catch-up determines whether the GP takes 12.7% or 20% of profit (calculator). With deal-by-deal on one asset, the waterfall structure is not the problem.
- **Fees vs outcome:** acquisition, asset management and disposition fees pay the GP whether or not the deal returns its 8% pref. Undisclosed affiliate fees could add more (`GEN-06`).

---

## 8. Questions for the GP

**Must-ask**

| ID | Question | Bad-answer signal | Why |
|---|---|---|---|
| `Q-EXIT-01` | Why is the exit cap below the going-in cap, and what's the IRR at an exit cap equal to or above going-in? | "Cap rates will compress"; the IRR breaks at a flat cap; no sensitivity offered | `EQUITY-06` fired |
| `Q-DS-01` | What share of projected LP IRR comes from in-place cash flow vs the exit, and what's the IRR at a flat exit cap? | Can't decompose it; "real estate always appreciates"; the IRR falls below the 8% pref at a flat cap | `GEN-08` fired |
| `Q-DS-02` | Strip out leverage and cap-rate compression: what is the unlevered, in-place return? | The levered IRR is the only figure; "leverage is just how the deal works" | `GEN-07` fired |
| `Q-DS-03` | What is the return under a bear case: flat rents, higher exit cap, no refinance? | Single-point pro forma; "we underwrite conservatively" with nothing to show | `GEN-13` fired |
| `Q-RISK-01` | When does the bridge debt mature relative to the 5-year hold, and what's the refinance or extension plan? | Maturity falls inside the hold; "we'll refinance" with no terms | `GEN-09` fired |
| `Q-RISK-02` | When does the rate cap expire relative to debt maturity, and what does it cost to extend at current pricing? | The cap expires before maturity; extension cost not modeled; "rates should be lower by then" | `GEN-10` open |
| `Q-EXIT-02` | Does the plan depend on a refinance, and what happens to distributions if the refi isn't available on the assumed terms? | Capital return requires a refi at lower rates; no fallback; "the refi market will reopen" | `EQUITY-07` fired |
| `Q-RISK-03` | Can you provide the T-12, rent roll and complete debt terms? | T-3/T-6 only; "confidential until you commit" | `GEN-15`, `GEN-17` |
| `Q-GP-02` | Restate the "30% IRR" as net-to-LP IRR on fully realized, exited deals only. | Only project/GP-level IRR; "most deals are still performing"; can't separate realized from marked | `GEN-05`, `GEN-14` |
| `Q-GP-01` | How much of your own capital is in this deal, on the same terms as LPs? | "Sweat equity"; a fee waiver instead of cash; a token amount on better terms | Co-invest undisclosed |
| `Q-GP-03` | Any regulatory action, enforcement, or investor litigation for you or your principals? | "Nothing material"; a search turns up something they didn't disclose | Unidentified sponsor |
| `Q-FEE-01` | Provide the complete fee schedule (with bases) and the full waterfall. | "Standard market fees"; "the PPM has it" without producing it | `GEN-16` fired |
| `Q-FEE-02` | Which providers (property management, construction management, loan placement) are GP-affiliated, and at what rates? | "All arm's-length" without naming them; no benchmark | `GEN-06` probe |
| `Q-FEE-03` | Deal-by-deal or whole-of-fund, and is there a clawback? What is the catch-up? | Can't explain the catch-up; "you get paid when we get paid" | Stated American waterfall |
| `Q-FEE-04` | Is the 8% pref cumulative, and does unpaid pref compound? | Non-cumulative; simple-only without saying so | Stated 8% pref |
| `Q-MKT-01` | What submarket supply pipeline and absorption data support the post-renovation rent growth? | Metro or "Sun Belt" optimism instead of submarket data; no supply pipeline acknowledged | `GEN-18` fired |
| `Q-DIST-01` | What is the projected distribution schedule, and when does LP capital start returning? | "When the deal supports it"; an IRR with no timing | `GEN-11` fired |
| `Q-LIQ-01` | What are my options if I need to exit before year 5 (or an extended hold)? | "A secondary market may develop"; silence | 5-year lock-up |

**Nice-to-ask**

| ID | Question | Bad-answer signal |
|---|---|---|
| `Q-GP-04` | How have headcount and asset management capacity grown alongside AUM (this is a $50M raise)? | AUM multiplied while the team stayed flat; no named asset manager |
| `Q-DIST-02` | Are capital calls possible (e.g., to buy a new rate cap or pay down the bridge), and what are the consequences of missing one? | "Calls as needed"; punitive dilution buried in the documents |
| `Q-LIQ-02` | When are K-1s delivered, and have they historically arrived before the filing deadline? | "As soon as we can"; a history of extensions |

---

## 9. Diligence Checklist

- **PPM / operating agreement:** fee bases, catch-up, cumulative pref, clawback, capital-call and dilution terms, GP removal rights.
- **Loan documents (independent read):** maturity, extension tests (DSCR/debt yield), rate-cap agreement and expiry, replacement-cap requirement, recourse and carve-outs.
- **Lender confirmation:** whether extension tests are achievable on the in-place NOI.
- **Background / regulatory check** on the sponsor and principals (SEC/FINRA/state, litigation search).
- **Track-record verification:** realized deal list with net-to-LP distributions, ideally confirmed by prior LPs or an administrator.
- **Third-party valuation / sales comps:** recent submarket multifamily cap rates, to test both 5.5% in and 5.0% out.
- **Rent comps:** renovated vs classic units in the submarket, to test the rent premium.
- **Submarket supply/absorption:** an independent source.
- **Audited or third-party-prepared T-12 and rent roll.**

---

## 10. Verdict

**PASS**

*Screening output only, not investment advice.*

**Reasoning.** Enough is disclosed to underwrite how this deal says it makes money, and the answer is a financing story (`GEN-07` + `GEN-08` + `EQUITY-06`). About three-quarters of the profit has to come from a sale in year 5. That sale assumes a buyer pays a 5.0% cap, 50bps tighter than entry and below today's 5.18% 10-year Treasury. The deal is funded with floating bridge debt that likely matures inside the hold (`GEN-09`), with unknown rate-cap protection (`GEN-10`) and a takeout refinance it depends on (`EQUITY-07`). That is the exact chain behind the 2022–24 multifamily capital calls. The one piece of evidence that the sponsor can deliver, "30% IRR across prior deals," is unverified (`GEN-05`, `GEN-14`). If 16% is gross, fees and promote take the LP to roughly 11.4–12.3% net before any of these risks play out.

**Biggest swing factor:** the exit cap. A flat 5.5% exit takes the illustrative IRR to ~11–12%. A 6.0% exit takes it to ~6–8.5%, below the 8% pref and short of the ~300–400bps illiquidity hurdle over VNQ.

**Who it could suit:** an LP who wants a leveraged bet on falling rates and cap compression in Sun Belt multifamily, can tolerate a capital call or loss of principal, and has independently verified this sponsor's realized exits.

**What would have to be true to re-screen as Pursue with conditions:**
1. The IRR still clears the 8% pref, net to LP, at an exit cap of at least 5.5%, and LP capital survives a 6.0% exit (`Q-EXIT-01`, `Q-DS-01`, `Q-DS-03`).
2. The bridge debt's fully extended maturity covers the 5-year hold under extension tests the in-place NOI can meet, and the rate cap runs to maturity or its replacement is budgeted (`Q-RISK-01`, `Q-RISK-02`, `Q-EXIT-02`).
3. The track record is restated as realized, net-to-LP returns on prior multifamily exits, at a credible level (`Q-GP-02`).
4. The full fee schedule with bases, the catch-up and pref terms, affiliate fees, and meaningful cash GP co-invest are disclosed (`Q-FEE-01`–`Q-FEE-04`, `Q-GP-01`).
5. The T-12, rent roll and submarket supply data support the renovation premium (`Q-RISK-03`, `Q-MKT-01`).
