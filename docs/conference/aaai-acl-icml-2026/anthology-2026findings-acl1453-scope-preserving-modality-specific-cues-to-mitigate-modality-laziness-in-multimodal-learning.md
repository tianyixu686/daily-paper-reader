---
title: "SCOPE: Preserving Modality-Specific Cues to Mitigate Modality Laziness in Multimodal Learning"
title_zh: "SCOPE: 保留模态特定线索以缓解多模态学习中的模态惰性"
authors: "Jingfan Yang, Rui Zhang, Liang Hong, Ke Yuan"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.1453.pdf"
tags: ["query:post-multi"]
score: 8.0
evidence: 多模态表示学习保留模态特定线索
tldr: SCOPE框架通过互信息引导的解耦模块分离共享与互补语义，保留模态特定线索，有效缓解多模态学习中的模态惰性问题，在多模态任务上取得显著性能提升。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1453/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1656, \"height\": 832, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1453/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 718, \"height\": 384, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1453/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 803, \"height\": 413, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1453/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 798, \"height\": 373, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1453/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 777, \"height\": 250, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1453/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1536, \"height\": 645, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1453/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 698, \"height\": 540, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1453/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 795, \"height\": 295, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1453/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 799, \"height\": 400, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1453/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 796, \"height\": 321, \"label\": \"Table\"}]"
motivation: 多模态模型常过度依赖主导模态，忽略互补信号，现有方法忽视模态特定线索。
method: 提出SCOPE框架，利用互信息解耦分离共享与互补语义，保留模态特定线索。
result: 在多个多模态任务上缓解了模态惰性，提升了整体性能。
conclusion: 保留模态特定线索是缓解模态惰性的有效策略，SCOPE为多模态学习提供了新框架。
---

## Abstract
Multimodal learning aims to learn unified multimodal representations from heterogeneous modalities and supports many natural language processing tasks. However, multimodal models often exhibit modality laziness: over-relying on a dominant modality and under-exploiting complementary signals. Existing approaches typically strengthen unimodal training or rebalance modality contributions, but they may still emphasize shared semantics and overlook modality-specific cues. To address this, we propose SCOPE, a unified framework for learning complete multimodal representations, achieving Shared-and-COmplementary cue PrEservation. Firstly, SCOPE uses a mutual information-guided disentanglement module to separate shared semantics from modality-specific cues and mitigate representation collapse. Secondly, SCOPE aligns modalities by enforcing structural consistency between modality-wise semantic graphs, avoiding brittle point-wise matching. Finally, SCOPE performs balanced fusion via structure-aware diffusion attention to integrate shared and complementary cues without feature homogenization. Experiments on four benchmark datasets show that SCOPE consistently outperforms SOTA baselines, achieving up to 27.10% accuracy improvement.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）
- **核心问题**：多模态学习模型普遍存在“模态惰性”（modality laziness），即过度依赖某一主导模态（如文本）而未能充分挖掘其他模态（如图像、音频）的互补信号。
- **现有方法局限**：已有工作主要通过增强弱模态训练（如架构正则化）或动态平衡模态贡献（如梯度调制），但仍然倾向于强化共享语义，忽视了模态特有的互补线索。
- **解决目标**：如何在学习统一的跨模态表示时，既对齐共享语义，又保留模态特定线索，从而有效抑制模态惰性。

## 2. 方法论：核心思想、关键技术细节
- **整体框架**：提出 **SCOPE**（Shared-and-COmplementary cue PrEservation），包含三个模块：
  1. **模态特定解耦（Modality-Specific Disentanglement）**  
     - 使用自注意力和交叉注意力提取单模态显著特征。  
     - 引入互信息（MI）引导的目标函数：最大化匹配样本对间的依赖（共享语义），最小化非匹配样本间依赖（避免表示坍缩）。  
     - 实际采用余弦相似度作为MI的代理，损失为 `L_dis = L_sim + L_diff`，分别惩罚匹配对相似度偏离1和交叉对相似度偏离0。
  2. **结构一致性对齐（Structure-Consistent Alignment）**  
     - 为每个模态构建参数无关的语义图：通过公式 `g_ij = sqrt((1 - (k^2-1)*f_ij / (k * sum f_ij))+ )` 获得闭式解，无需调节超参数且尺度不变。  
     - 对齐不同模态的语义图结构：最小化图邻接矩阵的Frobenius范数差异 `L_align`。
  3. **平衡融合（Balanced Fusion）**  
     - 加权组合各模态特征和图结构。  
     - 结构感知掩码注意力：基于图边集对全连接注意力的结果进行掩码，实现局部聚合。  
     - 扩散注意力：通过指数衰减的幂级数 `˜A = sum ξ(1-ξ)^t A^t` 传播多跳邻近信息，避免过平滑，最后残差连接更新表示。

