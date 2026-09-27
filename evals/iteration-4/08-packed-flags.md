# Eval fixture 08 — Multifamily syndication, flag cluster
*Iteration-4 run, 2026-09-27, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 1c7faff.*

**Verdict: PASS.** This is a merits verdict, not a disclosure one. Even with most numbers missing, the terms that *were* disclosed carry six independent RED flags. The sponsor has no capital at risk (`GEN-01`) and a principal named in an SEC action (`GEN-02`). The waterfall is American, pays a 50% promote and has no clawback (`EQUITY-01` + `EQUITY-02`). The rate cap expires before the 2028 maturity (`GEN-10`), and the track record is unrealized only (`GEN-14`). The pieces reinforce each other: the GP keeps half the profit with nothing at risk, and the only evidence that it can protect LP capital through a refinance is marks it set itself. The biggest swing factor is the 2027–28 refinance. The cap runs out in about 12 months, the loan comes due in 2028, and the projections include no case in which either goes badly.

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Multifamily. Value-add vs core is **not stated** 🟡 (floating-rate debt and a 50% promote point to value-add/bridge, so I use the `01` value-add baseline: 5–7 yr hold, 12–18% target / 12–15% realized net IRR) |
| Deal type | Equity syndication, single asset 🟢 |
| Sponsor | Not stated. One principal named in a prior SEC action 🟢 (nature, date and outcome not stated) |
| Geography / submarket | Not stated |
| Minimum investment | Not stated |
| Hold period | Not stated (loan maturity 2028 is the only time marker) |
| Raise / equity size | Not stated |
| Claimed return | Not stated as a number. "Upside case only" 🟢 |
| Pref / catch-up | Not stated |
| Promote | 50%, American (deal-by-deal) waterfall, no clawback 🟢 |
| GP co-invest | $0. "Our expertise is our investment" 🟢 |
| Debt | Floating rate. Rate cap expires in ~12 months (~Q3–Q4 2027). Loan matures 2028 (month not stated). Rate, spread, LTV, cap strike and extension options not stated |
| Track record | All current, unrealized marks. No realized exits cited 🟢 |

## 2. Return Stress-Test

**No net-to-LP return is disclosed, and the only projection is an upside case (`GEN-13`).** So the stress test has to be built from structure, not from the sponsor's pro forma. Every figure below comes from illustrative inputs I chose (tagged 🔴 ASSUMED); none of them are the deal's numbers.

**Promote-only view** (50% promote, all other fees set to 0 because they are undisclosed, 5-yr hold ASSUMED, 8% pref + 100% catch-up ASSUMED):

| Scenario | Gross deal IRR (ASSUMED) | Net LP IRR | Promote drag | vs VNQ 4.92% (10yr) | 5-yr illiquidity hurdle ~300–400bps |
|---|---|---|---|---|---|
| "Upside case" (the only case shown) | 15% | **8.53%** | 647 bps/yr | +361 bps | **Clears (thin)**, lower half of band |
| Upside + a typical `02` fee load (2% acq, 1.5% AM, 1% disp, 0.3% admin, ASSUMED) | 15% | **6.13%** | 887 bps/yr total | +121 bps | **Fails** |
| Moderate miss | 10% | 6.96% | 304 bps/yr | +204 bps | Fails |
| Bear: cap expires → rates stay high → refi fails at 2028 maturity | — | **Capital impairment / capital call / forced sale** | — | — | Not modeled by the sponsor 🔴 |

- **The key number** 🟢 (script output): at a 15% gross IRR with a 50% promote and a full catch-up, **the GP takes 50% of total profit**. The pref only affects when cash is paid, not how the profit is finally split. The sponsor keeps half the upside with $0 of capital at risk.
- **The Treasury floor is tighter than the comparator** 🟢 (`05`): the 10yr Treasury is ≈5.18% and the 2yr ≈4.87%. At the full-stack figure (6.13% net), the LP gets roughly 95bps over a risk-free 10yr bond for a single-asset, illiquid, floating-rate position. That is almost no pay for the risk.
- **Concentration amplifier** (`05`): a single-asset syndication carries idiosyncratic risk that VNQ's basket diversifies away. The hurdle should sit at the upper end of the band, not the lower end.
- **Swing assumptions:** (1) the **refinance at 2028 maturity** (whether it is available, its rate and its proceeds); (2) **debt cost after the cap expires** (unhedged floating exposure from about Q4 2027 to maturity); (3) **exit cap** (not disclosed, so compression cannot be ruled out).

