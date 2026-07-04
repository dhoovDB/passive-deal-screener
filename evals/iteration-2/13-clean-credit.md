# Eval fixture 13 — Diversified BDC-style private credit fund
*Iteration-2 run, 2026-07-04, blind generation by fresh-context agent, against SKILL.md (post S1–S3 fixes).*

**Verdict: Pursue with conditions — the disclosure posture is the good-answer profile on nearly every `03` debt-fund axis (leverage 1.1x clearly disclosed and under the 1.5x line, 400+ loans, through-cycle default *and* recovery, levered *and* unlevered IRR shown, high-water mark). The conditions: the management fee is charged on **gross (levered) assets** — materially more than its 1.5% headline on an equity basis — and the hurdle rate, catch-up mechanics, actual return figures, and liquidity terms are not stated.**

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Private credit 🟢 |
| Deal type | Debt fund, BDC-style, large and diversified 🟢 |
| Sponsor | **Not stated** |
| Geography / sectors | Diversified across sectors (breakdown **not itemized**) 🟢 |
| Minimum investment | **Not stated** |
| Hold / liquidity | **Not stated** — traded BDC vs non-traded (lock-up/tender mechanics) is a first-order LP difference |
| Fund size | "Large" — figure **not stated** |
| Claimed return | Net IRR stated on a levered basis **with the unlevered figure also shown** 🟢 — but the actual numbers are not in the paste 🔴 |
| Leverage | ~1.1x, clearly disclosed, within standard BDC range 🟢 |
| Portfolio | 400+ loans; through-cycle default and recovery rates disclosed 🟢 |
| Fees | 1.5% management on gross assets (1.0% on assets below the 200% asset-coverage threshold); two-part incentive fee with hurdle + high-water mark 🟢 |

Routing: `01` private credit baseline (8–12% net, senior secured, 3–7yr); `02` private credit fee inventory; `03` `GEN-`, `CREDIT-`; `05` HYG / PRIV + 2yr Treasury.

## 2. Return Stress-Test

Swing assumptions: **(a) the credit cycle** — default frequency against the disclosed through-cycle history; **(b) base-rate path** — BDC books are mostly floating; falling rates compress income (and rising rates stress borrowers — the exposure is two-sided); **(c) NAV marks and (if non-traded) tender liquidity** in a dislocation.

- **Base:** the `01` category band, 8–12% net; the fund's actual stated figure must be slotted in (not in the paste 🔴). At 1.1x leverage on a senior book, a low-double-digit net is structurally plausible without heroic assumptions 🟡.
- **Bull:** benign defaults + elevated base rates → top of band.
- **Bear:** a default cycle at, say, 1.5–2x the disclosed through-cycle rate with recoveries at the historical 60–80% (`01`) — at 1.1x leverage this compresses returns to low/mid single digits rather than impairing principal, *if* the disclosed history is representative 🟡. Contrast fixture 05: leverage under the `02` 1.5x line is what keeps the bear case a yield event, not an equity event.
- **Benchmark (`05`):** category net 8–12% vs HYG 5.0% = **+300–700bps**, and over the 2yr Treasury (4.15%) ≈ **+385–785bps** of credit + illiquidity spread — clears the ~300–400bps hurdle for a 3–7yr commitment across most of the band; thin at the very bottom. PRIV is unseasoned per `05`; note also `05`'s smoothed-marks caveat — private-credit NAV stability overstates true risk, so any "low volatility" pitch should be discounted, disclosed leverage or not 🟡. Verify the fund's stated net against this once the number is provided.

## 3. Where LP Returns Come From

Contractual interest on a 400+-loan senior book — income-driven; no terminal-value or cap-rate story (`GEN-08` n/a). Leverage contributes a measured slice: at ~1.1x the return is amplified but not manufactured, and the fund *shows both bases* — the exact good-answer signal of `Q-RISK-06`, which is what separates this from a `CREDIT-01`/`GEN-07` financing story 🟢. Rules 3–4: no flag; the unlevered figure (once its value is confirmed) is the honest earning power to anchor on.

## 4. Fee Stack Summary

