# Iteration 7 — scorecard

**Method.** Each of the 13 `evals/evals.json` fixtures was screened by a blind, fresh-context generator subagent (model: Opus) against SKILL.md @ 181fdd7, which applies the notice-wording fix from cycle 6. Fixture 01 ran three times, each by a new agent, to test whether cycle 6's verdict flip repeats, so the cycle has 15 reports. Generators saw an isolated copy of `SKILL.md`, `references/` and `scripts/` only, never `expected_output`, and wrote to neutral file names. At most four ran at once. Fixture 11 answers the second message of a conversation whose first message is fixture 10's prompt. Fixture 13's `expected_output` was corrected in the same commit: the 1.0% coverage tier is a leverage-linked tier, not a step-down. `evals/scan_reports.py` ran before grading, and its four CHECKs are false negatives (see Observations). Grading was done by an independent, fresh-context grader (model: Opus) that did not write the skill, the fixtures or the reports. Six reports have a blank line between their two header lines, left as generated. The trigger check (TESTING-PLAN section 7, step 5) is not part of this scorecard.

Independent grader. Inputs read in full: `evals/evals.json` (13 fixtures), `evals/TESTING-PLAN.md` §4 and §8, all 15 reports in `evals/iteration-7/`, `SKILL.md`, and `references/01`–`05`. Every cited flag and question ID was checked against `03` and `04`. None of the iteration-1 to iteration-6 folders, `examples/`, `README.md`, `ROADMAP.md`, or git history were opened. Selected script figures were re-run with `scripts/fee_drag_calculator.py` and `scripts/benchmark_comparator.py`. No repository file was edited.

## Headline

- **Grades (15 reports):** PASS **11**, PASS w/ notes **4**, FAIL **0**.
- **Strict count** (a verdict that differs from `expected_output` counts as FAIL): **14 PASS / 1 FAIL**. The one is `01-multifamily-value-add-run2.md`, which says Pass where Pursue-with-conditions is expected.
  - Ultra-strict variant: suppose "Pass as presented — insufficient disclosure" also counts as different from a bare expected "Pass". Then 04, 05 and 06 move too, and the count is 11 / 4. I don't apply that reading in the main count. SKILL.md defines the label as the Pass verdict given when disclosure is insufficient, and fixtures 04, 05 and 06 all accept Pass.
- **Discrimination: 4/4.**
  - 3 vs 4: Pursue with conditions vs Pass as presented.
  - 10 vs 11: Deal B is called materially riskier, and `GEN-08` fires RED on B only.
  - 12 and 13: Pursue and Pursue with conditions, both positive with no RED.
  - 5 vs 13: `CREDIT-01` fires RED on 5 and is not fired on 13.
- **Fixture 01, three runs:**
  - Run 1: **Pursue with conditions** (matches expected).
  - Run 2: **Pass** (differs).
  - Run 3: **Pursue with conditions** (matches).
  - In run 2, a verdict reason rests on an unstated input: `GEN-09` is fired RED on an undisclosed loan maturity, and the "debt-failure chain" drives the Pass. Runs 1 and 3 hold `GEN-09`/`GEN-10` as probes. Both still fire `EQUITY-07` from the word "bridge" alone, and run 3's §10 cites a figure built on assumed leverage.
- **4.7 (not-investment-advice line):** present on its own line directly under both the top verdict and the §10 verdict in **all 15**.
  - The scanner's four CHECKs (01-run3, 02, 07, 09) are false negatives; the Observations section explains why.
- **Gate: CLEARED** (0 FAIL).

## Results

