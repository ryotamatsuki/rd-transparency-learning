# Canonical workflow status — manuscript drafting session, 2026-11-10

**Authority:** [ryotamatsuki/research-paper-workflow](https://github.com/ryotamatsuki/research-paper-workflow) current `main`, **v2.9** (`GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → stage templates and figure/exposition checklists).

**Project:** `rd-transparency-learning`. **Deliverable:** `paper/main.tex`, a **pre-certification working manuscript**, not an accepted Stage-10/Stage-13 or submission-ready paper. There has been no scientific model change in this drafting pass.

## Actual evidence status vs workflow stages

| Stage | State | Evidence | Gate limitation |
|---|---|---|---|
| 0–3 candidate, sources, novelty pre-screen | RETROSPECTIVE / INCOMPLETE | research_history, related_literature_master, novelty_matrix | No fully documented source-exhaustive novelty kill or canonical parent mapping |
| 4 model derivation | ANALYTICAL CANDIDATE | docs/model.md; code/finite_cost_proof.py; appendices in paper/main.tex | Need clean-room, off-path/global domain proof |
| 4A independent adversarial math | **UNRESOLVED — NOT PASSED** | Fresh independent algebraic price FOCs and welfare derivatives; script reproduction | Independent global candidate-deviation and alternative-equilibrium audit not completed |
| 5 mechanism hardening | PARTIAL | experience-feedback diagnostic; fixed-s,b welfare counterfactual | Formal diagnostic proof/full alternative mechanism assessment open |
| 6 novelty re-kill | **UNRESOLVED — NOT PASSED** | 24-paper master, Section 7.3 Baik & Kim crosswalk | Latest Kim & Poggi revised full text and parent-theorem absorption need review |
| 7 welfare | PARTIAL | model surplus formula, benchmark and `W=CS+profits` identity | Welfare selection under alternative equilibria unresolved |
| 7.5 / 7.5A contribution/quantifier/formal | **UNRESOLVED — NOT PASSED** | high-cost sufficient conditions and exact-certificate code | Formal verification applicability decision and proof-assistant mapping missing; portability audit not done |
| 8 theory freeze | **NOT AUTHORIZED** | none | Stage 4A/6/7.5A prerequisites open |
| 9 repository setup | DONE (limited) | code, bibliography, README, CI | Current public repository; author disclosure controls to check |
| 10 writing architecture & drafting | WORKING DRAFT ONLY | paper/main.tex; docs/EXPOSITION_ARCHITECTURE_2026-11-10.md | Not an official Stage-10 GO because upstream gates open |
| 11 hostile referee | NOT STARTED | none | Fresh audit to follow upstream certification |
| 12 journal positioning | PRELIMINARY ONLY | docs/roadmap.md | No broad candidate universe or current journal requirements ledger |
| 13 integration | NOT FORMALLY PASSED | single internally consistent draft | Requires certified inputs and real reviewer attack |
| 14/15 submission QA / freeze | NOT STARTED | none | PDF/rules/AI disclosure/author sign-off outstanding |

## Mathematical checks performed in this session (do not inflate)

- Re-derived dynamic period-1 and static period-2 price FOCs from primitive demand and continuation payoff using an independent SymPy scratch path, obtaining the stored rational D1 equation.
- Independently differentiated public continuation payoff and A price with respect to lambda at zero; exact expressions match paper/main.tex and docs/propositions.md.
- Independently derived W_lambda, baseline W_s and W_b, u_A' and u_B' in SymPy; matched the general expansion.
- Re-ran the pre-existing certificate code: all scripted rational Bernstein checks printed success and the finite-cost numerical benchmark matched.
- Independently solved the fixed-(s,b) hidden-learning counterfactual at k_lambda=0.3: lambda about 0.2185406068, welfare about -0.9295847447.
- Independent direct-payoff *numerical* solver: optimized A's and B's Stage-0 investment against the other candidate action over the full [0,0.5] box, and B's hidden Stage-1 investment with A's current price fixed over [0,1]. At k_lambda=0.3, all optimization improvements were within numerical precision (~1e-16). Also sampled 101 off-path quality gaps and found interior learning and positive prices. Evidence: `code/independent_payoff_audit.py`; this complements but does not replace the exact algebraic certificates.
- **Not done:** independent global continuation solver, comprehensive boundary/alternative equilibrium search, Lean/other formal proof, theorem priority/full-text mapping, author verification.

## Editorial and reproducibility checks

- Cited keys: 14 unique, all available in 24-key references.bib.
- All 52 manuscript labels referenced resolve in the source text at static inspection; environment begin/end pairs balanced.
- Main text: six sections, main mathematical family 1 lemma + 2 propositions + 1 theorem, a single timeline diagram, a single numerical equilibrium table, technical appendices. No decorative exhibit.
- Manuscript uses explicit working-draft disclaimer. No unsupported claim of voluntary disclosure equilibrium, universal welfare effect, persistent technological turnover, or fixed-budget R&D allocation.
- The desired PDF build is triggered via `.github/workflows/build-paper.yml`. GitHub build status must be reported separately; a file written to GitHub is not a PDF QA PASS.

## Mandatory next gates

1. Stage 4A: clean-room finite-deviation audit, separate multiplicity search, boundary/corners, off-path histories, proof-readable certificates.
2. Stage 6: theorem-to-theorem parent-class matching, especially Baik & Kim 2020 Section 7.3, Cabral–Riordan 1994, Kim–Poggi September 2026 revision, Cohen–Levinthal 1994.
3. Stage 7.5A: generality/portability and formal-verification applicability; do not mark `N/A` without a reason.
4. Stage 8: author judgment record, theory freeze **only after** preceding gates PASS.
5. Stage 10–13: restructure manuscript if audits alter theorem scope, then independent reader/referee and exposition compression audit.
6. Stage 12–15: journal requirements and AI-use declaration audited against actual chosen venue, final PDF and source identity, author sign-off.

## AI provenance, not authorship verification

AI assistance: OpenAI GPT-6, 2026-11-10, drafting, algebraic scratch checks, literature organization, LaTeX source and build workflow. Verification actors: `AI` and `COMPUTATION`. **No `AUTHOR` or `EXTERNAL HUMAN` verification is claimed** by these results. The author remains responsible for scientific judgment and all assertions in a future submitted manuscript.
