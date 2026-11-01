# Eval fixture 06

*Iteration-7 run, 2026-11-01, blind generation by fresh-context agent (model: Opus), against SKILL.md @ 181fdd7.*

**Verdict: Pass as presented — insufficient disclosure.** A first-time developer is asking you to fund a ground-up deal whose return depends on the exit. The pro forma assumes the exit cap compresses, shows no downside case, and pays two separate construction-period fees. The facts you do have already lean toward Pass, and what you don't have isn't enough to underwrite the core return story.

*Screening output only, not investment advice.*

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Development (ground-up) 🟢. The property type it delivers (multifamily, industrial, etc.) is **Not stated** |
| Deal type | Development (equity) 🟡, inferred. The capital-stack position is **Not stated** |
| Sponsor | **Not stated** (name). Stated: this is the sponsor's **first ground-up project** 🟢 |
| Geography / submarket | **Not stated** |
| Minimum investment | **Not stated** |
| Hold | 3 years 🟢. That's the low end of the 3–5 yr development norm (`01`) |
| Raise / total project cost / capital stack | **Not stated** |
| Claimed return | 25% IRR / 2.5x 🟢. **Gross or net to LP: Not stated** |
| Fees disclosed | 5% development fee + 4% construction management 🟢. Fee bases (project cost? hard costs? equity?) **Not stated** |
| Underwriting | Single pro forma, no downside case 🟢. Exit cap underwritten below the going-in basis 🟢 |
| Debt | **Not stated**: no construction loan, rate, maturity, rate cap or takeout |
| Waterfall / pref / promote | **Not stated** |
| Distribution schedule | **Not stated** |

**The headline numbers don't agree with each other** 🟢 (arithmetic on stated figures). Over 3 years, a 2.5x multiple implies an IRR of about **35.7%** (2.5^(1/3) − 1), even if every dollar comes back at exit, which is the slowest possible timing for a given multiple. At 25% IRR, 3 years compounds to only about **1.95x** (1.25³). Reaching 2.5x at 25% takes about **4.1 years** (ln 2.5 / ln 1.25). So one of three things is true: the hold is longer than 3 years once equity draws and lease-up are counted, the 2.5x is a project-level or gross figure, or the figures come from different models 🟡. Whichever it is, the LP can't take any of the three numbers at face value. This goes to Q-DS-01 and Q-DIST-01 in §8.

---

## 2. Return Stress-Test

**Swing assumptions** (there is no downside case, so these are named rather than modeled, per `GEN-13`):
1. **Exit cap.** It's already underwritten below the going-in basis (`EQUITY-06`). On a 3-year development exit, the sale price *is* the return.
2. **Hard cost and schedule.** `01` warns that development returns often come in below target because of cost overruns and lease-up misses. Neither the contingency % nor the budget is disclosed.
3. **Construction financing / takeout.** Debt terms, maturity and takeout are not disclosed. Any delay pushes the exit past the construction loan's maturity (`GEN-09` / `EQUITY-07`, not confirmed).

| Case | What has to happen | LP outcome |
|---|---|---|
| Bull | Delivered on budget and on schedule, leases up per pro forma, sells at the compressed exit cap | The sponsor's 25% / 2.5x (basis unknown, and the two figures are inconsistent, see §1) 🔴 |
| Base (realistic) | `01`: development realized "often below" the 18–22% target. A first-time developer with no contingency disclosed is the profile most exposed to that miss | Below the pro forma. Not quantifiable without the budget, capital stack and waterfall 🔴 |
| Bear | Cost overrun plus a 6–12 month schedule slip, exit cap flat to or above going-in, construction loan matures before stabilization | Equity is first loss. On a levered development deal, a flat exit cap combined with an overrun can wipe out the whole development spread, and a forced sale or rescue capital call can impair principal 🟡. This is the scenario the sponsor didn't show |

