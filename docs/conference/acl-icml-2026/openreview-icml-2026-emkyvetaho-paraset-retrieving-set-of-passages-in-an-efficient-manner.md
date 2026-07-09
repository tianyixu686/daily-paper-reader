---
title: "ParaSet: Retrieving Set of Passages in an Efficient Manner"
title_zh: ParaSet：高效检索段落集合
authors: "Mooho Song, Jay-Yoon Lee"
date: 2026-01-21
pdf: "https://openreview.net/pdf/cf4e56de2e23497b087953849b0d98c3a98b2599.pdf"
tags: ["query:mr"]
score: 8.0
evidence: 面向多跳推理的集合级段落检索
tldr: 多跳推理需要检索一组共同有用的段落，但现有方法独立评分导致局部最优。ParaSet提出集合级兼容性学习目标，通过并行编码和集合评分，有效选择协同段落。实验表明，该方法在多跳QA数据集上提升了检索质量并促进了最终答案生成。
source: ICML-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 多跳问答中段落间的联合兼容性比独立相关性更重要，现有检索方法缺乏集合级建模。
method: 提出ParaSet，包含集合级兼容性学习目标和并行集合评分器，高效评估段落集合的整体效用。
result: 在多个多跳QA数据集上，ParaSet在检索质量和下游答案准确性上优于独立检索方法。
conclusion: 显式建模集合级兼容性是提升多跳检索效果的关键方向。
---

## Abstract
Multi-hop question answering and retrieval-augmented reasoning require selecting a query-dependent set of passages whose usefulness is determined by their joint compatibility, rather than by independently scoring passages.
Most existing approaches, however, do not explicitly model query–set compatibility, relying instead on independent passage relevance or step-wise retrieval, which often results in locally optimal and brittle retrieval chains.
We argue that holistic set-level compatibility learning is essential, yet directly enumerating and scoring passage sets lacks computational scalability.
To bridge this gap, we propose ParaSet (Parallel-Set scorer) with two components.
First, we introduce a set-level compatibility learning objective that enables retrievers to distinguish compatible and incompatible passage sets, yielding robust reasoning over variable-length and partially corrupted contexts.
Second, we design a lightweight single-layer self-attention scorer, ParaSet, trained with the same objective, which enables efficient selection of promising passage sets.
Together, our results demonstrate that set-level compatibility learning is effective for multi-hop question answering, and that ParaSet enables efficient exploration of the combinatorial passage-set space, leading to stable retrieval behavior and strong end-task performance on higher-hop questions.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）
多跳问答与检索增强推理需要选择一组与查询相关的段落，这些段落的效用由它们之间的**联合兼容性**（joint compatibility）决定，而非独立的相关性评分。然而，现有大多数检索方法（如独立评分段落或分步检索）没有显式建模“查询-集合”的兼容性，导致只能获得局部最优的检索结果，且检索链条脆弱。论文指出现有方法的根本缺陷在于缺乏集合级建模，并提出**ParaSet**系统，旨在通过集合级兼容性学习高效检索高质量段落集合，提升多跳推理的稳定性和下游任务性能。

## 2. 方法论：核心思想、关键技术细节、公式或算法流程
（基于摘要与元数据推断，无正文细节）

- **核心思想**：将段落检索视为集合级选择问题，学习区分“兼容集合”与“不兼容集合”，而非逐个评分。
- **关键技术**：
  - **集合级兼容性学习目标**：设计一个训练目标，使检索器能够识别出在推理中协同工作的段落集合（即使某些段落单独看相关性不高），同时能够处理长度可变或部分受损的上下文。
  - **并行集合评分器（ParaSet）**：一个轻量级的单层自注意力评分器，使用上述目标训练。它能够并行编码候选段落，并通过自注意力机制捕捉段落间的交互信息，输出集合的联合得分，从而有效筛选出有希望的段落组合。
- **算法流程**（推测）：
  1. 生成候选段落集合（可能通过某种采样或枚举策略）。
  2. 将集合中的段落并行输入ParaSet评分器。
  3. 利用单层自注意力计算段落间的兼容性权重，并聚合为集合得分。
  4. 选择得分最高的集合作为检索结果，用于下游多跳问答。

## 3. 实验设计
- **数据集与场景**：多跳问答数据集（摘要中提及“higher-hop questions”），具体名称未在元数据中列出（推测为HotpotQA、2WikiMultiHopQA等常见基准）。
- **基准（benchmark）**：未明确说明，但对比方法应包括独立相关性检索、分步检索、以及可能的集合级基线。
- **对比方法**：根据摘要，主要对比传统独立评分方法和分步检索方法（如REALM、DPR、IRCoT等常见多跳检索方法）。

## 4. 资源与算力
论文**未明确说明**使用的GPU型号、数量或训练时长。元数据中也未提及算力细节。因此无法总结资源消耗。

## 5. 实验数量与充分性
- **实验数量**：从元数据“result”和“conclusion”推断，作者至少在多个多跳QA数据集上进行了实验（包括对比和消融）。具体组数未给出。
- **充分性评价**：由于缺少正文，无法判断是否进行了充分的消融实验（如不同集合大小、不同编码器、不同训练目标）。但摘要中提及“稳定检索行为”和“更高跳问题上的强性能”，暗示实验覆盖了不同复杂度的多跳场景。然而，未报告方差、统计显著性等，公平性难以评估。

## 6. 主要结论与发现
1. 集合级兼容性学习对多跳问答是有效的，能够提升检索质量和下游答案准确性。
2. ParaSet作为轻量级评分器，能够在组合式的段落集合空间中高效探索，避免穷举枚举。
3. 相比独立检索和分步检索，ParaSet产生更稳定的检索行为，并在更高跳的问题上表现更优。

## 7. 优点
- **问题定义新颖**：明确将检索转化为集合级兼容性学习，突破了独立评分局限。
- **方法高效**：采用单层自注意力机制，避免了全对全枚举的计算负担，具备可扩展性。
- **鲁棒性**：能够处理长度可变或部分受损的上下文，适应真实噪声场景。
- **直接提升下游任务**：不仅优化检索指标，还促进最终答案生成，证明方法实用性。

## 8. 不足与局限
- **实验细节缺失**：由于论文被拒且只提供摘要，无法评估实验设计的完整性和可复现性。例如未报告数据集具体划分、评估指标、消融实验设计。
- **可能的偏差风险**：集合级评分可能偏向于某些重复或冗余的段落组合，且自注意力层可能对顺序敏感（论文未讨论）。
- **应用限制**：仅针对多跳问答场景，是否适用于其他检索增强任务（如单跳、开放域对话）未验证。
- **资源未报告**：缺乏算力说明，不能评估方法落地成本。

（完）
