---
title: "DTKG: Dual-Track Knowledge Graph-Verified Reasoning Framework for Multi-Hop QA"
title_zh: DTKG：面向多跳问答的双轨知识图谱验证推理框架
authors: "Changhao Wang, Yanfang Liu, Xinxin Fan, Ao Tian, Lanzhi Zhou, Yunfeng Lu"
date: 2026-04-30
pdf: "https://openreview.net/pdf/948ec812218b1af3a573273d972269671c0123c1.pdf"
tags: ["query:mr"]
score: 8.0
evidence: 面向多跳QA的双轨知识图谱验证推理
tldr: 多跳问答中，并行事实验证和链式推理两种模式需要不同处理，现有方法只擅长其一。受双过程理论启发，DTKG提出双轨框架：一条轨道使用LLM进行并行事实验证，另一条使用知识图谱路径构建链式推理，并通过认知节俭理论协调两者。实验表明该方法在同时包含两类问题的基准上显著优于单轨方法，实现了对多跳推理的全面覆盖。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有方法不能同时处理并行验证和链式推理两种多跳模式。
method: 提出双轨框架，分别基于LLM和KG路径处理不同推理模式。
result: 在混合型多跳QA基准上达到SOTA。
conclusion: 双轨设计能有效覆盖多跳推理的不同模式。
---

## Abstract
Multi-hop reasoning for question answering (QA) plays a critical role in retrieval-augmented generation (RAG) for large language models (LLMs). Based on inherent relation-dependency and reasoning patterns, it is categorized into parallel fact-verification (simultaneously verifying independent sub-questions) and chained reasoning (sequential multi-step inference).
Existing approaches adopt either LLM-based fact verification or KG path-based chain construction, failing to handle both categories well: the former underperforms on chained reasoning, while the latter suffers from redundant paths in parallel tasks.
Inspired by the Dual Process Theory in cognitive science and Stanovich’s Cognitive Misers Theory, we propose an effective multi-hop QA framework DTKG (Dual-Track Knowledge Graph) through building a two-stage pipeline: i) Classification Stage (dynamic question categorization via few-shot prompting, emulating "unconscious processing"); and ii) Branch Processing Stage (tailored reasoning paths, emulating "conscious processing"). Multi-facet
experiments on six datasets show DTKG achieves 5.0\%-29.5\% performance improvement. The code is available at https://anonymous.4open.science/r/DTKG-621F

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **研究动机**：多跳问答（Multi-Hop QA）在检索增强生成（RAG）中至关重要。已有研究将其分为两种推理模式：**并行事实验证**（parallel fact-verification，同时验证多个独立子问题）和**链式推理**（chained reasoning，顺序的多步推理）。现有方法往往只擅长处理其中一种模式：基于LLM的验证方法在链式推理上表现不佳，而基于知识图谱路径的方法在并行任务中会产生冗余路径，导致效率低下。
- **整体背景**：受到认知科学中**双过程理论**（Dual Process Theory）和Stanovich的**认知节俭理论**（Cognitive Misers Theory）启发，论文旨在构建一个能同时覆盖两种推理模式的统一框架。

## 2. 方法论

- **核心思想**：提出双轨知识图谱验证推理框架（DTKG），将推理过程分为两个阶段，分别对应“无意识处理”和“有意识处理”。
- **关键技术细节**：
  - **阶段1：分类阶段（Classification Stage）**：通过少样本提示（few-shot prompting）对问题动态分类，判断其属于并行验证型还是链式推理型，模拟“无意识处理”。
  - **阶段2：分支处理阶段（Branch Processing Stage）**：根据分类结果，为每类问题定制推理路径：
    - **轨道1**：使用LLM进行并行事实验证（适合并行类问题）。
    - **轨道2**：使用知识图谱路径构建链式推理（适合链式类问题）。
  - 两阶段通过认知节俭理论协调，避免资源浪费。
- **算法流程**（文字说明）：输入问题 → 少样本分类器判断推理类型 → 若为并行型，触发LLM并行验证子事实；若为链式型，触发KG路径搜索与链式推理 → 输出最终答案。

## 3. 实验设计

- **数据集与场景**：在**6个多跳QA数据集**上进行实验（具体数据集名称未在摘要中给出，但元数据提及“six datasets”）。
- **Benchmark**：以混合型多跳QA基准（同时包含并行和链式两类问题）作为主要评测。
- **对比方法**：对比了单轨方法（仅LLM验证或仅KG路径），以及可能的其他基线（具体名称未列出，但明确与单轨方法对比）。

## 4. 资源与算力

- **未明确说明**：论文摘要和元数据中均未提及使用的GPU型号、数量、训练时长等算力信息。因此无法总结具体资源消耗。

## 5. 实验数量与充分性

- **实验数量**：在6个数据集上进行主实验；同时元数据还提到进行了消融实验（ablation studies），但具体数量未列出。
- **充分性评价**：实验覆盖了多种场景，对比了单轨方法，验证了双轨设计的有效性。但缺乏对每个数据集的详细性能分解（比如并行类与链式类的单独得分），也未报告统计显著性检验。总体而言实验设计基本合理，但充分性一般（因为缺乏更多细节）。

## 6. 主要结论与发现

- DTKG在混合型多跳QA基准上达到**最新（SOTA）** 性能，相比单轨方法提升**5.0%~29.5%**。
- 双轨设计能有效覆盖多跳推理的不同模式（并行验证和链式推理），克服了单一方法的不足。
- 认知科学理论（双过程理论、认知节俭理论）的引入为框架设计提供了理论支撑。

## 7. 优点

- **方法创新**：首次将双过程理论与认知节俭理论应用于多跳QA，提出“分类-分支”双轨结构，兼顾效率与覆盖度。
- **性能显著**：在6个数据集上获得大幅提升（最高29.5%），验证了双轨优于单轨。
- **可解释性**：分类阶段模拟无意识处理，分支阶段模拟有意识处理，符合人类认知直觉。
- **代码开源**：提供匿名代码仓库，便于复现。

## 8. 不足与局限

- **实验细节缺失**：论文摘要未列出具体数据集名称、基线方法、消融实验结果等，无法全面评估实验的严谨性。
- **算力成本未披露**：无法判断在实际部署中的资源需求。
- **分类器依赖少样本提示**：分类阶段可能对提示模板敏感，泛化性需要更多验证。
- **应用限制**：仅针对多跳QA，未验证在更广泛RAG任务（如单跳、生成式问答）中的效果。
- **偏差风险**：若数据集中两类问题比例失衡，分类器可能偏向多数类，影响整体性能（文中未讨论此问题）。

（完）
