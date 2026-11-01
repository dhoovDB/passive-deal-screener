# Eval fixture 13
*Iteration-7 run, 2026-11-01, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 181fdd7.*

# Passive Deal Screen: Diversified BDC-Style Private Credit Fund

**Verdict: Pursue with conditions.** The structure is sound: no RED flags, and the disclosures that matter most for private credit (leverage, loan count, sector spread, through-cycle default and recovery, levered and unlevered IRR) are all there. What's left is numbers and people. The memo describes the structure but doesn't give the figures (net IRR, incentive-fee rates, hurdle level, term or liquidity) or name the sponsor and its realized record. Those are conditions to clear before committing, not grounds to pass.

*Screening output only, not investment advice.*

---

## 1. Deal Snapshot

| Field | Value | Confidence |
|---|---|---|
| Asset class | Private Credit (fund) | 🟢 stated |
| Deal type | Private credit fund, BDC-style (fund-level leverage, asset-coverage regime) | 🟢 stated |
| Sponsor / GP | Not stated | — |
| Geography | Not stated (sector-diversified; regional mix not given) | — |
| Minimum investment | Not stated | — |
| Hold / term / liquidity | Not stated. The `01` norm for private credit is 3–7 yrs. Whether this is a traded or non-traded vehicle, evergreen or closed-end, is not stated. | 🔴 |
| Raise / fund size | Not stated beyond "large" | 🟡 |
| Claimed return | Net IRR "stated on a levered basis, with the unlevered figure also shown", but the figures were not given in what was shared | 🟢 that it exists / 🔴 its value |
| Management fee | 1.5% on gross assets; 1.0% on assets financed above the 200% asset-coverage threshold (i.e. leverage beyond 1.0x debt/equity) | 🟢 stated |
| Incentive fee | Two-part (income + capital-gains style), with a hurdle and a high-water mark. **Rates, hurdle level, and catch-up not stated.** | 🟢 structure / 🔴 terms |
| Fund leverage | ~1.1x, disclosed, "within the standard range" | 🟢 stated |
| Portfolio | 400+ loans, diversified across sectors | 🟢 stated |
| Credit history | Through-cycle default and recovery rates disclosed (figures not given here) | 🟢 that it exists |

---

## 2. Return Stress-Test

**The headline figure wasn't included, so this section shows the bar the stated net IRR has to clear rather than a verdict on a number.** Benchmark per `05`: HYG (4.83% 10yr) plus the 2yr Treasury (4.87%) as the duration-matched floor. PRIV has too short a history to use. Results from `benchmark_comparator.py --deal-type private-credit`, run across the `01` private-credit net range (8–12%) and the `01` hold range:

| Net-to-LP IRR (levered) | Premium over HYG | Over 2yr UST | 3–5 yr lock-up (hurdle ~300–400bps) | 7 yr lock-up (hurdle ~400–600bps) |
|---|---|---|---|---|
| 8% | ≈317bps | ≈313bps | CLEARS (thin) | THIN / FAILS |
| 10% | ≈517bps | ≈513bps | CLEARS comfortably | CLEARS (thin) |
| 12% | ≈717bps | ≈713bps | CLEARS comfortably | CLEARS comfortably |

🟢 for the comparator and hurdle figures; 🔴 for where this fund actually lands, because the IRR and the term weren't provided.

**The read:** below about 9% net, this fund is a thin trade for a multi-year lock-up. The Treasury curve alone pays about 4.9% with no credit or liquidity risk. Ten percent or more net on a 3–5 yr effective lock-up clears comfortably.

**Run the comparison on the unlevered figure too.** The fund discloses it, which is unusual and useful. If the *unlevered* net return barely clears HYG, then most of the illiquidity premium comes from the 1.1x leverage, not from loan selection (see §3).

