# Eval fixture 05 — Private credit fund, 2.5x levered, 60% one sector
*Iteration-2 run, 2026-07-04, blind generation by fresh-context agent, against SKILL.md (post S1–S3 fixes).*

**Verdict: Pass as presented — insufficient disclosure, with a structural RED that disclosure alone can't fix: 2.5x fund-level leverage (`CREDIT-01`, threshold 1.5x) stacked on a book that is 60% one sector (`CREDIT-02`) means the quoted 12% "net" is a levered, concentrated credit bet — and whether 12% is even a levered or unlevered figure is unstated.**

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Private credit (senior secured) 🟢 |
| Deal type | Debt fund 🟢 |
| Sponsor | **Not stated** |
| Geography | **Not stated** |
| Minimum investment | **Not stated** |
| Hold / fund term | **Not stated** (category norm 3–7yr committed, `01`) |
| Raise / fund size | **Not stated** |
| Claimed return | 12% net IRR — **levered or unlevered basis not stated** 🔴 |
| Fund leverage | ~2.5x 🟢 |
| Sector mix | ~60% of loan book in one sector (**which sector not stated**) 🟢 |
| Management fee | 2% (base — committed? invested? gross assets? **not stated**; no step-down mentioned) |

Routing: `01` private credit baseline (8–12% net, senior secured); `02` private credit fee inventory; `03` `GEN-`, `CREDIT-`; `05` HYG / PRIV + 2yr Treasury.

## 2. Return Stress-Test

Swing assumptions: **(a) fund leverage** — at ~2.5x, a small rise in defaults is multiplied through the equity; **(b) the concentrated sector's credit cycle** — 60% of the book moves together; **(c) cost and stability of the fund's own financing** — levered credit funds die from their liabilities (margin/borrowing-base calls) as often as from their assets.

