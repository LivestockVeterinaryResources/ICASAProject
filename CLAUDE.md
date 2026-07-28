# ICASAProject

Public **Quarto website** for the ICASA beef-feedlot antimicrobial-use (AMU)
project. This repo is the **canonical, live front page** of the project.

- Built with Quarto (`type: website`, `output-dir: docs`).
- Published via **GitHub Pages from `/docs` on `main`**:
  https://livestockveterinaryresources.github.io/ICASAProject/
- Remote: `github.com/LivestockVeterinaryResources/ICASAProject`

## How it works

- Source pages are the `.qmd` files at the repo root (`index.qmd`, `About.qmd`,
  `Methods.qmd`); site config is `_quarto.yml`.
- Build with `quarto render` (Quarto 1.8.26). The pages are plain markdown with
  **no R code chunks**, so no R/Rscript is needed to render.
- `quarto render` writes into `docs/`; `docs/` is committed directly and is what
  GitHub Pages serves. After rendering, commit `docs/` and push to `main`.
- `_quarto.yml` `render:` is limited to `*.qmd` so context files like this one and
  `README.md` are **not** turned into published pages.

## Key facts & relationships

- **The data pipeline is not in this repo.** Numbers originate in the private
  `ICASA` repo (raw `DataOriginal/` + Steps 1–5, `MasterDataProcessing.R`), are
  anonymized into `ICASA-anonymous` (`MasterDataProcessing_Anonymous.R`), which
  builds and deploys three Shiny apps to **shinyapps.io, account `lvr-explore`**.
- Homepage (`index.qmd`) links its three sections to those live apps — all three
  verified live 2026-07-15:
  - Antimicrobial Use Metrics → `ICASA_FeedlotMetrics`
  - Therapeutic Outcomes → `ICASA_Disease`
  - Intervention Economics → `ICASA_Econ`
- **Which source file backs each live app** (verified 2026-07-20 by diffing the
  deployed bundles against `ICASA-anonymous`; those folders hold many
  near-identical scratch copies, so do not guess):
  - `ICASA_FeedlotMetrics` → `ShinyMetrics_Anonymous/app_metrics.R`
  - `ICASA_Disease` → `shinyMorbidityParameters/`**`app7.R`** (*not* `app3.R` —
    `app3.R` went to the retired `ICASAMorbidityParameters` app; the data-flow
    map said `app3.R` until it was corrected on 2026-07-20)
  - Note each app also carries a **commented-out "for test" block** with
    repo-root paths. When reading an app to find out what it loads, take the
    *uncommented* block — the map got `deads_all.rds` wrong by reading the other
    one (fixed 2026-07-28).
  - `ICASA_Econ` → `ShinyExportsPredict/app.R`
