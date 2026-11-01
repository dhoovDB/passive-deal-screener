# Eval fixture 01
*Iteration-8 run, 2026-11-01, blind generation by fresh-context agent (model: Opus), against SKILL.md @ ef2a4f5 plus the one-line GEN-09 edit.*

**Verdict: Pursue with conditions. Commit nothing yet: this is a financing story as underwritten, and it earns further diligence only if it survives a flat exit cap on a net-to-LP basis.**

*Screening output only, not investment advice.*

Confidence tags: 🟢 stated or from a reference, 🟡 inferred, 🔴 assumed or unverifiable.

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Multifamily, value-add 🟢 |
| Deal type | Equity syndication 🟢 (the bridge loan is the deal's senior debt, not the investment, so `HML-` flags don't apply) |
| Sponsor | Not stated |
| Geography | Sun Belt; metro and submarket not stated |
| Size | 280 units; $50M equity raise, or about $178,600 of equity per door 🟢 |
| Purchase price, total capitalization, LTV | Not stated |
| Minimum investment | Not stated |
| Hold | 5 years 🟢 (bottom of the 5–7 year norm) |
| Claimed return | 16% IRR / 2.0x. Gross or net not stated |
| Pref / promote | 8% / 20%, American (deal-by-deal) 🟢 |
| Caps | Going-in 5.5%, underwritten exit 5.0% 🟢 |
| Debt | Bridge, floating 🟢. Amount, spread, maturity, extensions, rate cap not stated |
| Fees | 2% acquisition, 1.5% annual asset management, 1% disposition 🟢. Bases not stated |
| Track record | "30% IRR across prior deals" 🟢 as a claim, 🔴 as a fact |

---

## 2. Return Stress-Test

**Facts that need no assumption**

- 🟢 Moving the cap from 5.5% to 5.0% adds 10% to asset value on identical NOI, before a single rent is raised. A flat exit removes 9.1% of the underwritten sale price, and a 6.0% exit removes 16.7%.
- 🟢 The 5.0% exit cap sits 18 bps **below** the 10yr Treasury (5.18%, as of 2026-09-24). The 5.5% going-in cap is only 32 bps above it. The sponsor is underwriting a sale at a yield below the risk-free rate.
- 🟡 16% and 2.0x are consistent with each other. A 2.0x paid entirely at exit is 14.87%, so the 16% implies some interim distributions. On level distributions that works out to about 5.3% a year and about 1.73x at exit, at the low end of the 5–8% stabilized cash-on-cash norm in `01`.
- 🟡 A flat exit cap costs at least 0.16x even with zero debt. Any leverage makes it worse.

**Scenarios.** The 16% is unlabeled, so it is treated as gross until the GP says otherwise. The sponsor's case is the bull case here because it already assumes compression and a fully delivered rent plan.

🔴 **The table is illustrative.** Leverage is undisclosed, so these rows assume 65% LTV on total capitalization with interest-only debt, level distributions and no sale costs. Ranges show 50–75% LTV. Treat this as sizing for the questions in §8. No flag or verdict below depends on it.

| Case | Swing assumptions | Gross IRR | Gross multiple | Net-to-LP IRR | Premium over VNQ (4.92%) | Against ~300–400 bps hurdle (5yr) |
|---|---|---|---|---|---|---|
| **Bull** (sponsor) | Exit 5.0%, rent plan hit | 16.0% | 2.00x | **11.36%** | +644 bps | Clears comfortably |
| **Base** | Exit 5.5% (flat), rent plan hit | 11.8% (10.3–12.8%) | 1.67x (1.57–1.75x) | **7.72%** (6.43–8.58%) | +280 bps (+151 to +366) | Thin / fails; only the 50% LTV end clears, and thinly |
| **Exit +50 bps** | Exit 6.0%, rent plan hit | 7.7% (4.3–9.9%) | 1.40x (1.21–1.54x) | **4.86%** (2.20–6.09%) | −6 bps (−272 to +117) | Fails; trails REITs at the midpoint |
| **Bear** | Exit 6.0%, exit NOI 10% under plan, interim distributions halved by debt cost or a failed refi | −0.7% (+3.6% to −7.9%) | 0.97x (1.18–0.68x) | **−2.80%** (+1.50% to −10.00%) | −772 bps | Fails; capital impaired at 65% LTV and above |

