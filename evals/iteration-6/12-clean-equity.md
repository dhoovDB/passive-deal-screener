# Eval fixture 12
*Iteration-6 run, 2026-11-01, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 436a76b.*

**Verdict: Pursue.** Worth taking to full diligence: every term you listed protects the LP and no RED flag fires. The one thing still unproven is the return itself, because your summary gives no target IRR, hold period or leverage.

*Screening output only, not investment advice.*

Confidence tags: 🟢 stated by you or from a reference, 🟡 inferred, 🔴 assumed or unverifiable. "Stated" means stated in your summary. I have not seen the T-12, rent roll, sensitivity, track record or PPM.

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Multifamily, value-add 🟢 |
| Deal type | Equity syndication 🟢 |
| Sponsor | Not stated |
| Geography | Not stated |
| Minimum | Not stated |
| Hold | Not stated. A planned exit exists but no year is given; the category norm is 5–7 years 🟢 |
| Raise | Not stated |
| Claimed return | Not stated (no target IRR, multiple or cash-on-cash) |
| Co-invest | 10% of equity, cash, pari-passu 🟢 |
| Waterfall | Whole-of-fund, secured clawback, 8% cumulative compounding pref, 20% promote 🟢 |
| Fees | 1% acquisition, 1.5% asset management, 1% disposition 🟢; fee bases not stated |
| Debt | Fixed rate, matures two years after planned exit 🟢; leverage, rate, amortization and prepayment terms not stated |
| Exit cap | Equal to going-in 🟢; the cap rate itself not stated |

## 2. Return Stress-Test

No deal return was given, so I can't say whether this deal clears the lock-up. What I can give you is the bar it has to clear and the gross return needed to get there on these terms.

**The bar (net to LP).** 🟢 Comparator is VNQ at 4.92% (10-year trailing, to 2026-06-30), plus the illiquidity premium. The 10-year Treasury at 5.18% (2026-09-24) is currently the tighter floor, so both are shown.

| Lock-up | Premium required | Over VNQ | Over 10-yr Treasury |
|---|---|---|---|
| 5 years | ~300–400 bps | 7.9–8.9% | 8.2–9.2% |
| 7 years | ~400–600 bps | 8.9–10.9% | 9.2–11.2% |

**Scenarios.** 🔴 The gross IRRs below are my illustrations, not the deal's numbers. Net figures come from `fee_drag_calculator.py` on the stated fees with an assumed 100% catch-up, the conservative case. The comparator read comes from `benchmark_comparator.py`.

| Case | Swing assumptions | Gross | Net to LP (5–7 yr) | Over VNQ | Read |
|---|---|---|---|---|---|
| Bull | Rent growth beats plan; exit at flat cap | 18% | 13.3–13.8% | ≈840–880 bps | Clears comfortably |
| Base | Plan delivered; exit at flat cap | 15% | 10.7–11.0% | ≈580–610 bps | Clears comfortably |
| Soft | Rent growth short of plan; flat cap | 12% | 8.1–8.4% | ≈320–345 bps | Thin at 5 years, fails at 7 |
| Bear | Flat rents; exit cap above going-in; sale slips | Not computable | Not computable | n/a | Read it from the GP's sensitivity |

What this shows:

- **Gross return needed.** 🟡 On these terms the deal needs roughly 13–15% gross to clear the top of the bar (about 13% for a 5-year hold, about 15% for 7). Anything under about 12–13% gross is thin or fails.
- **Earning just the pref isn't enough.** 🟢 An 8% net return is about 308 bps over VNQ. That is thin for 5 years and fails for 7, so the pref protects your priority in the waterfall but doesn't pay for the lock-up on its own.
- **Category check.** 🟢 Value-add realized returns cluster at 12–15% net, against 14–18% targets. 🟡 On this stack a 12% net takes about 16–16.5% gross. Judge the deal's stated net target against that realized range, not the marketing range; a target well above 15% net needs a specific explanation.
- **Exit cap is the biggest swing.** 🟢 `01` names it the largest in most pro formas. 🔴 For scale only: at an assumed 5.5% going-in cap, a 100 bps rise cuts value about 15%, which at an assumed 60% LTV is about 38% of original equity before NOI growth and loan paydown. Going-in cap and LTV are the two numbers that replace these assumptions.
- **Flat is neutral, not conservative.** 🟡 Equal-to-going-in removes baked-in compression, which is what you want. It doesn't test expansion, so that test has to be in the sensitivity. Also compare the going-in cap with the 5.18% 10-year Treasury 🟢: the thinner that spread, the more a flat exit assumes about future buyers.
- **Necessary, not sufficient.** 🟢 Clearing the bar is the floor. Dispersion is wide across private real estate, and a single asset carries risk VNQ's basket diversifies away. Both raise the premium you should demand.

