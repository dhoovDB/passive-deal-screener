# Eval fixture 13 — Diversified BDC-style private credit fund (clean case)

*Iteration-1 run, 2026-07-03, against SKILL.md @ cddc52d. Fixture prompt: evals.json id 13.*

---

**Verdict: Pursue.** This fund discloses the exact items that decide a levered credit vehicle — leverage ratio within the standard band, levered *and* unlevered net IRR side by side, through-cycle default and recovery, 400+ loan diversification, and a fee structure with a hurdle and high-water mark. It answers Q-RISK-06's good-answer signal verbatim before being asked. Remaining questions are calibration (the actual numbers behind the disclosed categories), not structure.

## 1. Deal Snapshot
- **Asset class:** Private credit 🟢
- **Deal type:** Debt fund, BDC-style, levered 🟢
- **Sponsor:** Not named in summary
- **Book:** 400+ loans, diversified across sectors 🟢
- **Leverage:** ~1.1x, clearly disclosed 🟢
- **Claimed return:** Net IRR stated on a levered basis **with the unlevered figure also shown** 🟢 (values not quoted in summary — request)
- **Minimum / lock-up / vehicle form (traded vs non-traded):** Not stated 🟡

## 2. Return Stress-Test
Values await the actual figures, but the structure supports an honest test:
- **Levered + unlevered both shown** 🟢 — the single most important disclosure for this deal type (`CREDIT-01`'s question, answered in the materials). The unlevered figure is the one to run against HYG (5.0% 10yr) and the 2yr Treasury floor (4.15%) per `05`; baseline (`01`): private credit nets 8–12%.
- At 1.1x, leverage amplifies modestly — inside `02`'s ≤1.5× standard band — so the levered-minus-unlevered gap should be small; a large gap would contradict the stated ratio (a consistency check worth running on the numbers).
- Swing assumptions: (1) credit cycle — through-cycle loss history is disclosed, so stress = disclosed defaults × today's book; (2) rate path — BDC yields float with base rates, so the quoted net IRR embeds today's elevated base (ask what the net looks like at −200bps base rates); (3) the leverage facility's behavior in a drawdown (mild at 1.1x).

## 3. Where LP Returns Come From
Interest income on a 400+ loan senior book, modestly levered — an income story with the leverage honestly labeled. With both bases shown, the LP can see precisely how much of the net is leverage (`GEN-07` family concern, pre-answered). The `05` caveat that applies even to clean private credit: reported marks are smoothed, so apparent low volatility understates true risk — a framing note, not a flag.

## 4. Fee Stack Summary
Per `02` (private credit inventory):

| Fee | Stated | `02` range | Read |
|---|---|---|---|
| Management | 1.5% on gross assets; 1.0% below the 200% asset-coverage threshold | 1–2% | In range; the step-down mechanism is present 🟢 |
| Incentive | Two-part, with hurdle **and high-water mark** | 10–20% over 5–7% hurdle; HWM standard | Structure matches the standard 🟢 — rate and hurdle values unstated, request |
| Leverage costs | Ratio disclosed (1.1x) | *Variable*; >1.5× flags | Within band 🟢 |

One genuine nuance to price, not a flag at this leverage: **the management fee is charged on *gross* (levered) assets**, so at 1.1x the effective fee on LP equity runs ≈2× the headline (~3.1% of NAV at full leverage). This is standard BDC construction and the asset-coverage step-down mitigates it — but the LP should know the effective-on-equity number, and note the mild structural incentive to run leverage high. Routed to §8.

## 5. Red Flags
**None RED. None YELLOW on the disclosed facts.** Checked and cleared:
- `CREDIT-01` → **defused**: 1.1x, disclosed, within `02`'s band; levered/unlevered both shown — the good-answer signal for Q-RISK-06, verbatim.
- `CREDIT-02` → **defused**: 400+ loans, diversified sectors.
- `HML-03`/`HML-04` (mechanism) → **defused**: through-cycle default *and* recovery disclosed — the pair.
- `HML-05` (mechanism) → **defused**: fee steps down (coverage-linked rather than period-linked; same LP-protective function).
- `GEN-16` → substantially defused: structure fully described; rates/values to be confirmed from documents.

Open clarifications (not flags): fee-on-gross-assets effective rate; hurdle and incentive values; the actual default/recovery figures; vehicle liquidity terms; sponsor identity.

## 6. Missing Disclosures
Calibration items only: the quoted net IRR values (levered and unlevered); incentive-fee rate and hurdle level; the disclosed default/recovery figures themselves; largest single-sector and single-borrower exposures; vehicle form (traded/non-traded) and redemption mechanics; sponsor identity and history.

## 7. GP Alignment
Structurally sound as disclosed: the high-water mark prevents carry on recouped losses, the hurdle gates the incentive fee, and the coverage-linked fee step-down ties GP economics to balance-sheet discipline. Verify: co-invest/insider ownership (unstated — ordinary ask), and whether the incentive fee has an income/capital-gains split that pays on unrealized appreciation (the two-part structure's known soft spot).

## 8. Questions for the GP
**Clarifying tier:**
1. The numbers behind the categories: net IRR (both bases), hurdle, incentive rate, default and recovery figures. (Confirmation of disclosed-as-existing items.)
2. "What is the effective management fee on LP *equity* at current leverage, and what does the two-part incentive pay on unrealized gains?" (fee-on-gross nuance, §4)
3. **Q-LIQ-01** — vehicle form and exit mechanics: traded BDC, quarterly tenders, or locked? *Bad answer:* "a liquidity event is anticipated." (the one question where a bad answer would matter here)
4. Largest sector and single-borrower exposure within the diversified book. (`CREDIT-02` verification)
5. "What does the net yield look like if base rates fall 200bps?" (floating-rate dependence)
6. **Q-GP-01** — insider/GP capital in the vehicle.

## 9. Diligence Checklist
Standard verification: offering docs vs summary (fee mechanics, coverage tests); audited financials (the disclosed loss history); portfolio schedule (sector/borrower concentrations, non-accruals); sponsor background; if non-traded, tender history through 2022–23.

## 10. Verdict
**Pursue.** The fund pre-answers the category's defining questions — leverage labeled and modest, both return bases shown, losses disclosed through the cycle, granular diversification, and incentive mechanics with the standard LP protections. The screen's residual work is numeric confirmation and one real economic nuance (the effective fee on equity from gross-asset charging). Biggest swing factor: liquidity terms — a clean fund with no exit mechanics still locks the LP, and that answer (Q-LIQ-01) sets the illiquidity premium the net IRR must clear. Suits an income-focused LP comfortable with credit beta at modest leverage; it is the credit-side proof that "screens clean" is an achievable bar, not a theoretical one.
