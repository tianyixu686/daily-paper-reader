---
title: Layer-Wise High-Impact Parameter Ratio Optimization in Post-Training Quantization for Large Language Models
title_zh: 大语言模型后训练量化中的层间高影响参数比例优化
authors: "Cuong Pham, Anh Dung Hoang, Cuong C. Nguyen, Trung Le, Gustavo Carneiro, Thanh-Toan Do"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.acl-long.2092.pdf"
tags: ["query:post-multi"]
score: 9.0
evidence: 大语言模型的后训练量化
tldr: 针对大语言模型后训练量化中固定比例保留高影响参数导致低比特精度损失的问题，提出基于二次优化的层间高影响参数比例分配框架，通过感知各层敏感度动态决定保留比例，在极低比特下有效保持模型精度。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.2092/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1656, \"height\": 547, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.2092/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1662, \"height\": 1188, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.2092/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1659, \"height\": 1475, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.2092/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1640, \"height\": 627, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2092/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1483, \"height\": 745, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2092/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1487, \"height\": 576, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2092/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1571, \"height\": 351, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2092/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1406, \"height\": 449, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2092/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 767, \"height\": 196, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2092/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 740, \"height\": 304, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2092/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 807, \"height\": 220, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2092/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1450, \"height\": 973, \"label\": \"Table\"}]"
motivation: 现有后训练量化方法在极低比特精度损失大，且固定保留比例忽略层间敏感性差异。
method: 提出二次优化框架，为每层动态分配高影响参数的保留比例。
result: 在多个LLM上实验，低比特下精度显著优于固定比例方法。
conclusion: 层间差异化比例分配是提升后训练量化效果的有效途径。
---

## Abstract
Large language models (LLMs) have advanced natural language processing, but their massive parameter counts create computational and memory challenges during deployment. Post-training quantization (PTQ) has emerged as a promising approach to mitigate these challenges. While existing PTQ methods can effectively quantize LLMs, they experience substantial accuracy loss at extremely low bit-widths due to high-impact parameters. Several approaches address this by retaining high-impact parameters in FP16 format, but they apply fixed ratios across all layers, overlooking layer-wise sensitivity variations. We propose a quadratic optimization framework that determines layer-specific ratios of high-impact parameters while considering inter-layer dependencies. We quantize high-impact parameters to moderate bit-widths while the remaining parameters are quantized to extremely low bit-widths. Under the same resource budget, this preserves more high-impact parameters than methods retaining a few in FP16 format. Our framework enables leveraging advanced quantization methods for high-impact parameters while applying lightweight computational quantization methods to the rest, achieving an effective balance between computational efficiency and accuracy during quantization process.

---

## 论文详细总结（自动生成）

# 详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）
大语言模型（LLMs）在部署时面临巨大的计算和内存挑战。后训练量化（PTQ）是缓解这些挑战的有效方法，但在极低比特宽度（如2-bit权重量化）下，由于存在“高影响参数”（high-impact parameters），现有PTQ方法会出现显著的性能损失。已有方法（如AWQ、CherryQ、SqueezeLLM）通过将少量高影响参数保留为FP16格式来缓解该问题，但它们对所有层采用**固定比例**保留高影响参数，忽略了不同层对量化敏感性的差异。论文作者通过实验（图1）发现，不同层的通道维度上Fisher信息分布差异显著，固定比例分配会导致次优的精度分配。因此，本文的核心问题是如何**动态确定每层高影响参数的最佳保留比例**，以在给定资源预算下最大化量化模型性能。

## 2. 论文提出的方法论：核心思想、关键技术细节
**核心思想**：通过**二次优化框架**，每层从一组候选高影响参数比例中选择最优比例，同时考虑层间依赖关系（仅在同一个transformer block内）。与将高影响参数保留为FP16不同，本文将这些参数量化到**中等比特宽度**（如3-bit或4-bit），从而在相同预算下保留更多高影响参数。其余普通参数则量化到极低比特宽度（如2-bit）。此外，采用**混合量化策略**：对高影响参数使用更先进的量化方法（如AdaRound），对普通参数使用轻量级量化方法（如OmniQuant中的可学习权值裁剪）。

**关键技术细节**：
- **参数影响度量**：使用Fisher信息矩阵的对角线近似Hessian矩阵，衡量每个参数对量化损失的敏感度，即高影响参数。
- **问题建模**：定义每层有|B|个候选比例（如{0.02,0.05,0.10,0.15,0.20}），用one-hot向量δ_l表示选择。将整体量化损失近似为δ^T M δ（M是依赖Hessian的矩阵），其中M的对角元素通过式(7)计算（单层量化损失），非对角元素通过式(8)计算（同block内两层联合量化损失，跨block近似为0）。
- **优化问题**：在总资源预算约束（总比特数≤C_target）和每层仅选一个比例的约束下，最小化δ^T M δ。这是一个二次整数规划问题。
- **混合量化执行**：根据优化得到的δ，将每层权重分为高影响组（比例由δ决定）和普通组。高影响组使用AdaRound（式11）进行可微四舍五入优化；普通组使用OmniQuant中的可学习权值裁剪（式13）。训练时通过块重建损失（block reconstruction loss）进行优化。

