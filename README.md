# passive-deal-screener

A Claude Code skill that reads a private investment deal — an equity syndication,
preferred equity, a hard money or bridge fund, private credit — and tells you what
a skeptical limited partner would notice. Paste an offering memo, a platform
listing, or a three-sentence GP email, and get back a stress-tested return, a
gross-to-net fee breakdown, severity-ranked red flags, the disclosures that are
*missing*, and the questions to ask — each with a note on what a bad answer sounds
like.

> **Status: v1.0, working.** Installable by hand today (see below). Not yet merged
> upstream — the PR to [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills)
> is pending, so it isn't in the `finance-skills` plugin yet.

---

## Layout

```
passive-deal-screener/
├── SKILL.md          # the skill itself
├── references/       # 01–05, loaded on demand by deal type
├── scripts/          # 2 stdlib-only CLIs (no pip install)
├── examples/         # 3 worked input/output pairs
├── evals/            # 13 fixtures + 3 iteration logs
└── ROADMAP.md        # build plan, decision log, ship gate
```

`ROADMAP.md` owns build status and the full decision history. This file covers
what the skill does and how to run it.

---

## Install

The skill is not on the plugin marketplace yet, so install it by hand. Copy the
three directories that make up the skill — the same subset that ships upstream —
into your personal skills directory:

```bash
git clone https://github.com/dhoovDB/passive-deal-screener.git
mkdir -p ~/.claude/skills/passive-deal-screener
cp -r passive-deal-screener/{SKILL.md,references,scripts} \
      ~/.claude/skills/passive-deal-screener/
```

Restart Claude Code and the skill loads on any deal-analysis prompt — "is this
deal worth pursuing", "what should I ask the GP", "analyze this offering memo".

Once the upstream PR merges, this becomes:

```bash
/plugin install finance-skills@claude-code-skills
```

`ROADMAP.md`, `CLAUDE.md`, and `evals/` are development files and deliberately
stay out of the skill directory.

---

## Usage

### In Claude Code

Paste the deal and ask. No template, no required format — the skill classifies
the deal type itself and loads only the reference slices that type needs.

```
Analyze this deal: [paste the offering memo, listing, or email]
```

Add `output as JSON` to get the structured shape instead of Markdown.

### The two scripts

Both are standalone, stdlib-only (`argparse`, `json`, `math`, `sys` — nothing to install),
and usable without the skill. They compose: the fee calculator gives you a net IRR,
which is the input the benchmark comparator wants.

**What does the LP actually keep?**

```console
$ python scripts/fee_drag_calculator.py --gross-irr 18 --hold-years 5 \
    --carry 20 --hurdle 8 --acquisition-fee 2 --mgmt-fee 2

Fee-drag estimate (screening, not underwriting)
================================================
  ASSUMED (not supplied): catch-up 100, disposition-fee 1, admin-fee 0.3
  These are demo defaults, not disclosed terms - pass 0 for any the deal lacks.

  Gross deal IRR           18.00%
  Estimated net LP IRR     12.31%
  Total fee drag            5.69%  (568 bps/yr)

  Drag breakdown (bps/yr)
    Recurring fees         230.0
    One-time fees           60.0
    Promote                278.5
```

Any input you leave out falls back to the worked example in
`references/02-fee-stack-library.md`, and the output names every value it had to
assume, so a fee the deal never disclosed can't hide in the total. Pass `0` for a
fee or carry the deal doesn't charge.

**Is that good, versus something liquid?**

```console
$ python scripts/benchmark_comparator.py --deal-type multifamily-equity \
    --net-irr 12.31 --hold-years 5

Benchmark comparison (screening, not underwriting)
==================================================
  Comparator           VNQ - Vanguard Real Estate / REITs (6.47% 10yr)
  Implied premium           584 bps over comparator
  Lock-up              5 yr  ->  illiquidity hurdle ~300-400 bps
  Verdict              CLEARS comfortably
```

`--list-types` shows the comparator map. `--json` emits machine-readable output.
`--self-check` runs internal assertions against `references/05`.

Exit codes are graded, because a screening tool that silently accepts a negative
fee is worse than one that refuses and says why:

| Code | Meaning | Example |
|---|---|---|
| `0` | Clean run — every input supplied and plausible | the fee calculator with all thirteen inputs passed |
| `1` | Runs, but check the inputs — warning on stderr, result still on stdout. Either a likely unit slip, or some inputs were filled from demo defaults | `--gross-irr 999` ("15 means 15%, not 0.15"); the sample above (three inputs assumed) |
| `2` | Structurally invalid, rejected with no output | `--hold-years 0`, `--mgmt-fee -1`, `--gross-irr nan` |

Comparator figures are hardcoded from dated snapshots in `references/data/`
(`LAST_UPDATED 2026-06-12`) — the stdlib-only constraint rules out a live data
pull. Pass `--benchmark-return` to override with a current figure.

---

## What you get back

Three complete worked examples live in [`examples/`](examples/), one per deal type,
each a real validated run rather than an illustration:

| Example | Deal type | Verdict |
|---|---|---|
| [`equity-syndication/`](examples/equity-syndication/) | Value-add multifamily | Pursue with conditions |
| [`hard-money-fund/`](examples/hard-money-fund/) | Senior-secured bridge fund | Pursue with conditions |
| [`private-credit-fund/`](examples/private-credit-fund/) | Diversified BDC-style credit | Pursue with conditions |

All three land on *Pursue with conditions* because they are the sound deals in the
suite. The Pass and Pass-as-presented paths — packed red flags, sparse
solicitations, aggressive development pro formas — are exercised in `evals/`.

---

## What's different about it

Surveyed against existing real-estate and deal-analyzer skills, the positioning is:

- **Missing disclosures are first-class output.** What a deal *doesn't* say matters
  as much as what it does. Most analyzers silently skip absences; this one names
  them and routes each to a question.
- **Public-market benchmark comparison.** Every deal must clear a liquid,
  net-of-fee hurdle plus an illiquidity premium. The question is never "is 14%
  good?" but "is 14% net, illiquid, for 7 years, good *versus* what I could hold
  liquid and free?"
- **Bad-answer signals on every question.** Not "ask the GP about the waterfall"
  but "ask about the waterfall, and a vague answer about 'industry-standard
  structure' is the evasion signal."
- **Source-agnostic.** No template required. An email blast, a platform listing,
  and a full offering memo are handled identically.
- **LP lens only.** Never assumes you are acquiring, developing, or operating. No
  deal-sourcing or asset-management framing.

---

## How it was built

**The evaluator came first.** The reference files and the eval suite were specified
before `SKILL.md` was written, so the skill was built against a harness that
already knew how to fail it.

- **Five reference files, 1,274 lines** — asset-class norms, a fee-stack library,
  34 red flags with `{ASSET_CLASS}-{NN}` IDs, 25 LP questions each citing the flags
  they answer, and public-market comparators. The skill loads a named slice per
  deal type, not the whole set.
- **13 eval fixtures across 3 iteration cycles** — 12 PASS / 1 PASS-with-notes /
  0 FAIL on the final run, with 5/5 on the discrimination tests that check the
  screener distinguishes sound deals from bad ones instead of flagging everything.
  The last two cycles ran under generator ≠ grader ≠ author separation.
- **No invented numbers.** Where a fee range or market norm isn't well established,
  it is flagged as *variable* rather than fabricated. Benchmark figures trace to
  dated snapshots in `references/data/`.

The full decision log, including the calls that were later reversed, is in
[ROADMAP.md](ROADMAP.md).

---

## Where it's going

Contribution target: [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills)
under `finance/`, via the `dhoovDB` fork, as a PR to the `dev` branch.

A companion React artifact (`deal-evaluator.jsx`) exists for the claude.ai chat
surface. It shares the analytical framework but is a separate deliverable on a
separate maintenance path, and is gitignored here — the skill stays Markdown-first
and free of UI concerns.

---

Built with [Claude Code](https://claude.com/claude-code). The analytical framework
is grounded in the author's background as a commercial credit analyst and
short-term-rental operator, oriented to passive LP investing rather than direct
operation.

License: MIT, matching the upstream skills repo.
