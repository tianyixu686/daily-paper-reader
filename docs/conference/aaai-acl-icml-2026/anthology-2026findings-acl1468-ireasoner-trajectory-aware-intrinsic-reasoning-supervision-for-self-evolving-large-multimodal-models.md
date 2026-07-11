---
title: "IREASONER: Trajectory-Aware Intrinsic Reasoning Supervision for Self-Evolving Large Multimodal Models"
title_zh: IREASONER：面向自演进大型多模态模型的轨迹感知内在推理监督
authors: "Meghana Sunil, Manikandarajan Venmathimaran, Muthu Subash Kavitha"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.1468.pdf"
tags: ["query:post-multi"]
score: 9.0
evidence: 大型多模态模型的自演进内部推理监督
tldr: 现有自演进框架仅奖励最终输出，对中间推理步骤约束不足。IREASONER通过轨迹感知的内在奖励信号，在提议-求解循环中监督CoT推理路径的内部一致性，使模型在无标注数据上自我提升多模态推理能力。实验证明该方法在视觉决策任务上更优。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1468/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 804, \"height\": 843, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1468/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1643, \"height\": 624, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1468/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 812, \"height\": 710, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1468/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 796, \"height\": 540, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1468/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 812, \"height\": 712, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1468/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 633, \"height\": 314, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1468/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1656, \"height\": 499, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1468/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1662, \"height\": 462, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1468/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1662, \"height\": 308, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1468/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1005, \"height\": 180, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1468/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 807, \"height\": 222, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1468/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1663, \"height\": 500, \"label\": \"Table\"}]"
motivation: 自演进多模态模型缺乏对中间推理步骤的有效监督，限制推理质量。
method: 在提议-求解循环中，基于推理轨迹的一致性设计内在奖励，区分不同推理路径。
result: 在视觉推理基准上超越了仅奖励最终输出的自演进框架。
conclusion: 轨迹监督信号能有效引导多模态模型生成更高质量的推理链。
---

## Abstract
Recent work shows that large multimodal models (LMMs) can self-improve from unlabeled data via self-play and intrinsic feedback. Yet existing self-evolving frameworks mainly reward final outcomes, leaving intermediate reasoning weakly constrained despite its importance for visually grounded decision making. We propose IREASONER, a self-evolving framework that improves an LMM’s implicit reasoning by explicitly eliciting chain-of-thought (CoT) and rewarding its internal agreement. In a Proposer–Solver loop over unlabeled images, IREASONER augments outcome-level intrinsic rewards with a trajectory-aware signal defined over intermediate reasoning steps, providing learning signals that distinguish reasoning paths leading to the same answer without ground-truth labels or external judges. Starting from Qwen2.5-VL-7B, IREASONER yields up to +2.1 points across diverse multimodal reasoning benchmarks under fully unsupervised post-training. We hope this work serves as a starting point for reasoning-aware self-improvement in LMMs in purely unsupervised settings.

---

## 论文详细总结（自动生成）

以下是基于提供的论文内容生成的详细中文总结。

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究动机**：大型多模态模型（LMM）可以通过自对弈和内在反馈从未标注数据中自我改进，但现有的自演进框架主要奖励最终输出（如答案或整体响应），对中间推理步骤缺乏有效约束。即使两个响应得出相同答案，其推理路径可能差异巨大（一个正确、一个依赖捷径或幻觉），但仅凭结果无法区分，导致中间推理质量不稳定。
- **整体含义**：IREASONER 旨在解决这一限制，通过在无监督自演进循环中显式引入轨迹感知的内在奖励，监督中间 Chain-of-Thought (CoT) 步骤的一致性，从而提升 LMM 在视觉任务中的隐含推理能力，无需任何标注数据或外部裁判。

### 2. 论文提出的方法论

- **核心思想**：在 Proposer–Solver 双角色自演进框架基础上，对 Solver 的奖励函数进行扩展：除了基于答案级自我一致性的奖励外，增加一个**内在 CoT 一致性奖励**，该奖励通过比较同一主导答案组内各 rollout 的中间步骤嵌入相似度来计算，并给予早期、重基础性步骤更高的权重。
- **关键技术细节**：
  - **Proposer–Solver 循环**：从无标签图像出发，Proposer 生成视觉问题，Solver 采样 N 个推理 rollout（每个包含 CoT 和答案）。
  - **主导答案组**：根据多数答案（empirical answer distribution）划分小组 G，只在该组内计算步骤一致性，避免强化错误答案。
  - **步骤嵌入与原型**：将每个步骤文本通过模型内部文本表示嵌入（ℓ2 归一化 token 嵌入均值），每个步骤 j 在组内形成原型 μj（平均嵌入），然后计算每个 rollout 的步骤与原型之间的余弦相似度。
  - **加权聚合**：采用递减权重 w1>w2>... 聚合各步骤相似度，反映早期步骤在接地和设置上的重要性。
  - **密度加权**：引入可靠性因子 ρ = (|G|/N)^γ，当主导组较小时降低步骤奖励权重。
  - **奖励混合**：Solver 的总奖励为答案级奖励 (rans) 与步骤级奖励 (rstep) 的加权和，权重 λ(t) 随训练逐步增加（含预热和斜坡）。
  - **优化目标**：使用 KL 正则化的 REINFORCE 算法（带 EMA 基线）分别优化 Solver 和 Proposer，Proposer 使用答案熵作为奖励（避免退化问题）。
