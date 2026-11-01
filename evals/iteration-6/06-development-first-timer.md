# Eval fixture 06
*Iteration-6 run, 2026-11-01, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 436a76b.*

**Verdict: Pass as presented — insufficient disclosure.** None of the five essential development disclosures was provided, and what was stated is a financing story: exit-priced, single-case, with an aggressive fee stack, run by a sponsor with no ground-up record. The headline return also does not reconcile with itself.

*Screening output only, not investment advice.* This report screens a deal for further diligence. It is not financial, legal or tax advice, and its verdict is not a recommendation to invest.

Confidence tags: 🟢 stated or from a reference, 🟡 inferred, 🔴 assumed or unverifiable.

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Development (ground-up) 🟢. Underlying property type: Not stated |
| Deal type | Development (equity) 🟡, inferred from the IRR / multiple pitch and fee stack. Position in the capital stack: Not stated |
| Sponsor | Name: Not stated. This is its first ground-up project 🟢 |
| Geography | Not stated |
| Minimum | Not stated |
| Raise / project size | Not stated |
| Hold | 3 years 🟢, the bottom of the 3–5 year category range |
| Claimed return | 25% IRR / 2.5x 🟢. Gross or net: Not stated |
| Stated fees | 5% development fee + 4% construction management 🟢. Fee bases: Not stated |
| Downside case | None shown 🟢 |
| Exit cap | Underwritten below the going-in basis 🟢. Neither figure stated |

**The headline does not reconcile.** 25% IRR, 2.5x and 3 years cannot all be true on one basis 🟢 (arithmetic):

| Hold these two fixed | The third must be |
|---|---|
| 2.5x over 3 years | About 35.7% IRR, if capital goes in at the start and comes out at year 3. Earlier distributions push the IRR higher, not lower |
| 25% IRR over 3 years | About 1.95x, not 2.5x |
| 25% IRR and 2.5x | About 4.1 years, not 3 |

So one of three things is true: the real hold is 4+ years, the multiple is really about 1.95x, or the two figures are on different bases (for example, a gross multiple beside a net IRR). Each changes the deal. This report tests 25% over 3 years (about 1.95x), the less flattering multiple.

---

## 2. Return Stress-Test

The sponsor supplied one case, so the sponsor's own swing assumptions are unknown. The cases below are **🔴 illustrations, not findings**, and the verdict does not rest on them. They assume $100 project cost, 60% loan-to-cost, a 5.5% exit cap and 50 bps of compression, calibrated to return 25% / 1.95x. They are before all fees and promote, and they add no extra interest carry for a delay.

| Case | Swing assumptions | Exit value | Equity multiple | Equity IRR, pre-fee |
|---|---|---|---|---|
| Bull: the sponsor's pro forma | 5.5% exit cap, on budget, 3 years | $138 | 1.95x | 25.0% |
| Base: no cap compression | 6.0% exit cap, on budget, 3 years | $127 | 1.67x | 18.5% |
| Bear | 6.5% exit cap, 10% overrun funded by equity, 12-month delay | $117 | 1.14x | 3.3% |

The sponsor's only case is treated as the bull case because it needs cap compression, an on-time three-year build and lease-up, and flawless execution from a first-time developer.

Three things to take from this:
- **Removing compression alone** costs about 650 bps in this illustration.
- **The return requires a large spread over cost.** At 60% loan-to-cost, 1.95x needs a finished value about 38% above total cost, and 2.5x needs about 60% above. Whether the actual deal supports that is unknowable without its budget and comps.
- **The failure mode is stacking.** A first-time developer's overrun and delay arrive together, then the sale prices into whatever cap rate exists at completion, possibly while construction debt is maturing.

**Net-to-LP vs comparator** (`benchmark_comparator.py`, development, VNQ 4.92% 10yr, 🟢 for the benchmark inputs):

| IRR tested | Basis | Premium over VNQ | Hurdle | Script read |
|---|---|---|---|---|
| 25.00% | Headline, unlabeled | 2008 bps | ~300–400 bps | Clears comfortably |
| 22.00% | After disclosed fees at face (§4) | 1708 bps | ~300–400 bps | Clears comfortably |
| 18.50% | 🔴 Base, pre-fee | 1358 bps | ~300–400 bps | Clears comfortably |
| 15.66% | 🔴 Headline after placeholder full stack (§4) | 1074 bps | ~300–400 bps | Clears comfortably |
| 3.30% | 🔴 Bear, pre-fee | −162 bps | ~300–400 bps | Fails outright |

