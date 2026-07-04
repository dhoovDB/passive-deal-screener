# Eval fixture 05 — Private credit fund, 2.5x levered, 60% single-sector

*Iteration-1 run, 2026-07-03, against SKILL.md @ cddc52d. Fixture prompt: evals.json id 5.*

---

**Verdict: Pass.** The two facts this fund does disclose are disqualifying in combination: 2.5x fund-level leverage stacked on a loan book with 60% in one sector. Leverage amplifies exactly the correlated-default risk that concentration creates — each risk makes the other worse, and no answer to a diligence question changes the structure. The quoted 12% "net" is almost certainly a leverage product, not a credit-selection product.

## 1. Deal Snapshot
- **Asset class:** Private credit 🟢
- **Deal type:** Debt fund (senior secured, levered) 🟢
- **Sponsor:** Not stated
- **Geography / sector:** 60% of book in one sector — **which sector is not stated** 🔴
- **Minimum / Hold / Raise:** Not stated
- **Claimed return:** 12% net IRR 🟢 — top of the `01` category range (8–12%); levered basis suspected 🔴
- **Leverage:** ~2.5x fund-level 🟢 (disclosed — credit where due)

## 2. Return Stress-Test
Baseline (`01`): private credit nets 8–12% — the 12% sits at the ceiling. With 2.5x fund leverage, the underlying book yield backs out to materially less; the ceiling-level net is being *manufactured* by leverage, not produced by the loans 🟡.

Benchmark (`05`): 12% over HYG (5.0%) ≈ 700bps; over the 2yr Treasury (4.15%) ≈ 785bps. Both clear any illiquidity hurdle on paper — but `05`'s spread table carries the exact caveat this deal trips: *"check fund leverage isn't manufacturing the spread (`CREDIT-01`)."* It is. The honest comparison is the **unlevered** book yield vs HYG, which is undisclosed 🔴.

Swing assumptions:
1. **Sector default correlation** — 60% in one sector means one sector downturn hits most of the book at once; at 2.5x, a modest correlated loss becomes a large LP loss.
2. **Leverage terms** — the fund's own credit line (rate, covenants, margin calls) is undisclosed; forced deleveraging into a falling book is how levered credit funds gate and impair.
3. **Whether 12% is levered** — presented without basis.

Bear case: a sector-specific stress producing, say, 8% defaults at 60% recovery on 60% of the book ≈ ~2% book-level loss → ~5% of LP equity at 2.5x, before the leverage facility's own reaction. Not computable precisely from disclosure — but the *shape* is the point.

## 3. Where LP Returns Come From
Interest income, amplified 2.5x by fund-level borrowing. This is the debt-fund version of a financing story: the LP's return is majority-attributable to the leverage facility, not the credit selection (`CREDIT-01` ↔ `GEN-07` family, per `03` notes). Strip the leverage and the book likely yields near HYG — meaning the LP is being paid a levered spread for levered risk, not an illiquidity premium for skill.

## 4. Fee Stack Summary
Per `02` (private credit inventory):

| Fee | Stated | `02` range | Read |
|---|---|---|---|
| Management | 2% | 1–2% investment period | At the top of range; **no step-down disclosed** — `02` flags absence 🟡 |
| Performance fee / carry | Not stated | 10–20% over 5–7% hurdle | Unknown 🔴 |
| Leverage costs | Not stated | *Variable*; >1.5× = compounded risk | 2.5x — above the `02` threshold; facility cost undisclosed |
| Servicing / admin | Not stated | 0.25–0.5% / $1–3k | Unknown |

**Gross-to-net not computable** (`GEN-16`, partial): with a 2% fee on top of undisclosed carry and undisclosed leverage costs, the drag between the book's yield and the LP's 12% can't be reconstructed — and on a levered basis, fees on gross assets scale against LP equity.

