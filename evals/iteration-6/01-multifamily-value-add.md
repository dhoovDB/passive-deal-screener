# Eval fixture 01
*Iteration-6 run, 2026-11-01, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 436a76b.*

# Passive Deal Screen: Sun Belt Value-Add Multifamily, 280 Units

**Verdict: Pass.** This is a financing story: the headline needs a sale at a 5.0% cap, below the 5.5% going-in cap and below the 10-year Treasury, on floating bridge debt, from a sponsor whose 30% record is unverified.

*Screening output only, not investment advice.*

Confidence tags: 🟢 stated or from a reference, 🟡 inferred, 🔴 assumed or unverifiable.

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Multifamily, value-add 🟢 |
| Deal type | Equity syndication 🟢. "Bridge" here is the property's loan, so the hard-money flags do not apply. |
| Sponsor | Not stated |
| Geography | "Sun Belt" only. Metro and submarket not stated. |
| Minimum investment | Not stated |
| Hold | 5 years 🟢 (`01` norm is 5–7) |
| Raise | $50M equity, 280 units 🟢, or **$178,571 of equity per door before any debt** |
| Claimed return | 16% IRR, 2.0x 🟢. **Not stated whether gross or net to LP.** |
| Pref / promote | 8% / 20%, American (deal-by-deal) 🟢. Catch-up, clawback and pref type not stated. |
| Cap rates | 5.5% going-in, 5.0% exit 🟢 |
| Debt | Bridge, floating 🟢. Amount, LTV, maturity, extensions, spread and rate cap not stated. |
| Fees | 2% acquisition, 1.5% annual asset management, 1% disposition 🟢. Fee bases not stated. |
| Purchase price, renovation budget, rent-growth assumption | Not stated |
| Track record | "30% IRR across prior deals" 🟢 as a claim, 🔴 as a fact |

---

## 2. Return Stress-Test

**The swing assumptions** are exit cap, operating performance (rent and NOI), and the leverage that magnifies both. Leverage is undisclosed, so the table shows two versions.

- **No-debt floor (🟡):** the smallest possible damage. It is not a real case, because the deal has debt, but it needs no assumption about leverage.
- **50–70% debt (🔴):** illustrative only. No flag or verdict below relies on this column.

All figures start from the sponsor's 16% / 2.0x, read as gross. Net figures show the range from a 100% catch-up to no catch-up.

| Case | Assumptions | No-debt floor: gross | No-debt floor: net to LP | 50–70% debt 🔴: gross | 50–70% debt 🔴: net to LP |
|---|---|---|---|---|---|
| **Bull** (sponsor case) | 5.0% exit, plan NOI, plan distributions | 16.0% / 2.00x | 11.4–12.3% | 16.0% / 2.00x | 11.4–12.3% |
| **Base** (flat cap) | 5.5% exit, plan NOI, plan distributions | 14.0% / 1.84x | 9.7–10.7% | 11.2–12.8% / 1.63–1.75x | 7.2–9.7% |
| **Bear** | 6.0% exit, exit NOI 5% under plan, distributions halved | 8.9% / 1.51x | 5.2–6.4% | 0.4–5.6% / 1.02–1.30x | −1.7–3.5% |

If exit NOI falls 10% under plan instead of 5%, the bear case at 70% debt is 0.85x gross 🔴, which is a loss of LP capital. No case above adds a separate hit for higher floating-rate interest, so they may flatter the real downside.

**Against the public hurdle** (5-year lock-up, so `05` requires about 300–400 bps over the comparator):

| Net-to-LP case | Over VNQ (4.92%) | Script read | Over 10-yr Treasury (5.18%) |
|---|---|---|---|
| 16.0%, only if the headline is already net | +1,108 bps | Clears comfortably | +1,082 bps |
| 11.4–12.3%, sponsor case read as gross | +644–739 bps | Clears comfortably | +618–713 bps |
| 9.7–10.7%, flat cap, no-debt floor 🟡 | +473–574 bps | Clears comfortably | +447–548 bps |
| 8.6%, flat cap, 50% debt, full catch-up 🔴 | +370 bps | Clears, thin | +344 bps |
| 7.2%, flat cap, 70% debt, full catch-up 🔴 | +225 bps | Thin / fails | +199 bps |
| 3.5%, bear, 50% debt, full catch-up 🔴 | −143 bps | Fails | −169 bps |

