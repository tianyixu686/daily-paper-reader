---
title: Reconcile Gradient Modulation for Harmony Multimodal Learning
title_zh: 调和梯度调制实现和谐多模态学习
authors: "Xiyuan Gao, Bing Cao, Baoquan Gong, Pengfei Zhu"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/39267/43228"
tags: ["query:post-multi"]
score: 7.0
evidence: 梯度调控实现和谐多模态学习
tldr: RGM提出统一框架SynOrth Grad，通过自适应调整梯度幅值和方向，同时解决多模态学习中的模态不平衡和梯度冲突问题，提升融合性能。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: 多模态学习中模态不平衡与梯度冲突相互耦合，现有方法孤立处理效果有限。
method: 提出RGM框架，核心SynOrth Grad自适应调整梯度方向和幅值。
result: 在多个多模态任务上平衡了模态贡献，缓解了冲突，提升了性能。
conclusion: 联合处理模态不平衡与梯度冲突是改善多模态学习的有效途径。
---

## Abstract
Multimodal learning frequently faces two coupled challenges: modality imbalance, where dominant modalities suppress others during training, and modality conflict, where opposing gradient directions hinder optimization. Existing methods typically address these issues in isolation, yet they are intrinsically correlated and most fundamentally reflected in the gradient space—severe imbalance may obscure conflicts, while suppressing conflict may homogenize features and worsen imbalance, affecting fusion performance. To jointly address this coupled challenge, we propose Reconcile Gradient Modulation (RGM), a unified framework that adaptively adjusts gradient magnitude and direction for harmony multimodal learning. The core of RGM is SynOrth Grad, which minimizes Dirichlet energy to perform minimal-gradient surgery. It enhances cooperation synergy when modalities are aligned and enforces orthogonality to preserve uniqueness in conflict situations, thus promoting stable and balanced learning. To guide this modulation, we propose Cumulative Gradient Energy (CGE) as a convergence-guaranteed measure of modality-wise progress, and construct a Balance-nonConflict Plane (BCP) for real-time diagnosis and control of training dynamics. Experiments on diverse benchmarks validate our effectiveness and generalizability, consistently outperforming counterparts that are designed to handle multimodal imbalance or conflict independently.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

多模态学习在实际应用中常面临两个相互耦合的挑战：
- **模态不平衡（Modality Imbalance）**：训练过程中强势模态压制弱势模态，导致弱模态表征学习不足。
- **模态冲突（Modality Conflict）**：不同模态的梯度方向相反或特征不一致，阻碍优化进程。

现有方法通常孤立处理这两个问题，但二者内在关联：严重不平衡会掩盖冲突，而强制抑制冲突可能导致模态特征同质化、加剧不平衡。论文认为，这两个问题最根本地反映在梯度空间中，因此提出**统一框架RGM**，在梯度层面同时、自适应地调节幅值和方向，实现和谐多模态学习。

## 2. 方法论

### 2.1 核心思想
- 提出**Cumulative Gradient Energy (CGE)** 作为模态学习进度的度量指标，具有收敛保证。
- 构建**Balance-nonConflict Plane (BCP)** 二维平面，实时诊断训练状态：x轴为平衡因子 \(\bar{w}_{ij}\)，y轴为非冲突因子 \(c_{ij}\)。
- 提出 **SynOrth Grad** 机制，根据BCP坐标动态执行两种梯度手术：
  - **协同增强投影**：当模态梯度对齐时，最小化Dirichlet能量，按块级比例缩放使其更共线。
  - **冲突正交化投影**：当模态梯度冲突（\(c_{ij}<0\)）时，施加最小形变的正交旋转，使调整后梯度正交，保留模态特异性。
- 通过软门控（sigmoid函数，斜率受平衡因子调控）平滑切换两种操作，并配合CGE驱动的能量感知重平衡（Energy-Aware Rebalancing）动态缩放梯度幅度。

### 2.2 关键技术细节
- **CGE定义**：\(E^{(T)}_k = \sum_{t=1}^T \| \eta_t g_k^{(t)} \|^2\)，反映模态k的累积贡献，与收敛性理论上界关联。
- **平衡因子**：\(\bar{w}_{ij} = 8w_i w_j - 1\)，其中 \(w_i = E_i/(E_i+E_j)\)，范围[-1,1]。
- **非冲突因子**：\(c_{ij} = \cos(g_i, g_j)\)。
- **协同投影缩放系数**：通过最小化块级Dirichlet能量得到封闭解 \(\alpha^{(k)}_i = \sqrt{w_i \cdot \sum_{i=1}^M \|g_i^{(k)}\|^2} / \|g_i^{(k)}\|\)。
- **正交投影修改量**：\(O_i = -\frac{w_j (g_i^\top g_j)}{w_i \|g_j\|^2 + w_j \|g_i\|^2} g_j\)，通过加权最小化调整幅度。
- **最终调制梯度**：\(g_i^{\text{mod}} = \tilde{r}_i [ \prod_{k} (\gamma_l P_i^{(k)} + (1-\gamma_l)g_i^{(k)}) ] + (1-\gamma_g) O_i\)，其中软门控由BCP坐标决定。

