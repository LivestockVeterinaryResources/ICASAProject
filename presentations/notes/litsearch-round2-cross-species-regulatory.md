# Lit search — Round 2: cross-species + regulatory/consensus frameworks

**Date:** 2026-07-16 (day before the talk)
**Prompted by Nora:** *"Are there other key papers related to evaluating antimicrobial
therapy outcomes that we should be mentioning? Any species, maybe even agriculture?"*

**Scope change from Round 1.** `litsearch-treatment-outcomes.md` was deliberately
scoped **human + cattle only** ("poultry & small-animal outcomes covered by other
speakers"). This round deliberately breaks that scope.

**Nora's stated purpose for the other-species material (2026-07-16):**
> *"I don't want to know about the other species to make slides, I want to know about
> them so I am prepared and aware of what other people might discuss."*

So: **§3 (human/regulatory) is slide material. §4 (other species) is briefing
material — for the Q&A and the hallway, not the deck.**

---

## 1. How to read this file

Five parallel research agents ran this; each was instructed to return only verifiable
sources with persistent identifiers, to state full-text vs abstract verification, and
to report negative findings honestly. **Verification status is recorded per item and
matters — do not put an unverified quote on a slide.** Agents explicitly discarded
several false negatives caused by publisher fetch-blocking (fda.gov, canada.ca, Wiley,
Cambridge return 403s and can masquerade as "no evidence of X").

Where an agent flagged a claim as unverified or soft, that flag is preserved below.
**§7 lists the open gaps that still need closing.**

> ### ⚠️ READ THIS BEFORE USING §3D
> The one gap that mattered has been **closed, and it falsified a claim in this file.**
> **A core outcome set for bovine respiratory disease DOES exist** — registered and
> ongoing at Guelph (COMET 3214, Renaud/Winder, due Dec 2026). **Never say "zero core
> outcome sets for food animals" or "our field has never done this."** The corrected,
> safe wording is in the boxed CORRECTION in **§3D**. Everything else in §3D stands.

---

## 2. Bottom line

1. **The strongest new material is not about other species.** It is (a) the honesty
   literature on DOOR's own limits, and (b) the regulatory vacuum in the US.
2. **One paper cuts against the current deck** and Nora needs to know it: DOOR/RADAR
   has been simulated declaring *placebo superior while placebo killed more children*.
3. **USDA already built Nora's four-category model — in 2011 — and never trended it.**
4. **No national AMU/AMR monitoring program measures whether the drug worked.** This is
   verified in the strong form (exhaustive field enumerations, not argument-from-silence).
5. **Across sectors, outcome measurement tracks whether a treated individual exists to
   follow.** Humans → DOOR. Cattle → Nora's model. Fish → tank mortality. Orchards →
   nothing. Her model is not a refinement of what other sectors do; it's a category most
   of them cannot reach.

---

## 3. SLIDE MATERIAL

### 3A. ★ The honesty arc — DOOR's own limits

#### VanBuren JM, Banks RK, Kuppermann N, Gerber JS, Ruddy RM, Casper TC, Florin TA.
"Evaluating the desirability of outcome ranking and response adjusted for duration of
antibiotic risk for clinical trials of antibiotics in pediatric pneumonia."
*Am J Epidemiol.* 2025;194(4):1090–1096. **DOI 10.1093/aje/kwae237 · PMID 39049448 ·
PMCID PMC12060002.** — **FULL TEXT VERIFIED (PMC).**

Monte Carlo, 10,000 iterations/scenario. In the scenario where amoxicillin was *genuinely
efficacious*, verbatim from full text:

> "the placebo group had an absolute increase in inadequate clinical response with
> additional emergency department or clinic visits of 7% (3% in the antibiotic group;
> 10% in the placebo group), an absolute increase in hospitalization of 8% (0.95%
> antibiotic group; 8.95% placebo group), and an absolute increase in rate of death of
> 4% (0.05% antibiotic group; 4.05% placebo group), **yet DOOR/RADAR identified placebo
> as the superior treatment.**"

> "patients receiving placebo had more than a 50% probability of the better outcome (56%)
> even though DOOR appropriately concluded amoxicillin was efficacious (41%)."

**CRITICAL NUANCE:** **DOOR alone got it right (41%). RADAR broke it.** The failure came
from bolting the "less antibiotic is better" duration preference onto the clinical
outcome. Do not state this as "DOOR is broken" — that's wrong and Apley/Ivanek would
catch it.

**Why it matters:** the deck currently leans on DOOR/RADAR as the credibility anchor
("we're not alone"). This paper is a live risk if someone in the room knows it and Nora
doesn't. It is also *on-thesis* — a composite is still a single number, and it hid a
component that mattered. Own it rather than avoid it.

#### ★ Evans S, Follmann D, Schoenfeld D, Fowler VG Jr, Chambers HF. "Reply to Phillips, Morris, and Walker."
*Clin Infect Dis.* 2015 Dec 9;62(6):815–816. **DOI 10.1093/cid/civ1003 · PMID 26658301 ·
PMCID PMC4772839.** — **FULL TEXT VERIFIED (PMC).**

⚠️ **This is a SEPARATE paper from Evans 2015 CID 61(5):800** (the DOOR/RADAR article
already in the deck). It is the inventors' rebuttal letter. **The single most valuable
find of this round.** The creators of DOOR concede Nora's exact thesis in print:

> "DOOR/RADAR results don't necessarily imply similar results on component outcomes.
> This is concerning when component outcomes have differing levels of importance and the
> influence of the less important components is too large."

> "DOOR/RADAR shouldn't be used to hide inferiority of important component outcomes."

> "DOOR novelty can increase complexity."

**Use:** converts "a single number lies" from Nora's opinion into the method architects'
own stated position. *"I'm not attacking composite outcomes — the people who invented the
leading composite outcome say the same thing I do."*

#### Phillips PPJ, Morris TP, Walker AS. "DOOR/RADAR: A Gateway Into the Unknown?"
*Clin Infect Dis.* 2016;62(6):814–815. **DOI 10.1093/cid/civ1002.** — extract verified on
publisher page; **full text paywalled. PMID not confirmed — cite by DOI.**

The formal published objection Evans is replying to:
> "Introducing a completely new effect measure may increase rather than reduce complexity
> and could potentially be misinterpreted."

#### Ajufo E, Nayak A, Mehra MR. "Fallacies of Using the Win Ratio in Cardiovascular Trials."
*JACC Basic Transl Sci.* 2023;8(6):720–727. **DOI 10.1016/j.jacbts.2023.05.004 ·
PMID 37426527 · PMCID PMC10322884.** — **ABSTRACT VERIFIED ONLY** (full text 403/CAPTCHA).

> win ratio advantages "may be counterbalanced by several fallacies (such as ignoring
> ties and weighting each hierarchal component equally)..."