**What this means:**

- **The lock-up is paid only while the exit assumption holds.** The Treasury is the tighter floor at this snapshot, so the practical bar is about **8.2–9.2% net**. With real leverage, the flat-cap case falls toward or through that bar.
- **The category norm is a tougher test.** Even the no-debt flat-cap floor (9.7–10.7%, or up to 11.7% on the dollar cross-check in §4) sits below the 12–15% that `01` gives as realized for value-add multifamily. 🟡
- **The sponsor case itself is below target if 16% is gross.** It lands under the 14–18% marketed net target in `01`.
- **If 16% really is net,** the deal must earn about 20–21% gross to deliver it. That is a more aggressive plan, not a safer one, and the flat-cap hit still applies.
- **Dispersion:** value-added funds show a 12.4% median net IRR and a 12.2-point interquartile range (2001–2017 vintages, `05` / Preqin note, a pattern rather than a live benchmark). A single asset adds concentration that VNQ's basket does not carry.
- **Liquid alternative:** SPY's trailing 10 years returned 15.39%. That was an exceptional decade and is no forward promise, but this deal owes a diversification or downside-protection reason, and none is offered.

Benchmark data: ETF returns to 2026-06-30, Treasury closes of 2026-09-24.

---

## 3. Where LP Returns Come From

**Exit dependence: fires at more than 60% (`GEN-08`).** 🟡

- A 2.0x with no interim cash is a 14.87% IRR. So the extra 1.13 points in the sponsor's 16% is all the interim cash there can be, and it is not much.
- With level distributions, the pair implies about **5.35% a year ($2.67M), then 1.73x ($86.6M) at sale**.
- That puts **73% of profit dollars and 82.5% of present value in the sale**.
- This does not depend on the distribution shape. Across every one-payment pattern tested (years 1–4), the sale is 65–89% of present value.
- The only way to bring the sale below 60% of profit dollars is about 0.63x paid out around year 4. That is a capital event such as a refinance, not operating cash flow, and it would fire `EQUITY-07` instead.

**Cap-rate compression: the stated assumption is doing real work (`EQUITY-06`).** 🟢

- Going from 5.5% to 5.0% adds **10% to the sale price** at the same NOI.
- To reach the same price at a flat 5.5% cap, the deal needs **10% more NOI at exit**, about 1.9 points more growth every year. At a 6.0% exit it needs 20% more, about 3.7 points a year.
- Compression accounts for at least 196 bps of the 16% with no debt 🟡, and 316–484 bps at 50–70% debt 🔴.

**Exit pricing against risk-free rates.** 🟡

- The underwritten 5.0% exit cap is **18 bps below the 10-year Treasury** (5.18%).
- The 5.5% going-in cap is only 32 bps above it.
- The plan therefore assumes that a buyer in year 5 accepts a starting yield below today's risk-free rate. That can happen only if rates fall or buyers pay heavily for growth. It is a rate bet, and nothing offered supports it.

**Leverage against the unlevered baseline (`GEN-07`).** 🟡

- NCREIF NPI, unlevered, returned 5.00% over the four quarters to Q2 2026, almost all income. Residential returned 5.3% in 2025.
- So about **11 of the 16 points** must come from leverage, assumed appreciation and the renovation lift.
- A rough build-up: 5.5 points in-place yield, about 1.9 points compression, leaving about 8.6 points for renovation NOI growth and leverage together.
- **I can't split that 8.6 from what's disclosed.** The renovation plan is a real operating thesis, so some of it may be earned. Until Q-DS-02 is answered, this reads as a financing story, because no unlevered figure has been offered and the stated exit cap and bridge debt both point that way.

**Thin current income, and what it does to the pref.** 🟡

- The bridge loan's base rate is floating. Using the 3-month Treasury (4.24%) as a proxy leaves about **126 bps of spread** before the loan's interest rate exceeds the 5.5% going-in yield. The actual spread is not stated. Past that point, leverage cuts current income instead of adding to it.
- The implied 5.35% a year is below the 8% pref. About **2.65 points a year, or about $6.6M over the hold, would go unpaid and accrue**. Whether the pref is cumulative is therefore a live economic question (`EQUITY-05`), not fine print.

---

## 4. Fee Stack Summary

