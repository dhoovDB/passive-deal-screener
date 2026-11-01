# Eval fixture 09
*Iteration-6 run, 2026-11-01, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 436a76b.*

# Passive Deal Screen: Unnamed Multifamily Fund

**Verdict: Pass as presented — insufficient disclosure.** Four sentences give a target and an entry ticket. They give nothing that lets you underwrite the return. That is a verdict on the disclosure, not on the fund, and it reverses if the re-screen list in §10 comes back clean.

*Not investment advice. This screens a deal for further diligence. It is not financial, legal or tax advice, and the verdict is not a recommendation to invest.*

**The quick take:**
- "15%+ returns" is undefined. It doesn't say IRR or annual return, gross or net, or over what hold. A target is also not a floor, so the "+" adds nothing.
- If 15% is gross, a typical fee stack puts you near 10–11% net. If it is net, it sits at the top of what value-add multifamily has actually realized (12–15%).
- Unlevered institutional real estate is returning about 5%. Roughly 10 points of the claim must come from leverage, appreciation or operations, and the blurb doesn't say which.
- It costs nothing to ask. Send the five questions in §10 and only spend more time if they answer in writing.

Tags: 🟢 stated or from a reference, 🟡 inferred, 🔴 assumed or unverifiable.

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Multifamily 🟢. Sub-strategy not stated; 15%+ reads as value-add or riskier, above the 8–12% core / core-plus range 🟡 |
| Deal type | Fund, screened as equity syndication 🟡. "Multifamily fund" could also hold preferred equity or debt, which would change the routing |
| Sponsor | Not stated |
| Geography | Not stated |
| Minimum | $100k 🟢 |
| Hold | Not stated (category norm is 5–7 years for value-add, 7–10 for core 🟢) |
| Raise / fund size | Not stated |
| Claimed return | "15%+", metric and basis not stated 🟢 |
| Investor eligibility | Accredited only 🟢. This is an eligibility gate, not a quality signal 🟡 |

One mismatch to raise: `01` lists funds as a common format for core / core-plus, but 15%+ is at least 300 bps above that class's range. So this is either a value-add or riskier fund, or a core fund with an aggressive claim. The GP should say which.

## 2. Return Stress-Test

Nothing here is the fund's underwriting, because none was provided. These rows show how far the claim moves on its unstated definition. They inform the questions, not the verdict. The comparator is VNQ at 4.92% (10yr, to 2026-06-30), and the 10yr Treasury at 5.18% (2026-09-24) is currently the tighter floor.

| Case | What has to be true | Net to LP | Over VNQ | Over 10yr Treasury | Against illiquidity hurdle |
|---|---|---|---|---|---|
| **Bull** | 15% is a net IRR and is delivered 🔴 | 15.0% | 1008 bps | 982 bps | Clears comfortably at 5 or 7 years |
| **Base** | Fund lands at the realized value-add norm (`01`) 🟡 | 12–15% | 708–1008 bps | 682–982 bps | Clears comfortably |
| **Soft bear** | 15% is gross, with the `02` worked-example stack 🔴 | 10.6% (7yr), 10.2% (5yr) | 568 / 527 bps | 542 / 501 bps | 7yr clears thin, inside the ~400–600 band; 5yr clears the ~300–400 band |
| **Bear** | As above, plus a 200 bps gross miss (13% gross) 🔴 | 8.8% (7yr), 8.5% (5yr) | 390 / 353 bps | 364 / 327 bps | **7yr thin / fails**; 5yr clears thin |

**Swing assumptions:**
1. **Gross vs net.** This alone moves the answer about 440 bps.
2. **Exit cap.** `01` calls it the single biggest swing in most value-add pro formas. No figure is disclosed, so the 200 bps miss stands in for it.
3. **Rent growth and refinance terms.** Both are undisclosed and neither can be modeled here.

**Reading it:**
- Clearing VNQ is necessary, not sufficient. VNQ's weak decade flatters every spread here, and dispersion is wide: private real estate interquartile spreads run about 8.4 points (core) to 13 points (opportunistic).
- A 15% net return is about what SPY delivered liquid over the trailing decade (15.39%). That was an exceptional decade and not a forward promise. Even so, the GP owes an explicit diversification or downside rationale for locking up capital to earn the same number.
- Treat base and bull as unproven until the basis is stated (`GEN-13`, `GEN-11`).

