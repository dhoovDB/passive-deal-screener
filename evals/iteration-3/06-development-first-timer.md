# Eval fixture 06 — Ground-up development, first-time sponsor
*Iteration-3 run, 2026-07-04, blind generation by fresh-context agent, against SKILL.md (post S1b/S2b fixes).*

**Verdict: Pass as presented — insufficient disclosure. Every `01` development essential is absent (entitlement status, budget/contingency, debt structure, absorption evidence, development track record), and what *is* disclosed is adverse: a first-time developer, a 9% combined development+CM fee load, exit-cap compression, and a single upside-only pro forma on the highest-risk deal type in the book.**

---

## 1. Deal Snapshot

| Field | Value |
|---|---|
| Asset class | Development — ground-up (property type not stated) 🟢 |
| Deal type | Equity (development) 🟢 |
| Sponsor | Not stated by name; **first ground-up project** 🟢 |
| Geography | Not stated |
| Minimum investment | Not stated |
| Hold | 3 years 🟢 |
| Raise | Not stated |
| Claimed return | 25% IRR / 2.5x — **gross or net not stated** 🔴 |
| Exit assumption | Exit cap underwritten below going-in basis 🟢 |
| Fees | 5% development fee + 4% construction management 🟢 |
| Pref / promote / waterfall | Not stated |

## 2. Return Stress-Test

Swing assumptions: **construction cost + timeline**, **exit cap**, **lease-up/absorption pace**.

- **Base.** 25% target vs the `01` development norm of 18–22% *target* — above the top of an already-optimistic category band, from a sponsor who has never delivered a project 🟡. `01` is explicit that realized development returns land *below* target on cost overruns, financing spikes, or lease-up misses.
- **Bear.** No downside case exists (GEN-13) — for the deal type where the downside is the story. Development's canonical bear: costs +10–15%, six months of delay, exit cap decompresses to going-in or above → the 2.5x compresses toward capital-back-or-worse; construction debt has no patience for that sequence. The sponsor has shown none of this math.
- **Fee-adjusted:** the disclosed fees alone (5% + 4%, treated as one-time over 3 years) are ≈300bps/yr of drag → 25% gross ≈ 22% net *before* any promote — and the CM fee is conventionally charged on hard costs, a larger base than equity, so the true drag on LP equity is likely **understated** by this estimate 🟡. Promote terms are undisclosed, so the real net is unknowable (GEN-16).
- **Benchmark (`05`):** even a haircut ~22% net vs VNQ 6.47% = ≈1,550bps — the spread table's own read for development applies: the largest *target* premium **and** the widest dispersion; discount the target heavily (per the routing rule for development: discount the target premium heavily). A first-timer sits, statistically, in the fat left tail of that dispersion.

## 3. Where LP Returns Come From

Effectively 100% from the terminal event: ground-up deals produce no operating cash flow through entitlement and construction, and little through lease-up — the entire 2.5x arrives at sale or refi at the end of Year ~3 → **GEN-08 fires by construction**, resting on an exit cap *below* the going-in basis (**EQUITY-06**) — i.e., the plan needs the market to pay more per dollar of NOI at exit than the project costs to create today, on top of execution going right. Financed with construction debt (terms undisclosed), this is the financing-story cluster (GEN-07 family) in its purest form: the return is a leverage-and-exit bet with zero income cushion.

## 4. Fee Stack Summary (`02`)

| Fee | Deal | `02` norm | Read |
|---|---|---|---|
| Development fee | 5% | 3–5% of project cost; aggressive: >6% **or split across both a development fee and a CM fee** | Top of range, **and** paired with CM → aggressive per `02` 🟢 |
| Construction management | 4% | 3–5% of hard costs | In range alone; the *stacking* is the flag |
| Combined | ~9% across two fee lines | — | The exact double-charge pattern `02` names |
| Pref / promote | Not stated | 15–30% over 6–10% | GEN-16 — waterfall undisclosed |
| Acquisition/other | Not stated | — | Unknown |
| Contingency reserve | Not stated | 5–10% of hard costs standard; <5% under-reserved | Undisclosed — feeds §6 |

**Drag: ≈300bps/yr from the two disclosed fees alone (fee-drag model, 3-yr hold), with the CM fee base likely making that a floor. Total drag not computable without the waterfall — that is the finding.**

## 5. Red Flags (`03`)

**RED**
- **EQUITY-06** — exit cap below going-in basis: unproven cap compression baked into the headline, on a deal type where the exit *is* the return.
- **GEN-08** — exit-dependent IRR: ~100% of return at the terminal event (structural to ground-up, which is exactly why the absent downside case and compressed exit cap are disqualifying rather than routine). (With EQUITY-06 and the levered construction structure, this is the GEN-07 financing-story cluster — named.)
- **GEN-14 (as applied)** — no realized development exits exist or can exist: first ground-up project. `01` is explicit that development experience is not fungible with acquisition experience; the category's essential disclosure ("last three development exits with realized timing and budget-vs-underwritten") is unmeetable.

