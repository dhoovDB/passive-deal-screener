# Eval fixture 12 — Multifamily value-add, LP-aligned structure (clean case)

*Iteration-1 run, 2026-07-03, against SKILL.md @ cddc52d. Fixture prompt: evals.json id 12.*

---

**Verdict: Pursue.** This deal's structure reads like a checklist of LP protections done right: real cash co-invest on LP terms, whole-of-fund waterfall with a secured clawback, cumulative *compounding* pref, market fees, a realized net-to-LP track record, fixed-rate debt outliving the plan, and a flat exit cap. The screen's job on a deal like this is to say so — and to keep the remaining questions proportionate: they are clarifying, not disqualifying.

## 1. Deal Snapshot
- **Asset class:** Multifamily — value-add 🟢
- **Deal type:** Equity syndication 🟢
- **Sponsor:** Not named in summary, but profile disclosed: 10% cash co-invest pari-passu; five fully-exited deals with net-to-LP IRRs 🟢
- **Geography / Minimum / Raise / Hold:** Not stated (hold implied by "planned exit")
- **Claimed return:** **Not stated** — notable and, unusually, a *good* sign of restraint in a summary; needs the number for benchmarking 🟡
- **Structure:** Whole-of-fund waterfall, secured clawback, 8% cumulative compounding pref, 20% promote 🟢
- **Debt:** Fixed-rate, matures **two years after** planned exit 🟢

## 2. Return Stress-Test
No projected IRR was stated, so the quantitative test waits on it. What can be said structurally:
- The deal *provides* a downside sensitivity 🟢 (`GEN-13` defused) — review its assumptions (does the bear case stress exit cap and rents together?).
- Exit cap = going-in cap 🟢: no baked-in compression (`EQUITY-06` defused); any exit upside is conservatism, not dependency.
- Fixed-rate debt through exit + 2 years 🟢: no rate-cap cliff, no maturity wall, no forced-refi scenario (`GEN-09`/`GEN-10` defused). A delayed exit has runway.
- Baseline (`01`): value-add targets 12–18% net; when the projection arrives, test it against the realized five-exit record and `05` (VNQ 6.47% + ~300–400bps hurdle for a typical 5–7yr hold).

## 3. Where LP Returns Come From
Not decomposable without the pro forma — but the structure removes the usual distortions: with a flat exit cap and fixed debt, the projection can't be manufactured from cap compression or a rate bet, so whatever IRR is claimed must come predominantly from the value-add rent delta (operations). Confirm the split with Q-DS-01 when the number arrives.

## 4. Fee Stack Summary
Per `02` (equity syndication inventory) — all disclosed fees in range, one below:

| Fee | Stated | `02` range | Read |
|---|---|---|---|
| Acquisition | 1% | 1–2% | Low end 🟢 |
| Asset management | 1.5% annual | 1–2% | In range 🟢 |
| Disposition | 1% | 0.5–1% | Top of range, in range 🟢 |
| Promote | 20% over 8% pref | 15–30% over 6–10% | Market 🟢 |
| Pref mechanics | Cumulative, compounding | Cumulative standard; compounding is LP-favorable | Better than typical 🟢 |

Estimated total drag ≈ 350–400bps on a mid-teens gross (verify with `scripts/fee_drag_calculator.py` once gross is known). Not disclosed: admin/IR, loan placement, catch-up rate — ordinary clarifications (§8).

## 5. Red Flags
**None RED. None YELLOW on the disclosed facts.** For discipline, what was checked and cleared:
- `GEN-01` co-invest → **defused** (10% cash, pari-passu — meaningful, on-terms)
- `EQUITY-01`/`EQUITY-02` waterfall → **defused** (whole-of-fund + secured clawback — the institutional-grade pairing)
- `EQUITY-04`/`EQUITY-05` pref → **defused** (8%, cumulative, compounding)
- `EQUITY-06` exit cap → **defused** (flat to going-in)
- `GEN-09`/`GEN-10` debt → **defused** (fixed-rate, maturity outside plan + 2yrs)
- `GEN-05`/`GEN-14` track record → **defused in form** (realized, net-to-LP, five exits) — the *numbers* still need reading (§7)
- `GEN-12`/`GEN-13`/`GEN-15` financials → **defused** (T-12, rent roll, downside case provided)

Open clarifications (not flags): affiliate relationships not addressed either way; projected return and market not yet stated; distribution schedule unstated.

## 6. Missing Disclosures
Short list, ordinary in kind: projected return and hold; market/submarket data behind the rent thesis; distribution schedule (`GEN-11` — ask, don't assume); affiliate service-provider map; catch-up rate; the five exits' actual figures (disclosed as existing — request the numbers).

## 7. GP Alignment
Strong as disclosed: 10% cash co-invest pari-passu is at the high end of market practice; whole-of-fund + secured clawback aligns promote with final LP outcomes rather than interim wins; realized net-to-LP disclosure is the honest form of a track record. Remaining verification: read the five exit IRRs against this deal's (forthcoming) projection — a GP projecting far above its own realized record reopens the question.

## 8. Questions for the GP
**Clarifying tier (no must-ask/bad-answer escalation is warranted on these facts):**
1. Projected net-to-LP IRR and hold — for the `05` benchmark test and comparison to the realized record.
2. **Q-MKT-01** — submarket supply/absorption behind the rent-growth assumption.
3. **Q-DIST-01** — distribution schedule and first-distribution milestone.
4. **Q-FEE-02** — any GP-affiliated service providers, and their benchmarking (unaddressed in the summary, not adverse).
5. The downside case's assumptions — confirm it stresses exit cap and rents jointly.
6. Catch-up rate within the promote (affects drag modestly).

## 9. Diligence Checklist
Standard verification, no red-flag chases: PPM vs summary terms (waterfall, clawback security, pref mechanics); T-12/rent roll review; the five exits verified (dates, sizes, net-to-LP); background check on principals; lender docs confirming rate/maturity.

## 10. Verdict
**Pursue.** The deal presents the alignment structure LPs are told to demand and rarely get: cash co-invest on their terms, a waterfall that pays the GP last, a compounding pref, boring fixed debt with room past the exit, a flat exit cap, and a track record in the only form that counts (realized, net-to-LP). The screen's remaining work is confirmation — the projection number, the submarket evidence, the PPM matching the summary — not investigation. Biggest swing factor: the value-add rent thesis vs its submarket (Q-MKT-01), which is the one place a clean structure can still hold a soft deal. Suits an LP wanting equity real-estate exposure with institutional-grade terms; the structure prices patience, not luck.
