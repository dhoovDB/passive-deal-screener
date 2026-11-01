# Eval fixture 09
*Iteration-7 run, 2026-11-01, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 181fdd7.*

# Passive Deal Screen: "Multifamily fund, 15%+ returns"

**Verdict: Pass as presented: insufficient disclosure.**
*Screening output only, not investment advice.*

The quick take: this is a solicitation, not a deal. What you have is one return number with no basis, plus an investor-eligibility gate and a minimum check size. No sponsor, market, strategy, hold, fee, waterfall, leverage or track record is given. "15%+" can't be tested, because nothing says whether it is gross or net, an IRR or a cash yield, or over how many years. Nothing here is a reason to commit, and on its own it isn't evidence of a bad deal either. The useful move is to ask for the documents listed under "Re-screen list" below and run the screen again on those.

---

## 1. Deal Snapshot

| Field | As disclosed |
|---|---|
| Asset class | Multifamily 🟢. Strategy (value-add vs core / core-plus) is **not stated**, and `01` gives these very different baselines (see §2) |
| Deal type | Fund (pooled equity vehicle, presumably blind or semi-blind pool) 🟡. Routed as multifamily equity |
| Sponsor / GP | **Not stated** |
| Geography | **Not stated** |
| Minimum | $100,000 🟢 |
| Investor eligibility | Accredited investors only 🟢 (a private placement; says nothing about deal quality) |
| Hold / fund term | **Not stated** |
| Raise size / fund size | **Not stated** |
| Number of assets / pipeline | **Not stated** |
| Claimed return | "15%+ returns" 🟢 as a claim. **Basis not stated:** gross or net to LP, IRR or cash-on-cash or "total return," or annual vs cumulative 🔴 |
| Leverage / debt | **Not stated** |
| Fees / waterfall / pref | **Not stated** |
| Distribution schedule | **Not stated** |

Every "Not stated" row feeds §6.

---

## 2. Return Stress-Test

**No swing assumptions are disclosed.** There is no exit cap, rent growth, refi plan or leverage, so a base / bull / bear on this deal's own underwriting can't be built. What follows frames the headline against the references. It is not a projection of this fund.

**Against the asset-class baseline (`01`).**
- *If value-add:* 15% falls within `01`'s 12–18% *target* band, but above the 12–15% that realized deals have actually blended to 🟢. A "+" on top of the upper end of realized outcomes is a marketing number until the GP shows realized exits.
- *If core / core-plus:* `01` puts net IRR at 8–12% 🟢. A 15%+ claim would be well outside the category norm, and that alone would warrant a hard question about what risk is generating the excess.
- The strategy isn't stated, so it can't be said which baseline applies. That gap is itself a §6 item.

**Against the public comparator + illiquidity hurdle (`05`, `scripts/benchmark_comparator.py`, multifamily equity → VNQ 4.92% 10yr).** The hold isn't disclosed, so a 7-year lock-up is **assumed** 🔴. That is within `01`'s 5–7 year value-add hold, and the hurdle is ~400–600bps.

| Scenario (all 🔴 assumed bases) | Net-to-LP IRR | Premium over VNQ | Over 10yr Treasury (5.18%) | Read |
|---|---|---|---|---|
| "Bull": 15% is already **net** to LP | 15.00% | ≈1008bps | ≈982bps | Clears comfortably |
| "Base": 15% is **net**, but lands at the low end of `01`'s realized value-add blend | 12.00% | ≈708bps | ≈682bps | Clears comfortably |
| "Bear": 15% is **gross**, run through `02`'s representative equity fee stack (2% acq, 1.5% AM, 1% dispo, 0.3% admin, 20% promote over 8% pref with 100% catch-up, all assumed) | 10.60% | ≈568bps | ≈542bps | **Thin**: lower half of the 400–600bps band |

**Read:** whether this clears the lock-up depends entirely on one undisclosed fact, the **basis of the 15%**. Read as net, it clears easily. Read as gross with a market-typical fee load, it barely clears, and a real-world shortfall on the property would push it under. Under rule 2 (never gross-to-gross), the claim can't be credited until the GP states it as **net-to-LP IRR**. Clearing the spread is also necessary but not sufficient: `05` notes that dispersion means the median fund earns well below the marketed figure, and a fund adds manager-selection risk on top.