## 3. Where LP Returns Come From

Not decomposable from this disclosure, and that gap matters more than any term in the deal.

- **Cap compression: none underwritten.** 🟢 This removes the most common way a financing story gets built (`EQUITY-06`).
- **Leverage: unknown.** 🔴 NCREIF NPI, the unlevered private real estate baseline, returned 5.00% over the trailing four quarters (residential 5.3% for 2025), almost entirely income 🟢. If this deal projects 12–15% net, then roughly 7–10 points must come from leverage and value-add NOI growth 🟡. With a flat cap, sale value can only rise with NOI, so that gain is earned operationally, but leverage still sizes it. Whether this is an asset story or a financing story (`GEN-07`) depends on the unlevered return, which is a must-ask.
- **Exit share: unknown.** 🔴 A flat cap doesn't by itself keep the return under the 60% exit-dependence line (`GEN-08`), because value-add profit still arrives mostly at sale. Using category norms as a rough proxy (share of profit, not IRR): 2.0x over 5 years with 5% cash-on-cash puts about 75% at sale, while 1.75x over 7 years with 7% puts about 35%. This deal could land on either side, so the flag doesn't fire on what's stated. The GP's IRR split settles it.

## 4. Fee Stack Summary

**Total gross-to-net drag: ≈395 bps/yr** 🔴 (15% illustrative gross, 7-year hold, assumed 100% catch-up; undisclosed fees passed as 0). That takes 15.0% gross to about 11.0% net. Across holds and catch-up assumptions at 15% gross, the range is about 320–430 bps.

| Layer | Stated | `02` norm | Drag (7 yr) | Read |
|---|---|---|---|---|
| Asset management | 1.5% annual | 1–2% of equity | 150 bps | In range 🟢 |
| Acquisition | 1% one-time | 1–2% of equity or 0.5–1.5% of price | 14 bps | In range on either basis 🟢 |
| Disposition | 1% one-time | 0.5–1% of sale price; aggressive above 1.5% | 14 bps | Top of range if on sale price, not aggressive 🟢 |
| Promote | 20% over 8% pref | 15–30% over 6–10% | 217 bps | In range 🟢; drag depends on assumed gross and catch-up 🔴 |
| Catch-up | Not stated | Often 50–100% | Included above | 0% catch-up would cut promote drag to about 141 bps |
| Loan placement | Not stated | 0.5–1.5% of loan | 0 passed | Gap |
| Refinance | Not stated | 0.5–1% of new loan | 0 passed | Gap; likely n/a if there's no refi |
| Construction management | Not stated | 3–5% of hard costs | 0 passed | Gap; common on heavier value-add |
| Admin / IR | Not stated | 0.1–0.5% of equity or $1–3k per LP | 0 passed | Gap; would add about 10–50 bps |

Three points on reading that number:

- **The disclosed fee layer alone is 179–190 bps** (7- and 5-year holds), and this is the only part that doesn't depend on my gross assumption. "In line with market" holds up for the fees you listed. 🟢
- **Fee basis could add about 40–60 bps.** 🔴 The figures above treat the headline percentages as percent of equity. If acquisition is on purchase price and disposition on sale price, then at an assumed 60% LTV the one-time load is about 5% of equity rather than 2%. That is in-market, but it is not the same number.
- **Compounding pref.** The calculator models a simple pref. Compounding changes nothing under a 100% catch-up at these return levels. Under no catch-up it lowers promote drag by about 15–20 bps (my side calculation, not script output). 🟡

