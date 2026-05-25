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
passive-deal-screener/
SKILL.md                          ← primary contribution
CLAUDE.md                         ← this file
ROADMAP.md                        ← task list and decision log
references/
01-asset-class-norms.md         ← factual foundation, build first
02-fee-stack-library.md         ← fee ranges by asset class
03-red-flag-library.md          ← warning signs by category
04-question-bank.md             ← LP questions + bad answer signals
05-benchmark-returns.md         ← public market comparators
examples/
equity-syndication/
input.md
output.md
preferred-equity/
input.md
output.md
hard-money-fund/
input.md
output.md

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

### 2026-05-24 — Created CLAUDE.md
woohoo!

### 2026-05-24 — Primary deliverable is SKILL.md, not the React artifact

The React artifact (deal-evaluator.jsx) was built first as an analytical 
prototype in claude.ai. The Claude Code skill is the contribution target. 
They share analytical logic but serve different surfaces and audiences. 
Keeping them separate prevents the skill from inheriting UI concerns that 
do not belong in a markdown-first tool.

### 2026-05-24 — References built before SKILL.md

The skill draws from reference files for all factual claims about market 
norms, fee ranges, and return expectations. Building the skill before the 
references are complete means the skill hallucinates its own foundation. 
Build order is enforced in this file and in ROADMAP.md.