## 5. Red Flags
**RED**
- `CREDIT-01` — Fund-level leverage (~2.5x) stacked on loan leverage, **above `02`'s >1.5× threshold**, with the quoted 12% presented without a levered/unlevered basis. Exposure: amplified credit losses plus facility-driven forced selling; the LP's IRR unwinds the way it was manufactured.
- `CREDIT-02`, escalated by context — 60% single-sector concentration. As a standalone, `03` scores this YELLOW; at 2.5x leverage the correlated-default mechanism is amplified into capital-impairment territory. The cluster (`CREDIT-01` + `CREDIT-02`) is RED even where one member alone might not be.

**YELLOW**
- No management-fee step-down disclosed (`02`: absence is a flag; `HML-05` mechanism applies to credit funds).
- Sector identity undisclosed — concentration is quantified but not named, which prevents even assessing the sector's cycle position.
- `GEN-16` (partial) — carry, hurdle, and leverage costs undisclosed.

## 6. Missing Disclosures
Per `01` (private credit essentials):
- **Which sector** holds the 60% — quantified but unnamed
- Loan count and average loan size (granularity of the book)
- **Historical default rate and recovery** — absent entirely
- Whether the 12% is levered or unlevered
- Leverage facility terms: rate, covenants, mark-to-market/margin mechanics
- Carry / performance fee and hurdle
- Fund term, lock-up, redemption
- Sponsor identity, track record, co-invest

## 7. GP Alignment
Not assessable: sponsor unnamed, co-invest undisclosed, track record absent. Note the one honest signal: the fund *did* disclose its leverage and concentration numbers — a better disclosure posture than hiding them — but the numbers disclosed are the problem.

## 8. Questions for the GP
**Must-ask**
1. **Q-RISK-06** — "What is the fund's leverage ratio, and is the quoted 12% levered or unlevered? Show the unlevered book yield." *Bad answer:* presents the levered IRR as the only figure; "leverage is conservative" with no unlevered number. (`CREDIT-01`)
2. "Which sector is the 60%, and what is the single-largest-borrower exposure?" *Bad answer:* names the sector but can't quantify borrower-level concentration. (`CREDIT-02`)
3. **Q-RISK-05** — Default and recovery history through 2020 and 2022–23. *Bad answer:* "we've never had a loss"; default without recovery. (`HML-03`/`HML-04` mechanism)
4. Leverage facility terms: "What are the covenants and margin/mark-to-market triggers on the fund's credit line, and what happens to LP distributions if the facility tightens?" *Bad answer:* can't describe the facility's stress behavior. (`CREDIT-01` exposure)
5. **Q-FEE-01** — Complete fee schedule: carry, hurdle, step-down, leverage cost allocation. *Bad answer:* "standard 2-and-20" without the hurdle/step-down mechanics. (`GEN-16`)

**Nice-to-ask**
- **Q-GP-01** — co-invest; **Q-GP-03** — regulatory history; **Q-LIQ-01** — redemption/lock-up mechanics (gating provisions especially, given leverage).

## 9. Diligence Checklist
- [ ] Fund docs: leverage authority ceiling, facility agreement, gating/redemption terms
- [ ] Audited financials: realized loss history, unlevered book yield
- [ ] Loan tape: sector detail, borrower concentration, covenant quality (maintenance vs cov-lite)
- [ ] Sponsor identification, background/regulatory search
- [ ] Facility lender identity and the intercreditor position of LP equity

## 10. Verdict
**Pass.** The disqualifier is structural, not informational: 2.5x fund leverage on a 60% single-sector book means correlated defaults arrive levered, and the ceiling-level 12% "net" is the leverage talking. Unlike a disclosure-starved deal, better answers don't fix this one — the answers are already on the table. **What would have to be true to reconsider:** materially lower leverage (≤1.5x per `02`), a diversified book, and an unlevered yield that still clears HYG + illiquidity premium — i.e., a different fund. Suits an LP explicitly seeking levered credit beta and sized for the tail; as a "senior secured, 12% net" income allocation, it is mispresented.
