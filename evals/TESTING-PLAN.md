# Testing Plan — passive-deal-screener

How `SKILL.md` is validated against real and synthetic deals before the upstream
PR opens. This plan governs the eval suite specified in `ROADMAP.md` §8 Phase 3
and feeds the Phase-4 ship gate (`evals/evals.json` carries the cases below;
SKILL.md must pass all of them after ≥2 iteration cycles).

It is written against what the skill actually does: the 10-section output schema,
the deal-type routing branches, the 34 flag IDs in `references/03-red-flag-library.md`,
and the `Q-` question IDs in `references/04-question-bank.md`.

---

## 1. Scope and file layout

```
evals/
  TESTING-PLAN.md      ← this file
  evals.json           ← the 11 cases as structured records
  inputs/NN-slug.md    ← one deal fixture per input (13 files: cases 3 and 9 are pairs)
  sources.md           ← provenance: every real source's URL, as-of date, and what was extracted
  iteration-N/         ← captured SKILL.md output per case, per iteration cycle
```

The eval is a manual run, per ROADMAP §8 Phase 3: load `SKILL.md`, screen each
input, capture the output to `iteration-N/`, score against §4, fix SKILL.md or a
reference, re-run. The bar is **all 11 cases passing after ≥2 cycles** (§8).

---

## 2. Testing philosophy

### 2.1 Real vs synthetic split

Two kinds of case, sourced differently:

- **Realism cases** parse a real fee stack, memo, or platform listing — they test
  that the skill extracts and classifies *messy real disclosure* correctly. These
  pull from public sources (§3).
- **Control cases** must be **synthetic**, because they hold a variable still that
  no real deal will: an identical IRR across a J-curve pair (case 9), a deal packed
  with co-occurring flags (case 7), a deal stripped to near-nothing (case 8). A
  real deal won't volunteer a clean controlled contrast; a constructed one will.

The split per case is in the §5 matrix. Roughly: realism cases are real, control
cases are synthetic, and two cases (3, 10/11) deliberately mix the two.

### 2.2 The circularity problem (why Tier 4 and real clean deals matter)

If the **same author** writes both the flag definitions (`03`) and the synthetic
deals designed to trip them, a passing synthetic proves only that the deal matches
the definition — not that the definition catches anything in the wild. The test is
tautological.

Two defenses are built into this plan:

- **Tier-4 real failures** (§3) break the circularity on the *miss* side. We did
  not author Nightingale or the 2022–24 multifamily blow-ups; if the skill flags
  what actually destroyed that LP capital, that is real-world accuracy, not a
  matched definition.
- **At least one real clean deal** (cases 10–11) breaks it on the *false-positive*
  side. A self-authored "clean" deal only proves the skill doesn't flag a deal
  built to be unflaggable. A real, well-structured deal the skill correctly leaves
  alone is the harder, more honest test.

**Stated plainly: synthetics validate mechanics; real cases (Tier 4 failures and
real clean deals) validate real-world accuracy.** Both are required.

### 2.3 Two failure modes — misses *and* false positives

The original nine cases test only **misses** (false negatives): did the skill
catch the problem? They say nothing about **false positives**: does the skill flag
a *sound* deal into oblivion? A screener that flags everything is useless even if
it never misses a real problem — it gives the LP no signal.

Cases 10 and 11 are the false-positive test: two genuinely sound deals where the
correct output is "this looks solid, here are minor clarifying questions." Without
them we cannot tell whether the skill is **discriminating** or just
**pattern-matching pessimism**.

---

## 3. Source tiers (richest first)

