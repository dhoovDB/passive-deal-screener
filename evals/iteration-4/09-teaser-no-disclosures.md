# Eval fixture 09 — Multifamily fund teaser ("15%+ returns")
*Iteration-4 run, 2026-09-27, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 1c7faff.*

**Verdict: Pass as presented — insufficient disclosure.** This is a teaser, not a deal. The only numbers are a return target and a minimum. It has no fee stack, no waterfall, no hold, no sponsor, no strategy, no assets, and no track record, so there is nothing to underwrite. The biggest swing factor is whether "15%+" is **net-to-LP IRR** or a gross/project figure. Under a market-standard fee stack that difference moves the LP outcome from about 15% to about 10.6%, which is the gap between clearing the illiquidity hurdle comfortably and clearing it thinly. Re-screen once the GP sends the items in §6.

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Multifamily. Strategy (value-add vs core/core-plus) **not stated** 🔴 |
| Deal type | Equity fund (blind pool assumed from "fund"; underlying assets **not stated**) 🟡 |
| Sponsor | **Not stated** |
| Geography | **Not stated** |
| Minimum | $100k, accredited only 🟢 |
| Hold / fund term | **Not stated** |
| Raise / fund size | **Not stated** |
| Claimed return | "15%+ returns". The metric is **not stated**: IRR, cash-on-cash, or total return, and gross or net 🔴 |

The "15%+" figure sits inside the multifamily value-add *target* band (14–18% net). `01` notes that realized results across vintages cluster at **12–15% net blended**. A core/core-plus fund (8–12% net) claiming 15%+ would sit outside its category norm. The claim cannot be placed until the strategy is disclosed. 🟢 (`01`)

## 2. Return Stress-Test

No pro forma, exit cap, rent growth, or debt terms were given, so the deal cannot support a base/bull/bear case of its own. The scenarios below bracket what "15%+" could mean. **Every fee input is ASSUMED** (the `02` market-standard stack: 2% acquisition, 1.5% annual asset management, 1% disposition, 0.3% admin, 20% promote over an 8% pref with 100% catch-up) over an ASSUMED 7-year hold. Comparator: VNQ, 4.92% 10yr trailing. Illiquidity hurdle for a 7-year lock-up is about 400–600bps.

| Scenario | Reading of "15%+" | Net-to-LP | Premium over VNQ | Read |
|---|---|---|---|---|
| Bull | 15% is already **net-to-LP IRR** | 15.0% | ≈1008bps | Clears comfortably |
| Base | 15% is **gross**, with a market fee stack | ≈10.6% | ≈568bps | Clears **thin**, in the lower half of the hurdle band |
| Bear | Gross lands at 12% (the low end of the realized band, `01`) with the same stack | ≈7.9% | ≈301bps | **Fails** the ~400–600bps hurdle |

