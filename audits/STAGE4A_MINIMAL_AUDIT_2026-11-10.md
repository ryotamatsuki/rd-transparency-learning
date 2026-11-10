# Minimal Stage 4A mathematical adversarial audit — 2026-11-10

**Project:** `ryotamatsuki/rd-transparency-learning`  
**Workflow authority:** `research-paper-workflow` v2.9, `GOVERNANCE.md` §2.6–2.9 and `templates/STAGE_04A_MATH_RED_TEAM.md`.  
**Evidence:** `code/stage4a_independent_audit.py`, `results/stage4a_independent_audit.log`, `results/stage4a_independent_numerical_results.json`, and the original `code/finite_cost_proof.py`.  
**Verification actors:** AI-assisted independent algebra plus exact symbolic calculation and numerical stress testing. **Not independent external human review or author certification.**

## 1. Verdict / scope (read before quoting)

**Narrow, model-specific mathematical certificate: PASS for the unique PURE-STRATEGY equilibrium and its stated signs, *conditional on the specified full-coverage price-game primitives and compact investment strategy domains*.** The independent derivation and rational-polynomial certificates support the normalized **finite-cost** result for

\[
 t=\delta=d_0=1,\quad k_s=k_b=4,\quad
 0\le s,b\le 1/2,\quad 0\le\lambda\le1,\quad
 k_\lambda>\frac{4343}{32448}.
\]

**The manuscript-wide Stage 4A is NOT closed.** In particular, the high-cost theorem for arbitrary structural parameters has not undergone the same independent global audit; mixed-strategy PBE uniqueness, full robustness outside the strategy box, and rigorous theorem-level novelty have **not** been certified. Do not turn this narrowly scoped result into an unrestricted SPNE/PBE or welfare claim. The Stage 7.5A formal proof-assistant and generality gates also remain open.

## 2. Frozen game and independent inputs

- Incumbent A at 0, entrant B at 1 on a full-coverage unit Hotelling line; period-1 entrant share \(D=(1-d+p_A-p_B)/2\).
- At Stage 0, A chooses \(s\), B chooses \(b\) simultaneously, both observed. \(d=1+s-b\in[1/2,3/2]\).
- At Stage 1, B selects \(\lambda\) with cost \(k_\lambda\lambda^2/2\), observed by A only in P; in H A uses the correct on-path belief, but cannot condition on a hidden unilateral deviation.
- First-period prices simultaneous; after first-period sales, B relative period-2 quality is \(q=-d+\lambda D\). Period-2 prices simultaneous following public observation of quality.
- Investment costs \(2s^2+2b^2+k_\lambda\lambda^2/2\); zero production costs, myopic consumers, \(\delta=1\), no outside-option use at equilibrium. Choose the common valuation sufficiently high to guarantee the stated coverage against unilateral deviations to losing all customers.

**Input separation:** The independently written script **does not import** the production symbolic proof. It starts from primitive demand and firm cash flows, solves price FOCs afresh, derives an alternative direct-share maximization for B's hidden deviation, constructs Stage-0 conditions, then independently implements rational Bernstein coefficient bounding. This is stronger than rerunning the old script, although it is still computer-assisted and uses related mathematical tools.

## 3. Stage-by-stage candidate-deviation audit

### A. Last period and the first-period price games — conditional globality

Second-period price equilibrium, conditional on quality, is the unique interior Hotelling solution: \(p_{A,2}=1-q/3\), \(p_{B,2}=1+q/3\). The independently reconstructed first-period joint FOC system solves to

\[
D(d,\lambda)=\frac{27-(9+2\lambda)d}{2(27-\lambda^2)},\quad
p_A=2(1-D)-\frac{\lambda(3-q)}{9},\quad
p_B=2D-\frac{\lambda(3+q)}{9}.
\]

**Uniform exact bounds on the whole Stage-0/Stage-1 continuation rectangle:**
\(0<D<1\), \(4/5<p_A<8/5\), \(p_B>0\). Under hidden unilateral learning deviations, keep A's price \(z\in[4/5,8/5]\) fixed, reoptimize B's current share:

\[
D_{\rm dev}=\frac{1-d+z+\lambda(3-d)/9}{4-\lambda^2/9}.
\]

The independent exact certificates verify \(0<D_{\rm dev}<1\), \(p_{B,\rm dev}>0\) for every \(d\in[1/2,3/2]\), \(\lambda\in[0,1]\), \(z\in[4/5,8/5]\). This covers **finite**, not just infinitesimal, hidden learning deviations and resulting B price optimizations.

**Why price corners cannot be better responses:** On the interior segment each price objective is strictly concave in own price (own-price second derivative \(-1+\lambda^2/36<0\)). At a zero-share boundary, entering the market by a sufficiently small price cut yields a strictly positive marginal current-sale return at a positive boundary price; additionally it either increases B's future learning payoff or deprives B of that payoff when A enters. At a full-share boundary, the firm can raise its price while maintaining the whole market, improving current revenue. Along a no-share/full-share plateau prices yield no better payoff than the feasible interior stationary maximum. This uses the verified positive on-path rival prices and full coverage. **No claim is made about price equilibria under arbitrary off-model types, consumer outside options, or alternative demand rules.**

