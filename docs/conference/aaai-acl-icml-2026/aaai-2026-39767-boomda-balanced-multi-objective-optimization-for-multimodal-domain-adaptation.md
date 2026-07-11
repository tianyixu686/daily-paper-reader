---
title: "Boomda: Balanced Multi-objective Optimization for Multimodal Domain Adaptation"
title_zh: Boomda：面向多模态域适应的平衡多目标优化
authors: "Jun Sun, Xinxin Zhang, Simin Hong, Jian Zhu, Xiang Gao"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/39767/43728"
tags: ["query:post-multi"]
score: 7.0
evidence: 多模态域适应的平衡多目标优化
tldr: 多模态域适应面临不同模态域偏移不一致的挑战。Boomda首先用信息瓶颈为各模态独立学习表示，然后通过相关对齐匹配源域和目标域，并采用平衡多目标优化协调各模态的贡献。实验证明在跨模态域适应任务中优于现有方法。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: 异质多模态域适应中不同模态的域偏移差异大，现有方法难以平衡。
method: 信息瓶颈提取各模态独立表示，再通过相关对齐和平衡多目标优化匹配域。
result: 在多个多模态域适应基准上取得最优性能。
conclusion: 平衡多模态贡献是域适应成功的关键。
---

## Abstract
Multimodal learning, while contributing to numerous success stories across various fields, faces the challenge of prohibitively expensive manual annotation. To address the scarcity of annotated data, a popular solution is unsupervised domain adaptation, which has been extensively studied in unimodal settings yet remains less explored in multimodal settings. In this paper, we investigate heterogeneous multimodal domain adaptation, where the primary challenge is the varying domain shifts of different modalities from the source to the target domain. We first introduce the information bottleneck method to learn representations for each modality independently, and then match the source and target domains in the representation space with correlation alignment. To balance the domain alignment of all modalities, we formulate the problem as a multi-objective task, aiming for a Pareto optimal solution. By exploiting the properties specific to our model, the problem can be simplified to a quadratic programming problem. Further approximation yields a closed-form solution, leading to an efficient modality-balanced multimodal domain adaptation algorithm. The proposed method features Balanced multi-objective optimization for multimodal
domain adaptation, termed Boomda. Extensive empirical results showcase the effectiveness of the proposed approach and demonstrate that Boomda outperforms the competing schemes.

---

## 论文详细总结（自动生成）

# 论文详细总结：Boomda: Balanced Multi-objective Optimization for Multimodal Domain Adaptation

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：异质多模态域适应（heterogeneous multimodal domain adaptation）中，不同模态从源域到目标域的分布偏移程度各异，直接应用单模态域适应方法会导致模态对齐不平衡——强模态主导训练，弱模态学习不足。
- **研究动机**：多模态学习在情感识别、行动识别等任务中性能优异，但人工标注昂贵。无监督域适应（UDA）可缓解标注短缺，但现有研究多聚焦单模态，多模态域适应（尤其是异质场景）探索不足。
- **整体含义**：本文旨在实现**模态平衡**的多模态域适应，使所有模态均能充分对齐，从而充分利用多模态互补信息。

## 2. 论文提出的方法论：核心思想、关键技术细节
### 核心思想
- 结合**信息瓶颈（IB）**、**相关对齐（CORAL）** 和**多目标优化（Pareto最优）**，为每个模态学习独立表示，并平衡各模态的域对齐损失。

### 关键技术细节
1. **模型框架**：
   - 各模态使用预训练骨干（如WavLM、APViT、Bert-base）并微调顶层，后接序列编码器得到表示 \( Z_m \in \mathbb{R}^d \)。
   - 多模态表示 \( Z_{M+1} \) 为各模态表示的拼接。
   - 每个模态（含多模态）都有一个分类器。
2. **信息瓶颈（IB）损失**：
   - 最小化 \( \beta I(X_m, Z_m) - I(Z_m, Y_m) \)。
   - 假设 \( Z_m \) 服从高斯分布，推导出具体形式（式5）：\( L_{IB} = \sum_m \left[ \frac{\beta}{2} \log |\Sigma_m^s| - \frac{1}{N^s} \sum_n \log p(y_n^s|z_n^m) \right] \)。
3. **伪标签（Pseudo Labeling）**：
   - 利用所有模态预测进行投票，仅选择置信度高的样本（得票数 ≥ \( M_v \)）生成伪标签，用于目标域监督（式6-9）。
4. **相关对齐（CORAL）损失**：
   - 对每个模态 \( m \)，计算源域和目标域表示的相关矩阵 \( C_m^s, C_m^t \)，最小化 \( L_m^{CA} = \|C_m^t - C_m^s\|_F^2 \)（式10）。
