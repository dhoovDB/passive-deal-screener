# Eval fixture 11

*Iteration-7 run, 2026-11-01, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 181fdd7.*

# Deal A vs Deal B: two multifamily deals with the same 14% IRR

**Verdict (both deals): Pass as presented, insufficient disclosure.** If the rest of the terms came back identical and clean, **Deal A would be the lower-risk way to earn 14%.** Deal B puts all of its return on a single Year-5 sale (`GEN-08`, RED).

*Screening output only, not investment advice.*

Neither deal shows enough to underwrite the core return story. Neither one names a sponsor or says whether 14% is gross or net. Neither discloses fees, a waterfall, debt terms, an exit cap or a track record. The comparison you asked for still has a clear answer. The two "14%" figures carry very different risk. Deal A pays you back as it goes. Deal B gives you nothing until the property sells, so every dollar of profit depends on the exit happening on time and at the assumed price. Deal B's one advantage: if the exit goes exactly to plan, it ends with more dollars (about 1.93x vs about 1.81x, illustrative). Below, each deal is screened on its own and then the two are compared directly.

Confidence tags: 🟢 stated, or taken from a reference · 🟡 inferred · 🔴 assumed or unverifiable.

---

## Part 1: Deal A screen

### 1. Deal Snapshot

| Field | Deal A |
|---|---|
| Asset class | Multifamily 🟢. Sub-type (value-add vs core/core-plus) Not stated. A 14% target fits value-add (`01`: 12–18% target) 🟡 |
| Deal type | Equity syndication 🟡 (inferred from "IRR" + "cash-on-cash"; structure Not stated) |
| Sponsor / GP | Not stated |
| Geography / submarket | Not stated |
| Minimum investment | Not stated |
| Hold period | Not stated ("capital returns progressively over the hold") |
| Raise / equity size | Not stated |
| Claimed return | 14% projected IRR 🟢. Gross vs net-to-LP Not stated |
| Distributions | 7% cash-on-cash, paid quarterly, starting Year 1 🟢. Capital returned progressively over the hold 🟢. The schedule and the mechanism for returning capital are Not stated |
| Leverage / debt | Not stated |
| Fees / waterfall / pref | Not stated |

### 2. Return Stress-Test

**Net vs gross.** The deal says "14% IRR" without saying whose IRR it is. Under the never-gross-to-gross rule, the net-to-LP figure has to be demanded (`Q-FEE-01`) before anything is concluded. Both readings are run below.

**Benchmark (`scripts/benchmark_comparator.py`, exit 0):**

| Reading | Net IRR used | vs VNQ (4.92% 10yr) | Illiquidity hurdle | Read |
|---|---|---|---|---|
| 14% is already net (as presented) | 14.00% 🟢 | ≈908 bps | 5-yr: ~300–400 bps · 7-yr: ~400–600 bps | Clears comfortably at either hold |
| 14% is gross, with a `02`-typical fee stack (all fees ASSUMED, see §4) | 9.32% 🔴 | ≈440 bps | 5-yr: ~300–400 bps | Clears, but only by ~40–140 bps |

The hold is not stated, so the comparator was run at both 5 and 7 years (`01` value-add norm: 5–7 yrs). On the Treasury floor (`05`: 10yr ≈ 5.18%), 14% is ≈882 bps over and 9.32% is ≈414 bps over. Per `05`, the Treasury currently out-yields VNQ's trailing 10-year return, so it is the tighter floor. Beating the spread is necessary, not sufficient. Per the Preqin dispersion note, the median deal earns well below the marketed figure.

**Unlevered overlay (`05`).** NCREIF NPI, which is unlevered and almost entirely income, returned 5.00% over the trailing four quarters. A 14% levered figure therefore implies roughly 9 points from leverage and assumed appreciation rather than in-place operations 🟡. That is not automatically bad, but the leverage is undisclosed, so the size of the financing bet can't be measured (`GEN-07`, see §5).

**Scenarios.** These are illustrative. The shape is ASSUMED 🔴: a 5-year hold, 7% a year, the remaining value paid at exit, and progressive capital return ignored (which makes A look more exit-dependent than described).

