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
    ├── README.md                   ← Install instructions, usage examples, changelog (skill-level)
    ├── references/
    │   ├── 01-asset-class-norms.md     ← LP-perspective baseline by asset class (hold / IRR / risk tier / essential disclosures)
    │   ├── 02-fee-stack-library.md     ← Full fee taxonomy by deal type + waterfall mechanics + total-drag framework
    │   ├── 03-red-flag-library.md      ← ≥25 categorized flags with severity + response questions; flag IDs in {ASSET_CLASS}-{NN} format
    │   ├── 04-question-bank.md         ← ≥20 LP questions with good/bad answer signals; cites ≥5 flag IDs from 03
    │   ├── 05-benchmark-returns.md     ← Public-market comparators + illiquidity-premium framework
    │   └── data/                       ← Versioned external-source snapshots
    │       ├── README.md                       ← vintage, source, and update instructions
    │       ├── ncreif-npi-snapshot.md
    │       ├── fred-10yr-snapshot.md
    │       └── preqin-vintage-note.md
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
```

## Output schema (required sections, in order)

1. Deal Snapshot — asset class, deal type, sponsor, hold, claimed return.
   One paragraph, no editorializing.

2. Return Stress-Test — base / bull / bear with the 2–3 swing
   assumptions called out explicitly. Not just "returns may vary."

3. Where LP Returns Come From — cash flow vs exit vs leverage.
   Flag if >60% of IRR is exit-dependent or leverage-dependent.

4. Fee Stack Summary — gross-to-net drag in basis points.
   Total drag figure, not just a list of fees.

5. Red Flags — ranked by severity (RED / YELLOW).
   Each flag: one-line mechanism + one-line LP exposure.

6. Missing Disclosures — what this deal type normally discloses
   that this deal didn't. Absence is first-class output.

7. GP Alignment Assessment — co-invest, track record quality
   (realized exits only), waterfall alignment.

8. Questions for the GP — prioritized, with bad-answer signals.
   Must-ask separated from nice-to-ask.

9. Diligence Checklist — items still requiring third-party
   verification before committing capital.

10. Verdict — Pursue / Pass / Pursue with conditions.
    Reasoning visible, not just the label.

## Analyst rules (the skepticism contract)

These apply regardless of how attractive a deal appears:

- Default to adversarial posture. The job is not to validate the deal
  but to find the conditions under which it fails. Every analysis starts
  from "how does this deal protect LP capital?"

- Never compare gross to gross. All return comparisons must be
  net-to-LP vs net-to-LP, or vs post-expense-ratio public benchmarks.
  Gross IRR comparisons are not permitted in any output section.

- Flag exit-dependent IRR. If >60% of projected LP return is driven by
  terminal value or exit cap rate assumption rather than in-place cash
  flow, call it out explicitly in Section 3 (Where LP Returns Come From)
  and again in the Verdict.

- Flag leverage-dependent IRR. If the deal's return story depends
  primarily on leverage and cap rate compression rather than operational
  value creation, label it a "financing story" not an "asset story" and
  flag it RED in Section 5.

- Treat unrealized track record as no track record. A GP's "track
  record" citing only unrealized or marked-to-market deals must be
  flagged as unverified in Section 7 (GP Alignment Assessment).

- Absent information is output, not silence. Every section must
  explicitly note what was not disclosed that normally would be for this
  deal type. Do not skip over absences.

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

Each reference is a focused factual baseline that SKILL.md indexes against. Adding a new factual claim to the skill means updating a reference, not the workflow. Files >300 lines should open with a table of contents; load triggers belong in SKILL.md so each reference loads only when relevant. **Numbering matches CLAUDE.md (authoritative).** Mechanics content that doesn't get a standalone file — syndication waterfalls, hard-money LTV/ARV/draw schedules — lives as subsections within the relevant file below (waterfalls in `02-fee-stack-library`, HML-specific red flags in `03-red-flag-library`, etc.).

| File | Load trigger | Status |
|---|---|---|
| `01-asset-class-norms.md` | Always (compact baseline) | ✅ Shipped 2026-05-25 |
| `02-fee-stack-library.md` | Always | ✅ Shipped 2026-05-30 |
| `03-red-flag-library.md` | Always | ✅ Shipped 2026-06-01 |
| `04-question-bank.md` | Always when a GP is identified | ✅ Shipped 2026-06-03 |
| `05-benchmark-returns.md` | Always for return stress-test | ✅ Shipped 2026-06-12 |

### 01-asset-class-norms.md — ✅ Shipped 2026-05-25

LP-perspective baseline for the 12 asset classes from `deal-evaluator.jsx`. Each row: typical hold, deal types, net-to-LP IRR range (target + realized where they diverge), risk tier; plus per-class "essential disclosures" so an absent field flags against the baseline. Uses *variable* as a real value where current-cycle norms are unstable (post-2020 office, regulatory STR, mixed-use composites). Categorical provenance — NCREIF / Preqin / ILPA / sector trade groups. Sets the format every subsequent reference follows.

### 02-fee-stack-library.md

**Content scope.** Every fee that can appear in a private real-estate or private-credit deal, grouped by category: acquisition, asset-management, disposition, financing, refinance, debt-service / servicing, promote / carry / waterfall mechanics, and miscellaneous (admin, "investor relations," K-1 prep, sponsor reimbursements). Per fee: typical range (% or $), what aggressive looks like, applicable deal types.

**Format.** Preamble + at-a-glance table (`Fee | Category | Typical range | Aggressive threshold | Applicable deal types`) + per-fee notes where mechanism needs explanation (especially American vs European waterfalls, GP catch-up, clawback). A "total drag" framework explaining how to estimate net IRR delta from a stack (compounds the way `scripts/fee_drag_calculator.py` does). Provenance footer + LAST_UPDATED.

**LP lens reminder.** Fees the LP bears vs fees the operator absorbs — keep that explicit. Skip operator-side cost-of-capital.

**DoD.** Every commonly-disclosed fee mapped; document can answer "what does a 1.5% mgmt + 20% over 8% pref cost an LP over 7 years?" via the total-drag framework; *variable* used where ranges are genuinely cycle-sensitive. <300 lines or TOC at the top.

### 03-red-flag-library.md

**Content scope.** Red flags grouped by category — (a) GP behavior: zero co-invest, prior FTC / SEC action, marketing-heavy language, rapid AUM growth without team scale-up. (b) Structural: European waterfall + high promote, no clawback, GP catch-up at 100%. (c) Financial: T-3 only / no T-12, aggressive exit cap (>50bps below acquisition), refi-dependent business plan, debt maturity inside the business plan. (d) Disclosure: missing financials, no realized exits cited, projections without sensitivity, "track record" that includes unrealized deals. (e) Market-cycle: rent growth in a slowing-cycle market, post-2020 office without occupancy-reset acknowledgement. (f) HML / private-credit specific: LTV-on-ARV without as-is value, geographic concentration, default rate hidden, recovery rate hidden, fund-level leverage stacked on top of loan leverage.

**Format.** Categorized table (`Flag | Severity yellow/red | Mechanism — why it's a flag | Response — what to ask`) + per-flag notes for the high-severity / commonly-misunderstood ones. Severity is assigned from the LP's recovery perspective.

