# passive-deal-screener — Developer Guide

A Claude Code skill that screens passive real-estate and private-market deals
from the LP perspective. `README.md` describes the product; `ROADMAP.md` owns
status, plan, and decisions. This file covers how to work in the repo.

## Before you do anything

Run `/globalrules` now. It contains the delegation rules, approval gates,
status reporting format, and architecture principles that govern every
session. The rest of this file assumes those rules are active.

---

## Two branches of work, two git rules

- **This repo** is the development workspace. Commits go straight to `main`
  and are pushed after approval.
- **The upstream contribution** (`alirezarezvani/claude-skills`, `finance/`)
  is a separate branch in the `claude-skills` clone, cut from `upstream/dev`
  and PR'd to `:dev` from the `dhoovDB` fork. Never commit to upstream `main`,
  and never branch from the fork's `main` (see `ROADMAP.md` → Phase 5).

---

## File structure

Ships upstream (the PR payload) is marked **[PR]**; everything else stays here.

```
passive-deal-screener/
├── SKILL.md                        [PR] the skill
├── README.md                            product README — install, usage, positioning
├── CLAUDE.md                            this file
├── ROADMAP.md                           status, plan, decision log
├── references/                     [PR]
│   ├── 01-asset-class-norms.md          net-to-LP baselines + essential disclosures per asset class
│   ├── 02-fee-stack-library.md          fees by deal type, waterfalls, total-drag framework
│   ├── 03-red-flag-library.md           flags with {PREFIX}-{NN} IDs
│   ├── 04-question-bank.md              GP questions + bad-answer signals, citing 03 IDs
│   ├── 05-benchmark-returns.md          public comparators + illiquidity-premium framework
│   └── data/                            dated source snapshots behind every number in 05
├── scripts/                        [PR] stdlib-only, graded exit codes 0/1/2, --self-check
│   ├── fee_drag_calculator.py           gross-to-net drag + waterfall
│   └── benchmark_comparator.py          net IRR vs public comparator + illiquidity hurdle
├── examples/                       [PR] three validated input/output pairs + README index
├── evals/
│   ├── evals.json                  [PR] 13 fixtures
│   ├── iteration-1..2/                  scorecards only (transcripts in git history)
│   ├── iteration-3/                     run transcripts + scorecard
│   ├── TESTING-PLAN.md                  eval design
│   └── sources.md                       fixture provenance
├── tools/
│   └── refresh_benchmarks.py            pulls FRED + Yahoo, computes the benchmark figures (makes network calls; never ships)
└── deal-evaluator.jsx                   gitignored claude.ai React artifact — a separate surface, not contributed
```

---

## Content rules

**No invented numbers.** If a fee range, return expectation, or market norm
isn't well established, write *variable* and say why. Every benchmark figure
traces to a dated snapshot in `references/data/`. A wrong number in a reference
propagates into every analysis the skill produces.

**LP lens only.** Every file is written for the passive investor. Operator work
(sourcing, acquisition underwriting, asset management) is out of scope.

**Source-agnostic.** The skill must handle a platform listing, a GP email blast,
or three sentences of raw terms equally well. No format assumptions.

**Missing disclosures are first-class output.** What a deal doesn't say is
flagged and routed to a question, never passed over.

**Keep IDs stable.** Flag IDs in `03` and question IDs in `04` are cited from
SKILL.md, `04`, and `evals/evals.json`. New entries take the next ID in their
sequence; existing IDs are never renumbered.

**Size budget.** Upstream's authoring standard says SKILL.md ≤10KB. Hold it under
10,000 bytes (the strict reading); any addition needs a compensating trim.

---

## Working on the scripts

- The calculation functions are pure; argument parsing, validation, and printing
  sit at the boundary (`parse_args`, `validate_params`, `format_human`, `main`).
- Both scripts are stdlib-only and must stay that way — upstream requires it.
- After any change, run `python scripts/<name>.py --self-check`. On Windows, set
  `PYTHONIOENCODING=utf-8` for the upstream validators.
- Benchmark refresh: `python tools/refresh_benchmarks.py`, then follow the steps
  in `references/data/README.md`. The comparator's self-check fails if its
  constants drift from `05`.

---

## Decision log

*Project and architectural decisions are logged in `ROADMAP.md`. This log tracks
changes to this CLAUDE.md only.*

### 2026-09-27 — Brought current after v1.0

Dropped the finished build order and "don't build SKILL.md yet" rules. Scoped the
main-branch rule: commits to this repo's `main` are normal; the rule applies to
the upstream contribution. Added the stable-ID, size-budget, and script-workflow
sections, and `tools/` to the file tree. The React artifact is now described once.

### 2026-05-24 — Created CLAUDE.md
