---
title: "Generative Giants, Retrieval Weaklings: Why do Multimodal Large Language Models Fail at Multimodal Retrieval?"
title_zh: 生成巨人，检索矮子：为何多模态大语言模型在多模态检索中失败
authors: "Hengyi Feng, Zeang Sheng, Meiyi Qiang, Yang Li, Wentao Zhang"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.781.pdf"
tags: ["query:mr"]
score: 8.0
evidence: 分析多模态大语言模型在零样本多模态检索中的失败原因
tldr: 研究发现多模态大语言模型在多模态检索任务中表现不佳的根本原因：其表示空间被文本语义主导，视觉语义占比极小。通过稀疏自编码器分解模型表示，揭示了这种不平衡是检索失败的主因。该分析对改进多模态检索模型具有重要指导意义。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.781/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 787, \"height\": 536, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.781/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 791, \"height\": 605, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.781/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1651, \"height\": 406, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.781/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 772, \"height\": 471, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.781/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 803, \"height\": 837, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.781/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1650, \"height\": 448, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.781/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1487, \"height\": 370, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.781/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 798, \"height\": 490, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.781/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1652, \"height\": 976, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.781/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 776, \"height\": 250, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.781/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1534, \"height\": 645, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.781/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1640, \"height\": 800, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.781/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1269, \"height\": 270, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.781/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1533, \"height\": 686, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.781/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1655, \"height\": 802, \"label\": \"Table\"}]"
motivation: MLLMs在生成任务上成功却意外地在零样本多模态检索中表现差。
method: 利用稀疏自编码器分解MLLM输出表征，分析语义成分。
result: 发现文本语义主导表示空间，视觉语义不足导致检索失败。
conclusion: 需增强MLLM中视觉语义的编码以提升多模态检索性能。
---

## Abstract
Despite the remarkable success of multimodal large language models (MLLMs) in generative tasks, we observe that they exhibit a counterintuitive deficiency in the zero-shot multimodal retrieval task. In this work, we investigate the underlying mechanisms that hinder MLLMs from being effective retrievers. With the help of sparse autoencoders (SAEs), we decompose MLLM output representations into interpretable semantic concepts to probe their intrinsic behavior. Our analysis reveals that the representation space of MLLMs is overwhelmingly dominated by textual semantics; and the visual semantics essential for multimodal retrieval only constitute a small portion. We find that this imbalance is compounded by the heavy focus of MLLMs on bridging image-text modalities, which facilitates generation but homogenizes embeddings and finally diminishes the discriminative power required for multimodal retrieval. We further discover that the specific feature components that contribute most to the similarity computations of MLLMs are actually distractors that greatly reduce retrieval performance. Building on these insights, we propose , a test-time adaptation approach that applies a whitening transformation to adjust the geometry of MLLM representation spaces. Empirical results show that this simple intervention consistently improves zero-shot multimodal retrieval performance across diverse MLLMs without fine-tuning efforts.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **核心问题**：尽管多模态大语言模型（MLLMs）在生成任务（如图像描述、视觉问答）中取得了巨大成功，但在零样本多模态检索任务中却表现反常地差。作者观察到，参数规模远小于MLLMs的对比式视觉语言模型（如CLIP）在检索上显著优于MLLMs。
- **研究动机**：探究MLLMs为何不能成为有效的多模态检索器，揭示其内在表示机制的瓶颈。
- **整体含义**：MLLMs并非天生缺乏检索能力，而是其表示空间的结构性缺陷（文本主导、视觉弱化、嵌入同质化）阻碍了检索性能。该工作为改进多模态检索模型提供了新的分析视角和轻量级解决方案。

## 2. 方法论：核心思想、关键技术细节与算法流程

- **核心思想**：
  - 使用**稀疏自编码器（SAE）** 将MLLM的密集表示分解为可解释的语义概念，通过能量、模态分数、桥接分数、检索归因分数等量化指标分析表示空间的特性。
  - 基于分析结果，提出**ReAlign**——一种测试时适应方法，通过**零相位成分分析（ZCA）白化变换**调整MLLM嵌入空间的几何结构，使其更有利于检索。

- **关键技术细节**：
  1. **稀疏自编码器（SAE）**：
     - 输入：MLLM最后一层隐藏状态经均值池化后的样本级表示 \(\bar{h} \in \mathbb{R}^d\)。
     - 编码：\(Z = \Phi(\bar{h} W_{\text{enc}}^\top + b)\)，\(\Phi\)为ReLU，\(W_{\text{enc}} \in \mathbb{R}^{c \times d}\)。
     - 重构：\(\hat{H} = Z D\)，\(D \in \mathbb{R}^{c \times d}\)为字典，每行对应一个概念向量。
     - 损失：\(\mathcal{L}_{\text{rec}} = \|\bar{h} - \hat{h}\|^2 + \alpha \|Z\|_1\)，兼顾重构与稀疏性。
  2. **评估指标**：
     - **能量**：\(\text{Energy}_i = \mathbb{E}[z_i]\)，反映概念激活的频繁/强度。
     - **模态分数**：\(\text{ModalityScore}_i = \frac{\mathbb{E}_{z \sim \tau}[z_i]}{\mathbb{E}_{z \sim \iota}[z_i] + \mathbb{E}_{z \sim \tau}[z_i]}\)，量化概念偏向文本（高）还是图像（低）。
     - **桥接分数**：\(B = \mathbb{E}[z_\iota^\top z_\tau] \odot (DD^\top)\)，衡量概念作为图文连接器的程度。
     - **检索归因分数**：\(A = \mathbb{E}[z_\iota \odot (M z_\tau) + z_\tau \odot (M z_\iota)]\)，衡量概念对跨模态相似度的贡献。
  3. **ReAlign方法**：
     - 对候选集计算全局协方差 \(\Sigma\)，引入收缩估计：\(\hat{\Sigma} = (1-\beta)\Sigma + \beta \frac{\operatorname{Tr}(\Sigma)}{d} I\)。
     - 特征值分解 \(\hat{\Sigma} = U \Lambda U^\top\)。
     - 白化与归一化：\(e_i = \frac{(\bar{h}_i - \mu)^\top U (\Lambda + \epsilon I)^{-1/2} U^\top}{\|(\bar{h}_i - \mu)^\top U (\Lambda + \epsilon I)^{-1/2} U^\top\|_2}\)。
     - 对查询使用支持集计算统计量以避免小批量方差。

