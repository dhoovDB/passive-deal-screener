# Iteration-8 Scorecard — fixture 01 rerun

**Method.** A focused rerun, not a full cycle: fixture 01 ran three times, each by a blind, fresh-context generator (model: Opus) that saw an isolated copy of `SKILL.md`, `references/` and `scripts/` only, against the one-line `GEN-09` edit. Fixture 01's `expected_output` gained the matching FAIL clause before the runs. Grading was done by an independent, fresh-context grader (model: Opus) that did not write the skill, the fixtures or the reports.

Line numbers refer to the report files. R1 = `01-multifamily-value-add.md`, R2 = `-run2.md`, R3 = `-run3.md`.

## Headline

- **The fix held in all three runs.** Each report probes GEN-09 instead of firing it, and no flag or verdict reason treats a maturity inside the hold as established. The EQUITY-07 route is also clean.
- **All three reach the same verdict:** Pursue with conditions, matching `expected_output`.
- **No FAIL clause triggers.** Grades: 3 PASS w/ notes, 0 FAIL. No verdict differs from `expected_output`, so the strict count is unchanged at 3 of 3.
- **The notes are about other red-tagged inputs, not maturity.** The most serious is in R1: a why-not-Pursue reason depends on the assumed 100% catch-up (L241).

## Results table

| Report | Verdict | GEN-09 treatment | Maturity under another ID? | 4.7 top | 4.7 s10 | Grade |
|---|---|---|---|---|---|---|
| R1 | Pursue with conditions | Probed, not fired, no severity assigned; "Fires RED if" stated (L122); Q-RISK-01 must-ask (L195) | No | Yes (L6) | Yes (L237) | PASS w/ notes |
| R2 | Pursue with conditions | Probed, not fired, no severity assigned (L114); Q-RISK-01 must-ask (L163) | No | Yes (L6) | Yes (L199) | PASS w/ notes |
| R3 | Pursue with conditions | Probed, not fired, no severity assigned (L148); Q-RISK-01 must-ask (L213) | No | Yes in source (L5); see note | Yes in source (L255); see note | PASS w/ notes |

## Notes (per report)

### Common to all three

**Criteria met in every report**
- **Classification (4.1):** multifamily value-add equity syndication, with `HML-` flags correctly excluded (R1 L17, R2 L17; R3 classifies as equity syndication at L16 and uses no `HML-` flags).
- **Target flags (4.2):** EQUITY-06, GEN-08 and GEN-05 are RED. EQUITY-01 is YELLOW, with the RED path routed through the clawback question.
- **Must-asks (4.3):** Q-DS-01, Q-EXIT-01, Q-FEE-03, Q-FEE-04 and Q-GP-02 all appear with bad-answer signals.
- **Absent items (4.4):** GEN-01, GEN-10, GEN-11 and GEN-09 each route to a must-ask.
- **IDs:** every flag and question ID exists in `03` and `04`. An independent regex check and `scan_reports.py` agree (0 of 3 need attention).

**Fee drag: reproduces in all three**
- Inputs: `--gross-irr 16 --hold-years 5 --carry 20 --hurdle 8 --catch-up 100 --acquisition-fee 2 --disposition-fee 1 --mgmt-fee 1.5 --admin-fee 0`.
- Output: 11.36% net, 464 bps (150 recurring, 60 one-time, 254 promote).
- Variants: no catch-up gives 369 bps and 12.31%. 50% catch-up gives 416 bps and 11.84%. About 21.3% gross gives about 16% net at about 526 bps.
- `--admin-fee 0` is required, because omitting it applies an ASSUMED 0.3%. All three disclose undisclosed fees as passed at 0 (R1 L79, R2 L76, R3 L107).
- Script self-check: PASS.

**GEN-07 fires RED while the operating share is unknown.** R1 L71 and R3 L87 say the operating share can't be measured. The RED has support on non-red inputs: stated compression, GEN-08, and `03`'s rule that the cluster names a financing story. It does not use the assumed leverage figures. This is acceptable, but it is a presumption pending Q-DS-02. R1 L103 and R3 L128 state how the GP can rebut it; R2 L96 does not.

### R1

**Grade:** PASS w/ notes.

**Verdict, exact wording**
- Top (L4): "Verdict: Pursue with conditions. Commit nothing yet: this is a financing story as underwritten, and it earns further diligence only if it survives a flat exit cap on a net-to-LP basis."
- Section 10 (L235): "Pursue with conditions."

**Maturity:** clean.
- GEN-09 (L122): "A 5-year hold is stated, the loan's maturity is not. Fires RED if maturity, with extensions, lands inside year 5."
- Closest passages, none of which asserts a maturity:
  - L124 (EQUITY-07, probe): "Bridge debt needs a takeout unless the sale comes first; plan not stated." This holds for any loan.
  - L243: "Debt terms come second, since they decide whether the LP gets to choose its exit date at all." This is conditional on terms not yet known.
  - L51: the bear case cites "a failed refi", under the 🔴 table label.