**Does it clear the lock-up?** On paper yes, but that says little here. A projection clearing a roughly 8–9% bar (VNQ plus premium) is not evidence the deal will. Three discounts apply:
- **The figure is unlabeled.** It cannot be treated as net until the sponsor says so; if it is gross, comparing it to VNQ is invalid.
- **It sits above the category's target.** 25% is 300 bps over the top of the 18–22% net *target* range, and realized development returns often land below target on overruns, financing-cost spikes and lease-up misses (`01`). `05` says to discount this premium heavily.
- **Amplifiers raise the bar.** This is a single asset against an index of hundreds, and private real estate dispersion is wide (opportunistic interquartile range about 13 points, `05`) 🟡 using opportunistic as the closest analog. Also, the 10-year Treasury at 5.18% currently out-yields VNQ, so it is the tighter floor. The bear case is below both.

---

## 3. Where LP Returns Come From

No decomposition was provided, which is the first finding.

- **Cash flow: little to none 🟡.** A ground-up asset produces no income during construction, and a 3-year hold leaves little or no stabilized period before sale.
- **Exit: nearly all of it 🟡.** The return is realized at sale, so it clears the >60% exit-dependence line (`GEN-08`). The exact share is the sponsor's to prove.
- **Cap-rate assumption: stated 🟢.** The exit cap is below the going-in basis (`EQUITY-06`).
- **Leverage: unknown.** Debt was not disclosed, so its share cannot be sized and goes to a must-ask.

**Unlevered overlay.** NCREIF NPI, unlevered institutional private real estate, returned 5.00% over the trailing four quarters and is almost entirely income 🟢. About 20 of the 25 points therefore come from something other than in-place real estate return: leverage, development margin and the exit cap assumption 🟡. Development margin is a legitimate source, but here it exists only at the moment of sale, at a price the deal assumes will improve.

**Read: a financing story (`GEN-07` + `GEN-08` + `EQUITY-06`)**, not an income story. `GEN-07` fires on the stated cap assumption plus the lack of an operating period. It does not depend on any assumed leverage figure.

**One caveat on `EQUITY-06` 🟡.** "Going-in basis" is unusual wording, because a ground-up project has no in-place going-in cap. If the sponsor means yield on cost, an exit cap below it is the normal development spread rather than compression. The test then becomes the exit cap against today's market cap for comparable stabilized product. The flag stands as RED on the deal as stated until the sponsor shows that comparison (`Q-EXIT-01`).

---

## 4. Fee Stack Summary

**Gross-to-net drag: at least 300 bps/yr from disclosed fees alone. This is a floor, and the full figure is not computable from this disclosure. That is the finding (`GEN-16`).**

| Fee | Stated | Norm (`02`) | Read | Drag at face, 3-yr hold |
|---|---|---|---|---|
| Development fee | 5%, base not stated | 3–5% of total project cost; aggressive >6% **or split across both a development and a CM fee** | Top of range, and the split fires the aggressive test | 167 bps/yr |
| Construction management | 4%, base not stated | 3–5% of hard costs; aggressive >6% | In range alone | 133 bps/yr |
| **Disclosed total** | **9% at face** | | **Aggressive as a pair 🟢** | **300 bps/yr** |

If the 25% is before these fees, the net is at most about 22% (`fee_drag_calculator.py`; the combined 9% was entered in its one-time fee field, because it has no development-fee input, and all undisclosed fees and carry were entered as 0).

Why 300 bps is a floor:
- **The bases are wrong for the math 🟡.** The calculator reads 9% as a share of equity, but these fees normally run on project and hard costs, a larger base in a levered deal. 🔴 At 60% loan-to-cost and hard costs at 70% of budget, the same fees equal 19.5% of equity, or 650 bps/yr (net about 18.5%).
- **The rest of the stack is silent.** Nothing was disclosed on promote, pref, catch-up, asset management, acquisition, disposition, loan placement, admin or any entitlement fee. A silence here is a flag, not a zero (`02`).
- **Timing may be worse than the math 🟡.** Development and CM fees typically pay out during construction, before the LP has seen a dollar. The calculator spreads them evenly across the hold.

**🔴 Illustration of a full stack.** Adding the `02` worked-example placeholders (1% disposition, 1.5% asset management, 0.3% admin, 20% promote over 8% with 100% catch-up) gives **934 bps/yr and about 15.66% net**: 180 recurring, 333 one-time, 421 promote. That is below the 18–22% category target and about level with SPY's 15.39% trailing decade, an exceptional one that `05` warns against extrapolating. These are not this deal's terms.

