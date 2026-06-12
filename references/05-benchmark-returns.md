# Benchmark Returns (LP perspective)

*LAST_UPDATED: 2026-06-12. All figures trace to `references/data/` snapshots —
this file synthesizes, it does not source. When a snapshot is refreshed, update
the figures here and bump this stamp.*

The forcing function: **every private deal must clear a liquid, net-of-fee public
hurdle plus an illiquidity premium**, or the LP is locking up capital for no
compensated reason. This file gives each private deal type its closest public
comparator, the spread the deal must beat, and the framework for judging whether
that spread pays for the lock-up. It is the antidote to evaluating a deal against
only its own pro forma — the question is never "is 14% good?" but "is 14% net,
illiquid, for 7 years, good *versus* what the LP could hold liquid and free?"

## How to read this file

- **Net-to-LP vs net-to-public.** Every comparator return is a public-market
  total return **after the fund's expense ratio** — apples-to-apples with a
  **net-to-LP** private return. Never compare a comparator to a deal's *gross*
  IRR (the analyst rule from the SKILL output contract).
- **Comparators are risk-matched, not return-matched.** Each private type maps to
  the public instrument with the *closest risk shape* (equity→REITs, debt→high
  yield, preferred→preferreds), then the residual mismatch is named. A raw spread
  over a mismatched comparator misleads.
- **The 10yr trailing is the spine; the 5yr is context.** Trailing windows carry
  their cycle: SPY's 10yr (15.54%) reflects an exceptional equity decade and is
  *not* a forward promise; LQD's ~0% 5yr reflects the 2022 bond drawdown. Read
  the window, don't extrapolate it.
- **Volatility is read against the equity baseline, not as an absolute number.**
  Uniform annualized std-dev across one basis isn't cleanly available from public
  aggregators (fund fact sheets 403; sources mix daily / 1yr / since-inception
  bases). Rather than imply false precision, the Vol column expresses each
  comparator *relative to the SPY broad-equity baseline* (≈ / below / well below),
  plus a drawdown contrast. This makes the baseline load-bearing: the sharp read
  is that REITs sit at ≈ equity volatility with a **deeper** drawdown (−73% vs
  −55%) for **lower** return — less reward, more tail. The relative ordering is
  robust even where the absolute numbers aren't.
- **Levered vs unlevered.** ETF equity comparators are levered-equity-like. The
  NCREIF NPI (unlevered private RE) is carried alongside so the skill can tell
  "clears the illiquidity hurdle" from "the return is leverage, not alpha"
  (grounds `03` → `GEN-07`, the financing-story flag, in a benchmark).
- **A deal beating the spread is necessary, not sufficient.** Clearing the hurdle
  is the floor. Dispersion (see Preqin note) means the *median* fund of a type is
  a coin-flip against its comparator once you weight the bottom quartile.

## Contents

