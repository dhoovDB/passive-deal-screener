# Eval fixture 02

*Iteration-7 run, 2026-11-01, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 181fdd7.*

# Deal Screen: "Exclusive preferred-equity opportunity" (multifamily, 10% pref)

**Verdict: Pass as presented — insufficient disclosure.**
*Screening output only, not investment advice.*

The email gives you a coupon and a minimum. That's all. There is no sponsor track record, no property, no capital stack, no fee schedule, no term, no say on whether the pref is paid in cash or just accrued, and no documents. What it does include is urgency ("exclusive," "limited allocation remaining") and wire instructions. A 10% pref is a normal number for preferred equity. The problem is that nothing in the email lets you check whether this 10% is safe. **Do not wire anything.** Ask for the documents listed in §10. If they come back clean, run this screen again.

---

## 1. Deal Snapshot

| Field | Value | Confidence |
|---|---|---|
| Asset class | Multifamily. Core, core-plus or value-add **not stated** | 🟢 stated / 🔴 sub-class unknown |
| Deal type | Preferred equity | 🟢 stated |
| Sponsor | **Not stated** (no name, entity or track record in the email) | 🟢 absence |
| Geography / property | **Not stated** (no market, address, unit count or vintage) | 🟢 absence |
| Minimum | $25,000 | 🟢 stated |
| Hold / term / redemption date | **Not stated** | 🟢 absence |
| Raise size / pref tranche size | **Not stated** | 🟢 absence |
| Claimed return | "10% preferred return". Net or gross, current-pay or accrued, cumulative or not, and simple or compounding are all **not stated** | 🟢 stated / 🔴 terms unknown |
| Capital stack position | **Not stated** (senior loan size, rate, maturity; how much common equity sits beneath the pref) | 🟢 absence |
| Fees | **Not stated** | 🟢 absence |
| Equity kicker / participation | **Not stated** | 🟢 absence |
| Offering documents | None. Only "wire instructions attached" | 🟢 stated |

Every "Not stated" row feeds §6.

---

## 2. Return Stress-Test

A preferred-equity return is a contractual coupon with capped upside, not an equity-style IRR (`05` → PFF note). The upside is fixed at the coupon, so the stress-test only asks whether the coupon gets paid and whether your capital comes back.

**Swing assumptions (all undisclosed):**
1. **Current-pay vs accrued.** If the 10% is paid in cash each quarter, part of your return arrives while you hold. If it accrues, every dollar of return waits on a redemption event.
2. **Redemption / take-out.** The sponsor usually pays off the pref out of a refinance or sale. Whether that money exists at maturity decides whether you get your principal back (`EQUITY-07`, `GEN-09`).
3. **Attachment point.** How much senior debt sits ahead of you and how much common equity sits beneath you. This sets how far the property's value can fall before your principal is impaired. The email gives no figures.

| Case | What has to be true | LP outcome |
|---|---|---|
| **Bull** | 10% paid in cash as stated, no fees, redeemed at par on schedule. Possibly an undisclosed kicker | ≈10% net. Capped, since a pref doesn't share in the upside 🔴 |
| **Base** | 10% accrues or is paid, but there are fees typical for pref equity (`02`) | Net below 10%. Illustrative run below: ≈8.4% 🔴 |
| **Bear** | Cash flow can't cover senior debt service plus the pref, and the refi or sale at maturity falls short (the 2022–24 frozen-refi pattern) | Pref accrues unpaid, redemption is delayed, principal is impaired if the senior lender forecloses. Not quantifiable without the capital stack 🔴 |

**Benchmark (`scripts/benchmark_comparator.py`, comparator PFF 3.00% 10yr, `05`):**

| Scenario | Net to LP | Lock-up | Premium over PFF | Hurdle | Read |
|---|---|---|---|---|---|
| Headline taken at face value | 10.00% 🔴 (assumes headline = net) | 3 yr / 5 yr / 7 yr 🔴 (term not stated) | ≈700 bps | ~300–400 / ~300–400 / ~400–600 bps | Clears comfortably at every tested term |
| Illustrative typical pref fees (see §4) | 8.40% 🔴 | 7 yr 🔴 | ≈540 bps | ~400–600 bps | Clears, but thin: lower half of the hurdle band |