| Report | Expected verdict | Actual verdict | 4.7 top | 4.7 s10 | Grade | One-line reason |
|---|---|---|---|---|---|---|
| 01-multifamily-value-add.md (run 1) | Pursue with conditions | Pursue with conditions | Yes (l.8) | Yes (l.226) | PASS | All target flags (`EQUITY-06`, `GEN-08`, `GEN-05`, `EQUITY-01` probe, `GEN-01`/`GEN-10`/`GEN-11` routed) and questions are present. Financing story named. Drag 464 bps reproduces. |
| 01-multifamily-value-add-run2.md | Pursue with conditions | **Pass** | Yes (l.8) | Yes (l.214) | PASS w/ notes | Verdict differs (no FAIL clause). `GEN-09` fired RED on an undisclosed maturity, and the Pass leans on that debt chain. |
| 01-multifamily-value-add-run3.md | Pursue with conditions | Pursue with conditions | Yes (l.7) | Yes (l.206) | PASS w/ notes | Content is correct. The §10 "why not a clean Pursue" cites a 🔴 figure built on assumed leverage ("net is about 7.5%, which fails"). |
| 02-pref-equity-email.md | Pass as presented, or PwC | Pass as presented — insufficient disclosure | Yes (l.8) | Yes (l.210) | PASS | Classified as pref equity. `GEN-15`/`16`/`17`/`03` fire. Nothing is fabricated: the illustrative fees are tagged 🔴 and don't drive the verdict. Re-screen list provided. |
| 03-hard-money-sound.md | Pursue (PwC acceptable) | Pursue with conditions | Yes (l.8) | Yes (l.200) | PASS w/ notes | HML-01 to HML-05 are correctly cleared and nothing is manufactured. The conditions are verification-grade. One illustrative drag run hides a 0% catch-up input. |
| 04-hard-money-problematic.md | Pass | Pass as presented (insufficient disclosure) | Yes (l.8) | Yes (l.217) | PASS w/ notes | HML-01 to HML-04, `GEN-14` and the must-asks are all present. Expected `HML-05` is held as a probe, not fired. Two flag/question mappings slip. |
| 05-private-credit-concentrated.md | Pass, or PwC | Pass as presented — insufficient disclosure | Yes (l.8) | Yes (l.187) | PASS | `CREDIT-01` RED and `CREDIT-02` form a RED cluster. `GEN-16` and `Q-RISK-06` are present. `HML-` IDs are borrowed for a credit fund (minor). |
| 06-development-first-timer.md | Pass, or PwC | Pass as presented — insufficient disclosure | Yes (l.7) | Yes (l.199) | PASS | `GEN-13`, `GEN-08`, `EQUITY-06`, `GEN-07` (pending leverage), dev+CM stacking (`GEN-06`) and the first-timer gap (`GEN-14`) all fire. `Q-DS-01`/`03` present. IRR/multiple/hold inconsistency caught and checked. |
| 07-office-2026.md | Pass as presented, or PwC | Pass as presented — insufficient disclosure | Yes (l.8) | Yes (l.196) | PASS | Office treated as variable, and the comparator returns "none – variable class". `GEN-19` RED, `GEN-17`, `GEN-09` RED and `Q-MKT-02` present. No office category IRR range applied. |
| 08-packed-flags.md | Pass | Pass (merits) | Yes (l.9) | Yes (l.210) | PASS | Every required flag fires: `GEN-01`, `GEN-02`, `EQUITY-01`+`02` with the 50% promote, `GEN-10`, `GEN-09`, `GEN-13`, `GEN-14`. All required questions present. The real-failure structures in section 4.5 named. |
| 09-teaser-no-disclosures.md | Pass as presented | Pass as presented: insufficient disclosure | Yes (l.7) | Yes (l.229) | PASS | Output is mostly what wasn't disclosed. `GEN-15`/`16`/`17` fire. `GEN-14` fires and routes to `Q-GP-02`. Re-screen list provided. No confident verdict. |
| 10-jcurve-deal-a.md | (not specified; lower-risk half, no major timing flag) | Pass as presented, insufficient disclosure | Yes (l.8) | Yes (l.199) | PASS | Classified as multifamily equity. Year-1 distributions noted. `GEN-11`/`GEN-08` not fired. Framed as the lower-risk shape. |
| 11-jcurve-deal-b.md | (not specified; must call B materially riskier) | Pass as presented, insufficient disclosure (both) | Yes (l.9) | Yes (l.164, l.302) | PASS | `GEN-08` RED at 100% exit, with `GEN-11` cited as the frame. `Q-DIST-01` present. The head-to-head states that equal IRR is not equal risk. |
| 12-clean-equity.md | Pursue (PwC acceptable) | Pursue | Yes (l.7) | Yes (l.210) | PASS | No RED. Every disclosed protection is cleared. The only YELLOW (`GEN-17`: return and hold absent) rests on a genuine absence. |
| 13-clean-credit.md | Pursue (PwC acceptable) | Pursue with conditions | Yes (l.8) | Yes (l.215) | PASS | `CREDIT-01` explicitly not fired on the disclosed 1.1x. `CREDIT-02` cleared. Conditions are verification-grade. The gross-asset fee-base finding is arithmetic on stated terms. |

