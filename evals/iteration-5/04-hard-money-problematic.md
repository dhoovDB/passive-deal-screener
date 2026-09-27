# Eval fixture 04 — Phoenix fix-and-flip bridge fund (thin, problematic)
*Iteration-5 run, 2026-09-27, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 7712624.*

**Verdict: Pass as presented — insufficient disclosure.** The pitch gives four claims (11% net target, "70% LTV," Phoenix fix-and-flip, "never had a loss") and none of the essential disclosures a hard-money fund normally carries (`01`): no as-is LTV, no default or recovery history, no fees, no fund term, no track record in numbers. What little is disclosed raises more questions than it answers: the 11% *net* target sits above the category's 8–10% net norm and at the midpoint of its 11–13% *gross* norm, and "we've never had a loss" is, word for word, the bad-answer signal the question bank lists for the default/recovery question (`Q-RISK-05`). Re-screen once the list in §10 comes back.

---

## 1. Deal Snapshot

| Field | Value | Tag |
|---|---|---|
| Asset class | Hard money / bridge loan (fix-and-flip residential) | 🟢 stated |
| Deal type | Hard money / bridge debt fund | 🟢 stated ("bridge fund") |
| Sponsor | Not stated (self-described "experienced team") | 🟢 |
| Geography | Phoenix metro, single metro | 🟢 stated |
| Minimum investment | Not stated | — |
| Hold / fund term | Not stated (category norm: 6–18 mo per loan, 3–5 yr fund, `01`) | — |
| Raise / fund size | Not stated | — |
| Claimed return | "Target 11% net" (whether IRR or yield, and whether fund-levered, not stated) | 🟢 stated / 🔴 basis unknown |
| LTV | "70%" (basis not stated: ARV or as-is?) | 🟢 stated / 🔴 basis unknown |
| Fees | Not stated | — |
| Distribution schedule / liquidity | Not stated | — |

## 2. Return Stress-Test

**Benchmark (claimed 11% net vs HYG 4.83% 10yr):** `scripts/benchmark_comparator.py`

