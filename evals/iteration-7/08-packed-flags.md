# Eval fixture 08

*Iteration-7 run, 2026-11-01, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 181fdd7.*

# Deal Screen: Multifamily Syndication (sponsor and asset not named)

**Verdict: PASS.** Six RED flags rest on facts you were told directly, not on anything assumed. The sponsor has no capital in the deal, one principal has a prior SEC action, and the GP takes 50% of profits with no clawback. On top of that, the rate cap expires before the loan matures and the track record is entirely unrealized. More disclosure can't fix the main problems, because they are the terms themselves.

*Screening output only, not investment advice.*

> This screen decides whether the deal deserves more diligence. It is not financial, legal or tax advice, and the verdict is not a recommendation to invest or not invest.

Confidence tags: 🟢 stated by you or taken from a reference · 🟡 inferred · 🔴 assumed or unverifiable.

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Multifamily 🟢. The strategy (value-add or core) is **not stated**. The single asset, floating-rate bridge-style debt and upside-only projections suggest value-add 🟡 |
| Deal type | Equity syndication, single asset 🟢 |
| Sponsor | Not stated. One principal was named in a prior SEC action 🟢 |
| GP co-invest | **None.** "Our expertise is our investment" 🟢 |
| Waterfall | American (deal-by-deal), **50% promote**, **no clawback** 🟢. Pref, catch-up and tiers are not stated |
| Debt | Floating rate 🟢. Rate cap expires in about 12 months (around Nov 2027) 🟢. Loan matures in 2028 (month not stated) 🟢. LTV, rate, spread, extension options and amortization are not stated |
| Geography / submarket | Not stated |
| Minimum investment | Not stated |
| Hold period | Not stated |
| Raise / equity size | Not stated |
| Claimed return | Not stated. The only projection shown is an upside case 🟢 |
| Fees (acquisition, asset management, disposition, financing, admin) | Not stated |
| Track record | All current, unrealized marks 🟢 |

---

## 2. Return Stress-Test

**No return figure was disclosed**, so there is nothing net-to-LP to test. A single upside case is a ceiling, not a projection. The figures below show what this waterfall would do to a typical deal. They use the fee_drag_calculator.py defaults (15% gross, 7-year hold, 8% pref, 100% catch-up) 🔴. They are **not** this deal's numbers.

**Swing assumptions:** (1) **the debt cost after the cap expires** and whether a 2028 refi or extension is available; (2) **the exit cap rate**; (3) **rent growth**. None of the three is disclosed.

| Case | Gross deal IRR (🔴 assumed) | Net LP IRR, promote only (disclosed fees = 0) | Promote drag |
|---|---|---|---|
| Bull | 20% | 12.58% | 742 bps/yr |
| Base | 15% | 9.02% | 598 bps/yr |
| Bear | 10% | 6.56% | 344 bps/yr |

Every case is **before** any acquisition, asset-management, disposition or admin fee, because none was disclosed. Adding the `02` typical stack (2% acquisition, 1.5% annual asset management, 1% disposition, 0.3% admin, all 🔴 assumed) to the 15% base case takes net LP IRR to **6.79%** (821 bps/yr total drag).

**Against the `05` comparator** (benchmark_comparator.py, multifamily equity, VNQ 4.92% 10-year, 7-year lock-up, illiquidity hurdle about 400–600 bps):
- 9.02% net (promote only): about **410 bps** over VNQ, which **clears, but thinly**, in the lower half of the hurdle band.
- 6.79% net (promote plus typical fees): about **187 bps** over VNQ, which is **thin and fails** the illiquidity hurdle. It is only about 160 bps over the 10-year Treasury (5.18%, `05`), a risk-free, liquid floor.
- 6.56% net (bear, promote only): it also **fails** the hurdle.

**What this means:** with a 50% promote, a deal has to perform at a strong value-add level just to give you a return that pays for the lock-up. If it does a little worse, you are left with a REIT-like return in a single illiquid asset. The bear case here also leaves out any debt-service shock after the cap expires (see §5, GEN-10). That shock is the most likely way the real bear case ends up below these numbers.

Both `05` amplifiers raise the premium you should demand here. **Concentration:** one asset against VNQ's basket of hundreds. **Dispersion:** the median outcome sits well below the marketed figure.

---

## 3. Where LP Returns Come From