| Case | Swing assumptions | Deal A IRR | Multiple |
|---|---|---|---|
| Base (as pitched) | Exit on plan | 14.0% | ~1.81x |
| Mild bear | Exit proceeds −10% (exit cap widens / flat rents) | ~12.0% | ~1.67x |
| Bear | Exit proceeds −20% | ~9.8% | ~1.52x |
| Severe | Exit proceeds −50% | ~1.8% | ~1.08x (capital still returned) |
| Delay | Same exit value, sold Year 7 instead of Year 5 | ~11.6% | n/a |

The three swing assumptions are the **exit cap** (the single biggest swing in multifamily pro formas, per `01`), **rent growth** to sustain 7% cash-on-cash, and whether capital return depends on a **refinance** (`EQUITY-07`). No sensitivity or downside case was provided (`GEN-13`).

**Year-1 7% cash-on-cash.** `01` puts multifamily value-add cash-on-cash at 5–8% *after stabilization*. Paying 7% from Year 1, before a value-add plan could have stabilized, raises a question 🟡: are the distributions funded by property operations, or by reserves and returned capital? If it's the latter, they are return OF capital, not return ON capital. Routed to `Q-DIST-01` and `Q-DS-02`. No flag fires on this, because the source of the cash is unknown, not shown to be a problem.

### 3. Where LP Returns Come From

- **Cash flow:** 7% a year starting in Year 1, plus capital returned progressively 🟢. On the illustrative shape above, about 43% of total profit arrives as cash flow before exit, and about 57% at exit 🔴. Once the progressive capital return is counted, the exit share is lower again.
- **Exit:** below the >60% `GEN-08` threshold on the illustrative shape, but close, and **not verifiable** without the GP's own IRR decomposition. `GEN-08` is therefore **not fired** and becomes a must-ask (`Q-DS-01`).
- **Leverage:** Not stated. The unlevered gap (14% vs NPI 5.00%) suggests a large leverage and appreciation component 🟡. `GEN-07` is not fired, because doing so would need an assumed debt structure.
- **How capital comes back:** "Progressively" could mean amortization, partial sales, or refinance proceeds. If it's refinance proceeds, the plan is refi-dependent (`EQUITY-07`). Unknown 🔴.

### 4. Fee Stack Summary

**Gross-to-net drag: not computable from disclosure. That is the finding** (`GEN-16`).

- `scripts/fee_drag_calculator.py` run with `0` for every undisclosed fee (exit 0) returns 0 bps of drag. That is a placeholder for "nothing disclosed," not a real figure. Undisclosed fees still get paid.
- For scale only: if the 14% is gross and the stack matches the `02` equity-syndication worked example, drag comes to **≈468 bps/yr**, taking the LP to **≈9.32% net**. That stack is a 2% acquisition fee, 1.5% annual asset management, 1% disposition, 0.3% admin, and a 20% promote over an 8% pref with 100% catch-up, at a 5-year hold. Every input there is ASSUMED 🔴, and the script flagged them (exit 1). Of the drag, 180 bps comes from recurring fees, 60 bps from one-time fees and 228 bps from the promote. Each assumed input is a §6 gap.
- Every fee layer in `02` that an equity syndication normally carries is missing: acquisition, asset management, disposition, loan placement, refinance (relevant if capital returns via refi), investor relations/admin, promote/pref/catch-up, the waterfall structure (deal-by-deal vs whole-of-fund, clawback), and any affiliate fees.

### 5. Red Flags

**Fired:**

