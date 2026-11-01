# Eval fixture 01
*Iteration-7 run, 2026-11-01, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 181fdd7.*

# Passive Deal Screen: Sun Belt Value-Add Multifamily Syndication (280 units, $50M raise)

**Verdict: Pursue with conditions.** This is close to a Pass. The 16% headline is a financing story: it rests on exit-cap compression (5.5% in, 5.0% out) on floating-rate bridge debt. Several hard conditions must clear before you commit (see §10).
*Screening output only, not investment advice.*

Confidence tags: 🟢 stated by the deal or from a reference · 🟡 inferred · 🔴 assumed or unverifiable.

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Multifamily, value-add 🟢 |
| Deal type | Equity syndication 🟢 (routes to `02` Equity + Waterfall; `03` GEN-/EQUITY- flags; `05` VNQ comparator + NCREIF NPI unlevered overlay) |
| Sponsor | Not stated |
| Geography | "Sun Belt" 🟢. Metro and submarket not stated |
| Units | 280 🟢 (about $179k of LP equity per unit 🟡) |
| Equity raise | $50M 🟢 |
| Purchase price / total capitalization | Not stated |
| Leverage (LTV / LTC, loan amount) | Not stated |
| Debt | Bridge, floating rate 🟢. Spread, term, extensions, rate cap and maturity are not stated |
| Minimum investment | Not stated |
| Hold | 5 years 🟢 (inside the `01` value-add norm of 5–7 years) |
| Claimed return | 16% IRR / 2.0x equity multiple 🟢. **Gross or net-to-LP basis not stated** |
| Business plan | Renovate interiors and raise rents 🟢. Renovation budget, rent premium and rent-growth assumption not stated |
| Cap rates | Going-in 5.5%, exit 5.0% 🟢 |
| Waterfall | 8% pref, 20% promote, American (deal-by-deal) 🟢. Catch-up, clawback, and whether the pref is cumulative or compounding are not stated |
| Fees | 2% acquisition, 1.5% annual asset management, 1% disposition 🟢. The base for each fee (equity vs price) is not stated |
| Track record | "30% IRR across prior deals" 🟢 as stated, 🔴 unverified |
| Distribution schedule | Not stated |
| GP co-invest | Not stated |

## 2. Return Stress-Test

**Basis first.** The deal does not say whether 16% is gross (property-level) or net-to-LP. That changes the answer, so both readings are carried below.

- A 2.0x multiple over 5 years with everything paid at exit would be about a 14.9% IRR. Reaching 16% requires meaningful distributions before exit. The schedule of those distributions is undisclosed (GEN-11). 🟡
- **If 16% is gross:** `fee_drag_calculator.py` with the stated fees, 8% pref and 20% promote puts net-to-LP at **about 11.4%** (catch-up modeled at 100%) to **about 12.3%** (no catch-up). The catch-up is unstated, so this is a §6 gap.
- **If 16% is already net-to-LP:** the property has to produce roughly 20%+ gross to get there after fees, which is a harder bar. 🟡

**The swing assumptions:**
1. **Exit cap (dominant).** The 5.0% exit sits 50 bps below the 5.5% going-in. On the same NOI, that alone raises exit value by about 10% (5.5 / 5.0), and leverage multiplies the effect on equity. 🟢 mechanism.
2. **Rent growth and renovation premium.** "Raise rents" is the whole operating thesis, but no rent-growth rate, premium or comps are given. 🔴
3. **Bridge debt cost and refinance.** The debt is floating and short-duration, with no disclosed cap, maturity or takeout plan. 🔴

**Illustrative scenarios.** Leverage is not disclosed, so this model assumes 🔴 65% LTV, interest-only, and about 0.30x of interim distributions in years 2–5. It is calibrated to the sponsor's 2.0x. Its purpose is to show sensitivity. It is not a forecast.

