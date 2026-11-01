# Eval fixture 01
*Iteration-7 run, 2026-11-01, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 181fdd7.*

# Passive Deal Screen: Sun Belt Value-Add Multifamily Syndication (280 units, $50M equity)

**Verdict: Pursue with conditions.** This is a financing story (`GEN-07` + `GEN-08` + `EQUITY-06`): the deal underwrites exit-cap compression (5.5% in, 5.0% out) on floating-rate bridge debt. The conditions below are hard gates. If any one fails, the verdict becomes Pass.

Screening output only, not investment advice.

Confidence tags: 🟢 stated in the deal or taken from a reference · 🟡 inferred · 🔴 assumed or unverifiable.

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Multifamily, value-add 🟢 |
| Deal type | Equity syndication, single asset 🟢 |
| Sponsor | Not stated (unnamed). Claims a "30% IRR track record across prior deals" 🟢 (basis unverified 🔴) |
| Geography | "Sun Belt" 🟢. Metro and submarket not stated |
| Units | 280 🟢 |
| Equity raise | $50M 🟢 |
| Purchase price / loan amount / LTV | Not stated |
| Minimum investment | Not stated |
| Hold | 5 years 🟢 (at the short end of the `01` 5–7 yr norm) |
| Claimed return | 16% IRR / 2.0x equity multiple 🟢. **Gross or net-to-LP is not stated** |
| Business plan | Renovate interiors, raise rents 🟢 |
| Pref / promote / waterfall | 8% pref, 20% promote, American (deal-by-deal) 🟢. Catch-up, cumulative/compounding, and clawback not stated |
| Cap rates | Going-in 5.5%, underwritten exit 5.0% 🟢 |
| Debt | Bridge, floating rate 🟢. Maturity, extensions, rate cap, LTV, and spread not stated |
| Fees | 2% acquisition, 1.5% annual asset management, 1% disposition 🟢. The base each fee is charged on is not stated, and the rest of the stack is not stated |
| GP co-invest | Not stated |
| Distribution schedule | Not stated |

---

## 2. Return Stress-Test

**Swing assumptions:** (1) exit cap, (2) rent growth from the renovation premium, (3) the bridge-debt path (rate cap, maturity, and refi or extension terms).

