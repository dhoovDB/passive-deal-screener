# Iteration-6 Scorecard — passive-deal-screener eval run

**Method.** Each of the 13 `evals/evals.json` fixtures was screened by a blind, fresh-context generator subagent (model: Opus) against SKILL.md @ 436a76b, the text that shipped upstream apart from line endings. Generators saw an isolated copy of `SKILL.md`, `references/` and `scripts/` only. Fixture 11 answers the second message of a conversation whose first message is fixture 10's prompt. Grading was done by an independent, fresh-context grader (model: Opus) that did not write the skill, the fixtures or the reports. This cycle adds criterion 4.7, the not-investment-advice line. The trigger check (TESTING-PLAN section 7, step 5) is not part of this scorecard.

Graded against SKILL.md @ 436a76b. Not read, as instructed: iteration-1 to iteration-5, examples/, README.md, ROADMAP.md, git history.

## Headline

- **PASS: 6** (02, 03, 07, 08, 10, 12)
- **PASS w/ notes: 6** (01, 04, 05, 06, 11, 13)
- **FAIL: 1** (09, criterion 4.7)
- **Discrimination: 4/4**
- **Gate: NOT met** (section 8 requires 0 FAIL)

**Grading rule used.** A fixture is FAIL only if a section 8 criterion does not hold (4.1-4.4, 4.7, or conditional 4.5/4.6) or an explicit FAIL clause fires in the fixture or in TESTING-PLAN section 6. Any other departure from `expected_output`, including a verdict mismatch with no FAIL clause attached, is PASS w/ notes.

**Checks run independently of the reports.**
- All flag and question IDs in all 13 reports were checked by script against the 34 flags in `03` and 25 questions in `04`: 0 invalid.
- Script re-runs match the reports: fixture 01 464 / 369 bps, 12 395.5 bps, 08 647 bps, 13 489 bps, 03 417 bps over HYG, office returns "none - variable class".

## Results table

| Id | Fixture | Classification | Target flags | Questions | Missing-data fires | Notice 4.7 | Verdict match | Grade |
|---|---|---|---|---|---|---|---|---|
| 01 | Multifamily value-add | OK | All surfaced; EQUITY-01 correctly not RED | All | Yes | OK, both | **No**: Pass vs expected Pursue-with-conditions | PASS w/ notes |
| 02 | Pref equity email | OK | All | All | Yes, dominant | OK, both | Yes: Pass as presented | PASS |
| 03 | Hard money, sound | OK | HML-01 to 05 all clear | All | Yes | OK, both | Yes: Pursue | PASS |
| 04 | Hard money, problematic | OK | HML-01 to 04 fired; **HML-05 routed, not fired** | All | Yes | OK, both | Yes, softly: Pass as presented vs Pass | PASS w/ notes |
| 05 | Private credit, concentrated | OK | All | All | Yes | OK, both | Yes: Pursue with conditions | PASS w/ notes |
| 06 | Development, first-timer | OK | All | All | Yes | **Deviates at both** | Yes: Pass as presented (Pass family) | PASS w/ notes |
| 07 | Office 2026 | OK, variable | All | All | Yes | OK, both | Yes: Pass as presented | PASS |
| 08 | Packed flags | OK | All nine | All | Yes | OK, both | Yes: Pass, merits | PASS |
| 09 | Teaser | OK | All; GEN-14 fired | All | Yes, dominant | **Not met** | Yes: Pass as presented | **FAIL** |
| 10 | J-curve A | OK | No major timing flag, as expected | All | Yes | OK, both | None specified; Pass as presented | PASS |
| 11 | J-curve B | OK | GEN-08 RED; GEN-11 frame | Q-DIST-01 present | Yes | OK, both | None specified; B shown riskier, conclusion hedged | PASS w/ notes |
| 12 | Clean equity | OK | No RED; one genuine YELLOW | Clarifiers | Yes | OK, both | Yes: Pursue | PASS |
| 13 | Clean credit | OK | CREDIT-01 not fired; step-down read differently | Clarifiers | Yes | OK, both | Yes: Pursue with conditions | PASS w/ notes |

## Notes

### 09 — FAIL (4.7)

The required sentence appears once, at line 211, and sits under no verdict.
- **Top verdict (line 6):** line 8 is a paraphrase, not the required sentence: "*Not investment advice. This screens a deal for further diligence...*"
- **Section 10:** the verdict is at line 205. The sentence is alone on line 211, but the Reasoning and Biggest swing factor paragraphs sit between them, so it is not directly under.