**Benchmark** (`05`, `scripts/benchmark_comparator.py`, deal type `development`, 3-yr lock-up):
- **Comparator:** VNQ at 4.92% 10yr trailing. **Illiquidity hurdle for a 3-yr lock-up:** about 300–400 bps. **Net-to-LP bar:** about **8.9–9.9%** 🟢.
- **Treasury floor:** the duration-matched risk-free rate sits between the 2yr (4.87%) and the 10yr (5.18%). At this snapshot the Treasury is the tighter floor relative to VNQ 🟢.
- **What we can compute:** if the 25% is gross, it falls to about **22.0% net** after the disclosed fees at face value (no promote, see §4), which is +1708 bps over VNQ and **CLEARS comfortably**. With a market-standard promote added as a placeholder (20% over 8%, 100% catch-up, *not disclosed*), it falls to about **17.8%** net: +1287 bps, still **CLEARS** 🔴. (That promote run is labeled ASSUMED.)
- **Why "clears" means little here:** `05` puts development at the *largest target premium and the widest dispersion* (opportunistic IQR around 13 pts, Preqin) and says to "discount heavily for realized-below-target." A *projected* 25% from a sponsor with zero realized development exits is a target, not evidence. The real question is whether LP capital survives the bear case, and the deal gives no answer to that.
- **Never gross-to-gross:** the 25% has no stated basis. If it's net, it sits **above the top of `01`'s 18–22% development target range**, which needs an explanation, not credit. If it's gross, the LP net is lower. Demand the net-to-LP figure (Q-FEE-01).

---

## 3. Where LP Returns Come From

- **Cash flow:** close to none 🟡. A 3-year ground-up hold is entitlement/construction, then lease-up, then sale. The asset doesn't stabilize long enough to throw off meaningful distributions before exit.
- **Exit:** essentially the whole return 🟡 (inferred from the structure, but with high confidence). That puts it well over the 60% threshold, so **`GEN-08` (exit-dependent IRR) fires**.
- **Cap-rate compression:** stated 🟢. Exit cap below going-in basis means **`EQUITY-06` fires**. One caveat matters here. If "going-in basis" means the *yield on cost*, then selling at a cap below it is the normal development spread, the thing development exists to capture. If it means the *market cap rate today*, the pro forma also assumes market cap compression on top of the spread. The deal doesn't say which, and the answer changes how much of the 25% is a market-timing bet (Q-EXIT-01).
- **Leverage:** Not stated 🔴. The `05` unlevered overlay shows NCREIF NPI at 5.00% trailing (almost entirely income, appreciation near zero). That means roughly 20 points of a 25% IRR has to come from development spread, leverage and cap compression, not from in-place operations 🟡. The cap-compression leg of the financing story is stated. The leverage leg isn't. **`GEN-07` is probable but unconfirmed** until the capital stack is disclosed (Q-DS-02).

**Read:** this is an exit bet resting on an assumed cap compression (`GEN-08` + `EQUITY-06`, with `GEN-07` pending leverage). That's the financing-story cluster from `03`, made riskier by a sponsor executing its first build.

---

## 4. Fee Stack Summary

| Fee | Disclosed | `02` norm | Read |
|---|---|---|---|
| Development fee | 5% 🟢 (basis not stated) | 3–5% of total project cost, one-time | At the top of the range |
| Construction management | 4% 🟢 (basis not stated) | 3–5% of hard costs | In range on its own |
| Dev fee **and** CM together | Both charged 🟢 | `02`: aggressive if ">6% **or split across both** a development fee *and* construction management fee" | **Aggressive per `02`.** Two fees for overlapping construction-period oversight |
| Acquisition / land fee | Not stated | 1–2% of equity | Unknown |
| Asset management | Not stated | 1–2% of equity, annual | Unknown |
| Disposition | Not stated | 0.5–1% of sale price | Unknown. A 3-yr sale exit makes this certain to be charged if it exists |
| Loan placement | Not stated | 0.5–1.5% of loan | Unknown. A construction loan is likely 🟡 |
| Promote / pref | Not stated | 15–30% over a 6–10% pref | Unknown, and this is the biggest drag item |
| Admin / IR | Not stated | 0.1–0.5% of equity | Unknown |
| Construction contingency | Not stated | 5–10% of hard costs | Unknown. Not a fee, but `02` flags <5% as under-reserved and >15% as possibly padding the fee base |

