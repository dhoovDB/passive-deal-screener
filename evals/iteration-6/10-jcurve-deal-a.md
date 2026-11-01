# Eval fixture 10
*Iteration-6 run, 2026-11-01, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 436a76b.*

# Deal A screen (comparison pending Deal B)

**Verdict: Pass as presented — insufficient disclosure.** The distribution shape is attractive, but no sponsor, fees, debt, hold or net-vs-gross basis means the 14% can't be underwritten yet.

*Screening output only, not investment advice.*

**Comparison status:** Deal B hasn't arrived, so no contrast has been run and nothing below assumes anything about it. Deal A is screened on its own terms, and the side-by-side is set up at the end, ready for Deal B.

Tags: 🟢 stated or from a reference, 🟡 inferred, 🔴 assumed or unverifiable. Flags and the verdict rest on 🟢/🟡 only. Anything needing a 🔴 input is a must-ask.

---

## 1. Deal Snapshot

| Field | Deal A |
|---|---|
| Asset class | Multifamily 🟢. Sub-type (value-add vs core/core-plus) not stated |
| Deal type | Equity syndication 🟡, inferred from the IRR-plus-cash-on-cash framing. If this is actually preferred equity, the routing and comparator change (PFF, `PREF-` flags) |
| Sponsor | Not stated |
| Geography | Not stated |
| Minimum | Not stated |
| Hold | Not stated |
| Raise | Not stated |
| Claimed return | 14% projected IRR 🟢. Net or gross not stated |
| Distributions | 7% cash-on-cash, quarterly, from Year 1 🟢. Capital returned "progressively over the hold" 🟢, with no schedule or source |

**The two return numbers point to different sub-types** 🟡. The `01` norm for value-add is 5–8% cash-on-cash *after stabilization*, so 7% from Year 1 comes before value-add stabilization would normally occur. If the asset is already stabilized (core/core-plus), the 14% sits above that category's 8–12% net range. Either the Year 1 distribution has a source other than stabilized operations, or the IRR is rich for the risk. The GP needs to say which.

## 2. Return Stress-Test

The hold is unstated, so I ran the `01` value-add range of 5–7 years. Comparator: VNQ 4.92% (10yr trailing, net of expense). Hurdle: ~300–400 bps at 5 years, ~400–600 bps at 7 years (`05`).

| Case | What has to be true | Net to LP | Over VNQ | Illiquidity read |
|---|---|---|---|---|
| **Bull** 🔴 | 14% is already net; capital return is funded without a refi | 14.00% | +908 bps | Clears comfortably at 5 and 7 years |
| **Base** 🔴 | 14% is gross; an in-range `02` fee stack applies (§4) | 9.32% (5yr) / 9.71% (7yr) | +440 / +479 bps | Clears comfortably at 5yr; **clears thin** at 7yr |
| **Bear** 🔴 | 7% is paid in full throughout, capital comes back at par, no gain | ≈7.2% | +227 bps | **Thin / fails** at 5 and 7 years |

**Swing assumptions:**
1. **Refi, or whatever else funds the capital return.** This decides whether the "progressive" return exists on schedule.
2. **Exit cap.** The biggest swing in most value-add pro formas (`01`). It can't be sized here because no going-in cap, exit cap or leverage is given.
3. **Rent growth.** Not stated, and no submarket is named to test it against.

**Reads:**
- **The net/gross question is worth about 430–470 bps.** That's the difference between a comfortable clear and a thin one on a longer hold. I'm not comparing 14% to any benchmark as if it were net until the GP confirms it.
- **The bear case isn't the floor.** It still assumes distributions never stop. The realistic downside is distributions suspended and capital impaired, and the sizing for that needs the debt terms.
- **Early cash gives real protection if it's actually paid** 🔴. At a full 7% on original capital, the LP collects $35 per $100 over 5 years or $49 over 7. Nominal breakeven would then need only about 65% or 51% capital recovery.
- **Other floors** 🟢. 14% is ≈880 bps over the 10yr Treasury (5.18%), the tighter floor at this snapshot. The base case is ≈410–450 bps over it. 14% still trails SPY's 15.39% 10yr, so the deal owes a diversification or downside rationale rather than a "high return" pitch (`05`; SPY's decade is exceptional, not a forward promise).
- **Clearing is necessary, not sufficient.** This looks like a single deal against VNQ's diversified basket, and dispersion and concentration both raise the premium an LP should demand (`05`).

