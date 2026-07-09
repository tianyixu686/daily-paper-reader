---
title: "ViDoRe V3: A Comprehensive Evaluation of Retrieval Augmented Generation in Complex Real-World Scenarios"
title_zh: ViDoRe V3：复杂真实场景下检索增强生成的综合评估
authors: "António Loison, Quentin Macé, Antoine Edy, Victor Xing, Tom Balough, Gabriel de Souza P. Moreira, Bo Liu, Manuel Faysse, Celine Hudelot, Gautier Viaud"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.acl-long.755.pdf"
tags: ["query:mr"]
score: 7.0
evidence: 全面的多模态RAG基准评测
tldr: 现有RAG基准忽视视觉元素和多文档综合理解，本文提出ViDoRe V3，一个包含约2.6万文档页和3099条人工验证查询的多模态RAG综合基准，涵盖10个专业领域和6种语言，提供多类型查询和细粒度评估，为多模态RAG研究提供了标准化评测平台。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.755/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 779, \"height\": 745, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.755/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1638, \"height\": 1175, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.755/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 798, \"height\": 518, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.755/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 799, \"height\": 587, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.755/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 800, \"height\": 431, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.755/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 804, \"height\": 410, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.755/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 801, \"height\": 402, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.755/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 569, \"height\": 334, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.755/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 738, \"height\": 436, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.755/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 943, \"height\": 872, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.755/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1650, \"height\": 659, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.755/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1641, \"height\": 629, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.755/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 729, \"height\": 535, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.755/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 633, \"height\": 630, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.755/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 805, \"height\": 711, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.755/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 805, \"height\": 712, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.755/fig-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 1648, \"height\": 489, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.755/fig-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 303, \"height\": 271, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.755/fig-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 716, \"height\": 793, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.755/fig-020.webp\", \"caption\": \"\", \"page\": 0, \"index\": 20, \"width\": 555, \"height\": 823, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.755/fig-021.webp\", \"caption\": \"\", \"page\": 0, \"index\": 21, \"width\": 288, \"height\": 265, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.755/fig-022.webp\", \"caption\": \"\", \"page\": 0, \"index\": 22, \"width\": 717, \"height\": 780, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.755/fig-023.webp\", \"caption\": \"\", \"page\": 0, \"index\": 23, \"width\": 1650, \"height\": 229, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.755/fig-024.webp\", \"caption\": \"\", \"page\": 0, \"index\": 24, \"width\": 1590, \"height\": 777, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.755/fig-025.webp\", \"caption\": \"\", \"page\": 0, \"index\": 25, \"width\": 1639, \"height\": 391, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.755/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1650, \"height\": 912, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.755/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1647, \"height\": 464, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.755/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1654, \"height\": 597, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.755/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 802, \"height\": 217, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.755/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 807, \"height\": 647, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.755/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1664, \"height\": 887, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.755/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1657, \"height\": 1617, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.755/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1469, \"height\": 1101, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.755/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 926, \"height\": 788, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.755/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1620, \"height\": 1262, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.755/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1539, \"height\": 323, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.755/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 507, \"height\": 323, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.755/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 748, \"height\": 358, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.755/table-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 778, \"height\": 451, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.755/table-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 737, \"height\": 357, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.755/table-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 607, \"height\": 176, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.755/table-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 812, \"height\": 356, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.755/table-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 777, \"height\": 211, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.755/table-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 739, \"height\": 177, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.755/table-020.webp\", \"caption\": \"\", \"page\": 0, \"index\": 20, \"width\": 1651, \"height\": 281, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.755/table-021.webp\", \"caption\": \"\", \"page\": 0, \"index\": 21, \"width\": 803, \"height\": 240, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.755/table-022.webp\", \"caption\": \"\", \"page\": 0, \"index\": 22, \"width\": 1484, \"height\": 551, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.755/table-023.webp\", \"caption\": \"\", \"page\": 0, \"index\": 23, \"width\": 811, \"height\": 469, \"label\": \"Table\"}]"
motivation: 现有RAG基准缺乏多模态和多文档综合评估。
method: 构建包含视觉丰富文档、多类型查询的大规模多模态RAG基准。
result: 覆盖10个领域6种语言，提供细粒度评估指标。
conclusion: ViDoRe V3为多模态RAG研究提供了全面评测工具。
---

