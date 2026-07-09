---
title: "QuDAR: Query-Wise Dual-Perspective Adaptive Retrieval"
title_zh: "QuDAR: 查询双视角自适应检索"
authors: "Joeun Kim, Seunghyouk Yoon, Xuan-Bach Le, Youngeun Nam, Doyoung Kim, Hwanjun Song, Jae-Gil Lee"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.acl-long.1791.pdf"
tags: ["query:mr"]
score: 4.0
evidence: 面向RAG的查询自适应检索权重分配框架
tldr: 提出双视角自适应检索框架QuDAR，根据查询特性动态调整稀疏与稠密检索器的权重以及查询扩展策略。该方法利用置信度评分实现自适应权重分配。实验证明能有效提升RAG系统的检索性能。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1791/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 745, \"height\": 279, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1791/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 802, \"height\": 418, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1791/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 802, \"height\": 418, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1791/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 801, \"height\": 671, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1791/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 810, \"height\": 396, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1791/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1648, \"height\": 435, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1791/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 798, \"height\": 655, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1791/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 797, \"height\": 675, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1791/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 800, \"height\": 674, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1791/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 811, \"height\": 396, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1791/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 813, \"height\": 396, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1791/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 810, \"height\": 396, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1791/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 745, \"height\": 279, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1791/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 791, \"height\": 944, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1791/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1576, \"height\": 780, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1791/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1576, \"height\": 814, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1791/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1414, \"height\": 564, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1791/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 809, \"height\": 290, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1791/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1625, \"height\": 836, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1791/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1624, \"height\": 836, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1791/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1624, \"height\": 836, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1791/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1625, \"height\": 641, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1791/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1408, \"height\": 272, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1791/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1378, \"height\": 598, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1791/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1375, \"height\": 598, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1791/table-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1376, \"height\": 600, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1791/table-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1375, \"height\": 599, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1791/table-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 1377, \"height\": 601, \"label\": \"Table\"}]"
motivation: 现有RAG混合检索方法使用固定权重，无法适应查询差异。
method: 提出双视角自适应框架，动态分配检索器类型和查询格式的权重。
result: 实验表明动态权重分配提升了检索效果。
conclusion: 自适应机制能有效应对RAG中的查询差异性问题。
---

## Abstract
Retrieval-augmented generation(RAG) systems depend on retrieval modules to supply grounding evidence for large language models. While hybrid approaches combining sparse and dense retrievers improve performance, most rely on fixed weights that ignore query-specific and corpus-specific variation. Similarly, query expansion has long been used to enrich recall, but its integration with original queries is usually static and can introduce noise. We present QuDAR, a dual-perspective adaptive retrieval framework that adapts along two perspectives: retriever type (sparse vs. dense) and query format (original vs.expanded). Leveraging margin-derived confidence (e.g., top-1–top-2 score gaps) and blind LLM-based relevance scoring, QuDAR dynamically assigns query-specific weights, fusing lexical specificity with semantic breadth while mitigating noise. QuDAR is lightweight, retriever-agnostic, and broadly applicable. Experiments show consistent gains over static baselines, improving overall retrieval quality and yielding more stable performance across queries.

---

## 论文详细总结（自动生成）

# 论文总结：QuDAR: 查询双视角自适应检索

## 1. 核心问题与整体含义（研究动机和背景）

- **背景**：检索增强生成（RAG）系统依赖检索模块为 LLM 提供事实证据。混合检索（稀疏检索+稠密检索）和查询扩展被广泛使用，但现有方法普遍采用**固定权重**，忽略了不同查询、语料库对检索策略的差异化需求。  
- **问题**：检索器的效果受**检索器类型**（稀疏 vs 稠密）和**查询格式**（原始查询 vs 扩展查询）两个维度共同影响，且两者之间存在交互作用。固定静态权重无法适应这种变化，导致检索性能不稳定。  
- **目标**：提出一种**查询级双视角自适应框架**，能够动态地为每个查询分配合理权重，融合不同检索信号的互补优势，减轻噪声影响，提升检索质量以及下游 RAG 任务的生成效果。

## 2. 论文提出的方法论

- **核心思想**：从**检索器类型**（稀疏 vs 稠密）和**查询格式**（原始 vs 扩展）两个视角出发，将四种检索结果（原始-稀疏、原始-稠密、扩展-稀疏、扩展-稠密）进行加权融合，权重随查询动态调整。  
- **整体框架（图6）**：  
  1. 对每个查询，分别用稀疏和稠密检索器对原始查询和扩展查询进行检索，得到四个排序列表。  
  2. 采用三种权重确定策略之一，计算每个列表的权重（和为1）。  
  3. 加权融合得到最终混合检索结果。  
- **三种权重策略（均为训练无关）**：  
  - **QuDAR-simple**：  
    - **RRF（互惠排名融合）**：基于排名位置加权，平滑各列表贡献。  
    - **Equal-weight**：直接对四个列表的归一化得分取平均。  
  - **QuDAR-confidence**（基于置信度）：利用每个检索结果中 top-1 与 top-2 得分的差（margin）作为置信度指标，通过带温度的 softmax 归一化为权重。公式：  
    \( m_i = \max(score_{i,1} - score_{i,2}, 0) \) → \( w_i = \exp((m_i + \epsilon)/\tau) / \sum_j \exp((m_j + \epsilon)/\tau) \)。  
  - **QuDAR-llm**（基于 LLM 评分）：将四个列表的 top-1 文档匿名混洗后，用 LLM（gpt-4o-mini）从0-5打评分，再 softmax 归一化得权重。  
