---
title: Hyper-Opinion Vagueness Quantification for Robust Multimodal Learning
title_zh: 超意见模糊性量化实现鲁棒多模态学习
authors: "Disen Hu, Xun Jiang, Xiaofeng Cao, Zheng Wang, Jingkuan Song, Heng Tao Shen, Xing Xu"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/39335/43296"
tags: ["query:post-multi"]
score: 7.0
evidence: 通过模糊性量化实现鲁棒多模态学习
tldr: 鲁棒多模态学习常忽视模型对依赖相同模态线索类别的模糊性。本文定义并量化这种模糊性（vagueness），通过超意见融合与调整机制减少类间歧义，提升特征提取的独特性。在多种扰动下模型鲁棒性显著提高。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: 现有鲁棒多模态学习难以区分共享相同模态特征的类别，导致模糊预测。
method: 提出模糊性量化方法，结合超意见机制调整融合权重，增强类别独特语义。
result: 在多个鲁棒性基准上超越现有方法，尤其对语义扰动更鲁棒。
conclusion: 量化模糊性并有效融合能显著提升多模态模型的鲁棒性。
---

## Abstract
Robust Multimodal Learning (RML) aims to address the issues of unreliable predictions of multimodal models.
Nevertheless, previous RML works often struggle to distinguish between different categories that rely on identical intra-modal cues, making ambiguous predictions.
We defined this degree of ``uncertain'' in extracting discriminative features of a multimodal model as vagueness.
Neglecting such vagueness, as previous RML works commonly do, will undermine the ability to extract unique semantics of each category in multimodal models, further resulting in worse robustness under disturbances that affect semantic representations.
Additionally, this vagueness will lead the parameter updating processes towards unreliable fusion, thus diverting the learning processes of the multimodal model from learning unique features of each category.
Based on the above insight, we propose a novel robust multimodal learning approach, termed Hyper-Opinion Quantifying Vagueness (HOQV).
Specifically, we first introduce hyper-opinion to capture and quantify the vagueness of multimodal learning in discriminating representations of different categories.
Moreover, to mitigate the interference in parameter updating of unreliable representations with high vagueness, we also design the Hyper-Opinion Gradient Modulation to guide the optimization processes. 
We evaluate our HOQV on six datasets with different disturbances, including noise and adversarial attack, and demonstrate that our proposed method achieves state-of-the-art performance consistently.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：现有鲁棒多模态学习（Robust Multimodal Learning, RML）方法无法有效区分那些**依赖相同模态内共同线索的不同类别**，导致模型产生模糊、不可靠的预测。作者将这种“不确定”程度定义为**模糊性**（vagueness）。
- **研究动机**：传统RML方法（如基于高斯投影或证据深度学习的不确定性量化）只关注单一类别的不确定性，忽略了**类别间语义过度耦合**带来的模糊性。这种模糊性在遇到扰动（噪声、对抗攻击）时会被放大，导致模型无法提取每个类别的独特语义，鲁棒性显著下降。此外，模糊性还会在反向传播中误导参数更新方向，使模型远离最优解。
- **整体含义**：要提升多模态模型的鲁棒性，必须**显式捕捉并量化模糊性**，并将其融入前向推理和反向优化中。

## 2. 论文提出的方法论

### 核心思想
基于**超意见（Hyper-Opinion）** 框架，在证据深度学习（Evidential Deep Learning）中引入**复合类别**（composite sets）来建模模糊性，并通过**分组狄利克雷分布（Grouped Dirichlet Distribution, GDD）** 量化模糊性。同时设计**超意见梯度调制（Hyper-Opinion Gradient Modulation, HOGM）** 根据不确定性动态调整更新步长。

### 关键技术细节
1. **复合类别构建**：
   - 计算每个类别的特征中心（centroid）\(h_k^v\)，通过余弦相似度判断哪些类别语义耦合度高，若相似度超过阈值\(\gamma\)，则将这些类别组合成一个复合集（composite set）。
2. **模糊性量化**：
   - 对每个模态（如视频和音频）分别提取证据向量\(e^v\)（包含单例证据和复合证据）。
   - 使用GDD建模超意见分布，其概率密度函数为：
     \[
     \text{GDD}^v(p|\alpha^v, c^v) = Z^{-1}\left(\prod_{k=1}^K p_k^{\alpha_k^v -1}\right)\left(\prod_{j=1}^\sigma \left(\sum_{l\in V_j} p_l\right)^{c_{V_j}^v}\right)
     \]
     其中\(\alpha^v\)为单例浓度参数，\(c^v\)为复合浓度参数。
   - 模糊性\(V^v = \sum_{j=1}^\sigma b_{V_j}^v\)，即复合集上的信念质量之和。
3. **模糊性校准**：
   - 将复合信念投影到对应单例上，修正单例的信念质量：\(b_k^v \leftarrow b_k^v + V_k^v\)。
4. **融合方法**：
   - 采用Dempster组合规则融合各模态的狄利克雷分布，得到联合意见和联合分布。
5. **梯度调制（HOGM）**：
   - 计算每个模态的GDD熵作为不确定性\(U^v\)，调制梯度权重\(\kappa^v = \omega^v \cdot \exp(-U^v)\)。
   - 更新规则：\(\theta_u^{t+1} = \theta_u^t - \eta \cdot \kappa^u g(\theta_u^t)\)，在模糊性高的迭代步减小梯度步长，避免被不可靠表示误导。
