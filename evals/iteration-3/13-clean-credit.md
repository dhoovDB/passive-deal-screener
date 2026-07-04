# Eval fixture 13 — Diversified BDC-style private credit fund (clean)
*Iteration-3 run, 2026-07-04, blind generation by fresh-context agent, against SKILL.md (post S1b/S2b fixes).*

**Verdict: Pursue with conditions — the structure passes every debt-fund screen (leverage 1.1x and disclosed, 400+ loans across sectors, through-cycle default and recovery shown, levered *and* unlevered IRR both stated); the conditions are the actual numbers (net IRR figures, hurdle/incentive rates) and the fee base — 1.5% on *gross assets* is a larger effective charge on LP equity than the headline suggests.**

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Private credit (senior secured, BDC-style) 🟢 |
| Deal type | Debt fund 🟢 |
| Sponsor | Not stated by name ("large, diversified") 🟡 |
| Geography | Not stated (implicitly broad) |
| Minimum investment | Not stated |
| Hold / fund term | Not stated (`01` norm: 3–7 yrs) |
| Raise / fund size | Not stated ("large") |
| Claimed return | Net IRR stated on a levered basis **with the unlevered figure also shown** — actual numbers not included in this summary 🟡 |
| Leverage | ~1.1x, clearly disclosed 🟢 |
| Portfolio | 400+ loans, diversified across sectors 🟢 |
| Credit history | Through-cycle default and recovery rates disclosed 🟢 |
| Fees | 1.5% mgmt on gross assets (1.0% below the 200% asset-coverage threshold); two-part incentive with hurdle + high-water mark 🟢 |

## 2. Return Stress-Test

Swing assumptions: **credit-cycle default wave**, **recovery realization**, **leverage cost vs portfolio yield spread**.

- **Base.** The `01` private-credit band is 8–12% net. The fund's own figures aren't in this summary — obtaining them is condition #1 — but the structure (1.1x leverage on senior-secured loans) is consistent with the band rather than dependent on exceeding it 🟡.
- **Bear.** Per `01`, recoveries run ~60–80% with wide dispersion. At 1.1x leverage the amplification is modest: a stress-case 6% default year at 65% recovery ≈ 210bps portfolio loss ≈ ~440bps against equity with leverage and financing cost 🟡 — painful, not structural impairment. Contrast the same arithmetic at 2.5x. The disclosed through-cycle default/recovery history makes this stress testable against the fund's own record rather than category priors — exactly what `01` asks for.
- **Benchmark (`05`, benchmark_comparator, `01`-band midpoint 10% and 5-yr term assumed 🔴):** 10% vs HYG 5.0% = ≈500bps vs a ~300–400bps hurdle → clears; **≈585bps over the 2yr Treasury (4.15%)** — a real credit + illiquidity spread. At the band's 8% floor the premium is ≈300bps — thin end of the hurdle; the fund's actual net decides which end of that range it lives at. `05`'s smoothed-marks caveat applies: private-credit NAV volatility understates true risk — don't credit "low vol" claims.

## 3. Where LP Returns Come From

Contractual loan interest across 400+ positions, modestly amplified at 1.1x — an income story. The financing-story concern (CREDIT-01/GEN-07 family) is affirmatively addressed rather than merely absent: leverage is below the `02` 1.5x threshold, disclosed, *and* the fund shows the unlevered figure alongside the levered one — the `04` good-answer signal for Q-RISK-06, provided pre-emptively 🟢. Verify the levered-minus-unlevered gap is modest (it should be roughly (portfolio yield − financing cost) × 0.1× leverage); a large gap means the leverage is doing more work than 1.1x implies.

## 4. Fee Stack Summary (`02`)

| Fee | Deal | `02` norm | Read |
|---|---|---|---|
| Management fee | 1.5% **of gross assets** (1.0% below the 200% coverage threshold) | 1–2% of committed/invested capital | Headline in range — **but the base differs** (below) 🟡 |
| Incentive fee | Two-part, hurdle + high-water mark | 10–20% over 5–7% hurdle; HWM standard | Structure conforms; **rates not stated** 🟡 |
| Hurdle type | Not stated (soft w/ catch-up vs hard) | Hard hurdle more LP-favorable; soft w/ 100% catch-up aggressive | Ask (Q-FEE-01) |
| Servicing / admin | Not stated | 0.25–0.5% / $1–3k per LP | Confirm |

**The fee-base catch 🟡:** at ~1.1x leverage, gross assets ≈ 2.1× equity, so 1.5% of gross assets ≈ **~3.15% of LP equity** — past the `02` >2% aggressive threshold *when restated on the equity base the `02` norm uses*. This is standard BDC convention, and the 1.0% tier below the coverage threshold plus the leverage cap bound it — but it also means the manager is paid more for levering up, a mild structural tilt. **Total drag not computable without the incentive rates and servicing/admin — the restated fee base is the finding to price, not a disqualifier.**

## 5. Red Flags (`03`)

**None fire on what is disclosed.** The debt-fund screens are affirmatively cleared:
- **CREDIT-01** — no: leverage ~1.1x (< the `02` 1.5x line), disclosed, with levered vs unlevered IRR both shown 🟢
- **CREDIT-02** — no: 400+ loans, diversified across sectors 🟢
- **HML-03/HML-04 (analogs)** — no: through-cycle default *and* recovery disclosed 🟢
- **GEN-14/GEN-05 (as presented)** — through-cycle disclosure implies a seasoned record; realized net-to-LP by vintage still to verify 🟡

