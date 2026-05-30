# passive-deal-screener — Roadmap
## Contributing to `alirezarezvani/claude-skills` (via `dhoovDB/claude-skills`)

**Status:** Pre-development  
**Target domain:** `finance/`  
**Target repo:** `alirezarezvani/claude-skills` (upstream of your fork `dhoovDB/claude-skills`)  
**Skill name (proposed):** `passive-deal-screener`

---

## 1. Why This Skill Doesn't Exist Yet

Before building, understand the gap you're filling vs. what's already out there.

### Existing real estate / deal analyzer skills (surveyed May 2026)

| Skill / Repo | Scope | Perspective | Gap |
|---|---|---|---|
| **Aznatkoiny/zAI-Skills** `real-estate-investment` | End-to-end RE analysis, BRRRR, STR, commercial. Multi-agent with live API integrations (Zillow, Redfin, market data). | **Operator / deal finder** | No LP/syndication mechanics. No fee-stack skepticism. Assumes you're acquiring or operating. |
| **ahacker-1/cre-agent-skills** | Commercial RE underwriting, rent rolls, due diligence, asset management, LP quarterly reviews | **CRE operator / institutional** | Closest to LP, but assumes you have a full deal package (rent roll, T12, etc.). Not designed for screening from email blasts or platform listings. Heavy CRE focus, not private credit or hard money. |
| **mcpmarket.com** `real-estate-infrastructure-investment-analysis` | Cap rates, NOI, FFO/AFFO, REIT analysis, LTV, DSCR | **Public REIT / direct property buyer** | REIT-focused metrics. No syndication waterfall logic. No GP evaluation. No source-agnostic input parsing. |
| **NextAutomation** 10 RE investing skills | Deal underwriter, comp analyzer, market trend predictor | **Active investor / wholesaler** | Operator tools. No passive LP framing. No cross-platform source parsing. |
| **alirezarezvani/claude-skills** `financial-analyst` | DCF, ratio analysis, budget variance, rolling forecasts | **Corporate finance** | No real estate specifics. No syndication structure. No GP/LP mechanics. |
| **alirezarezvani/claude-skills** `business-investment-advisor` | Generic investment analysis | **General** | Too broad to be useful for deal screening. No RE-specific framework. |
| **agi-now/buffett-skills** | Public equity analysis, moat evaluation | **Stock investor** | Not private markets at all. |

### What none of them do

- Screen a deal from **any source** (platform listing, email blast, raw terms) without assuming a specific format
- Apply a **passive LP lens** (fee-stack skepticism, GP alignment, waterfall mechanics, benchmark comparison)
- Cover **cross-asset classes** in one skill (equity syndications AND preferred equity AND hard money/bridge AND private credit funds)
- Flag **what is missing** as a first-class output — not just analyze what's present
- Generate **GP questions** with explicit "bad answer" signals
- Compare to a **public market benchmark** as a forcing function

This is the skill's differentiated position. Keep it narrow to this and don't try to replicate the operator tools above.

---

## 2. Skill Architecture

### Proposed folder structure

```
finance/
└── passive-deal-screener/
    ├── SKILL.md                    ← Required. Frontmatter + core workflow (<500 lines)
    ├── README.md                   ← Install instructions, usage examples, changelog
    ├── references/
    │   ├── 01-asset-class-norms.md     ← Benchmark returns, typical fee ranges, market norms by asset class
    │   ├── 02-syndication-mechanics.md ← LP/GP structure, waterfall types, preferred return types, carry
    │   ├── 03-hard-money-framework.md  ← HML/bridge loan underwriting: ARV, LTV, draw schedules, risk factors
    │   ├── 04-gp-evaluation-rubric.md  ← Track record signals, alignment checks, red flag patterns
    │   └── 05-fee-stack-decoder.md     ← Full taxonomy of fees by deal type, how to calculate total drag
    └── scripts/
        ├── fee_drag_calculator.py      ← CLI: input fee %, hold period, gross IRR → net IRR estimate
        └── benchmark_comparator.py     ← CLI: input deal type, net IRR, hold years → vs. public equivalent
```

### Progressive disclosure mapping (three-level loading)

| Level | What loads | When |
|---|---|---|
| **1 — Metadata** | `name` + `description` frontmatter (~100 words) | Always — at session start |
| **2 — SKILL.md body** | Workflow, routing logic, output schema, red flag taxonomy | When skill triggers |
| **3 — Reference files** | Load only the file(s) relevant to the deal type being analyzed | On-demand per deal |

