# Eval fixture 13 — Diversified BDC-style private credit fund (clean)
*Iteration-4 run, 2026-09-27, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 1c7faff.*

**Verdict: Pursue.** This is a structurally sound private credit fund. It discloses what `01` says a private credit fund should: leverage, loan count, sector mix, and through-cycle default *and* recovery. Leverage is moderate (~1.1x, under the 1.5x line in `02`/`03`), and it shows the unlevered IRR next to the levered one. That is the exact disclosure `CREDIT-01` exists to force. No RED flag fires. The one real economic finding is the **fee base**. A 1.5% fee on *gross assets* at 1.1x leverage works out to **~310 bps/yr on your equity**, not 150. The levered net IRR already absorbs this, so it is not a hidden cost. It does matter when you compare this fund to anything that charges on equity. **Biggest swing factor:** the gap between the levered and unlevered net IRR. That gap shows how much of the premium over HYG comes from the loan book and how much from the 1.1x leverage.

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Private Credit (fund) 🟢 |
| Deal type | Private credit fund, BDC-style (fund-level leverage) 🟢 |
| Sponsor | Not stated |
| Geography | Not stated (sector-diversified; geographic mix not given) |
| Minimum investment | Not stated |
| Hold / lock-up | Not stated. `01` baseline is 3–7 yrs. Whether the fund has a finite term or is evergreen is also not stated |
| Raise / fund size | Not stated ("large") |
| Claimed return | Net IRR, levered, with the unlevered figure shown. **The figures themselves were not in what you pasted** |
| Management fee | 1.5% of gross assets; 1.0% on assets beyond the 200% asset-coverage threshold 🟢 |
| Incentive fee | Two-part, with a hurdle and a high-water mark. Rates, hurdle level and catch-up not stated |
| Fund leverage | ~1.1x, disclosed, within the standard range 🟢 |
| Portfolio | 400+ loans, diversified across sectors 🟢. Average loan size and seniority not stated |
| Credit history | Through-cycle default and recovery rates disclosed 🟢 (figures not pasted) |

## 2. Return Stress-Test

You didn't paste the net IRR figure, so I benchmarked the `01` private credit range (8–12% net). The swing assumptions are:

1. **Credit loss rate** (default rate × (1 − recovery)).
2. **Leverage amplification.** At 1.1x, gross assets ≈ 2.1x equity. So each **100 bps of annual credit loss on the loan book costs ≈ 210 bps of NAV** 🟡 (arithmetic from the disclosed leverage).
3. **Rate path.** This moves both the coupons on the book and the fund's own borrowing cost. Whether the loans are floating-rate is not stated.

| Case | Net-to-LP IRR (assumed) | vs HYG 4.83% (10yr) | 5-yr hurdle ~300–400 bps | Read |
|---|---|---|---|---|
| Bear: `01` low end; losses run above the disclosed through-cycle rate | 8% | +317 bps | Lower half of band | **Clears (thin)** |
| Base: `01` midpoint | 10% | +517 bps | Above band | Clears comfortably |
| Bull: `01` high end | 12% | +717 bps | Above band | Clears comfortably |

*(`scripts/benchmark_comparator.py --deal-type private-credit --net-irr {8,10,12} --hold-years 5`, all exit 0. Hold of 5 yrs is 🔴 assumed.)*

