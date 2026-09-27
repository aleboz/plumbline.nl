# plumbline.nl

Static website for Plumbline, hosted on GitHub Pages.

- Served from the `main` branch, repository root. `CNAME` binds the site to `plumbline.nl`; do not delete it.
- `.nojekyll` disables Jekyll processing, so files are served as-is.

## Editing the copy

The four language pages (`/`, `/nl/`, `/it/`, `/zh/`) are generated from one template:

- `tools/template.html` — layout, wordmark, analytics tag, consent notice
- `tools/build.py` — all text per language, plus the sitemap

Edit the text in `tools/build.py` (or the layout in the template), then run

    python3 tools/build.py

and commit the regenerated `index.html` files and `sitemap.xml`. Styles live in `style.css`.