| Case | Assumptions | Read |
|---|---|---|
| **Bull** | Renovation premiums land, rents grow as underwritten, cap rates compress to 5.0%, bridge is refinanced or the asset is sold before cap or maturity stress | Sponsor's 16% / 2.0x, if the 16% is net. If it is gross, about 11.4–12.3% net (see §4) 🟡 |
| **Base (screen's view)** | Rents roughly as underwritten, **exit cap flat at 5.5%** | At the same NOI, exit value is **~9.1% lower** than underwritten (5.0/5.5 = 0.909) 🟢 arithmetic. Leverage magnifies that cut at the equity level by V/(V−D). For illustration only, at 65% loan-to-value at exit 🔴 assumed, the 9.1% value cut takes **~26% off exit equity**. The sponsor has not provided a flat-cap IRR (`Q-EXIT-01`). |
| **Bear** | Exit cap at or above going-in, rent growth stalls (`GEN-18` probe), rate cap expires before the loan matures (`GEN-10` probe), and the bridge has to refinance or extend on worse terms (`EQUITY-07`, `GEN-09` probe) | Debt service rises while NOI growth stalls, distributions stop, and a capital call or rescue raise becomes possible. This is the 2022–24 multifamily-syndication pattern named in `03`. LP principal is at risk, not just the return. The size of the loss can't be told from this disclosure 🔴. |

No sensitivity or downside case was provided (`GEN-13`).

**Benchmark (net-to-LP vs `05`; `benchmark_comparator.py`, multifamily-value-add, 5-yr lock-up):**

| Net-to-LP IRR used | Premium over VNQ (4.92% 10yr) | Illiquidity hurdle (5 yr) | Script read |
|---|---|---|---|
| 16.00% (if the sponsor's figure is already net) 🔴 basis unknown | ≈1,108 bps | ~300–400 bps | Clears comfortably |
| 12.31% (16% treated as gross, 0% catch-up) 🔴 | ≈739 bps | ~300–400 bps | Clears comfortably |
| 11.36% (16% treated as gross, 100% catch-up) 🔴 | ≈644 bps | ~300–400 bps | Clears comfortably |
| 8.00% (break-even probe) | ≈308 bps | ~300–400 bps | Clears (thin) |

- **What the LP needs:** a net-to-LP IRR of about **8.2–9.2%** clears VNQ plus the 5-year premium. The 10yr Treasury (5.18%) currently out-yields VNQ's trailing 10yr return, which makes it the tighter floor. Against the Treasury the same hurdle is about 8.5–9.2% 🟢 (`05`).
- **Pro forma vs reality:** on paper the deal clears easily. But the `01` realized range for this category is **12–15% net blended**, and dispersion (`05` → Preqin note) means a below-median outcome is a real possibility. The premium only exists if the exit-cap and debt assumptions hold. In the bear case it can fall below the ~8–9% bar. Beating the comparator is necessary, not sufficient.

---

## 3. Where LP Returns Come From

- **Exit vs cash flow (`GEN-08`, 🟡 inferred).** A 2.0x multiple means $50M of profit on $50M of equity. `01` puts value-add cash-on-cash at 5–8% *after stabilization*. During the renovation period, with floating-rate bridge debt, it is typically lower. Even at an average of 5% a year across all five years 🟡, operations return about $12.5M, which leaves about **75% of the profit dependent on the sale**. That is above the 60% threshold. A 16% IRR alongside a 2.0x multiple (a single payment at year 5 would give ≈14.9%) points to some interim distributions, but not enough to change that conclusion. The GP must provide the actual split (`Q-DS-01`).
- **Exit-cap compression is baked in (`EQUITY-06`, 🟢 stated).** The exit cap of 5.0% is 50 bps below the going-in 5.5%. About 10% of exit value (5.5/5.0 = 1.10) comes from assuming the market pays a higher multiple in five years, not from operations.
- **Leverage vs operations (`GEN-07`, 🟢 benchmark / 🟡 application).** The `05` unlevered overlay is NCREIF NPI at **5.00%** trailing four quarters, almost all of it income, and residential NPI was 5.3% in 2025. A 16% headline is therefore about **11 points above the unlevered, in-place return** of institutional real estate. Those points come from leverage, assumed rent growth, and cap compression. The financing on this deal is floating-rate bridge debt, which is the most rate-sensitive, shortest-dated form of leverage.
- **Conclusion:** more than 60% of the return depends on the exit and on leverage, so rules 3 and 4 both fire. The three-flag cluster (`GEN-07` + `GEN-08` + `EQUITY-06`) means `03` requires the verdict to call this a **financing story**. The asset story (interior renovations driving rent premiums) is real but unmeasured: no rent roll, T-12, or renovation-premium evidence was provided (`GEN-15`).

---

## 4. Fee Stack Summary

| Fee | Stated | `02` typical | `02` aggressive | Read |
|---|---|---|---|---|
| Acquisition | 2% (base not stated) | 1–2% of equity, or 0.5–1.5% of purchase price | >2.5% of equity, or >2% of purchase price | Top of range if charged on equity. **At the aggressive line if charged on purchase price.** |
| Asset management | 1.5% annual (base not stated) | 1–2% of equity raised, annual | >2.5% | In range. Equity raised vs invested capital vs revenue changes the drag |
| Disposition | 1% (base not stated) | 0.5–1% of sale price | >1.5% | Top of range. Confirm there is no double charge alongside the brokerage commission |
| Promote | 20% over 8% pref | 15–30% over 6–10% pref | >30%, or pref <6% | In range |
| Catch-up | Not stated | 50 / 80 / 100% | 100% is the aggressive lever (`EQUITY-03`) | Modeled at both 0% and 100% |
| Loan placement / refinance | Not stated | 0.5–1.5% of loan / 0.5–1% of new loan | >2% / >1.5% | **Likely present** 🟡: bridge financing on a 5-yr hold implies a refinance or extension event |
| Construction management | Not stated | 3–5% of hard costs | >6% | Common on interior-renovation plans; absence needs confirming |
| Investor relations / admin | Not stated | 0.1–0.5% of equity or $1–3k/LP | >$5k/LP | Passed as 0 |
| Property management / affiliates | Not stated | — | — | `GEN-06` probe |

**Gross-to-net drag (`fee_drag_calculator.py`, 16% treated as gross 🔴, 5-yr hold, undisclosed fees = 0):**

| Scenario | Recurring | One-time | Promote | **Total drag** | Net LP IRR |
|---|---|---|---|---|---|
| Fees on equity, **100% catch-up** (catch-up not disclosed, so the script's ASSUMED default) | 150 bps | 60 bps | 254 bps | **≈464 bps/yr** | 11.36% |
| Fees on equity, **0% catch-up** | 150 bps | 60 bps | 159 bps | **≈369 bps/yr** | 12.31% |
| Acquisition and disposition on **purchase / sale price**, at an illustrative ~60% LTV 🔴 (≈5% and ≈2.5% of equity), 100% catch-up | 150 bps | 150 bps | 254 bps | **≈554 bps/yr** | 10.46% |

**Headline figure: ≈464 bps/yr of gross-to-net drag** on the disclosed stack, with a range of ≈369–554 bps depending on the undisclosed catch-up and fee bases. That figure excludes the fees not disclosed (loan placement, refinance, construction management, admin, affiliate property management), so the true drag is **higher**.

The deeper problem is that we don't know whether the 16% is gross or net:
- If 16% is gross, the LP's net is about 10.5–12.3%, which sits at or below the low end of the `01` realized range.
- If 16% is net, the implied gross is about 20%+ on a stabilized-acquisition business plan. That is development-level territory per `01`.

ASSUMED inputs that are §6 gaps: catch-up rate, fee bases, IRR basis (gross vs net), and LTV.

---

## 5. Red Flags

**RED**

- **`GEN-07` Financing story** (🟢 benchmark / 🟡 application). About 11 points of a 16% headline sit above the 5.0% unlevered NPI baseline and depend on floating bridge leverage plus cap compression. LP exposure: the return falls apart if rates stay high or credit tightens at refi or exit. → `Q-DS-02`
- **`GEN-08` Exit-dependent IRR** (🟡). By inference, about 75% of profit depends on the sale (§3). LP exposure: the deal is a bet on the sale price, not on income. → `Q-DS-01`
- **`EQUITY-06` Aggressive exit cap** (🟢). The exit cap of 5.0% is below the going-in 5.5%, which builds about 10% of exit value from assumed compression. LP exposure: at a flat cap, exit equity falls by a leverage multiple of 9.1%. → `Q-EXIT-01`, `Q-DS-01`
- *Cluster:* `GEN-07` + `GEN-08` + `EQUITY-06` together mean `03` calls this a **financing story** explicitly.
- **`GEN-05` GP-IRR vs LP-IRR divergence** (🟢 that no basis was given / 🔴 the actual figure). "30% IRR across prior deals" has no net-to-LP or realized qualifier. That is about double the `01` realized blended range of 12–15%, which suggests 🟡 a project-level, gross, or short-hold-flattered figure. LP exposure: there is no validated record of LP outcomes. Treat as RED until restated. → `Q-GP-02`
- **`GEN-14` Unrealized-only track record** (🔴 can't tell). The sponsor did not separate realized exits from marks. Together with `GEN-05` this is a RED cluster under the `03` notes, not two soft gaps. → `Q-GP-02`

**YELLOW–RED**

- **`EQUITY-07` Refi-dependent business plan** (🟡). `01` and `02` classify bridge debt as short-duration. Pairing it with a 5-year hold implies an extension, a refinance, or a sale timed to the debt rather than the business plan. LP exposure: the refi market can freeze, as it did in 2022–24. → `Q-EXIT-02`
- **`GEN-15` Missing financials** (🟢 absent). No rent roll, T-12, or complete debt terms were provided. LP exposure: the renovation premium and in-place NOI can't be checked. → `Q-RISK-03`
- **`GEN-16` Incomplete fee and waterfall disclosure** (🟢 partial). Fee bases, catch-up, cumulative/compounding, clawback, and financing, construction, admin, and affiliate fees are all absent. LP exposure: the drag in §4 is a floor, not the full figure. → `Q-FEE-01`

**YELLOW**

- **`GEN-13` No sensitivity or downside case** (🟢 absent). The pro forma is a single point resting on its three most fragile assumptions. → `Q-DS-03`
- **`GEN-11` No distribution schedule** (🟢 absent). An IRR was quoted with no timing, so we can't tell whether capital comes back early or only at exit. → `Q-DIST-01`
- **`GEN-17` Essential category disclosures absent** (🟢). `01` lists the exit cap *with sensitivity*, debt structure and maturity, refi assumptions, and the GP's record on *prior multifamily exits*. None of these were provided. → `Q-RISK-03`, `Q-DS-03`, `Q-GP-02`

**Probed, not fired.** These need a term the deal didn't disclose. They are must-asks, not flags.

- **`GEN-10` Rate cap expiry.** The loan is floating-rate bridge debt, but no rate cap is disclosed. If the cap expires before maturity, this becomes RED immediately. → `Q-RISK-02`
- **`GEN-09` Debt maturity inside the hold.** The bridge maturity isn't stated. Given what bridge debt is, a maturity inside the hold is likely 🟡. → `Q-RISK-01`
- **`GEN-18` Rent growth vs submarket supply.** The plan depends on rent growth, but no submarket is named. → `Q-MKT-01`
- **`GEN-01` GP co-invest** not stated. → `Q-GP-01`
- **`GEN-02` Regulatory or litigation history** not stated. → `Q-GP-03`
- **`GEN-06` Affiliate fees** not stated. → `Q-FEE-02`
- **`EQUITY-01` / `EQUITY-02`.** The deal-by-deal waterfall at a 20% promote is in range per `02`, so `EQUITY-01` does not fire on its own. Clawback is unstated. For a single asset, the practical risk is promote paid on interim or refi proceeds before LP capital comes back. → `Q-FEE-03`
- **`EQUITY-03` Catch-up** unstated. → `Q-FEE-03`
- **`EQUITY-05` Cumulative pref** unstated. → `Q-FEE-04`
- **`EQUITY-04`** does not fire, because an 8% pref is at or above the 6% floor.

---

## 6. Missing Disclosures

These are the disclosures `01` (multifamily value-add essentials) and `02` (equity-syndication fee inventory and waterfall) say a deal of this type normally carries. This deal omitted them all.

1. **Net-to-LP vs gross basis** of the 16% IRR and 2.0x multiple.
2. **Rent roll and T-12 actuals** (`GEN-15`).
3. **Debt terms.** Lender, loan amount and LTV, spread over index, maturity, extension options and their tests, **rate cap strike, expiry, and replacement cost**, and recourse.
4. **Refinance or exit assumptions.** Whether the plan needs a refi, and on what terms.
5. **Exit-cap sensitivity**, plus a downside case at an exit cap at or above 5.5%.
6. **Rent-growth and renovation-premium assumptions**, with submarket supply and absorption, and the specific metro and submarket.
7. **Distribution schedule** and when LP capital starts coming back.
8. **Fee bases.** Acquisition on equity or purchase price, asset management on equity raised or invested capital, disposition on sale price.
9. **Undisclosed fee categories.** Loan placement, refinance, construction management, admin/IR, property management, and whether any provider is a GP affiliate.
10. **Waterfall detail.** Catch-up rate, cumulative or non-cumulative pref, simple or compounding pref, clawback, and treatment of refinance proceeds.
11. **GP co-investment.** Amount, whether it is cash, and whether it is pari passu.
12. **Realized, net-to-LP track record** on prior multifamily exits.
13. **Sponsor identity, minimum investment, capital-call provisions, and LP liquidity / transfer terms.**

---

## 7. GP Alignment

- **Co-invest:** not stated. Alignment is asserted, not shown. `Q-GP-01` must confirm cash, the amount, and pari-passu terms, not a fee waiver or sweat equity. 🔴
- **Track record:** **unverified.** "30% IRR across prior deals" names no realized vs unrealized split, no project vs net-to-LP basis, no deal count, and no hold periods. Under the skill's rules, a marks-only or project-level IRR is not a track record. The figure is about twice the realized category range, which is itself a reason for skepticism 🟡. (`GEN-05`, `GEN-14`)
- **Waterfall alignment:** an 8% pref with a 20% promote is market-standard per `02` 🟢. The protections an LP needs are unknown: the catch-up rate (100% vs 50% moves promote drag by ≈95 bps/yr in §4), whether the pref is cumulative, and the clawback. In a single-asset American waterfall, the specific risk is the GP taking promote on refinance proceeds while the LP's capital is still at risk in the asset.
- **Fee alignment:** acquisition and disposition fees pay the GP to buy and to sell regardless of outcome. Both sit at the top of the `02` range, and the acquisition fee may sit at the aggressive line depending on its base. A short 5-year hold with fees at both ends pays the GP for a fast round trip.
- **Affiliate fees:** unknown (`GEN-06`). Property management and construction management on a renovation plan are common affiliate channels.

---

## 8. Questions for the GP

**Must-ask**

| ID | Question | Bad-answer signal (the specific dodge) | Flag |
|---|---|---|---|
| `Q-DS-01` | What share of projected LP IRR comes from in-place cash flow versus the exit, and what's the IRR at a flat exit cap? | Can't or won't break down the IRR; pivots to "real estate always appreciates"; the IRR falls below the 8% pref at a flat cap. | `GEN-08`, `EQUITY-06` |
| `Q-EXIT-01` | Why is the exit cap (5.0%) below the going-in cap (5.5%), and what's the IRR at an exit cap equal to or above going-in? | "Cap rates will compress"; the IRR breaks at a flat exit cap; no sensitivity offered. | `EQUITY-06` |
| `Q-DS-02` | Strip out leverage and cap-rate compression. What is the unlevered, in-place return? | Treats the levered IRR as the only relevant figure; "leverage is just how the deal works"; no unlevered view exists. | `GEN-07` |
| `Q-DS-03` | What is the return under a bear case: flat rents, higher exit cap, no refinance? | A single-point pro forma; "we underwrite conservatively" with nothing to show; a bear case that is still a gain. | `GEN-13` |
| `Q-RISK-02` | When does the rate cap expire relative to debt maturity, and what does it cost to extend at current pricing? | The cap expires before maturity; extension cost isn't modeled; "rates should be lower by then." | `GEN-10` |
| `Q-RISK-01` | When does the bridge loan mature relative to the 5-year hold, and what's the refinance or extension plan? | Maturity falls inside the hold; "we'll refinance" with no terms; no plan if the refi market shuts. | `GEN-09` |
| `Q-EXIT-02` | Does the business plan depend on a refinance, and what happens to distributions if the refi isn't available on the assumed terms? | Distributions or return of capital require a refi at lower rates; no fallback; "the refi market will reopen." | `EQUITY-07` |
| `Q-RISK-03` | Can you provide trailing-twelve-month actuals, the rent roll, and complete debt terms? | T-3/T-6 only; the rent roll is withheld; "the financials are confidential until you commit." | `GEN-12`, `GEN-15` |
| `Q-GP-02` | Can you restate the "30% IRR" track record as net-to-LP IRR on fully realized, exited deals only? | Offers only project-level or GP-level IRR; "most deals are still performing"; can't separate realized from unrealized. | `GEN-05`, `GEN-14` |
| `Q-GP-01` | How much of your own capital is in this deal, on the same terms as LPs? | "Our sweat equity is our investment"; the co-invest is a fee waiver rather than cash; a token amount on better terms than LPs. | `GEN-01` |
| `Q-GP-03` | Have you or your principals faced any regulatory action, enforcement, or investor litigation? | "Nothing material"; blames the LP or regulator; a search surfaces something they didn't disclose. | `GEN-02` |
| `Q-FEE-01` | Can you provide the complete fee schedule, including the base for each fee, and the full distribution waterfall? | "Standard market fees"; a partial list; "the PPM has it" without producing it; fees surface only after commitment. | `GEN-16` |
| `Q-FEE-02` | Which service providers (property management, construction management, loan placement) are GP-affiliated, what do they charge, and are the rates benchmarked against third parties? | "All arm's-length" without naming providers; affiliate fees undisclosed; no benchmark offered. | `GEN-06` |
| `Q-FEE-03` | Is the waterfall deal-by-deal or whole-of-fund, what is the catch-up rate, and is there a clawback, including on promote paid from refinance proceeds? | Deal-by-deal with no clawback; can't explain the catch-up; "you get paid when we get paid." | `EQUITY-01`, `EQUITY-02` (`EQUITY-03`) |
| `Q-FEE-04` | Is the 8% pref cumulative and compounding? | Non-cumulative; simple-only with no carry-forward; evasive on how unpaid pref is treated. | `EQUITY-04`, `EQUITY-05` |
| `Q-MKT-01` | What submarket supply pipeline and absorption data support the rent-growth and renovation-premium assumptions? | Metro-level or "Sun Belt" optimism in place of submarket data; "rents always go up here"; no supply pipeline acknowledged. | `GEN-18` |
| `Q-DIST-01` | What is the projected distribution schedule, and at what milestones does LP capital start coming back? | "We'll distribute when the deal supports it" with no milestones; an IRR with no timing; silence. | `GEN-11` |
| `Q-LIQ-01` | What are my options if I need to exit before the hold ends? | "A secondary market may develop"; "we'll try to accommodate"; silence about the lock-up. | — |

**Nice-to-ask**

| ID | Question | Bad-answer signal | Flag |
|---|---|---|---|
| `Q-GP-04` | How have your headcount and deal-monitoring capacity grown alongside AUM? | AUM multiplied while the team stayed flat; "we're lean and efficient" as the whole answer; no named asset manager. | `GEN-04` |
| `Q-DIST-02` | When are capital calls expected, and what's the consequence of a missed or late call? | "Calls as needed" with no notice period; punitive dilution buried in the docs. More important than usual here, because bridge-debt stress is the classic trigger for a capital call. | — |
| `Q-LIQ-02` | When will K-1s be delivered each year, and have you historically delivered them before the filing deadline? | "As soon as we can"; a history of extensions. | — |

---

## 9. Diligence Checklist

- [ ] **PPM and operating agreement.** Read the waterfall (catch-up, cumulative pref, clawback, treatment of refi proceeds), the fee definitions and their bases, capital-call and dilution provisions, and transfer restrictions.
- [ ] **Loan documents and term sheet.** Confirm maturity, extension tests (DSCR / debt yield), rate cap strike and expiry, cap-replacement escrow requirements, recourse and carve-outs.
- [ ] **Rent roll and T-12** checked against the offering's in-place NOI and against the going-in 5.5% cap.
- [ ] **Third-party rent comps** for renovated vs classic units in the specific submarket, plus submarket supply pipeline data.
- [ ] **Appraisal or broker opinion of value**, including current submarket cap rates against the 5.0% exit assumption.
- [ ] **Sponsor background check.** SEC/FINRA/state records, litigation searches, and references from LPs in prior deals, *including deals that went badly*.
- [ ] **Realized track-record verification.** Prior offering memos against actual distribution statements for exited deals, recomputed as net-to-LP.
- [ ] **Lender reference.** Confirm the loan terms and the sponsor's standing with the lender.
- [ ] **Affiliate disclosure.** Identify which property manager and construction manager are used and how each relates to the GP.

---

## 10. Verdict

**Pursue with conditions.**

Screening output only, not investment advice.

**Reasoning.** The headline (16% IRR, 2.0x over 5 years, 8% pref with a 20% promote) sits inside the `01` value-add target range. The fees are in market range but at its top. On paper the deal clears VNQ plus the 5-year illiquidity hurdle with room to spare. That room exists only if the deal's two most fragile assumptions hold:

1. **The exit cap compresses from 5.5% to 5.0%** (`EQUITY-06`).
2. **Floating-rate bridge debt survives a 5-year hold** (`EQUITY-07`, with `GEN-10` and `GEN-09` probes).

With about 75% of profit inferred to come from the sale (`GEN-08`) and about 11 points of return above the unlevered NPI baseline (`GEN-07`), this is a **financing story, not an asset story**. The track record behind the sponsor is unverified (`GEN-05`, `GEN-14`). Enough is disclosed to see how the deal makes its return, so this is a merits verdict, not "insufficient disclosure." The gaps in §6 become conditions.

**Biggest swing factor:** the exit cap combined with the bridge-debt path. At a flat 5.5% exit, exit value is about 9.1% lower, and equity takes a multiple of that cut. If the rate cap or the loan's maturity falls inside the hold, the LP's downside moves from a lower return to a capital call or loss of principal.

**Conditions. Each one is a pass trigger if not met:**

1. The GP provides an IRR at a **flat (5.5%) or higher exit cap**, and it still clears the 8% pref and about 8.2–9.2% net (VNQ plus the 5-yr premium, and the Treasury floor). (`Q-EXIT-01`, `Q-DS-01`)
2. **The rate cap covers the loan through maturity**, or its extension cost is budgeted, **and maturity plus extension options cover the 5-year hold** without needing a refinance at lower rates. (`Q-RISK-02`, `Q-RISK-01`, `Q-EXIT-02`)
3. The **16% is confirmed as net-to-LP**, or a net figure is supplied, and the full fee stack, fee bases, catch-up, cumulative pref, and clawback terms are produced. (`Q-FEE-01`, `Q-FEE-03`, `Q-FEE-04`)
4. The **"30% IRR" is restated as net-to-LP on realized multifamily exits.** (`Q-GP-02`)
5. **Cash GP co-invest on pari-passu terms**, plus a clean regulatory and litigation history. (`Q-GP-01`, `Q-GP-03`)
6. The **rent roll and T-12** support in-place NOI at the 5.5% going-in cap, and submarket supply data supports the rent-growth assumption. (`Q-RISK-03`, `Q-MKT-01`)

**Who it suits:** an LP with a 5–7-year horizon who doesn't need liquidity, who can absorb a capital call or partial principal loss, who knowingly wants a levered bet on the cap-rate and rate path in a Sun Belt multifamily market, and who keeps the position small relative to their real-estate allocation.

**What would have to be true:** the asset earns its return through renovation premiums and NOI growth rather than cap compression; the debt can't be forced into a refinance or sale at a bad moment; and the sponsor's record holds up once restated as realized and net-to-LP.
