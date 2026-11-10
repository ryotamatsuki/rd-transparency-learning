# Proposed theorem architecture and economic interpretation
**Working outline for submission, 2026-11-10. Not a manuscript or a peer-reviewed proof.**

## Editorial decision / 論文の主張を一文で

**日本語:** 販売経験が翌期の技術力を改善する産業では、新規企業の学習能力投資の公開が既存企業の先制的価格反応を誘発し、新規企業の研究開発を「将来の学習」から「即時品質」へ転換させる。公開は両社の私的利潤を増加させても、将来の技術的競争力および社会厚生を低下させ得る。

**English (claim, not a priority statement):** When an entrant's future quality depends on its current customer base, observability of learning-capability investment induces defensive pricing by the incumbent and redirects the entrant's R&D toward immediate quality. This may benefit both firms while reducing future technological performance and social welfare.

**Novelty restraint:** disclosure enhancing joint profits and reducing welfare, disclosure discouraging R&D, and short-term R&D bias under disclosure have precedents. The potential contribution is the **specific causal channel and endogenous two-firm R&D-composition adjustment**, not any individual sign alone.

## What belongs in the main text

Recommended order: **Lemma 1 → Lemma 2 → Proposition 1 → Proposition 2 → Theorem 1 → Corollary 1 → Corollary 2**, with an optional **Lemma 3 (feedback removal)** placed after Lemma 2 to identify the mechanism. The supplementary counterfactual is an **illustration**, not a theorem.

Notation: incumbent A chooses persistent-quality R&D \(s\); entrant B chooses immediately effective, persistent quality R&D \(b\) and learning capability \(\lambda\). Relative quality \(-d\), \(d=d_0+s-b\); B's period-2 relative quality \(-d+\lambda D_1\); learning is tied to period-1 realized entrant share \(D_1\). Superscripts P=public, H=hidden. Private profits \(\Pi_A,\Pi_B\) are **net of R&D costs**, and welfare \(W=CS+\Pi_A+\Pi_B\).

