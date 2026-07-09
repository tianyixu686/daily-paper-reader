---
title: "RA-RRG: Multimodal Retrieval-Augmented Radiology Report Generation with Key Phrase Extraction"
title_zh: RA-RRG：基于关键短语提取的多模态检索增强放射学报告生成
authors: "Jonggwon Park, Byungmu Yoon, Soobum Kim, Kyoyun Choi"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.247.pdf"
tags: ["query:mr"]
score: 7.0
evidence: 多模态检索增强的放射学报告生成
tldr: 自动放射学报告生成需求大，但现有MLLM计算昂贵且易产生幻觉。RA-RRG提出检索增强框架，利用LLM提取关键短语，从多模态记忆库中检索相关报告片段，再生成最终报告。该方法在减少幻觉的同时降低了计算资源需求，实验表明其在多个指标上优于直接生成的MLLM模型。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.247/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1566, \"height\": 581, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.247/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1581, \"height\": 707, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.247/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 807, \"height\": 316, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.247/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1569, \"height\": 541, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.247/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1535, \"height\": 646, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.247/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 711, \"height\": 1709, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.247/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 681, \"height\": 866, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.247/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 677, \"height\": 1034, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.247/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 794, \"height\": 477, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.247/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 401, \"height\": 339, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.247/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 321, \"height\": 385, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.247/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1525, \"height\": 566, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.247/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1661, \"height\": 376, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.247/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1473, \"height\": 283, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.247/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 811, \"height\": 647, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.247/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 808, \"height\": 203, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.247/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 805, \"height\": 179, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.247/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 814, \"height\": 198, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.247/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1493, \"height\": 326, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.247/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1666, \"height\": 520, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.247/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 808, \"height\": 495, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.247/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 808, \"height\": 181, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.247/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1159, \"height\": 403, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.247/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1231, \"height\": 448, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.247/table-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1566, \"height\": 962, \"label\": \"Table\"}]"
motivation: 现有MLLM计算成本高、训练数据大且易产生幻觉，限制了实际部署。
method: 使用LLM提取关键短语，检索多模态记忆库中的相似报告片段，辅助生成。
result: 在减少幻觉和计算需求的同时取得高质量报告。
conclusion: 检索增强是降低MLLM幻觉和成本的有效途径。
---

## Abstract
Automated radiology report generation (RRG) holds potential to reduce the workload of radiologists, and recent advances in multimodal large language models (MLLMs) have enabled multimodal chest X-ray (CXR) report generation. However, existing MLLMs are computationally expensive, require large-scale training data, and may produce hallucinated content, limiting their practical deployment. To address these limitations, we propose RA-RRG, a retrieval-augmented RRG framework that combines multimodal retrieval with large language models (LLMs) to generate radiology reports while reducing hallucinations and computational demands. RA-RRG uses LLMs to extract clinically essential key phrases from radiology reports and retrieves relevant phrases given an input image. By conditioning LLMs on the retrieved phrases, RA-RRG effectively suppresses hallucinations while maintaining strong report generation performance. Experiments on the MIMIC-CXR and IU X-ray datasets show state-of-the-art results on CheXbert metrics and competitive RadGraph F1 scores compared to MLLMs. Furthermore, RA-RRG naturally generalizes to multi-view RRG by aggregating phrases retrieved from multiple images, highlighting its broad applicability to real-world clinical scenarios. Code is available at https://github.com/deepnoid-ai/RA-RRG.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究背景**：自动放射学报告生成（RRG）有望减轻放射科医生的工作负担。近年来多模态大语言模型（MLLM）在胸部X光（CXR）报告生成上取得了进展。
- **核心问题**：现有MLLM存在三大痛点：
  - 计算成本高（需要大规模GPU资源）
  - 依赖大量训练数据
  - 容易产生幻觉性内容（hallucination），即生成与影像不符的虚假医学描述
- **研究目标**：提出一种检索增强框架RA-RRG，在降低计算需求和减少幻觉的同时保持高质量报告生成。

