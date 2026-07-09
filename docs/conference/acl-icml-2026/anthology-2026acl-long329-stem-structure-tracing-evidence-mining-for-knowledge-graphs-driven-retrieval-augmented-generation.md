---
title: "STEM: Structure-Tracing Evidence Mining for Knowledge Graphs-Driven Retrieval-Augmented Generation"
title_zh: STEM：面向知识图谱驱动检索增强生成的结构追踪证据挖掘
authors: "Peng Yu, En Xu, Bin Chen, Haibiao Chen, Yinfei Xu"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.acl-long.329.pdf"
tags: ["query:mr"]
score: 9.0
evidence: 将多跳推理重构为知识图谱上的模式引导图搜索
tldr: 知识图谱问答中多跳推理面临结构异构和缺乏全局视角的问题，本文提出STEM，通过语义到结构的投影将查询分解为原子关系断言并构建自适应查询模式图，将多跳推理转化为模式引导的图搜索，显著提升了复杂推理的准确性和效率。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.329/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 781, \"height\": 579, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.329/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1612, \"height\": 981, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.329/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1614, \"height\": 572, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.329/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1434, \"height\": 386, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.329/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1453, \"height\": 428, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.329/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 782, \"height\": 590, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.329/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 780, \"height\": 599, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.329/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 753, \"height\": 593, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.329/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 754, \"height\": 592, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.329/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 769, \"height\": 835, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.329/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 764, \"height\": 577, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.329/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 777, \"height\": 404, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.329/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 763, \"height\": 1427, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.329/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 797, \"height\": 1231, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.329/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 800, \"height\": 259, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.329/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 640, \"height\": 264, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.329/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 743, \"height\": 262, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.329/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 639, \"height\": 126, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.329/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 795, \"height\": 245, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.329/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 765, \"height\": 278, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.329/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1257, \"height\": 196, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.329/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1014, \"height\": 198, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.329/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 445, \"height\": 413, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.329/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 808, \"height\": 235, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.329/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 519, \"height\": 237, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.329/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 629, \"height\": 195, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.329/table-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 784, \"height\": 152, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.329/table-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 419, \"height\": 154, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.329/table-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 715, \"height\": 196, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.329/table-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 1547, \"height\": 588, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.329/table-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 1547, \"height\": 491, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.329/table-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 1546, \"height\": 680, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.329/table-020.webp\", \"caption\": \"\", \"page\": 0, \"index\": 20, \"width\": 1542, \"height\": 1113, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.329/table-021.webp\", \"caption\": \"\", \"page\": 0, \"index\": 21, \"width\": 1548, \"height\": 800, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.329/table-022.webp\", \"caption\": \"\", \"page\": 0, \"index\": 22, \"width\": 1546, \"height\": 794, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.329/table-023.webp\", \"caption\": \"\", \"page\": 0, \"index\": 23, \"width\": 1546, \"height\": 903, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.329/table-024.webp\", \"caption\": \"\", \"page\": 0, \"index\": 24, \"width\": 668, \"height\": 277, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.329/table-025.webp\", \"caption\": \"\", \"page\": 0, \"index\": 25, \"width\": 602, \"height\": 254, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.329/table-026.webp\", \"caption\": \"\", \"page\": 0, \"index\": 26, \"width\": 632, \"height\": 254, \"label\": \"Table\"}]"
motivation: KGQA中多跳推理存在语义匹配不足和缺乏全局结构视角。
method: 设计语义到结构投影构建查询模式图，将推理转化为图搜索。
result: 在多个KGQA数据集上性能领先。
conclusion: STEM为KG驱动的多跳推理提供了有效框架。
---

## Abstract
Knowledge Graph-based Question Answering (KGQA) plays a pivotal role in complex reasoning tasks but remains constrained by two persistent challenges: the structural heterogeneity of Knowledge Graphs(KGs) often leads to semantic mismatch during retrieval, while existing reasoning path retrieval methods lack a global structural perspective. To address these issues, we propose Structure-Tracing Evidence Mining (STEM), a novel framework that reframes multi-hop reasoning as a schema-guided graph search task. First, we design a Semantic-to-Structural Projection pipeline that leverages KG structural priors to decompose queries into atomic relational assertions and construct an adaptive query schema graph. Subsequently, we execute globally-aware node anchoring and subgraph retrieval to obtain the final evidence reasoning graph from KG. To more effectively integrate global structural information during the graph construction process, we design a Triple-Dependent GNN (Triple-GNN) to generate a Global Guidance Subgraph (Guidance Graph) that guides the construction. STEM significantly improves both the accuracy and evidence completeness of multi-hop reasoning graph retrieval, and achieves State-of-the-Art performance on multiple multi-hop benchmarks.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：知识图谱问答（KGQA）中的多跳推理任务面临两大障碍：  
  1. **结构异构性**：语言模型生成的推理计划与KG的实际模式存在“语义-结构鸿沟”，导致“模式幻觉”（schema hallucination）——生成的逻辑关系在KG中不存在。  
  2. **缺乏全局视角**：现有方法（如路径解码、逐步搜索）依赖局部语义相似性或LLM逐步决策，容易产生路径偏移、枢纽节点膨胀和信息碎片化，难以找回完整的证据子图。  
