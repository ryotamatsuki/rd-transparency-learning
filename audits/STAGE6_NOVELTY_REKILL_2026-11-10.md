# Stage 6 — Novelty re-kill / 既存定理への吸収可能性監査
**As-of:** 2026-11-10 (Asia/Tokyo)  
**Repository:** \`ryotamatsuki/rd-transparency-learning\`, review branch \`paper/draft-v0-1-audit\`  
**Workflow authority:** \`ryotamatsuki/research-paper-workflow\` v2.9, \`THEORY_PAPER_RESEARCH_PIPELINE.md\`, Stage 6; \`GOVERNANCE.md\` sections 2.12 and 2.12A.  
**Inputs:** \`audits/GENERAL_HIGH_COST_STAGE4A_2026-11-10.md\`, \`audits/STAGE4A_MINIMAL_AUDIT_2026-11-10.md\`, \`docs/propositions.md\`, \`paper/main.tex\`, \`literature/related_literature_master.md\`, and earlier \`literature/novelty_matrix.md\`.

## 0. Executive conclusion and separate status axes

**Stage 6 provisional verdict: \`CONDITIONAL GO — THEOREM-NOVELTY NOT YET CERTIFIED\`.**

- **Mathematical status:** the revised general high-\(k_\lambda\) model has computer-assisted, independently reconstructed arguments for a unique **pure** equilibrium **only on explicit compact action sets**, with \(0<d_0-\bar b<d_0+\bar s<3t\) and sufficiently small \(\bar\lambda\). The original *unbounded* general equilibrium theorem was **falsified** by a profitable monopoly-region deviation. The normalized finite-cost result is separate and has its own verified (computer-assisted) sufficient threshold. Mixed-strategy PBE and universal \(K_0\) are not claimed.
- **Novelty status:** **UNRESOLVED**, not \`EVIDENCE-SCOPED NOVELTY CERTIFIED\`. The public-vs-hidden marginal-incentive wedge is a **standard strategic-investment envelope/reaction term**. The pure sign pattern \(\Pi_A^P>\Pi_A^H,\Pi_B^P>\Pi_B^H,W^P<W^H\) is **already present** in Baik & Kim (2020, Section 7.3), and the general idea of short-run R&D allocation under disclosure or of sales-driven quality improvement is known. A model-specific **joint** result remains a plausible contribution but not an established priority claim.
- **Exactly one decisive remaining Stage-6 blocker:** close **full-theorem parent-class absorption** for the *joint* outcome (sales-experience-dependent **chosen learning coefficient**, exogenous observability, endogenous immediate-quality choices for B and persistent-quality choice for A, conditional profit/welfare and intertemporal-share comparisons). In particular a version-complete comparison with the foundational dynamic-learning parent class (Cabral & Riordan 1994, for which only the accessible abstract has been checked) and the general strategic-commitment parent theorems is needed before claiming nonabsorption. Do not replace that with absence of identical keywords/formulas.

**Decisions already made:** do **not** restore the unbounded theorem; do **not** add a disclosure-choice, patent, asymmetric private-type, fixed-budget, or more-than-two-period extension to make the paper look novel. Keep a theory-first, six-section, conditional manuscript.

## 1. The actual certified object (not an application label)

Two-period complete-coverage, fixed-location, differentiated Bertrand market with no production cost and uniform consumers. Let \(d=d_0+s-b\), B's period-1 share be \(D_1=(t-d+p_{A1}-p_{B1})/(2t)\), and B's next-period relative quality be
\[
q_2=-d+\lambda D_1 .
\]
A chooses persistent-quality investment \(s\); B chooses separately paid-for persistent *immediate* quality investment \(b\) and learning efficiency \(\lambda\); quadratic costs. P reveals \(\lambda\) to A before first-period pricing; H hides realized \(\lambda\), so after B's **unobserved unilateral deviation** A's first-period price cannot condition on it, while B's own price may adjust. Period-2 relative quality is observed.

### Application-neutral mathematical form

A parameter-controlled two-player smooth dynamic game with an **endogenous interaction/experience operator**
\[
Q_2(\boldsymbol{a},\boldsymbol{x})=Q_0(\boldsymbol{a})+
\lambda \,D_B(\boldsymbol{p};\boldsymbol{a}),\quad
\boldsymbol{a}=(s,b),\quad
\boldsymbol{p}=(p_A,p_B).
\]
Continuation payoffs:
\[
U_A=p_A(1-D_B)+\delta\Phi_A(Q_2)-\tfrac12 k_s s^2,\quad
U_B=p_B D_B+\delta\Phi_B(Q_2)-\tfrac12 k_b b^2-\tfrac12 k_\lambda\lambda^2,
\]
where \(\Phi_A(q)=(3t-q)^2/(18t)\), \(\Phi_B(q)=(3t+q)^2/(18t)\), on the strictly interior price domain. Player B controls the coefficient \(\lambda\) of the **own action-dependent experience stock**. Information regimes change A's *contingent price strategy space*, not a primitive market demand intercept or the cost of research.

Plausible standard parent classes, searched both with and without "R&D"/"learning" labels:
1. Observable strategic commitment in oligopoly with postinvestment pricing (Fudenberg & Tirole 1984; Bulow, Geanakoplos & Klemperer 1985).
2. Multi-stage experience-state Bertrand competition / predation / learning-by-doing (Spence 1981; Cabral & Riordan 1994; Besanko et al. 2014, 2019).
3. Dynamic competition over output-based autonomous learning and chosen quality-control inputs (Kogan & El Ouardighi 2019).
4. Information-sensitive R&D intensity and welfare in differentiated Bertrand (Baik & Kim 2020, 2025; Sengupta 2016; Jiang & Xiong 2025).
5. Investable learning capability and composition of innovation (Cohen & Levinthal 1989/1994; Lin & Zhou 2013; Kim & Poggi 2026; Huang et al. 2023; Chen, Liang & Petrov 2024).

## 2. Explicit generic-theorem absorption: the marginal-incentive wedge is NOT novel

Write \(U_B(p_B,p_A,\lambda)\) for B's two-period gross continuation payoff after solving period-2 prices. In the public game the incumbent plays \(p_A^*(\lambda)\), whereas under an unobserved B deviation from \(\lambda_0\), A keeps \(p_A^*(\lambda_0)\) fixed. At a common baseline \(\lambda_0=0\), the envelope theorem gives **exactly**
\[
\left.{dV_B^P\over d\lambda}
-{\partial V_B^H\over\partial\lambda}\right|_0
=
\left.{\partial U_B\over\partial p_A}\right|_0
\left.{dp_A^*\over d\lambda}\right|_0 .
\]
For our Hotelling model:
\[
\left.{\partial U_B\over\partial p_A}\right|_0
={3t-d\over 6t},\quad
\left.{dp_A^*\over d\lambda}\right|_0
=-{\delta(9t+d)\over27t},
\]
hence
\[
{dV_B^P\over d\lambda}
-{\partial V_B^H\over\partial\lambda}
=-{\delta(3t-d)(9t+d)\over162t^2}<0
\quad (0<d<3t).
\]
**Direct canonical absorption:** This product is the familiar strategic response/commitment channel. The economic content of a contingent investment changing the rival's subsequent action is **not new**, even though these particular Hotelling polynomial coefficients are newly derived for the present game. **Priority verdict on the generic wedge: ABSORBED; author should never claim it as a new general result.** Algebra independently checked by \`code/stage6_strategic_commitment_identity.py\` (the tool only proves the encoded identity, not any journal priority claim).

**Controlled ablation:** Replacing \(Q_2=-d+\lambda D_1\) by \(Q_2=-d+\lambda\) removes the dependence of later quality on current prices. The first-period price FOCs then contain no \(\lambda\), so (given period-2 observability and unique continuation equilibria) the public/hidden investment objectives coincide. This **pinpoints the ingredient needed in our model**, but is not an independent broad novelty theorem and cannot alone defeat the generic strategic-investment objection.

## 3. Theorem-absorption map (source/version/reading depth)

Classification rule:
- \`DIRECTLY ABSORBED\`: our claim is already given by or immediately follows from the cited established result under a defensible mapping.
- \`PARTIALLY ABSORBED\`: a component or the same sign pattern is established, but the full-game mapping does not preserve the prior game's own strategies, timing, technology and welfare.
- \`NOT ABSORBED IN INSPECTED SCOPE\`: exact source sections and theorem objects compared; no direct specialization established **within those inspected scopes**, not universal nonexistence.
- \`UNRESOLVED\`: a plausible full parent theorem has not been exhaustively mapped from the necessary full text.

### P1: disclosure reduces learning investment; strategic-response wedge

| Parent result | Mathematical attempted mapping | Assessment |
|---|---|---|
| Fudenberg & Tirole (1984), strategic-commitment/fat-cat-puppy-dog framework. **Bibliographic record/secondary theory descriptions only** | Initial investment \(x=\lambda\); follower's response \(y=p_A\); entrant's payoff \(U_B(x,y)\). Chain-rule strategic term \(U_{By}y'(x)\). | **DIRECTLY ABSORBED** as a *generic strategic-reaction effect*. Parent theorem's full hypotheses not audited; no claim its original printed formula equals our one. |
| Bulow, Geanakoplos & Klemperer (1985), strategic complements/substitutes. **Stanford/Yale working-paper abstract and publisher record checked** | Observable commitment's induced response of second decision \(p_A\) to investment \(\lambda\); Bertrand price complementarity. | **PARTIALLY ABSORBED**. General topology is known, but exact \(\lambda D_1\) marginal and full dynamic technology are not shown in accessible abstract. |
| Baik & Kim (2020), differentiated Bertrand Section 7.3, **author PDF pp.30–31 actually inspected** | Their \(x_i\) maps to observable R&D commitment. But \(c_i=c_M-\delta x_i\) is contemporaneous deterministic marginal cost, not investable coefficient multiplying demand-based future quality. | **PARTIALLY ABSORBED** (direction of marginal investment under P vs H is known; full game not a nested specialization). |

### P2: B reallocates from learning to immediate quality while A increases persistent quality under concealment

| Parent | Mathematical attempted mapping | Assessment |
|---|---|---|
| Cohen & Levinthal (1989, 1994), investable absorptive capacity; **publisher abstracts, not full proposition audit** | \(\lambda\) maps conceptually to learning ability, but their capacity absorbs external knowledge; not a controllable coefficient times sales share of a period-1 differentiated-price market. | **PARTIALLY ABSORBED** (learning ability as a choice is known); full theorem-level verdict **UNRESOLVED** without full text. |
| Lin & Zhou (2013), multiproduct R&D portfolios; **publisher abstract** | Map \(b,\lambda\) onto two R&D product lines, but this loses the endogenously acquired cross-period customer stock and B's disclosed response threat; mapping changes the technology. | **PARTIALLY ABSORBED**: endogenous portfolio change is known. |
| Kogan & El Ouardighi (2019), *Autonomous and induced production learning under price and quality competition*, *Applied Mathematical Modelling* 67, 74–84, DOI 10.1016/j.apm.2018.10.018. **Publisher full HTML model and listed propositions inspected** | Their state evolves as \(\dot Y_i=\rho q_i(p_1,p_2)+\vartheta u_i\) with **fixed** learning coefficients \(\rho,\vartheta\), chosen control \(u_i\), continuous-time Bertrand price decisions and differences between commitment vs contingent **observability of the quality state**. To obtain our game one would have to add a choice of \(\rho=\lambda\) before pricing, hide or reveal that choice to the rival, collapse time to two periods, add separate persistent \(b,s\) and compare welfare. Those are **new strategy/information primitives**, not parameter restrictions. | **NOT ABSORBED IN INSPECTED SCOPE** for the joint P2 theorem; **very close component overlap** (do not call price + quality investment + sales learning new). |
| Kim & Poggi (2026 September revised), *Strategic Concealment in Innovation Races*, CRC TR 224 DP648 v2. **Full 68-page revised paper opened; Sections 2–5 and Propositions 1–3/Theorem 1 examined** | Their unit resource share \(\sigma_i\) splits innovation-race effort between development and breakthrough research; private vs public **research progress** induces fallback/continued research; patents and licensing transmit technological knowledge. No simultaneous consumer-price competition, chosen \(\lambda\) multiplier on own current customers, or Hotelling consumer surplus objective. | **NOT ABSORBED IN INSPECTED SCOPE** for the precise joint P2 result; research-direction change under secrecy is **PARTIALLY ABSORBED**. Critically, this is the **September 2026 revised PDF**, not the May 2025 author preprint. |

### T1: both firms prefer disclosure, society prefers secrecy, and triple investment changes

| Parent | Attempted mapping | Assessment |
|---|---|---|
| Baik & Kim (2020), **full Section 7.3** | Their public and hidden investment/price/profit/consumer-surplus/welfare comparisons show \(x_i^P<x_i^H\), \(\Pi_i^P>\Pi_i^H\), \(CS^P<CS^H\) and \(W^P<W^H\) **when product substitutability \(\theta\le 0.52\)**; \(W^P>W^H\) for \(\theta\ge0.53\). One R&D type per firm and no \(\lambda D_1\). | **DIRECTLY ABSORBED as qualitative profit/welfare sign combination**, not as our joint equilibrium theorem. Never label that sign configuration an innovation. |
| Jiang & Xiong (2025), endogenous cost-information disclosure, **university/publisher abstract checked** | Publicly disclose cost produced by R&D to soften Bertrand investment and increase firm profit; cost signal is a chosen information object. To map, add dynamic customer state and chosen learning coefficient, change welfare. | **PARTIALLY ABSORBED** as privately preferred disclosure and R&D moderation; full welfare scope not assumed. |
| Cabral & Riordan (1994), learning curve and predatory pricing in differentiated Bertrand, **journal/RePEc abstract only; full text not obtained** | Their learning stock is accumulated output; pricing dynamically changes future costs/market dominance; no verified chosen \(\lambda\) disclosure or dual R&D input. But a broad dynamic learning theorem **might** imply an investment response after treating learning efficiency as a parameter/commitment instrument. | **UNRESOLVED, priority remaining full-paper parent class**. Cannot infer no stronger general theorem from abstract absence. |
| Besanko, Doraszelski & Kryukov (2014, 2019), dynamic price as investment, **AER abstracts/article descriptions** | Their experience-dependent state and predatory current price map to \(D_1\)-driven future quality, but the model would need an explicitly chosen publicly disclosed/hidden learning coefficient and s,b to establish full triple-and-welfare ranking. | **PARTIALLY ABSORBED**; strategic price defense and dynamic welfare wedges are preexisting. |
| Fudenberg/Tirole/Bulow general strategic investment parent | Generic \(U_{By}y'(x)\) explains P1. It has **no model-free sign theorem** implying our specific pair of endogenous Stage-0 quality adjustments and the \(\lambda D_1\)-dependent total-welfare ranking without additional payoff restrictions/derivations. | **DIRECT generic-wedge absorption; T1 full signs not established as a short corollary from checked summaries**. Need full-theorem review before claiming certified nonabsorption. |

### Other implications

| Candidate | Source risk | Assessment |
|---|---|---|
| B's first-period share falls under H but second-period share/relative B quality rises in the **normalized finite-cost region** | Cabral & Riordan, Besanko et al., Kogan & El Ouardighi may generate catch-up after learning | **NOT ABSORBED IN INSPECTED SCOPE**, but **model-specific and untested as general law**. Keep as a conditional secondary finding; not standalone first-ever claim. |
| Fixed-s,b counterfactual: welfare inversion survives; endogenous R&D amplifies it for one benchmark | Existing two-part payoff decompositions/known learning welfare effects | **MODEL-SPECIFIC ILLUSTRATION ONLY**. The composition shift is **not a necessary cause** of welfare inversion. |
| Observability improves consumer welfare or efficiency universally | Contradicted by Baik & Kim, existing paper results and our own conditional claims | **REJECT** as general theorem/policy conclusion. |
| Endogenous *voluntary* disclosure equilibrium | Baik & Kim 2025 and other work | **NOT IN OUR MODEL**; remove from purported contribution. |

## 4. Source-quality register (actual evidence checked in this Stage)

| Paper/version | Evidence | Exact source | Limits |
|---|---|---|---|
| Baik & Kim 2020 | FULL SECTION 7.3, printed pages 30–31; PDF screenshot/text | https://swb.skku.edu/_res/khbaik/etc/JEZN1.pdf | Main quantity game and the differentiated Bertrand extension must not be conflated |
| Kim & Poggi 2026 Sep v2 | 68-page official DP648 PDF opened; 2026 cover and Propositions 1–3 and Theorem 1 inspected, sections 2–5 | https://www.crctr224.de/research/discussion-papers/archive/dp648 | Did not inspect **every appendix proof**; thus no absolute general parent claim |
| Kogan & El Ouardighi 2019 | Publisher full HTML model (equations) and numbered proposition excerpts | https://www.sciencedirect.com/science/article/pii/S0307904X18305092 | Some tools intermittently show 403; original model text and proposition extracts were available from indexed source |
| Cabral & Riordan 1994 | Journal metadata and full abstract, NOT full paper | https://ideas.repec.org/a/ecm/emetrp/v62y1994i5p1115-40.html | **Definitive theorem-level exclusion impossible** |
| Bulow, Geanakoplos & Klemperer 1985 | Stanford/Yale abstract and publisher bibliographic data, NOT full proofs | https://www.gsb.stanford.edu/faculty-research/working-papers/multimarket-oligopoly-strategic-substitutes-complements | Generic strategic commitment mechanism has algebraic mapping, but full theorem hypotheses unreviewed |
| Fudenberg & Tirole 1984 | Publisher/RePEc bibliographic record and standard strategic investment classification | https://ideas.repec.org/a/aea/aecrev/v74y1984i2p361-66.html | Full published article not obtained; cannot claim exhaustive theorem comparison |
| Lin & Zhou 2013 | Publisher full abstract | https://doi.org/10.1016/j.ijindorg.2012.11.003 | No full proposition/appendix audit |
| Cohen & Levinthal 1994 | Publisher full abstract | https://doi.org/10.1287/mnsc.40.2.227 | No full theorem/appendix audit |
| Jiang & Xiong 2025 | Official Duke/HKU abstract | https://doi.org/10.2308/TAR-2023-0296 | Full Bertrand derivation not inspected here |
| Besanko et al. 2014/2019 | AEA abstracts | https://doi.org/10.1257/aer.104.3.868 ; https://doi.org/10.1257/aer.20180131 | No theorem-level full-paper review |
| Huang et al. 2023, Chen et al. 2024 | Publisher abstract/full HTML respectively | https://doi.org/10.1016/j.econmod.2022.106144 ; https://doi.org/10.1111/1475-679X.12546 | Empirical/investor disclosure is a different outcome/information institution |

**Search strategy performed:** (a) original exact titles, revised working-paper version and publisher metadata; (b) mechanism queries with “observability / private learning investment / strategic price responses / market-share feedback / R&D portfolio”; (c) stripped-sector strategic-investment and strategic complements/substitutes parent classes; (d) adjacent quality-control, autonomous-and-induced learning and R&D-capability investment. An explicit search failing to find the exact algebra **is not evidence of novel priority**.

## 5. Retractions and contribution memo

**False-positive novelty regression:** Earlier framing risked presenting *the sign of the disclosure profit–welfare wedge* or *the existence of short-horizon innovation bias* as a discovery. These are demonstrably known. Similarly, our exact investment derivative is a generic strategic-commitment chain-rule term. All three must be downgraded in Abstract, Introduction, Conclusion and cover letter.

**Surviving candidate contribution (precisely conditional):**

> In a two-period differentiated Bertrand market, the investment that is revealed or concealed is **the conversion rate from own current customer share to future quality**. A rival's contingent current price therefore makes an unobserved learning-investment deviation more valuable than an observed deviation. When immediate quality investments of both firms are endogenous, the high-learning-cost pure equilibrium exhibits an explicit joint R&D-composition shift and a region in which both firms prefer observability but welfare prefers concealment. Under a separately certified normalized finite-cost region, the entrant's current and future market-share rankings reverse.

The novelty argument is **specific model interaction and conditional new prediction**, **not** a general strategic-commitment theorem. A referee can object that this is a narrow functional-form combination of known mechanisms. That objection cannot be dismissed merely by the presence of a new polynomial threshold.

### Editorial value and completeness (provisional Stage-6 check)

- **Why a field editor might care:** provides an analytically transparent, mechanism-specific reason for a disclosure institution to redirect technology from long-term customer learning to immediate quality and not merely alter aggregate R&D, while separating firm-private and consumer consequences. Two periods and a small number of actions allow a clean condition and counterfactual.
- **Strongest objection:** generic commitment response (Fudenberg/Tirole/Bulow) + known R&D transparency profit/welfare reversal (Baik/Kim) + known price/experience/induced quality interactions (Cabral/Riordan; Kogan/El Ouardighi) may make the complete result an immediate application with insufficient independent theorem novelty. The **exogenous investment caps** further narrow external validity.
- **ESSENTIAL FOLLOW-UP:** complete theorem-absorption map against closest dynamic learning/strategic-investment general parent results using **full text or precise theorem statements**; if absorbed, revise claim or route to a short focused note rather than pretending novelty.
- **BOUNDED LIMITATION:** feasible s,b,lambda caps and sufficient \(0<d<3t\) ensure global interiority; original unbounded model counterexample is kept. Not an asymptotically derived no-monopoly condition.
- **BOUNDED LIMITATION:** no endogenous voluntary disclosure, mixed-PBE claim, general explicit high-cost threshold or fixed research budget.
- **FUTURE PAPER:** privately distributed technological types, endogenous disclosure choice, more general learning technologies, or endogenous customer foresight. **Not authorized for this submission**.
- **NOT APPLICABLE:** a policy-instrument/first-best implementation theorem (this is diagnostic pure theory).
- **Baseline vs extension/reframe:** continue **baseline-only** with a mechanistic framing and explicit ablation; do not add strategic primitives to rescue novelty. If future full-theorem check kills the result, prefer a concise research note or stop, not a result-selected extension.

## 6. Preliminary future-question map (NOT authorized or certified)

1. **Endogenous measurement of the learning coefficient:** can a cheaper noisy disclosure signal preserve the public incentive wedge without direct verification of \(\lambda\)? Economic insight: disclosure accuracy, not binary observability, can alter customer-experience investment. Killer: generic Bayesian persuasion/information disclosure models. Minimum falsifier: no change in incumbent price response to precision. \`OPEN WITH EVIDENCE / UNVERIFIED\`.
2. **Predetermined customer captivity:** does the R&D-direction effect survive when a nonzero customer mass is inaccessible to incumbent price defense? Economic insight: contestability of the learning base. Killer: standard LBD with captive buyers. Minimum falsifier: sign of learning-investment incentive wedge over a simple captivity interval. \`PROPOSED / NOT AUTHORIZED\`.
3. **Capacity endogeneity under actual cap relaxation:** can a primitive economically grounded capacity choice permit unrestricted s,b while avoiding the documented profitable monopoly deviation? Killer: endogenous entry deterrence/monopoly parent classes. Minimum falsifier: profitable exclusionary quality deviation persists under plausible capacity costs. \`PROPOSED / NOT AUTHORIZED\`.

No future candidate strengthens the current-paper Stage-6 verdict or justifies drifting into a new model.

## 7. Next-stage contract

**Stage-6 \`CONDITIONAL GO\`:** One blocking item is required before the word "novel" can appear as an evidence-scoped claim: **perform a full-paper/complete-theorem nonabsorption comparison against the strongest strategic-investment and learning-by-doing parent classes**, beginning with Cabral & Riordan (1994) and Bulow/Geanakoplos/Klemperer (1985); specifically determine whether the joint (s,b,lambda) comparative-static + P-private/H-social theorem can be obtained as a specialization or short corollary. If unavailable, retain \`UNRESOLVED\` and do not declare Stage 6 \`GO\` by inference from search failure.

Pending this, **the revised compact action set and corrected finite-cost theorem remain mathematically usable research results**, but no journal-priority claim has been certified and Stage 8 theory freeze is **not authorized**. Stage 7.5A formal-verification and author-verification obligations remain separate.

### Reproducible artifact

\`python code/stage6_strategic_commitment_identity.py\` checks the generic strategic derivative absorption and the no-sales-feedback ablation. Its success certifies only its symbolic identities, not literature completeness or publication novelty. No journal PDF is copied into this repository; URLs and source depth are retained for lawful scholarly reinspection.