## 3. Where LP Returns Come From

**Can't be decomposed from this disclosure, and the missing piece is decisive.** What can be said:

- **Income covers about half the headline** 🟡. The 7% cash-on-cash is roughly half of the 14% IRR. The other ~7 points must come from gain on sale, refi proceeds or operating growth, and none of these is disclosed.
- **Unlevered overlay** 🟢. NCREIF NPI's trailing return is 5.00%, almost all income (`05`). So ~9 points of a 14% return would come from leverage and assumed appreciation rather than in-place operations. The 7% yield also sits about 220 bps above NPI's ~4.8% income return, which suggests leverage 🟡. Leverage itself is unstated, so `GEN-07` is open rather than fired.
- **The 60% exit test can't be run.** Illustration on $100 at a fixed 14% IRR, with quarterly payments 🔴 (not used for any flag):

| Capital shape | 5-yr: final payment / share of value / multiple | 7-yr: final payment / share of value / multiple |
|---|---|---|
| All capital at exit, 7% on original (ruled out by "progressively"; shown as the upper bound) | $144 / 75% / 1.79x | $171 / 68% / 2.20x |
| Straight-line capital, 7% on remaining balance | $25 / 13% / 1.44x | $42 / 17% / 1.68x |
| Straight-line capital, 7% on original | $5 / 3% / 1.40x | $10 / 4% / 1.59x |

**What this shows:**
- **The `GEN-08` answer depends entirely on the withheld schedule.** The terminal share runs from about 3% to 75%. "Progressively" could still be back-weighted enough to cross 60%.
- **The funding gap is the core finding** 🟡. Straight-line return of capital is $14–20 per $100 a year, two to three times the stated 7% yield. Operations paying 7% can't plausibly fund that as well. So either the schedule is much slower or back-weighted, or the money comes from a refi or asset sales. A refi moves the risk from exit-dependence to refi-dependence (`EQUITY-07`) and adds leverage (`GEN-07`) rather than removing it.
- **The same 14% can be a 1.4x or a 2.2x** 🔴. IRR rewards early cash, and returned capital has to be reinvested by the LP to earn anything further. An LP should get the projected equity multiple alongside the IRR.

## 4. Fee Stack Summary

**Gross-to-net drag: not computable from disclosure. That's the finding** (`GEN-16`). No fee, pref, promote or waterfall term is stated.

With undisclosed fees passed as 0, the calculator returns 0 bps. That means nothing was disclosed, not that nothing is charged.

**Illustrative only, ≈430–470 bps/yr** 🔴, using the script's `02` worked-example stack on 14% gross. All of these are assumed inputs and §6 gaps:

| Layer (assumed) | 5-yr hold | 7-yr hold |
|---|---|---|
| Recurring: 1.5% asset mgmt + 0.3% admin | 180 bps | 180 bps |
| One-time: 2% acquisition + 1% disposition | 60 bps | 43 bps |
| Promote: 20% over 8% pref, 100% catch-up | 228 bps | 206 bps |
| **Total drag** | **468 bps** | **429 bps** |
| **Net to LP** | **9.32%** | **9.71%** |

**Layers this estimate misses or can't capture:**
- **Refi fee.** 0.5–1% of the *new loan* per event, a larger base than equity. It applies directly if refis fund the capital return, and the same goes for loan placement fees. Neither is in the total above.
- **Fee base.** If the asset management fee is on equity raised rather than invested capital, it doesn't shrink as capital comes back, so the effective drag on remaining capital rises each year. Worth pinning down given this deal's structure.
- **Affiliate fees.** Property management and construction management could sit outside this stack (`GEN-06`).
- **Feeder or wrapper.** If accessed through one, add 50–150 bps/yr (`02`).
- **Model limit.** The promote calculation assumes a single bullet exit. With progressive distributions the timing differs, so treat the promote line as an order of magnitude.