- L249 asks the GP to show the maturity fits the plan, which is permitted.

**Red-tagged inputs**
- **Verdict reason on assumed catch-up (the main finding).** L241: "about 11.36% net if the 16% is gross, already under the 12–15% realized range." The gross condition is stated, but the 100% catch-up that L79 tags 🔴 is not. With no catch-up the script gives 12.31%, inside the band. L56 repeats the claim at 🟡.
- **Unconditional conclusion on two assumed inputs.** L57: "The deal only pays for the lock-up if cap rates compress." It has no tag and rests on the 65% LTV and the gross reading. L49 shows the 50% LTV end clearing, and the net reading was not tested here.
- **Verdict section cites an assumed-leverage figure.** L243: "The illustrative base case at a flat cap (7.72% net) falls below the hurdle band." It is labelled illustrative but carries no 🔴, and it sits awkwardly with L44 ("No flag or verdict below depends on it"). The swing factor itself, the exit cap, is stated.
- **No flag rests on assumed leverage or catch-up.** GEN-08 uses a timing-independent present-value range (L67), which I re-derived as 65–89%.

**Fee figures:** the 590 bps and 10.10% at 65% LTV reproduce with acquisition 5.714% and disposition 3.59% of equity. The stress table reproduces exactly from level distributions on total-capitalization LTV. Labelling is complete, including the simple pref (L79, L161).

**Minor**
- L255 "and likely longer" has no stated basis.
- L198 adds GEN-17 to Q-RISK-03, which `04` does not map.

### R2

**Grade:** PASS w/ notes.

**Verdict, exact wording**
- Top (L4): "Verdict: Pursue with conditions. This is a financing story, and it is worth one more round of questions but no capital yet: the return needs a 5.0% exit cap, which is below both the 5.5% going-in cap and today's 5.18% 10yr Treasury."
- Section 10 (L197): "Pursue with conditions."

**Maturity:** clean.
- GEN-09 (L114): "the hold is stated but the loan maturity isn't. Bridge debt's usual term isn't this loan's maturity. Via `Q-RISK-01`."
- L201 treats the gap as a gap: "the debt floats with no disclosed cap or maturity."
- L116 probes EQUITY-07. L43 says only that "A refinance may also matter."
- L210 is a confirm-with-GP condition, which is permitted.

**Red-tagged inputs**
- **Overclaim on distribution shape.** L32: "the only distribution pattern the stated numbers imply." This is false: R1 L67 and R3 L75–78 show other shapes reproduce 16% / 2.0x. Distribution shape is on SKILL.md's list of assumed inputs (L75).
  - GEN-08 survives because L64 sets a floor without that shape.
  - That floor is exactly 60% against a >60% test, and its 8%-a-year path does not reconcile to 16% / 2.0x (it gives a higher IRR).
  - L72 and L215 ("the implied distributions run below the pref") still lean on the shape.
- **Wrong statement on catch-up.** L46: "11.4% (12.3% with no catch-up). That sits below the 12–15% realized band." 12.3% is inside the band.
- **Answer rests on the gross reading.** L45: "Only if the exit cap assumption holds." The next line says a net reading clears at Base.
- **Verdict stays off assumed inputs.** L205 is correctly tagged 🔴, and conditions go to the GP.
- **GEN-07 includes a hedged inference.** L96: "the debt may not be accretive on day one." The spread is undisclosed, but this is not the basis of the flag.

**Fee figures**
- The 580 bps and 10.2% reproduce with acquisition 5.2% and disposition 3.6% of equity.
- **Unlabelled input:** L87's "$2.6M" implies a $130M price, while 65% leverage on the $50M equity implies about $142.9M of capitalization ($2.86M). The price basis is not stated.
- The simple pref is not labelled. It does not change the 464 bps at 100% catch-up.

**Severity and softness**
- L106 lists GEN-16 as YELLOW. `03` makes it YELLOW–RED, treated as RED until answered. It is not a target flag.
- L207 limits Pass triggers to conditions 1–4. Co-invest, clawback, T-12 and rent roll can fail without a Pass, although `03` calls REDs pass-or-resolve.

### R3

**Grade:** PASS w/ notes.

**Verdict, exact wording**
- Top (L4): "Verdict: Pursue with conditions. As presented this is a financing story: do not commit capital until the GP shows the return holds at a flat exit cap, on net-to-LP numbers, with the debt terms in hand."
- Section 10 (L254): "Pursue with conditions. This is a financing story as presented."

