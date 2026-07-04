# Eval fixture 05 — Private credit fund, 2.5x levered, sector-concentrated
*Iteration-3 run, 2026-07-04, blind generation by fresh-context agent, against SKILL.md (post S1b/S2b fixes).*

**Verdict: Pass — the 12% net is leverage-manufactured (CREDIT-01, fund leverage ~2.5x vs the 1.5x threshold) sitting on a book with 60% in one sector (CREDIT-02); "senior secured" does not survive that combination. The structure, not a missing disclosure, is the verdict.**

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Private credit (senior secured) 🟢 |
| Deal type | Debt fund (private credit) 🟢 |
| Sponsor | Not stated |
| Geography | Not stated |
| Minimum investment | Not stated |
| Hold / fund term | Not stated (`01` norm: 3–7 yrs committed) |
| Raise / fund size | Not stated |
| Claimed return | 12% net IRR — **levered or unlevered basis not stated** 🔴 |
| Fund leverage | ~2.5x 🟢 |
| Concentration | ~60% of loan book in one sector 🟢 |
| Management fee | 2% 🟢 |

## 2. Return Stress-Test

Swing assumptions: **fund leverage (2.5x)**, **sector-correlated defaults**, **recovery rates**.

- **Base.** 12% net sits at the very top of the `01` private-credit band (8–12%) 🟢 — and at 2.5x leverage that is unremarkable arithmetic, not skill: a modest unlevered loan yield levered 2.5x produces exactly this kind of headline.
- **Bear.** Leverage cuts both ways with the same multiplier. Per `01`, private-credit recoveries run ~60–80% on defaults with wide dispersion. A correlated default event in the 60% sector — the precise scenario diversification exists to prevent — hits the levered equity 2.5x. Schematically 🟡: a 5% default wave in the concentrated sector at 70% recovery is ~90bps of portfolio loss, ≈315bps against LP equity at 2.5x, *before* financing costs on the leverage line; a genuine sector recession (double-digit default rates) threatens principal, not just yield. "Senior secured" describes the loans, not the LP — the LP sits in levered first-loss equity of the fund.
- **Benchmark (`05`, benchmark_comparator, 5-yr term assumed 🔴):** 12% vs HYG 5.0% = ≈700bps; ≈785bps over the 2yr Treasury (4.15%) → clears the ~300–400bps hurdle comfortably *on paper* — but `05`'s own spread-table caveat applies verbatim: "check fund leverage isn't manufacturing the spread (`CREDIT-01`)." Here it demonstrably is. The honest comparison is the *unlevered* portfolio yield vs HYG — which the fund has not shown.

## 3. Where LP Returns Come From

Loan interest income, amplified ~2.5x by fund-level borrowing. This is the debt-fund version of a financing story (GEN-07 family via CREDIT-01): the return driver is the leverage line, not underwriting alpha. Strip the leverage and the implied unlevered yield is likely in the mid-single digits 🟡 — around or below HYG, which the LP could hold liquid and diversified for 49bps of expense.

## 4. Fee Stack Summary (`02`)

| Fee | Deal | `02` norm | Read |
|---|---|---|---|
| Management fee | 2% | 1–2% committed; aggressive: >2% **or no step-down** | At the aggressive boundary; step-down not disclosed 🟡 |
| Performance fee / carry | Not stated | 10–20% over 5–7% hurdle, high-water mark | Undisclosed 🟡 |
| Hurdle structure | Not stated | Hard hurdle more LP-favorable | Undisclosed |
| Fund leverage costs | Not stated | `02`: >1.5x = compounded credit risk | 2.5x, financing cost undisclosed |
| Servicing / admin | Not stated | 0.25–0.5% / $1–3k per LP | Undisclosed |

**Gross-to-net drag is not computable** — management fee alone is 200bps/yr; carry, leverage financing cost, and servicing are all unknown. Also verify the fee *base*: 2% charged on gross (levered) assets rather than committed capital would be ~5% of LP equity at 2.5x leverage — a materially different fund (Q-FEE-01).

## 5. Red Flags (`03`)

**RED**
- **CREDIT-01** — fund leverage ~2.5x, far above the `02` 1.5x threshold: BDC-style leverage stacked on loan leverage amplifies losses, and the quoted 12% may be a levered figure presented as the fund's return quality (basis unstated). This is the deal's defining flag.