**YELLOW / YELLOW–RED**
- **GEN-13** — single pro forma, no downside case: on a cycle-exposed deal type, `03` notes this pairing is sharper than either flag alone.
- **GEN-16** (YELLOW–RED) — no pref, promote, or waterfall disclosed.
- Fee stacking: development fee + CM fee split — the `02` aggressive pattern 🟢; also probe whether the CM flows to a GP affiliate (**GEN-06**, unresolved).
- **GEN-15** (YELLOW–RED) — no budget, no debt terms, no absorption data.
- **GEN-11** — 25% IRR with no distribution schedule (there will be none until exit — which is the point).

## 6. Missing Disclosures (`01` development essentials — all five absent)

- Entitlement and permit status (entitled-but-not-permitted is a different deal than shovel-ready)
- Hard-cost budget with contingency % (`02`: 5–10% standard)
- Debt structure including takeout assumptions (construction-to-perm vs separate takeout)
- Market absorption assumptions with comp evidence
- Sponsor's prior development exits — structurally unavailable (first-timer)
- Plus: property type, market, raise size, waterfall/pref/promote, co-invest, guarantor/completion-guarantee structure, gross-vs-net basis of the 25%

## 7. GP Alignment

- **Track record:** none in this discipline — first ground-up project; whatever record exists is in a different, non-fungible business (`01`) 🟢. Unverified and unverifiable.
- **Fees vs risk:** the GP collects ~9% across two fee lines largely during construction — i.e., paid heavily *before* the LP's all-at-exit return is proven; without a disclosed pref/promote, alignment cannot be assessed (GEN-16), and with fees this front-loaded it tilts GP-favorable.
- **Co-invest:** not stated (GEN-01 unresolved). For a first-time developer, meaningful personal capital plus a completion guarantee is the minimum credible alignment.

## 8. Questions for the GP (`04`)

**Must-ask**
1. **Q-EXIT-01** (EQUITY-06) — why an exit cap below going-in basis; the IRR at exit cap ≥ going-in. *Bad answer:* "cap rates will compress"; no sensitivity.
2. **Q-DS-01** (GEN-08, EQUITY-06) — IRR decomposition; return at a flat exit cap. *Bad answer:* can't decompose; collapses at flat cap.
3. **Q-DS-03** (GEN-13) — bear case: costs +10%, 6-month delay, higher exit cap, slow lease-up. *Bad answer:* "we underwrite conservatively" with nothing shown.
4. Entitlement/permit status and the hard-cost budget with contingency % (`01` essential; `02`: <5% contingency is under-reserved). *Bad answer:* "entitlements are basically done"; no line-item budget.
5. **Q-RISK-01** (GEN-09) — construction-loan term vs the 3-year plan; takeout structure and lender. *Bad answer:* "we'll refinance at completion" with no committed takeout.
6. **Q-FEE-01 / Q-FEE-04** (GEN-16, EQUITY-04) — full waterfall: pref, promote, catch-up, clawback, and why both a development fee *and* a CM fee. *Bad answer:* fee stacking defended as "standard"; no pref.
7. **Q-FEE-02** (GEN-06) — is the CM (or the GC) a GP affiliate, and is its pricing third-party-benchmarked? *Bad answer:* "all arm's-length" without names.
8. **Q-GP-01** (GEN-01) — GP cash co-invest and personal completion guarantee. *Bad answer:* "our development fee is our skin in the game."
9. **Q-GP-02** (GEN-05, GEN-14) — full prior record, realized net-to-LP, and specifically who on the team has *delivered* ground-up before. *Bad answer:* acquisition-deal IRRs offered as development credentials.
10. **Q-MKT-01** (GEN-18) — absorption comps and supply pipeline behind lease-up assumptions. *Bad answer:* metro-level optimism.
11. **Q-DIST-01** (GEN-11) — when does any LP cash return before exit? *Bad answer:* silence.

**Nice-to-ask:** Q-DIST-02 (capital-call schedule and overrun-funding mechanics — escalate to must-ask if there is any LP recall/dilution provision), Q-LIQ-01.

## 9. Diligence Checklist

- Entitlement/permit documents from the municipality, not the sponsor
- Third-party review of the construction budget (cost consultant), GMP contract status, contingency adequacy
- Construction lender term sheet: term, extensions, recourse, completion guarantee
- Absorption/lease-up comps from independent market data
- Sponsor and principal background: prior projects in any role, litigation, liens
- Waterfall and fee schedule from the PPM — currently nonexistent in the materials

## 10. Verdict

**Pass as presented — insufficient disclosure.** All five `01` development essentials are missing, so the core return story — entitle, build on budget, lease, exit — cannot be underwritten on any axis. And this is not a neutral thin deal: what is disclosed stacks adversely — an above-category 25% target from a first-time developer (the widest-dispersion, least-forgiving category), ~9% of fees split across two lines (`02`'s named aggressive pattern), exit-cap compression (EQUITY-06), and a single upside-only pro forma (GEN-13) on an all-at-exit return profile (GEN-08). Biggest swing factor: execution risk of a first-time developer against a compressed-exit, zero-cushion plan. **Re-screen list:** entitlement/permit evidence; line-item budget with ≥5% contingency; committed debt structure with takeout; absorption comps; full waterfall and fee justification; co-invest and completion guarantee. Even with all of that delivered, the residual REDs (first-timer + compression + fee stacking) would need to clear — this deal suits only an LP explicitly pricing venture-grade development risk, and the disclosed 25% does not obviously pay for it.
