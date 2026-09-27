# Eval fixture 08 — Multifamily syndication, flag cluster
*Iteration-5 run, 2026-09-27, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 7712624.*

**Verdict: Pass.** This is a verdict on the terms you were given, not a "missing information" pass. The deal has five REDs you can see directly: the GP puts in no money, a principal has a prior SEC action, the GP takes a 50% promote with no clawback, the rate cap expires before the loan does, and the track record is all unrealized. A better OM wouldn't fix any of them. Only the GP changing the terms would.

---

## 1. Deal Snapshot

| Field | Value | Confidence |
|---|---|---|
| Asset class | Multifamily (value-add vs core: **Not stated**) | 🟢 class / 🔴 sub-class |
| Deal type | Equity syndication, single asset | 🟢 |
| Sponsor | Not named; one principal named in a prior SEC action | 🟢 |
| GP co-invest | **None**. "Our expertise is our investment" | 🟢 |
| Geography | Not stated | — |
| Minimum investment | Not stated | — |
| Hold period | Not stated | — |
| Raise size | Not stated | — |
| Claimed return (IRR / multiple / CoC) | Not stated as a number; projections show an **upside case only** | 🟢 |
| Waterfall | American (deal-by-deal), **50% promote**, **no clawback**; pref and catch-up **Not stated** | 🟢 / 🔴 |
| Debt | Floating rate; **rate cap expires in ~12 months (≈Sep 2027)**; loan matures **2028** | 🟢 |
| Track record | All current, **unrealized marks** | 🟢 |
| Other fees (acquisition, AM, disposition, financing, admin) | Not stated | — |

## 2. Return Stress-Test

The deal gives no return to test and no downside case (`GEN-13`). So this section tests the **structure** and uses illustrative inputs. Every input marked 🔴 is an assumption, not a disclosed term.

**The swing factors:**
1. **Rate path through the uncapped window.** From about Sep 2027 until the 2028 maturity, debt service floats with nothing capping it. This is the `GEN-10` pattern.
2. **Refi / exit conditions in 2028.** Maturity forces a refinance or sale into whatever market exists then (`GEN-09`, `EQUITY-07`).
3. **Exit cap.** It isn't disclosed, and for value-add multifamily it is "the single biggest swing in most pro formas" (`01`).

| Case | What has to happen | LP outcome |
|---|---|---|
| **Bull (the only case the GP shows)** | Rates fall or stay flat, the refi or sale lands in 2028 on good terms, and the exit cap holds | The GP's upside case, before a 50% promote |
| **Base** | Rates stay near today's curve (10yr ≈5.18%, `05`). The cap has to be re-bought at market or the loan floats unhedged. Refi proceeds are constrained | Distributions shrink in the uncapped window. The 50% promote still takes half of whatever profit remains |
| **Bear** | Cap expires, rates stay elevated, refi is frozen at the 2028 maturity. This is the 2022–24 path (`03` Provenance) | Distributions suspended, capital call or forced sale, LP equity impaired. No GP capital shares the loss (`GEN-01`) |

**What the 50% promote alone costs the LP** (from `scripts/fee_drag_calculator.py`). Assumed inputs, all 🔴: 15% gross IRR, 5-year hold, 8% pref, 100% catch-up.

| Scenario | Net LP IRR | Drag | vs VNQ 4.92% (5-yr hurdle ~300–400 bps) |
|---|---|---|---|
| 20% promote, no other fees (market reference) | 12.59% | 241 bps | +767 bps: **clears comfortably** |
| **50% promote, no other fees** | **8.53%** | **647 bps** | +361 bps: **clears only thinly** |
| 50% promote + a typical `02` fee stack (2% acq, 1.5% AM, 1% dispo, 0.3% admin), all 🔴 assumed | **6.13%** | **887 bps** | +121 bps: **fails** the illiquidity hurdle |