**Possible offset.** If the fees are already capitalized in the project budget, the 25% may already reflect them, and the drag is not additive to that figure. The sponsor must say which. It does not change that the fee load is aggressive.

---

## 5. Red Flags

**RED**

| ID | Finding | LP exposure | Tag |
|---|---|---|---|
| `EQUITY-06` | Exit cap below the going-in basis bakes unproven cap movement into the headline | The LP's return depends on a sale price the market may not pay at completion | 🟢, subject to the §3 definition check |
| `GEN-08` | Exit-dependent IRR: little or no operating period inside a 3-year hold | No income cushion; one sale event decides the whole return | 🟡 |
| `GEN-07` | Financing story: return rests on exit pricing and undisclosed leverage rather than operations; about 20 points above the unlevered baseline | Collapses if rates rise or credit tightens at completion | 🟡 |
| `GEN-14` | No realized ground-up exits exist, because this is the first project. Development experience is not fungible with acquisition experience (`01`) | The LP funds the sponsor's learning curve on budget, schedule and lease-up | 🟢 |

**YELLOW–RED (treated as RED until answered)**

| ID | Finding | LP exposure | Tag |
|---|---|---|---|
| `GEN-06` | Development plus CM fees is the split `02` calls aggressive. Recipients not named; likely sponsor or affiliates | Layered fees paid regardless of LP outcome. Fees sized on cost also reward a bigger budget, and a first-time developer collecting a CM fee has no record of doing that job | 🟢 split; 🟡 affiliate |
| `GEN-16` | Fee disclosure is partial and no waterfall is disclosed | Gross-to-net drag is unknowable | 🟢 |
| `GEN-15` | No debt terms or budget. T-12 and rent roll do not apply to a ground-up project, so debt terms are the live gap | The capital stack ahead of the LP is invisible | 🟢 |

**YELLOW**

| ID | Finding | LP exposure | Tag |
|---|---|---|---|
| `GEN-13` | Single pro forma, no sensitivity or downside case | Fragility is concealed. Sharper here, since development is cycle-exposed | 🟢 |
| `GEN-11` | IRR with no distribution schedule | Return is back-loaded to exit. A schedule would also resolve the 25% / 2.5x / 3-year conflict | 🟢 |
| `GEN-17` | All five essential development disclosures absent (§6) | The deal is unscreenable on each of those axes | 🟢 |

**Clusters.** `GEN-07` + `GEN-08` + `EQUITY-06` is the financing story. `GEN-13` on top of it means nobody has shown what happens when that story fails. `GEN-14` means no record exists to justify trusting the single case.

**Finding with no `03` ID:** the return figures do not reconcile (§1). Routed to `Q-DS-01` and `Q-DIST-01`.

**Not fired, because nothing was stated.** These are must-asks in §8, not findings:
- `GEN-01` (co-invest)
- `GEN-02` (regulatory or litigation history)
- `GEN-05` (no track-record figures cited to test)
- `GEN-09` and `GEN-10` (debt maturity, rate cap)
- `EQUITY-01` through `EQUITY-05` (waterfall, clawback, catch-up, pref)
- `EQUITY-07` (refi dependence)
- `GEN-18` (no rent-growth or submarket data)

`GEN-19` applies only if the project turns out to be office, which would also make this a variable class with no VNQ comparator.

---

## 6. Missing Disclosures

**Essential development disclosures (`01`): 0 of 5 provided.**
1. Entitlement and permit status. Entitled-but-not-permitted is a different deal from shovel-ready, and a 3-year hold leaves no room for this
2. Hard-cost budget with contingency %. The norm is 5–10% of hard costs; <5% is under-reserved, >15% may pad the fee base (`02`)
3. Debt structure, including takeout assumptions
4. Market absorption assumptions with comp evidence
5. The GP's last three development exits with realized timing and budget vs underwritten. These cannot exist for this sponsor

**Fee and structure (`02`):**
- Fee bases for both stated fees, and who receives them
- Preferred return: rate, cumulative or not, simple or compounding
- Promote, catch-up, split tiers and any clawback
- Asset management, acquisition, disposition, loan placement, refinance, admin and entitlement fees

**Return story:**
- Whether 25% / 2.5x is gross or net
- Going-in and exit cap values, and what "going-in basis" means
- Yield on cost, and exit cap vs current market cap
- Any sensitivity or downside case
- Distribution schedule and capital-call terms

