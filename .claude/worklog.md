# ICASAProject — worklog

Newest entry on top. Dates are absolute.

> ⚠️ **PUBLIC-REPO CLEANUP OWED (set 2026-07-16).** The whole `presentations/`
> tree (incl. candid strategy notes and a text dump of Mike Apley's unpublished
> keynote), plus `Apley ICASA 4-2-2026.pptx` and `MindwalkJul2026.pptx` at the
> root, were pushed to this **public** repo as a temporary convenience. Nora
> asked to be reminded every 12h that this is public and needs cleaning up —
> move the sensitive items to a private location and `git rm` them (history
> rewrite needed to fully purge). Until then, treat everything here as world-readable.

## 2026-07-16 — Built "An Overview of Outcomes" talk deck

**Done:**
- Created `presentations/outcomes-overview.qmd` — a 14-slide Quarto **reveal.js**
  deck for Nora's 11:00 AM "Outcomes overview" at the July 17 2026 AMU meeting.
  Narrative journey: respect for effective antimicrobials → measure use (regimens
  in disease context) → *did the drug work?* (therapeutic outcomes) → a single
  number lies (Success/Relapse/Sold/Died decomposition) → trend within farm
  context → drive appropriate use (welfare anchor) → where resistance/ARGs fit
  (Bruce bridge) → hand to Bruce & Ken.
- Slide-native figures via `make_figures.py` (matplotlib); ICASA `theme.scss`;
  inline SVG diagrams; reused the `dataflow.html` map for the pipeline/3-apps slide.
- Excluded the deck from the live site build (`!presentations/` + nested
  `_quarto.yml`); self-contained HTML also copied to repo root next to Apley's.
- Verified the DOOR/RADAR sourcing: "Moving Beyond Mortality" 2024 (CID, free on
  PMC10874265) is the fully-read anchor; Evans 2015 is origin (2023 CI correction).
- Consolidated all research/planning into `presentations/notes/` (was in scratchpad).
- Installed Python 3.12 + matplotlib/pandas/python-pptx/pdfplumber/markitdown;
  `python` works in new shells (user PATH fixed ahead of the Store stub).

**Why:** Nora presents the outcomes overview; the deck operationalizes her 2022
benchmarks paper and positions therapeutic outcomes as the decision/welfare layer
above resistance measurement, meshing with Apley's prelim.

**Gotchas:**
- Edit `presentations/outcomes-overview.qmd`, render (RStudio or `quarto render`),
  then re-copy the HTML to the root `Schrag ICASA Outcomes 7-17-2026.html`.
- Multi-`<div>` raw HTML must be wrapped in ```` ```{=html} ```` blocks or Quarto
  escapes the tags (bit slide 11 once).
- Quarto bundled with RStudio: `C:\Program Files\RStudio\resources\app\bin\quarto\bin\quarto.exe`.

**Next:** Clean up the public-repo exposure (see warning above). Optionally polish
figures with real ICASA data; refresh app screenshots from the live Shiny apps.


## 2026-07-15 — Data-flow map + navbar link; established repo context

**Done:**
- Traced the whole project data flow (backwards from the website) across the six
  `C:\GIT\ICASA*` repos and confirmed **ICASAProject** is the live site; the
  `index.qmd` links to `ICASA_FeedlotMetrics`, `ICASA_Disease`, `ICASA_Econ` were
  all verified live on shinyapps.io.
- Added `docs/dataflow.html`, a standalone visual data-flow map, and linked it in
  the navbar as **Data Flow** (`_quarto.yml`). Registered it as a Quarto resource
  and kept a source copy at the repo root.
- Rebuilt the map as inline SVG after the Mermaid version failed on GitHub Pages;
  later removed the "Project folders outside the live pipeline" section per request.
- Added `CLAUDE.md` (durable repo context) and this worklog; limited Quarto
  `render:` to `*.qmd` so these don't publish.

**Why:**
- The project had three near-identical website copies; only this one has real app
  links, so it needed to be marked canonical to stop edits landing in dead copies.
- Mermaid-via-CDN broke because the v11 build is an ES module (a classic
  `<script>` tag never defines `window.mermaid`); inline SVG removes the whole
  external-dependency failure mode.

**Gotchas:**
- Edit the **source** (`index.qmd`, `_quarto.yml`, root `dataflow.html`), then run
  `quarto render`, then commit `docs/` and push. GitHub Pages serves `/docs`.
- `ICASA_Website` (no git) and `ICASAFeedlotAMUReports` are stale — don't edit them
  expecting the live site to change.

**Next:** Create a user-guide document that walks people through how to use the
website and its three apps. See the resume prompt under **Next session** below.

## Next session — website how-to guide

```text
Resume work on ICASAProject (C:\GIT\ICASAProject).

Context: read CLAUDE.md and .claude/worklog.md in that repo first. In short: this
is the live Quarto site (published to GitHub Pages from /docs on main) for the
ICASA beef-feedlot antimicrobial-use project. Its home page links to three live
Shiny apps on shinyapps.io/lvr-explore: ICASA_FeedlotMetrics (AMU metrics),
ICASA_Disease (therapeutic/disease outcomes), and ICASA_Econ (intervention
economics). A visual data-flow map lives at docs/dataflow.html (navbar: Data Flow).

Task for this session: create a user-guide document that walks a non-technical
reader through how to use the website — what each of the three apps is for, how to
read and interact with them, and how to interpret the key outputs. Decide with me
whether it should be a new Quarto page in the site navbar (e.g. Guide.qmd) or a
standalone page like the data-flow map, then draft it. Open each app first to
describe what's actually there; don't guess at controls or outputs.

Constraints / things to know:
- Build with `quarto render` (Quarto 1.8.26; pages are plain markdown, no R needed),
  then commit docs/ and push to main. Pages serves /docs; hard-refresh to see changes.
- If adding a navbar page, add it to _quarto.yml right nav and re-render so it bakes
  into every page.
- The three app URLs are https://lvr-explore.shinyapps.io/<slug>/ for the slugs above.
```
