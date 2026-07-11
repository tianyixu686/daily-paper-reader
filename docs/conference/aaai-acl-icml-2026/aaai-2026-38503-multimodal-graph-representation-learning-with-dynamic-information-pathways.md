---
title: Multimodal Graph Representation Learning with Dynamic Information Pathways
title_zh: 基于动态信息路径的多模态图表示学习
authors: "Xiaobin Hong, Mingkai Lin, Xiaoli Wang, Chaoqun Wang, Wenzhong Li"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/38503/42465"
tags: ["query:post-multi"]
score: 6.0
evidence: 基于动态信息路径的多模态图表示学习
tldr: DiP框架通过在多模态图中引入模态伪节点实现动态信息路由，自适应进行模态内消息传递和模态间聚合，提升了多模态图表示学习的灵活性和表达能力。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: 现有图神经网络在多模态图上依赖静态结构，缺乏灵活性。
method: 引入模态伪节点实现动态消息路由，支持自适应跨模态聚合。
result: 在多个多模态图基准上取得最优性能。
conclusion: 动态信息路径有效增强了多模态图表示学习的能力。
---

## Abstract
Multimodal graphs, where nodes contain heterogeneous features such as images and text, are increasingly common in real-world applications. Effectively learning on such graphs requires both adaptive intra-modal message passing and efficient inter-modal aggregation. However, most existing approaches to multimodal graph learning are typically extended from conventional graph neural networks and rely on static structures or dense attention, which limit flexibility and expressive node embedding learning. In this paper, we propose a novel multimodal graph representation learning framework with Dynamic information Pathways (DiP). By introducing modality-specific pseudo nodes, DiP enables dynamic message routing within each modality via proximity-guided pseudo-node interactions and captures inter-modality dependence through efficient information pathways in a shared state space. This design achieves adaptive, expressive, and sparse message propagation across modalities with linear complexity. We conduct the link prediction and node classification tasks to evaluate performance and carry out full experimental analyses. Extensive experiments across multiple benchmarks demonstrate that DiP consistently outperforms baselines.

---

## 论文详细总结（自动生成）

# 基于动态信息路径的多模态图表示学习（DiP）论文总结

## 1. 核心问题与整体含义（研究动机和背景）
- **问题背景**：现实世界中的图数据常包含多模态节点属性（如图像和文本），形成多模态图（MMG）。现有方法大多将传统图神经网络（GCN、GAT）直接扩展，依赖静态图结构或稠密注意力，导致灵活性差、表达能力不足，且难以处理模态间信息粒度差异。
- **主要挑战**：
  - 视觉与文本特征粒度不匹配，直接融合导致语义稀释；
  - 静态聚合拓扑无法适应任务特定的动态依赖，容易过平滑、过挤压；
  - 现有模态无关融合忽视模态间的互补性。
- **研究目标**：设计一种自适应、高效、可扩展的多模态图表示学习框架，同时捕获模态内和模态间的依赖关系。

## 2. 方法论：核心思想与关键技术细节
- **核心思想**：提出**动态信息路径（DiP）**，通过引入**模态特定的伪节点**作为轻量级动态中介，解耦消息传递与固定拓扑，实现自适应路由。
- **关键技术细节**：
  - **模态编码器**：使用预训练模型（CLIP、ViT、DINOv2、T5、ImageBind）将原始图像/文本投影到潜在空间，编码器参数冻结。
  - **统一状态空间**：节点和伪节点共享可学习状态嵌入 \( S \in \mathbb{R}^{d_s} \)，通过**多通道路径积分**（公式1）计算近邻度，避免每对参数。
  - **模态内扩散路径（Intra-Modal）**：
    - **局部消息传递（LocalMP）**：节点在一跳邻域内聚合；
    - **全局消息传递（GlobMP）**：伪节点作为全局代理，收集图节点消息（G2P），在伪节点间扩散（P2P），再分发回图节点（P2G）。复杂度 \( O(\tau n n_p) \)，\( n_p \ll n \)。
  - **模态间聚合路径（Inter-Modal）**：视觉和文本伪节点在共享状态空间通过近邻度互相更新（公式8-9），使跨模态信息以线性代价融合。
  - **递归更新**：使用单循环层，参数跨步骤共享，L步后得到最终表示。
  - **模态融合与任务头**：拼接视觉和文本状态后线性投影，用于链接预测（内积+sigmoid）或节点分类（MLP+softmax）。