**Scenarios. These name the swing assumptions; no figures are assumed:**
- **Base:** loan coupons minus realized credit losses minus facility interest, at about 1.1x leverage, minus the fee drag in §4. That lands at the stated levered net IRR.
- **Bull:** defaults stay below the disclosed through-cycle rate and recoveries hold at the top of the `01` range (~60–80% historically). The incentive fee takes a larger share of the upside above the hurdle.
- **Bear:** a credit cycle pushes defaults above the through-cycle average while recoveries fall toward or below the bottom of the `01` range. **Leverage amplifies this mechanically.** At 1.1x, gross assets are about 2.1x NAV, so each 1% of credit loss on the loan book costs about 2.1% of LP NAV (🟢 arithmetic from the stated leverage). If losses also erode asset coverage toward the 200% floor, the fund may have to deleverage, and forced sales would crystallize marks.

**The 2–3 swing assumptions:**
1. **Default rate × (1 − recovery rate)**, the realized loss rate. The disclosed through-cycle figures are the anchor. Make sure they cover 2020 and 2022–23 (`Q-RISK-05`).
2. **Cost and terms of fund-level debt.** The spread between loan yield and facility cost is what the 1.1x levers. Facility maturity and repricing matter (`Q-RISK-01`, `Q-RISK-06`).
3. **Mark-to-model valuation.** Per `05`, private-credit vehicles report *smoothed* marks, so reported volatility understates true risk. A low-volatility NAV history is not evidence of low risk.

---

## 3. Where LP Returns Come From

- **Cash flow, not exit.** Return is contractual interest income on 400+ loans. There is no terminal-value or exit-cap bet. `GEN-08` (exit-dependent IRR) and `EQUITY-06` (aggressive exit cap) **do not apply** to a diversified loan book. 🟢
- **Leverage share: measurable here, but not yet measured.** The fund shows both levered and unlevered net IRR, which is exactly what `02` (fund-level leverage costs) and `CREDIT-01` ask for. The gap between the two figures is the leverage contribution. **The >60% leverage-driven test can't be run without the two figures.** That makes it a condition, not a finding. If the unlevered figure is more than ~60% below the levered one, return the finding to `GEN-07` (financing story).
- **The financing-story flag does not fire on what's disclosed.** `GEN-07` is not fired. Leverage is moderate (1.1x, below the `02`/`03` >1.5x threshold) and the unlevered return is disclosed, not hidden. This is a transparent use of leverage, not a disguised one. 🟢

---

## 4. Fee Stack Summary

| Fee | Stated term | `02` norm (private credit) | Read |
|---|---|---|---|
| Management fee | 1.5% of **gross assets**, 1.0% on assets financed above 1.0x leverage | 1–2% of committed/invested capital | Rate is in range, **but the base is gross assets, not LP capital** (see below) |
| Incentive fee (income + capital gains) | Hurdle + high-water mark; rates, hurdle level, and catch-up not stated | 10–20% above a 5–7% hurdle; aggressive >25% or hurdle <5%; soft hurdle with 100% catch-up is aggressive | High-water mark is the LP-favorable standard. Rates are needed to compute drag |
| Servicing fee | Not stated | 0.25–0.5% of loan balance | Ask; may be borne at the loan level |
| Fund-level leverage costs | Facility interest at ~1.1x (cost not stated) | *Variable* | Disclosed in shape; cost not given |
| Admin / IR / fund expenses | Not stated | $1–3k per LP, or 0.1–0.3% of capital | Ask. In BDC-style vehicles, operating expenses are a material separate line |

**The fee-base finding (🟢, arithmetic on stated terms).** A management fee on *gross assets* is charged on borrowed money too. At 1.1x leverage, gross assets are 2.1x LP NAV:
- 1.5% on the first 2.0x of NAV (assets up to the 200% coverage level) = 3.0% of NAV
- 1.0% on the next 0.1x of NAV = 0.1% of NAV
- **Effective management fee ≈ 3.1% of LP equity per year**, against a 1.5% headline.

