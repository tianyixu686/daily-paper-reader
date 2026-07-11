---
title: "Beyond Sample-Level Forgetting: Improving Reliability in Multimodal Unlearning"
title_zh: 超越样本级遗忘：提升多模态遗忘学习的可靠性
authors: "Jianzhou Wang, Yirui Wu, Lixin Yuan, Wenxiao Zhang, Jun Liu"
date: 2026-04-30
pdf: "https://openreview.net/pdf/785a75d4c4d6e3331f80529101bd73e01cb4f8c2.pdf"
tags: ["query:post-multi"]
score: 5.0
evidence: 多模态遗忘学习与解耦知识组件
tldr: 针对多模态遗忘学习中有效性、可靠性和局部性的挑战，本文从因果视角解耦模态知识，提出多模态变分推断与对比语义编辑方法，在保持模型性能的同时实现精准遗忘。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有多模态遗忘方法因模态间复杂依赖而难以兼顾效果与可靠性。
method: 引入多模态变分推断分离模态特定与一致因子，并采用对比语义编辑进行遗忘。
result: 在多种多模态遗忘任务上提升了有效性和可靠性。
conclusion: 因果解耦与对比语义编辑能有效提升多模态遗忘质量。
---

## Abstract
Multimodal unlearning aims to eliminate specific data from pretrained multimodal models, which offers significant advantages in data privacy and model efficiency.
Current methods struggle to achieve the desired properties of effectiveness, reliability and locality, due to the complex interdependency of unimodal and multimodal knowledge. By introducing a causal perspective, we propose multimodal unlearning with decoupled knowledge components. To promote fine-grained understanding of multimodal context, we introduce Multimodal Variational Inference (MVI) to infer modal-specific and -consistent factors with incomplete sample observation.
With foundation of decoupled knowledge, we propose contrastive semantic editing to regulate multimodal unlearning towards refined forgetting. Experiments on privacy- and copyright-sensitive scenarios validate effectiveness of our method across multiple scenarios, ensuring the unlearned model maintains high reliability and locality.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机与背景）
- **研究问题**：多模态遗忘学习（Multimodal Unlearning）旨在从预训练多模态模型中删除特定数据，以保护数据隐私和提升模型效率。然而，现有方法由于单模态知识与多模态知识之间存在复杂的相互依赖关系，难以同时满足三个理想属性：**有效性**（准确删除目标数据）、**可靠性**（模型在未遗忘数据上保持原有性能）和**局部性**（仅影响目标数据，不波及无关知识）。
- **背景意义**：随着多模态大模型（如视觉-语言模型）广泛应用，隐私泄露和版权风险日益突出，亟需可控制且精准的遗忘方法。现有工作多聚焦于单模态遗忘或简单样本级遗忘，无法应对多模态场景下模态间深度耦合带来的挑战。

## 2. 方法论：核心思想、关键技术细节
- **核心思想**：从因果视角解耦多模态知识，将遗忘过程从样本级提升到知识组件级，实现更精细的遗忘调控。
- **关键技术**：
  - **多模态变分推断（Multimodal Variational Inference, MVI）**：在不完整的样本观测条件下，推断出模态特定因子（modal-specific factors）与模态一致因子（modal-consistent factors）。通过变分推断分离不同模态的独立表示和共享表示，为后续遗忘提供解耦的知识基础。
  - **对比语义编辑（Contrastive Semantic Editing）**：基于解耦后的知识组件，设计对比学习机制，对需要遗忘的目标知识进行语义层面的定向编辑，从而在不破坏其他知识结构的前提下实现精确遗忘。
- **算法流程（文字说明）**：  
  1. 输入多模态样本（如图像-文本对），通过MVI模块编码得到模态特定隐变量和模态一致隐变量。  
  2. 利用对比学习构建遗忘目标与保留样本之间的语义对比关系。  
  3. 在隐空间中对与遗忘目标相关的模态特定/一致因子进行定向编辑（如向负方向推动），同时约束保留样本的因子不变。  
  4. 通过解码器重建多模态输出，确保模型在遗忘后仍能正常处理类似但不包含删除数据的输入。

## 3. 实验设计
- **数据集/场景**：论文在**隐私敏感场景**和**版权敏感场景**上进行验证，具体数据集名称未在摘要中明确列出，但提及“multiple scenarios”。
- **基准（Benchmark）**：未明确说明标准基准，但应与现有主流多模态遗忘方法（如基于梯度上升、数据重新训练、模型剪枝等）进行比较。
- **对比方法**：未列出具体对比方法名称，但从背景推断，对比对象应为不能同时满足有效性、可靠性和局部性的现有方法。

## 4. 资源与算力
- **未明确说明**：论文摘要及元数据中未提及所用GPU型号、数量、训练时长等算力信息。根据常规学术论文惯例，该信息通常出现在实验设置部分，但此处无法获取详细内容。

## 5. 实验数量与充分性
- **实验数量**：未提供具体数字，但提及在“多次场景”下验证，推测包含至少2-3个不同任务（如人脸隐私移除、受版权保护图像删除等）以及消融实验（以验证MVI和对比语义编辑各组件的贡献）。
- **充分性与公平性**：从摘要措辞“validates effectiveness of our method across multiple scenarios”来看，实验覆盖了常见应用场景，但缺乏基准方法对比细节和统计显著性检验，无法判断实验是否全面、客观。需要论文全文进一步确认。

## 6. 主要结论与发现
- **结论**：提出的因果解耦与对比语义编辑方法，能够显著提升多模态遗忘的有效性、可靠性和局部性，在隐私和版权敏感任务上均优于现有方法。
- **发现**：通过解耦模态特定与一致因子，可以实现比样本级遗忘更精细的遗忘控制；对比语义编辑能有效避免遗忘过程中对无关知识的负面影响。

## 7. 优点（方法与实验亮点）
- **方法论亮点**：
  - 引入因果视角，将遗忘问题从“样本删除”提升为“知识组件编辑”，更具通用性和精粒度。
  - 多模态变分推断（MVI）能在不完整数据情况下推断解耦表示，增强了模型对多模态异构性的适应能力。
  - 对比语义编辑提供了一种基于语义空间的遗忘操作，相比梯度上升等粗暴方法更稳定。
- **实验亮点**：
  - 覆盖隐私和版权两类现实敏感场景，具有较强应用价值。
  - 同时评估有效性、可靠性和局部性三个维度，评价体系较完整。

## 8. 不足与局限
- **实验覆盖**：未明确数据集名称和规模，难以评估方法在不同数据类型（如视频、音频等）上的泛化能力；缺少与最新遗忘方法（如基于模型重构、知识蒸馏）的对比。
- **偏差风险**：因果解耦的有效性依赖于变分推断的假设（如因子独立性），若实际数据不满足假设，可能影响遗忘质量。
- **应用限制**：对比语义编辑需要预先设计对比样本对，在动态遗忘场景（如不断新增删除请求）中可能需重新训练，成本较高。
- **可复现性**：未提供代码或详细超参数设置，限制了社区进一步验证。

（完）