**LP lens reminder.** Each flag is the LP's risk exposure, not an operator's underwriting concern.

**DoD.** ≥25 flags across categories; every flag has severity + mechanism + a one-line response question; HML / private-credit category present (otherwise the skill misclassifies risk on debt deals).

**Additional flags from design review (2026-06-01).**

GP behavior:
- GP IRR vs LP IRR divergence — track record cites project-level or
  GP-level IRR rather than net-to-LP IRR. Severity: RED.

Structural:
- Affiliate fee stacking — property management, construction
  management, and loan placement all flowing to GP-affiliated entities
  without disclosure or fee reduction. Severity: YELLOW–RED.
- "Financing story" disguised as asset story — LP returns driven
  primarily by leverage and cap rate compression rather than operational
  value creation. Severity: RED.

Financial:
- Cash-flow timing / J-curve not disclosed — IRR presented without
  distribution schedule; no indication of when LP capital starts
  returning. Severity: YELLOW.
- Rate cap expiry risk — floating-rate debt where the rate cap expires
  before the projected hold end or refi event. The specific 2022–2024
  failure pattern: rate cap expires, rates stay elevated, refi market
  freezes. Severity: RED.
- Exit-dependent IRR — >60% of projected LP return comes from terminal
  value / exit cap assumption rather than in-place cash flow.
  Severity: RED.

### 04-question-bank.md

**Content scope.** Questions an LP should ask the GP, grouped by category — deal-specific, GP / sponsor-specific, market-specific, fee / structure-specific, risk-specific, exit-specific. Each entry has the differentiator treatment: what a GOOD answer sounds like + what a BAD answer sounds like (the explicit evasion signals — the "what evasion looks like" that distinguishes this skill from existing question generators).

**Format.** Triplet entries — `Question / Good-answer signals / Bad-answer signals` — grouped by category. Cross-reference column or note: "ask this if [red flag] surfaced from 03-red-flag-library." Optional priority tier (must-ask / nice-to-ask).

**LP lens reminder.** Questions about the LP's own decision (capital call timing, K-1 timing, exit-distribution mechanics, secondary-market liquidity) belong here; questions about acquisition strategy or asset management belong to the operator's diligence, not the LP's.

**DoD.** ≥20 questions across categories; every question has bad-answer signals (the differentiator); ≥5 cross-references from `03-red-flag-library.md`. *Shipped 2026-06-03: 25 questions, 28 distinct flag IDs cited.*

**Additional question categories from design review (2026-06-01).**

Distribution timing:
- "What is the projected distribution schedule, and at what milestones
  does LP capital start returning?"
  Good answer: specific schedule tied to operational triggers.
  Bad answer: "We'll distribute when the deal supports it" with no
  milestones, or silence.

LP liquidity / secondary market:
- "What are my options if I need to exit before the hold period ends?"
  Good answer: named secondary platforms, stated process, realistic
  liquidity timeline.
  Bad answer: vague reference to "a secondary market may develop,"
  "we'll try to accommodate," or silence.

### 05-benchmark-returns.md

**Content scope.** Public market comparators by deal type: REITs (VNQ, IYR) for equity-style RE; investment-grade corporates (LQD) for stabilized core; high-yield (HYG) and private-credit ETFs (PRIV) for HML / private credit; preferreds (PFF) for preferred equity; broad equity (SPY) as universal anchor. Per comparator: trailing 10yr / 5yr returns with `LAST_UPDATED` date, volatility (std dev), and the best private-deal-type it serves as a comparator for. Plus an **illiquidity-premium framework**: minimum spread an LP should demand over the liquid equivalent (rule of thumb: ≥200bps over the closest public comparator, scaled by lock-up length).

**Format.** Preamble + at-a-glance comparator table (`Ticker | Trailing 10yr | Trailing 5yr | Vol | Best comparator for`) + per-comparator one-paragraph note + illiquidity-premium framework + provenance + LAST_UPDATED stamp at top.

**LP lens reminder.** Returns are net to a public-market investor (post-expense-ratio) — apples-to-apples with net-to-LP private returns. Don't compare gross to net.

**DoD.** ≥6 comparators covering every major private-deal type; illiquidity-premium framework lets the skill output "this deal's claimed net IRR exceeds [comparator] by Xbps — is that enough premium for the lockup?"; LAST_UPDATED visible so the file ages predictably and triggers a refresh task in v1.1.

**Additional DoD item (from design review 2026-06-01):**
- Include an unlevered return comparator alongside each headline ETF
  return, so the skill can distinguish "this deal clears the
  illiquidity hurdle" from "this deal's IRR is driven by leverage, not
  alpha." Without an unlevered baseline, the financing-story flag
  cannot be grounded in a benchmark comparison.

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

### Resolved (locked 2026-05-29 / 2026-05-30)

- **Output format** — **Markdown default; JSON opt-in.** SKILL.md emits structured Markdown by default; pass "output as JSON" in the prompt (or the `--json` flag to the scripts) for the JSON shape consumed by the React artifact. Markdown reads naturally in the CLI; JSON keeps the artifact and skill compatible.
- **Reference file granularity** — **5 files per CLAUDE.md naming** (outputs-focused: asset-class-norms / fee-stack-library / red-flag-library / question-bank / benchmark-returns). The older mechanics-focused list (`02-syndication-mechanics`, `03-hard-money-framework`) is retired; that content is woven into the output-focused files (waterfalls in fee-stack-library, HML mechanics in red-flag-library). Loading efficiency preserved via the load-trigger column in Section 5.
- **Domain placement** — **`finance/` for v1.0.** Propose a `private-investing/` domain expansion in the PR discussion only if the maintainer raises it; don't lead with a new-domain ask.
- **Slash command** — **Add `/cs:screen-deal`.** Consistent with other finance skills; low effort, high discoverability.
- **React artifact vs SKILL.md** — **Ship both.** Different surfaces (claude.ai chat with embedded UI vs Claude Code CLI). The artifact stays in this repo (gitignored); the SKILL.md is the upstream contribution. Documented in the README.
- **Contribution target** — **PR from `dhoovDB` fork to `alirezarezvani:dev`.** Feature branches targeting `dev`, never `main`.
- **Frontmatter tags field** *(2026-05-30)* — **Include tags.** Use the list already drafted in the §2 frontmatter sketch. Confirm the format matches other `finance/` skills in the upstream fork before the PR opens — that check belongs in the Phase 4 quality checklist, not here.
- **Benchmark data freshness** *(2026-05-30)* — **Hardcode + manual override.** Trailing figures hardcoded with a `LAST_UPDATED` constant and an annual-refresh comment. Also accept `--benchmark-return` as a manual override so users can supply current figures. No network dependency; stdlib-only constraint holds.
- **Third script (`deal_scorer.py`)** *(2026-05-30)* — **Skip v1.0; defer to v1.1+.** A composite 0–100 score adds false precision at this stage and the eval suite doesn't require it. Tracked in the v1.1+ Backlog; revisit post-evals.

