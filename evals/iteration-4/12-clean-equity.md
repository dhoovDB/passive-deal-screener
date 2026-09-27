# Eval fixture 12 — Clean multifamily value-add syndication
*Iteration-4 run, 2026-09-27, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 1c7faff.*

**Verdict: Pursue.** The structure is well aligned with LPs on every axis this screen tests: cash co-invest on pari-passu terms, a whole-of-fund waterfall with a secured clawback, an 8% cumulative compounding pref, market fees, realized net-to-LP track record, fixed-rate debt that matures after the exit, a flat exit cap, and full financials with a downside case. No RED flag fires. The one open YELLOW is `GEN-11`: no distribution schedule, and in fact no target return or hold period was stated at all. **The biggest swing factor is the value-add NOI lift.** With a flat exit cap and fixed-rate debt, cap-rate compression and refi risk are off the table, so the LP is betting on the GP's ability to grow NOI. Next steps are confirming the rent-growth assumption and getting the headline target return, hold, and distribution schedule in writing.

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Multifamily — value-add 🟢 |
| Deal type | Equity syndication (single asset implied) 🟢 |
| Sponsor | Not stated |
| Geography / submarket | Not stated |
| Minimum investment | Not stated |
| Hold period | Not stated. Exit is "planned," with debt maturing 2 years after it. Category norm is 5–7 yrs (`01`) 🟡 |
| Raise / equity size | Not stated |
| Claimed return (IRR / multiple / cash-on-cash) | **Not stated** |
| Pref / promote | 8% cumulative, compounding / 20% 🟢 |
| Waterfall | Whole-of-fund (European), secured clawback 🟢 |
| GP co-invest | 10% of equity, cash, pari-passu 🟢 |
| Fees | 1% acquisition, 1.5% asset mgmt (annual), 1% disposition 🟢. Fee bases, catch-up, admin/IR, and loan-placement fees not stated |
| Debt | Fixed rate, maturity 2 yrs after planned exit 🟢. LTV/LTC, rate, amortization, and prepayment terms not stated |
| Exit cap | Equal to going-in cap 🟢 (the actual cap value was not stated) |
| Financials | Full T-12, rent roll, downside sensitivity provided 🟢 |

## 2. Return Stress-Test

No claimed return was provided, so every return figure below uses an **assumed** gross IRR as its input 🔴. I anchored on the `01` value-add band and ran it through `scripts/fee_drag_calculator.py` with the disclosed fee stack: 1% acquisition, 1.5% annual asset management, 1% disposition, 20% carry over an 8% hurdle. Undisclosed items were handled as follows:
- **Admin fee:** passed as 0 (it was not disclosed).
- **Catch-up:** assumed 100%, the conservative case for the LP.
- **Hold:** assumed 5 years, with a 7-year check.

| Case | Gross deal IRR (assumed) | Net-to-LP IRR (script) | Total drag | vs VNQ 4.92% 10yr (`05`) | Illiquidity hurdle | Read |
|---|---|---|---|---|---|---|
| Bull | 18% | 13.3% | 468 bps | ≈840 bps | ~300–400 bps (5-yr) | Clears comfortably |
| Base | 15% | 10.7% (5-yr) / 11.0% (7-yr) | 431 / 396 bps | ≈577 / ≈612 bps | ~300–400 / ~400–600 bps | **Clears comfortably** (`benchmark_comparator.py`) |
| Bear | 12% | 8.1% | 391 bps | ≈317 bps | ~300–400 bps (5-yr) | **Clears (thin)**, lower half of the hurdle band |

**Swing assumptions:**
1. **Rent growth / renovation premium (NOI lift).** The exit cap is flat, so exit value moves only with NOI. This is the dominant driver.
2. **Exit cap vs going-in.** It is underwritten flat, which is sound (`EQUITY-06` does not fire). The bear case should still test a cap *above* going-in, because a flat cap removes compression but does not protect against expansion.
3. **Refi.** Largely neutralized. The fixed-rate debt runs 2 years past the planned exit, so the plan does not need a refinance (`GEN-09`, `GEN-10`, and `EQUITY-07` do not fire).

**Treasury floor (`05`):** the 10yr Treasury is 5.18%. The base net of ~10.7% is ≈550 bps above it. The bear net of ~8.1% is only ≈290 bps above it, so the bear case pays for the lock-up only thinly.

