# Eval fixture 01
*Iteration-8 run, 2026-11-01, blind generation by fresh-context agent (model: Opus), against SKILL.md @ ef2a4f5 plus the one-line GEN-09 edit.*

**Verdict: Pursue with conditions. As presented this is a financing story: do not commit capital until the GP shows the return holds at a flat exit cap, on net-to-LP numbers, with the debt terms in hand.**
*Screening output only, not investment advice.*

Confidence tags: 🟢 stated or from a reference, 🟡 inferred, 🔴 assumed or unverifiable.

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Multifamily, value-add 🟢 |
| Deal type | Equity syndication (appears to be a single asset, 280 units) 🟡 |
| Sponsor | Not stated |
| Geography | Sun Belt; market and submarket Not stated |
| Minimum investment | Not stated |
| Hold | 5 years 🟢 (`01` norm: 5–7 years) |
| Raise | $50M equity 🟢, or $178,571 of equity per unit 🟡 |
| Purchase price, total capitalization, leverage | Not stated |
| Claimed return | 16% IRR / 2.0x equity multiple 🟢. Gross or net: Not stated |
| Waterfall | 8% pref, 20% promote, American (deal-by-deal) 🟢. Catch-up, clawback, cumulative or compounding: Not stated |
| Cap rates | Going-in 5.5%, underwritten exit 5.0% 🟢 |
| Debt | Bridge, floating rate 🟢. Amount, spread, maturity, extensions, rate cap: Not stated |
| Fees | 2% acquisition, 1.5% annual asset management, 1% disposition 🟢. Fee bases: Not stated |
| Track record | "30% IRR track record across prior deals" 🔴 unverified |

---

## 2. Return Stress-Test

**The sponsor's numbers are the bull case, not the base case.** They depend on the buyer in year 5 paying a lower cap rate than this deal is paying today. The swing assumptions are exit cap, NOI against plan, and debt cost, which shows up in distributions.

**How to read the table.** Leverage is undisclosed, so this is a mechanical back-solve from the sponsor's own 16% / 2.0x, not a property model. It assumes level distributions and tests three exit loan-to-value levels, all 🔴. Treat the direction as reliable and the point estimates as illustrative. "Net" runs each gross figure through `fee_drag_calculator.py`, with fees on the equity base and 100% catch-up assumed.

| Case | Exit cap | NOI vs plan | Distributions | Sale value vs sponsor case | Gross IRR / multiple at 50% / 60% / 70% exit LTV 🔴 | Net IRR if headline is gross, at 50% / 60% / 70% 🔴 |
|---|---|---|---|---|---|---|
| **Bull (sponsor case)** | 5.0% | On plan | 5.3%/yr | n/a | 16.0% / 2.0x at any LTV | 11.4% |
| **Base (flat cap)** | 5.5% | On plan | 5.3%/yr | −9.1% 🟢 | 11.9% / 1.69x; 10.8% / 1.61x; 8.8% / 1.48x | 7.8% / 6.9% / 5.2% |
| **Bear** | 6.0% | −10% | Halved, from unhedged debt cost or slower rents | −25% | 0.0% / 1.00x; −5.1% / 0.78x; −17.5% / 0.42x | −2.1% / −7.2% / −19.6% |

- **Upper bound with no debt at all, flat cap:** 14.0% gross, 1.84x, about 9.65% net. Even with zero leverage, removing the compression costs about 200 bps of gross IRR.
- **If the headline is already net to LP:** read the gross column as an approximate LP figure. It slightly understates the LP result, because the promote shrinks as returns fall.
- **Refi is not modeled.** The plan's reliance on one is undisclosed (`EQUITY-07`, `GEN-09`), and a forced sale or refi would make the bear case worse.

**Net-to-LP vs comparator** (`benchmark_comparator.py`, `05`). Comparator is VNQ at 4.92% (10yr). The 5-year lock-up hurdle is about 300–400 bps. I also show the 10yr Treasury at 5.18%, which `05` names as the tighter floor at this snapshot. That puts the all-in bar at about 8.2–9.2% net.

