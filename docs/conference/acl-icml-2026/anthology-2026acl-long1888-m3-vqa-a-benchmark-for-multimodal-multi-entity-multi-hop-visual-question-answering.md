---
title: "M3-VQA: A Benchmark for Multimodal, Multi-Entity, Multi-Hop Visual Question Answering"
title_zh: M3-VQA：多模态、多实体、多跳视觉问答的基准
authors: "Jiatong Ma, Longteng Guo, Yuchen Liu (刘雨辰), Zijia Zhao, Dongze Hao, Xuanxu Lin, Jing Liu (刘晶, 刘璟)"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.acl-long.1888.pdf"
tags: ["query:mr"]
score: 9.0
evidence: 多模态多跳推理外部知识库基准
tldr: 现有VQA数据集多关注单实体和简单推理，缺乏对多实体、多模态多跳推理的细粒度评估。本文提出M3-VQA基准，包含多样化的多实体问题，要求模型从视觉和文本源进行顺序和并行多跳推理，并提供可追溯证据和精心策划的多模态知识库。通过在16个主流多模态大语言模型上的评估，M3-VQA揭示了现有模型在复杂多跳推理上的不足，为多模态多跳推理与外部知识检索的研究提供了重要测试平台。该基准对于推进多模态检索增强生成（RAG）和多跳推理能力评估具有关键价值。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1888/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1474, \"height\": 890, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1888/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1182, \"height\": 545, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1888/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1182, \"height\": 627, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1888/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1328, \"height\": 1339, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1888/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 849, \"height\": 866, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1888/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1627, \"height\": 942, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1888/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1476, \"height\": 736, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1888/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 931, \"height\": 732, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1888/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 729, \"height\": 641, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1888/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 933, \"height\": 1154, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1888/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 933, \"height\": 1233, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1888/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 933, \"height\": 773, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1888/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 933, \"height\": 701, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1888/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 930, \"height\": 627, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1888/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 930, \"height\": 702, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1888/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1641, \"height\": 540, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1888/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 573, \"height\": 723, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1888/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1650, \"height\": 791, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1888/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1585, \"height\": 465, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1888/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1509, \"height\": 358, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1888/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1645, \"height\": 500, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1888/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 740, \"height\": 362, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1888/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 782, \"height\": 411, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1888/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1530, \"height\": 317, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1888/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1635, \"height\": 214, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1888/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1604, \"height\": 2167, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1888/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1579, \"height\": 1469, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1888/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1601, \"height\": 1470, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1888/table-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1193, \"height\": 1247, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1888/table-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1050, \"height\": 431, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1888/table-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 1255, \"height\": 282, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1888/table-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 1636, \"height\": 1139, \"label\": \"Table\"}]"
motivation: 现有VQA数据集对多模态多实体多跳推理的评估不足，缺乏细粒度和可追溯的评估基准。
method: 构建M3-VQA基准，包含多实体问题、多模态知识库和可追溯证据，支持顺序和并行多跳推理。
result: 在16个多模态大模型上的评估揭示了模型在复杂多跳推理任务上的显著性能差距。
conclusion: M3-VQA为多模态多跳推理和外部知识检索提供了标准化评估平台，推动该领域发展。
---

## Abstract
We present M 3 -VQA, a novel knowledge-based Visual Question Answering (VQA) benchmark, to enhance the evaluation of multimodal large language models (MLLMs) in fine-grained multimodal entity understanding and complex multi-hop reasoning. Unlike existing VQA datasets that focus on coarse-grained categories and simple reasoning over single entities, M 3 -VQA introduces diverse multi-entity questions involving multiple distinct entities from both visual and textual sources. It requires models to perform both sequential and parallel multi-hop reasoning across multiple documents, supported by traceable, detailed evidence and a curated multimodal knowledge base. We evaluate 16 leading MLLMs under three settings: without external knowledge, with gold evidence, and with retrieval-augmented input. The poor results reveal significant challenges for MLLMs in knowledge acquisition and reasoning. Models perform poorly without external information but improve markedly when provided with precise evidence. Furthermore, reasoning-aware agentic retrieval surpasses heuristic methods, highlighting the importance of structured reasoning for complex multimodal understanding. M 3 -VQA presents a more challenging evaluation for advancing the multimodal reasoning capabilities of MLLMs. Our code and dataset are available at https://github.com/CASIA-IVA-Lab/M3VQA.

