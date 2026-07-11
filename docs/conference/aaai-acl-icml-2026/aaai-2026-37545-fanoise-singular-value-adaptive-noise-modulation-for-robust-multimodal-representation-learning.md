---
title: "FANoise: Singular Value-Adaptive Noise Modulation for Robust Multimodal Representation Learning"
title_zh: FANoise：基于奇异值自适应噪声调制的鲁棒多模态表示学习
authors: "Jiaoyang Li, Jun Fang, Tianhao Gao, Xiaohui Zhang, Zhiyuan Liu, Chao Liu, Pengzhang Liu, Qixia Jiang"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/37545/41507"
tags: ["query:post-multi"]
score: 8.0
evidence: 多模态表示学习中的自适应噪声调制
tldr: 现有噪声注入方法多采用静态噪声，忽略了特征分布的动态变化。FANoise根据奇异值自适应调节噪声强度，从梯度和特征分布角度系统研究噪声作用，提升了多模态表示的鲁棒性和泛化能力，在多个多模态任务上取得更优效果。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: 静态噪声注入无法适应训练过程中的特征分布变化，影响多模态表示质量。
method: 通过奇异值分解自适应调整噪声幅度，结合梯度分析和分布匹配实现动态噪声调制。
result: 在图像-文本检索等任务中，FANoise显著提升表示鲁棒性和泛化性能。
conclusion: 自适应噪声调制是一种有效的多模态表示学习增强手段。
---

## Abstract
Representation learning is fundamental to modern machine learning, powering applications such as text retrieval and multimodal understanding. However, learning robust and generalizable representations remains challenging. While prior work has demonstrated that active noise injection, a form of data augmentation, can enhance encoding performance, most existing methods rely on heuristic or static noise, overlooking the dynamic nature of feature distributions during training. In this work, we systematically study the role of noise in representation learning from both gradient-based and feature distribution perspectives, using InfoNCE loss as a representative example. Focusing on multimodal representation learning, we propose FANoise, a novel feature-adaptive noise injection strategy. By leveraging the dynamics of contrastive learning, FANoise effectively mitigates the negative impacts of noise while preserving its benefits. Under this theoretically grounded framework, comprehensive experiments demonstrate that FANoise consistently improves overall performance on multimodal tasks across various base VLM models.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **核心问题**：多模态表示学习中，现有噪声注入方法大多采用**启发式或静态噪声**（如均匀高斯噪声、Dropout等），未能考虑训练过程中特征分布随模型更新的动态变化，导致噪声效果不稳定甚至损害关键特征。
- **研究背景**：对比学习框架（如CLIP、SigLIP、VLM2Vec）在图文检索、视觉问答等任务中取得显著进展，但鲁棒性和泛化性仍是瓶颈。主动噪声注入（如NEFTune、SimCSE）已被证明能提升表示质量，但其作用机制缺乏系统理论分析，且噪声强度与分布设计多凭经验。
- **整体含义**：本文试图建立噪声注入与多模态对比学习之间更深刻的理论联系，并提出一种**特征自适应噪声调制方法**，以同时利用噪声的正则化效益并避免破坏重要特征。

## 2. 方法论：核心思想、关键技术细节与流程

