# Eval fixture 05
*Iteration-7 run, 2026-11-01, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 181fdd7.*

# Passive Deal Screen: Private Credit Fund (unnamed sponsor)

**Verdict: Pass as presented — insufficient disclosure**

*Screening output only, not investment advice.*

The terms you have show a fund that gets its 12% by putting leverage (~2.5x) on a loan book that is ~60% in one sector. Those two facts together are a RED cluster (`CREDIT-01` + `CREDIT-02`). Most of what a private-credit fund normally discloses is also missing: loan count, default and recovery history, carry and hurdle, hold period, track record, and the sponsor's name. Without those, the core return story can't be underwritten. Re-screen only if the GP answers the must-asks in §8. The biggest swing factor is how much of the 12% comes from leverage and how much from the loans themselves.

Confidence tags: 🟢 stated, or taken from a reference · 🟡 inferred · 🔴 assumed or unverifiable.

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Private Credit (fund) 🟢 |
| Deal type | Private credit fund, senior secured, with fund-level leverage 🟢 |
| Underlying collateral / borrower type | Not stated (corporate or real-estate lending?) |
| Sponsor / GP | Not stated |
| Geography | Not stated |
| Minimum investment | Not stated |
| Hold / fund life | Not stated (category norm is 3–7 yrs per `01`) |
| Raise / fund size | Not stated |
| Claimed return | "12% net IRR to investors", quoted, so a target and not a realized figure 🟢/🟡 |
| Fund leverage | ~2.5x 🟢. The basis is not stated: debt-to-equity, or assets-to-equity? |
| Sector concentration | ~60% of the loan book in one sector 🟢. The sector is not named |
| Seniority | "Senior secured" 🟢 at the loan level. The LP still sits behind the fund's own lender (see §3) |
| Management fee | 2% 🟢. Basis (committed, invested, or gross assets) and step-down not stated |
| Carry / hurdle / catch-up | Not stated |
| Other fees (servicing, admin, leverage costs) | Not stated |
| Distribution schedule | Not stated |
| Track record | Not stated |

## 2. Return Stress-Test

**Benchmark (via `scripts/benchmark_comparator.py`, deal type `private-credit`, net IRR 12%):**

- 12% net vs **HYG 4.83%** (10yr trailing) gives **≈717 bps** of premium. At an assumed 5-yr lock-up 🔴 the illiquidity hurdle is ~300–400 bps. At 7 yrs, the top of the `01` range, it is ~400–600 bps. Read: **clears comfortably** at either hold.
- Over the **2yr Treasury (4.87%)** the premium is **≈713 bps**. That is the absolute credit-plus-illiquidity spread the LP is being promised.
- **Why the headline clear doesn't settle it.** HYG is an unlevered, diversified basket of hundreds of issuers. This fund is (a) levered ~2.5x and (b) ~60% in one sector. The comparator diversifies away exactly the two risks this fund concentrates, so the ≈717 bps buys levered, correlated credit risk and not just illiquidity. The `05` spread table says it directly for private credit: "Clears; check fund leverage isn't manufacturing the spread (`CREDIT-01`)." 12% is also the **top** of the `01` net range (8–12%) 🟢. Top-of-range from a 2.5x-levered book suggests the unlevered loan yield may be ordinary 🟡. Private-credit marks are smoothed (`05`, PRIV note), so any "low volatility" claim understates the true risk.

**Scenarios.** This is credit, so the upside is capped at the coupon. The swing is all on the downside. The three swing assumptions:

1. **Default rate in the concentrated sector.** Defaults in one sector move together, so a downturn there hits ~60% of the book at once.
2. **Recovery rate.** `01` gives ~60–80% historically for senior secured, "with wide dispersion by vintage and credit quality."
3. **Cost and continuity of the fund's leverage facility.** Facility cost, covenants, and margin or borrowing-base triggers are all undisclosed.