## 3. Where LP Returns Come From

**Can't tell from this. That is the finding.** There is no split of cash flow, exit and leverage, so the >60% test can't be run.

The one thing the benchmarks do say: NCREIF NPI, the unlevered private real estate baseline, returned 5.00% over the four quarters to Q2 2026, almost all of it income (1.17% of the latest quarter's 1.29%). Residential returned 5.3% in 2025. Against that, **about 10 points of a 15% claim have to come from leverage, assumed appreciation or operating gains** 🟡.

That is normal for levered real estate equity, but it decides whether this is an asset story or a financing bet. `GEN-07` and `GEN-08` do not fire, because leverage and exit share are unknown and firing them would rest on assumptions. They stay open as must-asks (`Q-DS-01`, `Q-DS-02`).

## 4. Fee Stack Summary

**Gross-to-net drag: not computable from disclosure.** No fee of any kind is disclosed. The calculator with all undisclosed fees at `0` returns 0 bps, which reflects the silence and does not mean the fund is free.

For scale only 🔴: the `02` worked-example stack gives **~440 bps/yr at a 7-year hold** and ~481 bps/yr at 5 years (15% gross). None of these terms come from this fund.

| Layer | Disclosed? | `02` typical range | In the illustration (7yr, bps/yr) |
|---|---|---|---|
| Acquisition fee | Not stated | 1–2% of equity | 43 (with disposition) |
| Disposition fee | Not stated | 0.5–1% of sale price | included above |
| Asset management | Not stated | 1–2% of equity, annual | 180 (with admin) |
| Admin / IR / K-1 | Not stated | 0.1–0.5% of equity, annual | included above |
| Promote and pref | Not stated | 15–30% over a 6–10% pref | 217 |
| Loan placement / refinance | Not stated | 0.5–1.5% / 0.5–1% of loan | 0 (not in the illustration) |
| Construction management | Not stated | 3–5% of hard costs | 0 (not in the illustration) |
| Affiliate fees (property management, etc.) | Not stated | Disclosure and benchmarking is the test | 0 (not in the illustration) |
| Feeder / fund-of-funds wrapper, if any | Not stated | 50–150 bps/yr on top | 0 (not in the illustration) |

The illustration is therefore a partial stack. A fund that charges the excluded layers would drag more.

## 5. Red Flags

None of these say the fund is bad. They say the blurb can't show it isn't. Every flag below fires on absence, which `03` scores rather than passes over.

**RED**
- **`GEN-14` No realized exits cited.** The flag's literal trigger is met by silence 🟢. No marks were shown either, so this is not a confirmed unrealized-only record. Your exposure is backing a track record you haven't seen. (`GEN-05` stays open: no IRR basis exists to test.)

**YELLOW–RED (treat as RED until answered)**
- **`GEN-16` No fee or waterfall disclosure.** Undisclosed fees are still paid, and gross-to-net drag is unknowable 🟢. Parenthetically untestable under this: `EQUITY-01`, `EQUITY-02`, `EQUITY-03`, `EQUITY-04`, `EQUITY-05`, `GEN-06`. In a multi-asset fund, `EQUITY-01` and `EQUITY-02` carry real weight: deal-by-deal promote with no clawback lets the GP bank early winners while later assets lose LP capital.
- **`GEN-15` Missing financials.** No rent roll, T-12 or debt terms 🟢. If no assets are identified yet, these can't exist at the fund level, which is a question in itself 🟡. Parenthetically untestable under this: `GEN-12`, `GEN-09`, `GEN-10`, `EQUITY-07`. The relevant failure mode is the 2022–24 pattern: rate cap expires, refi market freezes, debt service erases distributions.

**YELLOW**
- **`GEN-11` Return with no distribution schedule.** A back-loaded and an early-paying fund can quote the same 15% with very different risk timing 🟢.
- **`GEN-13` No sensitivity or downside case.** A single number conceals how fragile it is 🟢.
- **`GEN-17` Essential category disclosures absent.** Against the `01` multifamily baseline: exit cap with sensitivity, refi assumptions, and GP record on prior multifamily exits 🟢.
- **`GEN-03` Marketing-heavy, substance-light.** A return headline and "contact us", with no underwriting or actuals 🟢.

**Cluster.** These all come from one fact, so they aren't seven separate problems, but `03` treats a YELLOW cluster as RED. The combined exposure is committing $100k to a return that can't be decomposed, with fees that can't be counted, from a sponsor who isn't named.

**Open: can't fire, can't clear.** These are must-asks, not findings:
- `GEN-01` (co-invest)
- `GEN-02` (regulatory history; can't be searched while the sponsor is unnamed)
- `GEN-07`, `GEN-08`, `EQUITY-06` (the financing-story family)
- `GEN-18` (rent growth vs supply)

`GEN-04` has no AUM data to test against.

## 6. Missing Disclosures

**Core return story (without these there is nothing to underwrite):**
- Return metric and basis: IRR vs annual vs cash-on-cash; net vs gross
- Hold period and lock-up terms
- Sub-strategy: value-add, core-plus or development
- Whether assets are identified, and how many (blind pool or named)
- Sponsor identity and realized multifamily exits, net to LP

**Fees and structure (`02`):**
- Complete fee schedule, including affiliates and any feeder layer
- Pref rate, cumulative or not, simple or compounding
- Promote, catch-up and tiers
- Deal-by-deal vs whole-of-fund waterfall, and clawback
- GP co-invest

**Asset and financing (`01`, per asset):**
- Rent roll
- T-12 actuals
- Pro forma exit cap with sensitivity
- Debt structure and maturity
- Rate cap terms
- Refi assumptions

**Fund mechanics:**
- Fund size and target leverage
- Distribution schedule
- Capital call terms and default penalties
- Geography and concentration limits
- Early-exit options

## 7. GP Alignment

**Unverified on every axis, because no GP is identified.**

| Axis | Status |
|---|---|
| Co-invest (cash, pari-passu?) | Not stated |
| Realized net-to-LP track record | Not stated, so treat as no track record 🔴 |
| Waterfall alignment | Not stated |
| Affiliate fees | Not stated |

The $100k minimum and accredited-only limit tell you who may invest, not how the GP is paid or what it has at risk.

## 8. Questions for the GP

**Must-ask**

| ID | Ask | Bad-answer signal | Flag |
|---|---|---|---|
| `Q-GP-02` | Restate your track record as net-to-LP IRR on fully realized, exited deals only. | Only project- or GP-level IRR; "most deals are still performing" | `GEN-14`, `GEN-05` |
| `Q-FEE-01` | Provide the complete fee schedule and full distribution waterfall. | "Standard market fees"; "the PPM has it" without producing it | `GEN-16` |
| `Q-FEE-03` | Is the waterfall deal-by-deal or whole-of-fund, and is there a clawback? | Deal-by-deal with a high promote and no clawback; "you get paid when we get paid" | `EQUITY-01`, `EQUITY-02` |
| `Q-FEE-04` | What pref do LPs receive before promote, and is it cumulative and compounding? | Below 6% or absent; non-cumulative | `EQUITY-04`, `EQUITY-05` |
| `Q-FEE-02` | Which providers are GP-affiliated, what do they charge, and is that benchmarked? | "All arm's-length" without naming anyone | `GEN-06` |
| `Q-GP-01` | How much of your own capital is in, on LP terms? | "Sweat equity is our investment"; a fee waiver instead of cash | `GEN-01` |
| `Q-GP-03` | Any regulatory action, enforcement or investor litigation? | "Nothing material"; a search surfaces something undisclosed | `GEN-02` |
| `Q-DS-01` | What share of LP IRR is in-place cash flow vs exit, and what is the IRR at a flat exit cap? | Can't decompose it; "real estate always appreciates" | `GEN-08`, `EQUITY-06` |
| `Q-DS-02` | Strip out leverage and cap-rate compression: what is the unlevered, in-place return? | No unlevered view exists; "leverage is just how the deal works" | `GEN-07` |
| `Q-DS-03` | What is the return with flat rents, a higher exit cap and no refinance? | "We underwrite conservatively" with nothing to show; the bear case is still a gain | `GEN-13` |
| `Q-DIST-01` | What is the distribution schedule, and when does capital start returning? | "We'll distribute when the deal supports it"; no milestones | `GEN-11` |
| `Q-RISK-03` | Provide T-12 actuals, rent rolls and complete debt terms. | T-3/T-6 only; "confidential until you commit" | `GEN-15`, `GEN-12` |
| `Q-RISK-01` | When does debt mature relative to the hold, and what is the plan? | "We'll refinance" with no terms | `GEN-09` |
| `Q-RISK-02` | When do rate caps expire, and what does extension cost today? | Cap expires before maturity; "rates should be lower by then" | `GEN-10` |
| `Q-EXIT-01` | Is any exit cap below going-in, and what is the IRR at flat or higher? | "Cap rates will compress"; no sensitivity | `EQUITY-06`, `GEN-17` |
| `Q-EXIT-02` | Does the plan depend on a refinance, and what if it isn't available? | "The refi market will reopen"; no fallback | `EQUITY-07` |
| `Q-MKT-01` | What submarket supply and absorption data support rent growth? | Metro-level optimism; "rents always go up here" | `GEN-18` |
| `Q-LIQ-01` | What are my options if I need out before the hold ends? | "A secondary market may develop." An honest "none" is a good answer | — |

`GEN-03` has no `04` question. Use its `03` response: "Can you provide the full underwriting model and the historical actuals behind these projections?" The bad-answer signal is more marketing material in place of a model.

**Nice-to-ask**

| ID | Ask | Bad-answer signal |
|---|---|---|
| `Q-GP-04` | How have headcount and monitoring capacity grown with AUM? (`GEN-04`) | "We're lean and efficient" as the whole answer |
| `Q-DIST-02` | When are capital calls expected, and what happens on a missed call? | "Calls as needed"; punitive dilution buried in the docs |
| `Q-LIQ-02` | When are K-1s delivered, and have they met the filing deadline? | "As soon as we can" |

## 9. Diligence Checklist

Third-party checks still needed once the sponsor is named:
- [ ] **PPM and operating agreement:** read fees, waterfall and clawback directly, and reconcile them to the marketing.
- [ ] **Background and regulatory:** principals, entities, investor litigation; Form ADV if the manager is an RIA.
- [ ] **Offering filing:** confirm the exemption and any filing with counsel (legal question, outside this screen) 🟡.
- [ ] **Track record:** verify realized exits against audited statements or actual LP distribution records.
- [ ] **Fund audit:** audited financials and any third-party administrator 🟡.
- [ ] **Comps and appraisal:** rent and sale comps, plus appraisals, for each identified asset.
- [ ] **Lenders:** confirm loan terms, maturities and rate-cap agreements from source documents.
- [ ] **LP references:** speak to LPs in a fully exited prior deal 🟡.

## 10. Verdict

**Pass as presented — insufficient disclosure.**

**Reasoning.** Essential disclosures are substantially absent, so the core return story can't be underwritten. There is no sponsor, hold, fee, waterfall, debt, asset or track record information. The claim isn't outlandish: 15% falls inside the value-add target range, and I'm not treating it as evidence of a bad deal. It just can't be tested.

**Biggest swing factor.** What "15%+" actually is. Net vs gross moves your outcome about 440 bps, and the source of the ~10 points above the unlevered baseline decides whether you're buying an asset or a financing bet.

*Screening output only, not investment advice.*

**Who it suits.** As presented, nobody, because it can't be evaluated. If it screens clean, it fits an accredited LP who can leave $100k locked for the unstated hold (likely 5+ years by category norm, with no assumed liquidity) and accept levered real estate equity risk.

**What would have to be true for a Pursue:**
- 15% or the corrected figure is stated net to LP, with a credible cash-flow share.
- Fees and waterfall sit in `02` norms: pref at 6% or higher and cumulative, promote at 30% or lower, and whole-of-fund or a secured clawback.
- The return still clears the VNQ-plus-premium and Treasury floors after a real bear case. On the illustration above, a 7-year fund has little room.
- Realized net-to-LP exits exist, and the GP has real cash in on LP terms.

**Re-screen list.** Send these five first, and re-run this screen on the answers:
1. Sponsor name, plus realized net-to-LP results on exited multifamily deals (`Q-GP-02`, `Q-GP-03`).
2. What "15%+" is: metric, net or gross, and over what hold, plus the bear case (`Q-DS-03`, `Q-LIQ-01`).
3. Complete fee schedule and waterfall, including pref, promote and clawback (`Q-FEE-01`, `Q-FEE-03`, `Q-FEE-04`).
4. The PPM, the asset list or stated blind-pool criteria, target leverage and debt terms (`Q-RISK-03`, `Q-DS-02`).
5. GP cash co-invest and the distribution schedule (`Q-GP-01`, `Q-DIST-01`).

A GP who won't answer these in writing has given you the answer.
