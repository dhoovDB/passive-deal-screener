# Eval fixture 03 — Hard-money bridge fund (well-disclosed)
*Iteration-3 run, 2026-07-04, blind generation by fresh-context agent, against SKILL.md (post S1b/S2b fixes).*

**Verdict: Pursue with conditions — the disclosures that usually hide the bodies (as-is LTV, through-cycle default and recovery, geographic mix, fee step-down) are all present and in-range; residual gaps are fund leverage, performance fee, co-invest, and liquidity terms, which become conditions, not the verdict.**

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Hard money / bridge loans (senior secured) 🟢 |
| Deal type | Debt fund 🟢 |
| Sponsor | Not stated |
| Geography | 12 states; no single metro >15% of book 🟢 |
| Minimum investment | Not stated |
| Hold / fund term | Not stated (`01` norm: 3–5-year fund commitment) |
| Raise / fund size | Not stated |
| Claimed return | 9% net to LPs (target) 🟢 |
| Loan book | Avg LTV 68% as-is / 72% ARV; grades A–D with mix disclosed 🟢 |
| Credit history | 3.1% default rate, 92% realized recovery, incl. 2020 and 2022–23 🟢 |

## 2. Return Stress-Test

Swing assumptions: **credit losses**, **fund leverage (undisclosed)**, **reinvestment yield as loans roll**.

- **Base.** 9% net sits inside the `01` category norm (8–10% net; 11–13% gross common) 🟢 — a credible, un-stretched target.
- **Bear.** Expected-loss math from the disclosed history: 3.1% default × (1 − 92% recovery) ≈ **25bps annual loss rate** 🟡 — comfortably absorbed by the yield. Stress it: at a 2008-style 3× default rate with recovery falling to 70%, loss ≈ 280bps — the 9% net degrades but stays positive *if the fund is unlevered*. Fund leverage is the undisclosed multiplier on this scenario 🔴.
- **Benchmark (`05`, benchmark_comparator, 4-yr fund term assumed 🔴):** 9% net vs HYG 5.0% (10yr) = **≈400bps premium** → clears the ~300–400bps hurdle for a 3–5-year lock-up. Duration-matched Treasury floor: **≈529bps over the 3mo (3.71%)** — the LP is paid a real credit + illiquidity spread, not just a rate ride.

## 3. Where LP Returns Come From

Current interest income from senior-secured, short-duration loans — an income story, not an exit or leverage story 🟢. No terminal-value assumption exists to lean on; the return is a function of coupon minus fees minus credit losses. The one place a hidden financing story could live is fund-level leverage, which is not disclosed either way — resolve before wiring (CREDIT-01 family, §5).

## 4. Fee Stack Summary (`02`)

| Fee | Deal | `02` norm | Read |
|---|---|---|---|
| Fund management | 1.5%, stepping to 1.0% after investment period | 1–2% AUM; absence of step-down is a flag | In range, **step-down present** 🟢 |
| Performance fee / carry | Not stated | 10–20% over 5–8% hurdle in some HML funds | Absent or undisclosed 🟡 |
| Servicing | Not stated | 0.25–0.5% of loan balance | Undisclosed 🟡 |
| Origination points | Not stated | 1–3 points, borrower-paid, should flow to fund yield | Verify they flow to the fund, not the GP |
| Late fees / default interest | Not stated | Should benefit the fund, not a GP "workout fee" | Verify |

**Drag as computable:** management fee alone = 150bps → 100bps post-step-down. Implied gross-to-net gap vs the 11–13% gross category norm is 200–400bps, which is plausible only once servicing/performance fees are known — **the full drag is not computable from this disclosure; that residual is the §8 ask (Q-FEE-01), not a verdict-changer.**

## 5. Red Flags (`03`)

**No RED flags fire on what is disclosed.** The four classic HML flags are affirmatively cleared:
- **HML-01** does *not* fire — LTV given on as-is (68%), not just ARV 🟢.
- **HML-02** does *not* fire — 12 states, no metro >15% 🟢.
- **HML-03 / HML-04** do *not* fire — default (3.1%) *and* recovery (92%) disclosed, through 2020 and 2022–23 🟢.
- **HML-05** does *not* fire — step-down present 🟢.

