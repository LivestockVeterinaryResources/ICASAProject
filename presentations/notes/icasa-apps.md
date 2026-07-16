# ICASA pipeline + 3 Shiny apps — for the data-flow & app-overview slides
Source: dataflow.html (repo), index.qmd, and app screenshots extracted from Apley deck (S22 = FeedlotMetrics, S23 = Disease).

## Pipeline (copper-arrow flow)
raw feedyard files (`DataOriginal/`, `SampleData/`)
→ **ICASA** source repo (Steps 1–5, `MasterDataProcessing.R`; incl. `Step5_outcomes.Rmd`)
→ **[anonymized handoff — intentional break]**
→ **ICASA-anonymous** engine (`MasterDataProcessing_Anonymous.R`, `CreateFilesForShinyOutcomes*`)
→ 3 Shiny app projects → 3 shinyapps.io apps (account `lvr-explore`) → **ICASAProject** website (`index.qmd` links all three).
Reusable visual: the inline SVG in `docs/dataflow.html`.

## The three apps (and how they fit the outcomes story)
1. **ICASA_FeedlotMetrics** (`ShinyMetrics_Anonymous` / `app_metrics.R`) — **THE USE LAYER.**
   - Screenshot (Apley S22): "Feedlot Antimicrobial Use Metrics"; Select Metric (e.g., metric_cdoa_per_hd_in), Treatment Category (Feed), Active Substance; tabs **Data Context / AMU Metrics / Regimen Descriptions**; stacked bars by yard×year; downloadable table.
   - Reads: df_wrangle_lot..., deno_yardyear_long, regimens_yardyear_long, master_regimens_long, get_expected_doses.
   - Role in talk: this is where "regimens as the metric" lives (Mike's territory). 8 feedyards.
2. **ICASA_Disease** (`shinyMorbidityParameters` / `app3.R`) — **THE OUTCOME LAYER ← Nora's star.**
   - Screenshot (Apley S23): "Feedlot Disease Descriptions"; Choose Yard (1001–1009), Disease (Respiratory…), Weight Class; **"Days between Therapeutic Events" = 7**; **"Days between TE and Outcome Evaluation" = 30**; tabs **Morbidity / Days to Next TE / Outcomes / Scatter / DataTable / SummaryTable**.
   - Reads: lots_for_outcomes, tx3_for_shiny, deads_all.
   - Role: operationalizes P13 exactly — 7-day TE grouping + 30-day outcome window → Success/Relapse/Sold/Died, trended by yard/disease/weight. This is the live embodiment of the whole talk.
3. **ICASA_Econ** (`ShinyExportsPredict` / `app.R`) — **THE DECISION/ECONOMICS LAYER.**
   - Reads: lots_with_dof_morb_mort_rail, dashboard_payload. (dof = days on feed; morb/mort/rail = morbidity/mortality/railer/chronic.)
   - Role: intervention economics given early disease info — closes the loop from outcome → action/value.

## One-line framing for the app-overview slide
**Use (FeedlotMetrics) → Outcome (Disease) → Value of intervention (Econ).** Nora's talk lives in the middle app and gives the other two their meaning: you measure use to interpret outcomes, and you value interventions by their outcomes.
