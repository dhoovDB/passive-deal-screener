# Eval fixture 02 — Preferred-equity email solicitation
*Iteration-4 run, 2026-09-27, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 1c7faff.*

**Verdict: Pass as presented — insufficient disclosure. Do not wire anything.** The email gives three facts: a 10% preferred return, multifamily, and a $25k minimum. That is too little to underwrite the core return story, because nothing tells you where the pref sits in the capital stack, what senior debt is ahead of it, or whether the 10% is actually paid or only accrues. The 10% headline is within normal range and would clear the public benchmark with room to spare *if* it is real (see §2). That makes it worth re-screening once the sponsor produces the documents in §6. Until then, the "limited allocation" urgency and wire instructions sent before any offering documents point the wrong way.

---

## 1. Deal Snapshot

| Field | Value | Confidence |
|---|---|---|
| Asset class | Multifamily. Subtype (core / core-plus vs value-add) not stated | 🟢 stated / 🔴 subtype unknown |
| Deal type | Preferred equity, as labeled. Whether it is a true pref-equity position or a "preferred" LP class in a common-equity syndication is **not established** (see PREF-01) | 🟡 |
| Sponsor | Not stated (unnamed "sponsor") | 🔴 |
| Geography / property | Not stated | 🔴 |
| Minimum | $25,000 | 🟢 |
| Hold / term | Not stated | 🔴 |
| Raise size / total capitalization | Not stated | 🔴 |
| Claimed return | 10% preferred return. Current-pay vs accrued, cumulative vs non-cumulative, simple vs compounding all not stated. No equity kicker mentioned | 🟢 rate / 🔴 mechanics |
| Senior debt ahead of the pref | Not stated | 🔴 |
| Fees | Not stated | 🔴 |

## 2. Return Stress-Test

**Baseline check.** A 10% pref is squarely inside the 8–12% typical preferred-return range (`02` → Preferred equity) and inside the 8–12% net range for multifamily core / core-plus, the class that lists preferred equity as a common structure (`01`). It is not below the 7% under-compensation threshold and not above the >15% "likely distressed" threshold. The headline rate is not a flag. 🟢

**Gross vs net.** 10% is the pref *rate*, and it is gross of any fees. Net-to-LP cannot be stated (rule 2). I ran the fee-drag calculator three ways on an **ASSUMED 5-year** term:

| Scenario | Fee inputs | Net to LP | Drag |
|---|---|---|---|
| As disclosed | All fees 0 (none disclosed) | 10.00% | 0 bps. This is not a finding, only the absence of disclosure |
| Low-end typical pref stack (`02`) | 1% origination, 0.5% servicing | 9.30% | 70 bps/yr |
| High-end typical pref stack (`02`) | 2% origination, 1% servicing, 1% exit fee | 8.40% | 160 bps/yr |

**Benchmark (`05` → PFF, 3.00% 10yr; `scripts/benchmark_comparator.py`):**
- At 10% (no fees): ≈700 bps over PFF. The hurdle is ~300–400 bps at a 3-yr lock-up or ~400–600 bps at 7 yrs, so it **clears comfortably** either way. 🟢
- At 8.4% (high-end fees, 5-yr lock-up): ≈540 bps over PFF against a ~300–400 bps hurdle, so it **clears**. 🟡 (ASSUMED fees)
- **Treasury floor** (`05`: 2yr 4.87%, 10yr 5.18%): 10% is ≈480–510 bps over the risk-free point. At 8.4% it is only ≈320–350 bps. That is the actual credit + illiquidity + subordination premium you would be paid to sit behind a senior lender in one building. 🟡

