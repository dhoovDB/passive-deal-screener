# Eval fixture 05 — Private credit fund, 2.5x levered, sector-concentrated
*Iteration-5 run, 2026-09-27, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 7712624.*

**Verdict: Pass as presented — insufficient disclosure.** The two facts you were given are both warnings: fund leverage of ~2.5x (RED, `CREDIT-01`) and 60% of the book in one sector (YELLOW, `CREDIT-02`). Together they mean a single sector's defaults get multiplied by the leverage and land on LP equity. The only things that could clear those flags are what's missing: the default and recovery history, the leverage definition and facility terms, which sector it is, and the carry and waterfall. Re-screen when you have them (list in §10). The 12% net is at the top of the private-credit range, and the most likely reason is leverage, not better lending.

---

## 1. Deal Snapshot

| Field | Value | Tag |
|---|---|---|
| Asset class | Private credit (fund) | 🟢 stated |
| Deal type | Private credit fund, senior secured | 🟢 stated |
| Sponsor / GP | Not stated | — |
| Geography | Not stated | — |
| Minimum investment | Not stated | — |
| Hold / fund term | Not stated (category norm 3–7 yrs, `01`) | — |
| Raise / fund size | Not stated | — |
| Claimed return | 12% **net** IRR to investors | 🟢 stated |
| Fund-level leverage | ~2.5x (debt/equity or assets/equity not specified) | 🟢 stated / basis 🔴 |
| Sector concentration | ~60% of loan book in one sector (sector not named) | 🟢 stated |
| Management fee | 2% (fee base not stated: committed, invested, or gross assets) | 🟢 stated / base 🔴 |
| Carry / hurdle | Not stated | — |
| Seniority | Senior secured | 🟢 stated |
| Loan count / avg size | Not stated | — |
| Default / recovery history | Not stated | — |
| Distribution schedule | Not stated | — |

## 2. Return Stress-Test

**Benchmark (`scripts/benchmark_comparator.py`, private-credit → HYG):**
- The 12% net IRR is **≈717bps over HYG** (4.83% 10yr) and **≈713bps over the 2yr Treasury** (4.87%). 🟢
- The hold isn't stated, so the lock-up was run at 5 yrs (hurdle ~300–400bps) and 7 yrs (hurdle ~400–600bps). Both **clear comfortably**. 🔴 hold assumed. That result holds across the whole 3–7 yr category range.
- The 12% sits at the **top** of `01`'s 8–12% net range for private credit. 🟢

**The headline clears the hurdle only if it's real.** `05` says so directly for this row: "check fund leverage isn't manufacturing the spread (`CREDIT-01`)." At 2.5x, it probably is.

**Where the leverage takes you (illustrative, 🔴 assumptions labeled):**
- Assume 2.5x means debt/equity, so assets are 3.5x equity. Assume the fund borrows at the 2yr Treasury + 200bps (≈6.87%). Under those assumptions the loan book only needs to yield **≈8.9%** to produce a 14% gross equity return. That is 12% net after a 2% fee on equity. 🔴
- The same multiplier works on losses: **every 1pt of credit loss on assets costs ≈3.5pts of LP equity.** 🟡 (follows from any 2.5x debt/equity reading)

| Scenario | Swing assumptions | LP outcome (illustrative) |
|---|---|---|
| **Bull** | Concentrated sector stays healthy; facility spread stays put; fee is on equity or invested capital | ~12% net as quoted |
| **Base** | Normal defaults in the concentrated sector, e.g. 10% of that sector's loans default at a 70% recovery (midpoint of `01`'s 60–80%) | Asset loss ≈ 0.6 × 10% × 30% = 1.8% → **≈6.3pts of LP equity**. That's about half a year's return. |
| **Bear** | Sector downturn, 20% of the sector defaults at 60% recovery; lender tightens the borrowing base | Asset loss ≈ 0.6 × 20% × 40% = 4.8% → **≈17pts of LP equity**, more than a full year's net return. Forced deleveraging could follow. |

The scenario inputs are 🔴 illustrations, not forecasts. The **mechanism** is 🟡: leverage turns concentrated sector losses into much larger equity losses. The three swing factors are (1) the concentrated sector's default and recovery rates, (2) the fund's cost and terms on its borrowing, and (3) what the 2% fee is charged on.

