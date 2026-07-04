# Eval fixture 04 — Bridge fund, Phoenix fix-and-flip ("never had a loss")

*Iteration-1 run, 2026-07-03, against SKILL.md @ cddc52d. Fixture prompt: evals.json id 4 (contrast pair 3b).*

---

**Verdict: Pass.** Same deal type as a sound bridge fund, opposite disclosure pattern: an above-category net target with no fee schedule, an LTV quoted with no basis, a single-metro book, and a loss history offered as a slogan ("we've never had a loss") — which is, verbatim, the bad-answer signal for the loss-history question, volunteered unprompted. Biggest swing factor: none to price — the deal as presented has no underwritable substance.

## 1. Deal Snapshot
- **Asset class:** Hard money / bridge (fix-and-flip) 🟢
- **Deal type:** Debt fund 🟢
- **Sponsor:** Not stated ("experienced team," unnamed)
- **Geography:** Phoenix metro only 🟢
- **Minimum / Hold / Raise:** Not stated
- **Claimed return:** 11% net target 🟢 — *above* the `01` category net range (8–10%) 🔴

## 2. Return Stress-Test
Baseline (`01`): hard-money funds net 8–10% to LPs. **The 11% target sits above the category ceiling** — in senior-secured lending, above-range net comes from somewhere: higher-risk borrowers, higher leverage, or optimism. None is disclosed 🔴.

Benchmark (`05`): 11% over HYG (5.0%) ≈ 600bps; over the 3mo Treasury (3.71%) ≈ 729bps. On paper that clears any illiquidity hurdle — but a senior-secured spread that wide is itself the question, not the answer: HYG's diversified high-yield book pays 500bps *of credit spread* for known risk; a single-metro fix-and-flip book paying more is pricing risk it hasn't disclosed 🟡.

Swing assumptions: unknowable — no fee stack, no loan-level data, no fund terms. The stress-test's honest output is that no case (base, bull, or bear) can be computed from this disclosure.

## 3. Where LP Returns Come From
Interest income on fix-and-flip loans, concentrated in one metro. Fix-and-flip repayment depends on the borrower completing the renovation and selling — in a single market, that is one housing cycle's risk, undiversified (`HML-02` mechanism). Whether the 11% requires fund-level leverage is undisclosed.

## 4. Fee Stack Summary
**Not computable — that is the finding** (`GEN-16`). No management fee, performance fee, servicing, or origination economics disclosed. An "11% net" with no stated fee stack is a marketing number: the gross the book must produce to deliver it — and the risk that gross implies — can't be reconstructed.

## 5. Red Flags
**RED**
- `HML-01` — "70% LTV" with **no basis stated**. In fix-and-flip lending the convention is LTV-on-ARV; 70% on ARV can exceed 100% of as-is value — no real equity cushion if the renovation thesis fails. Until the as-is figure is produced, treat the cushion as unproven.
- `HML-03` + `HML-04` — Default and recovery **not disclosed**; in their place, "we've never had a loss." A zero-loss claim through 2020 and 2022–23 is either a very young book, a survivor-biased denominator, or untrue — and it is precisely the bad-answer signal `04` lists for the loss-history question (Q-RISK-05: *"we've never had a loss"*), volunteered before the question was asked. The pair fires at RED.

**YELLOW**
- `HML-02` — 100% Phoenix-metro concentration: one local downturn, no offset. (Phoenix is also a historically boom-bust housing market — the concentration is in a high-beta metro.)
- `GEN-03` — Substance-light presentation: "experienced team" with no names, no track record, no figures beyond two numbers and a slogan.
- `GEN-16` (YELLOW–RED) — No fee or structure disclosure.
- `GEN-15` (YELLOW–RED) — No financials: no loan tape, no fund statements, no terms.
- Above-category net target (11% vs `01`'s 8–10%) with no explanation of the source of the extra yield.

**Cluster note:** `HML-01` + `HML-03/04` + `HML-02` is the full debt-fund risk triad — basis, losses, concentration — all unresolved in one deal.

## 6. Missing Disclosures
Per `01` (hard money essentials), this fund omits effectively all of them:
- LTV on **as-is** value (only an unbasised "70%" given)
- Default rate history — replaced by a slogan
- Recovery rate and workout process
- Sponsor identity and history through a downturn
- Fee schedule (management, performance, servicing) — entirely absent
- Fund terms: size, lock-up, redemption, leverage
- Loan-book data: grade mix, average size, seasoning
- GP co-investment

## 7. GP Alignment
Nothing verifiable: unnamed team, no co-invest disclosure, and a track-record claim ("never had a loss") that is structurally unverifiable as stated — a claim of perfection is weaker evidence than a disclosed loss history, because it forecloses the follow-up (`HML-03`/`HML-04` notes: a 2% default rate with 90% recovery is a *better* signal than "zero"). Treated as no validated record.

## 8. Questions for the GP
**Must-ask — the deal cannot advance past a bad answer on any:**
1. **Q-RISK-04** — "What is the average portfolio LTV on **as-is** value, not ARV?" *Bad answer:* quotes only ARV; "our borrowers always complete." (`HML-01`)
2. **Q-RISK-05** — "Default rate *and* realized recovery, including 2020 and 2022–23 — with the loan-level basis." *Bad answer:* repeats "we've never had a loss"; produces no data. (`HML-03`/`HML-04`) — *note: the bad answer has already been given unprompted; the question now tests whether data exists behind it.*
3. **Q-FEE-01** — Complete fee schedule; how does the book produce 11% net, and is that figure levered? *Bad answer:* "standard fees"; won't decompose gross-to-net. (`GEN-16`; `CREDIT-01` mechanism)
4. "What is the geographic plan — is Phoenix-only a mandate or a current state?" *Bad answer:* "we know our market" as the entire risk answer. (`HML-02`)
5. **Q-GP-01** — Named principals, their capital in the fund, same terms. *Bad answer:* "experienced team" without names or dollars. (`GEN-01`)
6. **Q-GP-03** — Regulatory/litigation history of the principals. *Bad answer:* "nothing material." (`GEN-02`)

## 9. Diligence Checklist
- [ ] Identify principals; background/regulatory search
- [ ] Audited fund financials (existence test, then loss verification)
- [ ] Loan tape: as-is LTVs, seasoning, payoff history
- [ ] Fund docs: fee schedule, leverage authority, redemption terms
- [ ] Phoenix fix-and-flip market data: inventory, days-on-market, flip-margin trend

## 10. Verdict
**Pass.** Not because bridge lending is unattractive — the sound version of this exact deal type screens as Pursue — but because this fund pairs an above-category return target with a disclosure pattern that answers none of the category's five defining risk questions (LTV basis, default, recovery, concentration, fees), and volunteers a known evasion signal as its track record. **What would have to be true to re-screen:** as-is LTV produced, loan-level loss data through the stress years, a complete fee schedule explaining the 11%, named principals with verifiable history, and a concentration plan. That is not a question list; it is the entire deal package — which is the point. Suits no LP as presented.