| ID | Severity | Mechanism → LP exposure | Confidence |
|---|---|---|---|
| `GEN-16` No fee or waterfall disclosure | YELLOW–RED (treat as RED until answered) | Fees still get paid even when they aren't disclosed, so the gap between 14% and what you actually keep can't be measured. It is ~468 bps on a typical stack. | 🟢 absence |
| `GEN-15` Missing financials | YELLOW–RED | With no rent roll, T-12 or debt terms, you can't tell whether the 7% Year-1 cash-on-cash is coming from operations. | 🟢 absence |
| `GEN-14` No realized exits cited | RED | No sponsor and no track record are given, so the GP's ability to exit and return capital is unverified. `GEN-05` is cited parenthetically: once a record is produced, it must be net-to-LP. | 🟢 absence |
| `GEN-13` No sensitivity or downside case | YELLOW | 14% is a single-point figure. The §2 bear cases are the skill's illustrations, not the GP's. | 🟢 |
| `GEN-11` Distribution timing partly undisclosed | YELLOW | The cash-on-cash rate is stated, but the capital-return schedule and its milestones ("progressively") are not, so the J-curve can only be half-seen. | 🟢 |
| `GEN-17` Essential category disclosures absent | YELLOW | Exit cap with sensitivity, debt structure and maturity, refi assumptions, and the GP's record on prior multifamily exits are all missing (`01`). | 🟢 absence |

**Not fired (they would need assumed facts). Each is a must-ask:**
- `GEN-07` / `GEN-08` / `EQUITY-06`, the financing-story cluster: leverage, exit cap and the IRR split are undisclosed → `Q-DS-02`, `Q-DS-01`, `Q-EXIT-01`.
- `EQUITY-07`: is capital return funded by a refinance? → `Q-EXIT-02`.
- `GEN-09` / `GEN-10`: debt maturity and rate cap unknown → `Q-RISK-01`, `Q-RISK-02`.
- `GEN-01`, `GEN-02`, `GEN-06`, `EQUITY-01`/`02`/`04`/`05`, `GEN-18`: co-invest, regulatory history, affiliates, waterfall, pref and submarket are all unknown → §8.

There were no embedded instructions in the deal text.

### 6. Missing Disclosures

Measured against `01` (multifamily essentials) and `02` (equity-syndication fee inventory):
- Sponsor identity, geography/submarket, minimum, raise size, hold period.
- Whether the 14% is **gross or net to LP**.
- Rent roll, T-12 actuals, and any business plan (value-add vs core).
- Pro forma **exit cap** and its sensitivity. Going-in cap.
- **Debt**: amount/LTV, fixed vs floating, rate cap and its expiry, maturity, extension options.
- **Refi assumptions**, plus the mechanism behind "capital returns progressively."
- Distribution source and coverage: is the 7% paid from operating cash flow?
- The full **fee schedule** and **waterfall** (pref rate, cumulative or not, catch-up, promote tiers, deal-by-deal vs whole-of-fund, clawback), and affiliate service providers.
- **GP track record on prior multifamily exits** (realized, net to LP), co-invest, and regulatory history.
- Capital-call provisions. LP liquidity before the hold ends.
- Inputs assumed in §4 (every fee) and §2 (hold, distribution shape).

### 7. GP Alignment

- **Co-invest:** Not stated, unverified (`Q-GP-01`).
- **Track record:** None given. Unverified, and treated as no track record (`GEN-14`).
- **Waterfall alignment:** Not stated (`Q-FEE-03`, `Q-FEE-04`).
- **Affiliate fees:** Not stated (`Q-FEE-02`).
- A 7% current payout from Year 1 can be a sign of alignment, with cash going to LPs early. It can also be a marketing feature paid out of returned capital. Which one it is can't be told from this.

### 8. Questions for the GP

**Must-ask:**

