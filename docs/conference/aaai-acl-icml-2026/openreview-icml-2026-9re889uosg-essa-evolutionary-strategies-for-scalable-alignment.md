---
title: "ESSA: Evolutionary Strategies for Scalable Alignment"
title_zh: "ESSA: 面向可扩展对齐的进化策略"
authors: "Daria Korotyshova, Boris Shaposhnikov, Alexey Malakhov, Alexey Khokhulin, Nikita Surnachev, Kirill Ovcharenko, George Bredis, Alexey Gorbatovski, Viacheslav Sinii, Daniil Gavrilov"
date: 2026-01-23
pdf: "https://openreview.net/pdf/fd608856c62908340975c36fded89f8ac09368db.pdf"
tags: ["query:post-multi"]
score: 9.0
evidence: 作为RLHF替代的无梯度对齐方法
tldr: ESSA提出一种基于进化策略的无梯度对齐方法，在微调后阶段仅需推理即可完成对齐，性能媲美GRPO等RLHF方法，且支持低精度推理，大幅降低分布式训练复杂度。
source: ICML-2026-Rejected-Public
selection_source: conference_retrieval
motivation: RLHF需要复杂分布式训练和调参，难以大规模应用。
method: 采用进化策略优化低秩适配器的奇异值，实现无梯度对齐。
result: 在多个基准上匹配GRPO性能，且支持INT4/INT8推理。
conclusion: 进化策略为大规模LLM对齐提供了一种简单高效的替代方案。
---

## Abstract
Alignment of Large Language Models (LLMs) typically relies on Reinforcement Learning from Human Feedback (RLHF) with gradient-based optimizers such as Proximal Policy Optimization (PPO) or Group Relative Policy Optimization (GRPO). While effective, these methods require complex distributed training and careful hyperparameter tuning, which becomes increasingly difficult at scale. We present ESSA, Evolutionary Strategies for Scalable Alignment, a gradient-free post-SFT alignment stage that replaces the online RL optimization loop with inference-only black-box optimization. ESSA optimizes only the singular values of low-rank adapters, making evolutionary search practical even for very large models and compatible with INT4/INT8 inference. Across benchmarks, ESSA matches GRPO and in our best configurations improves test accuracy by up to 21.9 percentage points (e.g., on MATH500, Qwen2.5-7B), while using only forward passes during the alignment stage. At scale, ESSA shows stronger scaling than gradient-based methods: Qwen2.5-32B trained on PRM800K reaches a fixed accuracy threshold on MATH500 2$\times$ faster on 16 GPUs and 6$\times$ faster on 128 GPUs than GRPO. These results position evolutionary strategies as a compelling, hardware-friendly alternative to gradient-based LLM alignment, combining competitive quality with substantially reduced wall-clock time and engineering overhead.

---

## 论文详细总结（自动生成）

# ESSA 论文详细总结

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：大型语言模型（LLMs）的对齐（alignment）通常依赖基于梯度的强化学习方法（如RLHF中的PPO、GRPO），这些方法需要复杂的分布式训练、细致的超参数调优，且难以扩展到更大规模模型。
- **研究背景**：现有基于梯度的对齐方法在训练过程中需要维护策略网络、价值网络等多个组件，并需要进行在线交互式采样，导致工程开销大、资源消耗高，制约了超大规模LLM的实用化。
- **整体含义**：论文提出一种**无梯度的进化策略**方法ESSA，作为监督微调（SFT）之后的对齐阶段，仅需推理（forward pass）即可完成对齐，显著降低分布式训练复杂度和硬件要求。

## 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程
- **核心思想**：使用进化策略（Evolutionary Strategies）代替基于梯度的优化器，在SFT之后的对齐阶段仅通过模型的**前向推理**（黑箱优化）来优化低秩适配器（LoRA）的参数。
- **关键技术细节**：
  - 只优化**低秩适配器的奇异值**（singular values），而非全部参数，从而大幅降低搜索空间，使进化搜索对大型模型可行。
  - 搭配**INT4/INT8低精度推理**，进一步降低计算和存储开销。
  - 无需反向传播、无需维护价值网络、无需在线采样训练。
