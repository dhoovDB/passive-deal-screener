# Eval fixture 10 — J-curve pair, Deal A (front-loaded distributions)
*Iteration-5 run, 2026-09-27, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 7712624.*

# Deal A — Screen (compare mode: part 1 of 2)

**Verdict: Pass as presented — insufficient disclosure.** Deal A discloses one thing a lot of deals leave out, which is the shape of its distributions. It is front-loaded: 7% cash-on-cash paid quarterly from Year 1, with capital coming back over the hold. Almost everything else needed to underwrite the 14% is missing: whether it's net or gross, sponsor, hold, fees, waterfall, debt and financials. **Biggest swing factor:** where the 7% Year-1 yield and the progressive capital return come from. Operating cash flow is one possibility. A refinance, or a payout from reserves or raised equity, are the others. If a plain 7% yield is the only interim cash, the deal is borderline exit-dependent despite the front-loaded label (§3). The re-screen list is at the end of §10. I'll hold the head-to-head until Deal B arrives, and the comparison frame is at the bottom.

---

## 1. Deal Snapshot

| Field | Deal A | Tag |
|---|---|---|
| Asset class | Multifamily. Sub-type not stated: a 14% target fits the value-add band (12–18% target, `01`) and sits above core / core-plus (8–12%) | 🟢 class / 🟡 sub-type |
| Deal type | Equity syndication, inferred from "multifamily" + IRR + cash-on-cash framing | 🟡 |
| Sponsor | Not stated | — |
| Geography | Not stated | — |
| Minimum | Not stated | — |
| Hold | Not stated (value-add norm 5–7 yrs, `01`) | — |
| Raise / equity | Not stated | — |
| Claimed return | 14% projected IRR, **net or gross not stated** | 🟢 figure / 🔴 basis |
| Distributions | 7% cash-on-cash, quarterly, from Year 1. Capital "returns progressively over the hold" (mechanism not stated) | 🟢 |

## 2. Return Stress-Test

**Benchmark (`scripts/benchmark_comparator.py`, VNQ 4.92% 10yr):**

| Case | Net-to-LP IRR used | Premium over VNQ | Illiquidity hurdle | Result |
|---|---|---|---|---|
| 14% is already **net** (5-yr hold) | 14.00% | 908 bps | ~300–400 bps | Clears comfortably |
| 14% is already **net** (7-yr hold) | 14.00% | 908 bps | ~400–600 bps | Clears comfortably |
| 14% is **gross**, typical stack (see §4) | 9.71% | 479 bps | ~400–600 bps | Clears (thin), lower half of the hurdle band |