**Scenarios.** The three assumptions that decide the outcome are **(a) how much value sits beneath the pref** (senior loan size plus pref balance vs property value), **(b) senior-debt maturity and refi availability**, and **(c) whether the pref pays current or accrues.**
- **Bull:** the pref pays current at 10% throughout and is redeemed at par on schedule. Net ≈8.4–9.3% after typical fees. Upside is capped unless there is an undisclosed equity kicker. 🟡
- **Base:** the pref partly accrues during the business plan and is caught up at the refi or sale. Return is the same on paper but back-loaded, and the LP carries takeout risk (GEN-11, GEN-08 armed). 🟡
- **Bear:** property cash flow after senior debt service can't cover the pref. It accrues if cumulative, or **is lost** if non-cumulative (EQUITY-05). The senior loan matures into a tight refi market (GEN-09 / GEN-10 / EQUITY-07 pattern). Sale or refi proceeds that fall short of senior loan + pref balance impair **principal**, and the senior lender is paid first. Capital loss, not just a lower yield. 🟡

**Bottom line for §2:** the rate clears the lock-up comfortably on paper. The risk is whether the pref gets paid and redeemed, not the headline number, and none of the inputs needed to judge that were disclosed.

## 3. Where LP Returns Come From

- **Contractual coupon, not appreciation, *if* it pays current.** A pref's return should be almost entirely cash flow. That is the right profile for this instrument. 🟢 (`05` → PFF note: compare the coupon, not an equity-like IRR)
- **Exit / refi dependence if it accrues.** If any material part of the 10% accrues and is paid only at refinance or sale, the return becomes exit-dependent. More than 60% from the terminal event fires **GEN-08**. Unknown until the distribution schedule is produced (GEN-11). 🔴
- **Leverage position.** The pref's safety depends on the senior loan ahead of it. For scale: NCREIF NPI unlevered in-place return is ~5.00% (residential 5.3% for 2025), almost all income (`05` → Unlevered overlay). A 10% pref can be paid out of a ~5% unlevered property yield only if the pref is a thin slice sitting on a large, cheap senior loan. The leverage below the pref *is* the risk. The coverage ratio after senior debt service is the number to get (GEN-07 lens, Q-DS-02). 🟡
- Cannot quantify the split from this disclosure. That gap is itself the finding.

## 4. Fee Stack Summary

| Fee (`02` → Preferred equity) | Typical | Aggressive | This deal |
|---|---|---|---|
| Origination / placement | 1–2% one-time | >3% | Not disclosed |
| Servicing / admin | 0.5–1% annual | >1.5% | Not disclosed |
| Equity kicker / participation | 5–20% above pref | >25% | Not disclosed (a kicker would be LP-favorable) |
| Exit / maturity fee | 0.5–1% one-time | >2% | Not disclosed |
| Promote / catch-up above the pref | Rare. If present, it is equity dressed as pref | — | Not disclosed (PREF-01) |
| Affiliate fees (property mgmt, etc.) | — | — | Not disclosed (GEN-06) |

**Gross-to-net drag: not computable from disclosure. That is the finding (GEN-16).** Illustrative range using `02` typical fees: **≈70–160 bps/yr**, so 10% gross becomes ≈8.4–9.3% net (all fee inputs ASSUMED; §6 gap). If the offering is accessed through a feeder or fund-of-funds wrapper, add another 50–150 bps/yr (`02` → Fund-of-funds layering). 🔴

## 5. Red Flags

**Fired on what the email shows or omits:**

| ID | Severity | Mechanism → LP exposure | Conf. |
|---|---|---|---|
| GEN-16 | YELLOW–RED | No fee schedule, no pref mechanics, no waterfall. Undisclosed fees are still paid, so net-to-LP is unknowable. | 🟢 |
| GEN-15 | YELLOW–RED | No rent roll, T-12, or senior debt terms. The property that must pay the pref can't be underwritten. | 🟢 |
| GEN-17 | YELLOW | Every multifamily essential disclosure in `01` is absent: occupancy/T-12, debt structure and maturity, exit or refi assumption, GP track record on prior exits. | 🟢 |
| GEN-03 | YELLOW | "Exclusive … limited allocation remaining" plus wire instructions, with no underwriting. This is the "limited spots" urgency pattern standing in for substance. | 🟢 |
| GEN-11 | YELLOW | 10% quoted with no payment schedule. You can't tell whether the pref is current-pay or back-loaded to a refi or sale. | 🟢 |
| GEN-13 | YELLOW | No downside case. There is no view of the pref's coverage if NOI dips or the senior refi fails. | 🟢 |