### B. Public learning investment — global deviation exclusion

For every \(d\in[1/2,3/2]\), and every \(0<\lambda\le1\), independent exact Bernstein inequalities give
\[
V_B(d,0)>V_B(d,\lambda).
\]
Since research cost is nonnegative and strictly positive for \(\lambda>0\), the **global** public Stage-1 best response is \(\lambda^P=0\), not just a local FOC solution.

### C. Hidden learning investment — global deviation exclusion

With A's period-1 price \(z\) fixed (unobserved deviation), the derivative of B's optimized gross continuation payoff \(G(d,\lambda;z)\) satisfies the exact uniform bound
\[
G_{\lambda\lambda}(d,\lambda;z)<1/10
\]
throughout the entire rectangle. Because \(k_\lambda>4343/32448>1/10\), B's **net** continuation payoff is strictly concave in \(\lambda\) over the complete feasible interval. Hence any interior first-order solution is the **unique global** learning-investment optimum, ruling out both \(\lambda=0\) and \(\lambda=1\) as profitable deviations whenever the derivative conditions place the solution inside.

At a self-consistent pure equilibrium, the first-order condition is \(k_\lambda=K(d,\lambda)\), where

\[
K(d,\lambda)=\frac{[27-(9+2\lambda)d][54-18d+(9-3d)\lambda-2\lambda^2]}{12\lambda(27-\lambda^2)^2}.
\]
Independent exact rational sign tests show \(K_d<0\), \(K_\lambda<0\) for \(0<\lambda\le1\), \(1/2\le d\le3/2\). Moreover \(K(d,\lambda)\to+\infty\) as \(\lambda\downarrow0\) and \(K(d,1)\le K(1/2,1)=4343/32448\). Therefore each \(d\) and \(k_\lambda\) in the claimed range has exactly one self-consistent interior \(\lambda(d;k_\lambda)\), with a rationally anticipated A price, and no alternative pure learning-investment continuation.

### D. Stage-0 finite deviations and globality

Let \(T_A(d;k)\) and \(T_B(d;k)\) denote operating continuation values for the unique hidden Stage-1/price continuation, with B's hidden learning investment cost included in \(T_B\) but neither firm's Stage-0 quality cost included. Holding \(k\) fixed, the exact derivative bounds independently verified over all \(d\in[1/2,3/2]\) and implied \(\lambda(d;k)\in(0,1)\) are

\[
0<T_A'<2,\qquad -2<T_B'<0,\qquad T_A''<2,\quad T_B''<2.
\]

Each firm's own Stage-0 objective is **globally strictly concave** in its own investment because its second derivative is \(T_i''-4<-2\); the derivative signs imply any best response is interior in \((0,1/2)\). Thus each firm has exactly one global best response, including against finite deviations to either boundary.

**Separate alternative-equilibrium proof:** If \(d=1+s-b\), the two Stage-0 FOCs yield

\[
 s=T_A'(d;k)/4,\qquad b=-T_B'(d;k)/4,
\]
\[
 H_k(d):=d-1-[T_A'(d;k)+T_B'(d;k)]/4=0.
\]