**Gross-to-net drag: at least 167 bps/yr. About 300 bps/yr with the disclosed fees at face value. The true total can't be computed from what's disclosed, and that is the finding.**

How the figure was built (`scripts/fee_drag_calculator.py`, 25% gross, 3-yr hold, every undisclosed fee and the promote passed as `0`):
- Development fee alone, entered at 5% of equity: **167 bps/yr**. This is a hard **floor**, because total project cost is always at least the equity, so 5% of cost is at least 5% of LP equity.
- Development fee plus CM at face value (9%): **300 bps/yr** (25.0% gross to 22.0% net).
- Same, plus a placeholder market promote (20% over 8%, 100% catch-up, ASSUMED, not disclosed): **721 bps/yr** (25.0% to about 17.8%) 🔴.

**Why the floor understates it** 🔴 (illustration, not a deal fact): both fees are charged on *project* dollars (total cost, hard costs) but paid out of the LP's *equity* return. If LP equity funds a third of total cost, a 5% development fee equals about 15% of LP equity, roughly three times the floor. A short 3-yr hold makes one-time fees worse, because `02` notes they annualize over fewer years. Both fees are also typically paid out of the construction budget during the build, regardless of whether the project ever exits profitably 🟡. Every ASSUMED input above is a §6 gap.

---

## 5. Red Flags

**RED**
- **`EQUITY-06`: exit cap below going-in** 🟢. The headline IRR has unproven cap compression built in. On a deal with no cash flow before exit, the exit cap sets the LP's entire return. Routes to Q-EXIT-01.
- **`GEN-08`: exit-dependent IRR** 🟡. Effectively all return comes from the sale after a 3-yr build-and-lease-up. If the exit slips or the cap widens, the IRR doesn't erode gradually. It collapses. Routes to Q-DS-01.
- **`GEN-14`: no realized track record in this strategy** 🟢. This is the sponsor's first ground-up project, so it has zero realized development exits. `01`: "development experience is not fungible with acquisition experience." Any prior acquisition record (none cited) doesn't carry over, and project-level or GP-level figures would also be unverified (`GEN-05`, cited for the probe). Routes to Q-GP-02.
- **`GEN-07`: financing story (probable, pending leverage)** 🟡/🔴. The cap-compression leg is stated (`EQUITY-06`). The leverage leg is undisclosed. Treat as RED until Q-DS-02 shows an unlevered, operations-driven return.

**Cluster:** `GEN-07` + `GEN-08` + `EQUITY-06` together are the financing-story pattern `03` says the verdict should name explicitly. Here it's compounded by `GEN-14`: the party executing the build-and-exit bet has never completed one.

**YELLOW–RED**
- **`GEN-06`: construction-period fee stacking** 🟢/🟡. A development fee and a CM fee are both charged, which `02` marks aggressive. If the CM firm is GP-affiliated (not stated), the GP earns layered fees on the budget whether or not LPs get their capital back. Routes to Q-FEE-02.
- **`GEN-16`: no fee or waterfall disclosure** 🟢. Pref, promote, catch-up, waterfall type, clawback, and the asset management, acquisition, disposition and placement fees are all missing, so the drag can't be known. (`EQUITY-01`, `EQUITY-02`, `EQUITY-03`, `EQUITY-04`, `EQUITY-05` can't be assessed. They're cited for their probes, not fired.) Routes to Q-FEE-01, Q-FEE-03, Q-FEE-04.
- **`GEN-15`: missing financials** 🟢. There are no debt terms, no budget and no capital stack, so the deal can't be underwritten on the debt axis. Routes to Q-RISK-03.

