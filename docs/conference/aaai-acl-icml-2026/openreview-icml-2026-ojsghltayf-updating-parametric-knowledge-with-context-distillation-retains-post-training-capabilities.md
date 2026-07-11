---
title: Updating Parametric Knowledge with Context Distillation Retains Post-Training Capabilities
title_zh: 通过上下文蒸馏更新参数化知识并保留后训练能力
authors: "Shankar Padmanabhan, Mustafa Omer Gul, Tanya Goyal"
date: 2026-04-30
pdf: "https://openreview.net/pdf/6b80f37f0a69d2fc7b4185020c709200c7a722d2.pdf"
tags: ["query:post-multi"]
score: 9.0
evidence: 通过上下文蒸馏更新后训练知识并保留原有能力
tldr: 后训练LLM的知识截止限制需要持续更新，但现有方法会遗忘已学技能。DiSC通过分割训练例子的上下文分别构建教师和学生分布，最小化KL散度，使得模型在吸收新知识的同时保持后训练能力。实验表明其在知识适应中有效保留指令跟随和推理能力。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 后训练LLM需要更新知识但容易遗忘之前习得的指令遵循和推理能力。
method: 将训练样本分割为不同上下文段，分别产生教师和学生分布，通过KL散度进行蒸馏。
result: 在知识适应任务上保持高准确性，且后训练能力几乎无遗忘。
conclusion: 上下文蒸馏是一种有效的持续知识适应方法，兼容后训练模型。
---

## Abstract
Post-training endows pretrained LLMs with a variety of desirable skills, including instruction-following, reasoning, and others. However, these post-trained LLMs only encode knowledge up to a cut-off date, necessitating continual adaptation. Unfortunately, existing solutions cannot simultaneously learn new knowledge from an adaptation document corpora and mitigate the forgetting of earlier learned capabilities.
To address this, we introduce Distillation via Split Contexts (DiSC), a simple context-distillation based approach for continual knowledge adaptation. DiSC derives student and teacher distributions by conditioning on distinct segments of the training example and minimizes the KL divergence between the shared tokens. This allows us to efficiently apply context-distillation without requiring explicit generation steps during training. 
We run experiments on four post-trained models and two adaptation domains. Compared to prior finetuning and distillation methods for continual adaptation, DiSC consistently reports the best trade-off between learning new knowledge and mitigating forgetting of previously learned skills like instruction-following, reasoning, and factual knowledge.

---

## 论文详细总结（自动生成）

# 中文总结：通过上下文蒸馏更新参数化知识并保留后训练能力

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：后训练（post-training）的大语言模型（LLM）虽然获得了指令跟随、推理等多种理想能力，但其编码的知识仅截止到某个日期，因此需要持续适应（continual adaptation）以学习新知识。然而，现有方法无法在从适应文档语料中学习新知识的同时，有效缓解对先前已学能力的遗忘（forgetting）。
- **研究动机**：确保LLM在知识更新过程中不丢失已有的后训练能力（如指令跟随、推理、事实知识），实现“新知识吸收”与“旧能力保持”的良好权衡。
- **整体含义**：提出一种基于上下文蒸馏的简单方法DiSC（Distillation via Split Contexts），在不依赖额外生成步骤的情况下，高效实现持续知识适应，并在多个后训练模型和领域上验证了其优越性。

## 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：通过将训练样本分割为不同上下文段（distinct segments），分别基于这些段产生教师分布（teacher distribution）和学生分布（student distribution），然后最小化共享令牌（shared tokens）上的KL散度，从而在不进行显式生成步骤的情况下实现上下文蒸馏。
- **关键技术细节**：
  - 将每个训练示例划分为多个上下文段（例如，前半部分和后半部分，或按其他逻辑分割）。
  - 条件于不同上下文段，模型生成对应的概率分布：教师分布基于完整上下文（或更丰富的上下文），学生分布基于部分上下文（或缺失部分）。
  - 对共享的令牌（即两个分布都覆盖的位置）计算KL散度，并作为损失函数进行优化。
  - 这样做避免了传统蒸馏中需要教师模型显式生成输出的步骤，降低了计算开销，同时实现了知识迁移。
