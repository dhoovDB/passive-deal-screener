# Eval fixture 11 — J-curve pair, Deal B (all-at-exit) + A/B comparison
*Iteration-4 run, 2026-09-27, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 1c7faff.*

**Verdict (Deal B): Pass as presented — insufficient disclosure.** All of Deal B's return arrives at one exit event (`GEN-08`, RED), and the deal discloses nothing about that exit: no exit cap, no debt terms, no fees, no waterfall, no sponsor. **A vs B: the two deals are not equal at 14%.** On the facts given, Deal A carries less risk. It returns cash every quarter, and the same exit shortfall costs it less. Deal B is a single bet on the Year-5 sale price.

---

## Deal B — screen

### 1. Deal Snapshot

| Field | Deal B |
|---|---|
| Asset class | Multifamily. Sub-type (value-add / core / development) not stated 🔴 |
| Deal type | Equity syndication (inferred from "property sells in Year 5") 🟡 |
| Sponsor | Not stated |
| Geography | Not stated |
| Minimum | Not stated |
| Hold | 5 years (sale in Year 5) 🟢 |
| Raise / capitalization | Not stated |
| Claimed return | 14% IRR, projected. Gross or net-to-LP not stated 🔴 |
| Distributions | None until sale. 100% of return realized at exit 🟢 |

The distribution profile is informative in its own right. Stabilized multifamily usually pays 5–8% cash-on-cash after stabilization (`01` → Multifamily value-add). Zero interim distributions means one of three things:
- the property's cash flow is being absorbed (heavy renovation, lease-up, or ground-up development);
- it is being consumed by debt service;
- it is being retained by the GP.

Each is a different deal. If this is **development**, the `01` target is 18–22% net, so 14% would be *under*-compensated for development risk. If it is **value-add**, 14% sits inside the 12–18% target band. 🟡

### 2. Return Stress-Test

Comparator per the routing table: **VNQ, 4.92% 10yr**, with the NCREIF NPI unlevered overlay. Hold 5 years → illiquidity hurdle **~300–400 bps** (`05`). Treasury floor: 10yr **5.18%** (`05`, 2026-09-24).

| Case | Net-to-LP IRR | vs VNQ (4.92%) | vs 10yr UST (5.18%) | Read |
|---|---|---|---|---|
| **Base — 14% is already net** | 14.00% | +908 bps | +882 bps | Clears comfortably (script) |
| **Base — 14% is gross, market-norm fee stack** (2% acq, 1.5% AM, 1% dispo, 0.3% admin, 20% over 8% pref, 100% catch-up) | ≈9.32% | +440 bps | +414 bps | Clears, but only by ≈40–140 bps over the hurdle (script) |
| **Bear — exit proceeds 20% below plan** (gross 9.0%, same fee stack) | ≈5.05% | +13 bps | **−13 bps** | **Fails.** A risk-free Treasury out-earns the LP |
| **Bear — exit proceeds 30% below plan** (before fees) | ≈6.15% gross | — | — | Net would sit below the Treasury |
| **Bear — sale slips 2 years, same proceeds** | ≈9.8% (before fees) | — | — | The lock-up grows to 7 years, so the hurdle rises to ~400–600 bps |

**Swing assumptions:**
1. **Exit cap rate.** It is the whole deal here. Not disclosed.
2. **Rent growth to the Year-5 NOI** that the buyer capitalizes. Not disclosed.
3. **Exit timing / debt maturity.** A 5-year hold with no stated debt term (`GEN-09`, `GEN-10` unassessable).

The headline clears the benchmark in every base case. It fails in a plausible bear case, and in Deal B nothing in the interim cushions that bear case. 🟡 (Scenario IRRs are illustrative; they are computed from the stated 14% / Year-5 shape, not from a pro forma.)

### 3. Where LP Returns Come From

