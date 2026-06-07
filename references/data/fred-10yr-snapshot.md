# FRED 10-Year Treasury Snapshot

**Series:** `DGS10` — Market Yield on U.S. Treasury Securities at 10-Year
Constant Maturity, quoted on an investment basis (daily).
**Source:** FRED, Federal Reserve Bank of St. Louis —
<https://fred.stlouisfed.org/series/DGS10>
**As of:** early June 2026 (most recent daily close cited below)
**Captured:** 2026-06-06

## Value

| Metric | Value | As of | Source |
|---|---|---|---|
| 10yr Treasury (DGS10) | **≈ 4.5%** | early June 2026 | FRED `DGS10`, via public reporting |
| Most recent daily close cited | 4.54% | most recent Friday, early June 2026 | TradingEconomics (US 10Y) |
| Intra-week range that week | 4.46% – 4.54% | early June 2026 | TradingEconomics (US 10Y) |

The week's move reflected a stronger-than-expected jobs report and a market
re-pricing toward a possible additional Fed hike by year-end — context only;
the snapshot value is the level, not the narrative.

## Why this file exists

The 10yr Treasury is the **risk-free anchor** for the illiquidity-premium
framework in `05-benchmark-returns.md`. The rule of thumb there — an LP should
demand ≥200bps over the closest *public* comparator, scaled by lock-up — sits on
top of the risk-free rate. When the 10yr moves materially, the entire premium
calculation shifts, which is why this is the file most sensitive to staleness.

## Provenance / refresh note

FRED's own pages (`/series/DGS10`, the `fredgraph.csv` endpoint) returned HTTP
403 to automated fetch on 2026-06-06, so the value here is the publicly reported
daily close, not a direct FRED pull. **On refresh, confirm the precise current
`DGS10` value directly at FRED** (the figure above is a daily-volatile market
rate and should be re-pulled, not assumed). FRED `DGS10` is the authoritative
daily series; `GS10` is its monthly-average sibling if a smoothed figure is
preferred.
