# Eval fixture 04 — Phoenix fix-and-flip bridge fund (thin, problematic)
*Iteration-4 run, 2026-09-27, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 1c7faff.*

**Verdict: Pass as presented — insufficient disclosure.** Four sentences of marketing cannot underwrite a bridge fund: the LTV basis (as-is vs ARV), default and recovery history, fee stack, fund term, and GP co-invest are all absent, and the one track-record claim ("we've never had a loss") is the exact dodge the question bank names as a bad answer. Re-screen when the list at the end of §10 is answered in writing.

---

## 1. Deal Snapshot

| Field | Value | Confidence |
|---|---|---|
| Asset class | Hard money / bridge loan (fix-and-flip residential lending) | 🟢 stated |
| Deal type | Hard money / bridge debt fund | 🟡 inferred ("this bridge fund") |
| Sponsor | Not stated (unnamed "experienced team") | 🔴 |
| Geography | Phoenix metro only | 🟢 stated |
| Minimum investment | Not stated | 🔴 |
| Hold / fund term | Not stated (category norm: 6–18 mo per loan, 3–5 yr fund commitment, `01`) | 🔴 |
| Raise / fund size | Not stated | 🔴 |
| Claimed return | "Target 11% net" | 🟢 stated, 🔴 unverified |
| Leverage | "70% LTV" — basis (as-is vs ARV) not stated | 🟢 stated, basis 🔴 |
| Track record | "Never had a loss" — no figures, no period, no loan count | 🔴 unverifiable |

## 2. Return Stress-Test

The 11% net target sits **above** the category norm: `01` gives hard money / bridge **8–10% net** to LP, with **11–13% gross** common before fees. 11% is the bottom of the *gross* band presented as a *net* figure. 🟢 (from `01`). Either the fund lends at higher rates / to riskier borrowers than the category, runs a lighter fee stack than typical, uses fund-level leverage, or the "net" label is loose. Each explanation is a different risk; none is disclosed.

**Swing assumptions:** (1) LTV basis — as-is vs ARV; (2) default rate × loss severity through a downturn; (3) the gross-to-net fee stack (is 11% really net?).

| Case | Assumptions | Net-to-LP | Confidence |
|---|---|---|---|
| Bull | GP's claim holds: coupon + points deliver 11% net, no credit losses, fees as implied | ~11% | 🔴 GP assertion only |
| Base | Category-typical outcome: 11–13% gross, typical fund fees (`02`) | ~8–10.5% (see §4 runs) | 🟡 inferred from `01`/`02` |
| Bear | Loans are 70% of **ARV**; Phoenix flip exits stall; borrowers default on unfinished projects; collateral is worth as-is value, which on a 70% ARV loan "can be 100%+ of current value" (`01`) — i.e., little or no equity cushion. Loss severity then depends on unknown workout competence (`HML-04`). | Coupon income offset by principal losses; LP capital impairment possible. Illustratively, per `03`'s own example, a 2% default rate at 40% recovery is ~1.2% of book lost per default cycle, before foreclosure costs and cash drag. Single-metro concentration makes the defaults correlated rather than diversified. | 🔴 assumed — no default/recovery data provided |

**Benchmark (net-to-LP vs `05` comparator)** — `scripts/benchmark_comparator.py --deal-type hard-money --net-irr 11`:

- 11.00% vs **HYG 4.83%** (10yr) → **≈617 bps** premium. Lock-up assumed 3–5 yr (fund term not stated — 🔴 ASSUMED) → illiquidity hurdle **~300–400 bps**. Script verdict: **CLEARS comfortably**. 🟢
- Over the duration-matched Treasury: **≈676 bps** over the 3mo (4.24%), ≈613 bps over the 2yr (4.87%). `05` puts the category's credit + illiquidity spread at **≈315–575 bps**. 🟢
- **Read:** the target *over*-clears both the comparator and the category's own Treasury spread. On a debt fund, a premium above category is not free money — it is payment for more credit risk (higher-LTV, lower-quality borrowers, one metro) or a figure that won't survive disclosure. Clearing the hurdle is necessary, not sufficient (`05`), and here it rests on an unverified number.

## 3. Where LP Returns Come From

