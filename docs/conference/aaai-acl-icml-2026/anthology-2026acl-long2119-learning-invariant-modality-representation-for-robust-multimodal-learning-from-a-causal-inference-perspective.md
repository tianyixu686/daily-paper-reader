---
title: Learning Invariant Modality Representation for Robust Multimodal Learning from a Causal Inference Perspective
title_zh: 基于因果推断视角的鲁棒多模态学习不变模态表示学习
authors: "Sijie Mai, Shiqin Han"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.acl-long.2119.pdf"
tags: ["query:post-multi"]
score: 9.0
evidence: 通过因果不变表示实现鲁棒多模态学习
tldr: 本文提出基于因果推断的多模态不变表示学习框架CmIR，用于鲁棒多模态情感计算。该方法从因果视角将每个模态分解为因果不变表示和环境特定伪相关表示，确保学习到的表示在分布偏移下保持稳定预测关系。实验表明该方法在情感识别等任务上显著提升了泛化能力。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.2119/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 766, \"height\": 291, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.2119/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 775, \"height\": 310, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.2119/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1573, \"height\": 581, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.2119/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 803, \"height\": 349, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.2119/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1625, \"height\": 331, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.2119/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 796, \"height\": 386, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.2119/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 800, \"height\": 618, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2119/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 819, \"height\": 328, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2119/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 783, \"height\": 329, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2119/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1594, \"height\": 406, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2119/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1522, \"height\": 582, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2119/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 660, \"height\": 326, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2119/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 806, \"height\": 296, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2119/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1598, \"height\": 430, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2119/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1598, \"height\": 202, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2119/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1201, \"height\": 135, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2119/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1660, \"height\": 229, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2119/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1208, \"height\": 223, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2119/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1209, \"height\": 212, \"label\": \"Table\"}]"
motivation: 多模态模型常学到模态间的伪相关，导致在分布偏移下泛化能力差，需要鲁棒的因果不变表示。
method: 提出因果模态不变表示学习框架，通过理论驱动的解耦方法分离每个模态的因果不变特征和伪相关特征。
result: 在多个多模态情感计算数据集上，该方法在分布偏移和噪声条件下取得了优于现有方法的鲁棒性能。
conclusion: 该工作为鲁棒多模态学习提供了因果视角的新范式，有助于提升多模态系统的泛化可靠性。
---

## Abstract
Multimodal affective computing aims to predict humans’ sentiment, emotion, intention, and opinion using language, acoustic, and visual modalities. However, current models often learn spurious correlations that harm generalization under distribution shifts or noisy modalities. To address this, we propose a causal modality-invariant representation (CmIR) learning framework for robust multimodal learning. At its core, we introduce a theoretically grounded disentanglement method that separates each modality into ‘causal invariant representation’ and ‘environment-specific spurious representation’ from a causal inference perspective. CmIR ensures that the learned invariant representations retain stable predictive relationships with labels across different environments while preserving sufficient information from the raw inputs via invariance constraint, mutual information constraint, and reconstruction constraint. Experiments across multiple multimodal benchmarks demonstrate that CmIR achieves state-of-the-art performance. CmIR particularly excels on out-of-distribution data and noisy data, confirming its robustness and generalizability.

---

## 论文详细总结（自动生成）

好的，以下是对论文《Learning Invariant Modality Representation for Robust Multimodal Learning from a Causal Inference Perspective》的详细中文总结。

---

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：多模态情感计算（MAC）模型常从训练数据中学习到模态间的伪相关（spurious correlations），而非真正的因果关系。这导致模型在遇到分布偏移（distribution shift）或模态噪声时，泛化能力严重下降。例如，模型可能过度依赖说话者始终微笑（视觉伪相关）来预测正面情感，当测试集出现微笑但表达负面内容的情况时，模型会出错。
- **整体含义**：本文旨在从因果推断的视角出发，通过学习跨环境稳定的因果不变表示（invariant representations），来提升多模态模型的鲁棒性和泛化能力，使其在真实场景中面对环境变化时仍能可靠工作。这是一种不依赖特定偏见先验知识的一般性框架。

### 2. 论文提出的方法论

- **核心思想**：提出 **CmIR（Causal modality-Invariant Representation）** 框架，从因果视角将每个模态的特征解耦为两个互补的部分：
    1.  **因果不变表示（$Z_{inv}^{m}$）**：包含与标签$Y$有稳定因果关系的特征，跨环境保持不变。
    2.  **环境特异性伪相关表示（$Z_{spu}^{m}$）**：捕获与环境相关的、非因果的噪声，与标签无因果联系。
- **关键技术细节**：通过一个联合优化的目标函数实现解耦，包含三个核心约束：
    1.  **不变性约束（$R_{inv}^{(m)}$）**：通过向原始特征注入不同强度的噪声来模拟多个虚拟环境，然后强制不同环境下得到的$Z_{inv}^{m}$尽量一致（使用L1距离），从而保证$Z_{inv}^{m}$对环境不敏感。
    2.  **互信息约束（$R_{dec}^{(m)}$）**：最小化$Z_{inv}^{m}$和$Z_{spu}^{m}$之间的互信息，促进两者解耦。实现中采用特征正交化的方式作为近似，迫使两者学习正交方向的表示。
    3.  **重构约束（$R_{rec}^{(m)}$）**：通过解码器从$(Z_{inv}^{m}, Z_{spu}^{m})$重构原始输入$X_m$（使用MSE损失），确保解耦后的表示保留了原始输入的完整信息，防止信息丢失。