**YELLOW**
- **`GEN-13`: single-point pro forma, no downside case** 🟢. `03`: a cycle-exposed asset with a single-point pro forma is sharper than either flag alone, and development is the most cycle-sensitive class in `01`. Routes to Q-DS-03.
- **`GEN-11`: IRR with no distribution schedule** 🟢. Development is back-loaded by nature. The inconsistent IRR/multiple/hold (§1) shows the timing isn't pinned down. Routes to Q-DIST-01.
- **`GEN-17`: essential development disclosures absent** 🟢. All five `01` development essentials are missing (see §6). Routes to the `GEN-17` probe in §8.

**Unconfirmed: probe, do not fire** (these would need 🔴 assumptions): `GEN-09` (construction loan matures inside the hold), `GEN-10` (rate-cap expiry on floating construction debt), `EQUITY-07` (refi/takeout-dependent), `GEN-18` (absorption in an undisclosed submarket), `GEN-01` (co-invest not stated), `GEN-02` (regulatory history unknown).

---

## 6. Missing Disclosures

Against the `01` **Development (ground-up)** essentials, every one is absent:
1. **Entitlement and permit status.** Entitled-but-not-permitted is a different deal than shovel-ready. On a 3-yr hold, permit delay eats directly into the schedule.
2. **Hard-cost budget with contingency %.** `02` norm is 5–10% of hard costs. This is also the base the 4% CM fee is likely charged on.
3. **Debt structure including takeout assumptions.** Construction loan size, rate (fixed or floating), rate cap, maturity, extension options, recourse/guarantor, and construction-to-perm vs separate takeout.
4. **Market absorption assumptions with comp evidence.** Without these, the lease-up and exit cap are assertions.
5. **The GP's last three development exits with realized timing and budget vs underwritten.** **None exist** (first project). This disclosure can't be cured by asking, only offset (see §10).

Also missing (general / `02`):
- Property type, location and submarket.
- Sponsor identity and principals.
- Raise, minimum, total project cost, LTC.
- Whether the 25% is gross or net to LP.
- Distribution schedule and capital-call schedule.
- Full fee schedule and the base each fee is charged on.
- Pref, promote, catch-up, waterfall type, clawback.
- GP co-investment.
- The going-in basis that the exit cap is compared against: yield on cost or market cap.

**Inputs ASSUMED in the scripts (`02` gaps):** gross vs net basis of the 25%; fee bases (development and CM entered at face value as % of equity); promote/pref (placeholder 20%/8%/100% in one run only); all other fees set to 0.

---

## 7. GP Alignment

- **Co-investment:** Not stated, so unverified 🔴. Routes to Q-GP-01.
- **Realized net-to-LP track record:** none in development 🟢 (first ground-up project). Any non-development record is not cited, so it's unverified, and per `01` it wouldn't transfer anyway. *Unverified stated as unverified.*
- **Waterfall alignment:** unknown. No pref, promote or clawback is disclosed.
- **Affiliate fees:** the development fee and CM fee are both GP-side economics paid during construction 🟢. Whether CM goes to an affiliate is not stated 🔴. The structure pays the GP up to 9% of construction-period dollars before any exit proves the thesis, and that pay is front-loaded while the LP's return is entirely back-loaded 🟡. That's the core alignment gap.

---

## 8. Questions for the GP

**Must-ask**

