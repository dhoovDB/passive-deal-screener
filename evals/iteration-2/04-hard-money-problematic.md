# Eval fixture 04 — Phoenix fix-and-flip bridge fund (thin, "never had a loss")
*Iteration-2 run, 2026-07-04, blind generation by fresh-context agent, against SKILL.md (post S1–S3 fixes).*

**Verdict: Pass as presented — insufficient disclosure. The 70% LTV has no stated basis (as-is vs ARV — `HML-01`), the book is 100% one metro (`HML-02`), and "we've never had a loss" is the verbatim bad-answer signal for the default/recovery question (`Q-RISK-05`), offered unprompted.**

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Hard money / bridge loans (fix-and-flip collateral) 🟢 |
| Deal type | Debt fund 🟢 |
| Sponsor | **Not stated** ("experienced team," unnamed) |
| Geography | Phoenix metro only 🟢 |
| Minimum investment | **Not stated** |
| Hold / fund term | **Not stated** |
| Raise / fund size | **Not stated** |
| Claimed return | 11% **net** target 🟢 (basis of "net" — after which fees — not stated) |
| Portfolio LTV | 70% — **on as-is or ARV not stated** 🔴 |
| Credit history | "Never had a loss" — no default rate, no recovery rate, no time period |
| Fees | **None disclosed** |

Routing: `01` hard money baseline (8–10% net; 65–75% LTV typical *on ARV*); `02` hard money / bridge fee inventory; `03` `GEN-`, `HML-`; `05` HYG + duration-matched Treasury.

## 2. Return Stress-Test

Swing assumptions: **(a) the LTV basis** — 70% on ARV against fix-and-flip collateral can be at or above 100% of as-is value (`01`), meaning the "equity cushion" only exists if every renovation completes and sells at projection; **(b) Phoenix housing prices** — a single-metro book means one local correction hits every loan at once; **(c) default/recovery under any stress** — with no history disclosed, the bear case has no floor to anchor on.

- **Base:** 11% net as targeted — **above** the `01` category norm of 8–10% net 🟡. Extra yield in senior-secured lending comes from somewhere: riskier borrowers, higher-LTV paper, more points, or aspiration. Which one is undisclosed.
- **Bull:** Phoenix flips keep clearing; 11% pays.
- **Bear:** a Phoenix-specific correction (the metro has run hot-cold historically) → concentrated defaults, and if the 70% is ARV-based, recoveries start from little or no real equity cushion; LP principal impairment is on the table, not just yield compression 🔴 (not sizeable from this disclosure — that is the finding).

**Benchmark (`05`):** 11% vs HYG 5.0% = **+600bps**; vs the 3mo–2yr Treasury (3.71–4.15%) ≈ **+700bps**. That is *above* the 300–500bps band the spread table says hard money pays. An outsized spread over the category is not a gift — it is unpriced or undisclosed risk 🟡. Clears the illiquidity hurdle arithmetically; fails the "why does this pay more than the asset class?" question.

## 3. Where LP Returns Come From

Contractual interest and points on short-duration loans — cash-flow-driven; no exit-cap or leverage-compression story (`GEN-07`/`GEN-08` n/a as stated). But whether the fund itself is levered to reach 11% is undisclosed — a warehouse line would quietly convert this into a levered credit bet (`CREDIT-01` mechanism) → ask. The return's real driver is credit performance in one metro, on collateral whose value basis is unstated.

## 4. Fee Stack Summary

**Nothing disclosed.** The `02` hard-money inventory expects: fund management fee (1–2%, step-down question — `HML-05`), possible performance fee (10–20% over 5–8% hurdle), servicing (0.25–0.5%), origination points (borrower-paid, 1–3), late-fee/default-interest treatment, possible wind-down fee. Zero of these appear.

**Gross-to-net drag: not computable — that is the finding (`GEN-16`).** "11% net" with no fee schedule is unfalsifiable; you cannot tell what gross book yield it implies or what happens to the net when the book underperforms.

## 5. Red Flags

**RED**
- `HML-01` — 70% LTV with no as-is value stated. On fix-and-flip collateral, LTV quoted without basis defaults to the flattering one (ARV); 70% on ARV can be 100%+ of current value — no real equity cushion if the renovation thesis fails. Proactive trigger fired per SKILL ("debt fund quoting LTV… with no as-is") → `Q-RISK-04`.

**YELLOW–RED**
- `HML-03` + `HML-04` — default rate and recovery rate not disclosed; "we've never had a loss" is the **listed bad-answer signal** for `Q-RISK-05`, volunteered before the question was asked. Either the fund is too young to have seasoned through stress (2022–23), or losses are being defined away (extensions, rewrites, interest accrual masking non-performance) 🟡 → `Q-RISK-05`.
- `GEN-16` — no fee disclosure at all → `Q-FEE-01`.
- `GEN-15` — no loan count, no book size, no vintage data, no fund terms; the fund can't be underwritten from this → `Q-RISK-03` (adapted to loan-tape form for a debt fund).

