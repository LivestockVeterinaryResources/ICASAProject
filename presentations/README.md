# Presentations — "An Overview of Outcomes"

Talk by **Nora Schrag** (Livestock Veterinary Resources) for the *Antimicrobial Use
Data Collection* meeting, **July 17, 2026**, Roseville MN. Nora's slot: 11:00 AM
"Outcomes overview" — opens the outcomes session, follows Mike Apley's prelim
("Monitoring our way to stewardship?"), hands to Bruce Stewart-Brown & Ken Opengart
(poultry outcomes).

> ⚠️ **This repo is PUBLIC.** The `notes/` folder and the source decks here
> (including Mike Apley's keynote `.pptx` at the repo root) are world-readable and
> permanent in git history. This was pushed as a temporary convenience and **should
> be cleaned up / moved private.** See the top of `.claude/worklog.md`.

## Files

| File | What it is |
|------|-----------|
| `outcomes-overview.qmd` | **The slide source** — edit this |
| `outcomes-overview.html` | Rendered self-contained reveal.js deck (generated) |
| `theme.scss` | ICASA color/typography theme for the deck |
| `figs/` | Slide-native charts + app screenshots |
| `make_figures.py` | Python script that regenerates the three data charts |
| `_quarto.yml` | Makes this a self-contained sub-project (keeps the deck out of the live website build) |
| `notes/` | All research & planning documentation (see `notes/README.md`) |

A copy of the rendered deck also lives at the repo root as
`Schrag ICASA Outcomes 7-17-2026.html`, next to `Apley ICASA 4-2-2026.pptx`.

## Rebuild the deck

**RStudio** (bundles Quarto): open `outcomes-overview.qmd` → click **Render**
(`Ctrl+Shift+K`).

**Command line:**
```
quarto render presentations/outcomes-overview.qmd
```
Then, to refresh the root copy:
```
copy presentations\outcomes-overview.html "Schrag ICASA Outcomes 7-17-2026.html"
```

## Rebuild the figures (only if changing chart data)

Needs Python 3.12 with `matplotlib` + `numpy` (installed on Nora's machine):
```
python presentations/make_figures.py
```
Outputs PNGs into `figs/`. Then re-render the deck.

## Speaker notes

Every slide has a `::: notes ... :::` block in the `.qmd`. In the browser, press
**`S`** to open the presenter view (slide + next slide + notes + timer).

## Gotchas

- **Raw HTML that needs to render** (multi-`<div>` blocks) must be wrapped in a
  ```` ```{=html} ```` raw block, or Quarto escapes the tags to literal text
  (this bit slide 11 once). Inline `<svg>` blocks are fine as-is.
- The deck is **excluded from the published website** two ways: `!presentations/`
  in the root `_quarto.yml` render list, and this folder's own `_quarto.yml`.
- `embed-resources: true` makes the `.html` fully self-contained (works offline,
  no dependency on `figs/`).

## Key sources (fully verified)

- **Schrag et al. 2022**, *Front Vet Sci* — benchmarks in disease + outcome context
  (the centerpiece). DOI 10.3389/fvets.2022.1022557
- **Apley et al. 2023** — multiple-metrics feedyard paper. DOI 10.3389/fvets.2022.1056476
- **"Moving Beyond Mortality" 2024**, *Clin Infect Dis* — DOOR endpoint (free:
  PMC10874265). First proposed by **Evans et al. 2015** (CID; 2023 CI correction).
- Full literature map in `notes/litsearch-treatment-outcomes.md`.
