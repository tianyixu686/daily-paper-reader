---
title: Multimodal Function Vectors for Visual Relations
title_zh: 面向视觉关系的多模态函数向量
authors: "Shuhao Fu, Esther A Goldberg, Ying Nian Wu, Hongjing Lu"
date: 2026-04-30
pdf: "https://openreview.net/pdf/8c1aabf24a213fc9a4c7b2d756a346e677590124.pdf"
tags: ["query:post-multi"]
score: 8.0
evidence: 大语言模型中用于视觉关系的多模态函数向量
tldr: 针对大型多模态模型内部机制不透明的问题，通过因果中介分析发现少量注意力头编码视觉关系，提取多模态函数向量可干预模型行为，提升零样本关系推理准确率，为理解多模态学习提供新视角。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 大型多模态模型的关系学习机制尚不清晰。
method: 利用因果中介分析识别并提取编码视觉关系的函数向量。
result: 操控这些向量可提升零样本关系推理性能。
conclusion: 函数向量揭示多模态模型内部表示机制，有助于可解释性。
---

## Abstract
Large Multimodal Models (LMMs) demonstrate impressive in-context learning abilities from few multimodal demonstrations, yet the internal mechanisms supporting such task learning remain opaque. Building on prior work of Large Language Models, we show that a small subset of attention heads in Large Multimodal Models is responsible for transmitting representations of visual relations. The activations of these attention heads, termed $\textit{function vectors}$, can be extracted and manipulated to alter an LMM’s performance on relational tasks. First, using synthetic and real image datasets, we apply causal mediation analysis to identify attention heads that strongly influence relational predictions, and extract multimodal function vectors that improve zero-shot accuracy at inference time. We further demonstrate that these multimodal function vectors can be fine-tuned with a modest amount of training data, while keeping LMM parameters frozen, to significantly outperform in-context learning baselines. Finally, we show that relation-specific function vectors can be linearly combined to solve analogy problems involving novel and untrained visual relations, highlighting the strong generalization ability of this approach. Through experiments on two LMMs, including OpenFlamingo and Qwen3-VL, our results show that these models encode visual relational knowledge within localized internal structures, which can be systematically extracted and optimized, thereby advancing our understanding of model modularity and enhancing control over relational reasoning in LMMs.

---

## 论文详细总结（自动生成）

# 多模态函数向量用于视觉关系：详细总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

大型多模态模型（LMMs）在少量多模态示例的上下文学习中展现了令人印象深刻的能力，然而支撑这种任务学习的内部机制仍然不透明。本文旨在揭示LMMs如何在内部表示和传递视觉关系，借鉴大型语言模型（LLMs）中“函数向量”（function vectors）的概念，首次证明LMMs中一小部分注意力头负责编码视觉关系。通过提取和操控这些注意力头的激活（即函数向量），可以改变模型在关系推理任务上的表现，从而提升对多模态模型内部模块化的理解，并增强对关系推理的可控性。

## 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：认为视觉关系知识在LMMs中由少数注意力头编码，其激活模式可被提取为多模态函数向量。这些向量可作为可干预的模块，在不改变模型参数的情况下影响模型行为。
- **关键技术细节**：
  - 首先使用**因果中介分析**（Causal Mediation Analysis）识别出对关系预测影响最显著的注意力头。
  - 提取这些头部的激活值，构成多模态函数向量。
  - 在推理时，通过注入或修改这些函数向量，可以**提升零样本关系推理准确率**。
  - 进一步地，使用少量训练数据对函数向量进行**微调**（fine-tune），同时保持LMM其他参数冻结，使模型性能显著超过上下文学习基线。
  - 最后，证明不同关系对应的函数向量可以**线性组合**，从而解决涉及未见过的、未训练过的视觉关系的类比问题，展示强泛化能力。

## 3. 实验设计：数据集、基准与对比方法

- **数据集**：
  - 合成图像数据集（synthetic image datasets）
  - 真实图像数据集（real image datasets）
  - 未明确列出具体名称，但从上下文判断可能包含视觉关系数据集（如“大于”、“小于”、“左/右”等空间关系或属性关系）。
- **基准（benchmark）**：使用关系推理任务（relational tasks）作为评估，包括零样本关系推理和类比问题。
- **对比方法**：
  - **上下文学习基线**（in-context learning baselines）：即提供少量示例让模型进行few-shot推理，作为主要对比。
  - 未提到与其他函数向量或可解释性方法比较。

## 4. 资源与算力

论文中**未明确说明**使用的GPU型号、数量、训练时长等具体硬件资源信息。仅提到在两个LMMs（OpenFlamingo和Qwen3-VL）上进行了实验。由于缺乏详细披露，无法评估其计算成本。

## 5. 实验数量与充分性

- **实验数量**：从摘要描述看，实验涵盖：
  - 因果中介分析识别注意力头（至少一组实验）；
  - 提取函数向量提升零样本准确率（可能在多个关系类型上测试）；
  - 函数向量微调与上下文学习基线的对比；
  - 线性组合函数向量解决类比问题（涉及未见关系）；
  - 在两个不同模型（OpenFlamingo和Qwen3-VL）上重复以上实验。
- **充分性与客观性**：
  - 覆盖了不同数据类型（合成+真实）、不同模型，具有一定的多样性。
  - 对比基准仅为上下文学习基线，缺少与其他注入式干预方法（如提示微调、prefix tuning）的比较，可能不够全面。
  - 未报告统计显著性检验或多次运行的方差，也未提及是否固定随机种子等，公平性需进一步确认。整体上实验设计合理但尚需更多细节支撑。

## 6. 论文的主要结论与发现

1. LMMs中确实存在少数注意力头编码视觉关系的局部内部结构。
2. 提取的多模态函数向量可以系统性优化，从而提升模型在关系任务上的表现。
3. 函数向量可被微调（保持模型冻结）并显著优于纯上下文学习。
4. 不同关系的函数向量可以线性组合，实现未见关系的推理，展示强泛化能力。
5. 这一发现推进了对多模态模型模块化的理解，并为控制关系推理提供了新工具。

## 7. 优点：方法或实验设计上的亮点

- **可解释性**：通过因果中介分析精确定位关系相关的功能结构，提供机制层面的理解。
- **轻量干预**：只操控少数注意力头的激活（函数向量），无需修改模型参数，计算高效。
- **强泛化能力**：线性组合关系向量解决类比问题是亮点，表明向量具有代数结构，可组合为新关系。
- **跨模型验证**：在两个不同的LMMs（OpenFlamingo和Qwen3-VL）上验证，增加结论稳健性。
- **实用性**：函数向量微调仅需少量数据，实用性强。

## 8. 不足与局限

- **实验覆盖有限**：仅使用了合成和真实图像数据集，但未给出具体数据集名称、规模、关系类型数量，难以判断泛化范围。类比问题也仅限于可视关系，未扩展至文本-图像混合任务。
- **对比基准单一**：仅对比上下文学习基线，未与其他主流干预方法（如adapter、LoRA、prefix tuning）或可解释性方法比较。
- **计算资源不明确**：未披露训练/推理所需硬件资源，可复现性受影响。
- **偏差风险**：因果中介分析依赖于特定模型架构（如注意头），结论可能不适用于其他架构（如Vision Transformer + MLP decoder等）。关系类型也可能存在偏见。
- **应用限制**：需要事先通过因果分析定位功能头，操作依赖模型内部结构；对于完全黑箱模型无法直接应用。此外，仅验证了两种模型，通用性待进一步证明。

（完）
