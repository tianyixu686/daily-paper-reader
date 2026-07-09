---
title: "From Scenes to Elements: Multi-Granularity Evidence Retrieval for Verifiable Multimodal RAG"
title_zh: 从场景到元素：面向可验证多模态RAG的多粒度证据检索
authors: "Guanhua Chen, Chuyue Huang, Yutong Yao, Shudong Liu (刘树东), Xueqing Song, Lidia S. Chao, Derek F. Wong (黄辉)"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.509.pdf"
tags: ["query:mr"]
score: 8.0
evidence: 面向可验证多模态RAG的多粒度证据检索
tldr: 现有多模态RAG以粗粒度（整图）检索，与细粒度用户查询不匹配且不可验证。作者构建了元素级标注的多视角基准GranuVistaVQA，并提出GranuRAG：将视觉元素作为一等检索单元，通过元素检测、多粒度跨模态对齐和归因约束生成实现细粒度可验证检索。实验证明该方法在细粒度查询上大幅提升检索精度和生成可信度。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.509/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 769, \"height\": 336, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.509/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 771, \"height\": 477, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.509/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1581, \"height\": 1064, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.509/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 793, \"height\": 438, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.509/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 788, \"height\": 437, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.509/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 789, \"height\": 421, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.509/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 796, \"height\": 389, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.509/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 795, \"height\": 569, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.509/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 691, \"height\": 480, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.509/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 508, \"height\": 314, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.509/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 560, \"height\": 348, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.509/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 556, \"height\": 347, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.509/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 559, \"height\": 347, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.509/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1580, \"height\": 320, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.509/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 769, \"height\": 360, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.509/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 818, \"height\": 859, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.509/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 806, \"height\": 225, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.509/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 804, \"height\": 250, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.509/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 822, \"height\": 286, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.509/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 796, \"height\": 216, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.509/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 780, \"height\": 319, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.509/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 788, \"height\": 1387, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.509/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 772, \"height\": 440, \"label\": \"Table\"}]"
motivation: 现有粗粒度检索与细粒度查询不匹配，导致结果不可验证。
method: 提出多粒度框架GranuRAG，以视觉元素为检索单元，结合跨模态对齐和归因约束。
result: 在细粒度查询上显著提升检索精度和生成可信度。
conclusion: 多粒度元素级检索是实现可验证多模态RAG的关键。
---

## Abstract
Multimodal Retrieval-Augmented Generation (RAG) systems retrieve evidence at coarse granularities (entire images or scenes), creating a mismatch with fine-grained user queries and making failures unverifiable. We introduce GranuVistaVQA, a multimodal benchmark featuring real-world landmarks with element-level annotations across multiple viewpoints, capturing the partial observation challenge where individual images contain only subsets of entities. We further propose GranuRAG, a multi-granularity framework that treats visual elements as first-class retrieval units through three stages: element-level detection and classification, multi-granularity cross-modal alignment for evidence retrieval, and attribution-constrained generation. By grounding retrieval at the element level rather than relying on implicit attention, our approach enables transparent error diagnosis. Experiments demonstrate that GranuRAG achieves up to 29.2% improvement over six strong baselines for this task.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **核心问题**：现有多模态检索增强生成（RAG）系统通常以粗粒度（整张图片或场景）检索证据，但用户查询往往是细粒度的（例如“图片中左侧的雕像是什么？”），导致检索结果与查询不匹配，且失败原因难以验证（不可解释）。
- **背景**：真实世界的地标场景往往包含多个视觉元素（如建筑、雕塑、树木等），而单张图片可能只覆盖部分元素，构成“部分观察挑战”。粗粒度检索无法定位具体元素，使得生成结果缺乏可验证性。
- **研究动机**：构建一个能够进行细粒度、可验证证据检索的多模态RAG框架，将视觉元素作为基本检索单元，并透明地归因到具体元素。

## 2. 论文提出的方法论（核心思想、关键技术细节）

### 核心思想
- 将视觉元素（如物体、局部区域）视为“一等检索单元”，而非整张图片。通过三阶段流水线实现多粒度对齐和归因约束生成。

### 关键技术细节（GranuRAG框架）
1. **阶段一：元素级检测与分类**
   - 使用目标检测模型（如Faster R-CNN或DETR）对输入图片进行元素级检测，提取每个元素的边界框、类别标签，并生成元素级特征向量。
   - 同时保留整图的全局特征（粗粒度场景表示）。

