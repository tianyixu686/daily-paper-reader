---
title: "PROGRAM: Programmatic Retrieval Optimization with Generative Reasoning and Augmented Multi-queries"
title_zh: PROGRAM：基于生成推理和增强多查询的程序化检索优化
authors: "Gun Il Kim, Jungkyu Shin, Jong Wook Kim, Beakcheol Jang"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.1090.pdf"
tags: ["query:mr"]
score: 8.0
evidence: 面向多跳推理的程序化检索优化
tldr: 现有RAG方法在多跳推理中依赖非结构化语义匹配，缺乏逻辑引导。PROGRAM提出程序化检索框架，通过程序类型选择、迭代剪枝和重排序，将检索转化为逻辑、时序等特定程序执行。在五个基准上，PROGRAM显著提升了多跳推理的检索准确性和答案质量。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1090/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 757, \"height\": 702, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1090/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1598, \"height\": 1173, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1090/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 780, \"height\": 865, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1090/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 784, \"height\": 638, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1090/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 747, \"height\": 2317, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1090/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 803, \"height\": 458, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1090/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1655, \"height\": 515, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1090/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1652, \"height\": 511, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1090/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1652, \"height\": 514, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1090/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1652, \"height\": 515, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1090/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 798, \"height\": 250, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1090/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1646, \"height\": 531, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1090/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 798, \"height\": 232, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1090/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 490, \"height\": 250, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1090/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1444, \"height\": 370, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1090/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 725, \"height\": 344, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1090/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 793, \"height\": 249, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1090/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1645, \"height\": 531, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1090/table-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1641, \"height\": 528, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1090/table-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1644, \"height\": 529, \"label\": \"Table\"}]"
motivation: 多跳推理需要结构化检索，但现有RAG缺乏逻辑引导，检索效果受限。
method: 提出PROGRAM框架，通过程序类型选择、迭代证据积累和重排，将检索视为程序执行。
result: 在五个多跳QA数据集上，PROGRAM在检索召回率和最终答案准确率上均取得最优结果。
conclusion: 程序化检索为复杂推理提供了可解释的检索逻辑，是多跳RAG的有效范式。
---

## Abstract
Current retrieval-augmented generation (RAG) methods struggle with complex multi-hop reasoning, relying on unstructured semantic matching that lacks the logical structure needed to systematically guide retrieval. We introduce Programmatic Retrieval Optimization with Generative Reasoning and Augmented Multi-queries (PROGRAM), a novel framework that elevates retrieval to structured, program-guided reasoning. PROGRAM treats retrieval as execution of specific program types, such as logical, temporal, causal, and so forth, through three stages of ’Program-Type Selection’ with dual-metric optimization, ’Iterative Active Program Pruning’ with evidence accumulation, and ’Final Answer Generation’ with reranking. Evaluated on five benchmarks including HotPotQA, 2WikiMultihopQA, ARC-Challenge, MMLU-Pro, and MedQA with various LLMs, PROGRAM achieves state-of-the-art performance with up to 24% relative improvement on HotPotQA and 13.2% on MedQA over strong baselines including FLARE, ProbTree and Self-RAG.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **问题**：当前检索增强生成（RAG）方法在处理复杂多跳推理时，依赖非结构化的语义匹配（如 token 级置信度或通用语义相似度），缺乏逻辑结构来系统性地引导检索过程。例如，因果比较、时序推理、argmax/argmin 等不同问题类型需要截然不同的检索策略，但现有方法（如 FLARE、Self-RAG）将它们视为同质化的相似度搜索，导致检索质量低下。
- **背景**：尽管 RAG 在知识密集型问答中取得显著进展，但推理复杂性增加时，非结构化匹配成为瓶颈。近期工作如 Chain-of-Thought、Tree-of-Thought 以及程序化推理（Program-of-Thoughts、DSPy）展示了结构化推理的优势，但尚未将程序化思想引入检索过程本身。
- **整体含义**：论文提出将检索从非结构化匹配提升为程序引导的推理，通过显式定义逻辑、时序、因果等程序类型，使检索语义对齐推理需求，从而改善多跳和领域特定推理。

## 2. 论文提出的方法论

### 2.1 核心思想
- **PROGRAM（Programmatic Retrieval Optimization with Generative Reasoning and Augmented Multi-queries）**：将检索视为执行特定程序类型（如逻辑、时序、因果等）的过程，通过结构化程序来引导检索路径，而非通用相似度搜索。
- 框架分为三个主要阶段：程序类型选择（PTS）、迭代主动程序剪枝（IAPP）、最终答案生成（FAG）。

### 2.2 关键技术细节