No occurrence in the report meets 4.7, and the lead verdict has no verbatim line at all.

**The root cause is in SKILL.md, not the generator.** 09 followed the contract's literal words twice:
- SKILL.md lines 13-15 say "Every report repeats this line directly under the Verdict", where "this line" is the longer blockquote. Report line 8 is close to that blockquote.
- SKILL.md schema item 10 orders the verdict section as "reasoning visible, biggest swing factor named, followed on its own line by" the sentence. Report lines 205-211 follow that order exactly.

Both instructions conflict with TESTING-PLAN 4.7. Everything else in 09 meets its fixture.

Secondary point: the fixture asks for roughly 80% "what was not disclosed". §2 and §4 use real space on conditional cases, so the report falls somewhat short of that share. All of it is labeled and does not drive the verdict. This alone would not have changed the grade.

### 06 — PASS w/ notes (4.7 and calibration)

**4.7: met in substance, not to the letter.**
- **Top (line 6):** the exact sentence sits directly under the verdict, italicized and opening its own paragraph, but two more sentences follow on the same line.
- **Section 10:** the sentence is alone on line 258, but 13 lines below the verdict at line 245, after Reasoning and Biggest swing factor. This again matches SKILL.md item 10's order.

Why this is not a FAIL when 09 is: 06 places the exact sentence directly under a verdict and only adds surplus disclaimer text after it. 09 places it directly under neither verdict.

**Calibration:** see Observation 4. The insufficient-disclosure label is borderline here.

Positive: it caught that 25% IRR, 2.5x and 3 years cannot all hold. I re-derived its figures (35.7%, 1.95x, 4.1 years) and they are correct.

### 01 — PASS w/ notes (largest judgment call among the non-FAILs)

**Verdict mismatch.** The fixture says "Verdict: Pursue-with-conditions" with no alternative, and TESTING-PLAN section 5 repeats it, while other fixtures list alternates when they accept them. The report says "**Pass.**" and "This is a merits verdict". Section 6's FAIL conditions for this case (missing the exit-cap sensitivity, or no drag figure) do not fire, and the verdict is not one of the section 8 criteria, so under the rule above this is not a FAIL. The reopen list works much like a conditions list, but the label is still wrong against the fixture.

**Two inputs push the verdict harsher:**
- `GEN-09` is fired RED while the same row says "Maturity is undisclosed". `GEN-10`, equally undisclosed, is correctly left open. Section 4.4 routes absences to questions, and the expected output lists no GEN-09.
- Verdict reason 2, "At a flat cap, even with no debt, net is 9.7–11.7%", holds only if 16% is gross, which the report's own snapshot says is "Not stated". See Observation 3.

Everything else is strong: fee drag matches the script, and exit dependence is derived correctly from the stated pair (I re-derived 5.35% a year, 1.73x at sale, 82.5% of present value).

### 04 — PASS w/ notes

- **HML-05:** the fixture says "Flags... HML-05". The report lists it under "Probed, not fired (undisclosed is not the same as adverse)" and adds the step-down question to Q-FEE-01. Surfaced by ID and routed, but no severity is assigned. Defensible: no fee or fund term is stated, and HML-05 is defined as no step-down, not as non-disclosure.
- **Verdict:** "Pass as presented" rather than "Pass", with "This is a disclosure call, not a judgment that the fund is bad." It remains a Pass and differs from 03, so it counts.

### 05 — PASS w/ notes

All targets are met. The SKILL.md routing table gives private credit `GEN-` and `CREDIT-` only, but the report fires `HML-03`, `HML-04` and `HML-05`.
- HML-03/04 are explained ("Applies through `Q-RISK-05`"), and that question is labeled for HML and credit funds.
- HML-05 is fired YELLOW with no off-route label. `02` supports the point for private credit, but the flag ID is off-route, and 04 and 13 hold the same flag open.

### 11 — PASS w/ notes

The FAIL clause (equal IRR treated as equal risk) does not fire. GEN-08 fires on B only, and B is quantified as worse: fully at risk until sale, and −0.8% against 1.6–6.3% if exit equity falls 50%.