## 5. Red Flags

**RED: none fired.**

**YELLOW: one, and it's minor.**

- **`GEN-11` Distribution timing not disclosed.** 🟡 No distribution schedule appears in your summary. You can't tell whether capital comes back along the way or all at sale, and value-add typically back-loads, which concentrates your risk at the exit. It may well be in the package; if it is, this clears.

**Checked and cleared on stated facts** 🟢 (subject to the documents matching your summary):

| ID | Why it doesn't fire |
|---|---|
| `GEN-01` | 10% cash co-invest, pari-passu |
| `GEN-05`, `GEN-14` | Five fully-exited deals, net-to-LP IRRs |
| `EQUITY-01`, `EQUITY-02` | Whole-of-fund waterfall with a secured clawback |
| `EQUITY-04`, `EQUITY-05` | 8% pref, cumulative and compounding; better than the simple pref most deals use |
| `EQUITY-06` | Exit cap equals going-in, not below |
| `GEN-09` | Debt matures two years after planned exit |
| `GEN-10` | Fixed rate, so no rate cap to expire |
| `GEN-12`, `GEN-13`, `GEN-15` | Full T-12, rent roll and downside sensitivity provided (remaining debt terms still to come) |

**Can't be evaluated yet; not fired, each routed to a must-ask** 🔴:

| ID | What's unknown |
|---|---|
| `GEN-07`, `GEN-08` | Leverage and the exit share of IRR. The financing-story cluster (`GEN-07` + `GEN-08` + `EQUITY-06`) is not present on what's stated |
| `EQUITY-03` | Catch-up rate |
| `EQUITY-07` | No refi is mentioned and the debt term doesn't need one; confirm capital return doesn't rely on one |
| `GEN-06`, `GEN-16` | Affiliates and fee lines beyond the three listed. Fee and waterfall disclosure is substantial, so `GEN-16` doesn't fire |
| `GEN-02` | Regulatory and litigation history; sponsor not named |
| `GEN-18` | Rent-growth assumption and submarket supply; market not named |

**One non-flag to probe: the debt term has a cost.** 🟡 Fixed-rate debt running two years past the planned sale gives real cushion if the sale slips, which is why `GEN-09` clears. It also means a sale on plan may require prepaying a fixed-rate loan early, or having a buyer assume it. Yield maintenance or defeasance could come out of LP proceeds. Check that the model includes it, under `Q-RISK-01` and `Q-RISK-03`.

## 6. Missing Disclosures

**Essential disclosures per `01`: substantially present.** Rent roll, T-12, exit cap with sensitivity, debt maturity and realized exits are all accounted for. That is why this gets a merits verdict rather than an "insufficient disclosure" pass.

Omitted from your summary. Some of this may be in the package:

- **Return:** target net IRR, equity multiple, cash-on-cash, split of IRR between cash flow and exit.
- **Deal basics:** sponsor, market, minimum, raise, hold.
- **Single asset or portfolio:** a whole-of-fund waterfall on one asset works very differently from one across several. On one asset it gives little added protection, and the clawback matters mainly if promote is paid before final sale.
- **Debt:** LTV, rate, amortization or interest-only period, prepayment terms, whether anything sits behind the senior loan.
- **Exit:** the going-in cap rate itself, and what's in the sensitivity.
- **Fees:** bases for all three fees, catch-up rate, loan placement, construction management, admin/IR, and any affiliate fees. `02` treats an absent standard fee as a flag rather than a neutral silence: it is either rolled in elsewhere or not disclosed.
- **Distributions:** schedule and milestones (`GEN-11`).
- **Track record:** the five IRR figures, asset types, and exit years.
- **Liquidity:** transfer rights or any early-exit route.

## 7. GP Alignment