| Net-to-LP scenario | Net IRR | Over VNQ | Over 10yr Treasury | Read |
|---|---|---|---|---|
| Headline is net, sponsor case | 16.00% | 1,108 bps | 1,082 bps | Clears comfortably, on the sponsor's assumptions |
| Headline is gross, sponsor case | 11.36% | 644 bps | 618 bps | Clears comfortably, but sits below `01`'s realized 12–15% band |
| Headline is net, flat cap, 60% LTV 🔴 | ≈10.8% | 589 bps | 563 bps | Clears comfortably |
| Headline is gross, flat cap, no debt (upper bound) 🔴 | 9.65% | 473 bps | 447 bps | Clears comfortably |
| Headline is gross, flat cap, 50% LTV 🔴 | 7.83% | 291 bps | 265 bps | Thin / fails |
| Headline is gross, flat cap, 60% LTV 🔴 | 6.87% | 195 bps | 169 bps | Thin / fails |
| Bear, headline is gross, 60% LTV 🔴 | −7.18% | −1,210 bps | −1,236 bps | Fails outright |

**Does it clear the lock-up?** Only on the sponsor's assumptions can I say yes. 🟡 At a flat cap the answer depends on two undisclosed items, gross vs net and leverage. If the headline is gross and leverage is ordinary, the lock-up is not paid for.

Three more context points from `05`:
- Clearing the hurdle is necessary, not sufficient. Private-market dispersion is wide, and a single asset carries concentration that VNQ's basket diversifies away. Both raise the premium an LP should demand.
- SPY's trailing 10yr return is 15.39%. Only a true 16% net beats it, so at anything less the deal owes you a diversification rationale. That decade is not a forward promise either.
- REIT comparators are also weak: VNQ's trailing return sits below today's 10yr Treasury, which is why I check both.

---

## 3. Where LP Returns Come From

**Flagged: exit- and leverage-driven, over the 60% line.** (`GEN-08`, `GEN-07`, `EQUITY-06`)

**Exit dependence, from the sponsor's own numbers.** 🟡 A 2.0x with no interim cash over 5 years is only 14.87% IRR, so 16% implies some distributions. The stated pair limits how much:

| Distribution shape that reproduces 16% / 2.0x | Interim cash | Sale proceeds | Exit share of the $50M profit |
|---|---|---|---|
| Level, 5.3%/yr | 0.27x | 1.73x | **73%** |
| Most interim cash possible within `01`'s 5–8% cash-on-cash norm (1.8%, then 8%/yr) | 0.34x | 1.66x | **66%** |

To get the exit share under 60%, some year must pay more than `01`'s 8% ceiling. That means a refi or other capital event, which is leverage rather than operating cash flow (`EQUITY-07`). So this finding does not rest on an assumed distribution schedule. The GP's actual schedule can still confirm or rebut it (`Q-DS-01`, `Q-DIST-01`).

**Cap compression.**
- 🟢 Moving from 5.5% to 5.0% adds 10% to sale value at any given NOI, with no operating improvement.
- 🔴 In the back-solve, that compression accounts for about 16% of the $50M projected profit with no debt, then 31% / 39% / 53% at 50% / 60% / 70% exit LTV.
- 🟢 The 5.0% exit cap sits below the current 10yr Treasury (5.18%, 2026-09-24), and the 5.5% going-in cap is only 32 bps above it. That curve can change over 5 years, but the underwriting asks a future buyer to accept an initial yield below today's risk-free rate.

**Unlevered overlay** (`05`). 🟡 NCREIF NPI's unlevered return is about 5.00%, almost entirely income. Against a 16% claim, about 11 points must come from leverage plus assumed appreciation and NOI growth. Some of that may be genuine renovation value, but the deal gives no rent premium, renovation budget or NOI bridge, so the operating share can't be measured.

**Debt carry.** 🟡 The 3-month Treasury is 4.24%, used here as a proxy for the floating base rate. Any lender spread above about 126 bps puts the coupon above the 5.5% going-in yield, which would make leverage negative on in-place NOI at closing. Early distributions would then depend on renovation lift rather than in-place income. The actual spread is a must-ask.

**Rate exposure.** 🔴 At 60–70% loan-to-cost, debt is 1.5–2.3x equity. Each +100 bps unhedged would cost 1.5–2.3% of equity per year, against an implied distribution of only about 5.3%.

**The strongest counter-argument:** a renovated asset can reasonably trade tighter than the unrenovated one. That is the "specific, defensible thesis" `Q-EXIT-01` allows for, but the deal hasn't made the case, and it needs comps.

---

## 4. Fee Stack Summary

