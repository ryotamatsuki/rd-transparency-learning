# Recommended submission outline — lean version (2026-11-10)

**Status:** editorial plan only; no newly claimed proofs. This document supersedes the *numbered-result density* proposed in `docs/theorem_architecture.md` for a first submission, but that earlier file remains the detailed register of candidate lemmas and intuitions.

## Goal

A focused field-journal theoretical paper: **one economic mechanism, one substantive R&D-direction proposition, and one headline private-profit / social-welfare theorem**. Target about 15–18 manuscript pages excluding appendices as an editorial guideline, not a journal requirement.

## Main text (six sections)

| Section | Approximate size | Content and reason to include |
|---|---|---|
| 1 Introduction | ~3 pp | Research question in the first paragraph; three-step causal chain; concise preview of strongest theorem; position carefully against Baik & Kim (2020), Sengupta (2016), Jiang & Xiong (2025), Besanko et al. (2014), Huang et al. (2023), Kim & Poggi (2026). Integrate literature review here, rather than make an independent long survey. |
| 2 Model | ~2–3 pp | Unit Hotelling line; two periods; A's persistent quality investment s, B's immediate but persistent quality investment b, learning capability λ; q2 = −d + λ D1; timing/information sets; quadratic costs, welfare definition; necessary regularity and compact strategy ranges. |
| 3 Pricing and learning incentives | ~2–3 pp | Solve second- then first-period prices in unified notation; **Lemma 1** pricing; **Proposition 1** observability wedge and (in its justified high-cost domain) λP=0<λH. Explain observation-conditional price reaction versus equilibrium P/H price levels. |
| 4 R&D composition, profits and welfare | ~4–5 pp | **Proposition 2:** sign changes in s,b,λ; **Theorem 1:** both firms prefer P although W(H)>W(P) under stated sufficient conditions. Explain which mechanism drives each sign and the welfare identity. Put exact A-profit restriction and all domain assumptions in the actual theorem. |
| 5 Economic interpretation and scope | ~2–3 pp | One compact benchmark equilibrium table; optional **Corollary 1** intertemporal market-share reversal (normalized finite-cost scope); a carefully qualified removal-of-sales-feedback comparison q2=−d+λ after formal proof; fixed-s,b numerical counterfactual as *amplification illustration*, not a general theorem. Distinguish global from branch-only finite-cost thresholds. |
| 6 Conclusion | ~1 p | Takeaway and limits. Exogenous observability comparison is not an endogenous voluntary-disclosure equilibrium; two periods do not imply a permanent innovation delay. No unsupported broad policy prescription. |

## Numbered results — limit to the following

1. **Lemma 1 — Dynamic Bertrand Price Equilibrium.** Technical and short. Equations for D1, D2 and equilibrium prices; lengthy derivation in Appendix A.
2. **Proposition 1 — Observability and the Incentive to Invest in Learning.** The public marginal return at λ=0 is negative while the hidden unobserved-deviation return is positive when 0<d<3t. Add equilibrium suppression (λP=0<λH) only with the correct strict conditions and global optimum argument.
3. **Proposition 2 — The Direction of Equilibrium R&D.** The statement sH>sP, bH<bP, λH>λP, with general high-cost sufficient conditions and explicit recognition that b persists into period 2 and no common fixed R&D budget is assumed.
4. **Theorem 1 — Privately Preferred Disclosure, Socially Preferred Concealment.** ΠA(P)>ΠA(H), ΠB(P)>ΠB(H), W(H)>W(P), restricted to the justified general sufficient domain. Distinguish known sign reversal from the novel causal mechanism being proposed.
5. **Corollary 1 — Intertemporal Market Share and Quality Reversal (optional).** Only for a separately proved normalized finite-cost region. Could be a short paragraph rather than a numbered result if the paper is too long.

**Do not add separate results** for: (i) merely λP=0 (already inside Prop. 1), (ii) the consumer surplus identity (accounting consequence of the theorem), (iii) finite-cost normalization solely to raise proposition count, (iv) a fixed-(s,b) counterfactual that is not a full equilibrium, or (v) voluntary disclosure without a disclosure-choice game.

## Technical appendix

- A. Price-subgame FOCs, uniqueness, full interior/admissibility checks, and hidden off-path deviations.
- B. Learning R&D optimality, comparative statics, Jacobian/implicit-function conditions for general high-cost theorem.
- C. Profit, welfare and consumer-surplus identities; proof of headline theorem; exactly state the sufficient incumbent-profit inequality.
- D. **Independent** normalized nonasymptotic theorem and explicit sufficient threshold \(k_\lambda>4343/32448\) on \(0\le s,b\le1/2,\;0\le\lambda\le1\). Rational Bernstein proof and any supplementary symbolic certificate. The branch-only extension to \(k_\lambda\ge 0.1\) is **not** a global-equilibrium theorem.
- E. Feedback-removal ablation only if its formal proof is sound; otherwise treat as a short discussion remark, not an established lemma.

## Example papers: learn a different editorial skill from each

1. **Sengupta (2016)**, *Investment Secrecy and Competitive R&D*, The B.E. Journal of Economic Analysis & Policy 16(3), 1573–1583. A short 11-page Letter; Introduction → The Model → Observability vs Secrecy. A pricing lemma and the regime-specific propositions lead directly to comparison and welfare. **Best reference for economy and flow**, although proof placement should be less dense for our more elaborate algebra. Author PDF: https://webhome.auburn.edu/~azs0074/BESecrecy.pdf
2. **Baik & Kim (2020)**, *Observable versus Unobservable R&D Investments in Duopolies*, Journal of Economics 130, 37–66. Main models are defined and solved, then compared; especially Sec. 7.3 for differentiated Bertrand. **Best exact-subject benchmark for why our theorem differs**, but its many variants/longer exposition should not be emulated for an early submission. Author PDF: https://swb.skku.edu/_res/khbaik/etc/JEZN1.pdf
3. **Matsumura & Matsushima (2011)**, *Locating Outside a Linear City Can Benefit Consumers*, Journal of Regional Science 52(3), 420–432. **Reference for writing a counterintuitive Hotelling welfare result around one economic mechanism.** Journal record: https://doi.org/10.1111/j.1467-9787.2011.00735.x
4. **Kim & Poggi (2026 revision)**, *Strategic Concealment in Innovation Races*. **Compare innovation-direction terminology and novelty claims; do not copy the length/complexity.** RePEc revision record: https://ideas.repec.org/p/bon/boncrc/crctr224_2025_648v2.html

## Last checks before manuscript drafting

- The general high-cost proof and normalized finite-cost certificate are logically **different** results and must not be conflated.
- Reproduce the exact earnings and social-welfare benchmarks, and retest the no-feedback auxiliary claim.
- Complete theorem-by-theorem novelty comparison, particularly differentiated Bertrand claims in Baik & Kim (2020).
- No new complex extensions unless a proof or novelty objection makes them necessary.
