---
title: "Chart-MRAG: Benchmarking Multimodal Retrieval Augmented Generation on Chart-based Documents"
title_zh: Chart-MRAG：基于图表文档的多模态检索增强生成基准
authors: "Yuming Yang, Jiang Zhong, Li Jin, Xiao Sun, Jingwang Huang, Gaojinpeng, Qing Liu, Yang Bai, Jingyuan Zhang, Rui Jiang, Qin Lei, Kaiwen Wei"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.acl-long.1164.pdf"
tags: ["query:mr"]
score: 9.0
evidence: 基于图表文档的多模态RAG基准
tldr: 现有多模态RAG基准多关注简单图文交互，忽略图表等复杂视觉格式。本文提出Chart-MRAG任务，并设计CHARGE半自动框架，通过多模态关键点提取、知识图谱构建和问答对合成生成高质量评估样本。经专家验证后形成Chart-MRAG Bench，全面评估多模态RAG系统在图表场景下的性能。实验发现现有系统在图表推理上存在显著短板。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1164/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 804, \"height\": 719, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1164/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1637, \"height\": 610, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1164/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 390, \"height\": 278, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1164/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 645, \"height\": 376, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1164/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 800, \"height\": 1124, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1164/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 796, \"height\": 416, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1164/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 798, \"height\": 594, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1164/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1663, \"height\": 1044, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1164/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 669, \"height\": 500, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1164/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 674, \"height\": 767, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1164/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 757, \"height\": 1064, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1164/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 690, \"height\": 353, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1164/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 713, \"height\": 656, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1164/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 668, \"height\": 756, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1164/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 909, \"height\": 438, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1164/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 1633, \"height\": 2210, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1164/fig-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 1642, \"height\": 1860, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1164/fig-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 532, \"height\": 402, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1164/fig-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 1628, \"height\": 1998, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1164/fig-020.webp\", \"caption\": \"\", \"page\": 0, \"index\": 20, \"width\": 1612, \"height\": 539, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1164/fig-021.webp\", \"caption\": \"\", \"page\": 0, \"index\": 21, \"width\": 1633, \"height\": 1992, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1164/fig-022.webp\", \"caption\": \"\", \"page\": 0, \"index\": 22, \"width\": 1560, \"height\": 534, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1164/fig-023.webp\", \"caption\": \"\", \"page\": 0, \"index\": 23, \"width\": 250, \"height\": 228, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1164/fig-024.webp\", \"caption\": \"\", \"page\": 0, \"index\": 24, \"width\": 1607, \"height\": 2016, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1164/fig-025.webp\", \"caption\": \"\", \"page\": 0, \"index\": 25, \"width\": 1436, \"height\": 877, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1164/fig-026.webp\", \"caption\": \"\", \"page\": 0, \"index\": 26, \"width\": 669, \"height\": 500, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1164/fig-027.webp\", \"caption\": \"\", \"page\": 0, \"index\": 27, \"width\": 690, \"height\": 352, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1164/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 813, \"height\": 417, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1164/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 788, \"height\": 535, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1164/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 815, \"height\": 392, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1164/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1649, \"height\": 687, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1164/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1650, \"height\": 1353, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1164/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1365, \"height\": 546, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1164/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 977, \"height\": 282, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1164/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1155, \"height\": 295, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1164/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1641, \"height\": 874, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1164/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1420, \"height\": 804, \"label\": \"Table\"}]"
motivation: 现有MRAG基准忽略图表等复杂视觉格式，缺乏对图表推理能力的评估。
method: 提出CHARGE半自动框架，通过多模态关键点提取、知识图谱构建和问答对合成生成评估样本。
result: 构建Chart-MRAG Bench基准，实验揭示现有MRAG系统在图表推理任务上表现不佳。
conclusion: 图表MRAG任务对现有系统构成挑战，亟需更强大的多模态理解和检索能力。
---