Also, private-credit marks are **smoothed** (`05`, PRIV note), so reported NAV volatility will understate this risk.

## 3. Where LP Returns Come From

- **Cash flow vs exit:** credit returns are interest income, not exit value, so exit dependence (`GEN-08`) doesn't apply. 🟢
- **Leverage:** under the §2 illustration, the unlevered loan-book yield (≈8.9%, 🔴) is below the 12% headline. **Roughly 3+ points of the net return come from fund-level borrowing, not lending.** 🟡
- This is the credit version of a **financing story** (`GEN-07`, via `CREDIT-01`; `03` notes "fund-level leverage is how a modest loan-book yield is levered into a marketable LP IRR, and it unwinds the same way"). It holds until the GP shows the unlevered return (`Q-RISK-06`, `Q-DS-02`).

## 4. Fee Stack Summary

| Fee | Disclosed | `02` norm | Read |
|---|---|---|---|
| Management fee | 2%, base unstated | 1–2% of committed during the investment period; 1–1.5% of invested after | Top of range. Step-down not disclosed (`HML-05`). |
| Performance fee / carry | Not stated | 10–20% over a 5–7% hurdle | Unknown (`GEN-16`) |
| Hurdle type (soft/hard, catch-up) | Not stated | Hard hurdle is LP-favorable; soft with 100% catch-up is aggressive | Unknown |
| Servicing fee | Not stated | 0.25–0.5% of loan balance | Unknown |
| Fund-level leverage costs | Not stated | *Variable*; >1.5× equity = compounded credit risk | Unknown, and a material cost at 2.5x |
| Admin / IR | Not stated | $1–3k/LP or 0.1–0.3% | Unknown |

**Gross-to-net drag (`scripts/fee_drag_calculator.py`, undisclosed fees = 0):**
- **If the 2% is on LP equity:** **200bps/yr** of disclosed drag, so ≈14% gross to 12% net. 🟢 fee / 🔴 5-yr hold
- **If the 2% is on gross assets at 3.5x equity:** **700bps/yr** on LP equity, so ≈19% gross needed for 12% net. 🔴 base assumed

**The finding:** the full drag can't be computed from what was disclosed. Carry, hurdle, servicing, and the fund's borrowing costs are all missing, and the fee base alone moves the drag by **500bps/yr**. Since the quote is already net, missing carry doesn't lower the 12%. It means you don't know what gross performance the 12% requires, or how much of the upside goes to the GP.

## 5. Red Flags

**RED**
- **`CREDIT-01` — Fund-level leverage stacked on loan leverage (~2.5x).** 🟢 This exceeds `02`'s 1.5× threshold. Even the most generous reading (2.5x assets/equity, i.e. 1.5x debt/equity) lands exactly on it. LP exposure: correlated losses are multiplied roughly 3.5x into LP equity. The fund's lender is senior to you and may force deleveraging when you can least afford it. The quoted 12% may also be a levered figure presented as if it weren't. Includes the financing-story read (`GEN-07`, 🟡). → `Q-RISK-06`, `Q-DS-02`

**YELLOW–RED** (treat as RED until answered)
- **`GEN-16` — No carry, hurdle, or waterfall disclosure.** 🟢 absent. Drag and GP upside share are unknown. The fee base (committed / invested / assets) is undisclosed too, and that alone is a 500bps/yr swing. → `Q-FEE-01`
- **`HML-03` / `HML-04` — Default and recovery history not disclosed.** 🟢 absent. These are essential private-credit disclosures (`01`), probed by the credit-fund-conditional `Q-RISK-05`. At 3.5x equity exposure, recovery rate matters most: `03` notes that a 2% default rate at 40% recovery is worse than 5% at 90%. → `Q-RISK-05`