**Total gross-to-net drag: about 464 bps/yr**, taking 16.00% gross to 11.36% net. This assumes the 16% is gross and uses `fee_drag_calculator.py`.

| Fee | Stated | `02` range | Read | Drag |
|---|---|---|---|---|
| Acquisition | 2%, base Not stated | 1–2% of equity, or 0.5–1.5% of purchase price; aggressive above 2% of price | Top of range on equity. Above the typical range and at the aggressive line if on price | 40 bps |
| Asset management | 1.5%/yr, base Not stated | 1–2% of equity; aggressive above 2.5% | In range | 150 bps |
| Disposition | 1%, base Not stated | 0.5–1% of sale price; aggressive above 1.5% | Top of range. Check for double-charging with the broker | 20 bps |
| Promote | 20% over 8% pref | 15–30% over 6–10% | In range | 254 bps (100% catch-up assumed) |
| Loan placement, refinance, construction management, admin/IR | Not stated | See `02` | Passed as 0. Absence is a flag, not evidence of no fee | 0 in this total |

**Dollar view on the equity base:** $1.0M acquisition, plus $3.75M asset management over 5 years, plus $0.5M disposition, equals **$5.25M, or 10.5% of equity**. The GP collects this whether or not LPs make money.

**The figure could move for these reasons:**
- **Catch-up:** with no catch-up, drag falls to 369 bps and net rises to 12.31%. The real term is undisclosed.
- **Fee base:** 🔴 if acquisition and disposition run on price rather than equity, as `02` norms suggest for disposition, one-time fees grow with leverage. At the 60% case, drag is about 590 bps and net about 10.1%.
- **Undisclosed fees:** these only add to drag. Admin at `02`'s 0.1–0.5% would add 10–50 bps/yr. Loan placement at 0.5–1.5% of the loan would add about 15–45 bps/yr at 60% loan-to-cost 🔴.
- **If 16% is already net:** the property must earn about 21% gross, with drag near 525 bps. That is a much harder ask of the asset.
- **Model limits:** the calculator adds drags together and assumes a single payout at exit, which slightly overstates drag. It is a screening estimate, not a waterfall model.

---

## 5. Red Flags

**Cluster: `GEN-07` + `GEN-08` + `EQUITY-06` is a financing story.** A second RED cluster sits in the track record (`GEN-05` + `GEN-14`).

### RED

- **`EQUITY-06` Exit cap below going-in** 🟢. 5.0% exit vs 5.5% going-in builds unproven compression into the headline. LP exposure: a flat cap cuts sale value 9.1%, and leverage magnifies that on equity.
- **`GEN-08` Exit-dependent IRR** 🟡. About 66–73% of projected profit comes from the sale, across shapes consistent with `01`'s cash-on-cash norm. LP exposure: the return is a year-5 sale bet, and interim income doesn't cushion it.
- **`GEN-07` Financing story** 🟡. Stated compression, floating bridge debt, and about 11 points over the unlevered baseline, with no quantified operating case. LP exposure: the return breaks if rates stay high or credit tightens. The GP can rebut this with an unlevered, in-place number (`Q-DS-02`).
- **`GEN-05` GP-IRR vs LP-IRR divergence** 🟡. "30% IRR" isn't labeled net-to-LP. It is about twice the top of `01`'s realized 12–15% band, and nearly twice what this sponsor projects here. LP exposure: you would be underwriting the GP on a number that excludes the fees and promote you would pay. Treat as fired until restated.
- **`GEN-14` No realized exits cited** 🟡. No deal count, multiple, vintage or exit list. LP exposure: marks or a few short-hold wins could account for the entire figure. `03` treats this pairing with `GEN-05` as a RED cluster, so as stated the record gives no validated information about LP outcomes.

### YELLOW–RED (treated as RED until answered, per `03`)

- **`GEN-15` Missing financials** 🟢. No rent roll, no T-12 and no complete debt terms. LP exposure: the renovate-and-raise-rents thesis can't be tested against in-place rents. `GEN-12` can't be assessed until financials arrive.
- **`GEN-16` Partial fee and waterfall disclosure** 🟢. Headline rates and waterfall type are given, which is why I hold this at the lower end. Bases, catch-up, clawback and several fee categories are not. LP exposure: 369–590+ bps of drag depending on the answers.

### YELLOW

