# Iteration-5 Scorecard — passive-deal-screener eval run

**Method.** Each of the 13 `evals/evals.json` fixtures was screened by a blind, fresh-context generator subagent (model: Opus) against SKILL.md @ 7712624. Fixture 11 answers the second message of a conversation whose first message is fixture 10's prompt. Grading was done by an independent, fresh-context grader (model: Opus) that did not write the skill, the fixtures or the reports, and was forbidden from reading iterations 1–4, `examples/`, `README.md`, `ROADMAP.md` or git history. The grading criteria are each fixture's `expected_output` plus TESTING-PLAN §4 (the universal checks 4.1–4.4, and the conditional checks 4.5/4.6 where they apply). The grader verified every flag and question ID against `references/03` and `references/04` rather than relying on the reports' own glosses. A mechanical scan found **no nonexistent IDs** in any report. The generators had CLAUDE.md files auto-loaded into their contexts. Those files contain no expected answers.

## Headline

**11 PASS / 2 PASS w/ notes / 0 FAIL.** Discrimination **4/4**.

## Results table

| Id | Fixture | Classification | Target flags | Questions | Missing-data fires | Verdict match | Grade |
|---|---|---|---|---|---|---|---|
| 1 | MF value-add, full memo | ✓ MF value-add equity; VNQ + NPI overlay | ✓ EQUITY-06 RED, GEN-08 RED (≈73% of profit at exit), GEN-05/14 RED, EQUITY-01 YELLOW (clawback unstated); GEN-01/10/11 routed | ✓ Q-DS-01, Q-EXIT-01, Q-FEE-03/04, Q-GP-02 | ✓ §6 list; drag of 370–460 bps computed with undisclosed fees set to 0 | ✓ Pursue w/ conditions | **PASS** |
| 2 | Pref-equity email | ✓ preferred equity; PFF | ✓ GEN-15/16/17, GEN-03; PREF-01 probed | ✓ Q-FEE-01/04, Q-LIQ-01 | ✓ output is mostly §6 + must-asks | ✓ Pass as presented + re-screen list | **PASS** |
| 3 | Hard money, sound | ✓ HML debt; HYG + T-bill/2yr | ✓ HML-01–05 all cleared by ID, no RED | ✓ Q-RISK-04/05 | ✓ carry, servicing and fund leverage routed | ✓ Pursue (differs from 4) | **PASS** |
| 4 | Hard money, problematic | ✓ HML debt | ◐ HML-01 RED, HML-02, HML-03/04, GEN-14 ✓; **HML-05 cited but "Not fired"** | ✓ Q-RISK-04/05 | ✓ as-is LTV, default and recovery → must-asks | ✓ Pass (as presented) | **PASS w/ notes** |
| 5 | Private credit, 2.5x, 60% sector | ✓ private credit; HYG + 2yr | ✓ CREDIT-01 RED, CREDIT-02 (clustered to RED), GEN-16 | ✓ Q-RISK-06 | ✓ hurdle, recovery and levered basis routed | ✓ Pass (as presented) | **PASS** |
| 6 | Development, first-timer | ✓ development equity; 18–22% target, discounted | ✓ GEN-13, GEN-08 RED, EQUITY-06 RED, GEN-06 (dev + CM stacking), GEN-14 (first-timer); GEN-07 probe | ✓ Q-DS-03, Q-DS-01 | ✓ 5 development essentials listed as absent | ✓ Pass (as presented) | **PASS** |
| 7 | Office 2026 | ✓ office = variable; comparator "none - variable class" | ✓ GEN-19 RED, GEN-17, GEN-09 (provisional) | ✓ Q-MKT-02 | ✓ physical occupancy + sublease → must-asks | ✓ Pass as presented (allowed) | **PASS** |
| 8 | Packed flags | ✓ MF equity syndication | ✓ GEN-01, GEN-02, EQUITY-01+02 (50% promote > 30%), GEN-10, GEN-09, GEN-13, GEN-14 | ✓ Q-GP-01/02/03, Q-FEE-03, Q-RISK-02 | ✓ | ✓ Pass (merits, explicitly not "as presented") | **PASS w/ notes** |
| 9 | Teaser, no disclosures | ✓ MF fund, inferred 🟡 | ✓ GEN-15/16/17; GEN-14 held unverified | ✓ Q-GP-02 + full must-ask set | ✓ output is mostly what was not disclosed | ✓ Pass as presented + re-screen list | **PASS** |
| 10 | J-curve A (front-loaded) | ✓ MF equity | ✓ no timing flag; GEN-11 explicitly not fired (timing disclosed) | ✓ Q-DIST-01 | ✓ | ✓ lower-risk half; sets up the comparison | **PASS** |
| 11 | J-curve B (all at exit) + compare | ✓ MF equity | ✓ GEN-08 RED at 100% on a stated fact; GEN-11 as frame | ✓ Q-DIST-01 | ✓ | ✓ "same 14% IRR is not the same deal"; B materially riskier | **PASS** |
| 12 | Clean equity | ✓ MF value-add equity | ✓ no RED, no YELLOW on disclosed facts; clearances cited by ID | ✓ clarifiers only | ✓ target return, hold and LTV routed | ✓ Pursue | **PASS** |
| 13 | Clean private credit | ✓ BDC-style private credit | ✓ CREDIT-01 not fired (1.1x < 1.5x, both IRR bases shown); CREDIT-02 cleared; YELLOWs only on genuine absences | ✓ verification clarifiers | ✓ seniority, incentive rates routed | ✓ Pursue w/ conditions (verification-grade) | **PASS** |