**YELLOW**
- `HML-02` — 100% Phoenix-metro concentration: one local housing downturn hits the entire book with no offset → `Q-RISK-04`-adjacent; the response question is the geographic-distribution one (per `03`: "What is the geographic distribution of the loan book?"). Concentration this total, paired with the unstated LTV basis, reads closer to RED as a cluster.
- `GEN-03` — marketing-heavy, substance-light: "experienced team," "never had a loss," and a yield 100–300bps above category norm, with no supporting figures → `Q-GP-02`.
- `HML-05` (probe) — no management fee disclosed, so no step-down disclosed either → `Q-FEE-01`.
- `GEN-11` — target return with no distribution schedule or lock-up terms → `Q-DIST-01`, `Q-LIQ-01`.

**Cluster note:** `HML-01` + `HML-02` + `HML-03`/`HML-04` together are the debt-fund equivalent of a financing story — the marketed safety ("senior secured, 70% LTV") is unverifiable on every axis that determines realized LP loss.

## 6. Missing Disclosures

Against the `01` hard-money essential-disclosure baseline (`GEN-17`) — **four of five essentials absent, the fifth (geographic mix) disclosed and adverse:**
- Average LTV **on as-is value** (and the ARV figure separately) — absent.
- **Default rate history** — absent (replaced by a slogan).
- **Foreclosure process and recovery rate** — absent.
- **Sponsor history through a downturn** (2020, 2022–23) — absent; "experienced team" is not a history.
- Plus: fee schedule, fund term/lock-up, fund-level leverage, loan count and average size, origination points, sponsor identity, GP co-investment, distribution schedule.

## 7. GP Alignment

- **Co-investment:** not stated → `Q-GP-01`.
- **Track record:** "never had a loss" is an anti-disclosure — it asserts a conclusion while withholding the data (defaults, recoveries, extensions, REO). Treat as **no validated track record** (`GEN-05`/`GEN-14` mechanism: unverifiable claims are unverified) 🔴 → `Q-GP-02`, `Q-RISK-05`.
- **Fee alignment:** unknowable — no fees disclosed; whether default interest flows to LPs or the GP is unknown.
- **Affiliates:** fix-and-flip lenders often affiliate with title, servicing, or construction draws — undisclosed → `Q-FEE-02` (`GEN-06` probe).

## 8. Questions for the GP

**Must-ask**
1. `Q-RISK-04` — Average portfolio LTV on **as-is** value, not just ARV. *Bad answer:* quotes only ARV; "our borrowers always complete."
2. `Q-RISK-05` — Historical default rate **and** realized recovery rate, including through 2020 and 2022–23. *Bad answer:* "we've never had a loss" — **already given**; treat a repeat as the flag confirmed.
3. `Q-FEE-01` — Complete fee schedule: management fee, any carry/hurdle, servicing, and who keeps default interest. *Bad answer:* "standard market fees"; fees surface only after commitment.
4. `Q-GP-02` — Realized net-to-LP returns on prior vintages, and how long the fund has operated. *Bad answer:* gross yield instead of LP net; the "track record" starts after 2023.
5. Geographic concentration (per `HML-02` response): What is the plan if Phoenix corrects — and how many loans/borrowers is the book? *Bad answer:* "Phoenix always comes back"; a handful of repeat borrowers is the whole book.
6. `Q-RISK-06`-style — Any fund-level leverage behind the 11% net? Levered or unlevered basis? *Bad answer:* a credit line exists but isn't counted (`CREDIT-01` mechanism).
7. `Q-GP-01` — GP cash invested on LP terms? *Bad answer:* "our sweat equity is our investment."
8. `Q-GP-03` — Regulatory action or investor litigation? *Bad answer:* "nothing material."
9. `Q-LIQ-01` — Lock-up and redemption mechanics. *Bad answer:* "we'll try to accommodate."

**Nice-to-ask:** `Q-DIST-01` (distribution schedule), `Q-GP-04` (underwriting team vs book growth), `Q-LIQ-02` (K-1 timing), extension/modification policy (how many loans have been extended rather than repaid — the place "no losses" usually hides).

## 9. Diligence Checklist

- PPM/LPA: fees, leverage authority, redemption terms.
- Loan tape or audited schedule: LTVs on both bases, delinquencies, extensions, REO — verify "no losses" against paper, not narrative.
- Background/regulatory search on principals (unnamed "experienced team" is step zero).
- Sample as-is appraisals/BPOs on current collateral.
- Fund inception date and AUM history — a 2024-vintage fund "never having a loss" is a different fact than a 2015-vintage one.
- Independent administrator confirmation.

## 10. Verdict

**Pass as presented — insufficient disclosure.** Four of the five `01` hard-money essentials are absent and the fifth — geography — is disclosed as total single-metro concentration. What little is stated makes it worse: an above-category 11% net with no fee schedule, an LTV with no basis, and a loss claim that is the question bank's textbook evasion (`Q-RISK-05` bad answer) delivered pre-emptively. Biggest swing factor: **the as-is LTV** — it decides whether "senior secured" means a real cushion or a renovation bet.

**Re-screen list:** as-is + ARV LTV; default/recovery/extension history with dates; fund inception and vintage returns net-to-LP; full fee schedule; fund-level leverage disclosure; loan count/size and borrower concentration; sponsor identity and downturn history; lock-up/redemption terms. **What would have to be true to pursue:** as-is LTV verifiably ≤75%, a seasoned book through 2022–23 with disclosed defaults and strong recoveries, and fees that reconcile gross-to-net. **Who it suits:** as presented, no one — an LP wanting Phoenix bridge-lending exposure should demand fixture-03-grade disclosure before wiring a dollar.