## Notes

### Fixture 01: all three runs (verdict, and whether any flag or verdict reason rests on an unstated input)

The deal states the 16% / 2.0x, the 5.5%→5.0% caps, an 8% pref and 20% promote with an American waterfall, the three fees, floating bridge debt, and a "30% IRR" track record. It does not state loan maturity, rate cap, LTV, catch-up, clawback, co-invest, the distribution schedule, or whether the 16% is gross or net.

**Shared by all three runs.** `GEN-08` is a 🟡 inference, and it is sound. The stated 16% IRR and 2.0x pin interim distributions to about 5.4% a year under a level-distribution shape, which puts about 73% of profit at exit. Run 2 l.73 makes this derivation explicitly; runs 1 (l.66) and 3 (l.79) bound it with `01`'s 5–8% cash-on-cash. `GEN-07` rests on the stated 16% against the `05` NPI overlay, which is the method `05` prescribes. Neither flag rests on an unstated input.

**Run 1: Pursue with conditions. PASS.**
- The verdict does not rest on an assumed number. §10's swing factor uses only stated arithmetic: "At a flat 5.5% exit, exit value is about 9.1% lower, and equity takes a multiple of that cut" (l.235). The 65%-LTV equity cut is confined to §2 and tagged "🔴 assumed" (l.45).
- Minor:
  - `EQUITY-07` is fired YELLOW–RED from "bridge" alone: "Pairing it with a 5-year hold implies an extension, a refinance…" (l.118). Maturity is unstated (🟡). Verdict reason 2 cites it (l.231), though that reason is framed as an assumption that must hold, with `GEN-10`/`GEN-09` named as probes.
  - `GEN-14` is listed RED but tagged "(🔴 can't tell)" (l.114). Run 3 tags the same absence 🟢, which is the cleaner reading.

**Run 2: Pass. PASS w/ notes. Strict: FAIL.**
- **The verdict differs from expected** (Pursue with conditions); fixture 01 has no verdict FAIL clause.
- **A verdict reason rests on an unstated input.**
  - `GEN-09` is fired **RED** on an undisclosed maturity: "`GEN-09` Debt maturity inside the hold 🟡. Bridge debt is short-duration by design (`01`)… Maturity and extensions are not disclosed" (l.107).
  - The top verdict ends "the financing is the 2022–24 failure shape (`GEN-09`, `GEN-10` open)" (l.6).
  - §10's reasoning says the debt "likely matures inside the hold (`GEN-09`), with unknown rate-cap protection (`GEN-10`) and a takeout refinance it depends on (`EQUITY-07`). That is the exact chain behind the 2022–24 multifamily capital calls" (l.216).
  - SKILL.md's anti-pattern applies: "a finding that needs a 🔴 assumption (leverage, cap terms…) is a must-ask or condition". Its proactive trigger says to *probe* `GEN-09` via `Q-RISK-01` when the hold-vs-maturity relationship is undisclosed.
- **Other assumed inputs in the reasoning:**
  - `GEN-07` adds "floating bridge debt that is likely negatively levered at entry" (l.106). That rests on an undisclosed spread ("Any spread above ~125bps…", l.75).
  - `GEN-10` is "treated as RED until answered" on 🔴 (l.114).
  - §10's swing factor quotes illustrative IRRs: "A 6.0% exit takes it to ~6–8.5%, below the 8% pref" (l.218). Those come from assumed 60–70% LTV and ~5%/yr distributions (l.49). The report says "The verdict does not rest on these figures" (l.49), but §10 still leans on them.
