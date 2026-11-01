# Eval fixture 08
*Iteration-6 run, 2026-11-01, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 436a76b.*

**Verdict: Pass.** Six terms you stated each fire a RED flag on their own. Together they mean the GP has no money in, takes up to half the profit, returns nothing if the deal later turns, and needs a 2028 debt transaction after the hedge has already lapsed.

*Screening output only, not investment advice.*

You asked whether to invest. I'm not a licensed advisor and can't make that call for you. What this screen can say is that the deal doesn't earn more diligence time as structured.

Confidence tags: 🟢 stated or from a reference, 🟡 inferred, 🔴 assumed or unverifiable. This rests on your summary; I have not seen the documents, so "not stated" means not in what you gave me.

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Multifamily; value-add vs core/core-plus not stated 🟢 |
| Deal type | Equity syndication, single asset 🟢 |
| Sponsor | Not stated (one principal named in a prior SEC action 🟢) |
| Geography | Not stated |
| Minimum | Not stated |
| Hold | Not stated |
| Raise | Not stated |
| Claimed return | Not stated; projections show an upside case only 🟢 |
| GP co-invest | $0: "our expertise is our investment" 🟢 |
| Waterfall | American, 50% promote, no clawback 🟢; pref and catch-up not stated |
| Debt | Floating rate; cap expires in 12 months; matures 2028 🟢 |
| Track record | All current, unrealized marks 🟢 |

## 2. Return Stress-Test

No return figure, NOI, debt balance or exit cap was given, so no case can be sized. The table shows the mechanics. Any figure the GP supplies from its upside case should be read as a ceiling.

| Case | Swing assumptions | What happens | LP result |
|---|---|---|---|
| **Bull** (the only case shown) | Rates ease or the cap is replaced cheaply; 2028 refi or sale closes on plan; rents hit pro forma | Business plan works | GP's figure not given. Up to half the profit above the pref goes to the GP 🟢 |
| **Base** (no GP version exists) | Cap lapses around Nov 2027 🟡, rates near today's; exit cap at or above going-in; rent growth flat to modest | Debt service reprices unhedged for the months before maturity; distributions fall; 2028 refi or sale at market terms | Can't size. Likely below the pro forma, possibly below the pref 🟡 |
| **Bear** (the 2022–24 pattern, `GEN-10`) | Cap lapses, rates stay elevated, refi market frozen at maturity, exit cap wider | Debt service erases distributions, then a capital call, rescue capital ranking ahead of LPs, or a forced sale | LP capital impaired, with no second asset to offset it. GP loses no cash of its own 🟢 |

**Rate timing.** If the 12 months runs from today, the cap ends around Nov 2027 and the loan matures 14–26 months from now, leaving roughly 2–13 months uncapped depending on the 2028 month 🟡. The `05` snapshot curve slopes up (3mo 4.24%, 2yr 4.87%, 10yr 5.18%), so it gives no support to "rates will be lower by then" 🟢.

**Against the public hurdle.** The comparator is VNQ at 4.92% (10yr). No net-to-LP IRR was given, so whether this clears the lock-up can't be determined. The bar it would have to meet 🟢:

| If the lock-up is | Illiquidity premium | Net-to-LP IRR needed |
|---|---|---|
| 5 years | ~300–400 bps | ~7.9–8.9% |
| 7 years | ~400–600 bps | ~8.9–10.9% |

Treat these as floors. `05` says single-asset concentration raises the premium an LP should demand, since VNQ is a basket of hundreds. The 10yr Treasury at 5.18% also out-yields VNQ's trailing return, so it is the tighter floor. Illustrative net figures against this bar are in §4.

## 3. Where LP Returns Come From

**Can't tell from this.** With no IRR split, exit cap or going-in cap, the >60% test can't be run, so `GEN-07`, `GEN-08` and `EQUITY-06` are unresolved rather than fired.