### Lemma 1 — Dynamic Bertrand pricing (technical base)
**Proposed statement:** Conditional on \(d,\lambda\) and interior positive sales, the unique period-2 Hotelling price equilibrium is
\[
p_{A,2}=t-q/3,\quad p_{B,2}=t+q/3,\quad
D_2=(3t+q)/(6t),\qquad q=-d+\lambda D_1.
\]
When the period-1 price game internalizes how sales experience improves future quality, its (interior) equilibrium has
\[
D_1(d,\lambda)=\frac{27t^2-9dt-2\delta d\lambda}{2(27t^2-\delta\lambda^2)}
\]
with price FOCs recorded in \`docs/model.md\`.

**Intuition:** A period-1 sale has a *dynamic value* because it changes B's future relative quality. Prices are thus not purely static markups: defending customers now can restrict a rival's future learning.

**Main text:** concise derivation and single expression for \(D_1\); proof and curvature/interior admissibility in Appendix A.

**Status:** analytical formula available. Off-path full-game admissibility needs independent audit.

### Lemma 2 — Learning-investment observability wedge (mechanism)
**Proposed statement:** At \(\lambda=0\), if \(0<d<3t\), the entrant's gross marginal incentive is
\[
\left.\frac{dV_B^{P}}{d\lambda}\right|_{0}
=-\frac{2\delta d(3t-d)}{81t^2}<0,
\qquad
\left.\frac{\partial V_B^{H}}{\partial\lambda}\right|_{0}
=\frac{\delta(3t-d)^2}{54t^2}>0,
\]
where in H the incumbent cannot condition its price on B's *unobserved unilateral deviation*, while B may optimally reprice. The incumbent's public conditional price reaction is
\[
\left.\frac{\partial p_{A,1}^{P}}{\partial\lambda}\right|_0
=-\frac{\delta(9t+d)}{27t}<0.
\]

**Intuition (central):** Publicly visible learning potential gives A a reason to cut its **current price in response to a higher disclosed \(\lambda\)**, reducing B's current customer base and the future value of learning. Under H, A still rationally anticipates equilibrium \(\lambda\) but cannot react to an unobserved change. This is an *incentive effect of contingent strategies*, not ignorance of the equilibrium investment.

**Caution:** Do **not** write that public equilibrium prices are necessarily lower than hidden equilibrium prices: the negative derivative compares *counterfactual \(\lambda\)-conditional responses*, not the two equilibrium levels.

**Main text:** one sign comparison, short intuition paragraph; full envelope calculation in Appendix A.

**Status:** closed-form analytical mechanism; not novel by itself.

### Optional Lemma 3 — Sales-experience feedback is necessary for the observability channel (identification/ablation)
**Proposed statement:** Holding the timing, observability, technology knowledge and unique equilibrium assumptions fixed, replace \(q_2=-d+\lambda D_1\) by \(q_2=-d+\lambda\). Then first-period pricing no longer affects second-period quality; its price equilibrium is independent of \(\lambda\), so the Stage-1 learning investment problem is identical under P and H. With unique equilibria, \(s^P=s^H,\;b^P=b^H,\;\lambda^P=\lambda^H\), hence equal profits and welfare.

**Intuition:** Investing in future quality alone does not generate the concealment effect. **Current market share must affect future learning** so the incumbent can strategically neutralize an observed learning investment with current prices.

**Role:** mechanism-removal test directly useful against the "combination of familiar results" referee critique.

**Status:** analytical argument, *needs a full formal proof* including assumptions and off-path strategies before promotion into the numbered results. If verified, place immediately after Lemma 2 or in a dedicated Mechanism subsection.

### Proposition 1 — Hidden learning investment / public suppression
**Proposed statement:** In an admissible equilibrium region with \(d>0\), sufficiently high \(k_\lambda\) yields
\[
\lambda^P=0<\lambda^H.
\]
For the normalized compact-domain benchmark \((t,\delta,d_0,k_s,k_b)=(1,1,1,4,4)\), the existing exact-algebra work supports \(\lambda^P=0<\lambda^H\) throughout its stated global-unicity sufficient region.

**Intuition:** Under public observability, A's ability to price against B's enhanced learning turns an otherwise profitable investment into an unattractive one. Concealment restores the marginal return to learning. The result concerns *investment incentives*, not successful secrecy about equilibrium levels.

**Scope:** never claim that public learning investment is zero for every feasible parameter configuration. The high-cost qualifier, compact strategy sets, and equilibrium solution conditions matter.

**Main text:** sign result, one paragraph; algebraic global check in Appendix B.

### Proposition 2 — Endogenous direction of R&D (first substantive contribution)
**Proposed statement:** Under Stage-0 response stability (e.g., \(k_s>c,k_b>c,\Delta>0\), with \(c=(1+\delta)/(9t)\), \(\Delta=k_sk_b-c(k_s+k_b)\)), \(0<d_*<3t\), and sufficiently high \(k_\lambda\), the change from P to H satisfies
\[
s^H>s^P,\qquad b^H<b^P,\qquad \lambda^H>\lambda^P.
\]
Equivalently, disclosure raises B's immediately effective quality investment but lowers future learning-capability investment; it also lowers A's persistent quality investment.

**Intuition:** If hidden learning creates a stronger future B, the two firms' quality choices adjust to the resulting competitive environment. B reduces upfront quality spending and develops future capability; A strengthens its own lasting quality. Disclosure tilts B toward *immediate* quality even though that quality persists into period 2; it is **not** a pure one-period investment. With independent quadratic costs, it is a **composition shift**, not literal division of a fixed budget.

**Scope:** Do not attribute A's \(s\) change to a simple weakening of defensive behavior: its *price response* and *technology investment response* are distinct strategic choices.

**Main text:** a sign table and a 2-paragraph economic explanation; comparative-statics Jacobian in Appendix B.

### Theorem 1 — Firm-preferred disclosure, socially preferred concealment (headline result)
**Proposed statement:** Under the stability/interiority/high-learning-cost assumptions of Proposition 2, a sufficiently pronounced baseline incumbent quality advantage \(t\le d_*<3t\) and a further strict condition controlling how much B cuts immediate quality under concealment (the incumbent-profit inequality), there is a nonempty parameter region where
\[
\Pi_A^P>\Pi_A^H,\quad
\Pi_B^P>\Pi_B^H,\quad
W^H>W^P.
\]
Together with Proposition 2, this describes disclosure-induced reorientation from learning capacity to immediate quality despite a *private profit ranking opposite to the welfare ranking*.

**Intuition:** Concealment lets B invest in learning, provoking more competitive product-market outcomes; A also raises persistent quality investment. Both firms may individually prefer the less aggressive learning environment under disclosure (higher profits), while consumers gain sufficiently from concealment's prices, investment-induced quality and future learning to outweigh these profit differences. In the stated sufficient region the entrant begins with a meaningful quality disadvantage: \(t\le d_*<3t\) implies \(0<D_B^*\le1/3\) at zero learning. This is a sufficient, not a necessary, condition.

**Precision about welfare accounting:**
\[
W^H-W^P=(CS^H-CS^P)
  -[(\Pi_A^P-\Pi_A^H)+(\Pi_B^P-\Pi_B^H)].
\]
Welfare conflict needs a consumer-surplus gain under H that exceeds the firms' combined public-profit gains. It does **not** imply endogenous voluntary disclosure; the information regimes are compared exogenously.

**Scope:** General parameters: a sufficiently-large-\(k_\lambda\) *existence/sufficient-conditions* theorem. Fixed normalized case: a **separately certified finite-cost statement**, not a universal threshold. Put full conditions in theorem statement, not informal prose.

**Main text:** central boxed result + discussion. Appendix C for proofs.

### Corollary 1 — Constructive finite-cost realization (separate nonasymptotic proof required)
**Proposed statement:** For \(t=\delta=d_0=1,\;k_s=k_b=4\), compact strategies \(s,b\in[0,1/2]\), \(\lambda\in[0,1]\), the symbolic certificate records the **sufficient** bound
\[
k_\lambda>\frac{4343}{32448}\simeq0.133845
\]
under which the main sign comparisons and proposed global uniqueness hold. The \(\lambda\)-parametrized equilibrium branch has algebraically certified comparison signs further down to \(k_\lambda\ge0.1\), but **global equilibrium uniqueness is not certified there**.

**Intuition:** The result is not confined to the infinitesimal-learning limit; it persists at finite R&D cost, including the original \(k_\lambda=0.3\) illustration. The numerical constant is a *normalization-dependent sufficient proof bound*, **not a universal economic phase transition**.

**Presentation caveat:** Calling this a corollary is acceptable only if a self-contained specialized proof is appended; it is *not obtained merely by substituting numerical parameters into the general asymptotic theorem*. If preferred by the journal, label it "Proposition 3 (Nonasymptotic benchmark)" for logical clarity.

**Status:** Exact rational Bernstein checks pass in \`code/finite_cost_proof.py\`; independent proof audit still pending.

### Corollary 2 — Intertemporal market-share reversal and future quality
**Proposed statement, normalized finite-cost sufficient region only:**
\[
D_1^H<D_1^P=D_2^P<D_2^H,\qquad q_{B,2}^H-q_{A,2}^H>q_{B,2}^P-q_{A,2}^P.
\]
The certificate additionally shows both periods' *gross market surplus* is higher under H in this region.

**Intuition:** B sacrifices some **current** market share under concealment yet obtains a **larger future** share because its learning capability strengthens future quality. This is an observable prediction of the technical channel, not just a welfare accounting identity. (The relative-quality claim is not necessarily an absolute B quality level comparison in another model.)

**Scope:** Do not generalize it to every parameter satisfying the broad high-cost theorem unless separately proven. The full two-period model establishes no permanent/infinite-horizon "technological replacement delay."

**Main text:** an annotated two-period table/figure plus statement; algebraic proof in appendix.

## Consumer-surplus consequence — state as a short sentence, not a third formal corollary

Theorem 1 implies:
\[
CS^H-CS^P>
(\Pi_A^P-\Pi_A^H)+(\Pi_B^P-\Pi_B^H)>0.
\]
It is an accounting implication, not an independently novel result. Benchmark: H minus P consumer surplus \(+0.121133858\); combined corporate net-profit change \(-0.093571178\); welfare \(+0.027562680\) (common base utility canceled). This highlights why both firms can privately prefer P while society prefers H.

## Numerical illustration — investment composition as an amplifier, not a prerequisite

At benchmark \(k_\lambda=0.3\), public welfare approx \(-0.941840\) and hidden full equilibrium welfare approx \(-0.914278\). Prior fixed-\(s,b\) counterfactual hidden calculation reported \(-0.929585\) (NOT a full game equilibrium). **Independent code replication pending**.

Interpretation: the welfare conflict appears even if the immediate-quality R&D levels are fixed; allowing both firms' R&D to adjust makes the welfare gap greater in this example. The portfolio change is **not a necessary condition** for the basic profit/welfare reversal. Do not promote an unverified counterfactual to a theorem or claim a general amplification inequality without a new proof.

## Suggested manuscript section and proof layout

| Section | Main-text content | Appendix |
|---|---|---|
| 1 Introduction | Research question; exactly what is/not new; mechanism graphic | — |
| 2 Related Literature | R&D disclosure and Bertrand, dynamic LBD pricing, R&D composition; exact proposition distinctions | Citation/theorem crosswalk as needed |
| 3 Model | 2 periods, consumers, investments, timing, observability, welfare | Assumptions/checks |
| 4 Pricing and learning incentives | Lemma 1, Lemma 2, optional Lemma 3 | A: price games, hidden deviation, ablation |
| 5 R&D equilibrium | Proposition 1, Proposition 2 | B: global/implicit response, high-cost expansion |
| 6 Profits and welfare | Theorem 1, Corollary 1 | C: welfare identities, strict conditions; D: finite-cost symbolic certificate |
| 7 Mechanism and predictions | Corollary 2, consumer-surplus implication, numerical/counterfactual illustration | Calibration calculations |
| 8 Conclusion | Conditional insight, voluntary disclosure not analyzed, 2 periods only | — |

## How to write economic intuition after each statement

Use **three consistent questions** for each result:
1. *What changes strategically?* (which player's action/contingent response changes)
2. *Why is the sign surprising?* (which conventional intuition fails, which cross-period payoff term dominates)
3. *What assumption sustains it, and when may it disappear?* (market-share-driven learning, quality-gap/stability conditions, high learning-cost, observed vs hidden deviations).

Avoid restating the inequalities as if they were explanations. Avoid "information disclosure harms innovation generally" language. Never conflate P/H exogenous-regime comparison with firms' voluntary choice of whether to disclose.

## Proof/novelty audit gate before locking proposition numbering

- Independently audit **global** best responses and the Bernstein certification, including all off-path price histories.
- Finalize the exact A-profit sufficient condition and correctly specify the stage-0 domain where implicit smooth equilibrium applies.
- Establish Lemma 3's no-feedback invariance formally; otherwise demote to a discussion remark.
- Confirm normalized Corollary 1 is presented with its *own* finite-cost proof, not as a direct implication of an asymptotic theorem.
- Read the specific corresponding propositions in Baik & Kim (2020), Huang et al. (2023), Kim & Poggi (2026 revision), Besanko et al. (2014), Jiang & Xiong (2025).
- Do **not** add a voluntary-disclosure equilibrium, fixed-budget R&D allocation, or forward-looking consumers solely to increase proposition count.

**Editorial recommendation:** One substantive headline theorem, two substantive R&D propositions, two well-scoped corollaries, and only the lemmas needed for pricing/information identification. This is enough for a focused field-journal submission if the independent proof and novelty audits succeed.