---

## 3. Where LP Returns Come From

**Can't tell from this** 🔴. No cash yield, leverage, exit cap or distribution schedule is disclosed, so the split between cash flow, exit and leverage can't be measured.

The `05` unlevered overlay frames the question. NCREIF NPI (unlevered institutional private RE) returned **5.00%** over the trailing four quarters to Q2 2026, almost all of it income. Residential NPI was 5.3% in 2025 🟢. If the 15% is a levered net IRR, **roughly 10 points would have to come from leverage and assumed appreciation rather than in-place operations** 🟡. That isn't automatically disqualifying, since leverage is how RE equity works, but it means most of the claimed return would be a financing bet (rate path, refi availability, exit cap), not an asset bet.

- `GEN-07` (financing story) and `GEN-08` (exit-dependent IRR >60%) **cannot be assessed**, and are **not fired**. Firing them would require assumed leverage and exit terms. Both route to must-asks `Q-DS-01` and `Q-DS-02` (§8).
- `EQUITY-06` (exit cap below going-in): no exit cap is disclosed, so it is unassessable. Routes to `Q-EXIT-01`.

---

## 4. Fee Stack Summary

**Disclosed fee stack: none.** Gross-to-net drag **is not computable from the disclosure**, and that is the finding (`GEN-16`).

`scripts/fee_drag_calculator.py`, run with `0` for every undisclosed fee as SKILL.md directs (15% gross, 7-yr hold both assumed): **0bps disclosed drag**. That figure is an artifact of disclosing nothing, not evidence of a fee-free fund. `02` says absent fees "are still paid."

For scale only: the same script on `02`'s representative multifamily equity stack (all inputs **ASSUMED**, none disclosed) gives **≈440bps/yr total drag**, taking 15.0% gross to ≈10.6% net (recurring ≈180bps, one-time ≈43bps, promote ≈217bps). That is the size of the gap the GP's fee schedule has to close.

Fee layers to surface, because none is disclosed (`02`):
- **Fund-level:** acquisition fee, asset management fee (and its base: committed vs invested capital), disposition fee, loan placement / refinance fees, admin / IR / K-1 fees.
- **Waterfall:** preferred return (rate, cumulative?, compounding?), promote / carry, catch-up rate, deal-by-deal vs whole-of-fund, clawback.
- **Affiliate layer:** property management, construction management, loan placement through GP affiliates (`GEN-06`).
- **Wrapper layer:** if this "fund" is a feeder or fund-of-funds into other sponsors' syndications, `02` puts the extra wrapper drag at 50–150bps/yr on top of the underlying deals' own fees. Verify both layers.

---

## 5. Red Flags

**RED (treated as RED until answered)**
- **`GEN-16`, No fee or waterfall disclosure (YELLOW–RED → treated RED)** 🟢. Not a single fee, pref, promote or waterfall term is given, so gross-to-net drag is unknowable and the 15% can't be translated into an LP outcome. → `Q-FEE-01`, `Q-FEE-03`, `Q-FEE-04`
- **`GEN-15`, Missing financials (YELLOW–RED → treated RED)** 🟢. No rent roll, T-12, debt terms or even an asset list; the absence is a choice. For a fund this is the portfolio/pipeline equivalent. → `Q-RISK-03`
- **`GEN-14`, No realized exits cited (RED)** 🟢. No track record of any kind is cited, realized or otherwise. The GP has not shown it has exited and returned capital. (`GEN-05`, GP-IRR vs LP-IRR divergence, is not fired since no IRR basis is cited at all; it is probed in the same question.) → `Q-GP-02`