**Clears the lock-up?**

- **On the sponsor's numbers, yes:** 11.36% net exceeds VNQ's 4.92% by about 644 bps against a ~300–400 bps hurdle for a 5-year lock-up, and it is about 618 bps over the 10yr Treasury, currently the tighter floor.
- **But that 11.36% is below** the 12–15% that `01` reports as the realized value-add range, even with every assumption hitting. 🟡
- **At a flat exit cap the premium mostly disappears.** The base case is about 254 bps over the Treasury. The deal only pays for the lock-up if cap rates compress.
- **If the 16% is already net,** it clears easily, but delivering it takes roughly 21.3% gross through this fee stack (script, same inputs). That would be a much bigger claim and should be supported as one. 🟡
- **Clearing is necessary, not sufficient.** This is a single asset against VNQ's diversified basket, and `05` says concentration and dispersion should raise the premium demanded, so read the hurdle at its top end. The 11.36% also trails SPY's 15.39% trailing decade, an exceptional window that shouldn't be extrapolated, but the deal still owes a diversification or downside rationale.

---

## 3. Where LP Returns Come From

| Source | What can be said | Tag |
|---|---|---|
| **Exit** | Under any non-negative distribution timing that produces 16% / 2.0x over 5 years, year-5 cash is **65–89% of present value** at 16%. On level distributions, about 73% of the profit arrives at sale. Exit's profit share falls under 60% only with heavily late-weighted interim cash; the theoretical low of 37% takes a single 0.63x payment in year 4, which is a capital event, not operating cash flow. | 🟡 |
| **Cap-rate compression** | Worth at least 16% of the total 1.0x profit at zero debt, and 25–43% at 50–75% LTV. | 🟡 / 🔴 at the levered end |
| **Leverage** | Bridge and floating are stated; the amount is not. NCREIF NPI's unlevered return is 5.00% (residential 5.3% in 2025), almost all income. **About 11 of the 16 points come from leverage, assumed appreciation and the renovation lift combined.** | 🟢 overlay, 🟡 read |
| **Debt carry** | Going-in yield is 5.5% against a 3-month bill of 4.24%, a rough proxy for the floating base. If the all-in spread exceeds about 126 bps, the debt costs more than the asset yields on day one, and the rent plan has to outrun that before leverage helps. Spread not disclosed. | 🟡 |
| **Operations** | Renovating interiors and raising rents is a real operating lever, but no NOI, rent premium or budget was given, so its share **can't be told from this**. | 🔴 |

**Flag result:** over 60% from exit on a present-value basis under any timing (`GEN-08`), resting on a stated below-going-in exit cap (`EQUITY-06`), with a large unexplained gap over the unlevered baseline (`GEN-07`). All three fire together, so **this is a financing story** until the GP's unlevered, flat-cap number shows otherwise. The renovation plan may carry real weight, and that is exactly what Q-DS-02 and Q-DS-01 should make the GP demonstrate.

---

## 4. Fee Stack Summary

**Gross-to-net drag: about 464 bps/yr 🟡 (16.00% gross to 11.36% net).** This assumes a 100% catch-up 🔴, a simple pref and all bases on equity, with undisclosed fees passed as 0. Treat it as a floor on fees rather than a point estimate.

| Layer | Stated | `02` norm | Read | Drag (bps/yr) |
|---|---|---|---|---|
| Acquisition | 2%, base not stated | 1–2% of equity, or 0.5–1.5% of price | In range on equity; above the typical range and at the aggressive threshold if on price | 40 |
| Asset management | 1.5% annual, base not stated | 1–2% of equity | In range | 150 |
| Disposition | 1%, base not stated | 0.5–1% of **sale price** | Top of range; verify no double-charge with brokerage | 20 |
| Promote | 20% over 8%; catch-up not stated | 15–30% over 6–10% | In range | 254 at 100% catch-up; 206 at 50%; 159 with none |
| Loan placement, refinance, construction management, admin/IR, affiliate property management | **Not stated** | Commonly present; bridge debt and renovation make placement and construction management especially likely | Passed as 0; unknown, not zero | 0 shown |
| **Total** | | | | **464** (369 with no catch-up) |

