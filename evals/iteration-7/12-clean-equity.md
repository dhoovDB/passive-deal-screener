# Eval fixture 12

*Iteration-7 run, 2026-11-01, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 181fdd7.*

**Verdict: Pursue.** The structure clears every LP-protection screen it discloses. The open question is the return itself: the deal does not state one.

*Screening output only, not investment advice.*

This is one of the cleanest term sets an LP will see in a retail syndication. It has real cash co-invest, a whole-of-fund waterfall with a secured clawback, a cumulative compounding pref, a flat exit cap, debt that outlasts the plan, full financials, a downside case and a realized net-to-LP track record. No RED flag fires. What remains is a set of disclosure gaps, chiefly target return, hold, leverage and full debt terms. Those are the first diligence asks, not reasons to pass.

---

## 1. Deal Snapshot

| Field | Value | Confidence |
|---|---|---|
| Asset class | Multifamily, value-add | 🟢 stated |
| Deal type | Equity syndication (routes to `02` Equity + Waterfall, `03` `GEN-`/`EQUITY-`, `05` VNQ + NCREIF NPI overlay) | 🟢 stated |
| Sponsor | Not stated | — |
| Geography / submarket | Not stated | — |
| Minimum investment | Not stated | — |
| Raise / equity size | Not stated | — |
| Hold period | Not stated. A "planned exit" is referenced but not dated | 🟢 absence |
| Claimed return (IRR / multiple / cash-on-cash) | Not stated | 🟢 absence |
| Leverage (LTV / DSCR) | Not stated | 🟢 absence |
| Debt | Fixed-rate, maturing two years after the planned exit. Rate, amortization and prepayment terms are not stated | 🟢 stated / gaps |
| Pref / promote | 8% cumulative, compounding pref; 20% promote. Catch-up not stated | 🟢 stated |
| Waterfall | Whole-of-fund with a secured clawback | 🟢 stated |
| Fees | 1% acquisition, 1.5% asset management (annual), 1% disposition. Fee bases not stated | 🟢 stated |
| GP co-invest | 10% of equity, cash, pari-passu | 🟢 stated (unverified) |
| Track record | Five fully exited deals, net-to-LP IRRs disclosed. The figures were not shown to us | 🟢 stated (unverified) |
| Exit cap | Equal to going-in cap | 🟢 stated |
| Financials | Full T-12, rent roll, downside sensitivity provided | 🟢 stated |

---

## 2. Return Stress-Test

**The deal states no return figure**, neither gross nor net, IRR nor multiple. Nothing here can be stress-tested against the GP's own number. The scenarios below therefore use an **assumed** gross deal IRR (🔴) to show what the disclosed fee and waterfall terms do to the LP. They are not a forecast of this deal. All runs use `scripts/fee_drag_calculator.py` with the disclosed fees (1% / 1.5% / 1% / 20% over 8%), 0 for undisclosed admin and loan-placement fees, an assumed 5-year hold (low end of the `01` 5–7 yr norm, 🔴) and an assumed 100% catch-up (🔴; the deal didn't state one, and 100% is the conservative case).

| Case | Assumed gross deal IRR 🔴 | Est. net-to-LP IRR | vs VNQ (4.92% 10yr) | 5-yr illiquidity hurdle ~300–400 bps | Read |
|---|---|---|---|---|---|
| Bull | 20% | 15.08% | +1016 bps | Clears | Top of the `01` value-add target band |
| Base | 15% | 10.69% | +577 bps | Clears comfortably | Below the `01` realized 12–15% blended range |
| Bear | 10% | 6.38% | +146 bps | **Thin / fails** | Only ~120 bps over the 10yr Treasury (5.18%) |

Base case at a 7-year hold: 11.04% net, +612 bps, clears the ~400–600 bps hurdle comfortably. (`scripts/benchmark_comparator.py`, multifamily-value-add → VNQ.)