---

## 论文详细总结（自动生成）

# 论文总结：M3-VQA：多模态、多实体、多跳视觉问答的基准

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：现有知识型VQA数据集（如OK-VQA、A-OKVQA）主要关注粗粒度类别和单实体简单推理，缺乏对多实体、多模态、多跳推理的细粒度评估。真实场景中，VQA需要识别图像中的多个细粒度实体（如人名、品牌、动物种类），并整合跨文档的外部知识进行多步推理。
- **研究动机**：为了填补这一空白，作者提出了M3-VQA基准，旨在评估多模态大语言模型（MLLMs）在**多实体交互**、**跨文档顺序/并行多跳推理**方面的能力。
- **整体含义**：M3-VQA为推进多模态复杂推理研究提供了更具挑战性的测试平台，揭示了当前MLLMs在知识获取和推理上的显著局限。

## 2. 论文提出的方法论：核心思想、关键技术细节
- **核心思想**：构建一个包含多实体图像、多跳问题、可追溯证据链和受控多模态知识库的VQA基准，支持并行和顺序两种多跳推理模式。
- **关键技术细节**：
  - **图像与实体标注**：从CelebTo、FGVD、FlickrLogos等细粒度图像数据集获取多实体图像；同时扩展单实体数据集（EVQA、InfoSeek）到多跳设置；人工补充多实体场景。
  - **实体链接与扩展**：将实体标签映射到Wikidata ID，进而获取对应的Wikipedia文章，实现多模态对齐。
  - **问题生成**：
    - **并行多跳问题**：利用Wikidata三元组设计模板，通过SPARQL查询获取答案；加入额外文本实体并聚合子答案。
    - **序列多跳问题**：采用“桥接实体”思想，将前一个答案作为下一个问题的输入，通过LLM生成候选问题并验证。
  - **知识库与证据标注**：从约200万实体的Wikipedia快照中提取文本和图像构建多模态知识库；为每个子问题标注支持句子作为金证据。
  - **质量控制**：人工筛选、多轮过滤、平衡分布，最终保留13k个（I, Q, A）三元组。
- **任务定义**：函数 f: (I, Q, K) → A，其中I为图像，Q为问题，K为外部Wikipedia知识库，A为答案。每个样本有参考证据链E。
- **复杂度度量**：实体复杂度（视觉+文本实体数），跳数复杂度（证据链节点数）。

## 3. 实验设计：数据集/场景、基准、对比方法
- **数据集**：M3-VQA（13,125个样本，10,565张图像，7,611个唯一问题，平均跳数3.1，平均实体数2.8）。
- **评估设置**：三种设定：
  - **Original**：仅提供图像和问题，无外部知识。
  - **Oracle**：提供金证据（分为句子级、章节级、实体名级三种粒度）。
  - **KB**：提供知识库，使用检索方法（Heuristic Retrieval 和 Agentic Retrieval）。
- **对比方法**：16个MLLMs，包括：
  - 闭源：GPT-4o
  - 开源：Qwen2.5-VL（3B/7B/32B/72B）、InternVL2.5（1B至78B各版本）、Qwen2-VL、LLaVA-OneVision、DeepSeek-VL2、MiniCPM-V-2.6
  - 纯语言模型：Llama-3.1-8B、Qwen2.5-7B（将图像替换为文本描述）
- **评价指标**：采用IoU（交集/并集）计算预测答案集与真实答案集的准确率，最终取算术平均。字符串答案精确匹配，时间答案允许一年误差。