**The headline fees are market. The disclosure is the problem.**

- **The fee base can move drag by more than the catch-up can.** The script treats every percentage as a share of equity, but `02` puts disposition on sale price, and acquisition may be on purchase price. At an illustrative 65% LTV 🔴, one-time fees rise from 60 to 186 bps/yr, total drag to 590 bps, and net to 10.10%.
- **Fixed fees are paid regardless of outcome.** Even on the smallest base they total about $5.25M, or 10.5% of equity 🟡: $1.0M acquisition, $3.75M asset management over 5 years, and at least $0.5M disposition. In the bear case the GP still collects that while the LP loses principal.

---

## 5. Red Flags

**RED**

- `EQUITY-06` **Exit cap below going-in** 🟢. 5.0% against 5.5%, unproven compression worth 10% of asset value and sitting below the 10yr Treasury. Exposure: at least 0.16x of the multiple on a flat exit, more with leverage. → Q-EXIT-01
- `GEN-08` **Exit-dependent IRR** 🟡. 65–89% of present value arrives in year 5 under any timing. Exposure: the return is a bet on one sale date and one market. → Q-DS-01
- `GEN-07` **Financing story** 🟡. About 11 points over the 5.00% unlevered baseline, with compression and floating bridge debt stated and no unlevered number offered. Moves down if the operating return stands on its own. → Q-DS-02
- `GEN-05` + `GEN-14` **Track record is unverified** 🟡. "30% IRR" has no net-to-LP label and no realized exits cited. It is at least double the 12–15% realized value-add range and nearly double the sponsor's own 16% projection, which suggests a different basis (project-level, or including marks). The library treats this pairing as a RED cluster until restated. → Q-GP-02

**Cluster:** `GEN-07` + `GEN-08` + `EQUITY-06` = financing story.

**YELLOW–RED** (treated as RED until answered)

- `GEN-15` **Missing financials** 🟢. No rent roll, T-12 or complete debt terms in what was shared. They may exist in the offering documents, but the deal can't be underwritten without them. → Q-RISK-03
- `GEN-16` **Partial fee and waterfall disclosure** 🟢. Headline rates are given; bases, catch-up, cumulative status and clawback are not, so drag is a range. → Q-FEE-01

**YELLOW**

- `GEN-11` **No distribution schedule** 🟢. An IRR with no timing hides the J-curve; §3's shape is inferred only. → Q-DIST-01
- `GEN-13` **No sensitivity or downside case** 🟢. A single-point pro forma; §2 had to be built from assumptions. → Q-DS-03
- `GEN-17` **Essential value-add disclosures absent** 🟢. Exit-cap sensitivity, refi assumptions and multifamily exit record (see §6). → Q-RISK-03, Q-EXIT-02, Q-GP-02
- `EQUITY-01` **Deal-by-deal waterfall** 🟢. Library RED only with a high promote and no clawback; 20% is in range, so not RED on stated facts. 🟡 It also reads as a single asset, where the early-winners, late-losers failure narrows to one case: promote paid on an interim capital event such as a refi, followed by a weak sale. → Q-FEE-03

**Open probes: not fired, because the needed fact is undisclosed**