| Fee | Stated | `02` range | Read |
|---|---|---|---|
| Management fee | 1.5% **of gross assets** (1.0% below the 200% asset-coverage threshold) | 1–2% of committed/invested capital | Headline in range — **base is not**. See below 🟡 |
| Incentive fee | Two-part, hurdle + high-water mark | 10–20% over 5–7% hurdle; HWM standard | Structure right; **rates and hurdle unstated** 🟡 |
| Hurdle type | Not stated (hard vs soft, catch-up %) | Soft hurdle w/ 100% catch-up = aggressive | Ask |
| Servicing / admin | Not stated | 0.25–0.5% / $1–3k per LP | Confirm |

**The gross-assets fee base is the sharpest finding 🟡:** at ~1.1x debt-to-equity, gross assets run ≈2.1x equity, so 1.5% of gross assets ≈ **~3.1% of LP equity per year** — roughly double the `02` range read on the basis LPs actually own. The 1.0% tier on above-threshold assets mitigates at higher leverage, and gross-asset fees are common BDC practice — but common is not cheap, and the structure pays the GP more for carrying more leverage (a mild misalignment the disclosed coverage-threshold step-down only partly offsets). **Total gross-to-net drag: not computable without the incentive-fee rates and hurdle — that residual is the §8 ask (`GEN-16` partial).** The levered-and-unlevered IRR disclosure means the *outcome* of the drag is at least visible end-to-end 🟢.

## 5. Red Flags

The debt-fund kill-list is affirmatively **clear**: `CREDIT-01` clear (1.1x, under the `02` 1.5x compounded-risk line; levered vs unlevered basis explicitly disclosed — the `Q-RISK-06` good answer); `CREDIT-02` clear (400+ loans, sector-diversified); `HML-03`/`HML-04` analogs clear (through-cycle default *and* recovery disclosed — the `Q-RISK-05` good answer); high-water mark present (`02` standard).

What still fires:

**YELLOW**
- Management fee on **gross assets** — effective ~3.1% on equity vs the `02` 1–2% capital-basis range; scored against `02`'s fee baseline and the `GEN-06`-adjacent pay-for-leverage mechanism (no `03` ID matches exactly; the `02` aggressive-threshold framework is the citation) → `Q-FEE-01`.
- Incentive-fee rates and hurdle unstated — a "hurdle + HWM" label with no numbers; `02` marks hurdle <5% and soft-hurdle-100%-catch-up as aggressive, and neither can be checked → `Q-FEE-01`.
- `GEN-11` (adapted) — no distribution schedule or liquidity mechanics stated; for a BDC the traded/non-traded distinction *is* the LP's liquidity reality (non-traded tender gates are the private-credit lock-up) → `Q-DIST-01`, `Q-LIQ-01`.
- `GEN-17` (residual) — actual return figures, seniority mix, average loan size not in the paste (see §6).

No RED or YELLOW–RED flags fire 🟢.

## 6. Missing Disclosures

Against the `01` private-credit essentials: loan count ✓ (400+), sector mix ✓ (asserted diversified — itemization missing), fund leverage ✓ (1.1x), default/recovery ✓ (through-cycle). Remaining:
- **Seniority position** — "BDC-style" and "diversified" are asserted; first-lien % vs second-lien/unitranche/equity kickers is not stated — an `01` essential, and the largest residual unknown in the risk position.
- **Average loan size** and single-name concentration (400+ loans can still carry outsized top-10 exposure).
- The **actual net IRR figures** (levered and unlevered) — described as shown, not in the paste.
- Incentive-fee rates, hurdle level, hard-vs-soft, catch-up %.
- Traded vs non-traded; if non-traded: tender program size, gates, NAV frequency.
- Non-accrual rate today (default history is backward-looking; non-accruals are the leading indicator).
- Sponsor identity, AUM, GP co-investment; PIK income share (PIK can flatter current yield).

## 7. GP Alignment

- **Disclosure conduct:** showing levered *and* unlevered IRR unprompted, plus through-cycle loss data, is the transparent-GP profile — the opposite of the `GEN-05`/`GEN-14` pattern 🟢 (self-reported until verified in filings 🟡).
- **Fee alignment:** the gross-assets base pays the GP on leverage as well as on assets — partially offset by the disclosed 1.0% below-coverage-threshold tier and disciplined actual leverage (1.1x); the HWM prevents incentive fees on recouped losses 🟢/🟡 mixed.
- **Co-investment:** not stated → `Q-GP-01` (for BDCs: insider/affiliate ownership of shares).
- **Track record:** portfolio-level credit stats disclosed; fund-level realized net-to-LP across vintages not stated → `Q-GP-02`.
- **Affiliates:** BDC complexes often route origination/servicing through affiliates → `Q-FEE-02` (`GEN-06` probe).

