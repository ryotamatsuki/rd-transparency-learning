# Stage 4A — General-parameter, high-learning-cost equilibrium audit

**Date:** 2026-11-10  
**Project:** `ryotamatsuki/rd-transparency-learning`  
**Independent reconstruction:** `code/general_high_cost_stage4a.py`  
**Targets:** general-parameter Proposition 2 and Theorem 1 in the November 10 draft.  
**Verdict:** **FAIL for the unrestricted-investment wording; conditional algebraic PASS for a corrected compact admissible-domain, pure-strategy theorem.** The latter is a **substantive scope change** that must be made explicit in the model, main propositions, and manuscript. The counterexample must not be discarded.

## Executive conclusions

1. The published-in-draft stability restrictions `k_s>c`, `k_b>c`, `Delta>0`, `t <= d_* < 3t`, and the *strict incumbent-profit condition* do **not** suffice to make the interior investment profile a global equilibrium when quality investments are unbounded. An exact counterexample is given below; a finite jump by A crosses the demand corner and gains a strictly positive amount even when `k_lambda` is arbitrarily high.
2. A genuine general-parameter theorem **can** be established for a distinct, clearly limited class of games: firms have explicit compact quality-investment sets whose **entire** quality-gap range lies in `(0,3t)`, and a suitably small admissible learning-investment bound. This is not merely choosing a selected equilibrium from the unbounded game; it is a change of feasible actions.
3. In that restricted game, a **uniform high-cost argument**, a fixed-incumbent-price hidden deviation proof, and a **strongly monotone Stage-0 pseudo-gradient** give **existence and uniqueness of a pure-strategy PBE** in both regimes and exclude *all finite unilateral investment deviations*, not just FOC deviations. The leading investment/profit/welfare coefficients agree with the previously derived general-parameter expressions. The proof covers open non-normalized parameter regions.
4. Six genuinely non-normalized numerical regressions, including `t != 1`, `delta != 1`, `d0 != 1`, and `k_s != k_b`, found zero positive finite-deviation gains and one interior pure equilibrium in 25 initializations each. This is supporting computation, **not** the uniform theorem proof.
5. **Not certified:** the original unbounded game, all mixed-strategy PBE, an explicit parameter-free finite threshold for general `k_lambda`, and theorem novelty. Stage 6/7.5A remains open.

## 1. Counterexample: existing general sufficient conditions are not global

Take

\[
t=\delta=d_0=1,\qquad k_s=\frac45,\quad k_b=4.
\]

Then `c=2/9`, `Delta=32/15>0`, and the candidate interior zero-learning R&D equilibrium is

\[
d_* = \frac52,\qquad s_*=\frac{55}{36},\qquad b_*=\frac1{36}.
\]

All inequalities in the manuscript's **stated algebraic** high-cost theorem hold. In particular `t<d_*<3t`, `k_s>c`, `k_b>c`, `Delta>0`; the extra strict incumbent-profit margin

\[
\frac{\delta(9t-2d_*)}{9t(1+\delta)}h(d_*)+B_1
=\frac{125}{559872}>0
\]