**Use:** generalizes the problem — it's inherent to *any* ranked composite, including
anything vet AMU might build. Two named failure modes to design around: **ties** and
**equal weighting**.

---

### 3B. ★ Whose values are in the ranks?

#### Finer E, Pulia MS, Harrison JD, et al. "A desirability of outcome ranking for adults with non-severe community-acquired pneumonia: a comparison of physician and patient preferences."
*Antimicrob Steward Healthc Epidemiol.* 2025;5(1):e282. **DOI 10.1017/ash.2025.10195 ·
PMID 41180299 · PMCID PMC12571681.** — **FULL TEXT VERIFIED.**

25 physicians and 20 hospitalized pneumonia patients ranked nine outcome vignettes.

> "When comparing component rankings between physicians and patients, ranks for **7 of the
> 9** initial case vignettes differed significantly."

Physicians prioritized death and readmission; **patients ranked antibiotic side effects —
nausea, *C. difficile* — as substantially worse.**

**Use:** the empirical backbone for the new partial-credit slide ("Who decides how bad
'bad' is?"). The vet's ranking of Success/Relapse/Sold/Died is *not* the producer's
ranking — and **"Sold" is exactly where vet and owner values diverge.** One line on that
slide; doesn't need its own.

#### Doernberg SB, Tran TTT, Tong SYC, ... Evans SR, Holland TL (ARLG). "Good Studies Evaluate the Disease While Great Studies Evaluate the Patient: Development and Application of a DOOR Endpoint for *Staphylococcus aureus* Bloodstream Infection."
*Clin Infect Dis.* 2019;68(10):1691–1698. **DOI 10.1093/cid/ciy766 · PMID 30321315.** —
**ABSTRACT VERIFIED ONLY.**

42 ID clinicians (97% response) ranked 20 real *S. aureus* BSI cases by global
desirability; agreement **r = 0.89**.

**Use:** the defensible answer to *"who decided Relapse is worse than Sold?"* — you
**measure** the ranking with a vignette survey and report the agreement statistic, rather
than asserting it. (Title alone is quotable.)

---

### 3C. ★★ The regulatory vacuum — "everyone promised the outcome; nobody built the measurement"

This is the strongest new *arc*, and it is aimed squarely at a room containing FDA.

**Everyone names the outcome:**

- **FDA's own definition of judicious use** is anchored to clinical outcome:
  > "Judicious use is defined as the optimal selection, dosage, and duration of
  > antimicrobial treatment that **results in the best clinical outcome** for the
  > treatment or prevention of infection, with minimal toxicity to the patient and
  > minimal impact on subsequent resistance."

  ⚠️ **CITATION TRAP — this is NOT in GFI #209.** Search engines confidently misattribute
  it. It is **footnote 1 of GFI #273 (FINAL, February 2026)**, sourced to *Supporting
  Antimicrobial Stewardship in Veterinary Settings, Goals for FY2024–2028*.
  **Final PDF: https://www.fda.gov/media/191092/download** — FDA's own search page still
  serves the Sept 2023 *draft* (`/media/172362/download`). Attributing this to #209 in
  front of CVM would be an unforced error. *(Footnote read verbatim.)*

- **AVMA, Antimicrobial Stewardship Definition and Core Principles:**
  > "Demonstrate commitment to systematically assessing the outcomes of antimicrobial
  > drug therapy."

  Outcome assessment appears in 3 of 5 core principles — **and is never defined or
  operationalized.** Note the asymmetry: Principle 4, the only one built into an actual
  program with feedback loops, is scoped to **prescribing/use data, not outcomes**.
  ⚠️ *AVMA blocks fetch; text is summarizer-mediated (two independent passes returned
  character-identical quotes). Eyeball before slide use.*

- **AABP/AVC, *Joint AABP-AVC Judicious Therapeutic Use of Medically Important
  Antimicrobials in Cattle*, March 2024** —
  https://www.aabp.org/resources/AABP_Guidelines/Antimicrobials_2024_guideline.pdf
  (**read in full**). Outcome evaluation is made *constitutive of stewardship itself*:
  > stewardship involves "using antimicrobials judiciously, sparingly, and **with
  > continual evaluation of the outcomes of therapy**, respecting the client's available
  > resources."

  But the operational text doesn't follow through: 4d monitors **use** (record/inventory/
  purchase-history reconciliation); 4f asks vets to evaluate efficacy "as information
  becomes available" — a *consumer* of evidence, not a generator. **No case definitions,
  no treatment-success definitions anywhere in the document.**
  *Naming note: "Prudent Drug Usage Guidelines for Cattle" is a legacy title (AVMA hosts
  a stale URL) — don't cite as current.*

**Nobody built it:**