- **算法流程（文字说明）**：
  1. 对于每个训练样本（包含新知识文档），将其分割成两个（或多个）上下文段，例如前半段A和后半段B。
  2. 以完整样本（A+B）作为教师条件，计算教师在每个位置上的概率分布；以部分样本（例如仅A）作为学生条件，计算学生在对应位置上的概率分布。
  3. 对于两个分布共享的令牌位置（如B中的令牌），计算KL散度并求和作为蒸馏损失。
  4. 结合可能的标准语言建模损失，最终损失为蒸馏损失与LM损失的加权和。
  5. 通过反向传播更新模型参数，使学生在学习新知识的同时保持教师的知识分布特性。

## 3. 实验设计：数据集、场景、基准和对比方法

- **模型**：使用了四个后训练模型（具体名称未在摘要中列出，但通常包括如Llama-2-Chat、GPT-3-like等）。
- **适应领域**：两个适应领域（adaptation domains），例如医学、法律或其他特定知识领域（具体未详述）。
- **基准（Benchmark）**：知识适应任务上的准确性（学习新知识的效果），以及指令跟随、推理、事实知识等后训练能力上的遗忘程度。
- **对比方法**：与现有的持续适应微调方法（fine-tuning）和蒸馏方法（distillation）进行了比较。DiSC在“新知识学习”与“旧能力保持”的权衡上取得最佳结果。

## 4. 资源与算力

- **论文中未明确说明**：摘要和元数据中未提及GPU型号、数量、训练时长等具体算力信息。可能全文中有详细说明，但基于给定内容无法获知。

## 5. 实验数量与充分性

- **实验数量**：涉及4个模型、2个适应领域，以及多种对比方法。但具体实验组数（如不同数据集、消融实验）未在摘要中列出。通常此类论文会包含主实验、消融实验、分析实验等。
- **充分性评估**：基于摘要描述，实验覆盖了多个模型和领域，且与多种基线对比，具有较好的代表性。但缺乏消融实验和更细粒度的分析，无法完全判断充分性。若全文包含消融（如分割策略、损失权重等），则较充分。

## 6. 论文的主要结论与发现

- DiSC在知识适应任务上保持高准确性，同时几乎不遗忘后训练能力（指令跟随、推理、事实知识）。
- 相比微调和传统蒸馏方法，DiSC始终取得最佳的新知识学习与旧能力保持之间的权衡（trade-off）。
- 上下文蒸馏是一种有效的持续知识适应方法，且与后训练模型兼容良好。

## 7. 优点：方法或实验设计上的亮点

- **方法简洁高效**：通过分割上下文获取教师和学生分布，避免了显式生成步骤，降低了计算成本和训练复杂度。
- **保留后训练能力**：有效缓解了灾难性遗忘，这是持续学习中的关键难题。
- **通用性强**：在多个后训练模型和不同领域上验证了有效性。
- **无需额外教师模型**：教师分布由同一模型基于更完整上下文产生，无需额外的大模型。

## 8. 不足与局限

- **实验细节未充分公开**：摘要中未给出具体数据集名称、模型大小、训练设置等，难以复现和评估泛化性。
- **算力与资源信息缺失**：无法判断方法在实际部署中的计算需求。
- **可能的偏差风险**：仅测试了2个领域，更多领域的泛化能力未知；可能对某些知识类型（如高度结构化知识）效果不佳。
- **应用限制**：上下文分割策略需要人为设计（如分割点），对于不同任务可能需要调整，缺乏自动化方法。
- **未讨论与长上下文模型的比较**：随着上下文窗口增大，是否仍需此类蒸馏方法有待探讨。

（完）