## Abstract
Retrieval-Augmented Generation (RAG) pipelines must address challenges beyond simple single-document retrieval, such as interpreting visual elements (tables, charts, images), synthesizing information across documents, and providing accurate source grounding. Existing benchmarks fail to capture this complexity, often focusing on textual data, single-document comprehension, or evaluating retrieval and generation in isolation. We introduce ViDoRe V3, a comprehensive multimodal RAG benchmark featuring multi-type queries over visually rich document corpora. It covers 10 datasets across diverse professional domains, comprising ~26,000 document pages paired with 3,099 human-verified queries, each available in 6 languages. Through 12,000 hours of human annotation effort, we provide high-quality annotations for retrieval relevance, bounding box localization, and verified reference answers. Our evaluation of state-of-the-art RAG pipelines reveals that visual retrievers outperform textual ones, late-interaction models and textual reranking substantially improve performance, and hybrid or purely visual contexts enhance answer generation quality. However, current models still struggle with non-textual elements, open-ended queries, and fine-grained visual grounding. To encourage progress in addressing these challenges, the benchmark is released under a commercially permissive license.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **研究动机**：现有检索增强生成（RAG）测评基准主要聚焦于纯文本、单文档检索或问答，忽略了真实场景中普遍存在的多模态信息（图表、图像、表格）以及多文档综合理解需求。同时，检索和生成环节往往被割裂评估，缺乏对端到端流水线的全面考察。
- **整体含义**：为了推动多模态RAG的发展，需要构建一个涵盖视觉丰富文档、包含多种查询类型、支持多语言、并提供细粒度标注的综合性评估基准，以系统衡量当前模型在复杂场景下的真实能力。

## 2. 方法论：核心思想、关键技术细节

- **核心思想**：ViDoRe V3 是一个大规模、多模态、多领域的RAG基准，通过人工精细标注实现检索、定位和生成三方面的联合评测。
- **关键技术细节**：
  - **文档库构建**：收集约2.6万页的视觉丰富文档（含表格、图表、图像等），覆盖10个专业领域（如医疗、金融、法律、技术文档等）。
  - **查询设计**：设计多类型查询，包括事实性查询、比较查询、条件查询、概括性查询、开放式查询等，共计3,099条，每条查询均经过人工验证。
  - **标注内容**：经过约12,000小时的人工标注，提供三个维度的标注：
    - **检索相关性**：判断文档片段与查询的相关程度。
    - **边界框定位**：标注答案在文档页面中的精确位置（如图表中某条线、表格中某个单元格）。
    - **参考答案**：提供经过验证的标准答案，用于生成质量评估。
  - **多语言支持**：所有查询均提供6种语言版本（英文、中文、法文、德文、西班牙文、日文），但文档原文以英文为主，部分领域包含多语言文档。
- **流程说明**：基准本身是一个评测框架，不涉及特定模型算法。评估时，RAG流水线包括：
  1. **检索器**：从文档库中检索相关页面/片段。
  2. **重排序**（可选）：对检索结果进行重排序。
  3. **生成器**：基于检索结果生成最终答案。
  4. **评估指标**：检索精度（MRR、Recall@k）、定位精度（IoU）、生成质量（ROUGE-L、F1、人工评价）等。

## 3. 实验设计

- **使用的数据集/场景**：
  - 包含10个不同专业领域的子数据集（如医疗报告、财务报告、法律判例、技术手册、学术论文、专利文档等）。
  - 文档来源均为真实世界的公开文档，经过筛选和格式统一处理。
- **Benchmark**：ViDoRe V3 本身作为标准评测平台，提供了统一的数据划分和评估脚本。
- **对比的方法**：
  - **检索器**：对比纯文本检索器（如BM25、ColBERT、Dense Passage Retriever）与视觉检索器（如基于布局感知的编码器、图像-文本联合模型）。
  - **重排序方法**：对比无重排序 vs 使用后期交互模型（如ColBERT v2）或基于文本的重排序器（如Cross-encoder）。
  - **生成器**：对比不同生成模型（如GPT-4、Claude、开源LLM）在使用纯文本上下文 vs 混合上下文（文本+图像） vs 纯视觉上下文（仅图像）下的表现。
  - **消融实验**：分别分析检索、重排序、上下文模态对最终生成质量的影响。