What can be said:
- **Unlevered baseline** 🟢: NCREIF NPI returned 5.00% over the trailing four quarters, almost all income (latest quarter 1.17% income, 0.12% appreciation). Residential was 5.3% in 2025. Whatever the deal projects above about 5% has to come from leverage, operating gains or assumed appreciation, and the GP should show which.
- **Both paths run through a 2028 transaction** 🟡. Every multifamily hold norm in `01` (5–7 or 7–10 years) runs past 2028. So one of two things is true:
  - The hold outlasts the loan, and the return needs a refi (`GEN-09`, `EQUITY-07`).
  - The asset sells by 2028, and most of the return is probably sale proceeds (`GEN-08`).
- Undisclosed extension options could change this. Ask for them.

## 4. Fee Stack Summary

**Total gross-to-net drag: not computable from disclosure, and that is the finding** (`GEN-16`). Only the promote percentage was given. Acquisition, asset management, disposition, loan placement, refinance, construction management and admin fees are all unstated, as are affiliate fees and any feeder layer (50–150 bps/yr if present).

**Illustrative only, on 🔴 assumed inputs:** 5-year hold, 8% simple pref, 50% as a flat split, bullet exit. "Promote only" passes 0 for every undisclosed fee, so it is a floor. "With `02` stack" adds the `02` worked-example fees (2% acquisition, 1% disposition, 1.5% annual asset management, 0.3% annual admin). None of these numbers can support a decision; they show sensitivity.

| Gross IRR | Fees | Catch-up | Total drag | Net to LP | Over VNQ | 5-yr hurdle read |
|---|---|---|---|---|---|---|
| 12% | Promote only | 100% | 504 bps | 6.96% | 204 bps | Thin / fails |
| 12% | Promote only | None | 240 bps | 9.60% | 468 bps | Clears |
| 15% | Promote only | 100% | 647 bps | 8.53% | 361 bps | Clears (thin) |
| 15% | Promote only | None | 373 bps | 11.27% | 635 bps | Clears |
| 15% | With `02` stack | 100% | 887 bps | 6.13% | 121 bps | Thin / fails |
| 15% | With `02` stack | None | 613 bps | 8.87% | 395 bps | Clears (thin) |

Reading the table:
- **Promote size.** `02` treats over 30% as aggressive 🟢. At 15% gross, the same model with a 20% promote and 100% catch-up costs 241 bps and nets 12.59%, versus 647 bps and 8.53% here.
- **Dead zone under a full catch-up.** Net to LP stays at 6.96% at every gross IRR the model was run on from 8% through 12%. All of the improvement in that range goes to the GP.
- **No pref.** If there is no pref, the LP keeps 50% of all profit, the same as the full catch-up at 15% gross (8.53% net).
- **Where this could overstate.** If 50% is only a top tier above a high IRR hurdle, these figures are too harsh. You stated "50% promote" without tiers, so this is a must-ask. Hold length barely moves the result (15% gross over 7 years: 598 bps with full catch-up, 374 bps with none).
- **Where this understates.** The model assumes a bullet exit, so it can't capture promote paid early on interim cash that is then never returned (see `EQUITY-02`).

## 5. Red Flags

**RED, stated terms**
- **`GEN-01` Zero GP co-investment** 🟢. "Our expertise is our investment" asserts alignment without creating it. The GP earns fees and promote whatever happens to your capital.
- **`GEN-02` Prior regulatory action** 🟢. A principal was named in an SEC action. Outcome, conduct and whether investors were harmed are all unknown 🔴, and being named is not a finding. The flag fires on the history; the facts decide how much it weighs.
- **`EQUITY-01` American waterfall with high promote** 🟢. At 50%, this is far above the 15–30% norm in `02`.
- **`EQUITY-02` No clawback in a deal-by-deal waterfall** 🟢. The library's mechanism is cross-asset (early winners, late losers), and this is one asset, so that exact path doesn't exist. The single-asset version: promote paid on interim distributions or refi proceeds before your capital is back, followed by a loss at sale, with nothing to recover it. Whether the documents allow that is 🔴. If the GP gets no promote until all LP capital and pref are returned, this exposure shrinks materially.
- **`GEN-10` Rate cap expiry** 🟢. The cap ends before the 2028 maturity, leaving the debt unhedged into the same window when it must be refinanced or repaid. Extension cost and budget are unknown.
- **`GEN-14` Unrealized-only track record** 🟢. The marks are self-reported, and the GP has not shown it can exit and return capital. By construction no realized net-to-LP figure exists (`GEN-05` subsumed; the basis of the marks is also unstated).