**Basics:** property type, geography, minimum, raise, project cost, capital stack, GP co-invest, sponsor identity and non-development record, LP liquidity terms.

---

## 7. GP Alignment

- **Co-invest:** Not stated. Unverified. Check whether fees received during construction exceed or effectively fund any co-invest, which would leave the GP with little net capital at risk 🟡.
- **Realized net-to-LP track record:** None for ground-up, by the deal's own statement 🟢. Any record from acquisitions is not stated, unverified, and not transferable to development (`01`). Treat this as no relevant track record.
- **Waterfall alignment:** Unknown. No pref, promote, catch-up or clawback was disclosed.
- **Affiliate fees:** Recipients not named. Up to 9% of cost-based fees may reach the sponsor whether or not the LP makes money 🟡. This is the core alignment concern: fee income is more certain than promote, and it is earned while the sponsor is learning the job at the LP's risk.

---

## 8. Questions for the GP

**Must-ask**

| ID | Ask | Fired by | Bad-answer signal |
|---|---|---|---|
| `Q-DS-01` | What share of LP IRR comes from cash flow vs exit, and what is the IRR at a flat exit cap? Also: which of 25%, 2.5x and 3 years is wrong, and on what basis is each stated? | `GEN-08`, `EQUITY-06` | Can't decompose the IRR; "real estate always appreciates"; IRR falls below pref at a flat cap; can't reconcile its own headline |
| `Q-DS-02` | Strip out leverage and cap compression: what is the unlevered return? | `GEN-07` | The levered IRR is the only figure; "leverage is just how the deal works" |
| `Q-DS-03` | What is the return under a bear case: flat rents, higher exit cap, no refinance? Add a cost overrun and a 12-month delay | `GEN-13` | "We underwrite conservatively" with nothing to show; a bear case that is still a gain |
| `Q-EXIT-01` | Why is the exit cap below going-in, and what is the IRR at or above going-in? What does "going-in basis" mean here, and how does the exit cap compare with today's market cap for comparable stabilized product? | `EQUITY-06` | "Cap rates will compress"; IRR breaks at a flat cap; no sensitivity offered |
| `Q-EXIT-02` | Does the plan depend on a refinance or takeout, and what happens if it isn't available on the assumed terms? | Not fired; debt undisclosed (`EQUITY-07`) | "The refi market will reopen"; no fallback |
| `Q-GP-01` | How much of your own cash is in this deal, on LP terms? | Not fired; undisclosed (`GEN-01`) | "Sweat equity is our investment"; co-invest is a fee waiver; a token amount on better terms |
| `Q-GP-02` | Restate your record as net-to-LP on fully realized deals only, separating any development from acquisitions | `GEN-14` (`GEN-05` untested) | Project-level or GP-level IRR only; "most deals are still performing"; acquisition wins offered as development proof |
| `Q-GP-03` | Any regulatory action, enforcement or investor litigation? | Not fired; undisclosed (`GEN-02`) | "Nothing material"; a search surfaces something undisclosed |
| `Q-FEE-01` | Provide the complete fee schedule and waterfall, with the base for the 5% and the 4% | `GEN-16` | "Standard market fees"; "the PPM has it" without producing it |
| `Q-FEE-02` | Who receives the development and CM fees, are they affiliated, and are rates benchmarked? Why both fees, and who actually performs construction management? | `GEN-06` | "All arm's-length" without naming providers; no benchmark offered |
| `Q-FEE-03` | Deal-by-deal or whole-of-fund, and is there a clawback? | Not fired; undisclosed (`EQUITY-01`, `EQUITY-02`) | "You get paid when we get paid"; can't explain the catch-up |
| `Q-FEE-04` | What pref before promote, and is it cumulative and compounding? | Not fired; undisclosed (`EQUITY-04`, `EQUITY-05`) | Pref below 6% or absent; non-cumulative |
| `Q-MKT-01` | What submarket supply pipeline and absorption data support the rent and lease-up assumptions? | `GEN-17`; `GEN-18` untested | Metro-level optimism in place of submarket data; no supply pipeline acknowledged |
| `Q-RISK-01` | When does the debt mature relative to the hold, and what is the extension plan? | Not fired; undisclosed (`GEN-09`) | Maturity inside the hold; "we'll refinance" with no terms |
| `Q-RISK-02` | If floating, when does any rate cap expire relative to maturity, and what does extending it cost? | Not fired; undisclosed (`GEN-10`) | Cap expires before maturity; "rates should be lower by then" |
| `Q-RISK-03` | Provide complete debt terms. For a ground-up deal, substitute the full budget for T-12 and rent roll | `GEN-15` | "The financials are confidential until you commit" |
| `Q-DIST-01` | What is the distribution schedule, and at what milestones does capital start returning? | `GEN-11` | "We'll distribute when the deal supports it"; an IRR with no timing |
| `Q-LIQ-01` | What are my options if I need to exit before the hold ends? | LP lock-up | "A secondary market may develop"; "we'll try to accommodate" |