| Case | Exit cap | NOI path | Equity multiple | IRR (sponsor's basis) |
|---|---|---|---|---|
| Bull | 4.75% | as underwritten | about 2.2x | about 17.7% |
| Base (sponsor) | 5.0% | as underwritten (about +13% NOI) | 2.0x | about 15.6–16% |
| Flat exit cap | 5.5% | as underwritten | about 1.7x | **about 11.5%** |
| Bear | 6.0% | half the NOI growth, thinner distributions | about 1.1x | **about 1.7%** |

Holding the exit cap flat at going-in removes roughly **400 bps** of IRR in this illustration. That is the price of the cap-compression assumption. 🔴 (The exact size depends on the undisclosed leverage. The direction does not.)

**Against the public comparator.** `benchmark_comparator.py`, multifamily-value-add, VNQ 4.92% 10yr, 5-year lock-up, illiquidity hurdle about 300–400 bps:

| Net-to-LP IRR scenario | Premium over VNQ | Read |
|---|---|---|
| 16.0% (headline, if already net) | 1108 bps | Clears comfortably |
| 12.3% (headline gross → net, no catch-up) | 738 bps | Clears comfortably |
| 11.4% (headline gross → net, 100% catch-up) | 648 bps | Clears comfortably |
| 7.5% (flat 5.5% exit cap, gross basis → net via fee calculator) | 258 bps | **Thin / fails** the illiquidity hurdle |
| 1.7% (bear) | −322 bps | **Fails**: trails the liquid comparator outright |

- **Treasury floor (`05`).** For a 5-year duration, the matched Treasury point sits between the 2yr at 4.87% and the 10yr at 5.18%. At the flat-cap outcome, the LP earns only about 250 bps over a risk-free bond for a 5-year illiquid, single-asset, levered position. 🟢 reference / 🟡 applied.
- **Read.** The deal clears the hurdle **only if the exit cap compresses**, or if the 16% turns out to be net. It beats its own pro forma but trails the comparator plus premium once compression is removed. In that case the lock-up is uncompensated.
- **Dispersion (`05`, Preqin).** Even when the hurdle clears, it is necessary but not sufficient. The median outcome sits well below a marketed figure. `01` puts realized value-add multifamily at about 12–15% net blended, against a 14–18% marketing range.

## 3. Where LP Returns Come From

- **In-place, unlevered yield is about 5.5%.** That is the going-in cap, before renovation capex. It lines up with the `05` NCREIF NPI unlevered baseline: 5.00% trailing four quarters, residential 5.3% in 2025, and almost entirely income. 🟢
- **The other 10+ points of the 16% headline** come from three sources: (a) leverage, (b) the renovation and rent-growth premium, and (c) exit-cap compression. 🟡 Only (b) is an operating story, and its inputs (renovation budget, rent premium, comps) are undisclosed.
- **Exit share of profit is at least about 60–70%.** 🟡 The 2.0x means 1.0x of profit. `01` puts value-add cash-on-cash at 5–8% after stabilization, so interim distributions over 5 years plausibly total around 0.2–0.35x. That leaves roughly **65–80% of profit coming from the sale**. The illustrative model lands at about 70%. This crosses the >60% threshold, so **GEN-08 fires**.
- **The leverage is likely negative or thin at the start.** 🟡 The going-in yield is 5.5%. Floating bridge debt prices off the short rate (the `05` short anchor is the 3-month Treasury at 4.24%) plus an undisclosed spread. Any all-in coupon above about 5.5% means the debt costs more than the asset yields. Early cash flow then gets thinner, and the return leans further on the exit.
- **Conclusion:** GEN-07 (financing story) + GEN-08 (exit-dependent) + EQUITY-06 (exit cap below going-in) all fire together. **This is a financing story.** A rate path, a refinance window and a cap-rate bet sit on top of a modest in-place yield.

## 4. Fee Stack Summary

| Fee | As stated | `02` typical range | Read |
|---|---|---|---|
| Acquisition | 2% (base unstated) | 1–2% of equity, or 0.5–1.5% of purchase price | Top of range if on equity. **At the aggressive threshold (>2% of price) if on purchase price** |
| Asset management | 1.5% annual (base unstated) | 1–2% of equity raised, annual | In range. Equity raised or invested capital? |
| Disposition | 1% (base unstated) | 0.5–1% of sale price | Top of range. Check for a double-charge with the brokerage commission |
| Promote | 20% over 8% pref | 15–30% over 6–10% pref | In range. EQUITY-04 does not fire |
| Catch-up | Not stated | 50 / 80 / 100% | Gap |
| Loan placement (bridge) | Not stated | 0.5–1.5% of loan | Likely present on bridge debt. Gap |
| Refinance fee | Not stated | 0.5–1% of new loan | Relevant if the plan refinances out of the bridge. Gap |
| Property management (affiliate?) | Not stated | Not stated | GEN-06 probe |
| Admin / IR | Not stated | 0.1–0.5% of equity | Gap |

**Gross-to-net drag: about 464 bps/yr.** This assumes 16% is gross, fees are charged on equity, catch-up is 100% (unstated), and undisclosed fees are passed as 0. The breakdown is 150 recurring + 60 one-time + 254 promote, for a net of about 11.4%.
- With no catch-up, drag falls to about 369 bps (net about 12.3%).
- **If acquisition and disposition are charged on purchase and sale price, as `02` commonly quotes them**, the one-time load rises sharply. An illustrative 🔴 run at about 3x price-to-equity (acquisition about 6%, disposition about 3.5% of equity) gives **about 594 bps of drag (net about 10.1%)**.
- The undisclosed lines (loan placement, refinance, admin, affiliate property management) would add to all of these figures.
- The drag is computable only within a band, and that band is itself the finding (GEN-16, partial).

## 5. Red Flags

**RED**
- **GEN-07: Financing story** 🟡. Of a 16% target, only about 5.5 points are in-place unlevered yield. The rest is leverage, renovation premium and cap compression. LP exposure: the return collapses if rates stay high or cap rates do not compress.
- **GEN-08: Exit-dependent IRR** 🟡. About 65–80% of profit comes from the sale (§3). LP exposure: this is a single-date sale bet, not an income stream.
- **EQUITY-06: Exit cap below going-in** 🟢. 5.0% vs 5.5% builds about a 10% value uplift into the headline before any operating gain. LP exposure: roughly 400 bps of IRR in the illustration (§2).
  - *Cluster:* GEN-07 + GEN-08 + EQUITY-06 = **financing story**, named explicitly.
- **GEN-05: GP-IRR vs LP-IRR divergence** 🟢 stated / 🔴 unverified. "30% IRR across prior deals" is not labeled net-to-LP. It is likely project-level or gross. LP exposure: the record says nothing about what LPs actually received.
- **GEN-14: Unrealized-only / no realized exits cited** 🟢. No realized exits, no deal count and no vintage are given. LP exposure: there is no proof the GP has exited and returned capital.
  - *Cluster:* GEN-05 + GEN-14 = **no validated track record** (RED cluster per `03`). A 30% figure is about double `01`'s 12–15% realized category range. That is a reason to see deal-level data, not a reason for comfort.

**YELLOW–RED**
- **EQUITY-07: Refinance-dependent business plan** 🟡. Bridge debt against a 5-year value-add hold implies either a takeout refinance or extensions. LP exposure: the 2022–24 frozen-refi pattern leads to capital calls or suspended distributions.
- **GEN-15: Missing financials** 🟢. No rent roll, no T-12 and no full debt terms. LP exposure: the "raise rents" thesis cannot be underwritten.
- **GEN-16: Fee/waterfall disclosure incomplete (partial)** 🟢. Headline fees are given. Catch-up, clawback, fee bases, loan placement, admin and property management are not. LP exposure: the drag is known only within the roughly 370–590+ bps band.

**YELLOW**
- **EQUITY-01: Deal-by-deal (American) waterfall** 🟢. The 20% promote is in range, so this is not RED on its own (`03` reserves RED for a high promote with no clawback). In a single-asset deal, the live risk is promote paid on interim or refinance distributions before the final sale outcome is known. Clawback is unstated (EQUITY-02 probe).
- **GEN-11: No distribution schedule** 🟢. An IRR is given with no J-curve (proactive trigger). Combined with GEN-08, LP capital is likely back-loaded to exit.
- **GEN-13: No sensitivity or downside case** 🟢. The pro forma is single-point, and the exit cap is the biggest swing in value-add multifamily (`01`).
- **GEN-17: Essential category disclosures absent** 🟢. Several of `01`'s value-add essentials are missing: exit-cap sensitivity, debt maturity, refinance assumptions, and prior multifamily exits (see §6).
- **GEN-18: Rent-growth assumption unverified** 🟡. The thesis depends on rent growth in an unnamed Sun Belt submarket with no supply or absorption data. Severity depends on the submarket pipeline. No specific market condition is asserted here.

**Probed, not yet fired (RED until answered)**
- **GEN-09: Debt maturity inside the hold** 🔴. The hold is 5 years and the bridge maturity is unstated. Probe via Q-RISK-01. Do not wait for the GP to volunteer it.
- **GEN-10: Rate cap expiry** 🔴. The debt is floating with no cap disclosed. If a cap exists and expires before maturity or the refinance, debt service can spike and erase distributions.
- **EQUITY-02** (clawback), **EQUITY-03** (catch-up rate), **EQUITY-05** (cumulative pref), **GEN-01** (co-invest), **GEN-02** (regulatory/litigation history) and **GEN-06** (affiliate fees) are all unstated. Each routes to a must-ask in §8.

**Checked and clear** 🟢
- 8% pref meets the ≥6% bar, so EQUITY-04 does not fire.
- 20% promote is ≤30%.
- Asset management fee is within `02`'s range.

## 6. Missing Disclosures

These are items `01` and `02` say a value-add multifamily equity syndication normally discloses. This deal omits them:

- **Financials:** rent roll; T-12 actuals (not T-3/T-6); in-place vs pro forma rents; renovation budget and rent premium per unit; rent-growth assumption.
- **Debt:** loan amount and LTV/LTC; spread and index; initial term and extension options with their tests; **rate cap strike, expiry and replacement cost**; maturity relative to the 5-year hold; refinance or takeout assumptions.
- **Returns:** whether 16% / 2.0x is gross or net-to-LP; exit-cap sensitivity; distribution schedule (J-curve); bear case.
- **Waterfall:** catch-up rate; clawback (and whether it is escrowed); whether the pref is cumulative and simple or compounding; whether promote can be paid on refinance distributions.
- **Fees:** the base for acquisition, asset management and disposition fees (equity vs price); loan placement, refinance, admin/IR and property management fees, and whether any go to GP affiliates.
- **Sponsor:** identity; prior *multifamily exits* with realized net-to-LP returns, deal count and vintages; GP co-invest and whether it is pari-passu cash; regulatory or litigation history.
- **Deal:** purchase price; metro and submarket; minimum investment; capital-call provisions; LP liquidity before exit.

## 7. GP Alignment

- **Co-invest:** not stated. 🔴 Whether the GP has cash at risk on the same terms as LPs is unknown (GEN-01 probe).
- **Track record:** **unverified.** "30% IRR across prior deals" has no stated basis (gross, project-level, GP-level or net-to-LP), no realized/unrealized split, no deal count and no vintage. Under the skepticism contract, a figure of unstated basis counts as no validated track record (GEN-05, GEN-14). 🔴
- **Waterfall alignment:** the 8% pref and 20% promote are market-standard. 🟢 The deal-by-deal structure with no disclosed clawback, plus an unknown catch-up, lets the GP collect promote on refinance proceeds before the sale proves the business plan. 🟡
- **Fee alignment:**
  - The acquisition fee (top of range or above, depending on base) and the 1.5% asset management fee pay the GP regardless of outcome. Over 5 years they total about 9.5% of equity (2% + 1.5% × 5) before any promote. 🟢
  - A GP with fee income sized like this and an undisclosed co-invest earns on the deal even when LPs do not.
- **Affiliate fees:** property management and any construction management for the renovations are not disclosed (GEN-06 probe).

## 8. Questions for the GP

**Must-ask**

| ID | Question | Bad-answer signal (the specific dodge) | Fired flag |
|---|---|---|---|
| Q-DS-01 | What share of projected LP IRR comes from in-place cash flow versus the exit, and what's the IRR at a flat exit cap? | Cannot or will not decompose the IRR; "real estate always appreciates"; the IRR drops below the 8% pref at a 5.5% exit. | GEN-08, EQUITY-06 |
| Q-DS-02 | Strip out leverage and cap-rate compression: what is the unlevered, in-place return? | Treats the levered IRR as the only relevant figure; "leverage is just how the deal works." | GEN-07 |
| Q-DS-03 | What is the return under a bear case: flat rents, higher exit cap, no refinance? | "We underwrite conservatively" with nothing to show; no downside model; a bear case that is still a gain. | GEN-13 |
| Q-EXIT-01 | Why is the exit cap below the going-in cap, and what's the IRR at an exit cap equal to or above 5.5%? | "Cap rates will compress"; the IRR breaks at flat; no sensitivity offered. | EQUITY-06 |
| Q-EXIT-02 | Does the plan depend on refinancing out of the bridge, and what happens to distributions if the refinance isn't available on the assumed terms? | Return of capital requires a refinance at lower rates; no fallback; "the refi market will reopen." | EQUITY-07 |
| Q-RISK-01 | When does the bridge loan mature relative to the 5-year hold, and what are the extension tests? | Maturity falls inside the hold; "we'll refinance" with no terms; extension tests (DSCR, debt yield) not disclosed. | GEN-09 (probe) |
| Q-RISK-02 | Is there a rate cap? When does it expire relative to maturity, and what does it cost to extend at current pricing? | Cap expires before maturity; extension cost not modeled; "rates should be lower by then." | GEN-10 (probe) |
| Q-RISK-03 | Can you provide trailing-twelve-month actuals, the rent roll, and complete debt terms? | T-3/T-6 only; rent roll withheld; "confidential until you commit." | GEN-15 |
| Q-GP-02 | Can you restate the 30% track record as net-to-LP IRR on fully realized, exited deals only? | Offers only project-level or GP-level IRR; "most deals are still performing"; cannot separate realized from marked. | GEN-05, GEN-14 |
| Q-GP-01 | How much of your own capital is in this deal, on the same terms as LPs? | "Our sweat equity is our investment"; co-invest delivered as a fee waiver; a token amount on better terms. | GEN-01 (probe) |
| Q-GP-03 | Have you or your principals faced any regulatory action, enforcement, or investor litigation? | "Nothing material"; blames the LP or regulator; a search turns up something undisclosed. | GEN-02 (probe) |
| Q-FEE-01 | Can you provide the complete fee schedule, including the base for each fee, and the full distribution waterfall? | "Standard market fees"; a partial list; "the PPM has it" without producing it. | GEN-16 |
| Q-FEE-02 | Which service providers (property management, construction management, loan placement) are GP-affiliated, what do they charge, and are the rates third-party-benchmarked? | "All arm's-length" without naming providers; affiliate fees undisclosed. | GEN-06 (probe) |
| Q-FEE-03 | The waterfall is deal-by-deal. Is there a clawback, how is it secured, and can promote be paid on refinance distributions? | No clawback; cannot explain the catch-up; "you get paid when we get paid." | EQUITY-01, EQUITY-02 |
| Q-FEE-04 | Is the 8% pref cumulative and compounding, and what is the catch-up rate? | Non-cumulative; vague on catch-up; 100% catch-up offered without justification. | EQUITY-05, EQUITY-03 (probe) |
| Q-MKT-01 | What submarket supply pipeline and absorption data support the rent-growth and renovation-premium assumptions? | Metro-level "Sun Belt growth" in place of submarket data; no supply pipeline acknowledged. | GEN-18 |
| Q-DIST-01 | What is the projected distribution schedule, and at what milestones does LP capital start returning? | "We'll distribute when the deal supports it"; no milestones; silence. | GEN-11 |
| Q-LIQ-01 | What are my options if I need to exit before the 5-year hold ends? | "A secondary market may develop"; "we'll try to accommodate." | — |

**Nice-to-ask**

| ID | Question | Bad-answer signal |
|---|---|---|
| Q-GP-04 | How have your headcount and deal-monitoring capacity grown alongside AUM? | AUM multiplied while the team stayed flat; no named asset manager. |
| Q-DIST-02 | When are capital calls expected, and what's the consequence of a missed or late call? | "Calls as needed" with no notice period; punitive dilution buried in the documents. (This matters more with floating bridge debt, where a cap replacement can force a call.) |
| Q-LIQ-02 | When will K-1s be delivered, and have you historically met the filing deadline? | "As soon as we can"; a history of extensions. |

## 9. Diligence Checklist

These are items that need third-party verification:

- [ ] **PPM and operating agreement:** confirm the waterfall (catch-up, clawback, pref terms, promote on refinance proceeds), every fee and its base, affiliate arrangements, and capital-call and dilution terms.
- [ ] **Loan documents and rate cap agreement:** lender term sheet, maturity, extension tests, cap strike and expiry, and cap-replacement escrow requirements.
- [ ] **Track record verification:** deal-level realized net-to-LP returns from distribution statements, plus references from LPs in prior exited multifamily deals.
- [ ] **Background and regulatory search:** SEC, FINRA and state actions, litigation and bankruptcy searches on the principals (GEN-02).
- [ ] **Third-party valuation:** appraisal or broker opinion on the in-place cap rate, a defensible exit cap, and rent comps for renovated units in the submarket.
- [ ] **Financials:** T-12 and rent roll reconciled to bank statements or the lender's underwriting.
- [ ] **Independent submarket data:** supply pipeline and absorption for the specific submarket, not the Sun Belt headline.

## 10. Verdict

**Pursue with conditions.**
*Screening output only, not investment advice.*

- **Why not a clean Pursue.** The 16% / 2.0x is a **financing story** (GEN-07 + GEN-08 + EQUITY-06).
  - About 5.5 points of in-place unlevered yield support a headline that needs leverage, rent growth and 50 bps of cap compression.
  - It also sits on floating bridge debt with no disclosed cap, maturity or refinance plan.
  - Remove the compression and the illustrative return falls to about 11.5% on the sponsor's basis. If that basis is gross, net is about 7.5%, which **fails** the 5-year illiquidity hurdle over VNQ (258 bps vs about 300–400 bps) and sits only about 250 bps over the Treasury floor.
  - The "30% IRR" track record is unverified (GEN-05 + GEN-14).
- **Why not a Pass.** The core return story is disclosed well enough to underwrite: return, multiple, hold, both cap rates, headline fees, pref and promote. The fees and pref/promote are in market range. The decisive unknowns (net basis, debt terms, realized record) are answerable. Neither the Pass case nor the Pursue case can rest on 🔴 assumptions, so they become hard conditions.
- **Biggest swing factor:** the **exit cap**. The 5.0% vs 5.5% assumption is worth roughly 400 bps of IRR in the illustration. Combined with the bridge debt terms, it determines whether LP capital survives a flat or rising cap-rate exit.

**Conditions. Each is a walk-away if it fails:**
1. The GP confirms the net-to-LP basis, and **net-to-LP IRR at a 5.5% (flat) exit cap still clears about 8–9%**. That is roughly the 300–400 bps hurdle over VNQ's 4.92%, and it also covers the 8% pref (Q-DS-01, Q-EXIT-01).
2. **Debt terms:** maturity plus extensions cover the 5-year hold under realistic extension tests. A rate cap runs to maturity, or its replacement cost is budgeted and reserved. There is a credible path if the refinance is unavailable (Q-RISK-01, Q-RISK-02, Q-EXIT-02).
3. **Track record restated** as realized, net-to-LP returns on prior multifamily exits (Q-GP-02).
4. **Clawback** (or no promote on refinance proceeds), a cumulative pref, a stated catch-up, the full fee schedule with bases, and affiliate fees disclosed (Q-FEE-01–04).
5. **GP co-invest in cash, pari-passu** (Q-GP-01), and a clean regulatory and litigation search (Q-GP-03).
6. T-12, rent roll and the submarket supply data support the rent thesis (Q-RISK-03, Q-MKT-01).

**Who it suits:** an LP who wants a levered bet on Sun Belt multifamily rent growth and cap-rate recovery, can hold for 5+ years with no liquidity, and can absorb a capital call or a loss of principal in the bear case (about 1.1x in the illustration, before any debt-service shock). It does not suit an LP looking for income: the return is about 65–80% back-loaded to the sale.

**What would have to be true:** cap rates at exit are at or below today's, the renovation premium is achieved on schedule, short rates fall or the cap holds through a refinance, and the GP's record survives a restatement to realized net-to-LP figures.