- **核心思想**：通过对InfoNCE损失的梯度分析和特征分布的谱分解，揭示**噪声强度应随特征主轴的重要程度自适应调节**：对强信号（大奇异值）施加较大噪声以增强鲁棒性，对弱信号（小奇异值）施加较小噪声以保护判别信息。
- **关键技术细节**：
  - **梯度分析**：对InfoNCE损失加入噪声（以键特征k为例），推导出噪声等价于给负样本赋予更大权重，加速正样本对齐，且不影响查询梯度期望。
  - **谱结构分析**：对特征矩阵进行SVD分解 \(X = U\Sigma V^\top\)，利用Weyl扰动定理、随机矩阵理论中的“相变阈值”（Marchenko-Pastur分布）和信息论视角，说明均匀噪声会导致小奇异值维度SNR崩溃。
  - **自适应噪声生成**：
    1. 在右奇异向量空间（主成分空间）生成噪声，用缩放函数 \(S(\Sigma_d)\) 调制噪声幅度。
    2. 将缩放后的噪声变换回特征空间：\(N' = N_{\text{scaled}} V^\top\)。
    3. 最终注入：\(\tilde{X} = X + \frac{\alpha}{\sqrt{n}} N'\)，其中 \(\frac{\alpha}{\sqrt{n}}\) 保证噪声总能量与维度无关。
  - **缩放函数设计**：
    - **均匀缩放**：\(S=1\)（等价于传统均匀噪声）。
    - **线性缩放**：\(S = \Sigma_d / \overline{\Sigma_d}\)，维持恒定信噪比。
    - **次线性缩放**（最优）：\(S = \sqrt{\Sigma_d} / \overline{\sqrt{\Sigma_d}}\)，折中方案，保护弱特征同时提供足够扰动。

- **算法流程**（文字描述）：
  1. 前向传播获取特征矩阵 \(X\)，计算SVD得到\(\Sigma, V\)。
  2. 生成高斯噪声矩阵 \(N_{\text{rand}} \sim \mathcal{N}(0,1)\)，应用次线性缩放函数得到 \(N_{\text{scaled}}\)。
  3. 通过 \(V^\top\) 将缩放噪声投影回原始特征空间，并除以 \(\sqrt{n}\) 归一化。
  4. 将噪声加到原始特征上，输入对比学习损失进行训练。

## 3. 实验设计：数据集、基准与对比方法

- **数据集与基准**：使用 **MMEB（Massive Multimodal Embedding Benchmark）**，包含36个数据集（20个域内IND、16个域外OOD），覆盖分类、VQA、检索、视觉定位四类元任务。评价指标为 **Precision@1**，平均所有数据集得出总体分数。
- **对比方法**：
  - **零样本基线**：CLIP、BLIP2、UniIR（两种融合方式）、MagicLens。
  - **微调基线**：UniME(Phi3.5-V/LLaVA-1.6)、MegaPairs(LLaVA-1.6)、VLM2Vec（多个骨干）、LLaVE(LLaVA-OV-7B)。
  - **自身上下游比较**：对同一骨干（Phi3.5-V、Qwen2-VL-2B/7B、LLaVA-1.6-LR/HR）对比有无FANoise，以及均匀/线性/次线性三种缩放方式。
- **骨干网络**：包括Qwen2-VL-2B/7B、LLaVA-NeXT-1.6（低分辨率/高分辨率）、Phi3.5-V-4B，以及LLaVA-OV-7B（仅引作参考）。

## 4. 资源与算力

- **明确说明**：所有主实验在 **8张H800 GPU** 上运行，随机种子42。
- **训练配置**：
  - LoRA适配器（rank=8），最大每数据集10万样本。
  - 线性学习率调度（初始2e-5），2000训练步，200预热步，每GPU每批次256样本（主实验），分析实验时批次大小为每GPU 16。
  - 使用GradCache技术缓解内存限制（chunk size=4）。
- **未提及**：训练总时长、单次实验耗时、能耗等细节。

## 5. 实验数量与充分性

- **实验数量**：
  - 主实验：5种骨干×6个模型变体（含不同分辨率），共约6个实验组（表1，含VLM2Vec基线和FANoise，另列出UniME等第三方结果）。
  - 消融实验：
    - **噪声强度实验**（图2）：7个α值（0, 0.1, 0.2, 0.5, 1, 2, 5）在MMEB上评估。
    - **噪声分布实验**（表2、图5）：均匀、线性、次线性三种缩放，固定α=0.1。
    - **谱分析实验**（图3、图4）：对1000个样本、特征维度1536，计算SVD并对比噪声嵌入、纯噪声的奇异值分布及向量对齐情况。
  - 此外，通过图3/4验证理论预测（Weyl定理、相变阈值）。
- **充分性与公平性**：
  - 实验设计较为全面：覆盖不同骨干、不同尺度（2B~7B）、不同分辨率、多噪声参数、多种缩放策略。
  - 与SOTA对比公平：在同一基准MMEB上，汇报了官方或重新评估的分数，注明了VLM2Vec原文的对比设置。
  - 不足：未在最大规模模型（如LLaVA-OV-7B）上执行FANoise（作者说明因GPU限制），但引用其基线；消融实验中α选择基于小批量试验，主实验采用α=0.1，但未给出完整的α搜索曲线（仅给出7个点，且分析实验中batch size减小可能影响最优值）。

## 6. 主要结论与发现

- **理论方面**：
  1. 梯度分析揭示噪声等效于增加负样本权重，加速正样本对齐。
  2. 谱分析表明均匀噪声会导致小奇异值维度SNR骤降，而次线性缩放可有效平衡保护与扰动。
- **实验方面**：
  1. **FANoise（次线性缩放）** 在5种骨干上平均提升 **2.04%**，最高提升 **4.2%**（LLaVA-1.6-LR）和 **3.5%**（LLaVA-1.6-HR）。
  2. 最佳模型（FANoise + LLaVA-1.6-HR）超越当前SOTA（UniME、MegaPairs等），达到 **66.4%** 平均分（vs VLM2Vec Qwen2-VL-7B的65.8%）。
  3. 噪声强度存在最优范围（α≈0.1~0.5），过高则破坏特征。
  4. 次线性缩放优于均匀和线性缩放，因其在强信号区提供适度扰动、在弱信号区保持较高相似度。
- **通用性**：FANoise即插即用，不依赖特定架构，适用于多种VLM。

## 7. 优点

- **理论驱动**：从梯度和谱两个角度系统分析噪声作用机制，提供了理论支撑（Weyl定理、Marchenko-Pastur分布、相变阈值），而非纯经验调参。
- **自适应设计**：根据奇异值动态调整噪声幅度，避免了静态噪声对弱特征的破坏。
- **即插即用**：无需修改模型架构或训练范式，可直接接入现有对比学习流程。
- **广泛兼容**：在多个不同容量、不同架构的VLM上验证有效，鲁棒性良好。
- **实验严谨**：消融实验覆盖噪声强度、分布类型，并辅以谱分析可视化，验证理论预测。

## 8. 不足与局限

- **实验覆盖**：
  - 未在最大规模模型（如LLaVA-OV-7B、LLaVA-1.6-13B）上测试，作者承认因GPU资源限制，这限制了结论的通用性。
  - 主实验的α固定为0.1（来自小批量搜索），但更大模型或不同骨干可能需要单独调参。
  - 消融实验中训练样本数减少（每数据集最多5000），可能影响最优参数结论的稳定性。
- **理论局限**：
  - 梯度分析假设k采样均匀且近似平行（\(k_l \approx \gamma_l q_l\)），实际中未必严格满足。
  - 信息论视角未提供紧的保真度下界，更多是定性解释。
- **应用限制**：
  - 计算开销：每次前向传播需执行SVD，虽然特征维度不大（1536），但可能对实时推理或极大规模训练产生额外代价（文中未报告时间开销）。
  - 仅评估了多模态检索/分类任务，未测试纯文本或纯图像表示学习，适用范围限于多模态场景。
- **公平性**：与LLaVE、UniME等对比时，后两者用了更复杂的硬负采样/奖励模型，而FANoise更简单，但作者未在相同模型骨干下进行公平对比（LLaVE基于LLaVA-OV-7B，FANoise最强基于LLaVA-1.6-HR），直接数值比较具有一定偏差。

（完）