- `GEN-09` **Debt maturity vs hold.** A 5-year hold is stated, the loan's maturity is not. Fires RED if maturity, with extensions, lands inside year 5. → Q-RISK-01
- `GEN-10` **Rate cap expiry.** Floating debt is stated; whether a cap exists and when it expires is not. Fires RED if it lapses before maturity or exit: cap expires, rates stay elevated, refi is frozen, debt service erases distributions. → Q-RISK-02
- `EQUITY-07` **Refi dependence.** Bridge debt needs a takeout unless the sale comes first; plan not stated. → Q-EXIT-02
- `EQUITY-02` **Clawback.** Not stated. A confirmed absence is RED in a deal-by-deal waterfall. → Q-FEE-03
- `EQUITY-03` **Catch-up rate.** Not stated; worth about 95 bps/yr between 100% and none. → Q-FEE-03
- `EQUITY-05` **Cumulative or compounding pref.** Not stated. → Q-FEE-04
- `GEN-01` **GP co-invest.** Not stated. Fires RED if zero. → Q-GP-01
- `GEN-02` **Regulatory or litigation history.** Sponsor unnamed, so unchecked. → Q-GP-03
- `GEN-06` **Affiliate fee stacking.** Not stated. Renovation plus property management is where it would sit. → Q-FEE-02
- `GEN-12` **Trailing window.** No financials shown, so length unknown. → Q-RISK-03
- `GEN-18` **Rent growth vs submarket supply.** "Raise rents" is the plan, but no submarket, growth rate or supply data was given. → Q-MKT-01

**Clean:** `EQUITY-04` does not fire. An 8% pref is inside the 6–10% norm.

---

## 6. Missing Disclosures

**Essential for value-add multifamily (`01`)**

- Rent roll
- T-12 actuals
- Exit-cap sensitivity (the point estimate is there, the sensitivity is not)
- Debt structure and maturity: LTV, spread and index, term, extensions, amortization, rate cap strike and expiry, prepayment
- Refi assumptions
- Track record on **prior multifamily exits**

**Return story**

- Whether 16% / 2.0x is gross or net to LP
- Distribution schedule and stabilized cash-on-cash
- NOI today and at exit; rent growth and renovation premium assumed
- Unlevered return
- Purchase price and sources and uses. $178,600 of equity per door is a lot of equity: at 50–75% LTV it implies $357k–$714k per door of capitalization 🔴. That points to low leverage, a high basis, or a raise carrying a large budget and reserves. Each is a different risk, and these references carry no per-door norm, so **can't tell from this**

**Fees and waterfall (`02`)**

- Base for each stated fee
- Catch-up rate (**🔴 assumed at 100% in §4**)
- Pref cumulative or not, simple or compounding (modeled as simple)
- Clawback and any security for it; split tiers above the 20%
- Loan placement, refinance, construction management and admin/IR fees (**passed as 0 in §4; unknown**)
- Affiliated service providers

**Sponsor and LP terms**

- Sponsor identity, GP co-invest, number and vintage of prior deals
- Metro and submarket
- Minimum investment, capital-call terms, liquidity or transfer rights, K-1 timing

---

## 7. GP Alignment

- **Co-invest:** not stated. Dollar amount, cash vs fee waiver, and pari-passu status are all unknown. 🔴
- **Track record:** **unverified.** "30% IRR across prior deals" counts as no validated record until restated as net-to-LP on fully realized multifamily exits, losers included. 🔴
- **Waterfall:** 8/20 is market and the pref does real work. A deal-by-deal structure gives less protection, but the single-asset reading limits the damage if promote is paid only at final sale. Under a 100% catch-up the pref affects timing rather than the final split: the GP ends with the full 20% of profit. 🟡
- **Fee-vs-performance mix:** at least $5.25M of fixed fees against a promote that's only earned on profit above the pref. The fixed layer rewards closing and holding, the promote rewards the exit. An underwritten compression lifts promote too, so the GP benefits from the same assumption the LP is being asked to accept. 🟡
- **Affiliate fees:** not stated. 🔴

---

## 8. Questions for the GP

**Must-ask**