**YELLOW**
- **`GEN-17`, Essential category-specific disclosure absent** 🟢. Every `01` multifamily essential disclosure is missing: rent roll, T-12, exit cap with sensitivity, debt structure and maturity, refi assumptions, GP's prior multifamily exits. → `Q-RISK-03`, `Q-DS-01`, `Q-RISK-01`, `Q-GP-02`
- **`GEN-03`, Marketing-heavy, substance-light** 🟢. A headline return and a "contact us" call to action stand in for underwriting. No urgency language is present, so this is a substance gap, not pressure selling. → `Q-FEE-01` / `Q-RISK-03` (request full underwriting and actuals)
- **`GEN-11`, Return with no distribution schedule** 🟢. A return figure with no indication of when capital comes back hides whether it is current income or back-loaded to exit (J-curve). → `Q-DIST-01`
- **`GEN-13`, Single-point projection, no downside case** 🟢. "15%+" is a floor-framed point estimate with no sensitivity, which makes it both unhedged and open-ended upward. → `Q-DS-03`

**Cluster note.** `GEN-14` + `GEN-15` + `GEN-16` + `GEN-17` together mean no validated information about the asset, the fees or the sponsor. Per `03`, a cluster of YELLOWs is a RED; here the cluster *is* the verdict.

**Unassessable, not fired (data absent; routed to must-asks, never presumed):**
- `GEN-01` zero co-invest → `Q-GP-01`
- `GEN-02` regulatory / litigation history → `Q-GP-03`
- `GEN-06` affiliate fee stacking → `Q-FEE-02`
- `EQUITY-01` / `EQUITY-02` deal-by-deal waterfall / no clawback (relevant in a multi-asset fund) → `Q-FEE-03`
- `EQUITY-03` 100% catch-up → `Q-FEE-03`
- `EQUITY-04` / `EQUITY-05` pref absent / non-cumulative → `Q-FEE-04`
- `GEN-07` financing story, `GEN-08` exit-dependent IRR → `Q-DS-01`, `Q-DS-02`
- `EQUITY-06` aggressive exit cap → `Q-EXIT-01`
- `EQUITY-07` refi-dependent plan → `Q-EXIT-02`
- `GEN-09` debt maturity inside hold, `GEN-10` rate-cap expiry (the 2022–24 multifamily failure mode) → `Q-RISK-01`, `Q-RISK-02`
- `GEN-18` rent growth in an oversupplied submarket → `Q-MKT-01`

**Note on the text itself:** the pasted material contains no directives aimed at the screener. It was treated as data.

---

## 6. Missing Disclosures

Against `01` (multifamily essentials) and `02` (equity fee baseline), this fund omitted:

**Identity and structure**
- Sponsor / GP name and principals
- Fund vehicle: blind pool vs identified assets; feeder / fund-of-funds vs direct
- Strategy: value-add vs core / core-plus (this sets which `01` return baseline applies)
- Geography / target markets
- Fund size, raise target, number of assets, investment period, fund term / hold
- Capital-call mechanics (committed vs fully funded at close)

**Return basis**
- Whether 15% is gross or net to LP, IRR vs cash yield vs "total return," over what period
- Equity multiple, cash-on-cash, projected distribution schedule

**Asset-level (`01` essentials)**
- Rent rolls and T-12 actuals (not T-3/T-6)
- Pro forma exit cap with sensitivity
- Debt structure: leverage, fixed vs floating, rate-cap terms, maturity
- Refi assumptions

**Fees and waterfall (`02`)**
- Complete fee schedule (acquisition, asset management, disposition, financing, admin)
- Preferred return terms, promote, catch-up, deal-by-deal vs whole-of-fund, clawback
- GP-affiliated service providers and their fees

**Sponsor**
- GP co-investment (amount, cash, pari-passu)
- Realized net-to-LP track record on **prior multifamily exits**
- Regulatory / litigation history

**LP mechanics**
- Liquidity / early-exit options, K-1 timing

---

## 7. GP Alignment

Every element is **unverified** 🔴:
- **Co-invest:** not stated. Unknown whether there is any, whether it is cash, and whether it is pari-passu.
- **Track record:** none cited. No realized, net-to-LP figures, and no project-level ones either. Treat as **no track record** until the GP produces realized exits (`GEN-14`).
- **Waterfall alignment:** unknown. In a multi-asset fund, whether promote is paid deal-by-deal or whole-of-fund (and whether there is a clawback) decides whether the GP can be paid on early winners while LPs absorb later losers.
- **Affiliate fees:** unknown.