**Residual (unresolved, not fired):**
- Management fee restated on equity ≈3.15% (`02` threshold flag by base-conversion; BDC-conventional — price it, question it) 🟡
- **GEN-16 (partial)** — incentive-fee rates, hurdle level, catch-up structure, servicing/admin not in the summary
- **GEN-11** — distribution schedule not stated
- **GEN-01 (unresolved)** — GP/manager co-investment not stated
- Income-incentive-fee mechanics: confirm whether the income incentive has a *total-return* lookback — without one, the manager can earn income fees while NAV declines (the known BDC structure gap; the HWM may cover only the capital-gains part) 🟡

## 6. Missing Disclosures (`01` private-credit essentials + `02`)

`01` essentials largely present (loan count ✓ 400+, sector mix ✓ diversified, leverage ✓ 1.1x, seniority ✓ senior secured, default/recovery ✓ through-cycle). Residual:
- The actual net IRR figures (levered and unlevered) and the actual default/recovery numbers — the summary says they're disclosed; this screen needs the values
- Incentive-fee rates, hurdle level, catch-up, total-return lookback
- Average loan size; single-largest-sector and single-name concentrations (diversified ≠ quantified)
- Fund term, capital-call and distribution schedule, redemption/liquidity terms
- Manager identity, AUM, co-invest; financing-facility terms (cost, covenants)

## 7. GP Alignment

Structurally sound, personally unverified 🟡: the disclosure posture is itself an alignment signal — leverage, both IRR bases, and through-cycle loss data offered up-front is the behavior of a manager comfortable with scrutiny (the anti-GEN-03 profile). The step-down fee tier below the coverage threshold is LP-protective. Open: manager co-invest (GEN-01 — ask), whether the incentive fee has the total-return lookback, and affiliate arrangements (GEN-06 — e.g., an affiliated administrator or origination platform charging the fund).

## 8. Questions for the GP (`04`)

**Must-ask**
1. The numbers behind the labels: actual levered and unlevered net IRR, and actual through-cycle default/recovery rates with workout timelines (**Q-RISK-05**, HML-03/HML-04 analogs; **Q-RISK-06**, CREDIT-01 — the fund has pre-answered the structure; now verify the values). *Bad answer:* the figures underwhelm the structure — e.g., unlevered yield barely above HYG.
2. **Q-FEE-01** (GEN-16) — complete schedule: incentive rates, hurdle, catch-up, servicing/admin; and confirm the management-fee base (gross assets vs net). *Bad answer:* "standard BDC terms" without the numbers.
3. Does the income incentive fee carry a total-return lookback (or does the HWM apply only to capital gains)? *Bad answer:* income fees are payable in quarters where NAV declined.
4. **CREDIT-02 quantification** — single-largest sector and single-name exposure caps. *Bad answer:* "diversified" with no numbers.
5. **Q-GP-01** (GEN-01) — manager/insider capital in the fund. *Bad answer:* none beyond fee income.
6. **Q-LIQ-01** — redemption/liquidity terms; if non-traded, the path to liquidity and any gates. *Bad answer:* "a liquidity event is anticipated."
7. **Q-DIST-01** (GEN-11) — distribution schedule, and whether distributions have ever included return of capital presented as yield. *Bad answer:* ROC-funded distributions unacknowledged.

**Nice-to-ask**
8. **Q-FEE-02** (GEN-06) — affiliated service providers and their pricing. 9. **Q-GP-03** (GEN-02) — regulatory history. 10. Financing facility terms: cost, maturity, mark-to-market/margin provisions. 11. **Q-GP-04** (GEN-04) — origination team scale vs AUM growth.

## 9. Diligence Checklist

- Offering documents/prospectus: fee mechanics (base, lookback), leverage limits, redemption terms
- Audited financials: verify NAV, non-accruals, realized loss history vs the stated default/recovery figures
- If BDC-registered: SEC filings (10-K/10-Q, N-2) — pull non-accrual and PIK-income trends independently
- Manager background: SEC/FINRA, Form ADV, litigation
- Facility documents: covenant and coverage-trigger review

## 10. Verdict

**Pursue with conditions.** Enough is disclosed to underwrite the core return story, and the story is the right kind: diversified senior-secured income at modest, honestly-presented leverage, from a manager whose disclosure behavior pre-answers this skill's hardest debt-fund questions (CREDIT-01, CREDIT-02, HML-03/04 analogs all cleared). No flag fires. The residual absences are genuinely conditions: (1) the actual net IRR values — the structure only earns its keep if the unlevered yield clears HYG (5.0%) plus a real spread and the levered net lands mid-band or better (8% would be thin against the ~300–400bps hurdle; §2); (2) incentive-fee rates and a total-return lookback confirmed; (3) the effective ~3.15%-of-equity management-fee base priced consciously; (4) liquidity terms in writing. Biggest swing factor: the credit cycle — a seasoned through-cycle loss record at 1.1x leverage is the best available insulation, which is what this fund claims; verify it. Suits an income-oriented LP allocating to diversified credit as a category; what must be true: the disclosed numbers survive the audit trail, and the LP accepts smoothed-mark illiquidity for a ~300–600bps spread over the liquid alternative.
