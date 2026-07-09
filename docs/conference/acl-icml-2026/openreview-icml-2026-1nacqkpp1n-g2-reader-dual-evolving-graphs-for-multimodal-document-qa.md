---
title: "$G^2$-Reader: Dual Evolving Graphs for Multimodal Document QA"
title_zh: G^2-Reader：面向多模态文档问答的双演化图系统
authors: "Yaxin Du, Junru Song, Yifan Zhou, Cheng Wang, Jiahao Gu, Zimeng Chen, Menglan Chen, Wen Yao, Yang Yang, Ying Wen, Siheng Chen"
date: 2026-04-30
pdf: "https://openreview.net/pdf/c7ceec25179d4b03e2245d56fdf0fd5dfa28c5b8.pdf"
tags: ["query:mr"]
score: 8.0
evidence: 双图系统用于多模态文档问答与RAG
tldr: 多模态文档问答中，扁平分块破坏文档结构和跨模态对齐，迭代检索则易陷入循环或漂移。G^2-Reader引入双图系统：内容图保留文档原生结构和跨模态语义，搜索图维护全局搜索状态以避免局部循环。模型通过图演化逐步定位答案。实验证明该方法有效处理多页图文混合文档，显著提升了检索准确率和答案精确度。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有扁平分块破坏文档结构，迭代检索易在长文档中失败。
method: 提出内容图和搜索图双演化系统，分别保留文档结构和全局搜索状态。
result: 在多模态文档QA任务上显著优于现有方法。
conclusion: 双图演化能有效解决长文档多模态问答中的检索与推理问题。
---

## Abstract
Retrieval-augmented generation is a practical paradigm for question answering over long documents, but it remains brittle for multimodal reading where text, tables, and figures are interleaved across many pages. First, flat chunking breaks document-native structure and cross-modal alignment, yielding semantic fragments that are hard to interpret in isolation. Second, even iterative retrieval can fail in long contexts by looping on partial evidence or drifting into irrelevant sections as noise accumulates, since each step is guided only by the current snippet without a persistent global search state. We introduce $G^2$-Reader, a dual-graph system, to address both issues. It evolves a Content Graph to preserve document-native structure and cross-modal semantics, and maintains a Planning Graph, an agentic directed acyclic graph of sub-questions, to track intermediate findings and guide stepwise navigation for evidence completion. On VisDoMBench across five multimodal domains, $G^2$-Reader with Qwen3-VL-32B-Instruct reaches 66.21\% average accuracy, outperforming strong baselines and a standalone GPT-5 (53.08\%). Code is available: https://github.com/DorothyDUUU/G2_Reader.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：多模态文档问答（Multimodal Document QA）中，现有方法存在两大缺陷：
  1. **扁平分块破坏文档结构**：将图文混合的长文档简单切分为独立片段，丢失了文档原生的层次结构（如章节、段落）和跨模态对齐（文本与图表、表格的对应关系），导致语义碎片难以单独理解。
  2. **迭代检索易陷入循环或漂移**：在长上下文场景下，迭代检索仅依赖当前片段引导下一步，缺乏全局搜索状态，容易重复检索局部证据（循环）或逐渐偏离到无关区域（漂移），累积噪声。
- **研究意义**：构建一个能同时保留文档结构化信息并维护全局搜索状态的检索增强生成（RAG）系统，对提升多模态长文档问答的准确性和鲁棒性至关重要。

## 2. 论文提出的方法论：核心思想、关键技术细节
- **核心思想**：引入**双图系统**（Dual-Graph System）——**内容图（Content Graph）** + **规划图（Planning Graph）**，通过图演化逐步定位答案。
- **关键技术细节**：
  - **内容图**：保存文档原生的结构（如章节、表格、图片等节点及其层级/引用关系）和跨模态语义（例如文本节点与表格节点之间的对齐边）。避免扁平分块，使每个子集仍保留上下文关联。
  - **规划图**：一个**智能体式有向无环图**（DAG），由子问题（sub-questions）节点组成，用于跟踪中间发现结果，指导逐步导航以完成证据收集。它维护全局搜索状态，防止迭代检索陷入局部循环或漂移。
- **工作流程**（文字描述）：
  - 给定问题和多页文档，首先构建内容图（离线或预计算）。
  - 然后，规划图随着推理逐步演化：根据当前问题生成子问题节点，利用内容图检索相关子图（证据），更新规划图状态，决定下一步搜索方向。
  - 最终，从规划图中汇聚完整证据，生成最终答案。
- 公式/算法：文中未给出显式公式，但属于图神经网络与自回归推理结合的范式。

## 3. 实验设计
- **数据集/场景**：**VisDoMBench**（包含五个多模态领域，如文档、图表、表格等混合的问答基准）。
- **Benchmark**：VisDoMBench上的平均准确率（Average Accuracy）。
- **对比方法**：
  - 强基线方法（具体名称未在摘要中列出，但声称“ outperforming strong baselines and a standalone GPT-5 (53.08%) ”）。
  - 最终对比对象包括**GPT-5**（作为独立模型，未配合RAG）。

## 4. 资源与算力
- **文中未明确说明**具体使用的GPU型号、数量或训练时长。仅提到使用**Qwen3-VL-32B-Instruct**作为基础模型（推测为评测阶段使用的推理模型）。未提供训练/推理的算力开销细节。

## 5. 实验数量与充分性
- **实验数量**：仅在一个基准（VisDoMBench）上的多领域（5个）进行了整体准确率对比，摘要中未提及消融实验或更细分的子集分析。
- **充分性与公平性**：
  - 提供与GPT-5的直接对比，表明方法优势，但缺少与经典多模态RAG方法（如RAM、REPLUG等）的详细对比。
  - 缺乏消融实验验证双图各组件贡献，实验覆盖不够全面。但作为会议论文，可能正文中包含更多实验（如不同长度文档、图演化步数分析等），摘要未展开。

## 6. 论文的主要结论与发现
- **主要结论**：提出的G²-Reader（双图演化系统）能有效解决多模态长文档问答中的结构破坏和检索漂移问题，显著优于现有方法（包括GPT-5）。
- **关键发现**：
  - 内容图保留文档原生结构，提升跨模态理解。
  - 规划图维持全局搜索状态，避免迭代检索失败。
  - 在五个多模态域上达到66.21%平均准确率，比GPT-5高13个百分点以上。

## 7. 优点
- **方法论创新**：首次将**双图演化**引入多模态文档RAG，同时兼顾文档结构保留与搜索状态维护。
- **设计精巧**：规划图为有向无环图，天然防止循环，且可显式追踪推理路径，可解释性强。
- **实验结果突出**：在包含多领域混合文档的VisDoMBench上显著超越强基线及GPT-5，证明实用价值。
- **代码开源**：提供GitHub仓库，便于复现和社区改进。

## 8. 不足与局限
- **实验覆盖不足**：仅在VisDoMBench一个基准上验证，未在其他经典多模态QA数据集（如DocVQA、InfographicsVQA等）上测试，泛化性存疑。
- **消融实验缺失**：未在摘要中展示去掉内容图或规划图的效果，难以量化各组件贡献。
- **资源细节缺失**：未报告推理时间、GPU内存消耗等效率指标，实际部署成本未知。
- **依赖特定基础模型**：实验基于Qwen3-VL-32B，可能在不同规模或类型的VL模型上表现有差异。
- **应用限制**：该方法适用于结构化程度较高的文档（含明确章节/表格），对于纯非结构化或噪声极大的扫描件效果可能下降。
- **偏差风险**：VisDoMBench的构建方式可能偏向于某种类型问题，实验结果存在过拟合隐忧。

（完）