**算法流程**（Algorithm 1）：
1. 使用校准数据X(T)和全精度模型θ_FP。
2. 对每个层l和每个候选比例i，计算单层量化误差∆_l,i，进而计算M的对角元素（式7）。
3. 对同一block内的层对(l1,l2)及候选对(m1,m2)，计算联合量化误差，更新M的非对角元素（式8），跨block元素置0。
4. 求解二次规划问题得到最优比例向量δ。
5. 返回δ，用于后续混合量化。

## 3. 实验设计
- **数据集与场景**：
  - **校准数据集**：从WikiText-2随机采样128条序列，每条2048个token。
  - **语言建模评估**：WikiText-2和C4数据集上的困惑度（PPL）。
  - **下游零样本任务**：HellaSwag、PIQA、WinoGrande、ARC-easy、ARC-challenge的准确率。
- **基准模型**：LLaMA-2-7B、LLaMA-2-13B（另在附录中补充OPT-125M）。
- **对比方法**：GPTQ、AWQ、SqueezeLLM、CBQ、OmniQuant。结果直接引用或复现自原作者论文。
- **设置**：权重仅量化（weight-only），激活保留FP16。评估不同位宽（W2A16、W3A16）及组大小（无分组、g128、g64）。

## 4. 资源与算力
论文提到：**所有实验在NVIDIA A100 GPU上运行**。具体GPU数量、训练总时长未明确说明。对于高影响参数的AdaRound优化，迭代5000次，学习率1e-3；整体量化流程在校准小数据集（128样本）上进行，计算开销可接受。

## 5. 实验数量与充分性
实验相对充分，包括：
- **主要结果**：表1（2-bit）、表2（3-bit）在LLaMA-2-7B/13B上给出WikiText-2和C4的PPL，与OmniQuant、CBQ等比较。
- **下游任务**：表3给出5个零样本任务准确率，与GPTQ、OmniQuant对比。
- **消融实验**：表4详细分析了固定比例 vs 优化比例、是否使用混合量化、以及结合两者，验证了各组件贡献。
- **附录补充**：表A.1对候选比例集B的敏感性分析；表A.2对OPT-125M的额外结果；表A.3不同校准数据集的稳定性；表A.4不同高影响位宽（3/4/16）在相同预算下的对比。图A.1、A.2可视化Fisher信息分布和优化后的比例。
- **公平性**：与多个SOTA方法在相同设置下比较，指标标准（PPL、准确率）。但未报告统计显著性（如置信区间），且部分对比结果来自原文引用而非完全复现，可能存在实现细节差异。

## 6. 论文的主要结论与发现
- 本文提出的**层间动态比例优化**框架显著优于固定比例方法，在极低比特（W2A16）下困惑度从37.37（OmniQuant）降至9.40，平均准确率提升约2.4%（消融表4）。
- **混合量化策略**（高影响参数用AdaRound，其余用轻量量化）进一步提升了性能，结合优化比例后效果最佳。
- 在3-bit设置下，方法接近全精度模型（差距约4%），验证了其有效性。
- 层间依赖性只存在于同一block内，简化了优化复杂度（时间复杂度O(B L_b (L_b-1))，B为block数）。

## 7. 优点
- **新颖性**：首次将二次整数规划用于确定每层高影响参数保留比例，而非固定比例，符合各层敏感性差异的观察。
- **理论支撑**：基于二阶泰勒展开和Fisher信息度量，推导出易于计算的损失变化近似。
- **效率与性能平衡**：仅对少量高影响参数使用昂贵的AdaRound，其余使用轻量量法，计算资源分配合理。
- **硬件友好**：采用通道级（channel-wise）而非元素级划分，支持标准均匀量化，利于硬件部署。
- **实验全面**：覆盖多种模型大小、位宽、组大小、下游任务及充分消融。

## 8. 不足与局限
- **手工设定候选高影响位宽**：需要预先指定高影响参数的量位宽度（如对于2-bit目标，b_H设为3），论文承认这可能不是最优，未来可动态调整。
- **校准数据依赖**：使用128条来自WikiText-2的数据，虽在附录中验证了跨数据集稳定性，但仍可能对特定领域泛化有影响。
- **未进行多轮重复实验**：未报告标准偏差或置信区间，结果可靠性略有减弱。
- **对比基线复现问题**：部分对比结果来自原始论文，而非统一复现，可能存在实现差异。
- **模型规模限制**：实验仅涉及7B/13B/125M，未在更大模型（如70B）上验证，通用性待检验。
- **应用限制**：混合量化策略中AdaRound需迭代优化，在校准数据上需一定额外计算时间，但整体仍具实际可行性。

（完）