**YELLOW**
- **CREDIT-02** — ~60% single-sector concentration: correlated default risk that diversification is supposed to dampen; at 2.5x leverage this YELLOW compounds the RED above (the cluster is the deal).
- **GEN-16** (YELLOW–RED) — carry/hurdle, leverage cost, servicing all undisclosed; drag not computable.
- Management fee at the 2% aggressive boundary with no disclosed step-down (`02`) 🟡.
- **GEN-15 / GEN-17** (YELLOW–RED) — `01` essentials absent: loan count/average size, default and recovery history, seniority detail, sector identity.
- **GEN-11** — no distribution schedule stated.
- **GEN-07 (parenthetical, via CREDIT-01)** — the return is a leverage product, not an asset product.

## 6. Missing Disclosures (`01` private-credit essentials)

- Loan count and average loan size
- Sector mix — and *which* sector holds the 60%
- Historical default rate and recovery rate, through-cycle
- Seniority confirmation (first lien? unitranche? "senior secured" is asserted, not evidenced)
- Whether the 12% is levered or unlevered; the unlevered portfolio yield
- Carry/hurdle terms, leverage financing cost, fee base, step-down
- Fund term, capital-call schedule, distribution schedule, redemption terms
- Sponsor identity, track record, co-invest

## 7. GP Alignment

Unassessable from the disclosure 🔴: sponsor unnamed, co-invest unstated (GEN-01 unresolved), no track record offered (GEN-05/GEN-14 unresolved). Structurally, a 2% fee at 2.5x leverage pays the GP handsomely for balance-sheet risk the LP carries — alignment runs the wrong way unless the GP has meaningful equity in the fund.

## 8. Questions for the GP (`04`)

**Must-ask**
1. **Q-RISK-06** (CREDIT-01) — leverage ratio confirmed; is the 12% levered or unlevered, and what is the unlevered figure? *Bad answer:* presents the levered IRR as if unlevered; "leverage is conservative" with no number.
2. **CREDIT-02 response** — sector breakdown and single-largest-sector exposure: which sector is the 60%, and why? *Bad answer:* "we know this sector deeply" with no concentration limit.
3. **Q-RISK-05** (HML-03/HML-04 analogs for credit) — historical default and realized recovery, incl. 2020 and 2022–23. *Bad answer:* "we've never had a loss"; one number without the other.
4. **Q-FEE-01** (GEN-16) — complete fee schedule: carry, hurdle, high-water mark, fee base (committed vs gross assets), step-down, leverage cost. *Bad answer:* partial list; "the PPM has it."
5. **Q-GP-01** (GEN-01) — GP capital in the fund, same terms. *Bad answer:* fee-waiver co-invest.
6. **Q-GP-02** (GEN-05, GEN-14) — realized net-to-LP track record. *Bad answer:* marks-only.
7. **Q-DIST-01** (GEN-11) — distribution schedule and what gates it (leverage covenants can trap distributions). *Bad answer:* no schedule.
8. **Q-LIQ-01** — lock-up/redemption; what happens to redemptions if the leverage line's covenants trip. *Bad answer:* silence on the interaction.

**Nice-to-ask:** Q-GP-03 (GEN-02), Q-GP-04 (GEN-04), terms of the credit facility itself (mark-to-market triggers, margin calls — the mechanism by which levered credit funds gate in stress).

## 9. Diligence Checklist

- PPM/LPA: leverage authority and limits, fee schedule and base, carry terms
- Credit facility documents: covenants, mark-to-market and margin-call triggers
- Portfolio tape: loan count, sector codes, lien positions, non-accruals
- Audited financials; administrator-verified NAV and default history
- Sponsor background and regulatory search

## 10. Verdict

**Pass.** Enough is disclosed to underwrite the core return story — and the story is the problem: the 12% is manufactured by 2.5x fund leverage (CREDIT-01, well past `02`'s 1.5x line) sitting on a book with 60% correlated exposure to a single sector (CREDIT-02). That combination converts "senior secured" loans into a levered, concentrated equity-like position for the LP, where one sector downturn plus one leverage covenant is the wipeout path. The residual disclosure gaps (§6) would matter for a fixable deal; here the disclosed structure itself is disqualifying, so they are secondary. Biggest swing factor: the unlevered portfolio yield — if the GP showed, say, 9%+ unlevered with modest leverage and a diversification plan, this re-screens. What would have to be true to pursue: leverage at or below ~1.5x, single-sector exposure materially reduced (or the LP explicitly pricing it), and an unlevered yield that clears HYG + ~300–400bps on its own. As presented, an LP wanting credit yield gets a better risk-per-bp trade in the liquid comparator.