## Abstract
Multimodal Retrieval-Augmented Generation (MRAG) enhances reasoning capabilities by integrating external knowledge. However, existing benchmarks primarily focus on simple image-text interactions, overlooking complex visual formats like charts that are prevalent in real-world applications. In this work, we introduce a novel task, Chart-based MRAG , to address this limitation. To generate high-quality evaluation samples, we propose CHARGE ( CHAR t-based document question-answering GE neration), a semi-automatic framework for generating evaluation samples through multi-modal keypoint extraction, knowledge graph construction, and qa pair synthesis.By combining CHARGE with expert validation, we construct Chart-MRAG Bench , a comprehensive benchmark for chart-based MRAG evaluation, featuring 4,738 question-answering pairs across 8 domains from real-world documents.Our experiments reveal three critical limitations in current approaches: (1) unified multimodal embedding retrieval methods struggles in chart-based scenarios, (2) even with ground-truth retrieval, state-of-the-art Multimodal Large Language Models (MLLMs) achieve only 71.15% Correctness and 80.74% Coverage scores, and (3) Widely-used MLLMs demonstrate consistent text-over-visual modality bias. These findings highlight great challenges in processing information-dense visual formats. We will make our code and dataset publicly available.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **研究动机**：现有多模态检索增强生成（MRAG）基准（如MRAG-Bench、Dyn-VQA等）主要评估简单图像与文本的交互，忽略了在现实应用中广泛存在的信息密集型图表（charts）。图表包含复杂的视觉细节和结构化数据，需要模型同时理解文本和图表中的信息才能正确回答。
- **核心问题**：缺乏针对图表场景的MRAG评估基准，导致现有系统在图表推理上的能力缺陷未被充分暴露。
- **整体含义**：本文首次提出**Chart-based MRAG**任务，并构建高质量的评估基准Chart-MRAG Bench，以推动MRAG系统在信息密集视觉格式（如图表）上的能力提升。

## 2. 论文提出的方法论：CHARGE框架

- **核心思想**：半自动生成基于图表的问答（QA）对，通过提取多模态关键点、构建知识图谱，并基于图谱生成需要跨文档/跨模态推理的高质量QA对。
- **关键技术细节**：
    1. **多模态关键点提取**：对文本段落使用GPT-4o提取文本关键点 \( T \)；对图表先用OCR（ChartOCR）提取数值，再用GPT-4o结构化形成图表关键点 \( C \)。
    2. **知识图谱构建**：将关键点转化为结构化表示（实体、关系、属性），并通过语义相似度阈值 \( \tau \) 去重，形成节点和边的知识图谱；进一步划分社区以组织主题。
    3. **QA对生成**：从社区随机选择起始关键点，检索最相关的前 \( n \) 个节点，由LLM配对 (\( K_i, K_j \)) 并生成QA对。采用LLM-as-a-Judge验证：确保仅当同时提供两个关键点时才可正确回答，单独提供任一关键点或无需检索时回答错误。
    4. **QA分类**：按文档来源（文档内/文档间）和模态（纯文本、纯图表、文本-图表）分为8种类型，同时包含单关键点（1-hop）和多关键点（2-hop）问题。
- **公式/算法**：算法1描述了QA生成的四步流程（随机选择起始点、检索相关节点、节点配对、生成与验证）。评估指标定义：
    - **Correctness**（正确性）：二进制指标，要求回答的关键点集合与真值完全匹配， \( 1[K_r \equiv K_{gt}] \)。
    - **Coverage**（覆盖率）：连续指标， \( |K_m| / |K_{gt}| \)，其中 \( K_m \) 为匹配到的真值关键点数量。

## 3. 实验设计

- **数据集与场景**：
    - 基于Pew Research Center的267份真实文档，包含1283个文本段落和627个图表，覆盖8个领域（如政治、科技、宗教等）。
    - 构建**Chart-MRAG Bench**，包含4738个QA对，分为8种类型（单点文本、单点图表、文档内文本、文档内图表、文档内文本-图表、文档间文本、文档间图表、文档间文本-图表）。
- **基准与对比方法**：
    - **检索方法**：三种策略。
        - 统一多模态嵌入+单向量库（CLIP、JINA、SigLIP）。
        - 多模态嵌入+组合向量库（BM25、BGE-M3-base/large、E5-base/large，图表预处理为文本摘要）。
        - 多模态嵌入+分离向量库（视觉模型编码图表，文本模型编码文本，加权聚合）。
    - **生成模型**：8种MLLMs，包括开源（SAIL-VL-2B、Qwen2-VL-7B、MiniCPM-V-2.6、Llama-3.2-90B-Vision）和闭源（GPT-4o、GPT-5、Gemini-2.5-Pro、Claude-4.5-Sonnet）。