- **The duration-matched Treasury is the tighter floor** (`05`): the 2yr is ≈4.87% and the 10yr ≈5.18%. A 10% net pref is ≈480–510 bps over risk-free, and ≈320–350 bps at 8.4%. That cushion is your whole pay for subordination, single-asset concentration and illiquidity.
- **Read:** the headline number would clear the hurdle *if* it is net, paid and reliably redeemed. Those are the three things the email doesn't establish. The pass on the benchmark rests on 🔴 assumptions and can't support a decision. Per `05`, beating the spread is necessary, not sufficient.

---

## 3. Where LP Returns Come From

- **In principle:** a pref's return is the coupon, paid out of property cash flow after senior debt service, plus return of principal at redemption. There is no appreciation upside unless a kicker exists.
- **In this deal:** **can't tell from this.** If the 10% accrues instead of being paid in cash, 100% of your return depends on a refinance or sale at maturity. That is the exit-dependent shape (`GEN-08`) and the refi-dependent shape (`EQUITY-07`), at their extreme. If it's current-pay, much less of it does.
- **Leverage:** a pref sits on top of a senior loan. Your safety depends on combined leverage through the pref (senior loan plus pref as a share of property value) and on the senior loan's maturity and rate-cap terms (`GEN-09`, `GEN-10`). None of this is disclosed. Whether the property's in-place cash flow alone covers debt service plus the pref (`GEN-07`, unlevered view) can't be assessed.
- None of these flags fire, because firing them would require 🔴 assumptions. They are routed to must-asks (Q-DIST-01, Q-EXIT-02, Q-RISK-01, Q-RISK-02, Q-DS-01, Q-DS-02).

---

## 4. Fee Stack Summary

**Gross-to-net drag: not computable from disclosure. That is the finding (`GEN-16`).**

What preferred-equity deals normally charge (`02` → Preferred equity), against what this deal disclosed:

| Fee | Typical range (`02`) | Aggressive threshold | This deal |
|---|---|---|---|
| Origination / placement ("structuring") | 1–2%, one-time | >3% | Not stated |
| Servicing / admin | 0.5–1% annual | >1.5% | Not stated |
| Equity kicker / participation | 5–20% above pref | >25% | Not stated |
| Exit / maturity fee | 0.5–1%, one-time | >2% | Not stated |
| Promote / catch-up above the pref | Rare in true pref (`PREF-01`) | Any (equity risk dressed as pref) | Not stated |
| Feeder / fund-of-funds wrapper | +50–150 bps/yr if present | — | Unknown (email blast; vehicle not identified) |

**`scripts/fee_drag_calculator.py` runs:**
- **As disclosed** (gross 10%, every fee passed as `0`, no carry, hold 5 yr ASSUMED): net 10.00%, **0 bps/yr drag.** That reflects missing disclosure, not low fees. Every input except the 10% is an assumption (§6).
- **Illustrative, 🔴 assumed** (top of the `02` typical ranges: 2% origination, 1% exit fee, 1% annual servicing, no promote, 5-yr hold): net **8.40%**, **≈160 bps/yr drag** (100 bps recurring, 60 bps one-time).

The ≈160 bps gap between these two runs is roughly how much the headline can overstate your take with no fee in the stack above its typical range. The real figure is unknown until Q-FEE-01 is answered.

---

## 5. Red Flags

**Fired on stated facts or stated absences:**

