# Related Literature master register / 関連研究の網羅的管理台帳
**Research snapshot:** 2026-11-10 | Repository: rd-transparency-learning

This register consolidates **all specific papers previously discussed in the project** and adds adjacent canonical and high-overlap papers identified in the follow-up search. It is a *reproducible working bibliography*, **not a claim to have enumerated every paper ever published on R&D, secrecy, or learning**. Entries include summaries **in our own words**, source links, model-level relevance, a suggested citation location, and evidence limits.

## How to use
- **A = essential in a short journal manuscript**, **B = read/check and cite selectively**, **C = foundations/context or writing example** (often only a brief reference).
- **Evidence F** = a materially relevant portion of author/publisher full text inspected; **E** = publisher/university abstract plus bibliographic metadata verified; **M** = metadata only. F does **not** mean the full theorem/proof was audited.
- Cite **the publication year** of the final journal article, not a working-paper or first-online date, except unpublished working papers.
- \`paper/references.bib\` is the usable citation database. \`literature/citation_plan.md\` chooses the minimum main-text cites. **Do not copy every entry here into the manuscript automatically.**
- Literature summaries below are paraphrases; exact page/section numbers and priority claims must be checked against the latest full text before submission.

## A. Directly overlapping disclosure / observability mechanisms

### A01. Baik & Kim (2020) — [A, F: Section 7.3]
**Full reference:** Baik, Kyung Hwan, and Sang-Kee Kim (2020), “Observable versus unobservable R&D investments in duopolies,” *Journal of Economics* 130(1), 37–66. [DOI](https://doi.org/10.1007/s00712-019-00679-3) | [author full text](https://swb.skku.edu/_res/khbaik/etc/JEZN1.pdf).

**Model:** Main model is a quantity-setting duopoly with uncertain cost-reducing R&D outcomes and privately observed realized marginal costs. **Section 7.3 is a separate differentiated Bertrand extension**: deterministic marginal-cost reduction, linear substitute-goods demand \(q_i=a-p_i+\theta p_j\) (0<θ<1), observable versus unobservable R&D investment before prices.

**Verified result (author PDF printed p.31, Section 7.3):** Under the stated admissible parameter conditions, observable R&D is smaller and firm profits are greater than when unobservable; consumer surplus is lower. **Social welfare is lower under observability for \(\theta\le0.52\), but reverses for \(\theta\ge0.53\).** The paper explicitly interprets price competition as strategic complements. **Do not attribute the Section 7.3 results to the stochastic main model**, nor treat their social-welfare sign as unconditional.

**Overlap:** Our P/H sign reversal is already known in this exact price-competition neighborhood. **Distinct candidate:** they have one **cost-reducing** R&D choice per firm, not B's chosen \(\lambda\) multiplied by **first-period customer experience** and an additional persistent quality choice \(b\), plus A's own \(s\).

**Use:** Required citation in Introduction immediately before our novelty sentence, and direct comparative discussion near Theorem 1; do not claim profit/welfare reversal itself as a new discovery.

### A02. Sengupta (2016) — [A, F: introduction and main propositions]
Aditi Sengupta (2016), “Investment Secrecy and Competitive R&D,” *The B.E. Journal of Economic Analysis & Policy* 16(3), 1573–1583. [DOI](https://doi.org/10.1515/bejeap-2016-0047) | [author PDF](https://webhome.auburn.edu/~azs0074/BESecrecy.pdf).

**Model:** Duopoly with uncertain outcome of cost-reducing R&D, private realized production-cost types and subsequent price competition; compare observable vs unobservable strategic investments.

**Result:** Concealed R&D investments can yield more R&D, greater industry profit and greater welfare than publicly observable investments. Revealed costs and investments must not be conflated; final realized cost is privately known.

**Overlap:** Concealment leading to higher investment or welfare is established. **Difference:** no deliberate partition into immediate quality vs market-experience-based future learning efficiency; no endogenous \(\lambda D_1\) feedback.

**Use:** Introduction information-secrecy theoretical baseline. A shorter paper whose writing economy is worth emulating. Avoid asserting it supports both firms preferring publicity: it reports higher aggregate industry profit with secrecy.

### A03. Jiang & Xiong (2025) — [A, E]
Xu Jiang and **Yan Xiong** (2025), “Disclosing Endogenous Cost Information,” *The Accounting Review* 100(2), 249–268. [DOI](https://doi.org/10.2308/TAR-2023-0296) | [HKU scholarly repository](https://hub.hku.hk/handle/10722/359069) | [Duke faculty record](https://scholars.duke.edu/publication/1668555).

**Model:** Firms voluntarily reveal privately known **endogenously chosen production-cost information** after cost-reducing investment; compare Cournot and Bertrand.

**Result:** With Bertrand pricing, disclosure restrains excessively aggressive cost-reduction investment and benefits the firms; consumers may lose. With Cournot, disclosure can generate a prisoners'-dilemma logic. The object disclosed is **cost information**, not necessarily investment in the learning rate itself.

**Overlap:** Disclosure, reduced R&D, and joint firm gain are known. **Difference:** no price-sensitive accumulation of customer-based learning as a future quality input; the direction of two R&D types is not their outcome.

**Use:** Essential paragraph on private disclosure incentives and the difference between outcomes/cost information and R&D-investment observability.

### A04. Baik & Kim (2025) — [A or B, F: published author abstract]
Baik, Kyung Hwan, and Sang-Kee Kim (2025), “Duopoly firms’ decisions on disclosing their R&D investment information,” *Journal of Economics* 146(2), 187–220. [DOI](https://doi.org/10.1007/s00712-025-00916-y) | [author PDF](https://swb.skku.edu/_res/khbaik/etc/JEZN2.pdf).

**Model:** First, each firm publicly chooses whether it will disclose its cost-reducing R&D investment; second, it chooses R&D; third, Cournot quantities or differentiated Bertrand prices. Investment-to-cost reduction is deterministic.

**Result:** Both firms choose to disclose their investments in the settings studied.

**Overlap:** Adding a voluntary-disclosure stage per se is not a novel extension. **Difference:** our main draft does **not** have firms voluntarily choosing P/H and does have experience-dependent future quality.

**Use:** One sentence in Introduction/discussion on the scope of disclosure endogeneity and explicit limitation of our **exogenous regime comparison**.

### A05. Huang, Liu, Chan & Chen (2023) — [A, E]
Dan Huang, Baohua Liu, Kam C. Chan, and Yining Chen (2023), “Intended and unintended effects of mandatory R&D disclosure on innovation outcomes,” *Economic Modelling* 119, article 106144. [DOI/publisher](https://doi.org/10.1016/j.econmod.2022.106144).

**Approach:** China-listed technology-intensive firms around 2012 disclosure mandate; empirical evaluation, with conceptual discussion of pressures on the innovation mix.

**Result:** R&D disclosure improves transparency and may stimulate innovation, but attention/pressure from analysts, media and large shareholders redirects effort toward easy/quick-return innovation, eroding long-run innovation and value.

**Overlap:** "Disclosure causes short-term innovation bias" is **already documented**. **Difference:** their mechanism is capital-market monitoring/managerial time horizons; ours is **product-market dynamic price defense even without capital-market pressure**.

**Use:** Introduction motivation and explicit mechanism contrast; do not claim to invent the phrase or phenomenon "R&D short-termism."

### A06. Chen, Liang & Petrov (2024) — [A, F: publisher full HTML]
Hui Chen, Pierre Jinghong Liang, and Evgeny Petrov (2024), “Innovation and Financial Disclosure,” *Journal of Accounting Research* 62(3), 935–979. [Open publisher article](https://doi.org/10.1111/1475-679X.12546).

**Model:** A two-period innovation/exploration-versus-exploitation **bandit** problem for a manager: old production method with known success probability, new unknown method; financial reporting/early vs late disclosure options affect investment and learning.

**Result:** Early voluntary plus later mandated disclosure can strengthen exploration; alternative disclosure timing can weaken it; market-price-concerned managers can over- or under-explore.

**Overlap:** Dynamic technology choice/learning and disclosure is not new. **Difference:** managerial incentives/investor reporting rather than competitor Bertrand prices tied to entrant experience and endogenous asymmetric duopoly R&D.

**Use:** Context paragraph separating financial disclosure from the **rival-observability** institution.

### A07. Kim & Poggi (2026 revision of 2025 working paper) — [A, E: revised abstract, original 2025 PDF *not* latest]
Yonggyun Kim and Francisco Poggi, “Strategic Concealment in Innovation Races,” *CRC TR 224 Discussion Paper Series* No. 648, working paper dated 2025; **revised September 2026**. [Revised record](https://ideas.repec.org/p/bon/boncrc/crctr224_2025_648v2.html) | [CRC archive](https://www.crctr224.de/research/discussion-papers/archive/dp648). Do not substitute the [older May 2025 author PDF](https://www.franciscopoggi.com/files/SCIR.pdf) as if it were the 2026 revision.

**Model:** Dynamic innovation race. Firms allocate resources between working directly on an existing technology and investigating a faster breakthrough; privately found interim innovation may be patented/revealed or concealed, depending on prize and intellectual-property protections.

**Result:** Large victory prizes and strong prior-use defense can support concealment, reduce spillovers and slow innovation.

**Overlap:** Choosing *direct development vs research for better future technology* under secrecy is already explicitly modeled. **Difference:** our learning capability is not a breakthrough spillover/patent input; it converts **own customer experience from a priced product market** into period-2 quality.

**Use:** Essential R&D-direction and dynamic-information comparison. **Mandatory before submission:** obtain and inspect the *2026* full text and every proposition. The revised abstract alone cannot establish theorem-level nonredundancy.

### A08. Lee & Wu (2026 working paper) — [B, E]
Seung Lee and Sang Wu (2026), “Social Value of Transparency in R&D Races,” working paper, manuscript dated January 31, 2026; SSRN posted September 18, 2026. [SSRN / DOI](https://doi.org/10.2139/ssrn.7476358) | [institutional record](https://portal.findresearcher.sdu.dk/en/publications/social-value-of-transparency-in-rampd-races/).

**Model:** Multi-stage R&D duopoly race; an intermediate success publicly announced by the leader reveals project feasibility but also strengthens the perception of a technological gap; follower decides to continue/exit.

**Result:** Disclosure can keep a laggard in the race or deter it. Social optimum depends on firm strengths; concealed intermediate success may improve welfare in intermediate cases.

**Overlap:** Disclosure-vs-concealment welfare rank depends on dynamic continuation incentives. **Difference:** exit/continuation and inference about breakthrough, rather than endogenous Bertrand market-share learning and composition of two R&D inputs.

**Use:** One brief recent-paper mention if space, or appendix literature comparison. **Working paper, not label as published.**

### A09. Gill (2008) — [B, E]
David Gill (2008), “Strategic Disclosure of Intermediate Research Results,” *Journal of Economics & Management Strategy* 17(3), 733–758. [DOI](https://doi.org/10.1111/j.1530-9134.2008.00193.x).

**Model/result:** In a patent contest, a research leader may reveal intermediate results to credibly signal commitment and make its opponent exit despite spillovers; in some cases deterrence occurs even without disclosure.

**Overlap:** Disclosure changes rival actions and strategic commitment. **Difference:** research contest/intermediate breakthroughs/exit rather than customer-sales feedback and two-period quality prices.

**Use:** Selectively in early strategic-disclosure literature discussion; not a key predecessor for quantitative welfare signs.

### A10. Vives (1984) — [B, E]
Xavier Vives (1984), “Duopoly Information Equilibrium: Cournot and Bertrand,” *Journal of Economic Theory* 34(1), 71–94. [DOI](https://doi.org/10.1016/0022-0531(84)90162-5).

**Model/result:** Private **demand information**, Cournot versus Bertrand, sharing incentives, and social value of information. In a substitutes Bertrand setting, private and social values need not align; welfare effects differ from Cournot.

**Overlap:** Private incentives to reveal information need not match social efficiency—classic result. **Difference:** demand signals are not R&D investments and no learning capability/experience loop.

**Use:** Optional single foundational cite on disclosure welfare, not an explanation of our specific technology channel.

### A11. Gal-Or (1985) — [C, M]
Esther Gal-Or (1985), “Information Sharing in Oligopoly,” *Econometrica* 53(2), 329–343. [DOI](https://doi.org/10.2307/1911239).

**Background:** Classic strategic information-sharing literature. Sengupta discusses **Gal-Or (1986)** separately; do not confuse those references or attribute its 1986 result to the 1985 paper without checking.

**Use:** Historical backdrop only when discussing the information-sharing lineage; full theorem-level comparison not yet done.

## B. Experience-based dynamic competition and investment in learning

### B01. Spence (1981) — [A or B, E]
A. Michael Spence (1981), “The Learning Curve and Competition,” *The Bell Journal of Economics* 12(1), 49–70. [Stanford GSB publication](https://www.gsb.stanford.edu/faculty-research/publications/learning-curve-competition).

**Model/result:** Costs depend on accumulated firm output; studies industry evolution and a two-period comparison of open-loop vs closed-loop equilibria and spillovers.

**Overlap:** Very important early analysis of how learning curves and **contingent strategies** affect current competition; cite when explaining the dynamic benefit of sales. **Difference:** our key investment is B's **endogenous ability to learn**, observed/hidden by A before pricing, alongside choices of immediate and persistent quality R&D.

**Use:** Introduction (learning-by-doing lineage), Section 3 pricing incentives; avoid claiming current sales endogenously affecting next-period competitiveness is new.

### B02. Fudenberg & Tirole (1983) — [B, E]
Drew Fudenberg and Jean Tirole (1983), “Learning-by-Doing and Market Performance,” *The Bell Journal of Economics* 14(2), 522–530. [RePEc](https://ideas.repec.org/a/rje/bellje/v14y1983iautumnp522-530.html).

**Model/result:** Learning-by-doing in dynamic markets; strategic interactions can alter output paths and welfare effects of learning diffusion. Two-period analysis shows that strategic feedback can reverse static/naive reasoning.

**Overlap:** Strategic market decisions under intertemporal learning and welfare. **Difference:** no dual-purpose entrant R&D portfolio contingent on visibility of the learning rate to an incumbent.

**Use:** A paired citation with Spence or Besanko if needed; minimize duplication.

### B03. Cabral & Riordan (1994) — [A, E]
Luís M. B. Cabral and Michael H. Riordan (1994), “The Learning Curve, Market Dominance, and Predatory Pricing,” *Econometrica* 62(5), 1115–1140. [DOI](https://doi.org/10.2307/2951509) | [RePEc abstract](https://ideas.repec.org/a/ecm/emetrp/v62y1994i5p1115-40.html).

**Model/result:** Differentiated price-setting duopoly with heterogeneous sequential customers and endogenous learning curve; Markov equilibrium, path-dependent dominance and dynamic predatory pricing. The private value of learning can be nontrivial even for an incumbent.

**Overlap:** **Closest foundational antecedent for rival-price effects through sales-induced learning** in a differentiated duopoly. **Difference:** our incremental claim concerns strategic observability of chosen \(\lambda\) and allocation between \(\lambda,b,s\), not an assertion that learning-based dominance or predatory incentives are new.

**Use:** Mandatory dynamic-learning baseline in Introduction or Section 3; obtain full text before a theorem-level "not implied" statement.

### B04. Besanko, Doraszelski & Kryukov (2014) — [A, E]
David Besanko, Ulrich Doraszelski, and Yaroslav Kryukov (2014), “The Economics of Predation: What Drives Pricing When There Is Learning-by-Doing?” *American Economic Review* 104(3), 868–897. [DOI/publisher](https://doi.org/10.1257/aer.104.3.868).

**Model/result:** Dynamic industry game with learning-by-doing; derives predatory price incentives and separates market-competition-for-efficiency from predation-like behavior; removing predatory incentives can remove certain equilibria.

**Overlap:** Incumbent's current price may strategically hinder a rival's accumulation of experience—known. **Difference:** B optimizes an **observable/concealable learning-capability investment** plus quality, and both firms' long-lived quality R&D is endogenous.

**Use:** Main dynamic-price-competition paragraph; do not describe predatory pricing mechanism as a new finding.

### B05. Besanko, Doraszelski & Kryukov (2019) — [A or B, E]
David Besanko, Ulrich Doraszelski, and Yaroslav Kryukov (2019), “How Efficient Is Dynamic Competition? The Case of Price as Investment,” *American Economic Review* 109(9), 3339–3364. [DOI/publisher](https://doi.org/10.1257/aer.20180131).

**Model/result:** Pricing today invests in future lower cost/higher demand; analyzes welfare efficiency of learning-based competition against a first-best planner. Dynamic competition can exhibit relatively small deadweight loss due to offsetting terms despite distinct equilibrium vs efficient allocations.

**Overlap:** Necessity of **proper welfare accounting** and private-vs-social valuation of experience accumulation. **Difference:** it does not directly evaluate information disclosure of chosen learning intensity and dual R&D directions (verify theorem-level).

**Use:** Cite with 2014 paper (e.g. Besanko et al., 2014, 2019) where pricing investment and welfare are discussed.

### B06. Cohen & Levinthal (1989) — [B, E]
Wesley M. Cohen and Daniel A. Levinthal (1989), “Innovation and Learning: The Two Faces of R&D,” *The Economic Journal* 99(397), 569–596. [DOI](https://doi.org/10.2307/2233763) | [RePEc](https://ideas.repec.org/a/ecj/econjl/v99y1989i397p569-96.html).

**Model/result:** R&D creates own innovation **and** learning/absorptive ability to exploit outside knowledge; learning capability affects investments and spillover incentives.

**Overlap:** R&D as investment in the *ability to learn* is emphatically not new. **Difference:** theirs is primarily ability to absorb external/industry knowledge, while our \(\lambda D_1\) is own market experience generated by own sales.

**Use:** Footnote or a short rationale when interpreting \(\lambda\), especially if using "learning capability".

### B07. Cohen & Levinthal (1990) — [C, E]
Wesley M. Cohen and Daniel A. Levinthal (1990), “Absorptive Capacity: A New Perspective on Learning and Innovation,” *Administrative Science Quarterly* 35(1), 128–152. [ERIC](https://eric.ed.gov/?id=EJ406851).

**Concept:** Ability to recognize, assimilate and exploit external knowledge depends on prior knowledge.

**Use:** Optional terminology bridge only. **Do not call our own-customer-experience accumulation "absorptive capacity" as an equivalent concept.**

### B08. Cohen & Levinthal (1994) — [A or B, E]
Wesley M. Cohen and Daniel A. Levinthal (1994), “Fortune Favors the Prepared Firm,” *Management Science* 40(2), 227–251. [DOI](https://doi.org/10.1287/mnsc.40.2.227).

**Model/result:** Explicit firm investment in **absorptive capacity**, uncertainty, path dependence and competitor entry/behavior. Entry can change an incumbent's capability investment.

**Overlap:** Investment **in learning capability** and competitor reaction are existing theoretical subjects. **Difference:** knowledge absorption/external technological possibilities vs **sales-driven learning and pricing defense**, and information about the capability is not the stated mechanism. **High-priority conceptual prior art**.

**Use:** Required to audit before claiming endogenous investment in learning capability is novel; consider one cite in introduction.

### B09. Lin & Zhou (2013) — [A, E]
Ping Lin and Wen Zhou (2013), “The effects of competition on the R&D portfolios of multiproduct firms,” *International Journal of Industrial Organization* 31(1), 83–91. [DOI](https://doi.org/10.1016/j.ijindorg.2012.11.003).

**Model/result:** Multiproduct firms choose cost-reducing R&D across products. Stronger product competition can lead firms to specialize their R&D portfolios and shift investments across product lines.

**Overlap:** Endogenous **R&D composition/portfolios** under strategic product-market competition is established. **Difference:** their margin is *which product*, not *immediate quality versus efficiency of future experience-driven learning* conditional on visibility.

**Use:** Brief direct cite in Proposition 2 discussion, rather than saying "our model is first to endogenize R&D portfolios."

### B10. Ishida, Matsumura & Matsushima (2011) — [B, E]
Junichiro Ishida, Toshihiro Matsumura, and Noriaki Matsushima (2011), “Market Competition, R&D and Firm Profits in Asymmetric Oligopoly,” *The Journal of Industrial Economics* 59(3), 484–505. [DOI](https://doi.org/10.1111/j.1467-6451.2011.00461.x).

**Model/result:** Asymmetric low-cost vs high-cost firms with strategic Cournot R&D; adding inefficient rivals may stimulate efficient firms' R&D and raise their profits. Connects to open knowledge disclosure.

**Overlap:** Asymmetry, strategic technology investment and an unexpected private-profit effect. **Difference:** no intertemporal market-experience learning or investment observability distinction.

**Use:** Optional cite when motivating incumbency/entrant asymmetry and strategic disclosure incentives; not a necessary core comparison.

## C. Spatial-price foundations and writing benchmark

### C01. Hotelling (1929) — [C, M]
Harold Hotelling (1929), “Stability in Competition,” *The Economic Journal* 39(153), 41–57. [JSTOR](https://www.jstor.org/stable/2224214).

**Use:** One citation for the line-city demand tradition if journal convention calls for it. Our **locations are fixed**, so this does not imply endogenous location choice.

### C02. d'Aspremont, Gabszewicz & Thisse (1979) — [C, E]
Claude d'Aspremont, Jean Jaskold Gabszewicz, and Jacques-François Thisse (1979), “On Hotelling's ‘Stability in Competition’,” *Econometrica* 47(5), 1145–1150. [University record](https://research.dial.uclouvain.be/entities/publication/93b14af8-a908-4118-8c5a-52c23c05ba91).

**Use:** Standard critique and equilibrium subtleties of linear-city pricing and endogenous locations; usually **not necessary** for a paper with fixed endpoints and admissible full-coverage interior price equilibria. If cited, explain the distinction.

### C03. Matsumura & Matsushima (2012) — [C, E: model-paper example; usually not cite as Related Literature]
Toshihiro Matsumura and Noriaki Matsushima **(2012)**, “Locating Outside a Linear City Can Benefit Consumers,” *Journal of Regional Science* 52(3), 420–432. [DOI](https://doi.org/10.1111/j.1467-9787.2011.00735.x).

**Model/result:** Strategic incentives can overturn standard consumer-welfare intuition in location-price games. **Relevance:** writing model for a compact paper centered on a counterintuitive Hotelling welfare result, **not** a close R&D-disclosure predecessor.

**Bibliographic correction:** First published online in **August 2011**, but journal *volume/issue citation year is 2012*. Cite as **2012** in bibliography.

## Cross-literature novelty map

| Candidate claim from our paper | Closest prior art | Defensible interpretation |
|---|---|---|
| Secrecy increases R&D or welfare | Sengupta 2016; Baik & Kim 2020 | **Known**: do not claim as new |
| Disclosure increases both firms' profit while lowering consumer surplus/welfare | Baik & Kim 2020 **Section 7.3**, Jiang & Xiong 2025 | **Known sign pattern**; our result cannot rely on this alone |
| Public R&D disclosures shift innovation toward short-run results | Huang et al. 2023; Chen et al. 2024 | **Known general phenomenon**, different capital-market manager/investor mechanisms |
| Endogenous immediate versus future research effort | Kim & Poggi 2026 revision; Cohen & Levinthal 1989/1994 | **Known choice class**; may differ by technology and information feedback |
| R&D portfolio changes with competition | Lin & Zhou 2013 | **Known**; here across two *temporal/learning* tasks, not across products |
| Sales today build future competitive advantage; incumbent may use price to influence learning | Spence 1981; Fudenberg & Tirole 1983; Cabral & Riordan 1994; Besanko et al. 2014/2019 | **Known feedback**; our novelty must reside in chosen *learning rate* + observability + other R&D |
| Dynamic leader's disclosure may change rivals' decisions | Gill 2008; Lee & Wu 2026 | **Known** via patent race/exit, not necessarily via Bertrand experience |
| Our linked price-defense → \(\lambda D_1\) → \(b,\lambda,s\) → P-private/H-social comparison | None of above source abstracts or Baik & Kim 2020 Sec. 7.3 states the *same combined mechanism* | **Candidate only, not verified first-in-literature**. Theorem-by-theorem comparison still required |

## Paper placement — avoid a long standalone survey

**Introduction paragraph 1/2 — closest disclosure precedent:** cite Baik & Kim (2020), Sengupta (2016), Jiang & Xiong (2025). No novel "disclosure-profit-welfare divergence" claim.

**Introduction paragraph 3 — experience-mediated price competition:** cite Spence (1981), Cabral & Riordan (1994), Besanko et al. (2014, 2019); Fudenberg & Tirole (1983) optional.

**Introduction paragraph 4 — R&D direction/learning investment:** cite Cohen & Levinthal (1989/1994), Lin & Zhou (2013), Kim & Poggi (2026 revised), Huang et al. (2023), Chen et al. (2024). Avoid a long paragraph listing them all; group them by mechanism.

**One short scope/limitations sentence:** cite Baik & Kim (2025) for endogenous disclosure; Lee & Wu (2026) and Gill (2008) optional if space.

**Model**: Hotelling (1929) as needed; price derivation independent. **Discussion**: use the exact comparison with Baik & Kim (2020) Sec. 7.3 and explain why \(\lambda D_1\) is essential.

See [citation_plan.md](citation_plan.md) for the minimum citation set and an English paragraph skeleton.

## Priority tasks before a novelty claim

1. Read **all proofs and proposition statements** of Kim & Poggi's *September 2026* revision; previous publicly available author PDF appears to be from May 2025.
2. Read Cabral & Riordan (1994) and Cohen & Levinthal (1994) deeply—**competition and learned ability are older and closer theoretical antecedents** than just recent accounting disclosure work.
3. Read the full propositions in Besanko et al. (2014, 2019), not merely abstract.
4. Re-derive Baik & Kim (2020) Section 7.3 inequality domains and compare **our P/H outcome mechanism** explicitly with theirs (their \(\theta\) threshold is not a universal R&D-disclosure result).
5. Audit all DOI/author fields for final publisher-ready BibTeX; do not silently treat bibliographic review as theorem audit.
6. Add relevant new literature discovered through **both forward/backward citation chasing**; a snapshot can be complete relative to prior discussions without being a systematic review.

## Source access and copyright

Links above point to publisher pages, DOI landing pages, author copies, or institution bibliographic records. This repo stores **our own summaries and citations, not copyrighted journal PDFs**. The 2026 unpublished papers have version and status caveats. **"F" means targeted inspection; no strong priority statement is authorized yet.**


## D. New Stage-6 parent-class threats (2026-11-10)

### D01. Fudenberg & Tirole (1984) — canonical strategic investment [A for generic-theory disclosure; bibliographic/standard-mechanism evidence]
Drew Fudenberg and Jean Tirole (1984), “The Fat-Cat Effect, the Puppy-Dog Ploy, and the Lean and Hungry Look,” *American Economic Review* 74(2), 361–366. [RePEc](https://ideas.repec.org/a/aea/aecrev/v74y1984i2p361-66.html); [MIT faculty bibliography](https://economics.mit.edu/people/faculty/drew-fudenberg/publications).

**Summary:** Pre-commitment in product markets shifts a follower's downstream reaction; an investment's strategic return can differ from its technological/direct return. Thus the **observability-induced price response** and related envelope term in our Proposition 1 are not an independently novel economic principle.

**Exact mapping:** learning-rate investment \(x=\lambda\), incumbent response \(y=p_{A1}^*(x)\), B payoff \(U_B(x,y)\); marginal public-hidden difference equals \(U_{By}y'(x)\). [Code](../code/stage6_strategic_commitment_identity.py).

**Status:** Published title/bibliography verified, abstract/secondary theoretical framework; full printed theorem wording not inspected. Cite in Introduction with Bulow et al.; do not claim novelty for a general strategic-commitment effect.

### D02. Bulow, Geanakoplos & Klemperer (1985) — strategic complements/substitutes [A; publisher/Stanford/Yale summary]
Jeremy I. Bulow, John D. Geanakoplos, and Paul D. Klemperer (1985), “Multimarket Oligopoly: Strategic Substitutes and Complements,” *Journal of Political Economy* 93(3), 488–511. [DOI](https://doi.org/10.1086/261312) | [Stanford GSB summary](https://www.gsb.stanford.edu/faculty-research/working-papers/multimarket-oligopoly-strategic-substitutes-complements).

**Summary:** Changes in costs/strategies spill across market decisions through strategic responses. Bertrand price complementarity and dynamic investment incentives are classic.

**Mapping:** our sign comes from a positive B-payoff response to a higher A price multiplied by the *negative* A price response to more observed learning efficiency, which is an instance of that general logic. The general result does not automatically imply our three-investment comparative statics and conditional consumer-welfare ranking.

**Status:** Journal/publisher and Stanford/Yale abstracts; full theorem-level mapping not yet closed. High-priority Stage-6 absorption threat; do not convert access limitations into an originality claim.

### D03. Kogan & El Ouardighi (2019) — autonomous plus induced learning under Bertrand pricing [A; full publisher HTML model/proposition excerpts]
Konstantin Kogan and Fouad El Ouardighi (2019), “Autonomous and Induced Production Learning under Price and Quality Competition,” *Applied Mathematical Modelling* 67, 74–84. [DOI](https://doi.org/10.1016/j.apm.2018.10.018) | [Institution](https://cris.biu.ac.il/en/publications/autonomous-and-induced-production-learning-under-price-and-qualit-4/).

**Model:** Differentiated duopoly with quality-hazard state \(\dot Y_i=\rho q_i(p_1,p_2)+\vartheta u_i\). Firms choose prices and induced-learning effort \(u_i\); autonomous learning coefficient \(\rho\) and induced coefficient \(\vartheta\) are **given**, not choices concealed/revealed as their own investment. They analyze commitment (open-loop) vs contingent (closed-loop) equilibrium controls with differences in quality-state observability, not exogenous P/H disclosure of a chosen learning-efficiency coefficient to a first-period rival.

**Results:** Autonomous/induced learning have opposing effects on pricing trajectories; effort and quality respond to current state and price dynamics, even with different initial quality. The combination of sales-driven quality learning + costly quality improvement + product-price competition is therefore **already in the literature**.

**Closest nonabsorption question:** Our specific ex-ante choice of \(\lambda\) multiplying *own current market share*, and information-regime-dependent A pricing in response to the **disclosure of that chosen \(\lambda\)**, are not strategy variables in their model. That is a proposed game-level difference, not proof of full originality over all related theories.

**Status:** Publisher model equation and numbered proposition text inspected in web full HTML; paper PDF unavailable through the normal web opening in this session. Cite in Introduction and discuss exact differences in Stage 6 report.

### Stage 6 outcome for all entries

See [STAGE6_NOVELTY_REKILL_2026-11-10.md](../audits/STAGE6_NOVELTY_REKILL_2026-11-10.md) for parent-theorem mapping and evidence depths. **Do not claim generic observability-wedge, firm-profit/welfare sign reversal, learning-by-doing strategic pricing, or autonomous-plus-induced quality learning is new.** The joint pure equilibrium under specifically disclosed learning-rate investment, two quality decisions, and future experience-based quality remains a **candidate** result pending full parent-theorem absorption review.