- **Break-even:** the stated levered net IRR needs to be **≥ ~7.8%** (HYG + 300 bps) to pay for a 5-yr lock-up, and ~8.8% to reach the top of the band. Below that, the lock-up goes unpaid 🟢 (`05` framework).
- **Treasury floor:** the 2yr sits at 4.87%, so the credit-plus-illiquidity spread the LP is paid is ≈313–713 bps across the range. At this snapshot the Treasury is the tighter floor (it pays more than HYG's trailing 10yr). Read the net IRR against it too 🟢 (`05`).
- **Run the same test on the unlevered figure.** If the *unlevered* net IRR alone clears HYG + ~300 bps, the loan book earns its premium. If only the levered figure clears, the premium over the lock-up is being made by leverage (the `CREDIT-01` / `GEN-07` mechanism). That is disclosed and moderate here, but it is still a financing contribution.
- **Caveat on "low volatility":** private credit vehicles report smoothed marks, so their apparent low volatility understates the true risk 🟢 (`05` → PRIV note). HYG's −34% worst drop (2008) is the honest reminder that credit is not crash-proof.

## 3. Where LP Returns Come From

- **Cash flow, not exit.** This is a loan book: the return is contractual interest income less credit losses. No terminal-value or exit-cap assumption drives it, so **`GEN-08` (exit-dependent IRR) and `EQUITY-06` do not apply** 🟢.
- **Leverage contribution is real but bounded and visible.** At ~1.1x, part of the levered IRR is spread earned on borrowed money. The fund shows both figures, so you can measure that contribution directly instead of estimating it. The `CREDIT-01` / `GEN-07` question is answered by disclosure, not left as an assertion 🟢. It crosses the >60% "leverage-driven" line only if the levered figure is more than roughly 2.5x the unlevered one. That is implausible at 1.1x, but check it once you have both numbers 🟡.
- **Diversification does the protecting.** 400+ loans across sectors means no single default is material. The tail risk is correlated default in a downturn, which is exactly what the through-cycle default and recovery history is there to evidence.

## 4. Fee Stack Summary

| Fee | As disclosed | `02` norm | LP-equity equivalent | Note |
|---|---|---|---|---|
| Management fee | 1.5% of gross assets; 1.0% beyond 200% asset coverage | 1–2% of committed/invested capital; aggressive >2% | **≈3.1% of NAV/yr** 🟡 | At 1.1x: equity E, gross assets 2.1E. 2.0E × 1.5% + 0.1E × 1.0% = 3.1% of E |
| Incentive fee | Two-part (income + capital gains), hurdle, HWM | 10–20% above 5–7% hurdle; usually with HWM; soft hurdle + 100% catch-up is aggressive | Not computable (rates not stated) | Hurdle and HWM present 🟢. Rate, hurdle level, and hard vs soft/catch-up unknown |
| Servicing | Not stated | 0.25–0.5% of loan balance | — | Ask whether it is charged, and to whom |
| Fund-level leverage cost | Implied by 1.1x | *Variable*; flag >1.5x | Inside the levered return | Disclosed; under the threshold |
| Admin / IR | Not stated | $1–3k/LP or 0.1–0.3% | — | Ask |

**Gross-to-net drag:**

- **~310 bps/yr from the disclosed management fee alone.** (`fee_drag_calculator.py --gross-irr 14 --hold-years 5 --fund-mgmt-fee 3.1`, with every undisclosed fee set to 0.) The result: 14.0% → 10.9%, 310 bps.
- **~480 bps/yr with an illustrative incentive fee** of 15% over a 6% hurdle with 100% catch-up. (Same command plus `--carry 15 --hurdle 6 --catch-up 100`.) The result: 14.0% → 9.2%, 479 bps, of which 169 bps is incentive fee.
- The 14% gross, 5-yr hold and incentive terms are 🔴 **assumed** (§6 gaps). The script models carry at fund level, which only approximates a quarterly income incentive fee.

**What this means:**

- **The headline 1.5% is in `02`'s range. The base is not.** Restated on the equity base `02` uses, it is ~3.1%, well past the >2% aggressive line. This is the conventional BDC fee base, and the net IRR already reflects it. Use it when you compare this fund to an unlevered or equity-base-fee credit fund, where "1.5%" means half the drag.
- **Alignment effect:** a fee on gross assets pays the manager more for adding leverage. The tiered 1.0% rate beyond the 200% threshold is a real mitigant 🟢. It cuts, but does not remove, the manager's incentive to lever up.
- **No step-down (`HML-05`):** not triggered on a time basis. This is a BDC-style vehicle, and the leverage tier plays the step-down role. If the fund has a finite term, ask what happens to the fee during wind-down.

## 5. Red Flags

**RED:** none.

**YELLOW:**
- **Fee base on gross assets (no `03` ID; `02` fee finding).** The equity-equivalent management fee is ~3.1% and it rises with leverage. Exposure: ~310 bps/yr of drag, plus a structural incentive to lever up, capped only by the leverage tier. → `Q-FEE-01`.
- **`GEN-11` — distribution schedule not disclosed.** An IRR is quoted with no distribution cadence or reinvestment policy. Income funds normally distribute quarterly; confirm it, and confirm whether DRIP is the default. → `Q-DIST-01`.
- **`GEN-17` — one essential `01` disclosure absent: seniority position.** Loan count and sector mix are given; first-lien vs second-lien/unitranche share and average loan size are not. Seniority drives the recovery rate. → `Q-RISK-05` (read the recovery figure by lien), plus a direct seniority question.

**Considered and cleared (cited so the reasoning is visible):**
- `CREDIT-01` (fund leverage stacked on loan leverage): ~1.1x is under the 1.5x line, and the levered/unlevered basis is disclosed. **Cleared by disclosure.** The residual is the §2 test of the unlevered figure against HYG. `GEN-07` (financing story) is cleared on the same evidence.
- `CREDIT-02` (sector concentration): 400+ loans across sectors. Cleared, subject to confirming the single-largest-sector share.
- `HML-03` / `HML-04` (default / recovery undisclosed): both disclosed, through-cycle. Cleared. Check the recovery figure against `01`'s ~60–80% historical range.
- `HML-05` (no fee step-down): not applicable on a time basis; see §4.
- `GEN-01`, `GEN-05`, `GEN-14`: **not fired, but unverified.** Co-investment and track record are simply absent from what you pasted (§6, §7). Their questions stay must-ask.
- `GEN-08`, `EQUITY-06`, `GEN-09`, `GEN-10`, `EQUITY-01`/`02`: not applicable (no exit cap, no single-asset debt maturity, no rate-cap structure, no property waterfall).

No clusters.

## 6. Missing Disclosures

Against the `01` Private Credit baseline and the `02` private credit fee inventory:

- **The actual figures:** the levered and unlevered net IRR, the default and recovery rates, and the leverage cost. These are described as disclosed but weren't in what you pasted. §2 and §4 run on assumed inputs until you have them.
- **Seniority position** (`01` essential): the lien mix.
- **Average loan size** (`01` essential) and the single-largest-sector exposure.
- **Incentive fee terms:** the rate on each part, the hurdle level, hard vs soft hurdle, catch-up %, and whether the high-water mark is a lookback or total-return test.
- **Servicing, admin/IR, and fund operating expenses.**
- **Hold / term / liquidity:** finite-life vs evergreen, and any redemption program with its gates.
- **Distribution schedule and DRIP policy** (`GEN-11`).
- **Sponsor identity, GP co-investment, and a realized net-to-LP track record.**
- **Minimum investment and fund size.**

None of these are gaps in the core return story. The structure, leverage, diversification, and credit history are all disclosed. They are items to confirm, not reasons to stop.

## 7. GP Alignment

- **Co-invest:** not stated. **Unverified** (`GEN-01` → `Q-GP-01`).
- **Track record:** not stated. The fund discloses through-cycle default and recovery, which is loan-level credit performance. That is a strong sign, but it is not the same as a **realized net-to-LP return** record. **Unverified** until you see it (`GEN-05` / `GEN-14` → `Q-GP-02`).
- **Incentive structure:** a hurdle plus a high-water mark is the LP-favorable form per `02`: no incentive fee on recouped losses 🟢. The unknown is the catch-up.
- **Fee-base alignment:** mixed. The gross-asset base rewards leverage; the 1.0% tier beyond 200% coverage tempers it (§4).
- **Affiliate fees:** not stated. Ask who services the loans and whether servicing or origination fees go to affiliates (`GEN-06` → `Q-FEE-02`).

## 8. Questions for the GP

**Must-ask**

| ID | Question | Bad-answer signal |
|---|---|---|
| `Q-RISK-06` (`CREDIT-01`) | "Confirm the fund's leverage ratio, the levered and unlevered net IRR to LPs, and the all-in cost of the fund's borrowing." | Won't give the unlevered number in writing, or gives it gross of fees. "Leverage is conservative" with no cost-of-debt figure. |
| `Q-RISK-05` (`HML-03`, `HML-04`) | "Give me the historical default rate and realized recovery rate, including 2020 and 2022–23, split by lien position." | Default without recovery (or vice versa). "We've never had a loss." Silence on 2022–23. Recovery not split by lien. |
| `Q-FEE-01` | "Provide the complete fee schedule: the incentive fee rate on each part, the hurdle level, hard or soft, the catch-up %, how the high-water mark works, and all servicing, admin and operating expenses. Restate the total as a % of NAV." | "Standard BDC fees." Won't restate on NAV. Operating expenses surface only in the PPM. |
| `Q-DIST-01` (`GEN-11`) | "What is the distribution cadence, and is DRIP the default?" | "We distribute when the portfolio supports it," with no cadence. An IRR quoted with no distribution timing. |
| `Q-GP-01` (`GEN-01`) | "How much of your own capital is in the fund, on the same terms as LPs?" | Co-invest is a fee waiver, not cash. A token amount, or better terms than LPs. |
| `Q-GP-02` (`GEN-05`, `GEN-14`) | "Restate your track record as net-to-LP IRR on fully realized, prior credit vehicles." | Offers only gross portfolio yield or marked NAV. "Most funds are still performing." |
| `Q-GP-03` (`GEN-02`) | "Any regulatory action, enforcement, or investor litigation?" | "Nothing material." A search surfaces something they didn't disclose. |
| `Q-LIQ-01` | "What are my options if I need to exit before the term ends? Is there a redemption program, and how is it gated?" | "A secondary market may develop." Redemption limits buried or undisclosed. |
| `Q-FEE-02` (`GEN-06`) | "Which service providers (servicing, origination, administration) are GP-affiliated, and what do they charge?" | "All arm's-length," without naming the providers. |

**Nice-to-ask**

| ID | Question | Bad-answer signal |
|---|---|---|
| `CREDIT-02` probe (per `03` response) | "What is your single-largest-sector exposure?" | Won't give the top sector's share; "diversified" is the whole answer. |
| `GEN-17` probe (per `03` response; `01` essential) | "What share of the book is first-lien senior secured, and what is the average loan size?" | Won't split by lien; averages hide a long tail of large loans. |
| `Q-GP-04` | "How has your credit and workout team grown alongside AUM?" | AUM multiplied while the team stayed flat. No named workout lead. |
| `Q-LIQ-02` | "When are K-1s delivered, and have you met that historically?" | A history of extensions. |

## 9. Diligence Checklist

- **Fund documents:** confirm the fee base (gross assets), the leverage tier, the incentive-fee mechanics and high-water mark, the leverage limits, and redemption or term provisions.
- **Audited financials:** check the audited default, non-accrual and realized-loss history against the marketed through-cycle figures, and look at the valuation policy for Level 3 marks (smoothed-mark caveat, `05`).
- **Leverage facilities:** lender, cost, covenants, and what happens to LP distributions if a covenant or the asset-coverage test is breached.
- **Background and regulatory check** on the adviser and its principals (Form ADV Part 2 for the fee schedule; `02` provenance).
- **Portfolio tape:** lien mix, largest positions, sector concentration, and loans on the watch list.
- **Independent administrator and auditor:** confirm both are third-party.

## 10. Verdict

**Pursue.**

- **Why:** the structure checks every box `01` and `03` set for private credit. Leverage is disclosed and moderate (~1.1x < 1.5x). The IRR basis is transparent (levered and unlevered both shown). The book is granular (400+ loans, sector-diversified). The credit history is disclosed through the cycle, with recovery alongside default, and the incentive fee has a hurdle and a high-water mark. Returns come from contractual income, not an exit bet. No RED flag fires. Across the `01` range (8–12% net), the fund clears HYG plus a 5-yr illiquidity hurdle, thinly at the low end and comfortably from the midpoint up.
- **Biggest swing factor:** the levered vs unlevered net IRR. If the unlevered figure alone clears ~7.8% (HYG + 300 bps), the loan book earns the premium and leverage is upside. If only the levered figure clears, you are being paid mainly for 1.1x leverage. That is fine, but then the ~2.1x NAV sensitivity to credit losses is the risk you're really underwriting.
- **Secondary:** the ~3.1%-of-NAV management fee. It is conventional for this structure and already inside the net IRR, but it is double what "1.5%" suggests. It also makes the net IRR sensitive to any drift upward in leverage.
- **Who it suits:** an income-oriented LP who wants senior-secured-style credit exposure, can accept the lock-up (term and liquidity to be confirmed, `Q-LIQ-01`), and understands that marked NAV understates volatility.
- **What would have to be true:**
  1. The stated levered net IRR is ≥ ~8% (the thin-clear line) and the unlevered figure is in the same neighborhood as the comparator plus hurdle.
  2. Realized recovery is within `01`'s ~60–80% band, and the book is predominantly first-lien.
  3. The hurdle is meaningful (≥5% per `02`) and the catch-up isn't a soft hurdle with 100% catch-up.
  4. The GP's realized net-to-LP record and co-invest check out.

  A miss on (1) or on the unlevered test downgrades this to Pass on price. Misses on (2)–(4) are negotiating points, not deal-breakers, unless the realized record doesn't exist.