**Calibration note 🟡:** a 15% gross nets to ~10.7–11.0%, which is below the `01` realized value-add band of 12–15% net. Landing inside that band would take roughly 16–17% gross, before any admin fees. The GP's actual gross/net target is therefore a must-ask.

The GP says a downside sensitivity exists (`GEN-13` does not fire). Check that it matches the bear case above: flat rents, exit cap above going-in, and no refinance (`Q-DS-03`).

## 3. Where LP Returns Come From

- **Leverage vs operations:** the NCREIF NPI unlevered overlay (`05`) is 5.00% trailing (residential 5.3% in 2025), almost all of it income. A ~11% levered net therefore gets roughly 6 points from leverage plus NOI growth. Because the exit cap is flat, **none of that comes from cap-rate compression**. That is an asset story (value-add NOI) amplified by fixed-rate leverage, not the financing story described in `GEN-07` 🟡.
- **Cash flow vs exit:** this can't be measured from the disclosure because there is no distribution schedule and no IRR decomposition. Value-add deals typically back-load return to exit, since the renovation lift is realized through the sale price. Even with a flat cap, the terminal share could exceed 60%. `GEN-08` is **not fired, but unverified** 🟡. Route it to `Q-DS-01` and `Q-DIST-01`.
- **Net read:** none of the financing-story cluster (`GEN-07` + `GEN-08` + `EQUITY-06`) fires on what was disclosed. The open item is the income-vs-exit split, not the source of the return.

## 4. Fee Stack Summary

| Fee | Disclosed | `02` norm | Read |
|---|---|---|---|
| Acquisition | 1% | 1–2% of equity (or 0.5–1.5% of price) | In range, low end 🟢 |
| Asset management | 1.5% annual | 1–2% of equity, annual | In range, mid 🟢 |
| Disposition | 1% | 0.5–1% of sale price | In range, top of band 🟢 |
| Promote | 20% over 8% cumulative, compounding pref | 15–30% over 6–10% | In range. Compounding is LP-favorable (most deals use simple) 🟢 |
| Catch-up | Not stated | — | Ask. A 100% catch-up would fire `EQUITY-03` (YELLOW) |
| Loan placement / refinance | Not stated | 0.5–1.5% of loan | Ask whether charged. It is absent, not confirmed as $0 |
| Admin / IR / K-1 | Not stated | 0.1–0.5% of equity or $1–3k/LP | Ask. It was passed as 0 in the calc, so it is a §6 gap |

**Gross-to-net drag: ≈430 bps/yr** at the assumed 15% gross, 5-yr hold, 100% catch-up (fees ≈190 bps, promote ≈241 bps). It falls to ≈330 bps if there is no catch-up and ≈400 bps on a 7-yr hold. 🟡 This is script output on assumed gross/hold/catch-up inputs.

**Caveats:**
- The calculator treats the fee percentages as percentages of equity. If the 1% disposition fee is charged on **sale price** (the `02` convention), its dollar cost on a levered deal is a multiple of 1% of equity, so the one-time drag is understated 🟡.
- If the 1.5% asset-management fee is charged on equity raised rather than invested capital, it is at the less LP-favorable end.
- The script does not model compounding pref. That feature helps the LP, so the net figure leans conservative.
- Confirm the fee bases (`Q-FEE-01`).

## 5. Red Flags

**RED:** none.

**YELLOW:**
- **`GEN-11` (cash-flow timing / J-curve not disclosed):** no distribution schedule, and no headline IRR, hold, or cash-on-cash. The LP can't tell whether capital returns during the hold or only at exit. For a value-add deal, back-loading is the default expectation. → `Q-DIST-01`

**Checked, not fired (cited for completeness):**
- `GEN-01`: 10% cash co-invest, pari-passu.
- `GEN-05` / `GEN-14`: realized, net-to-LP IRRs on 5 exited deals. Verify the figures themselves (§9).
- `EQUITY-01` / `EQUITY-02`: whole-of-fund waterfall with a secured clawback.
- `EQUITY-04` / `EQUITY-05`: 8% cumulative, compounding pref.
- `EQUITY-06`: exit cap equals going-in.
- `GEN-07`: no cap compression, per the unlevered overlay in §3.
- `GEN-09` / `EQUITY-07`: debt matures 2 yrs after exit.
- `GEN-10`: fixed rate, no cap to expire.
- `GEN-12` / `GEN-15`: full T-12 and rent roll.
- `GEN-13`: downside sensitivity provided.
- `GEN-16`: fees and waterfall disclosed at headline level.