**YELLOW (unresolved, not fired):**
- **GEN-16 (partial)** — performance fee, servicing fee, and fee-flow of points/default interest undisclosed; drag not fully computable.
- **CREDIT-01 (family, unresolved)** — fund leverage undisclosed; a levered 9% is a different risk than an unlevered 9%.
- **GEN-01 (unresolved)** — GP co-invest not stated.
- **GEN-11** — no distribution schedule stated (income funds typically pay monthly/quarterly; confirm).
- **GEN-14 (unresolved)** — credit statistics are strong but self-reported; fund-level realized net-to-LP not shown.

## 6. Missing Disclosures (`01` HML essentials + `02`)

`01` essentials are largely **present** (as-is LTV ✓, default history ✓, recovery ✓, geographic mix ✓). Sponsor downturn history is partially covered by the 2020/2022–23 stats but the sponsor itself is unnamed. Still missing:
- Fund term, lock-up, and redemption/withdrawal terms
- Fund-level leverage (yes/no, ratio)
- Performance fee / hurdle; servicing fee; where origination points and default interest flow
- GP co-invest; sponsor identity and fund-level realized net-to-LP returns
- Distribution schedule and frequency
- Loan-grade definitions behind the A–D mix

## 7. GP Alignment

- **Co-invest:** not stated → Q-GP-01.
- **Track record:** the disclosed credit stats are the right *kind* of evidence (realized recovery, through stress periods) 🟢 — but self-reported and not yet third-party verified, and fund-level net-to-LP by vintage is not shown 🟡.
- **Fee alignment:** step-down after the investment period is an LP-favorable, ILPA-consistent structure 🟢.
- **Affiliate fees:** no disclosure either way (GEN-06 unresolved).

## 8. Questions for the GP (`04`)

**Must-ask**
1. **Q-FEE-01** (GEN-16) — complete fee schedule: performance fee/hurdle, servicing, and where points and default interest flow. *Bad answer:* "standard market fees"; fees surface only after commitment.
2. **Q-RISK-06** (CREDIT-01) — fund leverage ratio; is the 9% net levered or unlevered? *Bad answer:* "leverage is conservative" with no number.
3. **Q-GP-01** (GEN-01) — GP cash in the fund, same terms. *Bad answer:* token amount or fee-waiver "co-invest."
4. **Q-RISK-05** (HML-03, HML-04) — loan-level tape or audited support for the 3.1%/92% figures, with workout timelines. *Bad answer:* can't produce support; the numbers move when documented.
5. **Q-LIQ-01** — redemption terms, gates, lock-up. *Bad answer:* "we'll try to accommodate."
6. **Q-DIST-01** (GEN-11) — distribution schedule and frequency. *Bad answer:* no committed schedule.
7. **Q-GP-02** (GEN-05, GEN-14) — fund-level realized net-to-LP by vintage. *Bad answer:* only portfolio-level gross yield.

**Nice-to-ask**
8. **Q-GP-03** (GEN-02) — regulatory/litigation history.
9. **Q-FEE-02** (GEN-06) — any GP-affiliated servicer/originator and its pricing.
10. **Q-GP-04** (GEN-04) — underwriting headcount vs AUM growth; definitions of grades A–D and who assigns them.

## 9. Diligence Checklist

- PPM + LPA: full fee schedule, leverage authority, redemption mechanics
- Audited financials; loan tape sample to verify LTV basis and grade mix
- Third-party verification of default/recovery history (auditor letter or fund admin)
- Sponsor background: SEC/FINRA/state search, litigation search
- Confirm servicing/custody arrangements and that default interest accrues to the fund

## 10. Verdict

**Pursue with conditions.** This fund discloses exactly the things weak HML funds hide — as-is LTV with the ARV shown alongside, both halves of the credit-loss story through the 2020 and 2022–23 stress windows, real geographic diversification, and an LP-favorable fee step-down — and the 9% net target is honest for the category rather than stretched. Enough is disclosed to underwrite the core return story, so the residual absences are conditions: (1) fund leverage confirmed at or near zero — this is the biggest swing factor, since leverage silently converts the 25bps expected-loss cushion into a multiplied exposure; (2) the complete fee schedule (performance/servicing/points flow) so drag is computable; (3) third-party verification of the credit stats; (4) redemption terms in writing. Suits an income-oriented LP wanting 8–10% with senior-secured collateral and modest duration; what must be true: the disclosed credit history survives an audit and the 9% is not leverage-assisted. A bad answer on Q-RISK-06 re-opens the verdict.