**Total gross-to-net drag: about 464 bps a year**, taking 16% gross to about **11.4% net** (full catch-up). 🟡 It is 369 bps and 12.3% net with no catch-up. Catch-up is undisclosed, so the 100% case is an assumption (§6). Undisclosed fees are entered at 0, so this total covers only the fees shown.

| Fee | Stated | `02` norm | Read | Drag |
|---|---|---|---|---|
| Acquisition | 2%, base not stated | 1–2% of equity, or 0.5–1.5% of price; aggressive above 2.5% of equity or 2% of price | In range on equity ($1.0M). **Above range and at the aggressive line if on price.** | 40 bps |
| Asset management | 1.5% a year, base not stated | 1–2% of equity, annual | In range ($750K a year, $3.75M over the hold, on equity) | 150 bps |
| Disposition | 1%, base not stated | 0.5–1% of sale price | Top of range. Check it does not double up with brokerage. | 20 bps |
| Promote | 20% over 8% | 15–30% over 6–10% | In range | 254 bps (159 with no catch-up) |
| Loan placement / refinance | Not stated | 0.5–1.5% of loan / 0.5–1% of new loan | Likely relevant: bridge debt needs a takeout | Not counted |
| Construction management | Not stated | 3–5% of hard costs | Possible on a renovation plan | Not counted |
| Admin / IR | Not stated | 0.1–0.5% of equity, or $1–3K per LP | 0.3% would add 30 bps a year | Not counted |
| Affiliate property management | Not stated | Test is disclosure and benchmarking (`GEN-06`) | Unknown | Not counted |
| Feeder wrapper, if any | Not stated | Adds 50–150 bps a year | Unknown | Not counted |

**The headline fees are market. The problem is what is missing, chiefly the fee bases:**

- **Fee base sensitivity.** If acquisition is 2% of price and disposition is 1% of sale price, at 65% debt 🔴 they equal about 5.7% and 3.6% of equity. Total drag becomes **590 bps and net falls to 10.1%**.
- **Dollar cross-check on a 2.0x gross.** Fees on the equity basis total $5.25M, or 10.5% of equity. The promote at plan is $4.95M to $8.95M. That leaves the LP **1.72–1.80x**, not 2.0x.
- **The calculator is conservative.** It models a single payment at exit and adds drags together. Those multiples are 11.4–12.4% with no interim cash and 12.4–13.4% on the implied level distributions, so the true sponsor-case net is about **11.4–13.4%**. The flat-cap floor on the same basis is 9.7–11.7%. Both remain below the marketed net target, and the flat-cap floor remains below the realized band.

---

## 5. Red Flags

**RED, fired**

| ID | Flag | Mechanism and LP exposure | Conf. |
|---|---|---|---|
| `EQUITY-06` | Exit cap below going-in | 5.0% against 5.5% bakes a 10% price gain into the sale. The LP pays for a market move, not for the plan. | 🟢 |
| `GEN-08` | Exit-dependent IRR | 65–89% of present value is in the sale on every shape tested. The LP is underwriting one transaction in year 5. | 🟡 |
| `GEN-07` | Financing story | About 11 of 16 points sit above the 5% unlevered baseline, no unlevered return is offered, and compression plus bridge debt carry the case. | 🟡 |
| `GEN-05`, `GEN-14` | IRR basis unstated, no realized exits cited | "30% across prior deals" does not say net-to-LP or realized. Together these are a RED cluster: no validated LP outcome data at all. | 🟢 absent, 🟡 read |
| `GEN-09` | Debt maturity inside the plan | Maturity is undisclosed, but bridge debt is interim financing and the hold is 5 years. The likely result is a refinance or sale at maturity, into whatever market exists. Comes off only if the term with extensions reaches year 5 and the extension tests are realistic. | 🟡 |

**YELLOW–RED, treated as RED until answered**

| ID | Flag | Mechanism and LP exposure | Conf. |
|---|---|---|---|
| `EQUITY-07` | Refi-dependent plan | Bridge debt needs a takeout. If the refinance sizes short, the gap falls on equity through a capital call, dilution or a forced sale. | 🟡 |
| `GEN-15` | Missing financials (`GEN-12` subsumed) | No rent roll, no T-12 of any length, no complete debt terms. The rent thesis can't be tested. | 🟢 |
| `GEN-16` | Partial fee and waterfall disclosure | Headline rates are given. Bases, catch-up, clawback, pref type and financing fees are not, and net can only be bracketed. | 🟢 |

**YELLOW, fired**