- **Base:** 12% net as quoted — top of the `01` 8–12% band. At ~2.5x leverage, the implied unlevered book yield is modest (roughly: 12% equity return at 2.5x leverage and today's borrowing costs implies an asset yield in the single digits before fees 🟡) — the fund's *assets* earn ordinary credit returns; the *structure* manufactures the 12%.
- **Bull:** benign defaults, stable funding → 12%+ pays.
- **Bear:** a default cycle in the concentrated sector — with recovery at the historical 60–80% (`01`) on, say, 10% of a book that is 60% correlated, levered ~2.5x — flows through to a double-digit equity hit; add a lender tightening the fund's own facility and the LP faces gates, suspended distributions, or forced deleveraging at the bottom 🔴. No downside case is provided to check any of this (`GEN-13`).

**Benchmark (`05`):** 12% vs HYG 5.0% = **+700bps**; vs the 2yr Treasury (4.15%) ≈ **+785bps**. Top of the private-credit band — but the spread table's own caveat is the operative one: *"check fund leverage isn't manufacturing the spread (`CREDIT-01`)."* Here it demonstrably is: HYG is an unlevered, diversified index; this is a 2.5x-levered, 60%-concentrated book. The comparison flatters the fund on both axes. Risk-matched, the true excess spread is far thinner than 700bps, and possibly negative 🟡. (PRIV is unseasoned per `05`; note also `05`'s smoothed-marks caveat — private credit's apparent low volatility understates risk, doubly so levered.)

## 3. Where LP Returns Come From

Contractual loan interest — but the LP's *return on equity* comes substantially from the leverage spread (borrow at fund level, lend at book level, keep the difference ×2.5). This is the credit-fund version of a financing story: `CREDIT-01` explicitly connects to `GEN-07` (cited parenthetically) — a modest loan-book yield levered into a marketable LP IRR, which unwinds the same way. Rules 3–4: return is leverage-driven → RED, stated in the verdict.

## 4. Fee Stack Summary

| Fee | Stated | `02` range | Read |
|---|---|---|---|
| Management fee | 2% | 1–2% committed during investment period, 1–1.5% invested after; **>2% or no step-down = aggressive** | At the aggressive boundary; no step-down mentioned → flag 🟡. Base undisclosed — 2% on *gross (levered) assets* at 2.5x would be ~5%+ on equity, far outside range → must ask |
| Performance fee / carry | **Not stated** | 10–20% over 5–7% hurdle; >25% or hurdle <5% aggressive | Undisclosed 🟡 |
| Hurdle structure | **Not stated** | Hard vs soft; soft w/ 100% catch-up aggressive | Undisclosed |
| Fund-level leverage cost | Implied by 2.5x, terms not stated | *Variable*; **>1.5x = compounded credit risk** | Fired — see `CREDIT-01` |
| Servicing / admin | **Not stated** | 0.25–0.5% / $1–3k per LP | Undisclosed |

**Gross-to-net drag: not computable — that is the finding (`GEN-16` partial).** With only "2% management fee" disclosed, and its base unstated, the gap between book yield and the 12% cannot be reconciled. On a levered fund the fee base question is first-order, not housekeeping.

## 5. Red Flags

**RED**
- `CREDIT-01` — fund-level leverage ~2.5x stacked on loan leverage, far above the `02` >1.5x compounded-credit-risk threshold; and the quoted 12% may be a levered figure presented as if it were the fund's earning power (basis unstated) → `Q-RISK-06`. (Connects to `GEN-07` — the financing-story family; cited parenthetically per `03` notes.)

**YELLOW (escalating as a cluster)**
- `CREDIT-02` — ~60% single-sector concentration: correlated default risk that diversification is supposed to dampen; at 2.5x leverage the correlation is amplified, so `CREDIT-01`+`CREDIT-02` together read RED as a pair → `Q from 03`: sector breakdown / single-largest exposure (routed via `Q-RISK-05`'s portfolio lens and the `CREDIT-02` response question).
- Management fee at the `02` aggressive boundary (2%, no step-down mentioned, base undisclosed) → `Q-FEE-01`.
- `GEN-13` — no downside or sensitivity case → `Q-DS-03` (adapted: defaults up, spreads wide, facility repriced).
- `GEN-11` — 12% IRR with no distribution schedule or fund-term disclosure → `Q-DIST-01`.

**YELLOW–RED**
- `GEN-15`/`GEN-16` — no loan count, average size, default/recovery history, hurdle terms, or fund terms; the fund cannot be underwritten from this disclosure → `Q-RISK-03` (loan-tape form), `Q-FEE-01`.

## 6. Missing Disclosures

Against the `01` private-credit essential-disclosure baseline (`GEN-17`):
- **Loan count and average loan size** — absent.
- **Sector mix** — only "60% one sector"; the sector itself, and the rest of the breakdown, absent.
- **Fund leverage ratio** — stated (2.5x) 🟢, but its terms (facility size, rate, covenants, mark-to-market triggers) absent.
- **Seniority position** — "senior secured" asserted 🟢; first-lien vs unitranche vs split-lien absent.
- **Historical default rate and recovery rate (through-cycle)** — absent entirely.
- Plus: whether 12% is levered/unlevered, carry/hurdle, fee base, fund term and redemption terms, sponsor identity and track record, GP co-investment, distribution schedule.

## 7. GP Alignment

- **Co-investment:** not stated → `Q-GP-01`.
- **Track record:** none offered — no vintages, no realized net-to-LP, no loss history. Treat as no validated record (`GEN-05`/`GEN-14` mechanism) 🔴 → `Q-GP-02`.
- **Fee alignment:** a 2% fee whose base is undisclosed, on a 2.5x-levered fund, raises the classic misalignment: if the fee is charged on gross assets, the GP is paid to add leverage regardless of LP outcome 🟡 → `Q-FEE-01`.
- **Affiliates:** origination/servicing affiliates undisclosed → `Q-FEE-02` (`GEN-06` probe).

## 8. Questions for the GP

**Must-ask**
1. `Q-RISK-06` — What is the fund's leverage ratio and facility terms, and is the quoted 12% levered or unlevered? *Bad answer:* presents the levered IRR as the only figure; "leverage is conservative" with no covenant detail.
2. `CREDIT-02` response — Full sector breakdown and single-largest-sector exposure; why is 60% in one sector consistent with "diversified" private credit? *Bad answer:* "we know this sector better than anyone" with no concentration limit.
3. `Q-RISK-05` — Historical default and realized recovery rates, through 2020 and 2022–23. *Bad answer:* "we've never had a loss"; default without recovery or vice versa.
4. `Q-FEE-01` — Complete fee schedule: the 2% fee's base (committed/invested/gross assets), step-down, carry, hurdle, high-water mark. *Bad answer:* "standard 2-and-20"; fee base dodged.
5. `Q-DS-03` (adapted) — Net LP return if defaults run 2x historical and the credit facility reprices +200bps? *Bad answer:* no downside case exists; "our loans are senior secured" as the whole answer.
6. `Q-GP-02` — Realized net-to-LP returns on prior funds. *Bad answer:* project/gross-level IRR; unrealized marks.
7. `Q-GP-01` — GP capital in the fund on LP terms. *Bad answer:* fee waiver counted as co-invest.
8. `Q-DIST-01` — Distribution schedule and fund term. *Bad answer:* no schedule; "evergreen" with undefined gates.
9. `Q-LIQ-01` — Redemption/withdrawal mechanics, gates, and what happens to redemptions if the facility lender tightens. *Bad answer:* "we've never gated" with no written mechanics.

**Nice-to-ask:** `Q-GP-03` (regulatory/litigation), `Q-GP-04` (team vs AUM), `Q-LIQ-02` (K-1s), covenant headroom on the fund facility today.

## 9. Diligence Checklist

- LPA/PPM: leverage authority and cap, fee base language, carry/hurdle, gates.
- Credit facility agreement: advance rates, mark-to-market and borrowing-base triggers, cross-defaults.
- Loan tape or audited portfolio schedule: sector, seniority, rates, non-accruals.
- Audited fund financials; verify the 12% and its basis.
- Background/regulatory search on the sponsor.
- Independent administrator and valuation-policy review (smoothed marks caveat, `05`).

## 10. Verdict

**Pass as presented — insufficient disclosure** — most `01` essentials (loan count, default/recovery history, fund terms) are absent, so no merits verdict is available on the book itself. But the re-screen list comes with a warning: the two facts the fund *did* disclose are a RED (`CREDIT-01`, 2.5x vs the 1.5x threshold) and a concentration YELLOW that the leverage escalates (`CREDIT-02`). Biggest swing factor: **the fund's own credit facility** — in a sector downturn, 2.5x leverage on a 60%-correlated book converts ordinary credit losses into an equity event, and the facility's covenants decide when.

**Re-screen list:** levered/unlevered basis of the 12%; facility terms and covenants; full sector breakdown; loan count/size; through-cycle default and recovery; complete fee schedule with base and step-down; fund term and gates; sponsor track record net-to-LP; GP co-invest. **What would have to be true to pursue:** leverage genuinely at or below ~1.5x (or the LP is knowingly buying a levered credit vehicle priced for it), concentration explained by a real concentration limit, and a verified through-cycle loss history. As presented it suits no senior-secured-income LP — the 12% is being produced by the two features (leverage, concentration) that senior-secured investing exists to avoid.