But the fixture says it "Must call this MATERIALLY RISKIER", and no sentence does so plainly. The closing is hedged: "That is the real case for Deal B", "Deal A's advantage is conditional". The closest direct statements are "the deals don't" match and "screen Deal A first".

### 13 — PASS w/ notes

The fixture says "Fee step-down and hurdle/high-water-mark present". The report lists "Time-based step-down | Not stated" and holds `HML-05` open, treating the 1.0% coverage tier as a leverage tier. It is arguably the better reading and nothing is fired on it, so 4.6 holds. It still differs from the fixture's premise, so the fixture or the report needs a ruling. The report's gross-asset fee finding (about 3.1% of NAV against the 2% line) is explicitly reported as no flag, which is correct.

### Minor observations (no grade effect)

- **GEN-14 on silence is inconsistent.** Fired RED in 02, 04 and 09; held open in 03, 05, 07, 10, 11 and 13. Each fixture accepts its result, but the same facts get different treatment.
- **GEN-09 on an unstated input.** 07 and 08 fire it provisionally with the hold unstated. SKILL.md's trigger says "probe". Both are tagged 🟡 and route to Q-RISK-01, and both fixtures expect the flag.
- **08 and criterion 4.5.** Rate cap and missing clawback are named directly. Zero co-invest is fired (the fixture's mapping for that pattern), but "misappropriation-enabling control" is only touched by "is that person still in control?" and GP removal rights in §9.
- **03.** The "Fired by" column lists flags that did not fire. GEN-16 sits under YELLOW against the library's YELLOW–RED; the report says so and explains why.
- **03 fixture quirk.** 68% as-is below 72% ARV implies as-is value above ARV. The report caught this and routed it without firing a flag.
- **05 and 13.** Both move Q-RISK-02 to nice-to-ask (05 also Q-DS-01), though the bank rates them must-ask. Neither is a target question.
- **TESTING-PLAN section 5 vs fixtures.** Case 7 lists EQUITY-03 and case 2 lists PREF-01 and EQUITY-04, which the fixtures do not require. Graded to the fixtures, as instructed. 08 and 02 route these by ID.
- **Positive:** 02 caught the wire-before-documents sequence as an unlisted risk and treated the instructions as data.

## Observations

### 1. Discrimination tests: 4/4

| Test | Result | Evidence |
|---|---|---|
| Hard money, 03 vs 04 | **Pass** | 03 "Pursue", RED none, HML-01 to 05 all cleared. 04 "Pass as presented", HML-01 RED, HML-03/04 treated as RED, HML-02 YELLOW. |
| J-curve, 10 vs 11 | **Pass** | 10: GEN-11 "Partly answered, in the deal's favor", GEN-08 not fired. 11: GEN-08 RED on B only ("100%"). Risk is quantified as different despite equal IRR. Wording is hedged (see note on 11). Both carry the same verdict label, which the fixtures do not prohibit. |
| Clean pair, 12 and 13 positive | **Pass** | 12 "Pursue", 13 "Pursue with conditions"; "RED: none" in each. All YELLOWs rest on genuine absences. |
| Leverage, 05 vs 13 | **Pass** | 05: CREDIT-01 RED at ~2.5x, above the 1.5x line. 13: "Checked and did not fire" at 1.1x with both IRR bases described. |

### 2. Fee-input honesty: no violation

No report presents an undisclosed fee as a disclosed term. All 13 separate the two, and undisclosed fees passed as 0 are called out (for example 04: "an artifact of having no inputs"; 07: "not an estimate").

Closest cases, none a breach:
- **01:** the lead 464 bps includes an assumed 100% catch-up and fee bases read as equity. The text states both, but the figure carries 🟡 rather than 🔴.
- **09:** the quick-take bullet "a typical fee stack puts you near 10–11% net" has no tag where it appears; §4 tags it 🔴.
- **12:** the lead 395 bps depends on an illustrative gross. It is tagged 🔴 and the disclosed 179–190 bps is broken out.

### 3. Assumed-number discipline: no flag fires on a 🔴 input; one verdict leg leans on an under-tagged assumption

- **08, EQUITY-04: not fired, correct.** Listed as unresolved, "If the pref is absent, `EQUITY-04` fires", and routed to Q-FEE-04. The 8% pref in §4 is assumed and labeled, and no flag rests on it. The fired flags all rest on stated terms. EQUITY-02 fires on the stated "no clawback", and the report tags its single-asset path 🔴 separately.
- **04, HML-05: routed, not fired** (see note). No assumption is involved. HML-01 fires on 🟡, inferring ARV from fix-and-flip lending and the `01` norm, which the fixture expects.
- **01, EQUITY-01: correct against `03`.** Listed as "not fired": "20% is not high by `02`" and "`03` makes this RED only with a high promote and no clawback." That matches the `03` note and the >30% threshold, and the fixture's "RED only if no clawback". Clawback is undisclosed, so it routes to Q-FEE-03 with EQUITY-02.
- **01, the one real concern.** The report says its reasoning uses "stated and inferred facts only", but reason 2 needs 16% read as gross, a term the report marks not stated. If 16% is net, the flat-cap figure lands around 14%, inside the 12–15% realized band, and that reason falls away. The other three reasons survive, so the verdict does not turn on it alone, but this should have been a 🔴 condition. The report does name it second in "Biggest swing factor". GEN-07 and GEN-09 fire at 🟡 with leverage and maturity unknown, while 09, 10 and 11 hold GEN-07 open on similar leverage silence. 01 is distinguished by its stated exit-cap compression; `03` supports naming the family when GEN-08 and EQUITY-06 fire.
- **Elsewhere: clean.** 02, 03, 05, 06, 09, 10, 11, 12 and 13 label assumed cases as illustrative, and I found no flag or verdict in them that depends on one. Small exception: 10's verdict conditions say "the 7-year base case at 9.71% is already thin" without repeating the 🔴 tag.

### 4. Verdict calibration: "Pass as presented - insufficient disclosure"

Used in 7 of 13. Correct: 6. Over-fired: 0. Borderline: 1.

| Id | Judgment | Why |
|---|---|---|
| 02 | Correct | Three sentences; the fixture names this verdict. |
| 04 | Correct | Three of five essentials absent and LTV has no basis. The fixture says "Pass"; the label is softer but the rule supports it. |
| 06 | **Borderline** | 0 of 5 essentials meets the rule. But the report says "More disclosure alone is not enough" and "this remains a Pass on the merits", and 08 refuses the label for that same reason. A merits Pass would have been more coherent. |
| 07 | Correct | No hold, leverage, fees or market; the fixture accepts it. |
| 09 | Correct | The fixture requires it. |
| 10 | Correct | One sentence; no fees, debt, hold or basis. |
| 11 | Correct, both deals | Same thin input; B's GEN-08 is kept visible. |

The label was also correctly withheld where it would have over-fired: 08 gives an explicit merits Pass with its reason, and 01, 03, 05, 12 and 13 state or show why they get merits verdicts.

### 5. Variable-class discipline, fixture 07: pass

- **No office IRR range is applied.** The report says "Office is a *variable* class" and there is "no 'clears the lock-up' result". The only other use of "clears" in the report is about the GEN-09 flag clearing, not a return comparison. The script confirms "none - variable class".
- **Analog context is present, and permitted.** The report places 18% against the value-add (14–18%) and development (18–22%) target ranges, labeled "not a hurdle". `05` and the script's own guidance both direct use of the "closest stable analog", and SKILL.md bans only an analog "clears" table. The fixture's FAIL clause does not fire.
- **The analysis runs on the deal's own terms:** "What 18% requires" as implied multiples by hold, and the 2028 maturity logic.

## Gate

**TESTING-PLAN section 8 bar: NOT met.** 12 of 13 fixtures (10 of 11 cases) pass; fixture 09 (case 8) fails 4.7. The cycle-count requirement looks satisfied by the existence of iteration-1 to iteration-6, though I did not read earlier cycles.

**The result depends on how strictly 4.7 and the verdict are read:**

| Reading | FAILs | Fixtures |
|---|---|---|
| Absence only (the literal "FAIL if it is missing") | 0 | none |
| **This scorecard** | **1** | 09 |
| Strict placement at every verdict, plus verdict as a hard requirement | 3 | 01, 06, 09 |

**Blocking item:** SKILL.md's notice instructions conflict with 4.7 in two places (lines 13-15 and schema item 10), and two of 13 reports diverged in the ways that text invites. Nothing has been fixed, per instructions.

**Owner decisions:**
1. Whether fixture 01 should accept a merits Pass, or whether the report's verdict is the defect.
2. Whether fixture 13's "fee step-down present" should count the coverage tier as a step-down.
