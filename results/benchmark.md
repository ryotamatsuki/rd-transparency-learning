# Benchmark and certified comparison signs (2026-11-10)

Environment: \(t=\delta=d_0=1\), \(k_s=k_b=4\), \(k_\lambda=0.3\), \(0\le s,b\le0.5\), \(0\le\lambda\le1\).

| Variable | Public P | Hidden H |
|---|---:|---:|
| A persistent quality investment s | 0.2291666667 (= 11/48) | 0.2524920154 |
| B immediate quality investment b | 0.1041666667 (= 5/48) | 0.0967458787 |
| B learning investment lambda | 0 | 0.2111017436 |
| Quality gap d = 1+s-b | 1.125 | 1.1557461367 |
| B first-period demand | 0.3125 | ~0.29883 |
| B second-period demand | 0.3125 | ~0.31789 |
| A net profit | 1.7855902778 (=2057/1152) | 1.7190065340 |
| B net profit | 0.3689236111 (=425/1152) | 0.3419361774 |
| Welfare, common v suppressed | -0.9418402778 (=-1085/1152) | -0.9142775978 |

Social welfare difference H-P: approximately **+0.02756268**. Prices are transfers and cancel out of W; R&D costs are counted as real costs.

## Algebraic certification

- The symbolic program constructs rational first-period shares, prices, gross continuation profits, the hidden Stage-1 first-order condition \(k_\lambda=K(d,\lambda)\), and an implicit Stage-0 scalar condition.
- It verifies the normalized equilibrium branch on \(0<\lambda\le0.5\) using exact rational multivariate Bernstein-coefficient bounds: R&D investment direction, both firms' profit ordering, total welfare, B's first-period and second-period share reversal, B's second-period relative quality, and both periods' gross market surplus.
- A second Bernstein check covers comparisons on the equilibrium branch for \(0<\lambda\le0.6\), supporting an **equilibrium-branch** bound \(k_\lambda\ge0.1\); do not equate this with global equilibrium uniqueness.
- Separate derivative/concavity and price-admissibility bounds are used for the **sufficient** globally unique-equilibrium threshold \(k_\lambda>4343/32448\approx0.1338449211\), conditional on the specified compact strategy sets.
- The threshold is sufficient, not a necessary or sharp economic phase boundary. The paper-quality proof requires an independent reading of every off-path/game-theoretic step.

## Reproduction

\`\`\`bash
python -m pip install -r requirements.txt
python code/finite_cost_proof.py
\`\`\`

The first-party script from the analysis session and its full original output are preserved without rewriting:
- \`code/finite_cost_proof.py\`
- \`results/finite_cost_proof_log.txt\`

The script was rerun on 2026-11-10 in a Python environment and ended with "All exact-rational certificates succeeded." Compare changes using a pull request and archive a new log for materially changed proof claims.

## Counterfactual caveat

Earlier calculations reported a hidden-regime counterfactual with s,b **fixed at their public values** and learning investment reoptimized. Estimated \(\lambda=0.218541\) and welfare \(-0.929585\). It is **not** a stand-alone equilibrium of the full investment game, and is recorded as a previous result awaiting independent coded replication. It suggests that R&D composition **amplifies** but is **not necessary for** the welfare reversal.