| ID | Flag | Mechanism and LP exposure | Conf. |
|---|---|---|---|
| `GEN-11` | No distribution schedule | IRR with no timing. The implied shape is back-loaded and pays below the pref. | 🟢 |
| `GEN-13` | No downside case | A single-point pro forma hides how the deal behaves at a flat or higher exit cap. | 🟢 |
| `GEN-17` | Category disclosures absent | Exit-cap sensitivity, refi assumptions and prior multifamily exits, per `01`. | 🟢 |
| `GEN-18` | Rent thesis with no submarket support | The plan is to raise rents, but no submarket, supply pipeline or growth rate is given. "Sun Belt" is a region, and a local pipeline can turn rent growth negative. | 🟡 |

**Open: must-ask, not fired (depends on undisclosed facts)**

| ID | Item | Why it is not fired | Exposure if confirmed |
|---|---|---|---|
| `GEN-10` | Rate cap expiry | Floating rate is stated. Cap existence, strike and expiry are not. | **The 2022–24 pattern:** the cap expires before takeout, rates stay high, the refinance freezes, debt service erases distributions, and a capital call follows. RED. |
| `EQUITY-01` | American waterfall with high promote | 20% is not high by `02`, and 280 units reads as one asset 🟡, so there are no later deals to net against. `03` makes this RED only with a high promote and no clawback. | Bites if the vehicle holds more than one property. Ask why a one-asset deal carries this label at all. |
| `EQUITY-02` | No clawback | Not disclosed either way. On one asset, exposure narrows to promote paid on a mid-hold capital event, followed by a weak sale. | LP cannot recover that promote. |
| `EQUITY-03` | 100% catch-up | Not stated. | Costs about 95 bps of LP net against no catch-up. |
| `EQUITY-05` | Non-cumulative or simple-only pref | Not stated. | About $6.6M of implied unpaid pref would be at stake. |
| `GEN-06` | Affiliate fee stacking | Affiliates not disclosed. | Layered fees regardless of LP return. |
| `GEN-01`, `GEN-02` | Co-invest, regulatory history | Not disclosed. | See §7 and §9. |

**Checked and clean:** `EQUITY-04` does not fire, since the 8% pref is within the 6–10% norm. The headline promote and fee rates are in range.

**Clusters:**

- `GEN-07` + `GEN-08` + `EQUITY-06` is the **financing story**.
- `GEN-09` + `GEN-10` + `EQUITY-07` is the connected **bridge-maturity failure path**.
- `GEN-05` + `GEN-14` means **no validated track record**.

---

## 6. Missing Disclosures

**Essential for value-add multifamily (`01`):**

- Rent roll
- T-12 actuals
- Exit-cap sensitivity (the cap is stated; the sensitivity is not)
- Debt structure and maturity (only "bridge, floating" is given)
- Refinance assumptions
- GP record on prior multifamily **exits**

**Needed to calculate the return (`02`):**

- Whether 16% / 2.0x is gross or net to LP
- Base for each fee: equity or asset value
- Catch-up rate (**assumed in §4 at 100%, and at 0% for the range**)
- Pref terms: cumulative, compounding or simple
- Clawback
- Loan placement, refinance, construction management, admin and affiliate fees (**entered at 0**)
- Any feeder or wrapper layer

**Also absent:**

- Sponsor identity, minimum investment, metro and submarket
- Distribution schedule, capital-call terms, GP co-invest
- Leverage, spread, rate cap terms and the debt's maturity and extensions
- Rent-growth assumption and post-renovation rent premium
- **Purchase price and sources and uses**

**Why the purchase price matters here.** The stated figures need reconciling. Equity alone is $178,571 per door. Each debt level below is 🔴, but the arithmetic is fixed:

| Debt share of cost 🔴 | All-in cost per door | In-place NOI per door at 5.5% | Exit price per door implied by the plan |
|---|---|---|---|
| 50% | $357K | $19.6K | $488K |
| 60% | $446K | $24.6K | $577K |
| 70% | $595K | $32.7K | $726K |

The references hold no per-door norm, so this is not a flag. It is a test to run against the rent roll and sale comps. Either leverage is low for a bridge deal, or the price per door is high, or much of the $50M is funding something other than the asset. Each answer changes the deal.

---

## 7. GP Alignment

