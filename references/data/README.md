# `references/data/` — versioned source snapshots

This folder holds the external-source data that `05-benchmark-returns.md`
synthesizes into LP-facing benchmark comparisons. It exists so that **every
number in `05` traces to a dated, source-cited snapshot** — a v1.1 refresh is
"re-pull into these snapshots," not "rewrite `05`'s prose." This is the
"no hallucinated ranges" rule (CLAUDE.md) enforced at the data boundary: the
highest-stakes place for it, because a wrong benchmark silently corrupts every
illiquidity-premium comparison the skill makes.

## Files

| File | Source | As of | What it holds |
|---|---|---|---|
| `fred-10yr-snapshot.md` | FRED `DGS10` / `DGS2` / `DGS3MO` (St. Louis Fed) | 10yr early June 2026; short points 2026-06-11 | Treasury curve — 10yr risk-free anchor + 3mo/2yr short points for duration-matching debt deals |
| `etf-comparators-snapshot.md` | Fund fact sheets, cross-checked vs public aggregators | Q1 2026 quarter-end (2026-03-31) / latest daily | Trailing 5yr/10yr total returns + expense ratios for the 7 public comparators |
| `ncreif-npi-snapshot.md` | NCREIF (via public secondary reporting) | Q4 2025 | NPI total / income / appreciation returns — the institutional private-RE baseline |
| `preqin-vintage-note.md` | Preqin (via public secondary citation) | 2001–2017 study window (latest public) | Categorical note on private-fund vintage-year net-IRR dispersion |

## How the figures were captured (2026-06-06)

Captured via `WebSearch` across public aggregators (financecharts.com,
stockanalysis.com, Morningstar, Yahoo Finance) and public secondary reporting
of institutional indices (RCLCO, Capital Economics, CAIS). **Issuer fact sheets
(ishares.com, vanguard.com, ssga.com) and FRED's own pages return HTTP 403 to
automated fetch**, so the figures here come from aggregators reporting those
sources, not the issuers directly. Where two aggregators diverged materially,
both are shown rather than one chosen silently.

Gated sources are marked as such: NCREIF detail beyond the public headline, and
Preqin's current per-vintage quartile tables, sit behind membership/subscription
paywalls. The snapshots capture the latest *publicly reported* figure and flag
the rest categorical — a documented gap is a correct output; a fabricated number
is a defect.

## Refresh procedure (v1.0 → v1.1)

1. **ETF returns** — re-run the per-ticker trailing-return searches; prefer the
   most recent quarter-end fact-sheet figures (uniform as-of date across funds).
   Cross-check each against ≥2 aggregators; fix the basis as **NAV total return,
   post-expense** (apples-to-apples with net-to-LP private returns).
2. **FRED 10yr** — confirm the current `DGS10` daily close at
   <https://fred.stlouisfed.org/series/DGS10> (or its CSV endpoint if fetchable).
3. **NCREIF NPI** — pull the latest quarter's NPI total/income/appreciation from
   NCREIF's release or public secondary reporting; update the vintage quarter.
4. **Preqin** — if a subscription is available, replace the categorical note with
   current per-vintage quartile boundaries; otherwise re-confirm the public
   secondary citation and its study window.
5. Update each file's `LAST_UPDATED` / `As of` stamp, then update `05`'s table
   and its own `LAST_UPDATED`.

Annual refresh is the minimum cadence; refresh sooner if a rate regime shifts
materially (the 10yr anchor moves the whole illiquidity-premium calculation).