**Unverified, not fired. Probe, don't score:**
- `GEN-08`: the exit share of return is unknown (§3).
- `EQUITY-03`: catch-up rate not stated.
- `GEN-06`: whether property management or construction management goes to GP affiliates is not stated.
- `GEN-18`: the rent-growth assumption and submarket are not stated.

**Pasted-text directives:** none present.

## 6. Missing Disclosures

Measured against the `01` value-add essential list and the `02` fee inventory:
1. **Target return.** No net-to-LP IRR, equity multiple, or cash-on-cash. This is the largest gap, because the benchmark comparison in §2 runs on an assumed input.
2. **Hold period** and **distribution schedule** (`GEN-11`).
3. **Sponsor identity, submarket, minimum, and raise size.**
4. **Debt detail.** Beyond fixed rate and maturity: LTV/LTC, rate, amortization / IO period, and prepayment or defeasance terms. Prepayment matters specifically here: selling 2 years before a fixed-rate maturity can trigger yield maintenance or defeasance costs at exit.
5. **Exit cap value** and **rent-growth assumption.** The fact that exit cap equals going-in is disclosed, but the numbers are not.
6. **Catch-up rate, admin/IR fee, loan placement fee, and fee bases** (equity raised vs invested vs sale price).
7. **Affiliate service providers** (property management, construction management).
8. **Track-record detail.** The five realized net-to-LP IRRs are "disclosed" but were not provided here, and the prior exits should be confirmed as **multifamily** (`01` essential disclosure).

## 7. GP Alignment

- **Co-invest 🟢 (stated, unverified):** 10% of equity, in cash, pari-passu. This is structural alignment, not asserted alignment. Verify at close via the subscription/capital account.
- **Track record 🟢/🔴:** five fully exited deals with net-to-LP IRRs is the right *form* of record (`Q-GP-02` satisfied as to form). The *numbers* are unverified until checked against LP distribution statements, and five exits is a modest sample.
- **Waterfall 🟢:** whole-of-fund with a secured clawback, cumulative compounding pref, and 20% promote. This is at the LP-protective end of retail syndication structures (`02`). The only open waterfall term is the catch-up rate.
- **Affiliate fees 🔴 (unknown):** not disclosed. Confirm (`Q-FEE-02`).

## 8. Questions for the GP

**Must-ask**

