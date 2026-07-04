# Eval fixture 03 — Hard-money bridge fund (disclosure-complete)

*Iteration-1 run, 2026-07-03, against SKILL.md @ cddc52d. Fixture prompt: evals.json id 3 (contrast pair 3a).*

---

**Verdict: Pursue** — this fund discloses exactly the things hard-money funds usually hide: as-is LTV alongside ARV, default *and* recovery through the 2020 and 2022–23 stress windows, geographic distribution, and a management-fee step-down. The remaining work is verification and the handful of items still unstated (fund leverage, performance fee, sponsor identity), none of which is currently a red flag. Biggest swing factor: whether the self-reported 3.1%/92% loss history survives third-party verification.

## 1. Deal Snapshot
- **Asset class:** Hard money / bridge loans 🟢
- **Deal type:** Debt fund (senior secured) 🟢
- **Sponsor:** Not stated in this summary
- **Geography:** 12 states, no metro >15% 🟢
- **Minimum:** Not stated
- **Hold:** Not stated (fund term/lock-up unstated; category norm 3–5yr fund commitment per `01`)
- **Raise:** Not stated
- **Claimed return:** 9% net to LPs 🟢

## 2. Return Stress-Test
Baseline (`01`): hard-money funds net 8–10% to LPs — the 9% target sits mid-range, not aggressive 🟢.

Benchmark (`05`): HYG 10yr = 5.0% → **≈400bps premium**. Duration-matched Treasury floor (3mo ≈3.71%) → **≈529bps absolute credit + illiquidity spread**. For a 3–5yr fund commitment the hurdle is ~300–400bps → **clears** 🟢 (verify with `scripts/benchmark_comparator.py`). The premium is paid for illiquidity plus the single-borrower concentration HYG diversifies away — which this fund's 12-state book partially mitigates.

Swing assumptions:
1. **Credit losses vs history** — the 3.1% default / 92% recovery implies ~25bps expected annual loss; a 2008-style dislocation would test both numbers.
2. **Fund-level leverage** — unstated; if the 9% net requires leverage on the loan book, the risk shape changes (see §5).
3. **Deployment / cash drag** — undeployed capital earns nothing; redemption and reinvestment mechanics unstated.

## 3. Where LP Returns Come From
Interest income on senior-secured short-duration loans — an income story, not an exit story 🟢. No terminal-value dependence; the J-curve concern of equity deals largely doesn't apply (current-pay interest), though the distribution schedule is unstated. The key structural question is whether the 9% net is produced by the loan book alone or by leverage on it — unstated, routed to §8.

## 4. Fee Stack Summary
Per `02` (hard money / bridge inventory):

| Fee | Stated | `02` range | Read |
|---|---|---|---|
| Fund management | 1.5% → 1.0% post-investment-period | 1–2%, step-down standard | In range; step-down present 🟢 (defuses `HML-05`) |
| Performance fee / carry | **Not stated** | 10–20% over 5–8% hurdle, when present | Unknown — ask 🔴 |
| Servicing | Not stated | 0.25–0.5% | Unknown |
| Origination points (borrower-paid) | Not stated | 1–3 pts | Flows to yield; confirm not siphoned |
| Late fees / default interest destination | Not stated | Should benefit the fund, not the GP | Confirm |

Drag to the stated **net** 9% is already embedded — but the stack behind it isn't fully disclosed, so the gross-to-net path can't be independently reproduced (`GEN-16`, partial). If a performance fee exists above the stated net, the finding changes; ask.

## 5. Red Flags
**Defused by disclosure (worth recording — these are the flags this deal type usually trips):**
- `HML-01` — **defused**: LTV given on as-is (68%) *and* ARV (72%); a real equity cushion exists on current value.
- `HML-03`/`HML-04` — **defused**: default (3.1%) *and* recovery (92%) disclosed, explicitly through 2020 and 2022–23 — the pair, not one half.
- `HML-02` — **defused**: 12 states, no metro >15%.
- `HML-05` — **defused**: step-down to 1.0% disclosed.

**Open (YELLOW):**
- Fund-level leverage undisclosed — if present and >1.5× equity, compounded credit risk (`CREDIT-01` mechanism applies to levered HML funds too).
- Performance fee / full fee schedule undisclosed (`GEN-16`, partial).
- Sponsor identity, track record beyond the loss stats, and co-invest unstated (`GEN-01` unresolvable as disclosed).
- Self-reported loss history — treat as unverified until the basis is shown (loan-level tape or audited statements).

**No REDs on the disclosed facts.**

## 6. Missing Disclosures
Per `01` (hard money essentials) — mostly satisfied; still absent:
- Fund-level leverage (and whether the 9% net is levered)
- Complete fee schedule: performance fee/hurdle, servicing, admin
- Sponsor identity and history through a downturn (stats given, sponsor not)
- Fund term, lock-up, and redemption mechanics
- GP co-investment
- Foreclosure/workout process description (recovery is stated; the *process* isn't)
- Distribution schedule (monthly income? quarterly?)

## 7. GP Alignment
- **Co-invest:** Not stated — ask (Q-GP-01).
- **Track record:** The 3.1%/92% through-cycle disclosure is exactly what `03` says a good debt-fund record looks like 🟢 — but it's self-reported and the sponsor is unnamed here; verification is the remaining step, not skepticism of the shape.
- **Fee alignment:** Step-down signals investor-period discipline 🟢; performance-fee structure unknown.

## 8. Questions for the GP
**Must-ask**
1. **Fund leverage** — "What is the fund's leverage ratio, and is the 9% net levered or unlevered?" *Bad answer:* won't disclose; a levered figure presented as if unlevered. (`CREDIT-01` mechanism)
2. **Q-FEE-01** — Complete fee schedule: performance fee and hurdle, servicing, admin; where do late fees and default interest go? *Bad answer:* "standard fees"; default interest routed to a GP "workout fee." (`GEN-16`)
3. **Q-RISK-05** (verification form) — "What's the basis for the 3.1%/92% — loan-level tape, audited?" *Bad answer:* can't produce the underlying data. (`HML-03`/`HML-04`)
4. **Q-GP-01** — GP capital in the fund, same terms. *Bad answer:* "sweat equity." (`GEN-01`)

**Nice-to-ask**
- **Q-LIQ-01** — Redemption/early-exit mechanics and lock-up.
- **Q-DIST-01** — Distribution frequency and history of paying it.
- Workout process: who runs foreclosures, in-house or counsel, and average timeline (`HML-04` context).
- Origination points and whether pricing has held as competition for deal flow increased (`02`: low origination = yield give-up).

## 9. Diligence Checklist
- [ ] Identify sponsor; background/regulatory search (`GEN-02` unprobed)
- [ ] Audited fund financials — verify default/recovery history
- [ ] Sample loan tape: grade mix, as-is LTVs, seasoning
- [ ] Fund docs: leverage authority, fee schedule, redemption terms
- [ ] Legal: fund structure, LP recognition rights on default

## 10. Verdict
**Pursue.** The fund's disclosure pattern is the inverse of the category's usual failure mode — it leads with as-is LTV, pairs default with recovery through the stress years, and shows geographic spread and a fee step-down. The 9% net clears both the HYG comparator (+400bps) and the duration-matched Treasury floor (+529bps) against a ~300–400bps hurdle. Remaining conditions are ordinary diligence, not deal problems: verify the loss history, pin down fund leverage and the full fee schedule, and identify the sponsor. A bad answer on leverage (levered net presented as unlevered) is the one response that would flip this toward Pass. Suits an income-focused LP wanting senior-secured yield with modest upside; not for an LP seeking equity-style appreciation.