| ID | Question | Bad-answer signal | Flag |
|---|---|---|---|
| Q-EXIT-01 | Why is the exit cap below the going-in cap, and what's the IRR at an exit cap equal to or above going-in? | "Cap rates will compress"; the IRR breaks at flat; no sensitivity offered. | `EQUITY-06` |
| Q-DS-01 | What share of projected LP IRR comes from in-place cash flow versus the exit, and what's the IRR at a flat exit cap? | Won't decompose it; "real estate always appreciates"; falls below pref at flat. | `GEN-08`, `EQUITY-06` |
| Q-DS-02 | Strip out leverage and cap-rate compression: what is the unlevered, in-place return? | Levered IRR is the only figure; no unlevered view exists; "leverage is just how the deal works." | `GEN-07` |
| Q-DS-03 | What is the return under a bear case: flat rents, higher exit cap, no refinance? | Single-point pro forma; "we underwrite conservatively" with nothing to show; the bear case is still a gain. | `GEN-13` |
| Q-GP-02 | Can you restate your track record as net-to-LP IRR on fully-realized, exited deals only? | Only project- or GP-level IRR; "most deals are still performing"; can't separate realized from unrealized. | `GEN-05`, `GEN-14` |
| Q-RISK-01 | When does the debt mature relative to the projected hold, and what's the refinance or extension plan? | Maturity inside the hold; "we'll refinance" with no terms; no plan if the refi market is shut. | `GEN-09` |
| Q-RISK-02 | When does the rate cap expire relative to debt maturity, and what's the cost to extend it at current pricing? | Cap expires before maturity; extension cost not modeled; "rates should be lower by then." | `GEN-10` |
| Q-EXIT-02 | Does the business plan depend on a refinance, and what happens to distributions if the refi isn't available on the assumed terms? | Capital return requires a refi at lower rates; no fallback; "the refi market will reopen." | `EQUITY-07` |
| Q-RISK-03 | Can you provide trailing-twelve-month actuals, the rent roll, and complete debt terms? | T-3/T-6 only; rent roll withheld; "confidential until you commit." | `GEN-12`, `GEN-15`, `GEN-17` |
| Q-FEE-01 | Can you provide the complete fee schedule and the full distribution waterfall? Include the base for each fee and whether the 16% / 2.0x is net to LP. | "Standard market fees"; partial list; "the PPM has it" without producing it. | `GEN-16` |
| Q-FEE-03 | Is the waterfall deal-by-deal or whole-of-fund, and is there a clawback? Also the catch-up rate, and whether promote can be paid on a refi. | High promote with no clawback; can't explain the catch-up; "you get paid when we get paid." | `EQUITY-01`, `EQUITY-02`, `EQUITY-03` |
| Q-FEE-04 | What preferred return do LPs receive before the GP earns promote, and is it cumulative and compounding? | Non-cumulative; can't say whether unpaid pref carries forward. | `EQUITY-04`, `EQUITY-05` |
| Q-FEE-02 | Which service providers are GP-affiliated, what do they charge, and are those rates third-party-benchmarked? | "All arm's-length" without naming providers; affiliate fees undisclosed; no benchmark. | `GEN-06` |
| Q-DIST-01 | What is the projected distribution schedule, and at what milestones does LP capital start returning? | "We'll distribute when the deal supports it"; no milestones; silence. | `GEN-11` |
| Q-GP-01 | How much of your own capital is in this deal, on the same terms as LPs? | "Sweat equity is our investment"; a fee waiver, not cash; token amount on better terms. | `GEN-01` |
| Q-GP-03 | Have you or your principals faced any regulatory action, enforcement, or investor litigation? | "Nothing material"; blames the LP or regulator; a search surfaces something undisclosed. | `GEN-02` |
| Q-MKT-01 | What submarket supply pipeline and absorption data support the rent-growth assumption? | Metro-level optimism; "rents always go up here"; no supply pipeline acknowledged. | `GEN-18` |
| Q-LIQ-01 | What are my options if I need to exit before the hold period ends? | "A secondary market may develop"; "we'll try to accommodate." An honest "there is none" is a good answer. | — |

**Nice-to-ask**

| ID | Question | Bad-answer signal | Flag |
|---|---|---|---|
| Q-DIST-02 | When are capital calls expected, and what's the consequence of a missed or late call? Matters here because a rate-cap extension may be funded this way. | "Calls as needed" with no notice period; punitive dilution buried in the docs. | — |
| Q-GP-04 | How have your headcount and deal-monitoring capacity grown alongside AUM? | AUM multiplied with a flat team; "lean and efficient" as the whole answer; no named asset manager. | `GEN-04` (not fired) |
| Q-LIQ-02 | When will K-1s be delivered each year, and have you historically delivered them before the filing deadline? | "As soon as we can"; a history of extensions. | — |

