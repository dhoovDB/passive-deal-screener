# Eval fixture 03 — Hard-money bridge fund (well-disclosed)
*Iteration-4 run, 2026-09-27, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 1c7faff.*

**Verdict: Pursue with conditions.** The credit story holds up. As-is LTV, default rate, recovery through 2020 and 2022–23, geographic spread and a fee step-down are all disclosed, and the fund fires none of the five `HML-` flags. A 9% net target is ≈417bps over HYG, which clears the ~300–400bps hurdle for a 3–5 year lock-up. The conditions are there to confirm things, not fix them. The sponsor, GP co-invest, performance fee, fund-level leverage and fund term are all unstated, and the LTV-as-is vs LTV-ARV pair needs one line explaining how each is measured. The biggest swing factor is loss severity in a housing-price drawdown. The 92% recovery rate protects the 9%, and that rate was earned in two downturns where collateral values stayed firm.

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Hard Money / Bridge Loan 🟢 |
| Deal type | Debt fund: senior-secured bridge loans 🟢 |
| Sponsor | Not stated |
| Geography | 12 states; no single metro above 15% 🟢 |
| Minimum investment | Not stated |
| Hold / fund term | Not stated. There is an investment period (implied by the fee step-down), so it is likely closed-end. `01` baseline: 3–5 yr fund commitment, 6–18 mo per loan 🟡 |
| Raise / fund size | Not stated |
| Claimed return | 9% net target to LPs 🟢. This sits inside the `01` band of 8–10% net for hard money |
| Collateral / LTV | 68% average on as-is value; 72% on ARV 🟢 |
| Credit history | 3.1% historical default rate; 92% realized recovery, including 2020 and 2022–23 🟢 |
| Loan grading | A–D internal grades; grade mix disclosed (the numbers were not included in what you pasted) 🟢 |
| Fees | 1.5% management fee, stepping down to 1.0% after the investment period 🟢. Every other fee is not stated |

## 2. Return Stress-Test

Scripts run with a **4-year** assumed lock-up (🔴 assumed: midpoint of the `01` 3–5 yr fund baseline, because the fund term is not stated).

| Case | Net to LP | Swing assumptions | vs HYG (4.83% 10yr) | vs 3mo T-bill (4.24%) | Clears ~300–400bps hurdle? |
|---|---|---|---|---|---|
| **Bull** | ~10% 🟡 | Defaults stay ~3%, capital fully deployed, loan coupons hold up | ≈517bps | ≈576bps | Yes |
| **Base** | 9% (GP target) 🟢 | Defaults at the historical 3.1%, recovery at 92% | **417bps** (script) | 476bps (script) | **Yes. CLEARS comfortably** |
| **Bear** | ~7.5% 🟡 | Defaults double to ~6.2%, recovery falls to ~80% as a price decline eats the as-is cushion, plus ~50bps of cash drag from slower deployment or extensions | **267bps** (script) | 326bps (script) | **No. THIN / FAILS** |

**The three swing assumptions:**
1. **Loss severity in a falling-price market.** The 92% recovery was earned in 2020 and 2022–23, when residential values mostly held or rose. A 68% as-is LTV gives about a 32% cushion. That cushion gets used up by a price decline plus foreclosure time and cost. If recovery falls from 92% to 80%, that alone roughly quadruples annual loss drag (3.1% × 8% ≈ 25bps becomes 3.1% × 20% ≈ 62bps; at doubled defaults it is ≈124bps). 🟡
2. **What "3.1% default rate" measures.** Annual vs cumulative, by loan count vs dollar balance, and whether extensions and modifications count as defaults. If it is cumulative since inception, the base case is conservative. If it counts loans and the defaults were the large ones, it understates the loss. 🔴 unverifiable from the disclosure
3. **Deployment and rate path.** Bridge coupons follow short rates. At this snapshot, 9% net is ≈476bps over the 3mo bill and ≈413bps over the 2yr (4.87%), inside the `05` band of 315–575bps. If short rates fall, loan coupons reset lower at origination and the 9% target is harder to hold without moving down the credit grades. 🟡

**Read:** At the base case the premium pays for the lock-up. The bear case shows the thin margin. A roughly 150bps move in loss plus cash drag takes the deal below its illiquidity hurdle. It is still a positive return well above the Treasury floor, so the bear case is "under-compensated", not "capital impaired". 🟡 Standard `05` caveat: beating the spread is necessary, not sufficient, because dispersion means the median fund underperforms the marketed figure.

## 3. Where LP Returns Come From