- `deployed_apps/` (git-ignored, ~343 MB) is a **local read-only reference** copy
  of the deployed bundles, downloaded from shinyapps.io to verify the above. It
  is the **old, pre-theming** code — never edit it or preview apps from it, and
  never commit it (it holds .rds files over GitHub's 100 MB limit).
- **Stale siblings — do not edit for the live site:** `ICASA_Website` (local, no
  git — a dead scratch copy) and `ICASAFeedlotAMUReports` (earlier website draft).
  `ICASA_ShinyApps` is an empty app scaffold (in progress).
- The navbar GitHub icon points at `github.com/damrine/ICASA-anonymous`.

## Data flow map

`dataflow.html` (source at the repo root, copied to `docs/` on render) is a
standalone visual map of the whole pipeline, linked from the navbar as
**Data Flow**. It is a self-contained **inline SVG** (no JS library) and does
**not** pick up the Quarto theme — it carries its own copy of the palette, so a
theme change here means editing that file too.

**Verified against the ICASA-anonymous source end to end on 2026-07-28** by
reading every `read_rds`/`write_rds` call rather than trusting documentation.
What that pass changed, and what it means for keeping the map honest:

- The map now shows **`DataStep2_Anonymous/`** as its own layer. That folder is
  the anonymized handoff; the anonymous scripts *consume* it. The old
  single-hop drawing implied `Step3_Granular_003_anonymous.Rmd` did the
  anonymizing, which it does not.
- **Red dashed arrows** mark inputs that no script places — `deads_all.rds`,
  the Econ `lots_with_dof_morb_mort_rail.rds` copy, `dashboard_payload.rds`,
  `get_expected_doses.csv`, and the `df_wrangle_lot_filtered_with_wt_out.rds`
  name drift. Solid copper means a script genuinely writes it. Keep that
  distinction if you extend the map — a solid arrow is a promise.
- **`Amrine/Predict V3.Rmd`** is drawn as an off-pipeline box because it writes
  the Econ app's `dashboard_payload.rds` and the master script never calls it.
- **`CreateFilesForShinyOutcomesYardYearWt_notLot.R`** is marked ✕: it is
  `source()`d but all four of its `write_rds()` calls are commented out.

## Site theme — slate + copper

`styles.scss` + `theme: [flatly, styles.scss]` in `_quarto.yml`. It is a **port
of `ICASA-anonymous/icasa_theme.R`**, which is the single source of truth for the
three Shiny apps. Palette hexes are copied verbatim from that file: slate
`#34495E` (primary/navbar), copper `#C0693B` (accent/links), green `#2F7D5B`,
teal `#3E6B75`, ground `#EEF1F4`, border `#D9E0E8`. **If the apps' palette
changes, change it here too** — nothing enforces the link.

Three things that will bite whoever touches this next:

- **`linkcolor:` in `_quarto.yml` beats the theme.** The site carried
  `linkcolor: "purple"`, which emits a hard link rule; no amount of `$link-color`
  in the SCSS would have won. It was removed — don't reintroduce it.
- **Quarto's navbar is driven by `$navbar-bg` / `$navbar-fg` / `$navbar-hl`,
  not `$primary`.** Setting `$primary` alone leaves the navbar untouched.
- **Flatly points several things at `$success` (green).** Two overrides carried
  across from `icasa_theme.R`: the `pagination-*` Sass variables (Flatly sets
  `$pagination-bg: $success`, so *every* page button is a solid green block, not
  just the active one — CSS on `.page-item.active` cannot reach it), and an
  `!important` override for `.bg-primary .navbar-nav .nav-link.active`.

Base is **flatly**, chosen because it is the same Bootswatch base the apps build
on; the font is therefore Flatly's Lato, with `$font-size-root` held at 17px so
switching off the old `pulse` theme did not reflow the pages.

## Decisions & rationale

- **Data-flow map is inline SVG, not Mermaid.** The first version used a Mermaid
  `<pre class="mermaid">` block loaded from a CDN. The Mermaid v11 CDN build is an
  ES module and never attaches to `window` via a classic `<script>` tag, so on
  GitHub Pages the diagram rendered as raw text. Hand-authored inline SVG has no
  external dependency and renders identically everywhere.
- **`dataflow.html` is registered as a Quarto `resource`** (in `_quarto.yml`) and
  kept as a source copy at the repo root, so `quarto render` copies it into
  `docs/` on every build instead of it drifting or getting dropped.
- **Restricted `render:` to `*.qmd`** so adding `CLAUDE.md` / worklog files
  couldn't leak into the published site.

## Status / open items

- Site is live and all three app links work.
- **Theme switched to slate + copper 2026-07-28** (was `pulse` purple) and the
  data-flow map corrected against the pipeline source. Both pushed to `main`
  and verified live: the served CSS has `.navbar{background-color:#34495e}` and
  `--bs-link-color:#C0693B`. Pages picked it up ~45s after the push.
- Two findings from the map pass belong to `ICASA-anonymous`, not here, and are
  logged in that repo's CLAUDE.md: `dashboard_payload.rds` is written outside the
  master pipeline, and `CreateFilesForShinyOutcomesYardYearWt_notLot.R` is
  `source()`d but writes nothing.
- Optional, not yet done: retire the two stale website repos; tidy stale deploy
  comments (`ICASAMorbidityParameters`, `ICASA_AMUMetrics`) in
  `ICASA-anonymous/MasterDataProcessing_Anonymous.R`.
- Planned next: a user-guide document walking people through how to use the
  website and its three apps (see `.claude/worklog.md` → Next session).
