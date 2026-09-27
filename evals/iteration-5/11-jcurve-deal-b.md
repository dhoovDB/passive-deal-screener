# Eval fixture 11 — J-curve pair, Deal B (all-at-exit) + A/B comparison
*Iteration-5 run, 2026-09-27, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 7712624.*

**Verdict — Deal B: Pass as presented (insufficient disclosure).** 100% of the return depends on one sale in Year 5 (🟢 stated). Nothing that sets the size of that sale is disclosed: basis, exit cap, leverage, debt maturity, sponsor, fees. **Comparison: the same 14% IRR is not the same deal.** On structure alone, Deal A is the stronger passive-LP position. Deal B carries all of its return risk, and all of the LP's capital, at a single exit date.

---

## Part 1 — Deal B screen

### 1. Deal Snapshot

| Field | Deal B |
|---|---|
| Asset class | Multifamily 🟢. Sub-type not stated. A 14% target and a sale-driven return look like **value-add** 🟡 (core/core-plus is cash-flow-driven per `01`, and this deal pays no cash flow) |
| Deal type | Equity syndication 🟡 (implied by "property sells"; not stated) |
| Sponsor | Not stated |
| Geography | Not stated |
| Minimum | Not stated |
| Hold | 5 years 🟢 ("sells in Year 5") |
| Raise | Not stated |
| Claimed return | 14% IRR 🟢. **Gross or net not stated** |
| Distributions | **None until sale.** 100% of the return comes at exit 🟢 |

### 2. Return Stress-Test

Only one exit-dependent cash flow exists, so the stress test is a stress test of that sale. The figures below are my arithmetic on $100 invested and a single Year-5 exit sized to the stated 14% IRR (terminal ≈ $192.5, 1.93x). They are 🟡 inference, because the deal gives no pro forma to test.

| Case | Swing assumption | LP IRR | Multiple |
|---|---|---|---|
| Bull | Exit value +10% | ≈16.2% | 2.12x |
| **Base (claimed)** | Exit as underwritten, Year 5 | **14.0%** | **1.93x** |
| Bear — price | Exit value −20% (exit cap widens / NOI misses) | ≈9.0% | 1.54x |
| Bear — timing | Same exit price, sale slips 2 years (no refi, frozen market) | ≈9.8% | 1.93x over 7 yrs |
| Severe | Exit value −50% | ≈−0.8% | 0.96x — **capital loss** |

**Swing assumptions:** (1) the **exit cap**, which is undisclosed and is the largest single swing in multifamily per `01`; (2) the **sale date**, which a zero-distribution deal cannot cushion; (3) **debt maturity or refi**, which is undisclosed. If the loan matures before Year 5, the "sale in Year 5" becomes a forced sale or refi on the loan's timetable (`GEN-09`).

**Benchmark (`05`, `scripts/benchmark_comparator.py`):**
- **If 14% is net-to-LP:** ≈908bps over VNQ (4.92% 10yr). The 5-year lock-up hurdle is ~300–400bps, so it **clears comfortably**. It is also ≈882bps over the 10yr Treasury (5.18%), the tighter floor at this snapshot.
- **If 14% is gross** and the deal carries the `02` illustrative equity stack (🔴 assumed, see §4): net ≈9.32%. That is ≈440bps over VNQ, which still clears the 300–400bps band but only just, and ≈414bps over the 10yr Treasury.
- Either way, clearing the spread is necessary, not sufficient. This is a single asset with a single binary-ish exit, which is the concentration amplifier `05` warns about. The premium is paying for a bet on one sale, not for a stream of income.

### 3. Where LP Returns Come From

| Source | Share of LP return |
|---|---|
| In-place cash flow distributed to LP | **0%** 🟢 |
| Exit / terminal value | **100%** 🟢 |
| Leverage | Unknown. Debt is undisclosed 🔴 |