**RED, inferred, pending the answer**
- **`GEN-09` Debt maturity inside the business plan** 🟡. Hold is unstated, but 2028 is about two years out and category holds are 5+ years, so a forced refi or sale at maturity is the likely shape.

**YELLOW–RED**
- **`EQUITY-07` Refi-dependent plan** 🟡. Follows from `GEN-09` unless extensions or a sale by maturity are the plan.
- **`GEN-15` Missing financials** 🟢. No rent roll, T-12 or complete debt terms were provided.
- **`GEN-16` No fee or complete waterfall disclosure** 🟢. See §4.

**YELLOW**
- **`GEN-13` No downside case** 🟢. Showing only an upside case is worse than a single-point pro forma, because it conceals the fragility and also sets the expectation at the top of the range.
- **`GEN-11` Distribution timing not disclosed** 🟢. No schedule was given, so the J-curve is unknown.
- **`GEN-17` Essential category disclosures absent** 🟢. Exit-cap sensitivity, refi assumptions and prior multifamily exits are missing (§6).

**Unresolved, not fired** (each needs a fact you didn't have; all routed in §8)
- `GEN-07`, `GEN-08`, `EQUITY-06`: return source and exit cap. I can't call this a financing story yet.
- `EQUITY-03`: catch-up rate.
- `EQUITY-04`, `EQUITY-05`: pref level and type. If the pref is absent, `EQUITY-04` fires.
- `GEN-06`: affiliate fees. Worth a hard look with a GP putting in no cash.
- `GEN-12`: T-3 or T-6 only.
- `GEN-18`: rent growth vs submarket supply.
- `GEN-03`: marketing over substance. Upside-only projections plus marks-only history point this way, but I haven't seen the materials.

**Clusters**
- **Rate cap and refi** (`GEN-10` + `GEN-09` + `EQUITY-07`): the connected 2022–24 failure mode behind many multifamily capital calls and wipeouts.
- **Alignment** (`GEN-01` + `EQUITY-01` + `EQUITY-02`): the GP holds a free option. It takes up to half the upside and has no cash in the downside. That setup also rewards risk-taking, which fits a short hedge on floating debt 🟡.
- **Trust** (`GEN-02` + `GEN-14` + `GEN-13`): a regulatory history, no proven exits, and no downside shown. The items that would normally let you verify the GP are the ones missing.

**Concentration** (no library ID): a single asset means no diversification against any of the above (`05`).

## 6. Missing Disclosures

**Return and hold**
- Hold period, target net-to-LP IRR, equity multiple
- Base and downside cases
- Distribution schedule

**Financials (`01` essentials)**
- Rent roll
- T-12 actuals; occupancy history if this is core/core-plus
- Value-add vs core classification and business plan
- Pro forma exit cap with sensitivity, and going-in cap
- Submarket and geography

**Debt (`01` essentials)**
- Maturity month, extension options and their tests
- Balance and LTV, spread, amortization, prepayment
- Cap strike and notional, cost to extend
- Refi assumptions

**Fees and waterfall (`02`)**
- All non-promote fees, and which providers are GP affiliates
- Pref rate; cumulative vs non-cumulative; simple vs compounding
- Catch-up rate; whether 50% is flat or a top tier
- Whether promote can be paid before return of capital
- Any feeder or fund-of-funds layer

**GP**
- Identity; prior multifamily exits with realized net-to-LP returns
- Basis and source of current marks
- SEC action details

**LP terms**
- Minimum and raise
- Capital-call and dilution mechanics
- Liquidity options

**Assumed in §§2 and 4 (none disclosed):** gross IRRs, hold of 5 and 7 years, 8% simple pref, catch-up of 0 and 100%, flat 50% split, 0 or `02` worked-example fees.

## 7. GP Alignment

| Test | Finding |
|---|---|
| Co-invest (cash, pari-passu?) | $0 🟢. Nothing is pari-passu because nothing is invested |
| Realized net-to-LP track record | None. **Unverified**: unrealized marks are not a track record 🟢 |
| Waterfall alignment | Poor as stated: 50% promote, no clawback 🟢. Pref and catch-up unknown |
| Affiliate fees | Not stated. Unverified |
| Conduct | Principal named in a prior SEC action 🟢. Facts unverified 🔴 |

There is no structural alignment and no proof of competence at exit. If a rescue is needed in 2028, the only committed capital is the LPs'.

## 8. Questions for the GP

**Already answered badly.** Your summary matches the bank's bad-answer signal on these five, and the bank says to treat a bad answer as the flag confirmed. A bad must-ask is on its own grounds to pass or hard-condition.

| ID (flag) | Question | Bad-answer signal | Status |
|---|---|---|---|
| `Q-GP-01` (`GEN-01`) | How much of your own capital is in this deal, on the same terms as LPs? | "Our sweat equity is our investment"; a fee waiver presented as co-invest | Given almost verbatim |
| `Q-GP-02` (`GEN-14`, `GEN-05`) | Can you restate your track record as net-to-LP IRR on fully-realized, exited deals only? | "Most deals are still performing"; project-level IRR only | Marks only |
| `Q-FEE-03` (`EQUITY-01`, `EQUITY-02`, `EQUITY-03`) | Is the waterfall deal-by-deal or whole-of-fund, and is there a clawback? Add: what is the catch-up, and can promote be paid before capital is returned? | Deal-by-deal, high promote, no clawback; can't explain the catch-up | Stated |
| `Q-RISK-02` (`GEN-10`) | When does the rate cap expire relative to debt maturity, and what's the cost to extend it at current pricing? | Cap expires before maturity; cost not modeled; "rates should be lower by then" | First half stated |
| `Q-DS-03` (`GEN-13`) | What is the return under a bear case: flat rents, higher exit cap, no refinance? | Single-point pro forma; "we underwrite conservatively" with nothing to show; a "bear case" that is still a gain | Upside only |

**Must-ask, still open**

| ID (flag) | Question | Bad-answer signal |
|---|---|---|
| `Q-GP-03` (`GEN-02`) | Have you or your principals faced any regulatory action, enforcement, or investor litigation? Add: which principal, what was alleged, how did it resolve, is that person still in control? | "Nothing material"; blames the regulator; a search surfaces what they didn't disclose. Note whether they told you or you found it |
| `Q-RISK-01` (`GEN-09`) | When does the debt mature relative to the projected hold, and what's the refinance or extension plan? | "We'll refinance" with no terms; no plan if the market is shut |
| `Q-EXIT-02` (`EQUITY-07`) | Does the plan depend on a refinance, and what happens to distributions if it isn't available on the assumed terms? | Capital return requires a refi at lower rates; "the refi market will reopen" |
| `Q-DS-01` (`GEN-08`, `EQUITY-06`) | What share of projected LP IRR comes from in-place cash flow vs the exit, and what's the IRR at a flat exit cap? | Won't decompose it; "real estate always appreciates"; IRR falls below pref at a flat cap |
| `Q-DS-02` (`GEN-07`) | Strip out leverage and cap-rate compression: what is the unlevered, in-place return? | "Leverage is just how the deal works"; no unlevered view exists |
| `Q-EXIT-01` (`EQUITY-06`) | If the exit cap is below going-in, why, and what's the IRR at an exit cap at or above going-in? | "Cap rates will compress"; no sensitivity offered |
| `Q-FEE-04` (`EQUITY-04`, `EQUITY-05`) | What preferred return do LPs receive before the GP earns promote, and is it cumulative and compounding? | Below 6% or absent; non-cumulative |
| `Q-FEE-01` (`GEN-16`) | Can you provide the complete fee schedule and the full distribution waterfall? | "Standard market fees"; "the PPM has it" without producing it |
| `Q-FEE-02` (`GEN-06`) | Which service providers are GP-affiliated, what do they charge, and are those rates third-party-benchmarked? | "All arm's-length" without naming providers |
| `Q-RISK-03` (`GEN-12`, `GEN-15`) | Can you provide trailing-twelve-month actuals, the rent roll, and complete debt terms? | T-3/T-6 only; "confidential until you commit" |
| `Q-DIST-01` (`GEN-11`) | What is the projected distribution schedule, and at what milestones does LP capital start returning? | "We'll distribute when the deal supports it"; no milestones |
| `Q-MKT-01` (`GEN-18`) | What submarket supply pipeline and absorption data support the rent-growth assumption? | Metro optimism standing in for submarket data; no pipeline acknowledged |
| `Q-LIQ-01` | What are my options if I need to exit before the hold ends? | "A secondary market may develop." An honest "none" is a good answer |
| `Q-DIST-02` (escalated) | When are capital calls expected, and what's the consequence of a missed or late call? | "Calls as needed"; punitive dilution buried in the docs. Escalated because the `GEN-10` failure path ends in capital calls that only LPs would fund |

**Nice-to-ask**
- `Q-GP-04` (`GEN-04`): How have headcount and deal-monitoring capacity grown alongside AUM? Bad answer: "we're lean and efficient" as the whole answer; no named asset manager.
- `Q-LIQ-02`: When are K-1s delivered, and have they historically arrived before the filing deadline? Bad answer: "as soon as we can"; a history of extensions.

## 9. Diligence Checklist

Only if the terms change (see §10). Verify independently, not through the GP:

- **Regulatory and background:** SEC action documents and final order; FINRA, state-regulator and court searches on every principal and entity. Ask counsel whether the action triggers Regulation D Rule 506(d) "bad actor" disqualification or disclosure (this point is from outside the skill's references 🟡).
- **PPM and operating agreement:** the actual waterfall language, clawback, catch-up, pref, all fees, capital calls and dilution, and any right to remove the GP.
- **Lender and loan documents:** maturity, extension tests, spread, cap strike and notional, and whether the lender requires a replacement cap on expiry (a common loan term, from outside the references 🟡). Direct lender confirmation of loan status.
- **Asset:** T-12 and rent roll tied to bank statements, independent appraisal, sale and rent comps, submarket supply data.
- **Track record:** third-party support for current marks; references from LPs in the GP's existing deals, ideally ones the GP didn't select.
- **Own advisers:** securities counsel and a tax adviser. This report is not legal or tax advice.

## 10. Verdict

**Pass.** This is a merits verdict.

*Screening output only, not investment advice.*

**Reasoning.** Six RED flags fire on terms you stated (`GEN-01`, `GEN-02`, `EQUITY-01`, `EQUITY-02`, `GEN-10`, `GEN-14`), and a seventh is likely (`GEN-09`). In `03`, a RED is pass-or-resolve before committing. Five must-asks in `04` have already drawn the bank's named bad answer.

The flags also compound. If the 2028 debt event goes badly, LPs alone bear the loss and fund any rescue, under a GP with no cash at risk, an SEC history and no record of returning capital. If it goes well, the GP keeps up to half the profit.

**Why not "Pass as presented — insufficient disclosure."** Disclosure is thin: no IRR, hold, pref, fees or financials, so the return can't be underwritten. But that label implies better paperwork could fix the deal. It couldn't. The problem is what was disclosed. A full PPM would still show zero co-invest, a 50% promote and a cap that ends before maturity. The missing items are a second, independent reason, not the main one.

**Biggest swing factor.** The 2028 debt event: whether the hedge is replaced, at what cost, and whether a refi or sale closes on acceptable terms. It can't be sized from what's disclosed, and it decides whether LP capital comes back at all. `Q-GP-03`, on the SEC action, can independently end the conversation.

**Who it suits.** No passive LP relying on sponsor alignment. It is arguable only for an anchor investor with the leverage to rewrite the terms, who could lose the whole check.

**What would have to be true to re-screen.** All of these, in writing:
1. Meaningful GP cash co-invest on pari-passu terms.
2. SEC action fully documented, resolved, disclosed by the GP and cleared by your counsel.
3. Realized, net-to-LP returns on exited multifamily deals, or an explicit discount for a first-time exit record.
4. Promote near the `02` range of 15–30% over a 6–10% cumulative pref, or a 50% tier only above a high return threshold; plus no promote before LP capital is returned, or a secured clawback.
5. Hedge covering the period to maturity or a funded extension budget; extension options or a plan that doesn't depend on a refi.
6. A real bear case in which LP capital survives, and a base-case net-to-LP IRR clearing VNQ plus the illiquidity premium (§2) and the Treasury floor, after all fees.