The tiered rate (1.0% above 1.0x leverage) is the market's own fix for this. It blunts the GP's incentive to keep adding leverage, but it doesn't remove it. The GP still earns more in fees at 1.1x than at 0.5x. Read against equity, 3.1% is above the `02` aggressive threshold (>2%), but that threshold is written for fees on committed or invested capital. That makes this a **base-definition mismatch to put to the GP**, not a fired flag. The fee is disclosed, and the stated net IRR already reflects it. It is still the alignment side of `CREDIT-01`.

**Gross-to-net drag (illustrative, `fee_drag_calculator.py`):**
- Management fee alone, on the stated base: **≈310bps/yr** of drag on LP equity (`--fund-mgmt-fee 3.1`).
- For comparison, the same 1.5% charged on NAV would be ≈150bps/yr. **The gross-asset base costs the LP about 160bps/yr more.**
- **Total drag: not computable from what was disclosed.** Incentive-fee rates, hurdle, catch-up, admin/operating expenses, and servicing are not stated, so they were passed as 0 per the script contract. The real total drag is **≥310bps/yr plus the incentive fee plus expenses**. 🔴 for the total.
- The script inputs gross IRR 13% and hold 5 yrs are **assumed placeholders** used only to size the management-fee line. They are §6 gaps, not findings. The management-fee drag in bps doesn't depend on them.

**This is the main thing to ask the GP:** the stated levered net IRR is already after this stack. The LP needs the full fee table to tell how much of the gross loan-book yield the GP's fees absorb, and how much of that is earned *on the leverage itself*.

---

## 5. Red Flags

**RED:** none fired. 🟢

**YELLOW:**
- **`GEN-16` (no fee or waterfall disclosure). Partial, YELLOW.** The fee *structure* is disclosed, but the incentive fee's rates, hurdle level, catch-up, and fund operating expenses are not. Without them, gross-to-net drag can't be computed (§4). → `Q-FEE-01`, `Q-FEE-04`.
- **`GEN-11` (cash-flow timing / J-curve not disclosed). YELLOW.** A net IRR is cited with no distribution policy or schedule. For an income vehicle, the distribution cadence and whether distributions are covered by net investment income is the core LP experience. → `Q-DIST-01`.

**Checked and not fired. Each is cited because §§2–4 touch its family:**
- **`CREDIT-01` (fund leverage stacked on loan leverage). Not fired.** Leverage is ~1.1x and disclosed, below the >1.5x threshold, and the IRR is shown on both a levered and unlevered basis, which is exactly what the flag's question asks for. Residual: the gross-asset fee base (§4) means leverage raises GP fees as well as LP returns. Confirm via `Q-RISK-06`.
- **`CREDIT-02` (sector concentration). Not fired.** 400+ loans across sectors. Ask for the largest single-sector exposure to confirm (`CREDIT-02` → its response question).
- **`HML-03` / `HML-04` (default / recovery rate not disclosed). Not fired.** Both are disclosed, through-cycle. Confirm the window covers 2020 and 2022–23 (`Q-RISK-05`).
- **`GEN-07` (financing story). Not fired on what's disclosed.** Leverage is moderate and the unlevered figure is shown. It would fire only if the levered/unlevered gap shows more than 60% of the return is leverage (§3).
- **`GEN-08` / `EQUITY-06`.** Not applicable to a loan book with no exit-cap assumption.
- **`HML-05` (no management-fee step-down).** Not assessable. The fund steps down by leverage tier, but whether it's evergreen or closed-end with an investment period isn't stated. Ask if closed-end.
- **`GEN-09` (debt maturity inside horizon).** Not assessable. The facility behind the 1.1x has no maturity stated. Probe via `Q-RISK-01` per the proactive trigger.
- **`GEN-13` (no sensitivity / downside case).** Not assessable; nothing says whether a stress case is provided. → `Q-DS-03`.