#### 阶段一：程序类型选择（PTS）—— 双指标优化
- 从预定义的程序类型库中选择适用类型（基础型：Simple Fact, ArgMax, Logical AND/OR, Causal, Temporal 等；高级型：Multi-hop, Entity-Linking, Diagnosis, Treatment Reasoning 等）。
- 针对每个程序类型 \( p_i \)，生成 \( M \) 个候选子查询 \( C_i = \{c_1, \dots, c_M\} \)。
- 使用两个指标评估每个候选子查询：
  - **信息增益（Information Gain, \( S_{IG} \)）**：用 KL 散度衡量子查询相对于仅使用程序类型时的新信息增量。
  - **语义分数（Semantic Score, \( S_{sem} \)）**：衡量子查询与原始问题 \( Q \) 的语义对齐。
- 最终选择得分最高的子查询 \( c^* = \arg\max_{c_j \in C_i} (S_{IG}(c_j) + S_{sem}(Q, c_j)) \)。

#### 阶段二：迭代主动程序剪枝（IAPP）—— 证据积累与统计测试
- 对每个程序类型的最优子查询，从知识库检索初始文档集合 \( D_{accum}^i \)。
- 计算**支持分数（Support Score, \( S_{sup} \)）**：子查询与其检索文档的语义相似度（使用 MiniLM-L6-v2 或 MPNet）。
- 迭代进行 \( T \) 步（最优 7 步）：
  - 统计所有程序的支持分数分布，使用 t 检验判断每个程序是否显著高于组均值，不显著的被剪枝。
  - 对保留的“活跃程序”，LLM 评估累积文档是否足够回答问题。若不足，则继续检索更多文档；若足够，则将该程序“锁定”（不再检索但保留证据）。
  - 迭代直到达到最大步数或仅剩一个活跃程序。

#### 阶段三：最终答案生成（FAG）—— 重排序与 CoT 推理
- 收集所有活跃和锁定程序的累积文档形成最终证据池 \( D_{final} \)。
- 使用重排序器（如 BGE-large-en-v1.5、ColBERTv2、GTE-Reranker-ModernBERT-Base）对文档按与原始问题的相关性重新排序，取 top-k。
- 通过少样本思维链（CoT）提示，将 top-k 文档与原始问题输入 LLM，生成最终答案 \( A \)。

### 2.3 算法流程（文字说明）
1. 生成候选程序类型列表，并初始化活跃/锁定集合。
2. 对每个程序类型，生成初始子查询并检索文档，计算初始支持分数。
3. 针对每个程序类型，生成多个候选子查询，计算信息增益+语义分数，选择最优子查询。
4. 迭代直至最大步数：
   - 对每个活跃程序，更新支持分数，判断是否锁定。
   - 对未锁定且未达到最大步数的程序，继续检索文档。
   - 执行 t 检验剪枝，将显著程序加入已选集。
5. 收集所有已选程序的文档，重排序后，通过 CoT 生成答案。

## 3. 实验设计

### 3.1 数据集
- **多跳推理**：HotPotQA（500 题，开发集）、2WikiMultihopQA（500 题，开发集）
- **常识推理**：ARC-Challenge（500 题，测试集）
- **科学推理**：MMLU-Pro（500 题，测试集）
- **生物医学**：MedQA（500 题，测试集）
- 知识库：多跳/常识/科学任务使用 2017 Wikipedia 摘要；生物医学使用 PubMed 摘要。

### 3.2 基准方法
- **对比方法**：Direct（直接生成）、CoT（思维链）、IRCoT（交错检索与推理）、FLARE（主动检索）、ProbTree（概率树搜索）、Self-RAG（自我反思）、SeaKR（自感知知识检索）
- **检索器**：GTE（Generalized Text Embeddings）
- **重排序器**：BGE-large-en-v1.5（双编码器）、ColBERTv2（延迟交互）、GTE-Reranker-ModernBERT-Base（交叉编码器）

### 3.3 LLM 骨干
- GPT-4o-mini（闭源）
- Gemma-2-9B-Instruct（开源）
- Qwen-2.5-7B-Instruct（开源）
- Mistral-Small-24B-Instruct（开源）

### 3.4 评估指标
- **多跳任务**：Exact Match（EM）、F1 分数
- **其他任务**：Accuracy

## 4. 资源与算力

- **论文未明确说明具体 GPU 型号、数量、训练时长或推理开销**。仅提及实验使用了多个 LLM 骨干（最大 24B 参数），但未提供计算资源细节。因此无法准确评估算力需求。从方法来看，PROGRAM 需要在推理时进行多轮迭代检索和 LLM 调用，计算开销高于单次检索方法，但论文在消融实验中报告了延迟（LAT）作为效率指标（例如程序类型数量对延迟的影响）。

