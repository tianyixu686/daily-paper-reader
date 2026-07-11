---
title: Towards Multimodal Continual Knowledge Embedding with Modality Forgetting Modulation
title_zh: 面向多模态持续知识嵌入的模态遗忘调制
authors: "Xiaowen Jiang, Jing Yang, ShunDong Yang, Yuan Gao, Xinfa Jiang, Laurence Tianruo Yang, Jieming Yang"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/38516/42478"
tags: ["query:post-multi"]
score: 7.0
evidence: 多模态知识图谱的持续学习
tldr: 针对多模态知识图谱动态演化中静态嵌入模型导致知识遗忘的问题，提出MoFot框架，通过模态遗忘调制策略有效缓解灾难性遗忘，在持续学习场景下保持多模态知识一致性，实验证明其在多模态知识嵌入任务上的有效性。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: 多模态知识图谱持续增长，现有方法重新训练浪费知识或微调导致遗忘。
method: 提出MoFot框架，利用模态遗忘调制抑制灾难性遗忘。
result: 在动态MMKG上持续学习性能优于基线。
conclusion: 模态遗忘调制是实现多模态知识持续嵌入的关键。
---

## Abstract
The continuous emergence of new entities, relations, triples, and multimodal information drives the dynamic evolution of multimodal knowledge graph (MMKG). However, existing MMKG embedding models follow a static setting, where training from scratch for growing MMKG wastes learned knowledge, while fine-tuning on new knowledge easily leads to catastrophic forgetting, severely limiting their applicability in real-world scenarios. To address this, we propose a multimodal continual representation learning framework (MoFot) for growing MMKG. Unlike existing static multimodal embedding methods, MoFot focuses on alleviating catastrophic forgetting rather than retraining to adapt to new knowledge. Specifically, MoFot effectively mitigates catastrophic forgetting caused by parameter updates and differing forgetting rates across modalities through a multimodal collaborative modulation mechanism. The mechanism ensures consistent retention of  previously learned multimodal knowledge across snapshots through multimodal weight modulation and multimodal feature modulation. MoFot outperforms existing MMKG embedding, KG continual learning, and MMKG inductive models.  Experimental results demonstrate that MoFot not only avoids forgetting but also enhances old knowledge by learning new knowledge, achieving adaptation to new knowledge while mitigating forgetting of old knowledge.

---

## 论文详细总结（自动生成）

# 1. 核心问题与整体含义（研究动机和背景）

- 多模态知识图谱（MMKG）在现实场景中不断演化增长，持续新增实体、关系、三元组及多模态信息。
- 现有 MMKG 嵌入方法均为静态设计，从头训练会浪费已学知识，而微调新知识则容易引发灾难性遗忘，严重限制实际应用。
- 不同模态的特征在持续学习中遗忘速率不一致，进一步加剧了性能退化。
- 因此，本文旨在设计一个能够适应不断增长的 MMKG、同时有效缓解灾难性遗忘的持续学习框架。

# 2. 方法论

### 核心思想
提出 **MoFot**（Multimodal Continual Representation Learning Framework with Modality Forgetting Modulation），通过**多模态协同调制机制**同时从权重和特征两个层面抑制遗忘，实现跨快照的多模态知识一致保留。

### 关键技术细节
- **关系驱动的路径传播（Relation-Driven Path Passing）**  
  基于 NBFNet，利用关系聚合建模实体对之间的路径语义，为每个查询三元组生成包含完整路径语义的实体表示。
- **历史路径保存（Historical Path Preservation）**  
  对查询关系特有的权重矩阵施加正则化约束（式4），防止旧路径语义被覆盖；同时通过拼接和线性变换构建查询相关的路径更新函数（式2）。
- **路径引导的多模态特征调制（Path-Guided Multimodal Features Modulation）**  
  将保留旧结构知识的路径语义作为引导，通过注意力机制融合视觉、文本和结构特征，确保各模态表示跨快照保持一致（式5-7）。
- **权重插值更新（Weight Interpolation Update）**  
  对每个模态的独立权重进行方向调整与幅度缩放，通过加权插值融合新旧权重（式9-10），统一调控各模态的更新幅度，缓解因参数更新和遗忘速率差异带来的问题。