## 8. Questions for the GP

**Must-ask**
1. `Q-FEE-01` — Full fee mechanics: incentive-fee rates, hurdle level, hard or soft, catch-up % — and the management fee restated as an effective % of **equity** at current leverage. *Bad answer:* "standard BDC 1.5%" with the equity-basis math dodged; hurdle below 5% (`02` aggressive); soft hurdle with 100% catch-up.
2. `Q-RISK-06` (confirmation) — The actual levered and unlevered net figures, and the leverage covenant/target range. *Bad answer:* the unlevered figure quietly disappears from follow-ups.
3. `Q-RISK-05` (verification) — The through-cycle default/recovery data by vintage, plus **current non-accruals** and PIK share. *Bad answer:* aggregate stats that can't be broken down; PIK income recharacterized as cash yield.
4. Seniority mix (per `01` essentials, `GEN-17` form) — First-lien % of the book, and top-10 borrower concentration. *Bad answer:* "substantially senior secured" with no percentage.
5. `Q-LIQ-01` — Traded or non-traded; if non-traded, tender-program mechanics, gates, and history of honoring tenders in full. *Bad answer:* "quarterly liquidity" that is board-discretionary and pro-rated in stress.
6. `Q-DIST-01` — Distribution rate vs NII coverage (is the distribution earned, or partly return of capital?). *Bad answer:* distribution coverage below 100% waved off.
7. `Q-GP-01` — GP/insider capital in the fund. *Bad answer:* token ownership; fee waivers counted as alignment.
8. `Q-GP-02` — Realized net-to-LP results on prior funds/vintages. *Bad answer:* since-inception marks only.

**Nice-to-ask:** `Q-GP-03` (regulatory/litigation), `Q-GP-04` (origination team vs AUM growth), `Q-LIQ-02` (K-1s vs 1099 — entity-form tax mechanics), sector itemization (`CREDIT-02` residual), the credit facility's terms (rate, covenants).

## 9. Diligence Checklist

- If a registered BDC: pull the 10-K/10-Q and N-2 — fee mechanics, non-accruals, PIK %, seniority tables, and leverage are all filed; verify every marketed stat against the filings.
- Fee table reconstruction: effective total expense ratio on equity (management + incentive + interest expense + operating costs) — BDC all-in costs routinely exceed the headline by multiples.
- Valuation policy review (Level 3 marks; smoothed-NAV caveat, `05`).
- Background/regulatory search on the adviser; SEC exam/enforcement history.
- Tender/redemption history through 2020 and 2022–23 if non-traded.
- Independent administrator/auditor confirmation.

## 10. Verdict

**Pursue with conditions.** On every axis where fixture-05-style credit funds fail, this one shows the good-answer pattern: leverage modest and disclosed on both bases, genuine diversification, both halves of the loss history, an HWM on the incentive fee. The `01` essentials are substantially met, so a merits verdict is warranted. Biggest swing factor: **the all-in fee load on an equity basis** — a 1.5% gross-assets fee (~3.1% of equity at 1.1x) plus an unquantified two-part incentive fee can consume several hundred bps of a senior-credit return that only earns ~8–12% gross of them; whether the net still clears HYG + 300–400bps after the *true* stack is the decision.

**Conditions:** (1) the actual levered and unlevered net figures, benchmarked per §2; (2) incentive-fee rates, hurdle, and catch-up — check against `02`'s aggressive lines; (3) effective total expense ratio on equity; (4) seniority mix and top-10 concentration; (5) liquidity mechanics (traded float or tender program) in writing; (6) filing-level verification of the credit stats. **Who it suits:** an income LP wanting diversified senior-credit exposure with modest leverage and a 3–7yr horizon, who accepts smoothed marks and tender-gated liquidity. **What would have to be true:** the net-of-everything yield clears the HYG-plus-illiquidity bar once the real fee stack is priced — the structure earns the diligence; the fee base is what the diligence must price.
