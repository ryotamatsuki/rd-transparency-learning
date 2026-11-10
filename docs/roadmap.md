# Submission-oriented roadmap

Objective: submit a defensible, concise, analytically focused paper to an appropriate field journal, rather than add unneeded modeling features.

## Priority 0 — reproducibility and math (must pass before submission)

- [x] Preserve finite-cost symbolic script and original run log.
- [x] Create readable model/timing definitions and assumptions register.
- [ ] Re-derive all price-demand FOCs and second-order/admissibility conditions independently.
- [ ] Audit hidden-information off-equilibrium deviations: A's price fixed, B may reprice; equilibrium beliefs consistent.
- [ ] Independently check every Bernstein sign bound and global-contraction premise; document exact rational lower bounds in appendix.
- [ ] Replicate fixed-(s,b) counterfactual in code; separate exact results from reported approximations.
- [ ] Add machine-readable benchmark CSV and unit tests for analytically known cases.
- [ ] Establish what breaks outside \(s,b\in[0,1/2]\), \(\lambda\in[0,1]\) and below the sufficient \(k_\lambda\) threshold.
- [ ] Prove the \(\lambda D_1\to\lambda\) learning-feedback ablation (formal invariance result).

## Priority 1 — originality/referee checks

- [ ] Read Baik & Kim (2020) section 7.3 and appendices; translate their welfare and price competition conditions into direct comparison.
- [ ] Read the **September 2026 revision** of Kim & Poggi, including every main theorem.
- [ ] Read Jiang & Xiong (2025), Sengupta (2016), and Besanko et al. (2014) for the same dynamic incentive components.
- [ ] Precisely separate investor/media short-termism (Huang et al. 2023) from competitor-price-defense short-termism (this model).
- [ ] Build a side-by-side mechanism-removal matrix and a one-paragraph nonredundancy argument; withdraw priority claims that do not survive.

## Priority 2 — paper and journal

- [ ] Complete English model, equilibrium characterization, propositions, proofs and economic discussion.
- [ ] In the body, emphasize **experience-contingent learning + price reaction + investment mix**; put lengthy polynomials and certificates in technical appendix.
- [ ] Declare welfare accounting clearly and explain that higher *public* profits do not imply endogenous voluntary public disclosure.
- [ ] Check journal scope, current manuscript requirements, code/data policy, preprint allowance and fees.
- [ ] Select between Journal of Economics / B.E. Journal of Economic Analysis & Policy and alternatives based on theorem-level novelty.
- [ ] Conduct a hostile mock referee assessment before submission.

## Avoid for the first submission unless strictly necessary

- Endogenous locations; >2 periods; patents, spillovers; public disclosure choice stage; privately drawn learning types; fixed R&D budget; forward-looking multi-period consumers.

## Definition of done

A candidate submission is **not ready** merely because a script runs: it needs a complete proof readable by a referee, a reproducible computational appendix, direct prior-paper proposition comparisons, and clear limitations.
