# passive-deal-screener — Developer Guide

A Claude Code skill for screening passive real estate and private market 
investment opportunities from the LP perspective. Paste any deal from any 
source and get back a structured analysis: deal snapshot, return 
stress-test, fee-stack breakdown, red flags, missing disclosures, GP 
alignment signals, and prioritized questions with explicit signals for 
what a bad answer looks like.

## Before you do anything

Run `/globalrules` now. It contains the delegation rules, approval gates, 
status reporting format, and architecture principles that govern every 
session. The rest of this file assumes those rules are active.

---

## Contribution target

Upstream repo: `alirezarezvani/claude-skills`
Domain: `finance/`
Branch strategy: feature branches targeting `dev`. Never commit directly 
to `main`.
PR from: `dhoovDB` fork

---

## Architecture

This skill has two distinct surfaces. Keep them separate.

**SKILL.md** — the Claude Code skill. This is the primary contribution 
to the upstream repo. It loads reference files, applies the LP analytical 
framework, and produces structured deal analysis inside a Claude Code 
session.

**deal-evaluator.jsx** — a React artifact for claude.ai. A companion 
demo tool, not the primary deliverable. It shares analytical logic with 
the skill but lives in a separate surface and has a separate maintenance 
path. Do not conflate the two.

---

## File structure

Ships upstream (the PR payload) is marked **[PR]**; everything else is
development-only and stays in this repo.

```
passive-deal-screener/
├── SKILL.md                        [PR] primary contribution
├── README.md                            product README — install, usage, positioning
├── CLAUDE.md                            this file
├── ROADMAP.md                           task list, decision log, ship gate
├── references/                     [PR]
│   ├── 01-asset-class-norms.md          factual foundation, build first
│   ├── 02-fee-stack-library.md          fee ranges by asset class
│   ├── 03-red-flag-library.md           34 flags, {ASSET_CLASS}-{NN} IDs
│   ├── 04-question-bank.md              25 LP questions + bad-answer signals
│   ├── 05-benchmark-returns.md          public market comparators
│   └── data/                            dated source snapshots (LAST_UPDATED 2026-06-12)
├── scripts/                        [PR] stdlib-only, graded exit codes 0/1/2
│   ├── fee_drag_calculator.py           gross-to-net drag + waterfall
│   └── benchmark_comparator.py          net IRR vs public comparator + illiquidity hurdle
├── examples/                       [PR]
│   ├── README.md                        index of the three pairs
│   ├── equity-syndication/              fixture 1 (value-add multifamily)
│   ├── hard-money-fund/                 fixture 3 (senior-secured bridge fund)
│   └── private-credit-fund/             fixture 13 (diversified BDC-style)
│                                        each: input.md + output.md
├── evals/
│   ├── evals.json                  [PR] 13 fixtures
│   ├── iteration-1..3/                  run transcripts + scorecards — process, not product
│   ├── TESTING-PLAN.md                  eval design
│   └── sources.md                       fixture provenance
└── deal-evaluator.jsx                   gitignored — claude.ai React artifact, separate surface
```

---

## Build order

References before SKILL.md. Every reference file is a dependency of the 
skill. Building SKILL.md before the references are complete produces a 
skill that hallucinates the factual foundation it is supposed to draw from.

Order:
1. CLAUDE.md (this file)
2. references/01-asset-class-norms.md
3. references/02-fee-stack-library.md
4. references/03-red-flag-library.md
5. references/04-question-bank.md
6. references/05-benchmark-returns.md
7. SKILL.md
8. examples/ (one per asset class)

---

## Content rules

**No hallucinated ranges.** If a fee range, return expectation, or 
market norm is not well-established in practice, flag it as variable 
rather than inventing a number. The references are a factual foundation. 
A wrong number in 01-asset-class-norms.md propagates through every 
analysis the skill produces.

**LP lens only.** Every file is written from the passive investor 
perspective. Operator-focused analysis (deal sourcing, underwriting for 
acquisition, asset management decisions) is out of scope.

**Source-agnostic.** The skill must work equally well on deals from 
EquityMultiple, CrowdStreet, direct GP email blasts, and any other 
source. Do not hardcode assumptions about deal format or presentation.

**Missing disclosures are first-class output.** What a deal does not 
say is as important as what it does. The skill should flag absent 
information explicitly, not silently pass over it.

---

## What not to do

- Do not build SKILL.md before all reference files are reviewed and 
  approved.
- Do not merge operator-focused analysis into LP-focused files.
- Do not invent market norms. Flag uncertainty explicitly.
- Do not conflate the SKILL.md and deal-evaluator.jsx surfaces.
- Do not commit to main directly. Feature branches only.

---

## Decision log

*Project and architectural decisions are logged in `ROADMAP.md` (including the primary-deliverable and references-first build-order decisions previously kept here). This log tracks changes to this CLAUDE.md only.*

### 2026-05-24 — Created CLAUDE.md
woohoo!