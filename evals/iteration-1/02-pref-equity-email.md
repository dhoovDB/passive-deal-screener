# Eval fixture 02 — Preferred equity, sparse sponsor email

*Iteration-1 run, 2026-07-03, against SKILL.md @ cddc52d. Fixture prompt: evals.json id 2.*

---

**Verdict: Pass as presented — do not wire.** This email discloses a rate, a minimum, and urgency; it withholds everything a preferred-equity commitment actually turns on. A deal this sparse is screened on what it withholds, and it withholds nearly all of it. Re-screen only if the sponsor produces the disclosure package below.

## 1. Deal Snapshot
- **Asset class:** Multifamily (segment — value-add? core? — not stated) 🟡
- **Deal type:** Preferred equity 🟢
- **Sponsor:** Not stated (unnamed in the email)
- **Geography:** Not stated
- **Minimum:** $25k 🟢
- **Hold / term:** Not stated
- **Raise:** Not stated
- **Claimed return:** 10% preferred return 🟢 — cumulative? compounding? current-pay or accrued? Not stated 🔴

Nearly every snapshot field feeds §6.

## 2. Return Stress-Test
The 10% pref sits inside `02`'s typical preferred-return range (8–12%), so the headline is not itself aggressive 🟢. But a pref is only as good as (a) the cushion beneath it and (b) the sponsor's ability to pay it — neither is disclosed. No stress-test is computable: position in the capital stack, attachment point, underlying asset performance, and term are all absent 🔴.

Benchmark (`05`): PFF 10yr = 3.72% → a 10% pref implies ≈630bps premium, comfortably above the ~300–400bps hurdle for a typical 3–5yr pref lock-up **if it is real, cumulative, and paid** 🟡. The spread is generous enough to ask *why* — a sponsor paying 10% for preferred capital in this market is paying up for money, which is itself a question (what cheaper capital said no?).

## 3. Where LP Returns Come From
Not determinable. A preferred return's source is the underlying deal's cash flow and the common equity cushion junior to it — neither the property's financials nor the capital stack is disclosed. If there is a promote or participation above the pref, this is equity risk dressed as preferred (`PREF-01`) — unknown 🔴.

## 4. Fee Stack Summary
**Not computable — that is the finding** (`GEN-16`). Preferred equity typically carries (per `02`): origination/placement 1–2%, servicing 0.5–1% annual, possible exit/maturity fee, possible equity kicker. None disclosed. The effective net yield on a "10% pref" can land materially below 10% once origination and servicing are netted — the gross-to-net drag is unknowable from this email.

## 5. Red Flags
**RED**
- `GEN-03`→RED in this presentation — "Exclusive," "limited allocation remaining," and **wire instructions attached to a cold solicitation** with no PPM, no sponsor identity, no underlying deal. Marketing urgency standing in for underwriting is a YELLOW; soliciting funds ahead of any disclosure pushes this presentation to pass-or-resolve. Exposure: this is the fact pattern of solicitation fraud as well as of merely sloppy sponsors — and the LP can't tell which from the email.

**YELLOW–RED**
- `GEN-16` — No fee or waterfall/structure disclosure: drag unknowable.
- `GEN-15` — Missing financials: no property, no T-12, no capital stack.

**Unresolvable as disclosed (treat as open, not clear):** `GEN-01` (co-invest), `GEN-02` (regulatory history — sponsor is unnamed, so it can't even be searched), `GEN-05`/`GEN-14` (track record), `PREF-01` (structure above the pref).

## 6. Missing Disclosures
This is the core output for this deal. Per `01` (multifamily essentials) and `02` (preferred equity inventory), a screenable preferred-equity offer discloses:
- **Sponsor identity and entity** — absent (blocks even a background search)
- **The underlying asset**: property, market, unit count, business plan — absent
- **Capital stack**: senior debt ahead of the pref, attachment/detachment, LTV — absent
- **Pref mechanics**: cumulative vs non-cumulative, simple vs compounding, current-pay vs accrued (`EQUITY-05` analog) — absent
- **Term / maturity and redemption mechanics** — absent
- **Fees**: origination, servicing, exit (`02` inventory) — absent
- **Equity kicker / participation and anything sitting above the pref** (`PREF-01`) — absent
- **Sponsor track record**, realized, net-to-LP — absent
- **Offering documents** (PPM/subscription) — absent; only wire instructions were attached
- **Rent roll / T-12 of the underlying property** — absent

## 7. GP Alignment
Nothing to assess: sponsor unnamed, co-invest undisclosed, track record undisclosed. Alignment is unverifiable as presented — stated as unverified, not assumed bad 🔴.

## 8. Questions for the GP
All must-ask — this deal cannot advance past any bad answer:
1. **Q-FEE-01** — Complete fee schedule and full structure (origination, servicing, exit, anything above the pref). *Bad answer:* "standard market fees"; "the PPM has it" without producing it. (`GEN-16`)
2. **Q-FEE-04** — Is the 10% pref cumulative and compounding? Current-pay or accrued? *Bad answer:* non-cumulative; accrual with no payment trigger. (`EQUITY-04`/`EQUITY-05`/`PREF-01`)
3. **Q-RISK-03** — The underlying property's T-12, rent roll, and complete senior debt terms. *Bad answer:* "confidential until you commit." (`GEN-12`/`GEN-15`)
4. **Q-GP-02** — Track record, net-to-LP, realized exits only. *Bad answer:* project-level IRR; "most deals are still performing." (`GEN-05`/`GEN-14`)
5. **Q-GP-03** — Regulatory action, enforcement, investor litigation. *Bad answer:* "nothing material." (`GEN-02`)
6. **Q-GP-01** — Sponsor cash co-invest, same terms. *Bad answer:* "sweat equity." (`GEN-01`)
7. **Q-LIQ-01** — Exit options before maturity. *Bad answer:* "a secondary market may develop."
8. Structural: **Where does this pref sit in the capital stack — how much senior debt is ahead of it, and what is the combined LTV through the pref?** *Bad answer:* can't or won't state the attachment point. (`PREF-01` context; `01` essentials)

## 9. Diligence Checklist
- [ ] Identify the sponsor entity and principals; background/regulatory search (`GEN-02`)
- [ ] PPM and subscription docs — before any funds move
- [ ] Underlying property underwriting package (T-12, rent roll, debt terms)
- [ ] Capital-stack verification: senior loan docs, intercreditor/recognition rights
- [ ] Verify the offering is a registered/exempt offering (Reg D filing search)

## 10. Verdict
**Pass as presented.** Not because a 10% multifamily pref is unattractive — the rate is in range and the PFF spread is generous — but because the email discloses nothing that lets an LP underwrite the pref's safety, and pairs that absence with urgency language and wire instructions. The absence pattern *is* the analysis: a sponsor with a sound deal sends a package; a sponsor with wire instructions and "limited allocation" is selling scarcity, not disclosure. **What would have to be true to re-screen:** the full §6 package arrives, the sponsor is identifiable and clean on a background search, and the pref's mechanics survive Q-FEE-04. Suits no LP in current form.