- Everything else is complete. All expected flags and questions are present, the cap-compression fact is correctly stated as decisive (l.49), and 4.7 is met (italicised, own line).

**Run 3: Pursue with conditions. PASS w/ notes.**
- `GEN-09` and `GEN-10` are correctly held as "Probed, not yet fired (RED until answered)" with 🔴 tags (l.126–128).
- `EQUITY-07` is fired YELLOW–RED from "bridge" as in run 1 (l.115).
- The note: §10's "Why not a clean Pursue" cites a 🔴-derived figure. "Remove the compression and the illustrative return falls to about 11.5%… If that basis is gross, net is about 7.5%, which **fails** the 5-year illiquidity hurdle" (l.211). That figure comes from the l.50 model, which "assumes 🔴 65% LTV, interest-only, and about 0.30x of interim distributions".
- The run's next bullet states the correct rule: "Neither the Pass case nor the Pursue case can rest on 🔴 assumptions" (l.213). The verdict matches expected and survives without the figure, so this is a note, not a failure.
- 4.7: the notice sits on the line immediately under the verdict (l.6→7 and l.205→206) with no blank line. See the Observations section for the scanner and rendering point.

**Cross-run read.** The PwC/Pass split follows how each run treats the undisclosed bridge maturity. Runs that hold `GEN-09` as a probe land on Pursue with conditions; the run that fires it lands on Pass. Run 3 itself calls the deal "close to a Pass" (l.6).

### 03-hard-money-sound.md: PASS w/ notes

- **An illustrative drag run hides one assumed input.** §4 says: "add a typical `02` servicing fee (0.5%) and a 20% carry over an 8% hurdle to the 1.5% management fee, and the calculator gives **≈291 bps of drag → 9.09% net**. That is almost exactly the stated target" (l.84). §10's swing factor reuses it (l.204).
  - I re-ran the calculator. 291 bps / 9.09% reproduces only with `--catch-up 0`. With the calculator's default 100% catch-up, the same stack gives 410 bps / 7.90%, which no longer matches the 9% target.
  - The listed assumptions are "12% gross and 4-yr hold ASSUMED 🔴" (l.80). Catch-up is not among them and is missing from §6.
  - The run is labelled illustrative and the verdict doesn't rest on it. But the inference "The 9% is consistent with an undisclosed carry and servicing layer of about that size" depends on an unlabelled input.
- Minor: `Q-FEE-04` (a pref question) is adapted to a performance-fee hurdle, and the report labels it "(adapted)" in §7 l.147. The §8 nice-to-ask row (l.174) instead marks it "*(if a performance fee exists)*" and cites "`02` threshold (>25% or no hurdle)" in the Flag column.
- Substance is otherwise strong. All `HML-` flags are correctly cleared (l.100–105), and the 68% as-is vs 72% ARV LTV inconsistency is caught and routed to `Q-RISK-04` rather than fired (l.98).

### 04-hard-money-problematic.md: PASS w/ notes

- **Expected `HML-05` (no fee step-down) is surfaced but not fired.** "**HML-05**, management-fee step-down: the fund term is unstated. → Q-FEE-01" (l.122, under "Probed, not fired"). `expected_output` lists it among the flags. The report's reasoning is defensible: no fee or term is disclosed, so "long-dated fund" can't be established. Partial on §4.2.
- **Flag-to-question mapping slips** (all IDs exist):
  - `HML-02` is routed to `Q-RISK-05` (l.107, and in the §8 flag column l.177). `Q-RISK-05` cites `HML-03`/`HML-04` only, and `04` has no question for `HML-02`. The report does also name "the geographic-distribution question attached to HML-02".
  - `Q-GP-02`'s flag column adds `GEN-03` (l.178). `GEN-03`'s own response question is the underwriting-model and actuals request, not `Q-GP-02`.