- **算法流程（文字说明）**：
  1. 加载预训练+SFT后的基座模型，并插入LoRA适配器。
  2. 初始化一组候选适配器参数（奇异值向量）。
  3. 对每个候选参数，在验证集或训练集上通过纯前向推理计算奖励（对齐目标，如准确率、安全性分数等）。
  4. 基于进化策略（如沿梯度方向的变异和选择）更新奇异值。
  5. 重复步骤3-4直到收敛或达到预算。
  6. 最终的适配器可直接用于推理。

## 3. 实验设计：数据集、基准、对比方法
- **数据集与基准**：
  - 主要使用**MATH500**（数学推理基准）进行测试。
  - 在Qwen2.5系列模型（7B和32B）上进行实验。
  - 训练数据使用**PRM800K**（过程奖励模型数据集）。
- **对比方法**：主要与**GRPO**（Group Relative Policy Optimization，一种基于梯度的RLHF方法）对比。
- **其他评估指标**：测试准确率（accuracy）、对齐速度（到达固定精度阈值所需的训练时间）等。

## 4. 资源与算力
- **明确提及**：在Qwen2.5-32B模型上使用**16块GPU**和**128块GPU**分别进行训练。
- **训练时长**：到达MATH500固定精度阈值，ESSA在16 GPU上比GRPO快**2倍**，在128 GPU上快**6倍**。
- **GPU型号**：未明确说明具体型号，但根据上下文推测为NVIDIA高端GPU（如A100/H100）。
- **其他**：ESSA支持INT4/INT8推理，进一步降低硬件需求。

## 5. 实验数量与充分性
- **实验数量**：
  - 在两个模型规模（7B、32B）上进行对比。
  - 测试了不同配置（如低精度推理、不同GPU数量）。
  - 与GRPO进行了公正对比。
- **充分性评估**：
  - 局限性：仅展示了MATH500一个基准任务，缺少对其他类型任务（如安全性、指令遵循、多轮对话等）的评估。
  - 客观性：直接比较了训练时间和最终准确率，公平性较好，但未展示更多消融实验（如不同进化策略变体、初始化方式等）。
  - 总体：**实验数量较有限**，但核心结论清晰，足以证明ESSA在数学推理对齐上的优势。

## 6. 论文的主要结论与发现
1. **性能匹敌GRPO**：在多种配置下，ESSA的性能与GRPO相当，甚至更好（最佳配置下在MATH500上准确率提升高达21.9个百分点，针对Qwen2.5-7B）。
2. **扩展性强**：随着GPU数量增加，ESSA的训练时间缩短幅度远大于GRPO，展现出更强的可扩展性。
3. **硬件友好**：兼容低精度推理（INT4/INT8），降低了对昂贵全精度计算资源的需求。
4. **工程简化**：无需反向传播、无需复杂的强化学习训练循环，仅需前向推理，大幅降低工程开销和调参成本。

## 7. 优点
- **方法创新**：将进化策略引入LLM对齐领域，并巧妙限定于低秩适配器的奇异值，解决了进化搜索在高维参数空间中的可行性。
- **实用性强**：支持低精度推理，可在消费级GPU或边缘设备上完成对齐；训练时间大幅缩短。
- **扩展性优势**：计算资源增加时，ESSA的速度提升更显著，有利于超大模型训练。
- **实验对比公平**：直接与当前主流的GRPO方法在相同模型、相同数据集上对比。

## 8. 不足与局限
- **任务覆盖不足**：仅测试了数学推理（MATH500），未验证安全性、对话质量、指令遵循等更广泛的对齐目标。
- **消融实验缺失**：未分析不同进化策略超参数（种群大小、变异强度、选择机制）的影响；未探索不同LoRA秩的敏感性。
- **依赖预训练SFT**：ESSA仅作为后对齐阶段，未测试从头开始的完全无梯度训练是否可行。
- **潜在偏差风险**：进化策略可能在某些任务上难以收敛到全局优解，相比梯度方法泛化性需更多验证。
- **应用限制**：仅适用于可以定义明确奖励函数的场景，对需要复杂人类偏好的开放任务可能不适用。

（完）