**Maturity:** clean.
- GEN-09 (L148): "Hold is stated, this loan's maturity is not. Bridge as a type doesn't establish this loan's term."
- L46: "The plan's reliance on one is undisclosed (`EQUITY-07`, `GEN-09`)" and "a forced sale or refi would make the bear case worse." This is hypothetical.
- L150 probes EQUITY-07. L257 says "unknown cap and maturity terms." L265 is a condition.

**Red-tagged inputs:** the cleanest of the three.
- L60 and L259 keep the outcome conditional: "I won't decide on assumed leverage."
- It carries gross and net side by side (L52–58) and tags the verdict's illustration 🔴 (L261).
- L53's "sits below `01`'s realized 12–15% band" depends on the 100% catch-up, but that is a table read rather than a verdict reason, and L112 discloses 12.31%.

**4.7:** the notice is on its own source line directly under both verdicts, and `scan_reports.py` passes it. However, L4–5 and L254–255 have no blank line or hard break between them. A strict CommonMark renderer merges each pair into one paragraph, so the notice would not display on its own line. R1 and R2 use a blank line and do not have this problem.

**"As presented" wording:** L4 and L254 use the phrase on a merits verdict. SKILL.md L93 says "Merits verdict (no "as presented" label)." It modifies "financing story" rather than the verdict, and L259 correctly calls this a merits verdict, so this is a wording note only.

**Fee figures**
- The 590 bps and 10.1% reproduce with acquisition 5.0% and disposition 4.33% (590.6 bps, 10.09%). These inputs mix 60% loan-to-cost with 60% exit LTV.
- Unrounded flat-cap figures reproduce: 9.65%, 7.83%, 6.87%, 5.18%.
- The simple pref is not labelled, with no effect on the 464 bps.

**Softness**
- L264 lets the GP clear condition 1 if it "defends the 5.0% with renovated-asset comps," with no flat-cap return test. `Q-EXIT-01` allows a defensible thesis, so this has support, but it is an exit from the main test.
- L266 and L267 require disclosure, not a result, despite "Failing any one is a Pass" (L263). R1 L247 requires capital back at a 6.0% exit, and R2 L209 requires capital back in its downside case.
- L55 marks a no-debt case "Clears comfortably" on a deal with stated bridge debt. It is labelled an upper bound, and L60 corrects the impression.

## Conclusions

**Did all three reach the same verdict?** Yes. There is no split to explain. The runs handle unstated inputs differently, and none of those differences moved the verdict:
- Gross vs net: R1 and R2 model gross and note the net case; R3 carries both.
- Leverage: 65% LTV with ranges (R1), 50–70% (R2), exit LTV (R3).
- Distribution shape: a range (R1), level (R2), a norm-bounded pair (R3).

**Did the fix cost anything?** The risk was not lost, but the explanation thinned unevenly.

| Report | §5 entry | Q-RISK-01 | Verdict | §9 lender check |
|---|---|---|---|---|
| R1 | Trigger stated (L122) | L195 | L243 ranks debt second; L249 condition is a Pass trigger | L224 |
| R2 | No mechanism or trigger (L114) | L163 | L201 reason; L210 condition is a Pass trigger | L191 |
| R3 | No mechanism or trigger (L148) | L213 | L257 reason; L265 condition is a Pass trigger | L246 |

- **R1 is the strongest.** It gives the trigger and explains why debt matters to the LP's exit date.
- **R3 is adequate.** The forced-sale consequence appears at L46, away from the GEN-09 entry.
- **R2 is the thinnest.** It never states the forced-refinance or forced-sale failure mode for maturity. The reader gets only the Q-RISK-01 signal "Maturity inside the hold" (L163). This falls short of the skepticism contract's rule 8 and is the one real cost of the fix.
- **Possible follow-up, not applied:** the probe could state the mechanism and "fires RED if" without implying a term, as R1 L122 and L124 do.

**Does any report read as softer than the stated facts warrant?** Not on the core finding. All three mark the stated exit cap RED, note it sits below the 10yr Treasury, name a financing story in the top verdict, and tell the LP not to commit yet. The softness is at the margins:
- R2's narrower Pass triggers (L207) and YELLOW GEN-16 (L106).
- R3's comps exit and disclosure-only conditions (L264, L266–267).
- R1's "Most of the REDs can be resolved by a few documents" (L239), which understates that EQUITY-06 is a stated term. R1 is otherwise the firmest on conditions (L247).

**Remaining pattern across runs.** Fixing GEN-09 did not address the broader habit of stating conclusions from 🔴 inputs in §2 and occasionally in §10: R1 L57, L241, L243 and R2 L45–46. These are the next candidates if SKILL.md's "Deciding on assumed numbers" rule is tightened.

**Method.** Reports, `evals.json` fixture 1, TESTING-PLAN §§4 and 8, SKILL.md, and `03` and `04` were read in full; `01`, `02` and `05` were spot-checked. Calculator, IRR and multiple figures were recomputed with a temporary scratchpad script, since removed. No project file was changed.