- **公式/算法流程（文字说明）**：
  1. 对每个图像 x，Proposer 生成问题 q。
  2. Solver 采样 N 个 rollout，每个包含步骤序列和答案。
  3. 计算答案分布，确定主导答案及其组 G。
  4. 对组内每个 rollout，提取步骤文本，通过编码器获得嵌入。
  5. 计算各步骤在组内的原型，再计算各 rollout 各步骤与原型余弦相似度，加权得到 rstep_i。
  6. 结合答案级奖励 rans_i（基于 p(ai | x,q) 和长度惩罚）和 rstep_i，得到最终 Solver 奖励。
  7. 用 KL 正则化 REINFORCE 更新策略。

### 3. 实验设计

- **数据集与场景**：训练使用 2,500 张无标签图像，来自六个来源：ChartQA（400）、AI2D（400）、InfoGraphic-VQA（400）、PlotQA（400）、ChartX（400）、Geometry3K（500）。无任何问答对、标题或外部奖励。
- **Benchmark**：在八个多模态推理基准上评估：InfoGraphic-VQA、AI2D、ScienceQA、MMMU（通用视觉理解）以及 ChartQA、MathVista、MathVision、MathVerse（视觉数学推理）。
- **对比方法**：
  - 基线：Qwen2.5-VL-7B（初始模型）
  - 离散奖励变体（如 Thawakar et al. 的离散奖励 + 步骤级多数）
  - EvoLMM（基于连续奖励的自我一致性）
  - VisPlay（使用 LLM-as-judge 的自我演进）
  - Vision-Zero（需外部监督，仅作参考）
  - IREASONER 的消融变体（仅步骤奖励、仅软多数奖励、移除预热/位置衰减/密度加权等）

### 4. 资源与算力

- 训练在 **8× AMD MI250X GPU** 上进行，使用 **bfloat16** 精度。
- 训练步数：2,500 步（Proposer 每 5 步更新一次），总时长约 **35 小时**。
- 使用 LoRA 微调，冻结主干，采用 AdamW 优化器（学习率 1e-6，权重衰减 0.01）。

### 5. 实验数量与充分性

- **实验组数**：包含主实验（Table 1，对比 6 种方法/变体）、消融实验（Table 2，对 10 种设计选择）、步骤预算敏感性（Table 3，4/6/8/10 步）、模型规模扩展（Table 4，3B/7B/32B 三个规模）、推理时 CoT 消融（Table 4 下半部分）、训练动态分析（Figure 3/5/6）、以及正确多数率统计（Table 5）。
- **充分性与公平性**：
  - 实验覆盖了从通用视觉理解到数学推理的多样基准，消融系统性强，验证了各组件贡献。
  - 对比方法采用相同基线和评估设置（lmms-eval 框架），客观公平。
  - 但训练仅使用 2,500 张图像和单个骨干（Qwen2.5-VL），更长训练和更多模型族尚未验证；此外，消融实验仅报告了单一配置下的结果，未进行多次随机种子重复。

### 6. 论文的主要结论与发现

- IREASONER 在八个基准上平均提升显著：通用理解平均 +1.32 分，视觉数学平均 +1.64 分，最大提升出现在 MathVerse（+2.13 分）。
- 步骤级一致性奖励在连续奖励框架下效果最好，与离散奖励结合效果有限。
- 答案稳定性奖励对高度可验证的短答案任务（如 ChartQA）最强，而步骤奖励对需要中间推理转移的任务（如 MMMU、MathVerse）更有帮助。
- 设计选择中，预热调度最关键，位置衰减和密度加权也带来稳定增益；移除这些组件会导致性能下降。
- 轨迹感知的步骤监督能区分相同答案但不同推理质量的 rollout，改善推理稳定性。
- 推理时保留 CoT 能带来额外增益，表明训练提升的不仅是输出格式，还包括底层表示。

### 7. 优点

- **完全无监督**：仅使用无标签图像，无需任何人工标注或外部奖励模型，具有高可扩展性。
- **轨迹感知**：首次在无监督自演进中显式优化中间推理步骤，解决了“相同答案但推理路径不同”无法区分的问题。
- **设计精心**：预热、位置衰减、密度加权等机制有效抑制了早期噪声和错误强化风险；步骤嵌入使用模型内部表示，轻量且与模型语言空间对齐。
- **透明诊断**：提供了跨 rollout 步骤差异性的可视化与分析，证明步骤对齐度随训练提升。
- **公平对比**：在所有实验中保持推理设置一致，避免评估时任务特定调优。

### 8. 不足与局限

- **可能强化错误推理**：当主导答案组错误且内部一致时，步骤级奖励会强化错误推理。论文虽指出预热和密度加权可缓解，但未完全消除风险。
- **规模与泛化有限**：训练仅 2.5k 步、2.5k 图像，且仅使用 Qwen2.5-VL 系列，未验证更长训练、更大图像规模或其他模型族（如 LLaVA）下的表现。
- **需访问模型内部**：优化需要 log-probability 和 KL 正则化，因此不适用于黑盒 API 模型。
- **步骤对齐依赖刚性索引**：要求 rollout 步骤数可对齐，若推理长度差异大或步骤结构松散，对齐可能引入噪声；论文通过最大步数截断缓解，但仍有限制。
- **未进行多次随机种子重复实验**：消融实验结果可能受单次运行影响，统计显著性未报告。

（完）