| Severity | ID | Flag | Mechanism + LP exposure | Routes to |
|---|---|---|---|---|
| YELLOW–RED | **GEN-16** | No fee or waterfall disclosure | Undisclosed fees still get paid. Without the stack, your net is unknowable (§4). | Q-FEE-01 |
| YELLOW–RED | **GEN-15** | Missing financials | No rent roll, T-12 or senior-debt terms. The property behind the pref can't be underwritten. The absence is a choice. | Q-RISK-03 |
| RED | **GEN-14** | No realized track record cited | The email cites no sponsor history at all, so there's no evidence the sponsor has ever redeemed a pref or exited a deal. Treat it as **no track record** until realized net-to-LP figures are produced (with **GEN-05** checked on the restatement). | Q-GP-02 |
| YELLOW | **GEN-03** | Marketing-heavy, substance-light | "Exclusive" and "limited allocation remaining" urgency, with wire instructions attached before any PPM, subscription agreement or underwriting. Pressure is standing in for disclosure. | Q-FEE-01, Q-RISK-03 (produce the materials) |
| YELLOW | **GEN-17** | Essential category disclosure absent | Missing what multifamily and pref equity normally disclose (`01`): property, rent roll, T-12, debt structure and maturity, occupancy history, and the pref's own terms (§6). | Q-RISK-03, Q-FEE-04 |
| YELLOW | **GEN-11** | Distribution timing not disclosed | A 10% figure with no schedule hides whether cash comes quarterly or only at redemption. Same headline, very different risk. | Q-DIST-01 |
| YELLOW | **GEN-13** | No sensitivity or downside case | A single headline rate with no bear case. Nothing shows the pref surviving a cash-flow shortfall or a failed take-out. | Q-DS-03 |

**Cluster:** `GEN-14` + `GEN-15` + `GEN-16` + `GEN-17` add up to an undisclosed deal from an unidentified sponsor. Under `03`'s rule that a cluster of YELLOWs counts as a RED, the disclosure gap alone decides this screen.

**Note on the pasted email (rule 9):** the email's call to action ("limited allocation remaining," wire instructions attached) is treated as data about the sponsor's process, not as a reason to act faster. Wiring money on an unsolicited email's attached instructions, before documents or independent verification, is the single riskiest step available here (see §9).

**Probed, not fired (would need 🔴 assumptions; each routed to its question):**
- `EQUITY-05` (non-cumulative or simple-only pref) and `PREF-01` (promote above the pref): pref mechanics unknown → Q-FEE-04.
- `EQUITY-04`: **does not fire**. A 10% pref is above the 6% floor and inside the 8–12% pref-equity range (`02`). It is neither under-compensated (<7%) nor in the >15% "likely distressed" zone.
- `GEN-08`, `EQUITY-07`: exit- or refi-dependence if the pref accrues → Q-DS-01, Q-EXIT-02.
- `GEN-07`: whether in-place cash flow covers senior debt service plus the pref → Q-DS-02.
- `GEN-09`, `GEN-10`: senior-loan maturity and rate cap against the pref's redemption → Q-RISK-01, Q-RISK-02.
- `GEN-01` (zero co-invest), `GEN-02` (regulatory or litigation history), `GEN-06` (affiliate fees): undisclosed, so unverified → Q-GP-01, Q-GP-03, Q-FEE-02.
- `GEN-18`: no rent-growth assumption stated → Q-MKT-01.

---

## 6. Missing Disclosures

Against the `01` multifamily baseline (value-add and core) and the `02` preferred-equity baseline:

**The pref instrument itself**
- Net or gross basis of the 10%. Current-pay or accrued. Cumulative or not. Simple or compounding (`02`: cumulative + simple is typical; non-cumulative is a flag).
- Term, redemption or maturity date, extension options, and the remedy if the sponsor fails to redeem (control rights, conversion, removal of the GP).
- Any kicker or participation, and any promote or catch-up above the pref.
- Tranche size and the capital stack: senior loan amount and terms, common equity beneath you, combined leverage through the pref.

**The property** (`01` → Multifamily)
- Name, market, submarket, unit count, vintage, and the business plan (core vs value-add).
- Rent roll and **T-12 actuals** (not T-3 or T-6); occupancy history (5+ years for core).
- Debt structure: rate, fixed or floating, rate-cap expiry, amortization, maturity, prepayment.
- Exit or refi assumptions behind the redemption, with sensitivity.

**Fees** (`02`): origination, servicing, exit or maturity fee, admin, any affiliate fees, and any feeder-vehicle layer.

**Sponsor:** legal entity, principals, **realized** track record (prior pref redemptions and multifamily exits, net to LP), co-invest.

**Process and liquidity:** PPM and subscription agreement, offering exemption (Reg D 506(b) vs 506(c), accreditation verification), K-1 timing, transfer and early-exit rights.

**Assumed inputs used in this screen (each is a gap above):** hold 3, 5 or 7 yr; 10% treated as net; all fees `0` in the as-disclosed run; illustrative fees of 2% / 1% / 1% per year in the sensitivity run.

---