- **Contractual interest plus origination points on short-dated senior loans.** This is income, not terminal value. The return does not depend on an exit cap, so `GEN-08` (exit-dependent IRR) and `EQUITY-06` do not apply. 🟢
- **Leverage: not determinable at the fund level.** Loan-level LTV is disclosed. Whether the *fund* borrows (a credit line or warehouse facility against the loan book) is not. If it does, part of the 9% is fund leverage on a thinner loan yield. That is the `CREDIT-01` mechanism: a modest book yield levered into a marketable LP number. It does not fire as a flag, but it has to be asked (Q-RISK-06). `GEN-07` (financing story) does not fire on what is disclosed. 🟡
- **Implied gross vs `01` norm.** The disclosed 1.5% management fee alone implies a gross of ≈10.5% for a 9% net. `01` says 11–13% gross is common. The gap means one of two things: (a) the book yields below the norm, which fits a conservative 68% as-is LTV, or (b) there are undisclosed fee layers (servicing, performance fee, admin) sitting between an ~11–13% gross and the 9% net. Either is plausible. The GP's gross portfolio yield answers it. 🟡

## 4. Fee Stack Summary

| Fee | Disclosed | `02` range | Status |
|---|---|---|---|
| Fund management fee | 1.5%, stepping to 1.0% after the investment period 🟢 | 1–2% of AUM; step-down expected | In range; step-down present (`HML-05` not fired). **Basis not stated**: committed vs invested capital changes the drag during ramp-up |
| Origination points (borrower-paid) | Not stated | 1–3 points | Unknown whether points go to the fund (LP yield) or the GP |
| Servicing fee | Not stated | 0.25–0.5% annual | Not stated |
| Performance fee / carry | Not stated | 10–20% above a 5–8% hurdle | **Not stated. This is the largest possible undisclosed layer** |
| Late fees / default interest | Not stated | Should go to the fund | Check they are not taken as a GP "workout fee" |
| Wind-down / liquidation fee | Not stated | 0.5–1% of remaining AUM | Not stated |
| Admin / IR | Not stated | 0.1–0.5% or $/LP | Not stated |

**Gross-to-net drag: ≈125–150bps/yr from disclosed fees only** (`fee_drag_calculator.py`: 150bps at a flat 1.5%; 125bps at an assumed 1.25% blended rate across the step-down, 🔴 assumed). Because the performance fee, servicing and admin were passed as `0` (undisclosed), **that is a floor, not the total.** A standard 20% carry over an 8% hurdle on a ~10.5% gross would add roughly 50bps. The full figure cannot be computed from this disclosure, and that is the finding. It is YELLOW, not RED, because the headline number is quoted *net* to LPs, which is the correct basis (`GEN-16`, partial).

## 5. Red Flags

**RED:** None fired. The disclosed facts support no RED, and none is manufactured here.

**YELLOW**
- **`GEN-16` (partial): incomplete fee and waterfall disclosure.** Only the management fee is disclosed. Carry, hurdle, servicing, the destination of origination points, and admin are unstated, so the full drag is unknowable. LP exposure: the 9% "net" cannot be reconciled to the gross book yield. → Q-FEE-01
- **`GEN-11`: net target with no distribution schedule.** A target return is quoted without saying whether income is distributed monthly or quarterly or reinvested during the investment period. For a debt fund, current distribution *is* the return story. Reinvested income turns an income fund into a back-loaded one. → Q-DIST-01
- **LTV basis inconsistency: an `HML-01`-family probe (flag not fired, because as-is LTV *is* disclosed).** A 68% LTV on as-is value and a 72% LTV on ARV can only both be true if the two ratios use different loan amounts, for example as-is on the initial advance and ARV on the full commitment including rehab holdbacks. ARV is normally *above* as-is value, so the same loan balance would give a *lower* LTV on ARV. This is probably a definitional issue, not a problem. But the as-is cushion is the central protection in this fund, so its definition must be pinned down: is it on funded balance or full commitment, and is it weighted by loan count or dollars? → Q-RISK-04
- **`GEN-06` (probe, unconfirmed): affiliate economics.** Servicing, origination points and workout or default fees in hard-money funds often go to GP affiliates. Nothing here says they do, and nothing says they don't. → Q-FEE-02

**Unverified, not fired**
- **`GEN-05` / `GEN-14`: track record.** The default and recovery statistics are realized loan-level data, which is good (🟢 stated). But no **net-to-LP realized fund return** is given for prior vintages. The loan book's history is disclosed; the LP outcome history is not. → Q-GP-02
- **`GEN-01`: GP co-invest.** Not stated. It is an absence, not evidence of zero co-invest. → Q-GP-01
- **`CREDIT-01`: fund-level leverage.** Not stated (see §3). → Q-RISK-06