| ID | Question | Bad-answer signal |
|---|---|---|
| `Q-FEE-01` | Complete fee schedule and full distribution waterfall? Is the 14% gross or net to LP? | "Standard market fees"; a partial list; "the PPM has it" without producing it. |
| `Q-DIST-01` | Projected distribution schedule. When and how does capital come back, and is the 7% paid from operating cash flow? | "We'll distribute when the deal supports it"; no milestones; can't say what funds the Year-1 7%. |
| `Q-DS-01` | What share of the 14% comes from in-place cash flow vs the exit, and what's the IRR at a flat exit cap? | Can't decompose the IRR; "real estate always appreciates"; the IRR drops below the pref at a flat cap. |
| `Q-DS-02` | Strip out leverage and cap-rate compression: what's the unlevered, in-place return? | "Leverage is just how the deal works"; no unlevered view exists. |
| `Q-DS-03` | Bear case: flat rents, higher exit cap, no refinance? | A single-point pro forma; "we underwrite conservatively" with nothing to show. |
| `Q-EXIT-02` | Does "capital returns progressively" depend on a refinance? What happens to distributions if the refi isn't available? | Capital return needs a refi at lower rates; no fallback; "the refi market will reopen." |
| `Q-EXIT-01` | Exit cap vs going-in cap. What's the IRR at an exit cap equal to or above going-in? | Exit cap below going-in "because cap rates will compress"; no sensitivity. |
| `Q-RISK-01` | When does the debt mature relative to the hold, and what's the refi or extension plan? | Maturity falls inside the hold; "we'll refinance" with no terms. |
| `Q-RISK-02` | If the debt floats: when does the rate cap expire, and what does it cost to extend? | The cap expires before maturity; extension cost not modeled; "rates should be lower by then." |
| `Q-RISK-03` | T-12, rent roll, complete debt terms? | T-3/T-6 only; "confidential until you commit." |
| `Q-GP-01` | How much of your own capital is in, on LP terms? | "Sweat equity"; a fee waiver presented as co-invest; a token amount. |
| `Q-GP-02` | Track record as net-to-LP IRR on fully realized, exited deals only? | Project-level IRR only; "most deals are still performing." |
| `Q-GP-03` | Any regulatory action, enforcement or investor litigation? | "Nothing material"; a search turns up something they didn't disclose. |
| `Q-FEE-02` | Which providers are GP-affiliated, and at what rates? | "All arm's-length" without naming anyone. |
| `Q-FEE-03` | Deal-by-deal or whole-of-fund, and is there a clawback? | Can't explain the catch-up; "you get paid when we get paid." |
| `Q-FEE-04` | Pref rate: is it cumulative and compounding? | Pref below 6% or none; non-cumulative. |
| `Q-MKT-01` | What submarket supply and absorption data support the rent growth that sustains 7% cash-on-cash? | Metro-level optimism; no supply pipeline acknowledged. |
| `Q-LIQ-01` | What are my options if I need to exit before the hold ends? | "A secondary market may develop"; silence. |

**Nice-to-ask:** `Q-GP-04` (team scale vs AUM: "we're lean and efficient" as the entire answer), `Q-DIST-02` (capital calls: "as needed," punitive dilution), `Q-LIQ-02` (K-1 timing: "as soon as we can," a history of extensions).

### 9. Diligence Checklist

- PPM/operating agreement: fees, waterfall, pref, clawback, capital-call terms.
- Sponsor background, regulatory and litigation search (SEC/FINRA/state, court records).
- Independent rent and sale comps for the submarket. Exit-cap sanity check against recent trades.
- Appraisal and property condition report.
- Lender term sheet: maturity, rate cap, extension tests.
- Verification of the distribution source: an operating-cash-flow reconciliation behind the 7%.
- References from LPs on the sponsor's prior realized deals.

### 10. Verdict

**Pass as presented, insufficient disclosure.**

*Screening output only, not investment advice.*

The deal's shape is the better of the two: current income from Year 1, with capital coming back during the hold rather than all at the end. But a sponsor-less, fee-less, debt-less 14% can't be underwritten. **Biggest swing factor:** whether the 7% and the progressive capital return come from property operations, or from reserves and refinance proceeds. If it's the operations, A is a genuine income-plus-growth deal. If it's the reserves or refinance, A carries a hidden refi and financing bet (`EQUITY-07`, `GEN-07`). **Re-screen list:** net-to-LP IRR, fee schedule and waterfall, debt terms (maturity, rate cap), exit cap and sensitivity, T-12 and rent roll, distribution schedule and its source, sponsor's realized track record, co-invest. **It would suit** an LP who wants current income and less dependence on a single exit, as long as the distributions are shown to come from operations.

---

## Part 2: Deal B screen

### 1. Deal Snapshot