| Case | Assumption | Effect on LP |
|---|---|---|
| **Bull** | Benign credit, facility stays cheap | ≈12% (the quote). Debt has no equity-style upside, so the bull case is "the quote holds" |
| **Base** | Quote as presented | 12% net 🟢 *if* it is net of all fees and carry, which is not confirmed (§4) |
| **Mild bear** (illustrative 🔴) | 5% of the concentrated sector defaults, 70% recovery | Loan-book loss ≈ 0.60 × 5% × 30% = **0.9%**. At ~3.5x assets/equity (if 2.5x is debt-to-equity), that is **≈3.2 pts off LP equity**. If 2.5x is assets-to-equity, it is ≈2.3 pts |
| **Bear** (illustrative 🔴) | 15% of the concentrated sector defaults, 60% recovery (low end of the `01` band) | Loan-book loss ≈ 0.60 × 15% × 40% = **3.6%**. On equity that is **≈12.6 pts** at 3.5x, or ≈9 pts at 2.5x: **roughly a full year's quoted return, or more.** A facility covenant breach could also force asset sales at the bottom |

The default and recovery inputs above are illustrative assumptions, not facts about this fund. The mechanism is the finding: **every point of loan-book loss costs the LP about 2.5–3.5 points of equity** 🟡, depending on how "2.5x" is measured. The fund has disclosed no downside case at all (`GEN-13`), and no default or recovery history (`HML-03`, `HML-04`) that would calibrate one.

## 3. Where LP Returns Come From

A credit fund's return has three sources: contractual loan income (coupon plus fees/OID), the leverage spread (loan yield minus facility cost, times leverage), and credit losses as the drag. There is no exit-cap or terminal-value component, so `GEN-08` does not apply.

- **Leverage share.** Equity yield ≈ loan yield + 2.5 × (loan yield − facility cost) − fees, if 2.5x is debt-to-equity. **Each 1 pt of spread between loan yield and facility cost adds ~2.5 pts to the LP's yield** 🟡. Neither the loan yield nor the facility cost is disclosed, so the levered/unlevered split can't be computed. Given 2.5x against `02`'s >1.5x aggressive threshold, a large share of the 12% plausibly comes from leverage 🟡. This is the debt-fund form of the **financing story** (`CREDIT-01`, which per `03` connects to `GEN-07`). Leverage works in reverse on losses (§2).
- **"Senior secured" is a loan-level label, not the LP's position.** The fund's leverage provider sits **ahead of LP equity**. If the facility has mark-to-market, borrowing-base, or concentration covenants, a downturn in the 60% sector could trigger a paydown or forced sales. Loan-level seniority then does not protect the LP in the way the label suggests 🟡.
- **The flag can't be confirmed or cleared yet.** It is not confirmed on numbers because the split is unstated. Routed to `Q-DS-02` and `Q-RISK-06`.

## 4. Fee Stack Summary

| Fee | Disclosed? | `02` norm (private credit) | Read |
|---|---|---|---|
| Management fee | **2%** 🟢 | 1–2% of committed capital during the investment period. 1–1.5% of invested capital after | At the top of the range. Aggressive if there is no step-down (`02`: "Absence is a flag"). Step-down not disclosed |
| Management-fee **basis** | Not stated | Committed or invested capital | **If charged on gross assets (BDC-style), 2% on ~3.5x assets ≈ 7% of LP equity per year** 🔴. That would be a different fund entirely. Must confirm |
| Carry / performance fee | Not stated | 10–20% above a 5–7% hurdle. High-water mark usual | Unknown. With leverage, a 5–7% hurdle is easy to clear on borrowed money |
| Hurdle structure / catch-up | Not stated | Hard hurdle is LP-favorable. Soft with 100% catch-up is aggressive | Unknown |
| Servicing fee | Not stated | 0.25–0.5% of loan balance | Unknown |
| Fund-level leverage costs | Not stated | *Variable*. Fund leverage >1.5x means compounded credit risk | Leverage is 2.5x 🟢, cost undisclosed |
| Admin / IR | Not stated | $1–3k/LP or 0.1–0.3% | Unknown |

**Gross-to-net drag (via `scripts/fee_drag_calculator.py`): ≥200 bps/yr on disclosed fees alone.** Inputs: 2% fund management fee. Carry and every other fee were passed as 0 because they are undisclosed. Gross of 14% and hold of 5 yrs are assumed 🔴. On that basis a 12% net needs **at least ~14% gross at the fund-equity level**.

- **Illustrative full stack** (assumed 🔴): 15% carry over a 6% hurdle with 100% catch-up, the midpoint of the `02` range. Drag rises to **≈379 bps/yr** (200 recurring + 179 promote), so 15% gross nets ≈11.2%. A real carry would push the gross needed for a 12% net to roughly 16%. On a senior-secured book, that gross mostly has to come from leverage.
- **The finding.** Total drag is **not computable from this disclosure**, and it is unclear whether "12% net" is after carry, leverage costs, and servicing (`GEN-16`). Each assumed input above is a §6 gap.