- **`EQUITY-01` Deal-by-deal waterfall** 🟢. Held at YELLOW on purpose: `03` makes it RED only with a high promote and no clawback, and 20% is mid-band. On what looks like a single asset, the classic harm of winners paying promote before later losers is limited. LP exposure: promote paid on interim or refi proceeds before the final sale.
- **`GEN-11` No distribution schedule** 🟢. An IRR is quoted with no schedule. LP exposure: renovation-period distributions may be thin, and return risk concentrates at exit.
- **`GEN-13` No sensitivity or downside case** 🟢. Nothing provided shows a bear case. LP exposure: fragility to the exit cap is hidden, and my table above is the only stress you have.
- **`GEN-17` Essential disclosures absent** 🟢. See §6, against the `01` value-add baseline.

### Open probes, not fired

These are real questions, but firing them would need facts the deal doesn't give.

- **`GEN-09` Debt maturity vs hold.** Hold is stated, this loan's maturity is not. Bridge as a type doesn't establish this loan's term. Probe via `Q-RISK-01`.
- **`GEN-10` Rate cap expiry.** The debt is floating, but no cap terms are disclosed. Probe via `Q-RISK-02`. The failure mode to rule out: cap expires, rates stay elevated, refi is frozen, debt service spikes and erases distributions, as in 2022–24.
- **`EQUITY-07` Refi dependence.** Unknown. Probe via `Q-EXIT-02`.
- **`EQUITY-02` Clawback.** Not disclosed. `02` treats absence in a deal-by-deal waterfall as a major flag, and it becomes RED if the answer is "none." Probe via `Q-FEE-03`.
- **`EQUITY-03` Catch-up rate.** Not disclosed; matters if 100%. Probe via `Q-FEE-03`.
- **`EQUITY-05` Pref type.** Cumulative and compounding not stated. Probe via `Q-FEE-04`.
- **`GEN-06` Affiliate fees.** Property management, construction management and loan placement providers not disclosed. Probe via `Q-FEE-02`.
- **`GEN-01` Co-investment.** Not stated. Probe via `Q-GP-01`.
- **`GEN-02` Regulatory or litigation history.** Sponsor unnamed. Probe via `Q-GP-03`.
- **`GEN-18` Rent growth vs supply.** The plan depends on raising rents, but "Sun Belt" names no submarket and no growth assumption is given. Probe via `Q-MKT-01`.

**Checked and clean:** `EQUITY-04` does not fire (8% pref, `02` norm 6–10%). The promote, the asset management fee and the hold are all within norms.

---

## 6. Missing Disclosures

**Against the `01` value-add baseline:**
- Rent roll
- T-12 actuals
- Exit cap sensitivity (`GEN-13`, `GEN-17`)
- Debt structure and maturity
- Refi assumptions
- GP record on prior multifamily **exits**, not just acquisitions

**Capital stack and return basis:**
- Whether 16% / 2.0x is gross or net to LP
- Purchase price and price per unit. $178,571 of equity per unit is high enough that any meaningful debt implies a large basis: about $446k per unit of total capitalization at 60% loan-to-cost and $595k at 70% 🔴. `01` has no per-unit norm, so this is a question for comps rather than a flag.
- Loan amount, spread, cap strike, cap term, cap cost, extension options, covenants
- Renovation budget and how it is funded, rent premium, NOI bridge, distribution schedule

**Against `02` (fees and waterfall):**
- Base for each fee
- Catch-up rate, split tiers above 80/20, clawback
- Pref: cumulative or not, compounding or simple
- Loan placement, refinance, construction management, admin/IR fees
- Any feeder or fund-of-funds layer (`02` expects 50–150 bps/yr more if present)

**ASSUMED in the math (not deal terms):** 100% catch-up in the 464 bps figure. Exit LTV and level distributions in the stress table.

**Also missing:** sponsor identity, minimum investment, specific market, co-invest, capital-call terms, LP liquidity terms.

---

## 7. GP Alignment