- **整体含义**：作者提出 STEM 框架，将多跳推理从顺序路径查找**重新定义为模式引导的子图匹配**，通过显式构造查询模式图并引入全局结构先验，实现精准、完整的证据子图检索。

### 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程

- **核心思想**：将自然语言查询转化为与KG拓扑结构对齐的**模式图**（schema graph），然后在该图指导下进行**全局感知的子图匹配**。  
- **关键技术细节**（三个主要模块）：

  - **语义 - 结构投影流水线**（Semantic-to-Structural Projection）：  
    - Schema-Grounded Decomposition Agent（SGDA）：将原始多跳问题分解为一系列原子关系断言（atomic relational assertions），并使用占位符 `[ENTX]` 保持实体链接的连续性。同时判别回答策略（Precision 或 Breadth）。  
    - Symbol-Aligned Graph Builder（SAGB）：将每个断言映射为KG中的标准三元组（实体、关系、实体），并组合成**模式图** \(G_{sch}\)。  
    - 训练数据来自“结构-查询反向生成”（Structure-to-Query Reverse Generation）进行数据增强。

  - **全局指导子图**（Global Guidance Subgraph）：  
    - 使用 Triple-Dependent GNN（Triple-GNN），将模式图中的三元组嵌入 \(E_T\) 通过平均池化得到查询表示 \(E_Q\)，作为实体初始特征的种子。  
    - 经过 L 层消息传递后，通过 MLP + Sigmoid 得到实体概率分布 \(P_Q\)，选择 Top-K 实体构建候选实体列表 \(N'_Q\)，再连接其关系形成**全局指导子图** \(G'_Q\)。

  - **结构追踪子图检索**（Structure-Tracing Subgraph Retrieval）：  
    - 对于每个问题实体，先检索 Top-N 最相似实体，并用**全局结构一致性偏置**（Entity-level Bias \(I_{Ent}\) 和 Triple-level Bias \(I_{Tri}\)）修正分数。  
    - 从模式图与KG的锚点匹配开始，递归执行**边匹配**，计算全局感知的三元组分数 T-Score（语义相似度 + Triple Bias）。  
    - 根据策略不同：Precision 使用贪婪选择（取最高分边），Breadth 使用阈值选择（保留超过阈值 \(\theta\) 的所有边）以收集多个答案。