---

## 9. Diligence Checklist

- [ ] **PPM and operating agreement:** read the waterfall language itself (pref, catch-up, clawback, promote on capital events), each fee's base, affiliate disclosures, capital-call and dilution terms, transfer restrictions.
- [ ] **Background and regulatory:** search the sponsor and each principal for SEC and state actions and investor litigation; pull Form ADV if an RIA is involved.
- [ ] **Track-record proof:** deal-by-deal realized results tied to distribution statements or K-1s, plus reference calls with LPs from exited deals, including the worst one.
- [ ] **Lender:** term sheet or commitment showing LTV, spread, maturity, extension tests, rate cap strike and expiry, and reserve requirements.
- [ ] **Exit-cap comps:** third-party sales comps for the submarket, to test whether 5.0% has any evidence behind it.
- [ ] **Appraisal:** independent as-is value against purchase price and price per door, with the capitalization reconciled to the $50M raise.
- [ ] **Rent comps and supply:** third-party submarket rent, absorption and pipeline data, to check the rent assumption.
- [ ] **Actuals:** rent roll and T-12 reconciled to the going-in 5.5% cap, confirming that cap is on actual rather than pro forma NOI.
- [ ] **Tax and legal:** your own counsel or CPA on the subscription documents and K-1 treatment.

---

## 10. Verdict

**Pursue with conditions.**

*Screening output only, not investment advice.*

**Why not Pass:** the structure is ordinary. An 8/20 waterfall, in-range headline fees and a 16% target that sits within `01`'s value-add range don't disqualify the deal. Enough was disclosed to read the core return story, so this is a merits verdict, and the gaps below are conditions. Most of the REDs can be resolved by a few documents the sponsor should already have.

**Why not Pursue:** the return as presented relies on selling at a lower cap rate than the purchase, below the 10yr Treasury, after holding floating bridge debt on undisclosed terms. Present value is 65–89% in the exit year. The only evidence of skill is a 30% figure with no basis. Fees and promote also take the sponsor's own best case to about 11.36% net if the 16% is gross, already under the 12–15% realized range.

**Biggest swing factor: the exit cap.** It's the one input that's both stated and unsupported. The illustrative base case at a flat cap (7.72% net) falls below the hurdle band, and one step further (6.0%) trails REITs. Debt terms come second, since they decide whether the LP gets to choose its exit date at all.

**Conditions: any failure is a Pass.**

1. **Net-to-LP numbers from the GP.** At a 5.5% exit, net IRR stays at or above about 8.92% (VNQ + 400 bps) and the pref is paid in full. At a 6.0% exit with flat rents and no refi, LP capital comes back whole.
2. **An unlevered return that holds up.** The operating return has to stand without compression, or the deal stays a financing story.
3. **Debt that fits the plan.** Maturity with extensions reaches past the planned exit, extension tests are achievable, and the rate cap runs through maturity or has a funded extension at current pricing.
4. **A realized record.** Net-to-LP results on exited multifamily deals, losers included, tied to statements.
5. **Clean documents.** Written fee bases and the full waterfall: cumulative pref, a stated catch-up, a clawback if promote can pay before final sale, and named affiliates with benchmarked rates.
6. **Cash alignment and clean history.** Meaningful GP cash co-invest on pari-passu terms, and a clean regulatory and litigation search.
7. **Underwritable financials.** Rent roll and T-12 that support the 5.5% going-in cap, and submarket data that supports the rent plan.

**Who it suits:** an LP who can leave this capital locked for 5 years and likely longer, can absorb a capital call, doesn't need current income, and can hold a single-asset position within a diversified allocation. It does not suit anyone relying on distributions or who may need the money back early.

**What would have to be true:** cap rates fall, or at least rents and NOI grow enough to make up for a flat cap; floating debt stays serviceable until sale; a buyer or lender is available in year 5; and a sponsor that reports 30% has actually delivered anything like that to its LPs after fees, on exited deals.