**YELLOW**
- **`CREDIT-02` — Sector concentration (~60% in one sector).** 🟢 Defaults in that sector are correlated, and leverage magnifies them (`CREDIT-01`). Together they are a **cluster → treat as RED** (`03`: "a cluster of YELLOWs is a RED"). The sector itself isn't named, so cyclicality can't be judged. → `03` response: "What is the sector breakdown of the portfolio, and your single-largest-sector exposure?" (no `04` question maps to `CREDIT-02`; asked directly)
- **`GEN-11` — IRR with no distribution schedule.** 🟢 absent. You can't see whether income is paid out or reinvested, or when capital comes back. → `Q-DIST-01`
- **`HML-05` — Management-fee step-down not disclosed.** 🟢 absent. A flat 2% after the investment period drags on net as the book winds down. → `Q-FEE-01`
- **`GEN-17` — Essential category disclosures absent.** 🟢 Loan count, average loan size, sector identity, and through-cycle loss history are missing (per `01`). → `Q-RISK-05`, `CREDIT-02` question

**Probed, not fired** (would need a 🔴 assumption to fire): `GEN-09` (fund credit-facility maturity or borrowing-base terms inside the fund life → `Q-RISK-01`); `GEN-01` (co-invest unknown → `Q-GP-01`); `GEN-05` / `GEN-14` (track record not presented → `Q-GP-02`); `GEN-06` (affiliate servicing → `Q-FEE-02`); `GEN-13` (no downside case shown → `Q-DS-03`).

**Cluster:** `CREDIT-01` + `CREDIT-02` (+ `GEN-07`) = a **levered, concentrated credit bet**. The headline is marketable because of the leverage, and it breaks in a sector downturn for the same reason.

## 6. Missing Disclosures

Checked against `01`'s private-credit essentials and `02`'s private-credit fee inventory:
1. **Historical default and recovery rates, through-cycle** (2020, 2022–23)
2. **Loan count and average loan size**
3. **Which sector** holds the 60%, and the rest of the sector mix
4. **Leverage definition** (debt/equity or assets/equity), facility lender, cost, maturity, recourse, and borrowing-base / mark-to-market covenants
5. **Whether the 12% net IRR is levered or unlevered, realized or target**
6. **Fee base** for the 2% management fee, plus any step-down
7. **Carry, hurdle rate, and hurdle type** (soft/hard, catch-up), and high-water mark
8. Servicing fee, admin/IR fee, and who pays the leverage costs
9. **Fund term / hold** and distribution schedule (income paid or reinvested)
10. **Sponsor identity**, track record, co-invest
11. Minimum, fund size, geography, liquidity or redemption terms
12. Seniority detail beyond "senior secured": first-lien vs unitranche, covenant package

Items 1, 4, and 7 are ASSUMED or zero inputs in §§2 and 4, so they're the gaps that most limit this screen.

## 7. GP Alignment

- **Co-invest:** not stated, so alignment is unverified. 🔴
- **Track record:** none presented. There's no realized net-to-LP history, so from this screen it counts as **no track record** (skepticism rule 5). 🔴
- **Waterfall alignment:** unknown. A 2% fee charged on gross assets would reward the GP for adding leverage whether or not it helps LP returns. That's a structural misalignment to rule out. 🟡
- **Affiliate fees:** unknown. Servicing is often done by an affiliate. 🔴

## 8. Questions for the GP

**Must-ask**