- **Label:** "Pass as presented (insufficient disclosure)" (l.6, l.215) against an expected bare "Pass". Disclosure here really is three unverifiable claims (l.6, l.157), so I count it as within the Pass verdict, and the 3/4 pair still differs. Under the ultra-strict label reading it would count as different.
- All other expected content is present: `HML-01` RED (l.99), `HML-02`/`03`/`04`, "never had a loss" treated as `GEN-14` and as `04`'s named bad-answer signal (l.100, l.102), and `Q-RISK-04`/`05`.

### Scanner CHECKs (01-run3, 02, 07, 09)

All four have the exact sentence, italicised, on the line immediately below the verdict line at both locations: 01-run3 l.7 and l.206, 02 l.8 and l.210, 07 l.8 and l.196, 09 l.7 and l.229. That meets the 4.7 rule as given. The grades for 02, 07 and 09 are therefore PASS. The scanner's cause is explained under the Observations section.

## Observations

### 1. Discrimination: 4/4

- **3 vs 4.**
  - 03 is Pursue with conditions on disclosure that clears `HML-01` to `HML-05`.
  - 04 is Pass as presented with `HML-01` RED and `HML-03`/`HML-04`.
  - The verdicts differ, as required.
- **10 vs 11.**
  - 11 fires `GEN-08` RED on Deal B: "100% of LP return comes from the Year-5 sale" (l.234).
  - It states "Equal IRRs, unequal risk timing" (l.324) and "B wins if the exit happens as planned. A wins in almost every path where it doesn't" (l.325).
  - 10 does not fire `GEN-11`/`GEN-08` on A.
  - Both carry the same disclosure label, but the risk discrimination the fixture tests is explicit.
  - Small inconsistency: 11's re-screen of Deal A fires `GEN-14` RED and `GEN-11` YELLOW ("partly undisclosed", l.87–89), while 10 holds both as probes (l.107–108).
- **12 and 13.**
  - 12 is Pursue with "RED: none" (l.100).
  - 13 is Pursue with conditions with "RED: none fired" (l.97).
- **5 vs 13.**
  - 05 fires `CREDIT-01` RED on stated 2.5x: "against `02`'s >1.5x threshold" (l.90).
  - 13 explicitly declines it: "`CREDIT-01`… Not fired. Leverage is ~1.1x and disclosed, below the >1.5x threshold, and the IRR is shown on both a levered and unlevered basis" (l.104).

### 2. Fee-input honesty: good, with one lapse

Every report passes `0` for undisclosed fees and says the resulting 0 bps is not a finding:
- 04 l.87: "That figure is not a result."
- 07 l.70: "This is **not** a finding that the deal is free."
- 09 l.71 and 10 l.82 make the same point.

Illustrative market stacks are tagged 🔴 or ASSUMED and listed as §6 gaps (01 l.101, 02 l.145, 05 l.132, 06 l.136, 08 l.127, 13 l.147).

The gross-vs-net basis of a headline IRR is consistently treated as unknown and run both ways (01 all runs, 06, 07, 09, 10, 11).

Every drag figure I re-ran reproduces:
- 01: 464 / 369 bps.
- 02: 160 bps.
- 05: 379 bps.
- 06: 300 / 721 bps.
- 07: 469 bps.
- 08: 598 / 821 bps.
- 09: 440 bps.
- 10: 429 bps.
- 11: 468 bps.
- 12: 431 bps.

**The lapse is 03.** Its 291 bps illustration silently uses a 0% catch-up, with the calculator default (100%) giving 410 bps (see Notes).

13's ≈310 bps is derived from stated terms (1.5% × 2.0x NAV + 1.0% × 0.1x NAV) and labelled as arithmetic. That is correct.

### 3. Assumed-number discipline: mostly held, with one verdict-level slip

**Held.** Reports 02 (l.67, l.112), 05 (l.107–114), 09 (l.62, l.98), 10 (l.68, l.93), 11 (l.92–96), 12 (l.111) and 13 (l.107–111) explicitly route flags that would need assumed leverage, cap terms or distribution shape to must-asks instead of firing them.