- Even if the property delivers a 15% gross, the promote alone cuts the LP to about 8.5%. The 5-yr hurdle band is 300–400 bps, and this premium sits in the lower half of it. It is also only ≈335 bps over the 10yr Treasury (5.18%), which `05` says is currently the tighter floor.
- With a normal fee stack on top, the LP ends up with about 6%, less than 100 bps over a risk-free Treasury. That is before any debt stress at all.
- Two things make the hurdle higher, not lower. This is a **single asset** (concentration: VNQ is a basket, this is one property), and private RE has wide dispersion (`05` illiquidity framework).

## 3. Where LP Returns Come From

**Can't tell from this, and that gap is itself a finding.** The deal gives no split between in-place cash flow and exit, no exit cap vs going-in cap, and no unlevered return. What the structure does show 🟡:

- **The floating-rate debt gives in-place cash flow no protection once the cap expires.** Any operating income is first in line to cover higher debt service after ≈Sep 2027.
- **The 2028 maturity makes a capital event mandatory.** Unless the hold ends before 2028, the LP's capital comes back through a refi or a sale.
- A bull-only pro forma for floating-rate multifamily is exactly the kind of projection the `05` unlevered overlay tests. The NCREIF NPI unlevered return is about 5.00%, almost all income. Anything the GP projects above that comes from leverage plus assumed appreciation.

`GEN-07`, `GEN-08` and `EQUITY-06` (the financing-story family) are **not fired**. The deal hasn't disclosed the exit cap or the return split, so firing them would rest on an assumption. They go to must-asks `Q-DS-01`, `Q-DS-02` and `Q-EXIT-01`. If the answers show more than 60% of the return comes from the exit, or an exit cap below the going-in cap, those flags fire and add to the Pass.

## 4. Fee Stack Summary

| Fee | Disclosed | `02` norm | Read |
|---|---|---|---|
| Promote | **50%** | 15–30%; aggressive above 30% | 🟢 **Well above the aggressive threshold** |
| Preferred return | Not stated | 6–10% cumulative | A missing pref is an `EQUITY-04` probe |
| Catch-up | Not stated | 50–100% | Probe (`EQUITY-03` if 100%) |
| Acquisition fee | Not stated | 1–2% of equity | Undisclosed |
| Asset management | Not stated | 1–2% of equity per year | Undisclosed |
| Disposition | Not stated | 0.5–1% of sale price | Undisclosed |
| Loan placement / refi | Not stated | 0.5–1.5% of the loan per event | Undisclosed. **Matters here because the 2028 maturity forces a financing event** |
| Admin / IR | Not stated | 0.1–0.5% or $1–3k per LP | Undisclosed |
| Affiliate fees (property management, construction management) | Not stated | — | `GEN-06` probe |

**Gross-to-net drag: can't be calculated from what's disclosed (`GEN-16`).** The only fee that can be quantified is the promote: **≈647 bps per year** under the §2 assumptions, versus ≈241 bps at a 20% promote. With a typical stack the illustrative total is **≈887 bps per year**. Every input other than the 50% promote is an assumption, and each one is a §6 gap.

## 5. Red Flags

**RED**
- **`GEN-01`: No GP co-investment** 🟢. "Our expertise is our investment" is almost word for word the bad answer to `Q-GP-01` ("our sweat equity is our investment"). The GP earns fees and a 50% promote whatever happens to the LP, and has no capital of its own to lose.
- **`GEN-02`: Prior SEC action against a principal** 🟢. A regulatory history signals a pattern of harm to investors or failures in compliance. Treat this as pass-or-resolve: you need the full record, not the GP's summary of it.
- **`EQUITY-01` + `EQUITY-02`: American waterfall, 50% promote, no clawback** 🟢. These are the RED pairing from `03` (deal-by-deal structure, high promote, nothing to give back). This is a single asset, so the whole-of-fund vs deal-by-deal distinction is narrower here. The clawback gap still matters wherever promote is paid out of interim cash or refi proceeds before the final sale. The GP banks that promote, and if the 2028 exit then impairs capital, nothing comes back to the LP. The 50% promote is also far past `02`'s aggressive threshold of 30%.
- **`GEN-10`: Rate cap expires before the loan matures** 🟢. The cap expires ≈Sep 2027 and the loan matures in 2028. That leaves the loan floating without a hedge until maturity, and then it has to be refinanced at maturity. This is the specific 2022–24 sequence: cap expires, rates stay elevated, the refi market freezes, debt service spikes, distributions stop and a capital call follows. `02`/`03` Provenance names it as the source of many multifamily-syndication wipeouts.
- **`GEN-14`: Track record is unrealized only** 🟢. Marks are self-reported and unproven, and the GP hasn't shown it can exit and return capital. Under the skepticism contract, a marks-only record counts as **no track record** (`GEN-05` applies too: nothing here is net-to-LP on realized deals).