The SKILL.md body should tell Claude *what to do*. The reference files tell Claude *the facts needed to do it*. Never put market benchmarks or fee norms in the SKILL.md body — they belong in `references/` so they're only loaded when needed and can be updated independently.

### SKILL.md frontmatter (draft)

```yaml
---
name: passive-deal-screener
description: >
  Screens private investment opportunities from the passive LP (limited partner)
  perspective. Analyzes any pasted deal — equity syndications, preferred equity,
  hard money / bridge loan funds, private credit — from EquityMultiple, CrowdStreet,
  direct GP emails, or other sources. Extracts deal snapshot, stress-tests projected
  returns against public benchmarks, deconstructs the full fee stack, surfaces red
  flags and missing disclosures, evaluates GP alignment, and generates prioritized
  questions with explicit signals for what a bad answer looks like. Use whenever
  asked to analyze, evaluate, screen, or review a real estate or private market
  deal, syndication, offering, or investment opportunity. Also triggers on phrases
  like "is this deal worth pursuing", "what should I ask the GP", or "analyze this
  offering memo".
author: dhoovDB
license: MIT
tags:
  - finance
  - real-estate
  - private-markets
  - syndication
  - lp-investor
  - deal-screening
  - passive-investing
  - hard-money
  - private-credit
agents:
  - claude-code
  - codex-cli
  - gemini-cli
  - openclaw
---
```

> **Open design choice #1 — Frontmatter `tags` field:** The upstream repo uses `tags` in some skills but not all. Confirm whether the current `SKILL-AUTHORING-STANDARD.md` requires them before finalizing.

---

## 3. Core Workflow (SKILL.md body outline)

The body should be a procedure, not a reference. Draft structure:

```
# Passive Deal Screener

You are a rigorous private investment analyst...

## When to read reference files
[routing table: which reference file to load for each deal type]

## Step 1: Classify and parse
## Step 2: Extract deal snapshot
## Step 3: Stress-test returns
## Step 4: Deconstruct fee stack
## Step 5: Evaluate GP/operator
## Step 6: Surface red flags and missing disclosures
## Step 7: Generate questions
## Step 8: Render verdict

## Output schema
[required sections and format]

## Analyst rules
[the skepticism contract — what the skill always does regardless of deal quality]
```

> **Open design choice #2 — Output format:** The React artifact (already built) outputs JSON consumed by a UI. The Claude Code skill should output structured Markdown for CLI use. These are different consumers. Decide whether the SKILL.md encodes the Markdown output format, the JSON format (for programmatic use), or both via a routing flag. Recommendation: default to Markdown, document JSON as an opt-in via "output as JSON" instruction.

---

## 4. Python Scripts

Both scripts must be stdlib-only (zero pip installs) — this is a hard requirement of the upstream repo.

### `fee_drag_calculator.py`

**Purpose:** Given gross IRR, fee structure, and hold period, calculate estimated net IRR to LP.

```
python3 passive-deal-screener/scripts/fee_drag_calculator.py \
  --gross-irr 15 \
  --mgmt-fee 1.5 \
  --acquisition-fee 2 \
  --disposition-fee 1 \
  --carry 20 \
  --hurdle 8 \
  --hold-years 5 \
  --json
```

Expected output: net IRR estimate, total fee drag in percentage points, carry threshold analysis.

### `benchmark_comparator.py`

**Purpose:** Given deal type and estimated net IRR, compare to relevant public market benchmark.

```
python3 passive-deal-screener/scripts/benchmark_comparator.py \
  --deal-type multifamily-equity \
  --net-irr 11.2 \
  --hold-years 5 \
  --illiquidity-premium-assumed 2
```

Expected output: benchmark return for comparable public instrument, illiquidity premium implied, whether the deal clears the bar.

> **Open design choice #3 — Benchmark data:** Public market benchmarks (VNQ trailing returns, investment grade bond yields, S&P 500 CAGR) change. The script can either hardcode trailing 10-year averages (simple, no network dependency, goes stale) or call a public API (accurate, requires network, adds complexity). Given the stdlib-only constraint, consider hardcoding with a `LAST_UPDATED` constant and a comment directing the user to update annually. Alternatively, accept `--benchmark-return` as a manual override.

> **Open design choice #4 — Script scope:** The upstream repo's existing finance scripts (ratio_calculator.py, dcf_valuation.py) are ~150-200 lines each. Two scripts is appropriate. A third option would be a `deal_scorer.py` that produces a single composite 0-100 score — useful for comparing multiple deals. Decide if this adds signal or false precision.

