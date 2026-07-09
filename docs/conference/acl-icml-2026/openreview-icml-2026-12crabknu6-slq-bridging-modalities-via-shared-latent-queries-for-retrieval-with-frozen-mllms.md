---
title: "SLQ: Bridging Modalities via Shared Latent Queries for Retrieval with Frozen MLLMs"
title_zh: SLQ：通过共享潜在查询桥接模态以利用冻结多模态大模型进行检索
authors: "Haoran Lou, Ziyan Liu, Chunxiao Fan, Yuexin Wu, Yue Ming, Hao Wu, Kai Zuo, Yibo Chen, Xu Tang"
date: 2026-04-30
pdf: "https://openreview.net/pdf/f5336c9fde56516fb74b3c3522df776ff85aee15.pdf"
tags: ["query:mr"]
score: 8.0
evidence: 通过共享潜在查询实现冻结多模态大模型的跨模态检索
tldr: 现有方法微调MLLM用于检索会破坏预训练语义空间，本文提出SLQ，通过引入少量共享潜在查询，在保持骨干网络冻结的情况下聚合多模态上下文，实现参数高效的跨模态检索。实验表明SLQ在多个跨模态检索基准上达到最优，且不损害原有推理能力。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 微调MLLM用于检索会破坏语义空间，缺乏参数高效方法。
method: 引入共享潜在查询，利用因果注意力聚合多模态上下文进行冻结检索。
result: 在跨模态检索任务上取得最优，且保持预训练能力。
conclusion: SLQ提供了一种冻结MLLM的高效跨模态检索方法。
---

## Abstract
Multimodal Large Language Models (MLLMs) possess intrinsic reasoning and world-knowledge capabilities, yet adapting them for dense retrieval remains challenging. Existing approaches rely on invasive parameter updates, such as full fine-tuning and LoRA, which may disrupt the pre-trained semantic space and impair the structured knowledge essential for reasoning. To address this, we propose **SLQ**, a parameter-efficient tuning framework that adapts MLLMs for retrieval while keeping the backbone entirely frozen. SLQ introduces a small set of **Shared Latent Queries** that are appended to both text and image tokens, leveraging the model’s native causal attention to aggregate multimodal context into a unified embedding space. Furthermore, to better evaluate retrieval beyond superficial pattern matching, we construct **KARR-Bench**, a benchmark designed for knowledge-aware reasoning retrieval. Extensive experiments show that SLQ outperforms full fine-tuning and LoRA on COCO and Flickr30K, while achieving competitive performance on MMEB and yielding substantial gains on KARR-Bench, validating that preserving the pre-trained representations via non-invasive adaptation is an effective strategy for MLLM-based retrieval. The code is available under: https://github.com/CnFaker/SLQ.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **核心问题**：多模态大语言模型（MLLMs）具有丰富的推理能力和世界知识，但将其适配用于密集检索任务时面临挑战。现有方法（如全微调、LoRA）通过侵入式参数更新来适配检索，这很可能破坏预训练的语义空间，损害模型固有的结构化知识，从而影响推理能力。
- **动机**：需要一种参数高效的、非侵入式的适配方法，在保持MLLMs骨干网络冻结的情况下实现高效的跨模态检索，同时不损害原有的推理能力。
- **背景**：当前缺乏针对冻结MLLMs进行检索的参数高效方法，已有方法要么性能受限，要么破坏语义空间。

## 2. 方法论：SLQ

- **核心思想**：引入少量**共享潜在查询（Shared Latent Queries）**，将其附加到文本和图像令牌之后，利用模型原生的因果注意力机制，自动聚合多模态上下文信息，形成一个统一的嵌入空间用于检索，而无需更新骨干参数。
- **关键技术细节**：
  - 共享潜在查询是一组可学习的向量，在输入时追加到文本与图像嵌入序列末尾。
  - 利用MLLMs的因果注意力（causal attention）机制，使得查询能够“看到”所有输入令牌（文本和图像），从而聚合多模态上下文。
  - 最终查询的输出作为检索的嵌入表示。
  - 训练时仅更新这些少量查询的参数，整个MLLM骨干冻结，实现参数高效的非侵入式适配。
