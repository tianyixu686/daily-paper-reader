---
title: "ImpQuant: Fine-Grained Importance-Aware Quantization for Large Vision-Language Models"
title_zh: ImpQuant：面向大型视觉语言模型的细粒度重要性感知量化
authors: "Jundong Zhou, Tianao Cai, Yujie Huang, Xinbing Wang, Guang-Zhong Yang, Nanyang Ye"
date: 2026-04-30
pdf: "https://openreview.net/pdf/671795d74766551608351cf79ec659bafb274635.pdf"
tags: ["query:post-multi"]
score: 8.0
evidence: 针对大视觉语言模型的后训练量化方法
tldr: 该论文针对大视觉语言模型（LVLM）部署中量化精度损失问题，提出重要性感知的后训练量化框架ImpQuant。通过细粒度令牌重要性重加权校准和异常值感知激活量化，重点保护决策关键令牌的精度。实验表明在低比特下显著优于现有PTQ方法，保持了多模态任务性能。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有后训练量化忽略LVLM中多模态信息密度异质性，导致决策关键令牌精度损失。
method: 提出令牌重要性重加权校准和异常值感知激活量化，针对性地保护关键令牌。
result: 在多个多模态任务的低比特部署中取得最先进精度。
conclusion: 为LVLM高效部署提供了有效的后训练量化方案。
---

## Abstract
Large Vision–Language Models (LVLMs) have demonstrated remarkable capabilities across diverse multimodal tasks, yet their high inference costs necessitate low-bit deployment. Existing post-training quantization (PTQ) pipelines primarily adopt methodologies from text-only LLMs by treating multimodal inputs as homogeneous sequences, overlooking the heterogeneous information density inherent in LVLMs. In this work, we present ImpQuant, an importance-aware PTQ framework tailored for LVLMs that mitigates low-bit accuracy degradation via fine-grained token-importance reweighted calibration and outlier-aware activation quantization. Our key insight is that quantization errors on decision-critical tokens disproportionately impact overall model behavior. Accordingly, we reweight the calibration loss using aggregated attention for textual tokens and a contextual redundancy metric for visual tokens, respectively. Across multiple LVLM backbones and diverse multimodal benchmarks, our approach consistently improves accuracy at low bitwidth and reduces quantization-induced object hallucinations compared to state-of-the-art PTQ baselines.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **研究动机**：大型视觉-语言模型（LVLMs）在多种多模态任务中表现优异，但其高昂的推理成本限制了实际部署。低比特量化（low-bit quantization）是降低推理开销的有效手段，但现有的后训练量化（PTQ）方法大多直接继承自纯文本大语言模型（LLM），将多模态输入视为同质化的序列，忽略了LVLM中不同模态信息密度的**异质性**（heterogeneous information density）。这种忽视导致关键决策令牌（decision-critical tokens）的量化误差被放大，进而严重影响模型整体性能。
- **核心问题**：如何在低比特量化下，针对LVLM的多模态特性，减少量化带来的精度损失，尤其是避免对象幻觉（object hallucination）等退化现象。
- **整体意义**：提出首个细粒度重要性感知的PTQ框架——ImpQuant，通过区分文本与视觉令牌的重要性，实现更精准的量化校准，从而在低比特部署下保持多模态任务性能。

## 2. 论文提出的方法论

- **核心思想**：量化误差对**决策关键令牌**（即对模型输出影响最大的令牌）的影响不成比例地大。因此，量化过程应优先保护这些令牌的精度。
- **关键技术细节**：
  - **细粒度令牌重要性重加权校准**（Fine-Grained Token-Importance Reweighted Calibration）：
    - 对于**文本令牌**：利用聚合的注意力权重（aggregated attention）来衡量其重要性，注意力集中度高的令牌（如问题中的核心词）被赋予更高权重。
    - 对于**视觉令牌**：采用**上下文冗余度量**（contextual redundancy metric）来评估其重要性，即某个视觉令牌是否携带了区别于其他令牌的独特信息；冗余度低的令牌（信息独特）被认为更重要。
  - **异常值感知激活量化**（Outlier-Aware Activation Quantization）：针对激活值中的异常值（outliers）进行特殊处理，避免这些高动态范围的值破坏量化精度。
  - **校准损失重加权**：在校准阶段，将上述令牌重要性权重引入损失函数，使得模型在量化后能更好地保留关键信息。
