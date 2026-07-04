# Eval fixture 04 — Phoenix fix-and-flip bridge fund (thin, problematic)
*Iteration-3 run, 2026-07-04, blind generation by fresh-context agent, against SKILL.md (post S1b/S2b fixes).*

**Verdict: Pass as presented — insufficient disclosure. "70% LTV" with no as-is/ARV basis, a single-metro book, zero fee disclosure, and "we've never had a loss" standing in for a default/recovery history — the core return story cannot be underwritten from this, and what little is stated points the wrong way.**

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Hard money / bridge loans (fix-and-flip) 🟢 |
| Deal type | Debt fund 🟢 |
| Sponsor | Not stated ("experienced team" — no names, no history) |
| Geography | Phoenix metro only 🟢 |
| Minimum investment | Not stated |
| Hold / fund term | Not stated |
| Raise / fund size | Not stated |
| Claimed return | 11% net (target) 🟢 |
| Loan book | "70% LTV" — **as-is or ARV not stated** 🔴 |
| Credit history | "We've never had a loss" — no default rate, no recovery rate |

## 2. Return Stress-Test

Swing assumptions: **LTV basis (as-is vs ARV)**, **Phoenix housing cycle**, **undisclosed leverage/fees**.

- **Base.** 11% net is *above* the `01` category norm (8–10% net) 🟢 — an above-market target with no explanation of where the extra 100–300bps comes from: higher-risk borrowers, retained points, fund leverage, or under-provisioned losses. Above-norm yield in senior-secured lending is bought with something.
- **Bear.** Fix-and-flip loans are customarily quoted on ARV 🟡; if this 70% is ARV-based, `01`'s warning applies directly — a 70% LTV on ARV can be at or above 100% of current value, meaning **no equity cushion if the renovation thesis fails**. In a single-metro book, one local downturn hits every loan at once: a Phoenix correction with ARV-based lending is the scenario where "never had a loss" ends abruptly.
- **Benchmark (`05`, benchmark_comparator, 3-yr term assumed 🔴):** 11% vs HYG 5.0% = ≈600bps; ≈729bps over the 3mo Treasury (3.71%) → clears the ~300–400bps hurdle on paper 🟡 — but with no fee stack or loss history, the 11% is an assertion, not a net figure that can be trusted (never gross-to-gross; here we cannot even confirm it's net of a *disclosed* stack).

## 3. Where LP Returns Come From

Nominally: interest income from short-duration fix-and-flip loans. Actually unverifiable: with no fee schedule, no leverage disclosure, and no loss history, whether the 11% is coupon income, leverage-assisted, or simply optimistic cannot be determined. The above-norm target with zero cost disclosure is itself the tell (§5).

## 4. Fee Stack Summary (`02`)

**Nothing is disclosed — GEN-16 fires outright.** Per `02`, a fund like this normally carries: fund management 1–2% (step-down after investment period), servicing 0.25–0.5%, possibly a performance fee 10–20% over a 5–8% hurdle, plus origination points whose flow (fund vs GP) must be verified. **Gross-to-net drag is not computable — that is the finding.** An 11% "net" with an undisclosed stack is not a net.

## 5. Red Flags (`03`)

**RED / treat-as-RED**
- **HML-01** — 70% LTV quoted with no as-is value stated. Fix-and-flip convention is ARV 🟡; per the proactive trigger, treat as ARV-based (no real equity cushion) until the as-is figure is produced.
- **HML-03** (YELLOW–RED) — default rate not disclosed; "we've never had a loss" is the *verbatim bad-answer signal* from Q-RISK-05, not a credit history. Either the book is too young to have seasoned through 2020/2022–23 or losses are being defined away.
- **HML-04** (YELLOW–RED) — recovery rate not disclosed (moot if defaults are claimed at zero — which is itself the problem).
- **GEN-16** (YELLOW–RED) — no fee, hurdle, or structure disclosure of any kind.

**YELLOW**
- **HML-02** — 100% Phoenix-metro concentration: a single local downturn hits the entire book with no offset; Phoenix is a historically high-beta housing market 🟡.
- **GEN-03** — "Experienced team," "never had a loss": assertion standing in for underwriting substance.
- **GEN-15** (YELLOW–RED) — "no other figures provided": no loan tape stats, fund terms, or financials.
- **GEN-14 (unresolved)** — no realized fund-level performance shown; the track-record claim is unverifiable.
- Above-category yield (11% vs the `01` 8–10% norm) with no source-of-yield explanation 🟡 — the mismatch itself is the question.

## 6. Missing Disclosures (`01` HML essentials)

Every `01` essential except geographic mix is absent:
- Average LTV on **as-is** value (the essential; ARV alone is not it)
- Default rate history, incl. 2020 and 2022–23
- Recovery rate and workout/foreclosure process
- Sponsor identity and history through a downturn
- Plus: fee schedule (all of it), fund leverage, fund term/redemption terms, distribution schedule, co-invest, loan count/size, grade or borrower quality data

## 7. GP Alignment

Unassessable 🔴: sponsor unnamed, co-invest unstated (GEN-01 unresolved), no verifiable track record — "never had a loss" without a default/recovery table is marketing (GEN-03), and if the team is genuinely experienced through 2020 and 2022–23, producing the loss table should be trivial.

## 8. Questions for the GP (`04`)

All must-ask — the first two decide the deal:
1. **Q-RISK-04** (HML-01) — average portfolio LTV on **as-is** value, not just ARV. *Bad answer:* quotes only ARV; "our borrowers always complete."
2. **Q-RISK-05** (HML-03, HML-04) — historical default *and* realized recovery, through 2020 and 2022–23. *Bad answer:* "we've never had a loss" — **already given, pre-emptively.** The re-answer must come with a loan tape.
3. **Q-FEE-01** (GEN-16) — complete fee schedule: management, servicing, performance/hurdle, where points flow. *Bad answer:* "standard market fees."
4. **Q-RISK-06** (CREDIT-01 family) — fund leverage, and is the 11% levered or unlevered? *Bad answer:* no number.
5. Source-of-yield: what generates 11% net when the category norm is 8–10 (`01`)? *Bad answer:* "our deal flow is just better" with no pricing/points/borrower-profile specifics.
6. **Q-GP-02** (GEN-05, GEN-14) — fund-level realized net-to-LP by vintage, and how long the fund has operated. *Bad answer:* can't separate realized from marks; the fund launched after 2023 (i.e., "never had a loss" = never seasoned).
7. **Q-GP-03** (GEN-02) — regulatory/litigation history of the principals. *Bad answer:* deflection.
8. **HML-02 response** — any plan to diversify beyond Phoenix, or a rationale for concentration plus the underwriting cushion it demands. *Bad answer:* "we know this market" as the whole answer.
9. **Q-LIQ-01** — lock-up and redemption terms. *Bad answer:* silence.

## 9. Diligence Checklist

- PPM/LPA: fee schedule, leverage authority, redemption terms — none seen yet
- Loan tape: as-is and ARV LTVs per loan, seasoning, delinquencies (30/60/90), extensions and modifications (extended loans are how "no losses" is manufactured)
- Sponsor background: principals named, SEC/state licensing (AZ mortgage-lending license), litigation search
- Fund audit or administrator verification of the no-loss claim
- Phoenix market data: fix-and-flip volume, price trend, months of inventory — independent of the sponsor

## 10. Verdict

**Pass as presented — insufficient disclosure.** The essential disclosures for this category are substantially absent — LTV basis, default history, recovery, fees, fund terms, sponsor identity — so the 11% target cannot be underwritten at all, and the two facts that *are* offered cut against the deal: full single-metro concentration (HML-02) and a loss claim phrased as the exact evasion the category's diligence question exists to catch (HML-03/04). Biggest swing factor: the as-is LTV. **Re-screen list:** as-is LTV alongside ARV; default/recovery table through 2020 and 2022–23 (or honest fund age); complete fee schedule and leverage disclosure; fund terms and redemption mechanics; named sponsor with verifiable history. Note the asymmetry with a well-disclosed peer: a fund at 9% net that shows its losses is a better LP proposition than 11% that shows nothing.