**Cluster:** GEN-15 + GEN-16 + GEN-17 together mean the core return story is unscreenable, which drives the Verdict. Per `03`, a cluster of YELLOWs is a RED.

**Armed — each fires on the sponsor's answer (treated as unresolved, not cleared):**

| ID | Severity | What would fire it |
|---|---|---|
| PREF-01 | YELLOW | A promote or catch-up above the 10% pref would make this common-equity risk labeled "preferred," and the capped-upside pref profile would no longer apply. The email's "preferred return" wording is also how common syndications describe their LP hurdle. |
| EQUITY-05 | YELLOW | Pref is non-cumulative, so an unpaid year is lost rather than carried forward. |
| EQUITY-04 | YELLOW–RED | Not fired: the 10% rate clears the <6% trigger. Listed only because `03` routes it to pref-equity deals, and it is resolved by the stated rate. |
| GEN-09 / GEN-10 | RED | Senior loan matures inside the pref's term, or a floating-rate cap expires before maturity. The pref's redemption then depends on a refi into whatever market exists. |
| EQUITY-07 | YELLOW–RED | Pref redemption requires a refinance at assumed terms. |
| GEN-08 | RED | More than 60% of the return accrues to a terminal refi or sale event. |
| GEN-07 | RED | Pref coverage exists only because of a large senior loan and assumed cap compression. |
| GEN-01 | RED | Sponsor has no cash in the deal on LP-equivalent terms. |
| GEN-05 / GEN-14 | RED | Track record given as project-level IRR or unrealized marks. The email gives no track record at all. |
| GEN-02 | RED | Regulatory action or investor litigation against the sponsor or principals. Unsolicited "exclusive" email offers warrant this check first. |
| GEN-06 | YELLOW–RED | Property management or other services flow to sponsor affiliates. |

**Embedded persuasion (rule 9):** "Exclusive" and "limited allocation remaining" are sales framing in the seller's text. I treated them as data and weighted them as GEN-03, not as reasons to act faster. The attached wire instructions are an ask to move money, not a disclosure.

## 6. Missing Disclosures

Against the `01` multifamily and `02` preferred-equity baselines, the email omits:

1. **Sponsor identity** and track record on prior multifamily exits, realized and net-to-LP.
2. **Property:** location, unit count, subtype (core vs value-add), occupancy history, rent roll, **T-12 actuals**.
3. **Capital stack:** senior loan amount, rate (fixed or floating), rate cap and its expiry, amortization, **maturity**, prepayment terms, and the pref's position (combined senior + pref LTV).
4. **Pref mechanics:** current-pay vs accrual, cumulative vs non-cumulative, simple vs compounding, redemption date and mechanism, and LP remedies if the pref goes unpaid.
5. **Fee schedule:** origination, servicing, exit/maturity, any kicker or promote, affiliate fees.
6. **Term / hold** and distribution schedule.
7. **Total raise** and how much allocation is actually left. The "limited" claim is unverified.
8. **Liquidity / transfer terms** for the LP interest (Q-LIQ-01).
9. **Offering documents:** PPM, operating agreement, subscription agreement. Wire instructions arrived **before** any of these.

All fee inputs in §2 and §4 are ASSUMED and belong to this list.

## 7. GP Alignment