| Tier | Source | Best for | Cases |
|---|---|---|---|
| 1 | **SEC EDGAR** — Reg A+ circulars (Form 1-A / 253G2), non-traded REIT prospectuses (S-11), BDC prospectuses & 10-Ks | Full fee stacks, waterfalls, risk factors, sponsor track records — legally required, fully public | 1, 3a, 4, 11 |
| 2 | **Platforms with public detail** — Fundrise, Groundfloor, CrowdStreet, Arrived | Real platform listings; the "paste a listing" framing | 3a, 5, 6, 10 |
| 3 | **Published reviews & forum posts** — deal teardowns, BiggerPockets / Reddit threads | Messy, source-agnostic, sparse inputs | 2 (form), 8 (form) |
| 4 | **Known blow-ups** — Nightingale/CrowdStreet, Tides/GVA/Applesway multifamily distress, SEC actions | Highest-value validation: outcome already known; breaks circularity | 7 (pattern), distress overlay |

### Extraction rules (every real source)

- **Facts and disclosed terms only** — fee percentages, hold, leverage, LTV,
  pref, waterfall type, occupancy, default/recovery rates. These are not
  copyrightable.
- **No prose.** Do not copy offering-memo or reviewer sentences. Re-express every
  fixture in neutral terms.
- **Scrub before commit.** Names, addresses, and sponsors are removed before any
  fixture lands in `inputs/` or `examples/` — the repo is public. Use a stand-in
  ("a Sun Belt multifamily sponsor", "Metro A").
- **Fixtures from facts, not republished documents.** Every real fixture cites its
  source + as-of date in `sources.md`; the fixture itself carries no identifying or
  copyrighted text.

---

## 4. Pass criteria

Applied to **every** case (1–11):

1. **Correct classification.** Deal type → the right `02`/`03` slice; asset class →
   the right `01`/`05` baseline and comparator. A misclassification routes the whole
   screen wrong and fails the case regardless of downstream output.
2. **Caught the target flags**, by ID from `03`. The §6 per-case spec lists the
   flag IDs each case exists to test; the output must surface them with correct
   severity.
3. **Generated the right must-ask questions**, by ID from `04`, with the bad-answer
   signal intact.
4. **Missing-data-as-flagged-output fired.** When a deal lacks the information a
   flag needs, the correct behavior is to *say so and route it to a must-ask* —
   e.g. "cannot assess floating-rate exposure: debt structure not disclosed → ask
   the GP" — **not** to stay silent. Absence of information is a first-class output.
   Every case verifies this fires where data is absent; a silent skip is a fail.

Two **conditional** criteria:

5. *(Tier-4 / known-outcome inputs)* The skill **flagged what actually broke the
   deal, before the break** — the rate-cap expiry, the missing clawback, the
   misappropriation-enabling structure — not just generic risk.
6. *(Clean cases 10–11)* **No manufactured RED flags.** Verdict is positive
   (Pursue), output is minor clarifying must-asks only. A RED flag invented on a
   sound deal is a false positive and fails the case — this is the discrimination
   test.

---

## 5. The case matrix

11 cases (13 input fixtures — cases 3 and 9 are contrast pairs).