## 3. 实验设计：数据集/场景、Benchmark与对比方法

- **Benchmark**：**M-BEIR**，包含8个多模态检索任务，共16种检索类型（涵盖文本→图像、图像→文本、混合查询→混合候选等），涉及4个领域（新闻、杂项、时尚、百科）。具体数据集：VisualNews、MSCOCO、Fashion200K、WebQA、EDIS、NIGHTS、OVEN、InfoSeek、FashionIQ、CIRR。
- **评估指标**：Recall@5（大部分任务）或Recall@10（Fashion200K、FashionIQ）。
- **对比方法**：
  - **基线MLLMs**：Qwen2-VL-7B-Instruct、Qwen3-VL-8B-Instruct、Paligemma2-3B-Mix-224、Chameleon-7B。
  - **对比式VLMs**：CLIP (ViT-B/32)、SigLIP2 (Base-16/512)。
  - **微调嵌入模型**：GME、VLM2Vec（基于Qwen2-VL-7B架构）。
- **消融与分析实验**：
  - 移除高检索归因概念（表2）。
  - 不同嵌入提取策略（表5）。
  - 各层贡献分析（图5）。
  - 参数β敏感性（图6）。
  - 与标准PCA/ZCA对比（表8）。
  - 与对比式VLM全面对比（表9）。

## 4. 资源与算力

- **SAE训练**：使用4块NVIDIA H20 GPU，对每个MLLM处理约28亿激活（以Qwen2-VL-7B为例）。SAE字典宽度固定为32768（MLLM）或7168（对比VLM）。训练采用Adam优化器，学习率8e-4，batch size 4096。文中未明确训练时长。
- **ReAlign**：测试时适应，无需训练，计算开销与相似度搜索相当（表7），在1M候选集上约需几秒，内存占用合理。

## 5. 实验数量与充分性

- **实验数量**：
  - 主实验：表3展示了4种MLLM在16个检索任务上的性能，共计64个指标。
  - 消融与分析：表2、5、8、9；图2-6；共约10组独立实验。
  - 与微调模型对比：表4（4个任务）。
  - 效率分析：表7。
- **充分性评价**：
  - **覆盖全面**：涵盖不同规模、架构的MLLM，多种检索类型（文本-图像、图像-文本、复合查询等），以及对多种基线（对比式VLM、微调模型、简单白化变体）。
  - **客观公平**：零样本设置，无额外训练，对比基线均采用官方或标准实现。
  - **鲁棒性验证**：参数敏感性分析（β）展示了稳定性；移除高归因概念的可逆结果（表2）支持了“干扰项”结论。
  - **局限性**：未在更大模型（30B/70B）上验证，仅考虑图像-文本模态。

## 6. 主要结论与发现

1. **文本主导表示**：MLLMs的表示空间严重偏向文本语义，视觉语义占比极小，导致跨模态检索时视觉信息编码不足。
2. **桥接努力同质化**：MLLMs将大量表示能量用于桥接图文模态，但这种对齐使嵌入变得过于相似（同质化），削弱了样本间的区分性。
3. **主导相似度的组件实为干扰**：对相似度贡献最大的概念（高检索归因分数）在移除后反而显著提升检索性能（表2），说明它们是阻碍而非帮助检索的“干扰项”。
4. **ReAlign有效**：简单白化变换可显著提升零样本检索性能，在多个MLLM上平均提升约20-30个Recall点，甚至超越部分微调模型（表4）。

## 7. 优点（方法或实验设计亮点）

- **可解释性分析**：利用SAE将MLLM的黑盒表示分解为语义概念，并设计定量指标（模态分数、桥接分数等）直观揭示问题根源，方法新颖。
- **轻量级解决方案**：ReAlign是训练无关的测试时适应方法，无需标注数据或微调，计算成本低（仅需一次协方差计算），可即插即用。
- **广泛的实证验证**：跨4种不同架构MLLM、16种检索场景、多种基线验证，结果一致且显著。
- **揭示反直觉现象**：发现对相似度贡献最大的特征反而有害，这一洞察对设计更好的检索表征有启发意义。

## 8. 不足与局限

- **模型规模限制**：受计算资源限制，仅评估了3B-8B参数范围的MLLM，未探索30B/70B等更大模型的行为，可能遗漏规模缩放带来的变化。
- **模态覆盖不全**：仅关注图像-文本模态，未涉及视频、音频等其他模态，ReAlign的普适性待验证。
- **分析依赖SAE**：SAE的训练和超参数（字典大小、稀疏度）可能影响概念分解的质量，但文中未进行全面敏感性分析。
- **未讨论对比式VLM的局限**：尽管CLIP等对比模型在简单图文匹配上优越，但在复杂复合查询任务上仍不如MLLMs+ReAlign，文中未深入分析其短板原因。
- **统计显著性报告缺失**：未给出性能方差或显著性检验（如t检验），虽然多次运行取平均（如脚注1），但未报告标准差。

（完）