6. **损失函数**：
   - 单模态GDD损失：\(L_{\text{GDD}}^v = L_{\text{PCE}}^v - \lambda L_{\text{KL}}^v\)。
   - 联合分类损失：\(L_f = \mathbb{E}[-\log p(\tilde{y}|p_f)] - \lambda_j \text{KL}(D(p_f|\bar{\alpha}_f) \| D(p_f|\mathbf{1}_K))\)。
   - 总损失：\(L_{\text{total}} = L_{\text{uni}} + L_f\)。

## 3. 实验设计

### 数据集与场景
- **视觉-语言**：MVSA-Single（图像-文本情感分析）
- **RGB-D**：NYU Depth V2, SUN RGB-D（室内场景识别）
- **音-视频**：CREMA-D（情感分析）, Kinetics-Sounds, UCF101（动作识别）

### 扰动类型
- **自然噪声**：高斯噪声、椒盐噪声，噪声率\(\epsilon = 5.0, 10.0\)（50%模态被损坏）。
- **对抗攻击**：\(\ell_2\) PGD攻击、FGM攻击，攻击大小\(\epsilon = 0.5\)。

### 对比方法
- 鲁棒多模态学习：QMF (ICML'23), EAU (CVPR'24), MMPareto (ICML'24), CRMT (ICLR'24)
- 鲁棒多视角分类：ECML (AAAI'24), NLC (AAAI'25)
- 所有方法使用官方代码复现。

### 评估指标
- 准确率（Accuracy），表1和表2报告五次随机种子的平均准确率。

## 4. 资源与算力

论文中**未明确说明**使用的GPU型号、数量、训练时长等算力信息。仅提及：
- 批量大小16，训练150个epoch，学习率1e-2。
- 优化器：CREMA-D、Kinetics-Sounds、UCF101使用SGD，其余使用Adam。
- 代码已开源（GitHub），可通过环境配置推测所需算力，但原文未提供具体资源报告。

## 5. 实验数量与充分性

### 实验覆盖
- **主实验**（表1）：4个数据集 × 5种噪声条件（清洁+两种噪声×两种强度）= 20个场景，对比6种方法。
- **附加实验**（表2）：2个数据集 × 3种条件（清洁+两种攻击）= 6个场景，对比4种方法。
- **消融实验**（表3）：MVSA-Single上对HOGM、\(L_{\text{uni}}\)、\(L_f\)的3种组合进行消融。
- **泛化性验证**（图4）：将HOGM模块嵌入ECML，在2个数据集上验证有效性。
- **超参数分析**（图5）：复合数量对SUN RGB-D性能的影响。
- **训练动态分析**（图6）：不同训练集规模下模糊性与准确率的关系。
- **可视化案例**（图7）：2个数据集上的定性对比。

### 充分性与公平性
- 实验较为充分，覆盖了多种扰动类型、多种模态组合、多个数据集。
- 对比方法较新（2023-2025年），且注明使用官方开源代码复现，公平性良好。
- **不足**：仅报告平均准确率，未提供标准差或置信区间，无法评估结果的稳定性；未进行统计显著性检验（如t-test）；未在大规模预训练模型（如CLIP）上测试；复合构建阈值\(\gamma=0.5\)未做敏感性分析。

## 6. 论文的主要结论与发现

1. **模糊性是影响多模态鲁棒性的关键因素**：传统RML忽略类别间语义耦合导致的模糊性，会严重损害模型在扰动下的性能。
2. **超意见可以有效量化模糊性**：通过GDD建模复合证据和单例证据，能够捕捉模型对不同类别的模糊认知，并校准信念分布。
3. **梯度调制提升优化鲁棒性**：HOGM根据不确定性动态调整学习速率，避免模型被高模糊性样本误导，使学习轨迹更稳定。
4. **HOVQ在多种扰动下达到最佳性能**：在6个数据集上，HOVQ在清洁、噪声和对抗攻击条件下均超越现有SOTA方法，提升约2-3%，部分场景提升更高（如CREMA-D下噪声条件提升6-8%）。
5. **HOGM具有良好的泛化能力**：将其集成到其他模型（如ECML）中，同样能带来性能提升，证实了该机制的有效性。

## 7. 优点

- **理论创新**：首次将“超意见”概念引入多模态鲁棒学习，明确定义并量化了语义耦合导致的“模糊性”，弥补了传统不确定性量化只关注单类别的不足。
- **方法完整性**：同时在前向（信念校准）和反向（梯度调制）两个阶段处理模糊性，设计系统且自洽。
- **实验全面**：涵盖了自然噪声和对抗攻击两大类扰动，数据集涵盖视觉-语言、RGB-D、音视频等多种模态组合，结果具有说服力。
- **代码开源**：提供了可复现的代码，便于社区验证和后续研究。
- **通用性强**：HOGM模块可即插即用，提升其他模型的鲁棒性，显示了广泛的应用潜力。

## 8. 不足与局限

- **算力信息缺失**：未报告GPU型号、数量、训练时间等，影响实验可复现性评估。
- **统计细节不足**：仅给出平均准确率，缺乏标准差或置信区间，无法判断结果的显著性。
- **超参数敏感度未分析**：复合构建阈值\(\gamma\)固定为0.5，未讨论其对性能的影响。
- **应用场景有限**：仅在封闭类别任务上验证，未涉及开放集识别或未见类别场景；复合类别构建需要类别标签，对无监督或增量学习场景不友好。
- **模型规模受限**：未与近年大规模预训练多模态模型（如CLIP、BLIP）在类似任务上比较，实际工业级应用中的表现未知。
- **基线覆盖**：缺少与更传统的集成方法或贝叶斯方法（如MC Dropout）的对比，消融实验仅在单一数据集上进行，可能不够普适。

（完）
