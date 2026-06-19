# Eval Sources — provenance index

Where each eval fixture's facts come from. Per `TESTING-PLAN.md` §3 and §9:

- **Real sources** are cited below with URL + as-of date + the facts extracted.
  Facts and disclosed terms only (not copyrightable); **no offering-memo or
  reviewer prose** is copied. Names, addresses, and sponsors are **scrubbed** from
  the built fixtures in `inputs/` and `examples/` (public repo) — they appear here,
  in the provenance log, only as citations.
- **Synthetic fixtures** are registered at the bottom and labeled synthetic, so a
  reviewer knows which fixtures validate *mechanics* vs *real-world accuracy*
  (`TESTING-PLAN.md` §2.2).

Full term extraction (complete fee tables, LTV specifics, waterfall language)
happens when each `inputs/NN-slug.md` fixture is built, reading the cited document
directly. This file is the index; the headline facts below are what the source was
selected for.

*Research pull: 2026-06-19. Re-confirm live links and as-of dates at fixture-build.*

---

## Real sources

### S1 — Groundfloor Finance Inc. (Reg A LRO offering circular) → Case 3a (hard money, sound)

- **URL:** SEC EDGAR CIK 1588504 — Form 1-A POS (Reg A Tier 2), e.g.
  <https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1588504&type=1-A>
  (FY2022 POS: `tm2224874d1_partiiandiii.htm`; FY2023 POS series).
- **As of:** FY2022–FY2023 qualified circulars. *Confirm the latest POS-qualified
  LRO circular at fixture-build.*
- **Deal type:** Hard money / bridge debt — Limited Recourse Obligations (LROs),
  each note tied to an individual fix-and-flip / bridge real-estate loan.
- **Facts extracted:** Reg A Tier 2 structure; $75M annual aggregate LRO cap;
  per-loan LRO with disclosed loan grade; hold-to-maturity, no early redemption
  (illiquid); non-accredited investor concentration limit (10% of greater of income
  or net worth); risk factors include borrower default and limited recourse.
- **Why case 3a (sound):** a real debt platform that *discloses* loan grading,
  LTV basis, and historical loss data — the half of the contrast where HML flags
  (`HML-01` ARV-vs-as-is, `HML-03/04` default/recovery) are *answered*, so the
  skill should clear it. Verifies the skill doesn't manufacture HML flags on a
  disclosed, sound debt deal.

### S2 — Fundrise eREIT (Reg A offering circulars) → Case 1 (full equity memo) / Case 10 (clean equity)

- **URL:** SEC EDGAR + <https://fundrise.com/oc>. Examples: Income eREIT V (CIK
  1776860, `tm2128279d1_253g2.htm`), Growth eREIT II (CIK 1661000), Development
  eREIT (CIK 1768726), original Income eREIT (CIK 1645583).
- **As of:** 253G2 circulars 2021–2022. **Note:** a sub-eREIT consolidation merger
  is effective 2026-04-29 (sub-eREITs roll into a single consolidated Fundrise
  eREIT) — fixture should reflect the post-consolidation structure or note the
  vintage.
- **Deal type:** Equity real estate (non-traded REIT, Reg A).
- **Facts extracted:** Reg A exemption (not a 1940-Act investment company);
  asset-management + advisory fee structure (~1%/yr range, full schedule in the
  circular); quarterly redemption program with limits; diversified portfolio.
- **Why:** a real, complete, *low-fee diversified* disclosure — good for case 1
  (full-memo parsing) and a candidate real "clean equity" anchor for case 10
  (in-range fees, diversified, disclosed redemption terms).

### S3 — Blue Owl Capital Corporation (OBDC) prospectus → Case 11 (clean private credit)

- **URL:** SEC EDGAR CIK 1655888 — Form 424B2, e.g.
  <https://www.sec.gov/Archives/edgar/data/0001655888/000162828025007185/ck0001655888-20250221.htm>
  (2025-02-21) and `…20250513.htm` (2025-05-13); Q3-2025 results 2025-09-30.
- **As of:** 424B2 dated 2025-02-21 / 2025-05-13.
- **Deal type:** Private credit (publicly traded BDC).
- **Facts extracted:** management fee 1.50% of gross assets (1.00% on assets below
  the 200% asset-coverage threshold); two-part incentive fee (pre-incentive net
  investment income component + capital-gains component); leverage up to ~2:1
  (150% asset-coverage election, June 2020); through-cycle financials disclosed.
- **Why case 11 (clean credit):** a large, diversified, *fully-disclosed* credit
  vehicle whose leverage is standard and stated. The test: the skill must treat
  **disclosed, standard** fund leverage as not-a-red-flag — i.e. NOT fire `CREDIT-01`
  on transparent 2:1 leverage — distinguishing it from case 4's hidden/excessive
  leverage. The clean counterpart to case 4.

### S4 — Nightingale / CrowdStreet (Elie Schwartz) → Case 7 (GP red flags, real pattern)

- **URL:** <https://therealdeal.com/national/2023/10/17/crowdstreet-nightingale-settlement-reveals-new-details/>;
  <https://propmodo.com/nightingale-properties-ceo-gets-hefty-sentence-for-his-involvement-in-the-crowdstreet-fraud/>;
  <https://www.bisnow.com/national/news/office/nightingale-ceo-elie-schwartz-makes-first-payment-to-crowdstreet-investors-122434>