- **Co-invest:** Not stated. Cash vs fee waiver and pari-passu status unknown. 🔴
- **Track record:** **Unverified.** The "30% IRR" has no net-to-LP label, no realized-only basis, no deal count, no multiple and no vintage. Counting only realized, net-to-LP results, this deal has shown you no track record at all. It also doesn't reconcile with the sponsor's own 16% projection here. Either the prior deals were different in kind, or the 30% is measured differently. Ask which, and specifically how prior deals held through 2022–24. (`GEN-05`, `GEN-14`)
- **Waterfall alignment:** 8% pref and 20% promote are market. 🟢 The American structure pays promote per deal, and clawback is unknown. With a 100% catch-up, the GP would take a full 20% of profit in any outcome that clears the pref, so the pref would govern timing rather than the final split.
- **Fees vs promote:** at least $5.25M of fees are paid regardless of outcome. 🟡 In the bear case the GP still collects them while LP capital is impaired. That weakens alignment unless co-invest is meaningful.
- **Affiliate fees:** Not stated. Each fee can be in range while the total through related parties is the problem. (`GEN-06`)

---

## 8. Questions for the GP

### Must-ask

| Question (ID) | Flag | Bad-answer signal |
|---|---|---|
| **`Q-EXIT-01`** Why is the exit cap below going-in, and what's the IRR at an exit cap equal to or above going-in? | `EQUITY-06` | "Cap rates will compress"; IRR breaks at flat; no sensitivity offered |
| **`Q-DS-01`** What share of LP IRR comes from in-place cash flow vs exit, and what's the IRR at a flat cap? | `GEN-08`, `EQUITY-06` | Won't decompose; "real estate always appreciates"; IRR falls below pref at flat |
| **`Q-DS-02`** Strip out leverage and compression: what's the unlevered, in-place return? | `GEN-07` | Levered IRR is the only figure; "leverage is just how the deal works" |
| **`Q-DS-03`** What's the return with flat rents, a higher exit cap and no refi? | `GEN-13` | "We underwrite conservatively" with nothing to show; the bear case is still a gain |
| **`Q-GP-02`** Restate the track record as net-to-LP IRR on fully realized, exited deals only. | `GEN-05`, `GEN-14` | Project- or GP-level IRR only; "most deals are still performing"; can't separate realized from unrealized |
| **`Q-RISK-01`** When does the debt mature relative to the hold, and what's the refi or extension plan? | `GEN-09` | Maturity inside the hold; "we'll refinance" with no terms; no plan if the refi market is shut |
| **`Q-RISK-02`** When does the rate cap expire relative to maturity, and what does extending it cost today? | `GEN-10` | Cap expires before maturity; extension cost not modeled; "rates should be lower by then" |
| **`Q-EXIT-02`** Does the plan depend on a refi, and what happens to distributions if it isn't available? | `EQUITY-07` | Capital return needs a refi at lower rates; no fallback; "the refi market will reopen" |
| **`Q-RISK-03`** Provide T-12, the rent roll and complete debt terms. | `GEN-12`, `GEN-15` | T-3 or T-6 only; "confidential until you commit" |
| **`Q-FEE-01`** Provide the complete fee schedule, including each fee's base, and the full waterfall. Is 16% / 2.0x gross or net? | `GEN-16` | "Standard market fees"; "the PPM has it" without producing it; can't give a net figure |
| **`Q-FEE-03`** Deal-by-deal or whole-of-fund (confirm), what's the catch-up, and is there a clawback? | `EQUITY-01`, `EQUITY-02`, `EQUITY-03` | Can't explain the catch-up; no clawback; "you get paid when we get paid" |
| **`Q-FEE-04`** Is the 8% pref cumulative, and does it compound? | `EQUITY-05` | Non-cumulative; vague on carry-forward |
| **`Q-FEE-02`** Which providers are GP-affiliated, what do they charge, and is it benchmarked? | `GEN-06` | "All arm's-length" without naming providers; no benchmark |
| **`Q-GP-01`** How much of your own capital is in this deal, on the same terms as LPs? | `GEN-01` | "Sweat equity"; co-invest is a fee waiver; token amount on better terms |
| **`Q-GP-03`** Any regulatory action, enforcement or investor litigation? | `GEN-02` | "Nothing material"; blames the LP or regulator; a search surfaces something undisclosed |
| **`Q-MKT-01`** What submarket supply and absorption data support the rent growth? | `GEN-18` | Metro-level optimism; "rents always go up here"; no supply pipeline acknowledged |
| **`Q-DIST-01`** What's the distribution schedule, and when does LP capital start returning? | `GEN-11` | "When the deal supports it"; no milestones |
| **`Q-LIQ-01`** What are my options if I need out before year 5? | n/a | "A secondary market may develop." An honest "there is none" is a good answer |

