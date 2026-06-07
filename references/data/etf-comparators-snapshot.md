# Public ETF Comparators Snapshot

Trailing total returns and expense ratios for the seven public-market
comparators `05-benchmark-returns.md` uses to give each private deal type a
liquid, net-of-fee hurdle.

**As of:** trailing returns reported as of the **Q1 2026 quarter-end
(2026-03-31)** per fund fact sheets, cross-checked against public aggregators
reporting through early June 2026.
**Captured:** 2026-06-06
**Basis:** NAV total return, **post-expense-ratio** (net to a public investor) —
apples-to-apples with net-to-LP private returns. Never compare these to a
private deal's *gross* IRR.

## At-a-glance

| Ticker | Fund | Trailing 5yr | Trailing 10yr | Expense ratio | Best comparator for |
|---|---|---|---|---|---|
| SPY | SPDR S&P 500 | 14.11% | 15.54% | 0.0945% | Universal equity anchor — the opportunity cost every private deal competes with |
| VNQ | Vanguard Real Estate (REIT) | 5.13% | 6.47% | 0.13% | Equity RE / REIT — multifamily, industrial, retail equity syndications |
| IYR | iShares U.S. Real Estate | 5.7%–6.7% † | 6.4%–6.8% † | 0.39% | Equity RE alternative to VNQ (Dow Jones U.S. Real Estate Capped) |
| LQD | iShares iBoxx $ IG Corp Bond | ≈ 0.1% ‡ | ≈ 3.1% ‡ | 0.14% | Stabilized core / investment-grade-quality debt; senior preferred-equity proxy |
| HYG | iShares iBoxx $ High Yield Corp | 3.8% | 5.0% | 0.49% | High yield / private credit & hard-money fund proxy |
| PFF | iShares Preferred & Income Securities | 1.6% | 3.72% | 0.45% | Preferred equity |
| PRIV | SPDR SSGA IG Public & Private Credit | n/a ※ | n/a ※ | 0.70% | Public + private credit — the most direct private-credit proxy, but too new for trailing returns |

† **IYR divergence:** aggregators disagreed materially this pull — 5yr quoted
between 5.7% and 6.7%, 10yr between 6.4% and 6.8%. Both ranges shown rather than
a false-precision single figure; confirm against the iShares fact sheet
(as of 2026-03-31) on refresh. VNQ is the cleaner, lower-cost REIT comparator
and should be the primary; IYR is the cross-check.

‡ **LQD low 5yr:** the ≈0.1% 5yr is single-sourced and reflects the 2022 IG-bond
drawdown sitting inside the trailing window; the 3yr was ≈4.0% as the drawdown
rolls off. Treat the 5yr as directional (IG corporates went roughly nowhere over
five years) and confirm the precise figure against the LQD fact sheet on refresh.

※ **PRIV too new:** inception 2025-02-26; only ~1 year of history, so no 5yr/10yr
trailing return exists. Since-inception NAV return was 1.81% as of 2025-06-30.
PRIV is the *conceptually* closest public proxy for a public+private IG-credit
sleeve, but it carries no trailing track record yet — note this explicitly when
`05` uses it; lean on HYG/LQD for credit hurdles until PRIV seasons.

## Per-comparator notes

- **SPY (0.0945%)** — the universal anchor. A private deal's net-to-LP return
  must clear SPY *plus* an illiquidity premium to justify the lock-up, since SPY
  is daily-liquid and nearly free. Its 10yr (15.54%) reflects an unusually strong
  equity decade; weight that when using it as the hurdle.
- **VNQ (0.13%)** — broad U.S. REITs; the cleanest liquid proxy for equity real
  estate. Lower-cost and more diversified than IYR. Primary RE comparator.
- **IYR (0.39%)** — narrower, pricier REIT index; useful only as a cross-check on
  VNQ. The higher expense ratio is itself an LP-lens point: same exposure, more
  drag.
- **LQD (0.14%)** — investment-grade corporates; the liquid analog for stabilized
  "core" cash-flow risk and the senior end of preferred equity. Its rate
  sensitivity is the cautionary tale for any private deal selling "bond-like"
  stability.
- **HYG (0.49%)** — high-yield corporates; the closest liquid proxy for
  hard-money / bridge funds and private credit. The 5.0% 10yr is the number a
  private credit fund's net-to-LP yield should be measured against, with a
  premium for illiquidity and single-borrower concentration.
- **PFF (0.45%)** — preferred securities; the direct liquid comparator for
  preferred-equity positions. Its modest trailing returns (1.6% 5yr / 3.72% 10yr)
  set a sober bar for preferred-equity deals claiming equity-like returns.
- **PRIV (0.70%)** — public+private IG credit; conceptually the most direct
  private-credit comparator, but unseasoned. Highest expense ratio of the set.

## Known gap — volatility / std-dev

This pull did **not** capture per-ticker volatility (standard deviation). The
`05` format calls for a `Vol` column; populate it on the next refresh from the
fact sheets, which report standardized trailing std-dev (commonly 3yr/5yr/10yr).
Flagged rather than filled with an invented figure.

## Provenance

Issuer fact sheets — iShares (VNQ via Vanguard; IYR, LQD, HYG, PFF), Vanguard
(VNQ), SSGA (SPY, PRIV) — are the authoritative source and return HTTP 403 to
automated fetch. Figures above are from public aggregators reporting those
fact-sheet and daily-close numbers: financecharts.com, stockanalysis.com,
Morningstar, Yahoo Finance, slickcharts (SPY), and SSGA fund docs (PRIV
inception/expense). Cross-checked across ≥2 sources per ticker; divergences are
flagged above (†, ‡). **On refresh, prefer the most recent quarter-end
fact-sheet figures for a uniform as-of date.**
