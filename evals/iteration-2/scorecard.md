# Eval suite — Iteration 2 scorecard (independent grader)

<!-- Finalized 2026-07-04. Grades below are the independent grader's verbatim; orchestrator additions are this comment block and the Method chain section. -->

## Method chain (orchestrator note)
Iteration 2 closed the same-author-grading limitation disclosed in iteration 1:
- **Generator:** fresh-context subagent — read only SKILL.md + references + the 13 prompts; blind discipline confirmed in its report (never read evals.json, iteration-1/, TESTING-PLAN, sources.md, or expected outputs). Ran both scripts for fee-drag figures.
- **Grader:** a second fresh-context subagent — grades assigned against expected_outputs with IDs verified against 03/04 definitions; instructed not to anchor on iteration-1 grades.
- **Orchestrator (evals author):** applied S1–S3/H1–H2 fixes pre-run, spot-verified both FAIL claims post-run (fixture 1: Q-FEE-04 zero citations + the S1-formula verdict quoted; fixture 8: GEN-09 zero citations vs fixture 7's two), and did not alter any grade.


**Run:** 2026-07-04, all 13 fixtures, reports at `evals/iteration-2/`, against SKILL.md post S1–S3 fixes.
**Grader:** fresh-context subagent, grader ≠ generator ≠ evals author. Grades assigned per-check and binary against each fixture's expected_output; flag/question IDs verified against `references/03-red-flag-library.md` and `references/04-question-bank.md` definitions, not against the reports' own claims. Iteration-1 scorecard used for format only, not anchoring.

**Grade rubric (binding, defined before grading):**
- **PASS** — every enumerated check in the fixture's expected_output satisfied; no FAIL condition triggered.
- **PASS w/ notes** — all substantive checks satisfied; one or more enumerated IDs/labels missing or divergent, divergence recorded; no FAIL condition triggered.
- **FAIL** — a fixture-stated FAIL condition triggered, or a substantive check missed. A FAIL partially attributable to a defect in the expected_output is still FAIL, with attribution noted.

## Results

| Id | Fixture | Classification | Target flags | Questions | Missing-data fires | Verdict match | Grade |
|---|---|---|---|---|---|---|---|
| 1 | MF value-add, full memo | ✅ | ✅ EQUITY-06/GEN-08/GEN-05/EQUITY-01 all handled per criteria | ⚠️ Q-FEE-04 not cited | ✅ | ❌ **S1 over-fire**: "Pass as presented — insufficient disclosure" vs expected Pursue-with-conditions | **FAIL** |
| 2 | Pref equity, sparse email | ✅ | ✅ GEN-03/15/16/17 all cited by ID | ✅ Q-FEE-01/04, Q-LIQ-01 | ✅ prominent | ✅ exact S1 formula + re-screen list; no fabrication | **PASS** |
| 3 | HML sound (pair 3a) | ✅ | ✅ all 5 HML flags affirmatively cleared, none manufactured | ✅ | ✅ | ⚠️ "Pursue with conditions" vs expected "Pursue" (same family; pair discrimination intact) | **PASS w/ notes** |
| 4 | HML problematic (pair 3b) | ✅ | ✅ HML-01 RED, HML-02/03/04/05 all by ID; "never had a loss" = GEN-14 pattern, unverified | ✅ Q-RISK-04/05 as must-asks 1–2 | ✅ | ✅ Pass-family; different verdict from id 3 | **PASS** |
| 5 | Private credit 2.5x levered | ✅ | ✅ CREDIT-01 RED, CREDIT-02, GEN-16 | ✅ Q-RISK-06 must-ask #1 | ✅ hurdle/recovery/basis routed | ✅ Pass-family (expected allows Pass) | **PASS** |
| 6 | Development first-timer | ✅ vs 18–22% target, premium discounted | ⚠️ first-timer gap via GEN-14 mechanism, not GEN-04 (expected's GEN-04 mapping is itself wrong — see D2); GEN-07 probe cited this time | ⚠️ Q-DS-01 cited in §3/§5 routing but not elevated to §8 list; Q-DS-03 ✅ | ✅ | ✅ Pass-family | **PASS w/ notes** |
| 7 | Office 2026 (*variable*) | ✅ refused category baseline explicitly | ✅ GEN-19 RED, GEN-17, GEN-09 probe (S3 trigger fired by ID) | ✅ Q-MKT-02 must-ask #1 | ✅ physical occ + sublease routed | ✅ (either acceptable form; exact S1 formula used) | **PASS** |
| 8 | Packed flags | ✅ | ❌ **GEN-09 not listed**: maturity risk analyzed in §2 and Q-RISK-01 asked, but the ID never fired/probed — "catches some but not all" triggered. GEN-01/02, EQUITY-01/02 + 50%>30% threshold, GEN-10, GEN-13, GEN-14 all ✅ | ✅ Q-GP-01/02/03, Q-FEE-03, Q-RISK-02 all present | ✅ | ✅ Pass, explicitly unsoftened ("merits pass") | **FAIL** (fixture-stated condition; 8/9 flags — one ID citation miss) |
| 9 | Teaser, near-total absence | ✅ | ⚠️ GEN-15/16/17 ✅; GEN-14 declared "unassessable" rather than fired (see D3 — expected's mapping is loose; absence still routed to Q-GP-02 must-ask) | ✅ | ✅ (~80% absence output) | ✅ exact S1 formula + re-screen list | **PASS w/ notes** |
| 10 | J-curve Deal A (early) | ✅ | ✅ no timing flag manufactured; GEN-11 explicitly not fired | ✅ | ✅ | ✅ lower-risk half stated; (no verdict enumerated in criteria) | **PASS** |
| 11 | J-curve Deal B (back-loaded) | ✅ | ⚠️ GEN-08 fired RED @100% (correct per 03); GEN-11 cited as mechanism/frame but deliberately *not fired* because timing is disclosed — diverges from expected's enumerated "flags GEN-11" (see D1) | ⚠️ Q-DIST-01 not cited (moot per D1, but enumerated) | ✅ | ✅ "MATERIALLY riskier" delivered emphatically; equal-IRR-equal-risk rejected | **PASS w/ notes** |
| 12 | Clean equity | ✅ | ✅ zero manufactured REDs; full clear-list recorded by ID | ✅ clarifying/verification tier | ✅ | ⚠️ "Pursue with conditions" vs "Pursue"; ⚠️ 5 YELLOWs vs expected "at most 1–2" (each tied to a genuine absence in the paste — see D4) | **PASS w/ notes** |
| 13 | Clean credit (1.1x) | ✅ | ✅ CREDIT-01 affirmatively cleared (FAIL condition avoided); CREDIT-02 clear; HWM/hurdle acknowledged | ✅ | ✅ | ⚠️ "Pursue with conditions" vs expected "Pursue" (same family; id 5 contrast intact) | **PASS w/ notes** |

**Headline: 11/13 — 5 PASS, 6 PASS w/ notes, 2 FAIL (fixtures 1 and 8).**

## Per-fixture notes (non-PASS only)

**1 — FAIL (S1 over-fire; check e).** Every flag/routing check lands (EQUITY-06 RED, GEN-05 RED, GEN-08 suspected-and-demanded, EQUITY-01 correctly held at YELLOW-probe because clawback is undisclosed, fee drag computed at 464bps via the script method). But the expected verdict is a merits **Pursue-with-conditions** and the report returns *"Pass as presented — insufficient disclosure"*, reasoning that T-12/rent roll/debt terms/track-record basis are absent essentials. This is the amended S1 rule displacing a merits verdict on the suite's designated happy-path memo — the exact over-application the rule needed calibration against. Secondary: **Q-FEE-04 not cited** anywhere (8% pref's cumulative/compounding status never probed) — an enumerated-question miss that would alone have capped this at PASS w/ notes.

**3 — PASS w/ notes.** Verdict label "Pursue with conditions" where expected enumerates "Pursue". Same family, discrimination vs id 4 preserved, and the conditions (undisclosed carry, term, co-invest) are real. Recorded as a label divergence, not a substantive miss.

**6 — PASS w/ notes.** (a) The first-time-sponsor gap is flagged RED via "GEN-14 (mechanism)" rather than expected's "GEN-04 / track-record" — but 03 defines GEN-04 as *rapid AUM growth without team scale-up*, which does not describe a first-timer; the report's choice is the better-grounded one (defect D2). (b) Q-DS-01 is cited twice with routing (§3, §5 GEN-08 → Q-DS-01) but never surfaces in the §8 question list; substance covered by Q-EXIT-01/Q-DS-03, placement divergence recorded.

**8 — FAIL (fixture-stated condition).** "Must list ALL flags" + "FAIL if it catches some but not all." **GEN-09 is never cited**: the 2028 maturity is stress-tested in §2, the hold is inferred as running ≥2 more years, and Q-RISK-01 is must-ask #7 — the S3 behavior half-landed (question asked, flag not fired/probed by ID), even though the report itself fired the GEN-09 probe correctly on fixture 7. All other eight enumerated elements are present with severity, the 50%-promote>30%-threshold is handled inside EQUITY-01 exactly as the corrected expected demands, and the verdict is an unsoftened merits Pass. One legit citation miss; no harness defect this time — the residual is the skill's. Quality note (ungraded): the verdict header says the cap expires "~2 years before loan maturity" while §1 says cap dies in ~12 months (≈mid-2027) against a 2028 maturity — a ~0.5–1.5yr gap; internal arithmetic inconsistency.

**9 — PASS w/ notes.** GEN-14 is listed as "unassessable (sponsor unnamed)" rather than fired. Per 03, GEN-14 = *unrealized-only track record (no realized exits cited)* — it presupposes a track-record claim, and the teaser makes none; the report routes the absence to §6 + Q-GP-02 must-ask instead. Divergence from the enumerated ID recorded; mapping defect D3 noted against the expected.

**11 — PASS w/ notes.** The substantive discrimination check is delivered hard (comparison table, "strictly riskier," equal-IRR≠equal-risk named as the principle). Divergences: (a) expected enumerates "flags GEN-11", but 03 defines GEN-11 as *cash-flow timing / J-curve **not disclosed*** — Deal B disclosed its timing, so the report fires **GEN-08 RED** (the correct ID for disclosed 100% exit-dependence, which the expected omits entirely) and cites GEN-11 only as the analytical frame; (b) Q-DIST-01 (the GEN-11 response question — "what is the distribution schedule?") is not cited, defensibly moot since the schedule is disclosed as zero-until-Y5. Both divergences trace to expected-output defect D1.

**12 — PASS w/ notes.** Zero manufactured REDs (the FAIL condition and the pair-4 discrimination check both clear), full clear-list by ID, Pursue-family verdict. Divergences: (a) 5 YELLOWs vs expected's "at most 1–2" cap — but each is a probe on a genuinely absent item in the paste (distribution schedule, catch-up rate, affiliates, submarket data, target/hold/raise), none manufactured (see D4); (b) "Pursue with conditions" vs "Pursue / looks solid" — conditions are verification-grade, consistent with "minor clarifying must-asks only" in spirit.

**13 — PASS w/ notes.** CREDIT-01 affirmatively cleared with the Q-RISK-06 good-answer signal named — the FAIL condition and discrimination test pass cleanly. Divergence: "Pursue with conditions" vs enumerated "Pursue" (same family). The gross-assets fee-base YELLOW is an honest analytic finding scored without inventing a 03 ID — not a manufactured flag.

## Discrimination tests

1. **Within-deal-type (hard money):** id 3 → Pursue-with-conditions (Pursue-family) vs id 4 → Pass as presented (Pass-family). Different verdicts. ✅
2. **Timing at identical IRR (J-curve):** id 10 lower-risk half; id 11 "materially/strictly riskier" with an explicit A-vs-B table and equal-IRR-equal-risk rejected by name. ✅
3. **False positives (clean deals):** id 12 zero manufactured REDs; id 13 zero REDs. Both Pursue-family. ✅
4. **Leverage discrimination:** id 5 fired CREDIT-01 RED (2.5x, basis hidden) vs id 13 cleared it (1.1x, both bases shown) — the pair-defining check, and id 13 explicitly contrasts fixture 05 in its own §2. ✅
5. **(Variable class):** id 7 refused the office category baseline; the fixture's FAIL condition avoided. ✅

All five discrimination tests passed.

## Findings for the skill author

### F1 — S1 over-fire (the special-attention item): confirmed once, and the rider is becoming the default verdict
"Pass as presented — insufficient disclosure" appears in **9 of 13 verdicts** (ids 1, 2, 4, 5, 6, 7, 9, 10, 11). It contradicts the expected verdict only on **fixture 1** (expected merits Pursue-with-conditions → graded FAIL, S1 over-fire). Everywhere else the expected verdict is Pass-family, silent, or explicitly permits the formula. But the pattern is clear: as worded ("Essential disclosures absent (`01`)? Then it's Pass as presented…"), the rule triggers on *any* missing essential, so any fixture that omits a T-12 — i.e., nearly every synthetic — funnels into the same verdict, and on the happy-path memo it displaced a merits call the deal's substantive disclosure had earned. **Suggested calibration:** add a materiality threshold — e.g., *"…when essential disclosures are **substantially** absent; if the deal discloses enough to underwrite the core return story, give the merits verdict and route the residual absences to conditions."* Fixture 1 vs fixture 9 is the boundary pair the wording should be tested against.

### F2 — ID-citation completeness (S2/S3 residual): the question fires, the flag ID still drops
Fixture 8's FAIL is the sharpest case: Q-RISK-01 asked, maturity risk stress-tested, GEN-09 never cited — while the same run cited the GEN-09 probe correctly on fixture 7. Same species: Q-FEE-04 dropped on fixture 1 (pref mechanics never probed despite an 8% pref front-and-center); Q-DS-01 routed but not listed in §8 on fixture 6; Q-DIST-01 absent on fixture 11 (defensibly moot). The S2/S3 fixes moved behavior (fixture 6's GEN-07 conditional and Q-DS-03 now cited; fixture 7's GEN-09 probe fires) but citation completeness is still the top recurring miss category. Possible fix: a closing self-check line in SKILL.md — *"before emitting, verify every flag family touched in §§2–3 appears by ID in §5 and every enumerated pref/waterfall term has its Q-FEE probe."*

### F3 — Verdict softening to "Pursue with conditions" where the expected says "Pursue" (ids 3, 12, 13)
Consistent one-notch softening on all three clean/sound deals. Arguably correct LP behavior (each had real undisclosed items: carry, catch-up, actual return figures), so this may be an evals-side fix: either accept Pursue-with-conditions on ids 3/12/13, or state in the fixtures that residual verification items do not demote a Pursue.

### D — Defects found in the expected_outputs themselves
- **D1 (id 11):** expected enumerates **GEN-11** for *disclosed* back-loading, but 03 defines GEN-11 as timing **not disclosed**; the correct ID for disclosed 100% exit-dependence is **GEN-08**, which the expected never mentions. Q-DIST-01 inherits the same mis-mapping (the schedule *is* disclosed). Same species as iteration-1's H1. Fix the expected to enumerate GEN-08 (+ optional GEN-11-as-mechanism).
- **D2 (id 6):** expected's "(GEN-04 / track-record)" — GEN-04 is *rapid AUM growth without team scale-up*, not first-time-sponsor risk; no 03 ID covers first-timers directly. The report's GEN-14-mechanism choice is better grounded. Reword the expected to "GEN-14-mechanism / track-record gap".
- **D3 (id 9):** expected fires GEN-14 for a *wholly absent* track record, but GEN-14 presupposes an unrealized record being *cited*. "Unassessable + routed to Q-GP-02" is a faithful reading of 03. Loosen the expected to "GEN-14 fired or explicitly held unassessable with the absence routed."
- **D4 (id 12):** "at most 1–2 YELLOW" conflicts with the fixture's own paste, which genuinely omits ≥5 items (distribution schedule, catch-up, affiliates, submarket data, target/hold). A run that probes real absences with YELLOWs will exceed the cap while doing exactly what the skill demands. Either trim the paste's omissions or raise the cap / restrict it to *non-probe* YELLOWs.
- **D5 (id 1, coordination with S1):** the fixture expects a merits Pursue-with-conditions while its prompt (per the report's reading) omits T-12/rent roll/debt terms — items `01` lists as essentials — so the S1 rule *as written* mandates the verdict the fixture forbids. The FAIL stands on the rubric, but resolving it requires either the F1 wording fix in SKILL.md or adding the essentials to the fixture prompt; doing neither leaves fixture 1 unpassable.

### Quality note (ungraded)
Fixture 8's internal cap-gap arithmetic is inconsistent (header "~2 years" vs §1's ~0.5–1.5yr implied gap). No graded check touches it, but it is the kind of slip an LP reader would catch.