- **Exit-dependent: 100% versus the 60% threshold, so `GEN-08` fires (RED) on a stated fact.** This is the extreme case of rule 3: the whole return is a future-sale bet.
- **Financing story: unassessable, and must-ask (`GEN-07`, `EQUITY-06`).** The `05` unlevered overlay puts institutional private RE at ~5.0% total return, almost all of it **income** (NCREIF NPI, trailing 4Q to Q2 2026: 1.17% income vs 0.12% appreciation in the latest quarter). Deal B distributes **none** of its income, yet projects 14%. The ~9-point gap between 14% and the ~5% unlevered baseline has to come from leverage, assumed appreciation or cap compression, or cash flow retained and recycled into the asset 🟡. Which of these it is decides whether this is an asset story or a financing story. Without the leverage and exit cap I will not call it either way.
- **Where does the operating cash flow go?** Stabilized multifamily value-add typically pays 5–8% cash-on-cash (`01`), and this deal pays zero for five years. Some combination is true: heavy renovation or lease-up consuming cash, debt service absorbing NOI (thin coverage), reserves being built, or the asset is effectively a development deal 🟡. Each answer implies a different risk profile. The GP has to say which (`Q-DIST-01`).

### 4. Fee Stack Summary

**Gross-to-net drag: not computable from disclosure. That is the finding (`GEN-16`).**

- With every undisclosed fee passed as `0` (`fee_drag_calculator.py`), the script returns 14.00% net and 0bps drag. That is a placeholder, not a result: it assumes a fee-free deal, which no equity syndication is (`02`).
- **Illustrative only (🔴 assumed):** if 14% is gross and the deal carries the `02` demo stack (2% acquisition, 1.5% annual AM, 1% disposition, 0.3% admin, 20% promote over an 8% pref, 100% catch-up) over the stated 5-year hold, **drag ≈ 468bps/yr** (180 recurring / 60 one-time / 228 promote), giving **net ≈ 9.32%**. Treat this as a §6 gap, not a fact.
- **Two fee mechanics bite harder in a zero-distribution structure** 🟡:
  - **Fees during the J-curve.** An annual AM fee on equity raised is paid out of property cash for five years while the LP receives nothing. The GP is paid throughout the hold, and the LP only at the end.
  - **Pref accrual is the LP's only time-value protection.** With no interim distributions, the pref accrues for the full five years. At an 8% pref, **simple** accrual is 40% of capital by Year 5; **compounding** is ≈46.9%. That 6.9-point gap goes straight to how early the GP reaches promote. Cumulative versus non-cumulative matters even more: a non-cumulative pref on a zero-distribution deal could be worth nothing (`EQUITY-05`, `EQUITY-04`).

### 5. Red Flags

**RED**
- **`GEN-08` — Exit-dependent IRR (100% from terminal value).** 🟢 Mechanism: the return is a single sale-price bet with no realized cash flow along the way. LP exposure: a 20% exit miss takes the IRR from 14% to ≈9%, and a 50% miss is a capital loss. → `Q-DS-01`.

**YELLOW–RED**
- **`GEN-16` — No fee or waterfall disclosure.** 🟢 Drag is unknowable, and gross versus net is not even stated. → `Q-FEE-01`.
- **`GEN-15` — Missing financials.** 🟢 No rent roll, no T-12, no debt terms. → `Q-RISK-03`.

**YELLOW**
- **`GEN-11` — J-curve / cash-flow timing.** 🟢 The *shape* is disclosed (nothing until sale), which is better than silence. But the risk this flag names is fully present, because the back-loaded deal "concentrates all return risk at the exit." No milestones and no gating conditions are given. → `Q-DIST-01`.
- **`GEN-13` — No sensitivity or downside case.** 🟢 A single-point 14%. → `Q-DS-03`.
- **`GEN-17` — Essential multifamily disclosures absent** (per `01`): rent roll, T-12, exit cap with sensitivity, debt structure and maturity, refi assumptions, GP prior multifamily *exits*. 🟢 → `Q-RISK-03`, `Q-EXIT-01`, `Q-GP-02`.

**Cluster.** `GEN-08` is confirmed. Its family members `GEN-07` (financing story) and `EQUITY-06` (exit cap below going-in) are **unassessed, not cleared**. If either confirms, this becomes the financing-story cluster, and a deal that is 100% exit-driven is the worst place for that cluster to land.