- **Source:** loan coupon + borrower-paid origination points flowing into fund yield (`02`), less fund-level fees. No exit-cap or appreciation component at the fund level. 🟡
- **Hidden exit dependence:** principal repayment on a fix-and-flip loan comes from the *borrower's* sale or refinance of the renovated property. The LP is not betting on an exit cap, but LP *principal* depends on the Phoenix flip resale market staying open. That is the credit-side version of exit risk — it shows up as defaults (`HML-03`), not as IRR decomposition. 🟡
- **Equity-lens flags considered and not fired:** `GEN-08` (exit-dependent IRR) and `GEN-07` (financing story) are equity-return tests; the fund doesn't project terminal value. `GEN-07`'s debt-fund cousin — fund-level leverage turning a modest loan yield into a marketable LP number (`03` notes on `CREDIT-01`) — **cannot be ruled out** and is one plausible explanation for 11% net sitting above the 8–10% band. Asked in §8.

## 4. Fee Stack Summary

**Gross-to-net drag: not computable — zero fees disclosed.** That is the finding (`GEN-16`). With every fee passed as `0`, the calculator returns 0 bps by construction — which says nothing about what the LP will actually pay.

Illustrative runs, `scripts/fee_drag_calculator.py`, all inputs 🔴 ASSUMED from `02` hard-money ranges (hold 3 yr):

| Scenario | Inputs | Net LP IRR | Drag |
|---|---|---|---|
| Disclosed-only | gross 11, every fee 0 | 11.00% | 0 bps (meaningless — nothing disclosed) |
| Typical, no carry | gross 13 (top of `01` gross band), fund mgmt 2%, servicing 0.5% | 10.50% | **250 bps/yr** |
| Typical + carry | as above + 20% carry over 8% hurdle, 100% catch-up | 8.14% | **486 bps/yr** |

**Implication:** even at the *top* of the category's common gross yield, a typical `02` fee stack lands the LP at ~8–10.5% net. To deliver 11% net after typical fees, the book must yield above 13% gross — meaning riskier loans, fund leverage, or a lighter fee stack than typical. The GP must say which. 🟡

Fees `02` says this deal type normally carries, none disclosed: fund management fee (1–2% of AUM, annual), servicing fee (0.25–0.5%), performance fee / carry (10–20% over a 5–8% hurdle; no hurdle = aggressive), wind-down fee, disposition of late fees / default interest (should go to the fund, not a GP "workout fee"), and origination points (1–3; who keeps them — fund or GP?).

## 5. Red Flags

**RED / treat as RED until answered**

- **`HML-01` — LTV basis unstated on a fix-and-flip book (RED).** Fix-and-flip lending typically quotes 65–75% on ARV (`01`). If "70%" is on ARV, current-value LTV can exceed 100%: no equity cushion if the renovation or resale fails. Proactive trigger. 🟡 (basis inferred from category; confirm) → `Q-RISK-04`.
- **`HML-03` + `HML-04` — default rate and recovery rate not disclosed (YELLOW–RED → RED).** "Never had a loss" is neither. It says nothing about defaults, extensions, loans rolled or modified to avoid booking a loss, or recovery, and it names no period — whether the book existed through 2020 or 2022–23 is unknown. `Q-RISK-05` lists "we've never had a loss" verbatim as the bad-answer signal. 🟢 → `Q-RISK-05`.
- **`GEN-14` — no realized, verifiable track record (RED); `GEN-05` cited parenthetically.** No realized net-to-LP figures, no loan count, no fund vintages — only an adjective ("experienced") and an absolute claim. Whether "11% net" is a net-to-LP figure or a portfolio yield is unverified (`GEN-05`). 🔴 → `Q-GP-02`.
- **`GEN-16` — no fee or waterfall disclosure (YELLOW–RED → RED).** Gross-to-net drag unknowable (§4), and the target sits above the category's net band. 🟢 → `Q-FEE-01`.

**YELLOW**

- **`HML-02` — geographic concentration.** 100% Phoenix metro: one local housing downturn hits every loan at once, and correlated defaults also mean correlated collateral values at foreclosure. 🟢 → Q from `HML-02`.
- **`GEN-17` — essential category disclosures absent.** Of the five `01` essentials for hard money (LTV as-is and ARV, default history, foreclosure/recovery, geographic mix, sponsor history through a downturn), only geographic mix is disclosed — and it's the concentrated answer. 🟢
- **`GEN-11` — no distribution schedule.** Monthly/quarterly income? Reinvested? Redemption gates? Not stated. 🟢 → `Q-DIST-01`.
- **`GEN-13` — no downside case.** A single target with no stress scenario. 🟢 → `Q-DS-03`.
- **`GEN-03` — marketing-heavy, substance-light.** The entire pitch is a target, a leverage figure, a market, and an assertion of perfection. 🟢 → `Q-GP-02` / `Q-FEE-01`.