Nothing here argues against alignment, but nothing establishes it either.

---

## 8. Questions for the GP

All escalated to must-ask where their `03` flag fired. Each has the bad-answer signal to listen for.

**Must-ask: the core story**
1. **`Q-FEE-01`** (`GEN-16`): "Can you provide the complete fee schedule and the full distribution waterfall?"
   *Bad answer:* "standard market fees"; a partial list; "the PPM has it" without producing it.
2. **`Q-GP-02`** (`GEN-14`, `GEN-05`): "Can you restate your track record as net-to-LP IRR on fully-realized, exited deals only?"
   *Bad answer:* only project-level or GP-level IRR; "most deals are still performing"; can't separate realized from unrealized.
3. **`Q-DS-01`** (`GEN-08`, `EQUITY-06`): "What share of projected LP IRR comes from in-place cash flow versus the exit, and what's the IRR at a flat exit cap?" Ask first: **is the 15% net to LP, and is it an IRR?**
   *Bad answer:* can't or won't decompose the IRR; "real estate always appreciates"; the IRR falls below pref at a flat exit cap.
4. **`Q-DS-02`** (`GEN-07`): "Strip out leverage and cap-rate compression — what is the unlevered, in-place return?"
   *Bad answer:* the levered IRR is the only figure; "leverage is just how the deal works."
5. **`Q-RISK-03`** (`GEN-15`, `GEN-12`, `GEN-17`): "Can you provide trailing-twelve-month actuals, the rent roll, and complete debt terms?" For a blind pool, ask for the pipeline and underwriting criteria.
   *Bad answer:* T-3/T-6 only; rent roll withheld; "the financials are confidential until you commit."
6. **`Q-DS-03`** (`GEN-13`): "What is the return under a bear case — flat rents, higher exit cap, no refinance?"
   *Bad answer:* no downside case; "we underwrite conservatively" with nothing to show; the bear case is still a gain.
7. **`Q-DIST-01`** (`GEN-11`): "What is the projected distribution schedule, and at what milestones does LP capital start returning?"
   *Bad answer:* "we'll distribute when the deal supports it"; no milestones; silence.

**Must-ask: alignment and structure**
8. **`Q-GP-01`** (`GEN-01`): "How much of your own capital is in this deal, on the same terms as LPs?"
   *Bad answer:* "our sweat equity is our investment"; a fee waiver presented as co-invest; a token amount on better terms.
9. **`Q-GP-03`** (`GEN-02`): "Have you or your principals faced any regulatory action, enforcement, or investor litigation?"
   *Bad answer:* "nothing material"; blames the regulator or LP; a search turns up something they didn't disclose.
10. **`Q-FEE-03`** (`EQUITY-01`, `EQUITY-02`): "Is the waterfall deal-by-deal or whole-of-fund, and is there a clawback?"
    *Bad answer:* deal-by-deal with high promote and no clawback; can't explain the catch-up; "you get paid when we get paid."
11. **`Q-FEE-04`** (`EQUITY-04`, `EQUITY-05`): "What preferred return do LPs receive before the GP earns promote, and is it cumulative and compounding?"
    *Bad answer:* pref below 6% or none; non-cumulative.
12. **`Q-FEE-02`** (`GEN-06`): "Which service providers are GP-affiliated, what do they charge, and are those rates third-party-benchmarked?"
    *Bad answer:* "all arm's-length" without naming providers; no benchmark offered.
13. **`Q-RISK-01`** (`GEN-09`): "When does the debt mature relative to the projected hold, and what's the refinance or extension plan?"
    *Bad answer:* maturity inside the hold; "we'll refinance" with no terms.
14. **`Q-RISK-02`** (`GEN-10`): "When does the rate cap expire relative to debt maturity, and what's the cost to extend it at current pricing?"
    *Bad answer:* cap expires before maturity; extension cost not modeled; "rates should be lower by then."
15. **`Q-EXIT-02`** (`EQUITY-07`): "Does the business plan depend on a refinance, and what happens to distributions if the refi isn't available on the assumed terms?"
    *Bad answer:* capital return requires a refi at lower rates; "the refi market will reopen."
