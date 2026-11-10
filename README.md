# R&D Transparency, Market-Based Learning, and the Direction of Innovation

Two-period Hotelling–Bertrand model of an incumbent (A) and an entrant (B). The entrant chooses **immediate quality R&D** and **future learning-capability R&D**; learning converts first-period market share into second-period quality. We compare observability (P) versus concealment (H) of the entrant's learning investment.

> **Research status — 2026-11-10:** working research project; not a published paper. Algebraic sign certificates and a benchmark replication are available. Journal-grade equilibrium proof, robustness, and novelty assessment still require independent scrutiny.

## Research question / 研究課題

Under which conditions does disclosure redirect the entrant's investment away from future learning toward immediately effective quality, raise both firms' profits, yet reduce subsequent technological performance and social welfare? Is this more than the combination of familiar R&D-disclosure and learning-by-doing mechanisms?

**Proposed contribution (not a priority claim):** the incumbent's ability to respond to *observed learning-capability investment* through first-period pricing changes the entrant's composition of R&D, while endogenous quality-investment adjustments can amplify a disclosure-induced welfare loss.

## Model, at a glance

- Locations: incumbent at 0 and entrant at 1 on a unit Hotelling line; full market coverage and linear transport disutility (t).
- Investments: (s) = A's persistent quality improvement; (b) = B's immediately effective quality improvement (persists into period 2); (λ) = B's learning capability.
- Quality gap: (d=d_0+s-b). Period-2 entrant-relative quality: (q_2=-d+λ D_1), where (D_1) is B's period-1 demand.
- Costs: (k_s s^2/2,;k_b b^2/2,;k_λ λ^2/2). Period-2 profit discounted by (δ).
- Timing: simultaneous (s,b) (observed); B chooses (λ) (observed by A only in P); simultaneous period-1 prices; experience/quality update; simultaneous period-2 prices.
- **Concealment is not an unanticipated equilibrium level:** A correctly anticipates B's equilibrium (λ), but cannot condition prices on an unobserved unilateral deviation.

## Current results

For normalized parameters (t=δ=d_0=1,;k_s=k_b=4) and strategy sets (s,bin[0,1/2],;λin[0,1]), the existing computer-assisted proof proposes a sufficient condition
[
k_λ > rac{4343}{32448} approx 0.133845
]
for a unique equilibrium in each information regime and, along the certified branch,
[
λ^H>λ^P=0,quad b^H<b^P,quad s^H>s^P,quad
Π_A^P>Π_A^H,quad Π_B^P>Π_B^H,quad W^H>W^P.
]
A broader algebraic *equilibrium-branch* sign check covers (k_λge 0.1), **without** asserting global equilibrium uniqueness throughout that larger interval.

At benchmark (k_λ=0.3), the hidden equilibrium has (sapprox0.252492,;bapprox0.096746,;λapprox0.211102); the public equilibrium has (s=11/48,;b=5/48,;λ=0). See [results/benchmark.md](results/benchmark.md).

**Critical novelty caveat:** disclosure increasing firm profits and reducing social welfare, and disclosure redirecting innovation toward the short term, are **already known separately** in the literature. The contribution must be established at the level of the specific *price-defense → customer experience → learning capability → R&D mix* mechanism. [literature/novelty_matrix.md](literature/novelty_matrix.md) is an evolving comparison, not proof of global novelty.

## Repository map

- [docs/model.md](docs/model.md): definitions, timeline, price subgames, information structure.
- [docs/propositions.md](docs/propositions.md): claim-by-claim proof status, assumptions, limitations.
- [docs/research_history.md](docs/research_history.md): research decisions and developments through 2026-11-10.
- [results/benchmark.md](results/benchmark.md): values, inequalities, reproducibility cautions.
- [literature/novelty_matrix.md](literature/novelty_matrix.md): closest prior work and non-claims.
- [literature/related_literature_master.md](literature/related_literature_master.md): comprehensive 24-paper register with bibliography, Japanese-context summaries, distinctions and evidence levels.
- [literature/citation_plan.md](literature/citation_plan.md): prioritized references, section placement and concise English related-literature paragraph plan.
- [docs/roadmap.md](docs/roadmap.md): manuscript and referee-readiness checklist.
- [docs/WORKFLOW_STATUS_2026-11-10.md](docs/WORKFLOW_STATUS_2026-11-10.md): v2.9 research workflow gate-by-gate status.
- [docs/EXPOSITION_ARCHITECTURE_2026-11-10.md](docs/EXPOSITION_ARCHITECTURE_2026-11-10.md): section and exhibit necessity map.
- [docs/PDF_QA_2026-11-10.md](docs/PDF_QA_2026-11-10.md): 13-page reproducible PDF build and page-level QA.
- [docs/AUTHOR_AND_AI_PROVENANCE_2026-11-10.md](docs/AUTHOR_AND_AI_PROVENANCE_2026-11-10.md): research assistance and verification-role ledger.
- [docs/manuscript_outline.md](docs/manuscript_outline.md): **recommended lean six-section submission structure**, numbered-results budget and model-paper examples.
- [docs/theorem_architecture.md](docs/theorem_architecture.md): proposed lemma/proposition/theorem/corollary order, economic intuitions, proof dependencies, and caveats.
- [code/finite_cost_proof.py](code/finite_cost_proof.py): original symbolic proof/certification script.
- [results/finite_cost_proof_log.txt](results/finite_cost_proof_log.txt): original run log.
- [paper/main.tex](paper/main.tex): **complete six-section English working manuscript v0.1**, with analytical appendices (not yet submission-certified).
- [paper/BUILD_AND_REVIEW.md](paper/BUILD_AND_REVIEW.md): PDF compilation/review instructions and source identity.

## Reproduce

```bash
python -m pip install -r requirements.txt
python code/finite_cost_proof.py
```

The exact Bernstein-coefficient sign checks use SymPy rational arithmetic. SciPy and NumPy are used for **numeric display**, not for the rational sign certificates. A successful script run is *not* a substitute for a complete independently audited mathematical proof.

## Publication and rights

Drafts, proofs, and literature notes are provisional; check each journal's preprint and code policies. No unpublished third-party manuscripts or private data should be committed without permission. **This repository was observed as PUBLIC at initialization.**