**Unassessable — not fired, routed to must-ask:** `GEN-01` (co-invest not stated → `Q-GP-01`), `GEN-02` (sponsor unnamed, no background possible → `Q-GP-03`), `GEN-06` (who keeps origination points / workout fees → `Q-FEE-02`), `HML-05` (fund term and management-fee basis unknown), fund-level leverage (analogous to `CREDIT-01` → `Q-RISK-06`).

**Cluster:** `HML-01` + `HML-03` + `HML-04` + `HML-02` is the debt-fund failure pattern. An ARV-based book with no disclosed loss history, concentrated in one metro, has its downside hidden in exactly the places a single local slowdown would expose. Together with `GEN-14`/`GEN-16`, the deal is unscreenable as presented.

## 6. Missing Disclosures

Against the `01` hard-money baseline and the `02` fee inventory:

1. Average portfolio LTV on **as-is** value, alongside ARV.
2. Historical default rate, by year, including 2020 and 2022–23.
3. Foreclosure process, realized recovery rate, and average workout timeline.
4. Sponsor identity and history through a downturn (loan count, years originating, capital deployed).
5. Complete fee schedule: management fee and basis, servicing, carry/hurdle, wind-down, and who keeps origination points and default interest.
6. Fund structure: term, investment period, redemption/liquidity terms, distribution frequency.
7. Minimum investment and fund size.
8. GP co-investment amount and terms.
9. Fund-level leverage (credit line / warehouse), if any.
10. Loan-level detail: average loan size, loan count, borrower concentration, first-lien position, extension/modification policy.
11. Whether "11% net" is net-to-LP after all fees, and whether it's a target or a realized figure.

Every figure the §2 and §4 calculations used beyond the stated 11% (hold, gross yield, fee rates) is an **ASSUMED** input.

## 7. GP Alignment

- **Co-invest:** not stated. Unknown whether any GP cash sits pari-passu with LPs. 🔴 Unverified.
- **Realized net-to-LP track record:** none provided. "Never had a loss" is an unverifiable absolute: no period, no loan count, no default or modification data. A lender that has never booked a loss either has not been through a stress period, has extended or modified loans instead of recognizing losses, or has a very short record. Each needs checking. 🔴 Unverified.
- **Waterfall alignment:** undisclosed. If a performance fee exists with no hurdle, the GP is paid on yield regardless of credit outcomes (`02`: no-hurdle promote is aggressive). 🔴
- **Affiliate fees:** unknown. Origination points are borrower-paid and should flow into fund yield (`02`); if the GP keeps them, the GP is paid on volume, not on credit quality. 🔴

## 8. Questions for the GP

**Must-ask**

| # | Question | Bad-answer signal | Ref |
|---|---|---|---|
| 1 | `Q-RISK-04` — "What is the average portfolio LTV on as-is value, not just ARV?" | Quotes only LTV-on-ARV; can't produce as-is LTV; "our borrowers always complete." | `HML-01` |
| 2 | `Q-RISK-05` — "What is your historical default rate and realized recovery rate, including through 2020 and 2022–23?" | Default without recovery (or vice versa); **"we've never had a loss"** (already given, so re-ask for the numbers); silence on 2022–23. | `HML-03`, `HML-04` |
| 3 | `Q-GP-02` — "Can you restate your track record as net-to-LP IRR on fully-realized, exited deals only?" | Only project-level or GP-level figures; "most loans are still performing"; can't separate realized from outstanding. | `GEN-14`, `GEN-05` |
| 4 | `Q-FEE-01` — "Can you provide the complete fee schedule and the full distribution waterfall?" | "Standard market fees"; partial list; "the PPM has it" without producing it. | `GEN-16` |
| 5 | `HML-02` response — "What is the geographic distribution of the loan book?" *(escalated: flag fired)* | Metro-wide statement with no submarket split; no concentration limit. | `HML-02` |
| 6 | `Q-GP-01` — "How much of your own capital is in this fund, on the same terms as LPs?" | "Our sweat equity is our investment"; co-invest via fee waiver; token amount on better terms. | `GEN-01` |
| 7 | `Q-GP-03` — "Have you or your principals faced any regulatory action, enforcement, or investor litigation?" | "Nothing material"; blames LP/regulator; a search surfaces something undisclosed. | `GEN-02` |
| 8 | `Q-RISK-06` — "What is the fund's leverage ratio, and is the quoted LP IRR levered or unlevered?" *(asked because 11% net sits above the 8–10% category band)* | Won't disclose leverage; levered IRR presented as unlevered; "leverage is conservative" with no number. | (`CREDIT-01` analog) |
| 9 | `Q-FEE-02` — "Which service providers are GP-affiliated, what do they charge, and who keeps origination points, late fees, and default interest?" | "All arm's-length" without naming providers; points or default interest go to the GP; no benchmark. | `GEN-06` |
| 10 | `Q-DS-03` — "What is the return under a bear case — a Phoenix flip slowdown with elevated defaults?" | "We underwrite conservatively" with nothing to show; the bear case is still 11%. | `GEN-13` |
| 11 | `Q-DIST-01` — "What is the projected distribution schedule, and what gates it?" | "We distribute when the fund supports it"; no frequency; silence. | `GEN-11` |
| 12 | `Q-LIQ-01` — "What are my options if I need to exit before the fund term ends?" | "We'll try to accommodate"; redemption rights undescribed; silence. | — |