**Slips:**
- **01-run2** fires `GEN-09` RED on an undisclosed maturity, and its Pass reasoning uses that chain plus 🔴 illustrative IRRs (details in Notes). This is the only verdict-level slip.
- **01-run3** cites a 🔴-derived "7.5% net fails" inside §10's reasoning, though the verdict doesn't depend on it.
- **Softer, all 🟡 inferences:**
  - 01-run1 and 01-run3 fire `EQUITY-07` from "bridge" alone.
  - 06 lists `GEN-07` RED "probable, pending leverage" with leverage unstated (l.98); the cap-compression leg is stated.
  - 07 (l.80) and 08 (l.101) fire `GEN-09` RED on an inferred hold. The fixture expects `GEN-09` in both.

### 4. Verdict calibration

**Where each report lands:**
- Pursue: 12.
- Pursue with conditions: 01 runs 1 and 3, 03, 13.
- Merits Pass: 01-run2, 08.
- Pass as presented: 02, 04, 05, 06, 07, 09, 10, 11.

**Every primary verdict sits inside `expected_output`'s allowed set.** Only 01-run2 falls outside.

**The insufficient-disclosure label is used heavily.** Eight of 13 fixtures get it. Each report justifies it against SKILL.md's "substantially absent" test: 06 has none of `01`'s five development essentials (l.201), and 09 has "not partly missing but **entirely**" (l.231).

**05 and 06 sit near the merits-Pass line.** Both have RED clusters on stated facts:
- 05: "Those two facts together are a RED cluster" (l.10).
- 06: "The facts that *are* disclosed already point toward Pass" (l.203).

A merits Pass, as 08 gives on stated facts (l.212), would arguably be the more precise call. Both labels lead to the same action.

**12 and 13 avoid reflexive pessimism.** 12 says "Inventing a RED here would be a false positive" (l.222).

**Fixture 01 is the calibration weak spot.** It splits 2 PwC to 1 Pass across runs, and the split follows the treatment of the undisclosed bridge maturity rather than any stated fact.

### 5. Fixture 07 variable-class discipline: held

- **No comparator is forced.** The report says "No comparator applies to this class… `benchmark_comparator.py --deal-type office --net-irr 18` returns *'Comparator: none – variable class'*" (l.34). I re-ran it and confirmed the output and exit code 1.
- **The variable baseline is named.** The report says "no stable 'office earns X% net' norm exists for this deal to be measured against" (l.34), and the verdict states "Office is a *variable* class, so the only valid benchmark is the deal's own underwriting, and none was provided" (l.198).
- **No office net-IRR range is invented or applied,** so the FAIL clause is not triggered.
- **Context references are labelled as context.**
  - These are office NPI 3.4% and the development 18–22% target (l.37–40). They sit under "Reference points for context (these are not hurdles the deal clears or fails)" (l.36).
  - The development comparison is the "closest stable analog" usage that `05` allows. It edges toward a category range, so watch it in future iterations.

### Additional: scanner false negatives and markdown rendering (input for the maintainer)

**Scanner false negatives.** The CHECKs on 01-run3, 02, 07 and 09 are wrong.
- `scan_reports.py`'s `notice_follows()` extends the "verdict paragraph" across consecutive non-blank lines to allow a two-line comparison verdict ("a comparison has one line per deal").
- When the notice sits on the very next line with no blank between, the loop swallows the notice into the verdict paragraph. It then looks for the notice in the next paragraph and fails.
- A fix: test whether the line right after each verdict line is the notice before extending the paragraph.

**Markdown rendering.** In CommonMark a single newline is a soft break. In those four reports the italic notice therefore *renders* in the same paragraph as the verdict, even though in the file it is on its own line. That meets 4.7 as given, but a blank line, as the other 11 reports use, would make it render on its own line too.

## Gate

**CLEARED.** There are 0 FAIL across 15 reports: 11 PASS and 4 PASS w/ notes.

- **Strict count:** 14/15. The one FAIL under the strict rule is 01-run2, whose Pass differs from the expected Pursue with conditions.
- **4.7:** met in all 15.
- **Discrimination:** 4/4.

Open items, none blocking:
- Fixture 01's verdict stability (2 of 3 runs on expected) and run 2's use of the undisclosed maturity.
- 03's unlabelled catch-up input.
- 04's `HML-05` held as a probe.
- The scanner false negative.
