# Lit search — how "therapeutic / treatment outcomes" for antimicrobials have been defined
Scope per Nora: **human medicine + cattle only.** (Poultry & small-animal outcomes covered by other speakers — deliberately excluded.)

> **⚠️ SUPERSEDED IN PART (2026-07-16).** Nora later asked for a cross-species + agriculture
> sweep — see **`litsearch-round2-cross-species-regulatory.md`**. That round breaks this
> scope, but *for briefing only*: other-species material is so she's prepared for what
> other speakers raise, **not** for slides. Round 2 also surfaces material that stresses
> the DOOR/RADAR framing below (VanBuren 2025: RADAR can invert the truth) and adds the
> US regulatory-vacuum arc. Read Round 2's §5 (deck impact) and §6 (traps) alongside this.

Big-picture finding: **Both human ID medicine and cattle medicine started with a single "did the bug clear / did it cure" endpoint, found it distorts interpretation, and moved toward multi-dimensional, patient-/animal-level, whole-course outcome measures.** That trajectory is the same one Nora's benchmarking work reached in production animals. Human medicine gives Nora a credible, independent precedent for "don't reduce it to one number."

---

## A. HUMAN MEDICINE

### A1. The classic endpoints (and their known failure)
- **Clinical cure** = resolution of signs/symptoms at a Test-of-Cure visit. **Microbiological (bacteriological) cure** = pathogen no longer detectable (e.g., <10^3 CFU/mL). **Radiographic cure** for pneumonia.
- FDA guidance for several indications uses a **composite clinical + microbiological endpoint** at a fixed post-treatment timepoint (e.g., cUTI/uUTI day 14). For HAP/VAP, FDA uses **all-cause mortality** as primary endpoint.
- Key admitted problem: **"microbiologic cure is not synonymous with improved health and recovery."** Patients can be micro-failures but clinically well, and vice versa → single endpoints misclassify.
  - Sources: FDA endpoints reanalyses (PMC10661658); COMBACTE STAT-Net perspective on endpoints for severe infection (PMC5487537); discordant clinical/micro outcomes in cUTI (PubMed 36625164).

### A2. Antimicrobial stewardship metrics framework
- AMS metrics classified as **structural / process / outcome**. Outcome metrics = **in-hospital mortality, length of stay, 30-day readmission, C. difficile, infection-related mortality.**
- Documented **gap between what clinicians value and what's measured** (infection-related mortality valued 34% vs measured 7%). → parallels Nora's point that we measure use because it's easy, but outcome is what matters.
  - Sources: Expert consensus on AMS metrics (PMC5241782); AMS measures/metrics review (PMC4431704); Sanford Guide AMS metrics.

### A3. THE key parallel — DOOR / RADAR (patient-centric, whole-course ranking)
- **Evans SR et al., "Desirability of Outcome Ranking (DOOR) and Response Adjusted for Duration of Antibiotic Risk (RADAR)," Clin Infect Dis 2015;61(5):800–806.** https://academic.oup.com/cid/article/61/5/800/304719
- Idea: stop collapsing to one endpoint. **Rank each patient's ENTIRE clinical course** on an ordinal desirability scale that **combines benefits AND harms**, and break ties by **shorter antibiotic duration** (RADAR). Higher rank = better overall outcome + less antibiotic risk.
- Motivation (quotable): trials are "limited by competing risks that distort outcome interpretation… and inadequate evaluation of benefits and harms at the patient level."
- Now operationalized for real indications: **"Moving Beyond Mortality: a DOOR endpoint for HAP/VABP," Clin Infect Dis 2024;78(2):259.** https://academic.oup.com/cid/article/78/2/259/7280930 — title alone is a gift for the talk. Also ABSSSI, cIAI, intra-abdominal DOOR analyses.
- **Why it matters for Nora:** human medicine's frontier endpoint is literally "an ordinal ranking of the whole outcome including harms and duration, because one number lies." Nora's within-farm, multi-outcome (Success/Relapse/Sold/Died) benchmarking is the **herd/production analog of DOOR.** Strong "we're not alone / this is where the science is going" slide.

---

## B. CATTLE

### B1. Feedlot BRD — the dominant outcome framework
- **Standard outcomes:** First Treatment Success (FTS), Case Fatality Risk all-cause (CFR_all) and BRD-specific (CFR_BRD), relapse (1st/2nd/3rd), and chronicity (chronic "railer" animals).
- **Concrete benchmark numbers** — 132,521 initial BRD treatments, 14 central US feedyards (2017–2020): **FTS 67.8%, CFR_all 10.0%, CFR_BRD 6.3%.**
  - Source: "Risk factors associated with case fatality and treatment success following initial BRD treatment," Bovine Practitioner 58(2), 2024. https://bovine-ojs-tamu.tdl.org/bovine/article/view/9012
