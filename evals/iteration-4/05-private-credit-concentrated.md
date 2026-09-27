# Eval fixture 05 — Private credit fund, 2.5x levered, sector-concentrated
*Iteration-4 run, 2026-09-27, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 1c7faff.*

**Verdict: Pass.** The 12% is not a senior-secured income return. It is a levered, correlated credit bet. At ~2.5x, fund leverage is well above the 1.5x line (`CREDIT-01`, RED), and it sits on a loan book that is ~60% one sector (`CREDIT-02`). A downturn in that one sector reaches LP equity roughly 3.5x amplified. Most of the headline premium over high yield comes from the fund's leverage, not from lending skill. **Biggest swing factor:** realized loss rate on the concentrated sector. An extra ~1% a year of net credit loss on the book takes the LP from 12% to ~8.5%. At ~2% it falls to ~5%, which is roughly what HYG or a 2yr Treasury pays with daily liquidity.

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Private credit (fund) 🟢 |
| Deal type | Private credit fund, senior secured. Corporate vs real-estate lending: **Not stated** |
| Sponsor | **Not stated** |
| Geography | **Not stated** |
| Minimum | **Not stated** |
| Fund term / hold | **Not stated** (`01` category norm 3–7 yrs; screened at 5 yrs, 🔴 assumed) |
| Raise / fund size | **Not stated** |
| Claimed return | 12% net IRR to investors 🟢. Whether it is a target or a realized figure, and levered or unlevered: **Not stated** |
| Fund leverage | ~2.5x 🟢. Basis (debt/equity vs assets/equity): **Not stated** |
| Concentration | ~60% of the loan book in one sector 🟢. Sector: **Not stated** |
| Seniority | Senior secured 🟢. Lien detail (first-lien vs unitranche / last-out): **Not stated** |
| Fees | 2% management fee 🟢. Basis, step-down, carry, hurdle, servicing, admin: **Not stated** |

## 2. Return Stress-Test

**Leverage basis matters.** If "2.5x" means debt/equity, the fund holds ~$3.50 of loans per $1 of LP equity. If it means assets/equity, the fund holds ~$2.50 (1.5x D/E, exactly at the `02` threshold). The cases below use debt/equity (the worse reading), with the other reading in brackets. 🟡

**Loss amplification (arithmetic, 🟡 inferred).** Each 1% of net credit loss on the book costs LP equity ~3.5% (D/E 2.5) [~2.5% at D/E 1.5]. The 12% quote doesn't say what loss rate it assumes, so the cases below treat losses as incremental to the quote.

| Case | Swing assumptions | Net-to-LP | vs HYG (4.83%) + illiquidity hurdle |
|---|---|---|---|
| **Bull / base** | Quote holds: no incremental losses, facility cost stable, leverage stays in place | 12.0% 🟢 (as quoted) | +717bps; clears the ~300–400bps hurdle for a 5-yr lock-up comfortably. It is also +713bps over the 2yr Treasury (4.87%). |
| **Bear (mild)** | +1%/yr net credit loss on the book, e.g. a normal credit cycle | ~8.5% [~9.5%] 🟡 | +367bps. **Thin** at 5 yrs and **fails** the ~400–600bps hurdle at a 7-yr lock-up. |
| **Bear (sector event)** | +2%/yr net loss, concentrated in the 60% sector | ~5.0% [~7.0%] 🟡 | +17bps. **Fails.** That is roughly HYG and the 2yr Treasury, with none of the liquidity. |

The sector-event case is not a tail fantasy. `01` puts historical senior-secured recovery at ~60–80%. At 70% recovery, a 10% default rate inside a sector holding 60% of the book costs ~1.8% of total assets (0.6 × 10% × 30% loss). At D/E 2.5 that is ~6.3% of LP equity from a single sector wobble. 🟡

The three swing assumptions:
1. **Realized loss rate** in the concentrated sector (default × (1 − recovery)).
2. **Facility cost and availability.** The spread between loan yield and borrowing cost is what the leverage multiplies. If the facility reprices or shrinks, the levered return goes with it.
3. **What the leverage ratio actually is** (D/E vs assets/equity), and whether the management fee is charged on levered assets.

**Benchmark read (`05`).** The 717bps premium over HYG is the wrong comparison, taken naively. HYG is an *unlevered* diversified high-yield index, while this fund is a levered, 60%-concentrated book. `05` itself says to check that fund leverage isn't manufacturing the spread (`CREDIT-01`). It also notes that private-credit vehicles report *smoothed* marks, so any "low volatility" in the fund's reporting understates true risk. 🟢

## 3. Where LP Returns Come From