- **Co-invest: strong as stated.** 🟢 10% in cash, pari-passu, which is real capital at risk on LP terms. 🔴 Check the net figure: at an assumed 60% LTV, a 1% acquisition fee on price is about 2.5% of equity, which would come back to the GP at close and offset part of its 10%.
- **Track record: right form, unverified substance.** 🟢 Realized and net-to-LP is exactly the format to demand. 🔴 But I haven't seen the figures, and "disclosed" says nothing about whether they're good. Check four things: whether they beat the 12–15% category realized range; whether these five are all the GP's exits or a selection; whether they're multifamily exits (`01` asks for that specifically); and whether any exited during or after 2022–24 rather than only into falling cap rates.
- **Waterfall: well above retail norm.** 🟢 Whole-of-fund, secured clawback and compounding pref are each more LP-favorable than the typical syndication described in `02`. 🔴 What "secured" means (escrow, guarantee, holdback) is unverified, and the catch-up rate is open.
- **Affiliate fees: unknown.** 🔴 Each fee can be in range while the total through related parties isn't, so this needs naming (`GEN-06`).

## 8. Questions for the GP

**Must-ask**

| ID | Question | Bad-answer signal | `03` ref |
|---|---|---|---|
| `Q-DS-01` | What share of projected LP IRR comes from in-place cash flow versus the exit, and what's the IRR at a flat exit cap? | Can't or won't split it; "real estate always appreciates" | `GEN-08`, `EQUITY-06` |
| `Q-DS-02` | Strip out leverage and cap-rate compression: what is the unlevered, in-place return? | Levered IRR is the only figure; "leverage is just how the deal works" | `GEN-07` |
| `Q-DS-03` | What is the return under a bear case: flat rents, higher exit cap, no refinance? | "We underwrite conservatively"; the "bear case" still shows a healthy gain | `GEN-13` |
| `Q-EXIT-01` | Exit cap equals going-in, so what's the IRR at an exit cap above going-in? | No sensitivity above flat; IRR breaks with a small rise | `EQUITY-06` |
| `Q-EXIT-02` | Does the plan depend on a refinance at any point, and what happens to distributions if one isn't available? | Capital return quietly needs a refi; "the refi market will reopen" | `EQUITY-07` |
| `Q-RISK-01` | When exactly does the debt mature relative to the hold, what are the extension options, and what does it cost to prepay or assume the loan at the planned sale? | "We'll refinance" with no terms; prepayment cost not in the model | `GEN-09` |
| `Q-RISK-03` | Can you provide complete debt terms: LTV, rate, amortization, prepayment, along with the T-12 and rent roll? | "Confidential until you commit"; T-12 turns out to be a T-3 or T-6 | `GEN-12`, `GEN-15` |
| `Q-GP-01` | How much of your own capital is in this deal on LP terms, net of fees taken at close? | Co-invest turns out to be a fee waiver or rolled fees; better terms than LPs | `GEN-01` |
| `Q-GP-02` | Can you share net-to-LP IRRs on all fully-realized deals, including any losers, with exit dates? | Project-level figures substituted; "most deals are still performing"; no losers ever | `GEN-05`, `GEN-14` |
| `Q-GP-03` | Have you or your principals faced any regulatory action, enforcement, or investor litigation? | "Nothing material"; a search surfaces something undisclosed | `GEN-02` |
| `Q-FEE-01` | Can you provide the complete fee schedule, with the basis for each fee, and the full waterfall? | "Standard market fees"; "the PPM has it" without producing it | `GEN-16` |
| `Q-FEE-02` | Which service providers are GP-affiliated, what do they charge, and are those rates benchmarked? | "All arm's-length" with no names; no benchmark | `GEN-06` |
| `Q-FEE-03` | Is this one asset or several, how is the clawback secured, and what's the catch-up rate? | Can't explain the catch-up; "secured" turns out to be an unbacked promise; "you get paid when we get paid" | `EQUITY-01`, `EQUITY-02`, `EQUITY-03` |
| `Q-FEE-04` | Is the 8% pref cumulative and compounding in the operating agreement, on all unreturned capital? | Documents say simple or non-cumulative despite the summary | `EQUITY-04`, `EQUITY-05` |
| `Q-MKT-01` | What submarket supply pipeline and absorption data support the rent-growth assumption? | Metro headlines standing in for submarket data; "rents always go up here" | `GEN-18` |
| `Q-DIST-01` | What is the projected distribution schedule, and at what milestones does capital start returning? | "We'll distribute when the deal supports it"; an IRR with no timing | `GEN-11` |
| `Q-LIQ-01` | What are my options if I need to exit before the hold ends? | "A secondary market may develop." An honest "there is none" is a good answer | none |