By the curvature bounds, \(H_k'(d)=1-[T_A''(d;k)+T_B''(d;k)]/4>0\) on the full domain. From the first-derivative bounds, \(H_k(1/2)<0<H_k(3/2)\). By continuity and strict monotonicity, there is **exactly one root**, therefore exactly one **pure** Stage-0 equilibrium under the fixed admissible continuation. This is **not** merely a numerical search for a second equilibrium; it is an analytic exclusion within the stated class.

The public Stage-0 game has \(\lambda=0\) at every off-path \(d\), quadratic own-action curvature \(c-4<0\) and the unique baseline \(s^P=11/48\), \(b^P=5/48\). No alternate pure boundary profile exists in either regime under the given assumptions.

### E. Strict comparative sign proof on the actual equilibrium branch

Define the scalar implicit Stage-0 condition \(F(d,\lambda)=4(d-1)-T_A'(d,\lambda)-T_B'(d,\lambda)\), where \(T_i'\) are derivatives **along fixed-\(k\) continuation levels**. For \(0<\lambda\le1/2\), a second independent exact polynomial certificate gives

\[
F(9/8+\lambda/8,\lambda)<0< F(9/8+\lambda/5,\lambda),
\]
\[
\partial_d F>0,\quad \partial_\lambda F<0
\]
inside the wedge, where **the partial derivatives are taken at fixed \(\lambda\) and fixed \(d\), respectively; these are not the fixed-\(k\) total derivatives in Section D**. Consequently the root \(d(\lambda)\) is unique and increasing in \(\lambda\). Along this root \(k=K(d(\lambda),\lambda)\) strictly decreases. At \(\lambda=1/2\),
\[
K(d(1/2),1/2)<K(19/16,1/2)=134915/1099104<4343/32448.
\]
Thus every \(k>4343/32448\) corresponds to the unique root with \(0<\lambda<1/2\).

Reconstructing net profits and welfare **from original payoff/consumer-surplus primitives rather than importing the production proof**, exact rational Bernstein certificates are strictly positive across the entire wedge for
\[
s^H-11/48,\quad5/48-b^H,\quad
2057/1152-\Pi_A^H,\quad425/1152-\Pi_B^H,\quad
W^H+1085/1152,
\]
as well as \(5/16-D_1^H>0\) and \(D_2^H-5/16>0\). These facts establish the full sign comparisons for the **specified finite-cost pure-equilibrium family**, not just the example \(k=0.3\).

## 4. Numerical attack separate from exact inequalities

An independent `scipy.optimize`/direct cashflow evaluator checked seven values spanning the threshold-near case to very high costs:

| Cost coefficient \(k_\lambda\) | Hidden \(\lambda\) | Alternate pure equilibria found in bracket search | Max beneficial finite unilateral gain |
|---:|---:|---:|---:|
| 0.134 | 0.453306 | 0 | numerical precision |
| 0.15 | 0.408471 | 0 | numerical precision |
| 0.30 | 0.211102 | 0 | numerical precision |
| 1 | 0.064605 | 0 | numerical precision |
| 3 | 0.021647 | 0 | numerical precision |
| 20 | 0.003254 | 0 | numerical precision |
| 100 | 0.000651 | 0 | numerical precision |

For each of the seven cases the independently reconstructed scalar equilibrium equation had one sign-crossing bracket on a 251-point mesh; the direct payoffs were checked via global 1D boundary-aware multi-start optimization for (a) A's s, (b) B's b, and (c) B's hidden \(\lambda\), with A's first-period price held fixed in case (c). All observed gains were of order machine round-off, at most around \(10^{-15}\). The code uses dense grids plus logarithmic near-zero probes, crucial when \(k=100\) and the interior investment is smaller than a uniform grid cell. **This is an adversarial numerical regression test, not proof of the uniform theorem.** The exact polynomial/monotonicity steps above provide the uniform algebraic part.

## 5. Unresolved threats / evidence maturity

| Issue | Result | Impact on claim |
|---|---|---|
| Price and customer-demand corners against an on-path rival price | **Addressed** in Section 3A for the fixed full-coverage model; a concise human-readable appendix proof should be retained | No broader claim about every price game outside the frozen primitives |
| Hidden learning finite and endpoint deviations | **Exact uniform concavity + fixed-A-price checks passed** | Supports unique pure hidden Stage-1 optimum |
| Stage-0 full-interval finite deviations | **Exact strict concavity/interior checks passed** | Supports pure global best responses |
| Other pure Stage-0 equilibria | **Analytically excluded** by strict monotonicity of \(H_k\) | Supports **unique pure-strategy** normalized equilibrium |
| Uniform private/social sign comparisons | **Independent exact polynomial certificates passed**, in the specified wedge | Supports normalized finite-cost comparisons |
| Mixed strategies and full arbitrary perfect Bayesian equilibrium set | **NOT TESTED** | Never claim that *all* equilibria are unique or that every PBE has identical welfare |
| Unbounded/expanded R&D strategy domains or more general structural parameters | **NOT CERTIFIED** | Original general high-cost theorem remains an unresolved separate Stage 4A claim |
| Independent human proof audit / proof assistant | **NOT TESTED** | Mathematical computer-assisted results are not external-author or formal certification |
| Novelty vs parent learning/R&D-disclosure theorems | **NOT IN SCOPE / Stage 6** | No priority claim follows from Stage 4A |

**Warning against a common fallacy:** certifying derivatives along a fixed-\(k\) continuation curve **does not** certify partial derivatives of the two-variable equation \(F(d,\lambda)\) at a fixed \(\lambda\). The two distinct derivatives are independently checked in the audit script. Likewise checking a candidate's lack of profitable deviation is not a proof of unique equilibrium; uniqueness is independently established by the scalar monotonicity argument.

## 6. Exact Stage 4A status and next research action

**Scoped certificate:** `PASS — NORMALIZED PURE-STRATEGY FINITE-COST THEOREM` conditional on the frozen primitive price game and compact investment strategy sets, with rational symbolic assistance and a separately written payoff optimizer. The proof does not rely on one selected numerical parameter vector.

**Project-level Stage 4A:** `UNRESOLVED / NOT FULLY PASSED`: the manuscript additionally states a general high-cost theorem outside the normalized parameter slice, which remains to be audited. Do not issue the formal workflow-wide `GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS` yet.

**Submission-oriented choice:** Either (a) conduct a similarly bounded adversarial audit of the manuscript's general theorem, or (b) **narrow the paper's theorem statement to the certified finite-cost normalized family** and describe more general conclusions as conjectural/partial results until proven. Do not broaden the model to escape the audit.

**Reproducibility:** `python code/stage4a_independent_audit.py` and `python code/finite_cost_proof.py`. Both output detailed exact algebraic checkpoints. The independent script emits a JSON file specified by the `RD_STAGE4A_OUTPUT` environment variable (default: `stage4a_independent_numerical_results.json`).