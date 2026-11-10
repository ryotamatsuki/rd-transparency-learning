# Propositions and verification register

Last reviewed: 2026-11-10 (minimal Stage 4A independent reconstruction added). **Distinguish a computer-checked and separately reconstructed symbolic certificate from human refereeing or formal proof-assistant certification.** Claims below describe research evidence, not journal acceptance or peer-reviewed originality.

| ID | Claim | Current evidence | Remaining verification |
|---|---|---|---|
| P0 | Unique interior period-2 Hotelling price equilibrium and period-1 dynamic price expressions | Algebraic derivation | Check admissibility at all off-path histories |
| P1 | At \(\lambda=0\), public marginal return is negative and hidden unilateral marginal return positive for \(0<d<3t\) | Closed-form differentiation | Reconcile all discount/derivative conventions in appendix |
| P2 | For sufficiently high \(k_\lambda\), hidden \(\lambda>0\), public \(\lambda=0\), \(s^H>s^P\), \(b^H<b^P\) | Local expansion, implicit-function argument | Formal global proof for general (unrestricted) parameters |
| P3 | Sufficient general conditions yielding private-profit / welfare reversal | First-order-in-\(\eta=1/k_\lambda\) expansion | Strict inequality range, payoff-envelope details |
| P4 | At normalized parameters, finite-cost branch has all R&D, profit and welfare sign comparisons | Exact rational Bernstein certificates; \(\lambda\in(0,1/2]\) | Human-readable full certificate appendix |
| P5 | Under specified compact strategy sets, unique **pure-strategy** equilibrium and full sign comparisons when \(k_\lambda>4343/32448\) | Separate primitive-demand reconstruction, independent exact rational sign certificates and global Stage-0 monotonicity; numerical finite-deviation attacks | Human proof audit; mixed PBE exclusion and general-parameter theorem **not** covered |
| P6 | Branch comparisons continue to \(k_\lambda\ge0.1\) | Exact rational Bernstein positivity | This does NOT establish global equilibrium uniqueness on entire extended range |
| P7 | At benchmark \(k_\lambda=0.3\), both firms profit more in public, while hidden yields higher welfare and period-2 relative B quality | Equilibrium solution and rational certificate | Optional second independent solver |
| C1 | Removing first-period-market-share dependence (\(q_2=-d+\lambda\)) eliminates disclosure effect under otherwise fixed common-knowledge setup | Analytical intuition / draft auxiliary lemma | Write complete proof, enumerate uniqueness and observability assumptions |
| N1 | Novelty beyond joint implication of disclosure and learning-by-doing papers | Targeted literature comparison | Full theorem-level adversarial comparison remains pending |

## Key derivative identities (general parameters)

\[
\left.\frac{d V_B^P}{d\lambda}\right|_0
=-\frac{2\delta d(3t-d)}{81t^2},
\qquad
\left.\frac{\partial V_B^H}{\partial\lambda}\right|_0
=\frac{\delta(3t-d)^2}{54t^2}.
\]

The hidden derivative uses **A's price held fixed under B's unobserved unilateral deviation** (while B's own price can readjust). Difference:

\[
\delta(3t-d)(9t+d)/(162t^2)>0.
\]

For the asymptotic general result define \(c=(1+\delta)/(9t)\), \(\Delta=k_sk_b-c(k_s+k_b)\), and the no-learning equilibrium
\[
d_*=\frac{d_0+3tc(1/k_s-1/k_b)}
{1-c(1/k_s+1/k_b)}.
\]

A sufficient region used in prior work is \(k_s>c\), \(k_b>c\), \(\Delta>0\), \(t\le d_*<3t\), plus a strict incumbent-profit inequality and sufficiently large \(k_\lambda\). **Do not extend the numerical threshold \(4343/32448\) to unrestricted \(t,\delta,d_0,k_s,k_b\).**

## Finite-cost numerical instance

At \(t=\delta=d_0=1\), \(k_s=k_b=4\), \(k_\lambda=0.3\):
- Public: \(s=11/48\), \(b=5/48\), \(\lambda=0\).
- Hidden: \(s\simeq0.2524920154\), \(b\simeq0.0967458787\), \(\lambda\simeq0.2111017436\).
- A profit: P \(\simeq1.7855903\) > H \(\simeq1.7190065\).
- B profit: P \(\simeq0.3689236\) > H \(\simeq0.3419362\).
- Welfare: H \(\simeq-0.9142776\) > P \(\simeq-0.9418403\).

## Minimal independent Stage 4A audit (new)

- Full report: [audits/STAGE4A_MINIMAL_AUDIT_2026-11-10.md](../audits/STAGE4A_MINIMAL_AUDIT_2026-11-10.md).
- Independent algebra and finite-deviation code: [code/stage4a_independent_audit.py](../code/stage4a_independent_audit.py). The production `finite_cost_proof.py` is *not* imported by this independent code.
- **Narrow result:** all finite unilateral learning/quality price/quantity-investment deviations and alternative **pure** Stage-0 equilibria are excluded within the normalized compact action sets for the explicit sufficient cost threshold, subject to the frozen full-coverage demand primitives.
- **Project Stage 4A still unresolved:** general structural parameters and mixed-strategy PBE remain outside the audit; do not call the general model formally certified.

## Essential qualifications

- Public profit gains + welfare loss are **not independently novel**.
- R&D shifting toward short-term activity under disclosure has related precedents.
- A fixed-quality-R&D counterfactual also yields a welfare reversal; composition effects **amplify**, rather than create as a necessary condition, the reversal.
- \(\lambda^H>\lambda^P\) does not imply that concealed investment is unpredictable in equilibrium.
- Claims about voluntary disclosure equilibrium require a different game, not covered here.
- A two-period result does **not** establish an infinite-horizon delay of technological replacement.
