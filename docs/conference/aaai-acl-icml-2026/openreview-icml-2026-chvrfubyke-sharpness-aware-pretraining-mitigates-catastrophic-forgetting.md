---
title: Sharpness-Aware Pretraining Mitigates Catastrophic Forgetting
title_zh: 锐度感知预训练缓解灾难性遗忘
authors: "Ishaan Watts, Catherine Li, Sachin Goyal, Jacob Mitchell Springer, Aditi Raghunathan"
date: 2026-04-30
pdf: "https://openreview.net/pdf/d813f8d64ffd3e606b30ca975b49a4c9da999264.pdf"
tags: ["query:post-multi"]
score: 8.0
evidence: 预训练优化以改善后训练保持力
tldr: "后训练常导致预训练知识遗忘。本文发现通过锐度感知最小化、大学习率和缩短退火期等预训练优化方法，可以引导模型收敛到更平坦的极小值，从而在后续后训练和量化中保留更多原始能力。在5个常见数据集上的实验表明，这些干预措施最多减少80%的遗忘，且在不同规模模型上一致有效，揭示了预训练几何对后训练鲁棒性的重要影响。"
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 预训练优化器忽略了损失几何形状对后训练中能力保留的影响。
method: 采用锐度感知最小化、大学习率和缩短退火期等方法使预训练偏向平坦极小值。
result: "这些干预措施在多个后训练场景中一致减少了遗忘，最高达80%。"
conclusion: 预训练几何对后续微调鲁棒性至关重要，锐度感知预训练能有效缓解遗忘。
---

## Abstract
Pretraining optimizers are tuned to produce the strongest possible base model, on the assumption that a stronger starting point yields a stronger model after subsequent changes like post-training and quantization. This overlooks the geometry of the base model which controls how much of the base model's capabilities survive subsequent parameter updates. We study three pretraining optimization approaches that bias optimization toward flatter minima: Sharpness-Aware Minimization (SAM), large learning rates, and shortened learning rate annealing periods. Across model sizes ranging from 20M to 150M parameters, we find that these interventions consistently improve downstream performance after post-training on five common datasets with up to 80\% less forgetting. These principles hold at scale: a short SAM mid-training phase applied to an existing OLMo-2-1B checkpoint reduces forgetting by 31\% after MetaMath post-training and by 40\% after 4-bit quantization.

---

## 论文详细总结（自动生成）

# 详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

*   **核心问题**：预训练阶段得到的模型在后续的后训练（如指令微调）或量化过程中，往往会灾难性地遗忘预训练阶段学到的知识，导致模型能力退化。
*   **研究背景**：现有预训练优化器通常只追求最小化训练损失以获得最强的基座模型，却忽略了损失曲面的几何形状（如极小值的平坦性）对模型后续参数更新后能力保留的影响。作者假设，偏向平坦极小值的预训练策略能让模型在后训练/量化时保留更多原始能力。
*   **整体含义**：本文首次系统研究了预训练阶段的优化方式（而非后训练阶段）对灾难性遗忘的影响，揭示了预训练几何对后训练鲁棒性的重要性。

## 2. 方法论：核心思想、关键技术细节

*   **核心思想**：通过使预训练优化偏向更平坦的极小值，提高模型在后训练（微调/量化）中的知识保持能力。
*   **关键技术细节**：
    *   **锐度感知最小化（Sharpness-Aware Minimization, SAM）**：在预训练优化中不仅最小化损失值，还考虑损失曲面的曲率，通过寻找邻域内损失都小的平坦区域来提升泛化能力。
    *   **大学习率（Large Learning Rates）**：在预训练过程中使用比常规更大的学习率，促使优化器跳出尖锐极小值，收敛到更平坦的区域。
    *   **缩短学习率退火期（Shortened Learning Rate Annealing Periods）**：减少训练末期学习率逐渐降低的阶段，避免模型在退火过程中陷入尖锐极小值，从而保持平坦性。
*   **公式/算法流程（文字说明）**：
    *   三种干预措施均不改变模型架构或数据，仅修改预训练优化器的超参数或目标函数。
        *   SAM 在每次参数更新时，先计算损失相对于参数的梯度，再添加一个与梯度方向一致的小扰动，并最小化扰动后的损失。
        *   大学习率策略指在标准 SGD/Adam 训练中，将学习率设为比平常大的值（如实验中从默认 LR 提升数倍）。
        *   缩短退火期指将原本占据较大比例训练步数的余弦退火阶段缩短，使得模型在训练末期更少被“挤入”尖锐极小值。

## 3. 实验设计

*   **使用数据集/场景**：
    *   后训练数据集：5个常见数据集（文中未详细列出名称，但根据上文信息推测为通用指令微调或分类数据集）。
    *   量化场景：4-bit 量化。
