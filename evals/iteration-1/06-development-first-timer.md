# Eval fixture 06 — Ground-up development, first-time sponsor, 25% IRR

*Iteration-1 run, 2026-07-03, against SKILL.md @ cddc52d. Fixture prompt: evals.json id 6.*

---

**Verdict: Pass.** A first-time ground-up sponsor projecting above the category's *target* ceiling, on a single pro forma with no downside case, with exit-cap compression baked in and a dual development + construction-management fee load at the aggressive threshold. Development is the asset class where realized returns most reliably land below target (`01`) — this deal projects above target with the least-proven sponsor profile the category allows.

## 1. Deal Snapshot
- **Asset class:** Development (ground-up) 🟢 — product type (multifamily? industrial?) not stated
- **Deal type:** Equity syndication (development) 🟢
- **Sponsor:** Not stated; **first ground-up project** 🟢
- **Geography / Minimum / Raise:** Not stated
- **Hold:** 3 years 🟢
- **Claimed return:** 25% IRR / 2.5x EM 🟢 — above the `01` target band (18–22%) 🔴
- **Structure:** Waterfall / pref / promote — **not stated** 🔴

## 2. Return Stress-Test
Baseline (`01`): development targets 18–22% net IRR, and "realized returns often below target on construction-cost overruns, financing-cost spikes, or lease-up misses." **This deal projects 25% — above the top of the target band — from a sponsor with zero realized development outcomes** 🔴.

Benchmark (`05`): development's ≈1150–1550bps *target* premium over VNQ is the largest in the spread table **and** carries the widest dispersion — the file's own instruction is to discount the target premium heavily for realized-below-target. A 25% projection widens the paper premium further while resting on nothing realized. Preqin dispersion (opportunistic IQR ~13pts) means the marketed number and the median outcome are different animals 🟡.

Swing assumptions:
1. **Exit cap** — underwritten below going-in basis: unproven compression on top of an untested lease-up (`EQUITY-06`).
2. **Construction cost / contingency** — budget and contingency % undisclosed; the canonical first-project failure mode.
3. **Lease-up / absorption** — no comps or absorption data provided; 3-year hold leaves no slack for a slow lease-up.

Bear case: not computable — **no downside case exists** (`GEN-13`), which on a development deal is itself close to disqualifying: the category's realized-below-target pattern *is* the base rate.

## 3. Where LP Returns Come From
Effectively 100% exit: ground-up development produces no meaningful in-place cash flow — the 2.5x in 3 years is built (construction margin) and sold (exit cap). That is the nature of the class rather than a hidden defect, but it makes the exit-cap assumption the entire deal (`GEN-08` structurally satisfied; `EQUITY-06` fired on the compression), and it makes the absent downside case (`GEN-13`) inexcusable — the one thing a development pro forma must show is what happens when the exit slips.

## 4. Fee Stack Summary
Per `02` (development-deal fee variations):

| Fee | Stated | `02` range | Read |
|---|---|---|---|
| Development fee | 5% | 3–5% of project cost | Top of range 🟡 |
| Construction management | 4% | 3–5% of hard costs | In range alone — but see below 🔴 |
| Pref / promote / waterfall | Not stated | 15–30% over 6–10% pref | Unknown (`GEN-16`, partial) 🔴 |
| Acquisition / other | Not stated | — | Unknown |

**`02` names this exact pattern as the aggressive threshold: ">6% *or split across both* a development fee *and* a construction management fee."** Combined, the sponsor takes ~9% of cost-basis fees before any promote — a first-time developer is paid handsomely at close and during construction regardless of outcome, which inverts alignment on exactly the deal profile where alignment matters most. Gross-to-net drag is not fully computable without the waterfall — that is a finding (`GEN-16`).

## 5. Red Flags
**RED**
- `EQUITY-06` — Exit cap underwritten below going-in basis: unproven compression baked into a 25% headline that already exceeds the category target.
- Fee stacking at `02`'s aggressive threshold — development fee *plus* construction management (5% + 4%): the GP's economics are front-loaded and outcome-independent. (If the CM entity is GP-affiliated, `GEN-06` also fires — undisclosed; asked below.)
- **First-time-developer track record gap** — `01` is explicit that development experience is not fungible with acquisition experience and lists "the GP's last three development exits" as an essential disclosure. Zero exist. The record isn't merely unverified (`GEN-14` mechanism) — it is structurally absent for this asset class.