**Nice-to-ask**

| ID | Question | Bad-answer signal | `03` ref |
|---|---|---|---|
| `Q-GP-04` | How have headcount and monitoring capacity grown alongside AUM? | "Lean and efficient" as the whole answer; no named asset manager | `GEN-04` |
| `Q-DIST-02` | When are capital calls expected, and what's the consequence of a missed call? | "Calls as needed"; punitive dilution buried in the documents | none |
| `Q-LIQ-02` | When are K-1s delivered, and have you historically met the filing deadline? | "As soon as we can"; a history of extensions | none |

Not applicable: `Q-RISK-02` (fixed rate; applies only if any floating piece exists in the stack), `Q-MKT-02` (not a variable class), `Q-RISK-04` to `Q-RISK-06` (debt funds).

## 9. Diligence Checklist

Third-party verification still needed:

- [ ] **PPM and operating agreement:** confirm the waterfall, compounding pref, clawback security, co-invest and full fee list match the summary. This is the top priority, since most of this screen rests on those terms being as described.
- [ ] **Counsel review** of the clawback's security and how it is enforced.
- [ ] **Background and regulatory:** SEC, FINRA and state records and litigation searches on the sponsor and principals.
- [ ] **Track record:** tie the five IRRs to LP distribution records or statements, ideally with a reference from an LP in one of those deals.
- [ ] **Financials:** confirm the T-12 is full actuals and ties to the rent roll and to the pro forma's starting NOI.
- [ ] **Comps:** independent sale comps for the going-in and exit cap, and rent comps for post-renovation rents.
- [ ] **Appraisal:** third-party value against purchase price.
- [ ] **Lender:** loan documents or term sheet confirming rate, term, amortization, prepayment and assumability.
- [ ] **Model:** rerun `fee_drag_calculator.py` and `benchmark_comparator.py` with the deal's actual gross IRR, net IRR and hold.

## 10. Verdict

**Pursue.** The test at this stage is whether the deal deserves more diligence, and it does.

*Screening output only, not investment advice.*

**Reasoning.** Alignment (10% cash, pari-passu), structure (whole-of-fund, secured clawback, compounding pref), fees (in range), track record format (realized, net-to-LP), debt (fixed, past the exit) and exit assumption (no compression) all land on the LP-protective side, and several beat the retail norm. No RED fired, and the one YELLOW is a schedule that may simply be in the package. The core disclosures exist, so the gaps here are next-step items rather than grounds to pass.

**Pursue isn't commit.** The strength found here is in the terms; a well-structured deal can still pay too little. Before capital goes in, these need to be resolved:

1. Base-case net IRR clears the bar: about 8–9% on a 5-year hold, about 9–11% on a 7-year hold.
2. The sensitivity shows LP capital surviving an exit cap above going-in, at the deal's actual leverage.
3. The five realized IRRs are good, complete and from multifamily.
4. The unlevered return and IRR split show operations, not leverage, doing the work (`GEN-07`, `GEN-08`).
5. The PPM matches this summary, including what "secured" means and the catch-up rate.

**Biggest swing factor:** the exit cap, and specifically what the LP keeps if it lands above going-in. Leverage, not yet disclosed, determines how hard that hits.

**Who it suits:** an LP who can leave capital locked for the full hold plus possible slippage (the debt term allows up to two extra years), has no need for early liquidity, and can size the position for single-sponsor concentration.

**What would change this to Pass:** a base case that needs well above the category's realized returns to clear the bar, a bear case that impairs capital at modest cap expansion, weak or selectively presented realized returns, or documents that don't match the summary.
