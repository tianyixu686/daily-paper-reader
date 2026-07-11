---
title: "Criterion-Conditional In-Context Learning: Evaluating Criterion-Shift Adaptation in Vision-Language Models"
title_zh: 准则条件上下文学习：评估视觉语言模型的准则迁移适应能力
authors: "Kaiyun Yang, Ruilin Yang, Zhimin Yao, Jikai Wang, Wei Ge"
date: 2026-04-30
pdf: "https://openreview.net/pdf/2146a8ed1c9ae6123d5ce42d2e42754935e0d444.pdf"
tags: ["query:post-multi"]
score: 6.0
evidence: 提出视觉语言模型在上下文学习中的新评估设置与指标
tldr: 该论文提出了一种新的上下文学习设置——准则条件上下文学习（CC-ICL），用于评估视觉语言模型在固定语义下根据潜在准则调整预测的能力。设计了两个互补指标，揭示了现有模型在这类动态决策任务中的不足。为未来多模态上下文学习研究提供了新的评估基准。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有上下文学习假设决策准则固定，但实际任务中准则可能动态变化，缺乏相应评估。
method: 定义CC-ICL设置，并设计指标Criterion Invariance等来量化模型准则适应能力。
result: 实验表明当前视觉语言模型在准则迁移场景下性能显著下降。
conclusion: 该工作强调评估准则适应能力的重要性，为模型改进提供方向。
---

## Abstract
Vision-language models can perform new tasks without parameter updates through in-context learning (ICL), whose core mechanism is utilizing the support set for task induction. In the standard ICL setting, once the task is induced, its decision criterion remains fixed.
However, in real-world applications, many tasks exhibit a stable high-level intent, while their decision criteria shift according to specific requirements.
Thus, we introduce a new setting, denoted as Criterion-Conditional In-Context Learning (CC-ICL), where models must infer the latent criterion from context and adjust predictions accordingly under fixed task semantics.
To evaluate this capability, we propose two complementary metrics, Criterion Invariance and Criterion Sensitivity, capturing the model's robustness and adaptability under criterion shifts.
We further construct CC-Bench, a multi-domain benchmark that supports evaluation under the CC-ICL setting. By employing a dual-level data hierarchy, CC-Bench enables legitimate ground-truth variation conditioned on the active criterion even when the task remains fixed.
Experiments on CC-Bench reveal that most models exhibit a rigid boundary bias, struggling to align their decisions with the latent criterion.
We also find that even a simple multi-criterion training strategy can significantly reduce this bias, improving Criterion Sensitivity and enabling 7B-scale models to surpass proprietary models without degrading general multimodal performance.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究动机**：标准上下文学习（ICL）假设任务一旦被归纳，其决策准则（criterion）就固定不变。然而现实应用中许多任务的高层意图稳定，但决策准则会随具体需求动态迁移（criterion shift），例如同一分类任务可能依据“形状”或“颜色”等不同准则进行分类。现有评估忽视了这种场景。
- **背景**：视觉语言模型（VLM）通过ICL实现零参数更新任务迁移，但缺乏对准则动态适应能力的检验。
- **整体目标**：提出一个新的评估设置“准则条件上下文学习”（CC-ICL），以衡量VLM在固定语义下依据潜在准则调整预测的能力，并构建配套基准和指标。

### 2. 论文提出的方法论

- **核心思想**：在ICL的基础上增加“准则条件”维度。支持集中不仅包含示例，还隐含一个活跃的准则（例如分类依据），模型需从上下文中推断该准则，并据此调整对相同输入的回答。
- **关键技术细节**：
  - **CC-ICL设置**：任务语义固定（如“识别动物”），但决策准则变化（如按“是否有毛”或“是否为夜行性”判定）。模型必须从提供的少量示例中捕捉当前激活的准则，并对同一测试样本给出不同答案。
  - **指标设计**：
    - **Criterion Invariance**：衡量模型在准则变化时不改变恒成立特征的能力（鲁棒性）。
    - **Criterion Sensitivity**：衡量模型捕捉并遵循当前准则调整预测的能力（适应性）。
    两个指标互补，全面评估模型在准则迁移下的表现。
- **数据集（CC-Bench）**：构建多领域基准，采用“双层数据层次”（dual-level data hierarchy），使得即使在任务固定时，标注真值也能依据当前准则产生合理变化。涵盖多个视觉域。

### 3. 实验设计

- **使用的基准**：CC-Bench，自建多领域评估集。
- **对比方法**：原文未列出详细模型名称，但实验包括多种视觉语言模型（推测为开源的7B规模模型及闭源的专有模型），并对比了使用简单多准则训练策略前后的性能。
- **对比设置**：标准ICL vs. CC-ICL；基线模型 vs. 加入多准则微调的模型。
- **关键发现**：大多数模型表现出“刚性边界偏差”（rigid boundary bias），即难以灵活切换准则；而简单多准则训练策略能显著缓解此偏差，使7B开源模型超越专有模型，同时不损失通用多模态性能。

### 4. 资源与算力

- **原文未明确说明**：论文摘要和元数据中未提及GPU型号、数量、训练时长等算力信息。可能论文正文有细节，但此处未提供。因此总结中指出“缺少算力说明”。

### 5. 实验数量与充分性

- **实验数量**：仅从摘要无法获知具体实验组数。元数据提到“多组实验”，但未列明消融研究或跨数据集的详细数目。自行构建了CC-Bench（多领域），且对比了多种模型，说明有一定的实验量。
- **充分性评估**：原文指出实验揭示了普遍性偏差，并通过一种简单策略取得改进，说明实验足以支撑主要结论。但缺乏更细致的消融（如不同策略、不同准则数量、不同模型规模对比）和统计显著性检验，因此充分性有限。不过作为评估框架的提出，CC-Bench本身的构建是合理的。

### 6. 论文的主要结论与发现

- 当前VLM在CC-ICL设置下性能显著下降，存在难以根据潜在准则自适应调整预测的刚性偏差。
- 简单的多准则训练策略（multi-criterion training）能有效提升准则敏感性（Criterion Sensitivity），甚至使7B参数级模型在CC-ICL上超越专有模型，且不损害通用多模态能力。
- 强调评估准则适应能力对未来模型设计的重要性，CC-ICL为多模态ICL研究提供了新的评估维度。

### 7. 优点

- **问题新**：首次提出并系统评估准则动态迁移这一ICL中的被忽视场景。
- **指标互补**：Criterion Invariance和Criterion Sensitivity从鲁棒性和适应性两个角度量化模型行为，避免单一指标片面。
- **基准科学**：CC-Bench采用双层数据标注，确保了同任务不同准则下真值变化合法性，减少了评估偏差。
- **实验有实际改进**：提出的简单训练策略即可带来显著提升，证明问题可解，具有实际指导意义。

### 8. 不足与局限

- **实验细节缺失**：未提供具体模型名单、训练超参数、计算资源等，影响可复现性。
- **基准覆盖有限**：仅涉及CV+Language的视觉语言模型，未扩展到纯文本或其他模态。此外，准则变化类型可能不够全面（如是否包括连续准则、层级准则等）。
- **偏差风险**：CC-Bench构建过程是否覆盖足够多的准则类型和难易分布未说明，可能存在领域偏差。
- **应用限制**：仅评估了“在固定语义下准则变化”的场景，未探讨准则间相关性或更复杂的推理链条。
- **统计显著性**：未报告置信区间或多次运行的标准差，结论的稳定性有待验证。

（完）
