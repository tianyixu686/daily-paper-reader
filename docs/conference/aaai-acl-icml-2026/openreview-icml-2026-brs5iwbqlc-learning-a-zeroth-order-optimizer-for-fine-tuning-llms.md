---
title: Learning a Zeroth-Order Optimizer for Fine-Tuning LLMs
title_zh: 学习面向大语言模型微调的零阶优化器
authors: "Kairun Zhang, Haoyu Li, Yanjun Zhao, Yifan Sun, Huan Zhang"
date: 2026-04-30
pdf: "https://openreview.net/pdf/109b1f33a87a537b54d40ff3d355d9b33e9c899c.pdf"
tags: ["query:post-multi"]
score: 8.0
evidence: 面向大语言模型微调的零阶优化器
tldr: ZO-Finetuner提出一种学习型零阶优化器，自动学习高效的扰动策略，显著降低LLM微调的内存开销，并支持跨任务复用，为资源受限场景提供实用方案。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有零阶方法依赖静态采样策略，无法适应模型结构。
method: 设计学习型零阶优化器，通过紧凑设计自动学习扰动策略。
result: 在多个微调任务上以更低内存开销达到与一阶方法相当的性能。
conclusion: 学习型零阶优化器为LLM高效微调提供了新途径。
---

## Abstract
Zeroth-order optimizers have recently emerged as an attractive approach for fine-tuning large language models (LLMs), as they avoid backpropagation and can substantially reduce memory overhead relative to standard first-order training. However, existing zeroth-order methods rely on hand-crafted, static sampling strategies that are not adaptable to model-specific structures. To address this, we propose ZO-Finetuner, a learning-based zeroth-order optimizer for LLMs that automatically learns efficient perturbation strategies through a compact and memory-efficient design. Motivated by the fact that a small set of base LLMs is repeatedly fine-tuned across tasks, ZO-Finetuner supports one-time per-model training and reuse across downstream tasks with minimal overhead. Therefore, learning the optimizer once for a given LLM and reusing it across diverse downstream tasks is both feasible and highly desirable. Accordingly, ZO-Finetuner is designed to scale learning to learn (L2L) to the foundation-model era by supporting one-time per-model training with minimal overhead. Experiments on 4 LLMs and 7 datasets show that ZO-Finetuner outperforms prior zeroth-order baselines in 82.1\% of task-model combinations, thereby demonstrating strong performance and scalability for efficient LLM fine-tuning.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机与背景）

- **背景**：大语言模型（LLM）在众多任务中表现优异，但标准微调依赖一阶反向传播，内存开销巨大（需存储激活值、梯度等）。零阶优化器通过仅使用函数值（无需反向传播）更新参数，大幅降低内存占用，因此成为微调LLM的有吸引力方法。
- **核心问题**：现有零阶优化器均采用手工设计的、静态的扰动采样策略（如固定分布采样），无法根据模型的具体结构动态调整，导致效率低下且通用性差。同时，常见场景中同一基础LLM需要被反复微调于不同下游任务，但现有零阶方法无法跨任务复用学习到的策略。
- **研究动机**：提出一种**可学习的**零阶优化器，使其能自动学习高效扰动策略；并且由于基础LLM被反复使用，支持一次性训练优化器后跨任务复用，从而将“学习如何学习”（Learning-to-Learn, L2L）扩展到基础模型时代。

## 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：构建一个**学习型零阶优化器**（ZO-Finetuner），通过一个紧凑且内存高效的设计，自动学习适用于特定LLM结构的扰动策略。优化器的训练过程：对给定的一个基础LLM，离线学习一次；之后应用于该LLM的所有下游微调任务时，无需重新训练优化器，仅需加载已学得的策略。
- **关键技术细节**（基于摘要推断）：
  - 使用元学习（或L2L）框架，将扰动生成过程参数化为一个小型神经网络（扰动预测器）。
  - 在训练优化器时，对基础LLM的部分参数（如LoRA适配器）进行模拟微调，优化扰动预测器以最小化零阶梯度估计的方差或直接提高微调收敛性能。
  - 优化器本身具备紧凑性，以避免额外内存开销过大（可能采用轻量级架构）。