## 4. 资源与算力
- **计算资源**：使用内部计算集群，配备NVIDIA A800 GPU。总计算成本约为**2000 GPU小时**，主要用于数据集构建和模型推理。未提及GPU具体数量或训练时长（未进行大规模训练）。
- **推理加速**：使用vLLM框架加速推理。未报告模型训练成本。

## 5. 实验数量与充分性
- **实验数量**：进行了大量实验，包括：
  - Original设置下16个模型在所有跳数和实体复杂度上的对比（约16×4×4 = 256个数据点）。
  - Oracle设置下6个模型在三种证据粒度上的对比。
  - KB设置下6-8个模型在两种检索方法上的对比。
  - 消融实验：证据数量对固定复杂度问题（4实体并行、3跳串行）的影响分析。
  - 跳数与实体数的影响分析（线图）。
  - 检索准确率分析（Heuristic vs Agentic）。
- **充分性**：实验覆盖了不同模型家族、参数规模、输入类型（多模态vs纯文本）、证据提供方式，全面评估了M3-VQA的挑战性。公平性方面，统一使用IoU指标，并控制了推理设置（如使用相同的检索器）。但缺少对不同推理策略（如Chain-of-Thought）的系统评估，且部分模型在长上下文下的KB结果可能缺失。

## 6. 论文的主要结论与发现
1. **M3-VQA对现有MLLMs极具挑战**：最佳模型Qwen2.5-VL-72B在Original设置仅有32.6%准确率。
2. **外部知识至关重要**：无外部知识时性能很差；提供金证据后大幅提升（最高58.7%），但仍有较大差距。
3. **实体识别是瓶颈**：从无证据到仅提供实体名，提升10.2%（约32.6%→45.1%），但精细属性检索仍需进一步改进（句子级证据进一步+15.2%）。
4. **检索方法影响显著**：Agentic Retrieval（分解问题、迭代检索）优于Heuristic Retrieval（单次全文检索），在KB设置下提升约3-5%绝对准确率。
5. **复杂度与性能负相关**：随着跳数或实体数增加，模型准确率单调下降（Oracle设置下）；但在无证据时，高跳/多实体问题可能因包含更多文本实体而反而表现稍好。
6. **视觉信息不可缺少**：仅用问题文本（Q-Only）性能（15.6%）显著低于Original（24.5%），证明图像输入对细粒度实体识别至关重要。

## 7. 优点：方法或实验设计上的亮点
- **新颖的基准设计**：同时涵盖多实体、多跳、可追溯证据链，填补了现有VQA基准的空白。
- **两种推理模式**：明确区分并行和顺序多跳推理，便于深入分析模型推理架构。
- **可控的知识库**：提供受控Wikipedia知识库和多种粒度金证据（句子、章节、实体名），支持精确评估。
- **全面的模型评估**：覆盖16个主流MLLMs，包括不同家族和规模，实验设置丰富（无证据、金证据、检索增强）。
- **代理检索方法**：Agentic Retrieval通过对象检测分割图像、分解查询、迭代规划，显著优于简单检索，为多跳检索提供了有效思路。
- **严谨的质量控制**：人工筛选、93%标注准确率，确保数据质量。

## 8. 不足与局限
- **语言限制**：仅限英文，无法评估跨语言或多语言推理。
- **知识来源单一**：仅基于Wikipedia，缺乏专业领域知识（如生物医学、法律）。
- **数据规模较小**：13k个样本，相较于百万级数据集仍较小，可能影响统计稳定性。
- **不可避免的噪声**：尽管人工筛选，但仍存在少量错误或歧义样本。
- **未系统评估推理策略**：未探索Chain-of-Thought等prompt方法对模型性能的影响。
- **模型评估的一次性**：每个实验仅运行一次，未报告方差，可能缺乏统计显著性。
- **代理检索的依赖性**：Agentic Retrieval使用GPT-4o作为规划器，可能存在成本高、可重复性问题。
- **计算资源报告不详细**：仅总GPU小时数，未说明每个模型的具体推理时间和资源分配。

（完）