- **Cash flow: 0%. Exit: 100%.** This is stated, not inferred 🟢. It is far past the 60% threshold, so **`GEN-08` fires as RED** by the deal's own description.
- At 14% over 5 years with one exit payment, the LP needs ≈**1.93x** at sale. Every dollar of profit depends on the buyer's price in Year 5.
- **Unlevered overlay:** NCREIF NPI is **5.00%** trailing, almost entirely income (1.17% of the latest 1.29% quarter). Deal B inverts that profile: 0% income, 100% terminal value. A 14% levered return against a ~5% income-driven unlevered baseline means ~9 points are coming from leverage and assumed appreciation. Deal B shows the market no in-place income to anchor them. This is the **financing-story** pattern (`GEN-07`): it is inferred, not confirmed, because leverage and the exit cap are undisclosed. It stays RED until the GP produces an unlevered, in-place return (`Q-DS-02`). 🟡
- `EQUITY-06` (exit cap below going-in) cannot be tested because neither cap rate is disclosed. In an all-exit deal it is the first thing to check.

### 4. Fee Stack Summary

**Gross-to-net drag: not computable from disclosure. That is the finding (`GEN-16`).**

| Input | Status |
|---|---|
| Acquisition, asset mgmt, disposition, admin, loan placement / refi | Not disclosed |
| Pref / promote / catch-up / waterfall type | Not disclosed |

- Script run with every undisclosed fee passed as `0` → 0 bps drag. That number is meaningless: it reflects missing data, not a clean deal.
- **Illustrative only:** a market-norm stack from `02` on a 5-year hold → **≈468 bps/yr** of drag (180 recurring + 60 one-time + 228 promote). A 14% *gross* becomes ≈9.3% net. Every input here is ASSUMED, so each one is a §6 gap.
- **B-specific fee issue:** with no distributions, how is the annual asset-management fee paid? It could come out of property cash flow (reducing what builds toward exit), or it could accrue against the LP's capital account. Both reduce the exit check, and neither is visible.

### 5. Red Flags

**RED**
- **`GEN-08` — Exit-dependent IRR.** 100% of the return comes at exit; the LP has received nothing if the Year-5 sale disappoints or slips. Stated 🟢.
- **`GEN-07` — Financing story (inferred).** 14% against a ~5% unlevered income-driven baseline, with zero in-place income distributed. The return likely depends on leverage plus exit pricing. Inferred 🟡, unresolved until the unlevered return is disclosed. With `GEN-08` this is the financing-story cluster; `EQUITY-06` is the likely third member but can't be tested (no cap rates).
- **`GEN-09` — Debt maturity vs hold (unassessable).** A 5-year hold is stated but the debt term is not. If the loan matures before the sale, the LP is forced into a refi or a sale at maturity. It is probed now per the proactive trigger, not waived.
- **`GEN-10` — Rate-cap expiry (unassessable).** It is unknown whether the debt floats. In a deal with no interim cash flow, a debt-service spike after cap expiry has no distribution buffer to absorb it. It goes straight to a capital call or a forced sale.
- **`GEN-05` / `GEN-14` — Track record not presented at all.** No sponsor is named. Nothing is verified.
- **`GEN-01` — Co-invest not disclosed.** Treat it as RED until answered.

**YELLOW–RED**
- **`GEN-16` — No fee or waterfall disclosure.** The drag is unknowable (§4).
- **`GEN-15` — Missing financials.** No rent roll, T-12, or debt terms. This is also why Deal B's zero-distribution profile can't be explained from the data.
- **`EQUITY-04` / `EQUITY-05` — Pref undisclosed.** Deal B depends on this more than most: with no distributions, **every dollar of pref accrues**. A non-cumulative pref would forfeit five years of pref, and a simple pref would forgo the compounding the LP is owed on a 5-year deferral.
- **`EQUITY-01` / `EQUITY-02` / `EQUITY-03` — Waterfall structure, clawback, and catch-up undisclosed.** The catch-up rate decides how much of the single exit check goes to the GP before the residual split.
- **`EQUITY-07` — Refi dependence (unassessable).** Any capital return before Year 5 would require a refi; none is described.
- **`GEN-06` — Affiliate fees (unassessable).** The fee disclosure needed to test this is absent.