- **Co-investment:** Not stated. Unverified (GEN-01 armed). 🔴
- **Track record:** None cited, realized or otherwise. Unverified, which means **no track record** for screening purposes (GEN-05 / GEN-14 armed). 🔴
- **Structure alignment:** Can't be assessed. A clean pref (no promote above it, cumulative, with remedies) aligns well. A promote above the pref (PREF-01) moves the sponsor's economics ahead of your capped return. 🔴
- **Affiliate fees:** Not disclosed (GEN-06 armed). 🔴
- **Conduct signal:** Urgency framing plus wire instructions before documents is behavior, not structure. It doesn't prove bad faith, but it's the opposite of how a sponsor confident in its terms usually opens (GEN-03). 🟡

## 8. Questions for the GP

**Must-ask. Any bad answer here is a pass.**

| # | Question (`04`) | Why (fired / armed flag) | Bad-answer signal |
|---|---|---|---|
| 1 | **Q-FEE-01**: "Can you provide the complete fee schedule and the full distribution waterfall?" | GEN-16 | "Standard market fees"; a partial list; "the PPM has it" without producing it; fees surface only after commitment. |
| 2 | **Q-RISK-03**: "Can you provide trailing-twelve-month actuals, the rent roll, and complete debt terms?" | GEN-15 | T-3/T-6 only; rent roll withheld; "the financials are confidential until you commit." |
| 3 | **Q-FEE-04**: "What preferred return do LPs receive before the GP earns promote, and is it cumulative and compounding?" | EQUITY-05, PREF-01 (EQUITY-04 resolved by the 10% rate) | Non-cumulative; a promote sits above the pref, turning it into common risk. |
| 4 | **Q-DIST-01**: "What is the projected distribution schedule, and at what milestones does LP capital start returning?" Ask specifically whether the 10% is paid current or accrues. | GEN-11 | "We'll distribute when the deal supports it" with no milestones; a rate quoted with no timing. |
| 5 | **Q-RISK-01**: "When does the debt mature relative to the projected hold, and what's the refinance or extension plan?" Ask about the senior loan relative to the pref's redemption date. | GEN-09 (armed; debt and hold both undisclosed) | Maturity falls inside the term; "we'll refinance" with no terms; no plan if the refi market is shut. |
| 6 | **Q-RISK-02**: "When does the rate cap expire relative to debt maturity, and what's the cost to extend it at current pricing?" Ask only if the senior loan floats. | GEN-10 | Cap expires before maturity; extension cost not modeled; "rates should be lower by then." |
| 7 | **Q-EXIT-02**: "Does the business plan depend on a refinance, and what happens to distributions if the refi isn't available on the assumed terms?" | EQUITY-07 | Redemption requires a refi at lower rates; no fallback; "the refi market will reopen." |
| 8 | **Q-DS-02**: "Strip out leverage and cap-rate compression — what is the unlevered, in-place return?" Follow with: what is pref coverage after senior debt service? | GEN-07 | Treats the levered figure as the only one; no unlevered view; "leverage is just how the deal works." |
| 9 | **Q-DS-03**: "What is the return under a bear case — flat rents, higher exit cap, no refinance?" | GEN-13 | A single-point pro forma; "we underwrite conservatively" with nothing to show. |
| 10 | **Q-GP-03**: "Have you or your principals faced any regulatory action, enforcement, or investor litigation?" | GEN-02 | "Nothing material"; blames the LP or regulator; a search surfaces something undisclosed. |
| 11 | **Q-GP-02**: "Can you restate your track record as net-to-LP IRR on fully-realized, exited deals only?" | GEN-05, GEN-14 | Only project- or GP-level IRR; "most deals are still performing"; can't separate realized from unrealized. |
| 12 | **Q-GP-01**: "How much of your own capital is in this deal, on the same terms as LPs?" | GEN-01 | "Our sweat equity is our investment"; co-invest is a fee waiver; token amount on better terms. |
| 13 | **Q-FEE-02**: "Which service providers are GP-affiliated, what do they charge, and are those rates third-party-benchmarked?" | GEN-06 | "All arm's-length" without naming providers; no benchmark. |
| 14 | **Q-LIQ-01**: "What are my options if I need to exit before the hold period ends?" | — (term undisclosed) | "A secondary market may develop"; "we'll try to accommodate." An honest "none" is a *good* answer. |