**Must-ask probes, not fired (they need a 🔴 assumption to fire):** `GEN-07` and `EQUITY-06` (leverage and exit cap unknown); `GEN-09`, `GEN-10`, `EQUITY-07` (debt maturity, rate cap, refi unknown; see the timing bear case in §2); `GEN-01` (co-invest); `GEN-05` and `GEN-14` (track record); `GEN-06` (affiliate fees); `EQUITY-01`, `EQUITY-02`, `EQUITY-03`, `EQUITY-04`, `EQUITY-05` (waterfall and pref terms); `GEN-18` (rent-growth assumption). These are conditions to resolve, not verdict drivers.

### 6. Missing Disclosures

Against the `01` multifamily baseline and the `02` equity-syndication fee inventory:

- Sponsor identity, geography/submarket, minimum, raise size
- **Gross versus net** basis of the 14% IRR
- Sub-type (value-add vs core) and the business plan that explains zero distributions
- Rent roll and **T-12 actuals**
- **Going-in cap, exit cap, and exit-cap sensitivity**
- **Debt:** amount/LTV, fixed or floating, rate cap and its expiry, **maturity relative to the Year-5 sale**, extension options
- Refi assumptions, if any
- Full fee schedule (acquisition, AM, disposition, financing, admin) and **waterfall** (pref rate, cumulative/compounding, catch-up, promote tiers, clawback)
- GP co-investment, and a **realized, net-to-LP** track record on prior multifamily exits
- Capital-call provisions (a deal with no distributable cash may also have no cushion)
- Liquidity / transfer provisions for a five-year, zero-cash lock-up

### 7. GP Alignment

**Unverified on every axis.** No co-invest, track record, waterfall, or affiliate disclosure 🔴.

One structural point comes from the stated shape 🟡. In a zero-distribution deal, recurring GP fees flow for five years while LP distributions are zero, and the GP's promote is settled in one event at the sale. Alignment therefore rests almost entirely on (a) a **cumulative, ideally compounding** pref that the GP must clear before promote, and (b) real **pari-passu co-invest**, so the GP also sits through the J-curve with its own cash. Neither is disclosed.

### 8. Questions for the GP

**Must-ask**

| ID | Question (as applied to Deal B) | Bad-answer signal |
|---|---|---|
| `Q-DIST-01` (`GEN-11`) | "Why are there no distributions for five years? Where does operating cash flow go, and at what milestone could distributions start?" | "We'll distribute when the deal supports it"; no milestones; can't say where the NOI goes |
| `Q-DS-01` (`GEN-08`, `EQUITY-06`) | "What's the IRR at a flat exit cap?" (the split is already 100% exit) | Won't produce a flat-cap IRR; "real estate always appreciates"; IRR falls below the pref at a flat cap |
| `Q-EXIT-01` (`EQUITY-06`) | "What are the going-in and exit caps, and what's the IRR at exit cap ≥ going-in?" | Exit cap below going-in, justified only by "cap rates will compress"; no sensitivity |
| `Q-DS-02` (`GEN-07`) | "Strip out leverage and cap-rate compression. What is the unlevered, in-place return?" | Only a levered IRR exists; "leverage is just how the deal works" |
| `Q-DS-03` (`GEN-13`) | "What's the return with flat rents, a higher exit cap, and the sale delayed two years?" | No downside case; "we underwrite conservatively" with nothing to show; the bear case is still a gain |
| `Q-RISK-01` (`GEN-09`) | "When does the debt mature relative to the Year-5 sale, and what are the extension terms?" | Maturity at or before Year 5; "we'll refinance" with no terms |
| `Q-RISK-02` (`GEN-10`) | "If the debt is floating, when does the rate cap expire, and what does extending it cost today?" | Cap expires before maturity; extension cost not modeled |
| `Q-EXIT-02` (`EQUITY-07`) | "If the sale market is shut in Year 5, does the plan need a refi, and on what terms?" | "The market will reopen"; no fallback |
| `Q-RISK-03` (`GEN-12`, `GEN-15`) | "Please provide the T-12, rent roll, and complete debt terms." | T-3/T-6 only; "confidential until you commit" |
| `Q-FEE-01` (`GEN-16`) | "Is 14% gross or net? Please send the complete fee schedule and waterfall." | "Standard market fees"; "the PPM has it" without producing it |
| `Q-FEE-04` (`EQUITY-04`, `EQUITY-05`), **escalated: this is the LP's only time-value protection here** | "What's the pref, and is it cumulative and compounding over the full five years with no distributions?" | Pref below 6% or none; non-cumulative; simple-only on a five-year accrual |
| `Q-FEE-03` (`EQUITY-01`, `EQUITY-02`) | "What catch-up and promote tiers apply at the single exit event? Is there a clawback?" | Can't explain the catch-up; "you get paid when we get paid" |
| `Q-FEE-02` (`GEN-06`) | "Which service providers are GP-affiliated, and what do they charge during the no-distribution years?" | "All arm's-length" without naming providers |
| `Q-GP-01` (`GEN-01`) | "How much of your own cash is in this deal, pari-passu?" | "Sweat equity is our investment"; co-invest is a fee waiver |
| `Q-GP-02` (`GEN-05`, `GEN-14`) | "What are your realized, net-to-LP results on prior multifamily **exits**?" | Project-level IRR only; "most deals are still performing" |
| `Q-GP-03` (`GEN-02`) | "Any regulatory action or investor litigation?" | "Nothing material"; a search turns up something undisclosed |
| `Q-MKT-01` (`GEN-18`) | "What submarket supply and absorption support the exit NOI?" | Metro-level optimism; no supply pipeline acknowledged |
| `Q-LIQ-01` | "What are my options if I need out before the Year-5 sale?" This matters more when there is zero cash along the way | "A secondary market may develop"; vague accommodation |

