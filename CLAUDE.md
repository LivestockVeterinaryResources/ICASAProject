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
- **Stale siblings — do not edit for the live site:** `ICASA_Website` (local, no
  git — a dead scratch copy) and `ICASAFeedlotAMUReports` (earlier website draft).
  `ICASA_ShinyApps` is an empty app scaffold (in progress).
- The navbar GitHub icon points at `github.com/damrine/ICASA-anonymous`.

## Data flow map

`docs/dataflow.html` is a standalone visual map of the whole pipeline, linked from
the navbar as **Data Flow**. It is a self-contained **inline SVG** (no JS library).

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
- Optional, not yet done: retire the two stale website repos; tidy stale deploy
  comments (`ICASAMorbidityParameters`, `ICASA_AMUMetrics`) in
  `ICASA-anonymous/MasterDataProcessing_Anonymous.R`.
- Planned next: a user-guide document walking people through how to use the
  website and its three apps (see `.claude/worklog.md` → Next session).
