# Eval fixture 08 — Multifamily syndication, multi-flag sponsor

*Iteration-1 run, 2026-07-03, against SKILL.md @ cddc52d. Fixture prompt: evals.json id 8.*

---

**Verdict: Pass.** Six RED flags fire on seven sentences of disclosure — alignment, conduct, structure, debt, and track record each fail independently. Any one of GEN-01, GEN-02, or the EQUITY-01/02 + 50%-promote structure is pass-or-resolve on its own; together they are not a deal with questions, they are a profile with a deal attached. No diligence path resolves this — several flags are facts, not gaps.

## 1. Deal Snapshot
- **Asset class:** Multifamily (segment not stated) 🟡
- **Deal type:** Equity syndication, single asset 🟢
- **Sponsor:** Not named — but one principal was named in a **prior SEC action** 🟢
- **Geography / Minimum / Raise / Hold / Claimed return:** Not stated
- **Structure:** American (deal-by-deal) waterfall, **50% promote**, **no clawback**; preferred return **not mentioned** 🔴
- **Debt:** Floating rate; **rate cap expires in 12 months; loan matures 2028** 🟢
- **Co-invest:** Zero ("our expertise is our investment") 🟢
- **Track record:** All current, unrealized marks 🟢

## 2. Return Stress-Test
No projected return was even stated — only that projections "show only an upside case" (`GEN-13`). There is nothing to stress-test, and that is the finding: a single-scenario pro forma from a sponsor with these structural terms is a sales document, not underwriting. The one computable stress is the debt (see §5, `GEN-10`): when the rate cap expires ~12 months in with the loan running to 2028, debt service floats uncapped for the remaining term — the 2022–24 syndication-failure pattern with the dates already visible.

## 3. Where LP Returns Come From
Not decomposable — no return figure, no distribution schedule, no cash-flow split. Structurally, a 50% promote means that above the (unstated) pref, **half of every marginal dollar goes to a GP with zero dollars in** — the LP carries all the capital risk for half the marginal return. Whatever the source of returns, the waterfall reroutes it.

## 4. Fee Stack Summary
**Not computable** (`GEN-16`, partial): no fee schedule disclosed; the waterfall is disclosed only enough to alarm. What is known:

| Element | Stated | `02` norm | Read |
|---|---|---|---|
| Promote | **50%** | 15–30%; >30% aggressive | Far beyond the aggressive threshold 🔴 |
| Waterfall | Deal-by-deal (American) | Standard in retail RE | RED *in combination* — see below |
| Clawback | **None** | Expected in deal-by-deal | 🔴 |
| Preferred return | Not mentioned | 6–10% | If absent → `EQUITY-04` 🔴 |
| All other fees | Not stated | — | Unknown |

## 5. Red Flags
**RED — each independently pass-or-resolve:**
- `GEN-01` — Zero GP co-investment; "our expertise is our investment" is verbatim the bad-answer signal for Q-GP-01. Fees and 50% promote accrue regardless of LP outcome; alignment is asserted, not structural.
- `GEN-02` — Principal named in a prior SEC action. Disclosed or discovered, it is a conduct history on the record.
- `EQUITY-01` — Deal-by-deal waterfall **with a 50% promote** — promote at 2–3× the `02` ceiling, taken deal-by-deal.
- `EQUITY-02` — **No clawback** in that deal-by-deal structure: promote banked on any early success is never returnable, even if the LP is later impaired. (Single-asset softens the multi-deal sequencing risk but a refi-then-sale still creates multiple promote events with nothing recoverable.)
- `GEN-10` — Rate cap expires in ~12 months; loan matures 2028. After expiry, debt service floats uncapped for years — the specific 2022–24 pattern (`03`: cap expires → rates stay elevated → distributions erased → capital call). The expiry-vs-maturity gap is stated in the materials themselves.
- `GEN-14` — Track record is entirely unrealized marks: self-reported, unexited, unproven. Per the contract: no track record.

**YELLOW / YELLOW–RED**
- `GEN-13` — Upside-only projections.
- `EQUITY-04` (YELLOW–RED) — No preferred return mentioned; if there is none beneath a 50% promote, the LP has no priority cushion at all.
- `GEN-16` (YELLOW–RED) — No fee schedule.

**Cluster note:** `GEN-14` + zero co-invest + SEC history + upside-only projections is the alignment-and-conduct cluster at full strength: nothing the sponsor has shown is verified, and nothing the sponsor risks is real.

## 6. Missing Disclosures
- Preferred return — existence and terms
- Complete fee schedule (`GEN-16`)
- The SEC action: which principal, what conduct, what resolution
- Realized track record — any exited deal, net-to-LP (`GEN-14`)
- Return projection basis, downside case (`GEN-13`)
- Rate-cap replacement cost for the post-expiry gap
- Sponsor entity, raise, hold, minimum, distribution schedule

## 7. GP Alignment
The deal's core failure. Zero cash at risk (`GEN-01`), a regulatory history (`GEN-02`), an unrealized-only record (`GEN-14`), and a 50% deal-by-deal promote with no clawback (`EQUITY-01/02`) — every alignment mechanism an LP relies on is absent, and every extraction mechanism is present at maximum setting. `03`'s GEN-14/GEN-05 note applies: a GP that can produce neither realized nor net-to-LP figures has no validated record at all.

## 8. Questions for the GP
Listed for completeness — the report's judgment is that no answers rescue the structure; these confirm rather than resolve:
1. **Q-GP-03** — The SEC action: full context and resolution. *Bad answer already implied:* it wasn't volunteered. (`GEN-02`)
2. **Q-GP-01** — Cash co-invest, same terms. *Bad answer already given:* "our expertise is our investment." (`GEN-01`)
3. **Q-GP-02** — Any realized exits, net-to-LP. *Bad answer:* "most deals are still performing." (`GEN-14`/`GEN-05`)
4. **Q-FEE-03** — Why 50% promote, deal-by-deal, no clawback? What pref sits beneath it? *Bad answer:* "you get paid when we get paid." (`EQUITY-01/02/04`)
5. **Q-RISK-02** — Cost to extend the rate cap through 2028 at current pricing, and is it budgeted? *Bad answer:* "rates should be lower by then." (`GEN-10`)
6. **Q-DS-03** — Any downside case. *Bad answer:* none exists. (`GEN-13`)

## 9. Diligence Checklist
Largely moot given the verdict; if pursued against advice:
- [ ] SEC EDGAR / litigation search on all principals — the named action and any others
- [ ] PPM: confirm pref existence, full waterfall, fee schedule
- [ ] Rate-cap dealer quote for a 2028-maturity cap at the loan's strike
- [ ] Independent verification of every marked deal's current basis

## 10. Verdict
**Pass — unambiguous.** Structure: a 50% deal-by-deal promote with no clawback and no stated pref (`EQUITY-01`, `EQUITY-02`, `EQUITY-04`). Alignment: zero co-invest (`GEN-01`). Conduct: a prior SEC action (`GEN-02`). Debt: a rate cap expiring years before maturity (`GEN-10`). Evidence: unrealized marks and an upside-only pro forma (`GEN-14`, `GEN-13`). Six independent REDs, several of which are facts rather than disclosure gaps — there is no answer set that converts this to Pursue. Suits no passive LP; the only rational engagement with this offering is declining it quickly.
