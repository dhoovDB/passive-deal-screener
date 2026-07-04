# Eval fixture 08 — Multifamily syndication, flag cluster
*Iteration-3 run, 2026-07-04, blind generation by fresh-context agent, against SKILL.md (post S1b/S2b fixes).*

**Verdict: Pass. Six RED flags fire on what is disclosed — zero co-invest, prior SEC action, 50% promote with no clawback in a deal-by-deal waterfall, a rate cap expiring ~2 years before loan maturity, upside-only projections, and an all-unrealized track record. No answer to any question cures this structure; this is not a diligence candidate.**

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Multifamily (sub-strategy not stated) 🟢 |
| Deal type | Equity syndication, single asset 🟢 |
| Sponsor | Not named; **zero co-invest; principal named in a prior SEC action** 🟢 |
| Geography | Not stated |
| Minimum investment | Not stated |
| Hold | Not stated (loan matures 2028 → implied ≥2 yrs) 🟡 |
| Raise | Not stated |
| Claimed return | Not stated numerically — "projections show only an upside case" |
| Waterfall | American (deal-by-deal), **50% promote, no clawback**; pref not stated 🟢 |
| Debt | Floating rate; **rate cap expires in 12 months; loan matures 2028** 🟢 |
| Track record | All current, unrealized marks 🟢 |

## 2. Return Stress-Test

No return number is given to stress — only "an upside case" exists (GEN-13). What can be stressed is the structure:

- **The rate-cap gap is a live, dated exposure:** the cap dies in ~12 months while the loan runs to 2028. If floating rates sit above the cap strike after expiry, debt service steps up mid-hold with no protection — the exact 2022–24 wipeout sequence `03` documents (cap expires → rates elevated → refi frozen → debt service erases distributions, then equity). Replacement caps are priced to that risk; no extension budget is disclosed 🟡 (GEN-10).
- **The waterfall consumes the upside even if the deal works:** a 50% promote is far past `02`'s >30% aggressive threshold — of every dollar of profit above the (undisclosed) pref, half leaves for the GP. Whatever the projections claim gross, the LP's net is structurally poor 🟡.
- **Benchmark (`05`):** no claimed net exists to compare against VNQ (6.47% 10yr) — but note the asymmetry: to deliver even VNQ + the ~300–400bps hurdle to LPs *through* a 50% promote, the asset must gross far above the `01` value-add band. Single asset vs the index basket adds the concentration amplifier.

## 3. Where LP Returns Come From

Cannot be decomposed (no projections beyond "upside") — but the shape is legible: single-asset multifamily on floating bridge-style debt with an expiring cap is return-by-exit-or-refi, i.e., the financing-story family (GEN-07/GEN-08, pending decomposition) 🟡, with the GP taking 50% of whatever survives. Downside: after cap expiry, elevated rates redirect cash flow to debt service first — LP distributions are the shock absorber.

## 4. Fee Stack Summary (`02`)

Only the promote is disclosed: **50% — vs `02`'s 15–30% norm and >30% aggressive threshold; roughly double the top of market** 🟢. Pref not stated (`02`: pref <6% or none is itself aggressive → EQUITY-04 unresolved, treat as fired pending disclosure). Acquisition, asset management, disposition, loan-placement, admin: all undisclosed (**GEN-16**). **Gross-to-net drag not computable — and with a 50% promote, the promote alone would dominate any computation.**

## 5. Red Flags (`03`)

**RED — six fire on the face of the disclosure**
- **GEN-01** — zero GP co-investment; "our expertise is our investment" is the verbatim Q-GP-01 bad-answer signal. Fees and 50% promote regardless of LP outcome; alignment is asserted, not structural.
- **GEN-02** — principal named in a prior SEC action. Pass-or-resolve; combined with the rest of this structure, unresolvable.
- **EQUITY-01** — deal-by-deal waterfall with a 50% promote (`03`: RED when paired with high promote and no clawback — both present).
- **EQUITY-02** — no clawback: the GP keeps promote taken along the way even if the LP ends below the pref or loses capital.
- **GEN-10** — rate cap expires ~12 months in; loan matures 2028: the named 2022–24 failure pattern, on this deal's actual dates.
- **GEN-14** — track record is entirely unrealized marks: self-reported, unproven; per `03`, paired with any headline IRR framing this is the no-validated-record cluster (GEN-05 family).