5. **平衡多目标优化**：
   - 定义向量 \( L^{CA}(\theta) = [L_1^{CA}, ..., L_{M+1}^{CA}]^T \)，目标为找到 Pareto 最优解。
   - 采用多梯度下降算法（MGDA），求解 \( \min_\gamma \|\sum_m \gamma_m \nabla_{Z_{M+1}} L_m^{CA}\|_2^2 \)（问题P2/P3）。
   - 利用模型特殊性质（梯度矩阵近似对角占优），进一步近似为对角二次规划问题（P4），得到闭式解：\( \gamma = \frac{\tilde{Q}^{-1} \mathbf{1}}{\mathbf{1}^T \tilde{Q}^{-1} \mathbf{1}} \)（式13）。
   - 最终总体损失：\( L = L_{IB} + \alpha_1 L_{PL} + \alpha_2 \sum_m \gamma_m L_m^{CA} \)（式14）。
6. **算法流程**（Algorithm 1）：
   - 初始化模型参数 → 每个迭代：生成伪标签 → 计算梯度矩阵Q → 求解权重γ → 计算总损失 → 用Adam更新参数。

## 3. 实验设计
- **数据集与场景**：多模态情感识别任务，使用 **IEMOCAP** 和 **MSP-IMPROV** 两个基准数据集，含声学、视觉、词汇三种模态。
  - 目标域人为注入噪声/扰动：声学加白噪声（SNR=1.0）、视觉降低亮度至20%并加高斯噪声（SNR=0.5）、词汇随机掩盖40%单词。
- **Benchmark**：将源域随机分成两半，一半直接用作源域，另一半经上述变换作为目标域。
- **对比方法**：DANN、CDAN、MADA、DALN、PCL、DADA（均为域适应经典或前沿方法）。
- **评估指标**：加权F1分数，取三次运行平均。
- **消融实验**：分析平衡相关对齐（CA）和伪标签（PL）各自贡献，以及有无平衡策略的对比。
- **训练动态分析**：展示矩阵Q的对角占优特性（比值r）、权重γ变化、伪标签准确度变化（图3）。

## 4. 资源与算力
- **明确提及**：使用4块Nvidia A40 GPU，每块48GB内存。训练超参数：Adam优化器，学习率1e-3，批大小48。
- **未明确**：具体训练时长（如迭代次数K=300，但未给出总时间）。

## 5. 实验数量与充分性
- **数量**：主表（表1）包含两个数据集×4种模态组合（A、V、L、AVL）及平均，共8组×对比方法数量（7种）≈56个F1分数；消融表（表2）5种设置；另有三张动态图。
- **充分性**：实验覆盖多模态组合，对比方法多样，消融设计合理，验证了核心组件贡献和平衡策略的有效性。
- **客观性与公平性**：使用了统一的数据分割和评测流程，超参数固定。但未提供统计显著性检验（如t-test），且仅在情感识别任务上验证，泛化性需谨慎。

## 6. 论文的主要结论与发现
- **性能优势**：Boomda在IEMOCAP上平均F1达48.73%，在MSP-IMPROV上达41.50%，优于所有对比方法（至少提升1.78和1.43个百分点）。
- **模态平衡的重要性**：未平衡时（如DALN）引入更多模态反而性能下降；平衡后Boomda随模态增加性能提升。
- **核心组件有效**：IB表示学习、伪标签、平衡多目标优化均贡献显著（消融表明CA和PL联合使用比单独使用提升约3.6）。
- **近似合理性**：矩阵Q的对角占优特性（r小）支持了闭式解近似。

## 7. 优点
- **方法创新性**：将多模态域适应显式建模为多目标优化问题，并利用问题特殊结构推导高效闭式解，避免每步求解二次规划。
- **平衡机制有效**：动态调整各模态对齐权重，防止强模态主导，提升弱模态利用率。
- **架构简洁**：基于IB和CORAL，易于实现和扩展；伪标签投票策略提高目标域监督质量。
- **实验充分**：两个数据集、多种模态组合、丰富对比方法、消融和动态分析，验证了方法稳健性。

## 8. 不足与局限
- **实验覆盖有限**：仅针对情感识别任务（IEMOCAP、MSP-IMPROV），未在更多任务（如动作识别、医学分析）上验证泛化性。
- **人为构造域偏移**：目标域扰动是人工添加的，可能无法完全模拟真实复杂域偏移，存在偏差风险。
- **超参数敏感性**：β、α1、α2、Mv等需手动调整，未进行系统敏感性分析。
- **计算资源消耗**：每迭代需计算梯度矩阵Q及求解权重，虽用闭式近似但仍有额外开销；未与现有方法对比训练时间。
- **未讨论多模态缺失场景**：本文假设所有模态数据完整，未考虑实际中部分模态缺失的情况。
- **统计显著性缺失**：未提供标准差或置信区间，结果可靠性需更多复现。

（完）