**Can't tell from this, and that is a finding.** The split between cash flow, exit and leverage is not disclosed. Four facts point to a return driven by financing and the exit, not by operations:
- **Floating-rate debt with a short cap** 🟢. In-place cash flow depends on where rates sit after the cap expires, so the income leg is not secure.
- **Upside-only projections** 🟢. A bull case is usually where cap-rate compression and rent growth do most of the work.
- **Loan maturity in 2028** 🟢. Capital most likely comes back through a refi or sale in about two years, not through accumulated cash flow 🟡.
- **The `05` unlevered overlay.** Institutional residential real estate returned 5.3% in 2025 (NCREIF NPI, almost all income). Any levered upside-case IRR well above that comes mostly from leverage and assumed appreciation.

Treat **GEN-07** (financing story) and **GEN-08** (exit-dependent IRR) as **open, not fired**. **EQUITY-06** (exit cap below going-in) is also open because the exit cap is not disclosed. All three go to must-asks Q-DS-01, Q-DS-02 and Q-EXIT-01 in §8. If the IRR split shows that more than 60% comes from the exit, or that the exit cap sits below the going-in cap, this becomes a named financing story.

---

## 4. Fee Stack Summary

| Layer | Disclosed? | Note |
|---|---|---|
| Promote | **50%** 🟢 | `02` says above 30% is aggressive. This is about 1.7× that line |
| Preferred return | Not stated | Required to price the promote (EQUITY-04 open) |
| Catch-up | Not stated | 100% would push the GP's economics forward (EQUITY-03 open) |
| Clawback | **None** 🟢 | Combined with American and 50%, this fires EQUITY-02 |
| Acquisition fee | Not stated | `02` norm: 1–2% of equity |
| Asset management fee | Not stated | `02` norm: 1–2% of equity per year |
| Disposition fee | Not stated | `02` norm: 0.5–1% of sale price |
| Loan placement / refi fee | Not stated | Relevant because a 2028 refi looks likely (0.5–1.5% per event) |
| Admin / IR | Not stated | `02` norm: 0.1–0.5% per year |
| Affiliate fees (property management, construction) | Not stated | GEN-06 open |

**Gross-to-net drag: at least about 598 bps/yr from the promote alone** (15% gross, 7-year hold, 8% pref, 100% catch-up, all 🔴 assumed; disclosed fees entered as 0). With the `02` typical fee stack it is **about 821 bps/yr**. The gap between those two numbers is the finding: **the total drag cannot be computed from what was disclosed** (GEN-16). Every input except the 50% promote is assumed (see §6).

A 50% promote means the GP keeps half of the profit above the pref. With a 100% catch-up, the calculator shows the GP still ends up with 50% of **total** profit. Compare that with about 20% in the `02` worked example.

---

## 5. Red Flags

**RED**
- **GEN-01: zero GP co-investment** 🟢. The sponsor earns fees and a 50% promote with none of its own capital at risk, so its upside is uncapped and its downside is nil. "Our expertise is our investment" is almost word for word the bad-answer signal in Q-GP-01.
- **GEN-02: prior regulatory action** 🟢. One principal was named in an SEC action, which points to a past pattern of investor harm or compliance failure. Until you have read the order itself, assume it is relevant to how this deal is run.
- **GEN-10: rate cap expires before maturity** 🟢. The cap expires around Nov 2027 and the loan matures in 2028, so you are fully exposed to floating rates for roughly 2–14 months, depending on the maturity month (not stated). This is the 2022–24 pattern: the cap expires, rates stay high, debt service jumps, distributions stop, and a capital call or forced sale follows. That happens exactly as the 2028 maturity needs a refi.
- **GEN-09: debt maturity inside the business-plan horizon** 🟡 (inferred). The hold is not stated, but `01` puts multifamily holds at 5–7 years (value-add) or 7–10 (core), and the loan comes due in 2028, about 2 years from now. You are pushed into a refi or sale in whatever market exists then, without a cap. The related refi-dependent plan, **EQUITY-07**, also fires (YELLOW–RED, 🟡).
- **EQUITY-01 + EQUITY-02: American waterfall, high promote, no clawback** 🟢. `03` treats this combination as RED. In a single-asset deal, the practical risk is the GP taking its 50% on interim cash flow or a refi-out before you have your capital and pref back. If a later sale disappoints, nothing makes the GP return it.
- **GEN-14: unrealized-only track record** 🟢. Marks are self-reported and the GP hasn't shown it can exit and return capital. Under skepticism rule 5, this counts as **no track record**. If the marks also turn out to be project- or GP-level IRR, **GEN-05** completes the RED cluster `03` describes (open until Q-GP-02 is answered).