## 3. 实验设计：数据集、基准、对比方法
- **数据集**（5个）：  
  - MVSA（文本-图像，3类）  
  - TumEmo（文本-图像，7类）  
  - CREMA-D（音频-视觉，7类）  
  - IEMOCAP（音频-文本-视觉，5类）  
  - MM-IMDb（文本-图像，多标签23类）
- **对比方法**：8个基线，分为三类：  
  - 传统融合：Sum、Concat、Late Fusion (LF)  
  - 架构正则化：LFM、MLA  
  - 动态协调：CRMT、OGM、InfoReg
- **评估指标**：准确率（Accuracy）和宏F1（macro-F1），均越高越好。

## 4. 资源与算力
- **硬件**：Linux服务器，Intel Xeon Gold 5320 CPU（2.20GHz）、1.0 TB RAM、4块NVIDIA A40 GPU。
- **软件**：Ubuntu 22.04，PyTorch相关框架。
- **训练参数**：100个epoch，batch size=60，初始学习率1e-4（AdamW优化器，带学习率衰减）。
- **未提供详细训练时间**，仅在消融实验中给出了图密度对每epoch时间的影响（例如MVSA上k=60时每epoch 95秒）。

## 5. 实验数量与充分性
- **主实验**：4个表（表2、3）覆盖5个数据集，报告各模态单独性能及融合性能，与8个基线对比。
- **泛化性验证**：表4评估了3种不同骨干网络（CLIP、ImageBind、Qwen2.5-Omni），证明方法不依赖特定特征提取器。
- **消融研究**：
  - 表6：依次移除特征细化（AFR）、MI解耦（MID）、结构对齐（SCA）、平衡融合（BF）的效果。  
  - 图2：可视化解耦前后的特征分布。  
  - 图3：分析图密度（k值）对准确率和时间的影响。  
  - 图4：评估自注意力、交叉注意力的组合效果。  
  - 表5：比较扩散注意力与GAT在不同扩散步数下的Dirichlet能量，验证抗过平滑能力。
- **充分性**：实验涵盖了多个模态组合、不同规模的模型、多种基线，并进行了充分的消融和灵敏度分析，结果客观、公平。但缺少与最新的大规模多模态模型（如LLaVA等）的对比，限定于经典多模态学习场景。

## 6. 主要结论与发现
- SCOPE在所有数据集上均取得最优或次优性能，融合准确率提升明显（最高达27.10%）。  
- 保留模态特定线索是缓解模态惰性的关键，单纯平衡模态贡献可能仍导致弱模态贡献不足。  
- 结构一致性对齐和扩散注意力融合能够有效整合共享与互补信息，避免特征同化。  
- 方法对不同的预训练骨干网络均有效，具有较好的泛化能力。

## 7. 优点
- **方法创新**：  
  - 提出互信息引导的解耦损失，分离共享与特定信息。  
  - 设计参数无关的语义图构造，无需调节超参数，适合多模态场景。  
  - 结构感知扩散注意力融合，兼顾局部与全局信息，防止过平滑。
- **实验全面**：在多种模态组合、多个数据集、多种基线以及消融、超参数分析上进行了系统评估。
- **代码/复现**：论文提及了详细实现细节，易于复现。
- **结果显著**：相对于强基线，性能提升幅度大，尤其在模态严重不平衡的数据集（如IEMOCAP）上表现突出。

## 8. 不足与局限
- **应用范围**：当前假设模态数据是严格对齐的（paired），未考虑未对齐或存在噪声的跨模态数据。论文在Limitations中明确指出了这一限制，未来需要扩展到弱对齐或伪对齐场景。
- **实验覆盖**：未与其他近期大规模多模态预训练模型（如VideoLLaMA等）直接比较，对比基线主要为2019-2025年的经典方法。
- **计算成本**：虽然复杂度分析为 `O(M^2 B^2 d + T k B d)`，但实验中未提供与其他方法的训练/推理时间对比，用户难以评估实际开销。
- **偏差风险**：实验数据集均来自标准评测，可能存在领域偏差；在更开放、低资源的实际场景下效果未知。

（完）
