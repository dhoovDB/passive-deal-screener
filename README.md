# passive-deal-screener

A Claude Code skill for screening passive real estate and private market
investment opportunities — equity syndications, preferred equity, hard money
and bridge debt funds, and private credit — from the **limited-partner**
(LP) perspective.

> **Status: Pre-development.** Not installable yet. The factual foundation
> (`references/01-asset-class-norms.md`) is shipped; the remaining four
> reference files, the skill itself (`SKILL.md`), the Python scripts, and the
> example deals are planned. See [ROADMAP.md](ROADMAP.md) for the build order
> and v1.0 ship gate. This README is the public-facing introduction to the
> repo — the eventual skill-level README (install + usage) ships with the
> upstream contribution.

---

## What it does (preview)

Paste any deal — a full offering memo, a CrowdStreet listing, a GP email
blast, a one-page teaser — and get back a structured analysis:

1. **Deal snapshot** — classified by asset class, deal type, sponsor, hold
   period, target return.
2. **Return stress-test** — claimed net IRR compared to category norms
   (`01-asset-class-norms.md`) and public-market comparators
   (`05-benchmark-returns.md`); illiquidity premium implied.
3. **Fee-stack breakdown** — every disclosed fee mapped against
   `02-fee-stack-library.md`; aggregate drag from gross IRR to net.
4. **Red flags + missing disclosures** — what's present and concerning,
   *and* what's absent that should be present at this deal type's category
   baseline. Absent is first-class output.
5. **GP alignment signals** — track-record, co-invest, prior-exits evidence;
   marketing-heavy language patterns.
6. **Prioritized questions for the GP** — ranked by importance, each with
   **explicit signals for what a bad answer looks like** (evasion patterns,
   not just "ask this").
7. **Verdict** — Pursue / Pass / Pursue with conditions, with the reasoning
   visible.

The skill produces structured Markdown by default; pass `output as JSON` to
get the JSON shape consumed by the companion React artifact.

---

## What's different about it

Surveyed against existing real-estate / deal-analyzer skills (May 2026), the
positioning is:

- **Source-agnostic input parsing.** No template required. Works on email
  blasts, platform listings, and offering memos identically.
- **Missing disclosures as a first-class output.** What a deal *doesn't* say
  matters as much as what it does. Most analyzer skills silently skip over
  absences; this one names them.
- **Public market benchmark comparison.** Forces every deal to clear a real
  hurdle — the spread over the closest liquid equivalent — not just an
  internal pro forma.
- **Bad-answer signals on questions.** Not "ask the GP about the waterfall"
  but "ask about the waterfall, and a vague answer about 'industry-standard
  structure' is the evasion signal."
- **LP perspective only.** Never assumes the user is acquiring, developing,
  or operating. No deal-sourcing or asset-management framing.

The full competitive analysis is in [ROADMAP.md §1](ROADMAP.md).

---

## Repo layout

```
passive-deal-screener/
├── CLAUDE.md          # developer guide — read this before contributing
├── ROADMAP.md         # build plan, decision log, v1.0 ship gate
├── README.md          # this file — repo-level introduction
├── references/
│   ├── 01-asset-class-norms.md   # ✅ shipped — LP factual baseline by asset class
│   │
│   │ Planned:
│   ├── 02-fee-stack-library.md   # every fee, every deal type, with aggressive thresholds
│   ├── 03-red-flag-library.md    # ≥25 flags, categorized, with severity + response questions;
│   │                             #   flag IDs in {ASSET_CLASS}-{NN} format
│   ├── 04-question-bank.md       # ≥20 LP questions, good + bad answer signals; cites ≥5 flag IDs from 03
│   ├── 05-benchmark-returns.md   # public-market comparators + illiquidity-premium framework
│   │                             #   (data pull required before writing — see references/data/)
│   └── data/                     # versioned snapshots from external sources
│       ├── README.md             #   vintage, source, and update instructions
│       ├── ncreif-npi-snapshot.md
│       ├── fred-10yr-snapshot.md
│       └── preqin-vintage-note.md
│
│ Planned (after references):
│   ├── SKILL.md       # the skill body — workflow, output schema, analyst rules
│   ├── scripts/       # fee_drag_calculator.py + benchmark_comparator.py
│   └── examples/      # ≥3 input/output pairs per asset class, with anonymized real deals where shareable
│
└── deal-evaluator.jsx # gitignored — React artifact companion (claude.ai chat surface)
```

The React artifact (`deal-evaluator.jsx`) and the Claude Code skill share
analytical logic but ship to different surfaces: the artifact is a
claude.ai-embedded UI prototype; the skill is the CLI-and-multi-platform
contribution. They're kept separate so the skill stays Markdown-first and
free of UI concerns. The artifact is gitignored.

---

## Where it'll live

Contribution target: [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills)
under `finance/`, via the `dhoovDB` fork. Branch strategy: feature branches
targeting upstream `dev`, never `main`. Once merged, the skill installs
alongside the existing finance skills in that repo.

The eventual install instructions and usage examples ship in a
**skill-level** `README.md` at `finance/passive-deal-screener/README.md`
inside the upstream PR — distinct from this repo-level README, which exists
to introduce the *repository* (build context, status, layout) rather than
the *skill* (which doesn't ship yet).

---

## Current build status

| Artifact | Status |
|---|---|
| `CLAUDE.md` (dev guide) | ✅ Shipped |
| `ROADMAP.md` (build plan + decision log) | ✅ Shipped — schemas for `02–05`, v1.0 ship gate, 8 eval cases all defined |
| `references/01-asset-class-norms.md` | ✅ Shipped 2026-05-25 |
| `references/02-fee-stack-library.md` | Planned (next in build order) |
| `references/03-red-flag-library.md` | Planned |
| `references/04-question-bank.md` | Planned |
| `references/05-benchmark-returns.md` | Planned — requires data pull (NCREIF NPI, FRED 10yr, Preqin vintage note) before writing |
| `SKILL.md` | Planned (after references) |
| `scripts/` | Planned (after SKILL.md) |
| `examples/` | Planned (after SKILL.md, ≥3 pairs) |

See [ROADMAP.md §8 v1.0 ship gate](ROADMAP.md) for the full list of
conditions before the upstream PR opens.

---

## Author note

Built collaboratively with [Claude Code](https://claude.com/claude-code).
Analytical framework grounded in the author's background as a commercial
credit analyst and short-term-rental operator, with goals oriented to
passive LP investing rather than direct operation.

License: MIT (matching the upstream skills repo).