- **Co-invest:** Not stated. 🔴 Fixed fees total about $5.25M on the equity basis, paid whatever the LP earns. A co-invest under about $1.0M would be covered by the acquisition fee alone, which is no real capital at risk. 🟡 Ask for cash, pari passu, in dollars (`GEN-01`).
- **Track record:** **Unverified.** "30% IRR" names no basis, no realized or unrealized split, no deal count and no vintages (`GEN-05`, `GEN-14`). 🟢
  - It sits far above the 12–15% realized norm for the category (`01`) and the 12.4% value-added median (Preqin note).
  - Dispersion that wide means a selectively presented record says little.
  - If 30% were a real net-to-LP realized figure, it would also be worth asking why this deal is underwritten to only 16%. I can't tell from this what explains the gap.
- **Waterfall alignment:** 8% over 20% is market. 🟢 The promote pays after the pref, which aligns the GP, but only at the sale on the implied shape. That gives the GP a reason to favor the exit timing and assumptions that crystallize it.
- **Affiliate fees:** Not disclosed (`GEN-06`). 🔴

---

## 8. Questions for the GP

**Send these five first. They decide whether to reopen.**

| Question | ID (flag) | Bad-answer signal |
|---|---|---|
| Is 16% / 2.0x gross or net to LP? Give me the complete fee schedule with the base for each fee, and the full waterfall. | Q-FEE-01 (`GEN-16`) | "Standard market fees"; "the PPM has it" without producing it. |
| Why is the exit cap below going-in, and what is the IRR at 5.5% and 6.0%? | Q-EXIT-01 (`EQUITY-06`) | "Cap rates will compress"; no sensitivity; the IRR breaks at a flat cap. |
| When does the debt mature relative to the 5-year hold, and what is the refinance or extension plan? | Q-RISK-01 (`GEN-09`) | "We'll refinance" with no terms; no plan if the refi market shuts. |
| When does the rate cap expire relative to maturity, and what would it cost to extend at current pricing? | Q-RISK-02 (`GEN-10`) | Cap expires before maturity; extension cost not modeled; "rates should be lower by then." |
| Restate your track record as net-to-LP IRR on fully realized, exited deals only. | Q-GP-02 (`GEN-05`, `GEN-14`) | Only project-level or GP-level IRR; "most deals are still performing"; can't separate realized from marked. |

**Remaining must-asks**

| Question | ID (flag) | Bad-answer signal |
|---|---|---|
| What share of LP IRR comes from cash flow versus the exit? | Q-DS-01 (`GEN-08`, `EQUITY-06`) | Won't decompose it; "real estate always appreciates"; falls below the pref at a flat cap. |
| Strip out leverage and compression: what is the unlevered, in-place return? | Q-DS-02 (`GEN-07`) | No unlevered view exists; "leverage is just how the deal works." |
| What is the return with flat rents, a higher exit cap and no refinance? | Q-DS-03 (`GEN-13`) | "We underwrite conservatively" with nothing to show; the "bear case" is still a gain. |
| Does the plan depend on a refinance, and what happens to distributions if it isn't available? | Q-EXIT-02 (`EQUITY-07`) | Capital return needs a refi at lower rates; "the refi market will reopen." |
| Provide T-12, rent roll, complete debt terms, and (added here) sources and uses with the purchase price. | Q-RISK-03 (`GEN-15`, `GEN-12`) | T-3 or T-6 only; "financials are confidential until you commit." |
| Is the waterfall truly deal-by-deal on one asset, is there a clawback, and what is the catch-up? | Q-FEE-03 (`EQUITY-01`, `EQUITY-02`; catch-up: `EQUITY-03`) | No clawback and can't explain the catch-up; "you get paid when we get paid." |
| Is the 8% pref cumulative and compounding, and is it paid currently or accrued? | Q-FEE-04 (`EQUITY-05`; `EQUITY-04` clean) | Non-cumulative; vague on how shortfalls are treated. |
| Which providers are GP-affiliated, what do they charge, and are the rates benchmarked? | Q-FEE-02 (`GEN-06`) | "All arm's-length" without naming anyone. |
| How much of your own cash is in this deal, on LP terms? | Q-GP-01 (`GEN-01`) | "Sweat equity"; a fee waiver instead of cash; a token amount on better terms. |
| Any regulatory action, enforcement or investor litigation? | Q-GP-03 (`GEN-02`) | "Nothing material"; a search finds what they did not mention. |
| What is the distribution schedule, and what starts capital returning? | Q-DIST-01 (`GEN-11`) | "We'll distribute when the deal supports it." |
| What submarket supply and absorption data support the rent growth? | Q-MKT-01 (`GEN-18`) | Metro optimism instead of submarket data; no pipeline acknowledged. |
| What are my options if I need out before year 5? | Q-LIQ-01 | "A secondary market may develop." An honest "none" is a good answer. |