| Field | Deal B |
|---|---|
| Asset class | Multifamily 🟢. Sub-type Not stated. Zero distributions for five years is unusual for stabilized multifamily (`01`: core is "cash-flow-driven"), which points to a heavy repositioning or a plan that retains cash 🟡 |
| Deal type | Equity syndication 🟡 (structure Not stated) |
| Sponsor / GP | Not stated |
| Geography / submarket | Not stated |
| Minimum investment | Not stated |
| Hold period | 5 years (sale in Year 5) 🟢. Inside the `01` value-add norm of 5–7 yrs |
| Raise / equity size | Not stated |
| Claimed return | 14% projected IRR 🟢, the same as Deal A. Gross vs net Not stated |
| Distributions | **None until sale in Year 5. The entire return is realized at exit** 🟢 |
| Leverage / debt | Not stated |
| Fees / waterfall / pref | Not stated |

### 2. Return Stress-Test

**Benchmark (`scripts/benchmark_comparator.py`, exit 0, 5-year hold as stated):**

| Reading | Net IRR used | vs VNQ (4.92%) | Hurdle (5-yr) | Read |
|---|---|---|---|---|
| 14% is net (as presented) | 14.00% 🟢 | ≈908 bps | ~300–400 bps | Clears comfortably |
| 14% is gross, `02`-typical stack (ASSUMED) | 9.32% 🔴 | ≈440 bps | ~300–400 bps | Clears by only ~40–140 bps |

The Treasury floor (10yr ≈ 5.18%) gives the same read as for A. One difference matters here: **Deal B's clearance depends entirely on the exit happening.** A benchmark spread on a back-loaded IRR is a spread on a *single future price*, not on income received.

**Unlevered overlay (`05`).** NPI's 5.00% is almost entirely income. Deal B pays the LP **zero** income. Whatever the property earns is either retained or used for capex and debt service, and the LP's whole 14% has to come out of sale proceeds. Relative to the unlevered, income-heavy baseline, B's return is made up entirely of terminal value 🟢. Whether that terminal value is driven by leverage and cap compression (`GEN-07`, `EQUITY-06`) can't be told without the debt and exit cap 🔴.

**Scenarios.** These are illustrative 🔴: one 5-year lump sum producing 14%.

| Case | Swing assumptions | Deal B IRR | Multiple |
|---|---|---|---|
| Base (as pitched) | Exit on plan | 14.0% | ~1.93x |
| Mild bear | Exit proceeds −10% | ~11.6% | ~1.73x |
| Bear | Exit proceeds −20% | ~9.0% | ~1.54x |
| Severe | Exit proceeds −50% | ~−0.8% | ~0.96x (**capital loss**) |
| Delay | Same proceeds, sold Year 7 | ~9.8% | n/a |

The swing assumptions are the **exit cap** (here it is the *only* source of return), **the timing of the sale** (a two-year delay costs B about 4.2 IRR points vs about 2.4 for A), and **debt maturity relative to the Year-5 sale** (if the loan matures near Year 5 and the sale market is shut, the LP faces a forced sale or a refinance with no income cushion: `GEN-09`, `GEN-10`). No downside case was provided (`GEN-13`).

### 3. Where LP Returns Come From

- **Cash flow to LP:** 0% 🟢.
- **Exit:** **100%** of LP return comes from terminal value 🟢. That is well above the >60% threshold, so **`GEN-08` fires as RED** on stated facts.
- **Leverage:** Not stated. Given 0% income and 100% exit, if the GP shows leverage and cap compression driving the exit value, B is a textbook financing story (`GEN-07` + `GEN-08` + `EQUITY-06`). Two of those three are still unconfirmed 🔴 and are must-asks.
- **Structural point:** a return that arrives entirely at exit can't be partly banked. Deal B holds no "money already received" if the market turns in Year 4 or 5.

### 4. Fee Stack Summary

**Gross-to-net drag: not computable from disclosure. That is the finding** (`GEN-16`).

