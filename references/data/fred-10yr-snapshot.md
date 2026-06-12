# FRED 10-Year Treasury Snapshot

**Series:** `DGS10` (10yr, the headline anchor), plus short points `DGS2` (2yr)
and `DGS3MO` (3-month) for duration-matching debt comparators — all Market Yield
on U.S. Treasury Securities at constant maturity, investment basis (daily).
**Source:** FRED, Federal Reserve Bank of St. Louis —
<https://fred.stlouisfed.org/series/DGS10>
**As of:** 10yr early June 2026; short points 2026-06-11 (daily closes below)
**Captured:** 2026-06-06 (10yr); 2026-06-12 (2yr, 3mo short points)

## Value — Treasury curve

| Point | Value | As of | Duration-matches | Source |
|---|---|---|---|---|
| 3-month T-bill (DGS3MO) | **≈ 3.71%** | 2026-06-11 | very-short hard money (6–18mo loans) | TradingEconomics (US 3M) |
| 2-year (DGS2) | **≈ 4.15%** | 2026-06-11 | short/mid private debt | TradingEconomics (US 2Y) |
| 10-year (DGS10) | **≈ 4.5%** | early June 2026 | equity-RE hold (~7yr); general anchor | FRED `DGS10`, via public reporting |

The curve is normally upward-sloping (3.71% → 4.15% → 4.5%). 10yr supporting
detail: most recent daily close 4.54%, intra-week range 4.46–4.54% (early June
2026, TradingEconomics US 10Y).

The week's move reflected a stronger-than-expected jobs report and a market
re-pricing toward a possible additional Fed hike by year-end — context only;
the snapshot value is the level, not the narrative.

## Why this file exists

The 10yr Treasury is the **risk-free anchor** for the illiquidity-premium
framework in `05-benchmark-returns.md`. The rule of thumb there — an LP should
demand ≥200bps over the closest *public* comparator, scaled by lock-up — sits on
top of the risk-free rate. When the 10yr moves materially, the entire premium
calculation shifts, which is why this is the file most sensitive to staleness.

The **short points** exist so debt deals get a *duration-matched* floor: a 6–18mo
hard-money fund's honest risk-free comparison is the 3mo/2yr bill, not the 10yr.
`05` reads a debt deal's net yield over the duration-matched Treasury as the
**credit + illiquidity spread** the LP is paid for taking the risk.

## Provenance / refresh note

FRED's own pages (`/series/DGS10`, the `fredgraph.csv` endpoint) returned HTTP
403 to automated fetch on 2026-06-06, so the value here is the publicly reported
daily close, not a direct FRED pull. **On refresh, confirm the precise current
`DGS10` value directly at FRED** (the figure above is a daily-volatile market
rate and should be re-pulled, not assumed). FRED `DGS10` is the authoritative
daily series; `GS10` is its monthly-average sibling if a smoothed figure is
preferred.