**Nice-to-ask**

| ID | Ask | Bad-answer signal |
|---|---|---|
| `Q-DIST-02` | When are capital calls expected, and what is the consequence of a missed call? Especially relevant, since an overrun may be funded by the LP | "Calls as needed"; punitive dilution buried in the docs |
| `Q-LIQ-02` | When are K-1s delivered, and have they historically met the deadline? | "As soon as we can"; a history of extensions |
| `Q-GP-04` | Who, by name, will monitor this project? Has capacity grown alongside AUM? | "We're lean and efficient" as the whole answer; no named asset manager |

---

## 9. Diligence Checklist

- [ ] PPM and operating agreement: confirm every fee, its base and recipient, plus the waterfall, capital-call and dilution terms
- [ ] Sponsor background: principals' regulatory, litigation and bankruptcy search, independent of what the sponsor says
- [ ] Realized record: verify any prior exits with closing documents and LP distribution statements
- [ ] Entitlement and permits: verify status directly with the municipality
- [ ] Budget: independent third-party review of cost and contingency
- [ ] Contractor: confirm who the general contractor is and whether any completion or cost guarantee exists, and from whom
- [ ] Lender: term sheet covering rate, maturity, extensions, recourse, covenants and any cap
- [ ] Appraisal: as-completed and as-stabilized value, with the cap rate used
- [ ] Market: independent comps for exit cap, rents, supply and absorption
- [ ] Model: obtain the live model, reconcile 25% / 2.5x / 3 years, and rerun at flat and higher caps

---

## 10. Verdict

**Pass as presented — insufficient disclosure.**

**Reasoning.** Zero of the five essential development disclosures were provided, so the core return story cannot be underwritten. It is not only a paperwork gap, though. What *was* stated all points the wrong way:
- The return comes from a sale priced on a favorable exit cap (`EQUITY-06`, `GEN-08`, `GEN-07`): this is a financing story.
- There is no downside case (`GEN-13`), in a category `01` rates High risk, at a return above that category's target range.
- The fee stack hits `02`'s aggressive test, and at least 300 bps/yr is paid regardless of outcome (`GEN-06`, `GEN-16`).
- The sponsor has never completed what it is asking to be paid to do (`GEN-14`).
- The headline figures cannot all be true.

Clearing VNQ plus the illiquidity premium on paper does not offset any of this.

**Biggest swing factor:** exit value at completion, meaning the exit cap the market actually pays on a project a first-time developer delivers on budget and on time. In the 🔴 illustration, compression alone moves the return about 650 bps, and a further 50 bps on the cap plus an overrun and a delay takes it from 25% to about 3%.

*Screening output only, not investment advice.*

**Who it could suit.** As it stands, no passive LP relying on this disclosure. Even fully documented, it would fit only an LP who can absorb a total loss of the check, needs no liquidity for 4+ years, and is deliberately taking first-time-developer risk for a commensurate price.

**What would have to be true to re-screen.** More disclosure alone is not enough, because the first-project fact does not go away.

*Disclosure:*
1. A reconciled headline, stated net to LP, with a distribution schedule
2. Entitlement and permit status
3. Budget with contingency in the 5–10% range
4. Full debt terms, including maturity, extensions, any rate cap and takeout
5. Absorption and exit comps, plus the exit cap vs today's market cap
6. Complete fee schedule with bases and recipients, and the full waterfall
7. Downside case showing LP capital survives a higher exit cap, an overrun and a delay

*Structure:*
8. A verifiable development track record brought in through a named, experienced development partner with real responsibility, since the sponsor cannot supply one itself
9. Meaningful cash co-invest on pari-passu terms
10. Fees reduced or restructured: one development-level fee rather than two, with part deferred until completion or LP capital return
11. A cumulative pref at or above 6%, with promote behind it

If items 1–7 come back clean but 8 does not, this remains a Pass on the merits.