1. [Public comparators at a glance](#public-comparators-at-a-glance)
2. [Per-comparator notes](#per-comparator-notes)
3. [The spread table — private type vs its comparator](#the-spread-table)
4. [Illiquidity-premium framework](#illiquidity-premium-framework)
5. [Unlevered overlay — separating leverage from alpha](#unlevered-overlay)
6. [Provenance](#provenance)

---

## Public comparators at a glance

Source: `references/data/etf-comparators-snapshot.md` (returns as of Q1 2026
quarter-end / latest daily; captured 2026-06-06, VTI + volatility 2026-06-12).
Net of expense ratio. Vol is expressed *relative to the SPY equity baseline* —
see the snapshot for why a uniform absolute std-dev isn't available.

| Ticker | Trailing 10yr | Trailing 5yr | Vol vs SPY | Expense | Best comparator for |
|---|---|---|---|---|---|
| SPY | 15.54% | 14.11% | baseline (~17%, −55% DD) | 0.0945% | Universal equity anchor — the liquid opportunity cost |
| VTI | 14.88% | 12.31% | ≈ SPY | 0.03% | Broad-equity anchor — total-market alternative to SPY |
| VNQ | 6.47% | 5.13% | ≈ SPY vol, deeper tail § | 0.13% | Equity real estate (REITs) — primary RE comparator |
| IYR | ~6.4–6.8% † | ~5.7–6.7% † | ≈ VNQ § | 0.39% | Equity RE cross-check on VNQ |
| LQD | ~3.1% | ~0.1% ‡ | below SPY | 0.14% | Stabilized core / IG-quality debt; senior preferred proxy |
| HYG | 5.0% | 3.8% | below SPY | 0.49% | High yield → hard-money & private-credit proxy |
| PFF | 3.72% | 1.6% | well below SPY | 0.45% | Preferred equity |
| PRIV | n/a ※ | n/a ※ | n/a ※ | 0.70% | Public+private IG credit — most direct, but unseasoned |

† IYR figures diverged across aggregators; ranges carried honestly. VNQ is the
primary REIT comparator, IYR the cross-check. ‡ LQD's ~0% 5yr is the 2022 IG-bond
drawdown sitting in the window (3yr had recovered to ~4%). ※ PRIV launched
2025-02-26 — no trailing return exists; since-inception NAV was 1.81% as of
2025-06-30. Use HYG/LQD for credit hurdles until PRIV seasons. § Vol ≈ the equity
baseline but the **tail is deeper**: VNQ's max drawdown ≈ −73% vs SPY/VTI ≈ −55%
— REITs carry equity-like volatility with a worse drawdown *while trailing the
equity anchor on return*. That asymmetry (less return, more tail) is the sharpest
single read in this table.

**Risk-free anchor (Treasury curve, `fred-10yr-snapshot.md`):** 3mo ≈ **3.71%**,
2yr ≈ **4.15%**, 10yr ≈ **4.5%** (10yr early June 2026; short points 2026-06-11).
The illiquidity premium sits *on top of* the duration-matched point — when the
curve moves, every hurdle below moves with it.

---

## Per-comparator notes

- **SPY (broad equity).** The humbling anchor: over the trailing decade, *every*
  private RE type below trailed SPY's 15.54% except development's *target* (which
  is rarely realized). This does not mean "just buy SPY" — private RE is a
  diversifier with a different risk factor — but a deal pitched as "high return"
  that trails a free, liquid index over 10 years owes the LP an explicit
  diversification or downside-protection rationale. Weight SPY's exceptional
  decade when using it forward.
- **VTI (total market).** The total-market alternative anchor — same role as SPY,
  cheaper (0.03%), and arguably the truer "all my equity dollars" opportunity cost
  since it includes mid- and small-cap. Tracks SPY closely (14.88% vs 15.54% 10yr;
  ≈ same vol and −55% drawdown). Use whichever anchor the LP thinks in — they are
  near-substitutes, not distinct exposures, so the spread table maps to RE/credit
  comparators, not to either equity anchor.
- **VNQ (REITs).** The cleanest liquid proxy for equity real estate, and the
  primary RE comparator. Broad, cheap (0.13%), daily-liquid. Its ~6.5% 10yr is
  the number a private equity-RE deal's *net* return must beat by an illiquidity
  premium. Higher vol than its return suggests — REITs price like equities.
- **IYR (REITs, cross-check).** Same exposure, pricier (0.39%). Use only to
  sanity-check VNQ. The fee gap is itself an LP lesson: identical exposure, more
  drag — the same scrutiny applies to private fee stacks (`02`).
- **LQD (IG corporates).** The liquid analog for stabilized "core" cash-flow risk
  and the senior end of preferred. Its rate sensitivity (near-0% 5yr) is the
  cautionary tale for any deal selling "bond-like stability" — duration is risk.
- **HYG (high yield).** The closest liquid proxy for hard-money / bridge funds and
  private credit. Its 5.0% 10yr is the bar a private credit fund's net yield must
  clear, *plus* premium for illiquidity and single-borrower concentration that
  HYG diversifies away.
- **PFF (preferreds).** The direct comparator for preferred-equity positions. Its
  sober trailing returns (3.72% 10yr) set a low but real bar — and a reminder that
  preferred is a capped-upside, income instrument, so a private pref's coupon is
  the thing to compare, not an equity-like IRR.
- **PRIV (public+private credit).** Conceptually the most direct private-credit
  comparator and the most expensive (0.70%). Too new to benchmark against; note
  also that private-credit vehicles report *smoothed* marks, so their apparent
  low volatility understates true risk — a caveat to carry into any private-credit
  deal claiming "low volatility."

---

## The spread table

For each `01-asset-class-norms.md` type with a stable baseline: its **net-to-LP**
IRR range, the risk-matched comparator's **10yr** trailing return, the approximate
premium, and whether it clears the illiquidity hurdle (≥200bps, scaled up for
multi-year lock-ups — see framework). Premiums are **approximate bands**, not
point estimates.

| Private type (net-to-LP, from `01`) | Comparator (10yr) | Approx. premium | Read |
|---|---|---|---|
| Multifamily value-add (12–15%) | VNQ (6.47%) | ≈550–850bps | Clears comfortably — but verify it's not leverage (see unlevered overlay) |
| Multifamily core/core-plus (8–12%) | VNQ (6.47%) | ≈150–550bps | Low end is *thin* for a 7–10yr lock-up |
| Industrial (7–15%) | VNQ (6.47%) | ≈50–850bps | Stabilized end barely clears; value-add end clears |
| Retail — necessity (8–12%) | VNQ (6.47%) | ≈150–550bps | Low end thin; anchor-credit risk not in the comparator |
| SFR (8–14%) | VNQ (6.47%) | ≈150–750bps | Mid-range adequate; shorter track record than the comparator |
| Development (18–22% *target*) | VNQ (6.47%) | ≈1150–1550bps *target* | Largest *target* premium **and** widest dispersion — discount heavily for realized-below-target |
| Hard money / bridge (8–10% net) | HYG (5.0%) | ≈300–500bps | Clears — premium pays for illiquidity + concentration HYG diversifies |
| Private credit (8–12%) | HYG (5.0%) | ≈300–700bps | Clears; check fund leverage isn't manufacturing the spread (`03` → `CREDIT-01`) |
| Preferred equity (coupon ≥6%; pref <6% is a flag, `03` → `EQUITY-04`) | PFF (3.72%) | ≈230bps+ at a 6% pref | **Thin** — a 6% pref over PFF is ~230bps for capped upside + illiquidity |

***Variable* classes — office, experiential retail, STR, mixed-use — get no row.**
Per `01`, their baseline is the deal's own underwriting, not a category default,
so a forced comparator would be false grounding. Benchmark these against the
deal's *own* stated return vs the closest stable analog, and treat the
category-baseline absence as itself informative.

**How the skill uses this row-by-row:** output "this deal's claimed net IRR of
X% exceeds [comparator]'s Y% by ≈Zbps — for an N-year lock-up, the illiquidity
hurdle is ~Wbps, so the deal [clears / is thin / fails] the bar." The premium is
necessary, not sufficient — pair with dispersion (below).

**Debt deals — also read the spread over the duration-matched Treasury.** For
hard money and private credit, the credit-analyst lens is the deal's net yield
over the *duration-matched* risk-free point (`fred-10yr-snapshot.md`), which is
the **credit + illiquidity spread** the LP is paid:

- Hard money (8–10% net, 6–18mo loans) over the 3mo–2yr bill (3.71–4.15%)
  → ≈ **385–630bps**.
- Private credit (8–12% net, 3–7yr) over the 2yr (4.15%; true 3–7yr floor sits a
  touch higher, between 2yr and 10yr) → ≈ **385–785bps**.

This complements the HYG row rather than duplicating it: HYG already embeds the
high-yield *credit* spread, so the Treasury floor isolates the **absolute** risk
premium — letting the skill say whether a debt deal is paid for credit risk, for
illiquidity on top, or neither.

---

## Illiquidity-premium framework

A liquid comparator can be sold any day at no cost. A private LP position locks
capital for years with no exit (see `04-question-bank.md` → Q-LIQ-01). The LP must
be *paid* for that, on top of the comparator return.

**Rule of thumb:** demand **≥200bps over the closest public comparator** as a
floor, **scaled up by lock-up length**. A rough tiering:

| Lock-up | Minimum premium over comparator (heuristic) |
|---|---|
| ≤1 yr (e.g. some hard-money) | ~200bps |
| 3–5 yr | ~300–400bps |
| 7–10 yr (typical equity syndication / core fund) | ~400–600bps |

This is a **heuristic, not a law** — it scales the price of illiquidity with its
duration; precise calibration is LP judgment (risk tolerance, portfolio liquidity
need, conviction in the GP). Apply it against the *spread table* above: a
multifamily core deal at 8% net (≈150bps over VNQ) for a 9-year lock-up **fails**
the ~400–600bps hurdle even though it "beats REITs" — that is the framework's
sharpest, least-intuitive output.

Two amplifiers that *raise* the premium an LP should demand:
- **Dispersion** (Preqin note, `references/data/preqin-vintage-note.md`): private
  RE strategies show wide top-to-bottom-quartile spreads (core IQR ~8.4pts;
  opportunistic ~13pts). The *median* fund earns far less than the marketed
  top-quartile figure, so the premium must compensate for the real chance of a
  below-median outcome — top-quartile is a narrow door.
- **Concentration**: a single deal carries idiosyncratic risk the diversified
  comparator (an index of hundreds) doesn't. A single-asset syndication vs VNQ's
  basket is not a clean swap.

---

## Unlevered overlay

The design-review requirement (2026-06-01): without an unlevered baseline, the
financing-story flag (`03` → `GEN-07`) is assertion, not measurement.

**NCREIF NPI (unlevered institutional private RE), 2025:** total return **4.9%**,
of which income was **~4.8%** and appreciation **~0.2%**
(`references/data/ncreif-npi-snapshot.md`). Read this as the **unlevered, in-place**
return of institutional real estate: almost entirely income, with appreciation
near zero in 2025.

How to use it: if a multifamily deal projects a 15% *levered* net IRR while the
unlevered private-RE baseline is ~5% (mostly income), then **~10 of those points
are coming from leverage and assumed appreciation, not operations.** That is not
automatically bad — leverage is how RE equity works — but it tells the LP exactly
how much of the return is a *financing bet* (rate path, refi availability, exit
cap) versus an *asset bet* (in-place cash flow). When the spread-table premium is
large but the unlevered baseline is thin, the deal is a leverage story
(`03` → `GEN-07`, `GEN-08`); the verdict should say so.

By property type, 2025 NPI total return was retail 6.8%, residential 5.3%,
industrial 4.5%, office 3.4% — office lagging is consistent with `01`'s *variable*
office baseline.

---

## Provenance

This file is **synthesis only** — every figure is sourced and dated in
`references/data/`:

- ETF comparators (returns, expense ratios, vol caveat) →
  `etf-comparators-snapshot.md`
- 10yr Treasury anchor → `fred-10yr-snapshot.md`
- Unlevered private-RE baseline (NCREIF NPI) → `ncreif-npi-snapshot.md`
- Dispersion / vintage caveat (Preqin) → `preqin-vintage-note.md`
- Private net-to-LP IRR ranges → `01-asset-class-norms.md`

See `references/data/README.md` for the refresh procedure and cadence. When any
snapshot is refreshed, update the corresponding figures here and bump the
`LAST_UPDATED` stamp at the top. The figures age predictably by design — a stale
benchmark silently corrupts every comparison, so the stamp is the trigger for the
v1.1 calibration refresh.
