# Iteration-9 Scorecard — fixture 03 rerun

**Method.** A focused rerun, not a full cycle: fixture 03 ran once, by a blind, fresh-context generator (model: Opus) that saw an isolated copy of `SKILL.md`, `references/` and `scripts/` only, against the notice-spacing edit. Grading was done by an independent, fresh-context grader (model: Opus) that did not write the skill, the fixtures or the report, and was also asked whether the report could ship unedited as an example.

Report graded: `evals/iteration-9/03-hard-money-sound.md`. Line numbers are that file's, so the two harness header lines count as lines 1 and 2.

## Headline

- **Grade: PASS w/ notes.** Strict count: 6 of 6 criteria met (§4.1, 4.2, 4.3, 4.4, 4.6, 4.7). The notes concern example quality, not the case.
- **Verdict, exact wording:** "Pursue with conditions." (line 4 as "**Verdict: Pursue with conditions.**", line 197 as "**Pursue with conditions.**").
- **Is the verdict correct as written?** Yes. `expected_output` accepts it "where the conditions are verification-grade residuals, not deal defects". All six conditions (lines 208-213) ask for disclosure or verification, and none names a defect. The verdict does not differ from `expected_output`, so no verdict penalty applies. TESTING-PLAN §5 says "Pursue" for case 3a, but the fixture's clause governs here.
- **Contrast with id 4:** the expected id 4 verdict is Pass, so this differs. Id 4 was not rerun in iteration-9, so the pair itself is not confirmed by this run.
- **Criterion 4.7: met.** Lines 6 and 199 are each exactly `*Screening output only, not investment advice.*`, with blank lines at 5, 7, 198 and 200. It sits directly under both verdicts. The notice appears exactly twice and contains no non-ASCII characters. The only addition is the italic markup that SKILL.md itself specifies.
- **Classification and routing:** correct. Hard money / bridge debt, `02` hard money inventory, `GEN-` and `HML-` flags, HYG plus Treasury floor.
- **IDs:** all 26 flag IDs and all 22 question IDs resolve to `03` and `04`. Every question cited in §5 appears in §8.
- **Example decision: DO NOT SHIP.** This is a close call; the reasons are in the last section. Fee honesty is clean. The blockers are about discipline on assumed numbers and basis, in or near §10.

## Hidden-input check

All script figures reproduce. Runs were made with every input explicit (exit 0, no ASSUMED inputs). The second table covers figures calculated by hand, which also matter here.

### Script figures

| Figure | Line | Inputs stated | Inputs the script needed | Reproduces? | Conclusion changes at default? |
|---|---|---|---|---|---|
| Bull 10.0%: 517bps HYG, 576bps 3mo, 513bps 2yr | 37 | Net 10.0, hold 4 (line 33, tagged 🔴) | deal-type, net-irr, hold-years, all stated. Script prints 3mo only; 2yr is hand arithmetic on 4.87% (`05`) | Yes. CLEARS comfortably | No. Default hold 5 is the same band |
| Base 9.0%: 417bps, 476bps, 413bps | 38, 43, 201 | Net 9.0, hold 4 | Same | Yes. CLEARS comfortably; 417 - 400 = 17bps is right | No |
| Bear ≈7.4%: 256bps, 315bps, 252bps | 39 | 9.3% defaults, 80% recovery, hold 4 | Net is hand-derived (7.388). **Unstated: that the 9% target already nets about 25bps of losses** | Yes at 7.39. Rounded 7.4 gives 257 and 316, which the "≈" covers. THIN / FAILS | No. Taking the full 186bps off gives 7.14% and 231bps, still THIN / FAILS |
| Hurdles at 1yr and 7yr: ~200bps, ~400-600bps | 43 | Hold named in the sentence | Same | Yes. 1yr CLEARS comfortably, 7yr CLEARS (thin), matching "thin" | No |
| 7.83% floor, 117bps cushion | 46 | Bottom of band, HYG | Same | Yes. 7.83% gives exactly 300bps | No |
| 150bps stepping to 100bps | 67 | "on what is disclosed" | fund or mgmt fee 1.5 / 1.0; carry 0, admin 0, acquisition 0, disposition 0 | Yes, 150.0 and 100.0 | Default run gives 389bps, but the "on what is disclosed" scope excludes those layers. No |
| 10.5% gross gives 9.00%; 9.5% after step-down | 81 | Gross 10.5, "less 150bps" | As above; hold, hurdle and catch-up have no effect at carry 0. Zero inputs are implied by "less 150bps", not listed. SKILL.md prescribes passing 0 for undisclosed fees | Yes, 9.00 and 9.50 | Default run gives 6.61% net, but "at least 10.5%" still holds, since extra layers only raise required gross. No |
| Stress: 440bps, 230bps, about 210bps, 7.60% | 83, 132 | Gross 12, servicing 0.5, admin 0.3, carry 20, hurdle 8, **full catch-up**, hold 4 | **Unstated in the sentence:** mgmt fee 1.5 held flat for all 4 years (visible only through the 230bps; step-down not modelled); acquisition 0; disposition 0; no credit losses in the drag | Yes: 439.9, 230.0, 209.9, 7.60 | No. See below |

