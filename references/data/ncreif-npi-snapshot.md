# NCREIF NPI Snapshot

The **NCREIF Property Index (NPI)** — the institutional private commercial
real-estate benchmark — measures unlevered total return on a large pool of
institutional-quality properties held by NCREIF members. It is the closest thing
to an "unlevered, in-place" baseline for private equity real estate, which makes
it the grounding figure for the financing-story flag (`03` → `GEN-07`): a deal
whose levered IRR towers over the NPI is earning its excess from leverage and
cap-rate movement, not operations.

**As of:** Q4 2025 (most recent reported)
**Captured:** 2026-06-06
**Source:** NCREIF, via public secondary reporting (NPI detail beyond the
headline is membership-gated)

## Values (Q4 2025)

| Metric | Value | Period | Source |
|---|---|---|---|
| NPI total return (quarterly) | 1.1% | Q4 2025 | RCLCO / Capital Economics |
| NPI total return (trailing 4-quarter) | 4.9% | 2025 full year | RCLCO / Capital Economics |
| NPI income return (trailing) | ≈ 4.8% | held ~4.8% for 5 consecutive quarters | Capital Economics |
| NPI appreciation (annual) | ≈ 0.2% | 2025 full year | Capital Economics |

Read together: 2025's ~4.9% total return was **almost entirely income** (~4.8%),
with appreciation roughly flat (~0.2%). That is the empirical anchor for LP
skepticism of deals underwriting large appreciation — at the institutional index
level, appreciation contributed almost nothing in 2025.

## By property type (2025 annual total return)

| Property type | 2025 total return | Source |
|---|---|---|
| Retail | 6.8% | RCLCO / Capital Economics |
| Residential | 5.3% | RCLCO / Capital Economics |
| Industrial | 4.5% | RCLCO / Capital Economics |
| Office | 3.4% | RCLCO / Capital Economics |

These pair with `01-asset-class-norms.md`: office's 3.4% (lagging, consistent
with the post-2020 *variable* baseline) and retail's lead are both LP-lens
signals about which sectors carried the index.

## How `05` uses this

NPI is the **unlevered private-RE baseline**. The design-review DoD for `05`
(2026-06-01) requires an unlevered comparator alongside each headline ETF return
so the skill can separate "clears the illiquidity hurdle" from "IRR is driven by
leverage, not alpha." The NPI total return is that unlevered grounding for equity
real estate: if a syndication's *unlevered* projected return doesn't beat the NPI
for its property type, the LP is being paid for leverage risk, not operating
skill.

## Provenance / gated-source note

The public NPI headline (quarterly and trailing total return, income, broad
property-type splits) is widely reported by NCREIF data partners — RCLCO's
quarterly NPI/ODCE recap and Capital Economics' NCREIF update are the sources
here. **Property-level detail, ODCE fund-level returns, and the full
sub-type/region matrices are membership-gated** behind NCREIF and are not
captured. On refresh, pull the next quarter's headline from the same public
recaps; if NCREIF membership becomes available, replace with the primary release.