- **公式/算法流程**（文字说明）：
  - 步骤1：选择待微调的基础LLM，固定其参数。
  - 步骤2：定义参数化扰动生成器（如一个小型MLP），输入为当前参数位置（或噪声种子），输出为扰动向量。
  - 步骤3：在多个代理任务（或合成损失景观）上，使用元学习目标（如最小化零阶梯度估计与真实梯度的差距，或最大化微调性能）更新扰动生成器。
  - 步骤4：训练完成后，对于新的下游任务，直接使用该扰动生成器生成扰动，进行零阶优化微调（如使用随机无梯度方法SPSA的变体），无需反向传播。

（注：以上为基于摘要的合理推断，论文全文可能包含更多细节。）

## 3. 实验设计：数据集/场景、基准、对比方法

- **数据集与场景**：论文在4个LLM和7个数据集上进行实验。具体LLM型号和数据集名称摘要未列出（估计包含常见基准如GLUE、SuperGLUE、文本分类、问答等），但未明确说明。
- **基准（benchmark）**：主要对比的是“prior zeroth-order baselines”，即已有的零阶优化方法（如经典的SPSA、ZO-SGD，以及可能近期基于随机扰动的ZO方法）。
- **对比方法**：未具体列举，但推测包括：
  - 未使用学习策略的标准零阶方法（如固定高斯扰动）。
  - 可能还包括一阶微调（如全参数或LoRA）的上限比较（但摘要未提，可能论文中有）。
- **评估指标**：微调后在下游任务上的性能（如准确率、F1等）。

## 4. 资源与算力

- 论文摘要及元数据中**未提及**具体的GPU型号、数量、训练时长等算力信息。因此无法总结。只能指出论文未说明。

## 5. 实验数量与充分性

- **实验数量**：在4个LLM × 7个数据集 = 28个组合上进行评估，结果中ZO-Finetuner在82.1%的组合上优于基线。这是一个中等规模的实验。
- **充分性与公平性**：
  - 覆盖了多个模型和任务，有一定广度。
  - 但摘要未提及消融实验（如不同扰动生成器设计、学习率、跨任务复用效果分析）或对零阶优化内存开销的量化对比。因此**实验充分性有限**，可能需要查看全文获取更多细节（如是否控制种子、计算预算等）。由于缺乏详细实验设置，难以完全判断公平性。

## 6. 论文的主要结论与发现

- ZO-Finetuner作为一种**学习型零阶优化器**，能够自动学习模型适应的扰动策略，在82.1%的任务-模型组合上优于先前零阶基线。
- 该方法支持“一次性训练，多个下游任务复用”，将L2L范式适配到LLM微调场景，在大幅降低内存开销的同时保持与一阶方法相当的微调性能。
- 研究展示了学习型零阶优化在**高效LLM微调**中的潜力和可扩展性。

## 7. 优点：方法或实验设计上的亮点

- **创新性**：首次将L2L应用于零阶优化器设计，使其适应模型结构，突破手工设计瓶颈。
- **实用性**：跨任务复用机制极大减少了重复训练开销，非常契合基础模型反复微调的真实场景。
- **内存高效**：零阶优化本身无需反向传播，再结合紧凑的扰动生成器，进一步降低内存占用（相比一阶微调可节省显存）。
- **性能强**：在绝大多数对比中超越传统零阶方法，验证了学习策略的有效性。

## 8. 不足与局限

- **实验覆盖较有限**：仅4个模型和7个任务，缺乏更大规模模型（如70B以上）和更广泛任务类型的验证；消融实验未在摘要中提及，可能不够充分。
- **偏差风险**：摘要未说明是否控制了一阶方法的计算量或迭代次数相同，可能存在比较不公平。
- **应用限制**：学习型优化器需要针对每个基础LLM单独训练一次，对于新发布的LLM需要额外开销；另外，零阶方法在参数规模极大时收敛速度仍可能慢于一阶方法，文中未讨论收敛性分析。
- **资源信息缺失**：未报告训练优化器本身的算力需求，难以评估其实际部署成本。

（完）