**Nice-to-ask**
- `Q-DIST-02`: capital-call mechanics. **I'd treat it as must-ask** 🟡: a deal paying out nothing may have no cash cushion for capex overruns. Bad-answer signal: "calls as needed," with punitive dilution buried in the docs.
- `Q-GP-04` (`GEN-04`): team capacity. Bad-answer signal: AUM multiplied while the team stayed flat.
- `Q-LIQ-02`: K-1 timing. Bad-answer signal: a history of extensions.

### 9. Diligence Checklist

- PPM and operating agreement: the waterfall, pref accrual mechanics, capital-call and transfer provisions
- Sponsor background: SEC/FINRA/state actions, litigation search, **realized** exits verified against LP references
- Rent and sale comps for the submarket, including exit-cap comps for similar-vintage assets
- Third-party appraisal or broker opinion of value against the purchase price
- Loan documents: maturity, extensions, rate cap term, prepayment and defeasance cost (all of which gate the Year-5 sale)
- T-12 and rent roll, reconciled to bank statements where possible

### 10. Verdict (Deal B)

**Pass as presented — insufficient disclosure.** Deal B tells us *when* the return arrives (entirely at the Year-5 sale 🟢) and nothing about *what sets its size*. There is no basis, exit cap, leverage, debt maturity, sponsor, or fee stack. For a deal whose return is 100% terminal value, those are not residual gaps; they *are* the core return story, so a merits verdict isn't possible yet.

- **Biggest swing factor:** the exit cap and sale timing. A 20% price miss or a 2-year slip each cuts the IRR to roughly 9–10%.
- **Re-screen list:** sponsor and realized exit record; gross vs net; going-in and exit cap with sensitivity; debt terms and maturity vs Year 5; the full fee schedule and waterfall with pref accrual mechanics; the reason for zero distributions; co-invest.
- **Who it could suit, if it re-screens well:** an LP who needs no income for five years, can lose the whole position without portfolio harm, and holds real conviction in this sponsor's exit execution.
- **What would have to be true:** exit cap at or above going-in; debt that matures after the sale window, with extensions; a cumulative, compounding pref; meaningful pari-passu co-invest.

---

## Part 2 — Deal A vs Deal B

Deal A's screen from the previous message stands. This section adds only the structural contrast you asked for.

### What's stated