**YELLOW**
- **`GEN-11` — J-curve.** The schedule *is* disclosed at headline level ("none until sale"), so the non-disclosure trigger is only partly met. The mechanism the flag describes is fully present, though: all return risk sits at exit. The flag's substance is carried by `GEN-08`. No milestones or sale gates are given (`Q-DIST-01`).
- **`GEN-13` — No sensitivity or downside case.** A single-point 14%.
- **`GEN-17` — Essential multifamily disclosures absent** (`01`: exit cap with sensitivity, debt structure/maturity, refi assumptions, exit track record).
- **`GEN-18` — Rent-growth assumption to Year 5.** No submarket is given, so it can't be tested.

### 6. Missing Disclosures

Per `01` (Multifamily) and `02` (Equity syndications), Deal B omits:
- **Return basis:** whether 14% is gross or net-to-LP; the equity multiple; the IRR at a flat exit cap.
- **Exit:** going-in cap, exit cap, and exit-cap sensitivity. This is the deal's only return source.
- **Debt:** amount/LTV, fixed vs floating, rate cap and its expiry, maturity vs the Year-5 sale, extension options.
- **Operations:** rent roll, T-12 actuals, and the reason distributions are withheld (renovation, lease-up, development, or debt service).
- **Fees:** full inventory (acquisition, asset mgmt, disposition, loan placement, refi, admin) and whether fees accrue or are paid currently.
- **Waterfall:** pref rate; cumulative or not; simple or compounding; catch-up; splits; deal-by-deal vs whole-of-fund; clawback.
- **Sponsor:** identity, prior **multifamily exits** net-to-LP, co-invest.
- **Offering:** minimum, raise size, geography/submarket, capital-call provisions, LP liquidity options.

### 7. GP Alignment

- **Co-invest:** not disclosed; unverified 🔴.
- **Track record:** none presented. No realized net-to-LP record means **no track record** (`GEN-14`, `GEN-05`) 🔴.
- **Waterfall alignment:** unknown. In an all-exit deal the promote is paid entirely from the one sale event. If the waterfall is deal-by-deal with a 100% catch-up and no clawback, the GP's economics are protected at the exact point where the LP's are most exposed.
- **Affiliate fees:** unknown. A no-distribution structure makes affiliate fees *harder* to see, because they are paid out of cash flow the LP never sees.

### 8. Questions for the GP

**Must-ask**

