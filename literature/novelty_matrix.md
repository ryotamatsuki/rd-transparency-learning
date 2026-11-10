# Novelty matrix — theorem/mechanism-level comparison

Status: **working assessment as of 2026-11-10**. Never claim that a feature is new merely because the same words are absent from abstracts. Read model, timing, information structure, propositions, welfare definitions, proofs and appendices before asserting non-derivability.

## Prior literature (bibliography cross-checked where DOI shown)

| Source | What is already established / modeled | What is NOT ours to claim as new | Remaining theorem-level test |
|---|---|---|---|
| [Sengupta (2016)](https://doi.org/10.1515/bejeap-2016-0047), *Investment Secrecy and Competitive R&D*, B.E. J. Econ. Anal. Policy 16(3), 1573–1583 | Investment observability, uncertain cost-reducing R&D, private realized costs, price competition; secrecy can improve investment and social welfare | "Secrecy may increase R&D and welfare" | Locate exact profit/welfare propositions; ascertain whether output-contingent learning could be embedded |
| [Baik & Kim (2020)](https://doi.org/10.1007/s00712-019-00679-3), *Observable versus unobservable R&D investments in duopolies*, Journal of Economics 130, 37–66 | Quantity duopoly plus a differentiated price-setting extension; observable vs unobservable cost-reducing R&D; compare profits and welfare | "Disclosure raises profits and lowers welfare" can occur already under differentiated Bertrand | Reproduce section 7.3 propositions and map parameters/payoff welfare precisely |
| [Jiang & Xiong (2025)](https://doi.org/10.2308/TAR-2023-0296), *Disclosing Endogenous Cost Information*, The Accounting Review 100(2), 249–268 | Cost-information disclosure affects endogenous investment and consumer consequences in Bertrand vs Cournot | Disclosure improving both firms' profit via weaker investment rivalry | Check timing of cost-information revelation vs investment observability |
| [Besanko, Doraszelski & Kryukov (2014)](https://doi.org/10.1257/aer.104.3.868), *The Economics of Predation: What Drives Pricing When There Is Learning-by-Doing?*, AER 104(3), 868–897 | Dynamic pricing, learning-by-doing and predatory incentives | "Incumbent strategically cuts prices to deter rivals' learning" | Evaluate whether endogenizing a learning-rate investment and information structure yields nonredundant comparative statics |
| [Baik & Kim (2025)](https://doi.org/10.1007/s00712-025-00916-y), *Duopoly firms' decisions on disclosing their R&D investment information*, Journal of Economics 146, 187–220 | Endogenous voluntary disclosure under quantity/price competition | "Firms voluntarily choose to disclose R&D" | Cannot claim endogenous voluntary disclosure result without separate model |
| [Huang et al. (2023)](https://doi.org/10.1016/j.econmod.2022.106144), *Intended and unintended effects of mandatory R&D disclosure on innovation outcomes*, Economic Modelling 119, 106144 | Disclosure pressure can shift innovation toward quick-return research, with investor/media pressure | "Disclosure tilts innovation toward short-run outcomes" | Contrast capital-market managerial pressure with product-market price-defense channel |
| [Chen, Liang & Petrov (2024)](https://doi.org/10.1111/1475-679X.12546), *Innovation and Financial Disclosure*, Journal of Accounting Research 62, 935–979 | Two-period innovation/exploration, exploitation, strategic financial disclosure | Disclosure and explore/exploit trade-off as an idea | Contrast bandit/financial performance information with price-setting against customer-experience learning |
| [Kim & Poggi (2025 working paper, revised September 2026)](https://ideas.repec.org/p/bon/boncrc/crctr224_2025_648v2.html), *Strategic Concealment in Innovation Races* | Dynamic race; division between direct development and research for better technology; strategic concealment/patents/spillovers | "Short-term development vs long-term research allocation under secrecy" | Read latest 2026 revision and all propositions; isolate reliance on innovation race, patent policy, interfirm spillovers |
| [Lee & Wu (2026), Social Value of Transparency in R&D Races](https://scholar.google.com/scholar?q=Social+Value+of+Transparency+in+R%26D+Races+Lee+Wu+2026) | Previously surfaced as relevant working paper; details not independently verified in this repo | No priority claims pending direct-source verification | Verify exact title, authors, version and full text before citing in manuscript |

## Hypothesized distinctive mechanism

1. B's first-period share \(D_1\) is jointly determined by *current Bertrand prices*.
2. B's future quality depends on *chosen learning efficiency* times its own sales experience \(\lambda D_1\).
3. A's period-1 price can condition on observed \(\lambda\) in P, but not on hidden unilateral deviations in H.
4. B reallocates between immediately effective quality improvement \(b\) and future learning capability \(\lambda\); A also endogenously chooses persistent quality improvement \(s\).
5. The resulting portfolio adjustments can **amplify** the welfare loss from disclosure, even when both firms favor disclosure.

## Falsification / ablation tests (critical)

- Remove sales feedback: replace \(q_2=-d+\lambda D_1\) with \(q_2=-d+\lambda\) while preserving game timing/information. Draft conjecture: observability effect disappears; prove all equilibrium statements formally.
- Fix \(s,b\) at public-equilibrium values, reoptimize hidden \(\lambda\): welfare reversal remains (reported benchmark: public welfare \(-0.941840\), fixed-quality-R&D hidden \(-0.929585\), fully endogenous hidden \(-0.914278\)). Thus **portfolio reallocation is an amplifier, not a necessary source** of reversal. Replicate with a dedicated script before treating the decomposition as independently verified.
- Check \(\delta\to0\), learning technology independent of D1, and alternative observability of b/s.
- Compare **mathematical predictions** and **economic mechanisms**, not just similar phrases.

## Claim discipline for manuscript

**Safe:** "We provide a tractable two-period price-competition mechanism linking disclosure of learning-capability R&D, experience-based future quality, and composition of R&D."

**Unsafe without more proof:** "Disclosure-profit-welfare reversal is new"; "disclosure always harms innovation"; "R&D short-termism is new"; "this establishes a voluntary disclosure equilibrium"; "the incumbent can never infer concealed investment"; "unconditionally novel relative to all prior theory."

## Verification log

- Bibliographic identification/DOIs for eight entries checked against journal, publisher, RePEc, author or university pages on 2026-11-10.
- Theorem-level comparison is *in progress*. Strong priority and novelty conclusions remain **unverified**.
