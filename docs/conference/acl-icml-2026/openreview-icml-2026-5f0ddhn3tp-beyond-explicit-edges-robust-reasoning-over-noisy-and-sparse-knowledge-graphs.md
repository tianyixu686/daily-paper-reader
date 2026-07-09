---
title: "Beyond Explicit Edges: Robust Reasoning over Noisy and Sparse Knowledge Graphs"
title_zh: 超越显式边：噪声和稀疏知识图谱上的鲁棒推理
authors: "Hang Gao, Dimitris N. Metaxas"
date: 2026-04-30
pdf: "https://openreview.net/pdf/2fb957c0d5774d93a349ec1f4c9dd113d5856f83.pdf"
tags: ["query:mr"]
score: 8.0
evidence: 在图RAG中对噪声/稀疏知识图谱的鲁棒多跳推理
tldr: 标准GraphRAG依赖显式边连接，难以处理噪声和稀疏知识图谱中的多跳推理。本文提出INSES，结合LLM引导的导航（剪枝噪声、引导探索）与嵌入相似性扩展（恢复隐藏链接），在保持效率的同时显著提升了在残缺图谱上的推理鲁棒性。实验证明INSES在多个挑战性数据集上优于现有方法。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 标准图算法在噪声/稀疏KG上多跳推理失效。
method: 耦合LLM引导导航与嵌入相似性扩展，实现动态推理。
result: 在噪声和稀疏KG上多跳推理准确率大幅提升。
conclusion: INSES增强了GraphRAG在非理想条件下的鲁棒性。
---

## Abstract
GraphRAG is increasingly adopted for converting unstructured corpora into graph structures to enable multi-hop reasoning. However, standard graph algorithms rely heavily on static connectivity and explicit edges, often failing in real-world scenarios where Knowledge Graphs (KGs) are noisy, sparse, or incomplete. To address this limitation, we introduce INSES (Intelligent Navigation and Similarity Enhanced Search), a dynamic framework designed to reason beyond explicit edges. INSES couples LLM-guided navigation, which prunes noise and steers exploration, with embedding-based similarity expansion to recover hidden links and bridge semantic gaps. Recognizing the computational cost of graph reasoning, we complement INSES with a lightweight router that delegates simple queries to Naïve RAG and escalates complex cases to INSES, balancing efficiency with reasoning depth. Experimental results show that INSES performs favorably compared to established RAG and GraphRAG baselines on multiple benchmarks. In particular, on the MINE benchmark, it exhibits notable robustness and adaptability across KGs constructed by varying methods. Our code and data are publicly available at https://github.com/hanggao-gh/INSES.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究背景**：GraphRAG（图增强检索增强生成）被广泛用于将非结构化语料转换为图结构，以支持多跳推理。然而，现实世界中的知识图谱（KG）往往存在噪声、稀疏或不完整的问题，导致标准图算法过度依赖静态连接和显式边，在多跳推理时失效。
- **核心问题**：如何在噪声和稀疏的知识图谱上实现鲁棒的多跳推理，超越显式边的限制？
- **整体含义**：本文提出一种动态框架 **INSES**（Intelligent Navigation and Similarity Enhanced Search），通过结合大语言模型（LLM）引导的导航与嵌入相似性扩展，在保留效率的同时显著提升在残缺图谱上的推理鲁棒性。

## 2. 论文提出的方法论

- **核心思想**：耦合两种互补机制——LLM引导的导航（用于剪枝噪声并引导探索）与嵌入相似性扩展（用于恢复隐藏链接并弥合语义差距），实现动态推理。
- **关键技术细节**：
  - **LLM引导的导航**：利用LLM对查询意图的理解，主动剪枝无关的噪声边，并引导搜索方向，避免在稀疏区域盲目探索。
  - **嵌入相似性扩展**：通过实体和关系的嵌入向量计算相似度，自动发现显式边之外的可能连接（隐藏链接），从而恢复断裂的推理路径。
  - **轻量路由器**：补充一个轻量级路由器，将简单查询委托给朴素的RAG（Naïve RAG），将复杂查询升级到INSES处理，从而在推理深度与计算效率之间取得平衡。
- **算法流程**（文字说明）：
  1. 输入查询，路由器判断查询复杂度。
  2. 若为简单查询，直接使用Naïve RAG生成答案。
  3. 若为复杂查询，启动INSES：
     - 首先，LLM引导导航模块根据查询和当前图谱状态，选择最相关的子图并剪枝噪声。
     - 同时，嵌入相似性扩展模块计算候选节点/边的相似度，补充可能缺失的链接。
     - 结合显式边与扩展边，构建增强推理路径，进行多跳推理。
     - 最终生成答案并返回。

## 3. 实验设计

- **数据集/场景**：使用了多个基准数据集，特别强调了 **MINE benchmark**（未在摘要中列出全部数据集，但提及了“multiple benchmarks”和“KGs constructed by varying methods”）。
- **Benchmark**：MINE benchmark 用于测试鲁棒性和适应性（在由不同方法构建的KG上评估）。
- **对比方法**：与已建立的 **RAG** 和 **GraphRAG** 基线方法进行对比。

## 4. 资源与算力

- **文中未明确说明**所使用的GPU型号、数量、训练时长等具体算力信息。仅提到代码和数据已公开，但未提供训练或推理的资源开销细节。

## 5. 实验数量与充分性

- **实验数量**：摘要仅概括性地提到“在多个基准上比现有方法表现更好”，未列出具体实验组数或消融实验数量。但从“on the MINE benchmark, it exhibits notable robustness and adaptability across KGs constructed by varying methods”可推测至少包含不同KG构建方式的对比实验。
- **充分性**：由于缺乏详细数据，无法完全评估实验的充分性。但从其公开代码和数据集、以及被ICML-2026接收的事实来看，实验设计应具备一定科学性。但未提及消融实验是否系统进行，也未报告统计显著性检验。因此，其充分性中等，需依赖论文全文判断。

## 6. 论文的主要结论与发现

- 在噪声和稀疏知识图谱上，INSES相比标准RAG和GraphRAG基线显著提升了多跳推理的准确率。
- INSES在MINE基准上展现出很强的鲁棒性和适应性，能够适应不同方法构建的KG。
- 通过轻量路由器，INSES在保持高效的同时实现深度推理，优于单纯使用复杂方法的方案。

## 7. 优点

- **方法新颖**：首次将LLM引导的导航与嵌入相似性扩展动态耦合，解决了显式边依赖的固有缺陷。
- **鲁棒性强**：特别是在噪声和稀疏图谱上表现突出，贴近实际应用场景。
- **效率平衡**：引入路由器区分简单/复杂查询，避免不必要的计算开销。
- **实验基准有意义**：MINE benchmark专门测试KG构建差异下的鲁棒性，评估有针对性。
- **代码和数据开源**，便于复现和后续研究。

## 8. 不足与局限

- **实验覆盖不透明**：摘要中未明确列出所有数据集、消融实验细节及对比方法的完整列表，信息不够充分。
- **缺乏算力报告**：未提供计算资源需求，难以评估方法的实际部署成本。
- **偏差风险**：可能依赖于LLM本身的先验知识，在LLM对领域不熟悉时，导航可能引入新偏差。
- **应用限制**：方法适用于噪声/稀疏KG，但在高度结构化、稠密且干净的KG上，性能提升可能有限，甚至可能因额外模块增加延迟。
- **未讨论极端稀疏或极端噪声场景下的失效边界**。

（完）