- `fee_drag_calculator.py` with `0` for all undisclosed fees (exit 0) gives 0 bps. That is a placeholder, not a figure.
- For scale, on the same ASSUMED `02`-typical stack at a 5-year hold: **≈468 bps/yr → ≈9.32% net** (exit 1, all inputs assumed 🔴).
- One fee point specific to B: with the whole return arriving at sale, the **disposition fee** and the **promote** are both paid out of the one cash event the LP has. Before the LP's share is known, you need to know the waterfall order at exit: return of capital, then pref accrual, then catch-up, then split. You also need to know whether the pref is **cumulative and compounding** (`EQUITY-05`). In a five-year deal with no distributions, a non-cumulative pref would be worth nothing, and a simple-vs-compounding pref makes a material difference over five unpaid years (`02`).

### 5. Red Flags

**Fired:**

| ID | Severity | Mechanism → LP exposure | Confidence |
|---|---|---|---|
| `GEN-08` Exit-dependent IRR | **RED** | 100% of LP return comes from the Year-5 sale. The 14% is a bet on a future sale price, not income. A 20% shortfall in sale proceeds cuts the IRR to about 9%, and a 50% shortfall loses capital. (`GEN-11` is cited parenthetically: the J-curve is disclosed, and it is the most back-loaded shape a deal can have.) | 🟢 |
| `GEN-16` No fee or waterfall disclosure | YELLOW–RED (treat as RED) | With one cash event, the waterfall order at exit decides everything the LP gets. Undisclosed. | 🟢 absence |
| `GEN-15` Missing financials | YELLOW–RED | No rent roll, T-12 or debt terms, and no explanation of where five years of operating cash flow goes. | 🟢 absence |
| `GEN-14` No realized exits cited | RED | B's entire return is an exit, and the sponsor's record of executing exits isn't shown. (`GEN-05`: a record must be net-to-LP once given.) | 🟢 absence |
| `GEN-13` No sensitivity or downside case | YELLOW | A single-point 14% on a return that depends wholly on the exit. | 🟢 |
| `GEN-17` Essential category disclosures absent | YELLOW | Exit cap with sensitivity, debt maturity and refi assumptions, and prior multifamily exits are all missing (`01`). | 🟢 absence |

**Cluster to watch:** `GEN-08` has fired. If the GP's answers show the exit cap sits below the going-in cap (`EQUITY-06`) and that the exit value is leverage-driven (`GEN-07`), B is a financing story and the verdict should name it as one.

