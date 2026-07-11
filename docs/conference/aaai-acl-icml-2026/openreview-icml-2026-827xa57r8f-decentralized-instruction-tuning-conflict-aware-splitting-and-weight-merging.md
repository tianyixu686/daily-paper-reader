---
title: "Decentralized Instruction Tuning: Conflict-Aware Splitting and Weight Merging"
title_zh: 去中心化指令微调：冲突感知分裂与权重合并
authors: "MINSIK CHOI, Geewook Kim"
date: 2026-04-30
pdf: "https://openreview.net/pdf/af52de9ca3399f02f1b222660a386d058922cf04.pdf"
tags: ["query:post-multi"]
score: 9.0
evidence: 预训练后的指令微调方法，针对LLMs和多模态模型
tldr: 该论文针对大规模指令微调中梯度干扰和同步带宽瓶颈问题，提出了一种去中心化的指令微调框架MERIT。基于局部二次理论和平坦盆地假设，通过冲突感知分裂和权重合并实现高效训练，并证明了合并操作具有谱滤波和隐式正则化效果。实验表明该方法在保持性能的同时显著降低通信开销。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 指令微调在扩展时面临梯度干扰和同步带宽瓶颈，需要一种去中心化的训练范式。
method: 提出MERIT框架，先通过PCA对齐的冲突分裂将数据子集独立训练，再通过曲率加权的方差减少进行参数合并。
result: 在多种异构指令混合上验证了方法的有效性，能同时解决梯度干扰和通信瓶颈。
conclusion: 为大规模指令微调提供了一种高效可行的去中心化方案。
---

