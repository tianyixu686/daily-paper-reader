---
title: "CAMP: Coherent Alignment of Multimodal Prototypes for Explainable Complementary Learning"
title_zh: "CAMP: 面向可解释互补学习的多模态原型一致性对齐"
authors: "Alvaro Lopez Pellicer, Eoin M. Kenny, Simran Lamba, Shubham Sharma, Plamen P Angelov, Saumitra Mishra"
date: 2026-04-30
pdf: "https://openreview.net/pdf/3e0466c6754ca61559c5a90cdf50db47aad77b6b.pdf"
tags: ["query:post-multi"]
score: 7.0
evidence: 互补多模态分类的原型对齐方法
tldr: CAMP针对互补多模态分类任务，通过最优传输对齐类别级证据，并施加几何约束防止模态主导，在保持可解释性的同时提升分类精度。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 互补多模态分类中现有方法在准确性与可解释性之间存在权衡。
method: 利用最优传输对齐类别级多模态证据，并施加几何约束抑制模态主导。
result: 在多个互补多模态数据集上实现了高精度与可解释性的双赢。
conclusion: CAMP为互补多模态分类提供了有效的可解释解决方案。
---

## Abstract
Most multimodal learning assumes redundant views (such as image–caption pairs), yet many applications require combining complementary modalities that provide distinct evidence (such as an X-ray and medical history). We term this setting *Complementary Multimodal Classification* (CMC). In CMC, existing explainable-by-design methods often force an accuracy–interpretability trade-off because single shared similarity metrics fail under asymmetric, class-conditional evidence. To address this, we propose Coherent Alignment of Multimodal Prototypes (CAMP). CAMP enforces coherent multimodal reasoning by aligning class-wise evidence via optimal transport and imposing geometric constraints to counter modality dominance and representation collapse. We provide theoretical guarantees showing that these mechanisms eliminate such degeneracies without restricting expressivity. Empirically, across 16 public CMC datasets, CAMP matches or exceeds large ($>$100M parameter) AutoML baselines with fewer than 1M trainable parameters, and when fine-tuned end-to-end it achieves state-of-the-art performance. To the best of our knowledge, this work is the first modality-agnostic prototype-learning framework designed for complementary multimodal tasks.

---

## 论文详细总结（自动生成）

# 详细中文总结

## 1. 论文的核心问题与整体含义

- **研究动机**：现有大多数多模态学习方法假设模态间信息冗余（如图像-标题对），但现实中许多应用需要结合**互补性模态**（如X光片与病历），它们提供的是**不同且独立的证据**。作者将这种场景定义为**互补多模态分类（CMC）**。
- **核心挑战**：在CMC中，现有的可解释性设计方法往往迫使**准确率-可解释性之间的权衡**，因为单一的共享相似度指标无法处理非对称、类别条件依赖的证据。
- **整体目标**：提出一种既保持高解释性又达到甚至超越大规模AutoML模型分类精度的原型学习框架。

## 2. 论文提出的方法论

- **核心思想**：CAMP（Coherent Alignment of Multimodal Prototypes）通过**最优传输（Optimal Transport）** 对类别级的多模态证据进行对齐，并施加**几何约束**来抑制模态主导和表示坍缩。
- **关键技术细节**：
  - 使用**最优传输**将每个类别的多模态原型在表示空间中一致性对齐，确保不同模态提供的证据在类别层面相互呼应。
  - 引入几何约束：防止某一模态过度主导最终决策，同时避免表征空间中的原型坍缩（即不同类别原型过于接近）。
  - 提供理论保证：证明这些机制能够在不限制表示表达能力的前提下消除上述退化现象。
  - 模型是**模态无关**的原型学习框架，适用于任意互补模态对。
- **算法流程**（文字说明）：
  1. 从每个模态提取特征，并为每个类别生成可解释的原型（prototype）。
  2. 通过最优传输损失将不同模态的类别级原型对齐。
  3. 施加几何正则项（如模态平衡约束、原型间距离约束）。
  4. 联合优化分类损失与对齐/约束损失。
  5. 最终预测基于对齐后的多模态原型进行推理，并利用原型提供可解释性证据。

## 3. 实验设计

- **使用数据集**：16个公开的CMC数据集（具体名称未列出，但涵盖不同领域的互补模态分类任务）。
- **基准（Benchmark）**：对比了超过1亿参数的**AutoML基线**，以及可能其他可解释多模态方法（如标准ProtoPNet等，但摘要未详细列出）。
- **对比方法**：主要是大规模AutoML模型（>100M参数），以及可能现有的原型学习方法（原文未展开）。
- **性能指标**：分类准确率，同时强调可解释性（原型是否一致、有语义）。

## 4. 资源与算力

- **模型规模**：CAMP仅有**少于100万可训练参数**，远小于对比的AutoML基线（>1亿参数）。
- **算力说明**：原文未明确说明使用的GPU型号、数量或训练时长，仅提及参数规模。因此算力资源信息不足。

## 5. 实验数量与充分性

- **数量**：在**16个数据集**上进行了评估，覆盖多个互补模态场景，实验数量充足。
- **充分性与公平性**：
  - 与大规模AutoML基线相比，CAMP在参数极少的情况下**匹配或超越**其性能，且经过**端到端微调后达到SOTA**，表明实验设计具有说服力。
  - 但原文未详细列出消融实验（如移除最优传输、几何约束的对比），也未提供统计显著性检验或超参数敏感性分析，因此**可能不够完全充分**。
  - 对比方法的选定（仅提及AutoML）可能不够全面，未与同等规模的可解释多模态方法进行直接比较。

## 6. 论文的主要结论与发现

- CAMP是**首个面向互补多模态任务的模态无关原型学习框架**。
- 通过最优传输对齐类别级证据和几何约束，能够**同时实现高精度和高可解释性**，打破了CMC中准确率-可解释性的权衡。
- 在16个数据集上，CAMP以**少于1M参数**匹配或超越大规模AutoML模型；端到端微调后达到**最优性能**。

## 7. 优点

- **方法创新**：将最优传输引入多模态原型对齐，专门针对互补模态场景，理论保证了消除模态主导和坍缩。
- **高效性**：参数极少（<1M），远超AutoML的百倍参数，训练和推理成本低。
- **可解释性**：原型对齐使得每个类别的多模态证据一致性可视化，提供清晰的决策理由。
- **模态无关**：设计通用，适用于X射线-病历、音频-文本等多种互补对。

## 8. 不足与局限

- **实验覆盖有限**：虽然在16个数据集上验证，但未提供数据集的具体名称和领域分布，可能偏向特定类型（如医学、多模态）。
- **消融实验缺失**：未系统评估最优传输、几何约束各自贡献，也未与简单基线（如直接拼接原型）对比。
- **对比方法不够广泛**：仅提到AutoML基线，未与同等参数规模的现代原型网络（如ProtoPNet、ProtoTree）比较。
- **资源信息不足**：未报告GPU型号、训练时间，难以复现或评估实际算力需求。
- **应用限制**：仅针对分类任务，未扩展到其他互补多模态任务（如回归、生成）；对模态缺失或噪声鲁棒性未分析。
- **偏差风险**：元数据中分数为7.0（ICML 2026 Accepted），可能存在评审偏好，实际部署效果需进一步验证。

（完）