## Notes

**Fixture 4: PASS w/ notes.** Every stated FAIL condition is avoided. HML-01 fires RED on the ARV trap ("Fix-and-flip is the lending type `01` says is typically quoted on ARV"; `01` confirms "Typical LTV 65–75% on **ARV**"), and the verdict differs from fixture 3. The expected output lists HML-05 among the fired flags, but the report places it under "Not fired (no 🟢/🟡 basis): … `HML-05` (fund term unknown)" and sends the step-down question to nice-to-ask. The ID is cited and routed, so this is a minor gap, not a miss. The report's reasoning is also consistent with the assumed-number anti-pattern, since `03` defines HML-05 as a missing step-down "in a long-dated fund" and the fund term is unstated.

**Fixture 8: PASS w/ notes.** All nine target flags are present with severity, both §4.5 break patterns are named (GEN-01 no co-invest; GEN-10 rate cap expiring before the 2028 maturity), and the verdict is an unsoftened Pass. Two contract deviations:
1. It fires `EQUITY-04` on an assumed fact: "**`EQUITY-04`: Pref not stated** 🔴. Treat the pref as absent until the GP shows one." That is a flag fired on a 🔴 basis, which the SKILL.md anti-pattern forbids. Fixture 9 routes the same absence to Q-FEE-04 instead.
2. It lists GEN-09 at YELLOW–RED where `03` rates it RED. The report gives a defensible reason (hold undisclosed).

Neither deviation changes the verdict.

**Minor observations on PASS fixtures (not grade-affecting).**
- Fixture 11 lists GEN-11 as a fired YELLOW even though `03` defines it on *undisclosed* timing. It does acknowledge "The *shape* is disclosed", and the expected output allows GEN-11 as a frame.
- Fixture 5 applies HML-03/04/05 to a private-credit fund. This is legitimate, because `04` marks Q-RISK-05 as "HML / credit fund".
- Fixture 6 correctly spots that 25% / 2.5x over 3 years does not reconcile: 2.5^(1/3) − 1 = 35.7%.

### Observation 1: Discrimination tests (TESTING-PLAN §6)

| Test | Result | Evidence |
|---|---|---|
| Hard-money pair 3 vs 4 | **Pass** | 3 → "Pursue", HML-01–05 cleared; 4 → "Pass as presented", HML-01 RED plus the HML-01/02/03/04 cluster. |
| J-curve pair 10 vs 11 | **Pass** | 11: "the same 14% IRR is not the same deal… Deal A is the stronger passive-LP position". GEN-08 fires on B at 100% and is withheld on A because A's shape is 🔴. |
| Clean pair 12 / 13 (both branches say "solid") | **Pass** | 12: "RED: none. YELLOW: none fired on disclosed facts" → Pursue. 13: "RED: none" → Pursue w/ conditions (verification-grade). |
| Leverage contrast 5 vs 13 | **Pass** | 5: CREDIT-01 RED, "exceeds `02`'s 1.5× threshold". 13: CREDIT-01 "Probed, not fired… ~1.1x… IRR shown levered and unlevered". |

**4/4.**

### Observation 2: Fee-input honesty