## 3. Where LP Returns Come From

**Can't tell from this, and that is the finding.** No split of cash flow vs exit was disclosed, no going-in or exit cap, and no unlevered return. What the structure does show:

- **Leverage-dependent** 🟡: floating-rate debt with a short-dated cap is a structure where debt cost, not operations, sets the LP's distributions once the cap is gone. The `05` unlevered overlay puts institutional private RE at ~5.0% (almost all income; residential 5.3% in 2025). Any projected multifamily return well above that is mostly leverage and assumed appreciation, which is the `GEN-07` question.
- **Probably exit- or refi-dependent** 🟡: if the hold is the typical 5–7 years, a 2028 maturity forces a refinance or sale partway through (`GEN-09`, `EQUITY-07`). An upside-only projection hides whether more than 60% of the IRR is terminal value (`GEN-08`) or depends on exit-cap compression (`EQUITY-06`).
- The financing-story cluster (`GEN-07` + `GEN-08` + `EQUITY-06`) **can't be confirmed or ruled out**. It is a must-ask (Q-DS-01, Q-DS-02), not a fired flag.

## 4. Fee Stack Summary

| Fee | Disclosed | `02` norm | Read |
|---|---|---|---|
| Promote | **50%** | 15–30%; aggressive >30% | **Well past the aggressive threshold** 🟢 |
| Preferred return | Not stated | 6–10% | Absent pref = `EQUITY-04` until answered |
| Catch-up | Not stated | Often 50–100% | `EQUITY-03` probe |
| Clawback | **None** | Rare in deal-by-deal, and its absence is a major flag | `EQUITY-02` 🟢 |
| Acquisition fee | Not stated | 1–2% of equity | Not disclosed |
| Asset management | Not stated | 1–2%/yr | Not disclosed |
| Disposition | Not stated | 0.5–1% of sale | Not disclosed |
| Loan placement / **refinance** | Not stated | 0.5–1.5% / 0.5–1% per event | Relevant here because a 2028 refinance looks likely |
| Admin / IR | Not stated | 0.1–0.5% or $1–3k/LP | Not disclosed |
| Affiliate fees (PM, CM, placement) | Not stated | — | `GEN-06` probe |

**Gross-to-net drag: not computable from disclosure, and that is the finding (`GEN-16`).** The disclosed promote alone costs **~647 bps/yr at a 15% gross IRR** (script, with 8% pref and 100% catch-up ASSUMED). A market-typical fee load on top brings the total to **~887 bps/yr**, i.e. **15% gross → ~6.1% net** (the fee inputs are 🔴 ASSUMED and listed in §6). Assuming zero GP capital, that is roughly the take a sponsor needs to make fees and promote its whole economic return.

## 5. Red Flags