| ID | Question | Bad-answer signal (the specific dodge) |
|---|---|---|
| Q-GP-02 (`GEN-14`, `GEN-05`) | Restate your track record as net-to-LP IRR on fully realized, exited deals, and who on this team has completed a ground-up project start to exit? | Offers acquisition-deal or project-level IRR in place of development experience. "Our GC has built hundreds of units," which substitutes the contractor's record for the sponsor's. Can't separate realized from marked. |
| Q-EXIT-01 (`EQUITY-06`) | Why is the exit cap below the going-in basis? Is "going-in" the yield on cost or today's market cap? What's the IRR at an exit cap equal to or above going-in? | "Cap rates will compress." The IRR breaks at a flat exit cap. No sensitivity offered. Won't say which "going-in" they mean. |
| Q-DS-01 (`GEN-08`, `EQUITY-06`) | What share of LP IRR comes from the exit vs cash flow, and how do 25% IRR, 2.5x and a 3-year hold reconcile? | Can't decompose the IRR. Can't reconcile the three numbers. "The model handles it." "Real estate always appreciates." |
| Q-DS-02 (`GEN-07`) | Strip out leverage and cap-rate compression. What is the unlevered return on cost? | Treats the levered IRR as the only figure. "Leverage is just how development works." No unlevered view exists. |
| Q-DS-03 (`GEN-13`) | What's the return under a bear case: hard-cost overrun, schedule slip, exit cap at or above going-in? | "We underwrite conservatively" with nothing to show. The bear case is still a gain. No downside model exists. |
| Q-FEE-01 (`GEN-16`) | Provide the complete fee schedule, with the base for each fee, and the full waterfall. Is the 25% gross or net to LP? | "Standard market fees." "The PPM has it" without producing it. Can't say whether the 25% is net. |
| Q-FEE-02 (`GEN-06`) | Who receives the development fee and the CM fee? Is the CM firm affiliated? Why charge both, and are they benchmarked? | "All arm's-length" without naming the CM provider. No justification for charging both fees. No benchmark. |
| Q-FEE-03 (`EQUITY-01`, `EQUITY-02`) | Is the waterfall deal-by-deal or whole-of-fund, and is there a clawback? | Can't explain the catch-up. "You get paid when we get paid." |
| Q-FEE-04 (`EQUITY-04`, `EQUITY-05`) | What pref do LPs get before promote? Is it cumulative and compounding through the no-cash-flow construction period? | Pref below 6% or none. Non-cumulative, so the construction years with no distributions accrue nothing. |
| Q-RISK-01 (`GEN-09`) | When does the construction loan mature relative to stabilization and sale, and what are the extension terms? | Maturity falls inside the hold. "We'll refinance" with no terms. No plan if the takeout market is shut. |
| Q-RISK-02 (`GEN-10`) | If the construction debt floats, when does the rate cap expire, and what does extending it cost? | Cap expires before maturity. Extension cost not modeled. "Rates should be lower by then." |
| Q-EXIT-02 (`EQUITY-07`) | Does capital return depend on a takeout refi or the sale? What happens if neither is available at month 36? | "The market will reopen." No fallback. Rescue capital call left undefined. |
| Q-RISK-03 (`GEN-15`) | Provide the full debt terms, the development budget and the capital stack. | "Confidential until you commit." |
| `GEN-17` probe (per `01` development baseline) | What is the entitlement/permit status, the hard-cost budget and contingency %, and the comp evidence behind absorption? | "Entitlements are in process" with no timeline. Contingency under 5%. Absorption given at metro level with no comps. |
| Q-MKT-01 (`GEN-18`) | What submarket supply pipeline and absorption data support the lease-up and exit assumptions? | Metro-level optimism. No supply pipeline acknowledged. |
| Q-DIST-01 (`GEN-11`) | What is the projected distribution schedule, and when does LP capital start returning? | "We'll distribute when the deal supports it." No milestones. |
| Q-GP-01 (`GEN-01`) | How much of your own cash is in this deal, on the same terms as LPs? | "Our sweat equity / development fee is our investment." Co-invest funded by the deferred development fee. |
| Q-GP-03 (`GEN-02`) | Any regulatory action, enforcement or investor litigation against you or your principals? | "Nothing material." A search turns up something undisclosed. |
| Q-LIQ-01 | What are my options if I need to exit before the hold ends, including if the hold extends? | "A secondary market may develop." Silence on what happens if the hold extends. |