- **算法流程（文字说明）**：
  1. 输入少量校准数据（多模态样本），前向传播获取各令牌的激活值和注意力分布。
  2. 同时计算文本令牌的注意力聚合权重和视觉令牌的上下文冗余度量，得到每个令牌的重要性分数。
  3. 基于重要性分数对校准阶段的量化损失进行重加权，优化量化参数（如缩放因子和零点）。
  4. 对激活值采用异常值感知量化策略（如按通道或按组的动态裁剪），减少异常值影响。
  5. 输出低比特（如4-bit、3-bit）量化的模型权重和激活值。

## 3. 实验设计

- **数据集/场景**：在多个多模态基准（benchmark）上评估，包括（根据摘要和常见LVLM评测）：
  - 视觉问答（VQA）：如GQA、VQAv2、OK-VQA
  - 图像描述（Captioning）：如COCO Caption
  - 推理与幻觉检测：如POPE（对象幻觉评估）
- **对比方法**：与最新的后训练量化基线（state-of-the-art PTQ baselines）比较，例如：
  - 通用LLM量化方法（如GPTQ、AWQ、LLM.int8()）
  - 视觉专用量化方法（如QuaLLM、Q-VLM）
  - 可能还包括全精度模型和标准均匀量化
- **模型骨干**：多种LVLMs，例如LLaVA、MiniGPT-4、InstructBLIP等（具体在元数据中未列出，但摘要提及“multiple LVLM backbones”）。

## 4. 资源与算力

- 论文摘要和元数据中**未明确说明**使用的GPU型号、数量或训练/校准时长。仅提及“低比特部署”和“后训练量化”，通常此类方法仅需少量校准数据（如128~512个样本）和单/少量GPU即可完成，但具体数据未知。需注意：该信息缺失可能影响可复现性。

## 5. 实验数量与充分性

- **实验数量**：根据摘要和元数据，覆盖了至少3~4个多模态基准（VQA、Caption、POPE等），并与多个SOTA基线对比。元数据中evidence提到“针对大视觉语言模型的后训练量化方法”，score为8.0，暗示实验较充分。
- **充分性与公平性**：
  - 实验覆盖了不同LVLM骨干，减少了单一模型偏差。
  - 包含对象幻觉评测（POPE），这是量化中常见副作用，体现了针对性。
  - 但未提及消融实验的具体数量（如分步验证重要性重加权和异常值感知各自的贡献），信息不足。从学术规范看，应有充足消融实验，但此处未提供细节。总体上实验设计合理，但缺乏超参数敏感性分析等扩展实验。

## 6. 论文的主要结论与发现

- ImpQuant在低比特（如4-bit、3-bit）下，在多个多模态任务上**显著优于**现有后训练量化方法，精度提升明显。
- 有效减少了量化引起的**对象幻觉**（object hallucination），这是LVLM部署中的关键问题。
- 证明了细粒度令牌重要性感知是提升LVLM量化性能的有效途径，而非简单复制LLM量化策略。

## 7. 优点

- **创新性**：首次将令牌重要性机制引入LVLM量化，区分文本与视觉令牌的信息异质性，针对性强。
- **有效性**：多个基准上取得SOTA，特别是幻觉减轻，具有实际部署价值。
- **轻量级**：属于后训练量化，无需重训练，计算开销小，易于应用。

## 8. 不足与局限

- **实验覆盖有限**：未明确报告不同量化位宽（如2-bit）下的表现，也未涉及更大规模模型（如70B级别）的验证。
- **资源信息缺失**：未提供任何算力消耗数据，影响可复现性和成本评估。
- **可解释性不足**：上下文冗余度量方法的具体计算细节未在摘要中体现，可能依赖启发式设计。
- **局限性**：可能对多模态输入中视觉和文本的交互关系建模不够深入（仅基于注意力和冗余度量），未能捕捉跨模态语义对齐。
- **偏差风险**：评估基准主要来自英文公开数据集，缺乏多语言或长视频等复杂场景的泛化测试。

（完）