| ID | Question (as applied to Deal B) | Bad-answer signal |
|---|---|---|
| Q-DS-01 (`GEN-08`, `EQUITY-06`) | What share of the 14% comes from exit (all of it, by your description), and what is the IRR at a flat exit cap? | Can't decompose; "real estate always appreciates"; the IRR falls below pref at a flat exit cap. |
| Q-EXIT-01 (`EQUITY-06`) | What are the going-in and exit caps, and the IRR at exit cap ≥ going-in? | Exit cap below going-in with "cap rates will compress"; no sensitivity. |
| Q-DS-02 (`GEN-07`) | Strip out leverage and cap-rate compression: what is the unlevered, in-place return? And why is none of the property's cash flow distributed? | Only the levered IRR exists; "leverage is just how the deal works"; no explanation of where the operating cash goes. |
| Q-DS-03 (`GEN-13`) | What is the return under a bear case: flat rents, higher exit cap, sale delayed 2 years? | Single-point pro forma; "we underwrite conservatively"; the bear case is still a gain. |
| Q-DIST-01 (`GEN-11`) | What gates the Year-5 sale? Is there any milestone before then at which capital or pref is paid? What if the sale is deferred? | "We'll distribute when the deal supports it"; no sale trigger; open-ended extension right. |
| Q-RISK-01 (`GEN-09`) | When does the debt mature relative to the Year-5 sale, and what is the extension plan? | Maturity inside the hold; "we'll refinance" with no terms. |
| Q-RISK-02 (`GEN-10`) | Is the debt floating? When does the rate cap expire, and what does extending it cost at current pricing? | Cap expires before maturity; extension cost not modeled; "rates should be lower by then." |
| Q-RISK-03 (`GEN-12`, `GEN-15`) | Provide the T-12, rent roll, and complete debt terms. | T-3/T-6 only; "confidential until you commit." |
| Q-FEE-01 (`GEN-16`) | Provide the full fee schedule and waterfall. Are fees paid currently or accrued against LP capital? | "Standard market fees"; "the PPM has it" without producing it. |
| Q-FEE-04 (`EQUITY-04`, `EQUITY-05`) | What pref do LPs receive? Is it cumulative and compounding over the 5-year deferral? | Pref <6% or none; non-cumulative (five years of pref forfeited); simple-only with no compounding. |
| Q-FEE-03 (`EQUITY-01`, `EQUITY-02`, `EQUITY-03`) | Deal-by-deal or whole-of-fund? Clawback? What catch-up rate at exit? | Deal-by-deal, high promote, no clawback; can't explain the catch-up. |
| Q-FEE-02 (`GEN-06`) | Which service providers are GP-affiliated, and what do they charge? | "All arm's-length" without naming providers. |
| Q-GP-01 (`GEN-01`) | How much of your own cash is in this deal, pari-passu? | "Sweat equity"; fee waiver presented as co-invest. |
| Q-GP-02 (`GEN-05`, `GEN-14`) | Restate your track record as net-to-LP IRR on realized multifamily exits only. | Project-level IRR only; "most deals are still performing." |
| Q-GP-03 (`GEN-02`) | Any regulatory action, enforcement, or investor litigation? | "Nothing material"; a search surfaces something undisclosed. |
| Q-MKT-01 (`GEN-18`) | What submarket supply and absorption data support the Year-5 NOI? | Metro-level optimism; no supply pipeline acknowledged. |
| Q-LIQ-01 | If I need out before Year 5, what are my options? | "A secondary market may develop." With zero distributions, the LP has no liquidity at all before the sale. |
| Q-EXIT-02 (`EQUITY-07`) | Does any capital return or pref payment depend on a refi? | Capital return requires a refi at lower rates; no fallback. |

**Nice-to-ask:** Q-DIST-02 (capital calls: with no distributions, a shortfall can only be funded by a call); Q-GP-04 (`GEN-04`, team scale); Q-LIQ-02 (K-1 timing).

### 9. Diligence Checklist

- PPM and operating agreement: waterfall, pref accrual, fee accrual mechanics, extension / sale-deferral rights, capital-call dilution terms.
- Lender term sheet: maturity, rate cap and expiry, extension conditions.
- Independent exit-cap and sales comps for the submarket; appraisal.
- Rent roll and T-12 (verify why no cash flow is distributable).
- Sponsor background: SEC/FINRA/state records, litigation search, references from LPs in **exited** deals.
- Supply pipeline for the submarket to Year 5.

### 10. Verdict — Deal B

**Pass as presented — insufficient disclosure.**
- Deal B's return story rests entirely on one exit number, and none of the inputs that set that number are disclosed: exit cap, debt, rent growth, fees, waterfall, sponsor. The core story cannot be underwritten, so a merits verdict isn't possible.
- **Biggest swing factor:** the Year-5 exit cap. A 20% miss on exit proceeds under a market-norm fee stack takes the LP from ≈9.3% to ≈5.05% net, below the 10yr Treasury.
- **Re-screen list:** net-vs-gross basis; going-in and exit caps with sensitivity; debt terms, including maturity and rate-cap expiry; the reason for zero distributions; full fees and waterfall, including whether the pref is cumulative/compounding; sponsor identity and realized multifamily exits net-to-LP; co-invest.
- **Who it could suit, if re-screened clean:** an LP with no income need and a genuine 5+ year horizon. The LP must be able to absorb a slip past Year 5, and must want a deferred, lump-sum outcome. It needs a cumulative, compounding pref, debt that matures beyond the sale with a covered rate cap, and an exit cap at or above going-in.

---

## A vs B — the comparison you asked for

Equal headline IRRs are not equal deals. IRR describes the average rate; it says nothing about *when* the cash arrives. That timing decides how much of the 14% is at risk until the very end.