## 7. GP Alignment

- **Co-invest:** not stated. Unverified (`GEN-01` probe, Q-GP-01).
- **Realized track record:** none cited. **Unverified. Treat it as no track record** (`GEN-14`; `GEN-05` applies to whatever figures are produced).
- **Waterfall alignment:** a true pref has no promote. Whether this one has a promote or catch-up above the 10% is unknown (`PREF-01`, Q-FEE-04). If it does, you're carrying equity risk at a capped return.
- **Affiliate fees:** unknown (`GEN-06`, Q-FEE-02).
- **Sponsor identity and conduct:** the sponsor isn't identified in the email, so no background check is possible yet (Q-GP-03).
- **Process signal:** urgency plus wire instructions ahead of documents (`GEN-03`). A sponsor who is aligned with LPs sends the PPM before asking for money.

---

## 8. Questions for the GP

**Must-ask**

| ID | Question | Bad-answer signal | Flag |
|---|---|---|---|
| Q-FEE-01 | "Can you provide the complete fee schedule and the full distribution waterfall?" | "Standard market fees"; a partial list; "the PPM has it" without producing it; fees surface only after you commit. | GEN-16 |
| Q-FEE-04 | "What preferred return do LPs receive before the GP earns promote, and is it cumulative and compounding?" | Non-cumulative; no answer on cumulative vs simple; a promote above the pref (turning it into common-equity risk). | EQUITY-04, EQUITY-05, PREF-01 |
| Q-RISK-03 | "Can you provide trailing-twelve-month actuals, the rent roll, and complete debt terms?" | T-3/T-6 only; rent roll withheld; "the financials are confidential until you commit." | GEN-12, GEN-15 |
| Q-DIST-01 | "What is the projected distribution schedule, and at what milestones does LP capital start returning?" | "We'll distribute when the deal supports it"; the 10% quoted with no timing; silence. | GEN-11 |
| Q-EXIT-02 | "Does the business plan depend on a refinance, and what happens to distributions if the refi isn't available on the assumed terms?" | Redemption requires a refi at lower rates; no fallback; "the refi market will reopen." | EQUITY-07 |
| Q-RISK-01 | "When does the debt mature relative to the projected hold, and what's the refinance or extension plan?" | Senior maturity falls before the pref's redemption; "we'll refinance" with no terms. | GEN-09 |
| Q-RISK-02 | "When does the rate cap expire relative to debt maturity, and what's the cost to extend it at current pricing?" | Cap expires before maturity; extension cost not modeled; "rates should be lower by then." | GEN-10 |
| Q-DS-01 | "What share of projected LP IRR comes from in-place cash flow versus the exit, and what's the IRR at a flat exit cap?" | Can't decompose it; the pref is fully accrued to redemption; "real estate always appreciates." | GEN-08, EQUITY-06 |
| Q-DS-02 | "Strip out leverage and cap-rate compression — what is the unlevered, in-place return?" | No unlevered view; in-place NOI doesn't cover senior debt service plus the pref; "leverage is just how the deal works." | GEN-07 |
| Q-DS-03 | "What is the return under a bear case — flat rents, higher exit cap, no refinance?" | No downside case; "we underwrite conservatively" with nothing to show; the bear case still pays 10%. | GEN-13 |
| Q-GP-02 | "Can you restate your track record as net-to-LP IRR on fully-realized, exited deals only?" | Only project- or GP-level IRR; "most deals are still performing"; can't separate realized from marked. | GEN-05, GEN-14 |
| Q-GP-01 | "How much of your own capital is in this deal, on the same terms as LPs?" | "Our sweat equity is our investment"; co-invest via fee waiver; a token amount on better terms. | GEN-01 |
| Q-GP-03 | "Have you or your principals faced any regulatory action, enforcement, or investor litigation?" | "Nothing material"; blames the LP or regulator; a search turns up something undisclosed. | GEN-02 |
| Q-FEE-02 | "Which service providers are GP-affiliated, what do they charge, and are those rates third-party-benchmarked?" | "All arm's-length" without naming providers; affiliate fees undisclosed. | GEN-06 |
| Q-MKT-01 | "What submarket supply pipeline and absorption data support the rent-growth assumption?" | Metro-level optimism in place of submarket data; no supply pipeline acknowledged. | GEN-18 |
| Q-LIQ-01 | "What are my options if I need to exit before the hold period ends?" | "A secondary market may develop"; "we'll try to accommodate." (An honest "none" is a good answer.) | — |