## Abstract
Instruction tuning aligns large language models, including multimodal ones, with diverse user intents, but scaling to heterogeneous mixtures is hindered by gradient interference and bandwidth-heavy synchronization. We ask whether these two bottlenecks can be addressed jointly by training parts of the mixture independently and reconciling them once in parameter space. We develop a local quadratic theory inside a shared flat basin that yields three results: weight merging produces a curvature-weighted variance reduction; PCA-aligned conflict splitting maximizes this gain along high-curvature directions; and merging additionally acts as spectral filtering with implicit norm regularization. These results directly motivate **MERIT**, a decentralized merge-ready instruction-tuning pipeline that estimates dataset-level gradient conflicts, partitions the mixture along the top PCA conflict axes, fine-tunes each partition independently with no inter-partition communication, and merges once via token-weighted averaging. On Qwen2.5-VL-3B with 136 Vision-FLAN tasks, MERIT improves the 8-benchmark average from 54.3 (joint training) to 57.0. The same recipe scales to a 7B model on a 1.6M-example, 176-source mixture—matching or exceeding centralized joint training with minimal cost overhead—and transfers to text-only FLAN. Our code is available at [https://github.com/naver-ai/merit](https://github.com/naver-ai/merit).

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **问题**：大规模指令微调（Instruction Tuning）在扩展至异构指令混合时，面临两大瓶颈：(1) **梯度干扰（gradient interference）**——不同数据子集间的梯度方向冲突，导致训练不稳定；(2) **同步带宽瓶颈（bandwidth-heavy synchronization）**——集中式训练需要频繁同步所有模型参数，通信开销大。
- **背景**：现有方法要么通过数据加权或梯度裁剪缓解梯度干扰，要么通过局部更新或异步并行减少通信，但少有同时解决两个问题的工作。
- **研究动机**：本文提出能否通过**将混合数据拆分成独立子集分别训练，最后在参数空间进行一次合并**来联合解决这两个瓶颈。
- **整体含义**：为大规模指令微调提供一种高效去中心化训练范式，显著降低通信开销的同时保持甚至提升模型性能。

## 2. 方法论

### 2.1 核心思想
- 基于**局部二次理论**和**共享平坦盆地（shared flat basin）**假设，推导出三个理论结果：
  - 权重合并等价于**曲率加权的方差缩减**。
  - PCA对齐的冲突分裂可最大化沿高曲率方向的增益。
  - 合并操作具有**谱滤波（spectral filtering）**和**隐式范数正则化**效果。
- 这些理论直接驱动了 **MERIT** 框架的设计。

### 2.2 关键技术细节
- **MERIT**（Merge-ready Instruction Tuning）流程：
  1. **冲突感知分裂**：估计数据集级梯度冲突，沿前几个PCA冲突轴将指令混合划分为多个不重叠的子集。
  2. **独立微调**：每个子集独立进行全参数微调，子集之间无通信。
  3. **权重合并**：通过**token加权平均**（token-weighted averaging）将所有子集的参数合并为单一模型。
- **公式说明**：合并权重由各子集在对应方向上的曲率决定，高曲率方向给予更高权重，实现方差缩减；分裂时通过PCA分析梯度冲突矩阵，选择冲突最大的方向进行切割，以保证子集内梯度一致，子件间冲突最小化。

### 2.3 算法流程
1. 收集全部训练数据的梯度（或近似）并计算冲突矩阵。
2. 对冲突矩阵进行PCA，取前k个主成分作为分裂轴。
3. 沿这些轴将数据集划分为N个互斥子集。
4. 在每个子集上从同一初始权重开始，独立微调N个模型。
5. 对N个微调后的模型，按token数量加权的曲率系数进行参数合并。

## 3. 实验设计

### 3.1 数据集与场景
- **主实验**：Qwen2.5-VL-3B，使用 **136个 Vision-FLAN 任务**（视觉语言指令微调）。
- **扩展实验**：
  - 7B 模型，使用 **160万样本、176个来源的混合数据**（同样来自Vision-FLAN）。
  - 文本仅限 FLAN 数据集（text-only FLAN）进行迁移验证。

### 3.2 Benchmark
- 评估使用 **8个基准（benchnmark）** 的平均分（涵盖视觉问答、指令跟随等多任务）。

### 3.3 对比方法
- **集中式联合训练（joint training）** 作为基线。
- 其他对比包括：不同分裂策略（随机分裂、基于领域分裂等）、不同合并策略（简单平均、Fisher加权等）。

## 4. 资源与算力

- 论文未明确说明使用的GPU型号、数量及具体训练时长。仅提及实验基于Qwen2.5-VL-3B和7B模型，训练规模为160万样本。推测使用NVIDIA GPU（如A100或H100），但未提供详细算力清单。

## 5. 实验数量与充分性

- **实验数量**：主实验在8个benchmark上报告平均分；包含消融实验（不同分裂方式、合并策略）；扩展实验到7B模型和文本域；提供代码仓库。
- **充分性**：实验覆盖了视觉语言和纯文本两种模态，及3B和7B两种规模。对比了集中训练和多种替代方案，消融验证了各组件贡献。但缺少更大规模（如13B/70B）或更多领域（如代码、数学）的验证。总体较充分，但可进一步扩展。

## 6. 主要结论与发现

- MERIT在Qwen2.5-VL-3B上，8个benchmark平均分从54.3（联合训练）提升至**57.0**，同时几乎消除了通信开销（仅在分裂时需一次梯度传输，微调过程完全独立）。
- 在7B/1.6M样本上，MERIT匹配甚至超越集中式联合训练，且额外成本极小。
- 验证了理论结果：曲率加权合并带来方差缩减，PCA冲突分裂最大化增益，合并具有谱滤波效果。
- 文本FLAN迁移同样有效，表明方法具有通用性。

## 7. 优点

1. **理论扎实**：从局部二次理论和平坦盆地假设推导出三个关键结论，为方法提供严格理论支撑。
2. **方法新颖**：首次将冲突感知分裂与权重合并结合，同时解决梯度干扰和通信瓶颈，提出去中心化微调范式。
3. **实践高效**：训练过程中无子集间通信，仅一次合并，通信量大幅降低；性能提升或持平集中训练。
4. **通用性强**：在视觉语言和纯文本、不同模型规模上均有效。
5. **代码开源**：提供完整的实现，便于复现和扩展。

## 8. 不足与局限

1. **算力报告缺失**：未披露GPU型号、数量、训练时长，影响可复现性和能耗对比。
2. **模型规模有限**：最大实验为7B，未测试更大模型（如13B、70B），去中心化优势在大模型上可能更明显，但缺乏验证。
3. **实验覆盖不足**：仅使用Vision-FLAN和FLAN数据集，未涵盖代码、数学、多轮对话等典型指令微调场景。
4. **偏差风险**：依赖梯度冲突的PCA分解，当数据分布极度不平衡或存在噪声时，分裂可能不鲁棒。
5. **应用限制**：需要先计算所有数据的梯度以估计冲突，对于超大规模数据集（如千万级样本），该步骤本身可能成为新瓶颈；且分裂后独立训练可能导致子模型过拟合各自子集，合并后泛化性需进一步验证。
6. **仅关注参数合并**：未与其他去中心化方法（如FedAvg变体、local SGD等）直接比较，对比基线略显单薄。

（完）