### Nice-to-ask

| Question (ID) | Flag | Bad-answer signal |
|---|---|---|
| **`Q-GP-04`** How have headcount and monitoring grown alongside AUM? | `GEN-04` | "Lean and efficient" as the whole answer; no named asset manager |
| **`Q-DIST-02`** When are capital calls expected, and what happens on a missed call? | n/a | "Calls as needed"; punitive dilution buried in the docs. Matters more here: a floating-rate deal under stress is where calls appear |
| **`Q-LIQ-02`** When are K-1s delivered, and have they historically arrived before the deadline? | n/a | "As soon as we can"; a history of extensions |

---

## 9. Diligence Checklist

Third-party verification still needed:

- [ ] **PPM and operating agreement:** read the waterfall, catch-up, clawback, pref, all fee bases, capital-call and transfer terms directly.
- [ ] **Background and regulatory:** SEC, FINRA and state records on the sponsor and principals, plus a litigation search. Form ADV Part 2 if RIA-managed.
- [ ] **Track record:** exit-by-exit statements, and ideally references from LPs in prior deals, confirming realized net-to-LP returns.
- [ ] **Rent and sale comps:** independent evidence for the post-renovation rents, the price per unit, and any renovated-asset cap rate near 5.0%.
- [ ] **Appraisal:** third-party value against the purchase price.
- [ ] **Lender:** loan term sheet confirming balance, spread, maturity, extension tests and covenants, plus the rate-cap agreement confirming strike, expiry and replacement cost.
- [ ] **Financials:** rent roll and T-12 reconciled to bank statements or a third-party review.
- [ ] **Submarket data:** independent supply pipeline and absorption for the actual submarket.

---

## 10. Verdict

**Pursue with conditions. This is a financing story as presented.**
*Screening output only, not investment advice.*

**Reasoning.** The terms themselves are ordinary: the pref, promote, fees and hold are all within `01`/`02` norms. The problem is how the return is built. Three RED flags form one finding: a stated cap-rate compression (`EQUITY-06`), about two-thirds or more of profit arriving at sale (`GEN-08`), and no quantified operating case behind 11 points of return over the unlevered baseline (`GEN-07`), all on floating bridge debt with unknown cap and maturity terms. The track record can't support the deal either (`GEN-05`, `GEN-14`).

This gets a merits verdict rather than "insufficient disclosure" because the returns, waterfall, fees, cap rates and debt type are enough to judge the core story. The remaining gaps are conditions. I am not passing outright because the two numbers that would settle it, gross vs net and leverage, are undisclosed, and I won't decide on assumed leverage. One round of GP answers settles them cheaply.

**Biggest swing factor: the exit cap.** A move from 5.0% to 5.5% alone takes the deal from 16% to roughly 9–12% gross at 50–70% exit LTV 🔴. If the headline is gross, that likely falls below the lock-up hurdle.

**Conditions. Failing any one is a Pass:**
1. **Return basis:** the GP states gross vs net, and shows net-to-LP IRR at a **5.5% exit cap of at least about 9.2%** (10yr Treasury 5.18% plus the top of the 300–400 bps hurdle), or defends the 5.0% with renovated-asset comps.
2. **Debt:** full terms provided. Maturity with extensions reaches the planned exit, or there is a costed, refi-independent plan. The rate cap runs through the hold, or its extension cost is in the model.
3. **Downside:** a real bear case (flat rents, higher exit cap, no refi) shows how much LP capital survives and whether capital calls are likely.
4. **Track record:** restated as realized, net-to-LP, deal by deal, including multifamily exits and how deals held through 2022–24.
5. **Alignment:** cash co-invest on pari-passu terms; catch-up, clawback, pref type and affiliate fees in writing.
6. **Financials:** rent roll, T-12 and distribution schedule delivered, and consistent with the rent plan.

**Who it suits, if the conditions clear:** an LP with capital that can stay locked up for 5–7 years if the hold extends, no reliance on distributions, a position sized for a single-asset loss, and a preference for a return earned at sale. It does not suit anyone seeking income or anyone who would struggle with a capital call.

**What would have to be true:** the renovation creates enough NOI growth that the return clears the bar with no compression; the debt survives until the planned sale at the actual rate path; and the sponsor's realized net-to-LP record shows it has done this before and returned capital.
