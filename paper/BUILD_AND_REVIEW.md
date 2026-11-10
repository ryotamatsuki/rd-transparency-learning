# Build and review instructions

Paper source: `main.tex`. Bibliography: `references.bib`. The manuscript is a **pre-certification v0.1 working draft**.

Local build from the `paper/` directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

If `latexmk` does not automatically process BibTeX, run `pdflatex main; bibtex main; pdflatex main; pdflatex main` and check that citations and cross-references resolve. The repository GitHub Actions workflow `build-paper.yml` compiles the same files and uploads PDF plus LaTeX log.

The output PDF is **for review only**. Independent proof and novelty audit, formal-verification applicability, author contribution verification, live journal compliance and final figure/table inspection are not complete. See `../docs/WORKFLOW_STATUS_2026-11-10.md`.
