# Eval fixture 06 — Ground-up development, first-time sponsor
*Iteration-5 run, 2026-09-27, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 7712624.*

**Verdict: Pass as presented — insufficient disclosure.** None of the five essential development disclosures is present, so the return can't be underwritten. The facts that *are* stated already lean Pass on the merits. A first ground-up project, a return that depends entirely on the exit, an exit cap below basis, and no downside case make up the riskiest profile in this category. More disclosure can fix the gaps, but it cannot give this sponsor a development track record.

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Development (ground-up). Product type (multifamily, industrial, etc.) not stated 🟢 |
| Deal type | Development equity. Routed as Equity + Development variations, `GEN-`/`EQUITY-`, VNQ comparator |
| Sponsor | Not stated. **First ground-up project** 🟢 |
| Geography | Not stated |
| Minimum investment | Not stated |
| Hold | 3 years 🟢 (bottom of the `01` 3–5 yr development norm) |
| Raise / total project cost | Not stated |
| Claimed return | 25% IRR / 2.5x. **Gross vs net not stated** 🟢 |
| Scenarios | Single pro forma, no downside case 🟢 |
| Exit cap | Underwritten below the going-in basis 🟢 (exact figures not stated) |
| Fees disclosed | 5% development fee + 4% construction management 🟢 (bases not stated) |

**The headline metrics don't reconcile** 🟢 (arithmetic on the stated figures):
- 2.5x over 3 years works out to at least a **35.7% IRR**, even if every dollar comes back at exit.
- 25% compounding for 3 years produces only **1.95x**.
- Reaching 2.5x at 25% takes about **4.1 years**.

In a development deal, capital drawn later or distributions paid earlier only *raise* the IRR, so no cash-flow pattern inside 3 years reconciles these numbers. Something is off. The hold may really be about 4+ years. The multiple may be gross while the IRR is net. Or the figures come from different model versions. Each explanation changes the screen.

## 2. Return Stress-Test

The key swing assumptions are:
- **Exit cap**, compared with today's market cap for stabilized comparable assets.
- **Construction cost and schedule**: overrun and delay extend the hold, and the fixed multiple then yields a lower IRR.
- **Lease-up / absorption pace**, which drives when the asset stabilizes and can be sold.

| Case | Assumption | LP IRR | vs VNQ (4.92% 10yr) + hurdle |
|---|---|---|---|
| Sponsor (as stated) | 25% taken as if net, 3 yr | 25.0% 🔴 (net basis unconfirmed) | +2008 bps; clears the ~300–400 bps 3-yr hurdle comfortably |
| Gross-read | 25% is gross; assumed 20% promote over 8% pref, 100% catch-up | ≈20.8% 🔴 | +1568 bps (run at 20.6%); clears |
| Delay | 2.5x holds but takes 5 yrs (typical cost/lease-up slip) | ≈20.1% 🔴 | +1518 bps; clears |
| Bear | Delay to 5 yrs **and** exit cap at or above basis, multiple compresses to 1.5x | ≈8.4% 🔴 | +348 bps over VNQ, thin (lower half of the 5-yr hurdle band). Only ≈322 bps over the 5.18% 10yr Treasury |

Reading the table:
- **The 25% headline is above the category's own *target*.** `01` puts the development target net IRR at 18–22% and notes realized returns are "often below target." A first-time developer projecting above the category target, with no downside case, is the wrong way round 🟢.
- `05` instructs discounting the development *target* premium heavily. The spread over VNQ is mostly marketing until construction risk is priced in.
- The bear case is where a first-time sponsor's development deal lives. It still "clears" VNQ, but only thinly. A cost overrun that requires a capital call, or a forced sale into a soft market, pushes it into a loss of capital. That tail is not in any row above because no budget or debt terms were disclosed.

## 3. Where LP Returns Come From

- **Essentially 100% from the exit/sale** 🟡 (inferred from deal type plus the 3-year hold). A ground-up project spends most of 3 years in construction and lease-up with no in-place cash flow, so there is at most a few months of stabilized income before sale. This is far past the 60% exit-dependence threshold → **`GEN-08` (RED)**.
- **Exit cap below basis → `EQUITY-06`.** One development-specific point matters here. If "going-in basis" means **yield-on-cost**, then selling at a cap below yield-on-cost is the development spread, which is the actual thesis and not compression. The test then becomes whether the exit cap sits below *today's market cap* for comparable stabilized product. If it does, cap-rate compression is baked into the headline. Which comparison the sponsor used is undisclosed, so treat the flag as RED until answered.
- **Leverage share: can't tell** 🔴. No debt terms were disclosed. The `05` unlevered overlay shows NCREIF NPI at 5.00% (trailing 4Q), almost entirely income. This deal's 25% has no income component during the hold, so all of it rests on the development spread, leverage, and the exit. With `GEN-08` and `EQUITY-06` both firing, a **financing story (`GEN-07`)** is likely, but it can't be confirmed without the construction loan and takeout terms. It is a must-ask, not a fired flag.