- 训练损失包括正负样本对比损失加上两项正则化项（历史路径保存 + 共享权重正则）。

# 3. 实验设计

### 数据集与场景
- 在 **5 个 MMKG 连续学习数据集**上评测：M-ENTITY、M-RELATION、M-FACT、M-HYBRID、M-GraphEqual。
- 每个数据集包含 5 个快照（时间步），增长策略分别为实体、关系、三元组或混合驱动。
- 文本和视觉特征分别使用 BERT 和 VGG16 提取。

### Benchmark 与对比方法
- **单模态持续学习模型**：PNN、EWC、SI、LKGE、IncDE。
- **静态 MMKG 模型（微调）**：IMF、MoCi。
- **归纳式多模态模型**：IndMKG。
- **多模态持续学习变体**：LKGE-M、IncDE-M（在原有单模态模型基础上添加多模态融合）。

### 指标
- 链接预测：MRR、Hits@1、Hits@3、Hits@10。
- 知识保留与迁移：BWT（反向迁移）、FWT（正向迁移）。

# 4. 资源与算力

论文中**未明确说明**所使用的 GPU 型号、数量及具体训练时长。仅在实验部分提供了时间效率对比图（图7），显示 MoFot 的训练时间远低于 MoCi/IMF 的重新训练或微调方案，但未给出硬件环境细节。

# 5. 实验数量与充分性

- **主实验**：在全部 5 个数据集上报告平均 MRR/Hits@K，并与多种基线全面对比。
- **单快照性能展示**：呈现了每个快照上的 MRR 热力图（图4），体现持续学习下的动态表现。
- **知识保留与迁移分析**：报告了 BWT/FWT 分数（表2）。
- **消融实验**：
  - **模态消融**：移除文本/视觉模态，验证多模态贡献（图6）。
  - **模块消融**：分别移除历史路径保存、路径引导特征调制、权重插值更新三个模块，分析对性能与 BWT 的影响（表3、表4）。
- **时间效率对比**：图7展示了训练时间累积。
- **整体评价**：实验设计较为充分，覆盖了多个数据集、多种增长策略、多种基线方法，且通过消融验证了各模块有效性，结果客观公平。但未包含跨数据集迁移测试或更大规模真实场景验证。

# 6. 主要结论与发现

- MoFot 在所有数据集上显著优于现有 MMKG 持续学习/静态/归纳方法。
- MoFot 不仅有效避免了灾难性遗忘，还能通过**学习新知识增强旧知识**，在多个数据集上实现**正向 BWT**（即旧快照性能提升）。
- 模态遗忘调制（权重+特征）是解决多模态持续学习中遗忘速率不一致问题的关键。
- 在效率上，MoFot 比重新训练和微调方案更省时。

# 7. 优点

- **创新性**：首次提出面向增长 MMKG 的多模态持续表示学习框架，填补了该领域空白。
- **机制设计巧妙**：双分支调制（权重调制 + 特征调制）协同解决参数更新和模态遗忘速率差异带来的问题。
- **正向知识迁移**：模型不仅能保留旧知识，还能利用新知识提升旧快照性能（正 BWT），这在持续学习中非常难得。
- **实验全面**：覆盖多种增长策略、多种基线、多种指标，消融实验验证充分。

# 8. 不足与局限

- **算力资源未公开**：缺少 GPU 型号、数量、训练时长等具体信息，不利于复现和公平比较。
- **任务覆盖有限**：仅针对链接预测任务，未验证在其他下游任务（如问答、推荐）上的有效性。
- **增长假设简化**：假设快照顺序严格、数据按序到达，未讨论非顺序或跳跃式增长场景。
- **泛化性未考察**：未进行跨数据集或跨领域的迁移实验，实际应用中的泛化能力有待验证。
- **方法复杂度**：尽管效率优于重训练，但引入多个新增模块（路径保存、注意力融合、权重插值）可能增加实现和调参难度。
- **缺乏更大规模真实场景验证**：实验数据集规模相对较小，在工业级大规模 MMKG 上的表现未知。

（完）