- **评估指标**：检索阶段使用Recall@5和Recall@10；生成阶段使用Correctness和Coverage，由四个LLM（GPT-4.1、Qwen2.5-Max、Grok-3、Claude-4.5-Sonnet）投票平均。

## 4. 资源与算力

- 文中明确指出：开源模型部署在**8×A100 GPU**上（“deployed on an 8\*A100 GPUs configuration”），参数设置遵循官方文档。闭源模型通过官方API调用，使用默认参数。
- **未明确说明**：训练时长、总GPU小时数、推理成本等具体算力消耗。因此无法提供更细粒度的资源信息。

## 5. 实验数量与充分性

- **实验组数**：
    - 检索实验：3种策略下涵盖7种模型（CLIP、JINA、SigLIP、BM25、BGE-M3、E5等），并对比不同k值（5和10）。
    - 生成实验：8种MLLMs在无RAG、RAG@k=5、RAG@k=10、GTR（ground-truth检索）共4种设置下评测，每种设置包含8个QA子类别，总计256+组结果（表4）。
    - 额外分析：不同k值对性能的影响（图5）、模型参数规模与性能关系（图6）、模态偏置分析（图7，包含100个专门构造的QA对）。
- **充分性与客观性**：
    - 覆盖了主流检索和生成模型，且对检索方法进行了三种架构对比。
    - 评估指标合理，超越传统词重叠指标，针对图表数值推理设计。
    - 消融实验（RAG有无、k大小、文档内/间、单/双跳）全面，揭示了模型在不同难度下的表现。
    - 模态偏置实验由人类专家验证，确保分析可靠。
    - 但仍未包含所有可能的检索器（如ColPali）和前沿MLLMs（如Claude-4 Opus），实验规模可进一步扩展。

## 6. 论文的主要结论与发现

1. **统一多模态嵌入方法在图表场景失效**：CLIP、SigLIP等在同一向量空间中编码图表和文本，在纯图表和文本-图表任务上召回率为0%，说明现有统一嵌入无法捕获图表中的密集数值信息。
2. **即使提供真值检索，最先进MLLMs表现依然有限**：Claude-4.5-Sonnet在GTR下仅达到71.15% Correctness和80.74% Coverage，说明跨模态推理仍远未解决。
3. **MLLMs存在一致的文本偏好偏差**：当答案同时存在于文本和图表中时（精确度不同），模型倾向于从文本中提取信息，即使图表包含更精确的数据；较大模型（如GPT-4o）能更主动识别信息冗余。
4. **检索窗口扩大带来权衡**：增大k值提高召回率但降低生成正确性（precision-召回率权衡）。
5. **参数规模与性能正相关**，但架构优化（如MiniCPM-V-2.6）可在较小参数下接近大模型性能。

## 7. 优点

- **任务创新**：首次将MRAG评估扩展到图表场景，填补了该领域空白。
- **数据高质量**：通过CHARGE半自动生成+专家验证（Fleiss’s kappa=0.82），最终保留4738对（近80%初始生成数），保证准确性与多样性。
- **评估指标针对性强**：提出Correctness和Coverage，直接衡量关键点匹配而非语义相似度，避免传统指标的误导（例如错误数值可能获得高BLEU分）。
- **分析深入**：包含多维度消融（文档内/间、模态、跳数、k值、参数规模）和模态偏置分析，实验设计系统且严谨。
- **开源可复现**：代码和数据集将公开，促进后续研究。

## 8. 不足与局限

1. **OCR误差影响**：尽管经过人工校验，但CHARGE框架中的OCR步骤（ChartOCR）仍可能引入错误，尤其在复杂图表布局中，可能影响后续QA质量。
2. **计算资源有限**：仅评估了部分主流MLLMs和检索器，未包含更多最新模型（如ColPali、Claude-4 Opus等），可能导致结论的泛化性受限。
3. **数据集偏差**：所有数据源自单一来源（Pew Research Center），领域偏向社会科学统计，可能限制对其他类型图表（如金融、医疗）的覆盖。
4. **评估指标依赖LLM裁判**：Correctness和Coverage通过四个LLM投票计算，虽增强了稳定性，但LLM自身也可能存在偏差。
5. **未包含端到端MRAG系统训练**：本文仅专注于评估，未提出新的训练方法或模型架构来改进图表MRAG。这是未来工作方向。
6. **多跳问题难度分布**：目前QA对中2-hop占多数（约80%），单跳较少，未来可进一步平衡难度分布。

（完）