**Nice-to-ask**

| # | Question | Bad-answer signal | Ref |
|---|---|---|---|
| 13 | `HML-05` response — "Does the management fee step down after the investment period?" | Full fee on committed capital through wind-down. | `HML-05` |
| 14 | `Q-GP-04` — "How have headcount and loan-monitoring capacity grown alongside AUM?" | AUM grew, team flat; no named asset manager / workout lead. | `GEN-04` |
| 15 | `Q-LIQ-02` — "When are K-1s delivered, and have they historically arrived before the filing deadline?" | "As soon as we can"; history of extensions. | — |

## 9. Diligence Checklist

- [ ] Obtain the PPM / operating agreement; reconcile fees and waterfall against any verbal answers.
- [ ] Identify the sponsor and principals; run a regulatory, enforcement, and litigation background search (`GEN-02`).
- [ ] If RIA-managed, pull the SEC Form ADV Part 2 fee schedule (`02` provenance).
- [ ] Request a loan tape: every loan's as-is value, ARV, LTV on both, status, extensions/modifications, and resolution. Verify the "no loss" claim at the loan level.
- [ ] Sample-verify as-is valuations against third-party appraisals or broker opinions for a subset of loans.
- [ ] Obtain audited fund financials (if any exist) and confirm loan-loss reserves and modification accounting.
- [ ] Confirm lien position (first-lien senior secured) and title/insurance practice on a sample of loans.
- [ ] Confirm any fund-level credit facility with the lender directly: size, covenants, recourse.
- [ ] Reference-check prior LPs on distribution consistency and redemption experience.

## 10. Verdict

**Pass as presented — insufficient disclosure.**

**Reasoning.** For a hard money / bridge fund, the core return story is *yield minus credit losses minus fees*. This offering discloses the yield target only. It withholds all four other `01` essentials that decide whether that yield survives (as-is LTV, default rate, recovery, sponsor history through a downturn) and every fee. What *is* disclosed points the wrong way: a target above the category's net band, a leverage figure whose basis is likely ARV, a single-metro book, and a perfect-record claim the question bank lists as a bad answer. The benchmark math clears easily (≈617 bps over HYG) — but it clears on an unverified number, and on a debt fund an above-category premium is more likely paid-for risk than free return.

**Biggest swing factor:** LTV basis. At 70% of *as-is* value this is a conventional senior-secured book with a real cushion. At 70% of *ARV*, a failed flip leaves the fund lending at or above current value in one metro, and the "never had a loss" record simply means the stress hasn't arrived yet.

**Who it could suit (if the answers come back clean):** an LP wanting short-duration, income-oriented real-estate credit who accepts single-metro concentration and has confirmed liquidity terms fit their needs.

**What would have to be true to re-screen toward Pursue with conditions:**
1. As-is LTV averages within the `01` 65–75% range *on as-is*, not just ARV.
2. Written default and recovery history covering 2020 and 2022–23, with loan-level support, including extensions and modifications.
3. Full fee schedule showing how 11% net reconciles from gross yield — with no undisclosed fund leverage, or leverage disclosed and sized.
4. Named sponsor with a clean background check and meaningful pari-passu co-invest.
5. Stated fund term, distribution frequency, and redemption mechanics.
