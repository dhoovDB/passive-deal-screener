# Eval fixture 03 — Senior-secured bridge loan fund (well-disclosed)
*Iteration-2 run, 2026-07-04, blind generation by fresh-context agent, against SKILL.md (post S1–S3 fixes).*

**Verdict: Pursue with conditions — every category-essential disclosure is present and in-range (as-is LTV, default *and* recovery through 2020 and 2022–23, geographic mix, fee step-down), and the 9% net target clears the HYG-plus-illiquidity hurdle; the conditions are the incentive-fee/carry layer, fund term and redemption mechanics, and GP co-investment, none of which are stated.**

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Hard money / bridge loans (senior secured) 🟢 |
| Deal type | Debt fund 🟢 |
| Sponsor | **Not stated** |
| Geography | Diversified, 12 states, no single metro >15% 🟢 |
| Minimum investment | **Not stated** |
| Hold / fund term | **Not stated** (category norm: 6–18mo loans, 3–5yr fund commitment, `01`) |
| Raise / fund size | **Not stated** |
| Claimed return | 9% **net** to LPs 🟢 |
| Portfolio LTV | 68% as-is / 72% ARV 🟢 |
| Credit history | 3.1% default rate, 92% realized recovery, incl. 2020 and 2022–23 🟢 |
| Management fee | 1.5%, stepping down to 1.0% post-investment-period 🟢 |

Routing: `01` hard money baseline (8–10% net; 65–75% LTV typical); `02` hard money / bridge fee inventory; `03` `GEN-`, `HML-`; `05` HYG + duration-matched Treasury.

## 2. Return Stress-Test

Swing assumptions: **(a) default frequency in a downturn** (3.1% historical is the base, not the ceiling), **(b) recovery rate under stress** (92% assumes workouts keep clearing at near-par; a housing-price drop compresses this first), **(c) redeployment yield** (short-duration loans reprice the book fast — good when rates rise, a drag when they fall).

- **Base:** 9% net as targeted — consistent with the `01` category norm of 8–10% net (11–13% gross common) 🟢.
- **Bull:** elevated rates persist and origination stays disciplined → top of the 8–10% band.
- **Bear:** defaults at 2–3x historical (say 6–9%) with recovery slipping to 75–80% on an as-is-value decline → the 68% as-is LTV cushion absorbs most of it; net likely degrades to mid-single digits rather than principal impairment 🟡 (that resilience is precisely what as-is-basis lending buys — contrast `HML-01` deals).

**Benchmark (`05`):** 9% net vs HYG 5.0% (10yr) = **+400bps** — inside the 300–500bps band the spread table says hard money should pay, and it clears the ~300–400bps hurdle for a 3–5yr fund commitment. Duration-matched Treasury lens: 9% over the 3mo–2yr bill (3.71–4.15%) ≈ **+485–530bps** of credit + illiquidity spread 🟢. Clears — and unlike equity deals, no leverage story is needed to get there (no fund-level leverage is claimed; confirm none exists).

## 3. Where LP Returns Come From

Contractual interest + origination points on a short-duration senior-secured book — **cash-flow-driven, not exit-driven**. No terminal-value assumption, no cap-rate bet, no refi dependence: `GEN-07`/`GEN-08` do not apply. The return's integrity rests on credit selection and workout competence, both of which this fund actually discloses evidence for (grade mix, default + recovery history). Rules 3–4: no exit- or leverage-driven return to flag.

## 4. Fee Stack Summary

| Fee | Stated | `02` range | Read |
|---|---|---|---|
| Fund management | 1.5% → 1.0% step-down | 1–2% AUM; absence of step-down is a flag in long-dated funds | In range, **with** the step-down — LP-favorable 🟢 (`HML-05` clear) |
| Performance fee / carry | **Not stated** | 10–20% over 5–8% hurdle; >25% or no-hurdle aggressive | Undisclosed — either none exists or it's not been told to you 🟡 |
| Servicing fee | **Not stated** | 0.25–0.5% of loan balance | Undisclosed 🟡 |
| Origination points (borrower-paid) | **Not stated** | 1–3 points; <1 is a flag (yield too low) | Ask — it's the book's yield engine |
| Late fees / default interest | **Not stated** | Should flow to the fund, not the GP | Verify no GP "workout fee" siphon |

**Gross-to-net drag:** the 9% is quoted **net**, which is the right basis (skepticism rule 2 satisfied). Against the 11–13% gross norm (`01`), the implied total drag is ≈200–400bps, of which only 100–150bps (management fee) is accounted for by disclosure. **The residual — carry, servicing, admin — is not computable from this disclosure, and that gap is the §5/§8 finding (`GEN-16` partial).**

## 5. Red Flags

The category's defining flags are affirmatively **clear**, which is worth stating: `HML-01` clear (LTV on as-is *and* ARV, 68/72%, inside the 65–75% norm); `HML-02` clear (12 states, no metro >15%); `HML-03`/`HML-04` clear (default *and* recovery disclosed, through the 2020 and 2022–23 stress windows — exactly what `Q-RISK-05` demands); `HML-05` clear (step-down present).