### Side by side

| | Deal A | Deal B |
|---|---|---|
| Headline IRR | 14% | 14% |
| Distributions | 7% CoC quarterly from Year 1; capital returned progressively 🟢 | None until the Year-5 sale 🟢 |
| Share of profit from exit | ≈57% or less 🟡 (below, if capital returns progressively) | **100%** 🟢 |
| `GEN-08` (>60% from exit) | Near but below threshold; confirm with a schedule | **Fires (RED)** |
| Required equity multiple at 14% | ≈1.81x 🟡 | ≈1.93x 🟡 |
| Capital at risk at Year 4 | Reduced by ≈28%+ of cash already received 🟡 | 100% of capital, plus all accrued return |
| Interim liquidity | Quarterly cash | None (`Q-LIQ-01`) |
| Main questions it raises | *How* is capital returned progressively: operations or refi (`EQUITY-07`, `Q-EXIT-02`)? Is 7% CoC covered by NOI or paid from reserves or capital? | Why is no cash flow distributed? What sets the exit (`GEN-07`, `GEN-08`, `EQUITY-06`)? |

*Deal A is modeled as 7% annual cash-on-cash plus a terminal payment that solves to 14%. That is a simplification; if capital returns progressively as stated, A's exit share is lower still.* 🟡

### Same shortfall, different outcome (before fees, illustrative 🟡)

| Scenario | Deal A IRR | Deal B IRR | Gap |
|---|---|---|---|
| Plan | 14.0% | 14.0% | — |
| Exit proceeds −10% | 12.0% | 11.6% | ~35 bps |
| Exit proceeds −20% | 9.8% | 9.0% | ~80 bps |
| Exit proceeds −30% | 7.4% | 6.2% | ~125 bps |
| Exit proceeds −50% | 1.8% | **−0.8% (loss)** | ~260 bps |
| Sale slips 2 years, same proceeds | ≈11.0% (A keeps paying 7%) | ≈9.8% | ~120 bps |

The gap widens as the exit gets worse. In a mild miss the two deals look similar. In a real downturn, Deal A has already returned ~35% of capital as cash and Deal B has returned nothing. In an exit-driven deal the losses are concentrated in exactly those downturn scenarios.

### Why B shows a *higher* multiple and still carries more risk

Deal B needs ≈1.93x to hit 14%, against Deal A's ≈1.81x. B's larger multiple is not a better deal. It is the extra compounding the LP is owed for leaving 100% of capital exposed for the full five years. If a GP markets B on its higher equity multiple, that is a reason to ask more questions, not fewer.

### What would change the ranking

- **Deal A's 7% is not covered by operations.** If it is paid from reserves, from raised capital, or from a refi (`EQUITY-07`), A's "early cash" is partly the LP's own money returned. That would narrow A's advantage sharply. Ask for the T-12 and NOI coverage of the distribution.
- **Deal B has a cumulative, compounding pref and a conservative exit cap** (≥ going-in), with debt maturing past Year 5 and a covered rate cap. That would make B a defensible deferred-return deal for an investor with no income need, though still more concentrated than A.
- **Deal B is development.** Then 14% is below the 18–22% `01` target for that risk, and B looks worse, not equivalent.
- **Fees.** Neither deal discloses them (`GEN-16` on both). A 14% gross is roughly 9.3% net under a market-norm stack, and that applies to both deals. Differences in fees could outweigh the timing difference.

### Comparative verdict

**On the facts given, Deal A is preferable to Deal B at the same 14% headline.** A's return is roughly half cash flow and half exit; B's is all exit (`GEN-08`). A gives the LP liquidity and returns part of the capital before the sale; B leaves all of it exposed until one event in Year 5.

That is a *relative* ranking, not a pursue on A. Neither deal discloses enough to underwrite: fees, waterfall, debt, exit cap, and sponsor are missing from both.

Deal B's standalone verdict is **Pass as presented — insufficient disclosure**. Deal A should clear the same disclosure bar, with its specific probe answered: is the 7% covered by operations, and how is capital returned?