**YELLOW–RED** (treat as RED until answered)
- **GEN-16: fee and waterfall terms only partly disclosed.** No fee schedule, pref, catch-up or tiers, so net-to-LP can't be computed.
- **GEN-15: financials missing.** No rent roll, T-12 or full debt terms (LTV, spread, extensions).

**YELLOW**
- **GEN-13: no downside case** 🟢. You were shown only an upside case, which is weaker than a single-point pro forma and gives no sense of how fragile the deal is. Related: **GEN-03** (marketing-heavy, light on substance) 🟡.
- **GEN-11: no distribution schedule** 🟢. You can't tell whether capital comes back over the hold or only at the 2028 refi or sale.
- **GEN-17: category disclosures missing.** These are the multifamily essentials from `01` (see §6).

**Open (not fired; the facts aren't disclosed):** GEN-07, GEN-08, EQUITY-06 (financing-story family), EQUITY-03 (catch-up), EQUITY-04 / EQUITY-05 (pref level and type), GEN-06 (affiliate fees), GEN-18 (submarket rent growth).

**Clusters**
- **Alignment cluster.** GEN-01, GEN-02, EQUITY-01 / EQUITY-02 and GEN-14 together describe a sponsor with no capital at risk, an enforcement history, a promote it keeps no matter what, and no realized results. Each is RED on its own, and they reinforce each other.
- **Debt cluster.** GEN-10, GEN-09 and EQUITY-07 are the connected rate-cap-expiry and frozen-refi failure described in `03`.
- **Possible financing story.** GEN-07, GEN-08 and EQUITY-06 are unresolved, but every disclosed fact leans that way.

---

## 6. Missing Disclosures

Measured against the `01` multifamily essentials and the `02` equity-syndication fee inventory:

- **Return figures:** gross IRR, net-to-LP IRR, equity multiple, cash-on-cash. None given. The scripts ran on the ASSUMED defaults of 15% gross, 7-year hold, 8% pref and 100% catch-up.
- **Base and bear cases** with exit-cap and rent-growth sensitivity (GEN-13).
- **Going-in cap and exit cap** (EQUITY-06 open).
- **Rent roll and T-12 actuals**, not just T-3 or T-6 (GEN-15, GEN-12 if short windows turn up).
- **Full debt terms:** lender, LTV, index plus spread, cap strike, cost to replace the cap, maturity month, extension options and their conditions (DSCR or debt-yield tests), amortization, prepayment.
- **Refi assumptions** for 2028 (EQUITY-07).
- **Hold period** (GEN-09 is inferred until it is stated).
- **Preferred return:** rate, cumulative or not, simple or compounding (EQUITY-04, EQUITY-05). **Catch-up rate** (EQUITY-03). **Split tiers.**
- **Full fee schedule:** acquisition, asset management, disposition, loan placement or refi, admin. All were entered as 0 or ASSUMED in §4 (GEN-16).
- **Affiliate service providers** and their fees (GEN-06).
- **Distribution schedule** (GEN-11).
- **Track record on prior multifamily exits.** `01` names this an essential disclosure, and there are none (GEN-14).
- **The SEC action:** which principal, the allegations, the outcome, and any sanctions or undertakings (GEN-02).
- **Market, submarket, asset vintage and unit count, business plan** (GEN-18 open).
- **Minimum investment, raise size, capital-call provisions, LP liquidity terms.**

---

## 7. GP Alignment

- **Co-invest: none** 🟢. No cash and no pari-passu stake. The only alignment is the promote, which pays out when things go well and costs the GP nothing when they don't.
- **Track record: unverified** 🟢. It is all current, unrealized marks. Realized net-to-LP results: **none**. It isn't stated whether the marks are net-to-LP or project-level (GEN-05 open).
- **Waterfall alignment: poor** 🟢. A 50% promote, American, with no clawback. The pref and catch-up that would protect you are undisclosed.
- **Affiliate fees: unknown.** GEN-06 open.
- **Conduct: prior SEC action** 🟢. It is unverified whether it was resolved and how.

Net read: nothing in the structure forces the GP's outcome to track yours. The alignment is only asserted.

---

## 8. Questions for the GP

**Must-ask** (each `03` flag that fired routes here)

| ID | Question | Bad-answer signal (the specific dodge) | Flag |
|---|---|---|---|
| Q-GP-03 | "Have you or your principals faced any regulatory action, enforcement, or investor litigation?" Ask for the SEC order or settlement document itself. | Deflects to "nothing material"; blames the regulator; your own search turns up more than they disclosed. | GEN-02 |
| Q-GP-01 | "How much of your own capital is in this deal, on the same terms as LPs?" | "Our sweat equity is our investment." **You've already heard this answer.** Other versions: co-invest offered as a fee waiver, or a token amount on better terms. | GEN-01 |
| Q-GP-02 | "Can you restate your track record as net-to-LP IRR on fully-realized, exited deals only?" | Offers only project-level or GP-level IRR; "most deals are still performing"; can't separate realized from unrealized. | GEN-14, GEN-05 |
| Q-RISK-02 | "When does the rate cap expire relative to debt maturity, and what's the cost to extend it at current pricing?" | Cap expires before maturity (**already true**); extension cost not modeled; "rates should be lower by then." | GEN-10 |
| Q-RISK-01 | "When does the debt mature relative to the projected hold, and what's the refinance or extension plan?" | Maturity falls inside the hold; "we'll refinance" with no terms; no plan if the refi market shuts. | GEN-09 |
| Q-EXIT-02 | "Does the business plan depend on a refinance, and what happens to distributions if the refi isn't available on the assumed terms?" | Capital return needs a refi at lower rates; no fallback; "the refi market will reopen." | EQUITY-07 |
| Q-FEE-03 | "Is the waterfall deal-by-deal or whole-of-fund, and is there a clawback?" Ask too why the promote is 50%, and whether any promote is paid on interim or refi distributions before LP capital and pref are returned. | Deal-by-deal with a high promote and no clawback (**already true**); can't explain the catch-up; "you get paid when we get paid." | EQUITY-01, EQUITY-02 |
| Q-FEE-04 | "What preferred return do LPs receive before the GP earns promote, and is it cumulative and compounding?" | Pref below 6% or absent; non-cumulative. | EQUITY-04, EQUITY-05 (also EQUITY-03: ask the catch-up rate) |
| Q-FEE-01 | "Can you provide the complete fee schedule and the full distribution waterfall?" | "Standard market fees"; a partial list; "the PPM has it" without producing it. | GEN-16 |
| Q-FEE-02 | "Which service providers are GP-affiliated, what do they charge, and are those rates third-party-benchmarked?" | "All arm's-length" without naming providers; no benchmark offered. | GEN-06 |
| Q-DS-03 | "What is the return under a bear case — flat rents, higher exit cap, no refinance?" | A single-point pro forma with no downside (**already true: upside only**); "we underwrite conservatively" with nothing to show. | GEN-13 |
| Q-DS-01 | "What share of projected LP IRR comes from in-place cash flow versus the exit, and what's the IRR at a flat exit cap?" | Can't or won't break down the IRR; "real estate always appreciates"; the IRR falls below the pref at a flat exit cap. | GEN-08, EQUITY-06 |
| Q-DS-02 | "Strip out leverage and cap-rate compression — what is the unlevered, in-place return?" | Treats the levered IRR as the only figure that matters; "leverage is just how the deal works." | GEN-07 |
| Q-EXIT-01 | "Why is the exit cap below the going-in cap, and what's the IRR at an exit cap equal to or above going-in?" | "Cap rates will compress"; the IRR breaks at a flat exit cap; no sensitivity offered. | EQUITY-06 |
| Q-RISK-03 | "Can you provide trailing-twelve-month actuals, the rent roll, and complete debt terms?" | T-3 or T-6 only; rent roll withheld; "the financials are confidential until you commit." | GEN-15, GEN-12 |
| Q-DIST-01 | "What is the projected distribution schedule, and at what milestones does LP capital start returning?" | "We'll distribute when the deal supports it"; no milestones. | GEN-11 |
| Q-MKT-01 | "What submarket supply pipeline and absorption data support the rent-growth assumption?" | Metro-level optimism instead of submarket data; no supply pipeline mentioned. | GEN-18 |
| Q-LIQ-01 | "What are my options if I need to exit before the hold period ends?" | "A secondary market may develop"; "we'll try to accommodate." | — |

**Nice-to-ask**

| ID | Question | Bad-answer signal | Flag |
|---|---|---|---|
| Q-DIST-02 | "When are capital calls expected, and what's the consequence of a missed or late call?" Ask this one before anything else on the list, because a capital call after the cap expires is a real possibility here. | "Calls as needed" with no notice period; punitive dilution buried in the documents. | — |
| Q-GP-04 | "How have your headcount and deal-monitoring capacity grown alongside AUM?" | AUM grew while the team stayed flat; no named asset manager. | GEN-04 (not fired) |
| Q-LIQ-02 | "When will K-1s be delivered each year, and have you historically delivered them before the filing deadline?" | "As soon as we can"; a history of extensions. | — |

---

## 9. Diligence Checklist

These need third-party verification. Don't rely on the GP's word for any of them.

- **Regulatory and background:** look up the principal on SEC enforcement records (litigation releases, administrative proceedings), FINRA BrokerCheck, the SEC IAPD and state securities regulators. Run court and litigation searches on every principal and the sponsor entity. Read the actual order, not a summary.
- **PPM and operating agreement:** confirm the waterfall, pref, catch-up, promote base, the lack of clawback, every fee, capital-call and dilution terms, and the GP removal and key-person provisions.
- **Loan documents and lender:** the cap's strike and expiry, the cap-reserve or cap-replacement covenant, extension conditions, maturity date, any recourse or carve-out guarantor, and whether a reserve for buying a new cap is funded.
- **Third-party financials:** a rent roll reconciled to bank deposits, T-12 actuals, and the property tax and insurance reassessment after acquisition.
- **Appraisal and comps:** an independent valuation and the going-in cap against submarket sales comps, plus a rent comp survey.
- **Track record:** for each prior deal, the deal-level documents and LP distribution statements, to separate realized from marked.
- **Your own counsel and tax adviser** before you commit any money.

---

## 10. Verdict

**PASS**

*Screening output only, not investment advice.*

**Reasoning.** This is a **merits Pass**, not "Pass as presented: insufficient disclosure." The deal does withhold most of the return story, but the disqualifying problems are terms that were disclosed (🟢), and more information wouldn't change them:
1. **No GP capital** (GEN-01) plus a **50% promote** (well above `02`'s 30% "aggressive" line) in an **American waterfall with no clawback** (EQUITY-01, EQUITY-02). Under the illustrative assumptions, the promote alone takes about 600 bps a year from you, and the GP risks nothing to earn it.
2. **A prior SEC action** involving a principal (GEN-02), together with a **record that is entirely unrealized** (GEN-14). You have no verified evidence that this team has ever returned capital to LPs.
3. **A rate cap that expires before a 2028 maturity** (GEN-10, GEN-09 🟡, EQUITY-07 🟡) on a **single asset**: the exact debt setup that led to 2022–24 multifamily capital calls and wipeouts.
4. **Upside-only projections** (GEN-13) with no fees, pref, IRR or debt terms disclosed (GEN-16, GEN-15). You can't stress-test it.

**Biggest swing factor:** debt service after the cap expires and whether a 2028 refi is possible. That combination decides whether you get distributions, face a capital call, or lose principal, and the sponsor has no capital in the deal to absorb the hit.

**Who it suits:** a passive LP shouldn't take this as offered. The structure puts the downside on LPs and gives half the upside to an unaligned GP with an enforcement history.

**What would have to be true to re-screen** (all of these, not just some):
- The SEC matter is fully disclosed and, after counsel reviews the order, judged unrelated to investor harm or long resolved with no repeat.
- The GP puts meaningful **cash** in on pari-passu terms.
- The promote comes down to the `02` range (15–30%) above a **cumulative pref of at least 6%**, with a clawback or a ban on promote from interim or refi distributions until your capital and pref are returned.
- The rate cap is extended or bought to cover through maturity (or a funded replacement reserve exists), and there is a documented 2028 extension or refi plan that a lender's term sheet supports.
- Base and bear cases are provided, with the full fee schedule, T-12, rent roll and debt terms, and net-to-LP clears the `05` hurdle (about 400–600 bps over VNQ for a 7-year lock-up) **in the base case**.
- At least some **realized**, net-to-LP exits can be verified from distribution records.

Even if all of that came through, a single asset still carries concentration risk that the VNQ comparison doesn't capture. Ask for a premium toward the top of the hurdle band, not the bottom.
