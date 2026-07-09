---
title: "TH-RAG : Topic-Based Hierarchical Knowledge Graphs for Robust Multi-hop Reasoning in Graph-based RAG Systems"
title_zh: TH-RAG：基于主题层次知识图的鲁棒多跳推理增强检索生成
authors: "JungHyoun Kim, Soohyeong Kim, Seok Jun Hwang, Jeonghyeon Park, Yong Suk Choi"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.acl-long.1740.pdf"
tags: ["query:mr"]
score: 9.0
evidence: 基于主题层次知识图增强图RAG的多跳推理
tldr: 图RAG通过知识图增强多跳推理，但LLM生成的三元组图往往碎片化且连接稀疏。TH-RAG提出层次化框架，将三元组组织为主题子图，构建多粒度知识结构，提升推理连贯性。实验表明，该方法在多个多跳问答任务上优于现有图RAG方法，且计算开销更低。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1740/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 801, \"height\": 430, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1740/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1639, \"height\": 756, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1740/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1577, \"height\": 652, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1740/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1599, \"height\": 690, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1740/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1575, \"height\": 987, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1740/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 797, \"height\": 658, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1740/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 802, \"height\": 1002, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1740/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 813, \"height\": 282, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1740/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1651, \"height\": 445, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1740/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1639, \"height\": 285, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1740/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 752, \"height\": 427, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1740/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 708, \"height\": 210, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1740/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 797, \"height\": 217, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1740/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 839, \"height\": 208, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1740/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 620, \"height\": 210, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1740/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 819, \"height\": 173, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1740/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1657, \"height\": 519, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1740/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 802, \"height\": 176, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1740/table-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1648, \"height\": 1752, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1740/table-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1100, \"height\": 171, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1740/table-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 1118, \"height\": 171, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1740/table-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 1264, \"height\": 208, \"label\": \"Table\"}]"
motivation: LLM生成的三元组图碎片化且连接稀疏，影响多跳推理连贯性。
method: 提出基于主题的层次化知识图框架，将三元组组织成主题子图，增强连通性和语义一致性。
result: 相比现有图RAG方法，TH-RAG在多跳问答上精度更高且计算成本更低。
conclusion: 层次化主题结构有效改善了图RAG中知识图的语义连接和推理路径质量。
---

## Abstract
Retrieval-augmented generation (RAG) enables large language models (LLMs) to incorporate external knowledge at inference. Graph-based RAG extends this by organizing corpora into knowledge graphs, improving multi-hop reasoning and offering a global understanding of the corpus. However, triplet-based graphs generated by LLMs are often fragmented and sparsely connected, which reduces coherence and hinders reasoning. Prior enrichment methods such as clustering, community detection, or approximate graph algorithms attempt to restore connectivity but incur high computational cost and risk semantic distortion. To address these issues, we propose TH-RAG, a hierarchical framework that organizes triplets into subtopics and topics, enhancing connectivity, integrating dispersed information, and supporting robust multi-hop reasoning. Experiments on abstractive and specific QA benchmarks show that TH-RAG outperforms strong baselines in accuracy and robustness while remaining efficient, providing a scalable foundation for graph-based RAG.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机与背景）

*  **研究背景**：检索增强生成（RAG）通过引入外部知识提升LLM推理能力；基于图的RAG（Graph-based RAG）将语料组织为知识图谱，改善多跳推理和全局理解。
*  **核心问题**：LLM生成的三元组（triplet）图往往碎片化严重、连接稀疏，导致语义连贯性差、推理路径中断。现有增强方法（聚类、社区检测、近似图算法）虽有改善但计算开销高且存在语义失真风险。
*  **整体含义**：论文提出TH-RAG，通过构建主题（Topic）—子主题（Subtopic）—三元组（Triplet）的三层层次化知识图谱，以极低的额外代价增强图连通性，同时保留原始语料信息，实现鲁棒高效的多跳推理。

## 2. 方法论

### 核心思想
*  构建层次化知识图谱：三个节点类型——实体（Entity）、子主题（Subtopic）、主题（Topic），形成语义包含层次（Topic ⊃ Subtopic ⊃ Entity）。
*  主题/子主题通过LLM在提取三元组时同时生成，仅需一次LLM调用/块，不引入额外聚类或摘要，避免信息损失和高计算成本。

### 关键技术细节
*  **层次图构建（Algorithm 1）**：对每个语料块，LLM提取三元组，并为每个实体分配子主题和主题；边包括：实体-实体（带源句子属性）、子主题-实体、主题-子主题。
*  **基于主题的图遍历（Algorithm 2）**：两阶段LLM引导选择：
  1. 主题选择：从所有主题中选出与查询最相关的N_T个主题。
  2. 子主题选择：对每个主题，选出最相关的N_ST个子主题。
  选择过程依赖LLM对候选列表的判断，利用LLM长上下文能力，仅需N_T+1次调用。
*  **基于查询的检索与过滤**：
  * 从选定的子主题收集所有实体，扩展1跳邻居，收集所有带源句子的边。
  * 两阶段过滤：余弦相似度筛选Top-K₁句子作为主要上下文；再从其中选Top-K₂句子并扩展其完整块作为扩展上下文。
*  **鲁棒性机制**：每个边保留原始句子，避免信息丢失；上下文扩展缓解实体遗漏；层次结构避免依赖直接实体连接。