## 3. 实验设计
- **数据集**：
  - 链接预测：Amazon-Sports、Amazon-Cloth、Goodreads-LP（来自MM-GRAPH基准）。
  - 节点分类：Ele-Fashion、Goodreads-NC。
- **基准与对比方法**：
  - 拓扑无关：MLP。
  - 传统GNN：GCN、SAGE、BUDDY（子图草图链接预测）。
  - 多模态GNN：MMGCN、MGAT、UniGraph2。
- **编码器组合**：视觉（CLIP、ViT、DINOv2、ImageBind）× 文本（CLIP、T5、ImageBind），共4种组合。
- **评估指标**：链接预测用MRR、Hit@1、Hit@10；节点分类用Accuracy。
- **实验设置**：每种配置重复10次，报告均值±标准差。

## 4. 资源与算力
- **GPU型号与数量**：4× Tesla V100-SXM2-32GB（论文实验部分明确说明）。
- **训练时长**：论文未明确给出总训练时间或每轮时长，仅在复杂度分析表（Table 4）中报告了每轮耗时（如Amazon-Sports上DiP每轮213.134秒），但未提及整个训练过程的总时长。
- **其他资源**：PyTorch 2.4.0, CUDA 12.2。

## 5. 实验数量与充分性
- **实验规模**：
  - 链接预测：3个数据集 × 4种编码器组合 = 12个主要实验组。
  - 节点分类：2个数据集 × 4种编码器组合 = 8个主要实验组。
  - 消融实验：1组（去除伪节点、局部/全局消息传递、跨模态交互），在Ele-Fashion和Amazon-Sports上各6项。
  - 复杂度分析：1个表格（时间和内存）。
  - 伪节点数量参数搜索：在Ele-Fashion和Amazon-Sports上各16种组合（npv, npt ∈ {16,32,64,128,256,512}，图中展示部分）。
  - 过平滑分析：1个图。
  - 消息路径可视化：1个图。
  - t-SNE可视化：4个模型。
- **充分性评价**：实验覆盖了多个域和多种编码器，充分验证了通用性；对比方法全面（包括传统GNN和多模态专用模型）；所有结果重复10次，统计可靠；包含消融、复杂度、参数敏感性分析，实验设计客观公平。**结论**：实验充分，支持核心主张。

## 6. 主要结论与发现
- DiP在所有数据集和编码器组合上**一致超越所有基线**，尤其在Goodreads-LP链接预测任务中，MRR提升高达+2.88。
- 节点分类任务中，DiP在Ele-Fashion最高比最佳基线高+2.28%，在Goodreads-NC平均高+2.35%。
- 消融实验证明：每个组件（视觉、文本伪节点、局部/全局消息传递、跨模态交互）均不可或缺。
- DiP能有效缓解过平滑：更深层时Dirichlet能量保持较高。
- 动态路径可视化显示伪节点可形成语义聚类中心。
- 复杂度分析：DiP每轮耗时接近SAGE，内存远低于MMGCN和MGAT，表明高可扩展性。

## 7. 优点
- **创新性强**：首次将动态伪节点与路径积分结合用于多模态图，同时解决了结构刚性和融合效率问题。
- **通用与可扩展**：支持多种预训练编码器；复杂度线性，适合大规模图。
- **鲁棒性**：有效缓解过平滑，在深层网络中仍保持判别力。
- **实验严谨**：多数据集、多编码器、多任务、多基线、带统计波动的重复实验。
- **可视化分析**：通过t-SNE和路径激活图解释模型行为。

## 8. 不足与局限
- **训练时长缺失**：未提供完整训练过程的壁钟时间，难以评估实际训练成本。
- **伪节点数量选择**：虽做了参数搜索，但最佳数量依赖验证集，缺乏理论指导，可能影响迁移效率。
- **编码器冻结假设**：所有预训练编码器参数固定，未能探索端到端微调对性能的提升。
- **模态对单一**：仅考虑图像和文本双模态，未验证更多模态（如音频、视频）的扩展性。
- **任务覆盖有限**：仅测试链接预测和节点分类，未涉及图分类、多模态知识图谱补全等其他多模态图任务。
- **潜在偏差风险**：数据集来自电商和图书领域，结论在更异构的场景（如生物网络）中需进一步验证。

（完）
