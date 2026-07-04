# Iteration-3 Scorecard — passive-deal-screener eval run

<!-- Finalized 2026-07-04. Grades are the independent grader's verbatim; orchestrator additions are this comment and the Method chain section. -->

## Method chain (orchestrator note)
Same role separation as iteration 2: blind fresh-context generator (SKILL.md + references + prompts only; discipline confirmed; both scripts executed) → independent fresh-context grader (IDs verified against `03`/`04`; no anchoring — forbidden from reading iterations 1–2) → orchestrator spot-verification (fixture 8 GEN-09: 1 citation; fixture 1 Q-FEE-04: 1 citation + merits-PwC verdict quoted; fixture 4 HML-05: 0 citations, confirming the single note; fixture 12: Pursue). No grades altered.

**Gate disposition:** cycle-3 exit criterion was "13/13 strict, or divergences accepted in the decision log." Result: 12 PASS + 1 PASS w/ notes, zero FAILs. The single divergence (fixture 4's HML-05 uncited when the fixture discloses zero fees — step-down absence subsumed by GEN-16) is **accepted** in the ROADMAP decision log rather than driving a fourth cycle: on a zero-fee-disclosure deal, the specific-fee flag and the no-fee-disclosure flag genuinely collapse into one finding. **The PR gate is cleared.**

*Graded 2026-07-04 by independent grader. Reports: `evals/iteration-3/*.md` (13). Criteria: scratchpad `expected/01.md`–`13.md` (2026-07-04 revision). Flag/question IDs verified against `references/03-red-flag-library.md` and `references/04-question-bank.md`. Iteration-1/2 materials not consulted.*

## Headline

**12 PASS / 1 PASS w/ notes / 0 FAIL**

## Results table

| Id | Fixture | Classification | Target flags | Questions | Missing-data fires | Verdict match | Grade |
|---|---|---|---|---|---|---|---|
| 01 | Multifamily value-add memo | ✓ MF value-add equity syndication; VNQ + NPI overlay | ✓ EQUITY-06, GEN-08, GEN-05 fired RED; EQUITY-01 probed per its clawback conditional (see notes) | ✓ Q-DS-01, Q-EXIT-01, Q-FEE-03, Q-FEE-04, Q-GP-02 all present | ✓ GEN-01→Q-GP-01, GEN-10→Q-RISK-02, GEN-11→Q-DIST-01 | ✓ Pursue-with-conditions (merits verdict, residuals as conditions) | **PASS** |
| 02 | Pref-equity email (sparse) | ✓ Preferred equity from 3 sentences | ✓ GEN-03, GEN-15, GEN-16, GEN-17 | ✓ Q-FEE-01, Q-FEE-04, Q-LIQ-01 | ✓ Output is ~all missing-disclosures→must-asks; no fabricated terms | ✓ Pass as presented — insufficient disclosure + re-screen list | **PASS** |
| 03 | Hard-money sound | ✓ HML debt; HYG + duration-matched Treasury | ✓ HML-01/02/03/04/05 all affirmatively CLEARED, none manufactured | ✓ Q-FEE-01, Q-RISK-05/06, Q-GP-01/02, Q-LIQ-01 | ✓ Residuals (leverage, perf fee, co-invest) routed to asks | ✓ Pursue-with-conditions; conditions are verification-grade residuals; differs from id 4 | **PASS** |
| 04 | Hard-money problematic | ✓ HML debt (fix-and-flip) | ✓ HML-01 (RED, ARV-presumed), HML-02, HML-03, HML-04, GEN-16, GEN-14-pattern on "never had a loss"; ✗ HML-05 never cited by ID | ✓ Q-RISK-04, Q-RISK-05 lead as must-asks | ✓ As-is LTV, default, recovery all fire → must-asks | ✓ Pass (insufficient-disclosure formula; essentials substantially absent); differs from id 3 | **PASS w/ notes** |
| 05 | Private credit 2.5x levered | ✓ Private credit; HYG + 2yr Treasury (4.15%) | ✓ CREDIT-01 RED (levered-figure demand explicit), CREDIT-02, GEN-16 (hurdle/HWM absent) | ✓ Q-RISK-06 first must-ask; Q-FEE-01, Q-RISK-05 | ✓ Hurdle, recovery, levered-vs-unlevered basis all routed | ✓ Pass — merits verdict, structure named as the problem | **PASS** |
| 06 | Development first-timer | ✓ Development equity; 25% vs 18–22% target, premium discounted | ✓ GEN-13, GEN-08 (by construction), EQUITY-06, GEN-07 cluster named, dev+CM fee stacking per 02, first-timer as GEN-14-as-applied | ✓ Q-DS-03, Q-DS-01 | ✓ All five 01 dev essentials named absent, routed | ✓ Pass family ("Pass as presented — insufficient disclosure" + full adverse-merits case; expected allows Pass) | **PASS** |
| 07 | Office 2026 | ✓ Variable class; category baseline REFUSED, deal's own underwriting is the benchmark | ✓ GEN-19 RED (fires on omission), GEN-17, GEN-09 RED with Q-RISK-01 probe per proactive trigger | ✓ Q-MKT-02 is must-ask #1 | ✓ Physical occupancy + sublease overhang fire → Q-MKT-02; "no comparator" stated | ✓ Pass as presented — insufficient disclosure (expected allows) | **PASS** |
| 08 | Packed flags | ✓ MF equity syndication | ✓ GEN-01, GEN-02, EQUITY-01, EQUITY-02, GEN-10, GEN-14 all RED; 50% promote vs >30% threshold explicit; GEN-13; GEN-09 probed by ID via Q-RISK-01 (self-check requirement met) | ✓ Q-GP-01/02/03, Q-FEE-03, Q-RISK-02 | ✓ Pref, fees, financials routed | ✓ Pass, explicitly a merits verdict, not softened; Nightingale (co-invest/alignment) + Applesway (cap-expiry) structures both named in substance | **PASS** |
| 09 | Teaser, no disclosures | ✓ MF fund teaser | ✓ GEN-15/16/17 fired; GEN-14/GEN-05 explicitly held unresolved → Q-GP-02 | ✓ Q-GP-02, Q-FEE-01 in omnibus must-ask list | ✓ Output is ~80% withheld-information; missing-data IS the report | ✓ Pass as presented — insufficient disclosure + re-screen list; no confident verdict | **PASS** |
| 10 | J-curve Deal A | ✓ MF equity; Year-1 distributions noted as low J-curve risk, capital amortizes | ✓ GEN-08 and GEN-11 affirmatively NOT fired on disclosed shape; no timing flag manufactured | ✓ Q-DIST-01 (distribution-source probe), Q-DS-01 | ✓ Fees/financials/sponsor absences routed | ✓ (No expected verdict enumerated) Lower-risk half correctly characterized | **PASS** |
| 11 | J-curve Deal B | ✓ MF equity, same 14% headline | ✓ GEN-08 RED at 100% (maximum); GEN-11 used as analytical frame with disclosure-met mechanism note; Q-DIST-01 correctly omitted (conditional — schedule disclosed) | ✓ Q-DS-01, Q-EXIT-01, Q-FEE-04 (pref accrual in back-loaded shape) | ✓ Exit-cap absence named the loudest omission | ✓ Called MATERIALLY riskier than Deal A; full A/B comparison table; "advance A, price B down" | **PASS** |
| 12 | Clean equity | ✓ MF value-add syndication | ✓ NO flag fired; GEN-01, EQUITY-01/02, EQUITY-04/05, EQUITY-06, GEN-09/10, GEN-13/15, GEN-05/14 all affirmatively cleared; all YELLOW residuals on genuinely absent items only | ✓ Clarifying must-asks (target return, Q-MKT-01, Q-DIST-01, Q-FEE-02) | ✓ Residual gaps listed, none manufactured | ✓ Pursue; residuals as conditions | **PASS** |
| 13 | Clean credit | ✓ BDC-style private credit | ✓ CREDIT-01 NOT fired on disclosed 1.1x with both IRR bases shown (the fixture's FAIL trap avoided); CREDIT-02 cleared (400+ loans); hurdle/HWM + fee tier acknowledged | ✓ Q-RISK-05/06 verification, Q-FEE-01, Q-GP-01 | ✓ Incentive rates, actual figures routed as conditions | ✓ Pursue with conditions; conditions verification-grade | **PASS** |

## Per-fixture notes (non-PASS and boundary items)

### 04 — PASS w/ notes
- **HML-05 (no management-fee step-down stated) is enumerated in expected_output and never appears in the report by ID.** The substance is partially covered — §4 fires GEN-16 on total fee non-disclosure and names the step-down as a `02` norm the fund should carry — but the report's own SKILL.md rule ("a flag subsumed by a broader finding is still cited parenthetically") demanded an explicit `(HML-05)` citation, and Q-FEE-01 as phrased in the report omits the step-down ask. All other enumerated checks satisfied; no FAIL condition (pair discrimination with id 3 holds: different verdict families). Divergence recorded per rubric.

### 01 — PASS, treatment note (not a deduction)
- Expected enumerates EQUITY-01 with its own conditional ("RED only if no clawback"). Clawback is *undisclosed*, not confirmed absent, and the 20% promote is mid-band, so the report's handling — EQUITY-02 YELLOW ("RED if confirmed absent alongside the promote"), EQUITY-01 cited by ID in §7 and in Q-FEE-03 — matches the conditional exactly. EQUITY-01 does not appear in the §5 list itself; recorded for transparency, judged conforming.

### 06 — PASS, verdict-form observation
- Expected allows "Pass / Pursue-with-conditions"; the report delivers Pass **via the insufficient-disclosure formula** while simultaneously mounting the full adverse-merits case (first-timer, EQUITY-06, GEN-08, fee stacking). Defensible — all five `01` development essentials are absent, which meets "substantially absent" — but this is the run's closest call on the recalibrated rule: a grader could argue the disclosed adverse facts alone carry a merits Pass. The hybrid framing ("and what *is* disclosed is adverse") keeps it inside expected bounds.

## Discrimination-test results — all four pass

| Test | Requirement | Result |
|---|---|---|
| id 3 vs id 4 (within-deal-type) | Different verdict families | ✓ Pursue-with-conditions (verification-grade residuals) vs Pass as presented — insufficient disclosure |
| id 10 vs id 11 (J-curve) | Identical 14% IRR treated as different risk; 11 materially riskier | ✓ 11 fires GEN-08 RED at 100%, explicit "materially riskier" framing, six-axis comparison table, "advance Deal A, price Deal B down" |
| id 12 (false-positive, equity) | No manufactured RED; no YELLOW against a disclosed fact | ✓ Zero flags fired; every clear itemized against the disclosure; residual YELLOWs only on genuine absences |
| id 13 (false-positive, credit) | Must NOT fire CREDIT-01 on disclosed 1.1x | ✓ CREDIT-01 affirmatively cleared, with the fund's pre-answered Q-RISK-06 good-answer signal recognized as such |

The id 5 / id 13 contrast is clean in both directions: CREDIT-01 RED on 2.5x undisclosed-basis leverage, cleared on 1.1x disclosed-both-bases leverage — the exact discrimination the pair exists to prove.

## Findings

### 1. Verdict-rule calibration (special attention #1) — correctly applied, boundary pair clean
- **Boundary pair:** fixture 1 (full memo, many residual gaps) received a **merits verdict** (Pursue-with-conditions) with absences converted to conditions; fixture 9 (teaser) received the **insufficient-disclosure formula** with a re-screen list. This is precisely the recalibrated rule's intent, applied at both poles.
- Formula used on 2, 4, 6, 7, 9, 10, 11 — in each, the fixture's category essentials are genuinely substantially absent. Merits verdicts on 1, 3, 5, 8, 12, 13 — in each, the core story was underwritable. **No fixture chose the wrong formula against its expected output.** Notably, fixture 5 and fixture 8 both resisted the temptation to hide behind insufficiency when the *disclosed* structure was the verdict (fixture 8 says so explicitly: "This is a merits verdict, not an insufficiency verdict").
- Watch-item: 7 of 13 verdicts use the formula. All are justified by these fixtures' thinness, but fixture 6 shows the model reaching for the formula even when it has a complete adverse-merits case in hand. If future fixtures add mid-density deals, monitor for formula over-use.

### 2. Self-check effectiveness (special attention #2) — both targeted requirements met
- **Fixture 8 / GEN-09:** probed by ID via Q-RISK-01 (§8 item 6), exactly the "cite or explicitly probe by ID" behavior demanded — and correctly probed rather than fired, since the hold is unstated (matches the SKILL.md proactive trigger).
- **Fixture 1 / Q-FEE-04:** present as must-ask #9, citing EQUITY-04/EQUITY-05, with the non-cumulative bad-answer signal. Pref-mechanics probes also appear wherever a pref is stated or structurally decisive (2, 8, 11, 12).
- **Residual self-check gaps:** (a) fixture 4's HML-05 omission shows the "every flag family touched must appear by ID" check does not reliably extend to flag families implied by an *absence* the report discusses generically (fee non-disclosure → step-down flag); (b) cosmetic: fixture 12 discusses GEN-07/GEN-08 as not-fired in §§2–3 but omits them from the §5 cleared list (the list covers all IDs the expected output enumerates, so no grade impact).

### 3. Residual expected_output defects
- **Expected 01's EQUITY-01 clause** ("deal-by-deal + promote — RED only if no clawback") is internally strained: `03` defines EQUITY-01 as deal-by-deal with *high* promote, and the fixture's 20% promote is mid-band per `02` (15–30%); with clawback merely undisclosed, neither the "high promote" nor the "no clawback" leg is established. The report's probe-not-fire treatment is more faithful to `03` than the expected text is. Suggest rewording expected 01 to "EQUITY-01/EQUITY-02 probed via Q-FEE-03, escalating to RED if clawback confirmed absent."
- **Expected 04 enumerates HML-05** on a fixture that discloses *no* fees at all. Legitimate (the flag fires on absence of a step-down), but it collides with GEN-16 subsumption in practice; either expected 04 should accept "(HML-05 subsumed under GEN-16, cited parenthetically)" or SKILL.md's parenthetical-citation rule needs to name absence-implied flags explicitly. The miss is still graded against the report (attribution: primarily report defect — the citation rule already required it).
- Expected 10 and 11 enumerate no verdicts; grading relied on risk-characterization checks only. Fine as designed, but worth stating an acceptable verdict set for 10/11 to prevent future drift.

### 4. New regressions this cycle
- **None found against the criteria.** The two recalibration-sensitive behaviors (verdict formula selection on 4/6/7/10/11; ID-citation discipline on 1/8) land on the right side in every case checked. The single divergence (04's HML-05) is an ID-coverage miss of the kind the new self-check was built to catch — i.e., a residual gap in the new mechanism, not a regression of previously-correct behavior.