## 5. Red Flags

**RED**

- **`CREDIT-01` (RED): Fund-level leverage stacked on the loan book.** 🟢 ~2.5x, against `02`'s >1.5x threshold. It amplifies losses ~2.5–3.5x (§2), and the 12% may be a levered figure presented as if unlevered. Debt-fund form of the financing story (`GEN-07`, not confirmable on numbers yet; see §3). → `Q-RISK-06`, `Q-DS-02`
- **Cluster: `CREDIT-01` + `CREDIT-02` (treat as RED).** 🟢 Leverage on a correlated book: a downturn in one sector hits ~60% of assets at once, and the leverage multiplies that hit into LP equity. It can also trip facility covenants exactly when loan marks are falling. This is the specific way the fund fails: one sector cracks, the borrowing base shrinks, and the fund sells loans or halts distributions to pay down its lender ahead of LPs 🟡.

**YELLOW–RED**

- **`HML-03` (YELLOW–RED): Default rate not disclosed** (debt-fund flag; Q-RISK-05 applies to credit funds). 🟢 The fund's credit performance through 2020 and 2022–23 is unknown. → `Q-RISK-05`
- **`HML-04` (YELLOW–RED): Recovery rate not disclosed.** 🟢 Workout competence decides realized loss. "Senior secured" without recovery history is a label, not evidence. → `Q-RISK-05`
- **`GEN-16` (YELLOW–RED): Incomplete fee and waterfall disclosure.** 🟢 Only the management fee is given. Carry, hurdle, catch-up, servicing, leverage costs, and the fee basis are missing, so drag can't be computed (§4). → `Q-FEE-01`

**YELLOW**

- **`CREDIT-02` (YELLOW, escalated by the cluster above): Sector concentration.** 🟢 ~60% in one unnamed sector, so defaults are correlated. → `03` response (no `04` entry): "What is the sector breakdown of the portfolio, and your single-largest-sector exposure?"
- **`GEN-11` (YELLOW): Distribution timing not disclosed.** 🟢 An IRR with no distribution schedule. Is income paid currently, or reinvested and back-loaded? → `Q-DIST-01`
- **`GEN-13` (YELLOW): No sensitivity or downside case.** 🟢 A single-point 12%. → `Q-DS-03`
- **`GEN-17` (YELLOW): Essential category disclosures absent** (per `01`): loan count and average size, named sector mix, default/recovery, borrower type. → §6, `Q-RISK-05`
- **`HML-05` (YELLOW, pending): Management-fee step-down not disclosed.** 🟢 The fee is at the 2% ceiling, and `02` treats an absent step-down as a flag. → `03` response: "Does the management fee step down after the investment period?"

**Not fired. No disclosure, routed to questions rather than scored on assumption:**

- `GEN-14` / `GEN-05`: no track record given at all. It is unverified, not unrealized (§7, `Q-GP-02`).
- `GEN-01`: co-invest unknown (`Q-GP-01`).
- `GEN-02`: regulatory history unknown (`Q-GP-03`).
- `GEN-06`: affiliate servicing unknown (`Q-FEE-02`).
- `GEN-09`: maturity of the fund's leverage facility relative to fund life is unknown (`Q-RISK-01`).
- `GEN-08`, `EQUITY-*`, and `HML-01` do not apply. This is a debt fund with no exit-cap or ARV basis.

## 6. Missing Disclosures

Against the `01` private-credit essential disclosures and the `02` fee inventory:

- **Loan count and average loan size** (`01` essential). The other half of concentration risk.
- **Full sector mix, and what the 60% sector is** (`01` essential). Only the single-sector share is given.
- **Basis of "2.5x":** debt-to-equity or assets-to-equity. Also facility type, cost, maturity, mark-to-market and covenant terms, and recourse (`01`, `02`).
- **Whether the 12% is levered or unlevered, and net of what** (`02`).
- **Historical default rate and recovery rate, through-cycle** (`01` essential).
- **Borrower and collateral type:** corporate or real-estate lending, first-lien or unitranche, floating or fixed.
- **Fee basis and step-down, carry, hurdle (hard or soft), catch-up, high-water mark, servicing, admin** (`02`).
- **Fund life, investment period, distribution policy, capital-call schedule.**
- **Sponsor identity, AUM, realized net-to-LP track record, GP co-invest.**
- **Liquidity terms:** redemption gates or secondary options.
- **Minimum, raise size, and geography.**