**Explicitly cleared:** `HML-01` (as-is LTV given), `HML-02` (12 states, no metro above 15%), `HML-03` and `HML-04` (default and recovery both disclosed, through-cycle), `HML-05` (step-down present). `GEN-07` and `GEN-08` do not apply to a short-duration income book.

**Cluster check:** No RED cluster. The YELLOWs are all *completeness* gaps in fees, alignment and structure. None is a gap in the credit underwriting. That split is what supports a merits verdict.

## 6. Missing Disclosures

Measured against the `01` Hard Money essential-disclosure list: average LTV as-is and ARV ✔, default rate ✔, recovery rate ✔, geographic mix ✔, **foreclosure process and workout timeline ✘**, **sponsor history through a downturn: partial** (the loss statistics span 2020 and 2022–23, but the sponsor is not named).

Also missing, per `02` and the fund structure:
- Sponsor identity, years lending, AUM, and number of loans in the book
- **Performance fee / carry and its hurdle**; servicing fee; where origination points go; admin; wind-down fee (`GEN-16`)
- Management fee basis: committed vs invested capital
- Fund term, investment-period length, redemption or liquidity terms (Q-LIQ-01)
- Distribution policy: current-pay vs reinvested, and frequency (`GEN-11`)
- Fund-level leverage or credit facility (`CREDIT-01`)
- GP co-invest amount and terms (`GEN-01`)
- Definitions: default (annual vs cumulative; count vs dollar; whether extensions count); recovery (principal only or including accrued interest; net of foreclosure and legal costs)
- The grade-mix *numbers*, especially the share of C and D grade loans, and whether the D-grade share has drifted up over time
- Borrower mix (fix-and-flip vs rental bridge vs commercial) and lien position confirmation (1st lien on every loan?)
- Gross portfolio yield (reconciles the 9% net)
- Minimum investment and fund size

## 7. GP Alignment

- **Co-invest:** Not stated. Unverified. 🔴
- **Realized net-to-LP track record:** Not stated. The loan-level default and recovery data is realized and through-cycle, which is better than most HML pitches 🟢. But it is not the same as net-to-LP fund returns by vintage. Treat the track record as **partly verified**: credit performance yes, LP outcome no. 🟡
- **Fee alignment:** The management-fee step-down after the investment period is an LP-favorable structural choice 🟢. Without carry terms you cannot tell whether the GP is paid mainly for gathering AUM (fee-heavy, which rewards growth) or for performance (carry above a hurdle, which rewards credit quality). 🔴
- **Affiliate fees:** Not stated. Servicing and origination are the usual places GP economics hide in this deal type. 🔴

## 8. Questions for the GP

**Must-ask**

| # | Question (`04` ID) | Why here | Bad-answer signal |
|---|---|---|---|
| 1 | **Q-FEE-01**: complete fee schedule and waterfall, including carry, hurdle, servicing, destination of origination points, and admin | `GEN-16` partial fired | "Standard market fees"; "the PPM has it" without producing it; carry with no hurdle |
| 2 | **Q-FEE-02**: which service providers (servicer, originator, workout or REO manager) are GP-affiliated, and what they charge | `GEN-06` probe; HML economics often go through affiliates | "All arm's-length" without naming providers; origination points kept by the GP with no offset to LPs; default interest routed to a "workout fee" |
| 3 | **Q-RISK-04**: average LTV on as-is value, *and how it is measured* (funded balance vs full commitment; dollar-weighted?). Reconcile 68% as-is with 72% ARV | `HML-01`-family basis inconsistency | Cannot reconcile the two ratios; as-is LTV turns out to be on initial advance only while the full commitment is well above 68%; "our borrowers always complete" |
| 4 | **Q-RISK-05**: default and recovery rate definitions (annual vs cumulative; count vs dollar), average workout timeline, and the numbers for 2020 and 2022–23 separately | Verifies the core credit claim; `HML-03` / `HML-04` cleared on the headline, so this confirms it | Recovery is on principal only, gross of foreclosure costs; "we've never had a real loss"; no workout timeline; vintages blended so the stress years can't be isolated |
| 5 | **Q-RISK-06**: does the fund use a credit line or other leverage, and is the 9% levered? | `CREDIT-01` probe; the implied gross looks thin for the net | Won't give a number; "leverage is conservative"; the 9% net depends on a facility the LP was not told about |
| 6 | **Q-GP-02**: net-to-LP realized returns by fund or vintage | `GEN-05` / `GEN-14` unverified | Offers only loan-book yield or "target" figures; cannot separate realized from marked; no fund-level history |
| 7 | **Q-GP-01**: GP capital in the fund, on the same terms | `GEN-01` unverified | "Our expertise is our investment"; co-invest is a fee waiver; a token amount |
| 8 | **Q-GP-03**: any regulatory action, enforcement, or investor litigation | Sponsor not identified; this is a baseline for any lending platform | "Nothing material" with no yes/no; a search turns up something they did not disclose |
| 9 | **Q-DIST-01**: distribution policy (current pay vs reinvest) and frequency | `GEN-11` fired | "We distribute when the fund supports it"; reinvestment by default with no opt-out |
| 10 | **Q-LIQ-01**: fund term, and your options to exit early | Fund term and liquidity not stated | "A secondary market may develop"; redemption gates or suspension rights that are not disclosed |