**Catch-up, specifically.** The only carry figure is at line 83. It says "full catch-up", which matches the script's 100 default, and line 132 lists catch-up as assumed. No `--catch-up 0` or other value is used anywhere, so there is no hidden catch-up.

Line 83's conclusion ("this full stack and a 9% net can't both be true at 12% gross") holds under each single move:

| Move | Net | Below 9%? |
|---|---|---|
| Catch-up omitted (default 100) | 7.60% | Yes |
| Catch-up 50 | 8.20% | Yes |
| Catch-up 0 | 8.79% | Yes |
| One-time fees at script default | 6.85% (515bps) | Yes |
| Mgmt fee blended at 1.25 | 7.85% | Yes |
| Mgmt fee flat at 1.0 | 8.10% | Yes |
| Hold 3 / 5 / 7 | 7.51% / 7.69% / 7.86% | Yes |
| Catch-up 0 and mgmt 1.0 together | 9.29% | **No**, but this changes a stated input as well as an unstated one |

### Hand-calculated figures

| Figure | Line | Check | Unstated or unlabelled input | Effect |
|---|---|---|---|---|
| About 25bps historical loss | 48 | 3.1 x 8% = 24.8 | Labelled "If the 3.1% is annual" | None |
| About 142bps loss budget; 17.7% and 7.1% default rates | 49, **225** | 117 + 24.8 = 141.8; /8% = 17.7; /20% = 7.09 | **Target already nets the 25bps (never stated); 3.1% is annual (line 139 open); 92% is on principal (line 55 tags this 🔴)** | Range is about 117-142bps. Cumulative over 4 years gives about 123bps; no losses in the target gives 117bps. 142 is the top of the range. "Wide margin" survives (14.6% default at 117bps) |
| About 160bps bear cost | 51 | 186 - 24.8 = 161 | Same embedded-loss input | 186bps if the target nets no losses. Direction unchanged |
| 62.6%, roughly 37% | 55 | 68 x 0.92 = 62.56; 37.44 | Labelled 🔴 in the sentence | None |
| 200-400bps gap, 50-250bps left | 82 | Correct | None | None |

**Answer to "does any sentence's conclusion change at a default?"** No. No script default changes a conclusion. The one material unstated input is outside the scripts: that the 9% target already nets about 25bps of losses.

## Notes

### Flags, verdict reasons and assumed inputs (item 5)

- **Flags:** none rests on a 🔴 input. `GEN-16`, `GEN-11`, `GEN-13` and `GEN-17` all fire on stated absences. Lines 61 and 105-115 route leverage and other assumption-dependent flags to questions instead of firing them, as SKILL.md requires.
- **Verdict and conditions:** the verdict and all six conditions (lines 208-213) rest on no 🔴 input. Line 201's "clears a 3-5 year lock-up 🟡" uses the `01` category range, and the band is the same across that range, so the 🔴 4-year point does not carry it. Fund term is listed as a condition.
- **Exception, line 225:** "credit losses stay well under about 142bps a year" sits untagged in §10, under "What would have to be true". The number needs the assumptions in the table above, including one line 55 tags 🔴, and it is the most favorable reading. It is not a flag or a listed condition, but it is the test the reader leaves with.
- **Undisclosed term shown as disclosed, line 101:** "12 states and a 15% metro cap are real diversification 🟢". The deal says "no single metro over 15%", which line 19 reports correctly. That may be a snapshot and not a limit. A "cap" is a governing term nobody stated, and it carries a green tag. Line 136 repeats it as "Metro limits". `HML-02` clears either way.
- **Fee terms:** no other undisclosed term is shown as disclosed. Carry, servicing, leverage, gross yield, term and co-invest all read "Not stated" or equivalent. Lines 26 and 139 are careful about the grade mix.

### HML flags (item 6): none manufactured