## 3. 实验设计

### 数据集/场景
*  **抽象式QA**：UltraDomain（农业、CS、法律、混合4个领域，每个125个问题，长段落）。
*  **具体式QA**：MultiHop-RAG（435篇文档，2.3K QA，长段落）和HotpotQA（9.8K段落，1K QA，短段落，Distractor设置）。
*  **大规模集成实验**：合并上述6个数据集（~11M tokens）测试扩展性。

### Benchmark与对比方法
*  **Baselines**：NaiveRAG、GraphRAG（Global & Local）、LightRAG、PathRAG、HyperGraphRAG；额外对比HippoRAG2（仅HotpotQA）。
*  **评估指标**：
  * UltraDomain：LLM-as-a-judge 1-vs-1胜率（综合、多样性、授权）。
  * 具体QA：F1、Precision、Recall、Accuracy；检索指标：Recall、F1、Rec@5、NDCG@5。

## 4. 资源与算力

*  论文使用了 **GPT-4o-mini**（OpenAI API）进行所有LLM调用（图构建、选择、答案生成），以及 **text-embedding-3-small** 进行嵌入。
*  **未明确说明**使用的具体GPU型号、数量、训练时长等信息，因为方法基于API调用，无本地训练。计算成本以LLM调用次数和token消耗衡量。
*  索引阶段：TH-RAG仅需902次LLM调用，2.3M token（以MultiHop-RAG为例），远低于LightRAG（5,978次调用，8M token）和HyperGraphRAG（2,772次调用，20.3M token）。
*  查询阶段：TH-RAG平均耗时3.54秒，上下文token 7.4K，效率良好。

## 5. 实验数量与充分性

*  **主要实验**：UltraDomain四个领域（每个125个问题）的6组对比，结果以胜率表呈现；MultiHop-RAG和HotpotQA上分别报告了答案质量和检索质量指标（共两组）。
*  **消融实验**：去除了块（chunks）、三元组、图遍历三个组件的效果对比（MultiHop-RAG上Accuracy从0.722降至0.580/0.692/0.624）。
*  **超参数分析**：对K₁和K₂进行网格搜索（K₁=5,10,30,50；K₂=1,3,5,10）。
*  **图结构分析**：对比TH-RAG与LightRAG的图统计（节点数、边数、子图数量、最大连通子图占比）。
*  **问题类型分析**：MultiHop-RAG上按Temporal/Inference/Comparison/Null类型比较TH-RAG与HyperGraphRAG。
*  **大规模实验**：集成6个数据集（~11M tokens）验证扩展性。
*  **额外对比**：在HotpotQA上与HippoRAG2比较。
*  **充分性评价**：实验覆盖多种数据集类型（长/短段落、抽象/具体）、多种基线、多种分析维度，设计公平（统一chunk大小、相同LLM和嵌入模型、统一答案生成prompt），结论可靠。

## 6. 主要结论与发现

*  TH-RAG在 **UltraDomain** 上全面超越除HyperGraphRAG外的所有基线，尤其在混合域上胜率高达90%以上；在 **MultiHop-RAG** 上F1达0.712，优于最佳基线HyperGraphRAG（0.526）及NaiveRAG（0.501）；在**HotpotQA**上F1=0.671，优于所有基线。
*  TH-RAG的层次结构显著减轻了图碎片化：与LightRAG相比，最大连通子图占比从56.11%提升至99.98%，子图数量从8,805降至约3个。
*  消融和超参数分析证实了主题-子主题遍历策略、块扩展、三元级信息均至关重要；K₂增大至10可进一步提升性能，但过大会因“上下文迷失”而下降。
*  效率分析表明TH-RAG在索引和查询阶段均具有更低的LLM调用次数和token消耗，同时保持高性能。

## 7. 优点

*  **创新性**：首次提出基于主题-子主题-实体的三层次层次化图RAG框架，直接在LLM提取三元组时同步生成主题/子主题，无额外聚类开销，同时保留原始句子证据。
*  **鲁棒性**：层次遍历+上下文扩展机制有效应对图碎片化和实体遗漏；不依赖实体-实体直接连接，通过语义层次检索信息。
*  **效率与可扩展性**：索引成本极低（一次LLM调用/块），查询仅需N_T+1次LLM调用；在大规模语料（~11M token）中主题数量亚线性增长，保持O(N_T)复杂度。
*  **全面性**：在多种QA任务（抽象式、具体式、长/短段落）上均实现最先进性能，且消融和超参数分析深入。

## 8. 不足与局限

*  **主题/子主题不一致**：LLM输出的主题/子主题标签存在同义不同名问题（如sports/sport），导致图结构膨胀。论文尝试预设schema但效果不佳，未来需嵌入聚类归一化。
*  **未集成常见RAG增强技术**：如查询扩展、重排序等未使用，以隔离层次结构的贡献。若整合可能进一步提升性能。
*  **LLM依赖性**：仅评估GPT-4o-mini，未测试其他LLM。论文提及更强/弱LLM会影响性能，但变化幅度与NaiveRAG类似。
*  **潜在偏差**：LLM-as-a-judge评估UltraDomain可能引入偏好偏差，但作者同时使用客观指标（F1等）弥补。
*  **应用限制**：需要LLM支持长上下文以处理主题/子主题候选列表；虽使用small模型，但API调用仍依赖外部服务。

（完）