- **★ There is no FDA BRD effectiveness guidance.** An agent parsed the **complete
  184-entry GFI list** (https://www.fda.gov/animal-veterinary/guidance-industry/guidance-number).
  The *only* respiratory-disease effectiveness guidance is **GFI #178, "Recommended
  Design and Evaluation of Effectiveness Studies for Swine Respiratory Disease Claims"
  (Oct 2007)**. The only bovine-specific effectiveness guidance is **GFI #49 (mastitis)**.
  **For the single largest use of antimicrobials in US cattle, FDA's published success
  definition is for pigs.**

- **★ ZACTRAN (gamithromycin) FOI Summary, NADA 141-328, approved June 16, 2011** —
  https://animaldrugsatfda.fda.gov/adafda/app/search/public/document/downloadFoi/886
  (**read in full text**). *Note: this is the exact drug in the existing PTI slide.*
  > "The primary variable was treatment success on Day 10. **Treatment success was defined
  > as any animal that remained alive and in the study on Day 10 and was not classified as
  > a treatment failure.**"

  Success is defined **negatively**. The real definition is failure (mortality/euthanasia
  due to BRD; depression ≥1 OR respiratory ≥2 **AND** temp ≥104.0°F; respiratory = 3
  regardless of temp; depression ≥3 regardless of temp).

  **Exhaustive term scan of the entire approval document:**
  | term | count |
  |---|---|
  | relapse / relapsed | **0** |
  | retreat | **0** |
  | second treatment | **0** |
  | sold | **0** |
  | salvage | **0** |
  | cull | **0** |
  | Day 30 / Day 60 / long-term | **0** |

  Results: Day-10 success 91/106 (86%) gamithromycin vs 19/53 (37%) saline (p=0.0019);
  control/metaphylaxis study 120/154 (78%) vs 90/154 (58%) (p=0.0016).

- **GFI #178 (swine) — what a published FDA success definition looks like** —
  https://www.fda.gov/media/69903/download (**read in full**). Table 1 verbatim:
  **SUCCESS** = Alive **and** T <104°F **and** Respiratory score ≤1 **and** Depression
  score ≤1. **FAILURE** = "All pigs that do not meet the definition of success on the
  evaluation day(s)." Plus: *"CVM considers success/failure determination as the primary
  variable for SRD studies"* and — **"Mortality may be a secondary variable."**
  → FDA's only published respiratory success definition collapses the animal to a
  one-day binary and **demotes death to secondary**.

- **VICH GL9 / GFI #85 (Good Clinical Practice)** — https://www.fda.gov/media/70333/download
  (**read in full**). Exhaustive counts: `treatment success` **0**, `endpoint` **0**,
  `efficacy variable` **0**, `relapse` **0**, `outcome` **2** (both procedural, referring
  to *the study's* outcome). → **Governs how rigorously you collect the data; never says
  what to collect.**

- **VFD rule, 21 CFR 558.6** — `outcome`, `effectiveness`, `efficacy`, `morbidity`,
  `mortality`, `treatment success` each appear **ZERO** times. The 15 mandatory fields
  (§558.6(b)(3)(i)–(xv)) are entirely authorization/exposure data. **Fifteen required
  fields, not one of which is whether the animal lived.**

- **GFI #263** is the one place FDA touches outcomes (§IV, read in full):
  > "The decision by the veterinarian to use a specific approved drug is generally based
  > on multiple factors, such as... **past treatment outcomes**, local burden of illness
  > information, and concurrent animal health issues."

  → FDA **assumes** the vet has past treatment outcomes to reason from. It has never
  required, defined, or standardized their capture.

#### ★★★ THE GIFT: USDA already built Nora's model — in 2011

**NAHMS Feedlot 2011, Part IV: Health and Health Management** —
https://www.aphis.usda.gov/animal_health/nahms/feedlot/downloads/feedlot2011/Feed11_dr_PartIV.pdf
(**read in full text**; `retreat` appears **44** times).

**Table D.2.g**, "For cattle that required a second retreatment for respiratory disease,
percentage of cattle by outcome" — categories read verbatim:

> **Responded** · **Died** · **Were considered chronics and were realized**

| | Responded | Died | Chronics realized |
|---|---|---|---|
| <700 lb | **37.9%** | **30.5%** | **22.1%** |
| ≥700 lb | **45.2%** | **31.4%** | **29.3%** |

> "The response rate to a second retreatment was lower... (37.9 and 45.2 percent,
> respectively) than the response rate to either an initial treatment (more than 80
> percent) or the first retreatment (from 60 and 70 percent)."

**That is Success / Relapse (retreatment) / Sold ("realized") / Died.** USDA validated the
*shape* of Nora's model — once, at national level, cross-sectionally, **and never turned
it into a trend.**

**The companion quote — NAHMS Feedlot '99**, *"Treatment of Respiratory Disease in U.S.
Feedlots"* — https://www.aphis.usda.gov/animal_health/nahms/feedlot/downloads/feedlot99/Feedlot99_is_TreatResp.pdf
(**read in full**). USDA says in print it could not answer whether treatment worked
*because it didn't collect the data*:
> "the economic advantages or disadvantages of increasing the number of product types for
> the treatment of BRD **cannot be evaluated because treatment success, case fatality
> rate, and chronicity data were not collected.** Therefore, it is unclear if
> administering pharmaceuticals and supportive therapies in addition to an injectable
> antimicrobial for BRD is advantageous."

⚠️ **HONEST LIMIT:** NAHMS *Health Management on U.S. Feedlots 2021, Part I (Management
Practices)* (https://www.aphis.usda.gov/sites/default/files/feedlot-health-2021-mgmt-practice-dr1.pdf,
read in full) has `retreat` **0**, `chronic` **0**, `realiz` **0**. But **it was not
confirmed whether a 2021 health report carrying a retreatment-outcome table exists or is
forthcoming.** **Do not claim NAHMS 2021 dropped the measure** — claim only that Part I
does not carry it.

#### ★★ The surveillance negative — verified in the STRONG form

**No national AMU/AMR monitoring program collects therapeutic outcome data.**

| Program | Collects | Outcome? | Confidence |
|---|---|---|---|
| **FDA ADUFA §105** | Sales/distribution volumes only | **No** | Very high |
| **NARMS** | Susceptibility of enteric isolates | **No** | Very high |
| **DANMAP + VetStat** (DK) | Use (incl. disease *indication*) + resistance | **No** | Very high |
| **EU ASU / ESUAvet** | Packages sold + used ÷ animal population | **No** | Very high |
| **WOAH ANIMUSE** | AMU only (no resistance at all) | **No** | Very high |
| **UK-VARSS** | Sales, use, resistance | **No** | Very high |
| **MARAN / SDa** (NL) | Sales, use (DDDA), resistance | **No** | High |
| **CIPARS** (CA) | Use + reason for use + resistance | **No** | Moderate-high ⚠️ |

**This is affirmative evidence, not argument-from-silence.** For DANMAP Ch.10, the EMA ASU
protocol, the WOAH template, and the VFD rule, these are **exhaustive field
enumerations** — a complete list of what is collected, with no outcome field in it.

- **EMA ASU technical implementation protocol (EMA/27838/2024, 52 pp, read in full)** —
  a field-by-field spec. Counts: **`outcome` 0, `efficacy` 0, `cure` 0, `recover` 0,
  `clinical` 0, `mortality` 0, `morbidity` 0, `diagnosis` 0.** EU mandatory reporting
  **doesn't even collect indication** — purely packages sold/used ÷ population.
- **FDA ADUFA's own concession:**
  > "These sales and distribution data **only reflect the total quantity of antimicrobial
  > drug product that enters the market, and does not represent how much or in what way
  > these drugs are ultimately used.**"

  → ADUFA doesn't even reach *use*, let alone whether it worked.
- **NARMS:** isolates come from retail meat and cecal contents **at slaughter — never
  linked to a treated animal or a treatment event.** Program page scan: `outcome` 0,
  `treatment` 0.
- **★ UK-VARSS 2024 (184 pp, read in full)** — the best quote available, because it is
  **the program itself conceding resistance ≠ outcome** (→ this is the **Bruce bridge**):
  > "the results in this chapter **do not necessarily indicate that a 'resistant' isolate
  > would correspond to a clinical treatment failure** (drug-resistant infection)."

  And on why its clinical chapter can't fill the gap:
  > "As this is a passive programme, the results in this chapter should not be considered
  > representative of AMR in animal populations..." — sampling biased because "**treatment
  > failure is a frequent reason for submission of samples.**"
- **DANMAP/VetStat** captures a **disease category** (indication) — 6 disease groups for
  pigs. Indication ≠ outcome. A VetStat methods paper (arXiv 1705.08663, full text read)
  is blunt that it's *purchase* data: *"the system had to make a compromise to only
  include purchase data in VetStat..."* and notes the disease code is unreliable
  (off-label use, pharmacy typing errors, herd diagnostic prescriptions).

⚠️ **TERMINOLOGY TRAP — pre-empt this.** EU/UK programs publish **"harmonised outcome
indicators."** This does **NOT** mean therapeutic outcome. In UK-VARSS it means (a) mg/kg
sales and (b) % of *E. coli* fully susceptible. **If a regulator says "we already monitor
outcomes," this is the confusion.**

⚠️ **SCOPE DISCIPLINE FOR THE PODIUM.** Eight programs were verified. The defensible claim
is *"no national AMU/AMR monitoring program collects therapeutic outcome data — they stop
at use and resistance,"* plus *"the one USDA survey that did collect it, collected it once
and never trended it."* **Do NOT say "no program anywhere in the world."**
**Weakest link: CIPARS** — canada.ca blocked every fetch; the conclusion rests on
peer-reviewed papers describing CIPARS methods, not the program's own methods chapter.
Soften it, or verify from a network that can reach canada.ca.

---

### 3D. The fix: core outcome sets (a transferable, published method)

- **Williamson PR, et al. "The COMET Handbook: version 1.0."** *Trials.* 2017;18(Suppl 3):280.
  **DOI 10.1186/s13063-017-1978-4 · PMID 28681707 · PMCID PMC5499094.** — abstract verified.
  The recipe: systematic review of outcomes already reported → candidate list → multi-round
  Delphi across stakeholder groups → consensus meeting → ratify.
- **Kirkham JJ, et al. "COS-STAD recommendations."** *PLoS Med.* 2017;14(11):e1002447.
  **DOI 10.1371/journal.pmed.1002447 · PMID 29145404 · PMCID PMC5689835.** — **full text
  verified.** The quality bar: **11 minimum standards across 3 domains** (Scope 4,
  Stakeholders 3, Consensus Process 4). Consensus threshold verified: *"at least 70% of
  the voting participants from each stakeholder group providing a score between 7 and 9."*
  ⚠️ An extracted sentence beginning *"The main rationales for COS are the need to improve
  comparability across similar trials..."* could **not** be confirmed verbatim — **do not
  quote it.**
- **★ Nguyen HQ, Bradley DT, Tunney MM, Hughes CM. "Development of a core outcome set for
  clinical trials aimed at improving antimicrobial stewardship in care homes."**
  *Antimicrob Resist Infect Control.* 2021;10:52. **DOI 10.1186/s13756-021-00925-8 ·
  PMID 33750479 · PMCID PMC7941135.** — **full text verified.** The proof it works in AMU
  specifically: three-round international Delphi (82 → 77 → 75), 14 candidates → 5-outcome
  COS, then a **second** two-round Delphi (59 → 54) to pick the measurement *instrument*
  for each outcome — separating **what to measure** from **how to measure it**. Threshold:
  *"rating of 7 to 9 by 80% or more of participants and 1 to 3 by 15% or fewer."*
  Rationale: *"Heterogeneity in reported outcomes across trials hindered data synthesis..."*
- **★ Sargeant JM, O'Connor AM, O'Sullivan TL, Ramirez A. "Maximizing value and minimizing
  waste in clinical trials in swine: Selecting outcomes to build an evidence base."**
  *J Swine Health Prod.* 2023;31(1):29–35. **DOI 10.54846/jshap/1300** —
  https://www.aasv.org/shap/issues/v31n1/v31n1p29.html (open access, **full text read**).
  **The stat to build a slide on:**
  > "Veterinary medicine has been slower to adopt core outcome sets; to date, there is a
  > core outcome set published for trials in feline chronic kidney disease and one for
  > therapeutic trials for canine atopic dermatitis."

  **Two core outcome sets in all of veterinary medicine — both companion animal, neither
  food animal — against 410 in human medicine** (their citation, Gargon 2019). They add:
  *"The development of core outcome sets is an area in which the swine industry could
  provide leadership."*

  > ### ⚠️⚠️ CORRECTION — verified 2026-07-16. **DO NOT say "zero for food animals."**
  >
  > **Sargeant 2023 is STALE and the "zero food-animal COS" line is FALSE.** The COMET
  > database was reached and searched directly (the earlier fetch failure was a malformed
  > URL, not blocking). **A core outcome set for bovine respiratory disease is registered
  > and ongoing right now:**
  >
  > - **COMET study 3214** — https://www.comet-initiative.org/Studies/Details/3214
  >   *"Protocol for the development of a core outcome set for studies of bovine
  >   respiratory disease **diagnosis** in **pre-weaned dairy calves**."*
  >   Katheryn Churchill; **David Renaud (PI)** and **Dr. Charlotte Winder**, University of
  >   Guelph. **Ongoing, Jul 2024 – Dec 2026.** Funder: **Dairy Farmers of Canada.**
  >   Methods: scoping review → interviews → two-round Delphi → consensus meeting.
  >   First output already published: *"Evaluating case definitions of respiratory disease
  >   in dairy calves: A scoping review,"* J Dairy Sci, Jan 2025, PII S0022-0302(25)00012-8.
  > - **COMET study 3278** — https://www.comet-initiative.org/Studies/Details/3278
  >   **Neonatal calf diarrhea** COS. Renaud (PI), Luiza Zakia. Ongoing Aug 2024 – Sep 2026.
  >   Dairy Farmers of Canada. Protocol: https://hdl.handle.net/10214/28653
  > - *Swine influenza:* Keay et al., Front Vet Sci 2025 (DOI 10.3389/fvets.2025.1465926,
  >   PMID 40007748) is a **call for** a COS — **not** one in development.
  >
  > **Why Sargeant is stale:** it published in 2023; COMET 3214 registered **July 2024**.
  > Note a Feb 2025 O'Connor paper *also* repeats "only two COS initiatives in veterinary
  > care" — it was **already out of date when published**, so a second secondary source
  > repeating "two" is *not* independent confirmation.
  >
  > **Both claimed completed vet COS verified as real:** feline CKD — Doit, Dean, Duz,
  > Finch, Brennan, *Prev Vet Med* 2021;192:105348, **PMID 34022713**; canine atopic
  > dermatitis (COSCAD'18) — Olivry et al., *BMC Vet Res* 2018;14(1):238, **PMID 30115047**.
  >
  > **THE SAFE LINE (use this):** *"There are only two **completed** core outcome sets in
  > all of veterinary medicine — feline CKD and canine atopic dermatitis. For food animals
  > the first ones are only now underway: Guelph has COS projects in development for BRD
  > **diagnosis** in pre-weaned dairy calves and for neonatal calf diarrhea, both due 2026.
  > **Nothing exists for feedlot BRD treatment outcomes.**"*
  >
  > That last sentence **holds** — 3214 is scoped to *diagnosis* in *dairy calves*, not
  > treatment outcomes in feedlot cattle. And it's the better line anyway: *"the field is
  > just starting this"* is more credible and more interesting than *"the field has never
  > done it,"* and it lets Nora cite the in-development work as **momentum** rather than be
  > corrected by it. **Renaud and Winder are prominent enough that a Guelph-affiliated or
  > FDA attendee may well know about 3214.**
  >
  > **Honest caveat:** COMET is **not exhaustive for veterinary** — neither feline CKD nor
  > canine AD appears in its disease vocabulary at all — and COMET keeps a separate
  > early-stage list that is **not returned by standard search**. So absence from COMET is
  > never evidence of absence. This cuts **against** the strong claim, never for it.

**Honest caveats to voice if this is used:**
- COS standardizes *what to measure*, not *how to summarize it* — complementary to, not a
  fix for, the composite problem.
- COS-STAD's own Delphi invited 1,089 COS users but only **12 patient representatives** —
  the standard demanding patient inclusion was itself set with thin patient
  representation. Don't let producer representation be similarly tokenistic.
- **Delphi manufactures consensus; consensus is not correctness.** VanBuren is the proof:
  an expert-endorsed composite still declared placebo superior while mortality ran 4%
  higher.

**Supporting (verified metadata):** REFLECT statement — Sargeant et al., *J Food Prot.*
2010;73(3):579–603, DOI 10.4315/0362-028x-73.3.579, PMID 20202349 (governs *reporting*,
not outcome definition). COSCAD'18 — Olivry et al., *BMC Vet Res.* 2018;14(1):238,
DOI 10.1186/s12917-018-1569-y, PMID 30115047, PMCID PMC6097451. Feline CKD COS — Doit et
al., *Prev Vet Med.* 2021;192:105348, DOI 10.1016/j.prevetmed.2021.105348 *(verified via
Sargeant's reference list, not independently fetched)*. AVMA call to action — Fajt,
Lehenbauer, Plummer et al., *JAVMA.* 2022;260(8):853–859, DOI 10.2460/javma.21.09.0431,
PMID 35271460 *(metadata only — paywalled, no claim about content)*.

**Verified negative:** No AVMA, AABP, or ACVIM consensus statement defines treatment
success or failure in cattle. The **ACVIM Consensus Statement** (Weese et al., *J Vet
Intern Med* 2015;29(2):487–498; DOI 10.1111/jvim.12562; PMID 25783842; PMCID PMC4895515)
is multi-species and supplies no success/failure definition. ⚠️ *Read via summarizer only;
structural claim is medium-high confidence.*

---

## 4. BRIEFING MATERIAL — other species (NOT for slides)

> Per Nora: this section exists so she is **prepared for what other people might raise**,
> not to generate slide content.

### The one-line answer if asked to generalize

**Outcome measurement across sectors tracks whether a treated individual exists to
follow.** Humans have patients → DOOR. Cattle have identified animals → Success/Relapse/
Sold/Died is constructible. Aquaculture has tanks → one group mortality ratio. Plant
agriculture has orchards → no individual at all, no cure concept. **Her four-way
classification is not a refinement of what other sectors do; it is a category they cannot
reach.**

### ★ The cleanest verified null: there is no veterinary DOOR

PubMed query `"desirability of outcome ranking" AND (veterinary OR canine OR dogs OR
cattle OR equine)` returns **"No results were found"** (verified 2026-07-16). DOOR has been
adapted to epilepsy, obstetrics, aspergillosis, skin/soft-tissue, intra-abdominal, and
bloodstream infection — **not to any animal species.** Independently corroborated by the
swine/poultry agent, which found no DOOR analog in any food-animal species.

⚠️ *Caveat: PubMed only. A DOOR-like scheme could exist under different terminology; Web of
Science / CAB Abstracts not searched.*

### SWINE

- **Glass-Kaastra SK, et al.** *BMC Vet Res.* 2013;9:238. **PMID 24289212 · PMCID
  PMC4220827 · DOI 10.1186/1746-6148-9-238.** — **full text verified.** Practitioner-
  reported efficacy collapsed to a **binary**: *"Treatment failure was deemed to have
  occurred if practitioners recorded a treatment as being not efficacious, or
  'occasionally' efficacious"* — an intermediate state forced into "failure." Result:
  *"In reports indicating antimicrobial use, treatment failure was surprisingly high
  (70%)."* And the denominator problem, verbatim: *"As records were made at the visit
  level, a record could reflect treatment and efficacy at the individual, pen, or herd
  level."* → A 70% failure rate nobody believes, produced by a binary outcome at an
  ambiguous denominator. *(Table 2's 473/676 counts could NOT be confirmed — use the 70%
  sentence only.)*
- **FDA FOI, NADA 141-244, DRAXXIN (tulathromycin)**, approved 2005-05-24 —
  https://animaldrugsatfda.fda.gov/adafda/app/search/public/document/downloadFoi/789
  (**full text verified, p.10**): *"A pig was considered a cure if, on Day 7 after
  treatment, it was alive and had a respiration score ≤ 1, an attitude score of ≤ 1, and a
  rectal temperature of <104 °F."* Results (p.11, Table 2.3): tulathromycin 266 treated,
  7 mortalities, 189 cured, 70.54%; saline 267 treated, 24 mortalities, 124 cured, 46.09%
  (LSM from model, not raw — the FOI says so).
  → FDA concedes success is four-dimensional, then collapses it to one binary at one day:
  a pig that **died** and a pig **alive but still coughing** are both "not cured."
- **Sargeant JM, et al.** "Systematic review of the efficacy of antibiotics for the
  prevention of swine respiratory disease." *Anim Health Res Rev.* 2019;20(2):291–304.
  **DOI 10.1017/S1466252319000185.** ⚠️ **landing page only — paywalled, internal quotes
  UNVERIFIED.** Eligible outcomes were morbidity *"as defined by the authors"* — the
  review surrendered the case definition to each trial.
- **Wayop IYA, et al.** *BMC Vet Res.* 2025;21:101. **PMCID PMC11854134 · DOI
  10.1186/s12917-025-04550-0.** — **full text verified.** Five performance indicators for
  swine *S. suis*: total AMU vs threshold; 1st- vs 2nd/3rd-choice ratio; documented
  justification; susceptibility testing; corticosteroid use. **Every one is process or
  input. None is a therapeutic outcome.** → Europe's most current swine stewardship
  scorecard measures **what the vet did**, never **what happened to the pig**.
- **Nutsch RG, et al.** *Vet Ther.* 2005;6(2):214–24. **PMID 16094568.** — abstract only
  (journal defunct). Cure: saline 46.4%, tulathromycin 71.1%, ceftiofur 63.1%.
  ⚠️ **Close to but NOT identical with the FOI's 70.54/46.09** — different analysis sets.
  **Do not mix the two.**

**Swine gaps:** no 30-day-window event-level model; **relapse/retreatment essentially
unstudied** — a targeted search returned almost exclusively bovine literature. *If a swine
person challenges Nora on relapse, the honest answer is their literature hasn't addressed
it.*

### POULTRY — ⚠️ Bruce & Ken's lane; consistent with the original scope call

- **Sargeant JM, et al.** "Efficacy of antibiotics to control colibacillosis in broiler
  poultry: a systematic review." *Anim Health Res Rev.* 2020;20(2):263–273. **DOI
  10.1017/S1466252319000264.** ⚠️ **landing page only, quotes unverified.** Of 9 controlled
  trials: **FCR** in 7 (25 comparisons); **mortality in 1 trial (2 comparisons)**;
  **condemnations: zero trials**; **total antibiotic use: zero trials.** → In broiler
  colibacillosis the literature overwhelmingly measures **feed conversion** and almost
  never whether the birds **died**.
- **Bueno I, et al.** "Efficacy of Antibiotic and Non-antibiotic Interventions... Necrotic
  Enteritis in Broiler Chickens." *Avian Dis.* 2023;67(1):20–32. **PMID 37140108 · DOI
  10.1637/aviandiseases-D-22-00069.** — abstract verified. 40 studies; 89 outcomes assessed
  for risk of bias — **34 "high," 55 "some concerns," none low.** Antibiotics trended
  better for mortality and jejunal/ileal lesion scores; **non-antibiotics trended better
  for duodenal lesion scores and crypt depth.** → Outcomes point in **opposite directions
  depending on which segment of gut you score.**
- **Van Cuong N, et al.** *Zoonoses Public Health.* 2021;68(5):483–492. **PMCID PMC8573609 ·
  DOI 10.1111/zph.12839.** — **full text verified.** *"the pattern was inconsistent across
  the combinations of antimicrobial classes and clinical signs with **14/29 decreasing and
  11/29 increasing** the per cent weekly mortality."* Also: *"there are little empirical
  data on the overall effects of prophylactic and therapeutic AMU on flock health."*
  ⚠️ Highest duplication risk — well known in poultry AMU circles.

**★ The concession to make, not the point to press:** in poultry an individual-event
outcome model may be **genuinely inapplicable**, not merely absent — birds are
mass-medicated via feed/water and individual events largely aren't recorded. **Conceding
this is both honest and protective of the handoff to Bruce & Ken.**

### COMPANION ANIMAL & EQUINE

- **★ Crosby DE, et al.** "Factors Associated With Survival and Return to Function
  Following Synovial Infections in Horses." *Front Vet Sci.* 2019;6:367. **PMID 31696123 ·
  PMCID PMC6817570 · DOI 10.3389/fvets.2019.00367.** — **full text verified.** One cohort,
  three defensible "success rates": **survival 145/161 = 90.1%; return to function
  79/120 = 65%; racehorses 30/60 = 50%.** *Nothing about the horses changed — only which
  number got reported.* ⚠️ *The authors do not themselves argue survival is inadequate —
  present as inference from their data, not their claim.*
- **Weese JS, et al.** "Development of standard consensus definitions for infectious urinary
  tract disease in dogs and cats, a modified Delphi study." *J Small Anim Pract.* 2026 Apr 7.
  **DOI 10.1111/jsap.70127 · PMID 41944143.** — abstract verified (Wiley 403). Four rounds
  (19/16/90/52 participants), **29 terms** + cut-off values. *"Unclear or variable
  definitions have commonly been present in studies of urinary tract disease in dogs and
  cats, causing confusion and hampering evidence assessment."* → In **2026**,
  companion-animal medicine is still agreeing on *nouns*.
- **Dorsch R, et al.** "Urinary tract infection and subclinical bacteriuria in cats."
  *J Feline Med Surg.* 2019;21(11):1023–1038. **PMID 31601143 · PMCID PMC6826873 · DOI
  10.1177/1098612X19880435.** — **full text verified.** *"the benefit of urine cultures
  during treatment is unclear as **the clinical outcome is of greater importance than the
  culture results per se**."* And: *"In one study of older cats, subclinical bacteriuria
  was not adversely associated with survival despite withholding antimicrobial treatment."*
  → Subclinical bacteriuria is the reductio: a microbiological "failure" who is a clinical
  success, where treating the number actively harms.
- **Loeffler A, et al.** "Antimicrobial use guidelines for canine pyoderma (ISCAID)."
  *Vet Dermatol.* 2025;36(3):234–282. **PMID 40338805 · PMCID PMC12058580 · DOI
  10.1111/vde.13342.** — **full text verified.** *"A major challenge for companion animal
  antimicrobial guidelines is the paucity of objective data..."* One cited study reported
  *"69% versus 79% achieved 'good' or 'complete' response"* — **without defining those
  terms.** → Two numbers compared where neither term has a definition.
- **Harris J, et al.** "Client-reported outcomes measures... dogs' clinical signs and
  quality of life during chemotherapy." *BMC Vet Res.* 2025;21:74. **PMID 39966841 · PMCID
  PMC11834653 · DOI 10.1186/s12917-025-04522-4.** — **full text verified.** *"No CROMs
  adhered to quality standards for the development of questionnaires..."* Recall periods
  ranged from daily to *"up to 5-years."* → The instinct to capture the caretaker's view is
  right; the discipline is missing. *(Oncology, not AMU — the honest bridge is "the
  measurement problem generalizes.")*
- **Weese JS, et al.** ISCAID UTI guidelines. *Vet J.* 2019;247:8–25. **PMID 30971357 · DOI
  10.1016/j.tvjl.2019.02.008.** ⚠️ **The widely-circulated line — microbiological cure
  "desirable but not necessarily achievable or required" — could NOT be verified** (NDSU
  mirror TLS error; ScienceDirect paywalled). **Do not quote until someone opens the PDF.**
  Use Dorsch (verified) for the same concept.

**Equine:** no equine ISCAID equivalent; no consensus guideline defining antimicrobial
treatment outcomes. What exists is retrospective single-hospital case series with
locally-invented, non-comparable definitions. **Report as: no consensus outcome framework
exists.**

**Also verified null:** no companion-animal/equine literature does longitudinal outcome
trending within a practice as a stewardship tool. Veterinary stewardship measurement is
overwhelmingly **use metrics**.

### AQUACULTURE

- **Narbonne JA, et al.** "Antimicrobial Use Surveillance Indicators for Finfish
  Aquaculture Production: A Review." *Front Vet Sci.* 2021;8:595152. **PMID 33778031 ·
  PMCID PMC7991786 · DOI 10.3389/fvets.2021.595152.** — full text. Every indicator is a
  *use* indicator (mg/PCU, mg/APCU, nDDDvet, nDCDvet, nUDDA, Treatment Frequency,
  Treatment Incidence). **The denominator can't even hold:** *"A PCU based on the total
  annual slaughter weight for finfish does not account for existing, live fish in the
  population at a given time or the fish that die."* ⚠️ *Verified the indicator list; did
  NOT confirm the authors explicitly lament the outcome gap — say "outcome is absent from
  the indicator set," not "the authors call out the gap."*
- **Bae JS, et al.** *Antibiotics (Basel).* 2025;14(4):346. **PMCID PMC12024054 · DOI
  10.3390/antibiotics14040346.** — full text. Endpoint = **Relative Percent Survival**, a
  group-level mortality ratio: *"% RPS = [1 − (% test group mortality/% control mortality)]
  × 100."* Amoxicillin at 40 mg/kg: olive flounder 100.0%, Japanese eel 82.2%, rainbow
  trout 75.5%, black rockfish 72.7%, **Israeli carp 33.3% (n.s.)** → same drug, 100% vs
  33% by species: "context changes the answer," arriving as a footnote.
- **Heckman TI, et al.** *J Aquat Anim Health.* 2025. **PMID 40668598 · DOI
  10.1093/jahafs/vsaf008.** — abstract only. Tank-level survival only: florfenicol 100%,
  erythromycin 93%, untreated controls 60% (18°C).

**Verdict:** outcome exists but is **binary and group-level**. No relapse, no chronic, no
"sold," no individual to follow.

### PLANT AGRICULTURE — the strong negative

- **Aćimović SG, et al.** *Front Plant Sci.* 2015;6:16. **DOI 10.3389/fpls.2015.00016.** —
  full text. **Group-mean disease severity percentages; no per-tree success/failure
  classification exists.** Streptomycin: 61% blossom blight control at medium pressure;
  36.5% shoot blight control (2013).
- **Archer L, et al.** *Phytopathology.* 2023. **PMID 36474420 · DOI
  10.1094/PHYTO-09-22-0330-R.** — abstract only. Outcome = **agronomic surrogates**
  (CLas titer, preharvest fruit drop, yield, fruit size, juice quality). The tree is never
  cured — HLB is incurable, the antibiotic is suppressive. *"Results varied due to the
  timing of injection and were not consistent across all three varieties."*
- **★⚠️ *Migrant Clinicians Network v. USEPA*, No. 21-70719 (9th Cir., Dec 13, 2023)** —
  https://cdn.ca9.uscourts.gov/datastore/opinions/2023/12/13/21-70719.pdf (**full 33-pp
  opinion read**).

  **DO NOT USE THE PRESS FRAMING.** CIDRAP/NRDC/Beyond Pesticides report the court found
  evidence streptomycin works against citrus greening "insufficient." **That is wrong.**
  Verbatim:
  > "although **substantial evidence supports the EPA's determination that streptomycin is
  > effective at treating HLB disease and citrus canker**, the EPA failed to provide a
  > sufficient explanation for the registration labels' suggestion that streptomycin can be
  > used to **prevent** either disease."

  The court **upheld** EPA's resistance assessment and its *treatment* efficacy finding.
  Vacatur was driven chiefly by EPA's **conceded ESA non-compliance** plus pollinator and
  *prevention*-claim defects. **Used loosely, a plant pathologist or regulator corrects
  Nora from the floor.**

  **The genuinely usable verified quote** — EPA's own concession, recorded by the court:
  EPA *"agrees that the registrants did not submit any data to support a claim that
  streptomycin prevents infection,"* yet argued it *"committed no error since it did not
  itself consider disease prevention as a benefit."* The court's retort: EPA cited no
  authority *"for the proposition that it could include an unsupported use in a
  registration decision and then police the issue on a back-end review of pesticide
  labels."*

  **Also verified and useful:** to assess resistance risk EPA *"adapted the analytical
  approach from **FDA Guidance for Industry #152**"* — **the plant regulator borrowed the
  animal-drug framework wholesale**, evidence plant ag had no native apparatus.

  **Context (verified, CIDRAP):** ~25 EPA-registered pesticides use streptomycin sulfate,
  20 use oxytetracycline HCl, 8 use calcium oxytetracycline; USGS estimates >125,000 lb of
  the two sprayed on crops in 2018; oxytetracycline expanded to ~700,000 acres of FL/CA
  citrus in 2018. Streptomycin citrus products unlawful to sell/distribute **Feb 5, 2024**
  (existing-stocks order allowed FL use through Aug 31, 2024). Streptomycin has been
  registered on crops since **1955**; oxytetracycline since **1974**.

**Verdict:** **no therapeutic-outcome framework in plant agriculture at all.** No cure, no
relapse, no case definition, no per-plant classification, no denominator of treated
individuals. Efficacy = group-mean disease incidence/severity + yield. The gate is
**EPA/FIFRA — a cost-benefit *pesticide* standard**, not FDA drug effectiveness — so "did
it work" is legally a *benefits* question about crop economics, adjudicated per
registration, **never trended**.

### CROSS-SECTOR / ONE HEALTH

- **★ Quadripartite (WHO/FAO/WOAH/UNEP), "Guidance to facilitate monitoring and evaluation
  for antimicrobial resistance national action plans"** —
  https://www.woah.org/app/uploads/2023/08/guidance-to-facilitate-m-e-for-amr-national-action-plans.pdf
  (**full 26-pp text searched exhaustively**). **`"treatment failure"` — 0 occurrences.
  `"cure"` — 0 occurrences.** The GAP results chain names as an **impact goal**:
  *"Continued ability to treat infectious diseases with effective and safe medicines."*
  Its measured **outcomes** are *"Optimized use of antimicrobials..."* and *"Reduced levels
  and slower development of resistance."* → **Names "continued ability to treat" as the
  goal, then never uses the words "cure" or "treatment failure" in 26 pages.**
- **WHO AWaRe** — GHO indicator https://www.who.int/data/gho/indicator-metadata-registry/imr-details/5765
  and WHO/MHP/HPS/EML/2023.04. Pure consumption accounting: *"relative use is calculated by
  dividing the number of DDD of the category by the total number of DDD and by multiplying
  by 100."* The **2024 UNGA High-Level Meeting on AMR** endorsed **≥70% of global human
  antibiotic consumption be WHO Access antibiotics by 2030** (superseding the 60% GPW13
  target). → The most politically prominent global AMR target is a **ratio of defined daily
  doses** — a country can hit it perfectly while every treated patient fails.
- **FAO RENOFARM** (10-year initiative, launched 2024) —
  https://www.fao.org/antimicrobial-resistance/background/fao-role/renofarm/en/ *(program
  pages, not peer-reviewed)*. **Note the name: "Reduce the Need for Antimicrobials on
  Farms."** Built on the Farm 5G Framework with a ~100 yes/no checklist and a five-star
  rating — a **practice-adoption** score, not a therapeutic outcome. Companion data system
  **InFARM** is for "farm-level AMR and antimicrobial use data."

**THE CROSS-SECTOR ANSWER:** **Outcome is essentially not measured anywhere outside
clinical medicine. Every major cross-sector framework stops at USE and RESISTANCE.** The
structural reason is visible in the documents themselves: **use and resistance are cheap
to measure from things already being counted** — kilograms sold, isolates tested — while
outcome requires an identified individual, a case definition, and follow-up time.
Aquaculture can't keep a denominator; plant agriculture has no individual at all.

---

## 5. Where this changes / stresses the existing deck

| Deck slide | Impact |
|---|---|
| "We're not alone — this is where the science is going" | **Stress.** DOOR/RADAR is the credibility anchor; VanBuren shows RADAR can invert the truth. Consider adding the Evans Reply so the limit is voiced by its inventors. |
| "The correction — and why I like it" | **Reinforced.** The honesty theme now has a second, stronger instance (Evans Reply + VanBuren). |
| "Who decides how bad 'bad' is?" (partial credit) | **Reinforced — add one line.** Finer 2025: physicians and patients disagreed on **7 of 9** vignettes; "Sold" is where vet and owner values diverge. |
| "They named our problem in 2015" (clinician decision) | **Reinforced.** ZACTRAN FOI: `relapse`/`retreat` = 0 occurrences — the regulator never even names the category. |
| "Context changed the answer" (subgroups) | **Reinforced.** Aquaculture RPS 100% vs 33% by species is the same lesson. |
| "Where resistance fits" (Bruce bridge) | **★ Upgrade available.** UK-VARSS concedes in print that a resistant isolate does **not** necessarily correspond to clinical treatment failure — a surveillance program saying resistance ≠ outcome. |
| (new arc, unbuilt) | "Everyone promised the outcome; nobody built the measurement" → FDA/AVMA/AABP all name outcomes → no BRD guidance, no VFD field, no surveillance program → **USDA had it in 2011 and dropped it.** |
| (core-outcome-set slide) | ⚠️ **Must use the corrected wording** — a BRD COS exists (Guelph, COMET 3214). See the CORRECTION box in §3D and trap #8 in §6. |

---

## 6. Traps to avoid on stage

1. **GFI #273 ≠ GFI #209.** The "best clinical outcome" definition is footnote 1 of #273
   FINAL (Feb 2026), **not** #209. Use https://www.fda.gov/media/191092/download.
2. **"Harmonised outcome indicators"** (EU/UK) means mg/kg sales + % susceptible *E.
   coli* — **not** therapeutic outcome. Pre-empt the confusion.
3. **ESVAC is retired** (voluntary, 2009/10–Nov 2023). The platform is EMA's **ASU**; the
   report series is **ESUAvet**. Get the naming right in front of regulators.
4. **The citrus court case did NOT find streptomycin ineffective** — the opposite. Use the
   "no data submitted for the *prevention* claim" angle only.
5. **Don't say "no program anywhere in the world."** Eight were verified. Say "no national
   AMU/AMR monitoring program" and note CIPARS is the softest link.
6. **Don't claim NAHMS 2021 dropped the retreatment-outcome measure** — only Part I was
   checked.
7. **VanBuren is about RADAR, not DOOR.** DOOR alone got it right.
8. **★ NEVER say "zero core outcome sets for food animals" / "our field has never run
   this process."** It is **false** and falsifiable in one search from the floor — a BRD
   COS is registered and ongoing (COMET 3214, **Renaud/Winder at Guelph**, due Dec 2026),
   plus neonatal calf diarrhea (COMET 3278). Say instead: two *completed* vet COS; food
   animal COS *only now underway*; **nothing for feedlot BRD treatment outcomes**. See the
   CORRECTION box in §3D. Guelph/FDA attendees may well know this work.
9. **Conflict flag:** Schrag NFD, Godden SM, Singer RS, et al. *Front Vet Sci.*
   2022;9:1022557 (PMID 36277073) is **Nora's own first-authored paper** — the direct
   ancestor of this model (*"the cow remained in the herd and had no further TE recorded
   within 30 days"*). Cite as ancestry, **not** as independent third-party corroboration.

---

## 7. ⚠️ OPEN GAPS — close before the podium

1. ~~**★ Does a veterinary core outcome set already exist for BRD?**~~ **✅ CLOSED
   2026-07-16 — and the answer was YES, so the claim in §3D was FALSE.** A BRD core
   outcome set **is registered and ongoing** (COMET 3214, Guelph — Renaud/Winder, due
   Dec 2026), plus one for neonatal calf diarrhea (COMET 3278). **See the boxed
   CORRECTION in §3D for the safe wording — do not say "zero for food animals" or "our
   field has never done this."** This was exactly the gap that would have embarrassed
   the line from the podium.
2. **CIPARS** — canada.ca blocked every fetch. Conclusion rests on peer-reviewed methods
   papers, not the program's own methods chapter. Verify or soften.
3. **ISCAID UTI quote** (microbiological cure "desirable but not necessarily achievable or
   required") — unverified; someone must open the PDF. Dorsch 2019 is the verified
   substitute.
4. **NAHMS 2021** — is there a health report with a retreatment-outcome table?
5. **Paywalled, do not quote verbatim:** Sargeant swine/poultry systematic reviews
   (Cambridge), Nutsch 2005 (defunct journal), Ajufo win-ratio full text, Phillips 2016
   full text (PMID unconfirmed).
6. **Explicitly NOT verified — do not cite:** *"Methodologies and standards for monitoring
   AMU/AMR in shrimp aquaculture"* (*Aquaculture* 2023, PII S0044848623009900 — 403, no
   DOI/PMID recovered); Thornber et al. 2020 *Rev Aquac* DOI 10.1111/raq.12367 (Wiley 403,
   **no content read**); a search-engine claim that phage therapy raised *P. monodon*
   survival "from 17 to 86%" (**underlying paper never reached**).

---

## 8. Method note

Five parallel research agents (swine+poultry; companion+equine; aquaculture+plant;
human-beyond-DOOR; regulatory/consensus), plus a sixth on international AMU monitoring.
Agents were instructed to demand persistent identifiers, distinguish full-text from
abstract verification, refuse to fabricate, and report negative findings.

**Important methodological finding, worth remembering for future searches:** `WebFetch`'s
PDF extraction repeatedly failed and returned *"no evidence of X"* for documents it never
actually read — a **false negative that looks like a finding**. fda.gov, canada.ca, Wiley,
Cambridge, and AVMA all block or degrade fetches. The regulatory findings above were
produced by downloading PDFs with `curl` and extracting locally with `pdftotext`/`pypdf`,
then keyword-scanning the extracted text directly. **Term counts cited in §3C are
exhaustive scans of locally extracted full text, not sampling.**