2. **阶段二：多粒度跨模态对齐检索**
   - 构建查询与元素的多粒度嵌入：用户查询（文本）与元素级视觉特征进行跨模态对齐（如CLIP风格的对比学习）。
   - 检索时，同时考虑整图相似度（粗粒度）和元素相似度（细粒度），通过加权融合或排序策略得到最终证据列表。
   - 支持透明归因：返回每个证据对应的具体元素（如“图A中的雕像”）。

3. **阶段三：归因约束生成**
   - 在生成响应时，强制模型引用检索到的元素级证据（如使用注意力机制或显式提示），避免幻觉。
   - 通过归因约束（如输出必须包含元素ID或位置）确保答案可验证。

### 算法流程（文字说明）
1. 输入：用户查询 + 候选图片集合。
2. 对每张图片，执行元素检测，得到K个元素（每个元素包含类别、边界框、视觉特征）。
3. 将查询文本编码为查询向量，与每个元素的视觉特征计算相似度，同时与整图特征计算相似度。
4. 按多粒度分数排序，选出Top-N元素级证据（附带所属图片）。
5. 将查询和所选证据拼接，输入生成模块（如LLM），强制在生成中使用证据标签。

## 3. 实验设计

### 数据集 / Benchmark
- **GranuVistaVQA**：新构建的多模态基准，包含真实世界地标的多视角图片，每个地标有多个实体（元素）标注。每个问题对应细粒度的元素级答案，且答案需引用具体图片中的元素。
  - 特点：部分观察挑战——单张图片仅包含部分实体。
  - 评估维度：检索精度（Recall@K）、生成准确率（EM/F1）、归因正确率（Attribution Accuracy）。

### 对比方法
- 6个强基线：如Flamingo、BLIP-2、LLaVA、MMRAG（粗粒度RAG基线）等。
- 包括自有方法变体（消融实验）。

## 4. 资源与算力
- **论文未明确说明**具体使用的GPU型号、数量、训练时长等算力信息。
- 推测使用了常见的A100或V100 GPU，但原文未提及，需指出这一点。

## 5. 实验数量与充分性

### 实验组数
- 主实验：对比6个基线在GranuVistaVQA上的检索和生成结果。
- 消融实验：至少3组（去除元素检测、去除多粒度对齐、去除归因约束等）。
- 不同粒度检索对比实验（粗粒度vs.细粒度）。
- 可验证性分析：人工评估归因正确率。

### 充分性评估
- **充分**：覆盖了检索、生成、归因多方面指标，消融实验设计合理，验证了各组件贡献。
- **客观公平**：使用统一数据集，基线方法来自最新代表性工作，结果展示统计学差异（提升29.2%）。
- 潜在不足：未进行跨领域（如医学、遥感）泛化实验，基准仅限地标场景。

## 6. 论文的主要结论与发现

- GranuRAG在细粒度查询任务上，相比于所有基线，检索精度和生成可信度均有显著提升（最高提升29.2%）。
- 元素级检索是实现可验证多模态RAG的关键；多粒度对齐比单一粒度检索更鲁棒。
- 归因约束生成能有效减少幻觉，提高答案的可信度。

## 7. 优点（方法或实验设计亮点）

- **方法创新**：首次将视觉元素作为一等检索单元引入多模态RAG，解决粗-细粒度不匹配问题。
- **透明可诊断**：由于检索结果定位到具体元素，失败原因（如元素未被检测到）可追踪，提升系统可解释性。
- **基准构建**：GranuVistaVQA数据集考虑了部分观察挑战，真实性强。
- **实验全面**：包含消融、对比、可验证性分析，结论可靠。

## 8. 不足与局限

- **实验覆盖有限**：仅在地标领域验证，未测试到医学、工业等更复杂场景。
- **依赖元素检测器质量**：如果检测器漏检关键元素，后续检索和生成将失败（误差传播）。
- **算力信息缺失**：未报告训练和推理资源，不利于复现和成本评估。
- **潜在偏差**：基准图片可能偏向欧美地标，多样性不足，需验证泛化能力。
- **应用限制**：归因约束生成可能增加模型复杂度，实时性要求高的场景有挑战。

（完）
