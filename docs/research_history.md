# Research history and decisions (through 2026-11-10)

This is a retrospective reconstruction from the project discussions, not an assertion that every intermediate derivation was independently checked. Maintain it as a chronological changelog going forward.

## 2026-11-09: research concept / original Hotelling explorations
- Target: a publishable, minimal Hotelling industrial-organization model with an analytically sharp and nontrivial contribution, rather than accumulating numerical examples.
- R&D learning/observability concept: incumbent A can use first-period price to deny entrant B sales experience that would raise future quality.
- Chosen structure: two-period fully covered Hotelling–Bertrand, fixed endpoint locations; incumbent persistent-quality \(s\), entrant immediate-quality \(b\), entrant learning-efficiency \(\lambda\); \(q_{B,2}=b-d_0+\lambda D_1\).
- Three candidate results: (1) hidden-vs-public incentive difference; (2) endogenous \(s,b,\lambda\) reallocations; (3) both firms preferring public while social welfare prefers hidden.
- Key concern recognized: equilibrium investment predictability under secrecy; interpret hidden deviations correctly.

## 2026-11-10 (first analysis): asymptotic sufficient conditions
- Backward induction through period-2 and period-1 price subgames.
- Analytic public and hidden one-sided derivatives at \(\lambda=0\) differ in sign for \(0<d<3t\).
- High-learning-cost expansion \(\eta=1/k_\lambda\to0^+\) gives \(\lambda^H=\eta \delta(3t-d)^2/(54t^2)+O(\eta^2)\), \(\lambda^P=0\).
- Under stability and sufficiently pronounced baseline incumbent quality advantage, \(s^H>s^P\), \(b^H<b^P\), and welfare can be higher in H even when both profits are higher in P.
- Initial benchmark from previous calculations: \(k_\lambda=0.3\) had \(s_P\sim0.2292\), \(s_H\sim0.2525\); \(b_P\sim0.1042\), \(b_H\sim0.0967\); \(\lambda_P=0\), \(\lambda_H\sim0.2111\).

## 2026-11-10 (finite-cost proof)
- With \(t=\delta=d_0=1,\;k_s=k_b=4\), compact domains \(s,b\in[0,1/2]\), \(\lambda\in[0,1]\), eliminated equilibrium decisions to a cubic in quality gap \(d\) parametrized by \(\lambda\) and a rational function \(k_\lambda=K(d,\lambda)\).
- Derived sufficient global-unicity threshold \(k_\lambda>4343/32448\) within these domains. Certified algebraic comparison signs on the related branch and extended sign check down to \(k_\lambda\ge0.1\) (branch only).
- Generated and reran \`code/finite_cost_proof.py\`; all reported rational Bernstein inequalities passed.
- Reproduced both profit comparisons, welfare gain under H, entrant share reversal from period 1 to period 2, and period-wise gross market-surplus comparisons.
- Research constraint: exact symbolic sign checks are evidence for these specific expressions/regions; retain independent human audit for proof completeness.

## 2026-11-10 (novelty/referee pass)
- Main negative finding: disclosure increasing profits and reducing welfare is already established in differentiated Bertrand R&D-observability literature (esp. Baik & Kim 2020).
- R&D disclosure inducing short-horizon innovation also has precedents (Huang et al. 2023; Chen, Liang & Petrov 2024 addresses exploration/disclosure).
- Kim & Poggi's innovation-race work already models direct development vs research for future technology; do not claim this binary R&D choice per se as novel.
- Reframe potential contribution: **endogenous price defense \u2192 experience-based learning \u2192 entrant R&D composition \u2192 amplification of a welfare loss**, with no appeal to investor myopia or technology spillovers.
- Important counterfactual: when s and b are held at public values, switching only \(\lambda\) under hidden information still improves welfare; therefore R&D portfolio reallocation is an amplifier, **not a necessary cause** of the welfare reversal.
- Suggested auxiliary lemma: remove demand feedback from learning (\(q_{B,2}=b-d_0+\lambda\)) and, under unchanged knowledge/timing, disclosure regime difference disappears. Formalize and audit.

## Publication decision
- Aim for early submission to an appropriate middle-tier field journal, not unnecessary extensions.
- Prioritize readable proof appendix, theorem-level prior-paper comparison, cautious originality statement, and a full manuscript draft.
- Candidate outlets discussed: Journal of Economics; The B.E. Journal of Economic Analysis & Policy; Economics of Innovation and New Technology; Review of Industrial Organization. No acceptance probability is implied.