- **公式/算法流程**（文字说明）：
  - 输入：图像+文本（如标题与图像对）。
  - 处理：提取图像与文本令牌嵌入，在序列末尾插入共享潜在查询（例如N个查询）。
  - 前向传播：通过冻结的MLLM骨干，利用因果注意力计算。查询通过注意力层聚合所有之前令牌（包括图像和文本）的信息。
  - 输出：取查询对应的隐藏状态作为联合嵌入，用于对比学习或检索任务。
  - 损失：采用对比损失（如InfoNCE）进行训练。

## 3. 实验设计

- **数据集/场景**：
  - 跨模态检索：COCO、Flickr30K（图像-文本检索）。
  - 多模态嵌入基准：MMEB。
  - 知识感知推理检索：作者构建了**KARR-Bench**基准，专门用于评估超越表面模式匹配的知识推理检索。
- **Benchmark**：COCO、Flickr30K、MMEB、KARR-Bench。
- **对比方法**：
  - 全微调（full fine-tuning）
  - LoRA（低秩适配）
  - 可能还包括其他冻结基线（如CLIP、ALIGN等），但摘要未详细列出。
- **实验充分性**：包含多个标准检索基准和新构建的推理检索基准，对比了侵入式和非侵入式方法，覆盖常见跨模态检索任务。

## 4. 资源与算力

- 论文摘要和元数据中**未明确说明**所使用的GPU型号、数量、训练时长等具体算力信息。
- 可以推测：由于仅训练少量查询参数，所需算力应远小于全微调，但具体数值未给出。

## 5. 实验数量与充分性

- **实验组数**：至少包括以下实验：
  - 在COCO和Flickr30K上与全微调和LoRA对比。
  - 在MMEB上与现有方法对比。
  - 在KARR-Bench上与全微调和LoRA对比。
  - 很可能还包含消融实验（如查询数量、冻结vs微调策略等），但摘要未展开。
- **充分性与公平性**：跨多个数据集、多种方法对比，且专门构建了推理检索基准，提升了评估的全面性。方法不更新骨干，公平性较好。但缺乏在更多样化场景（如视频检索、多语言）的验证，可能存在覆盖面不足。

## 6. 主要结论与发现

- SLQ在COCO和Flickr30K上**优于**全微调和LoRA，在MMEB上达到具有竞争力的性能，在KARR-Bench上获得**显著提升**。
- 验证了通过非侵入式适配（冻结骨干）保持预训练表示是一种有效的策略，能同时提升检索性能和保留推理能力。

## 7. 优点

- **方法新颖**：首次提出共享潜在查询在冻结MLLM上实现参数高效的跨模态检索，简单有效。
- **资源高效**：仅训练少量查询参数，训练成本低，且不破坏预训练语义空间。
- **实验设计合理**：包含标准检索和专门设计的推理检索基准，验证了方法不仅提升检索，还保持推理能力。
- **代码开源**：提供GitHub链接，可复现。

## 8. 不足与局限

- **实验覆盖有限**：仅在图像-文本检索和少量多模态基准上测试，未涉及视频、音频等其他模态的检索。
- **基准构建**：KARR-Bench是新基准，可能缺乏广泛性和标准性，其设计细节未详述，需进一步验证。
- **资源信息缺失**：未报告算力、训练时间等，难以评估实际计算成本。
- **潜在偏差**：方法依赖MLLM的因果注意力，对于某些架构（如编码器-解码器）可能不适用，泛化性需验证。
- **检索性能上限**：冻结骨干可能限制了在复杂任务上的能力提升，尤其当预训练语义空间与检索任务存在较大差异时。

（完）
