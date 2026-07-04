# Eval suite — Iteration 1 scorecard

**Run:** 2026-07-03, all 13 fixtures from `evals/evals.json`, against SKILL.md @ cddc52d (9.07KB compressed body, minimal frontmatter).
**Method:** For each fixture, only the `prompt` field was read before generating the report (blind generation); `expected_output` was read only after the report was on disk (contamination-controlled grading). Grading is per-check binary against each fixture's stated criteria, not holistic.

**Disclosed limitations (adversarial review, 2026-07-03):**
- *Same-author grading.* The SKILL.md, fixtures, reports, and grades share one author. The blind protocol controls same-session reading contamination, but the author of `evals.json` (2026-06-28) retains residual knowledge of what each fixture tests. Iteration 2 should use a fresh-context subagent as grader (grader ≠ generator).
- *Circularity weighting.* Per TESTING-PLAN, synthetics validate mechanics; externally-grounded fixtures validate real-world accuracy. The externally-grounded set here: ids 1/12 (Fundrise-patterned), 3 (Groundfloor LRO), 8 (Nightingale/Applesway failure overlays), 13 (OBDC-patterned) — see `evals/sources.md`. The remaining ids are self-authored synthetics and prove mechanics only.

**Grade rubric (defined before reading the table):**
- **PASS** — every enumerated check in the fixture's `expected_output` satisfied; no FAIL condition triggered.
- **PASS w/ notes** — all substantive checks satisfied; one or more enumerated IDs/labels missing or divergent, with the divergence recorded; no FAIL condition triggered.
- **FAIL** — a fixture-stated FAIL condition triggered, or a substantive check missed. A FAIL partially attributable to a harness defect is still recorded as FAIL, with the attribution noted.

## Results

| Id | Fixture | Classification | Target flags | Questions | Missing-data fires | Verdict match | Grade |
|---|---|---|---|---|---|---|---|
| 1 | MF value-add, full memo | ✅ | ✅ (EQUITY-01 softer, reasoned) | ⚠️ Q-EXIT-01, Q-FEE-04 not cited | ✅ | ✅ PwC | **PASS w/ gaps** |
| 2 | Pref equity, sparse email | ✅ | ⚠️ GEN-17 concept present, ID not cited | ✅ | ✅ | ⚠️ label divergence (see F1) | **PASS w/ notes** |
| 3 | HML sound (pair 3a) | ✅ | ✅ all 5 HML flags *defused*, none manufactured | ✅ | ✅ | ✅ Pursue | **PASS** |
| 4 | HML problematic (pair 3b) | ✅ | ⚠️ HML-05 subsumed under GEN-16; GEN-14 ID not cited | ✅ Q-RISK-04/05 | ✅ | ✅ Pass | **PASS w/ notes** |
| 5 | Private credit 2.5x levered | ✅ | ✅ CREDIT-01/02, GEN-16 | ✅ Q-RISK-06 | ✅ | ✅ Pass | **PASS** |
| 6 | Development first-timer | ✅ | ⚠️ GEN-07 conditional not cited (no leverage data — defensible) | ⚠️ Q-DS-01 not cited | ✅ | ✅ Pass | **PASS w/ notes** |
| 7 | Office 2026 (*variable*) | ✅ refused baseline | ✅ GEN-19/17/09 | ✅ Q-MKT-02 | ✅ | ⚠️ label divergence (see F1) | **PASS w/ note** |
| 8 | Packed flags | ✅ | ❌ GEN-09 probe missed; 🔧 EQUITY-03 = evals defect (see H1) | ✅ all 5 | ✅ | ✅ Pass, unsoftened | **FAIL** (strict: "catches some but not all"; 7/9 — one legit miss + one harness defect) |
| 9 | Teaser, near-total absence | ✅ | ✅ GEN-14/15/16/17 | ✅ | ✅ (output ≈80% absence) | ✅ "cannot screen" (rider noted, F1) | **PASS w/ note** |
| 10 | J-curve Deal A (early) | ✅ | ✅ no timing flag manufactured | ✅ | ✅ | ✅ lower-risk half | **PASS** |
| 11 | J-curve Deal B (back-loaded) | ✅ | ✅ GEN-08 @100%, GEN-11 mechanism | ✅ Q-DIST-01 | ✅ | ✅ materially riskier | **PASS** |
| 12 | Clean equity | ✅ | ✅ zero manufactured flags; all defusals recorded | ✅ clarifying tier | ✅ | ✅ Pursue | **PASS** |
| 13 | Clean credit (1.1x) | ✅ | ✅ CREDIT-01 *not* fired (FAIL condition avoided) | ✅ | ✅ | ✅ Pursue | **PASS** |