## 4. Fee Stack Summary

| Fee | Stated | `02` norm | Read |
|---|---|---|---|
| Development fee | 5% (base not stated) | 3–5% of total project cost, one-time | Top of range 🟢 |
| Construction management | 4% (base not stated) | 3–5% of hard costs | In range on its own 🟢 |
| **Combined** | Dev fee **and** CM fee | `02`: aggressive is ">6% **or split across both a development fee *and* construction management fee**" | **Named aggressive pattern** 🟢 |
| Acquisition / land fee | Not stated | 1–2% of equity (applies to Development) | Absent: rolled in or undisclosed |
| Asset management | Not stated | 1–2% of equity, annual | Absent |
| Disposition | Not stated | 0.5–1% of sale price | Absent |
| Loan placement | Not stated | 0.5–1.5% of loan | Absent (construction loan presumed) |
| Pref / promote / catch-up | Not stated | 15–30% over 6–10% pref | **Absent: the waterfall is the core economic** |
| Construction contingency | Not stated | 5–10% of hard costs | Absent (aggressive if <5% or >15%) |

**Gross-to-net drag: not computable from this disclosure.**
- Running `fee_drag_calculator.py` with every disclosed equity-basis fee returns **0 bps**, because the dev and CM fees are on project-cost and hard-cost bases the calculator can't take, and everything else is undisclosed. That 0 bps is a disclosure artifact, not a clean fee stack.
- Converting the dev and CM fees to an LP-equity basis needs the loan-to-cost and hard-cost share, and neither is stated.
- Illustration only 🔴: at an assumed 35% equity and 65% hard-cost share of project cost, the two fees equal about **22% of LP equity** (≈14.3% + ≈7.4%). Over a 3-year hold that is roughly **700 bps/yr** of drag under `02`'s one-time ÷ hold framework, before any promote.
- An assumed standard 20/8/100% catch-up promote adds **≈420 bps/yr** at 25% gross.
- These fees are usually capitalized into the budget, so it matters whether the 25% is stated before or after them. That is a must-ask.

## 5. Red Flags

**RED**
- **`GEN-14`: No realized development track record.** This is the sponsor's first ground-up project 🟢. `01` says development experience "is not fungible with acquisition experience," and the essential disclosure is the GP's last three development exits with budget vs actual. There are none to give. Any prior acquisition record (`GEN-05` risk if quoted at project level) does not validate this deal. LP exposure: construction-cost and schedule execution by an untested team.
- **`GEN-08`: Exit-dependent IRR.** About 100% of the return comes from the sale 🟡. LP exposure: the whole return is one transaction, priced at a date 3+ years out.
- **`EQUITY-06`: Exit cap below going-in basis** 🟢 (development-spread nuance in §3). LP exposure: if it is below today's market cap, cap compression is baked into the headline.
- *Cluster:* `GEN-08` + `EQUITY-06` together point to a **likely financing story (`GEN-07`)**. Leverage is unconfirmed, so this needs the debt terms before it can be stated as fact.

**YELLOW–RED**
- **`GEN-06`: Stacked GP development fees.** A 5% dev fee plus a 4% CM fee is the `02`-named aggressive split 🟢. Whether the CM goes to a GP affiliate is not stated 🟡. LP exposure: the GP is paid about 9 points of cost basis whether or not the project succeeds, and more if the budget grows.
- **`GEN-16`: No waterfall disclosure.** Pref, promote, catch-up and the remaining fee lines are absent 🟢. Net-to-LP is unknowable, and the 25% can't even be placed as gross or net. (`EQUITY-04`/`EQUITY-05` can't be assessed.)
- **`GEN-15`: Missing financials.** No hard-cost budget, contingency, or debt terms 🟢.

