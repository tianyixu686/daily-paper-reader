---
title: Reinforcement Fine-Tuning Naturally Mitigates Forgetting in Continual Post-Training
title_zh: 强化微调在持续后训练中自然缓解遗忘
authors: "Song Lai, Haohan Zhao, Rong Feng, Changyi Ma, Wenzhuo Liu, Hongbo Zhao, Xi Lin, Dong Yi, Qingfu Zhang, Hongbin Liu, Gaofeng Meng, Fei Zhu"
date: 2026-04-30
pdf: "https://openreview.net/pdf/6c4b92466c2b046fdf36d0e8cafa951c44496790.pdf"
tags: ["query:post-multi"]
score: 9.0
evidence: 对比监督微调与强化微调在持续后训练中的遗忘缓解效果
tldr: 在持续后训练场景下，针对多模态大语言模型的遗忘问题，本文对比了监督微调与强化微调两种范式。实验表明，基于Qwen2.5-VL模型，强化微调能自然缓解遗忘，为后训练方法选择提供重要指导。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 持续后训练中不同学习范式对知识保留的影响尚未明确。
method: 在多模态持续后训练设置下，对比监督微调和强化微调两种范式。
result: 强化微调比监督微调更有效地缓解了知识遗忘。
conclusion: 学习范式选择对持续后训练至关重要，强化微调具有优势。
---

## Abstract
Continual post-training (CPT) is a popular and effective technique for adapting foundation models like multimodal large language models to ever-evolving downstream tasks. While existing research primarily focuses on methods like data replay, model expansion, or parameter regularization, the fundamental role of the learning paradigm remains largely unexplored. This paper presents a comparative analysis of two core post-training paradigms: supervised fine-tuning (SFT) and reinforcement fine-tuning (RFT), investigating their respective impacts on knowledge retention during CPT. Our experiments are conducted across multiple multimodal tasks, utilizing Qwen2.5-VL-7B-Instruct as the base model. The investigation yields two significant findings: (1) When continuously learning on downstream tasks, SFT leads to catastrophic forgetting of previously learned tasks. In contrast, RFT inherently preserves prior knowledge and achieves performance comparable to multi-task training. (2) RFT successfully protects and even enhances the model's general knowledge on standard benchmarks, while SFT degrades general model capabilities severely. Further analysis reveals that this stability is not primarily due to explicit mechanisms like KL penalty or chain-of-thought reasoning. We investigate RFT's learning dynamics and find that its selective update mechanism inherently prevents interference with established knowledge. Based on this insight, we propose a rollout-based instance filtering algorithm (RIF-RFT) that enhances the training efficiency of RFT by focusing on learnable samples. Our comprehensive study demonstrates the superiority of RFT as a robust paradigm for continual post-training.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **研究动机**：持续后训练（Continual Post-Training, CPT）是使多模态大语言模型适应不断演化的下游任务的有效技术。现有研究主要关注数据回放、模型扩展或参数正则化等方法，但学习范式本身对知识保留的根本作用尚未被充分探索。
- **整体含义**：本文旨在系统比较两种核心后训练范式——监督微调（Supervised Fine-Tuning, SFT）和强化微调（Reinforcement Fine-Tuning, RFT）——对持续后训练中知识遗忘的影响，为后训练方法选择提供重要指导。

## 2. 方法论：核心思想与关键技术细节

- **核心思想**：通过对比实验揭示RFT相比于SFT能自然缓解遗忘，原因在于RFT的选择性更新机制天然避免了与已有知识的干扰。
- **关键技术细节**：
  - 基础模型：Qwen2.5-VL-7B-Instruct。
  - 持续学习设置：在多个多模态下游任务上顺序训练。
  - **RIF-RFT算法**（Rollout-based Instance Filtering）：基于对RFT学习动态的分析，提出通过rollout筛选可学习样本，提升RFT训练效率。
  - **无显式机制依赖**：分析表明RFT的稳定性并非主要源于KL惩罚或链式思维推理等显式机制，而是其学习动态本身。
- **未提供完整公式或伪代码**但描述了算法思路：使用强化学习范式（类似PPO/GRPO等），在持续训练中自动选择需要更新的样本，减少对旧知识的覆盖。

## 3. 实验设计

- **数据集与场景**：多模态任务，具体数据集未在摘要中列出（仅称“multiple multimodal tasks”），同时使用标准基准（standard benchmarks）评估通用能力。
- **基准模型**：Qwen2.5-VL-7B-Instruct。
- **对比方法**：
  - SFT（监督微调）
  - RFT（强化微调）
  - 多任务训练（multitask training，作为上界参考）
  - 未提及与数据回放、正则化等经典持续学习方法对比（因重点在学习范式层面）。
- **评价指标**：持续学习后知识的保留程度（遗忘程度）、通用模型能力变化。

## 4. 资源与算力

- **未明确说明**：文中未提及GPU型号、数量、训练时长等算力信息。可能需等待全文补充。

## 5. 实验数量与充分性

- **实验数量**：从摘要看，主要实验包括：
  - 持续学习场景下SFT与RFT的遗忘对比（多个多模态任务）。
  - 通用基准（standard benchmarks）上模型能力变化。
  - RIF-RFT效率提升验证（隐含消融）。
  - 额外分析：KL惩罚、思维链等机制是否主要原因。
- **充分性评价**：揭示了两范式的根本差异，比较充分；但缺少与经典持续学习方法（如数据回放、EWC）的对比，限制了结论的普适性。未提供统计显著性检验或误差条信息。

## 6. 主要结论与发现

- **发现1**：在持续学习下游任务时，SFT导致对先前学过的任务灾难性遗忘；相反，RFT天然保留先前知识，性能接近多任务训练。
- **发现2**：RFT成功保护甚至提升了模型在标准基准上的通用能力，而SFT严重降低了通用模型能力。
- **机制分析**：RFT的稳定性主要源于其选择性更新机制，而非显式的KL惩罚或思维链推理。
- **效率提升**：提出的RIF-RFT算法通过关注可学习样本进一步提升RFT训练效率。

## 7. 优点

- **范式洞察新颖**：首次系统对比SFT与RFT在持续后训练中的遗忘问题，发现RFT的自然缓解优势，具有重要实际指导意义。
- **机制剖析深入**：排除了常见显式机制（KL、CoT）的影响，定位到选择性更新这一内生特性，提供了理论理解。
- **效率优化贡献**：基于动态分析提出RIF-RFT，既保持抗遗忘优势又提升训练效率，具有良好的实用价值。
- **实验设计清晰**：直接对比两种核心范式，并加入多任务训练上界和通用基准评估，结论可信。

## 8. 不足与局限

- **数据集细节缺失**：未明确列出具体任务和数据集，读者无法直接复现或判断任务多样性。
- **对比方法有限**：未与数据回放、正则化、模型扩展等经典持续学习方法比较，无法说明RFT是否超越这些专门抗遗忘方法。
- **计算资源不明**：未提及训练成本（GPU型号、时间），不利于评估实验门槛和可复现性。
- **偏差风险**：仅使用单一基础模型（Qwen2.5-VL-7B），结论是否泛化到其他架构（如LLaVA、InternVL）未知。
- **应用限制**：RFT依赖奖励模型设计，实际部署时奖励函数的构建可能复杂，且强化学习训练不稳定风险未讨论。
- **统计充分性**：未报告多次运行的标准差，结论稳健性需进一步验证。

---

（完）
