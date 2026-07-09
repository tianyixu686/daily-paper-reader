---
title: "DocHop: Benchmarking Out-of-domain Multi-hop Reasoning in Information-Dense Documents"
title_zh: "DocHop: 信息密集文档中的域外多跳推理基准"
authors: "Zhuoran Yu, Le Thien Phuc Nguyen, Jaden Park, Xinyi Gu, Zexue He, Soochahn Lee, Rogerio Feris, Yong Jae Lee"
date: 2026-04-30
pdf: "https://openreview.net/pdf/9200ad9847da4c20f5706e69974714fc0960a622.pdf"
tags: ["query:mr"]
score: 9.0
evidence: 文档中多模态多跳推理的基准测试
tldr: 现有基准分别评估图表和文档问答，忽略了图表与文本上下文的整合推理。DocHop基准专门评估多模态大语言模型在文档图像中的综合图表-上下文多跳推理能力。问题要求模型根据文本叙述中描述的多步约束从图表中选择和聚合数据。该基准揭示了当前MLLMs在该任务上的不足，推动了多模态多跳推理的研究。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有基准未能评估模型整合图表与文本上下文进行多步推理的能力。
method: 构建DocHop基准，要求模型根据文本约束从图表中聚合数据。
result: 揭示了当前MLLMs在整合图表-上下文推理上的显著差距。
conclusion: 需要专门的多步跨模态推理能力来应对此类任务。
---

## Abstract
Multimodal Large Language Models (MLLMs) have achieved strong performance on structured visual understanding tasks such as chart and document question answering. However, existing benchmarks typically evaluate these domains in isolation, leaving underexplored a key capability: whether models can use textual context to determine how chart evidence should be selected, interpreted, and aggregated.
We introduce DocHop, a benchmark for integrated chart--context reasoning in document-style images. In DocHop, the document narrative specifies multi-step compositional constraints, while charts provide the corresponding data values. Questions are grounded on a semantic reference label defined in the narrative, requiring models to resolve target entities from context before aggregating evidence across multiple charts. To enable systematic evaluation, we construct DocHop via a stochastic logic-first generation pipeline with controllable reasoning depth and visual density, covering 1,876 examples across six task categories. Experiments on a wide range of proprietary and open-source MLLMs show a substantial gap to human performance: annotators achieve over 90% accuracy, while the best model reaches only 60.18%. Reasoning-enhanced models consistently show improved results, but performance degrades as reasoning complexity increases. 
Overall, DocHop provides a controlled testbed for challenging multi-hop document reasoning.

---

## 论文详细总结（自动生成）

# DocHop: 信息密集文档中的域外多跳推理基准——中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究动机**：现有的多模态大语言模型（MLLMs）在结构化视觉理解任务（如图表问答、文档问答）上表现良好，但这些基准通常**孤立地评估图表或文档领域**，忽略了模型是否能够根据**文本上下文**来决定图表证据应如何选择、解释和聚合这一关键能力。
- **核心问题**：模型能否在文档风格图像中，利用文本叙述中指定的**多步组合约束**，从多个图表中选取并聚合数据，完成跨模态的多跳推理？
- **整体含义**：当前的MLLMs缺乏整合图表与文本上下文的推理能力，需要专门的基准来推动这一方向的研究。DocHop 提供了一个受控的测试平台，用于挑战多跳文档推理。

## 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程

- **核心思想**：构建一个**通过多步组合约束在图表与文本间进行推理**的基准（DocHop）。文档叙述指定多步组合约束，图表提供相应数据值。问题基于叙述中定义的**语义参考标签**，模型需先解析上下文中的目标实体，再跨多个图表聚合证据。
- **关键技术细节**：
  - **数据生成管线**：采用**随机逻辑优先（stochastic logic-first）** 的生成流水线，具有**可控的推理深度**和**视觉密度**，覆盖6个任务类别，共1,876个样本。
  - **任务设计**：问题要求模型根据文本约束（如“哪些产品在A季度销量超过B产品的两倍？”）从图表中聚合数据，需要多步推理（例如：先定位目标实体，再跨图表比较、计算）。
  - **推理深度可控**：通过控制逻辑链的长度和图表数量来调节难度。