16. **`Q-LIQ-01`**: "What are my options if I need to exit before the hold period ends?"
    *Bad answer:* "a secondary market may develop"; vague accommodation promises. An honest "there is none" is a good answer.

**Nice-to-ask**
- **`Q-EXIT-01`** (`EQUITY-06`): "Why is the exit cap below the going-in cap, and what's the IRR at an exit cap equal to or above going-in?" Escalates to must-ask once an exit cap is disclosed below going-in.
- **`Q-MKT-01`** (`GEN-18`): "What submarket supply pipeline and absorption data support the rent-growth assumption?" Escalates once markets are named.
- **`Q-DIST-02`**: "When are capital calls expected, and what's the consequence of a missed or late call?" (relevant if this is a commitment-and-call fund). *Bad answer:* "calls as needed"; punitive dilution buried in the docs.
- **`Q-GP-04`** (`GEN-04`): "How have your headcount and deal-monitoring capacity grown alongside AUM?"
- **`Q-LIQ-02`**: "When will K-1s be delivered each year, and have you historically delivered them before the filing deadline?"

---

## 9. Diligence Checklist

Independent verification still needed once documents arrive:
- **PPM, operating agreement, subscription docs.** Reconcile the fee schedule and waterfall against the marketing claim.
- **Regulatory filings.** Form D on SEC EDGAR for the offering; if the manager is a registered adviser, Form ADV Part 2 for fees and disciplinary history.
- **Background checks** on principals (regulatory, litigation, bankruptcy).
- **Realized track record verification.** Request audited fund financials or LP references from prior exited deals.
- **Asset-level:** rent rolls and T-12s (or pipeline underwriting for a blind pool), third-party appraisals, rent and sales comps, property condition reports.
- **Debt:** lender term sheets / loan docs, rate-cap agreements and their expiry dates.
- **Fund administration / audit:** confirm an independent administrator and auditor.

---

## 10. Verdict

**Pass as presented: insufficient disclosure.**
*Screening output only, not investment advice.*

**Reasoning.** The `01` essential disclosures for multifamily are not partly missing but **entirely** absent, along with the fee stack, waterfall, sponsor identity and track record. There is no core return story to underwrite, only a headline. That clears the "substantially absent" bar for an insufficient-disclosure pass. It is a verdict on the *disclosure*, not a finding that the fund is bad: no RED flag was fired on the merits, and none should be invented.

**Biggest swing factor:** the **basis of the "15%+."** As net-to-LP IRR, it clears the VNQ + 7-year illiquidity hurdle by a wide margin (≈1008bps vs ~400–600bps). As a gross figure under a market-typical `02` fee stack, it compresses to ≈10.6% net, a thin ≈568bps premium that a modest operating shortfall would erase. Second is how much of it is leverage. With unlevered private RE at ~5% (NCREIF NPI), most of a 15% levered return would be a financing bet.

**Who it could suit (if it re-screens well):** an accredited LP with $100k they can lock up for an undisclosed multi-year term, comfortable with multifamily equity risk and blind-pool manager risk, who has verified the sponsor independently.

**What would have to be true for a merits verdict:**
- The 15% is restated as net-to-LP IRR, with a distribution schedule and a bear case.
- Fees and waterfall are disclosed and land within `02` norms (pref ≥6%, cumulative; promote ≤30%; whole-of-fund or deal-by-deal with clawback).
- The GP produces realized, net-to-LP results on prior multifamily exits.
- Debt terms show maturity and rate-cap coverage beyond the business plan.
- The GP has meaningful cash co-invest on pari-passu terms.

**Re-screen list (send back to the sponsor):**
1. PPM / offering memorandum with full fee schedule and waterfall
2. Return basis (net-to-LP IRR, equity multiple, cash-on-cash, distribution schedule) with sensitivity
3. Strategy, target markets, fund size, term, and asset list or pipeline
4. Rent rolls and T-12s (or underwriting criteria for a blind pool) and full debt terms
5. Realized track record, net to LP, on exited multifamily deals
6. GP co-invest amount and terms; regulatory/litigation disclosure
7. Liquidity / redemption terms and capital-call mechanics