| Flag | Line | Treatment | Correct? |
|---|---|---|---|
| `HML-01` | 100 | Not fired; as-is LTV disclosed, basis question stays open | Yes. Line 54: "a question, not a defect" |
| `HML-02` | 101 | Not fired | Yes, apart from the "cap" wording |
| `HML-03` | 102 | Not fired | Yes |
| `HML-04` | 102 | Not fired | Yes. The 5%/90% comparison matches `03` |
| `HML-05` | 103 | Not fired; fee steps down | Yes |

`Q-RISK-04` and `Q-RISK-05` stay must-asks as definitional probes, which TESTING-PLAN §5 expects.

### Internal consistency (item 7)

- **The 68% / 72% quirk is handled well (line 54).** It identifies that ARV LTV should be at or below as-is on the same balance, offers funded-versus-commitment as an inference tagged 🟡, and routes it to `Q-RISK-04`. Line 55's cushion test is also sound.
- **Arithmetic:** no errors found.
- **Line 201, basis mismatch in a verdict reason:** it calls "as-is LTV of 68%" "within norm". `01` line 197 sets the norm as "65-75% on **ARV** (after-repair value, not as-is) - note the distinction". Line 29 has the same looseness. 72% on ARV is in band, but the as-is figure has no norm in the reference. This is the same distinction the report presses at line 54.
- **Line 221, a Pass trigger that contradicts the report's own test:** "A lock-up long enough that 417bps no longer clears (~400-600bps at 7-10 years)". Line 46 defines failing as falling below the bottom of the band, and 417 is above 400. The comparator returns CLEARS (thin) at 7, 10 and 30 years, and line 43 says "thin". Read that way, the trigger cannot fire at 417bps.
- **Line 37, bull label:** "Book yield at the top of the category" gives 10.0% only if it means the top of the 8-10% *net* range. Read as book yield using line 82's 13% top gross, disclosed fee and losses give about 11.25%, and line 51's "about 100bps" upside would be about 225bps. The row is tagged 🔴 and drives no decision. The qualitative point at line 51 (capped debt upside) stands.
- **Lines 59 and 112, `GEN-08`:** line 59 says it "does not fire" on the asset's structure. Line 112 lists it under "Can't fire without assuming facts". The treatment is the same, but the reasons differ.
- **Lines 87 and 97:** "none fired as a standalone flag" alongside "A YELLOW cluster counts as RED". The qualifier makes this consistent, and it follows `03`.

### Minor points, not blocking

- `CREDIT-01` is touched in §3 (line 61) but absent from §5, which misses SKILL.md's self-check literally. Line 61 explains it is outside routing.
- `Q-RISK-02` is must-ask in `04` but sits under nice-to-ask (line 178). It is reasonable because it is conditional on a floating line that may not exist, but it is not what `04` says.
- Lines 217-218 turn `02`'s "aggressive" thresholds into Pass triggers. This is analyst judgment, not a library rule.
- Line 216, "won't supply any of the above", is ambiguous between "any one" and "none".
- Line 67's 150bps assumes the fee base equals LP capital. Lines 71 and 132 say the base is not stated.

### What the report does well

§4 is a strong example of fee honesty. It leads with "not computable", limits 150bps to what is disclosed, labels the stress stack as assumed and lists it in §6. It also draws the right lesson from the stress test: the schedule will show which layers exist. Refusing to fire `GEN-07` on an assumed leverage figure is the right discipline.

## Example decision

**DO NOT SHIP.** Case grade is unaffected. The fee work and the hidden-input check both pass. Four statements fail the unedited bar, and none is a style point:

1. **Line 225 (with line 49):** the 142bps carries an unstated assumption and a 🔴-tagged assumption into §10, untagged, at the favorable end of about 117-142bps. This is the named criterion, discipline on assumed numbers.
2. **Line 201:** a verdict reason applies an ARV-basis norm to an as-is figure, against `01`'s explicit "note the distinction".
3. **Line 221:** a Pass trigger contradicts line 46's test and the comparator's output.
4. **Line 101:** a 🟢 tag covers "15% metro cap", a term the deal did not state.

**How close this is.** None of the four changes the verdict, a flag or a condition, and each is a one-sentence fix. A reasonable reviewer could accept items 3 and 4 as loose wording. Items 1 and 2 decide it: an example meant to teach tag and basis discipline should not slip on either in its verdict section.

Correcting these by hand would mean the file is no longer a blind generation. Whether to hand-edit or regenerate is the owner's decision.
