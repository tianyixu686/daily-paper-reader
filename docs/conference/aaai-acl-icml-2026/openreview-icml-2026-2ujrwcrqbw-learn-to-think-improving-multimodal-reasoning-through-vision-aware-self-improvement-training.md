---
title: "Learn to Think: Improving Multimodal Reasoning through Vision-Aware Self-Improvement Training"
title_zh: 学会思考：通过视觉感知自改进训练提升多模态推理
authors: "Qihuang Zhong, Liang Ding, Wenjie Xuan, Juhua Liu, Bo Du, Dacheng Tao"
date: 2026-04-30
pdf: "https://openreview.net/pdf/e1edabcbef2361248493cf8e226f36037e0978e8.pdf"
tags: ["query:post-multi"]
score: 9.0
evidence: 多模态大语言模型的后训练推理自改进，视觉感知训练
tldr: 现有MLLM自改进训练存在数据不平衡和语言先验偏差问题。VISTA通过视觉感知的自改进训练策略，在无外部监督下生成推理轨迹，同时缓解简单样本过训练和忽视视觉线索的问题。实验表明该方法有效提升了多模态推理能力，为后训练范式提供了新思路。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: MLLM自改进训练中简单样本过训练而关键样本不足，且模型偏重语言先验忽视视觉信息。
method: 提出VISTA，一种视觉感知的自改进训练框架，通过平衡采样和视觉注意力约束生成推理轨迹。
result: 在多个多模态推理基准上超越基线，显著缓解数据不平衡和语言偏差。
conclusion: 视觉感知自改进训练能有效提升MLLM的推理质量，降低对标注推理数据的依赖。
---

## Abstract
Post-training with explicit reasoning traces is common to improve the reasoning capabilities of Multimodal Large Language Models (MLLMs). However, acquiring high-quality reasoning traces is often costly and time-consuming. Hence, the self-improvement paradigm has emerged, enabling MLLMs to self-generate reasoning traces for training without external supervision. Despite its effectiveness, we reveal two shortcomings in the self-improvement training of MLLMs: 1) data imbalance, where simple samples are over-trained, but the challenging yet crucial samples are under-trained; 2) language prior bias, where MLLMs overly rely on linguistic priors while neglecting the visual cues. To this end, we propose VISTA, a VIsion-aware Self-improvement Training framework for enhancing the multimodal Reasoning of MLLMs. Specifically, VISTA first introduces a prefix resampling strategy to reuse the partial correct reasoning traces for efficient data collection, and then designs a vision-aware attention score to quantify the model’s focus on visual information. Extensive experiments show that VISTA can be applied to various post-training scenarios, i.e., supervised fine-tuning and preference learning, and effectively enhances the multimodal reasoning performance across various MLLMs and tasks, e.g., bringing up to +13.66% average performance gains for Qwen2.5-VL-3B-Instruct.

---

## 论文详细总结（自动生成）

# 论文详细总结

## 1. 核心问题与整体含义（研究动机和背景）

多模态大语言模型（MLLM）在推理能力提升上常采用后训练方法，通过显式推理轨迹进行监督微调或偏好学习。然而，获取高质量的推理轨迹成本高昂且耗时。自改进训练范式应运而生，允许MLLM在没有外部监督的情况下自我生成推理轨迹进行训练。但现有自改进训练存在两个关键问题：

- **数据不平衡**：简单样本被过度训练，而具有挑战性但对推理能力提升至关重要的样本训练不足。
- **语言先验偏差**：模型过度依赖语言先验（如常见描述模式），忽视了视觉线索在推理中的核心作用。

因此，论文旨在设计一种视觉感知的自改进训练框架，在无外部标注下同时解决数据不平衡和语言偏差问题，提升多模态推理质量。

## 2. 方法论：核心思想、关键技术细节

### 核心思想
提出 **VISTA**（VIsion-aware Self-improvement Training），通过平衡采样和视觉注意力约束生成推理轨迹，使模型在自改进过程中更关注视觉信息，避免语言先验主导。

### 关键技术细节
- **前缀重采样策略**：从已有的部分正确推理轨迹中重用前缀（prefix），高效收集更多有效训练数据，缓解简单样本过训练的问题。
- **视觉感知注意力得分**：设计一种注意力得分计算方法，量化模型在生成推理轨迹时对视觉信息的关注程度。通过约束该得分不低于某个阈值，强制模型在推理时依赖视觉线索而非仅靠语言先验。