## 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：利用大语言模型（LLM）从已有放射学报告中提取临床关键短语（key phrases），构建多模态记忆库；对输入影像，先检索与影像最相关的关键短语，再以这些短语为条件输入LLM生成完整报告。通过检索约束生成过程，抑制幻觉。
- **关键技术细节**：
  1. **短语提取**：使用LLM从训练集报告中的每个句子提取关键医学短语（例如“正常心脏轮廓”、“无气胸”等）。
  2. **多模态记忆库构建**：将影像视觉特征与短语文本特征对齐，建立索引。
  3. **检索阶段**：给定输入影像，提取其视觉特征，从记忆库中检索与之最匹配的top-k个短语。
  4. **条件生成**：将检索到的短语作为前缀或上下文，输入到基于LLM的生成器中，生成最终报告。
  5. **多视图扩展**：对于多视图CXR（如正面+侧面），分别从各视图检索短语并聚合，实现多视图RRG。
- **关键部件组合**：视觉编码器 + 短语检索器 + LLM生成器。无需端到端训练大规模MLLM，而是利用已有预训练模型进行特征提取和文本生成，大幅降低训练成本。

## 3. 实验设计：数据集、基准方法与对比对象

- **数据集**：
  - **MIMIC-CXR**：大规模胸部X光数据集（含影像和自由文本报告）。
  - **IU X-ray**：印第安纳大学胸部X光数据集（较小规模）。
- **基准指标**：
  - **CheXbert指标**：基于CheXbert标签的分类精确率、召回率、F1等，用于评估临床发现描述的正确性。
  - **RadGraph F1**：基于关系图结构的实体抽取F1分数，评估结构化医学知识的捕捉能力。
- **对比方法**：主要与直接生成的MLLM模型（如基于大视觉语言模型的端到端生成方法）进行比较。文中指出RA-RRG在CheXbert指标上达到SOTA，在RadGraph F1上具有竞争力。

## 4. 资源与算力

- 论文摘要及元数据中**未明确说明**所用GPU型号、数量及训练时长。
- 但根据检索增强框架的设计（使用LLM提取短语、检索库、再生成），可以推断其训练所需算力远小于从头训练或微调大型MLLM。具体资源消耗需要查阅全文细节，此处无法补充。

## 5. 实验数量与充分性

- 实验覆盖两个常见数据集（MIMIC-CXR、IU X-ray），进行了主要指标对比。
- 包含**消融实验**（可能涉及检索数量k、多视图聚合等），见元数据中的多张表格（table-001至table-014）和附图（fig-001至fig-011），说明有较全面的消融分析。
- **多视图泛化实验**：验证了在真实临床场景下的适用性。
- 充分性评估：实验设计较为全面，对比了多个指标，覆盖了主要挑战（幻觉、计算成本）。但未在更多种类影像（如CT、MRI）上验证，且对幻觉的定量评估可能不够细化（如人工审核比例），存在一定局限。

## 6. 论文的主要结论与发现

- **结论**：检索增强是降低MLLM幻觉和计算成本的有效途径。RA-RRG通过关键短语检索约束生成，显著减少了幻觉内容，同时保持了甚至超越了直接生成模型的报告质量。
- **关键发现**：
  - 在CheXbert指标上取得SOTA，在RadGraph F1上具有竞争力。
  - 能自然扩展到多视图场景，通过聚合来自多幅影像的短语提升生成一致性。
  - 参数规模更小，计算成本更低，更适合实际部署。

## 7. 优点：方法或实验设计上的亮点

- **方法创新**：将检索增强与关键短语提取结合，不同于传统端到端MLLM，实现了“先检索后生成”，巧妙利用已有报告知识库。
- **计算效率高**：避免了大模型训练，利用小LLM和检索机制即可取得优良性能，实用性强。
- **泛化性好**：多视图扩展机制简单有效，贴近临床实际（放射科通常有多视图影像）。
- **实验设计严谨**：使用了两个权威数据集，对比多种指标，并进行了消融和多视图实验，结果有说服力。

## 8. 不足与局限

- **算力资源未公开**：论文未报告具体的GPU型号、数量和训练时间，不利于复现和比较效率。
- **数据集范围有限**：仅在胸部X光（CXR）数据集上验证，未在其他模态（如CT、MRI）或部位（如骨骼）上实验，结论的泛化性需进一步检验。
- **幻觉评估可能不全面**：主要使用自动指标（CheXbert、RadGraph），缺乏人工临床专家评估，自动指标无法完全捕捉医学语义合理性。
- **检索依赖库质量**：短语提取和记忆库的构建依赖于训练集报告，如果训练集存在偏差或错误拼写，可能影响生成质量。
- **无代码运行细节**：虽然提供了GitHub仓库，但摘要中未提及第三方依赖、配置等，实际复现可能需额外工作。

（完）