- **特点**：框架轻量、与具体检索器无关（retriever-agnostic），无需训练。

## 3. 实验设计

- **数据集**：  
  - **检索评估**：BEIR 基准中的四个数据集——FiQA（金融QA）、SciDocs（科学文献）、HotpotQA（多跳QA）、Climate-FEVER（气候事实核查）。  
  - **生成评估**：从 FiQA 和 HotpotQA 各随机抽取500条查询，用 Qwen2.5-7B 作为生成器，用 LLM 评估生成质量。  
- **检索器配置**：  
  - 稀疏：BM25。  
  - 稠密：主实验用 Contriever；额外泛化实验用 E5-base、BGE-M3。  
  - 扩展查询：由 LLaMA 3.1-8B 生成自包含段落。  
- **对比方法**：  
  - 四个独立检索器（OS、OD、ES、ED）。  
  - 单视角混合方法：  
    - 检索器类型混合（仅原始查询）：静态平均、网格搜索最优权重、DAT（动态 Alpha 调优）。  
    - 查询格式混合（固定检索器）：静态平均、网格搜索最优权重。  
  - 双视角混合：静态平均、网格搜索最优权重、QuDAR 三种变体。  
- **指标**：Recall@10、nDCG@10、Precision@1；生成任务用 LLM 评估分数。

## 4. 资源与算力

- 论文**未明确说明**训练所需 GPU 型号、数量或训练时长。  
- QuDAR 本身**无需训练**，仅推理阶段。但涉及查询扩展（LLaMA 3.1-8B）和 LLM 评分（gpt-4o-mini），因此有少量推理开销。  
- 文中给出了 gpt-4o-mini 评分每查询的耗时（约0.7秒）、token数（约600-1300）和成本（约1.7e-4 美元），表明开销可接受。

## 5. 实验数量与充分性

- **主检索实验**：在4个数据集上、3种指标、对比了4个独立检索器、4个单视角基线、2个双视角静态基线及3个 QuDAR 变体，共约12组对比。  
- **生成实验**：在2个数据集（各500条）上验证，对比了代表性方法。  
- **泛化实验**（附录F）：更换稀疏（SPLADE++）、稠密（E5-base, BGE-M3）及扩展方法（HyDE, PRF），共4种额外配置，验证结论的普适性。  
- **消融分析**（附录H）：对比单视角 LLM 加权与双视角，说明双视角胜过单视角。  
- **充分性**：实验覆盖多领域、多检索器、多扩展策略，且包含下游生成验证，**较为充分**。但未在更大规模真实RAG系统（如多轮对话）中评估，且生成实验仅500条，规模略小。  
- **公平性**：固定检索器、统一扩展生成方式（同一种prompt），对比基线均为公开方法，**公平合理**。

## 6. 主要结论与发现

1. **固定权重不可行**：最优稀疏-稠密权重随数据集和检索器变化，且在不同查询之间差异巨大（图2-4）。  
2. **查询扩展是双刃剑**：混合原始与扩展查询通常好于单独使用，但最优比例同样随查询变化（图3）。  
3. **双视角交互不是加法**：两个视角之间存在组合效应，联合动态调整能解锁更大的性能空间（图5）。  
4. **QuDAR 显著优于静态方法**：在全部四个 BEIR 数据集上，Recall@10 提升12–16%（vs 最佳独立检索器），最高达30%（vs 静态平均）。生成质量也提升6–10%（vs 单视角方法）。  
5. **QuDAR-llm 效果最强**，但 QuDAR-confidence 和 QuDAR-simple 也表现稳健，且无需额外 LLM 调用，成本更低。

## 7. 优点

- **视角新颖**：首次系统地将“检索器类型”和“查询格式”两个维度联合考虑，并证明其组合效应。  
- **方法轻量**：所有策略无需训练，且与检索器无关，易于集成到现有RAG流水线。  
- **实验充分**：覆盖多数据集、多检索器、多扩展方法，并验证了生成质量。  
- **分析深入**：在动机部分通过大量实验揭示了静态混合的局限性，对后续研究具有启发意义。

## 8. 不足与局限

- **未能达到理论上下界**：文中自身承认，动态加权策略未能完全达到查询级最优上界，仍有提升空间（如引入学习式预测器）。  
- **扩展策略有限**：仅使用了 HyDE/PRF 等少数扩展方法，未穷尽所有可能性。  
- **生成评估规模有限**：仅500条查询，且使用单一 LLM 评估，可能存在偏差。  
- **未讨论极端场景**：当某一视角信号完全主导时，双视角策略可能不如仅优化单视角（文中少量案例已体现）。  
- **计算开销的问题**：QuDAR-llm 依赖 GPT-4o-mini 调用，虽然单次成本低，但在大规模实时系统下仍可能成为瓶颈；开源替代方案（如本地 LLM）未测试。  
- **仅涉及检索阶段**：未考虑改写、重排序等其他 RAG 模块的协同优化。

（完）