**Nice-to-ask**
- **Q-DS-03**: bear-case return with defaults doubled and recovery at ~80%. Bad answer: "we underwrite conservatively" with no numbers, or the bear case still shows 9%.
- **Q-GP-04**: headcount and servicing or workout capacity vs AUM growth. Bad answer: AUM multiplied while the team stayed flat, and no named head of asset management or workouts. Workouts are a craft skill (`01`).
- **Q-DIST-02**: capital-call schedule, if it is a commitment fund. Bad answer: "calls as needed", or punitive dilution buried in the documents.
- **Q-LIQ-02**: K-1 delivery timing and history.
- Unindexed, category-specific: *"What share of the book is C and D grade today, and how has that share moved over the last three years?"* Bad answer: the D share is rising while the headline default rate is quoted from an older, higher-grade book.

## 9. Diligence Checklist

- [ ] **PPM and LPA**: confirm every fee, the carry and hurdle, management-fee basis, fund term, redemption or gate provisions, and where default interest and late fees go
- [ ] **Background check** on the sponsor and principals: SEC IAPD / Form ADV (if an RIA), FINRA BrokerCheck, state securities and lending-license regulators, litigation search
- [ ] **Audited fund financials** (most recent 2–3 years) and the auditor's name; confirm loss reserves and non-accrual loans
- [ ] **Loan tape**: loan-level LTV (as-is and ARV, with basis), grade, state or metro, maturity, extension status, lien position. Recompute the 68% / 72% and the metro concentration yourself
- [ ] **Default and recovery file**: every defaulted loan since inception, with resolution path (payoff, modification, foreclosure, REO sale), timeline, and net recovery after costs
- [ ] **Valuation practice**: who produces the as-is value and ARV (third-party appraisal vs BPO vs internal) and how old the valuations are
- [ ] **Credit facility documents** (if any): advance rate, covenants, recourse to LP capital
- [ ] **Servicer**: in-house or third-party; if affiliated, the fee schedule vs a third-party benchmark
- [ ] **LP references**, including an LP who invested before 2022, on distribution reliability through the rate spike

## 10. Verdict

**Pursue with conditions.**

**Why it clears:** This is the rare hard-money pitch that discloses what the `01` baseline says it should. It gives as-is LTV (not just ARV), a default rate *and* a recovery rate, loss history through both recent stress periods, genuine geographic diversification, and a fee step-down. The return is contractual income, not an exit bet. A 9% net sits in the middle of the 8–10% category band and is ≈417bps over HYG, clearing the ~300–400bps lock-up hurdle. It is also ≈413–476bps over the duration-matched Treasury, so the LP is paid for credit *and* illiquidity. 🟢

**Biggest swing factor:** Loss severity if residential collateral values fall. The 92% recovery is the protection behind the 9%, and it was earned in downturns where house prices held. The bear case (defaults doubled, recovery ~80%) takes the net to ~7.5%, below the illiquidity hurdle, but still well above the Treasury floor. That is under-compensation, not capital loss. 🟡

**Conditions (all confirmatory):**
1. The full fee schedule shows total drag reconcilable from the gross book yield to the 9% net, and any carry sits above a hurdle of 5–8% or more (`GEN-16`).
2. The fund uses no leverage, or modest disclosed leverage without recourse to LP capital, so the 9% is not levered (`CREDIT-01`).
3. The as-is LTV definition and the default and recovery definitions hold up against the loan tape (`HML-01` basis, `HML-03` / `HML-04`).
4. The sponsor passes the background check and shows meaningful co-invest and net-to-LP fund history (`GEN-01`, `GEN-02`, `GEN-05` / `GEN-14`).

**Who it suits:** An LP looking for income and a spread over high yield and T-bills, who can lock up capital for the fund term (probably 3–5 years), and who is willing to hold concentrated residential-credit exposure to one sponsor's workout skill. **It does not suit** an LP who needs liquidity before the term ends, or who is already heavily exposed to residential real-estate prices.

**What would have to be true:** Recoveries stay in the high 80s or above in a price-down market. That depends on the as-is cushion being real (measured on the full commitment, from independent valuations) and on the sponsor running workouts as competently as the 2020 and 2022–23 figures suggest.