**Headline: 12/13 — 6 PASS, 6 PASS w/ notes, 1 FAIL (fixture 8, strict).** The fixture-8 FAIL decomposes into one legitimate detection miss (GEN-09 unprobed when hold is unstated → fix S3) and one harness defect (EQUITY-03 mis-mapped → fix H1); with H1 corrected, the residual gap is S3's. It is recorded as FAIL because the fixture's stated criterion triggered — the rubric does not launder harness defects into passes.

## Discrimination tests — all four passed
1. **Within-deal-type (hard money):** id 3 → Pursue vs id 4 → Pass. ✅
2. **Timing at identical IRR (J-curve):** id 10 lower-risk vs id 11 materially riskier; equal-IRR-equal-risk explicitly rejected. ✅
3. **False positives (clean deals):** ids 12/13 → Pursue with zero manufactured REDs in both branches. ✅
4. **Leverage discrimination:** id 5 (2.5x, basis hidden) fired CREDIT-01 RED vs id 13 (1.1x, both bases shown) cleared it. ✅
5. *(Variable-class)* id 7 refused a generic office baseline — the per-fixture FAIL condition avoided. ✅

## Triaged fix list for iteration 2

### S — SKILL.md fixes (behavioral, recurring)
- **S1 (top priority): verdict vocabulary lacks an insufficient-input state.** Fixtures 2, 7, 9 each improvised around it ("Pass as presented," "Cannot screen; treat as Pass") while the evals expect "Cannot-assess / PwC-pending-disclosures." Fix: add one rule to the SKILL.md verdict section — when essential disclosures are absent, the verdict is *"Pass as presented — insufficient disclosure"* with an explicit re-screen list, and it is never a confident Pursue/Pass on merits. One sentence; ends the improvisation. (Coordinate with H2.)
- **S2: ID-citation completeness.** Recurring theme (fixtures 1, 2, 4, 6): the run *describes* the right concept but skips the specific flag/question ID when a broader finding subsumes it (Q-EXIT-01/Q-FEE-04/Q-DS-01/GEN-17/HML-05/GEN-14). Fix: strengthen SKILL.md's citation instruction — every fired flag routes to its `04` question **by ID**, and subsumed flags are still cited parenthetically.
- **S3: unstated-hold debt rule.** Fixture 8: debt maturity was given, hold wasn't, and the GEN-09 probe didn't fire. Fix: SKILL.md proactive trigger — *debt maturity stated with hold unstated → probe GEN-09 via Q-RISK-01*.

### H — Harness (evals.json) fixes
- **H1: id 8 flag mis-mapping.** `expected_output` cites "EQUITY-03 (50% promote is aggressive)" — but `03` defines EQUITY-03 as *GP catch-up at 100%*, unmentioned in the prompt. Promote-size aggressiveness belongs to EQUITY-01 + `02`'s >30% threshold. Fix the expected_output text.
- **H2: verdict-vocabulary alignment.** ids 2/9 expect "Cannot-assess," which SKILL.md's three-state verdict doesn't define. Resolve via S1 (preferred), then align the two fixtures' expected wording to the S1 formula.

### Notes carried, no action
- Fixture 6's GEN-07 conditional and GEN-04-vs-GEN-14 ID choice: defensible on the facts; re-examine after S2 lands.
- Script invocations (`fee_drag_calculator.py`, `benchmark_comparator.py`) were referenced, not executed, in reports — consistent with how the skill will actually run them in-session; no fix needed.

## Iteration-2 protocol
Apply S1–S3 to SKILL.md (size gate: stays ≤10KB — S1/S3 are one line each; S2 is a phrase edit), fix H1–H2 in evals.json, then re-run all 13 fixtures blind per this method — with one upgrade from the adversarial review: **grading by a fresh-context subagent** (grader ≠ generator ≠ evals author), closing the same-author-grading limitation above. Target: 13/13 strict PASS with the notes column empty on the S-fix themes.

*PR-packaging note (Phase 4.5):* `evals/iteration-1/` (and `-2/`) are repo-local iteration logs; the upstream skill subtree convention carries `evals.json` only. Decide the PR's eval payload at packaging time — don't ship iteration transcripts upstream by default.