- 🟡 **The net/gross ambiguity decides the result.** As net, the 14% clears comfortably. As gross with a category-typical fee stack, it lands near 9.7%: a thin clear over VNQ, and only ≈450 bps over the 10yr Treasury (5.18%, `05`), which is currently the tighter floor. Don't compare it to anything until the GP states the net figure (skepticism rule 2).
- **Swing assumptions:** none are disclosed. For multifamily, `01` names three that drive the result:
  1. **Exit cap rate.** The single biggest swing in most pro formas.
  2. **Rent growth.** Needs submarket supply and absorption behind it (`GEN-18` can't be assessed yet).
  3. **Refinance.** Matters most here, because "capital returns progressively" may mean a refi return of capital (§3).
- **Base / bull / bear:** 🔴 can't be built from this disclosure. A single-point 14% with no downside case is `GEN-13`.
  - **Base:** the GP's 14%, basis unknown.
  - **Bull:** plausible only if the 7% is fully covered by operations and the exit holds cap.
  - **Bear:** the 7% is partly return of capital or refi-funded, the refi market is shut (the 2022–24 pattern, `03`), and distributions are cut. The IRR then falls back onto the exit.
- **Dispersion caveat (`05`):** clearing the spread is necessary, not sufficient. Realized multifamily value-add has clustered at 12–15% net blended, below the marketing range (`01`).

## 3. Where LP Returns Come From

The front-loaded shape is real and worth something. It reduces the share of the return that rests on the exit compared with a back-loaded deal at the same IRR. But a 7% yield alone does not get a 14% IRR clear of exit dependence.

**Stylized decomposition** (annual approximation of quarterly pay; 7% paid on original capital with no interim return of capital; everything else arrives at exit; 🟡 illustrative, not the deal's model):

| Hold | Exit balloon needed for 14% IRR | Equity multiple | Exit share of PV | Exit share of profit |
|---|---|---|---|---|
| 5 yrs | 1.46x | 1.81x | ~76% | ~57% |
| 7 yrs | 1.75x | 2.24x | ~70% | ~61% |

- On that stylized shape, Deal A sits right at the `GEN-08` 60% line. By profit share it is 57–61%, and by present value 70–76%. **So the "progressive capital return" is carrying much of the load.** Whether Deal A is an income deal or an exit deal depends on how large that return of capital is, when it arrives, and where it comes from. `GEN-08` is **not fired**, because the mechanism is a 🔴 unknown. It is the first must-ask (`Q-DS-01`).
- **Unlevered overlay (`05`).** The NCREIF NPI unlevered institutional return is ~5.00% trailing (almost all income, ≈4.8% income in 2025; residential 5.3% total in 2025). That implies roughly 9 of Deal A's 14 points come from leverage and assumed appreciation, not operations (🟡). Deal A also pays a 7% levered cash yield from Year 1. Against ~4.8% unlevered income and a 5.18% 10yr Treasury, that yield needs one of three things:
  - positive leverage at today's debt costs;
  - an above-market going-in yield;
  - distributions funded by something other than operating cash flow.

  For a value-add asset, `01` puts cash-on-cash at 5–8% **after stabilization**, and 7% in Year 1 means before stabilization. `GEN-07` (financing story) is **not fired**, because leverage and debt terms are undisclosed (🔴). It routes to `Q-DS-02`.
- **Specific failure mode:** if the Year-1 7% is partly funded from raised equity or reserves, the early distributions are the LP's own capital coming back and labeled as yield. The front-loaded profile then flatters the IRR while real exposure stays at the exit. Only a sources-and-uses and a distribution-coverage schedule settle this (`Q-DIST-01`, `Q-RISK-03`).

## 4. Fee Stack Summary

**Gross-to-net drag: not computable from disclosure. That gap is itself the finding** (`GEN-16`).

| Run (`scripts/fee_drag_calculator.py`, 14% gross, 7-yr hold) | Net LP IRR | Total drag |
|---|---|---|
| As disclosed: every fee and the promote passed as `0` | 14.00% | 0 bps (a floor, not an estimate) |
| Category-typical stack, 🔴 ASSUMED: 2% acquisition, 1.5% AM, 1% disposition, 0.3% admin, 20% promote over 8% pref, 100% catch-up | 9.71% | **~429 bps/yr** (recurring 180, one-time 43, promote 206) |

- The ~429 bps figure is **only** a range marker. Every input is assumed (script exit 1, `ASSUMED` warning), and each one is a §6 gap.
- Stacked-fee layers to confirm:
  - Loan placement fee, charged if the deal is levered.
  - **Refinance fee:** if capital is returned by refi, a 0.5–1% of new loan fee typically applies per event (`02`).
  - Affiliate property management (`GEN-06`, can't be assessed).
  - Any feeder or platform wrapper, 50–150 bps/yr (`02`).

## 5. Red Flags

**YELLOW–RED**
- **`GEN-16` No fee or waterfall disclosure.** There is no fee schedule, pref, promote or waterfall structure, so the LP can't know the drag. The 14% could land anywhere from ~9.7% to 14% net. Routes to `Q-FEE-01`.
- **`GEN-15` Missing financials.** There is no rent roll, T-12 or debt terms, so the 7% Year-1 yield can't be tied to operating cash flow. Routes to `Q-RISK-03`.

**YELLOW**
- **`GEN-13` No sensitivity or downside case.** A single-point 14% hides how fragile the return is to exit cap, rent growth and the refi. Routes to `Q-DS-03`.
- **`GEN-17` Essential multifamily disclosures absent.** The missing items are exit cap with sensitivity, refi assumptions, debt maturity and the GP's prior multifamily exits (`01`). Routes to `Q-RISK-01` / `Q-EXIT-01` / `Q-GP-02`.

**Not fired, open until answered** (🔴 inputs; per the anti-patterns these are must-asks, not flags):
- `GEN-08` / `GEN-07` / `EQUITY-06`, the financing-story family. §3 puts a stylized 7% yield right at the 60% threshold. Routes to `Q-DS-01`, `Q-DS-02`, `Q-EXIT-01`.
- `EQUITY-07` refi-dependent plan. "Capital returns progressively" is the classic refi-return-of-capital wording. Routes to `Q-EXIT-02`.
- `GEN-09` / `GEN-10`: debt maturity and rate-cap expiry are unknown. Routes to `Q-RISK-01`, `Q-RISK-02`.
- `GEN-01`, `GEN-05`, `GEN-14`: sponsor not identified, so co-invest and track record can't be assessed. Routes to `Q-GP-01`, `Q-GP-02`.
- `EQUITY-01` / `02` / `03` / `04` / `05`: the waterfall terms are unknown. Routes to `Q-FEE-03`, `Q-FEE-04`.

**`GEN-11` (J-curve not disclosed) does NOT fire.** Deal A states its distribution start and cadence, and that disclosure is its strongest feature. The open point is *how the capital comes back*, not *when distributions start*.

**Cluster watch:** the pattern to watch is a front-loaded yield above the unlevered baseline, plus capital return via refi, plus no debt terms. That is the `GEN-07` + `EQUITY-07` + `GEN-09`/`GEN-10` shape behind many 2022–24 capital calls. It's unconfirmed here, and nothing is fired until the debt terms are known.

## 6. Missing Disclosures

Against the `01` multifamily value-add baseline and the `02` equity-syndication fee inventory:

1. **Net vs gross basis of the 14% IRR.**
2. **Full fee schedule:** acquisition, asset management, disposition, loan placement, refinance, admin/IR.
3. **Waterfall:** pref rate, cumulative or not, catch-up, promote tiers, deal-by-deal vs whole-of-fund, clawback.
4. **Rent roll and T-12 actuals.**
5. **Debt structure:** amount/LTV, fixed or floating, rate cap and its expiry, maturity.
6. **How capital "returns progressively":** refi, partial sale, excess cash flow, or return of capital.
7. **Distribution coverage:** is the Year-1 7% paid from operating cash flow?
8. **Pro forma exit cap vs going-in cap, with sensitivity.**
9. **Hold period.**
10. **Sponsor identity, co-invest, and realized track record on prior multifamily exits.**
11. **Geography / submarket and the supply pipeline.**
12. **Minimum and raise size.**
13. **LP liquidity / early-exit options.**

## 7. GP Alignment

**Unverified on every axis. The sponsor is not identified.**
- **Co-invest:** not stated, so there's no evidence of cash at risk on pari-passu terms (`GEN-01` can't be assessed).
- **Track record:** none cited. Treat it as no track record until restated as **realized, net-to-LP** results on prior multifamily exits (`GEN-05`, `GEN-14`).
- **Waterfall alignment:** unknown. A front-loaded distribution profile does pay the pref early, which is LP-favorable in timing. But with a 100% catch-up, the GP still reaches its full promote share (`02`).
- **Affiliate fees:** unknown (`GEN-06`).

## 8. Questions for the GP

**Must-ask**

| # | Question (`04` ID) | Bad-answer signal | `03` |
|---|---|---|---|
| 1 | `Q-DIST-01` — "What is the projected distribution schedule, and at what milestones does LP capital start returning?" Ask for it split into return *on* vs return *of* capital, by quarter. | "We'll distribute when the deal supports it"; no split between yield and returned capital. | GEN-11 |
| 2 | `Q-DS-01` — "What share of projected LP IRR comes from in-place cash flow versus the exit, and what's the IRR at a flat exit cap?" | Can't decompose the IRR; the IRR drops below the pref at a flat exit cap. | GEN-08, EQUITY-06 |
| 3 | `Q-EXIT-02` — "Does the business plan depend on a refinance, and what happens to distributions if the refi isn't available on the assumed terms?" | The progressive capital return *is* the refi; no fallback; "the refi market will reopen." | EQUITY-07 |
| 4 | `Q-FEE-01` — "Can you provide the complete fee schedule and the full distribution waterfall?" Also confirm the 14% is **net to LP**. | "Standard market fees"; "the PPM has it" without producing it; a gross figure presented as the headline. | GEN-16 |
| 5 | `Q-RISK-03` — "Can you provide trailing-twelve-month actuals, the rent roll, and complete debt terms?" | T-3/T-6 only; "confidential until you commit." | GEN-12, GEN-15 |
| 6 | `Q-DS-02` — "Strip out leverage and cap-rate compression — what is the unlevered, in-place return?" | No unlevered view exists; "leverage is just how the deal works." | GEN-07 |
| 7 | `Q-DS-03` — "What is the return under a bear case — flat rents, higher exit cap, no refinance?" | "We underwrite conservatively" with nothing to show. | GEN-13 |
| 8 | `Q-RISK-01` — "When does the debt mature relative to the projected hold, and what's the refinance or extension plan?" | Maturity inside the hold; "we'll refinance" with no terms. | GEN-09 |
| 9 | `Q-RISK-02` — "When does the rate cap expire relative to debt maturity, and what's the cost to extend it?" (if floating) | The cap expires before maturity; extension cost not modeled. | GEN-10 |
| 10 | `Q-EXIT-01` — "What's the exit cap vs going-in, and the IRR at an exit cap equal to or above going-in?" | Exit below going-in with "cap rates will compress." | EQUITY-06 |
| 11 | `Q-FEE-03` + `Q-FEE-04` — "Deal-by-deal or whole-of-fund, with clawback? What pref, cumulative and compounding?" | Can't explain the catch-up; pref below 6% or non-cumulative. | EQUITY-01, -02, -04, -05 |
| 12 | `Q-GP-01` — "How much of your own capital is in this deal, on the same terms as LPs?" | "Our sweat equity is our investment"; co-invest is a fee waiver. | GEN-01 |
| 13 | `Q-GP-02` — "Restate your track record as net-to-LP IRR on fully-realized, exited deals only." | Project-level IRR only; "most deals are still performing." | GEN-05, GEN-14 |
| 14 | `Q-GP-03` — "Any regulatory action, enforcement, or investor litigation?" | "Nothing material"; a search surfaces something undisclosed. | GEN-02 |
| 15 | `Q-FEE-02` — "Which service providers are GP-affiliated, what do they charge, and are those rates benchmarked?" | "All arm's-length" without naming providers. | GEN-06 |
| 16 | `Q-MKT-01` — "What submarket supply pipeline and absorption data support the rent-growth assumption?" | Metro-level optimism; no supply pipeline acknowledged. | GEN-18 |
| 17 | `Q-LIQ-01` — "What are my options if I need to exit before the hold ends?" | "A secondary market may develop." | — |

**Nice-to-ask:**
- `Q-DIST-02`, capital-call schedule and missed-call consequences. Relevant if a failed refi forces a call.
- `Q-GP-04`, team scale vs AUM.
- `Q-LIQ-02`, K-1 timing.

## 9. Diligence Checklist

- **PPM / operating agreement.** Verify the fee schedule, waterfall, and distribution and return-of-capital mechanics against the marketing claim.
- **Sources-and-uses.** Check for a distribution reserve funded from raised equity; that is how an uncovered Year-1 yield is paid.
- **Background and regulatory search** on the sponsor and principals (SEC / FINRA / state actions, litigation).
- **Rent roll, T-12, and rent and sale comps** for the submarket, to test the rent-growth and exit cap assumptions.
- **Lender term sheet:** rate, fixed or floating, cap expiry, maturity, extension options, prepayment. If capital is to be returned by refi, check the assumed refi proceeds against current debt pricing.
- **Third-party appraisal** or broker opinion of value at the going-in price.
- **Sponsor references from LPs in prior exited deals.** Did stated distributions actually get paid from cash flow?

## 10. Verdict

**Pass as presented — insufficient disclosure.**

- **Reasoning.** The core return story can't be underwritten, because four essential disclosures for multifamily are absent (`01`):
  - the IRR's net/gross basis;
  - the fee stack and waterfall;
  - debt terms;
  - financials.

  The distribution shape is disclosed, and it is a genuine positive. A front-loaded profile shortens the capital's time at risk and lowers the share of the return that rests on the exit. But the §3 math shows a 7% yield alone leaves a 14% IRR at the 60% exit-dependence line. The deal's claim to be an income deal therefore rests on the "progressive capital return," and that mechanism is undisclosed. If it's a refi, the income story becomes a refi-market bet (`EQUITY-07`, `GEN-09`/`GEN-10`).
- **Who it could suit (if it re-screens well):** an income-oriented LP who values early cash and a shorter effective duration. They would accept a lower equity multiple than a back-loaded deal at the same IRR (≈2.24x vs ≈2.50x over 7 yrs, stylized).
- **What would have to be true for a merits verdict:**
  1. The 14% is net to LP, or a net figure is provided and still clears the 7-yr hurdle (~400–600 bps over VNQ).
  2. The Year-1 7% is covered by operating cash flow.
  3. Returned capital comes from operations or planned sales, not a refi that has to happen on assumed terms. Or, if it is a refi, the debt maturity and cap expiry sit safely outside it.
  4. Market-range fees, a pref of 6% or more that is cumulative, and cash co-invest.
  5. A realized net-to-LP track record on prior multifamily exits.

**Re-screen list:** net/gross basis; fee schedule + waterfall; debt terms (maturity, rate, cap expiry); T-12 + rent roll; distribution schedule split into yield vs returned capital; how capital is returned; exit cap vs going-in with sensitivity; hold; sponsor + co-invest + realized track record.

---

## Comparison frame, ready for Deal B

When Deal B arrives, I'll screen it the same way, then contrast on:

1. **Distribution timing (J-curve).** Equal headline IRRs are not equal. A back-loaded deal at 14% over 7 years needs ≈2.50x all at exit (100% exit-dependent). Deal A's stylized front-loaded shape needs ≈2.24x, with 57–61% of profit from the exit. Deal A returns cash sooner. Deal B, if back-loaded, pays more total dollars but concentrates all the risk at one sale date.
2. **Source of the early cash.** A front-loaded deal only beats a back-loaded one if the early cash is earned, not refinanced or returned from the raise.
3. **Net-to-net.** Both IRRs are restated net to LP before they're compared. Never gross-to-gross.
4. **Leverage and debt timing.** Which deal's return depends more on the refi or exit market (`GEN-07` / `EQUITY-07` / `GEN-09`).
5. **Disclosure quality.** If Deal B is also thin, the comparison can still be made on timing shape, but both verdicts stay "as presented."