- 11.00% net is **≈617bps over HYG** (4.83% 10yr). At a ≤1yr lock-up the illiquidity hurdle is ~200bps; at a 3–5yr fund lock-up (the category norm, because the term isn't stated) it is ~300–400bps. **On the headline number, it clears comfortably under either assumption.** 🟢 (script) / 🔴 (hold assumed)
- Over the duration-matched Treasury floor, it's ≈676bps over the 3mo bill (4.24%) or ≈613bps over the 2yr (4.87%). 🟢
- **Clearing the hurdle only tells you the pitch is priced right for what it promises. It says nothing about whether the promise holds.** The 11% is an unverified target, not a realized number, and it's quoted with no stated fees, so you can't tell whether it's really net (see §4).

**The above-norm problem.** `01` puts hard-money net-to-LP at **8–10%**, with 11–13% *gross* common. An 11% *net* target means one of three things, and the pitch doesn't say which: 🟡

1. **Higher gross loan yields.** That means riskier borrowers or higher LTVs, which contradicts the "conservative, never lost" framing.
2. **Fund-level leverage.** A credit line levering the loan book would inflate the LP number. This is the financing-story mechanism (`GEN-07`) in debt form.
3. **Fees below market, or not yet disclosed.** If they're undisclosed, the "net" is really a gross.

For scale: at a category-typical fund stack (1.5% annual management fee, 20% carry over an 8% hurdle, no catch-up; every input 🔴 assumed from `02` ranges), the fund needs **≈13.75% gross to deliver 11.0% net** (272bps/yr drag, `fee_drag_calculator.py`). That puts it at the top of the 11–13% gross range, or above it.

**Scenarios.** These are qualitative. No loan-level data exists to model them, and each is 🔴.

| Case | Swing assumptions | LP outcome |
|---|---|---|
| Bull | Flips complete on schedule; borrowers exit by sale or refi within term; defaults near zero; fees modest | ≈ Target 11% net, paid as current income |
| Base | Some defaults, cured through workouts at near-full recovery; extensions stretch loan duration | Below target. Default interest can partially offset it, *if* it flows to the fund and not to a GP "workout fee" (`02`) |
| Bear | Phoenix resale prices soften mid-renovation; flips stall; loans written at 70% of **ARV** turn out to be at or above as-is value (`01`: "an ARV-based 70% LTV can be 100%+ on current value") | Principal loss. The capped upside (coupon only) meets uncapped downside (the collateral shortfall). A single-metro book gives no offset (`HML-02`) |

**The 2–3 swing assumptions:** (1) the **LTV basis**, as-is vs ARV; (2) **default rate × recovery rate** through a stress period; (3) **fund leverage and fees**, i.e. how "net" the 11% really is.

## 3. Where LP Returns Come From

- **Cash flow: essentially all of it.** 🟡 A debt fund's return is the loan coupon plus borrower-paid origination points (`02`). There's no terminal value or exit cap, so `GEN-08` (exit-dependent IRR) doesn't apply. 🟢
- **The real risk is on the other side of the ledger.** Upside is capped at the coupon, and the downside is principal. The return depends on **loss avoidance**, and loss history is exactly what the pitch declines to quantify.
- **Leverage: unknown.** If the fund borrows against its loan book, part of the 11% is leverage, not lending skill. That's the debt-fund version of a financing story (`GEN-07`, probe only; not fired because no leverage is stated). You can't tell from this whether more than 60% of the return is leverage-driven. 🔴

## 4. Fee Stack Summary

**Gross-to-net drag: not computable from disclosure. That's the finding.** 🟢

| Fee (`02` hard money / bridge) | Norm | Disclosed? |
|---|---|---|
| Origination points (borrower-paid) | 1–3 pts; <1 is a yield flag, >5 is predatory | No |
| Fund management fee | 1–2% of AUM annual; >2.5% aggressive; step-down expected in long-dated funds | No |
| Servicing fee | 0.25–0.5% annual; >1% aggressive | No |
| Performance fee / carry | 10–20% over 5–8% hurdle; no hurdle is aggressive | No |
| Late fees / default interest | Should go to the fund, not the GP | No |
| Wind-down / liquidation | 0.5–1% of remaining AUM; >2% aggressive | No |
| Admin / K-1 | 0.1–0.5% or fixed $/LP | No |

- `fee_drag_calculator.py` with every undisclosed fee passed as `0` → **0 bps disclosed drag** (11.00% gross = 11.00% net). The zero is an artifact of non-disclosure, not a feature of the fund. 🟢
- Illustrative only: a category-typical stack (1.5% management fee + 20% carry over an 8% hurdle, no catch-up, 4-yr hold, every input 🔴 ASSUMED) implies **~259–272 bps/yr** drag (259 at 13% gross, 272 at 13.75%). If "11% net" is really the gross before a stack like that, the LP nets **≈8.3–8.4%**. That's back inside the category range and ≈350bps over HYG. This is a §6 gap, not a finding.

## 5. Red Flags

**RED (treat as RED until the answer moves it down)**

- **`HML-01` — "70% LTV" with no basis stated, on a fix-and-flip book.** 🟡 Fix-and-flip is the lending type `01` says is typically quoted on ARV. At 70% of ARV, a stalled renovation can leave the loan at or above as-is value, with no equity cushion. LP exposure: principal. → `Q-RISK-04`.
- **`GEN-14` — no track record in numbers** (the unrealized-only / no-realized-exits flag). 🟢 "Experienced team" and "never had a loss" come with no realized loan count, vintages, default rate, or net-to-LP returns. The track record is unverified; under the skepticism contract that counts as no track record. (`GEN-05` is probed parenthetically: any record produced must be net-to-LP, not gross loan yield.) → `Q-GP-02`.

**YELLOW–RED**

- **`HML-03` + `HML-04` — default and recovery rates not disclosed.** 🟢 "Never had a loss" is not a default rate and not a recovery rate. It's the exact dodge `04` names under `Q-RISK-05`. It can also be literally true while hiding defaults cured through extensions, loans rolled to avoid booking a loss, or losses absorbed by the GP to preserve the claim. Recovery rate is what separates a 2% default / 40% recovery book from a 5% / 90% one (`03` notes). → `Q-RISK-05`.
- **`GEN-16` — no fee or waterfall disclosure.** 🟢 The "net" is unverifiable (§4). → `Q-FEE-01`.
- **`GEN-15` (via `GEN-17`) — essential category disclosures absent.** 🟢 Average as-is LTV, default history, foreclosure/recovery process, geographic mix, and sponsor history through a downturn are the `01` hard-money baseline, and none is provided. → `Q-RISK-03`, `Q-RISK-04`, `Q-RISK-05`.

**YELLOW**

- **`HML-02` — single-metro concentration.** 🟢 The whole book is Phoenix metro, exposed to one local housing cycle, with no diversification offset. For fix-and-flip, the borrower's exit (resale) and the collateral value fall together. → `Q-RISK-05` stress-period answer; HML-02 has no dedicated `04` question, so ask it directly: *"What is the geographic distribution of the loan book?"*
- **`GEN-03` — marketing-heavy, substance-light.** 🟡 The pitch consists of assertions ("experienced," "never had a loss") standing in for data. → *"Can you provide the full underwriting model and the historical actuals behind these projections?"* (`03` response line; no dedicated `04` question).
- **`GEN-11` — return target with no distribution schedule.** 🟢 Monthly or quarterly income vs reinvested? When does capital return? → `Q-DIST-01`.
- **`GEN-13` — single-point target, no downside case.** 🟢 → `Q-DS-03` (adapted for debt: default spike, recovery haircut, extension wave).

**Cluster.** `HML-01` + `HML-03` + `HML-04` + `HML-02`: an unknown LTV basis, an unquantified loss history, and a single-metro book form one failure mode, not four separate gaps. The collateral cushion, the loss record, and the diversification are all unverifiable at once. The cluster reaches RED.

**Not fired (no 🟢/🟡 basis):** `GEN-01` (co-invest undisclosed, not shown to be zero), `GEN-06` (affiliates unknown), `HML-05` (fund term unknown), `GEN-02` (no information). All route to questions in §8.

## 6. Missing Disclosures

Against the `01` hard-money baseline and the `02` fee inventory:

1. Average portfolio LTV on **as-is** value (and on ARV), plus the basis of the quoted 70%
2. Historical **default rate**, including 2020 and 2022–23
3. Realized **recovery rate** and average workout / foreclosure timeline
4. Foreclosure process and who runs workouts
5. Geographic mix within Phoenix metro (submarkets) and any out-of-metro exposure
6. Sponsor history **through a downturn**, with loan count, vintages, and dollars lent
7. Complete **fee schedule** (management, servicing, carry/hurdle, origination-point policy, default-interest allocation, wind-down)
8. **Fund term**, lock-up, and redemption / liquidity terms
9. **Fund-level leverage** (credit line), and whether the 11% is levered
10. Return basis: IRR vs cash yield, and whether it's net of *all* fees
11. Distribution schedule and reinvestment policy
12. GP co-investment, amount and terms
13. Sponsor identity, and any regulatory / litigation history
14. Minimum investment and fund size / AUM

## 7. GP Alignment

- **Co-invest:** not disclosed. Unverified. 🔴
- **Track record:** no numbers, realized or otherwise. "Never had a loss" is an assertion, and **unverified** (`GEN-14`). Loan-level realized net-to-LP returns are the only acceptable form. 🟢
- **Fee/incentive alignment:** unknown. Whether carry sits above a hurdle, and whether default interest goes to LPs or to the GP, both determine whether the GP gains from a workout or from a clean repayment. 🔴
- **Affiliate fees:** unknown (e.g., whether origination points or servicing go to a GP affiliate rather than the fund). 🔴

## 8. Questions for the GP

**Must-ask**

| # | Question | Bad-answer signal | Cites |
|---|---|---|---|
| 1 | `Q-RISK-04`: "What is the average portfolio LTV on **as-is** value, not just ARV?" | Quotes only LTV-on-ARV; can't produce as-is LTV; "our borrowers always complete." | `HML-01` |
| 2 | `Q-RISK-05`: "What is your historical default rate and realized recovery rate, including through 2020 and 2022–23?" | Default without recovery (or the reverse); **"we've never had a loss"** (already given); silence on 2022–23. | `HML-03`, `HML-04` |
| 3 | `Q-GP-02`: "Restate your track record as net-to-LP returns on fully-realized loans only." | Gross loan yield or GP-level figures only; "most loans are still performing"; can't separate realized from outstanding. | `GEN-14`, `GEN-05` |
| 4 | `Q-FEE-01`: "Provide the complete fee schedule and the distribution waterfall." | "Standard market fees"; partial list; "the PPM has it" without producing it. | `GEN-16` |
| 5 | `Q-RISK-03` (adapted to a loan book): "Provide the loan tape: count, sizes, LTVs, maturities, extensions, and delinquencies." | "Confidential until you commit"; summary stats only. | `GEN-15`, `GEN-17` |
| 6 | `Q-DS-03` (adapted): "What happens to LP returns if defaults spike, recoveries fall, and half the book extends?" | "We underwrite conservatively" with nothing to show; no downside case exists. | `GEN-13` |
| 7 | `Q-DIST-01`: "What is the distribution schedule, and when does LP capital come back?" | "We distribute when the fund supports it"; no schedule. | `GEN-11` |
| 8 | `Q-GP-01`: "How much of your own capital is in the fund, on the same terms as LPs?" | "Our sweat equity is our investment"; token amount on better terms. | `GEN-01` |
| 9 | `Q-GP-03`: "Any regulatory action, enforcement, or investor litigation?" | "Nothing material"; a search surfaces something undisclosed. | `GEN-02` |
| 10 | `Q-LIQ-01`: "What are my options if I need to exit before the fund term ends?" | "We'll try to accommodate"; lock-up undisclosed. | — |
| 11 | *(escalated; above-norm return)* `Q-RISK-06` adapted: "Does the fund use a credit line or other leverage, and is the 11% levered or unlevered?" | Won't disclose leverage; "leverage is conservative" with no number. | probes `GEN-07` (and the `CREDIT-01` mechanism) |
| 12 | *(no `04` entry for `HML-02`)*: "What is the geographic distribution of the loan book within and beyond Phoenix metro?" | "Phoenix is a strong market" in place of a breakdown. | `HML-02` |

**Nice-to-ask**

| # | Question | Bad-answer signal | Cites |
|---|---|---|---|
| 13 | `Q-FEE-02`: "Which service providers (servicing, origination, workouts) are GP-affiliated, and what do they charge?" | "All arm's-length" without naming providers. | `GEN-06` |
| 14 | "Does the management fee step down after the investment period?" | No step-down on a multi-year term. | `HML-05` |
| 15 | `Q-GP-04`: "How have headcount and loan-monitoring capacity grown alongside AUM?" | AUM up, team flat; no named asset manager. | `GEN-04` |
| 16 | `Q-LIQ-02`: "When are K-1s delivered, and have they been on time historically?" | "As soon as we can"; a history of extensions. | — |

## 9. Diligence Checklist

- PPM / operating agreement: fee schedule, carry, hurdle, default-interest allocation, leverage limits, redemption terms
- Loan tape, independently reconciled to audited financials (ask whether the fund is audited, and by whom)
- Background and regulatory check on principals (SEC / FINRA / state; Arizona lending license status); court search for investor litigation and foreclosure filings
- Independent verification of "never had a loss": foreclosure and REO records against the fund's lending history
- Sample loan files: appraisal / BPO basis for the as-is value vs ARV, draw-control process
- Credit-line lender terms, if any fund leverage exists
- LP references, ideally investors who were in the fund through 2022–23

## 10. Verdict

**Pass as presented — insufficient disclosure.**

- **Why not a merits verdict:** the core return story of a debt fund is *coupon minus losses minus fees*. None of the three is disclosed: no loan pricing, no loss history (only an assertion), no fees. The essential `01` disclosures are **substantially** absent, so the 11% can't be underwritten, only repeated.
- **Biggest swing factor:** the **as-is LTV** (`HML-01`). At 70% of as-is value, a Phoenix fix-and-flip book has a real cushion and the 11% could be a well-priced senior loan. At 70% of ARV, the cushion can be zero, and the "never had a loss" record is a bull-market artifact waiting for its first stall.
- **What would have to be true to re-screen as Pursue with conditions:** (1) as-is LTV disclosed and credibly ≤75%; (2) loan-level default and recovery history through 2020 and 2022–23, independently verifiable; (3) a full fee schedule under which 11% survives as a true net, *or* the target restated honestly into the 8–10% norm; (4) fund leverage disclosed and modest; (5) meaningful GP co-invest.
- **Who it could suit, if it clears:** an LP who wants current income, accepts single-metro residential credit risk, and can hold a multi-year lock-up. It would be a satellite position, sized so that a Phoenix housing correction doesn't impair the core portfolio. It should not substitute for diversified credit (HYG spreads its risk across hundreds of issuers; this fund carries one metro's).