**YELLOW–RED**
- **`GEN-09`: The debt matures inside a hold that hasn't been disclosed** 🟡. A 2028 maturity with no stated hold means a refi or sale is probably forced into whatever market exists at maturity. Probe it via `Q-RISK-01` now; don't wait for the GP to disclose the hold.
- **`EQUITY-07`: The plan likely depends on a refi** 🟡. This follows from the maturity above. If the plan depends on refinancing in 2028, a frozen refi market suspends distributions.
- **`GEN-16`: Fee and waterfall disclosure is incomplete** 🟢. The only fee term disclosed is the promote.
- **`GEN-15` / `GEN-17`: Financials and essential disclosures are missing** 🟢. The rent roll, T-12, exit cap and full debt terms are all absent (see §6).
- **`EQUITY-04`: Pref not stated** 🔴. Treat the pref as absent until the GP shows one.

**YELLOW**
- **`GEN-13`: Upside case only** 🟢. A pro forma with only a bull case hides how fragile the return is. For floating-rate debt with a cap about to expire, the downside is the whole question.
- **`GEN-11`: No distribution schedule** 🟢. There is no timing for when LP capital comes back.
- **`GEN-03`: Marketing over substance** 🟡. An upside-only deck with no underwriting detail fits this pattern.

**Clusters**
- **GP alignment and conduct:** `GEN-01` + `GEN-02` + `GEN-14` (+`GEN-05`). No capital at risk, a regulatory history, and no realized proof the GP can return capital. Any one of these is RED. Together they leave **no evidence the GP is aligned with LPs or can perform for them**.
- **The debt failure sequence:** `GEN-10` + `GEN-09` + `EQUITY-07`, made worse by `GEN-13`. The GP shows only an upside case, and the risk the deal actually carries is a downside one.
- **Economics that favor the GP:** a 50% promote + `EQUITY-01`/`EQUITY-02` + zero co-invest (`GEN-01`). The GP can profit substantially without putting in capital or being exposed to the loss.

## 6. Missing Disclosures

Against the `01` multifamily value-add essential disclosures and the `02` equity-syndication fee inventory:

- **Rent roll** and **T-12 actuals** (`GEN-15`)
- **Pro forma exit cap with sensitivity**, and the going-in cap for comparison (`EQUITY-06` probe)
- **Full debt terms**: spread over the index, current all-in rate, loan balance/LTV, extension options and their conditions, cap strike, and the cost to replace the cap
- **Refi assumptions** for 2028
- **Hold period**
- **Projected return**: net-to-LP IRR, equity multiple, cash-on-cash
- **Downside or base case** (`GEN-13`)
- **Distribution schedule** (`GEN-11`)
- **Preferred return rate, and whether it is cumulative/compounding**, plus the catch-up rate
- **The complete fee schedule**: acquisition, AM, disposition, financing, admin, affiliate
- **GP track record on prior multifamily *exits***, realized and net to LP
- **The substance and resolution of the SEC action**
- **Sponsor identity, geography, minimum investment, raise size**
- **LP liquidity terms / secondary options** (`Q-LIQ-01`)

## 7. GP Alignment