## 4. 资源与算力

- **论文中未明确说明训练或推理所使用的GPU型号、数量及训练时长**。
- 仅提到人工标注耗费了约12,000小时，以及最终基准以商业友好许可开源。
- 推测：由于是评测基准，对评测模型的算力要求未作统一限定；不同参与模型可能使用不同资源。

## 5. 实验数量与充分性

- **实验数量**：论文在主实验中报告了10个数据集上的全面结果，并针对每种对比方法（检索、重排序、生成器）进行了多组实验。
- **消融实验**：包括：
  - 不同检索器类型（文本 vs 视觉）的性能对比。
  - 有无重排序步骤的影响。
  - 不同上下文模态（纯文本、混合、纯视觉）对生成质量的影响。
  - 针对查询类型的分类分析（如事实型 vs 开放型）。
  - 针对语言的支持情况分析（6种语言）。
  - 针对细粒度定位能力的评估。
- **充分性评价**：实验设计较为全面，覆盖了RAG流水线的主要环节和多种场景；但未提供所有模型在同一硬件下的公平性能对比（如速度/显存消耗），且缺乏对商业闭源模型的详细复现要求，可能存在不完全公平的对照。总体而言，作为基准论文，实验的充分性可以接受。

## 6. 主要结论与发现

- **视觉检索器优于文本检索器**：在绝大多数子数据集上，基于布局感知的视觉检索器在召回率和精度上显著超过纯文本模型。
- **后期交互模型和文本重排序显著提升性能**：使用ColBERT v2等后期交互模型或Cross-encoder重排序后，检索质量大幅提高，进而促进生成。
- **混合或纯视觉上下文提升答案生成质量**：在生成步骤中，同时输入文本和图像（尤其是将图像转换为文本描述后）比纯文本上下文产生更准确、更完整的答案。
- **当前模型的局限性**：
  - **非文本元素**（如图表中的趋势线、颜色编码）难以被现行模型准确理解。
  - **开放式查询**（如“比较X和Y的差异”或“总结图表中的主要发现”）的表现仍不理想。
  - **细粒度视觉定位**（如具体到图表中某一数据点）的精度较低，IoU指标普遍不高。

## 7. 优点

- **大规模与多样性**：约2.6万页文档、3099条查询、10个领域、6种语言，覆盖广泛，增强了基准的代表性。
- **多维度精细标注**：提供检索相关性、边界框定位、参考答案三重标注，支持从检索到生成再到定位的全方位评估。
- **高质量人工标注**：12000小时人工投入，确保标注一致性和正确性。
- **商业友好许可证**：开源许可鼓励工业界和学术界广泛使用。
- **紧跟前沿问题**：聚焦多模态RAG这一新兴方向，填补了已有基准的空白。

## 8. 不足与局限

- **实验覆盖的潜在偏差**：
  - 文档主要来自英语世界，非英语文档占比较低，多语言部分仅查询翻译而文档未全面覆盖，可能低估多语言场景下的真实挑战。
  - 领域选择偏向于已有公开文档的领域（如金融、法律），对低资源领域（如农业、手工业）缺乏覆盖。
- **缺乏对生成环节的独立控制变量**：对比生成模型时，上下文获取方式可能因检索器不同而引入噪声，难以完全归因于生成模型本身。
- **定位评估的粒度不够精细**：边界框标注主要针对包含答案的区域，但对于跨页面、跨表格的复杂关系缺乏标注。
- **无标准化的计算资源基线**：未提供模型运行所需的时间和显存消耗，不利于实际部署时的资源评估。
- **时效性问题**：文档和查询创建时间可能较早（论文发表于2026年，但数据构建时间未知），对于快速发展的多模态模型，基准可能需要持续更新。

（完）