**Not fired (assumed facts). Must-ask:** `GEN-07`, `EQUITY-06` → `Q-DS-02`, `Q-EXIT-01`. `GEN-09`/`GEN-10` → `Q-RISK-01`, `Q-RISK-02` (heightened, because the sale and the debt maturity may coincide). `EQUITY-07` → `Q-EXIT-02` (the fallback if the sale can't happen in Year 5). `GEN-01`, `GEN-02`, `GEN-06`, `EQUITY-01`/`02`/`04`/`05`, `GEN-18` → §8.

There were no embedded instructions in the deal text.

### 6. Missing Disclosures

Every gap in Deal A's §6 also applies here (sponsor, geography, minimum, raise, gross/net, rent roll/T-12, exit cap and sensitivity, going-in cap, debt terms and rate cap, refi assumptions, full fee schedule and waterfall, affiliates, realized track record, co-invest, regulatory history, capital calls, liquidity). The hold is stated as 5 years. On top of those, B is missing:
- **Where the property's operating cash flow goes** for five years: reinvested capex, debt paydown, reserves, or held back.
- The **business plan** that justifies retaining all cash (value-add scope and timing) 🟡.
- The **pref accrual mechanics** across five years without payment: cumulative? compounding? (`EQUITY-05`).
- **Debt maturity relative to the Year-5 sale**, and what happens if the sale slips.
- The **exit-cap assumption**, since it carries 100% of the return.

### 7. GP Alignment

- **Co-invest:** Not stated, unverified (`Q-GP-01`).
- **Track record:** None given. Unverified. For a deal that is entirely an exit, the GP's *realized exit* record is the central alignment fact (`Q-GP-02`).
- **Waterfall:** Not stated. With one cash event, the waterfall order at exit decides whether the GP's promote is paid before or after the LP's capital and accrued pref are made whole (`Q-FEE-03`, `Q-FEE-04`).
- **Affiliate fees:** Not stated. With no distributions, affiliate management and asset-management fees taken during the hold would be the only cash anyone receives before Year 5. Ask who is being paid in the meantime (`Q-FEE-02`).

### 8. Questions for the GP

**Must-ask** (the ones specific to B come first):

| ID | Question | Bad-answer signal |
|---|---|---|
| `Q-DS-01` | 100% of the return is exit. What's the IRR at a flat exit cap, and at +50/+100 bps? | Won't run it; "cap rates will compress"; the IRR falls below the pref at a flat cap. |
| `Q-EXIT-01` | What exit cap are you assuming vs the going-in cap? | Exit below going-in with no specific thesis; no sensitivity offered. |
| `Q-DS-02` | Unlevered, in-place return, with leverage and cap compression stripped out? | "Leverage is just how the deal works"; no unlevered view. |
| `Q-RISK-01` | When does the debt mature relative to the Year-5 sale, and what are the extension options? | Maturity at or before Year 5 with no extension; "we'll sell or refinance" with no terms. |
| `Q-RISK-02` | If floating: when does the rate cap expire, and what does extending it cost? | The cap expires before the sale; cost not modeled. |
| `Q-EXIT-02` | If a Year-5 sale isn't available on your assumed terms, what's the fallback, and does it depend on a refinance? | "We'll hold until the market recovers," with no plan for debt service or LP returns. |
| `Q-DIST-01` | Why no distributions for five years? Where does operating cash flow go, and what milestones could trigger an earlier distribution? | "We'll distribute when the deal supports it"; can't say where five years of cash flow goes. |
| `Q-FEE-04` | Is the pref cumulative and compounding over five unpaid years? | Non-cumulative; simple-only; pref below 6% or none. |
| `Q-FEE-03` | Waterfall order at exit: capital and accrued pref first, then catch-up? Deal-by-deal, and is there a clawback? | Can't explain the catch-up; "you get paid when we get paid." |
| `Q-FEE-01` | Full fee schedule and waterfall? Is the 14% gross or net to LP? | "Standard market fees"; "the PPM has it" without producing it. |
| `Q-FEE-02` | GP-affiliated providers and their fees during the hold? | "All arm's-length" without naming anyone. |
| `Q-DS-03` | Bear case: flat rents, higher exit cap, no refinance, delayed sale? | A single-point pro forma; the bear case is still a gain. |
| `Q-RISK-03` | T-12, rent roll, complete debt terms? | T-3/T-6 only; "confidential until you commit." |
| `Q-GP-02` | Realized, exited deals, net to LP? | Project-level IRR; "most deals are still performing." |
| `Q-GP-01` | Your own capital in, on LP terms? | "Sweat equity"; a fee waiver; a token amount. |
| `Q-GP-03` | Regulatory action or investor litigation? | "Nothing material"; undisclosed findings. |
| `Q-MKT-01` | What submarket supply and absorption data support the exit-year rent and NOI? | Metro-level optimism; no supply pipeline. |
| `Q-LIQ-01` | Options to exit before Year 5? | "A secondary market may develop"; silence. |

**Nice-to-ask:** `Q-GP-04` (team scale: no named asset manager), `Q-DIST-02` (capital calls: "as needed." This could be escalated, because a deal with no distributions has no income buffer to fund shortfalls), `Q-LIQ-02` (K-1 timing: a history of extensions).

### 9. Diligence Checklist

Everything in Deal A's list, plus:
- An independent check of the exit-cap assumption against recent submarket trades. In B, that assumption carries the whole return.
- The lender term sheet read specifically for the **maturity date vs Year 5**, extension tests, and rate-cap expiry.
- A capex budget and schedule that explains why cash is retained.
- An operating-agreement review of how the pref accrues and the order of the exit waterfall.

### 10. Verdict

**Pass as presented, insufficient disclosure.**

*Screening output only, not investment advice.*

Even if the disclosure gaps were filled, Deal B carries a confirmed RED (`GEN-08`). Every dollar of the 14% depends on selling in Year 5 at the assumed price. **Biggest swing factor:** the exit cap, and whether the sale happens on time. A two-year delay takes B to about 9.8%. A 50% shortfall in sale proceeds loses capital, where Deal A would still roughly return capital plus income. **Re-screen list:** net-to-LP IRR, exit cap vs going-in with sensitivity, debt maturity and rate cap vs Year 5, fee schedule and the exit waterfall, pref accrual mechanics, where operating cash goes, realized exit track record, co-invest. **It would suit** an LP who needs no current income, can stay fully locked up for 5+ years, and has independent confidence in the exit market. It would also take a GP who can show the exit value comes from operations, not cap compression.

---

## Part 3: Head-to-head, why "same 14%" is not the same deal

| | Deal A | Deal B |
|---|---|---|
| Cash to LP before exit | 7%/yr from Year 1 + progressive capital return 🟢 | None 🟢 |
| Share of return from exit | ~57% of profit on the illustrative shape, lower with progressive capital return 🔴 | **100%** 🟢 → `GEN-08` RED |
| Illustrative multiple at 14% / 5 yrs | ~1.81x 🔴 | ~1.93x 🔴 |
| Exit −20% | ~9.8% IRR | ~9.0% IRR |
| Exit −50% | ~1.8% IRR, capital returned | ~−0.8% IRR, **capital loss** |
| Sale slips 2 years | ~11.6% IRR | ~9.8% IRR |
| Capital back before exit? | Partly, "progressively" (mechanism unknown) | No |
| Exposure to debt maturity near the sale | Cushioned by cash already received | Unbuffered |
| Key unknown | Is the 7% paid from operations, or from returned capital or refinance proceeds? | Is the exit value driven by operations, or by leverage and cap compression? |

**What the comparison shows:**

1. **Equal IRRs, unequal risk timing.** Both claim 14%. Deal A hands you part of that return every quarter, and you keep it whatever happens at sale. Deal B asks you to trust that one sale in Year 5 will deliver the whole 14%. The `03` library treats this explicitly (`GEN-11`): identical IRRs can carry very different risk timing, and the back-loaded one concentrates all return risk at the exit.
2. **Deal B's real advantage is dollars, not safety.** At the same IRR, B's capital compounds untouched for longer, so if everything goes to plan it ends with more money: about 1.93x vs about 1.81x. Deal A only matches that if you can reinvest its distributions at about 14%. Reinvested at Treasury bill or note rates (4.24–5.18%), A's distributions bring you to roughly 1.84–1.85x, about 13.0–13.1% on a terminal-wealth basis. **B wins if the exit happens as planned. A wins in almost every path where it doesn't.**
3. **The downside is lopsided.** A sale-proceeds shortfall hurts both, but A's early cash puts a floor under the loss. In these illustrations, B starts losing capital at roughly a 48% shortfall, while A still gets its capital back at a ~56% shortfall.
4. **Deal A's caveat.** A is only "better" if its 7% is real operating cash flow. If Year-1 distributions are funded by reserves or by your own returned capital, or if "progressive capital return" means refinance proceeds, A carries a disguised refi and financing bet (`EQUITY-07`, `GEN-07`), and the gap between the deals narrows. That is the first question to put to Deal A's sponsor (`Q-DIST-01`, `Q-EXIT-02`).

**The bottom line on the comparison.** Neither deal is underwritable as presented. Both are **Pass as presented, insufficient disclosure**. If both came back with clean, comparable terms (net IRR, fees, waterfall, debt, exit cap, track record), Deal A's distribution profile is the lower-risk way to earn the same headline 14%, provided its distributions are shown to come from operations. Deal B would need a demonstrably conservative exit cap, debt that matures well after Year 5, a cumulative and compounding pref, and a realized record of exits to make up for putting the entire return on one sale.

*Screening output only, not investment advice.*

*Scripts run: `benchmark_comparator.py` (multifamily-equity at 14% for 5 and 7 years, and at 9.32% for 5 years; exit 0) and `fee_drag_calculator.py` (all-zero undisclosed run, exit 0; `02`-typical ASSUMED-stack run, exit 1). Scenario IRRs are illustrative calculations on assumed cash-flow shapes, not GP projections.*