**YELLOW**
- `GEN-16` (partial) — the fee stack below the management fee is undisclosed (carry? servicing? admin?); undisclosed fees are still paid → `Q-FEE-01`.
- `GEN-11` — a net target with no distribution schedule or redemption/lock-up terms; for a debt fund this is the liquidity gate, not a J-curve, but the LP still can't see when cash comes back → `Q-DIST-01`, `Q-LIQ-01`.
- `GEN-01` (probe) — GP co-investment not stated; zero would be RED → `Q-GP-01`.

No RED flags fire on the disclosed facts 🟢.

## 6. Missing Disclosures

The `01` hard-money essentials are all present (as-is + ARV LTV, default history, recovery, geographic mix, downturn history). Remaining gaps against the `02` and general baselines:
- Performance fee / hurdle structure — or an explicit statement that there is none.
- Servicing and admin fees.
- Fund term, investment period length, redemption/withdrawal mechanics, lock-up.
- Fund-level leverage: none is mentioned — confirm the fund is unlevered (a levered book would change the whole risk read).
- Sponsor identity, team, and AUM; GP co-investment.
- Loan count / average loan size; the actual grade-mix table (referenced as disclosed, not shown here).
- Whether default interest and late fees accrue to the fund or the GP.

## 7. GP Alignment

- **Co-investment:** not stated → `Q-GP-01`.
- **Track record:** the credit stats (3.1% default / 92% recovery through two stress windows) are the *right kind* of disclosure and are realized figures 🟢 — but they are self-reported until verified (audit, loan tape) 🟡. Fund-level realized net-to-LP returns across prior vintages: not stated → `Q-GP-02`.
- **Fee alignment:** the step-down is an LP-favorable, ILPA-consistent structure (`02`) 🟢. Whether carry exists — and whether default interest flows to LPs or the GP — determines the rest.
- **Affiliates:** servicing/origination affiliates undisclosed → `Q-FEE-02`.

## 8. Questions for the GP

**Must-ask**
1. `Q-FEE-01` — Complete fee schedule: is there a performance fee, at what rate over what hurdle, plus servicing/admin? *Bad answer:* "standard market fees"; fees surface only in the PPM after commitment.
2. `Q-RISK-05` — Provide the loan-level default/recovery data behind the 3.1%/92%, including workout timelines. *Bad answer:* the aggregate stat can't be broken down; recovery excludes legal costs and accrued interest. *(Disclosed at the summary level — verify at the loan level.)*
3. `Q-GP-01` — GP capital in the fund, same terms as LPs? *Bad answer:* "our sweat equity is our investment"; token amount.
4. `Q-GP-02` — Realized net-to-LP returns on prior fund vintages. *Bad answer:* gross portfolio yield offered instead of LP net; can't separate realized from marks.
5. `Q-LIQ-01` — Lock-up, redemption gates, and exit options before fund end. *Bad answer:* "we'll try to accommodate"; no defined mechanics.
6. `Q-DIST-01` — Distribution schedule: monthly/quarterly income? reinvestment option? *Bad answer:* no defined schedule.
7. `Q-RISK-06`-style confirmation — Is there any fund-level leverage (credit line, note program), and is the 9% net on a levered or unlevered basis? *Bad answer:* a warehouse line exists but "doesn't really count." *(Asked proactively; `CREDIT-01` mechanism applies to any levered debt fund.)*
8. `Q-GP-03` — Any regulatory action or investor litigation? *Bad answer:* "nothing material."

**Nice-to-ask:** average origination points and whether <1pt loans are being written to win flow (`02` — low origination is a yield flag); `Q-GP-04` (underwriting headcount vs book growth); `Q-LIQ-02` (K-1 timing); do late fees/default interest accrue to the fund?

## 9. Diligence Checklist

- PPM and LPA: fee schedule, carry, redemption terms, leverage authority.
- Audited financials for prior vintages; verify the default/recovery stats against the audit or a sample loan tape.
- Background/regulatory search on sponsor and principals.
- Sample third-party appraisals or BPOs behind "as-is" values — the 68% is only as good as the valuations under it.
- Servicing and foreclosure process review: who forecloses, in which states, average timeline.
- Confirm custody/administration: independent fund administrator, not GP-prepared statements.

## 10. Verdict

**Pursue with conditions.** This is what good debt-fund disclosure looks like against the `01`/`03` baselines: LTV on the honest basis, both halves of the credit history through the stress years, real diversification, and a fee step-down. The 9% net clears HYG by ~400bps and the duration-matched Treasury by ~500bps — paid for credit risk and illiquidity, with no leverage story required. Biggest swing factor: **recovery rate in a falling as-is-value market** — the 92% is the number to verify hardest.

**Conditions:** (1) full fee schedule including any carry — the gross-to-net residual is currently unexplained; (2) fund term, lock-up, and redemption mechanics in writing; (3) GP co-investment confirmed in cash; (4) loan-tape / audit verification of the default and recovery stats; (5) written confirmation of no fund-level leverage. **Who it suits:** an income-oriented LP wanting senior-secured, short-duration yield uncorrelated to an exit market, who can tolerate a 3–5yr commitment. **What would have to be true:** the verified numbers match the marketed ones — nothing in the structure needs to change.
