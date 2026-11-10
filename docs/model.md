# Model specification (working; 2026-11-10)

## Economic environment

Two firms on a unit Hotelling line, A at 0 and B at 1; uniform unit mass of myopic consumers per period, full coverage, marginal production cost 0, transport disutility t>0. Outside-option utility v is sufficiently high.

For period k=1,2:

- \(\ U_{A,k}(x)=v+q_{A,k}-p_{A,k}-tx\ \)
- \(\ U_{B,k}(x)=v+q_{B,k}-p_{B,k}-t(1-x)\ \)

Both firms maximize first-period profit plus \(\delta\in(0,1]\) times second-period profit minus real R&D expenditure.

## R&D and timing

- Stage 0: A and B simultaneously choose \(s\ge0\) and \(b\ge0\), observed before pricing.
- Stage 1: B chooses learning capability \(\lambda\ge0\). In P, A observes \(\lambda\); in H, A does not.
- Stage 2: simultaneous period-1 prices; B's resulting share is \(D_1\).
- Stage 3: B learns \(\lambda D_1\); period-2 quality is observed; simultaneous period-2 prices.

Qualities: \(q_{A,1}=q_{A,2}=s\), \(q_{B,1}=b-d_0\), \(q_{B,2}=b-d_0+\lambda D_1\). Define \(d=d_0+s-b\) and \(q=-d+\lambda D_1\).

Costs: \(C_A=k_s s^2/2\), \(C_B=k_b b^2/2+k_\lambda\lambda^2/2\).

**Interpretation:** b has an immediate effect that **persists** in period 2. It is not a quality investment that expires at the end of period 1. "R&D composition" does not imply a fixed R&D budget.

## Stage 3: exact Hotelling price equilibrium

For entrant relative quality q:

\[
p_{A,2}=t-q/3,\qquad p_{B,2}=t+q/3,\qquad
D_2=(3t+q)/(6t).
\]

Second-period profits:

\[
\pi_{A,2}=(3t-q)^2/(18t),\quad
\pi_{B,2}=(3t+q)^2/(18t).
\]

Maintain interior demand/price conditions.

## Stage 2: exact dynamic price equilibrium

\[
D_1=\frac{27t^2-9dt-2\delta d\lambda}
{2(27t^2-\delta\lambda^2)},
\quad q=-d+\lambda D_1.
\]

\[
p_{A,1}=2t(1-D_1)-\delta\lambda(3t-q)/(9t),
\quad p_{B,1}=2tD_1-\delta\lambda(3t+q)/(9t).
\]

Continuation gross profits \(V_i\) are \(p_{i,1}D_{i,1}+\delta\pi_{i,2}\) evaluated at these prices.

## Public vs hidden information

Public: after investment, A conditions first-period price on the observed \(\lambda\); B faces an *endogenous price response* when deviating.

Hidden: A anticipates the equilibrium \(\lambda\), but A's first-period price cannot condition on the realized (unobserved) \(\lambda\). Deviations by B in Stage 1 must hold A's strategy fixed, while B can reoptimize its own price.

This is a pure-strategy, common-knowledge equilibrium with unobserved deviations; it is **not** a Bayesian private-technology-type model.

## Social welfare

With shares \(D_1,D_2\), constant common utility suppressed:

\[
\begin{aligned}
W={}&(1+\delta)s-d(D_1+\delta D_2)+\delta\lambda D_1D_2\\
&-\frac t2[(1-D_1)^2+D_1^2+\delta((1-D_2)^2+D_2^2)]\\
&-k_s s^2/2-k_b b^2/2-k_\lambda\lambda^2/2.
\end{aligned}
\]

Prices are transfers and cancel in aggregate surplus. Do not confuse gross market surplus \(T_1+\delta T_2\) with welfare after real research costs.

## Exactly normalized certification environment

\(t=\delta=d_0=1\), \(k_s=k_b=4\); restrict \(s,b\in[0,1/2]\), \(\lambda\in[0,1]\). All global-equilibrium statements from the finite-cost certificate are conditional on these compact strategy sets.

Equivalent normalizations for other parameter values have **not** been established. See \`code/finite_cost_proof.py\` and \`docs/propositions.md\`.