## 5. Red Flags

**Fired, on what's in front of us**

| Flag | Severity | Mechanism and LP exposure |
|---|---|---|
| `GEN-16` No fee or waterfall disclosure | YELLOW–RED (treat as RED until answered) | Undisclosed fees are still paid. The LP can't tell whether 14% is 14% or about 9–10%. |
| `GEN-15` Missing financials | YELLOW–RED (treat as RED until answered) | No rent roll, T-12 or debt terms, so neither the 7% nor the IRR can be traced to actual income. |
| `GEN-17` Essential category disclosure absent | YELLOW | No exit cap sensitivity, refi assumptions or prior multifamily exits (`01`). |
| `GEN-13` No sensitivity or downside case | YELLOW | A single 14% hides how fragile the return is to exit cap, rents and refi. |

**Cluster:** a cluster of YELLOWs reads as a RED, and these four all share one cause: the deal can't be underwritten as presented.

**Partly answered, in the deal's favor**

- `GEN-11` J-curve (YELLOW). Income timing is specific and early, which is the good version of this disclosure. The residual is that "progressively" has no milestones, so capital timing is still open. Route to `Q-DIST-01`.

**Not fired, because the facts aren't stated. Each is a must-ask, not a finding**

| Family | IDs | What would fire it |
|---|---|---|
| Financing story | `GEN-07`, `GEN-08`, `EQUITY-06` | Return is mostly leverage and cap compression; >60% from terminal value; exit cap below going-in. Would be a RED cluster if they fire together |
| Refi and debt | `EQUITY-07`, `GEN-09`, `GEN-10` | Capital return requires a refi; debt matures inside the hold; rate cap expires early. `EQUITY-07` is the most likely to fire, given the §3 funding gap 🟡 |
| Waterfall | `EQUITY-01`–`EQUITY-05`, `GEN-06` | Promote, pref and affiliate terms. `EQUITY-01`/`02` matter if capital comes back through asset sales in a multi-asset deal, since promote could be paid per exit with no clawback |
| GP | `GEN-01`, `GEN-02`, `GEN-05`, `GEN-14` | Nothing is stated about the sponsor at all, so silence can't fire these; §7 treats the record as unverified |
| Market | `GEN-18` | Rent growth against an oversupplied submarket; no submarket named |

## 6. Missing Disclosures

Against the `01` multifamily baseline and the `02` equity inventory:

- **Return basis:** net vs gross IRR, equity multiple, hold period
- **Sub-type and asset:** value-add vs core, unit count, single asset vs portfolio, location, sponsor
- **Financials:** rent roll, T-12 actuals, occupancy history, source of Year 1 distributions
- **Exit:** going-in cap, exit cap, sensitivity
- **Debt:** amount and leverage, rate type, maturity, amortization, rate cap expiry, prepayment, refi assumptions
- **Distributions:** capital-return schedule and source; whether 7% is on original or remaining capital; whether it's income or return of capital; what suspends it
- **Fees:** acquisition, asset management and base, disposition, loan placement, refinance, construction management, admin/IR, affiliates
- **Waterfall:** pref rate, cumulative or not, simple or compounding, catch-up, promote tiers, deal-by-deal vs whole-of-fund, clawback, whether pref accrues on unreturned capital only
- **Track record:** realized multifamily exits, net to LP
- **LP terms:** minimum, raise size, capital calls, lock-up and transfer rights

## 7. GP Alignment

**Unverified on every axis** 🔴. No sponsor is named.

- **Co-invest:** not stated. Unknown whether cash, or pari passu.
- **Track record:** none cited, so there's no verified record. This isn't "unrealized only" (`GEN-14`) or project-level IRR (`GEN-05`) yet; it's nothing at all. Require realized, net-to-LP figures on prior multifamily exits.
- **Waterfall alignment:** not stated. Check how progressive capital return interacts with it: returning capital shrinks the pref base if pref accrues on unreturned capital, which can bring the GP's promote forward.
- **Affiliate fees:** not stated.

## 8. Questions for the GP

**Must-ask, in priority order for this deal**