---

## 5. Reference Files

Each reference file should have a table of contents at the top if it exceeds 300 lines. Load triggers should be stated explicitly in SKILL.md.

| File | Load trigger | Key content |
|---|---|---|
| `01-asset-class-norms.md` | Always (it's short) | Typical return ranges, hold periods, and risk profiles by asset class. Used for stress-testing. |
| `02-syndication-mechanics.md` | Deal type is equity, preferred equity, or fund | American vs. European waterfall, cumulative vs. non-cumulative preferred, promote structures, clawback mechanics |
| `03-hard-money-framework.md` | Deal type is HML, bridge, or private credit | ARV, LTV norms, draw schedule risk, borrower qualification signals, default/foreclosure process |
| `04-gp-evaluation-rubric.md` | Always when a GP/sponsor is identified | Track record green/yellow/red signals, alignment checklist, marketing-heavy language patterns to flag |
| `05-fee-stack-decoder.md` | Always | Full fee taxonomy by deal type, how to calculate aggregate drag, what each fee should and shouldn't look like |

> **Open design choice #5 — Reference file granularity:** You could merge `02` and `03` into a single "deal mechanics" file and split `04` into separate GP track record and GP alignment files. The current split prioritizes loading efficiency (a hard money deal doesn't need waterfall mechanics loaded). Evaluate during testing.

---

## 6. Competitive Differentiation to Preserve

Do not let scope creep dilute these during development:

1. **Source-agnostic input parsing.** The skill must handle unstructured text — not require a template or specific format. This is what makes it work on email blasts.
2. **Missing disclosures as a first-class output.** Most analyzer skills only analyze what's present. Surfacing what was withheld is equally important.
3. **Public market benchmark comparison.** Forces every deal to clear a real hurdle, not just an internal one.
4. **Bad-answer signals on questions.** Not just "ask this" but "here's what evasion looks like."
5. **LP perspective, not operator perspective.** The skill should never assume the user is acquiring, developing, or operating. Avoid any output framing that implies the investor has operational control.

---

## 7. Open Design Choices (consolidated)

Decisions to make before finalizing files. Document the choice you make and why in the PR description.

| # | Decision | Options | Recommendation |
|---|---|---|---|
| 1 | **Frontmatter tags field** | Include / omit | Check `SKILL-AUTHORING-STANDARD.md` in upstream repo before finalizing |
| 2 | **Output format** | Markdown (default) / JSON (opt-in) / both | Markdown default; JSON as `--json` flag or "output as JSON" instruction |
| 3 | **Benchmark data freshness** | Hardcoded with `LAST_UPDATED` / manual `--benchmark-return` flag / API call | Hardcode + manual override; avoids network dependency, keeps stdlib-only |
| 4 | **Third script** | `deal_scorer.py` composite score / skip | Skip v1.0; false precision risk; add in v1.1 after evals validate usefulness |
| 5 | **Reference file granularity** | 5 files as proposed / merge deal mechanics / split GP evaluation | Test with 5 files; merge only if SKILL.md routing logic gets unwieldy |
| 6 | **Domain placement** | `finance/` (existing) / new `private-investing/` domain | `finance/` for v1.0; propose `private-investing/` domain expansion in PR discussion if maintainer agrees |
| 7 | **Slash command** | Add `/cs:screen-deal` command / skip | Add — consistent with other finance skills; low effort, high discoverability |
| 8 | **Asset class routing** | Single workflow / branching by deal type | Branch at Step 2 (classify); load relevant reference file; reconverge at output |
| 9 | **React artifact vs. SKILL.md** | Ship both / SKILL.md only / artifact only | Both — they serve different surfaces (claude.ai chat vs. Claude Code CLI). Document in README. |
| 10 | **Contribution target** | PR from `dhoovDB` fork to `alirezarezvani` upstream / maintain in fork only | PR to upstream via `dev` branch — this is the stated goal |

---

## 8. Contribution Process (Step by Step)

The upstream repo's wiki (`Writing Your Own Skill`) specifies this process:

### Phase 1: Setup (one-time)

```bash
# Confirm your fork is up to date with upstream
cd your-local-clone-of-dhoovDB-claude-skills
git remote add upstream https://github.com/alirezarezvani/claude-skills.git
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

### Phase 2: Build the skill

```bash
# Branch from dev, not main
git checkout dev
git checkout -b feat/finance-passive-deal-screener

# Create the skill folder
mkdir -p finance/passive-deal-screener/references
mkdir -p finance/passive-deal-screener/scripts
```

Build order:
1. `references/01-asset-class-norms.md` — start here; this is the factual foundation everything else draws from
2. `references/05-fee-stack-decoder.md` — needed to write the fee analysis step
3. `references/02-syndication-mechanics.md`
4. `references/03-hard-money-framework.md`
5. `references/04-gp-evaluation-rubric.md`
6. `SKILL.md` — write last; the reference files clarify what belongs in the body vs. Level 3
7. `scripts/fee_drag_calculator.py`
8. `scripts/benchmark_comparator.py`
9. `README.md`

### Phase 3: Test the skill (Claude.ai workflow, per `skill-creator` SKILL.md)

Since you're in Claude.ai (not Claude Code), subagent-based parallel evals aren't available. Use the adapted process:

1. Write `evals/evals.json` with 6-8 test cases covering:
   - Multifamily equity syndication (full offering memo)
   - Preferred equity deal (sparse email blast)
   - Hard money fund (platform listing)
   - Deal with obvious red flags (test flag detection)
   - Deal missing most disclosures (test missing-disclosure output)
   - Direct GP email with aggressive return projections (test stress-testing)

2. For each test case, load SKILL.md yourself and follow the workflow against the test input. Record outputs in `evals/iteration-1/`.

3. Review: does each output correctly classify the deal, surface the right flags, generate useful questions?

4. Iterate on SKILL.md and reference files. Aim for 2-3 iteration cycles before PR.

5. Optimize the description frontmatter for triggering accuracy — confirm it fires on phrases like "analyze this deal", "is this worth pursuing", "what should I ask the GP".

### Phase 4: Quality checklist (from `SKILL-AUTHORING-STANDARD.md`)

Before opening the PR, verify:

- [ ] SKILL.md is under 500 lines
- [ ] Frontmatter has `name`, `description`, `author`, `license`
- [ ] Description is written in third person
- [ ] Description includes both what the skill does AND trigger contexts
- [ ] All Python scripts run with `python3 script.py --help` (zero pip installs)
- [ ] Reference files are linked from SKILL.md with explicit load guidance
- [ ] README.md includes install instructions and usage examples
- [ ] No hardcoded API keys, credentials, or personally identifying information
- [ ] Skill passes the security auditor: `python3 engineering/skill-security-auditor/scripts/skill_security_auditor.py finance/passive-deal-screener/`

### Phase 5: Commit and PR

```bash
# Commit convention used by the upstream repo
git add finance/passive-deal-screener/
git commit -m "feat(finance): add passive-deal-screener — LP-perspective deal screening for syndications, preferred equity, and hard money"

git push origin feat/finance-passive-deal-screener
```

Open a PR from `dhoovDB:feat/finance-passive-deal-screener` → `alirezarezvani:dev`.

**PR description should include:**
- What the skill does and who it's for
- Competitive positioning (what existing skills don't cover)
- Open design choices you resolved and why
- Test cases run and iteration summary
- Any proposed changes to `finance/CLAUDE.md` or top-level `README.md` to add the skill to the domain table
- Screenshot or sample output for one test case

---

## 9. Files to Update in the Repo (Beyond the Skill Folder)

| File | Change needed |
|---|---|
| `finance/CLAUDE.md` | Add `passive-deal-screener` to the finance domain skill list |
| Top-level `README.md` | Add row to the Finance domain table: `passive-deal-screener \| Screens private market deals from LP perspective: syndications, preferred equity, hard money, private credit` |
| `CHANGELOG.md` | Add entry under next version: `feat(finance): passive-deal-screener — LP-perspective deal screener for private markets` |

The upstream maintainer (alirezarezvani) typically handles `CHANGELOG.md` on merge, but including a draft entry signals professionalism and reduces maintainer friction.

---

## 10. Relationship to the React Artifact (Already Built)

The React artifact in this chat (`deal-evaluator.jsx`) and the Claude Code skill are different deliverables for different surfaces:

| | React Artifact | Claude Code Skill |
|---|---|---|
| **Surface** | claude.ai chat, embedded UI | Claude Code CLI, Codex, Cursor, etc. |
| **Input** | Paste into textarea, click button | Natural language prompt with pasted deal text |
| **Output** | Structured tabs with color-coded UI | Structured Markdown report |
| **API call** | Makes its own Anthropic API call | IS the skill — no nested API call |
| **Portability** | claude.ai only | 12 platforms via conversion scripts |
| **Contribution target** | Not contributed — personal tool | `alirezarezvani/claude-skills` |

The system prompt in the React artifact is the best draft of the analytical framework. When writing the SKILL.md body, adapt (don't copy verbatim) that prompt into the workflow steps and reference file structure. The JSON output schema from the artifact can inform the optional `--json` output mode.

---

## 11. Estimated Effort

| Phase | Effort estimate | Notes |
|---|---|---|
| Research & reference files | 3-4 hours | Most of the intellectual work. The reference files ARE the skill. |
| SKILL.md body | 1-2 hours | Straightforward once reference files are done |
| Python scripts | 2-3 hours | Both are ~100-150 lines; arithmetic-heavy but not complex |
| Test cases and evals | 2-3 hours | Finding or writing good test inputs takes time |
| Iteration cycles | 2-4 hours | Minimum 2 cycles; plan for 3 |
| README + PR prep | 1 hour | |
| **Total** | **~12-17 hours** | Spread across sessions; skill improves with deal reading experience you'll accumulate anyway |

The reference files will get better as you read more real deals. Consider a v1.1 update 3-6 months after initial contribution, once you've run 20+ real deals through the tool and identified gaps.

---

## 12. Versioning Plan

| Version | Scope |
|---|---|
| **v1.0** | Core skill: all 5 asset classes, fee-stack analysis, red flags, GP evaluation, question generation, 2 scripts |
| **v1.1** | Calibration update: benchmark data refresh, refined red flag taxonomy based on real deal reps |
| **v1.2** | `deal_scorer.py` script (if evals validate usefulness), expanded test suite |
| **v2.0** | Consider multi-agent upgrade: orchestrator + specialist sub-skills (equity analyzer, HML analyzer, GP track record researcher) — only if SKILL.md approaches 500-line limit or if asset class routing becomes unwieldy |

---

## Decision log

*Project and architectural decisions live here. Changes to this repo's CLAUDE.md are logged in CLAUDE.md, not here.*

### 2026-05-24 — Primary deliverable is SKILL.md, not the React artifact

The React artifact (deal-evaluator.jsx) was built first as an analytical prototype in claude.ai. The Claude Code skill is the contribution target. They share analytical logic but serve different surfaces and audiences. Keeping them separate prevents the skill from inheriting UI concerns that do not belong in a markdown-first tool.

### 2026-05-24 — References built before SKILL.md

The skill draws from reference files for all factual claims about market norms, fee ranges, and return expectations. Building the skill before the references are complete means the skill hallucinates its own foundation. Build order is enforced in CLAUDE.md and in this file.

*(Both entries moved here from CLAUDE.md on 2026-05-25 — they are project decisions, per `writing-kit/ROADMAP-TEMPLATE.md`.)*

### 2026-05-29 — Built `references/01-asset-class-norms.md` (first reference file)

- **"Variable" is a real value, not a hole.** Where a category's norm is genuinely unstable in the current cycle (post-2020 office, regulatory-sensitive STR, cycle-sensitive development, mixed-use composites), the cell is *variable* with a one-line reason. This implements the CLAUDE.md "no hallucinated ranges" rule literally — *variable* tells the analyst the baseline is the deal's own underwriting, not a category default. Coverage of variable cells is a feature, not a coverage hole.
- **Categorical provenance, not point citations.** "Industry survey norms" cites NCREIF (NPI, ODCE), Preqin, ILPA, sector trade groups (NMHC / NAIOP / ICSC / MBA), and a cross-section of LP marketing materials — rather than pinning specific numbers to specific reports. The file lags the cycle; the trade-off is keeping it concise and updatable without invalidating every citation when a vintage rolls.
- **Absent disclosures are first-class.** Each asset class lists its "essential disclosures" — when a real deal omits one of those against a category that normally has it, that's a flag, not a neutral silence. This wires the CLAUDE.md "missing disclosures as a first-class output" rule into the factual baseline.
- **Asset-class taxonomy follows the React artifact's `asset_class` enum** so the SKILL.md (Level 2) and the artifact's surface use the same vocabulary.

---

*Generated from conversation context: passive real estate investing learning path, LP/GP structure, hard money lending, EquityMultiple analysis, fee drag mechanics. The analytical framework is grounded in the investor's background (commercial credit analyst, STR operator) and goals (passive LP, not operator).*

*Last updated: 2026-05-29*