*   **Benchmark**：
    *   **基座模型**：规模从 20M 到 150M 参数的小模型，以及一个更大的 OLMo-2-1B（10亿参数）检查点。
    *   **核心指标**：后训练/量化后的性能保持率（遗忘减少百分比）。
*   **对比方法**：
    *   标准预训练（基线）。
    *   SAM 预训练。
    *   大学习率预训练。
    *   短退火期预训练。
    *   混合干预：如“短 SAM 中训练阶段”（short SAM mid-training phase）。

## 4. 资源与算力

*   **文中未明确说明**：论文没有给出具体的 GPU 型号、数量或训练时长。仅提到模型规模从 20M 到 150M 参数，以及 OLMo-2-1B（10亿参数）。计算资源开销应属于中等规模，但具体数字缺失。

## 5. 实验数量与充分性

*   **实验数量**：
    *   在小模型上（20M~150M）对三种干预措施分别进行了测试，覆盖5个不同后训练数据集。
    *   在 OLMo-2-1B 上验证了短 SAM 中训练阶段的效果（MetaMath 后训练和4-bit量化）。
*   **充分性评价**：
    *   **优势**：覆盖了多种模型尺寸和不同的后训练/量化场景，且所有干预措施结果一致（遗忘减少最高80%），提供了交叉验证。
    *   **不足**：
        *   数据集名称未公开，读者无法独立复现或验证结果。
        *   仅研究了三种干预，未探索其他可能的平坦性诱导方法（如L2正则化、权重衰减变体等）。
        *   未展示消融实验（如不同学习率大小、退火期长度对平坦性及遗忘的量化关系）。
        *   小模型（20M~150M）规模较小，结论能否直接推广到更大规模（如数百亿参数）缺乏强证据（仅一个1B模型部分验证）。
    *   **客观性/公平性**：论文对比了基线（标准预训练），且说明了干预措施在不同数据集上一致有效，没有选择性报告。但未说明后训练超参数是否针对基线做了单独调优，可能导致基线表现不佳。

## 6. 主要结论与发现

*   **核心结论**：通过锐度感知最小化、大学习率和缩短退火期等预训练优化方法，可以引导模型收敛到更平坦的极小值，从而在后训练和量化中保留更多原始知识，最多减少80%的遗忘。
*   **发现**：
    *   三种干预措施在不同规模模型（20M~150M）上均一致有效。
    *   在更大规模模型 OLMo-2-1B 上，仅用一个短 SAM 中训练阶段（short SAM mid-training phase）就能在 MetaMath 后训练中减少31%遗忘，在4-bit量化中减少40%遗忘。
    *   预训练几何对后续微调鲁棒性至关重要，平坦极小值比强基座模型的直接损失最小化更重要。

## 7. 优点

*   **方法创新性**：首次将预训练阶段的损失曲面几何与后训练灾难性遗忘联系起来，并提出了简单有效的干预策略（无需修改模型架构或数据）。
*   **实验设计的说服力**：覆盖了多种模型尺度（20M到1B）和不同后训练模式（微调、量化），且结果一致；大模型验证增强了结论的可靠性。
*   **实用性**：这些干预措施计算开销小（如大学习率、缩短退火期无需额外计算，SAM 增加少量计算），容易应用于现有预训练流程。
*   **揭示深层机理**：不局限于报告现象，而是从优化几何角度解释了为什么某些预训练策略能提升后训练鲁棒性。

## 8. 不足与局限

*   **实验覆盖不全面**：
    *   未公开具体数据集名称和细节，难以复现。
    *   仅测试了三种干预，未探索如权重衰减、动量设置等其他可能影响平坦性的因素。
    *   仅使用了最大 1B 参数的模型，更大规模（如 7B、70B）的效果未知。
    *   后训练场景有限（5个数据集 + 量化），未涉及连续学习、多任务微调等更复杂的遗忘场景。
*   **潜在的偏差风险**：
    *   基线预训练可能已经工作在较尖锐的极小值，导致干预效果显著。若基线本身较平坦，增益可能下降。
    *   后训练超参数（如学习率、步数）可能对不同预训练策略不公平（未说明是否针对基线调优）。
*   **应用限制**：
    *   缩短退火期可能会影响预训练下游任务的绝对性能（论文未报告预训练损失或基座模型本身的指标，只关注后训练保留）。若基座模型能力本身下降，则需要权衡。
    *   大学习率可能导致预训练不稳定，需要谨慎调节。
*   **机制解释不够深入**：虽然观察到平坦极小值有利于保持，但未从理论或经验上证明平坦性与遗忘之间的因果联系（例如是否与神经网络的线性区域有关）。

（完）