| # | Question | Bad-answer signal | Flag |
|---|---|---|---|
| `Q-RISK-06` | "What is the fund's leverage ratio, and is the quoted LP IRR levered or unlevered?" | Won't disclose leverage; presents a levered IRR as if unlevered; "leverage is conservative" with no number. | `CREDIT-01` |
| `Q-RISK-05` | "What is your historical default rate and realized recovery rate, including through 2020 and 2022–23?" | Default rate without recovery (or vice versa); "we've never had a loss"; silence on 2022–23. | `HML-03`, `HML-04` |
| *(from `03`)* | "What is the sector breakdown of the portfolio, and your single-largest-sector exposure?" Also: which sector, and why concentrate? | Won't name the sector; "diversified within the sector"; no concentration limit in the documents. | `CREDIT-02` |
| `Q-FEE-01` | "Can you provide the complete fee schedule and the full distribution waterfall?" Include the management-fee base and step-down. | "Standard market fees"; partial list; "the PPM has it" without producing it. | `GEN-16`, `HML-05` |
| `Q-DS-02` | "Strip out leverage — what is the unlevered return?" | Treats the levered IRR as the only relevant figure; "leverage is just how the deal works." | `GEN-07` |
| `Q-RISK-01` | "When does the fund's credit facility mature relative to fund term, and what's the refinance or extension plan?" Also: what are the borrowing-base and margin-call terms? | Facility matures inside the fund term; "we'll refinance" with no terms; can't describe covenants. | `GEN-09` |
| `Q-DS-03` | "What is the return under a bear case?" Here: a default spike in the concentrated sector plus a facility spread widening. | A single-point projection; "we underwrite conservatively" with nothing to show. | `GEN-13` |
| `Q-DIST-01` | "What is the projected distribution schedule, and at what milestones does LP capital start returning?" | "We'll distribute when the fund supports it"; an IRR with no distribution timing. | `GEN-11` |
| `Q-GP-02` | "Can you restate your track record as net-to-LP IRR on fully-realized funds only?" | Only gross or unrealized marks; can't separate realized from unrealized. | `GEN-05`, `GEN-14` |
| `Q-GP-01` | "How much of your own capital is in this fund, on the same terms as LPs?" | "Our sweat equity is our investment"; co-invest is a fee waiver. | `GEN-01` |
| `Q-FEE-02` | "Which service providers (servicing, admin) are GP-affiliated, what do they charge, and are those rates benchmarked?" | "All arm's-length" without naming providers. | `GEN-06` |
| `Q-LIQ-01` | "What are my options if I need to exit before the fund term ends?" | "A secondary market may develop"; vague promises of liquidity. | — |

**Nice-to-ask**
- `Q-GP-03`: regulatory or litigation history. Bad answer: "nothing material" with no detail. (`GEN-02`)
- `Q-DIST-02`: capital-call schedule and missed-call consequences. Bad answer: "calls as needed," with punitive dilution buried in the documents.
- `Q-LIQ-02`: K-1 delivery timing. Bad answer: a history of extensions.

## 9. Diligence Checklist

- [ ] PPM / LPA: fee base, carry, hurdle type, step-down, leverage limits, concentration limits
- [ ] Credit facility agreement: lender, cost, maturity, recourse, borrowing-base and mark-to-market triggers
- [ ] Loan tape: count, sizes, sector, lien position, covenants, marks
- [ ] Audited financials and valuation policy: who marks the loans, and how often
- [ ] Realized fund-level track record, net to LP, from the GP's prior funds, verified by an administrator or auditor
- [ ] Background and regulatory check on the GP and principals (SEC Form ADV / IAPD, FINRA BrokerCheck, litigation search)
- [ ] Independent read on the concentrated sector's credit cycle position

## 10. Verdict

**Pass as presented — insufficient disclosure.**

- **Reasoning:** The core return story here is loan yield, minus losses, magnified by leverage. You were given the leverage and the concentration but not the losses, the cost of leverage, or the carry. A 12% net quote that clears HYG by ~717bps (🟢) clears the hurdle on paper. But `05` warns that fund leverage can be what's manufacturing the spread, and the stated facts point that way (🟡).
- **Biggest swing factor:** default and recovery rates in the concentrated sector, multiplied by ~3.5x equity exposure. A 1.8% asset loss erases about half a year's return (§2, 🔴 illustration).
- **Who it could suit:** an LP who already holds diversified credit, wants to add levered income, and can live with correlated sector drawdowns. Only if the re-screen items check out.
- **What would have to be true to move to Pursue with conditions:** (1) a through-cycle recovery rate at or above `01`'s 60–80% band, with low defaults in 2020 and 2022–23; (2) 2.5x is defined, and the credit facility is term-matched with no hair-trigger mark-to-market margin calls; (3) the 60% sector is non-cyclical or a documented area of GP expertise, with a concentration cap in the LPA; (4) the 2% fee is on equity or invested capital, not gross assets, and steps down; (5) carry is ≤20% over a hard hurdle ≥5–7%; (6) a realized net-to-LP track record.

**Re-screen list:** default and recovery history · leverage definition and facility terms · sector identity and full mix · fee base, carry, and hurdle · fund term and distribution schedule · levered-vs-unlevered basis of the 12% · sponsor and realized track record.
