# Eval fixture 11 — J-curve pair, Deal B (back-loaded) + the A/B contrast

*Iteration-1 run, 2026-07-03, against SKILL.md @ cddc52d. Fixture prompt: evals.json id 11 (pair with id 10). Compare-two-deals mode: Deal B screen + the pair contrast.*

---

**Deal B read: the same 14% headline as Deal A, with none of the same risk.** 100% of the return arrives at a single event — the Year-5 sale — so the IRR is an exit-cap bet held for five years with no interim de-risking. **Comparison verdict: the deals are not equivalent, and Deal A is the superior risk-adjusted structure at identical IRR.**

## 1. Deal Snapshot
- **Asset class:** Multifamily (segment not stated) 🟡
- **Deal type:** Equity (structure not stated) 🟡
- **Claimed return:** 14% IRR 🟢 — identical headline to Deal A
- **Distributions:** **None until the Year-5 sale; entire return at exit** 🟢
- **Sponsor / Geography / Minimum / Raise / Fees:** Not stated 🔴

## 2. Return Stress-Test
Baseline and benchmark identical to Deal A on paper (14% in the `01` value-add band; ≈750bps over VNQ if net). But the stress-test is where the twins diverge: **Deal B's entire 14% rides the exit assumption** — one variable, one date. Stress the exit cap 50–100bps or slip the sale a year and the whole return moves; there is no realized-cash floor beneath it. Deal A stressed the same way loses only its residual.

Swing assumptions: (1) **the Year-5 exit cap — effectively the whole deal**; (2) sale timing (a 1-year slip on a back-loaded 14% costs ~200bps of IRR mechanically); (3) whatever supports value creation in the interim (undisclosed).

## 3. Where LP Returns Come From
**100% exit — `GEN-08` fires at maximum: the >60% threshold is met at 100%.** This is a terminal-value bet structured as an equity hold. Nothing wrong with that *as a category* — development deals look this way natively (see fixture 06) — but for stabilized-style multifamily it means the LP holds illiquid, non-distributing exposure for five years with the entire outcome decided by one market print. If the exit also assumes cap compression, the financing-story cluster completes (`GEN-07`/`EQUITY-06` — exit-cap assumption undisclosed; asked below).

## 4. Fee Stack Summary
**Not computable — no fees disclosed** (`GEN-16`). Note the waterfall interaction cuts *worse* here than for Deal A: with all cash at exit, promote mechanics concentrate at the same single event as the LP's return — the gross-to-net gap is decided all at once, at the GP's exit of choice.

## 5. Red Flags
**RED**
- `GEN-08` — Exit-dependent IRR at 100% of return: the definition of the flag, disclosed plainly.

**YELLOW / YELLOW–RED**
- `GEN-11` (mechanism) — timing is disclosed (so the *nondisclosure* flag doesn't fire), but the disclosed timing is the maximally back-loaded J-curve: five years of zero distributions concentrates all risk at exit — the exact "identical IRRs, very different risk timing" case the flag exists to catch.
- `GEN-16` (YELLOW–RED) — no fee/waterfall disclosure; promote-at-exit interaction above.
- `GEN-15`/`GEN-17` (YELLOW) — no financials or category essentials; no interim value-creation plan stated.
- Exit-cap assumption undisclosed — if below going-in, `EQUITY-06` joins (asked below).

## 6. Missing Disclosures
Everything Deal A is missing (sponsor, fees, financials, market, structure), plus the items Deal B's shape makes critical: the exit-cap assumption, the value-creation plan that justifies five distribution-free years, and any interim liquidity mechanics.

## 7. GP Alignment
Not assessable — and the back-loaded shape raises the stakes: for five years the GP collects fees (undisclosed) while the LP receives nothing, and the GP chooses the exit moment that crystallizes both the LP return and the promote. Alignment mechanics (pref, clawback, co-invest) matter *more* here than for Deal A; all undisclosed.

## 8. Questions for the GP
1. **Q-DS-01** — "What exit cap produces the 14%, and what's the IRR at going-in cap, and with a 1-year sale slip?" *Bad answer:* IRR collapses at a flat cap; "the market will be there." (`GEN-08`/`EQUITY-06`)
2. **Q-DIST-01** — "Why zero distributions for five years on multifamily — where does interim cash flow go?" *Bad answer:* can't say where operating cash goes; it funds fees. (`GEN-11`)
3. **Q-FEE-01** — full fee schedule and waterfall — especially promote mechanics at the single exit event. (`GEN-16`)
4. **Q-DS-03** — bear case: exit at going-in cap, Year-6/7 sale. *Bad answer:* none exists. (`GEN-13`)
5. **Q-LIQ-01** — "Five years, no distributions: what if I need out in Year 2?" *Bad answer:* "a secondary market may develop."
6. **Q-GP-01/02** — co-invest; realized net-to-LP record.

## 9. Diligence Checklist
- [ ] Exit-cap sensitivity table (or build one: IRR at going-in, +50, +100bps)
- [ ] PPM: waterfall, promote crystallization, fee schedule
- [ ] Interim cash-flow plan: where does the property's operating income go?
- [ ] Sponsor background and realized record

## 10. Verdict — Deal B standalone, then the pair
**Deal B standalone: Pursue with conditions, weaker than A** — the shape is legitimate for a heavy-reposition thesis, but that thesis is undisclosed, and at 100% exit-dependence the conditions are load-bearing: exit-cap sensitivity that survives a flat cap, a disclosed value-creation plan, and waterfall mechanics that don't concentrate against the LP at the single payout event.

**The comparison (the actual question asked):** identical 14% IRRs, **materially different deals** —

| | Deal A | Deal B |
|---|---|---|
| Return source | ~7pts income + progressive capital return | 100% terminal value (`GEN-08`) |
| At-risk capital over time | Declining from Year 1 | Full principal, all 5 years |
| Exit-assumption weight | Residual | Total |
| Downside if Year-5 market is bad | Reduced base, realized cash retained | Entire return and principal exposed |
| J-curve | None | Maximal |

**Preference: Deal A, and it is not close.** IRR is indifferent to *when* risk resolves; an LP is not. Deal B must offer something A doesn't — a lower price, a higher pref, a demonstrably superior asset plan — to justify holding 100% of the outcome hostage to a single future sale. On the disclosed facts it offers the same 14% with strictly worse risk timing. Same-IRR-therefore-same-deal is exactly the equivalence the screen exists to reject.