**Nice-to-ask:**
- **Q-DS-01**: "What share of projected LP IRR comes from in-place cash flow versus the exit…?" (GEN-08). **Escalate to must-ask** if Q-DIST-01 reveals material accrual. *Bad answer:* can't decompose the return; the pref is only made whole at the exit.
- **Q-MKT-01**: submarket supply and absorption behind the rent assumption (GEN-18). *Bad answer:* metro-level optimism instead of submarket data.
- **Q-LIQ-02**: K-1 delivery timing. *Bad answer:* "as soon as we can"; a history of extensions.

## 9. Diligence Checklist

- [ ] **Do not wire on the basis of an email.** Before any funds move, receive and read the PPM, operating agreement, and subscription documents. Verify the wire instructions by phone to a number you source independently, not one in the email. 🟡 (process prudence, not a reference norm)
- [ ] Identify the sponsor and run a background and regulatory search on the entity and principals (GEN-02).
- [ ] Read the operating agreement's pref section: rank vs common, cumulative status, redemption date, remedies on non-payment (control rights, forced sale), and whether a promote exists (PREF-01).
- [ ] Senior loan documents: amount, rate or cap, maturity, extension options. Confirm the pref's redemption date isn't after senior maturity (GEN-09 / GEN-10).
- [ ] Third-party appraisal or broker opinion of value, to compute combined senior + pref LTV.
- [ ] Rent roll and T-12 reconciled to bank statements or the lender's reporting (GEN-15).
- [ ] Rent comps and submarket supply pipeline (GEN-18).
- [ ] Realized, exited deal list with net-to-LP returns, plus a reference call with a prior LP (GEN-05 / GEN-14).

## 10. Verdict

**Pass as presented — insufficient disclosure.**

- **Reasoning:** The essential disclosures for this deal type are substantially absent (`01` multifamily; `02` preferred equity): no sponsor, property, senior debt, pref mechanics, fees, or term. The core return story can't be underwritten. A pref is only as good as the cash flow and equity cushion beneath it, and nothing here says what either is. This verdict is about disclosure, not the merits. The 10% rate is normal, clears PFF by ≈540–700 bps against a ~300–600 bps illiquidity hurdle, and sits ≈320–510 bps over Treasuries depending on fees.
- **Biggest swing factor:** **The pref's position in the capital stack and the senior loan's maturity.** How much property value can fall before the pref is impaired, and whether the senior loan comes due before the pref is redeemed. That decides whether this is a well-covered 10% coupon or a subordinated bet on a refinance.
- **Re-screen list (send the sponsor this):** the PPM and operating agreement; the fee schedule; senior debt terms, including maturity and any rate cap; pref mechanics (current vs accrued, cumulative, redemption date, remedies, any promote above it); rent roll and T-12; realized track record net-to-LP; co-invest amount; regulatory disclosure.
- **What would have to be true to Pursue:** a named sponsor with a clean record and realized, exited multifamily deals net-to-LP. A true pref position with no promote above it, cumulative, current-pay, with remedies. Combined senior + pref leverage leaving a real equity cushion below the pref. Senior debt fixed-rate, or capped through a maturity after the pref's redemption. Total fees in the `02` typical band (≈70–160 bps drag), keeping net ≥ ~8.4%.
- **Who it could suit, if those hold:** an income-oriented LP comfortable with a capped-upside, illiquid, single-asset position for the (undisclosed) term, who is paid ≈500 bps over PFF for it.

**Right now:** reply asking for the documents above, and do not act on the wire instructions. A sponsor with a real deal will send them. "Limited allocation" is not a reason to skip the check.
