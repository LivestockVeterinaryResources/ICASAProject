# ICASAProject — worklog

Newest entry on top. Dates are absolute.

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