| # | Case | Real / Synth | Tier | Target flags (`03`) | Key questions (`04`) | Expected verdict |
|---|---|---|---|---|---|---|
| 1 | Multifamily value-add, full offering memo | Real | 1–2 | EQUITY-06, GEN-08, GEN-11, GEN-01 | Q-DS-01, Q-EXIT-01, Q-FEE-03/04, Q-GP-02 | Pursue-with-conditions |
| 2 | Preferred equity, sparse email blast | Synth | 3 (form) | PREF-01, EQUITY-04, GEN-15/16/17 | Q-FEE-04, Q-LIQ-01 | Conditions / missing-data |
| 3a | Hard money / bridge fund — **sound** | Real | 1–2 | (clears) HML-01 answered on as-is; disclosed default/recovery | Q-RISK-04/05 | **Pursue** |
| 3b | Hard money / bridge fund — **problematic** | Synth | — | HML-01, HML-02, HML-03, HML-04, HML-05 | Q-RISK-04/05 | **Pass** |
| 4 | Private credit fund, sector concentration | Real | 1 | CREDIT-01, CREDIT-02, GEN-16 | Q-RISK-06 | varies |
| 5 | Development, aggressive projections | Real/Synth | 2 | GEN-13, GEN-08, EQUITY-06, GEN-07 | Q-DS-03, Q-DS-01 | Pass / conditions |
| 6 | Office in 2026 (variable class) | Real/Synth | 2 | GEN-19, GEN-17, GEN-09 | Q-MKT-02 | drive off own underwriting |
| 7 | Obvious GP red flags | Synth (Tier-4 patterned) | 4 | GEN-01, GEN-02, EQUITY-01, EQUITY-02, EQUITY-03, GEN-13, GEN-14 | Q-GP-01/02/03, Q-FEE-03 | Pass (reject) |
| 8 | Missing nearly all disclosures | Synth | 3 (form) | GEN-14, GEN-15, GEN-16, GEN-17 | most must-asks | Pass / cannot-assess |
| 9 | Identical IRR, different J-curve (pair) | Synth (pair) | — | GEN-11 | Q-DIST-01 | back-loaded = materially riskier |
| 10 | **Clean equity syndication** | Real preferred / Synth | 1–2 | none RED (≤1–2 YELLOW if genuinely present) | minor clarifiers only | **Pursue / solid** |
| 11 | **Clean private-credit fund** | Real preferred / Synth | 1 | none RED (≤1–2 YELLOW if genuinely present) | minor clarifiers only | **Pursue / solid** |

---

## 6. Per-case detail

Each entry: what it exercises · target flags and why · expected verdict · what a
FAIL looks like.

**Case 1 — Multifamily value-add, full memo (real).** The happy path on a complete
package. Must extract the full snapshot, compute fee drag (`02` + `fee_drag_calculator.py`),
stress the exit cap, and decompose return sources. Flags fire only where the real
deal warrants. *FAIL:* misses the exit-cap sensitivity (EQUITY-06/GEN-08) or can't
produce a gross-to-net drag from disclosed fees.

**Case 2 — Preferred equity, sparse email (synthetic form, real pattern).**
Source-agnostic parse of three sentences. Must classify it as preferred equity,
then make the output *mostly missing-disclosures + must-asks*. *FAIL:* refuses to
classify on thin input, or fabricates terms not stated.

**Case 3a — Hard money, sound (real).** A real Groundfloor / HML fund circular with
LTV on **as-is** value, disclosed default and recovery history, diversified book.
Demonstrates the skill can clear a debt fund. *FAIL:* manufactures HML flags the
disclosure actually answers (a false positive on a sound debt deal).

**Case 3b — Hard money, problematic (synthetic).** Same asset class, opposite
facts: LTV quoted on **ARV only**, default/recovery hidden, single-metro
concentration, no fee step-down. *FAIL:* doesn't catch HML-01's ARV-vs-as-is trap,
or verdicts it the same as 3a. **3a→Pursue and 3b→Pass together prove the skill
discriminates within a deal type rather than treating "hard money" as one verdict.**

**Case 4 — Private credit, sector concentration (real BDC).** Tests CREDIT-01
(fund leverage stacked on loan leverage; levered IRR shown as if unlevered) and
CREDIT-02 (sector concentration). *FAIL:* misses that the quoted IRR is levered, or
treats fund-level leverage as benign.

**Case 5 — Development, aggressive projections.** Stress-test against `01`'s 18–22%
*target* development baseline and `05`'s VNQ comparator (discount the target
premium heavily for realized-below-target). *FAIL:* accepts the headline IRR without
flagging the absent sensitivity (GEN-13) or the exit-dependence (GEN-08).

**Case 6 — Office in 2026 (variable class).** Must **refuse a generic baseline** and
drive the analysis off the deal's own underwriting (physical occupancy, class, debt
maturity); `benchmark_comparator.py` returns "variable — no comparator." *FAIL:*
applies a category IRR range to office, or doesn't trigger GEN-19/Q-MKT-02.