**YELLOW**
- `GEN-13` — Single-point pro forma, no downside case — on the asset class with the widest realized dispersion. (Per `03` notes, cycle-exposed asset + no downside case is sharper than either alone.)
- `GEN-16` (YELLOW–RED) — No waterfall/pref disclosure; promote structure unknown.
- Missing entitlement/permit status (see §6) — the single largest binary risk in ground-up development is undisclosed.

## 6. Missing Disclosures
Per `01` (development essentials), this deal omits nearly all of them:
- **Entitlement and permit status** (entitled ≠ permitted ≠ shovel-ready)
- **Hard-cost budget with contingency %** (`02`: <5% contingency is under-reserved)
- **Debt structure**: construction loan terms, takeout assumptions
- **Market absorption assumptions with comp evidence**
- GP's development-specific team (first project — who has actually built?)
- Waterfall, pref, promote
- Sponsor identity, co-invest (`GEN-01` unresolvable)
- Product type and market

## 7. GP Alignment
Inverted as disclosed: ~9% of cost basis in fees paid at close and through construction, regardless of outcome, to a sponsor with no realized development history, with the promote structure undisclosed and co-invest unstated. The bar for a first-time developer should be *more* skin in the game and *lighter* front-loaded fees; this deal shows the opposite on fees and is silent on skin.

## 8. Questions for the GP
**Must-ask**
1. **Q-DS-03** — "What is the return under a bear case — cost overrun, 6-month lease-up slip, exit at going-in cap or above?" *Bad answer:* "we underwrite conservatively" with nothing to show. (`GEN-13`)
2. **Q-EXIT-01** — "Why is the exit cap below going-in basis, and what's the IRR at a flat cap?" *Bad answer:* "caps will compress"; IRR breaks at flat. (`EQUITY-06`)
3. **Entitlement status** — "Is the project fully entitled and permitted today? What approvals remain?" *Bad answer:* "entitlements are on track" without a date-stamped status. (`01` essentials / `GEN-17`)
4. **Q-FEE-02** — "Is the construction manager GP-affiliated? What do both entities charge, benchmarked against third parties — and why both a 5% development fee *and* 4% CM?" *Bad answer:* "all arm's-length" without names; no benchmark. (`GEN-06`; `02` aggressive threshold)
5. **Q-FEE-01** — Full waterfall: pref, promote, catch-up, clawback. *Bad answer:* "standard structure" without the schedule. (`GEN-16`)
6. **Q-GP-01** — GP cash co-invest, same terms. *Bad answer:* "the development fee is our investment." (`GEN-01`)
7. **Team experience** — "Who on the team has personally taken a ground-up project through completion, and on whose balance sheet?" *Bad answer:* borrowed credentials — the GC's or a consultant's record presented as the sponsor's.
8. **Q-RISK-01** — Construction loan maturity vs the 3-year plan; takeout terms. *Bad answer:* "we'll refinance at stabilization" with no committed takeout. (`GEN-09`/`EQUITY-07`)

## 9. Diligence Checklist
- [ ] Entitlement/permit documentation, date-stamped
- [ ] Hard-cost budget with line-item contingency; GC contract type (GMP vs cost-plus)
- [ ] Construction lender term sheet; takeout commitment or plan
- [ ] Third-party absorption study / lease-up comps for the submarket
- [ ] Sponsor principals: background, litigation, and any prior *non-development* track record, realized and net-to-LP
- [ ] Affiliate map: who owns the CM entity

## 10. Verdict
**Pass.** Development is the category where `01` warns realized returns most often miss target; this deal answers that base rate with an above-target 25% projection, no downside case, baked-in exit-cap compression, ~9% of front-loaded fees at `02`'s stated aggressive threshold, and a sponsor who has never completed the thing being underwritten. Each item alone is a hard question; together they are a profile. **What would have to be true to reconsider:** a full downside case that survives a flat exit cap, permits in hand, a GMP contract with real contingency, a benchmarked single-layer fee structure, meaningful GP cash co-invest, and a development-experienced principal — at which point it is a different deal from a different sponsor. Suits no passive LP as presented; first-time-developer risk is venture risk and should be priced — and structured — as such.