### 2.3 算法流程（文字说明）
1. 前向传播获取各模态特征，计算融合特征和损失。
2. 反向传播得到各模态梯度 \(g_i\)。
3. 计算CGE、平衡因子 \(\bar{w}_{ij}\)、余弦相似度 \(c_{ij}\) 和块级相似度 \(c_{ij}^{(k)}\)。
4. 根据BCP坐标计算软门控 \(\gamma_g, \gamma_l\)。
5. 对每对模态判断：若局部块对齐则应用协同投影缩放；若全局冲突则应用正交投影调整。
6. 结合CGE能量感知缩放因子 \(\tilde{r}_i\)，得到最终调制梯度。
7. 用新梯度更新模型参数。

## 3. 实验设计

### 3.1 数据集与场景
- **Kinetics Sounds**：31类视频-音频对，约20k视频切片，8:1:1划分。
- **CREMA-D**：7,442个音视频情感片段（6种情绪），随机划分训练6,698、测试744。
- **UCF-51**：UCF-101的子集，6,845个视频，RGB和光流双模态，5,466训练/1,379测试。

### 3.2 Benchmark
- **不平衡方法对比**（13种）：Joint training、G-Bleeding、Greedy、OGM-GE、AL、IMCL、AGM、PMR、Diag&Re、LFM、ARM、Remixing、InfoReg。
- **冲突感知方法对比**（8种）：GradNorm、PCGrad、MMCos、GMD、ReconBoost、MMPareto、CGGM、BALGRAD。

### 3.3 骨干网络
- CNN-based：ResNet-18
- Transformer-based：ViT-Base

### 3.4 实验设置
- 均采用SGD优化器，momentum 0.9，学习率1e-3，权重衰减1e-4，batch size 64。
- Kinetics Sounds和CREMA-D从头训练，UCF-51使用ImageNet预训练权重。
- 融合方式：静态特征拼接（concatenation）。

## 4. 资源与算力

论文**未明确说明**使用的GPU型号、数量、训练时长等算力资源信息。仅在实验设置部分提及训练细节（优化器、学习率等），未披露硬件配置。

## 5. 实验数量与充分性

### 实验数量
- **主实验**：在3个数据集上，针对2种骨干网络（CNN/Transformer），对比了13种不平衡方法和8种冲突方法，共产生大量对比结果（表1、表2）。
- **消融实验**（表3）：对三个模块（EAR、Syn、Orth）分别和组合进行消融，共7组+baseline。
- **定性分析**：BCP训练动态可视化（图3）、互信息分析（图4）、CGE收敛曲线（图5）。

### 充分性与公平性
- 复现了所有基线方法在相同训练协议下，避免不公平比较。
- 采用多个数据集覆盖不同模态组合（音视频、光流+RGB），且包含CNN和Transformer两种架构。
- 消融实验完整验证了每个模块的必要性。
- 定性分析补充了定量结果，揭示了RGM在平衡和冲突解决上的优势。
- **充分且客观**：设计全面，控制变量严格，结果一致领先。

## 6. 主要结论与发现

1. **RGM在几乎所有设置下达到最优**：表1中RGM在KS（72.56%）、CREMA-D（74.91%）、UCF-51（76.30%）均超过所有不平衡方法；表2中在冲突方法对比中也全面领先。
2. **平衡因子\(\bar{w}_{ij}\)最高**：RGM的平衡因子均高于基线，表明其有效促进了模态贡献的平衡。
3. **SynOrth Grad** 能根据冲突程度自适应切换协同与正交旋转，避免过对齐或欠对齐。
4. **CGE** 是有效的收敛感知度量，结合BCP可实时监控和引导训练。
5. **互信息分析**显示RGM比其他方法（如CGGM）更好地保留了各模态特有信息，未造成特征同质化。
6. 联合处理不平衡和冲突比孤立处理效果更好。

## 7. 优点

- **统一框架**：首次在梯度空间同时、自适应地处理模态不平衡与冲突，无需额外损失或复杂架构。
- **理论支撑**：Dirichlet能量最小化解具有封闭形式；CGE有收敛保证（定理1）；块级缩放可提高余弦相似度（定理2）。
- **可解释性**：BCP平面提供可视化的训练诊断工具，清晰展示梯度状态演变。
- **兼容性**：与任意融合策略、骨干网络兼容，泛化性强。
- **实验全面**：覆盖多种数据集、骨干、基线，结果稳健。

## 8. 不足与局限

- **未处理数据级冲突**：论文仅关注表征层（梯度）冲突，未考虑模态对齐错误、语义不一致等数据层冲突，适用范围受限。
- **资源信息缺失**：未报告GPU型号、训练时长等，影响可复现性评估。
- **理论分析深度有限**：虽给出CGE收敛界和封闭解，但未提供更严格的优化收敛速度分析。
- **仅验证两类模态**：实验均为双模态场景（音/视频、RGB/光流），对更多模态（如文本、深度、触觉）的扩展性未验证。
- **潜在的调参依赖**：门控函数的温度参数q（依赖于\(\bar{w}_{ij}\)）可能对训练超参数敏感，虽然文中声称自适应，但未充分讨论敏感度。
- **部署代价**：需额外计算块级Dirichlet能量和正交投影，可能增加训练开销（但未量化）。

（完）
