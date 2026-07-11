---
title: Theoretical Perspectives on Data Quality and Synergistic Effects in Pre- and Post-Training Reasoning Models
title_zh: 预训练和后训练推理模型中数据质量与协同效应的理论视角
authors: "Adel Javanmard, Baharan Mirzasoleiman, Vahab Mirrokni"
date: 2026-04-30
pdf: "https://openreview.net/pdf/4196d33ecd2711232aecacdc9c6fcaeafe5ba164.pdf"
tags: ["query:post-multi"]
score: 9.0
evidence: 后训练数据质量理论分析
tldr: 本文理论分析了大型语言模型后训练阶段的数据质量与规模效应。针对指令微调和强化学习两种后训练方式，研究发现监督微调偏好小规模高质量数据，而强化学习则受益于大规模反馈数据。通过在线性回归任务上的理论推导，揭示了预训练与后训练数据需求差异的根本原因，为后训练数据设计提供了理论指导。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有研究缺乏对后训练数据质量与规模效应的理论解释，本文旨在从理论上阐明监督微调和强化学习对数据需求差异的原因。
method: 提出一个理论框架，分析基于上下文权重预测任务的Transformer模型，比较预训练、监督微调和强化学习阶段的数据规模与质量影响。
result: 发现监督微调更适合小规模高质量数据，强化学习需要大规模反馈数据，并揭示了数据规模与质量之间的协同效应。
conclusion: 该理论为后训练阶段的数据选择提供了依据，有助于优化大型语言模型的训练策略。
---

## Abstract
Large Language Models (LLMs) are pretrained on massive datasets and later instruction-tuned via supervised fine-tuning (SFT) or reinforcement learning (RL). Best practices emphasize large, diverse pretraining data, whereas post-training operates differently: SFT relies on smaller, high-quality datasets, while RL benefits more from scale, with larger amounts of feedback often outweighing label quality. Yet it remains unclear why pretraining and RL require large datasets, why SFT excels on smaller ones, and what defines high-quality SFT data. In this work, we theoretically analyze transformers trained on an in-context weight prediction task for linear regression. Our analysis reveals several key findings: $(i)$ balanced pretraining data can induce latent capabilities later activated during post-training, and $(ii)$ SFT learns best from a small set of examples challenging for the pretrained model, while excessively large SFT datasets may dilute informative pretraining signals. In contrast, RL is most effective on large-scale data that is not overly difficult for the pretrained model. We validate these theoretical insights with experiments on large nonlinear transformer architectures.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）
- **研究动机**：大型语言模型（LLMs）在预训练阶段通常依赖大规模、多样化的数据，而在后训练阶段（指令微调SFT或强化学习RL）实践中发现最佳策略存在显著差异：SFT偏好小规模高质量数据，RL则受益于大规模反馈数据。但现有理论缺乏对后训练数据质量与规模效应的合理解释，也不清楚高质量SFT数据的定义。
- **背景**：预训练数据强调“大而全”，后训练数据却呈现不同规律。本文试图从理论层面阐明预训练与后训练对数据需求差异的根本原因，并指导后训练数据的设计。

### 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程
- **核心思想**：通过构建一个基于上下文权重预测任务的线性回归理论框架，分析Transformer模型在预训练、SFT和RL阶段的数据规模与质量影响。
- **关键技术细节**：
  - 将预训练数据设计为平衡的（balanced）样本，能够诱导出潜在能力，这些能力在后训练阶段被激活。
  - SFT从少量对预训练模型具有挑战性的样本中学习最佳；过大的SFT数据集可能稀释预训练信号。
  - RL在大规模数据上最有效，且要求数据对预训练模型不“过于困难”。
- **公式或算法**：文中未给出具体数学公式，但理论推导基于线性回归任务的损失函数和参数学习动态，通过理论分析得出上述结论。

### 3. 实验设计：使用了哪些数据集 / 场景，它的 benchmark 是什么，对比了哪些方法
- **数据集 / 场景**：基于上下文权重预测任务（线性回归）的理论分析，未明确指定真实世界数据集。文中提到在“大型非线性Transformer架构”上进行了实验验证。
- **Benchmark**：未提及具体的标准基准测试集。
- **对比方法**：未明确列出对比方法，主要是理论分析与实验验证的自我对比（不同数据规模、质量水平的SFT和RL设置）。

### 4. 资源与算力
- **未明确说明**：文中未提及使用的GPU型号、数量、训练时长等具体算力信息。仅提到在大型非线性Transformer架构上验证，但无资源细节。

### 5. 实验数量与充分性：大概做了多少组实验，是否充分、客观、公平
- **实验数量**：从摘要和内容看，实验部分主要是对理论发现的验证，未给出具体实验组数或消融实验的详细列表。
- **充分性与公平性**：实验用于验证理论预测，由于理论本身在简化线性回归任务上推导，其结论在非线性Transformer上的泛化需要通过实验确认。文中声称验证了这些理论见解，但未提供详细对比基线或统计显著性说明，因此实验的充分性和客观性尚不完全清晰。

### 6. 论文的主要结论与发现
- **发现1**：平衡的预训练数据可以诱导潜在能力，在后训练阶段被激活。
- **发现2**：SFT最佳数据是少量对预训练模型具有挑战性的样本；过大的SFT数据集会稀释预训练信号。
- **发现3**：RL在大规模数据上最有效，且数据不应过于困难。
- **核心结论**：预训练、SFT和RL对数据规模与质量的需求不同，存在协同效应；该理论为后训练数据选择提供了依据。

### 7. 优点：方法或实验设计上的亮点
- **理论创新**：首次从理论上系统分析了后训练阶段数据质量与规模的效应，填补了该领域的理论空白。
- **框架简洁**：使用线性回归的上下文预测任务作为代理，使得理论推导可行，同时结论具有直观解释性。
- **指导实践**：结果为实际后训练数据选择（如SFT应挑选小批量难例，RL应使用大规模中等难度反馈）提供了明确理论指导。

### 8. 不足与局限：包括实验覆盖、偏差风险、应用限制等
- **实验覆盖不足**：未在真实自然语言任务（如对话、推理）上验证，仅在线性回归和Transformer模型上进行理论和简单实验，泛化性存疑。
- **偏差风险**：线性回归任务与真实语言建模差异较大，理论结论可能不直接适用于复杂语义场景。
- **应用限制**：未考虑多任务、多模态等复杂后训练场景；未讨论数据质量的具体度量（如噪声类型、标注一致性等）。
- **资源信息缺失**：缺乏算力与训练细节，难以评估实验可复现性。

（完）