| ID | Question | Bad-answer signal |
|---|---|---|
| `Q-DIST-01` | What is the projected distribution schedule, and at what milestones does LP capital start returning? Is 7% on original or remaining capital, and is it income or return of capital? | "We'll distribute when the deal supports it"; no milestones; IRR quoted with no timing |
| `Q-EXIT-02` | Does the plan depend on a refinance to fund the capital return, and what happens to distributions if the refi isn't available on the assumed terms? | Capital return requires a refi at lower rates; no fallback; "the refi market will reopen" |
| `Q-FEE-01` | Can you provide the complete fee schedule and full waterfall, and is 14% net to LP? | "Standard market fees"; partial list; "the PPM has it" without producing it |
| `Q-DS-01` | What share of projected LP IRR comes from in-place cash flow vs the exit, and what's the IRR at a flat exit cap? | Can't or won't decompose; "real estate always appreciates"; IRR falls below pref at a flat cap |
| `Q-DS-02` | Strip out leverage and cap-rate compression: what is the unlevered, in-place return? | Levered IRR is the only figure; "leverage is just how the deal works" |
| `Q-DS-03` | What's the return with flat rents, a higher exit cap and no refi? | Single-point pro forma; "we underwrite conservatively" with nothing to show; bear case is still a gain |
| `Q-RISK-03` | Can you provide T-12 actuals, the rent roll and complete debt terms? Does T-12 NOI after debt service cover 7% in Year 1? | T-3/T-6 only; rent roll withheld; "confidential until you commit" |
| `Q-RISK-01` | When does the debt mature relative to the hold, and what's the refi or extension plan? | Maturity inside the hold; "we'll refinance" with no terms |
| `Q-RISK-02` | If floating, when does the rate cap expire relative to maturity, and what does extending it cost at current pricing? | Cap expires before maturity; cost not modeled; "rates should be lower by then" |
| `Q-EXIT-01` | What are the going-in and exit caps? If exit is below going-in, why, and what's the IRR at equal or higher? | "Cap rates will compress"; IRR breaks at a flat cap; no sensitivity |
| `Q-FEE-04` | What pref do LPs receive before promote, and is it cumulative and compounding? | Pref below 6% or absent; non-cumulative |
| `Q-FEE-03` | Is the waterfall deal-by-deal or whole-of-fund, and is there a clawback? | High promote, no clawback; can't explain the catch-up; "you get paid when we get paid" |
| `Q-FEE-02` | Which providers are GP-affiliated, what do they charge, and is it benchmarked? | "All arm's-length" without names; no benchmark |
| `Q-GP-02` | Can you restate your track record as net-to-LP IRR on fully realized exits only? | Project- or GP-level IRR only; "most deals are still performing" |
| `Q-GP-01` | How much of your own capital is in this deal, on the same terms as LPs? | "Sweat equity"; fee waiver instead of cash; token amount on better terms |
| `Q-GP-03` | Have you or your principals faced regulatory action, enforcement or investor litigation? | "Nothing material"; a search turns up something undisclosed |
| `Q-MKT-01` | What submarket supply and absorption data support the rent-growth assumption? | Metro-level optimism; "rents always go up here"; no pipeline acknowledged |
| `Q-LIQ-01` | What are my options if I need to exit before the hold ends? | "A secondary market may develop"; vague promises. An honest "there is none" is a good answer |

**Nice-to-ask**

| ID | Question | Bad-answer signal |
|---|---|---|
| `Q-DIST-02` | When are capital calls expected, and what's the consequence of a missed or late call? | "Calls as needed"; punitive dilution buried in the docs |
| `Q-LIQ-02` | When are K-1s delivered, and have they historically met the deadline? | "As soon as we can"; history of extensions |
| `Q-GP-04` | How has team and monitoring capacity grown with AUM? | "Lean and efficient" as the whole answer; no named asset manager |

## 9. Diligence Checklist

Third-party verification once the materials exist:

- [ ] **PPM and operating agreement:** read the waterfall, fee and distribution-suspension clauses directly, and reconcile them to the marketing numbers
- [ ] **Background and regulatory:** SEC, FINRA, state records and litigation searches on the sponsor and principals
- [ ] **Financials:** tie rent roll and T-12 to bank or audited statements, and reconcile T-12 cash flow after debt service to the 7%
- [ ] **Prior distributions:** on the sponsor's earlier deals, compare projected to actual, and separate income from return of capital
- [ ] **Comps:** rent and sale comps, plus submarket supply pipeline, from an independent source
- [ ] **Appraisal:** independent value against purchase price and going-in cap
- [ ] **Lender:** term sheet or loan documents confirming rate, maturity, covenants, rate cap and any refi assumptions
- [ ] **Track record:** LP statements or references from realized multifamily exits

## 10. Verdict

**Pass as presented — insufficient disclosure.**

*Screening output only, not investment advice.*

**Reasoning.** The deal gives a headline IRR and a distribution shape. It gives no sponsor, net-vs-gross basis, hold, fees, waterfall, debt, T-12, rent roll or exit assumptions, so the core return story can't be underwritten. This is a statement about the materials, not the asset, and nothing here says the deal is bad. No RED was fired on an assumed fact.

**What's genuinely attractive.** Quarterly income from Year 1 and progressive capital return are the LP-friendly version of the J-curve. If real, they reduce the bet on a single exit date.

**Biggest swing factor: what funds the capital return.** If surplus operating cash funds it, this is an income story with real early de-risking. If a refi funds it, the early-cash appeal rests on a credit market and added leverage, the failure mode the 2022–24 frozen-refi cases illustrate. Net-vs-gross is second, at about 430–470 bps.

**Would have to be true to move to Pursue:**
- 14% is net to LP, or the net still clears the hurdle for the actual hold (the 7-year base case at 9.71% is already thin)
- T-12 cash flow after debt service covers the 7% from Year 1
- Capital return has a dated schedule that doesn't depend on a refi at assumed terms, or has a credible fallback
- The flat-exit-cap case still clears the pref, with less than 60% of the return from terminal value
- Debt matures at or after the planned exit, with rate cap coverage
- Realized net-to-LP multifamily exits and cash co-invest on pari-passu terms

**Who it would suit, if it holds up.** An LP who values current income and earlier capital back, and who can redeploy returned capital. It won't suit an LP maximizing equity multiple, since this shape may produce a meaningfully lower multiple at the same IRR, or one who may need liquidity before exit.

**Re-screen list:** PPM or memo with fee schedule and waterfall; net IRR, equity multiple and hold; distribution schedule with funding source; T-12 and rent roll; full debt terms; going-in and exit caps with sensitivity; sponsor name with realized exits and co-invest.

---

## Comparison set-up (waiting on Deal B)

Send Deal B and it gets the same screen, then this contrast. Headline IRRs won't be treated as comparable until both are on a net-to-LP basis.

| Compare on | Deal A | Deal B |
|---|---|---|
| Net-to-LP IRR | Not stated (14% projected, basis unknown) | Pending |
| Equity multiple | Not stated | Pending |
| Hold / lock-up, and hurdle | Not stated | Pending |
| First distribution | Year 1, quarterly 🟢 | Pending |
| Current yield | 7% cash-on-cash 🟢 (coverage unverified) | Pending |
| Capital return | Progressive 🟢 (no schedule) | Pending |
| Share of return from terminal value | Unknown; about 3–75% across illustrated shapes 🔴 | Pending |
| Funding source of capital return | Not stated | Pending |
| Net premium over comparator | +908 bps if net; +440–479 bps if gross with an assumed stack 🔴 | Pending |
| Leverage and refi dependence | Not stated | Pending |
| Fee drag | Not computable | Pending |
| Sponsor and realized record | Not stated | Pending |

**The point of the contrast.** Timing cuts both ways at equal IRRs. If Deal B back-loads to exit, it concentrates return risk on one sale in one market (`GEN-11`), but it may offer a higher multiple. Deal A's shape reduces that exit concentration, but only if the cash is genuinely earned, and it leaves the LP with reinvestment risk on returned capital. The early-cash deal is the stronger one only if its cash holds up under `Q-DIST-01` and `Q-EXIT-02`.
