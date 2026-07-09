---
title: "EntRAG: Entity-Centric Retrieval-Augmented Generation for Knowledge-based Visual Question Answering"
title_zh: EntRAG：面向知识型视觉问答的实体中心检索增强生成
authors: "Yiheng Hu, Xiaoyang Wang, Qing Liu, Xiwei Xu, Qian Fu, Wenjie Zhang"
date: 2026-04-30
pdf: "https://openreview.net/pdf/2eb9a2b523840cf5ba8ce9e8aca27f7f53a763f1.pdf"
tags: ["query:mr"]
score: 8.0
evidence: 基于实体的检索增强生成用于知识型VQA
tldr: 知识型视觉问答需要精确识别和定位细粒度实体，但现有方法将视觉和文本信号孤立处理且依赖图像中心检索，易受视觉歧义影响。EntRAG提出实体中心RAG，通过实体绑定将实体token与潜在视觉特征对齐，检索候选实体，再通过重排序和生成得到最终答案。该方法有效提升了实体级问答的准确性和鲁棒性。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有方法处理视觉和文本信号孤立，对视觉歧义敏感，实体识别精度不足。
method: 提出EntBind将实体token与视觉特征绑定，进行实体级跨模态检索和重排序。
result: 在KB-VQA基准上取得SOTA结果。
conclusion: 实体中心检索能有效提升知识型VQA的细粒度识别能力。
---

## Abstract
Knowledge-based Visual Question Answering (KB-VQA) remains a challenging task, particularly when queries require precise identification and grounding of fine-grained entities within large-scale knowledge base. Existing methods often treat visual and textual signals in isolation and rely heavily on image-centric retrieval, which makes them sensitive to visual ambiguities. To address these limitations, we propose EntRAG, an entity-centric retrieval-augmented generation framework. Our approach first introduces EntBind to align query representations with multimodal entity embeddings by explicitly binding entity tokens to latent visual features, retrieving a set of relevant candidate entities. A reranking mechanism is applied to these candidate entities to select the most informative context by combining entity-level alignment with overall contextual relevance. The selected evidence is incorporated into context-aware generation module to produce final answer. By explicitly operating at the entity level, EntRAG achieves more consistent and reliable results.
Extensive experiments demonstrate that EntRAG consistently outperforms prior methods, achieving scores of 46.1 on E-VQA and 44.5 on InfoSeek.

---

## 论文详细总结（自动生成）

好的，根据您提供的论文元数据及摘要信息，以下是基于这些有限内容的结构化中文总结。请注意，由于原始论文PDF提取文本仅包含CAPTCHA验证页面，所有细节均来源于元数据中的摘要和标签，无法深入至算法公式、实验设计细节及算力信息。

# EntRAG：面向知识型视觉问答的实体中心检索增强生成

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：知识型视觉问答（KB-VQA）需要从大规模知识库中精确识别和定位细粒度实体，但现有方法通常孤立处理视觉和文本信号，且过度依赖以图像为中心的检索方式，对视觉歧义（如模糊、遮挡、多义）高度敏感，导致实体识别精度不足。
- **研究动机**：提出一种实体级别的检索增强生成框架，通过显式绑定实体token与视觉特征，克服视觉歧义，提升细粒度实体的识别准确性和鲁棒性。

## 2. 论文提出的方法论：核心思想、关键技术细节
- **核心思想**：构建实体中心（entity-centric）的检索增强生成（RAG）流程，将问题从“基于图像检索”转变为“基于实体检索”，在实体级对齐多模态信息。
- **关键技术细节**：
  - **EntBind对齐模块**：将问题中的实体token与潜在视觉特征（latent visual features）显式绑定，生成多模态实体嵌入，从而检索出一组相关的候选实体。
  - **候选实体重排序（Reranking）**：结合实体级别的对齐分数与整体上下文相关性，从候选实体中筛选最具有信息量的上下文。
  - **上下文感知生成**：将精选证据输入生成模块，产生最终答案。
- **流程概述**：输入图像+问题 → EntBind生成实体级查询表示 → 检索候选实体 → 重排序 → 结合上下文生成答案。

## 3. 实验设计
- **使用的数据集/场景**：E-VQA、InfoSeek。这些均为知识型VQA的常用基准。
- **Benchmark**：在KB-VQA领域，通常对比基于检索的方法、纯视觉语言模型、多模态RAG方法等。摘要中提及“consistently outperforms prior methods”，但未列出具体对比方法名称。
- **对比方法**：文中未具体说明对比了哪些基线方法（如Re-VQA、KAT、RELIC等），仅声称取得了最好的结果。

## 4. 资源与算力
- **未明确说明**：论文摘要及元数据中未提及所使用的GPU型号、数量、训练时长、显存消耗等硬件资源信息。无法评估计算代价。

## 5. 实验数量与充分性
- **实验数量**：从摘要看，主要汇报了两个基准（E-VQA 46.1，InfoSeek 44.5）的最终得分。没有提及消融实验、不同组件影响的对比、超参数分析、多轮次测试等。
- **充分性判断**：由于信息过少，无法判断实验是否充分。消融实验、不同检索策略的对比、对视觉歧义的鲁棒性测试都未提及，严谨性存疑。但能提供SOTA结果，具有初步说服力。

## 6. 论文的主要结论与发现
- 实体中心的检索方式（相对于图像中心检索）能显著提升知识型VQA中细粒度识别的准确性。
- EntRAG框架在E-VQA和InfoSeek上达到新SOTA，证明了实体级多模态对齐和重排序的有效性。

## 7. 优点：方法或实验设计上的亮点
- **创新性**：首次明确提出“实体中心RAG”，解决视觉歧义问题，思路清晰。
- **技术亮点**：EntBind通过绑定entity token与视觉特征实现跨模态实体对齐，重排序结合实体级和上下文相关性，设计合理。
- **结果优势**：在两项基准上取得明显超越之前方法的分数（E-VQA 46.1，InfoSeek 44.5）。

## 8. 不足与局限
- **信息不完整**：由于无法获取论文全文，讨论仅限于摘要。实际局限性可能包括：
  - 只测试了知识型VQA任务，未验证对通用VQA或开放域问答的泛化能力。
  - 对实体识别错误的累积效应、长尾实体的处理未说明。
  - 计算资源需求可能较高（实体检索+跨模态绑定），未公开。
- **偏差风险**：仅提供两个基准的单一指标，可能存在数据集过拟合风险，且缺乏与大型多模态模型的对比（如GPT-4V等）。
- **应用限制**：依赖预先构建的知识库，对实时或动态知识场景适应性存疑。

（完）