**Nice-to-ask**

| ID | Question | Bad-answer signal | Flag |
|---|---|---|---|
| Q-DIST-02 | "When are capital calls expected, and what's the consequence of a missed or late call?" | "Calls as needed"; punitive dilution buried in the documents. | — |
| Q-LIQ-02 | "When will K-1s be delivered each year, and have you historically delivered them before the filing deadline?" | "As soon as we can"; a history of extensions. | — |
| Q-GP-04 | "How have your headcount and deal-monitoring capacity grown alongside AUM?" | AUM multiplied while the team stayed flat; no named asset manager. | GEN-04 |

---

## 9. Diligence Checklist

- [ ] **Verify the sender before anything else.** Confirm the sponsor's identity and the wire instructions by phone, using a number you find yourself (not one from the email). **Never wire on emailed instructions alone**, and never before the documents below are signed.
- [ ] Get and read the **PPM, operating agreement and subscription agreement**. Confirm the pref's terms, redemption rights and remedies in writing.
- [ ] Get the **senior loan documents** or a term sheet: amount, rate, cap expiry, maturity, and whether the lender consents to the pref (intercreditor agreement).
- [ ] **Background and regulatory check** on the sponsor entity and its principals: SEC EDGAR (Form D filing), FINRA BrokerCheck, state securities regulator, and court and litigation searches.
- [ ] Confirm the **offering exemption** and how accreditation is verified.
- [ ] Get a **third-party appraisal or rent and sales comps** to set combined leverage through the pref.
- [ ] Get **T-12 and rent roll**, ideally reconciled to bank statements or audited financials.
- [ ] Ask for **references from LPs on prior deals that were redeemed or exited**, not ones still running.
- [ ] Have counsel or a tax advisor review the documents before you commit.

---

## 10. Verdict

**Pass as presented — insufficient disclosure.**
*Screening output only, not investment advice.*

**Reasoning.** Preferred equity is screened on three things: the pref's terms, the capital stack it sits in, and whether the sponsor can redeem it. The email discloses none of the three. The 10% headline is in range for pref equity (`02`: 8–12%), and taken at face value it beats PFF by ≈700 bps. That pass depends entirely on 🔴 assumptions: that the 10% is net, that it's paid, and that a redemption actually happens. With realistic fees it falls toward ≈8.4%, a thin clear for a 7-year lock-up. What actually fires is a cluster of disclosure gaps (`GEN-14`, `GEN-15`, `GEN-16`, `GEN-17`) plus urgency standing in for diligence (`GEN-03`), with wire instructions attached.

**Biggest swing factor:** the capital stack and the take-out. How much senior debt sits ahead of the pref, when it matures, and whether a refinance or sale at that point can repay you. This decides whether 10% is a well-secured coupon or an unsecured bet on the refi market.

**Who it could suit (if re-screened clean):** an income-focused LP who accepts capped upside, a multi-year lock-up with no liquidity, and single-asset concentration, in exchange for priority over common equity.

**What would have to be true for "Pursue" (the re-screen list):**
1. An identified sponsor with a **realized**, net-to-LP track record, including prior prefs redeemed on time (Q-GP-02) and a clean regulatory and litigation search (Q-GP-03).
2. The pref is **cumulative**, with no promote above it, and current-pay or with a clear accrual schedule (Q-FEE-04, Q-DIST-01).
3. A full **fee schedule**, so the net-to-LP figure is computable and still clears PFF plus the illiquidity hurdle for the stated term (Q-FEE-01, re-run both scripts).
4. **Senior-debt terms** where maturity and any rate cap run past the pref's redemption date, with a redemption path that doesn't need a refi at lower rates (Q-RISK-01, Q-RISK-02, Q-EXIT-02).
5. **T-12 and rent roll** showing in-place NOI covers senior debt service plus the pref with room to spare (Q-RISK-03, Q-DS-02), plus a bear case in which your principal survives (Q-DS-03).
6. A **PPM and subscription documents** in hand, and wire instructions verified independently, before any money moves.