- **公式或算法流程**（文字说明）：
  1. 定义一组逻辑规则（如比较、聚合、过滤、排序等）。
  2. 随机生成叙述文本，包含多步约束，并嵌入对应的语义标签（如“产品X”、“季度Y”）。
  3. 生成与叙述匹配的图表（柱状图、折线图、表格等），图表中的数据值与叙述中的约束对应。
  4. 根据逻辑规则和图表数据自动生成问题及正确答案。
  5. 对每个样本，确保推理链的唯一性和可验证性。

## 3. 实验设计：使用了哪些数据集/场景，它的 benchmark 是什么，对比了哪些方法

- **基准 (Benchmark)**：DocHop 本身作为一个新基准，覆盖**6个任务类别**（具体类别摘要未列出，但可推测包括比较、聚合、筛选等），共**1,876个样本**。
- **实验场景**：文档风格图像（包含图表和文本），要求模型同时处理视觉图表和文本上下文。
- **对比方法**：
  - 多种**专有和开源 MLLMs**（未具体列出模型名称，但提及“reasing-enhanced models consistently show improved results”）。
  - 人类标注者作为性能上限：**人类准确率超过90%**。
- **评估指标**：准确率（Accuracy）。

## 4. 资源与算力

- **文中未明确说明**使用的GPU型号、数量或训练时长。仅描述了模型评估过程，未提及训练细节或资源消耗。因此无法总结具体算力要求。

## 5. 实验数量与充分性

- **实验数量**：论文在**一个基准（DocHop）** 上进行了评估，包含1,876个样本。报道了人类基线及多个MLLMs的结果，并进一步分析了**推理复杂度与性能之间的关系**（性能随复杂度增加而下降）。此外，还比较了“推理增强模型”（可能指使用CoT等策略的变体）与标准模型。
- **充分性与公平性**：
  - 覆盖了**6个任务类别**，具有多样性。
  - 使用了**随机逻辑优先生成管线**，确保每类样本的推理深度和视觉密度可控，有利于系统评估。
  - 人类标注者提供了高准确率基准，对比公平。
  - 但实验**仅在一个基准上**进行，缺乏跨基准的泛化验证；且未提供消融实验（如不同推理深度下的分解分析）的详细数据，因此充分性有一定局限。

## 6. 论文的主要结论与发现

- 当前最先进的MLLMs在DocHop上性能**远低于人类**：人类准确率>90%，最佳模型仅达**60.18%**。
- **推理增强模型**（例如使用链式思维）相比标准模型有**一致提升**，但性能仍随推理复杂度的增加而**显著下降**。
- 现有模型在**整合图表证据与文本上下文进行多步推理**方面存在显著差距，表明该能力是**尚未解决的挑战**，需要专门的多步跨模态推理能力。

## 7. 优点

- **任务设计新颖**：填补了现有基准在跨模态多跳推理上的空白，聚焦于图表与文本结合的复杂推理。
- **数据生成可控**：采用随机逻辑优先的生成管线，可调节推理深度和视觉密度，便于系统分析模型在**不同难度级别**上的表现。
- **覆盖全面**：包含6个任务类别，1,876个样本，规模适中但覆盖度较高。
- **人类基线清晰**：提供了90%+的人类准确率，明确指出了当前模型的不足。

## 8. 不足与局限

- **实验覆盖局限**：仅在DocHop单基准上评估，未在现有图表QA或文档QA基准上做迁移或对比，难以说明模型在其他任务上的泛化损失。
- **未报告算力资源**：无法复现或评估实验成本。
- **缺少消融实验**：未分析不同推理深度、图表数量、文本复杂度等因素对性能的影响，对模型失败原因的分析不够深入。
- **偏差风险**：数据由自动化管线生成，可能引入与真实文档风格（如布局、噪声）的差异；逻辑规则限定，可能未覆盖所有真实世界的多跳推理场景。
- **应用限制**：基准仅限于文档图像中的图表-文本推理，未涉及其他模态（如地图、流程图）或跨文档推理。

（完）
