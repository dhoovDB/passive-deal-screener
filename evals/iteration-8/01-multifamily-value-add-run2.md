# Eval fixture 01
*Iteration-8 run, 2026-11-01, blind generation by fresh-context agent (model: Opus), against SKILL.md @ ef2a4f5 plus the one-line GEN-09 edit.*

**Verdict: Pursue with conditions.** This is a financing story, and it is worth one more round of questions but no capital yet: the return needs a 5.0% exit cap, which is below both the 5.5% going-in cap and today's 5.18% 10yr Treasury.

*Screening output only, not investment advice.*

Confidence tags: 🟢 stated or from a reference. 🟡 inferred from stated facts. 🔴 assumed or unverifiable.

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Multifamily, value-add 🟢 |
| Deal type | Equity syndication 🟢 (the bridge loan is the deal's financing, not the LP's position, so debt-fund flags don't apply) |
| Sponsor | Not stated |
| Geography | "Sun Belt," no metro or submarket named |
| Size | $50M equity raise, 280 units 🟢, which is about $179k of equity per unit 🟡 |
| Minimum investment | Not stated |
| Hold | 5 years 🟢 (low end of the `01` 5–7 yr norm) |
| Claimed return | 16% IRR / 2.0x equity multiple. **Gross or net to LP: not stated** |
| Waterfall | 8% pref, 20% promote, American (deal-by-deal) 🟢 |
| Caps | 5.5% going-in, 5.0% exit 🟢 |
| Debt | Bridge, floating rate 🟢. Amount, spread, maturity, extensions and rate cap: not stated |
| Fees | 2% acquisition, 1.5% annual asset management, 1% disposition 🟢. Base for each: not stated |
| Track record | "30% IRR across prior deals" 🔴 unverified |

## 2. Return Stress-Test

The leverage is undisclosed, so these cases are a sizing exercise and the verdict does not rest on them. 🔴 Assumptions: debt at 50–70% of total capitalization, interest-only, no sale costs. The starting point is the only distribution pattern the stated numbers imply (see §3): about 5.35% a year, with $86.6M of LP cash at sale. Net figures come from `fee_drag_calculator.py`, reading 16% as gross and using a 100% catch-up.

| Case | Exit cap | NOI vs plan | Annual distributions | Gross IRR / multiple | Net-to-LP IRR | Premium over VNQ (4.92%), against a 300–400 bps hurdle |
|---|---|---|---|---|---|---|
| **Bull** (the sponsor's plan) | 5.0% | On plan | 5.35% | 16.0% / 2.0x | **11.4%** | +644 bps, clears comfortably |
| **Base** (no compression) | 5.5% | On plan | 5.35% | 11.2–12.8% / 1.63–1.75x | **7.2–8.6%** | +225 to +370 bps, fails to thin |
| **Bear** | 6.0% | −10% | Halved | −3.4% to +3.6% / 0.85–1.18x | **−5.5% to +1.5%** | Trails VNQ outright |

The swing assumptions:
- **Exit cap (largest).** Moving only from 5.0% to 5.5%, with NOI fully on plan, takes 316–484 bps off the gross IRR. That one move can take the deal from clearing the lock-up to failing it. In the bear case, LP capital is impaired before fees at 65–70% leverage (0.97x and 0.85x).
- **Rent growth.** "Raise rents" is the plan, but no rent-growth figure or submarket data was given (`GEN-18`, probed).
- **Floating-rate cost.** On $50–117M of debt 🔴, each +100 bps costs $0.5–1.2M a year, or 19–44% of the implied $2.67M annual distribution. A refinance may also matter, but none is disclosed (`EQUITY-07`, probed).

**Does it clear the lock-up?** Only if the exit cap assumption holds.
- **Gross or net matters by about 460 bps.** If 16% is gross, the LP's net on full plan is 11.4% (12.3% with no catch-up). That sits below the 12–15% realized band in `01`, and well below the 14–18% target range. If 16% is already net (+1,108 bps over VNQ), the deal needs roughly 21% at the deal level, and the Base case would net about 11–13% and clear. The sponsor has to say which, in writing.
- **Treasury floor.** `05` calls this the tighter floor right now. Base net is only about 200–345 bps over the 5.18% 10yr Treasury, for an illiquid, single-asset, floating-rate position.
- **Equity anchor.** Every case trails SPY's 15.39% trailing 10yr, so the deal owes a diversification or downside rationale. It hasn't given one.
- **Clearing is necessary, not sufficient.** Dispersion and single-deal concentration (`05`) raise the premium an LP should demand.

## 3. Where LP Returns Come From

**Exit-driven: at least 60% of the profit, most likely about 73%. Flag fires (`GEN-08`).** 🟡

A 2.0x on $50M means $50M of profit. Here is how the stated numbers split it:

| Source | Amount | Share of profit | Basis |
|---|---|---|---|
| Interim cash flow | $13.4M | 27% | 🟡 16% and 2.0x reconcile at about 5.35% a year. A sale-only 2.0x would be 14.9%, so the extra IRR implies this much interim cash |
| Exit gain | $36.6M | 73% | 🟡 About 82% of the present value of all LP cash arrives at sale |
| of which 50 bps of cap compression | $12.4–18.5M | 25–37% | 🔴 A flat cap cuts the sale price 9.1%. The dollar figure depends on leverage |
| of which NOI growth (the renovation story) | $18–24M | 36–48% | 🔴 The remainder after compression |

This finding doesn't depend on guessing the distribution schedule. `01` puts stabilized cash-on-cash at 5–8%. Even paying 8% every year from day one, through the renovation period, totals $20M, which still leaves 60% of the profit to the exit. Getting below 60% requires cash yields above the `01` range or refinance proceeds, and refi proceeds are leverage rather than cash flow.

**Leverage and compression: the financing-story flag fires (`GEN-07`).** 🟡
- **Unlevered overlay.** NCREIF NPI is 5.00% trailing (residential 5.3% in 2025), almost all income. That leaves about 11 of the 16 points to come from leverage, assumed appreciation and whatever the renovations add.
- **The exit cap is below the risk-free rate.** A 5.0% exit means the year-5 buyer accepts an initial yield under today's 5.18% 10yr Treasury. The 5.5% going-in cap is only 32 bps above it. 🟢
- **Leverage may not add cash yield on day one.** The break-even is a spread of 126 bps over the 3-month rate (4.24%, used as a proxy, since the index isn't stated). Above that, the debt costs more than the 5.5% in-place yield, so leverage pays off only through NOI growth and the sale. 🟡 The actual spread is a must-ask.
- **The operating story is real but is not carrying the deal alone.** Renovating and raising rents is a legitimate plan. The sponsor just hasn't shown that it clears the hurdle without compression.

Distributions also matter for income: about 5.35% a year is below the 8% pref, so about $1.33M a year would accrue unpaid (about $6.7M over the hold) 🟡. The pref is largely paid at sale, not along the way, which makes its cumulative and compounding terms matter (`EQUITY-05`, probed).

## 4. Fee Stack Summary

**Gross-to-net drag: 464 bps a year** (16.0% gross to 11.36% net; `fee_drag_calculator.py`). Undisclosed fees were passed as 0. The catch-up is undisclosed, and the 100% used here is the ASSUMED input (§6); with no catch-up, drag is 369 bps and net is 12.31%.

| Fee | Stated | `02` norm | Read | Drag (bps/yr) |
|---|---|---|---|---|
| Acquisition | 2%, base unstated | 1–2% of equity, or 0.5–1.5% of price | Top of range on equity. On price, it's above typical and at the >2% aggressive line | 40 |
| Asset management | 1.5% annual, base unstated | 1–2% of equity | In range; $750k a year, $3.75M over the hold if on equity | 150 |
| Disposition | 1%, base unstated | 0.5–1% of sale price | Top of range. Check for double-charging with brokerage | 20 |
| Promote | 20% over 8% | 15–30% over 6–10% | In range; catch-up and tiers undisclosed | 254 |
| **Total** | | | | **464** |

Each headline term is in range, so the problem is what's missing and how the bases are defined:
- **Fee base (🔴).** The 464 bps treats each one-time fee as a percent of equity. If acquisition is on purchase price and disposition on sale price (illustrated at 65% leverage: about $2.6M and $1.8M), drag rises to 580 bps and the bull-case net falls to 10.2%.
- **Fees not disclosed.** Loan placement, refinance, construction management, admin/IR and any affiliate property management. At `02` norms, placement and admin alone would add about 20–120 bps a year 🔴, so a fully loaded high-end stack is about 700 bps.
- **Model limits.** The drag is additive and uses a single payout at exit. It slightly overstates drag, which is the conservative direction for a screen.

## 5. Red Flags

**RED**
- **`EQUITY-06` Exit cap below going-in** 🟢. 5.0% against 5.5% bakes in a 10% price gain at constant NOI, and the LP absorbs the shortfall if it doesn't arrive.
- **`GEN-08` Exit-dependent return** 🟡. At least 60% and likely about 73% of profit arrives at sale, so the LP is holding a single-date bet on the year-5 market.
- **`GEN-07` Financing story** 🟡. About 11 of 16 points sit above the unlevered baseline, compression is explicit, and the debt may not be accretive on day one. The return breaks if rates stay high or credit tightens.
- **`GEN-05` GP-IRR vs LP-IRR divergence** 🟡. "30% IRR" carries no net-to-LP or project-level label, so the LP can't tell what it measures and treats it as unverified.
- **`GEN-14` No realized exits cited** 🟡. Nothing separates exited deals from marks.
- **`GEN-15` Missing financials** 🟢 (YELLOW–RED, treated as RED until answered). No rent roll, T-12 or complete debt terms, so the renovation and rent thesis can't be tested.

**YELLOW**
- **`EQUITY-01` Deal-by-deal waterfall** 🟢. Yellow rather than red because a 20% promote isn't high. If this is one asset 🟡, there's no later deal to lose on, so the classic risk is muted. What remains is promote paid on interim cash or refi proceeds before capital comes back.
- **`EQUITY-02` Clawback not disclosed** 🟡. **Becomes RED if the documents confirm there is none.** `02` treats this absence as a major flag in a deal-by-deal structure.
- **`GEN-11` No distribution schedule** 🟢. The IRR comes with no timing, and the ~5.35% in §3 is implied by the numbers, not disclosed.
- **`GEN-13` No sensitivity or downside case** 🟢. A single-point pro forma hides the fragility §2 shows.
- **`GEN-16` Partial fee and waterfall disclosure** 🟢. Headline terms allow a drag estimate, but catch-up, tiers, pref type, fee bases and several fee categories are absent.
- **`GEN-17` Essential disclosures absent** 🟢. See §6.

**Clusters**
- `GEN-07` + `GEN-08` + `EQUITY-06` is the financing story, viewed from three angles.
- `GEN-05` + `GEN-14` means no validated LP track record at all, which `03` treats as a RED cluster.

**Probed, not fired (the facts aren't disclosed, so each goes to a must-ask in §8)**
- `GEN-09`: the hold is stated but the loan maturity isn't. Bridge debt's usual term isn't this loan's maturity. Via `Q-RISK-01`.
- `GEN-10`: the debt floats and no cap terms were given. If a cap expires before the sale, debt service can spike and erase distributions just as the exit or refi needs a healthy NOI. Via `Q-RISK-02`.
- `EQUITY-07`: refi dependency, via `Q-EXIT-02`.
- `GEN-18`: rent growth in an unnamed submarket, via `Q-MKT-01`.
- `GEN-01` (co-invest, `Q-GP-01`), `GEN-02` (regulatory history, `Q-GP-03`), `GEN-06` (affiliate fees, `Q-FEE-02`), `GEN-12` (T-12 vs shorter windows, `Q-RISK-03`), `EQUITY-03` (catch-up rate, `Q-FEE-03`), `EQUITY-05` (pref type, `Q-FEE-04`), `GEN-04` (team scale, `Q-GP-04`).

**Checked and clean:** `EQUITY-04` doesn't fire because the 8% pref is above the 6% threshold. The promote, asset management fee and acquisition fee (on equity) are within `02` norms.

## 6. Missing Disclosures

Against the `01` value-add baseline:
- Rent roll and T-12 actuals
- Exit cap sensitivity (the 5.0% is given, the sensitivity isn't)
- Debt structure: amount and LTV, index and spread, maturity, extensions, rate cap strike and expiry, amortization
- Refinance assumptions
- GP record on **prior multifamily exits**
- Rent-growth assumption, and submarket supply and absorption

Against `02`:
- Whether 16% / 2.0x is net to LP
- Base for each fee
- Catch-up rate and split tiers (**ASSUMED at 100% in §4**)
- Pref: cumulative or not, simple or compounding
- Clawback
- Loan placement, refinance, construction management and admin/IR fees, plus affiliate arrangements

Also absent: sponsor identity, minimum investment, distribution schedule, sources and uses, and LP liquidity terms.

One number to reconcile in sources and uses: $179k of equity per unit implies about $357–595k per unit of total capitalization at 50–70% leverage 🔴. The references carry no per-unit norm, so this is a check against sale comps (§9), not a flag. It suggests modest leverage, a very large renovation budget, a high basis, or some mix of these.

## 7. GP Alignment

- **Co-invest:** not stated. Cash amount and pari-passu terms are unknown 🔴. Not fired as `GEN-01`, because silence isn't proof of zero.
- **Track record:** **unverified.** "30% IRR" has no realized-only or net-to-LP basis 🔴, and it's about twice the 12–15% realized band in `01`. It also sits oddly beside this deal's 16%. If 30% were a realized net result, the sponsor should be able to explain why this plan projects about half of it. The likeliest explanations are gross or project-level IRR, unrealized marks, or a few short holds 🟡. Until restated, it counts as no track record.
- **Waterfall alignment:** 8% over 20% is a market structure. The American label matters less on a single asset 🟡, but catch-up, clawback and promote timing are all unknown.
- **Who gets paid when it goes wrong:** about $5.25M of fees (on the equity base) is owed on all but the worst outcomes, including the bear case, against about $10–11M of promote on plan 🟡. Roughly a third of the GP's plan economics doesn't depend on LP results.
- **Affiliate fees:** not stated. Property management and construction management are the usual places to look.

## 8. Questions for the GP

**Must-ask**

| ID | Ask | Bad-answer signal |
|---|---|---|
| `Q-FEE-01` | Is 16% / 2.0x net to LP? Provide the complete fee schedule, bases and full waterfall | "Standard market fees"; "the PPM has it" without producing it |
| `Q-EXIT-01` | Why is the exit cap below going-in, and what's the IRR at 5.5% and above? | "Cap rates will compress"; the IRR breaks at flat; no sensitivity offered |
| `Q-DS-01` | What share of LP IRR comes from cash flow versus exit, and what's the IRR at a flat exit cap? | Won't decompose it; "real estate always appreciates"; falls below pref at flat |
| `Q-DS-02` | Strip out leverage and compression: what's the unlevered, in-place return? | No unlevered view exists; "leverage is just how the deal works" |
| `Q-DS-03` | What's the return with flat rents, a higher exit cap and no refinance? | "We underwrite conservatively" with nothing to show; the bear case is still a gain |
| `Q-RISK-01` | When does the debt mature relative to year 5, and what's the extension or refi plan? | Maturity inside the hold; "we'll refinance" with no terms |
| `Q-RISK-02` | When does the rate cap expire relative to maturity, and what does extending it cost now? | Cap expires first; cost not modeled; "rates should be lower by then" |
| `Q-EXIT-02` | Does the plan depend on a refinance, and what happens to distributions if it isn't available? | Capital return needs a refi at lower rates; "the refi market will reopen" |
| `Q-GP-02` | Restate the 30% as net-to-LP IRR on fully realized, exited deals only | Project-level or GP-level IRR only; "most deals are still performing" |
| `Q-GP-01` | How much of your own cash is in this deal, on LP terms? | "Sweat equity"; a fee waiver instead of cash; a token amount on better terms |
| `Q-GP-03` | Any regulatory action, enforcement or investor litigation? | "Nothing material"; a search turns up something undisclosed |
| `Q-FEE-03` | Deal-by-deal or whole-of-fund (one asset or several?), is there a clawback, and can promote be paid before capital returns? | Can't explain the catch-up; "you get paid when we get paid" |
| `Q-FEE-04` | Is the 8% pref cumulative and compounding? | Non-cumulative; vague on whether unpaid pref carries forward |
| `Q-FEE-02` | Which providers are GP-affiliated, what do they charge, and is that benchmarked? | "All arm's-length" with no names; no benchmark |
| `Q-RISK-03` | Provide T-12, rent roll and complete debt terms | T-3 or T-6 only; "confidential until you commit" |
| `Q-DIST-01` | What's the distribution schedule, and when does LP capital start returning? | "When the deal supports it"; IRR with no timing |
| `Q-MKT-01` | What submarket supply and absorption data support the rent growth? | Metro or Sun Belt optimism in place of submarket data; "rents always go up here" |
| `Q-LIQ-01` | What are my options if I need out before year 5? | "A secondary market may develop." An honest "none" is a good answer |

**Nice-to-ask**

| ID | Ask | Bad-answer signal |
|---|---|---|
| `Q-DIST-02` | When could capital calls come, and what happens on a missed call? (Worth pressing given floating debt) | "Calls as needed"; punitive dilution buried in the documents |
| `Q-GP-04` | How has the team grown alongside AUM? | "Lean and efficient" as the whole answer; no named asset manager |
| `Q-LIQ-02` | When are K-1s delivered, and have they met deadlines? | "As soon as we can"; a history of extensions |

## 9. Diligence Checklist

Third-party verification still needed:
- **PPM and operating agreement:** waterfall, catch-up, pref type, clawback, promote timing, fee bases, capital-call terms. Have your own counsel read them, plus a tax adviser if useful.
- **Background and regulatory:** SEC, FINRA and state records, litigation search on the sponsor and principals. Form ADV if applicable.
- **Track record:** deal-by-deal realized results tied to investor statements or K-1s, including any losers.
- **Lender:** term sheet or loan agreement, rate cap confirmation (strike, expiry, counterparty), extension tests, covenants.
- **Financials:** T-12 and rent roll, independently tied out. Sources and uses.
- **Market:** third-party appraisal, sale comps for cap rate and price per unit, submarket rent comps, supply pipeline.

## 10. Verdict

**Pursue with conditions.**

*Screening output only, not investment advice.*

**Name it what it is: a financing story.** The headline terms are fine: 8% over 20%, with in-range fees. The problem is what the 16% rests on. At least 60% of the profit arrives at sale, the sale assumes a cap rate 50 bps tighter than purchase and below today's Treasury, and the debt floats with no disclosed cap or maturity. The track record that's meant to give comfort is unverified.

It stays alive because enough is disclosed to frame the story, the structure itself is market, and the deciding answers cost the sponsor one email. Those answers should be in hand before any commitment.

**Biggest swing factor: the exit cap.** Next comes whether 16% is gross or net, worth about 460 bps. Illustratively, removing compression takes net to about 7–9% against a hurdle of about 8–9%. 🔴

**Conditions.** Failing 1, 2, 3 or 4 is a Pass:
1. **Net at a flat cap.** The sponsor documents net-to-LP IRR at an exit cap of 5.5% or higher, and it reaches about 9% or better (VNQ or the 10yr Treasury plus the 300–400 bps hurdle).
2. **Downside.** LP capital comes back in a case with flat rents, an exit cap above going-in and no refinance.
3. **Debt.** The rate cap runs through maturity or has a budgeted extension, and maturity plus extensions reach the planned exit or there's a refi-independent path.
4. **Track record.** Realized, net-to-LP results on prior multifamily exits, verifiable and including losers.
5. **Alignment.** Meaningful cash co-invest on LP terms, a cumulative pref, a disclosed catch-up, and no promote before capital return or else a secured clawback.
6. **Documents.** T-12, rent roll, sources and uses, the full fee schedule and affiliate arrangements, with nothing that moves the conclusions above.

**Who it suits:** an LP who wants a leveraged, rate-sensitive bet on Sun Belt multifamily and can sit through a 5+ year lock-up in a single asset. It doesn't suit someone who needs current income (the implied distributions run below the pref) or who needs capital back on a schedule.

**What would have to be true:** rents rise as planned in a submarket no one has named yet, rates and credit cooperate through a floating-rate hold, and in year 5 a buyer pays a tighter cap than this sponsor did. If the first holds without the other two, and the numbers still clear, this becomes an asset story worth a real look.