**Not tested (no information provided, so not fired, routed to must-asks):**
- `GEN-01` (co-invest) → `Q-GP-01`
- `GEN-05` / `GEN-14` (track record basis and realization) → `Q-GP-02`
- `GEN-02` (regulatory history) → `Q-GP-03`
- `GEN-06` (affiliate fees) → `Q-FEE-02`

**Clusters:** none. The two YELLOWs are disclosure gaps, not a structural pattern.

---

## 6. Missing Disclosures

Against the `01` Private Credit essential-disclosure list (loan count and average loan size, sector mix, fund leverage, seniority position, through-cycle default and recovery):

| `01` essential | Status |
|---|---|
| Loan count | 🟢 Disclosed (400+) |
| **Average loan size** | **Missing** |
| Sector mix | 🟢 Disclosed qualitatively ("diversified"). Ask for the breakdown |
| Fund leverage ratio | 🟢 Disclosed (~1.1x) |
| **Seniority position** (first-lien / unitranche / second-lien / mezz mix) | **Missing.** Material: the `01` recovery norm of ~60–80% assumes senior secured |
| Through-cycle default and recovery | 🟢 Disclosed (figures to confirm) |

**Also missing (from `02` and the snapshot):**
- The actual net IRR figures, levered and unlevered (the input that's needed most)
- Incentive-fee rates, hurdle level, hurdle type (hard vs soft), catch-up
- Fund operating / admin expenses, servicing fees
- Fund-level facility cost, maturity, fixed vs floating
- Distribution policy and schedule (`GEN-11`)
- Term, structure (evergreen / closed-end, traded / non-traded), and redemption or liquidity mechanics
- Sponsor identity, realized net-to-LP track record, GP co-investment
- Minimum investment, fund size
- Non-accrual rate and valuation methodology (marks are smoothed, per `05`)

**Assumptions used in this report (🔴, each a gap):** the 8–12% IRR band and the 3/5/7-yr lock-ups in §2 (taken from the `01` range, not from the deal); gross IRR 13% and hold 5 yrs as placeholders in the §4 drag run; 0 passed for every undisclosed fee.

---

## 7. GP Alignment

- **Co-investment: not stated.** Unverified. → `Q-GP-01`.
- **Track record: not stated.** No realized net-to-LP record was given. Until it is, the GP's record is **unverified** (`GEN-14` / `GEN-05` are untested, not cleared). → `Q-GP-02`.
- **Incentive-fee alignment, mixed:**
  - ✅ **High-water mark.** No incentive fee on losses being recouped. This is LP-favorable and the `02` standard.
  - ✅ **Hurdle present.** Its level and type are unknown. A soft hurdle with 100% catch-up would be the aggressive variant (`02`).
  - ⚠️ **Gross-asset management-fee base.** The GP earns fees on borrowed capital, so it has a modest built-in incentive to run leverage toward the top of the permitted range. The 1.0% rate above 1.0x leverage dampens this. 🟢
  - ⚠️ **Two-part incentive fee.** The income component is typically paid on accrued income, so the GP can be paid on interest that later defaults. Ask whether the income fee carries any total-return or look-back protection. (🟡: the mechanism is common to two-part structures; this fund's specific terms are not stated.)
- **Affiliate fees: not stated.** → `Q-FEE-02`.
- **Transparency signal (positive, 🟢):** disclosing the unlevered IRR, through-cycle defaults, *and* recoveries is above the usual marketing standard. A GP that volunteers what `CREDIT-01`, `HML-03`, and `HML-04` ask for has pre-answered the hardest debt-fund questions.

---

## 8. Questions for the GP

### Must-ask

| ID | Question | Bad-answer signal (the specific dodge) | Fired by |
|---|---|---|---|
| `Q-FEE-01` | "Can you provide the complete fee schedule, including incentive-fee rates, hurdle level, catch-up, operating expenses, and servicing?" | "Standard market fees"; partial list; "the PPM has it" without producing it; fees surface only after commitment. | `GEN-16` |
| `Q-FEE-04` | "What hurdle does the LP receive before any incentive fee, is it hard or soft, and is it cumulative?" (adapted from the pref question to the credit-fund hurdle) | Hurdle below the `02` 5% floor; soft hurdle with 100% catch-up; can't explain how the high-water mark interacts with it. | `GEN-16` (incentive terms) |
| `Q-DIST-01` | "What is the distribution policy and schedule, and are distributions covered by net investment income?" | "We'll distribute when the portfolio supports it" with no milestones; an IRR quoted with no distribution timing. | `GEN-11` |
| `Q-RISK-06` | "What is the fund's leverage ratio, and is the quoted LP IRR levered or unlevered?" (already answered, so ask for the two figures and the maximum leverage the documents permit) | Won't give the permitted maximum; "leverage is conservative" with no number; the unlevered figure turns out to be gross of fees. | `CREDIT-01` (confirm) |
| `Q-RISK-05` | "What are your historical default and realized recovery rates, including through 2020 and 2022–23?" | Default rate without recovery (or the reverse); the "through-cycle" window starts after 2020; silence on 2022–23. | `HML-03`, `HML-04` (confirm) |
| `Q-RISK-01` | "When does the fund's credit facility mature relative to the fund's term, and what's the refinance or extension plan?" | Facility matures inside the fund's life with "we'll refinance" and no terms; no plan if the facility market tightens. | `GEN-09` (probe; stated debt term) |
| `Q-GP-02` | "Can you restate your track record as net-to-LP IRR on fully-realized prior funds only?" | Only gross or portfolio-level IRR; "most funds are still investing"; can't separate realized from marked. | `GEN-05`, `GEN-14` (untested) |
| `Q-GP-01` | "How much of your own capital is in this fund, on the same terms as LPs?" | Co-invest is a fee waiver, not cash; a token amount on better terms. | `GEN-01` (untested) |
| `Q-GP-03` | "Have you or your principals faced any regulatory action, enforcement, or investor litigation?" | "Nothing material"; a search surfaces something not disclosed. | `GEN-02` (untested) |
| `Q-FEE-02` | "Which service providers are GP-affiliated (administrator, servicer, origination platform), what do they charge, and are those rates benchmarked?" | "All arm's-length" without naming providers; affiliate fees undisclosed. | `GEN-06` (untested) |
| `Q-DS-02` | "Strip out leverage — what is the unlevered, in-place return?" (already shown, so ask for the two figures side by side) | The unlevered figure is gross of fees, or computed on a different basis or period than the levered one. | `GEN-07` (test) |
| `Q-DS-03` | "What is the return under a bear case: defaults at the worst observed vintage, recoveries at the low end, and facility cost up?" | Single-point projection; "we underwrite conservatively" with nothing to show; the bear case is still a gain. | `GEN-13` (not assessable) |
| `Q-LIQ-01` | "What are my options if I need to exit before the fund's term ends: redemption program, tender limits, gating?" | "A secondary market may develop"; "we'll try to accommodate"; the redemption cap and gating terms aren't stated. | — |

### Nice-to-ask

| ID | Question | Bad-answer signal |
|---|---|---|
| `CREDIT-02` response | "What is the sector breakdown and your largest single-sector exposure?" | "Diversified" with no breakdown. |
| `Q-FEE-03` | "How do the income and capital-gains incentive fees interact with the high-water mark, and is there any look-back or clawback?" | Can't explain how the components interact; income fee paid on accrued interest that later defaults, with no look-back. |
| `Q-GP-04` | "How have headcount and credit-monitoring capacity grown alongside AUM?" | AUM multiplied with a flat team; no named workout function for a 400+ loan book. |
| `Q-DIST-02` | "Is capital called or funded up front, and what's the consequence of a missed call?" | "Calls as needed" with no notice period; punitive dilution buried in the docs. |
| `Q-LIQ-02` | "When are K-1s / 1099s delivered each year?" | "As soon as we can"; a history of extensions. |

---

## 9. Diligence Checklist

- [ ] **Offering documents / PPM or prospectus:** confirm the fee table (incentive rates, hurdle, catch-up, high-water mark mechanics), the expense cap, leverage limits, and redemption or gating terms.
- [ ] **Audited financials:** non-accrual rate, realized vs unrealized losses, NII coverage of distributions, facility terms.
- [ ] **Valuation policy:** who marks the loans (third-party valuation agent?) and how often. Read reported volatility knowing private-credit marks are smoothed (`05`).
- [ ] **Default and recovery data:** source, period (must include 2020 and 2022–23), and definition (realized loss vs non-accrual).
- [ ] **Portfolio schedule:** seniority mix, average loan size, top-10 borrowers, sector breakdown.
- [ ] **Credit facility:** lender, maturity, covenants, cost, and headroom against the 200% asset-coverage floor.
- [ ] **Sponsor background:** SEC Form ADV (Part 2 fee schedules), regulatory and litigation search on the manager and principals.
- [ ] **Realized track record:** net-to-LP returns on prior, fully-realized vehicles.
- [ ] **Tax reporting:** form type and delivery timing.

---

## 10. Verdict

**Pursue with conditions.**

*Screening output only, not investment advice.*

**Reasoning.** This is a structurally clean private-credit fund. It discloses what `01` treats as essential for the class: fund leverage, loan count, sector diversification, and through-cycle default *and* recovery. It also does what `CREDIT-01` asks of BDC-style funds: it states the IRR on a levered basis and shows the unlevered figure. Leverage at ~1.1x is moderate and below the >1.5x threshold. The return is contractual income, not an exit bet. The incentive fee has both a hurdle and a high-water mark. Nothing disclosed fires a RED. Enough is disclosed to underwrite the core return story, so this is a merits verdict, not "as presented." The residual absences are conditions.

**Biggest swing factor:** realized credit loss (default × (1 − recovery)) **amplified by leverage.** At 1.1x, each 1% of loan-book loss costs about 2.1% of LP NAV. The disclosed through-cycle figures are the right evidence, provided the window covers 2020 and 2022–23.

**Second issue: what the fees cost the LP.** The management fee is charged on gross assets, so it runs at about 3.1% of LP equity per year (≈310bps of drag) before any incentive fee. That's about twice the headline rate, and the GP earns part of it on the leverage itself.

**Conditions to move forward:**
1. **Net IRR, levered and unlevered:** clears HYG (4.83%) and the 2yr Treasury (4.87%) by the illiquidity hurdle for the actual lock-up. That's ≥300–400bps for 3–5 yrs, ≥400–600bps for 7 yrs. Below about 9% levered net, this is a thin trade. If the unlevered figure barely clears HYG, the premium is leverage, not credit selection (`GEN-07` test).
2. **Full fee table** (`GEN-16`): incentive rate ≤20%, hurdle ≥5% (hard, or soft without a 100% catch-up), and the total drag including operating expenses is acceptable against the gross loan-book yield.
3. **Distribution policy** (`GEN-11`): distributions covered by net investment income, not return of capital.
4. **Default and recovery window** includes 2020 and 2022–23; the seniority mix is mostly first-lien.
5. **Sponsor:** a realized net-to-LP track record (`Q-GP-02`), meaningful cash co-invest (`Q-GP-01`), and a clean regulatory search (`Q-GP-03`).
6. **Liquidity terms** are known and acceptable (`Q-LIQ-01`).

**Who it suits:** an income-oriented LP who wants diversified senior-credit exposure, accepts a multi-year lock-up or redemption that can be gated, and knows that smoothed NAV marks understate true volatility.

**What would have to be true:** the stated levered net IRR clears the Treasury floor plus the illiquidity hurdle after all fees, *and* the unlevered figure shows that most of that premium comes from credit selection rather than the 1.1x leverage. A levered net IRR in the high single digits with an unlevered figure near HYG would move this toward Pass. The LP would be paying about 3%+ per year to own levered high yield in an illiquid wrapper.