- **No standardized case definition exists** (Apley): diagnosis = visual observation + rectal-temp threshold, repeatedly shown inaccurate. → outcome measurement inherits diagnostic noise; a reason to trend within-farm rather than compare absolute levels across farms.
  - Source: refined case-definition trial (PMC7575691); BRD diagnosis reviews (PMC10885951).

### B2. THE retreatment nuance, scientifically grounded — Post-Treatment Interval (PTI)
- **PTI = time that must pass after treatment before an animal is eligible for retreatment.** If PTI is too short, an animal still in its normal recovery window gets counted as a "failure" and re-treated.
- Field study of gamithromycin PTIs (eligible at 3/6/9/12 days): **animals eligible for retreatment at 3 days had higher retreatment rates** — i.e., "failure" was partly an artifact of measuring too soon.
- **This is the mechanism behind Nora's "aggressive retreatment" point:** a rising retreatment/relapse rate can reflect a shortened effective PTI or protocol change, not true drug failure → *investigate the trend, don't just read the number.*
  - Sources: "Role of Timing in BRD Retreatment Decisions" (Drovers, summarizing PTI field trial); AMU 20 feedyards 2018–19 defines the exact **30-day window: death (any cause) within 30d, OR retreated for that disease within 30d, else success** (matches Nora's method).

### B3. Retreatment ↔ resistance (bridge to Bruce)
- **"Switching between bacteriostatic and bactericidal antimicrobials for retreatment of BRD relapses is associated with increased frequency of resistant pathogen isolation."** biorxiv 675066. → retreatment behavior is itself linked to resistance signals; another reason retreatment trends deserve scrutiny, and a concrete tie between OUTCOME dynamics and Bruce's AMR question.
- Also class-selection retreatment outcomes: PMC7179807 (AMD class for treatment/retreatment vs health, performance, carcass).

### B4. Dairy mastitis — an entire literature on "what is success"
- **Ruegg / selective treatment:** goals = **clinical cure + bacteriological cure while minimizing health/economic harm**; treat only cases with higher odds of bacteriological cure. (Invited review, J Dairy Sci 2023, S0022-0302(23)00182-0.)
- **Middleton/… "What Is Success? A Narrative Review of Research Evaluating Outcomes of Antibiotics Used for Treatment of Clinical Mastitis," Front Vet Sci 2021.** https://www.frontiersin.org/journals/veterinary-science/articles/10.3389/fvets.2021.639641/full
  - Six outcomes used across studies, each defined inconsistently: **Bacteriological cure (BC) 27–95% across studies** depending on sampling (single vs multiple, day 7/14 vs 21–28); **Clinical cure** = "milk/gland returned to normal," but observed anywhere from **day 2 to day 28**; **SCC cure** (thresholds 200k or 250k, 7–90 d); plus recurrence, milk yield, culling (each in <8 studies).
  - **Killer quotes:**
    - "Return to normal milk appearance… is not a reliable indicator of therapeutic success."
    - "The finding of differences in BC in research trials does not appear to be predictive of differences in clinical outcomes."
    - "Few researchers have evaluated important clinical outcomes such as post-treatment milk yield or culling."
  - **Use for talk:** even within ONE cattle disease, "success" is defined a dozen ways and the easy-to-measure endpoint (milk appearance / BC) doesn't predict what we care about → you must define outcomes deliberately, in context, and trend them.

---

## C. SYNTHESIS — how to deploy in the talk
1. **Human medicine's arc validates Nora's thesis.** Micro-cure → composite → **DOOR/RADAR** = the field concluded a single endpoint distorts, so rank the whole course incl. harms + duration. Nora reached the same conclusion for herds (Success/Relapse/Sold/Died, in disease + use context). Slide line: *"Moving beyond mortality" — human ID medicine's own words.*
2. **Cattle already has the vocabulary** (FTS, CFR, relapse, chronic; 30-day window) — Nora's contribution is putting it **in disease + use context and trending it within farm.**
3. **The retreatment nuance is real science, not hand-waving** — PTI shows early retreatment manufactures "failure"; retreatment switching is linked to resistance. → justifies "investigate the trend."
4. **"What is success?" is unsettled even in one disease** (mastitis review) → deliberate, contextual, trended outcome definitions are necessary, not optional.
5. **Bruce bridge:** outcome dynamics (retreatment, relapse) connect to resistance signals; outcomes are the actionable, welfare-anchored layer while resistance measurement stays method-dependent and contested.

## Full-text still worth pulling if desired
- Evans 2015 DOOR/RADAR (CID) — for the exact ranking schema graphic.
- "Moving Beyond Mortality" HAP/VABP DOOR 2024 (CID) — for a ready-made human-side outcome-ladder figure.
- Bovine Practitioner 2024 FTS/CFR risk-factor paper — for exact BRD outcome definitions & denominators.