**Nice-to-ask**
- **Q-DIST-02:** "When are capital calls expected, and what's the consequence of a missed call?" Bad answer: "calls as needed," punitive dilution buried in the docs. This one is especially relevant for development, where overruns are typically funded by a capital call.
- **Q-GP-04:** "How have headcount and monitoring capacity grown?" Bad answer: no named construction or development manager on the sponsor side.
- **Q-LIQ-02:** "When will K-1s be delivered?" Bad answer: "as soon as we can."

---

## 9. Diligence Checklist

- **PPM / operating agreement.** Read the fee definitions and bases, the waterfall, pref accrual during construction, capital-call and dilution mechanics, and the GP removal provisions.
- **Background / regulatory.** Search the sponsor and principals (SEC, FINRA, state securities, litigation). Confirm the first-project status and identify who the actual developer is.
- **Entitlements.** Verify zoning, permits and approvals independently with the municipality.
- **Budget.** Get a third-party cost review of the hard and soft budget and contingency. Get the GC contract type (GMP vs cost-plus), the GC's track record and bonding.
- **Comps / absorption.** Independently check rent and sale comps and the submarket supply pipeline. Check exit cap comps for newly delivered product in this submarket.
- **Appraisal.** Get the as-complete / as-stabilized appraisal and compare it to the pro forma exit value.
- **Lender.** Get the construction loan term sheet: maturity, extensions, rate cap, completion guarantee and guarantor net worth (a first-time sponsor's guarantee may be thin).
- **Model.** Get the full pro forma and reconcile IRR, multiple and hold. Run your own sensitivity on exit cap, cost and timing.

---

## 10. Verdict

**Pass as presented — insufficient disclosure.**

*Screening output only, not investment advice.*

**Reasoning.** Of the five essential disclosures `01` lists for development, none is provided, and one (the sponsor's last three development exits) is known not to exist. Asset type, market, budget, capital stack, debt and waterfall are all absent. The headline IRR, multiple and hold don't reconcile with each other. There isn't enough here to underwrite the core return story.

The facts that *are* disclosed already point toward Pass. The return is an exit bet (`GEN-08`) built on assumed cap compression (`EQUITY-06`), probably amplified by undisclosed leverage (`GEN-07`). It is shown as a single pro forma (`GEN-13`), executed by a first-time developer (`GEN-14`), with two construction-period fees that `02` calls aggressive (`GEN-06`). That's the financing-story cluster: the sponsor makes money building it, and the LP makes money only if the sale goes as modeled.

**Biggest swing factor:** the exit cap. With no cash flow before sale, the exit cap applied to an unproven lease-up sets the LP's entire outcome. It's already assumed tighter than going-in, and it's being executed by a team that has never taken a project to exit.

**Who it could suit:** only an LP sized for a total loss on this position, who wants opportunistic development exposure and can hold through a schedule slip without needing liquidity.

**What would have to be true to re-screen:**
1. An experienced development partner or co-GP with realized ground-up exits (last three, with budget and timing vs underwritten), or a third-party fee developer, on the team.
2. A downside case where LP capital survives an exit cap at or above going-in plus a hard-cost overrun.
3. Clarity that the 25% is net to LP, with IRR, multiple and hold reconciled.
4. A full fee schedule with bases, one combined construction-period fee or a justified split, and the CM affiliate status disclosed.
5. Pref, promote and waterfall terms. A cumulative pref accruing through construction.
6. Construction loan terms: maturity beyond the realistic stabilization date, extensions, rate-cap coverage.
7. Entitlement/permit status, a budget with contingency of at least 5%, and absorption comps.
8. Meaningful GP cash co-investment on pari-passu terms.

If those come back clean, the deal gets a merits screen. If even the downside case and the experienced-partner question come back badly, it's a Pass on the merits.