| Axis | Finding | Confidence |
|---|---|---|
| Co-invest | **None.** "Expertise" is not capital. There is no pari-passu dollar at risk | 🟢 |
| Track record | **Unverified.** Marks only, nothing realized, no figures net to LP. Treat it as no track record | 🟢 |
| Regulatory history | **Adverse.** A principal was named in a prior SEC action; the substance is unknown | 🟢 fact / 🔴 substance |
| Waterfall alignment | **Poor.** A 50% promote with no clawback, and the pref is undisclosed. The GP is paid well on upside and loses nothing on downside | 🟢 |
| Affiliate fees | Unknown (`GEN-06` probe) | — |

**Net read:** every alignment lever runs toward the GP. The GP has no downside, and a 50% promote means it doesn't even need a big win to be well paid.

## 8. Questions for the GP

**Must-ask** (each one's flag has fired, or it guards a term the deal states):

| ID | Question | Bad-answer signal | Flag |
|---|---|---|---|
| `Q-GP-03` | "Have you or your principals faced any regulatory action, enforcement, or investor litigation?" | Deflects to "nothing material"; blames the regulator; an independent search turns up more than they disclosed | `GEN-02` |
| `Q-GP-01` | "How much of your own capital is in this deal, on the same terms as LPs?" | **Already given:** "our expertise is our investment." Also: co-invest that is really a fee waiver; a token amount on better terms than LPs | `GEN-01` |
| `Q-GP-02` | "Can you restate your track record as net-to-LP IRR on fully realized, exited deals only?" | Only project- or GP-level IRR; "most deals are still performing"; can't separate realized from marked | `GEN-14`, `GEN-05` |
| `Q-RISK-02` | "When does the rate cap expire relative to debt maturity, and what's the cost to extend it at current pricing?" | Extension cost not modeled; "rates should be lower by then"; no budgeted reserve for replacing the cap | `GEN-10` |
| `Q-RISK-01` | "When does the debt mature relative to the projected hold, and what's the refinance or extension plan?" | "We'll refinance" with no terms; no plan if the refi market is shut; extension options with conditions the deal can't meet | `GEN-09` |
| `Q-EXIT-02` | "Does the business plan depend on a refinance, and what happens to distributions if the refi isn't available on the assumed terms?" | Capital return requires a refi at lower rates; no fallback; "the refi market will reopen" | `EQUITY-07` |
| `Q-DS-03` | "What is the return under a bear case: flat rents, higher exit cap, no refinance?" | No downside exists; "we underwrite conservatively" with nothing to show; the "bear case" is still a gain | `GEN-13` |
| `Q-FEE-03` | "Is the waterfall deal-by-deal or whole-of-fund, and is there a clawback?" | **Already given:** deal-by-deal with a high promote and no clawback. Also: can't explain the catch-up; "you get paid when we get paid." Follow up: why 50%? | `EQUITY-01`, `EQUITY-02` |
| `Q-FEE-04` | "What preferred return do LPs receive before the GP earns promote, and is it cumulative and compounding?" | A pref below 6% or none at all; non-cumulative | `EQUITY-04`, `EQUITY-05` |
| `Q-FEE-01` | "Can you provide the complete fee schedule and the full distribution waterfall?" | "Standard market fees"; "the PPM has it" without producing it | `GEN-16` |
| `Q-FEE-02` | "Which service providers are GP-affiliated, what do they charge, and are those rates third-party-benchmarked?" | "All arm's-length" without naming anyone; no benchmark | `GEN-06` |
| `Q-RISK-03` | "Can you provide trailing-twelve-month actuals, the rent roll, and complete debt terms?" | T-3/T-6 only; "the financials are confidential until you commit" | `GEN-15`, `GEN-12` |
| `Q-DS-01` | "What share of projected LP IRR comes from in-place cash flow versus the exit, and what's the IRR at a flat exit cap?" | Can't or won't break the IRR down; "real estate always appreciates"; the IRR falls below the pref at a flat cap | `GEN-08`, `EQUITY-06` |
| `Q-DS-02` | "Strip out leverage and cap-rate compression. What is the unlevered, in-place return?" | No unlevered view exists; "leverage is just how the deal works" | `GEN-07` |
| `Q-EXIT-01` | "Why is the exit cap below the going-in cap (if it is), and what's the IRR at an exit cap equal to or above going-in?" | "Cap rates will compress"; the IRR breaks at a flat cap | `EQUITY-06` |
| `Q-DIST-01` | "What is the projected distribution schedule, and at what milestones does LP capital start returning?" | "We'll distribute when the deal supports it"; no milestones | `GEN-11` |
| `Q-LIQ-01` | "What are my options if I need to exit before the hold period ends?" | "A secondary market may develop"; the lock-up is left vague | — |
| `Q-MKT-01` | "What submarket supply pipeline and absorption data support the rent-growth assumption?" | Metro-level optimism; no supply pipeline acknowledged | `GEN-18` |

**Nice-to-ask:** `Q-GP-04` (team capacity vs AUM), `Q-DIST-02` (capital-call mechanics; escalate to must-ask here, because the bear case in §2 runs through a capital call), `Q-LIQ-02` (K-1 timing).

## 9. Diligence Checklist

- **Regulatory background, done independently:** SEC enforcement records and litigation releases, FINRA BrokerCheck, state securities regulators, and court dockets for every principal. Don't rely on the GP's description.
- **The loan documents:** maturity date, extension options and their tests (DSCR/debt yield), the cap agreement (strike, expiry), and any requirement to buy a replacement cap. **Get a lender's quote to replace the cap at current pricing.**
- **The PPM/operating agreement:** full waterfall, pref terms, catch-up, fee schedule, affiliate arrangements, capital-call and dilution provisions, and how GP removal works.
- **Realized track record:** prior exits confirmed against closing statements or K-1s from prior LPs, and references from LPs in *exited* deals.
- **Property financials:** rent roll, T-12, and an independent check of occupancy and rents against submarket comps.
- **Appraisal / valuation:** the current as-is value vs the loan balance, which tells you whether a 2028 refi is feasible at today's cap rates.

## 10. Verdict

**Pass.** This verdict rests on the disclosed terms, not on what's missing.

**Reasoning.** The screen fails on facts you stated, not on gaps.
- The GP risks **no capital** (`GEN-01`), carries a **regulatory history** (`GEN-02`), and has **no realized exits** to show it can return capital (`GEN-14`).
- It takes a **50% promote with no clawback** (`EQUITY-01`/`EQUITY-02`). That is far above the `02` norm. Under illustrative assumptions it cuts a 15% gross to about 8.5% net before any other fee, and to about 6% with a typical stack. At about 6% the deal fails the illiquidity hurdle over VNQ and barely beats a risk-free 10yr Treasury.
- The debt carries the textbook 2022–24 failure mode: a **rate cap expiring about a year before a 2028 maturity** (`GEN-10`, `GEN-09`). The deal shows an **upside case only** (`GEN-13`) against it.
- Any one of these REDs is pass-or-resolve. Five together, spread across GP conduct, economics and debt, make a merits Pass.

**Biggest swing factor:** the rate path and the refi market between the cap expiry (≈Sep 2027) and the 2028 maturity. The downside lands entirely on LP capital, and the GP has nothing at risk.

**Who it could suit:** no passive LP on these terms. Only an investor who has independently cleared the SEC matter and is knowingly speculating on falling rates would consider it. Even that investor is paying a 50% promote for the bet.

**What would have to be true to re-screen:**
1. The SEC matter is independently shown to be immaterial, resolved, and unrelated to investor harm.
2. The GP commits meaningful cash co-invest on pari-passu terms.
3. The promote comes down into the `02` range (≤30%), with a stated cumulative pref of at least 6% and a clawback or escrow on any promote paid from interim cash or refi proceeds.
4. A replacement or extended rate cap through maturity is funded (or reserved) at current pricing, and there is a credible 2028 refi/extension plan with a bear case showing LP capital survives it.
5. There is a realized, net-to-LP track record on exited multifamily deals.

Items 1 and 2 are pass-or-resolve on their own. If either fails, the other three don't matter.