- **公式与算法流程**（文字说明）：  
  - 查询表示：\(E_Q = \frac{1}{N}\sum E_{t_i}\)  
  - 实体嵌入：\(H_L^Q = \text{Triple-GNN}(G, H_e^0, H_r^0)\)  
  - 实体概率：\(P_Q = \text{Sigmoid}(\text{MLP}(H_L^Q))\)  
  - 实体偏置：\(I_{Ent}(e) = 1.5\)（若 \(e \in G'_Q\) 否则 1）  
  - 三元组偏置：\(I_{Tri}(t) = 0.5\)（若 \(t \in G'_Q\) 否则 0）  
  - T-Score = 余弦相似度 + \(I_{Tri}\)

### 3. 实验设计：数据集、Benchmark、对比方法

- **数据集**：  
  - WebQSP（~1,628 测试样本，1–2 跳）  
  - CWQ（~3,531 测试样本，1–4 跳）  
  - 均采用 Freebase 作为背景KG，使用 RoG 公开的子图格式。

- **基准方法**（分为四类）：  
  - 纯 LLM：GPT-4o（zero-shot、few-shot、CoT）  
  - 微调方法：NSM、DeCAF、KD-CoT、RoG（LLaMA2-7B/LLaMA3.1-70B/GPT-4o）、GRAG、LightProf  
  - 提示方法：Kaping、ToG、G-Ret、PoG、ReKnoS、MFC、SubgraphRAG、FiDeLiS、ProgRAG、GNN-RAG 等  
  - 本文提出的 STEM + LLaMA3.1-8B/70B/GPT-4o

- **评估指标**：Hit@1、F1 Score

### 4. 资源与算力

- **训练**：SGDA、SAGB 使用 Qwen3-8B 进行微调，Triple-GNN 参数约 10M。所有训练在 **1 台 4×NVIDIA H100 GPU** 上进行，使用 Bfloat16 精度和 AdamW 优化器。  
- **训练时长**：SGDA 和 SAGB 各训练 2 个 epoch，Triple-GNN 训练 2 个 epoch。具体耗时未明确给出。  
- **推理**：结构-结构投影共 2B 次 LLM 调用（SGDA 一次 + SAGB B 次，B=4），GNN 1 次前向传播，子图检索并行执行，最终 LLM 推理一次。

### 5. 实验数量与充分性

- **主要对比**：在 WebQSP 和 CWQ 两个基准上对比了 20+ 种方法，覆盖纯 LLM、微调和提示方法。  
- **消融实验**：  
  - 去掉语义-结构投影（用 LLM 直接生成模式图）  
  - 去掉全局结构一致性偏置（仅实体偏置、仅三元组偏置、两者皆无）  
  - 不同回答策略（仅贪婪、仅阈值、自适应）  
  - 不同初始实体数 K'（1–6）  
  - 不同 Beam Size B（1–7）  
  - 是否使用反向生成数据增强  
  - 指导图偏置参数 λ 和 τ 的网格搜索  
- **细粒度分析**：按答案数量（1/2–4/5–9/≥10）、推理跳数（1/2/≥3）分层。  
- **案例研究**：7 个典型样本的端到端推理过程分析。  
- **效率对比**：与 FiDeLiS、PoG、RoG、GNN-RAG 比较平均推理延迟。  
- **错误传播分析**：构建 Schema 正确性 vs QA 正确性、子图正确性 vs QA 正确性两个混淆矩阵。  
- **充分性**：实验设计较为全面，覆盖性能、鲁棒性、可解释性、效率；但未提及跨域迁移性实验到其他KG。

### 6. 论文的主要结论与发现

1. STEM 在 WebQSP 和 CWQ 上均取得 SOTA：STEM+GPT-4o 在 WebQSP 上 Hit@1 达 90.94%，CWQ 上 Hit@1 达 74.09%，显著优于所有基线。  
2. 语义-结构投影流水线相比直接使用 LLM 生成模式图，Hit@1 提升约 24%（CWQ）。  
3. 全局结构一致性偏置（尤其是三元组级偏置）对性能至关重要，去除后 CWQ Hit@1 下降约 10%。  
4. 反向生成数据增强使模式图生成 Recall 提升约 15%，对复杂多跳问题增益显著。  
5. STEM 的推理延迟（平均 5–6 秒）远低于交互式方法（FiDeLiS 约 35 秒），仅略高于纯生成/检索方法，但以较小效率代价换来大幅精度提升。

### 7. 优点

- **创新性**：首次将多跳推理重构为模式引导的子图匹配，从根本上解决语义-结构鸿沟。  
- **完整性**：通过模式图 + 全局指导子图实现全局结构先验，避免局部优化导致的证据碎片化。  
- **鲁棒性**：多个候选计划、模糊语义匹配和指导图校正机制共同构成容错链条，案例分析展示了其在复杂场景下的纠偏能力。  
- **高效性**：离线模式生成 + 一次 GNN 前向传播，避免逐跳 LLM 调用，实际成本低于交互式方法。  
- **可解释性**：模式图和检索过程可显式可视化，便于调试和理解。

### 8. 不足与局限

- **领域依赖**：方法需要对目标KG的模式进行预训练（微调 SGDA/SAGB），并非零样本通用方法。  
- **扩展性**：Breadth 策略下的阈值扩展导致计算延迟增加，虽有必要但影响效率。  
- **实验局限**：只在 Freebase 的两个数据集上评估，未在 Wikidata、DBpedia 等其他KG上验证跨域迁移性。  
- **潜在偏差**：KG本身（如 Freebase）存在人口、地理和文化偏斜，STEM 忠实检索子图，可能传播这些偏斜。  
- **错误传播**：虽然分析了错误传播（约 16% 的QA失败来自上游规划错误），但上游误差仍可能影响下游，尤其当所有候选模式都不正确时。

（完）