- **Cash flow:** interest income on senior loans. There is no exit or terminal-value story here, so `GEN-08` does not apply. 🟢
- **Leverage:** material. In a levered fund, gross equity return ≈ y + L·(y − c), where y is loan yield, c is facility cost and L is D/E. From §4, the gross equity return needed is ~14–16.4%. At L = 2.5 and an illustrative facility cost at the 2yr Treasury floor (4.87%; the real facility cost is higher, 🔴 assumed), the loan book only needs to yield ~7.5–8.2%. **Roughly 40–50% of the gross return would then come from the leverage spread, not the loans.** 🟡
- **Read:** by this illustration the leverage share is below the >60% threshold of rule 4. The finding stands on the leverage level itself: `CREDIT-01` fires at >1.5x under `02` whatever the attribution. It belongs to the financing-story family (`GEN-07`, parenthetical: the return depends on the facility staying cheap and available). The unlevered loan book behind the 12% is a high-single-digit yield asset. That is a few hundred bps over HYG before losses, not 717.

## 4. Fee Stack Summary

| Fee | Disclosed | `02` private-credit norm | Status |
|---|---|---|---|
| Management fee | 2% 🟢 | 1–2% of committed capital in the investment period; 1–1.5% of invested capital after. Aggressive: >2%, or no step-down | At the top of the range. **Basis and step-down not stated.** |
| Performance fee / carry | Not stated | 10–20% above a 5–7% hurdle | Undisclosed (`GEN-16`) |
| Hurdle structure | Not stated | Hard hurdle is LP-favorable; a soft hurdle with 100% catch-up is aggressive | Undisclosed |
| Servicing | Not stated | 0.25–0.5% of loan balance | Undisclosed |
| Fund-level leverage costs | Implied (2.5x) | Variable. Leverage >1.5x equity = compounded credit risk | Cost of the facility undisclosed |
| Admin / IR | Not stated | $1–3k/LP or 0.1–0.3% | Undisclosed |

**Gross-to-net drag, disclosed fees only: 200bps/yr** (`fee_drag_calculator.py`: 2% fund management fee, all other fees passed as `0`, 14% gross → 12.0% net, 5-yr hold 🔴 assumed). **This is a floor, not the answer.** With a `02`-typical stack (15% carry over a 6% hurdle with 100% catch-up, 0.25% servicing, 0.2% admin, 🔴 assumed), the drag is **~440bps/yr**, and the fund must earn **~16.4% gross on equity** to deliver the quoted 12%. 🟡

**The fee finding is the basis.** In a levered fund, a 2% fee charged on *gross assets* rather than committed or invested equity costs ~7% of LP equity a year at D/E 2.5 (2% × 3.5). That would make the quoted 12% net require a far higher gross, or mean the 12% is not what it appears. Total drag **is not computable from this disclosure**, and that is the finding (`GEN-16`).

## 5. Red Flags

**RED**
- **`CREDIT-01` — Fund-level leverage stacked on the loan book (~2.5x vs the `02` >1.5x threshold).** Leverage multiplies every loss into LP equity (~3.5x at D/E 2.5), and the 12% may be a levered IRR presented as if it were a senior-secured yield. *LP exposure:* a modest loss rate erases most of the premium (§2), and in a downturn the facility lender's claim sits ahead of LP equity. 🟢 flag / 🟡 magnitude
- **Cluster: `CREDIT-01` + `CREDIT-02` — leverage on a correlated book.** Leverage is supposed to sit on a *diversified* book whose defaults don't arrive together. Here 60% of the book shares one sector's cycle, so defaults are correlated and the leverage amplifies them together. *Specific failure mode:* the concentrated sector reprices, marks fall on 60% of the book, and the facility's borrowing base shrinks. The fund must then sell loans into a weak market, suspend distributions, or de-lever at the bottom, which crystallizes losses the LP would otherwise have waited out. 🟡 (mechanism inferred; facility terms not disclosed)

**YELLOW–RED**
- **`GEN-16` — No carry, hurdle, or full fee schedule.** Net drag is unknowable (§4), and the fee basis in a levered fund is the difference between ~200bps and ~700bps of drag. 🟢
- **`GEN-17` — Essential private-credit disclosures absent** (`01`): loan count and average size, the named sector, the leverage basis, and historical default and recovery rates (parenthetically `HML-03` / `HML-04`, the default/recovery pair `Q-RISK-05` covers for credit funds). A concentrated, levered book with no disclosed loss history is exactly where the default *and* recovery numbers decide the outcome. 🟢