- **Swing assumptions (can't be tested, none disclosed):** (1) gross vs net, (2) exit cap, the single biggest swing in multifamily pro formas per `01`, and (3) refi and debt terms.
- **Treasury floor:** 10yr ≈ 5.18%, which currently out-yields VNQ's trailing 10yr return. Even the bear case clears the risk-free rate by only about 270bps for a multi-year lock-up. 🟢 (`05`)
- **Dispersion:** clearing the spread is necessary, not sufficient. The *median* private RE fund earns well below the marketed figure (`05`, Preqin note), and "15%**+**" is marketing phrasing aimed at the top of the range.

## 3. Where LP Returns Come From

**Can't tell from this.** 🔴 The teaser does not split the return between cash flow, exit, and leverage. As context from the `05` unlevered overlay: NCREIF NPI returned about **5.0%** unlevered over the trailing four quarters, almost entirely income. A 15% levered multifamily return therefore implies roughly **10 points from leverage and assumed appreciation**, not operations. That is a financing bet (rate path, refi availability, exit cap), not an asset bet. It is not yet a fired `GEN-07`/`GEN-08`, because nothing is disclosed to test. It is the first thing to probe (Q-DS-01, Q-DS-02). 🟡

## 4. Fee Stack Summary

**Gross-to-net drag: not computable from disclosure. That is the finding.** 🔴 No fees of any kind are disclosed.

- With every fee entered as undisclosed (0), the calculator returns 0bps of drag and a net equal to the gross. That output only reflects that nothing was disclosed; the real fees are not zero.
- Under the `02` market-standard stack (ASSUMED, not disclosed), drag is about **440bps/yr**: 180 recurring, 43 one-time, and 217 promote. That turns 15% gross into about 10.6% net.
- **Fund-specific layers to surface.** A fund structure can add a fund-level management fee on committed capital on top of asset-level fees. If this is a feeder or fund-of-funds vehicle, `02` estimates an additional **50–150bps/yr** of wrapper drag that is rarely disclosed next to the underlying fees. Also ask about affiliate property-management and construction-management fees (`GEN-06`, probe).

## 5. Red Flags

No RED fires on stated terms, because no terms are stated. The flags below all fire on **absence**. Taken together they form a cluster, and `03` treats a cluster of YELLOWs as a RED.

**YELLOW–RED (treat as RED until answered)**
- **GEN-16: No fee or waterfall disclosure.** Undisclosed fees are still paid. Without them, the LP cannot tell whether 15% becomes 15%, 10.6%, or less. → Q-FEE-01
- **GEN-15: Missing financials.** No rent roll, T-12, or debt terms for any underlying asset. In a blind-pool fund the LP may not even know what the assets are. → Q-RISK-03

**YELLOW**
- **GEN-03: Marketing-heavy, substance-light.** The only content is a headline return with a "+", an access gate, and "contact us." The headline projection is standing in for underwriting. → Q-DS-03 (full model and actuals)
- **GEN-17: Essential category disclosures absent.** Every multifamily essential in `01` is missing (see §6). → Q-RISK-03
- **GEN-11: Return quoted with no distribution schedule.** The J-curve is hidden. The LP can't tell whether capital comes back through cash flow or only at exit. → Q-DIST-01
- **GEN-13: No sensitivity or downside case.** A single "15%+" point with no bear case. → Q-DS-03

**Probe (not fired; nothing disclosed to test)**
- **GEN-05 / GEN-14 (track record):** no track record is cited at all. Treat it as unverified until realized net-to-LP figures are produced. → Q-GP-02
- **GEN-01 (co-invest):** GP capital at risk is not stated. → Q-GP-01
- **EQUITY-01 / EQUITY-02 (waterfall):** a multi-asset fund on a deal-by-deal waterfall with no clawback is the specific LP exposure to rule out. → Q-FEE-03
- **EQUITY-04 / EQUITY-05 (pref):** pref rate and cumulative status are not stated. → Q-FEE-04
- **GEN-07 / GEN-08 (financing story):** see §3. → Q-DS-01, Q-DS-02
- **GEN-09 / GEN-10 / EQUITY-07 (debt):** multifamily is the category behind the 2022–24 rate-cap-expiry failures, and no debt terms are given. → Q-RISK-01, Q-RISK-02, Q-EXIT-02
- **GEN-06 (affiliate fees):** → Q-FEE-02
- **GEN-02 (regulatory):** sponsor unnamed, so no background search is possible yet. → Q-GP-03

## 6. Missing Disclosures

Against the `01` multifamily baseline and the `02` equity/fund fee inventory:

- **Sponsor identity** (blocks all background diligence)
- **Strategy:** value-add vs core/core-plus, which sets the return baseline
- **Return definition:** IRR vs cash-on-cash vs total return; gross vs net-to-LP
- **Hold period / fund term** and the distribution schedule
- **Fee schedule:** acquisition, asset management, fund management fee (committed vs invested capital), disposition, loan placement/refi, admin/IR, and any feeder-level fee
- **Waterfall:** pref rate, cumulative/compounding, catch-up, split tiers, deal-by-deal vs whole-of-fund, clawback
- **Assets:** identified vs blind pool, geographies, and for each asset the **rent roll and T-12 actuals** (not T-3/T-6)
- **Debt:** fixed/floating, maturity, rate-cap expiry, refi assumptions
- **Exit cap assumption with sensitivity**
- **GP track record on prior multifamily *exits*:** realized, net-to-LP
- **GP co-investment**
- **Fund size / raise, and capital-call mechanics**
- **LP liquidity terms** (redemption or secondary options, if any)

## 7. GP Alignment

**Entirely unverified.** 🔴
- **Co-invest:** not stated (cash vs fee waiver, and pari-passu status, both unknown).
- **Track record:** none cited. Unverified is the same as no track record until realized net-to-LP figures on exited multifamily deals are produced.
- **Waterfall alignment:** unknown. For a fund, whole-of-fund with a pref ahead of promote is the aligned structure. Deal-by-deal without a clawback is the misaligned one.
- **Affiliate fees:** unknown.

## 8. Questions for the GP

**Must-ask**

| ID | Question | Bad-answer signal |
|---|---|---|
| Q-FEE-01 | "Can you provide the complete fee schedule and the full distribution waterfall?" | "Standard market fees"; partial list; "the PPM has it" without producing it; fees surface only after commitment. |
| Q-GP-02 | "Can you restate your track record as net-to-LP IRR on fully-realized, exited deals only?" | Only project- or GP-level IRR; "most deals are still performing"; can't separate realized from unrealized. |
| Q-DS-01 | "What share of projected LP IRR comes from in-place cash flow versus the exit, and what's the IRR at a flat exit cap?" | Can't or won't decompose the IRR; "real estate always appreciates"; IRR falls below the pref at a flat exit cap. |
| Q-DS-02 | "Strip out leverage and cap-rate compression — what is the unlevered, in-place return?" | Levered IRR is treated as the only relevant figure; "leverage is just how the deal works." |
| Q-DS-03 | "What is the return under a bear case — flat rents, higher exit cap, no refinance?" | "We underwrite conservatively" with nothing to show; no downside case; the bear case is still a gain. |
| Q-FEE-03 | "Is the waterfall deal-by-deal or whole-of-fund, and is there a clawback?" | Deal-by-deal with high promote and no clawback; can't explain the catch-up; "you get paid when we get paid." |
| Q-FEE-04 | "What preferred return do LPs receive before the GP earns promote, and is it cumulative and compounding?" | Pref below 6% or absent; non-cumulative. |
| Q-GP-01 | "How much of your own capital is in this fund, on the same terms as LPs?" | "Our sweat equity is our investment"; co-invest is a fee waiver, not cash; token amount on better terms. |
| Q-GP-03 | "Have you or your principals faced any regulatory action, enforcement, or investor litigation?" | "Nothing material"; blames the LP or regulator; a search surfaces something undisclosed. |
| Q-RISK-03 | "Can you provide trailing-twelve-month actuals, the rent roll, and complete debt terms for each asset?" | T-3/T-6 only; rent roll withheld; "the financials are confidential until you commit." |
| Q-DIST-01 | "What is the projected distribution schedule, and at what milestones does LP capital start returning?" | "We'll distribute when the deal supports it"; no milestones. |
| Q-RISK-01 | "When does the debt mature relative to the projected hold, and what's the refinance or extension plan?" | Maturity falls inside the hold; "we'll refinance" with no terms. |
| Q-RISK-02 | "If any debt is floating, when does the rate cap expire relative to maturity, and what's the cost to extend?" | Cap expires before maturity; extension cost not modeled; "rates should be lower by then." |
| Q-LIQ-01 | "What are my options if I need to exit before the fund term ends?" | "A secondary market may develop"; "we'll try to accommodate." (An honest "none" is a *good* answer.) |

**Nice-to-ask**

| ID | Question | Bad-answer signal |
|---|---|---|
| Q-FEE-02 | "Which service providers are GP-affiliated, what do they charge, and are rates benchmarked?" | "All arm's-length" without naming providers. |
| Q-EXIT-01 | "What exit cap is assumed vs going-in, and what's the IRR at an exit cap at or above going-in?" | Exit cap below going-in with "cap rates will compress." |
| Q-EXIT-02 | "Does the plan depend on a refinance, and what happens to distributions if it isn't available?" | Distributions depend on a refi at lower rates; "the refi market will reopen." |
| Q-MKT-01 | "What submarket supply and absorption data support the rent-growth assumption?" | Metro-level optimism; no supply pipeline acknowledged. |
| Q-DIST-02 | "When are capital calls expected, and what's the consequence of a missed call?" | "Calls as needed"; punitive dilution buried in the docs. |
| Q-LIQ-02 | "When are K-1s delivered, and have you historically met the filing deadline?" | "As soon as we can"; a history of extensions. |

Escalate the exit, refi, and debt questions to must-ask as soon as the GP confirms leveraged, value-add assets.

## 9. Diligence Checklist

- [ ] Obtain the **PPM, LPA, and subscription docs**. Confirm fees and waterfall in the legal text, not the deck.
- [ ] **Sponsor background:** SEC IAPD / Form ADV (if RIA-registered), FINRA BrokerCheck, state securities regulators, litigation search on principals.
- [ ] Check for a **Form D** filing on the offering (confirms the exemption relied on, the raise size, and related persons).
- [ ] **Realized-deal verification:** request LP references from exited deals and match distributions to K-1s or statements.
- [ ] Per asset: **rent comps, third-party appraisal, lender term sheet / loan docs**.
- [ ] Fund admin / auditor identity (third-party vs in-house).

## 10. Verdict

**Pass as presented — insufficient disclosure.** The essential disclosures for this deal type are substantially absent (`01`, `02`), and the core return story cannot be underwritten. The GP has not said what the return figure *is*, let alone what drives it. This verdict judges the materials, not the fund.

- **Biggest swing factor:** whether "15%+" is net-to-LP. If it is, the fund clears the 7-year illiquidity hurdle by a wide margin (≈1008bps over VNQ). If it is gross with a market fee stack, it clears thinly (≈568bps). At the realized-band low end it fails (≈301bps).
- **What would have to be true to move to "Pursue with conditions":** the 15% is a net-to-LP IRR; fees sit within `02` ranges; the waterfall is whole-of-fund (or deal-by-deal with a secured clawback) behind a cumulative pref of at least 6%; there is a realized, net-to-LP multifamily exit record; the GP has meaningful cash co-invest; and the debt has no maturity or rate-cap expiry inside the hold.
- **Who it could suit, once disclosed:** an accredited LP who can lock up $100k for an unstated (likely 5–10 year) term, holds diversified liquid equity and REIT exposure already, and accepts that about 10 points of any 15% levered multifamily return is a financing bet.
- **Re-screen list:** everything in §6. At minimum: sponsor name, the fee schedule and waterfall (Q-FEE-01), the return definition, hold, realized track record (Q-GP-02), and the asset list with debt terms.