### Still open

| # | Decision | Options | Lean | When to decide |
|---|---|---|---|---|
| 8 | **Asset class routing** | Single workflow / branching by deal type | Branch at Step 2 (classify); load the relevant reference file; reconverge at output | During SKILL.md build |

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

Build order (matches numbering after the 2026-05-29 reconciliation; numerical = build order):
1. `references/01-asset-class-norms.md` — factual foundation. ✅ Shipped 2026-05-25.
2. `references/02-fee-stack-library.md` — needed to write the fee analysis step. ✅ Shipped 2026-05-30.
3. `references/03-red-flag-library.md` — flag ID format `{ASSET_CLASS}-{NN}`, extended with a `GEN-` prefix for cross-asset flags (see 2026-06-01 decision log). Establishes the cross-reference convention `04` depends on. ✅ Shipped 2026-06-01 (34 flags).
4. `references/04-question-bank.md` — depends on 03 for cross-references.
5. `references/05-benchmark-returns.md` — depends on 01's asset-class IRR ranges for spread math.
6. `SKILL.md` — write last; the reference files clarify what belongs in the body vs Level 3. ✅ Shipped 2026-06-13 (185 lines / 12.8KB; routing branches by deal type per Open Design Choice #8).
7. `scripts/fee_drag_calculator.py` — ✅ Shipped 2026-06-14 (stdlib-only; pure core + I/O boundary; `--self-check` validates against `02`'s worked examples; net 10.6% on the default run).
8. `scripts/benchmark_comparator.py` — ✅ Shipped 2026-06-18 (stdlib-only; hardcoded comparators from `references/data/` + `--benchmark-return` override per design choice #3; `--self-check` validates against `05`'s spread table). **Both scripts now built.**
9. `README.md` *(skill-level, at `finance/passive-deal-screener/README.md` in the upstream PR — distinct from this repo's own root `README.md`)*.

### Phase 3: Test the skill (Claude.ai workflow, per `skill-creator` SKILL.md)

Since you're in Claude.ai (not Claude Code), subagent-based parallel evals aren't available. Use the adapted process:

1. Write `evals/evals.json` with the 9 test cases below. Each is chosen to exercise a *distinct* part of the skill so a regression in one is hard to mask. Each reference file should be built against the cases it has to support; SKILL.md should pass all nine before the upstream PR opens.

   | # | Case | What it exercises |
   |---|---|---|
   | 1 | Multifamily value-add equity syndication, full offering memo | The default path — happy-case parsing on a complete deal package. Tests deal-snapshot extraction, fee-stack breakdown, GP track record, exit-cap stress-test. |
   | 2 | Preferred equity deal, sparse email blast | Source-agnostic parsing + missing-disclosures-as-output. The skill should classify it, flag what's absent, and ask the right questions despite the thin input. |
   | 3 | Hard money / bridge debt fund (platform listing) | Debt-fund workflow branch. Tests `03-red-flag-library`'s HML category (LTV-on-ARV claims, geo concentration, default-rate disclosure). |
   | 4 | Private credit fund with sector concentration risk | Fee-stack and red-flag interaction. Tests `02-fee-stack-library`'s debt-fund fee subsection + the credit-specific red flags. |
   | 5 | Development (ground-up) deal with aggressive return projections | Return stress-test against `01-asset-class-norms` development baseline and `05-benchmark-returns` comparators. Tests the illiquidity-premium framework. |
   | 6 | Office deal in 2026 | Tests the `01-asset-class-norms` *variable* baseline. Output should refuse to give a generic baseline and instead drive the analysis off the deal's own underwriting (occupancy, class, debt maturity). |
   | 7 | Deal with obvious GP red flags | Multi-flag detection: prior FTC action mentioned, zero co-invest, European waterfall + 50% promote, projections without sensitivity. The skill must list them all with severity. |
   | 8 | Deal missing nearly all disclosures | Worst-case missing-disclosure case. Output should be 80% "here's what wasn't said" rather than vacuous "looks fine." Tests that absence is first-class. |
   | 9 | Two deals with identical projected IRR: one distributes cash flow quarterly from Year 1, one back-loads all return to exit | Tests whether the skill flags J-curve difference and distribution timing as material LP risk rather than treating the deals as equivalent on IRR alone |
   | 10 | Clean, sound equity syndication | False-positive / discrimination test — a well-structured deal where the correct output is "looks solid, minor clarifying questions." Without it we can't separate discrimination from reflexive pessimism. |
   | 11 | Clean, sound private-credit fund | Second clean case, in the *debt* branch — proves the skill can say "solid" in both equity and credit, not just one clean archetype. |

   **Expanded to 11 cases (2026-06-19):** added cases 10–11 (clean deals → false-positive testing) and split case 3 into a sound/problematic hard-money contrast pair (3a→Pursue, 3b→Pass, demonstrating the skill discriminates *within* a deal type). The authoritative case matrix, four-part pass criteria, source tiers, and circularity rationale now live in **`evals/TESTING-PLAN.md`**; this table is the summary.

   Hold each test input in `evals/inputs/NN-<slug>.md`; reference materials (real anonymized deals, where shareable, or constructed synthetic equivalents) cited in `evals/sources.md`.

2. For each test case, load SKILL.md yourself and follow the workflow against the test input. Record outputs in `evals/iteration-1/`.

3. Review: does each output correctly classify the deal, surface the right flags, generate useful questions?

4. Iterate on SKILL.md and reference files. Aim for 2-3 iteration cycles before PR.

5. Optimize the description frontmatter for triggering accuracy — confirm it fires on phrases like "analyze this deal", "is this worth pursuing", "what should I ask the GP".

### Phase 4: Quality checklist (from `SKILL-AUTHORING-STANDARD.md`)

Before opening the PR, verify:

- [ ] SKILL.md is **≤10KB** (the binding cap from `SKILL-AUTHORING-STANDARD.md` — ≈160 lines at the 58–64 bytes/line of shipped `finance/` skills; the largest, `business-investment-advisor`, sits at exactly 10.0KB/159 lines). The old "<500 lines" figure was ~3× too loose and is retired. **Current draft is 12.8KB / 185 lines — ~2.8KB over; resolve via a compression pass or a documented divergence rationale before the PR.**
- [ ] Frontmatter has `name`, `description`, `author`, `license` (this skill follows the standard's `metadata:` block: `version`/`author`/`category`/`updated`; `tags` carried per the 2026-05-30 decision — confirm against merged `finance/` PRs, since shipped finance skills omit them)
- [ ] Description is written in third person
- [ ] Description includes both what the skill does AND trigger contexts
- [ ] All Python scripts run with `python3 script.py --help` (zero pip installs)
- [ ] Reference files are linked from SKILL.md with explicit load guidance
- [ ] README.md includes install instructions and usage examples
- [ ] No hardcoded API keys, credentials, or personally identifying information
- [ ] Skill passes the security auditor: `python3 engineering/skill-security-auditor/scripts/skill_security_auditor.py finance/passive-deal-screener/`

**v1.0 ship gate (in addition to the standard checklist above).** The upstream `SKILL-AUTHORING-STANDARD` covers file conventions; the items below are the *content* gates specific to this skill — the standard doesn't know about reference files or evals at this depth.

- [ ] References `01–05` all built; each ≤300 lines (or with internal TOC); LP-lens only; *variable* used honestly where ranges are unstable
- [ ] Cross-reference integrity: each `03-red-flag-library` entry carries a flag ID in format `{ASSET_CLASS}-{NN}`; `04-question-bank` entries each cite ≥1 flag ID; `04` as a whole cites ≥5 distinct entries from `03`
- [ ] `examples/` has ≥3 input/output pairs covering different deal types (e.g. multifamily equity, hard money / bridge fund, preferred equity)
- [ ] `evals/evals.json` carries the 11 cases from Phase 3 / `evals/TESTING-PLAN.md` (9 original + 2 clean deals; case 3 is a sound/problematic pair → 13 input fixtures); SKILL.md passes all 11 after ≥2 iteration cycles, with iteration logs in `evals/iteration-N/`
- [ ] This repo's own `README.md` (root) reflects the shipped state and points users to the upstream skill location
- [ ] Decision log captures every resolved design choice with rationale (reviewers see the *why*, not just the *what*)

### Phase 4.5: PR Readiness

Before opening the PR, complete these steps in order.

**Step 1 — Read merged PRs in `finance/`, not just the skills.**

The PR discussion thread is where maintainer preferences surface. Read 2–3 recently merged `finance/` PRs. Note any review comments, requested changes, or patterns in what got pushed back.

**Step 2 — Map every divergence between this skill and their patterns.**

For each place where passive-deal-screener differs from the existing `finance/` skills (structure, depth, tone, file count, frontmatter, output format), write one line: what is different and why.

**Step 3 — Make a call on each divergence.**

If it is not defensible: align to their pattern before opening the PR. If it is defensible: that line becomes your response if a maintainer asks. Keep it in the decision log.

**Step 4 — Confirm the decision log is complete.**

Every intentional divergence should have a rationale entry dated before the PR opens. Reviewers see the why, not just the what.

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

## v1.1+ Backlog (parking lot — not committed)

Items that don't block v1.0 but inform later versions. Promote to §12 Versioning Plan when a version targets them.

- **`deal_scorer.py`** — composite 0–100 deal score for comparing multiple deals side by side. Deferred from v1.0: false precision risk; eval cases don't require it. Revisit post-evals.
- **Sector deep-dives** — senior housing, self-storage, industrial. Candidates for additional reference files once the core four asset classes (multifamily, hard money, preferred equity, private credit) are validated against real deal flow.
- **Multi-agent specialist split** — separate agents for fee analysis, red-flag detection, and GP evaluation. Requires the v1.0 eval baseline first so a split can be measured against the monolithic SKILL.md.
- **`06-syndication-mechanics-deep-dive.md`** — only if eval cases expose gaps in waterfall / promote / clawback coverage that can't be addressed by expanding the subsection inside `02-fee-stack-library.md`.
- **Enforced refresh of `references/data/`** — the snapshot layer (built 2026-06-06) currently ages on an *honor system*: a `LAST_UPDATED` / `As of` stamp per file and the README's manual refresh procedure, but nothing detects or enforces staleness. Two-phase research item:
  - *Phase 1 (earlier, lighter): a staleness warning.* Surface a warning when time-since-last-refresh on any snapshot exceeds a material threshold (the 10yr Treasury is the most time-sensitive; ETF/NCREIF figures age over quarters). Mechanism TBD — could be a read of the `As of` stamps emitted when the skill loads `05`, or a check the data files carry themselves. Goal: the skill (or a contributor) gets told "this benchmark data is N months stale" rather than silently comparing against old numbers.
  - *Phase 2 (later, heavier): enforced refresh.* A date-check script and/or a scheduled job (cron / CI) that fails or nags when snapshots pass their refresh cadence. Decide script-vs-schedule then. Depends on Phase 1 defining the staleness thresholds. Note the constraint: the upstream repo is stdlib-only Python and issuer fact sheets / FRED 403 automated fetch, so an *auto-pull* refresh isn't trivially scriptable — the enforced piece is more likely "detect staleness + prompt a human re-pull" than "fetch and overwrite."

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

### 2026-05-29 — ROADMAP buildout: schemas, numbering, gates

Following the first reference shipping, the ROADMAP shifted from "what we plan to build" to "what each unbuilt artifact needs to contain." Four interlocking changes landed in one pass:

- **Reference-file numbering reconciled to CLAUDE.md.** The older ROADMAP §5 list (mechanics-focused: `syndication-mechanics`, `hard-money-framework`, `fee-stack-decoder`, `gp-evaluation-rubric`) is retired in favor of the CLAUDE.md outputs-focused list (`fee-stack-library`, `red-flag-library`, `question-bank`, `benchmark-returns`). CLAUDE.md was authoritative anyway; this aligns the planning doc to it. The mechanics content (waterfalls, LTV / ARV / draw schedules) lives as subsections within the relevant output-focused file — waterfalls in fee-stack, HML mechanics in red-flag-library, etc. Trade: slight loss of standalone discoverability for syndication mechanics; gain: every reference is anchored to a *skill output* the workflow produces.
- **Per-file content schemas defined up front for `02–05`.** Each unbuilt reference now has scope, format, LP-lens reminder, and DoD pinned in §5 before writing starts. The lesson from building `01` solo: improvising the schema mid-write produces a defensible file, but locking the schema across the set up front guarantees compatibility (column names match, provenance pattern matches, *variable* discipline applies uniformly). The schema also de-risks the SKILL.md write: SKILL.md doesn't ship until the references it indexes against have the shape it expects.
- **Eight specific eval cases enumerated** in §8 Phase 3, one per distinct skill behavior — happy case (full memo), sparse input, debt fund, private credit, aggressive returns, *variable* baseline (office in 2026), multi-red-flag deal, near-total disclosure absence. Each reference must be built against the case it has to support; SKILL.md ships when all 8 pass.
- **v1.0 ship gate split from the upstream `SKILL-AUTHORING-STANDARD` checklist.** The upstream standard covers file conventions (frontmatter shape, script `--help`, security auditor); this skill needs *content* gates the standard doesn't know about (5 references built, 8 evals passing, ≥3 examples, cross-reference integrity between `03` and `04`, this repo's own README updated). Phase 4 now carries both checklists.

Open design choices in §7 collapsed from 10 to 4 — six were resolvable now and are recorded as locked. The remaining four (frontmatter tags, benchmark data freshness, third script, asset class routing) each have a clear "when to decide" anchor so they don't get re-litigated.

### 2026-05-29 — Repo-level README.md added

The repo has been public on GitHub since creation but had no front door — anyone landing on it from a portfolio link or search got CLAUDE.md (a dev guide), not a "what is this and who's it for" page. The new root `README.md` is the portfolio-facing introduction: skill name, the differentiated LP-perspective stance, current pre-development status (with the `01` reference already shipped), repo layout, contribution target, and a preview of the workflow the shipped skill will produce. Distinct from the eventual *skill-level* README at `finance/passive-deal-screener/README.md` in the upstream PR — that one carries install instructions and usage examples and ships only once SKILL.md exists.

### 2026-05-30 — Decisions following the strategy session

These resolve the remaining §7 open choices and add several conventions surfaced in the strategy session. Where a row duplicates a 2026-05-29 prose entry (output format), both are kept — the table is the formal record; the prose carries the narrative.

| Date | Decision | Rationale |
|---|---|---|
| 2026-05-30 | Include frontmatter tags | Additive; format-check against upstream deferred to Phase 4 quality checklist |
| 2026-05-30 | Default output: structured Markdown; JSON opt-in via explicit instruction | SKILL.md serves CLI/multi-platform consumers; React artifact is separate surface |
| 2026-05-30 | Benchmark scripts: hardcode with LAST_UPDATED constant + --benchmark-return override | Stdlib-only constraint; no network dependency; user can supply own figures |
| 2026-05-30 | deal_scorer.py deferred to v1.1+ | False precision at this stage; eval cases don't require it |
| 2026-05-30 | No 06-syndication-mechanics file for v1.0 | Waterfall mechanics live as subsection in 02-fee-stack-library; if 02 runs long, tighten it |
| 2026-05-30 | 05-benchmark-returns.md requires data pull before writing | NCREIF NPI, FRED 10yr, Preqin vintage note; all figures timestamped at build time |
| 2026-05-30 | Flag ID convention: {ASSET_CLASS}-{NN} | Stub 03 with IDs before entries; 04 entries must cite ≥1 flag ID; prevents PR retrofit pass |
| 2026-05-30 | Anonymized deal samples in examples/; data snapshots in references/data/ | Real artifacts grounded in practice; deal-evaluator.jsx test runs excluded (gitignored surface) |

### 2026-05-30 — Built `references/02-fee-stack-library.md`

Lands the second reference and the heaviest one in v1.0 — fee inventories across four deal types, waterfall mechanics, total-drag framework. Six non-obvious calls worth recording:

- **Spine is deal type, not asset class.** Multifamily and industrial syndications share the same fee shape; the divergence is whether the deal is equity, preferred equity, hard money, or private credit. The 12 asset classes from `01-asset-class-norms.md` don't drive `02`'s subsections — they fold into a single "applies to" column on each fee row.
- **`Frequency` is a 6th column on every fee row.** The user-spec'd 5 fields (Fee / Range / Aggressive threshold / Applies to / Notes) silently equates one-time and annual recurring fees, which lands very differently on LP IRR drag. Making Frequency visible per row keeps the drag math derivable from the table alone.
- **Waterfall mechanics live as an H3 inside Equity Syndications**, not a standalone H2. Reasoning: waterfalls determine how promote pays; promote is an Equity fee; co-locating keeps the reader's mental model intact. Preferred Equity gets a smaller H3 that cross-refs rather than duplicates. *Trade-off:* a standalone H2 would give the topic more skim-visibility but invites scope creep toward the deferred `06-syndication-mechanics-deep-dive.md`.
- **Plain-English-first framing for waterfall terms.** The canonical industry jargon (American / European) appears parenthetical to the descriptive labels (deal-by-deal / whole-of-fund) on first mention. Reader who knows the jargon gets the cross-reference labels; reader who doesn't learns them inline.
- **Development-deal fee variations as an H3 inside Equity**, not a 5th deal-type H2. Same reasoning as waterfall — co-locating keeps scope contained. Eval case #5 will surface whether this depth holds; if not, promote to its own H2 in v1.1.
- **Worked examples use two IRR scenarios (12% and 15% gross)** instead of one. The promote drag scales non-linearly with gross IRR — showing both demonstrates that the same waterfall structure compresses or widens the gross-to-net spread depending on outcome. A single example would risk implying linear drag.

File lands at exactly 300 lines (the convention's TOC threshold is *strictly* >300, so no TOC required). If `03–05` exhibit similar density, the convention may need a revisit — but for now `02` is well-organized enough that scanning the H2 hierarchy serves as a de facto TOC.

### 2026-06-01 — Design review: output schema, analyst rules, and flag gaps

Following a structured design review against LP practitioner feedback and
comparative analysis (Perplexity), several categories of gaps were identified
and addressed in this pass:

1. Output schema specified. The SKILL.md body outline's `## Output schema`
   placeholder is now a 10-section required output structure. The most
   critical addition is Section 3 (Where LP Returns Come From), which forces
   the skill to decompose cash flow vs exit vs leverage — the "financing story"
   detection that no existing LP skill performs.

2. Analyst rules specified. The skepticism contract is now explicit: adversarial
   posture by default, no gross-to-gross comparisons, automatic flagging when
   IRR is exit-dependent or leverage-dependent, unrealized track record treated
   as unverified.

3. Red flag library expanded. Six new flags added to the planned 03 scope:
   GP IRR vs LP IRR divergence, affiliate fee stacking, financing story,
   cash-flow timing / J-curve absence, rate cap expiry risk, and
   exit-dependent IRR. All were absent from the original 03 content scope.

4. Question bank expanded. Two new question categories added to 04 scope:
   distribution timing (with bad-answer signals) and LP liquidity / secondary
   market access (with bad-answer signals).

5. Benchmark returns file refined. 05 DoD now requires an unlevered return
   comparator alongside each ETF figure, enabling the skill to ground the
   financing-story flag in a benchmark comparison rather than assertion alone.

6. Eval case #9 added. Tests J-curve / distribution timing analysis — the one
   gap in the original 8-case suite.

### 2026-06-01 — Built `references/03-red-flag-library.md` (third reference file)

Lands the red-flag library — 34 flags across the six planned categories (GP
behavior, structural, financial, disclosure, market-cycle, hard-money/private-
credit), comfortably clearing the ≥25-flag DoD. Every flag carries an ID,
severity (14 RED / 12 YELLOW / 8 YELLOW–RED), a one-line mechanism, and a
one-line response question — the response questions are the seeds `04-question-
bank.md` will cite by ID. The six design-review flags added to scope earlier
today (GEN-05 GP-vs-LP IRR, GEN-06 affiliate stacking, GEN-07 financing story,
GEN-08 exit-dependent IRR, GEN-10 rate-cap expiry, GEN-11 J-curve) are all in
with their committed severities. Three non-obvious calls:

- **Flag-ID scheme extended with a `GEN-` prefix — divergence from the §8
  build-order line.** The build order specified four asset-class prefixes
  (`EQUITY`, `HML`, `PREF`, `CREDIT`). But the largest categories — GP behavior,
  disclosure, most structural/financial/market-cycle flags — apply across *all*
  deal types, and forcing them under `EQUITY-` would misrepresent their scope.
  Resolution: `GEN-` for cross-asset flags (19 of 34), asset-class prefixes only
  where a flag is genuinely asset-specific (EQUITY 7, HML 5, CREDIT 2, PREF 1).
  The ID still encodes scope-of-applicability, which is *more* useful to `04`
  than an asset-class label would be. Defensible divergence; logged here so a
  reviewer sees the why.
- **Severity is RED / YELLOW / YELLOW–RED, the third for boundary flags whose
  severity depends on the GP's answer** (e.g. affiliate stacking, refi
  dependence, missing financials). Mirrors the YELLOW–RED usage already in
  `02-fee-stack-library.md` rather than inventing a new scale.
- **No new numeric thresholds invented.** Where a flag needs a trigger it
  borrows one already established in `02` (promote >30%, pref <6%) or a
  committed analyst rule (exit-dependent IRR >60%); otherwise the flag describes
  the *pattern* and defers to the deal's own underwriting, per the "no
  hallucinated ranges" rule. `GEN-17` is an explicit pointer into `01`'s
  per-class essential disclosures rather than a duplicated list.

File lands at 233 lines with a Contents section up top — under the 300-line TOC
threshold, but the six-category structure benefits from the index, which also
doubles as the flag-ID lookup for `04`.

### 2026-06-03 — Built `references/04-question-bank.md` (fourth reference file)

Lands the question bank — 25 LP questions across the eight planned categories
(deal, GP/sponsor, market, fee/structure, risk, exit, plus the two
design-review additions: distribution timing and LP liquidity/secondary).
Comfortably clears the ≥20-question and ≥5-cross-reference DoD: 28 distinct
flag IDs from `03-red-flag-library.md` are cited, every one resolving to a real
entry. File lands at 227 lines with a Contents index up top — under the
300-line TOC threshold, but the eight-category structure benefits from the
index. Three non-obvious calls worth recording:

- **The bad-answer signal is treated as the deliverable, not the question.**
  ROADMAP §6.4 names this the skill's sharpest differentiator. The discipline
  applied: every bad-answer cell names the *specific* dodge for that question —
  the substituted metric, the redirect, the silence — never a generic "they
  were evasive." A bad signal that could be pasted under any question was
  rewritten until it could only belong to its own.
- **`Q-<CAT>-NN` ID scheme, parallel to `03` but category-keyed.** `03` encodes
  scope-of-applicability in its prefix (GEN/EQUITY/HML/…); `04` encodes
  *category* (DS/GP/MKT/FEE/RISK/EXIT/DIST/LIQ) because that's the axis a reader
  navigates a question bank on. Cross-reference flows one way — `04` cites `03`
  flag IDs, never the reverse — so the two ID schemes don't need to align.
- **Two categories carry no `03` cross-reference by design.** Distribution-call
  mechanics (Q-DIST-02), secondary-market liquidity (Q-LIQ-01), and K-1 timing
  (Q-LIQ-02) concern the LP's *own* cash-management and tax decision, not a deal
  defect — so they have no matching flag. This is the LP-lens boundary made
  concrete: `03` is scoped to the deal's risks, while the LP's liquidity and tax
  timing are equally part of commit-or-pass. An "—" in the ref column is
  intentional, not a missing citation.

Build order now has only `05-benchmark-returns.md` remaining before SKILL.md;
`05` stays gated on the NCREIF/FRED/Preqin data pull (2026-05-30 decision).

### 2026-06-12 — Built `references/05-benchmark-returns.md` (final reference; reference set complete)

Lands the fifth and last reference — the public-market benchmark layer that turns
every analysis into a forcing function: a private deal must clear a liquid,
net-of-fee comparator plus an illiquidity premium, or the lock-up isn't
compensated. Pure **synthesis**: every figure traces to `references/data/`
(built 2026-06-06) or `01`'s net-IRR ranges; `05` sources nothing itself. Carries
8 comparators, the spread table mapping each `01` asset class to its
risk-matched comparator with an approximate premium band, the illiquidity-premium
framework (≥200bps floor scaled by lock-up), and the NCREIF-NPI unlevered overlay
that grounds the financing-story flag (`03` → `GEN-07`) in a benchmark. The two
decisions flagged when the data layer shipped both resolved toward honesty over
precision:

- **Volatility column → relative-to-baseline, not a fabricated number.** The
  planned vol pull found no clean uniform annualized std-dev publicly available
  (fact sheets 403; aggregators mix daily / 1yr / 3yr / since-inception bases).
  Forcing a numeric column would be false precision the skill forbids. First pass
  used a coarse High/Med/Low tier; on review that flattened the key signal (SPY
  and the REITs all read "High"), so the final resolution expresses each
  comparator **relative to the SPY equity baseline** plus a **drawdown contrast** —
  surfacing that REITs carry ≈ equity volatility with a *deeper* tail (−73% vs
  −55%) for *lower* return. This makes the baseline load-bearing. The snapshot vol
  gap is closed with this resolution (snapshot is source of truth; `05`
  synthesizes from it). Both files travel in one commit.
- **IYR/LQD ranges carried as ranges.** No false-precision single number; VNQ is
  the primary REIT comparator, IYR the cross-check, per the snapshot's designation.
- **VTI added as a second broad-equity anchor (8th comparator).** Total-market
  alternative to SPY — near-substitute (14.88% vs 15.54% 10yr, ≈ same vol and
  −55% drawdown) but cheaper (0.03%) and arguably the truer "all equity dollars"
  opportunity cost. Treated as an *anchor*, not a private-type comparator: it gets
  no spread-table row (maps to no distinct exposure), only the at-a-glance,
  per-comparator notes, and the vol-vs-baseline framing. Logged so a reviewer sees
  it's a deliberate anchor, not redundant clutter.
- **Treasury short points added for duration-matched debt floors.** The 10yr was
  already the risk-free anchor; added 3mo (≈3.71%) and 2yr (≈4.15%) points to
  `fred-10yr-snapshot.md` so debt deals get a *duration-matched* floor (a 6–18mo
  hard-money fund's honest risk-free comparison is the bill, not the 10yr). `05`
  now reads a debt deal's net yield over the matched Treasury as the credit +
  illiquidity spread — the credit-analyst lens, complementing HYG (which embeds
  the HY credit spread) by isolating the absolute risk premium. Treasury remains
  the *anchor/floor*, not a comparator row — comparator count stays 8.

*Variable* `01` classes (office, experiential retail, STR, mixed-use) deliberately
get **no** spread-table row — a forced comparator would be false grounding; they
benchmark against the deal's own underwriting. File carries a TOC up top.

**Reference set (`01`–`05`) is now complete.** Build order advances to SKILL.md
(the body that indexes against these five), then the two stdlib-only Python
scripts, the eval suite, and the skill-level README.

### 2026-06-19 — Wrote `evals/TESTING-PLAN.md` + `evals/sources.md` (eval scaffolding before the suite)

Before building the 9 eval inputs, wrote the testing plan that governs them — so the
fixtures are built against an explicit method, not improvised. Two structural changes
to the eval design, both at the user's direction, plus a research pull:

- **Expanded to 11 cases.** Added two *clean/sound* deals (case 10 equity, case 11
  private credit) — the original 9 only tested *misses* (false negatives); nothing
  tested *false positives*. A screener that flags every deal is useless even if it
  never misses. The two clean cases span equity and credit so the discrimination test
  covers both branches.
- **Case 3 (hard money) is now a sound/problematic contrast pair** (3a real → Pursue,
  3b synthetic → Pass) — proving a "varies" verdict is real discrimination on the
  facts, not a dodge. Parallels case 9's existing pair structure. 11 cases, 13 input
  fixtures.
- **Pass criteria made explicit, four universal checks**: correct classification,
  caught the target flag IDs, generated the right `04` questions, and
  *missing-data-fires-as-output* (when a deal lacks what a flag needs, the skill must
  say so and route it to a must-ask, never stay silent) — plus two conditional checks
  (Tier-4 "flagged what actually broke the deal"; clean-case "no manufactured RED").
- **Circularity named as a first-class risk.** If one author writes both the flag
  definitions (`03`) and the synthetics that trip them, the test is tautological.
  Resolution stated in the plan: synthetics validate *mechanics*; the Tier-4 real
  failures and the real clean deals — which we did not author — validate *real-world
  accuracy*.
- **Live research populated `sources.md`** (facts/URLs only, names scrubbed from
  fixtures per the public-repo rule): Groundfloor Reg A LRO circular (case 3a),
  Fundrise eREIT circulars (case 1/10), Blue Owl OBDC 424B2 (case 11 clean credit),
  the Nightingale/CrowdStreet misappropriation and Applesway/Tides 2022–24 multifamily
  distress (Tier-4 overlays for cases 7/1/5), and 2025–26 office repricing (case 6).

`TESTING-PLAN.md` is the authoritative case matrix; ROADMAP §8's table is now the
summary. Next: build the 13 input fixtures + `evals.json`, then run the suite.

### 2026-06-18 — Built `scripts/benchmark_comparator.py` (build step 8; both scripts now built)

Implements the `05-benchmark-returns.md` forcing function as a tool: deal type +
net-to-LP IRR + hold -> the risk-matched public comparator, the premium the deal
implies over it, and whether that premium clears the lock-up's illiquidity hurdle.
Same shape as `fee_drag_calculator.py` (pure data + pure core + thin I/O boundary,
`--self-check`, zero-arg demo). Implements the *already-resolved* design choice #3
(hardcode + override); the build-time calls worth recording:

- **Comparator figures hardcoded from `references/data/` with a `LAST_UPDATED`
  constant**, plus `--benchmark-return` to override with a current number — exactly
  the 2026-05-30 design-choice-#3 resolution. The data lives in module-level dicts
  (config-is-data, no logic), so a v1.1 refresh is "edit the constants + bump the
  stamp," and the figures trace to `etf-comparators-snapshot.md` /
  `fred-10yr-snapshot.md`.
- **Deal types map to comparators per `05`'s spread table** (RE equity -> VNQ,
  debt -> HYG, preferred -> PFF). `--list-types` enumerates them; an unknown type
  errors to stderr with exit 2 rather than guessing.
- **"Variable" classes (office, experiential-retail, STR, mixed-use) return guidance,
  not a forced comparator** — preserving the `01`/`05`/SKILL.md stance that their
  honest baseline is the deal's own underwriting. Forcing a comparator would be the
  false grounding the skill forbids.
- **Debt deals also report the duration-matched Treasury floor** (hard-money over
  the 3mo, private-credit over the 2yr) — the absolute credit + illiquidity spread,
  complementing the HYG credit-spread comparator, per `05`'s credit-analyst lens.
- **Illiquidity hurdle uses `05`'s tier band** (~200 / ~300-400 / ~400-600 bps by
  lock-up) reported as a range; `--illiquidity-premium-assumed` overrides it with a
  single user figure. Verdict is a three-state read (fails / thin / clears
  comfortably) against the band.

Verified by execution (Python 3.12.10): `--self-check` PASS against `05`'s spread-table
anchors (mf value-add 653bps clears; preferred 228bps thin; hard-money 400bps + 529bps
3mo-Treasury floor; office -> variable), plus `--help`, `--json`, `--list-types`, the
ROADMAP example, and the unknown-type error path. Output is ASCII-clean for non-UTF-8
consoles (the em-dash-portability lesson from the 2026-06-14 script, reapplied).

**Both scripts (steps 7-8) are now built and verified.** Build order advances to the
eval suite (ROADMAP §8 Phase 3, 9 cases), with the SKILL.md compression to <=10KB still
owed before the PR.

### 2026-06-14 — Built `scripts/fee_drag_calculator.py` (build step 7; first executable artifact)

Turns `02-fee-stack-library.md`'s "Total-drag framework" from prose into a
deterministic tool. stdlib-only (`argparse`/`json`/`sys`); structured as a pure
calculation core (`recurring_drag_bps`, `one_time_drag_bps`, `promote_drag`,
`compute_fee_drag`) behind a thin I/O boundary (`parse_args`/`format_human`/`main`),
per the portfolio's engine-pure / IO-at-the-boundary rule. Four non-obvious calls:

- **Additive drag model, matching `02`.** Net IRR ≈ gross − recurring(annual %) −
  one-time(% ÷ hold) − promote, each in bps. This mirrors `02`'s worked example
  line-for-line (and slightly overstates total drag vs a full sequential waterfall —
  the conservative direction for a screening tool). The bare run reproduces `02`'s
  headline example: 15% gross multifamily, 7-yr, full stack → **net 10.6%** (`02`
  says ~10.5–11%).
- **Promote via a real bullet-exit waterfall**, not a hand-wave: return-of-capital +
  simple pref → GP catch-up scaled by `--catch-up` → residual carry split, computed
  on profit then annualized. Verified anchors: ~184bps @12% gross, ~217bps @15%
  (`02` hand-estimates ~150/~200; the script computes the actual compounding
  waterfall, so it reads a touch higher — documented, not a bug). Surfaces the LP
  lesson that a **100% catch-up makes the pref timing-only**, not a final-split
  change (drop catch-up to 0 and LP net rises 10.6%→11.4%, GP share 20%→13%).
- **`--self-check` is the test layer.** Stdlib-only means no pytest; the mode asserts
  the worked example lands in 10.4–11.0% and the promote anchors fall in band, exiting
  non-zero on regression. Satisfies the "validate against `02`" DoD without a test
  framework, consistent with the upstream "sample data embedded" Pattern 10.
- **Defaults reproduce `02`'s example**, so a zero-arg run is a live demo (Pattern 10).

Verified by execution (Python 3.12.10, installed this session — the machine had only
Windows Store stubs): `--help`, `--self-check` (PASS), bare run, `--json`, and the
below-hurdle edge case all behave correctly; output is ASCII-clean for non-UTF-8
consoles. Full-waterfall promote modeling (American vs European tiers) deferred to
v1.1 per the "screening heuristic, not underwriting" stance. Build order advances to
step 8, `benchmark_comparator.py`.

### 2026-06-13 — Built `SKILL.md` (the keystone; reference set now drives a workflow)

Lands the skill body — the Level-2 workflow that indexes against the five
references rather than restating them. Built accuracy-first per an explicit
instruction to optimize quality before length. Resolves Open Design Choice #8 and
reconciles the ROADMAP's analytical framework with the upstream
`SKILL-AUTHORING-STANDARD.md`. Six non-obvious calls:

- **Open Design Choice #8 (asset-class routing) resolved → branch by deal type.**
  A two-axis classify: *asset class* drives the `01` baseline and `05` comparator;
  *deal type* drives the `02` fee section and `03` flag prefixes. The deal type is
  the spine (per `02`'s "spine is deal type" model), so a single routing table maps
  deal type → fee section → flag prefix → comparator, then every type reconverges on
  the same 10-section output. `#8` moves from "Still open" to resolved.
- **Workflow and output schema unified, not duplicated.** ROADMAP §3 specs both an
  8-step workflow and a 10-section output schema; transcribing both verbatim would
  duplicate ~half the content and blow the byte budget. The body carries a tight
  3-step workflow (classify → route → assemble) feeding the 10-section schema as the
  deliverable spine. The detailed §3 prose stays here as the spec.
- **Frontmatter follows the standard's `metadata:` block**, not ROADMAP §2's flat
  `author/license/tags/agents` draft — three different shapes existed (§2 draft, the
  standard's template, and the *actual* shipped `financial-analyst` which uses only
  `name`+`description`). Chose the standard (authoritative DNA doc): `name`,
  `description`, `license`, `metadata{version,author,category,updated}`. Kept `tags`
  (locked 2026-05-30, additive); dropped `agents` (in neither the standard nor any
  shipped finance skill). Empirical tags-vs-shipped-skills check deferred to Phase 4.5.
- **Size cap corrected: ≤10KB binds, not "<500 lines."** Measuring shipped `finance/`
  skills (58–64 bytes/line; largest = `business-investment-advisor` at exactly
  10.0KB/159 lines) showed the standard's ≤10KB ≈ 160 lines — the old "<500 lines"
  gate was ~3× too loose. Phase 4 checklist updated. The draft lands at **12.8KB /
  185 lines, ~2.8KB over** — accepted now (accuracy-first), flagged for a compression
  pass or documented divergence before the PR.
- **Zero market numbers in the body.** Every fee range, IRR, flag, and benchmark
  routes to a reference — enforcing the "no hallucinated ranges" rule structurally
  (the body *can't* drift from the references because it cites, never restates). The
  only number-shaped text is one illustrative example distinguishing specific from
  generic risk phrasing.
- **Forward references to `scripts/*.py` (build steps 7–8, not yet built).** Consistent
  with `02`/`05`, which already cite `fee_drag_calculator.py`. Creates a temporary
  dangling pointer in the repo until the scripts land; resolves when they do, and the
  upstream PR bundles all of it so the skill never ships with broken links.

Cross-reference integrity verified at build time: every flag ID (`GEN-*`, `EQUITY-*`,
`PREF-*`, `HML-*`, `CREDIT-*`) and question ID (`Q-FEE-03`, `Q-MKT-02`) cited in the
body resolves to a real entry; the "34 flags / 25 questions" counts match `03`/`04`.
Build order advances to the two scripts, then evals, then the skill-level README.

### 2026-06-06 — Built the `references/data/` snapshot layer (the `05` data pull)

`05-benchmark-returns.md` was gated on a data pull (2026-05-30 decision: "requires
data pull before writing — NCREIF NPI, FRED 10yr, Preqin vintage note; all figures
timestamped at build time"). That layer now exists as a versioned, source-cited
snapshot folder so every number in `05` traces to a dated snapshot and a v1.1
refresh is "re-pull into the snapshots," not "rewrite the prose" — the
"no hallucinated ranges" rule enforced at the data boundary. Five files:
`data/README.md` (convention + refresh procedure), `fred-10yr-snapshot.md`,
`etf-comparators-snapshot.md`, `ncreif-npi-snapshot.md`, `preqin-vintage-note.md`.
Three non-obvious calls:

- **Added a 4th snapshot (`etf-comparators-snapshot.md`) beyond the three named in
  §2 — defensible divergence.** §2's folder sketch lists only NCREIF / FRED /
  Preqin, but `05`'s headline comparator table is ETF-driven (VNQ, IYR, LQD, HYG,
  PFF, SPY, PRIV). Snapshotting only the institutional inputs would leave the
  *bulk* of `05`'s numbers with no provenance — guarding the side door, not the
  front. §2's list predates the design-review work that made `05`'s table
  ETF-driven; it's stale, not authoritative. Approved 2026-06-06.
- **Figures come from cross-checked aggregators, not issuer pages.** iShares,
  Vanguard, SSGA fact sheets and FRED's own pages all return HTTP 403 to
  automated fetch. WebSearch reliably surfaces those figures with sources, so each
  ETF return was confirmed across ≥2 aggregators; material divergences (IYR 5/10yr,
  LQD 5yr) are *shown as ranges with a flag*, not silently resolved to one number.
- **Gated sources marked honestly, not fabricated.** NCREIF property-level detail
  and Preqin's live per-vintage quartile tables are paywalled. The snapshots
  capture the latest *publicly reported* headline (NCREIF Q4 2025 NPI; CAIS-cited
  Preqin dispersion, 2001–2017 window) and flag the rest categorical — a
  documented gap is a correct output; an invented number is a defect. PRIV
  likewise flagged as too new (Feb-2025 inception) for a trailing return.

Known gap logged for the next refresh / the `05` build: per-ticker volatility
(std-dev) was not captured this pull; populate from fact sheets when `05`'s `Vol`
column is written. Build order now: `05-benchmark-returns.md` is unblocked and is
the next file, then SKILL.md.

---

*Generated from conversation context: passive real estate investing learning path, LP/GP structure, hard money lending, EquityMultiple analysis, fee drag mechanics. The analytical framework is grounded in the investor's background (commercial credit analyst, STR operator) and goals (passive LP, not operator).*

*Last updated: 2026-06-19 (eval scaffolding written — evals/TESTING-PLAN.md + evals/sources.md; suite expanded to 11 cases / 13 fixtures. Next: build the input fixtures + evals.json, then run the suite; SKILL.md compression to ≤10KB still owed. PR note: user wants a detailed PR summary when feat/skill-md is opened.)*