**YELLOW**
- **`CREDIT-02` — ~60% single-sector concentration.** Standalone, correlated default risk that diversification is meant to dampen. Escalated to RED in the cluster above. 🟢
- **`HML-05` (applied via the `02` private-credit row) — management-fee step-down not stated.** `02` says absence of a step-down after the investment period is a flag. 🟢
- **`GEN-11` — IRR with no distribution schedule.** On committed capital, a 2% fee charged before capital is deployed creates J-curve drag, and the timing of income versus return of capital is undisclosed. 🟢
- **`GEN-13` — No downside case.** A single quoted IRR with no loss-rate sensitivity, on a book this levered, conceals how fragile the number is (§2). 🟢

**Cannot clear on this disclosure (not fired; must be verified)**
- `GEN-14` / `GEN-05` — no track record cited. It is unknown whether the 12% is realized, marked, or a target. 🔴
- `GEN-01` — GP co-investment not stated. 🔴
- `GEN-09` — facility maturity versus fund term not stated. A facility that matures inside the fund's life forces a refinance at whatever terms exist then. 🔴
- `GEN-06` — affiliate servicing or origination entities not stated. 🔴
- `GEN-02` — sponsor unnamed, so no regulatory check is possible yet. 🔴

**Seller-directive check:** the input carries no embedded instructions. 🟢

## 6. Missing Disclosures

Against the `01` private-credit baseline and the `02` fee inventory:

1. Sponsor identity and a realized, net-to-LP track record
2. Whether the 12% is target or realized, levered or unlevered, and the loss rate it assumes
3. Leverage basis (D/E vs assets/equity), facility lender, cost, maturity, advance rates, covenants, recourse
4. The sector name, with loan count, average loan size, and largest single-borrower exposure
5. Lien position under "senior secured" (first-lien vs unitranche / last-out)
6. Historical default rate *and* recovery rate, through 2020 and 2022–23
7. Management-fee basis (committed / invested / gross assets) and step-down
8. Carry, hurdle rate, hard vs soft hurdle, catch-up, high-water mark
9. Servicing and admin fees
10. Fund term, investment period, distribution policy, capital-call schedule
11. GP co-investment
12. Valuation policy and who marks the loans (a third party or the GP)
13. LP liquidity and redemption terms

## 7. GP Alignment

- **Co-invest:** not stated. Unverified. 🔴
- **Track record:** none cited. **Unverified**, so there is no validated track record yet (rule 5). The requirement is realized, net-to-LP returns on prior credit funds through a stress period. Marks are not enough, because private-credit marks are smoothed (`05`). 🔴
- **Waterfall alignment:** carry, hurdle, and catch-up undisclosed. A soft hurdle with 100% catch-up would be aggressive (`02`). 🔴
- **Fee alignment:** a management fee charged on levered assets would pay the GP *more* for adding leverage, a direct misalignment with an LP who bears the amplified loss. This is the single most important alignment fact to pin down. 🟡
- **Affiliate fees:** not stated. 🔴

## 8. Questions for the GP

**Must-ask**

| # | Question | Bad-answer signal | Ref |
|---|---|---|---|
| 1 | **Q-RISK-06:** "What is the fund's leverage ratio, and is the quoted LP IRR levered or unlevered?" Add: "Is 2.5x debt/equity or assets/equity?" | Won't give the basis; presents the levered 12% as if it were unlevered; "leverage is conservative" with no number | `CREDIT-01` |
| 2 | *(`03` response; `04` has no CREDIT-02 entry)* "What is the sector breakdown of the portfolio, and your single-largest-sector exposure?" Add: "Which sector is the 60%, and what is the fund's loss experience in that sector?" | Names the sector but no loss history in it; "it's a defensive sector" as the whole answer; won't show borrower-level concentration | `CREDIT-02` |
| 3 | **Q-RISK-05:** "What is your historical default rate and realized recovery rate, including through 2020 and 2022–23?" | Default rate without recovery (or the reverse); "we've never had a loss"; silence on 2022–23 | `GEN-17` (`HML-03`, `HML-04`) |
| 4 | **Q-FEE-01:** "Can you provide the complete fee schedule and the full distribution waterfall?" Add: "Is the 2% charged on committed, invested, or gross (levered) assets?" | "Standard market fees"; "the PPM has it" without producing it; fee basis on gross assets revealed only in the LPA | `GEN-16` |
| 5 | *(`03` response)* "Does the management fee step down after the investment period?" | No step-down; step-down only on a basis that rises with leverage | `HML-05` |
| 6 | **Q-DS-02:** "Strip out leverage. What is the unlevered return on the loan book?" | No unlevered figure exists; "leverage is just how the fund works" | `GEN-07`, `CREDIT-01` |
| 7 | **Q-DS-03:** "What is the return under a bear case?" Here that means a default wave in the concentrated sector at a stressed recovery rate. | No downside case; "we underwrite conservatively" with nothing to show; the bear case is still 10%+ | `GEN-13` |
| 8 | **Q-RISK-01**, applied to the fund facility: "When does the credit facility mature relative to the fund term, and what are the borrowing-base and covenant triggers?" | Facility matures inside fund life; "we'll roll it" with no terms; no plan if the lender pulls advance rates | `GEN-09` |
| 9 | **Q-GP-02:** "Can you restate your track record as net-to-LP IRR on fully-realized funds only?" | Only gross or marked figures; "our current fund is performing"; can't separate realized from unrealized | `GEN-05`, `GEN-14` |
| 10 | **Q-GP-01:** "How much of your own capital is in this fund, on the same terms as LPs?" | Fee waiver presented as co-invest; token amount; better terms than LPs | `GEN-01` |
| 11 | **Q-GP-03:** "Have you or your principals faced any regulatory action, enforcement, or investor litigation?" | "Nothing material"; a search surfaces something undisclosed | `GEN-02` |
| 12 | **Q-DIST-01:** "What is the projected distribution schedule, and when does LP capital start returning?" | "When the portfolio supports it"; an IRR quoted with no timing | `GEN-11` |
| 13 | **Q-FEE-02:** "Which service providers (origination, servicing, valuation) are GP-affiliated, and what do they charge?" | "All arm's-length" without naming providers; the GP marks its own loans with no third-party agent | `GEN-06` |
| 14 | **Q-LIQ-01:** "What are my options if I need to exit before the fund term ends?" | "A secondary market may develop"; redemption gates not disclosed | — |