**YELLOW**
- **`GEN-13`: Single-point pro forma, no downside** 🟢. This is sharper here because development is the category `01` flags as realizing "often below target on cycle misses."
- **`GEN-17`: Essential development disclosures absent.** Entitlement/permit status, budget with contingency %, debt/takeout structure, absorption comps, and GP development exits are all missing 🟢 (§6).
- **`GEN-11`: IRR with no distribution schedule** 🟢. Development is J-curve by construction, with zero distributions until sale. The IRR/multiple mismatch (§1) suggests the timing assumptions are not what the 3-year hold implies.

**Not fired (probes only, facts not stated):** `GEN-01` (co-invest), `GEN-02` (regulatory), `GEN-09`/`GEN-10`/`EQUITY-07` (construction-loan maturity, rate cap, takeout), `GEN-18` (absorption / rent growth).

## 6. Missing Disclosures

Measured against `01` → Development essential disclosures and `02` → Equity / Development variations:

1. Entitlement and permit status: entitled vs permitted vs shovel-ready.
2. Hard-cost budget with **contingency %** (`02`: 5–10% typical).
3. Debt structure: construction loan amount/LTC, rate (fixed/floating, any cap), maturity and extensions, construction-to-perm vs separate takeout.
4. Market absorption / lease-up assumptions with comp evidence.
5. GP's last three development exits with realized timing and budget vs underwritten. **Not possible here: first project.**
6. Whether the 25% / 2.5x is gross or net to LP, and why the two don't reconcile over 3 years.
7. Full waterfall: pref rate, cumulative/compounding, promote, catch-up.
8. Bases of the dev and CM fees; any acquisition, asset-management, disposition, loan-placement, or admin fees.
9. Product type, geography, total capitalization, raise size, minimum.
10. GP co-investment amount and terms.
11. Capital-call provisions for cost overruns (development-specific LP exposure).
12. Distribution schedule and projected stabilization date.
13. What the exit cap is compared against (yield-on-cost vs current market cap) and the actual figures.

## 7. GP Alignment

- **Co-invest:** not stated. Unverified.
- **Track record:** **none in this strategy.** This is a first ground-up project, so there are no realized development exits and no net-to-LP development record. Any acquisition-side record is not a substitute (`01`). Unverified.
- **Waterfall alignment:** unknowable because no pref, promote, or catch-up was disclosed.
- **Fee alignment:** poor on what *is* disclosed. The dev and CM fees are paid on cost, early and certain, so they pay the GP for *spending* rather than for LP outcomes. A larger budget means larger fees. If the CM entity is GP-affiliated, the GP is also grading its own construction oversight (`GEN-06`).

## 8. Questions for the GP

**Must-ask**

| ID | Question | Bad-answer signal | Flag |
|---|---|---|---|
| Q-GP-02 | Restate your track record as net-to-LP IRR on fully realized, exited deals, and specifically any development or construction exposure. | Offers acquisition or project-level IRR as a stand-in for development experience; "our team has built before at other firms" with no attributable realized record. | GEN-14, GEN-05 |
| Q-DS-01 | What share of LP IRR comes from the sale vs in-place cash flow, and what's the IRR at a flat exit cap? | Can't decompose; "development always creates value"; the IRR drops below the pref at a flat cap. | GEN-08, EQUITY-06 |
| Q-EXIT-01 | Why is the exit cap below the going-in basis? Is "basis" yield-on-cost or the current market cap for stabilized comps? What's the IRR at exit cap = current market cap? | "Cap rates will compress"; won't state the current market cap; no sensitivity. | EQUITY-06 |
| Q-DS-03 | What's the return under a bear case: 12+ month delay, cost overrun, exit cap at or above today's market? | "We underwrite conservatively" with nothing to show; the bear case is still a gain. | GEN-13 |
| Q-DS-02 | Strip out leverage and cap compression: what is the unlevered return on cost? | Treats the levered IRR as the only figure; "leverage is how development works." | GEN-07 |
| Q-FEE-01 | Provide the complete fee schedule (with bases) and the full waterfall. Is the 25% / 2.5x gross or net, and why don't they reconcile over 3 years? | "Standard market fees"; "the PPM has it" without producing it; can't explain the IRR/multiple gap. | GEN-16 |
| Q-FEE-02 | Is the construction manager GP-affiliated? Why charge both a dev fee and a CM fee, and are they benchmarked? | "All arm's-length" without naming the entity; no benchmark; both fees defended as "industry standard." | GEN-06 |
| Q-FEE-04 | What pref do LPs receive before promote, and is it cumulative and compounding? | Pref <6% or none; non-cumulative. | EQUITY-04, EQUITY-05 |
| Q-RISK-03 | Provide the hard-cost budget with contingency, and complete construction-loan terms. | Budget withheld until commitment; contingency <5%; debt terms "still being negotiated." | GEN-15 |
| Q-RISK-01 | When does the construction loan mature relative to stabilization and sale, and what are the extension/takeout terms? | Maturity falls inside the lease-up; "we'll refinance" with no terms. | GEN-09 |
| Q-RISK-02 | Is the construction loan floating? When does any rate cap expire, and what does it cost to extend? | Cap expires before maturity; extension cost not modeled. | GEN-10 |
| Q-EXIT-02 | Does capital return depend on a takeout or refinance, and what happens if it isn't available? | "The refi market will reopen"; no fallback. | EQUITY-07 |
| Q-DIST-01 | What's the distribution schedule, and when does LP capital start returning? | IRR quoted with no timing; "at sale." | GEN-11 |
| Q-MKT-01 | What submarket supply pipeline and absorption comps support the lease-up and exit rents? | Metro-level optimism; no supply pipeline acknowledged. | GEN-18 |
| Q-GP-01 | How much of your own cash is in this deal, pari-passu with LPs? | "Our dev fee is our skin in the game"; a deferred fee counted as co-invest. | GEN-01 |
| Q-GP-03 | Any regulatory action, enforcement, or investor litigation? | "Nothing material"; a search surfaces something undisclosed. | GEN-02 |
| Q-LIQ-01 | What are my options if I need to exit before the hold ends? | "A secondary market may develop." | — |

