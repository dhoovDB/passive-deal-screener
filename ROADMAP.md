# passive-deal-screener — Roadmap
## Contributing to `alirezarezvani/claude-skills` (via `dhoovDB/claude-skills`)

**Status:** v1.0 built; pre-PR fix pass in progress (Phase 4.6), then Phase 5 (PR)  
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

> **Open design choice #1 — Frontmatter `tags` field — RESOLVED 2026-07-03 (superseded; see decision log):** The frontmatter sketch above is retired. `CONVENTIONS.md` allows `name` + `description` only, so the shipped SKILL.md carries two fields — no `tags`/`author`/`license`/`metadata`/`agents`. The block above is kept for historical context.

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
- **Directory placement inside `finance/`** *(resolved 2026-08-16)* — **`finance/passive-deal-screener/`** (flat `<domain>/<skill-name>/`), not `finance/skills/<name>/`. Three independent confirmations: `CONTRIBUTING.md`'s skill-creation guide, the PR template's "follows existing directory structure (`domain/skill-name/SKILL.md`)" checkbox, and the one external-contributor finance PR (#298, merged at `finance/saas-metrics-coach/`). The `finance/skills/<name>/` shape visible in the tree is a **maintainer post-merge restructure** (PRs #591/#593, 2026-05-02), not the contribution shape. Closes the "left open" item from the 2026-07-03 conformance review.
- **Skill-level `README.md`** *(resolved 2026-08-16)* — **Do not ship one.** No merged `finance/` skill carries a README, and neither `CONTRIBUTING.md`'s skill-creation guide nor its PR checklist mentions one; the requirement traces only to `SKILL-AUTHORING-STANDARD.md`. Install/usage guidance lives in this repo's root `README.md` instead. Phase-4 checklist item recorded as a documented divergence.
- **Upstream PR payload** *(resolved 2026-08-16)* — **Ship `SKILL.md` + `references/` + `scripts/` + `evals/evals.json` + `examples/`**; keep `evals/iteration-1..3/`, `scorecard.md`, `TESTING-PLAN.md`, and `sources.md` repo-local. Repo-wide precedent exists for both shipped items (`engineering/{behuman,code-tour,demo-video}/evals.json`, `marketing-skill/webinar-marketing/evals/evals.json`, `marketing-skill/content-creator/examples/`). The 39 iteration transcripts are process, not product, and would push the diff toward the "bloated diff" rejection criterion.
- **Slash command** *(2026-05-30; **SUPERSEDED 2026-08-16**)* — Originally "add `/cs:screen-deal`." Reversed by the Phase-4.5 divergence map: `commands/` entries are added by the maintainer in the post-merge integration release (that is what PR #309 did for `saas-metrics-coach`), and the external-contributor PR (#298) shipped no command. The command is **proposed in the PR description, not committed in the PR**. See the 2026-08-16 decision-log entry.
- **React artifact vs SKILL.md** — **Ship both.** Different surfaces (claude.ai chat with embedded UI vs Claude Code CLI). The artifact stays in this repo (gitignored); the SKILL.md is the upstream contribution. Documented in the README.
- **Contribution target** — **PR from `dhoovDB` fork to `alirezarezvani:dev`.** Feature branches targeting `dev`, never `main`.
- **Frontmatter tags field** *(2026-05-30; **SUPERSEDED 2026-07-03**)* — Originally "include tags." Reversed after the pre-PR conformance review: `CONVENTIONS.md` permits `name` + `description` only, so `tags` (and `license`/`metadata`/`author`/`agents`) are dropped. Shipped SKILL.md is two-field. See the 2026-07-03 decision-log entry.
- **Benchmark data freshness** *(2026-05-30)* — **Hardcode + manual override.** Trailing figures hardcoded with a `LAST_UPDATED` constant and an annual-refresh comment. Also accept `--benchmark-return` as a manual override so users can supply current figures. No network dependency; stdlib-only constraint holds.
- **Third script (`deal_scorer.py`)** *(2026-05-30)* — **Skip v1.0; defer to v1.1+.** A composite 0–100 score adds false precision at this stage and the eval suite doesn't require it. Tracked in the v1.1+ Backlog; revisit post-evals.

- **Asset class routing (#8)** *(resolved 2026-06-13 during the SKILL.md build)* — **Branch by deal type.** A two-axis classify: asset class drives the `01` baseline and `05` comparator; deal type drives the `02` fee section and `03` flag prefixes. One routing table maps deal type → fee section → flag prefix → comparator, then every type reconverges on the same 10-section output. See the 2026-06-13 decision-log entry.

### Still open

None. Every design choice is resolved as of 2026-08-16; the remaining work is execution (Phase 5).

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

1. Write `evals/evals.json` with the 11 test cases below (the authoritative matrix is `evals/TESTING-PLAN.md`; cases 3 and 9 are contrast pairs, so `evals.json` carries **13 runnable fixtures**, ids 1–13). Each is chosen to exercise a *distinct* part of the skill so a regression in one is hard to mask. Each reference file should be built against the cases it has to support; SKILL.md should pass all 11 before the upstream PR opens.

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

   **Iteration tracker** *(status of record; details in the dated decision-log entries)*

   | Cycle | Date | Result | FAILs | Fixes triaged → applied |
   |---|---|---|---|---|
   | 1 | 2026-07-03 | 12/13 strict; 5/5 discrimination | #8 (GEN-09 unprobed + harness defect) | S1–S3, H1–H2 → applied 2026-07-04 |
   | 2 | 2026-07-04 | 11/13; 5/5 discrimination (independent grader) | #1 (S1 over-fire), #8 (GEN-09 ID drop) | S1b, S2b, H3–H7 → applied 2026-07-04 |
   | 3 | 2026-07-04 | **12 PASS / 1 w-notes / 0 FAIL; 5/5 discrimination — GATE CLEARED** | none | single divergence (#4 HML-05 subsumed by GEN-16 on a zero-fee fixture) accepted in the decision log |

   **Cycle-3 work list (CLOSED 2026-07-04 — all items done, run passed):**
   - [x] **S1b** — materiality threshold added to the §10 verdict rule. Boundary pair verified in the run: fixture 1 → merits PwC, fixture 9 → formula.
   - [x] **S2b** — closing self-check line added to Communication. Verified: fixture 8 cites GEN-09, fixture 1 probes Q-FEE-04.
   - [x] **H3 (D1)** — id 11 re-enumerated to GEN-08 (+GEN-11 as frame); Q-DIST-01 conditional. Mirrored in TESTING-PLAN (case-9 row + prose).
   - [x] **H4 (D2)** — id 6 reworded to "GEN-14-mechanism / track-record gap."
   - [x] **H5 (D3)** — id 9 loosened to "fired or explicitly held unassessable, routed to Q-GP-02."
   - [x] **H6 (D4)** — id 12 YELLOW cap replaced with "probes on genuine absences OK; none manufactured." Mirrored in TESTING-PLAN (cases 10–11 rows).
   - [x] **H8 (F3)** — ids 3/12/13 accept PwC on verification-grade residuals.
   - [x] **Re-run** — `evals/iteration-3/`: 12 PASS / 1 w-notes / 0 FAIL, 5/5 discrimination, independent grading.
   - SKILL.md at 9,801B after S1b/S2b — gate held.

   **Accepted divergence (gate disposition):** fixture 4's expected HML-05 goes uncited when the fixture discloses *zero* fees — the step-down-absence flag collapses into `GEN-16` (no fee disclosure at all). Accepted rather than running a fourth cycle; if id 4's expected is ever revised, loosen HML-05 to "cited or subsumed under GEN-16." Grader watch-items for v1.1: expected 01's EQUITY-01 "high promote" phrasing vs `03`'s definition (20% is mid-band); fixture 6's report reached for the insufficiency formula while also holding a complete adverse-merits case (verdict-form preference, not an error).

5. Optimize the description frontmatter for triggering accuracy — confirm it fires on phrases like "analyze this deal", "is this worth pursuing", "what should I ask the GP".

### Phase 4: Quality checklist (from `SKILL-AUTHORING-STANDARD.md`)

Before opening the PR, verify:

- [x] SKILL.md is **≤10KB** (the binding cap from `SKILL-AUTHORING-STANDARD.md` — ≈160 lines at the 58–64 bytes/line of shipped `finance/` skills; the largest, `business-investment-advisor`, sits at exactly 10.0KB/159 lines). The old "<500 lines" figure was ~3× too loose and is retired. **Met 2026-06-29: compressed 12.8KB → 9.07KB (0.93KB headroom), full fidelity, no behavioral regression (see decision log).**
- [x] Frontmatter is **`name` + `description` only** — reduced 2026-07-03 to satisfy `CONVENTIONS.md`'s two-field-only rule (supersedes the earlier `metadata:`-block + `tags` plan; see decision log). No `license`/`metadata`/`tags`/`author`.
- [x] Description is written in third person — confirmed 2026-07-11 (opens "Screens…", "Produces…", "Use whenever…"; no first/second person)
- [x] Description includes both what the skill does AND trigger contexts — confirmed 2026-07-11 (carries the trigger phrases "is this deal worth pursuing", "what should I ask the GP", "analyze this offering memo")
- [x] SKILL.md has a labeled **Anti-Patterns** section — `CONVENTIONS.md` Required Section. **Met 2026-07-11:** 5-bullet `## Anti-Patterns` section added via consolidate-and-relabel; SKILL.md 10,224B (under the 10,240 cap), no eval-behavior regression (see decision log)
- [x] All Python scripts run with `python3 script.py --help` (zero pip installs) — confirmed 2026-07-19: both `--help` exit 0; `skill_validator.py` reports both scripts "uses only standard library"
- [x] Both scripts return graded exit codes (`0` ok / `1` warnings / `2` bad input) per `CONVENTIONS.md` §4. **Met 2026-07-19:** added a boundary `validate_params()` to both scripts (errors → stderr + exit 2, no output; warnings → stderr + result on stdout + exit 1; clean → exit 0); each `--self-check` now asserts one reject + one warn case; verified by execution across clean/warn/bad inputs (see decision log)
- [x] Reference files are linked from SKILL.md with explicit load guidance — confirmed 2026-07-19: SKILL.md Routing table links `01`–`05` each with a "Load when" trigger
- [~] README.md includes install instructions and usage examples — **documented divergence, resolved 2026-08-16: no skill-level README ships.** The requirement traces only to `SKILL-AUTHORING-STANDARD.md`; `CONTRIBUTING.md`'s skill-creation guide and PR checklist never mention one, and none of the four merged `finance/` skills carries one. Install/usage guidance lives in this repo's root `README.md` instead (see the 2026-08-16 decision-log entry)
- [x] No hardcoded API keys, credentials, or personally identifying information — confirmed 2026-07-19 by the security auditor's `sensitive_data_exposure` check (0 findings)
- [x] Skill passes the security auditor. **PASS 2026-07-19** (0 CRITICAL / 0 HIGH / 0 INFO, exit 0) via `python engineering/skills/skill-security-auditor/scripts/skill_security_auditor.py <shippable subset>`. **Premise corrected:** the validators are **present** locally at `engineering/skills/skill-tester/` and `engineering/skills/skill-security-auditor/` (not the pre-`skills/` path the 2026-07-03 note assumed) and need `PYTHONIOENCODING=utf-8` on Windows. Run against the shippable subset (SKILL.md + references/ + scripts/), not the repo root — the root scan's lone HIGH was `[FS-HIDDEN] .claude`, a dev artifact that never ships. Final confirm against a fork-staged copy on synced `dev` at PR time (see decision log)

**v1.0 ship gate (in addition to the standard checklist above).** The upstream `SKILL-AUTHORING-STANDARD` covers file conventions; the items below are the *content* gates specific to this skill — the standard doesn't know about reference files or evals at this depth.

- [x] References `01–05` all built; each ≤300 lines (or with internal TOC); LP-lens only; *variable* used honestly where ranges are unstable — **verified 2026-08-16:** 258 / 300 / 232 / 227 / 257 lines, all at or under the threshold
- [x] Cross-reference integrity: each `03-red-flag-library` entry carries a flag ID in format `{ASSET_CLASS}-{NN}`; `04-question-bank` entries each cite ≥1 flag ID; `04` as a whole cites ≥5 distinct entries from `03` — **verified by extraction 2026-08-16:** 34 flag IDs defined in `03`, 25 question IDs in `04`, **28 distinct `03` flag IDs cited by `04`** (threshold ≥5), and **zero dangling IDs** — every flag/question ID appearing in `04` *or* in `SKILL.md` resolves to a real entry
- [x] `examples/` has ≥3 input/output pairs covering different deal types. **Met 2026-07-25:** 3 pairs — `equity-syndication/` (fixture 1), `hard-money-fund/` (fixture 3), `private-credit-fund/` (fixture 13) — plus an `examples/README.md` index. Each `output.md` is byte-identical to its iteration-3 validated report minus the eval-harness header (see decision log)
- [x] `evals/evals.json` carries the 11 cases from Phase 3 / `evals/TESTING-PLAN.md` (9 original + 2 clean deals; case 3 is a sound/problematic pair → 13 input fixtures); SKILL.md passes all 11 after ≥2 iteration cycles, with iteration logs in `evals/iteration-N/` — **met 2026-07-04: three cycles (12/13 → 11/13 → 12 PASS/1 w-notes/0 FAIL), 5/5 discrimination on every run, final two cycles under generator ≠ grader ≠ author subagent separation; single cycle-3 divergence accepted in the decision log**
- [x] This repo's own `README.md` (root) reflects the shipped state and points users to the upstream skill location — **now also absorbs the install/usage content** that would have gone in the dropped skill-level README (2026-08-16). **Rewritten 2026-09-01** as a product README: status, layout, install, usage, worked examples, positioning, build story. Every command in it was executed before commit; every count re-derived from disk. See the 2026-09-01 decision-log entry
- [x] Decision log captures every resolved design choice with rationale (reviewers see the *why*, not just the *what*) — **met 2026-08-16:** §7 "Still open" is empty; the Phase-4.5 divergence map records an align/defend call plus a PR-thread response line for every divergence

### Phase 4.5: PR Readiness — ✅ COMPLETE 2026-08-16

Steps 1–4 were run on 2026-08-16; the divergence map, the align/defend call on each
row, and the PR-thread responses live in that date's decision-log entry. The steps
below are kept as the method of record.

**Step 1 — Read merged PRs in `finance/`, not just the skills.**

The PR discussion thread is where maintainer preferences surface. Read 2–3 recently merged `finance/` PRs. Note any review comments, requested changes, or patterns in what got pushed back.

**Step 2 — Map every divergence between this skill and their patterns.**

For each place where passive-deal-screener differs from the existing `finance/` skills (structure, depth, tone, file count, frontmatter, output format), write one line: what is different and why.

**Step 3 — Make a call on each divergence.**

If it is not defensible: align to their pattern before opening the PR. If it is defensible: that line becomes your response if a maintainer asks. Keep it in the decision log.

**Step 4 — Confirm the decision log is complete.**

Every intentional divergence should have a rationale entry dated before the PR opens. Reviewers see the why, not just the what.

### Phase 4.6: Pre-PR fix pass — 🔄 IN PROGRESS (opened 2026-09-27)

A whole-codebase adversarial review on 2026-09-27 returned **BLOCK** (1 critical,
6 warnings, 6 notes; see that date's decision-log entry). Every finding is fixed
before Phase 5. One commit per step, in order; each runs `/codereview`, gets
approval, commits and pushes. `/adversarialreview` runs once over the full series
before the last push.

**Resume here in a fresh session:** find the first unchecked step below, confirm
the earlier steps' commits exist in `git log`, and continue from there.

- [x] **Step 0 — Record this fix pass in ROADMAP.md** (this section + decision-log entry).
- [x] **Step 1 — Script correctness (C1, W1, W2).** Done 2026-09-27; `benchmark_comparator.py` had the same silent-default pattern (`--net-irr` / `--deal-type` / `--hold-years`) and got the same ASSUMED labeling.
  - C1: `fee_drag_calculator.py` fills omitted inputs from defaults without saying so (a sparse hard-money call reported 780 bps drag, ~680 of it invented). Keep the defaults, but report every defaulted input as `ASSUMED (not supplied)` in human output and as `assumed_inputs` in JSON.
  - W1: `clears_hurdle` compares compound IRR to the simple pref *rate*, so gross = hurdle = 8% over 7 yr prints "no promote is earned" beside 133 bps of promote. The simple-pref math matches `02` and stays; derive the flag from the waterfall (`total_profit > pref_accrual`) and keep the note consistent.
  - W2: NaN/inf pass validation in both scripts. Reject non-finite numbers (exit 2).
  - Extend both `--self-check`s with these cases; regenerate the README console samples from real runs.
- [x] **Step 2 — Benchmark drift guard (W3).** Done 2026-09-27; the guard skips (does not fail) when `05` isn't beside the script, since the scripts are usable standalone. `benchmark_comparator.py --self-check` parses `05`'s comparator table and Treasury line and fails on any mismatch with the script constants. `references/data/README.md` refresh step 5 names the script constants.
- [x] **Step 3 — Data refresh (N6).** Done 2026-09-27, and the refresh consolidated from ~10 sources to 4 (FRED, Yahoo Finance, IREI, CAIS). ETF returns to 2026-06-30 plus vol and worst drop all computed from Yahoo daily closes (method validated once against an independent source, within 0.08 pts); FRED 2026-09-24 pulled directly; NCREIF Q2 2026 via IREI; Preqin re-confirmed. The 10yr Treasury (5.18%) now exceeds VNQ's and HYG's trailing 10yr; `05` says so.
- [x] **Step 3b — Benchmark refresh script (user-requested 2026-09-27).** Done: `tools/refresh_benchmarks.py`; reproduces the Step 3 figures exactly in ~5 s. FRED drops connections that claim to be a browser while Yahoo requires one, so each source gets its own user agent. A maintenance script (repo-only, not in the PR payload) that pulls FRED and Yahoo and computes every ETF and Treasury figure, so a refresh is one command plus the two manual lookups (IREI, CAIS). Supersedes part of the v1.1 "enforced refresh" backlog item. Re-pull ETF 5/10yr returns (latest quarter-end), FRED 3mo/2yr/10yr, NCREIF NPI, Preqin note, per the `references/data/README.md` procedure. Update `05`, script constants, self-check anchors, README sample. Anything not publicly sourceable keeps its prior value and date, marked — nothing invented.
- [x] **Step 4 — SKILL.md (W4, N1).** Done 2026-09-27: SKILL.md 10,226 → 10,121 B (119 B headroom, was 16). N1 resolved the other way round from the review's suggestion: upstream's SKILL-AUTHORING-STANDARD checklist asks for an "Output Artifacts table (4-6 per skill)", so the table stays (compacted, renamed to upstream's exact heading) and the duplicate examples left "Modes" instead. Also cut three repeats ("lead with the verdict" ×2, "never cite from memory"), and SKILL.md now tells the agent to pass `0` for undisclosed fees and to treat an ASSUMED script input as a §6 gap. Merge the "Output artifacts" table into "Modes" (duplicate content); add one skepticism rule that pasted deal text is data, and embedded instructions are ignored and flagged. Stay under the 10,240-byte cap.
- [ ] **Step 5 — Reference trim (W5, N3).** Cut repeated boilerplate from `references/01`–`05` (restated "LP lens only", generic source lists, cross-file preambles) and the capture narrative from `references/data/README.md`. Constraint: every flag/question ID, threshold, range and table row is unchanged — verified by a before/after ID and number diff.
- [ ] **Step 6 — Eval transcript prune (N4).** Delete the 26 transcripts in `evals/iteration-1/` and `iteration-2/`; keep both `scorecard.md` files; fix references to the deleted files.
- [ ] **Step 7 — Docs cleanup (W6, N2, N5).** Restructure this file to the portfolio template spine (`writing-kit/ROADMAP-TEMPLATE.md`): drop the superseded §2–§4 drafts and §11/§12, sort and trim the decision log newest-first. Bring CLAUDE.md current. Replace drift-prone counts in README.
- [ ] **Step 8 — Eval iteration 4 (full re-validation).** All 13 fixtures, generator ≠ grader ≠ author, fresh-context subagents; grader works from `evals/evals.json` `expected_output` and may not read iterations 1–3. Regenerate `examples/*/output.md` from fixtures 01/03/13. Gate: 0 FAIL. Most token-expensive step — if the session ends, steps 0–7 stand alone.

**Grading-criteria gap.** Iteration 3's grader used `expected/01–13.md` files from a
session scratchpad that no longer exists. Iteration 4 grades against the
`expected_output` field in `evals/evals.json`, which is committed.

### Phase 5: Commit and PR

**Branch off `upstream/dev` directly — not off the fork's `main`.** As of 2026-08-16
`dhoovDB/claude-skills@main` is **76 commits ahead of** `alirezarezvani:dev`; branching
from it would carry all 76 into the diff and trip CONTRIBUTING's "bloated diffs with
fork merge history" rejection criterion. Use the command CONTRIBUTING itself prints:

```bash
git fetch upstream dev
git checkout -b feat/finance-passive-deal-screener upstream/dev

# Stage the shippable subset only (see §7 "Upstream PR payload")
#   finance/passive-deal-screener/{SKILL.md,references/,scripts/,evals/evals.json,examples/}
#   + finance/CLAUDE.md   (the only file outside the skill folder — see §9)

# Run all three validators against the staged skill path before committing
python3 engineering/skills/skill-tester/scripts/skill_validator.py finance/passive-deal-screener
python3 engineering/skills/skill-tester/scripts/script_tester.py finance/passive-deal-screener --verbose
python3 engineering/skills/skill-security-auditor/scripts/skill_security_auditor.py finance/passive-deal-screener --strict

git add finance/passive-deal-screener/ finance/CLAUDE.md
git commit -m "feat(finance): add passive-deal-screener — LP-perspective deal screening for syndications, preferred equity, and hard money"

git push origin feat/finance-passive-deal-screener
```

> **Validator path note.** `CONTRIBUTING.md` prints `engineering/skill-tester/scripts/…`;
> the actual path on `dev` is **`engineering/skills/skill-tester/scripts/…`** (confirmed
> 2026-08-16). Stale doc, not a missing tool. On Windows the auditor needs
> `PYTHONIOENCODING=utf-8`. `--strict` is CONTRIBUTING's stated invocation and was **not**
> used in the 2026-07-19 local run — re-run with it before the PR.

Open a PR from `dhoovDB:feat/finance-passive-deal-screener` → `alirezarezvani:dev`.

**PR description should include:**
- What the skill does and who it's for
- Competitive positioning (what existing skills don't cover)
- Open design choices you resolved and why
- Test cases run and iteration summary
- The defensible-divergence lines from the 2026-08-16 decision-log entry (5 numbered
  references; no skill-level README; `evals/` + `examples/` included; unlabeled Overview)
- **Proposed** (not committed) follow-ups for the maintainer's integration release:
  the `finance/CLAUDE.md` domain-list row, a `commands/screen-deal.md` slash command,
  and a draft `CHANGELOG.md` line
- Sample output for one test case (link `examples/equity-syndication/output.md`)

**CI expectations on the PR.** Two bots comment automatically: a GitHub Actions
**Skill Security Audit** (posts per-domain CRITICAL/HIGH counts) and a `claude` PR
reviewer. On PR #298 the maintainer merged with a friendly review and hand-fixed one
py3.14 `argparse` issue post-merge — a `%` in a help string. **Ours is already clean:**
every `%` in both scripts' help text is escaped as `%%` (verified 2026-08-16).

---

## 9. Files to Update in the Repo (Beyond the Skill Folder)

**Corrected 2026-08-16** — the original three-row table would have violated
`CONTRIBUTING.md` on two of its three rows. Only one file outside the skill folder
belongs in this PR.

| File | Change needed | In the PR? |
|---|---|---|
| `finance/CLAUDE.md` | Add `passive-deal-screener` to the finance domain skill list | **Yes** — the one external-contributor finance PR (#298) touched exactly this file and nothing else outside its skill folder |
| Top-level `README.md` | *(was: add a row to the Finance domain table)* | **No** — CONTRIBUTING rejects "PRs that change the skill count (205 — curated number)" and "no 3rd party links added to README". Propose it in the PR description instead |
| `CHANGELOG.md` | *(was: add a draft entry)* | **No** — CONTRIBUTING's "After Your PR is Merged" section states maintainers run the sync scripts, generate docs pages, update mkdocs nav, plugin.json counts, and marketplace.json. A draft entry here reads as scope creep, not professionalism |
| `.codex/`, `.gemini/`, `marketplace.json`, `docs/` | — | **Never** — explicitly listed under "What We Do NOT Accept" as auto-generated |

The earlier claim that "including a draft `CHANGELOG.md` entry signals professionalism
and reduces maintainer friction" is retired: CONTRIBUTING asks contributors *not* to do
this, so it would add friction, not reduce it.

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
- **Enforced refresh of `references/data/`** — the snapshot layer (built 2026-06-06) currently ages on an *honor system*: a `LAST_UPDATED` / `As of` stamp per file and the README's manual refresh procedure, but nothing detects or enforces staleness. *(2026-09-27: `tools/refresh_benchmarks.py` now automates the market-data pull and reports what changed; staleness detection below is still open.)* Two-phase research item:
  - *Phase 1 (earlier, lighter): a staleness warning.* Surface a warning when time-since-last-refresh on any snapshot exceeds a material threshold (the 10yr Treasury is the most time-sensitive; ETF/NCREIF figures age over quarters). Mechanism TBD — could be a read of the `As of` stamps emitted when the skill loads `05`, or a check the data files carry themselves. Goal: the skill (or a contributor) gets told "this benchmark data is N months stale" rather than silently comparing against old numbers.
  - *Phase 2 (later, heavier): enforced refresh.* A date-check script and/or a scheduled job (cron / CI) that fails or nags when snapshots pass their refresh cadence. Decide script-vs-schedule then. Depends on Phase 1 defining the staleness thresholds. Note the constraint: the upstream repo is stdlib-only Python and issuer fact sheets / FRED 403 automated fetch, so an *auto-pull* refresh isn't trivially scriptable — the enforced piece is more likely "detect staleness + prompt a human re-pull" than "fetch and overwrite."

---

## Decision log

*Project and architectural decisions live here. Changes to this repo's CLAUDE.md are logged in CLAUDE.md, not here.*

### 2026-09-27 — Adversarial review returns BLOCK; pre-PR fix pass opened (Phase 4.6)

Whole-codebase `/adversarialreview` (Saboteur / New Hire / Security Auditor), run
before Phase 5 with an emphasis on bloat. Verdict **BLOCK**. The critical finding
was a correctness bug, not bloat: `fee_drag_calculator.py` silently applied its
worked-example defaults (acquisition 2%, disposition 1%, mgmt 1.5%, admin 0.3%,
20% carry over an 8% hurdle) to any fee the caller omitted. The eval suite did not
catch it. Most bloat sits outside the PR payload (this file is 131 KB); inside the
payload, the boilerplate in the always-loaded references costs tokens on every
screen.

Decisions (grill-me, same day):
- **Defaults stay, labeled.** A bare run still reproduces the `02` worked example;
  every defaulted input is reported as assumed. Chosen over zero-defaults to keep
  the demo behavior.
- **W1 is a flag bug, not a math bug.** `02` specifies a simple pref and
  `promote_drag` implements it; only the `clears_hurdle` flag is wrong.
- **Iteration-1/2 transcripts deleted, scorecards kept.** Git history keeps the
  transcripts; the scorecards carry the lessons.
- **Examples are never hand-edited.** They are regenerated from iteration 4 so the
  benchmark refresh doesn't leave them quoting old figures.
- **Full 13-fixture iteration 4** after the fixes, so the eval claim describes the
  files that actually ship.
- **Decision log stays in ROADMAP.md**, sorted newest-first, per the portfolio
  ROADMAP template.

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

### 2026-08-16 — Phase 4.5: divergence map vs upstream's *actual* merged practice (align/defend on 12 rows)

Ran Phase 4.5 steps 1–4 before writing either README, because Phase 4.5 decides what
those READMEs are. Method note: all upstream reading went through `gh api` / `gh pr view`
against `alirezarezvani/claude-skills@dev` — the local `claude-skills` clone is a
read-only fork per the portfolio CLAUDE.md and was not touched. Drift check first:
`dhoovDB/claude-skills@main` is **ahead 76 / behind 0** vs `alirezarezvani:dev`, so no
sync was needed to read current upstream state accurately.

**The find that reframed the pass: `CONTRIBUTING.md` exists and this ROADMAP had never
cited it.** Every prior conformance review here reasoned from `CONVENTIONS.md` and
`SKILL-AUTHORING-STANDARD.md`. `CONTRIBUTING.md` is more specific than both, and it
settles four rows outright — including two where this ROADMAP was actively planning the
wrong thing.

**Evidence base (Step 1).** Read PR **#298** (`saas-metrics-coach` — the *only* external
contributor finance skill, merged to `dev`), PR **#309** (the maintainer's follow-on
integration release), PR **#455** (a 4-skill community batch), and the layout-restructure
PRs **#591/#593**; plus `CONTRIBUTING.md`, `CONVENTIONS.md`, and
`.github/PULL_REQUEST_TEMPLATE.md` at `dev` HEAD.

The single most useful observation is the **split between the two PRs**: #298 (contributor)
touched *only* `finance/saas-metrics-coach/**` + `finance/CLAUDE.md`. #309 (maintainer)
then did `marketplace.json`, `docs/skills/finance/*`, `.codex/`, `.gemini/`,
`commands/*.md`, and `agents/*` as a separate release. That boundary — contributor ships
the skill folder, maintainer does integration — decides rows 3, 6, and 7 below.

**The divergence map.** Every row carries what differs, why, and the call. "Defend" rows
carry the line to paste into the PR thread if a maintainer asks.

| # | Divergence | Written rule vs observed practice | Call |
|---|---|---|---|
| 1 | **Directory layout** | CONVENTIONS + CONTRIBUTING + PR template all say `<domain>/<skill-name>/`; the tree shows `finance/skills/<name>/` for 3 of 4 skills | **ALIGN → `finance/passive-deal-screener/`.** The `skills/` nesting is a maintainer *post-merge* restructure (#591/#593, 2026-05-02); #298 was contributed flat. Three docs and the one contributor PR agree |
| 2 | **Skill-level README** | `SKILL-AUTHORING-STANDARD.md` requires one; CONTRIBUTING's skill-creation guide and PR checklist never mention one; 0 of 4 merged finance skills have one | **ALIGN → don't ship it.** Deletes a planned task. Install/usage moves to this repo's root README |
| 3 | **Top-level `README.md` + `CHANGELOG.md` edits** (ROADMAP §9) | CONTRIBUTING: "PRs that change the skill count (205)" and "PRs modifying `.codex/`, `.gemini/`, `marketplace.json`" are **not accepted**; maintainers handle docs/changelog/counts after merge | **ALIGN → drop both rows.** §9 corrected in place. This ROADMAP's claim that a draft CHANGELOG entry "signals professionalism" was backwards — CONTRIBUTING asks contributors not to |
| 4 | **`finance/CLAUDE.md` edit** | Not in any checklist, but #298 did exactly this | **KEEP.** The one file outside the skill folder that belongs in the PR |
| 5 | **`Cross-References` section** | CONVENTIONS Required Section #5; named in the CONTRIBUTING PR checklist. Ours was labeled `## Related skills` (SKILL.md:109) — right content, wrong label | **ALIGN → rename. ✅ DONE 2026-09-01.** Heading-only swap; the two bullets already matched CONVENTIONS' "related skills in this repo". SKILL.md now 111 lines / 10,226 B. See the 2026-09-01 decision-log entry — the "16 bytes of headroom under the 10,240 cap" premise did not survive verification |
| 6 | **Slash command `/cs:screen-deal`** | Locked "add it" on 2026-05-30. But #298 shipped no command; the maintainer added `commands/financial-health.md` in the #309 integration release | **ALIGN → propose in the PR description, don't commit.** Supersedes the 2026-05-30 lock |
| 7 | **PR payload: `evals/` + `examples/`** | No merged *finance* skill carries either; repo-wide precedent exists (`engineering/{behuman,code-tour,demo-video}/evals.json`, `marketing-skill/webinar-marketing/evals/evals.json`, `marketing-skill/content-creator/examples/`) | **DEFEND → ship `evals/evals.json` + `examples/`; keep the 39 iteration transcripts, `scorecard.md`, `TESTING-PLAN.md`, `sources.md` repo-local.** *PR line:* "13 fixtures and 3 worked outputs are how you verify the screener discriminates instead of flagging everything; the iteration transcripts are process, not product, so they stay out of the diff." |
| 8 | **5 numbered reference files** vs 2–4 unnumbered in merged finance skills | No rule either way; CONTRIBUTING calls `references/` optional | **DEFEND.** *PR line:* "The numbers encode load order and build order — `04` cites flag IDs defined in `03`, `05` does spread math off `01`'s ranges. SKILL.md's routing table loads a named slice per deal type rather than the whole set." |
| 9 | **Unlabeled Overview** (H1 + intro paragraph, no `## Overview`) | CONVENTIONS Required Section #2, phrased "should include"; absent from the CONTRIBUTING PR checklist | **DEFEND.** *PR line:* "The paragraph under the H1 is the overview; a labeled heading would cost bytes against the 10KB cap without adding information." Weaker rule than #5's — "should", not the frontmatter's "will be closed" |
| 10 | **Two-field frontmatter** | PR template still lists `license` as expected; CONVENTIONS forbids it with "PRs that violate them will be closed"; CONTRIBUTING repeats "Do NOT add `license`, `metadata`, `triggers`, `version`, `author`" | **HOLD the 2026-07-03 call.** Now supported by a second doc. The PR template is the stale one |
| 11 | **Line/size cap** | CONTRIBUTING says "under 500 lines"; SKILL-AUTHORING-STANDARD says ≤10KB. Ours: 111 lines / 10,224 B | **No action** — satisfies both. The 2026-06-13 note that "<500 lines" was retired should read "superseded by the *binding* constraint," not "wrong" |
| 12 | **Validator paths** | CONTRIBUTING prints `engineering/skill-tester/scripts/…`; actual path on `dev` is `engineering/skills/skill-tester/scripts/…` | **No action** — confirms the 2026-07-19 correction. Stale doc, not a missing tool |

**Two things this pass caught that a checklist wouldn't have.**

- **A pre-empted post-merge bug.** After merging #298 the maintainer noted he would fix a
  Python 3.14 incompatibility himself: a bare `%` in an `argparse` help string. Checked
  ours — **every `%` in both scripts' help text is already escaped `%%`** (15 occurrences
  across `fee_drag_calculator.py` and `benchmark_comparator.py`). Nothing to fix; worth
  knowing it was checked rather than lucky.
- **`--strict` was never run.** CONTRIBUTING invokes the security auditor with `--strict`;
  the 2026-07-19 local run did not record that flag. Added to the Phase-5 command block.
  Also noted: CI posts *two* automated reviews on every PR (a GitHub Actions Skill Security
  Audit and a `claude` reviewer), so the first response to the PR will be machine-generated.

**Ship-gate items closed in the same pass** (verified by extraction, not assertion):
references `01–05` at 258 / 300 / 232 / 227 / 257 lines, all within the 300-line
convention; cross-reference integrity clean — 34 flag IDs in `03`, 25 question IDs in
`04`, **28 distinct `03` IDs cited by `04`** against a ≥5 threshold, and **zero dangling
IDs** across `04` *and* `SKILL.md`.

**§7 now has no open design choices.** Directory placement, skill-level README, and PR
payload resolved here; asset-class routing (#8) was resolved on 2026-06-13 and had been
left sitting in the "Still open" table by oversight.

**Remaining before the PR:** ~~(1) the `## Cross-References` rename in SKILL.md with a
byte-cap re-check~~ — **done 2026-09-01**; ~~(2) the root `README.md` refresh — now also
carrying the install/usage content the dropped skill-level README would have held~~ —
**done 2026-09-01**; (3) **Phase 5 — the only thing left.**

### 2026-09-01 — Root README rewritten as a product README

The last content gate before Phase 5. The old README was not merely stale, it argued
the opposite of the current plan: a dedicated section promised that "install
instructions and usage examples ship in a **skill-level** `README.md` at
`finance/passive-deal-screener/README.md`" — the very file Phase 4.5 decided not to
ship. It also opened with "**Status: Pre-development.** Not installable yet," marked
`03`/`04`/`05`/`SKILL.md`/`scripts/`/`examples/` as *Planned* in its layout tree, omitted
`evals/` entirely, and carried a build-status table with six wrong rows.

**Four decisions, locked in a grill-me pass before writing:**

1. **It is a product README, not a repo introduction.** The deciding evidence: the root
   README is **not in the PR payload** (§7 ships `SKILL.md` + `references/` + `scripts/` +
   `evals/evals.json` + `examples/`), so an upstream reviewer never sees it in the diff.
   The real reader is someone landing on the GitHub repo — a would-be user or a hiring
   manager. Structure now leads with what it does, install, and usage; build context is
   demoted below the fold.
2. **Install documents the manual path, not the plugin.** Clone, then copy exactly
   `SKILL.md` + `references/` + `scripts/` into `~/.claude/skills/passive-deal-screener/`
   — the same subset that ships upstream, so a local install behaves identically to the
   merged one. The `/plugin install finance-skills@claude-code-skills` route is named as
   the post-merge future state without claiming it works today. Verified by executing the
   copy into a scratch tree; the result is a valid skill directory with intact frontmatter.
3. **Status callout: "v1.0, working. Not yet merged upstream."** Honest in both
   directions — doesn't undersell a finished skill, doesn't imply marketplace
   availability. Eval evidence lives under "How it was built" rather than the headline.
4. **Build-status table dropped; a short accurate layout tree kept.** A table of ✅s is a
   build log, and `ROADMAP.md` already owns status. The tree survives because it sits
   directly above Install and shows what the three copied directories contain.

**Every command in the README was executed before commit**, and one claim did not
survive that check: the exit-code line originally read "`2` bad input," which is vague
and half-wrong. `--gross-irr 999` returns **1**, not 2 — it is a runnable unit-slip
warning that still emits the result. Reading `validate_params()` gave the real contract,
now documented as a table with a verified example per row: `0` clean, `1` runs-but-suspect
(warning to stderr, result to stdout), `2` structurally invalid (rejected, no output).
The worked usage examples are real transcripts, and the two scripts are shown composing —
`fee_drag_calculator` yields a 12.31% net IRR that becomes `benchmark_comparator`'s input.

Counts re-derived from disk rather than inherited from prose: 5 reference files totalling
1,274 lines, 34 flag IDs, 25 question IDs, 13 eval fixtures, 3 example pairs, both scripts
importing only `argparse`/`json`/`sys`.

### 2026-09-01 — `## Cross-References` rename, and the 10,240-byte cap fails verification

Divergence-map row 5 executed. `SKILL.md:109` `## Related skills` → `## Cross-References`,
matching `CONVENTIONS.md:77` ("**Cross-References** — related skills in this repo").
Heading only — the two bullets (`financial-analyst`, `business-investment-advisor`, each
with a "NOT this" disambiguation) already matched the required content, so the diff is
exactly one insertion and one deletion. SKILL.md: 111 lines, 10,226 B.

**The byte cap this ROADMAP has been budgeting against could not be sourced.** Before
running the rename I went looking for the 10,240-byte limit to confirm the +2 B fit, and
found no rule to confirm it against:

- `CONVENTIONS.md:62` sets a **line** limit — "Under 500 lines." We are at **111**, with
  389 lines of headroom.
- `SKILL-AUTHORING-STANDARD.md` states no size rule at all.
- `skill_validator.py` has no SKILL.md size check. Its `script_size_range` values
  (100–300 / 300–500 / 500–800) are **Python script LOC tiers**, not SKILL.md bytes —
  the likeliest source of the original misreading.
- `grep -rn "10240\|10,240"` across every `.md` and `.py` upstream returns only unrelated
  hits (a Grafana colour threshold, a mock file size in a test fixture).

**Why it matters beyond this task.** The phantom cap has been shaping decisions. The
2026-07-11 Anti-Patterns work was executed as a "consolidate-and-relabel" *specifically*
to fit inside it, and divergence-map **row 9** still defends the unlabeled Overview with
the line "a labeled heading would cost bytes against the 10KB cap without adding
information" — an argument resting on a constraint with no found source. That PR line is
now weak and should be re-argued on its own merits (the paragraph under the H1 *is* the
overview; CONVENTIONS says "should include", not "must") rather than on byte scarcity,
before the PR opens.

**Not re-opened:** the Anti-Patterns consolidation itself. It reads well as written and
passed three eval cycles; only the *rationale* was wrong, not the result. Re-litigating a
good outcome because its justification was flawed would burn the session for no gain.

### 2026-07-25 — Built `examples/` (3 input/output pairs; content ship-gate item)

Assembled the `examples/` directory the v1.0 content gate requires — one input/output
pair per deal type, following CLAUDE.md's `examples/<deal-type>/{input,output}.md`
structure. Three calls:

- **Deal-type set chosen for spread: equity / hard-money / private-credit** (fixtures 1,
  3, 13), user-selected over two alternatives. The DoD and CLAUDE.md's illustrative
  structure named *preferred-equity* as the third type, but the only preferred-equity
  fixture (id 2) is a sparse-email *Pass-as-presented* case; the roadmap footer's earlier
  1/3/12 suggestion was two equity deals + HML (only two distinct types). The chosen set
  gives three genuinely distinct deal types, all clean full analyses, and the widest
  asset-class spread (equity / debt-fund / credit). CLAUDE.md's structure block updated
  to `private-credit-fund/` accordingly (the DoD's type list is "e.g.", non-binding).
- **Outputs are the validated eval reports, not fresh prose.** Each `output.md` is the
  iteration-3 report (the run that cleared the PR gate) with only the eval-harness header
  (title + provenance line) swapped for an example note — verified **byte-identical** to
  the source from line 3 on. This keeps the examples honest: what ships is exactly what
  the eval suite graded, not a hand-polished ideal.
- **All three land on Pursue-with-conditions by design** — these are the *sound* deals in
  the suite; the Pass / Pass-as-presented paths stay demonstrated in `evals/`, not the
  shipping examples, which are meant to show a full clean analysis end-to-end. The
  `examples/README.md` index states this so a reviewer doesn't read three "Pursue"
  verdicts as the skill being agreeable — the discrimination lives in the *conditions* and
  the named swing factor.

Remaining before the PR: the two READMEs (this repo's root already exists — the
skill-level `finance/passive-deal-screener/README.md` is the pending one), then Phase 5
(sync `dev`, clean validator pass, open the PR).

### 2026-07-19 — Ran the upstream validators (post-eval conformance fix 3 of 3); security auditor PASSES; validator FAILs triaged as CONVENTIONS conflicts

Ran the three `claude-skills` validators against the skill. The task's stated premise
was **stale**: the validators are *not* absent — they live locally at
`engineering/skills/skill-tester/scripts/{skill_validator,quality_scorer}.py` and
`engineering/skills/skill-security-auditor/scripts/skill_security_auditor.py` (the
2026-07-03 note recorded a pre-`skills/` path). So they could run **directly against the
skill without syncing or modifying the fork**. Two environment/method calls mattered:

- **`PYTHONIOENCODING=utf-8` is required on Windows** — all three crash on cp1252 when
  printing their `✓`/`🔴`/box-drawing output; not a skill defect.
- **Run against the shippable subset, not the repo root.** The repo root pulls in
  `evals/` (58 iteration markdowns), `.claude/`, ROADMAP/CLAUDE — 72 files. Staged just
  SKILL.md + references/ + scripts/ (16 files) to mirror what ships in
  `finance/passive-deal-screener/`.

Results (shippable subset):

- **security_auditor → ✅ PASS, 0 findings, exit 0.** The Phase-4 security gate is met.
  The repo-root run's single HIGH (`[FS-HIDDEN] .claude`) was a dev/session artifact that
  never ships — it vanishes on the subset.
- **skill_validator → 76.5/100 GOOD.** All script checks pass (both stdlib-only, argparse,
  main guard, valid syntax — the fix-2 validation layer is clean).
- **quality_scorer → 45.7/100 (F).** Opinionated/old-schema scorer; its security dimension
  is broken (flat 0.0 across all four sub-scores, incl. `input_validation` — 0.0 right
  after fix-2 *added* input validation), which alone drags a ~60 to an F. Not a CONVENTIONS
  gate.

**The judgment call — most validator FAILs must NOT be "fixed".** The validator's `ERRORS`
demand frontmatter `Name/Tier/Category/Dependencies/Author/Version` and
`Features/Usage/Examples` sections — the **older `SKILL-AUTHORING-STANDARD` schema**. These
**directly conflict with `CONVENTIONS.md`** (mandatory; "PRs that violate them will be
closed"), which permits **`name` + `description` only** and names `version/author/category`
as reject-on-sight. Adding them to satisfy the validator would *violate* CONVENTIONS and get
the PR closed — so the correct response is to **not act on that output** and resolve toward
CONVENTIONS, consistent with the 2026-07-03 decision. Same shape for "SKILL.md 93 lines <
100": the validator counts *lines*, CONVENTIONS binds on ≤10KB *bytes* (skill at
10,224/10,240) — not padded. Real-but-sequenced FAILs (README.md missing, 0 example files)
are the **next two tasks** (`examples/`, the skill-level README), not defects.

**Fork sync deferred to pre-PR (approved).** The local validators are stale (fork 33 behind
its own origin; `dev` not checked out), so whether the frontmatter conflict is even live for
the PR depends on the maintainer's *current* validator. Syncing `dev` (and the Phase-1
`git push origin main`) is an outward-facing write on a "do-not-modify" repo — deferred to
the Phase-5 pre-PR step, after `examples/` + READMEs, when one clean validation pass against
synced `dev` + a fork-staged skill copy is the natural final check. No changes were made to
the `claude-skills` fork this session.

### 2026-07-19 — Added a graded input-validation layer to both scripts (post-eval conformance fix 2 of 3)

`CONVENTIONS.md` §4 requires graded exit codes (0 ok / 1 warnings / 2 bad input). The
checklist framed this as "return the right exit code," but reading both scripts showed
the real gap was **no semantic input validation at all** — `argparse` caught non-numeric
input (and `benchmark` already exited 2 on an unknown deal type), but numeric nonsense
passed silently: `fee_drag --mgmt-fee -5` reported the LP *earning* the fee (negative
drag), `--hold-years 0` reported zero drag (net = gross), `--carry 150` ran an
out-of-domain waterfall. For a tool feeding an LP's capital decision, a silent wrong
answer is the exact failure a screener exists to prevent — so this shipped as a
**data-validation layer**, not a one-line exit code. Calls:

- **Validation lives at the I/O boundary, not the engine.** A `validate_params(params)
  -> (errors, warnings)` function sits with `args_to_params` / `main`; the pure
  calculation core (`compute_fee_drag`, `promote_drag`, `compute_comparison`) is
  untouched. Engine-pure / IO-at-the-boundary held.
- **Three grades, drawn at "the math is undefined" vs "the deal is bad."** Exit 2 (reject,
  no output) for structurally impossible inputs — hold ≤ 0, negative fees, carry/catch-up
  outside [0,100], IRR < −100%, negative illiquidity premium. Exit 1 (emit result to
  stdout, warning to stderr) for runnable-but-suspect unit slips — IRR > 100%, a headline
  fee that looks like a fraction (0.015 where 1.5 was meant), total fee load > 50%. Exit 0
  clean. A *legitimately bad* deal (negative IRR, below-hurdle gross) is never
  hard-rejected — only inputs the model can't represent are.
- **The validator is self-tested (stdlib-only, no pytest).** Each `--self-check` now
  asserts one reject case (hold 0 → error) and one warn case (IRR 150 → warning) alongside
  the existing `02`/`05` anchor checks — so the validation layer can't silently rot.
- **Verified by execution** (Python 3.12): both `--self-check` PASS; clean/`--json`/bare
  runs exit 0; the warn cases exit 1 with the report still on stdout and the warning on
  stderr; every bad-input case (incl. argparse non-numeric and the unknown-deal-type
  ValueError path) exits 2 with no result printed; `--help` exits 0 for both (zero pip).

Post-eval conformance fix 3 of 3 remains: **fork sync + upstream validators** (cross-repo;
needs the `claude-skills` fork's `dev` synced before the `skill-tester` / security-auditor
validators can run). Then `examples/`, the two READMEs, and the PR.

### 2026-07-11 — Added the labeled `Anti-Patterns` section to SKILL.md (post-eval conformance fix 1 of 3)

First of the three post-eval conformance fixes. `CONVENTIONS.md` lists **Anti-Patterns**
as a Required Section (a reject-on-sight omission); the skill's "what not to do" was
present but folded unlabeled into the Skepticism contract and the intro. The binding
constraint was the ≤10KB (10,240B) size cap — SKILL.md sat at 9,801B, ~439B of headroom,
not enough for a full new section. Approach and calls:

- **Consolidate-and-relabel, not append.** Rather than add net-new prose (which would
  blow the cap or duplicate the 8 skepticism rules), the section is 5 concise don'ts, and
  the two spots that already carried this guidance were trimmed to relocate it, not restate
  it: the intro's "Operator concerns … out of scope" sentence and the routing block's
  "Never state a … from memory" sentence both collapse into the labeled bullets
  (Operator-lens creep; Citing from memory).
- **The section adds what the rules didn't state.** The two highest-value bullets are
  *net-new* anti-patterns the eval work validated but the contract never encoded:
  **Manufacturing flags** (false-positive discipline — a sound deal earns "Pursue"; the
  discrimination tests turn on this) and **Over-firing "insufficient disclosure"** (the S1b
  materiality threshold from eval cycle 2→3, stated as a don't). The "don't summarize"
  bullet was dropped as a pure restatement of skepticism rule 1.
- **First draft overshot to 10,518B (+278 over).** Reclaimed by tightening the bullets and
  the `Related skills` block (which duplicated the frontmatter disambiguation). Final:
  **10,224B — 16B under the cap.** Headroom is deliberately thin; any future SKILL.md
  content addition now needs a compensating trim (noted so it isn't a surprise).
- **No behavioral regression.** Edits were localized to the intro tail, the routing
  memory-sentence, the new section, and `Related skills`; the fidelity-rubric elements
  (5 reference links + load triggers, 8 skepticism rules, 10 output sections, deal-type
  branches, variable-class carve-out, JSON mode, confidence tags) all verified intact.

Also closed the two adjacent Phase-4 description checks (third-person; what-it-does +
trigger contexts) — both already true of the shipped frontmatter, confirmed this pass.
Remaining post-eval conformance fixes: **script exit codes** (`fee_drag_calculator.py`
lacks an exit-2 bad-input path; `benchmark_comparator.py` already grades 0/1/2), then
**fork sync + upstream validators**. Then `examples/`, the two READMEs, and the PR.

### 2026-07-04 — Eval cycle 3: 0 FAILs — the PR gate clears; Phase-3 eval requirement closed after three cycles

Applied the approved cycle-3 triage (S1b materiality threshold + S2b emit-time
self-check to SKILL.md, landing at 9,801B; H3–H6 + H8 to evals.json; D1/D4 mirrored
into TESTING-PLAN so the authoritative matrix and the harness don't diverge), then
re-ran all 13 fixtures under the iteration-2 method — blind fresh-context generator,
independent fresh-context grader forbidden from reading prior cycles, orchestrator
spot-verification only.

- **Result: 12 PASS / 1 PASS-with-notes / 0 FAIL; 5/5 discrimination tests — third
  consecutive run.** The trajectory across cycles (12/13 → 11/13 → 0 FAILs) is the
  suite working as designed: cycle 2's regression (S1 over-fire) was caught by
  independent grading, calibrated with one phrase, and verified against the boundary
  pair (fixture 1 → merits PwC; fixture 9 → insufficiency formula). Both cycle-2 FAIL
  mechanisms are confirmed fixed in the run itself: fixture 8 cites GEN-09, fixture 1
  probes Q-FEE-04 — the S2b self-check closing the question-fires-flag-ID-drops
  pattern.
- **The one note, accepted as the gate's permitted divergence:** fixture 4's expected
  HML-05 is uncited because the fixture discloses zero fees — on such a deal the
  step-down-absence flag genuinely collapses into `GEN-16`. Recorded in the Phase-3
  tracker with the eventual expected-side loosening noted; not worth a fourth cycle.
- **Watch-items logged for v1.1, not v1.0:** expected 01's EQUITY-01 phrasing vs
  `03`'s promote bands; fixture 6's preference for the insufficiency form when an
  adverse-merits case is also complete.

**Phase-3 step 4 is closed** (3 cycles, ≥2 required) and the Phase-4 eval checkbox is
checked. Build order advances to the post-eval conformance fixes (Anti-Patterns
section, script exit codes, fork sync + upstream validators), then `examples/`
(candidates: the iteration-3 clean-run reports for fixtures 1, 3, and 12 — one per
deal type, already validated), the two READMEs, and the upstream PR.

### 2026-07-04 — Eval iteration 2: 11/13 with independent grading; S1 fix over-fires; cycle 3 required before PR

Applied the iteration-1 triage (S1 insufficient-input verdict rule, S2 ID-citation
completeness, S3 unstated-hold→GEN-09 trigger to SKILL.md, holding the gate at 9,485
bytes; H1 EQUITY-03 mis-map + H2 Cannot-assess vocabulary in evals.json, extended to
id 7 — same root cause), then re-ran all 13 fixtures with the adversarial-review
upgrade: **generator and grader were separate fresh-context subagents** (generator
read only SKILL.md + references + prompts, blind discipline confirmed; grader verified
IDs against `03`/`04` definitions and was told not to anchor on iteration 1). The
evals author only orchestrated and spot-verified the FAILs. Scorecard:
`evals/iteration-2/scorecard.md`.

- **Headline: 11/13 — 5 PASS, 6 PASS w/ notes, 2 FAIL; all five discrimination tests
  passed again** under a stricter, independent grader — the discrimination core is
  now validated by two graders across two runs.
- **The S1 fix over-fires — a regression this cycle introduced.** As worded, any
  single missing essential triggers "Pass as presented — insufficient disclosure";
  the formula appeared in 9 of 13 verdicts and displaced the merits
  Pursue-with-conditions on the happy-path fixture 1 (→ FAIL). Grader's calibration:
  add a materiality threshold — *substantially* absent → S1 formula; enough to
  underwrite the core return story → merits verdict with residuals as conditions.
  Fixture 1 vs fixture 9 is the boundary pair to test the wording against.
- **Fixture 8 FAILed again, narrower:** Q-RISK-01 now asked and maturity
  stress-tested (S3 moved behavior — the same run fired GEN-09 by ID on fixture 7),
  but the flag ID itself still never cited on 8. The residual pattern: *the question
  fires, the flag ID drops* (also Q-FEE-04 on fixture 1). Grader's suggested fix: a
  closing self-check line in SKILL.md.
- **Verdict softening pattern (ids 3/12/13):** all three clean deals came back
  Pursue-with-conditions vs expected "Pursue" — arguably correct LP behavior on
  genuinely absent items; resolve on the evals side (accept PwC on clean deals with
  real residuals).
- **Four new expected_output defects documented (D1–D4)** — sharpest is id 11
  enumerating GEN-11 for *disclosed* back-loading (per `03`, GEN-11 = timing *not
  disclosed*; the correct ID, GEN-08, is absent from the expected). Plus D5: id 1's
  expected verdict and the current S1 wording are mutually unsatisfiable — the
  formal statement of the over-fire.

Triage for cycle 3: **S1b** (materiality wording, one phrase), **S2b** (closing
self-check line), **H3–H6** (D1–D4 expected fixes), **H7** (D5 resolves via S1b).
Phase-3's ≥2-cycle minimum is met, but shipping on a cycle that introduced a
regression would gut the eval suite's purpose — **cycle 3 (apply S1b/S2b/H3–H6,
re-run blind with independent grading) is the gate before examples/ + READMEs + PR.**

### 2026-07-03 — Ran the eval suite, iteration 1: 12/13 strict (1 FAIL); 4 discrimination tests pass; 5 fixes triaged

First full run of the 13-fixture suite against the final 9.07KB body (Phase 3 step 2;
outputs in `evals/iteration-1/`, per-check grades in `scorecard.md`). Method held to a
contamination control: for each fixture, only the `prompt` was read before generating
the report; `expected_output` was read only after the report was on disk, and grading
was per-check binary, not holistic — the self-grading mitigation named when this task
was scoped. An adversarial review (adversarial-reviewer skill, run post-hoc at the
user's direction) then audited the grading itself and forced two corrections recorded
here honestly: an initial "13/13 no hard fails" headline was self-graded inflation, and
the grade labels lacked a rubric. Both fixed in `scorecard.md` before commit.

- **Headline: 12/13 strict — 6 PASS, 6 PASS-with-notes, 1 FAIL** (fixture 8: its
  "catches some but not all" criterion triggered at 7/9 flags — one legitimate miss,
  GEN-09 unprobed; one harness defect, EQUITY-03 mis-mapped). Every other
  fixture-level FAIL condition was avoided — no fabricated terms on sparse input, no
  category baseline forced onto office, no manufactured REDs on the clean deals, no
  softened verdict on the packed-flags deal.
- **All four discrimination tests passed** — the results that matter most, because they
  can't be fudged by verbosity: hard-money pair 3/4 → Pursue vs Pass; J-curve pair
  10/11 → same 14% IRR, materially different risk verdicts; clean pair 12/13 → Pursue
  with zero manufactured flags in both branches; leverage contrast 5/13 → CREDIT-01
  fired at 2.5x-undisclosed and correctly *not* fired at 1.1x-disclosed.
- **The recurring weakness is citation, not reasoning.** In 4 fixtures the report
  described the right concept but skipped the specific flag/question ID the eval
  enumerates (Q-EXIT-01, Q-FEE-04, Q-DS-01, GEN-17, HML-05, GEN-14 across fixtures
  1/2/4/6). One legitimate detection miss: fixture 8's GEN-09 probe (maturity stated,
  hold unstated → should still probe).
- **The verdict vocabulary has a hole.** Three disclosure-starved fixtures (2, 7, 9)
  each forced an improvisation ("Pass as presented," "cannot screen") because SKILL.md
  defines only Pursue / Pass / Pursue-with-conditions and the evals expect
  "Cannot-assess." Top iteration-2 fix (S1): one rule defining the insufficient-input
  verdict formula.
- **The harness itself surfaced a defect** — the run works as an eval *of the evals*:
  fixture 8's expected_output cites "EQUITY-03 (50% promote is aggressive)" but `03`
  defines EQUITY-03 as GP-catch-up-at-100%, unmentioned in that prompt (H1); and the
  "Cannot-assess" wording in ids 2/9 references a verdict state the skill never defined
  (H2, resolves via S1).

Triage: 3 SKILL.md fixes (S1 verdict rule, S2 ID-citation completeness, S3
unstated-hold→GEN-09 trigger — all sized to keep the ≤10KB gate) + 2 evals.json fixes
(H1, H2). Iteration 2 = apply S/H fixes, re-run all 13 blind, same method **plus the
adversarial-review upgrade: a fresh-context subagent grades the reports** (grader ≠
generator ≠ evals author), closing the same-author-grading limitation the review
surfaced. The ≥2-cycle Phase-3 requirement stays on track; `examples/` can draw on the
iteration-1 outputs once cycle 2 confirms them. PR-packaging note: iteration
transcripts are repo-local; the upstream subtree carries `evals.json` only (decide
final payload at Phase 4.5).

### 2026-07-03 — Pre-PR conformance review vs upstream governance; frontmatter reduced to two fields

Before running the eval suite, reviewed the shipped skill against the upstream
`claude-skills` governance docs (`CONVENTIONS.md`, `SKILL-AUTHORING-STANDARD.md`) and
the actually-merged `finance/` skills. The review surfaced a governance conflict the
earlier frontmatter decisions couldn't have known about, and reversed one locked choice.
All fixes below are sequenced **after the eval run** — none block it.

- **Frontmatter conflict found; resolved toward the strict rule.** `CONVENTIONS.md`
  (labeled mandatory — "PRs that violate them will be closed") allows **`name` +
  `description` only** and explicitly names `license`, `metadata`, `version`, `author`,
  `category`, `updated`, and `tags` as reject-on-sight. `SKILL-AUTHORING-STANDARD.md`
  shows the fuller `metadata:` block. The merged skills themselves disagree —
  `financial-analyst` is bare two-field, `saas-metrics-coach` carries the full
  `metadata:` block, `finance-skills` uses a third flat shape. Read as: CONVENTIONS is
  the newer, stricter direction the maintainer enforces. **Decision: reduce to `name` +
  `description` only** (matches `financial-analyst`; safest for merge). **Applied this
  session** — stripped `license`, the `metadata:` block, and `tags` from SKILL.md. This
  **supersedes** the 2026-05-30 "Include tags" lock and the 2026-06-13 "follow the
  standard's `metadata:` block" call; the Phase-4.5 empirical tags check is now moot.
- **Domain placement: two patterns exist in the fork; decide at PR time.** The fork has
  both `finance/<skill>/` (business-investment-advisor) and `finance/skills/<skill>/`
  (financial-analyst, saas-metrics-coach). CONVENTIONS says `<domain>/<skill-name>/`.
  Left open — resolve against the synced `dev` HEAD when the PR branch is cut.
- **New pre-PR fixes (after the eval run):**
  - Add a labeled **Anti-Patterns** section to SKILL.md — CONVENTIONS lists it as a
    Required Section; ours currently folds "what not to do" into the skepticism contract
    without labeling it.
  - Give both scripts **graded exit codes** (`sys.exit(2)` bad input, `1` warnings);
    both already have `--json` + argparse + `--help`.
  - **Sync the fork's `dev` before the PR.** The fork is behind upstream — the validators
    CONVENTIONS tells contributors to run (`engineering/skill-tester/skill_validator.py`,
    `quality_scorer.py`, the security auditor) **don't exist in the local clone**. Run
    them against the skill on the synced branch, not locally.
- **pm-skills confirmed not the contribution target** — separate plugin marketplace
  (phuryn/pm-skills), different conventions; only `claude-skills/finance` governs this PR.
  Checked so it isn't re-litigated.

Sequencing unchanged: run the eval suite (≥2 cycles) against the ≤10KB body next; these
conformance fixes land in the same pre-PR pass as `examples/` + READMEs.

### 2026-06-29 — Compressed `SKILL.md` to ≤10KB via a conditional 2-variant comparison

SKILL.md was 12.8KB / 185 lines, ~2.8KB over the binding ≤10KB cap. Rather than one
compression attempt, used a **conditional variant comparison** so the choice was
principled, not eyeballed:

- **Two variants on the trim↔offload axis.** A = in-place prose trim (structure and
  the 5 references untouched). B = reference offload (move the per-section output-schema
  detail to a new `references/06-output-schema.md`, body keeps the 10 names + pointer).
- **A three-tier check** decided it: (1) size gate ≤10KB; (2) a fidelity rubric — a
  fixed checklist of load-bearing elements that must survive (all 5 reference links +
  load triggers, all 5 deal-type branches, the variable-class carve-out, the 8 contract
  rules, the 10 output sections, the missing-data-as-output rule, confidence tags, JSON
  mode, scripts, third-person trigger description); (3) a behavioral spot-check running
  the 4 discrimination-sensitive eval cases (packed-flags id 8, missing-disclosures id 9,
  J-curve pair ids 10/11, clean-equity id 12) against the compressed body.
- **Result: A wins.** A = 9.07KB / 0.93KB headroom, **full fidelity**, **zero structural
  change**; behavioral spot-check passed all four (notably the clean-deal false-positive
  test — A's contract rules are each tied to a *specific* condition, so none misfire on a
  sound deal). B also cleared (8.42KB) but only by adding a 6th reference (an extra load
  step every screen + ripple to the routing table and the "01–05" Phase-4 line) — buying
  headroom that wasn't needed. **C (hybrid) was correctly skipped**: the conditional rule
  fires only when A is cramped or fails, and A cleared with comfortable headroom, so the
  hybrid middle would have been filler. Variant drafts were scratch-only (not committed);
  this entry is the rationale of record.

Phase-4 size gate now met. Build order: the eval suite can now **run** against the final
body (the reason compression was sequenced before the run). Remaining: run the suite
(≥2 cycles), then `examples/` + READMEs + upstream PR.

### 2026-06-28 — Built `evals/evals.json` (Phase 3 step 1; eval harness, schema reconciled to upstream)

Turned the TESTING-PLAN matrix into the runnable harness. Read the upstream
`evals.json` examples first (`engineering/{code-tour,demo-video,behuman}`) and found
a divergence from the ROADMAP's implied design — reconciled toward the upstream
convention:

- **Matched the upstream schema exactly**: a flat array of
  `{id, prompt, expected_output, scenario_type}`. Our richer pass criteria (target
  `03` flag IDs, expected verdict, the §4 missing-data and discrimination checks) live
  *inside* the `expected_output` prose, not as new top-level fields — so the file is
  PR-compatible while still encoding what each case must prove. `scenario_type` maps to
  the upstream two values only (no invented third): 4 happy_path, 9 edge_case.
- **Prompts inlined; separate `inputs/` retired.** Upstream inlines the prompt; we
  follow suit (one canonical place per fixture, `sources.md` the provenance). Real-deal
  prompts are condensed authentic pastes with names scrubbed. `TESTING-PLAN.md` §1/§7/§9
  updated to match; the earlier separate-`inputs/` plan is superseded.
- **13 runnable fixtures for 11 cases**, ids 1–13: the contrast pairs expand to two
  entries each — 3a/3b (sound/problematic hard money → different verdicts) at ids 3/4,
  and 9-early/9-back-loaded (identical IRR, different J-curve) at ids 10/11. The pairs'
  `expected_output` explicitly requires *different* outcomes, which is the
  within-deal-type discrimination test.
- **Validated**: parses (`python -m json.tool`), uniform 4-key schema, ids 1–13 unique.
- **Straggler fix**: ROADMAP §8 step-1 intro still said "9 test cases / all nine" —
  bumped to 11 (the table beneath it already had rows 10–11); annotated the 2026-06-18
  log entry's "9 cases" forward-reference.

Next: build is unblocked to *run* the suite — but the SKILL.md compression to ≤10KB
should land first, so the run validates the final body, not a draft about to shrink.

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
eval suite (ROADMAP §8 Phase 3, 9 cases — expanded to 11 / 13 fixtures on 2026-06-19;
see that decision-log entry), with the SKILL.md compression to <=10KB still owed before
the PR.

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

*Last updated: 2026-08-16 (Phase 4.5 COMPLETE — divergence map vs upstream's actual merged practice, 12 rows, align/defend called on each. Key find: CONTRIBUTING.md exists and this ROADMAP had never cited it; it is more specific than CONVENTIONS.md / SKILL-AUTHORING-STANDARD.md and settles four rows. Decisions: directory is finance/passive-deal-screener/ (flat — the finance/skills/ nesting is a maintainer post-merge restructure, #591/#593); NO skill-level README ships (0 of 4 merged finance skills have one; not in CONTRIBUTING's guide or PR checklist) — that planned task is deleted, install/usage moves to the root README; §9 corrected — top-level README + CHANGELOG rows DROPPED (CONTRIBUTING rejects skill-count changes and index-file edits; maintainers handle docs/changelog post-merge), leaving finance/CLAUDE.md as the only file outside the skill folder; /cs:screen-deal proposed in the PR description, NOT committed (supersedes the 2026-05-30 lock — the maintainer adds commands in the integration release, cf. #309); PR payload = SKILL.md + references/ + scripts/ + evals/evals.json + examples/, iteration transcripts stay repo-local. One real gap found: CONVENTIONS Required Section #5 is Cross-References and ours is labeled "Related skills" — rename is the next task (+2B against 16B headroom under the 10,240 cap). Pre-empted the py3.14 argparse bug the maintainer hand-fixed after #298 — our % are already escaped %%. --strict was never run on the security auditor; added to the Phase-5 block, which now also branches from upstream/dev directly (fork main is 76 ahead → bloated-diff rejection risk). Ship-gate items closed by extraction: references 258/300/232/227/257 lines, and cross-ref integrity clean — 34 flags, 25 questions, 28 distinct 03 IDs cited by 04, zero dangling IDs across 04 and SKILL.md. §7 has NO open design choices. Remaining: (1) Cross-References rename, (2) root README refresh, (3) Phase 5 (fork sync + validators with --strict + PR). PR note: user wants a detailed PR summary when the upstream PR is opened. Prior — 2026-07-25 (built `examples/` — 3 input/output pairs (equity-syndication / hard-money-fund / private-credit-fund, fixtures 1/3/13) + README index; each output byte-identical to its iteration-3 validated report minus the eval header; CLAUDE.md structure block updated to match. v1.0 examples ship-gate item met. Remaining: skill-level README (finance/passive-deal-screener/README.md), then Phase 5 (sync dev + clean validator pass + PR). Prior — 2026-07-19: ran the upstream validators — security auditor PASSES (0 findings) on the shippable subset, Phase-4 security gate met; skill_validator 76.5 GOOD / quality_scorer F, but their frontmatter/section/line-count FAILs are validator-vs-CONVENTIONS conflicts NOT to be "fixed" (adding the retired fields would get the PR closed); premise corrected — validators present at engineering/skills/, need PYTHONIOENCODING=utf-8; fork dev sync deferred to pre-PR. All three post-eval conformance fixes now DONE. Remaining before PR: examples/, the two READMEs, then Phase-5 (sync dev + clean validator pass + PR). Prior — post-eval conformance fix 2 of 3: graded input-validation layer added to both scripts — boundary `validate_params()`, 0 ok / 1 warnings / 2 bad input, self-tested in `--self-check`, verified by execution; pure cores untouched. Remaining: fix 3 of 3 (fork sync + upstream validators), then examples/, the two READMEs, and the PR. Prior — 2026-07-11: post-eval conformance fix 1 of 3: labeled `## Anti-Patterns` section added to SKILL.md via consolidate-and-relabel — 5 don'ts, SKILL.md 10,224B under the 10,240 cap with 16B headroom, no eval-behavior regression; two adjacent Phase-4 description checks confirmed. Remaining conformance fixes: script exit codes, then fork sync + upstream validators; then examples/, the two READMEs, and the PR. Prior — 2026-07-04: eval cycle 3 CLEARS THE GATE: 12 PASS / 1 w-notes / 0 FAIL, 5/5 discrimination — third consecutive run; S1b boundary pair verified (fixture 1 merits PwC, fixture 9 formula), S2b self-check confirmed in-run (f8 GEN-09, f1 Q-FEE-04); single divergence (f4 HML-05 subsumed by GEN-16) accepted in the decision log; SKILL.md 9,801B, gate held; D1/D4 mirrored into TESTING-PLAN. Phase-3 evals closed after 3 cycles (12/13 → 11/13 → 0 FAILs); Phase-4 eval checkbox checked. Next: post-eval conformance fixes (Anti-Patterns section, script exit codes, fork sync + upstream validators), then examples/ (candidates: iteration-3 reports for fixtures 1/3/12), the two READMEs, and the upstream PR. PR note: user wants a detailed PR summary when the upstream PR is opened.)*