| ID | Question | Bad-answer signal |
|---|---|---|
| `Q-DIST-01` (`GEN-11`) | "What is the projected distribution schedule, and at what milestones does LP capital start returning?" | "We'll distribute when the deal supports it" with no milestones; IRR with no timing. |
| `Q-DS-01` (`GEN-08`, `EQUITY-06`) | "What share of projected LP IRR comes from in-place cash flow versus the exit, and what's the IRR at a flat exit cap?" | Can't decompose the IRR; the flat-cap IRR falls below the 8% pref. |
| `Q-DS-03` (`GEN-13`) | "What is the return under a bear case — flat rents, higher exit cap, no refinance?" | The provided sensitivity only tests mild moves; the bear case is still a gain; no exit-cap-*above*-going-in run. |
| `Q-MKT-01` (`GEN-18`) | "What submarket supply pipeline and absorption data support the rent-growth assumption?" | Metro-level optimism; "rents always go up here"; no supply pipeline acknowledged. This is the key question, since NOI growth is the swing factor. |
| `Q-GP-02` (`GEN-05`, `GEN-14`) | "Can you restate your track record as net-to-LP IRR on fully-realized, exited deals only?" *(Ask for the five deals' statements and whether they were multifamily.)* | Numbers can't be tied to LP distribution statements; the exits are a different asset class; losers omitted. |
| `Q-FEE-01` (`GEN-16`) | "Can you provide the complete fee schedule and the full distribution waterfall?" *(Include catch-up, admin, loan placement, and the base of each fee.)* | "Standard market fees"; catch-up or admin surfaces only in the PPM after commitment. |
| `Q-FEE-02` (`GEN-06`) | "Which service providers are GP-affiliated, what do they charge, and are those rates third-party-benchmarked?" | "All arm's-length" without naming providers; affiliate property management at undisclosed rates. |
| `Q-RISK-01` (`GEN-09`) | "When does the debt mature relative to the projected hold, and what's the refinance or extension plan?" *(Add: what prepayment / defeasance cost applies at a sale 2 years before maturity?)* | Prepayment cost not modeled in the exit proceeds. |
| `Q-GP-01` (`GEN-01`) | "How much of your own capital is in this deal, on the same terms as LPs?" *(Confirmatory.)* | The 10% is partly fees rolled in rather than cash; a side letter gives better terms. |
| `Q-GP-03` (`GEN-02`) | "Have you or your principals faced any regulatory action, enforcement, or investor litigation?" | "Nothing material"; a search surfaces something undisclosed. |
| `Q-FEE-03` (`EQUITY-01`, `EQUITY-02`) | "Is the waterfall deal-by-deal or whole-of-fund, and is there a clawback?" *(Confirmatory: how is the clawback secured?)* | "Secured" means only a GP guarantee with no escrow or holdback. |
| `Q-FEE-04` (`EQUITY-04`, `EQUITY-05`) | "What preferred return do LPs receive before the GP earns promote, and is it cumulative and compounding?" *(Confirmatory: stated as yes.)* | The PPM language reads simple, not compounding. |
| `Q-EXIT-02` (`EQUITY-07`) | "Does the business plan depend on a refinance, and what happens to distributions if the refi isn't available on the assumed terms?" *(Confirmatory: the maturity implies no.)* | A mid-hold cash-out refi is in the model after all. |
| `Q-LIQ-01` | "What are my options if I need to exit before the hold period ends?" | "A secondary market may develop"; the lock-up is not stated. |

**Nice-to-ask:** `Q-GP-04` (`GEN-04`) on team scale vs AUM; `Q-DIST-02` on capital-call mechanics; `Q-LIQ-02` on K-1 timing. `Q-EXIT-01` (`EQUITY-06`) only needs confirming, since the exit cap equals going-in.

## 9. Diligence Checklist

- **PPM / operating agreement:** confirm the whole-of-fund waterfall, clawback security mechanism, compounding pref, catch-up, fee bases, and any admin or affiliate fees.
- **Track record:** tie the five realized net-to-LP IRRs to LP distribution statements or a third-party administrator. Confirm they are multifamily exits.
- **Background / regulatory:** check the principals against SEC / FINRA / state records and litigation (`Q-GP-03`).
- **Loan documents:** rate, LTV, IO/amortization, maturity, and prepayment / defeasance at a sale 2 years early.
- **Market:** get independent submarket supply and absorption data and rent comps to test the rent-growth assumption.
- **Valuation:** request the appraisal and cap-rate comps to confirm the going-in cap, since the exit is pegged to it.
- **Financials:** reconcile the T-12 to the rent roll, and check that the downside sensitivity stresses the three swing assumptions.
- **Co-invest:** confirm the GP's 10% cash contribution at funding.

## 10. Verdict

**Pursue.**

**Reasoning:** every structural protection this screen tests for is present, and none of the common failure modes fires:
- No financing story, since there is no cap compression.
- No refi or rate-cap trap, since the debt is fixed rate and matures after the exit.
- No unverified track record: the record is realized and net-to-LP.
- No deal-by-deal promote leakage: the waterfall is whole-of-fund with a clawback.

The gaps are the headline economics (target return, hold, distribution schedule) and a few fee and debt details. Those are residual items to close in diligence, not structural defects. Enough is disclosed to underwrite the core return story: a value-add NOI lift on fixed-rate leverage with no exit-cap bet.

**Biggest swing factor:** achieving the NOI growth. With cap rate and refi neutralized, the LP's outcome depends almost entirely on the GP executing the value-add and on the submarket supporting the assumed rent growth. At the assumed 12% gross bear case, the net return (~8.1%) only thinly clears the illiquidity hurdle and sits under 300 bps above the 10yr Treasury.

**What would have to be true:**
- The stated target net IRR sits near or above ~11% on a 5–7 yr hold.
- The distribution schedule shows meaningful in-hold cash flow.
- The rent-growth assumption holds up against submarket supply data.
- The five realized IRRs verify.
- The catch-up and affiliate fees don't materially widen the ≈400–430 bps drag.

**Who it suits:** an LP who can lock up capital for the implied 5–7 yrs, wants multifamily equity exposure with strong LP-protective terms, and accepts that single-asset execution risk is the main bet.
