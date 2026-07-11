---
title: "Video-OPD: Efficient Post-Training of Multimodal Large Language Models for Temporal Video Grounding via On-Policy Distillation"
title_zh: Video-OPD：基于在线策略蒸馏的多模态大语言模型后训练高效视频时间定位
authors: "Jiaze Li, Hao Yin, Haoran Xu, Boshen Xu, Wenhui Tan, Zewen He, Jianzhong Ju, Zhenbo Luo, Jian Luan"
date: 2026-04-30
pdf: "https://openreview.net/pdf/efe888ac68003d9ee30bb96c5115c20688ac9cf5.pdf"
tags: ["query:post-multi"]
score: 9.0
evidence: 多模态大语言模型的后训练用于视频时间定位
tldr: 针对多模态大语言模型在视频时间定位任务中后训练效率低且奖励稀疏的问题，提出Video-OPD框架，利用在线策略蒸馏从前沿教师模型获取密集监督，保持训练与推理分布一致，显著提升定位精度并降低计算成本。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有GRPO后训练方法在视频定位中奖励稀疏且计算开销大。
method: 提出在线策略蒸馏框架，用前沿教师提供密集token级监督。
result: 在多个视频定位基准上达到最优精度，且训练更高效。
conclusion: 在线策略蒸馏有效提升了多模态后训练的效率与效果。
---

## Abstract
Reinforcement learning has emerged as a principled post-training paradigm for Temporal Video Grounding (TVG) due to its on-policy optimization, yet existing GRPO-based methods remain fundamentally constrained by sparse reward signals and substantial computational overhead. We propose Video-OPD, an efficient post-training framework for TVG inspired by recent advances in on-policy distillation. Video-OPD optimizes trajectories sampled directly from the current policy, thereby preserving alignment between training and inference distributions, while a frontier teacher supplies dense, token-level supervision via a reverse KL divergence objective. This formulation preserves the on-policy property critical for mitigating distributional shift, while converting sparse, episode-level feedback into fine-grained, step-wise learning signals. Building on Video-OPD, we introduce Teacher-Validated Disagreement Focusing (TVDF), a lightweight training curriculum that iteratively prioritizes trajectories that are both teacher-reliable and maximally informative for the student, thereby improving training efficiency. Empirical results demonstrate that Video-OPD consistently outperforms GRPO while achieving substantially faster convergence and lower computational cost, establishing on-policy distillation as an effective alternative to conventional reinforcement learning for TVG.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究背景**：时序视频定位（Temporal Video Grounding, TVG）要求多模态大语言模型（MLLM）根据自然语言查询定位视频中的相关片段。强化学习（RL）因其在线策略（on-policy）优化特性，成为 TVG 后训练的有效范式。
- **核心问题**：现有基于 GRPO（Group Relative Policy Optimization）的方法面临两大瓶颈：
  - **奖励稀疏**：任务级（episode-level）反馈无法提供细粒度指导，导致学习信号不足；
  - **计算开销大**：GRPO 需要采样大量轨迹进行组间比较，训练效率低下。
- **整体含义**：本文旨在设计一种高效、轻量的后训练框架，通过在线策略蒸馏（on-policy distillation）将稀疏奖励转化为密集的 token 级监督，在保持训练与推理分布一致的同时显著降低计算成本。

### 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程

- **核心思想**：用前沿教师模型（frontier teacher）提供密集的 token 级监督，通过反向 KL 散度（reverse KL divergence）蒸馏给学生模型，从而保留在线策略（on-policy）特性，避免分布偏移。
- **关键技术细节**：
  - **Video-OPD 框架**：直接从当前策略（学生）采样的轨迹进行优化，确保训练和推理的分布一致；教师模型（通常为更大或预训练的先进模型）对每条轨迹的每个 token 输出软标签，作为密集监督。
  - **损失函数**：采用反向 KL 散度 \( D_{KL}(p_{\text{student}} \parallel p_{\text{teacher}}) \)，使学生的输出分布向教师对齐。
  - **TVDF（Teacher-Validated Disagreement Focusing）**：一种轻量训练课程，迭代筛选出同时满足“教师可靠”和“对学生最具信息量”的轨迹，优先训练这些高价值样本，从而提升训练效率。
- **算法流程**（文字描述）：
  1. 学生策略在环境中采样一批轨迹（视频-查询对生成时间戳）。
  2. 对每条轨迹，教师模型输出 token 级的概率分布作为监督信号。
  3. 计算学生分布与教师分布的反向 KL 散度损失，并反向传播更新学生。
  4. 利用 TVDF 评估每条轨迹的教师置信度和学生不确定性，对轨迹排序并优先训练高价值样本。
  5. 重复上述步骤直到收敛。

### 3. 实验设计：使用的数据集、基准、对比方法

- **数据集 / 场景**：论文未在摘要中明确列出具体数据集，但元数据提到“在多个视频定位基准上达到最优精度”。通常 TVG 常用数据集包括 ActivityNet Captions, Charades-STA, TACoS 等。
- **Benchmark**：时序视频定位的标准评测指标（如 R@1, IoU=0.5/0.7 等）。
- **对比方法**：主要与 GRPO（基于组相对策略优化的基线）比较，同时隐含与直接微调、其他 RL 方法（如 PPO）对比。但本文未列出具体基线名称。

### 4. 资源与算力

- **未明确说明**：论文摘要及元数据中未提及使用的 GPU 型号、数量、训练时长等信息。仅在元数据中提及“计算开销低”作为结论，但无具体数值。需获取全文才能获知。

### 5. 实验数量与充分性

- **实验数量**：由于只有摘要，无法获知具体实验数量。但根据元数据“在多个视频定位基准上达到最优精度”以及通常论文标配（主实验、消融、可视化等），推测至少包含 3-5 个数据集上的主实验，以及消融 TVDF、教师规模、损失函数选择等。
- **充分性与公平性**：仅从摘要看，实验设计偏向于展示 Video-OPD 相对于 GRPO 的优势，但未说明是否严格控制其他变量（如教师模型大小、采样数量等）。需要全文验证对比是否公平（如 GRPO 是否最优调参）。总体而言，摘要中的声明需要更多细节支持。

### 6. 论文的主要结论与发现

- Video-OPD 在多个 TVG 基准上一致优于 GRPO 方法。
- 收敛速度显著更快，计算成本更低。
- 在线策略蒸馏可以作为传统强化学习（RL）在 TVG 后训练中的有效替代方案。
- TVDF 课程进一步提升了训练效率和最终精度。

### 7. 优点：方法或实验设计上的亮点

- **方法创新**：将在线策略蒸馏引入 TVG 后训练，巧妙地将稀疏奖励转化为密集 token 级监督，缓解了 RL 的优化困难。
- **效率导向**：TVDF 优先训练高信息量样本，避免无效计算，轻量且实用。
- **理论优势**：保持 on-policy 特性，避免分布偏移，这是很多蒸馏方法（如 offline distillation）难以做到的。
- **实验结论清晰**：直接对比 GRPO，展示了速度与精度的双重提升，说服力强。

### 8. 不足与局限

- **公开信息不足**：摘要未给出具体数据集、基线、实验设置等，无法全面评估实验充分性。
- **依赖性**：依赖一个强教师模型，若教师不可用或领域不匹配，方法可能失效。
- **适用范围**：目前仅在 TVG 任务上验证，是否适用于其他多模态定位任务（如 grounded QA、视频指代）尚不明确。
- **潜在偏差风险**：若教师本身在特定场景上存在偏见，蒸馏可能放大这些偏见。

（完）
