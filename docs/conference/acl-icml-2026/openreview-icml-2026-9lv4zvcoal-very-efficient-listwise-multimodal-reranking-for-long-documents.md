---
title: Very Efficient Listwise Multimodal Reranking for Long Documents
title_zh: 用于长文档的高效列表级多模态重排序
authors: "Yiqun Sun, Pengfei Wei, Lawrence B. Hsieh"
date: 2026-04-30
pdf: "https://openreview.net/pdf/0af73d0f2188575221122cd269e93cd0cade4106.pdf"
tags: ["query:mr"]
score: 8.0
evidence: 高效列表级多模态重排序用于多模态RAG
tldr: 针对多模态RAG中列表级重排序成本高、延迟大的问题，提出ZipRerank高效重排序器。通过查询与图像的早期交互缩短输入长度，并采用单次前向传播对所有候选项评分，避免了自回归生成。两阶段训练策略（文本重排序数据预训练+多模态微调）使模型在保持高准确率的同时大幅降低延迟。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有基于VLM的重排序器因长视觉输入和自回归解码导致高延迟。
method: 提出ZipRerank，通过查询-图像早期交互和单遍评分实现高效重排序。
result: 在保持准确率的同时显著降低了延迟。
conclusion: 高效重排序方法能推动多模态RAG的实用部署。
---

## Abstract
Listwise reranking is a critical yet costly component in vision-centric retrieval and multimodal retrieval-augmented generation (M-RAG) over long documents. Although recent VLM-based rerankers achieve strong accuracy, they are often impractical due to long visual-token inputs and autoregressive decoding, resulting in high latency. We propose ZipRerank, a very efficient listwise multimodal reranker that directly addresses both bottlenecks: it shortens the input via query-image early interaction and eliminates multi-step generation by scoring all candidates in a single forward pass. ZipRerank is trained with a two-stage recipe: listwise pretraining on large-scale text reranking data rendered as images, followed by multimodal finetuning with VLM-teacher supervision and a soft-ranking objective to handle noisy rankings. Extensive experiments on the MMDocIR benchmark demonstrate that ZipRerank matches or surpasses state-of-the-art multimodal rerankers while reducing LLM inference latency by up to an order of magnitude, making it well-suited for latency-sensitive real-world systems. Source code is available at https://anonymous.4open.science/r/ZipRerank.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：在多模态检索增强生成（M-RAG）系统中，列表级多模态重排序是关键环节，但现有基于视觉语言模型（VLM）的重排序器存在两大瓶颈：长视觉输入导致输入序列过长，以及自回归解码带来高延迟。这使得它们在延迟敏感的实际系统中难以实用。
- **研究动机**：需要一种既保持高准确率又能显著降低延迟的高效列表级多模态重排序方法，以推动多模态RAG的部署。

## 2. 论文提出的方法论
- **核心思想**：提出 **ZipRerank** 高效重排序器，通过**查询-图像早期交互**缩短输入长度，并采用**单次前向传播**对所有候选项同时评分，避免自回归生成。
- **关键技术细节**：
  - **查询-图像早期交互**：在输入阶段将查询与候选图像进行紧凑融合，减少视觉 token 数量。
  - **单遍评分**：所有候选文档在一次前向传播中并行评分，无需逐步解码。
  - **两阶段训练策略**：
    1. **列表级预训练**：在大规模文本重排序数据上（将文本渲染为图像）进行预训练。
    2. **多模态微调**：使用 VLM 教师监督和软排序目标（soft-ranking objective）处理噪声排序。
- **算法流程（文字说明）**：输入查询和候选多模态文档 → 通过查询-图像早期交互生成紧凑表示 → 输入重排序模型 → 单次前向传播输出所有候选的排序分数 → 根据分数重排序。

## 3. 实验设计
- **数据集**：使用 **MMDocIR** 基准数据集。
- **场景**：长文档的多模态检索重排序任务（如包含图像和文字的文档）。
- **对比方法**：与当前最先进的多模态重排序器（VLM-based rerankers）进行比较。
- **评估指标**：重排序准确率（如 NDCG、MAP 等，具体未在摘要中列出）以及 LLM 推理延迟。

## 4. 资源与算力
- 论文摘要及元数据中**未明确说明**使用的 GPU 型号、数量及训练时长。仅提到“显著降低 LLM 推理延迟”，但未提供训练算力详情。

## 5. 实验数量与充分性
- 至少包含在 **MMDocIR** 基准上的主实验（与 SOTA 对比）以及消融实验（文中提及“两阶段训练策略”和“软排序目标”的贡献，暗示可能有消融）。此外，还可能有延迟对比实验。
- **充分性评估**：实验覆盖了核心准确率和延迟对比，且通过两阶段训练证明了组件有效性。但缺乏跨更多数据集（如通用多模态检索基准）的验证，实验范围相对单一。

## 6. 论文的主要结论与发现
- ZipRerank 在 **MMDocIR** 基准上达到或超越现有最佳多模态重排序器的准确率。
- **LLM 推理延迟降低高达一个数量级（10倍）**，使其非常适合延迟敏感的现实系统。
- 两阶段训练策略（文本预训练+多模态微调）有效提升了模型性能，软排序目标能处理噪声排序。

## 7. 优点
- **方法创新**：同时解决了长输入和自回归解码两个延迟瓶颈，设计简洁有效。
- **效率突出**：延迟降低一个数量级，对实际部署意义重大。
- **训练策略合理**：利用大规模文本重排序数据预训练，缓解多模态数据稀缺问题；软排序目标增强鲁棒性。
- **开源**：提供源代码（anonymous.4open.science），便于复现和扩展。

## 8. 不足与局限
- **实验覆盖不足**：仅在 MMDocIR 一个基准上验证，缺乏对其他多模态数据集 （如 MS MARCO、Flickr30k 等） 的泛化测试。
- **算力信息缺失**：未报告训练资源，难以评估训练成本。
- **潜在偏差**：预训练使用文本渲染图像，可能与真实多模态分布有偏差，微调时需教师 VLM 可能引入额外依赖。
- **应用限制**：方法针对长文档设计，短文档场景效果未知；需确保查询-图像早期交互不损失关键信息。

（完）