**Case 7 — Obvious GP red flags (synthetic, Tier-4 patterned).** Packed with
co-occurring flags drawn from real enforcement patterns: zero co-invest, prior
regulatory action, deal-by-deal waterfall + high promote + no clawback, projections
with no downside. Must list **all** with severity and verdict Pass. *FAIL:* catches
some but not all, or softens the verdict. (Grounded in real patterns per §2.2, but
labeled synthetic — it validates mechanics, not accuracy.)

**Case 8 — Missing nearly all disclosures (synthetic).** A teaser with almost no
terms. Output should be ~80% "here is what was not said," routed to must-asks, not a
confident verdict. *FAIL:* returns "looks fine" or a Pursue/Pass verdict instead of
"cannot assess — here's everything missing."

**Case 9 — Identical IRR, different J-curve (synthetic pair).** Two deals, same
headline IRR; one distributes from year 1, one back-loads everything to exit. Must
flag GEN-11 / Q-DIST-01 and call the back-loaded deal materially riskier. *FAIL:*
treats equal IRR as equal risk.

**Case 10 — Clean equity syndication (real preferred).** A well-structured deal:
meaningful pari-passu GP co-invest, clawback present, cumulative compounding pref at
market, in-range fees, realized track record, debt maturing after the exit, exit cap
≥ going-in. Verdict Pursue; output is minor clarifiers. *FAIL:* invents a RED flag.
Prefer a real institutional-quality deal to break circularity (§2.2).

**Case 11 — Clean private-credit fund (real preferred).** The clean counterpart to
case 4: conservative LTV on as-is, through-cycle default + recovery disclosed,
diversified, fee step-down present, modest/no fund leverage with the IRR basis
stated. Verdict Pursue. *FAIL:* flags conservative disclosed leverage as CREDIT-01
when it isn't. Spanning equity (10) and debt (11) proves the skill can say "solid"
in *both* branches.

---

## 7. Execution protocol

Per ROADMAP §8 Phase 3:

1. Load `SKILL.md`; screen each `inputs/NN-slug.md` fixture.
2. Capture each output verbatim to `evals/iteration-N/NN-slug.md`.
3. Score each against §4. Record pass/fail + the specific criterion that failed.
4. On a failure, fix `SKILL.md` or the implicated reference (not the test), then
   re-run the affected case. Aim for 2–3 cycles.
5. After the cases pass, confirm the `description` frontmatter triggers on
   "analyze this deal", "is this worth pursuing", "what should I ask the GP".

---

## 8. Scoring and exit bar

A case **passes** when all four universal criteria (§4.1–4.4) hold, plus the
conditional criterion that applies to it (§4.5 Tier-4, §4.6 clean). The suite
**clears** when all 11 pass after ≥2 iteration cycles, with iteration logs retained
in `iteration-N/`. This is the Phase-4 content gate; the PR does not open until it
clears.

---

## 9. Pre-commit checklist (anonymization & provenance)

Before any fixture or output is committed (public repo):

- [ ] No real names, addresses, or sponsors in `inputs/`, `iteration-N/`, or `examples/`
- [ ] No copied offering-memo or reviewer prose — facts re-expressed in neutral terms
- [ ] Every real fixture cites its source URL + as-of date in `sources.md`
- [ ] Synthetic fixtures labeled synthetic in `sources.md` (so a reviewer knows which validate mechanics vs accuracy)
- [ ] No API keys, credentials, or PII anywhere in `evals/`

---

## 10. Sources to populate (Part 2 — live research)

Filled into `evals/sources.md` after this plan is approved. Targets:

- [ ] Groundfloor (or comparable) hard-money circular → case 3a
- [ ] Fundrise Reg A circular → case 1 or 10
- [ ] A BDC prospectus / 10-K (e.g. a public private-credit BDC) → case 4 or 11
- [ ] An office repricing / distressed office offering → case 6
- [ ] Tides / GVA / Applesway multifamily distress post-mortems → distress overlay (cases 1, 5, 7)
- [ ] Nightingale / CrowdStreet misappropriation post-mortem → case 7

Each entry in `sources.md` records: URL, as-of date, deal type, which case it
feeds, and the specific facts extracted (never prose).