**Nice-to-ask**

| Question | ID | Bad-answer signal |
|---|---|---|
| When are capital calls expected, and what follows a missed call? This matters more than usual given the bridge path. | Q-DIST-02 | "Calls as needed"; punitive dilution buried in the documents. |
| How has team and monitoring capacity grown with AUM? | Q-GP-04 (`GEN-04`, not fired) | "Lean and efficient" as the whole answer; no named asset manager. |
| When are K-1s delivered, and have they been on time? | Q-LIQ-02 | "As soon as we can"; a history of extensions. |

---

## 9. Diligence Checklist

Third-party checks, only worth running if the deal reopens:

- [ ] **PPM and operating agreement:** waterfall, pref type, catch-up, clawback, fee bases, capital-call and dilution terms, GP removal rights.
- [ ] **Lender documents:** term sheet and loan agreement for amount, spread, maturity, extension tests, and rate cap strike, expiry and replacement cost.
- [ ] **Background and regulatory:** SEC, FINRA and state records, litigation search on principals, independent of the GP's answer.
- [ ] **Track record:** distribution records or statements from LPs in exited deals, tied to net-to-LP figures.
- [ ] **Comps and appraisal:** cap rates and price per door on recent sales in the submarket, tested against both the 5.5% entry and the 5.0% exit.
- [ ] **Financials:** rent roll and T-12 tied to the 5.5% going-in NOI, so the cap rate is on actual income rather than pro forma.
- [ ] **Market:** independent submarket supply pipeline, absorption and rent data.
- [ ] **Current benchmarks:** refresh the Treasury and comparator figures, which date from September and June 2026.

---

## 10. Verdict

**Pass.**

*Screening output only, not investment advice.*

**This is a merits verdict, not an insufficient-disclosure one.** The gaps are large, but the return story is disclosed well enough to judge: the stated caps, debt type, return pair, fees and promote already show how the headline is built. It is a **financing story** (`GEN-07` + `GEN-08` + `EQUITY-06`).

**The reasoning, on stated and inferred facts only:**

1. **The return is mostly one sale.** 65–89% of present value is in the exit, at a cap 50 bps below entry and 18 bps below the 10-year Treasury.
2. **Remove the compression and the LP result misses the category.** At a flat cap, even with no debt, net is 9.7–11.7%, below the 12–15% realized norm. The real deal has debt, so it will be lower.
3. **The debt adds a separate way to lose.** Floating bridge debt on a 5-year hold points to a takeout at or before maturity (`GEN-09`, `EQUITY-07`), with cap terms unknown (`GEN-10`). Thin current income leaves little cushion, and equity is what absorbs a short refinance.
4. **The sponsor gives no verified reason to trust the plan.** The 30% figure is unverified (`GEN-05`, `GEN-14`).

**In fairness:** the headline fees, 8% pref and 20% promote are market, and the renovation plan is a real operating thesis. The sponsor case does clear the public hurdle. The Pass rests on the underwriting and the debt, not the terms.

**Biggest swing factor: the exit cap**, then whether 16% is gross or net.

**Who it suits:** an LP who has verified this sponsor independently, can hold past year 5 if the sale or refinance slips, can meet a capital call, and knowingly wants a concentrated bet on cap rates and floating-rate financing.

**What would have to be true to reopen:**

- The GP's own model shows **at least about 12% net to LP at an exit cap of 5.5% or higher**, which puts the flat-cap case inside the realized band and above the 8.2–9.2% hurdle.
- It also shows LP capital intact at a 6.0% exit with no refinance.
- The debt term, with realistic extensions, reaches the planned exit, and a rate cap or budgeted replacement covers the whole period.
- The sponsor documents realized, net-to-LP results on prior multifamily exits.
- The fee bases, catch-up and clawback are in writing, and the pref is cumulative.
- The purchase price and per-door figures reconcile to the rent roll and comps.

The first gate takes one email to test: ask for the 5.5% and 6.0% exit cases, net to LP.