is strictly satisfied. The A payoff at this candidate (with B's public learning investment zero, as it is at sufficiently high learning cost) equals

\[
\Pi_A^{\rm cand} =\frac{1573}{648}.
\]

Holding B's `b=1/36` fixed, A can unilaterally choose `s'=5/2`, giving `d'=125/36>3t`. The **actual price equilibrium changes regimes**: A captures the whole market at `p_A=d'-t=89/36`, B charges zero and has no customers. The new A payoff is

\[
\Pi_A^{\rm dev}=(1+\delta)(d'-t)-\tfrac{k_s}{2}(s')^2
=\frac{22}{9}.
\]

Thus

\[
\Pi_A^{\rm dev}-\Pi_A^{\rm cand}=\boxed{\frac{11}{648}>0}.
\]

At the corner B receives no customer experience; B's learning investment has no payoff and its best response is zero. Hence the strictly profitable deviation remains relevant to the **public regime at high learning cost**. This is a failure of **global best response**, not numerical instability or a second equilibrium on the original interior branch. The violation is strict and therefore persists under sufficiently small parameter perturbations.

**Consequence:** The original unrestricted Stage-0 theorem cannot be described as `SPNE/PBE verified`. The phrase "regularity of globally unique continuation" is not a substitute for bounding a competitor-exclusion deviation when the primitive model permits it.

## 2. Corrected general-parameter theorem: exact scope and assumptions

### Primitive game and domain

Fix arbitrary

\[
t>0,\quad 0<\delta\le1,\quad d_0>0,\quad k_s,k_b>0.
\]

**Change the primitive strategy domains** to

\[
s\in[0,\bar s],\qquad b\in[0,\bar b],\qquad
\lambda\in[0,\bar\lambda],
\]

where `bar s`, `bar b`, `bar lambda` are technological or feasible-investment caps, **not** just numerical-solver boundaries. Put

\[
J=[d_0-\bar b,\ d_0+\bar s],\qquad
0<d_0-\bar b<d_0+\bar s<3t. \tag{G1}
\]

Choose `bar lambda > 0` **sufficiently small for every** quality gap `d in J`, so that (i) public period-1 price equilibria, (ii) B's price best reply when A keeps the on-belief price fixed under a hidden deviation, and (iii) all second-period realized-quality price games retain their unique, strictly interior global best-response solution. Such a positive cap exists by uniform continuity from the strictly interior zero-learning Hotelling equilibrium over compact `J`; see the pricing argument below. This explicit smallness requirement cannot be omitted.

Let

\[
c=\frac{1+\delta}{9t},\qquad
\Delta=k_sk_b-c(k_s+k_b), \tag{G2}
\]

\[
d_* = \frac{d_0+3tc(k_s^{-1}-k_b^{-1})}
           {1-c(k_s^{-1}+k_b^{-1})},\quad
s_* = \frac{c(3t+d_*)}{k_s},\quad
b_* = \frac{c(3t-d_*)}{k_b}.\tag{G3}
\]

Assume `k_s>c`, `k_b>c`, `Delta>0`, `s_* in (0,bar s)`, `b_* in (0,bar b)`, and `0<d_*<3t` (the latter follows from G1 and the interior stage-0 solution). For the headline welfare reversal further assume

\[
t\le d_*<3t,\qquad
\mathcal M_A:=\frac{\delta(9t-2d_*)}{9t(1+\delta)}h(d_*)+B_1>0,\tag{G4}
\]

with `h(d)=delta(3t-d)^2/(54t^2)` and `B_1` as below.

### Corrected Theorem G (high-cost, pure-strategy, compact investment game)

Under G1–G3 and a sufficiently small positive learning cap, there exists finite `K_0` **depending on the primitive parameters and the three caps** such that for each `k_lambda>K_0`, the public and hidden games each have a **unique pure-strategy PBE in investment/pricing actions** on the stipulated feasible set; all material price and investment best responses are globally optimal within that set. The public equilibrium has `lambda^P=0`. In the hidden equilibrium,

\[
\begin{aligned}
\lambda^H&=\frac{h(d_*)}{k_\lambda}+O(k_\lambda^{-2})>0,\\
s^H-s^P&=\frac{S_1}{k_\lambda}+O(k_\lambda^{-2})>0,\\
b^H-b^P&=\frac{B_1}{k_\lambda}+O(k_\lambda^{-2})<0.
\end{aligned}
\]

If, in addition, G4 holds, then for all sufficiently large `k_lambda`,

\[
\Pi_A^P>\Pi_A^H,\qquad
\Pi_B^P>\Pi_B^H,\qquad W^H>W^P.
\]

The parameter/cap conditions describe a nonempty open family; for example `t=d0=1`, `delta=4/5`, `ks=kb=4`, `bar s=bar b=1/2` satisfy all strict inequalities, with an appropriately small positive `bar lambda`.

**No statement is made** about PBE multiplicity after relaxing the primitive action caps, mixed-strategy PBE, or explicit `K_0` uniform over the whole parameter space. The normalized finite-cost certification with learning cap 1 remains a distinct, independently established domain and need not meet this theorem's small-cap construction.

## 3. Independent proof: every relevant stage and all pure unilateral deviations

### 3A. Price subgames and boundaries

Period-1 demand under interior sharing and a fixed quality gap is

\[
D_1=\frac{t-d+p_A-p_B}{2t},\qquad
q=-d+\lambda D_1.
\]

Substituting second-period optimal profits `(3t-q)^2/(18t)` and `(3t+q)^2/(18t)` in the first-period price objectives and differentiating from **primitive payoffs** gives the unique candidate

\[
D(d,\lambda)=\frac{27t^2-9dt-2\delta d\lambda}
{2(27t^2-\delta\lambda^2)},\quad
p_A=2t(1-D)-\frac{\delta\lambda(3t-q)}{9t},\quad
p_B=2tD-\frac{\delta\lambda(3t+q)}{9t}.
\]

At `lambda=0`, the equilibrium is `p_A=t+d/3>0`, `p_B=t-d/3>0`, with shares bounded away from both 0 and 1 **uniformly on J**. The static full-market-coverage Hotelling price game with `0<d<3t` has a unique global Nash price pair: the two individual price payoffs are quadratic on the interior segment, linear in price when capturing all consumers, and zero in current operating revenue when capturing none. The corners cannot be Nash for `d<3t` because a profitable small share-expanding or margin-raising deviation exists.

For the dynamic price game, each interior own-price second derivative equals `-1/t + delta*lambda^2/(36*t^3)`; the first-order equation has determinant proportional to `27*t^2-delta*lambda^2`. Both properties persist for small `lambda`. Any price-equilibrium sequence as `lambda -> 0` has a bounded subsequence: when a firm earns zero current demand, its rival's price must be low enough to prevent a profitable zero/positive-price undercut; the fully served firm cannot face an indefinitely large no-demand rival price without raising its own price. Interior equilibria have prices bounded directly by their FOCs. By compactness and upper hemicontinuity, a sequence of additional corner equilibria for `lambda -> 0` would converge to a forbidden corner equilibrium at `lambda=0`. Hence **one common small cap** exists on compact J under which there is a unique globally valid interior pricing equilibrium. This also covers the last-stage game for all realized shares if `bar lambda<min(d_min, 3t-d_max)`.

For additional boundary clarity, at a putative corner with **zero entrant demand**, B could enter profitably at a small positive price whenever A's price exceeded `d-t`. Hence a corner Nash must have `p_A <= d-t`; but at the sharing boundary the incumbent's derivative from increasing its price is at least

\[
\frac{3t-d_{\max}}{2t}-\frac{\delta\bar\lambda(3t+d_{\max})}{18t^2}>0
\]

provided `bar lambda < 9t(3t-d_max)/(delta(3t+d_max))`. The incumbent would therefore raise its price; the corner cannot be an equilibrium. The opposite corner, **zero incumbent demand**, fails because A can charge a small positive price to enter and simultaneously reduce B's learning. At a boundary price `p_A=0`, A's one-sided payoff derivative is uniformly positive for sufficiently small learning cap; at `p_B=0` with interior demand, A's best response converges uniformly to `(t+d)/2` as learning vanishes and B's own price derivative converges to `(3t-d)/(4t)>0`. Thus all nonnegative-price and zero-share boundaries are excluded before applying the unique interior FOC system.

**Under hidden Stage-1 deviations**, the incumbent's price is **fixed at its on-belief equilibrium price z**, while B can reoptimize its own first-period price. From B's primitive price FOC, its optimized period-1 share is

\[
D_{\rm dev}(d,\lambda,z)=
\frac{9t(t-d+z)+\delta\lambda(3t-d)}{36t^2-\delta\lambda^2}.
\]

Because `z` is uniformly near `t+d/3` and `lambda` is within a small compact cap, this B best response is strictly interior and globally optimal; every larger price or corner alternative is inferior. **This corrects the common error** of allowing A to reset its first-period price in response to an investment deviation A cannot observe.

### 3B. Public Stage-1 learning: zero globally, not just locally

Differentiate B's gross continuation payoff **along the publicly observed investment/price equilibrium**. At zero,

\[
\partial_\lambda V_B^P(d,0)
=-\frac{2\delta d(3t-d)}{81t^2}<0.
\]

On compact `J subset (0,3t)`, the negative derivative is bounded away from zero. By continuity, for the same sufficiently small positive `bar lambda`, `V_B^P(d,lambda)` is **strictly decreasing over the entire feasible learning interval**, for every feasible d. The convex learning cost further decreases its payoff away from zero. Therefore `lambda^P(d)=0` is its unique **global** Stage-1 optimum at every observed quality investment history.

### 3C. Hidden Stage-1 learning: global uniqueness with fixed A price

Hold A's first-period price `z` fixed. At B's reoptimized first-period price, the envelope derivative of B's gross continuation payoff is

\[
G_{\rm dev}(d,\lambda,z)
=\frac{\delta}{9t}D_{\rm dev}(d,\lambda,z)
  [3t-d+\lambda D_{\rm dev}(d,\lambda,z)].
\]

Over the compact feasible `(d,lambda,z)` set this quantity and its lambda derivative have finite uniform bounds. Therefore, for any `k_lambda > sup |partial_lambda G_dev|`, B's hidden investment payoff is strictly concave on its **entire learning interval**; its derivative at 0 is strictly positive and at `bar lambda` strictly negative for sufficiently large k_lambda. This **globally excludes zero, cap, and interior alternative investment deviations**.

In a pure PBE, the incumbent correctly anticipates the equilibrium `lambda^H(d)` and chooses the on-belief price from 3A. Thus the fixed-point condition is

\[
k_\lambda\lambda^H=G(d,\lambda^H),\quad
G(d,\lambda)=\frac{\delta}{9t}D(d,\lambda)
 [3t-d+\lambda D(d,\lambda)].\tag{3.1}
\]

Since `G(d,0)=h(d)>0` and `G` has uniformly bounded derivatives, for sufficiently high `k_lambda` equation (3.1) has **exactly one** positive root for each d in J. The implicit-function theorem gives an analytic policy, uniformly in d,

\[
\lambda^H(d;k_\lambda)=k_\lambda^{-1}h(d)+O_{C^2}(k_\lambda^{-2}).
\]

This constructs **all** pure hidden Stage-1 equilibria at every Stage-0 history, not just a selected branch.

### 3D. Stage-0 full-interval deviations and alternate pure equilibria

Let `eta=1/k_lambda`. Both firms' endogenous Stage-1 continuation payoffs are smooth functions only of d:

\[
T_A^H(d)=F_A(d)+\eta u_A(d)+O_{C^2}(\eta^2),\quad
T_B^H(d)=F_B(d)+\eta u_B(d)+O_{C^2}(\eta^2),
\]

where

\[
F_A=\frac{(1+\delta)(3t+d)^2}{18t},\quad
F_B=\frac{(1+\delta)(3t-d)^2}{18t},
\]

\[
\begin{aligned}
g_A(d)&=-\frac{\delta(9t-2d)(3t+d)}{81t^2},\\
g_B(d)&=-\frac{2\delta d(3t-d)}{81t^2},\\
h(d)&=\frac{\delta(3t-d)^2}{54t^2},\\
u_A&=g_Ah,\qquad u_B=g_Bh-\frac{h^2}{2}.
\end{aligned}
\]

The Stage-0 pseudo-gradient for `x=(s,b)` is

\[
\mathcal G(x)=\begin{pmatrix}
\partial_d T_A^H(d)-k_s s\\
-\partial_d T_B^H(d)-k_b b
\end{pmatrix},\qquad d=d_0+s-b.
\]

At `eta=0`, its Jacobian is the **symmetric constant matrix**

\[
\frac{\partial\mathcal G}{\partial(s,b)}(x,0)
=-\begin{pmatrix}k_s-c & c\\ c & k_b-c\end{pmatrix}.
\]

Under `k_s>c`, `k_b>c`, `Delta>0`, it is **uniformly negative definite on the entire compact strategy rectangle**. The `C^2` uniform expansion implies the **symmetric part** of the hidden pseudo-gradient Jacobian remains negative definite for all sufficiently small positive eta. Consequently each firm's payoff remains strictly concave in its **entire own quality-investment range**, and the pseudo-gradient is **strongly monotone decreasing**. A pure Stage-0 Nash equilibrium exists by continuity/concavity on compact convex strategy spaces. Two distinct Nash equilibria would violate the variational inequalities together with strict monotonicity: no alternative pure equilibrium can exist. These statements certify both **global own-deviation optimality and uniqueness**, not merely local FOCs.

The public Stage-0 payoffs are exactly `F_A(d)-k_s s^2/2` and `F_B(d)-k_b b^2/2`, so the same negative-definiteness argument works without asymptotics. The unique public equilibrium is `(s_*, b_*)` from G3, which lies strictly inside the stipulated caps. The hidden equilibrium is unique, interior for high costs by continuity, and smooth in eta by IFT.

### 3E. Comparative statics, profit signs and welfare

The first-order changes are

\[
s^H=s_*+\eta S_1+O(\eta^2),\quad
b^H=b_*+\eta B_1+O(\eta^2),
\]

\[
S_1=\frac{(k_b-c)u_A'+cu_B'}{\Delta}>0,\quad
B_1=-\frac{cu_A'+(k_s-c)u_B'}{\Delta}<0,
\]

where all derivatives are evaluated at d_*. The symbolic sign factors independently verified from primitives are

\[
u_A'(d)=\frac{\delta^2(3t-d)(-8d^2+21dt+45t^2)}{4374t^4}>0,
\]

\[
u_B'(d)=\frac{\delta^2(3t-d)^2(5d+3t)}{4374t^4}>0
\]

for `0<d<3t`. The quadratic `-8(d/t)^2+21(d/t)+45` is positive over `(0,3)`; its endpoint values are 45 and 36, and it is concave.

The hidden-minus-public first-order net-profit coefficients are

\[
\Phi_A=u_A-F_A'(d_*)B_1,
\qquad \Phi_B=u_B+F_B'(d_*)S_1<0.
\]

Since `F_A'>0`, `Phi_A=-F_A'(d_*) M_A`, the **strict** `M_A>0` condition in G4 is precisely the additional incumbent-profit restriction. Both profit differences are therefore strictly negative for high learning cost.

Independently reconstruct welfare from the uniform consumer density, transportation losses and real costs. The first-order difference equals

\[
W^H-W^P=\eta\left\{
\frac{\delta h(d_*)}{162t^2}(10d_*^2-27d_*t+27t^2)
+\frac{1+\delta}{6t}
[(t+d_*)S_1+(t-d_*)B_1]
\right\}+O(\eta^2).
\]

The quadratic `10(d/t)^2-27(d/t)+27` has discriminant `-351<0` and a positive leading coefficient, so it is everywhere strictly positive. If `d_*>=t`, the quality terms are nonnegative: `S_1>0`, `B_1<0`, `t+d_*>0`, `t-d_*<=0`. Therefore the welfare difference is strictly positive. These inequalities are **open and strict** (apart from the allowed boundary `d_*=t`), so they persist for all sufficiently high but finite learning costs.

## 4. Separate attacks / verdict ledger

| Question | Independent attack/evidence | Verdict | Scope |
|---|---|---|---|
| Stage-3 price subgame and offpath realized quality | Exact static Hotelling demand, uniform interior margin | PASS (corrected J, small learning cap) | Pure equilibria and nonnegative prices |
| Stage-2 (first-period) pricing | Independent simultaneous FOCs, corner-nearness contradiction | PASS (corrected J, small learning cap) | Pure, all feasible public learning actions |
| Unobserved B learning deviation | Derive fixed-z B price response, envelope, strict global learning concavity | PASS (corrected game, high K) | Every lambda in [0,bar lambda] |
| Public B learning deviation | Uniform strictly negative gross marginal return for full learning cap | PASS (corrected game) | Every lambda in [0,bar lambda] |
| A and B Stage-0 global quality deviations | Uniform own strict concavity, compact rectangle | PASS (corrected game, high K) | Every s/b in permitted ranges |
| Alternative pure investment equilibria | Uniform negative-definite pseudo-gradient / VI uniqueness | PASS (corrected game, high K) | All pure Stage-0 equilibria |
| Signed R&D/profit/welfare comparisons | Independent primitive-based symbolic identities and strictly signed coefficients | PASS (corrected G1–G4, high K) | Existence of finite model-dependent K0 |
| **Unbounded quality-investment equilibrium** | Exact profitable monopoly deviation (Section 1) | **FAIL** | Refutes original algebraic conditions as globally sufficient |
| Alternate mixed PBE / mixed pricing | Not tested | UNRESOLVED | Do not claim arbitrary PBE uniqueness |
| Uniform explicit general K0 | No closed-form bound derived | NOT CLAIMED | The original high-cost theorem is existential |
| Formal proof assistant | Not executed | Stage 7.5A OPEN | Candidate targets: Rosen monotonicity and sign inequalities |
| External human/author independent verification | Not performed | OPEN | AI+computation only; author intellectual audit required |
| Theorem novelty | Not part of this gate | Stage 6 OPEN | Parent model absorption unresolved |

## 5. Non-normalized numerical regression log

The independent script evaluated the following cases at `k_lambda=20`; each uses the stated bounded Stage-0 actions and small learning cap, with baseline investments strictly interior. It globally optimized each firm's *own* investment against the other candidate action on the entire stated interval, holding the incumbent price fixed for hidden learning deviations; checked public learning deviations; and launched 25 interior Stage-0 equilibrium searches per case.

| Case | t | delta | d0 | ks | kb | S, B | learning cap | Outcome |
|---|---:|---:|---:|---:|---:|---|---:|---|
| I | 1 | 1 | 1 | 4 | 4 | 0.5,0.5 | 0.2 | No positive deviation |
| II | 1 | 0.5 | 1 | 4 | 4 | 0.5,0.5 | 0.2 | No positive deviation |
| III | 1 | 0.75 | 1.2 | 4 | 5 | 0.5,0.5 | 0.2 | No positive deviation |
| IV | 2 | 1 | 2 | 2 | 2 | 1,1 | 0.4 | No positive deviation |
| V | 1 | 0.8 | 1.05 | 3 | 5 | 0.5,0.5 | 0.2 | No positive deviation |
| VI | 1 | 0.6 | 1.2 | 8 | 7 | 0.5,0.5 | 0.2 | No positive deviation |

Observed maximal gains were at numerical rounding scale (about `1e-16`). A grid/multistart check cannot certify the uniform theorem; analytical strong monotonicity is what rules out additional pure equilibria. The exact counterexample and all symbolic general identities are machine-checked with SymPy. The script writes `results/general_high_cost_numeric_results.json`.

## 6. Manuscript/workflow change control and recommendation

**Do not silently keep** `s,b,lambda>=0` with no upper bounds in the published theorem. The profitable A deviation proves that the prior quoted general assumptions are insufficient for unrestricted investments. A revised model must either (a) **explicitly adopt admissible compact action bounds G1 and sufficiently small bar lambda** and state the result for that game, or (b) prove separate no-entry/monopoly-regime-deviation inequalities for the original unrestricted game. Only (a) has been audited here. The normalized finite-cost theorem is independently valid on its **own** specified `[0,1/2] x [0,1/2] x [0,1]` domain; it remains distinct from the small-learning-cap asymptotic construction.

**Workflow routing:** Original Stage 4A **FAIL → reopen Stage 4** (global-deviation omission); record explicit scope modification. For the corrected compact **pure-strategy high-cost theorem**, this report supplies Stage 4A's mathematical arguments and an independent reproduction trail, but no `FORMAL VERIFICATION PASS`, author verification, or novelty certificate. Stage 6 and Stage 7.5A remain next required gates; manuscript claims must remain conditional, and a general unbounded-equilibrium theorem must not be reintroduced by prose.

**Source artifacts:** `code/general_high_cost_stage4a.py`, `results/general_high_cost_stage4a.log`, `results/general_high_cost_numeric_results.json`; manuscript versioning and PR history serve as permanent regression evidence.