Assumed inputs used in this screen 🔴: hold 5 yrs (7 yrs also shown), gross 14%, the illustrative carry and hurdle in §4, and the illustrative default and recovery figures in §2.

## 7. GP Alignment

- **Co-invest:** Not stated. Unverified (`GEN-01` probe, `Q-GP-01`).
- **Track record:** None provided. The 12% is a quote, not a realized result. No realized net-to-LP history means **no validated track record** (`GEN-14`, `GEN-05` probe, `Q-GP-02`).
- **Waterfall alignment:** Unknown. Leverage weakens a hurdle-based carry. A 5–7% hurdle (`02` norm) is easy to clear when the fund borrows at a spread, so the GP can earn carry on a return produced by leverage rather than credit selection 🟡. A **hard** hurdle and a high-water mark would partly offset this.
- **Fee basis:** A 2% fee on gross (levered) assets would pay the GP more for adding leverage, which aligns the GP against the LP on the single biggest risk in this fund 🔴, unconfirmed (§4).
- **Affiliate fees:** Unknown. Servicing is a common affiliate line in credit funds (`GEN-06` probe, `Q-FEE-02`).

## 8. Questions for the GP

**Must-ask**

| ID | Question | Bad-answer signal (the specific dodge) | Fires on |
|---|---|---|---|
| `Q-RISK-06` | "What is the fund's leverage ratio, and is the quoted LP IRR levered or unlevered?" Ask also: is 2.5x debt-to-equity or assets-to-equity? | Won't disclose. Presents a levered IRR as if unlevered. "Leverage is conservative" with no number | `CREDIT-01` |
| `Q-DS-02` | "Strip out leverage — what is the unlevered, in-place return?" (the loan-book yield before fund leverage) | Treats the levered IRR as the only relevant figure. No unlevered view exists. "Leverage is just how the deal works" | `GEN-07` via `CREDIT-01` |
| `CREDIT-02` response (no `04` entry) | "What is the sector breakdown of the portfolio, and your single-largest-sector exposure?" Ask also: which sector is the 60%, and why? | Names the sector but no borrower count. "It's a defensive sector" in place of a stress case. Won't produce the loan tape | `CREDIT-02` |
| `Q-RISK-05` | "What is your historical default rate and realized recovery rate, including through 2020 and 2022–23?" | Default rate without recovery, or the reverse. "We've never had a loss." Silence on 2022–23 | `HML-03`, `HML-04` |
| `Q-RISK-01` (escalated: fund leverage is the debt here) | "When does the debt mature relative to the projected hold, and what's the refinance or extension plan?" Ask also about the facility's mark-to-market and covenant triggers | Facility matures inside the fund life. "We'll roll it" with no terms. No plan if the lender pulls back | `GEN-09` probe |
| `Q-FEE-01` | "Can you provide the complete fee schedule and the full distribution waterfall?" Ask also: is the 2% on committed, invested, or gross assets? | "Standard market fees." "The PPM has it" without producing it. Fee basis dodged | `GEN-16` |
| `Q-DS-03` | "What is the return under a bear case?" (for credit: a default spike in the concentrated sector, low recovery, facility repricing) | Single-point pro forma. "We underwrite conservatively" with nothing to show. The bear case is still a gain | `GEN-13` |
| `Q-DIST-01` | "What is the projected distribution schedule, and at what milestones does LP capital start returning?" | "We'll distribute when the fund supports it." An IRR with no distribution timing | `GEN-11` |
| `Q-GP-02` | "Can you restate your track record as net-to-LP IRR on fully-realized, exited deals only?" | Only marks or project-level IRR. "Most loans are still performing." Can't separate realized from unrealized | `GEN-14`, `GEN-05` |
| `Q-GP-01` | "How much of your own capital is in this fund, on the same terms as LPs?" | "Our sweat equity is our investment." Co-invest is a fee waiver. Token amount on better terms | `GEN-01` |
| `Q-GP-03` | "Have you or your principals faced any regulatory action, enforcement, or investor litigation?" | "Nothing material." Blames the regulator. A search surfaces something undisclosed | `GEN-02` |
| `Q-FEE-02` | "Which service providers are GP-affiliated (servicing especially), what do they charge, and are rates benchmarked?" | "All arm's-length" without naming providers. Affiliate fees undisclosed | `GEN-06` |
| `HML-05` response (no `04` entry) | "Does the management fee step down after the investment period?" | No step-down. Fee stays on committed capital as the book winds down | `HML-05` |
| `Q-LIQ-01` | "What are my options if I need to exit before the fund ends?" | "A secondary market may develop." Vague redemption promises. Gates not disclosed | — |