- **预测与优化**：最终的任务预测仅使用融合后的多模态因果不变表示$\{Z_{inv}^{m}\}$。总损失为预测损失与上述三项约束的加权和：$L = L_{pred} + \sum_m (\lambda_1 R_{inv}^{(m)} + \lambda_2 R_{dec}^{(m)} + \lambda_3 R_{rec}^{(m)})$。

### 3. 实验设计

- **使用的数据集与场景**：
    - **多模态情感分析（MSA）**：CMU-MOSI、CMU-MOSEI、CH-SIMS-v2（中文）。
    - **多模态幽默检测（MHD）**：UR-FUNNY。
    - **多模态讽刺检测（MSD）**：MUStARD。
    - **分布偏移（OOD）**：CMU-MOSI (OOD)（一个经过特殊构造、存在显著词-情感相关偏移的测试集）。
    - **噪声模态**：在CMU-MOSI和CMU-MOSEI上加入高斯噪声（10%-70%）以及未见的噪声类型（拉普拉斯噪声、随机擦除噪声）进行评估。
- **基准（Benchmark）与对比方法**：
    - **标准MSA**：对比了Self-MM, FDMER, SuCI（因果方法）, C-MIB, ITHP, Diffusion Bridge, GSCon等十余种方法。
    - **MHD/MSD**：对比了MulT, Self-MM, HKT, DMD, DMD+SuCI, AtCAF, MCL, MGCL, ITHP, MIL等。
    - **OOD场景**：对比了CLUE, GEAR, MulDeF等专门处理OOD的因果方法以及ITHP, Self-MM等。
    - **噪声实验**：对比了TMDC, C-MIB, Multimodal Boosting。

### 4. 资源与算力

- 论文在“F Experimental Details”中明确说明：实验使用 **PyTorch 1.13.1**，在 **NVIDIA RTX3090 GPU**（CUDA 11.6）上运行。优化器为 **AdamW**。
- **未明确说明训练时长**：论文未报告每个实验或完整训练所需的具体时间、GPU数量或总训练时长，只提及通过随机搜索50次确定超参数。

### 5. 实验数量与充分性

- **实验数量丰富**：论文进行了大量实验，涵盖：
    - 4个标准评测（MSA×3, MHD×1, MSD×1）。
    - 1个OOD评测。
    - 2组噪声鲁棒性评测（高斯噪声、混合未见噪声）。
    - 全面的消融实验（移除每个约束项）。
    - 超参数敏感性分析（λ1, λ2, λ3, 环境数K, 噪声强度α(1)）。
    - 模型复杂度对比（参数量和FLOPs）。
    - 探针实验（Probing Experiment）验证$Z_{inv}$和$Z_{spu}$的语义分离。
    - 显著性检验（t-test vs ITHP）。
    - 不同不变性约束实现的对比。
- **实验充分性与公平性**：
    - **充分**：各方面验证了方法的有效性和鲁棒性。
    - **客观**：遵循了公开的评测协议（如统一特征集、多次运行取平均等），并公开了代码。
    - **公平**：所有对比方法在相同设置下重现或引用原始结果。噪声实验采用统一的协议。整体实验设计严谨，结论可信。

### 6. 论文的主要结论与发现

- **方法有效性**：CmIR在多个多模态情感计算任务上达到了最先进的（SOTA）性能，显著优于包括现有因果方法在内的强基线。
- **鲁棒性显著**：在OOD数据和各种噪声条件下，CmIR的性能优势更加突出，证明了其学习因果不变表示抵抗分布偏移和噪声的能力。例如，在CMU-MOSI (OOD)上，Acc2比ITHP提升3.5%，Acc7提升7.2%。
- **每个约束的必要性**：消融实验证实，三个约束（不变性、互信息、重构）缺一不可，移除任何一个都会导致性能下降，其中不变性约束最为关键。
- **理论支撑**：论文提供了三个定理，从理论上证明了不变表示的存在性、可提取性以及在OOD最坏情况风险上的优势。

### 7. 优点

- **方法创新性强**：首次系统地提出将每个模态解耦为因果不变和伪相关两部分，并提供了完整的信息论和因果推断理论支撑，而非针对特定偏好的经验性方法。
- **理论贡献扎实**：三个定理从定义、可提取性和泛化风险上提供了严格的数学证明，提升了工作的科学严谨性。
- **实验全面深入**：覆盖多种任务、OOD和噪声场景，并进行了丰富的消融、探针和敏感性分析，验证充分。
- **鲁棒性突出**：在更具挑战性的分布偏移和噪声条件下，性能提升尤为显著，展示了极大的实际应用潜力。
- **模型复杂度可控**：复杂度分析表明，CmIR在取得更好性能的同时，其模型参数量和计算量（FLOPs）能与现有先进方法持平甚至更低，效率高。

### 8. 不足与局限

- **环境模拟的局限性**：通过向特征注入噪声来模拟环境变化，虽然有效，但可能无法完美捕获真实世界中复杂、多样的分布偏移（如说话风格、背景变化等）。更真实的跨环境数据集或更精细的环境生成策略值得探索。
- **近似的互信息约束**：使用特征正交化作为互信息最小化的代理，是一种近似手段，可能不如直接估计互信息精确。更精确的估计方法（如变分下界）可能会带来更好的解耦效果，但会增加计算成本。
- **对超参数的依赖**：虽然进行了敏感性分析，但模型性能仍然依赖于多个超参数（λ1, λ2, λ3, K, α(1)）的调优，需要一定的调试成本。
- **应用限制**：方法假设不同环境的数据存在，并依赖构造的虚拟环境标签。在环境信息完全缺失或环境划分不合理的场景下，性能可能会受到影响。

（完）