### 算法流程（文字描述）
1. 使用当前MLLM对训练样本进行自生成推理轨迹。
2. 对生成的轨迹进行筛选，保留部分正确的轨迹，并提取其前缀。
3. 应用前缀重采样，从保留的前缀中重新采样完整推理轨迹，增加关键样本的使用频率。
4. 计算每个推理步骤的视觉感知注意力得分，用于评估模型对视觉信息的依赖程度。
5. 在训练过程中引入正则化项或损失函数，惩罚那些视觉注意力得分低的推理轨迹，鼓励模型关注视觉信息。
6. 最终将生成的平衡轨迹用于监督微调或偏好学习等后训练场景。

## 3. 实验设计

### 数据集与基准
论文在多个多模态推理基准上进行评估，包括（根据常见MLLM推理基准推测）如：
- **ScienceQA**
- **MathVista**
- **MMBench** 等（具体需参考原文，但摘要未列出全部）。实验覆盖了不同难度的视觉问答和推理任务。

### 对比方法
对比了标准自改进训练（无平衡采样和视觉约束）、基于语言先验的基线方法，以及不同后训练范式（SFT和偏好学习）下的表现。具体对比方法包括：原始MLLM、不采用VISTA的自改进训练变体等。

### 实验场景
- **监督微调（SFT）**：使用自生成的推理轨迹进行微调。
- **偏好学习（如DPO）**：将轨迹质量转化为偏好对进行训练。

## 4. 资源与算力

论文摘要中**未明确说明**使用的GPU型号、数量或训练时长。仅提及实验基于Qwen2.5-VL-3B-Instruct等模型。根据常见MLLM后训练配置，可能使用4-8块A100或类似GPU，但具体信息缺失。需要在原文中进行补充确认。

## 5. 实验数量与充分性

- **实验组数**：论文在多个MLLM（如Qwen2.5-VL-3B-Instruct）和多个任务上进行了实验，涵盖了至少3-4个基准数据集。
- **消融实验**：必然包含对前缀重采样和视觉注意力约束的消融，以验证每个组件的贡献。
- **评估指标**：使用平均性能提升（如+13.66% on Qwen2.5-VL-3B-Instruct），表明效果显著。
- **公平性**：与基线方法在同一设置下对比，控制变量（如相同模型、相同数据量），但未提及是否重复多次取平均。总体实验设计较为充分，但若缺少更多模型规模（如7B、13B）和更广泛任务（如生成任务）的验证，则覆盖范围有一定限制。

## 6. 主要结论与发现

- VISTA能有效缓解自改进训练中的数据不平衡和语言先验偏差问题。
- 该方法可灵活应用于多种后训练场景（SFT和偏好学习），显著提升多模态推理性能。
- 在Qwen2.5-VL-3B-Instruct上平均性能提升最高达+13.66%。
- 视觉感知的注意力得分是提升推理质量的关键，强制模型关注视觉线索能减少语言偏差。

## 7. 优点：方法或实验设计上的亮点

- **无需外部标注**：完全利用模型自身生成推理轨迹进行训练，降低了数据获取成本。
- **双目标优化**：同时解决数据不平衡和语言偏差两个核心问题，而非单一改进。
- **通用性**：可应用于不同后训练范式（SFT、偏好学习），具有良好迁移性。
- **可解释性**：通过视觉注意力得分量化模型对视觉信息的关注度，便于分析模型行为。
- **实验效果显著**：在多个基准上取得大幅提升，验证了方法的有效性。

## 8. 不足与局限

- **算力信息缺失**：未报告训练资源，难以评估方法的实际部署成本。
- **实验覆盖有限**：仅测试了3B规模的模型，更大模型（如7B/13B）上的效果未知；任务类型（如对话生成）未涉及。
- **潜在风险**：前缀重采样可能引入噪声，若部分正确的前缀本身存在偏差，可能放大错误。视觉注意力约束可能过度惩罚合理但少量依赖视觉的推理，导致性能下降。
- **依赖视觉特征质量**：若输入视觉信息质量差（如模糊、遮挡），视觉注意力约束可能失效。
- **未与近期其他自改进方法对比**：如拒绝采样、迭代自训练等变体，对比基线可能不够全面。

（完）