**No violations found.** Every report either passes 0 for undisclosed fees, or labels any market-typical stack as assumed and hypothetical. Examples: 02 ("It is **not** this deal's number"), 04 ("every input 🔴 ASSUMED… This is a §6 gap, not a finding"), 07 ("Illustrative only 🔴, not this deal's terms"), 08 ("all 🔴 assumed"), 09/10/11 ("ASSUMED 🔴 and a §6 gap"), 13 ("illustrative 15% incentive"). Fee *bases* that were undisclosed are also handled honestly:
- Fixture 1 runs a separate 🔴 price-basis row.
- Fixture 5 brackets equity vs gross-asset bases.
- Fixture 13's gross-assets reading is a reading of a disclosed term, tagged 🟡.

### Observation 3: Assumed-number discipline

No report's **verdict** turns on a 🔴 figure. Flags or verdict support touching assumed inputs:
- **08: flag fired on a 🔴 basis.** "`EQUITY-04`: Pref not stated 🔴. Treat the pref as absent until the GP shows one." (see Notes)
- **07: borderline.** GEN-08 fires RED as "🟡 (inferred from the thesis)" with no disclosed cash-flow/exit split: "The return is most likely exit-dependent above the 60% threshold, which fires `GEN-08`". The anti-pattern names distribution shape as a 🔴 input, and fixtures 8, 9 and 10 declined GEN-08 on the same kind of absence. The verdict rests on non-disclosure, not on this flag.
- **05: borderline.** "Roughly 3+ points of the net return come from fund-level borrowing, not lending. 🟡" This derives from a 🔴 borrowing-cost/definition illustration. CREDIT-01 itself fires on the stated 2.5x, so nothing hinges on it.
- **08: supporting color only.** Verdict reasoning cites "At about 6% the deal fails the illiquidity hurdle", which comes from an all-🔴 fee stack. The verdict explicitly "rests on the disclosed terms" (five stated REDs).
- **01: inference, not assumption.** GEN-09 RED is tagged 🟡 from the `01` bridge-term norm (6–18 mo), because maturity is not stated. The GEN-08 73% is sound arithmetic on stated IRR / multiple / hold.

### Observation 4: Verdict calibration

**8 of 13** verdicts use "Pass as presented — insufficient disclosure": 02, 04, 05, 06, 07, 09, 10, 11.

| Id | Judgment |
|---|---|
| 02 | **Correct.** Three sentences; nothing but a coupon disclosed. |
| 04 | **Correct.** None of the debt-fund core (as-is LTV, loss history, fees) is disclosed. The expected merits "Pass" was also supportable. |
| 05 | **Over-fired (mild).** The report's own words are "The two facts you were given are both warnings". Stated 2.5x > 1.5x is a RED that no missing disclosure can clear, so a merits Pass was available. |
| 06 | **Formula met by the letter** (0 of 5 development essentials), but the report concedes "The facts that *are* stated already lean Pass on the merits". A merits Pass was equally supportable. Borderline. |
| 07 | **Correct.** The office essentials (physical occupancy, sublease, submarket, debt terms, fees) are absent, and the expected output allows it. |
| 09 | **Correct.** Teaser only; required by the expected output. |
| 10 | **Correct.** A one-line deal: IRR plus distribution shape only. |
| 11 | **Correct.** A one-line deal. The report argues well that for a 100%-exit deal the missing exit inputs *are* the core story. |

Fixture 8 correctly chose a merits Pass, and 1, 12 and 13 correctly chose merits verdicts despite residual gaps. Fixture 12 gave Pursue with no target return stated.

### Observation 5: Variable-class discipline (fixture 7)

**Compliant.** "No category comparator applies… `benchmark_comparator.py --deal-type office` returned 'none - variable class'". The only figures shown are labeled "Reference points (context, not a 'clears' test)":
- the Treasury floor
- the NPI unlevered overlay, including office NPI at 3.4%

There is no office IRR range and no analog "clears" table.

## Gate

The TESTING-PLAN §8 exit bar is met. There are **0 FAIL** across all 13 fixtures (11 cases), this is the fifth iteration cycle (≥2 required), and the iteration logs are retained. The two PASS-w/-notes items are both minor:
- 04: HML-05 was routed rather than fired.
- 08: EQUITY-04 was fired on a 🔴 basis.

The one calibration issue worth tightening is fixture 05's "insufficient disclosure" label, which over-fired on a deal with a stated disqualifying RED.