## 5. 实验数量与充分性

- **实验数量丰富**：
  - 主实验：4 个 LLM 骨干 × 5 个数据集 = 20 组主表结果（表 2-5）。
  - 消融实验：
    - 模块消融（6 种组合，表 6 及附录表 13-15）
    - 程序类型消融（Basic-only, Basic+Advanced, All Types，表 7）
    - 重排序器架构消融（3 种，表 8）
    - 最终程序选择模式消融（多 vs 单程序，表 9）
    - 评分方法消融（IG-only, SEM-only, IG+SEM，表 10）
    - 迭代次数敏感性（图 4）
    - 候选子查询数量敏感性（表 11）
    - 重排序激活/非激活对比（附录表 12）
- **公平性**：所有方法使用相同的检索器（GTE）和相同的文档库，对比基准采用原始论文推荐设置或官方实现；评估采用 500 题随机子集（与先前 SOTA 工作一致），并报告多次运行？未明确提及统计显著性（除 p 值外），但实验设计较为规范。
- **充分性**：实验覆盖了多跳、常识、科学、医学四种推理类型，四个不同规模的 LLM，以及多种组件变体，足以验证方法的有效性。但未在更多领域（金融、视觉、表格 QA）进行测试。

## 6. 论文的主要结论与发现

- **PROGRAM 在所有数据集上达到 SOTA**：相对于最佳基线（Self-RAG、ProbTree、SeaKR），HotPotQA F1 提升 24%（Gemma-2-9B），MedQA 准确率提升 13.2%（Mistral-Small-24B）。
- **结构化程序引导优于非结构化置信度**：程序类型划分（因果、时序、逻辑等）提供明确的检索方向，而 token 级反思（Self-RAG）或概率树（ProbTree）缺乏结构。
- **双指标优化（信息增益+语义分数）有效**：结合两者在多数场景下优于单一指标，且信息增益更重要（表 10）。
- **迭代剪枝（t 检验）提高检索质量**：通过统计显著过滤低效程序，加速收敛并避免噪声积累。
- **重排序是必要组件**：缺少重排序时性能大幅下降（表 6），因为它能过滤多程序聚集的噪声文档。
- **多程序聚合优于单程序**：最终阶段使用多个活跃程序比仅用最高支持度程序效果更好（表 9）。
- **较小模型收益更大**：对 Gemma-2-9B 等较弱模型，PROGRAM 提供更显著的“逻辑支架”效果，缩小与大型模型的差距。

## 7. 优点

- **创新性**：首次将检索过程显式建模为程序执行，填补了非结构化 RAG 与结构化逻辑推理之间的空白。
- **可解释性强**：程序类型和子查询生成使检索过程透明，易于分析错误原因。
- **领域通用性**：程序类型库包含基础和高级类别，可针对不同领域（如医学的 Diagnosis、Treatment Reasoning）进行适配。
- **方法稳健**：双指标选择和统计剪枝降低了噪声路径的影响，提高了复杂推理的鲁棒性。
- **高效的效率-精度权衡**：仅激活高价值的程序类型，避免全面枚举所有类型导致的巨大开销（表 7）。
- **全面的消融实验**：验证了每个组件的必要性，增强了方法设计的可信度。

## 8. 不足与局限

- **程序类型手动设计**：当前库需人工预定义，可能无法覆盖未探索的领域（如金融、视觉、表格 QA）中的有效推理路径。论文承认这是主要局限。
- **计算开销**：多轮迭代检索和 LLM 调用导致延迟远高于单步方法（例如 All Types 延迟是 Basic-only 的 5 倍）。虽然论文报告了延迟，但未深入讨论性价比。
- **实验覆盖有限**：仅测试了 5 个数据集（各 500 题），未在更大规模或更多样化的基准（如 MultiQA、Musique、MMLU 全量）上评估。虽然与 SOTA 一致，但样本量较小可能影响统计可靠性。
- **未评估拒绝率或幻觉**：只报告了 EM/F1/Accuracy，未分析由于证据不足或错误检索导致的错误类型。
- **依赖强大 LLM 作为生成器和决策者**：方法依赖于 LLM 生成候选子查询、评估证据充分性等，较弱模型可能效果有限（Qwen-2.5-7B 在 MedQA 上提升较小）。
- **未考虑动态知识库或实时更新**：所有实验基于静态知识库，不适合时效性应用。
- **共享随机种子与方差缺失**：未报告多次运行的方差，可能影响结果的可重复性（仅提及 p 值但未全面使用）。

（完）