**RED**
- **`GEN-01` Zero GP co-investment**: "our expertise is our investment." The GP earns fees and a 50% promote whatever happens to the LP, so alignment is claimed, not built into the structure. The pitch *is* the bad-answer signal for Q-GP-01, word for word. 🟢
- **`GEN-02` Prior regulatory action**: a principal was named in an SEC action. The mechanism is a pattern of investor harm or compliance failure. Until the nature and outcome are known, treat it as disqualifying. 🟢
- **`EQUITY-01` American waterfall with high promote**: 50% is far past the `02` aggressive threshold (>30%). On a single asset, the practical exposure is that the GP takes promote on **interim distributions or refinance proceeds**, and the asset later loses value at the refinance or sale. 🟢 / 🟡 (single-asset mechanism inferred)
- **`EQUITY-02` No clawback**: the promote already paid to the GP cannot be recovered if the final outcome falls short. Together with `EQUITY-01` this is the combination `03` calls RED. 🟢
- **`GEN-10` Rate cap expiry risk**: the cap expires in ~12 months but the loan runs to 2028. This matches the 2022–24 failure sequence exactly: cap expires → rates stay high → debt service jumps and wipes out distributions → refinance frozen at maturity → capital call or forced sale. 🟢
- **`GEN-14` Unrealized-only track record**: current marks only, no realized exits. The GP has not shown it can exit and return capital. (**`GEN-05`** also applies: whether the marks are project-level, GP-level or net-to-LP is not stated. If they are project-level, `03` treats the pair as a **RED cluster**: no validated LP-outcome data at all.) 🟢 / 🟡
- **`EQUITY-04` Pref not stated** (YELLOW–RED, treated as RED until answered). With no stated pref, the LP carries equity risk with no priority cushion before a 50% promote. (**`EQUITY-05`**, whether the pref is cumulative or compounding, is also unknown.) 🔴
- **`GEN-16` No fee disclosure** (YELLOW–RED, treated as RED). Gross-to-net cannot be calculated. 🟢
- **`GEN-15` Missing financials** (YELLOW–RED): no rent roll, T-12 or full debt terms. (**`GEN-12`** T-3/T-6-only risk can't be ruled out.) 🟢

**YELLOW (inferred or probe)**
- **`GEN-09` Debt maturity inside the business plan** 🟡: hold unstated, but a 2028 maturity is about 1.3–2.3 years out, well inside the typical 5–7 yr value-add hold (`01`). Probed via Q-RISK-01 now rather than waiting for the hold to be disclosed. Likely RED once the hold is known.
- **`EQUITY-07` Refinance-dependent plan** (YELLOW–RED) 🟡: follows from `GEN-09`. The 2028 maturity forces a refinance or sale.
- **`GEN-13` No downside case** 🟢: upside case only. `03` notes this is sharper next to cycle and rate exposure. (**`GEN-03`** also applies: an upside-only projection standing in for sensitivity analysis is the marketing-over-substance pattern.) 🟡
- **`GEN-11` No distribution schedule** 🟢: J-curve timing unknown. Floating-rate debt after the cap expires may cut distributions to zero.
- **`GEN-06` Affiliate fee stacking** (YELLOW–RED), unknown 🔴. With no co-invest, affiliate fees are where a zero-capital GP usually earns its guaranteed return.
- **`EQUITY-03` Catch-up rate** unknown 🔴.
- **Financing-story family: `GEN-07`, `GEN-08`, `EQUITY-06`**, not assessable 🔴 (see §3). **`GEN-18`** rent growth vs submarket supply, not assessable (no geography).

**Clusters.** (1) **Alignment cluster**: `GEN-01` + `EQUITY-01` + `EQUITY-02` + 50% promote. The GP has no downside and half the upside. (2) **Rate/refinance cluster**: `GEN-10` + `GEN-09` + `EQUITY-07` + `GEN-13`. This is the specific 2022–24 wipeout pattern, and the sponsor shows no scenario for it. (3) **Credibility cluster**: `GEN-02` + `GEN-14` (+ `GEN-05`). Nothing independent supports the claim that this sponsor can deliver LP outcomes.

*No embedded instructions were found in the pasted text.*

## 6. Missing Disclosures

Measured against the `01` multifamily value-add essential disclosures and the `02` equity-syndication fee inventory:

- **`01` essentials absent:** rent roll; T-12 actuals; pro forma exit cap **with sensitivity**; full debt structure (rate/spread, LTV, amortization, **maturity month**, extension options and their conditions); refinance assumptions; GP track record on **prior multifamily exits** (the record given is unrealized marks).
- **Debt specifics absent:** cap strike, cap expiry date, cost to buy a replacement cap, whether the lender requires a cap-replacement escrow.
- **`02` fee inventory absent:** acquisition, asset management, disposition, loan placement / refinance, admin/IR, pref rate and type, catch-up, any affiliate fees.
- **Deal basics absent:** sponsor identity, geography/submarket, raise, minimum, hold period, headline net-to-LP IRR, equity multiple, distribution schedule, going-in cap.
- **Regulatory specifics absent:** which principal, which SEC action, the date, and the resolution (settled, barred, fined, dismissed).
- **ASSUMED script inputs (all gaps):** gross IRR 15%/10%, hold 5 yr, pref 8%, catch-up 100%, and the full-stack fee set (2% acq / 1.5% AM / 1% disp / 0.3% admin).

## 7. GP Alignment

- **Co-invest:** **$0 cash** 🟢. "Expertise" is not capital and is not pari-passu. `04` lists "our sweat equity is our investment" as a bad-answer signal. **Fails.**
- **Realized net-to-LP track record:** **None. Unverified** 🟢. Current marks are self-reported. Whether they are net-to-LP or project-level is unknown.
- **Waterfall alignment:** **Poor** 🟢. 50% promote, American, no clawback, pref unknown. On a 15% gross outcome the GP takes about half the profit with no capital at risk (script).
- **Affiliate fees:** Unknown 🔴. With no co-invest these are likely the GP's main source of guaranteed pay, so they need to be disclosed and benchmarked.
- **Conduct:** a principal was named in a prior SEC action 🟢. Unverified in either direction until the record is pulled.

**Net read:** the GP's interests line up with raising capital and getting a promote on the upside, not with protecting LP capital.

## 8. Questions for the GP

**Must-ask**

| ID | Question | Bad-answer signal (the specific dodge) | Flag |
|---|---|---|---|
| Q-GP-03 | "Have you or your principals faced any regulatory action, enforcement, or investor litigation?" | "Nothing material"; blames the regulator; a search turns up something they didn't disclose, **or they describe the SEC action only after being asked** | GEN-02 |
| Q-GP-01 | "How much of your own capital is in this deal, on the same terms as LPs?" | **Already given:** "our expertise is our investment." Also: a fee waiver presented as co-invest | GEN-01 |
| Q-GP-02 | "Can you restate your track record as net-to-LP IRR on fully-realized, exited deals only?" | Only project- or GP-level IRR; "most deals are still performing"; can't separate realized from marked | GEN-05, GEN-14 |
| Q-FEE-03 | "Is the waterfall deal-by-deal or whole-of-fund, and is there a clawback?" | Deal-by-deal with a high promote and no clawback (**the stated terms**); can't explain the catch-up; "you get paid when we get paid" | EQUITY-01, EQUITY-02, EQUITY-03 |
| Q-FEE-04 | "What preferred return do LPs receive before the GP earns promote, and is it cumulative and compounding?" | Pref below 6% or none; non-cumulative | EQUITY-04, EQUITY-05 |
| Q-FEE-01 | "Can you provide the complete fee schedule and the full distribution waterfall?" | "Standard market fees"; "the PPM has it" without producing it | GEN-16 |
| Q-FEE-02 | "Which service providers are GP-affiliated, what do they charge, and are those rates third-party-benchmarked?" | "All arm's-length" without naming providers; no benchmark | GEN-06 |
| Q-RISK-02 | "When does the rate cap expire relative to debt maturity, and what's the cost to extend it at current pricing?" | Cap expires before maturity (**already true**); extension cost not modeled; "rates should be lower by then" | GEN-10 |
| Q-RISK-01 | "When does the debt mature relative to the projected hold, and what's the refinance or extension plan?" | Maturity falls inside the hold; "we'll refinance" with no terms; no plan if the refinance market shuts | GEN-09 |
| Q-EXIT-02 | "Does the business plan depend on a refinance, and what happens to distributions if the refi isn't available on the assumed terms?" | Capital return requires a refinance at lower rates; "the refi market will reopen" | EQUITY-07 |
| Q-DS-03 | "What is the return under a bear case — flat rents, higher exit cap, no refinance?" | Single-point pro forma; "we underwrite conservatively" with nothing to show; the bear case is still a gain | GEN-13, GEN-03 |
| Q-DS-01 | "What share of projected LP IRR comes from in-place cash flow versus the exit, and what's the IRR at a flat exit cap?" | Can't break the IRR down; "real estate always appreciates"; IRR falls below the pref at a flat exit cap | GEN-08, EQUITY-06 |
| Q-DS-02 | "Strip out leverage and cap-rate compression — what is the unlevered, in-place return?" | Treats the levered IRR as the only relevant figure; "leverage is just how the deal works" | GEN-07 |
| Q-RISK-03 | "Can you provide trailing-twelve-month actuals, the rent roll, and complete debt terms?" | T-3/T-6 only; "the financials are confidential until you commit" | GEN-12, GEN-15 |
| Q-DIST-01 | "What is the projected distribution schedule, and at what milestones does LP capital start returning?" | "We'll distribute when the deal supports it"; IRR with no timing | GEN-11 |
| Q-MKT-01 | "What submarket supply pipeline and absorption data support the rent-growth assumption?" | Metro-level optimism; "rents always go up here" | GEN-18 |
| Q-LIQ-01 | "What are my options if I need to exit before the hold period ends?" | "A secondary market may develop"; "we'll try to accommodate" | — |

**Nice-to-ask**

| ID | Question | Bad-answer signal | Flag |
|---|---|---|---|
| Q-DIST-02 | "When are capital calls expected, and what's the consequence of a missed or late call?" | "Calls as needed"; punitive dilution buried in the docs. **Consider treating it as must-ask here**: a capital call is the usual way `GEN-10` plays out | — |
| Q-GP-04 | "How have your headcount and deal-monitoring capacity grown alongside AUM?" | AUM multiplied while the team stayed flat | GEN-04 |
| Q-LIQ-02 | "When will K-1s be delivered each year?" | "As soon as we can"; a history of extensions | — |

## 9. Diligence Checklist (third-party verification)

- **Regulatory/background:** SEC enforcement actions and litigation releases, FINRA BrokerCheck, the state securities regulator, and court dockets for the named principal and all other principals. Confirm the action's nature, date, sanctions and any bars.
- **PPM + operating agreement:** the actual waterfall (pref, catch-up, tiers), clawback language (confirm there is none), GP removal rights, capital-call and dilution terms, all fees, affiliate relationships.
- **Loan documents + rate cap agreement:** cap strike, expiry, counterparty, lender-required replacement cap or escrow, extension conditions (DSCR/debt-yield tests), maturity date, recourse or carve-outs.
- **Lender reference:** the sponsor's history with this lender. Have any prior loans needed modifications or extensions?
- **Track-record verification:** LP references and K-1s from *exited* deals. Match the current marks against independent valuations.
- **Property:** T-12 and rent roll against bank deposits; third-party appraisal; rent and sales comps for the exit and refinance valuation.

## 10. Verdict

**PASS.**

- **Reasoning:** the disclosed terms alone contain multiple structural REDs, so this is not a "we need more information" deal. Better disclosure cannot fix the lack of co-investment, the missing clawback, the 50% promote or the SEC history. Only a restructured deal could. The rate-cap gap (`GEN-10`) followed by a 2028 maturity (`GEN-09`, `EQUITY-07`) is the exact pattern behind the 2022–24 multifamily capital calls and wipeouts, and the sponsor shows only an upside case (`GEN-13`). On illustrative inputs, even the upside case nets the LP roughly 6–8.5%. That is thin or failing against VNQ plus a 5-year illiquidity hurdle, and only about 100–340bps over a risk-free 10yr Treasury, for single-asset, floating-rate, illiquid risk.
- **Biggest swing factor:** the **refinance at 2028 maturity after a cap that expires about Q4 2027.** This is where LP capital is lost, and the sponsor's materials don't model it.
- **Who it suits:** no passive LP on these terms.
- **What would have to be true to re-screen** (all of these, not any one): (1) the SEC action is minor, fully resolved, disclosed unprompted and independently verified; (2) meaningful GP cash co-invest, pari-passu; (3) promote cut to within the `02` range (≤30%) over a cumulative pref of at least 6–8%, with a secured clawback or promote held back until final sale; (4) a funded rate-cap extension or fixed-rate refinance path through the full hold; (5) a realized, net-to-LP track record on exited multifamily deals; (6) a full fee schedule, T-12, rent roll, and a bear case in which LP capital survives.