- **As of:** raise 2022; misappropriation revealed / settlement Oct 2023;
  sentencing (7+ years) 2025.
- **Deal type:** Single-asset office equity via crowdfunding platform.
- **Facts extracted:** $54M from 654 investors (Atlanta Financial Center) + $8.8M
  from 167 investors (Miami Beach, 1601 Washington); ~$53M misappropriated to other
  ventures and personal use (incl. First Republic stock/options before its
  collapse); CEO sentenced to 7+ years.
- **Why case 7:** the real-world pattern that breaks circularity (`TESTING-PLAN.md`
  §2.2) — single-asset concentration, platform-intermediated raise with no real
  GP capital at risk, control over investor funds without escrow protection. Maps to
  `GEN-02` (misconduct), `GEN-01` (co-invest), `GEN-14` (track record). The synthetic
  packed-flag fixture is *patterned on this*, not authored from nothing.

### S5 — Applesway / Tides 2022–24 multifamily distress → distress overlay (Cases 1, 5, 7)

- **URL:** <https://therealdeal.com/texas/houston/2024/02/21/applesway-facing-more-distress-on-arbor-multifamily-loan/>;
  <https://www.multifamilydive.com/news/Multifamily-distress-foreclosures-Class_C-capital_expenditures/648338/>;
  <https://finance.yahoo.com/news/applesway-investors-delinquent-60m-linked-180708075.html>
- **As of:** foreclosure April 2023; further distress Feb 2024.
- **Deal type:** Value-add multifamily equity syndication on floating-rate debt.
- **Facts extracted:** Applesway defaulted on a ~$229–230M floating-rate Arbor loan
  across 4 Houston complexes (3,200+ units), bought Aug 2021–Apr 2022; Arbor
  foreclosed (2023); 123 investors sued alleging $12.4M fraud. Tides Equities
  avoided foreclosure by securing loan workouts (the contrast outcome).
- **Why:** the canonical floating-rate / rate-cap / frozen-refi failure pattern
  behind `GEN-10` (rate-cap expiry), `GEN-09` (debt maturity inside the plan), and
  `EQUITY-07` (refi-dependent). Used as a *distress overlay* — facts seeded into the
  multifamily (case 1), development (case 5), and red-flag (case 7) fixtures so the
  skill is tested against what actually broke real LP capital (Tier-4 criterion §4.5).

### S6 — 2025–26 office repricing → Case 6 (office, variable class)

- **URL:** <https://www.commercialsearch.com/blog/distress-drives-chicago-office-sales-with-steep-discounts-in-early-2025/>;
  <https://credaily.com/newsletters/national/issue/office-market-hits-reset-in-2025-as-deep-discounts-spark-investor-activity/>
- **As of:** 2025 sales; market data Aug 2025; reset continuing into 2026.
- **Deal type:** Office equity (variable class per `01`/`05`).
- **Facts extracted:** 46% of 2025 office sales closed below prior sale price (vs
  20% in 2021); 70%+ of A-rated assets sold below prior valuation. Examples:
  200 South Wacker Dr (Chicago, 41-story) sold $68M, ~−70% vs $214.5M (2013);
  600 W Chicago Ave $88.7M vs $510M (2018); 101 Merrimac St (Boston) $22.5M vs
  $64M assessment.
- **Why case 6:** real repricing magnitudes for an office fixture. Tests that the
  skill **refuses a category baseline** (`01` office = *variable*), drives off the
  deal's own underwriting (physical occupancy, class, debt maturity), fires `GEN-19`
  / `Q-MKT-02`, and that `benchmark_comparator.py` returns "variable — no comparator."

---

## Synthetic fixtures (validate mechanics, not accuracy — §2.2)

These have no external URL by design; they hold a variable still that no real deal
will. Labeled synthetic so reviewers weight them accordingly.

| Case | Synthetic because | Grounded in |
|---|---|---|
| 2 | Sparse-email *form* is constructed to test thin-input parsing | Real preferred-equity term patterns (`01`/`02`) |
| 3b | Problematic HML constructed as the opposite-facts half of the contrast | `03` HML flags (HML-01/02/03/04/05) |
| 4 | Sector-concentrated credit vehicle constructed (OBDC serves the clean counterpart, S3) | `03` CREDIT-01/02; *find a real sector-focused BDC at fixture-build if available* |
| 5 | Aggressive-projection development deal constructed | `01` dev baseline + S5 distress facts |
| 7 | Packed multi-flag deal constructed | **S4 Nightingale + S5 Applesway** real patterns |
| 8 | Near-empty teaser constructed to test absence-as-output | `01` essential-disclosure baseline |
| 9 | Identical-IRR / different-J-curve *pair* (cannot be real — no two real deals share an IRR to the basis point) | `03` GEN-11; `04` Q-DIST-01 |
| 10 | Synthetic-clean equity fallback if no real clean syndication is sourced (S2 Fundrise preferred) | in-range `02` fees, clawback, market pref |

**Coverage check:** every case has either a real source (S1–S6) or a labeled
synthetic above; the two clean cases (10 real-preferred / 11 real) and the Tier-4
overlays (S4, S5) carry the real-world-accuracy weight, per `TESTING-PLAN.md` §2.2.