**YELLOW / YELLOW–RED**
- **EQUITY-04** (YELLOW–RED) — preferred return not stated; possibly absent beneath a 50% promote.
- **GEN-13** — upside-only projections; no downside case.
- **GEN-16** (YELLOW–RED) — no fee schedule.
- **GEN-15** (YELLOW–RED) — no financials (T-12, rent roll, full debt terms).
- **GEN-11** — no distribution schedule.
- Single-asset concentration (`05` amplifier) 🟢.

Cluster note: GEN-01 + GEN-02 + EQUITY-01/02 is a GP that captures the upside, has nothing at risk, and has a regulatory history — the alignment failure is total, independent of the debt problem (GEN-10), which is independently disqualifying on its own timeline.

## 6. Missing Disclosures (`01` multifamily essentials + `02`)

- Rent roll, T-12 actuals, occupancy
- Pref rate and mechanics (cumulative/compounding)
- Full fee schedule; catch-up and split tiers
- Debt terms beyond the cap/maturity dates: rate, spread, cap strike, extension cost
- Exit cap and sensitivity; hold period; raise; sponsor identity in full
- Realized track record (none exists as presented)
- Distribution schedule; SEC-action specifics (order, resolution, undertakings)

## 7. GP Alignment

The section answers itself 🟢: **zero cash at risk (GEN-01), a regulatory history (GEN-02), a 50%/no-clawback promote (EQUITY-01/02), and a track record consisting entirely of unrealized marks (GEN-14).** Every alignment axis the skill checks — co-invest, realized net-to-LP record, waterfall alignment — fails on the sponsor's own representations. Affiliate fees undisclosed (GEN-06 unresolved), which at this point is a rounding error.

## 8. Questions for the GP (`04`)

Listed for completeness — the screen does not depend on the answers, because the disqualifying features are disclosed facts, not open questions:
1. **Q-GP-03** (GEN-02) — the SEC action: order, allegations, resolution, undertakings. *Bad answer:* "nothing material"; blaming the regulator. (Verify independently regardless.)
2. **Q-GP-01** (GEN-01) — any cash co-invest, same terms. *Bad answer:* already given: "our expertise is our investment."
3. **Q-FEE-03** (EQUITY-01, EQUITY-02) — why 50%, and where is the clawback? *Bad answer:* "you get paid when we get paid."
4. **Q-FEE-04** (EQUITY-04, EQUITY-05) — what pref, cumulative and compounding? *Bad answer:* none, or non-cumulative.
5. **Q-RISK-02** (GEN-10) — cap strike, replacement cost at current pricing, and who funds the extension. *Bad answer:* "rates should be lower by then."
6. **Q-RISK-01** (GEN-09) — intended hold vs the 2028 maturity and extension tests. *Bad answer:* no plan if refi markets are shut.
7. **Q-GP-02** (GEN-05, GEN-14) — realized, exited, net-to-LP deals. *Bad answer:* "most deals are still performing."
8. **Q-DS-03** (GEN-13) — any downside case. *Bad answer:* the upside case restated.
9. **Q-FEE-01** (GEN-16) + **Q-RISK-03** (GEN-15) — full fee schedule; T-12, rent roll, debt terms. *Bad answer:* withheld until commitment.
10. **Q-DIST-01** (GEN-11) — distribution schedule. *Bad answer:* none.

## 9. Diligence Checklist

Only one item matters, and it is free: **pull the SEC action** (SEC litigation releases / administrative proceedings, plus state and FINRA records) and confirm the principal's identity against it. Everything else — PPM, loan documents, cap confirmation, financials — is moot unless an LP intends to override six REDs, which this screen does not recommend.

## 10. Verdict

**Pass.** This is a merits verdict, not an insufficiency verdict: the disclosures that *are* made are individually and jointly disqualifying. Six REDs fire — zero co-invest (GEN-01), prior SEC action (GEN-02), 50% promote with no clawback in a deal-by-deal waterfall (EQUITY-01/EQUITY-02), a rate cap expiring ~2 years before maturity (GEN-10), and an all-unrealized track record (GEN-14) — against a `03` standard where a *single* RED is pass-or-resolve, and none of these resolve: the SEC action happened, the co-invest is zero by design, the waterfall is the offer, and the cap gap is on the calendar. The undisclosed remainder (pref, fees, financials) could only make this worse. Biggest swing factor: none — there is no assumption whose favorable resolution changes the answer. Who it suits: no passive LP; what would have to be true: a different sponsor, a different waterfall, and different debt — i.e., a different deal.
