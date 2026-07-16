# "An Overview of Outcomes" — planning notes

Presenter: **Nora Schrag** (Livestock Veterinary Resources)
Meeting: *Antimicrobial Use Data Collection: Approaches, Metrics, Data Gaps and Reporting*
Date: July 17, 2026 · Midland Hills Country Club, Roseville, MN (+ Zoom)
Slot: **11:00 AM — "Antimicrobial Use Outcomes / Outcomes overview"** (~20–25 min, opens the session)
Immediately followed by: **Bruce Stewart-Brown & Ken Opengart — "Outcome measurements used in poultry."**
(Afternoon continues: companion-animal outcomes — Granick/Bollig/Beaudoin; then other species / group discussion.)

---

## The through-line (thesis)
**Trending outcomes over time, within farm context, is the only way to drive data-driven action on antimicrobial use.**

## The narrative spine — "our journey"
1. **Why we started.** Respect for the *power of effective antimicrobials* + a desire to act so these tools stay functional as long as possible. Motivation is stewardship, not restriction for its own sake.
2. **To act, we had to measure use — and use needs disease context.** You can't interpret AMU in a vacuum.
3. **So regimens became our favored AMU metric** — because a regimen has a well-defined relationship to reality and to disease (dose × duration × indication), unlike blunter sales/weight metrics.
4. **But the real question surfaced fast: did the drug work?** Therapeutic outcome is the ultimate question. Use measurement was a means; outcomes are the end.
5. **Why outcomes drive stewardship.** If we know whether use improves animal welfare, we can drive *appropriate* use directly: **effective → use it; not effective → don't.** Welfare is the anchor.
6. **Outcomes only mean something as trends over time, in farm context:** ↓ mortality, ↓ morbidity, ↑ therapeutic success.
7. **Outcomes shift each other (the concrete example).** If the outcome of interest is **therapeutic success**, it can be pulled down by:
   - **Death** → unambiguously bad.
   - **Aggressive retreatment** → not inherently good or bad, BUT a change in it over time warrants investigation.
   → The lesson: a single number is uninterpretable; the *interaction and the trend within a farm* is what points to action.
8. **Landing:** data-driven action requires within-farm trends over time — not cross-sectional snapshots, not use data alone.

## Where Bruce's ARG question fits (framing, not rebuttal)
- Bruce (email): can **ARGs / resistance genes** — in animals or environment (wastewater) — serve as a valid measure of AMR "current state" and "progress over time," irrespective of use?
- Handle as a **levels-of-measurement map**, then hand to Bruce:
  **Use → Resistance (ARGs / phenotype) → Therapeutic outcome → Animal welfare & system performance.**
- **Validate:** he's right that progress-over-time has been badly under-measured; ARG/wastewater surveillance is a real, important frontier.
- **Reframe (defensible version):** resistance measurement gives a *state*; outcomes give a *decision*. *Outcomes tell you what to do when the resistance science is still uncertain or contested.* Outcomes give AMR data meaning — they don't replace it.
- Avoid the phrasing "outcomes trump resistance science" in the room (draws fire from Ivanek/Apley); use the "what to do under uncertainty" version.
- Rhetorical payoff: elevate Bruce's question into the organizing frame for the whole day, then literally hand him the floor.

## Audience (expert; tri-partite — no AMR 101, no assumed consensus on metrics)
- **Regulators/policy:** Kate Huebner + FDA-CVM contingent (Mongeluzzi, McCoig, Cornwell, Tadesse, Ceric), Edie Marshall (CDFA), AVMA (Murphy, Costin), OFW Law (antitrust counsel).
- **Academic:** Randy Singer (organizer, epi), Mike Apley (KSU pharmacology/feedlot — will scrutinize outcome definitions), Renata Ivanek (Cornell, modeling/AMR dynamics — most likely to press ARG methodology), Majid Jaberi-Douraki (KSU data science), UMN group (Granick, Bollig, Beaudoin).
- **Industry:** Bruce Stewart-Brown (Perdue) & Ken Opengart (3 Birds) — poultry; Rebecca Robbins (Seaboard) & Heather Fowler (Pork Board) — swine; Denise Heard (USPOULTRY).
- Framing consequence: present outcomes as a **metric with definitional + data-quality challenges** (fits the meeting subtitle "Approaches, Metrics, Data Gaps and Reporting"), not a soft welfare appeal.

## Format / build decisions (tentative)
- **Primary:** Quarto `revealjs` (HTML slides) — renders in-repo, sharp, `pptx` export possible later.
- Must **not leak into the published ICASAProject site** (current `_quarto.yml render:` is limited to the three page `.qmd`s; keep this file excluded).
- Concrete-example figure(s): build with **R** (already installed here — R 4.6.1 / 4.2.3); no Python needed for the core deck. Python installable if a specific tool helps.
- Likely a synthetic/illustrative dataset for the "outcomes shift each other" example unless we pull real feedlot numbers from the ICASA_Disease work.

## Open questions for Nora
- Exact time budget (assume ~20–25 min?).
- Real ICASA feedlot outcome data in the example, or synthetic/illustrative?
- Any existing figures/branding to match?

## Status: ORGANIZING — awaiting more context from Nora before drafting.