**Nice-to-ask**

| ID | Question | Bad-answer signal |
|---|---|---|
| `Q-FEE-04` | "What hurdle do LPs receive before the GP earns carry: hard or soft, and is there a catch-up?" | Hurdle below 5% (`02` aggressive threshold). Soft hurdle with 100% catch-up |
| `Q-GP-04` | "How have headcount and loan-monitoring capacity grown alongside AUM?" | AUM multiplied while the team stayed flat. No named credit or workout team |
| `Q-DIST-02` | "When are capital calls expected, and what's the consequence of a missed call?" | "Calls as needed." Punitive dilution buried in the docs |
| `Q-LIQ-02` | "When are K-1s delivered, and have they historically arrived before the deadline?" | "As soon as we can." A history of extensions |

## 9. Diligence Checklist

- **PPM / LPA review:** fee basis, step-down, carry, hurdle, high-water mark, distribution policy, redemption gates, key-person clause.
- **Credit facility agreement:** lender, cost, maturity, advance rates, mark-to-market and borrowing-base triggers, concentration covenants, recourse to the fund.
- **Loan tape:** borrower count, sizes, sector, lien position, coupon type, current non-accruals and amendments or PIK conversions.
- **Valuation policy:** who marks the loans, how often, and whether there is third-party valuation (smoothed marks, `05`).
- **Audited financials** of prior funds, plus an independent fund administrator.
- **Background and regulatory check:** SEC Form ADV (fee schedule, disciplinary history), FINRA BrokerCheck, litigation search on the principals.
- **References:** LPs from a prior fund that went through 2020 and 2022–23.
- **Tax / structure:** UBTI exposure from fund leverage if investing through an IRA or tax-exempt vehicle. Confirm with your tax advisor.

## 10. Verdict

**Pass as presented — insufficient disclosure**

*Screening output only, not investment advice.*

**Reasoning.** The headline clears its comparator comfortably: 12% net is ≈717 bps over HYG and ≈713 bps over the 2yr Treasury. That clear is bought with the two risks HYG diversifies away. On stated facts 🟢, the fund is levered ~2.5x (`CREDIT-01`, RED) on a book that is ~60% in one sector (`CREDIT-02`), and together they form a RED cluster. Of the five essential disclosures `01` lists for private credit, only leverage and seniority are given, and sector mix is partial. Loan count, default and recovery history, carry and hurdle, fee basis, hold, distribution schedule, sponsor, and track record are all absent. That leaves too little to underwrite the core question: is 12% a credit return or a leverage return?

**Biggest swing factor:** the levered-vs-unlevered split, together with the concentrated sector's default and recovery behavior. Every point of loan-book loss costs LP equity about 2.5–3.5 points.

**Re-screen list (what would have to be true):**

1. The unlevered loan-book yield is disclosed, and stands as a credible credit return on its own (`Q-DS-02`, `Q-RISK-06`).
2. The facility terms show no mark-to-market or borrowing-base trigger that would force sales in a sector downturn, and its maturity covers the fund life (`Q-RISK-01`).
3. The 60% sector is named, with a loan count and a stress case showing LP capital survives a sector default spike at the low end of recovery (`CREDIT-02`, `Q-DS-03`).
4. Through-cycle default **and** recovery history is provided (`Q-RISK-05`).
5. The fee is on committed or invested capital and not gross assets, steps down after the investment period, and carry sits behind a hard hurdle with a high-water mark (`Q-FEE-01`, `HML-05`).
6. There is a realized net-to-LP track record and meaningful GP co-invest (`Q-GP-02`, `Q-GP-01`).

**Who it could suit, if it re-screens well:** an LP who can hold through the full fund life with no liquidity need, and who wants levered credit income as a deliberate, sized bet. It should not replace "senior secured" fixed income. With leverage and concentration this high, the risk is closer to a levered sector bet than to a diversified loan portfolio.