| | Deal A | Deal B |
|---|---|---|
| Asset class | Multifamily | Multifamily |
| Claimed IRR | 14% (gross/net not stated) | 14% (gross/net not stated) |
| Distributions | 7% CoC, quarterly, from Year 1 🟢 | None until sale 🟢 |
| Capital return | Progressive over the hold 🟢 | Entirely at the Year-5 sale 🟢 |
| Exit dependence | Partial. Split not disclosed | **100%** (`GEN-08` fired) |
| `GEN-11` J-curve | Front-loaded. Shallow curve | Maximum-depth curve |
| Sponsor / fees / debt / exit cap | Not stated | Not stated |

### Illustrative side-by-side (🔴 assumed shape for A)

Deal A's hold and capital-return schedule were not stated. To put the two on one axis I assumed a 5-year hold for A, 7% CoC quarterly on original capital, 5% of capital returned at each of Years 2–5, and the remainder at sale, calibrated to the same 14% IRR. Deal B is modeled as stated. Both use $100 invested.

| Metric | Deal A (illustrative) | Deal B |
|---|---|---|
| Interim cash to LP before sale | $55 | **$0** |
| Exit proceeds | ≈$119 | ≈$193 |
| Equity multiple | ≈1.74x | ≈1.93x |
| Exit share of value (PV) | ≈62% | **100%** |
| IRR if exit value −20% | ≈10.3% | ≈9.0% |
| IRR if exit value −50% | ≈3.5% (1.15x) | ≈−0.8% (**0.96x**) |
| IRR if sale slips 2 years (A keeps paying CoC) | ≈12.2% | ≈9.8% |
| **Cash back if the exit is worth zero** | **$55 of $100** | **$0 of $100** |
| Year-5 wealth if distributions are reinvested at ~5% (10yr Treasury 5.18% / VNQ 4.92%) | ≈$180 | ≈$193 |

### What the comparison shows

1. **Equal IRRs, unequal risk.** Every exit shock hurts B more than A. Under a total exit failure, B loses everything, while A has already returned more than half the capital. B concentrates all return risk and all capital risk at one date. That is the `GEN-11` mechanism in its purest form.
2. **Timing risk is B's specific failure mode.** A 2-year sale delay costs A ~180bps, because the CoC keeps paying through it. It costs B ~420bps, and in a frozen market that delay can also run into a debt maturity (`GEN-09`).
3. **B's genuine offset: a higher multiple and no reinvestment drag.** A's 14% IRR implicitly assumes each distribution is reinvested at 14%. Reinvested at today's ~5% risk-free or REIT rates, A's Year-5 wealth (≈$180) trails B's (≈$193). **If both deals hit plan, B leaves the LP with more money.** B's structure is not simply worse. It trades a better base case for a much worse left tail.
4. **A is not automatically a cash-flow story either.** Under the illustrative 5-year shape, ~62% of A's value still comes from the sale, right at the `GEN-08` line. That result depends on an assumed hold and schedule 🔴, so it is a must-ask for A (`Q-DS-01`), not a fired flag.
5. **The undisclosed items decide the real ranking, and they hit B harder.** Pref accrual (`Q-FEE-04`) is B's only time-value protection. Debt maturity versus the sale (`Q-RISK-01`) is B's only way out. Liquidity (`Q-LIQ-01`) matters most when there is no cash along the way.

### Bottom line

**On the structure disclosed, Deal A is the better passive-LP position for most investors.** It returns capital early, has a shallower J-curve, and holds up better when the exit disappoints. **Deal B pays for its concentrated risk only through a higher multiple in the base case.** That trade makes sense only for an LP with no income need, high conviction in the exit, and a B that proves out on the conditions in §10.

**What would flip the ranking:** B discloses a conservative exit cap (≥ going-in), modest fixed-rate leverage maturing well after Year 5, a compounding cumulative pref, and real co-invest, while A's return turns out to rest on an aggressive exit cap or a refi. Neither deal is underwritable yet on sponsor, fees, debt, or exit assumptions. Send both GPs the same core requests: `Q-FEE-01`, `Q-DS-01`, `Q-RISK-01`, `Q-GP-02`.