**Swing assumptions** (the ones this deal's own downside sensitivity should be shown to stress):
1. **Exit cap.** It is underwritten flat to going-in, which removes baked-in compression (🟢). The live risk is now *expansion*: a flat exit cap is not conservative if the asset was bought at a cycle-low cap. Ask for the IRR at going-in +50 and +100 bps (`Q-EXIT-01`).
2. **Value-add rent premium and rent growth.** With the exit cap held flat, every dollar of exit gain has to come from NOI growth. That makes the renovation premium and submarket rent growth the main return driver (🟡). Submarket and supply data are not disclosed (`Q-MKT-01`).
3. **Exit timing against the debt.** Refinance is *not* a swing here: the fixed-rate loan matures two years after the planned exit (🟢). The debt-side swing is instead the **prepayment cost of selling on schedule**. Fixed-rate multifamily debt commonly carries yield maintenance or defeasance, so a sale two years before maturity can trigger a payoff premium that sits between the gross sale price and LP distributions. Its size depends on the rate path and the loan's terms, which are not disclosed (🔴; `Q-RISK-03`).

**Treasury floor.** At this snapshot the 10yr Treasury (5.18%) out-yields VNQ's trailing 10yr (4.92%), so the Treasury is the tighter floor (`05`). The base case clears both. The bear case clears neither by a lock-up-worthy margin.

**Model caveat.** The calculator models a simple pref. This deal's pref is **compounding**, which is more LP-favorable (`02`: "Compounding is more favorable to the LP. Most deals use simple"). The promote drag above is slightly overstated, so the net figures are slightly conservative.

---

## 3. Where LP Returns Come From

**Can't tell from this. No IRR, no distribution schedule, no leverage figure.** What the disclosed terms do establish:

- **Cap-rate compression is excluded by construction** (exit cap = going-in, 🟢). The main mechanism behind a financing story (`EQUITY-06` → `GEN-07`) is absent.
- **Refi dependence is absent** (debt matures after the planned exit, 🟢). Distributions and capital return should not hinge on a refinance (`EQUITY-07` not fired; confirm with `Q-EXIT-02`).
- **Leverage share is unmeasurable.** The unlevered overlay (`05`: NCREIF NPI 5.00% trailing four quarters, almost all income; residential 5.3% in 2025) says institutional real estate earns roughly 5% unlevered and in place. Everything the deal projects above that comes from leverage plus value-add NOI growth. Without the LTV and the levered IRR, the split can't be computed (`GEN-07` not fired; it is a must-ask via `Q-DS-02`).
- **Exit share is unmeasurable.** Value-add returns are typically back-weighted to the sale, so the >60% terminal-value test (`GEN-08`) may well be met. Here, though, the exit gain would be *operational* (NOI growth at a flat cap), not cap compression. `GEN-08` is not fired on unstated numbers. It routes to `Q-DS-01` and `Q-DIST-01`.

Net read (🟡): the disclosed structure points to an **asset story, not a financing story**. That has to be confirmed with the decomposition the GP has not yet provided.

---

## 4. Fee Stack Summary

| Fee | Disclosed | `02` typical range | Status |
|---|---|---|---|
| Acquisition | 1% (basis not stated) | 1–2% of equity, or 0.5–1.5% of price | In range on either basis 🟢 |
| Asset management | 1.5% annual (basis not stated) | 1–2% of equity, annual | In range 🟢 |
| Disposition | 1% (basis not stated) | 0.5–1% of sale price | Top of range 🟢 |
| Promote | 20% | 15–30% over a 6–10% pref | In range 🟢 |
| Pref | 8% cumulative, compounding | 6–10%; cumulative standard; compounding better than typical | Better than typical 🟢 |
| Catch-up | Not stated | 50 / 80 / 100% common | Gap (§6) |
| Loan placement / financing | Not stated | 0.5–1.5% of loan | Gap. Modeled as 0 |
| Admin / IR / K-1 | Not stated | 0.1–0.5% of equity or $1–3k/LP | Gap. Modeled as 0 |
| Affiliate fees (property / construction management) | Not stated | Disclosure + benchmark test (`GEN-06`) | Gap |

**Gross-to-net drag: ≈431 bps/yr.** This is the conservative case: 5-yr hold, 15% assumed gross, 100% catch-up assumed. Recurring fees are 150 bps, one-time fees 40 bps and promote 241 bps. The range is ≈320–431 bps/yr across a 5–7 yr hold and 0–100% catch-up. With no catch-up the promote drag falls to ≈141–143 bps, so **the undisclosed catch-up rate is worth about 100 bps/yr to the LP** and is the largest single unknown in the stack.

Caveats:
- **Fee bases.** The calculator treats one-time fees as a percent of equity. If the acquisition and disposition fees are charged on *purchase / sale price*, their equity-equivalent drag scales with leverage. At a hypothetical 60% LTV with flat value (🔴 illustrative), 1% of price is ≈2.5% of equity, and one-time drag would roughly double the 40 bps shown. Confirm the bases (`Q-FEE-01`).
- **Disposition and brokerage.** `02` notes that the disposition fee stacks with brokerage paid by the deal. Verify there is no double charge.
- **"In line with market"** is the sponsor's characterization. The three disclosed numbers support it, but the undisclosed lines (catch-up, admin, financing, affiliates) are what the phrase can hide.

Adding a typical 0.1–0.5% admin fee would add ≈10–50 bps/yr.

---

## 5. Red Flags

**RED:** none.

**YELLOW**
- **`GEN-17` — Essential category disclosure absent (target return and hold period).** `01` says a deal that omits hold period or return expectation when the category has a baseline is "a flag, not a neutral silence." Without them, the LP can't run the benchmark test (§2) or the IRR decomposition (§3) on the GP's own numbers. LP exposure: the lock-up length and the return being bought are both unknown. Routes to `Q-DS-01`, `Q-DIST-01`, `Q-RISK-01`. 🟢 (absence)

**Checked and cleared (cited so the self-check is visible):**
- `GEN-01` zero co-invest: cleared. 10% cash, pari-passu (🟢 stated; verify, `Q-GP-01`).
- `GEN-05` / `GEN-14` GP-level IRR / unrealized-only track record: cleared. Five realized exits on a net-to-LP basis (🟢 stated; verify figures and completeness, `Q-GP-02`).
- `EQUITY-01` / `EQUITY-02` deal-by-deal waterfall without clawback: cleared. Whole-of-fund with a *secured* clawback (`Q-FEE-03`).
- `EQUITY-04` / `EQUITY-05` low or non-cumulative pref: cleared. 8% cumulative, compounding (`Q-FEE-04`).
- `EQUITY-06` exit cap below going-in: cleared. Flat (`Q-EXIT-01`).
- `GEN-07` / `GEN-08` financing story / exit-dependent IRR: not fired. Cap compression is excluded, but leverage and the exit share are undisclosed, so they are must-asks rather than flags (`Q-DS-02`, `Q-DS-01`).
- `GEN-09` debt maturity inside the hold: cleared. Matures two years after the planned exit (`Q-RISK-01`).
- `GEN-10` rate-cap expiry: not applicable. The debt is fixed-rate, so `Q-RISK-02` is not asked.
- `EQUITY-07` refi-dependent plan: not fired on the stated maturity (`Q-EXIT-02` to confirm).
- `GEN-12` / `GEN-15` short-window or missing financials: cleared. Full T-12 and rent roll (`Q-RISK-03` for complete debt terms).
- `GEN-13` no downside case: cleared. Downside sensitivity provided (`Q-DS-03` to confirm what it stresses).
- `GEN-16` no fee / waterfall disclosure: not fired. Headline fees and waterfall are disclosed. Catch-up, admin and financing fees are residual gaps (§6, `Q-FEE-01`).
- `GEN-06` affiliate fee stacking: not fired, because nothing is disclosed either way (`Q-FEE-02`).
- `EQUITY-03` 100% catch-up: unknown, so not fired (`Q-FEE-03`, `Q-FEE-01`).
- `GEN-18` rent growth in an oversupplied submarket: unknown, because the submarket is not stated (`Q-MKT-01`).
- `GEN-11` J-curve undisclosed: not fired, since no IRR is quoted. The distribution schedule is still absent (`Q-DIST-01`).
- `GEN-02` regulatory / litigation history: unknown (`Q-GP-03`, background check in §9).

No cluster: the financing-story family (`GEN-07` + `GEN-08` + `EQUITY-06`) has its anchor flag, `EQUITY-06`, affirmatively cleared.

---

## 6. Missing Disclosures

Against the `01` multifamily value-add essentials and the `02` equity fee inventory:

1. **Target / projected return.** Gross and net-to-LP IRR, equity multiple, cash-on-cash. Not stated.
2. **Hold period.** The planned exit year, which also dates the debt maturity. Not stated.
3. **Debt terms beyond "fixed, matures exit + 2 yrs".** LTV, rate, amortization / IO, DSCR, and **prepayment terms** (yield maintenance / defeasance / step-down) are not stated. `01` lists "debt structure and maturity" as essential, and the prepayment provision decides what selling on schedule costs.
4. **Refi assumptions.** Implicitly none, given the maturity. Confirm the plan has no interim cash-out refi.
5. **GP catch-up rate.** Worth ≈100 bps/yr of drag between 0% and 100% (§4).
6. **Fee bases.** Acquisition and disposition on equity or price; asset management on equity raised or invested capital.
7. **Admin / IR, loan placement and any refinance fees.** Not stated. Modeled at 0, which is an ASSUMED input.
8. **Affiliate service providers** (property management, construction management) and their rates.
9. **Distribution schedule / J-curve.**
10. **Track-record detail.** The five IRR figures themselves, whether all five were multifamily value-add (`01` asks specifically for prior *multifamily exits*), their vintages, and whether five is the GP's complete exited set or a selection.
11. **Sponsor identity, geography / submarket, minimum, raise size.**
12. **Clawback mechanics.** What "secured" means (escrow / holdback / guarantee) and, for a single-asset syndication, what "whole-of-fund" covers.

---

## 7. GP Alignment

- **Co-invest: strong (🟢 stated, 🔴 unverified).** 10% of equity, in cash, pari-passu, is meaningful skin in the game on the same terms as LPs. That is the `Q-GP-01` good-answer profile. Verify it is funded cash at close, not deferred fees or a promote rollover counted as "cash."
- **Track record: realized, net-to-LP (🟢 stated, 🔴 unverified).** This is the right basis (`GEN-05` and `GEN-14` cleared). Residual caution: five exits is a small sample. If they were sold in the 2010s–2021 cap-compression tailwind, they show the GP can exit in a rising market, not through a down-cycle. Ask for the figures, vintages and whether any deals were lost, recapitalized or are still unexited.
- **Waterfall alignment: LP-favorable (🟢 stated).** Whole-of-fund means the GP earns nothing until LP capital plus pref is returned (`02`). The *secured* clawback addresses the residual risk that promote paid from interim distributions turns out to be excess. The pref compounds, which is better than market. The catch-up is the one undisclosed lever.
- **Affiliate fees: unknown.** The test is disclosure and benchmarking, not whether affiliates exist (`03` → `GEN-06`).

---

## 8. Questions for the GP

**Must-ask**

| ID | Question | Bad-answer signal (the specific dodge) |
|---|---|---|
| `Q-DS-01` | "What share of projected LP IRR comes from in-place cash flow versus the exit, and what's the IRR at a flat exit cap?" *(Here: and what is the projected net-to-LP IRR and hold in the first place?)* | Can't or won't decompose the IRR; pivots to "real estate always appreciates"; IRR collapses below pref at a flat exit cap. |
| `Q-DS-02` | "Strip out leverage and cap-rate compression — what is the unlevered, in-place return?" | Treats the levered IRR as the only relevant figure; no unlevered view exists; "leverage is just how the deal works." |
| `Q-DS-03` | "What is the return under a bear case — flat rents, higher exit cap, no refinance?" *(Confirm the provided sensitivity stresses exit cap* above *going-in, not just rents.)* | A single-point pro forma with no downside; "we underwrite conservatively" with nothing to show; the bear case is still a gain. |
| `Q-EXIT-01` | "What's the IRR at an exit cap equal to or above going-in?" *(Ask for +50 / +100 bps.)* | No sensitivity offered; the IRR breaks with modest cap expansion. |
| `Q-EXIT-02` | "Does the business plan depend on a refinance, and what happens to distributions if the refi isn't available on the assumed terms?" | Distributions or capital return require a refi at lower rates; no fallback; "the refi market will reopen." |
| `Q-RISK-01` | "When does the debt mature relative to the projected hold, and what's the refinance or extension plan?" *(Here: what year, and what if the sale slips past the 2-yr cushion?)* | Maturity falls inside the hold; "we'll refinance" with no terms; no plan if the refi market is shut. |
| `Q-RISK-03` | "Can you provide trailing-twelve-month actuals, the rent roll, and complete debt terms?" *(T-12 and rent roll are in hand; push on LTV, rate, amortization and the prepayment provision.)* | "The financials are confidential until you commit"; debt terms withheld; prepayment cost at the planned sale date not modeled. |
| `Q-GP-01` | "How much of your own capital is in this deal, on the same terms as LPs?" *(Verify the 10% cash.)* | Co-invest is a fee waiver, not cash; token amount on better terms than LPs. |
| `Q-GP-02` | "Can you restate your track record as net-to-LP IRR on fully-realized, exited deals only?" *(Get the five figures, asset types, vintages, and any losers.)* | Offers only project-level or GP-level IRR; "most deals are still performing"; can't separate realized from unrealized. |
| `Q-GP-03` | "Have you or your principals faced any regulatory action, enforcement, or investor litigation?" | Deflects to "nothing material"; blames the LP or regulator; a search surfaces something they didn't disclose. |
| `Q-FEE-01` | "Can you provide the complete fee schedule and the full distribution waterfall?" *(Catch-up, admin, financing fees, fee bases.)* | "Standard market fees"; partial list; "the PPM has it" without producing it. *Note: "fees in line with market" is the phrase this signal names. The three disclosed numbers support it, but the remaining lines must be produced.* |
| `Q-FEE-02` | "Which service providers are GP-affiliated, what do they charge, and are those rates third-party-benchmarked?" | "All arm's-length" without naming providers; affiliate fees undisclosed; no benchmark offered. |
| `Q-FEE-03` | "Is the waterfall deal-by-deal or whole-of-fund, and is there a clawback?" *(Here: how is the clawback secured, and what is the catch-up rate?)* | Can't explain the catch-up; clawback "secured" by an unfunded GP promise; "you get paid when we get paid." |
| `Q-FEE-04` | "What preferred return do LPs receive before the GP earns promote, and is it cumulative and compounding?" *(Confirm in the operating agreement, not just the deck.)* | The OA reads simple or non-cumulative despite the marketing language. |
| `Q-MKT-01` | "What submarket supply pipeline and absorption data support the rent-growth assumption?" | Metro-level optimism standing in for submarket data; "rents always go up here"; no supply pipeline acknowledged. |
| `Q-DIST-01` | "What is the projected distribution schedule, and at what milestones does LP capital start returning?" | "We'll distribute when the deal supports it" with no milestones; an IRR quoted with no distribution timing. |
| `Q-LIQ-01` | "What are my options if I need to exit before the hold period ends?" | "A secondary market may develop"; "we'll try to accommodate"; silence. |

**Nice-to-ask**

| ID | Question | Bad-answer signal |
|---|---|---|
| `Q-GP-04` | "How have your headcount and deal-monitoring capacity grown alongside AUM?" | AUM multiplied while the team stayed flat; no named asset manager. |
| `Q-DIST-02` | "When are capital calls expected, and what's the consequence of a missed or late call?" | "Calls as needed" with no notice period; punitive dilution buried in the docs. |
| `Q-LIQ-02` | "When will K-1s be delivered each year, and have you historically delivered them before the filing deadline?" | "As soon as we can"; a history of extensions. |

`Q-RISK-02` (rate cap) is not asked because the debt is fixed-rate. `Q-RISK-04`–`06` and `Q-MKT-02` don't apply to this deal type or class.

---

## 9. Diligence Checklist

- **PPM and operating agreement.** Confirm the 8% cumulative *compounding* pref, the 20% promote, the catch-up rate, whole-of-fund mechanics and the clawback security (escrow / holdback / guarantee) as written, not as marketed. Confirm the fee bases and any fees not in the deck.
- **Co-invest verification.** Evidence the GP's 10% is funded cash at close (subscription or closing statement).
- **Track-record verification.** Obtain the five exits' net-to-LP IRRs with distribution histories. Where possible, cross-check with an LP from a prior deal.
- **Background / regulatory.** SEC / FINRA / state searches and litigation search on the sponsor and principals (`GEN-02`).
- **Loan documents.** Lender, LTV, rate, amortization, maturity date, extension options, prepayment provision (yield maintenance / defeasance), assumability, recourse carve-outs.
- **T-12 and rent roll tie-out.** Reconcile the T-12 to the rent roll and to the pro forma's in-place NOI. Check the downside sensitivity's inputs.
- **Appraisal / third-party valuation.** Supports the purchase price and the going-in cap.
- **Submarket comps.** Rent comps for renovated units (supports the value-add premium), the supply pipeline, and sale comps for exit-cap reasonableness.
- **Lender / reference call** where feasible on the sponsor's prior debt performance.

---

## 10. Verdict

**Pursue.**

*Screening output only, not investment advice.*

**Reasoning.** Every structural protection an LP screens for is present and on the LP-favorable side of the `02` / `03` norms:
- Alignment is cash and pari-passu (`GEN-01` cleared).
- The track record is realized and net-to-LP (`GEN-05` / `GEN-14` cleared).
- The waterfall is whole-of-fund with a secured clawback (`EQUITY-01` / `EQUITY-02` cleared).
- The pref is cumulative *and compounding*, better than most deals (`EQUITY-05` cleared).
- The fees are in range.
- The exit cap bakes in no compression (`EQUITY-06` cleared).
- Fixed-rate debt outlasts the plan, removing both rate-cap-expiry and refi-wall risk (`GEN-10` not applicable; `GEN-09` cleared).
- The core financials and a downside case are provided (`GEN-12` / `GEN-13` / `GEN-15` cleared).

Inventing a RED here would be a false positive. The essential `01` disclosures for underwriting the return story are substantially present, so this is a merits verdict.

**Biggest swing factor.** The return itself. No target IRR, hold or leverage is disclosed. At an assumed 15% gross, the disclosed fee and waterfall terms leave the LP at ≈10.7–11.0% net, which clears VNQ plus the illiquidity hurdle by a comfortable margin. At an assumed 10% gross, the LP is at ≈6.4% net, which **fails** the hurdle and barely beats the 10yr Treasury. Where the GP's own projection, and its downside sensitivity, land in that range decides the deal. With the exit cap held flat, that projection rests on value-add execution and submarket rent growth, which is the operational bet an LP should want to be taking.

**What would have to be true** to move from screen to commit:
1. The projected net-to-LP IRR clears the `05` hurdle for the actual hold (≈300–400 bps over VNQ for a 3–5 yr lock-up, ≈400–600 bps for 7–10 yr). The provided downside case should still return LP capital.
2. The IRR decomposition shows the return is NOI growth plus moderate leverage, not leverage alone (`Q-DS-01`, `Q-DS-02`).
3. The catch-up rate, fee bases and affiliate fees come back in line, and total drag stays near or below the ≈430 bps/yr computed here.
4. The loan's prepayment cost at the planned sale date is known and modeled.
5. The co-invest, the five realized exits and the clawback security verify against documents.

**Who it suits.** An LP who can lock up capital for the full hold *plus* the two-year cushion before debt maturity (assume no liquidity, `Q-LIQ-01`). It also suits someone who wants an operational value-add multifamily exposure under institutional-style LP protections, and who accepts single-asset concentration that VNQ diversifies away.