**Nice-to-ask**

| ID | Question | Bad-answer signal | Flag |
|---|---|---|---|
| Q-DIST-02 | What are the capital-call mechanics if construction runs over budget, and what's the penalty for a missed call? *(Close to must-ask for development: overrun calls are the typical first-time-developer failure.)* | "Calls as needed"; punitive dilution buried in the docs. | — |
| Q-FEE-03 | Single asset, but confirm the waterfall mechanics and any clawback. | Can't explain the catch-up. | EQUITY-01, EQUITY-02 |
| Q-LIQ-02 | K-1 delivery timing? | History of extensions. | — |

## 9. Diligence Checklist

- **PPM / operating agreement:** fee bases, waterfall, capital-call and dilution provisions, GP removal rights.
- **Background checks** on principals: SEC/FINRA/state, litigation, prior-deal outcomes (`GEN-02`).
- **Construction verification:** third-party cost review of the budget and contingency, GC contract type (GMP vs cost-plus), completion guarantee and **who backs it** (a first-time sponsor's guarantee strength is itself a diligence item).
- **Entitlement documents:** zoning approvals and permits in hand vs pending.
- **Lender term sheet:** construction loan and takeout commitment, recourse and guarantor.
- **Market:** independent absorption and rent comps; current cap rates for stabilized comparable product (to test `EQUITY-06`).
- **Model:** the full cash-flow model, to reconcile the 25% / 2.5x / 3-year mismatch.

## 10. Verdict

**Pass as presented — insufficient disclosure.**

- **Why "as presented":** none of `01`'s five essential development disclosures (entitlement, budget/contingency, debt/takeout, absorption, GP development exits) was provided. Gross vs net is unstated, the waterfall is absent, and the headline IRR and multiple contradict each other over the stated hold. The core return story can't be underwritten.
- **Why it leans Pass on the merits anyway:** three things are stated, not inferred:
  - a **first-time** ground-up sponsor (`GEN-14`),
  - an exit cap below basis (`EQUITY-06`) on a return that is ~100% exit-driven (`GEN-08`),
  - no downside case (`GEN-13`), with a 25% headline above the category's own 18–22% target.

  Stacked dev and CM fees (`GEN-06`) pay the GP on cost regardless of outcome. Only the track record gap is permanent. Everything else is a disclosure the sponsor could cure.
- **Biggest swing factor:** construction execution by an untested team. Cost overrun and delay extend the hold, trigger capital calls, and push the exit into whatever market exists at completion.
- **Re-screen if the sponsor provides:**
  - items 1–4 and 6–8 of §6,
  - an exit cap at or above today's market cap for stabilized comps that still clears the pref,
  - a bear case in which LP capital survives,
  - an experienced development partner or a GC with a GMP contract and a credit-worthy completion guarantee,
  - a single fee (or a CM fee credited against the dev fee).
- **Who it could suit, if cured:** an LP sizing it as a small, speculative allocation who is explicitly underwriting the *team* and can meet capital calls. It does not suit an LP who needs the 25% to happen or needs liquidity inside 5 years.