**Nice-to-ask**
- **Q-FEE-04 / Q-FEE-03:** the hurdle rate, whether it is hard or soft, the catch-up rate, and whether carry is whole-of-fund with a high-water mark. *Bad answer:* a soft hurdle with 100% catch-up, or a hurdle below 5% (`02` aggressive thresholds). (`EQUITY-04`, `EQUITY-01`/`EQUITY-02` analog)
- **Q-DIST-02:** capital-call schedule and missed-call penalties. *Bad answer:* "calls as needed," punitive dilution.
- **Q-GP-04:** how the team scaled with AUM. *Bad answer:* no named credit or workout team. (`GEN-04`)
- **Q-LIQ-02:** K-1 delivery timing. *Bad answer:* a history of extensions.

## 9. Diligence Checklist

- [ ] **LPA / PPM:** fee basis, step-down, carry, hurdle, catch-up, fund term, leverage limits in the governing documents
- [ ] **Credit facility agreement:** lender, cost, maturity, advance rates, borrowing-base tests, covenants, recourse to LP commitments
- [ ] **Loan tape:** borrower count, sizes, sector, lien position, non-accruals and watch list
- [ ] **Audited financials** and auditor identity. **Valuation policy** and whether a third-party valuation agent marks the book
- [ ] **SEC Form ADV Part 2** (fee schedules; `02` provenance) and a regulatory / litigation background check on the principals
- [ ] **Realized fund-level returns** on prior vintages, independently verified (fund administrator statements or an auditor), not the GP's deck
- [ ] **Sector outlook** for the named 60% sector, independent of the GP

## 10. Verdict

**Pass.** Enough is disclosed to underwrite the core story (leverage, concentration, seniority, headline fee and return), so this is a merits verdict, not an insufficient-disclosure one. The core story is the problem. "Senior secured" describes the loans, not the LP's position: the LP holds a levered equity slice of a single-sector-heavy loan book. The quoted 12% sits at the very top of the `01` 8–12% private-credit range, and it gets there through ~2.5x fund leverage (`CREDIT-01`), not through the loans themselves. The same leverage then triples-plus the impact of correlated losses in the 60% sector (`CREDIT-02`). About 1%/yr of incremental net loss turns a comfortable 717bps premium over HYG into a thin one. About 2%/yr leaves the LP locked up for roughly Treasury money.

**Biggest swing factor:** realized net loss rate in the concentrated sector, multiplied by the true leverage ratio.

**Who it could suit:** an LP who already holds diversified credit elsewhere, deliberately wants levered exposure to *this specific sector*, and can hold through the full term with no liquidity need.

**What would have to be true to re-screen as Pursue with conditions:**
1. "2.5x" turns out to be assets/equity (≈1.5x D/E), *or* the GP shows the unlevered book return still clears HYG plus the illiquidity hurdle.
2. The 2% fee is on committed or invested equity, not levered assets, with a stated step-down.
3. Realized, net-to-LP loss history through 2020 and 2022–23 in *this sector* shows low default and high recovery.
4. The facility matures after fund end and has no mark-to-market margin triggers that force selling in a downturn.
5. Carry and hurdle land inside `02` norms (≤20% over a ≥5% hard hurdle), and the GP has meaningful pari-passu co-invest.
