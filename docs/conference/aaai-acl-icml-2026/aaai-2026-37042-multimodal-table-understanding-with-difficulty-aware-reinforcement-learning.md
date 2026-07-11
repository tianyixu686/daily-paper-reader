---
title: Multimodal Table Understanding with Difficulty-aware Reinforcement Learning
title_zh: 基于难度感知强化学习的多模态表格理解
authors: "Chaohu Liu, Haoyu Cao, YongXiang Hua, Linli Xu"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/37042/41004"
tags: ["query:post-multi"]
score: 8.0
evidence: 使用强化学习进行多模态学习微调
tldr: 该论文针对多模态大模型在复杂表格理解中的性能退化问题，提出MM-Table-R1模型，通过难度感知的强化学习来增强模型对复杂表格结构的感知与推理能力。实验表明，该方法在多种表格理解任务上显著提升了准确性，尤其在高度结构化的表格上效果明显，为多模态表格理解提供了新的训练范式。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: 多模态大模型在表格复杂度增加时性能显著下降，暴露出对复杂表格结构的感知和推理能力不足。
method: 提出难度感知强化学习框架MM-Table-R1，根据表格结构复杂度动态调整奖励信号以优化模型。
result: 在多个表格理解基准上，该方法显著提升了模型性能，尤其在复杂表格上改善明显。
conclusion: 难度感知的强化学习能有效增强多模态模型对复杂表格的理解能力。
---

## Abstract
Multimodal table understanding, which aims for a comprehensive grasp of table content by integrating cellular text, tabular structure, and visual presentation, remains a core yet challenging area of research.
We identify that the structural complexity of a table, quantifiable by intrinsic properties such as the ratio of merged cells and the total number of cells, presents a significant obstacle for existing models. 
Our empirical analysis reveals that the performance of leading Multimodal Large Language Models (MLLMs) deteriorates markedly as table complexity increases, exposing a critical vulnerability in their ability to perceive and reason over intricate tabular data.
To address this challenge, we propose MM-Table-R1, a model enhanced through difficulty-aware reinforcement learning (RL) post-training strategy. 
Specifically, we introduce both task-level and data-level curriculum learning. 
The task-level curriculum is designed to establish a capability ladder, where the model first learns basic perceptual and semantic alignment of table data, and then progresses to acquiring multi-step reasoning capabilities.
The data-level curriculum ensures that the model is not exposed to difficult samples prematurely, facilitating a more gradual and effective learning process.
Furthermore, we invest considerable effort in constructing a high-quality, large-scale training corpus by curating and processing data from diverse open-source table datasets, ensuring that each instance is paired with an objectively verifiable reward signal.
Demonstrating exceptional parameter efficiency, our 3B-parameter model sets a new benchmark by surpassing both established 3B and 7B models, including those specifically designed for table reasoning.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究动机**：多模态表格理解（MTU）旨在整合单元格文本、表格结构及视觉呈现（如字体、颜色、对齐）来全面理解表格内容。然而，现有多模态大语言模型（MLLMs）在处理结构复杂表格时性能显著下降。作者通过量化表格复杂度（合并单元格比例和单元格总数），实证发现Qwen2.5-VL在WTQ和HiTab基准上的准确率随表格复杂度增加而急剧恶化，暴露出模型在视-结构感知方面的脆弱性。
- **整体含义**：为解决这一问题，论文提出**MM-Table-R1**，一个基于难度感知强化学习（RL）后训练策略的模型，旨在通过课程学习让模型先学会基本表格感知，再进阶到多步推理，从而有效应对复杂表格带来的挑战。

### 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：采用**难度感知的强化学习**，结合**任务级课程学习**和**数据级课程学习**，使训练过程更加稳定高效。
- **关键技术细节**：
  - **任务级课程学习**分两阶段：
    - **阶段1（表格感知）**：通过表格重建任务（使用HTML格式）训练模型理解空间布局、合并单元格逻辑等。使用**表格验证奖励**（Table Verification Reward, \( R_{tr} \)）：按单元格正确率加权（考虑合并单元格面积）计算奖励。
    - **阶段2（表格推理）**：采用GRPO算法，引导模型输出包含<think>标签的推理过程及\boxed{}格式的最终答案。奖励由格式奖励（\( R_{format} \)）和准确率奖励（\( R_{acc} \)）组成。
  - **数据级课程学习**：根据样本难度（合并单元格比例、单元格总数对数、模型当前失败率）排序，从易到难训练，并过滤掉所有回答都正确的过简单样本。
  - **难度定义**：\( D = R + \alpha \log(N) + F \)，其中\( R \)为合并单元格比例，\( N \)为理论最大单元格数，\( F \)为模型失败率，\( \alpha \)为超参数（默认0.5）。
- **公式/算法流程**：
  - 表格复杂度度量：合并单元格比例 \( R = 1 - L/N \)，单元格总数 \( N = \sum_i m_i \cdot n_i \)（\( m_i, n_i \)为行、列跨距）。
  - GRPO目标函数：\( J_{GRPO}(\theta) = E[ \frac{1}{G} \sum \min(r_i(\theta)A_i, \text{clip}(r_i(\theta), 1-\epsilon, 1+\epsilon)A_i) - \beta D_{KL}(\pi_\theta\|\pi_{\text{ref}}) ] \)。
  - 表格重建奖励：\( R_{tr} = \frac{\sum I(\hat{c}_i=c_i \land \hat{m}_i=m_i \land \hat{n}_i=n_i) \cdot m_i n_i}{N} \)。

### 3. 实验设计：数据集、评估基准与对比方法

- **数据集**：训练数据来自TabMWP、WTQ、HiTab、TAT-QA、FeTaQA、TabFact、InfoTabs、ToTTo等公开数据集，经HTML格式转换、图像渲染、问答对分离（FeTaQA使用DeepSeek-V3处理）构建。
- **评估基准**：覆盖8个表格理解基准：TabMWP、WTQ、HiTab、TAT-QA、FeTaQA（问答任务）、TabFact、InfoTabs（事实核查任务）、ToTTo（表格重建任务）。此外还使用TableVQA-Bench进行零样本评估。
- **对比方法**：包括通用MLLMs（Qwen2.5-VL-3B/7B、InternVL-2.5-8B、MiniCPM-V-2.6-8B、Ovis2-8B）和专注表格的模型（Table-LLaVA-7B、TabPedia-7B、HIPPO-8B、SynTab-LLaVA-7B、Turbo-8B等）。

### 4. 资源与算力

- 论文明确提到了训练设置：batch size=256，每个阶段训练2个epoch，使用AdamW优化器（学习率1e-6，权重衰减1e-2），每条提示采样8个候选响应，最大响应长度2000，KL惩罚项β=0.01。
- **未明确说明**使用的GPU型号、数量及训练总时长，因此无法给出具体算力消耗数据。

### 5. 实验数量与充分性

- **实验数量**：在主表（Table 1）中比较了8个基准上的性能；Table 2为零样本评估（4个子集）；Table 3为消融实验（不同训练策略）；Figure 4为数据级课程学习消融（包括无课程、无过滤、单指标及α敏感性）。
- **充分性与客观性**：
  - 涵盖问答、事实核查、表格重建多种任务，包括合成与真实场景。
  - 对比方法包括通用模型和专门为表格设计的模型，且使用公开基准以保证公平。
  - 消融实验覆盖了SFT、单独阶段、替换SFT、随机顺序、无简单样本过滤、不同难度指标等，验证了各组件的必要性。
  - 不足：对Turbo和SynTab-LLaVA因未开源而无法完全对齐评估；未报告所有方法的置信区间或统计显著性检验。

### 6. 论文的主要结论与发现

- 表格的结构复杂度（合并单元格比例和单元格总数）是导致MLLMs性能下降的关键因素。
- 提出的**难度感知强化学习**（任务级+数据级课程学习）能显著提升模型对复杂表格的处理能力。
- MM-Table-R1-3B在全部8个基准上均达到新SOTA，超越了包括Turbo-8B在内的参数量更大的模型，展示了优秀的参数效率。
- 零样本评估也取得领先，说明模型具有良好的泛化能力。
- 消融实验证实：RL比SFT更适合训练表格感知能力；两阶段课程学习优于任单一阶段；数据级课程学习比随机训练或不过滤策略更有效。

### 7. 优点

- **创新性**：首次系统量化表格结构复杂度对MLLMs的影响，并设计难度感知课程学习解决该问题。
- **方法设计巧妙**：任务级课程将感知与推理解耦，数据级课程自适应调整训练顺序，两者结合使RL训练稳定高效。
- **参数效率高**：3B模型超越7B甚至8B专用模型，表明方法可大幅降低计算成本。
- **数据构建细致**：从多个公开数据集构建含可验证奖励的大规模训练语料，并针对FeTaQA等进行了问答对分离处理。
- **实验充分**：覆盖多种任务、多个对比方法及大量消融实验，结论可靠。

### 8. 不足与局限

- **算力未公开**：未提供GPU型号、数量、训练时长，不利于复现和成本评估。
- **有限的数据多样性**：训练数据主要来自公开基准，可能无法涵盖实际工业场景中更复杂的表格布局（如手写表格、不规则合并）。
- **对比不完整**：Turbo和SynTab-LLaVA因未开源，评估基准可能不完全一致；未与更多近期的大模型（如DeepSeek-VL系列）对比。
- **单指标评估**：主要使用准确率，未报告其他指标（如F1、BLEU、ROUGE），尤其对于表格重建任务，仅用细胞级准确率可能忽略格式正确性。
- **未分析失败案例**：虽指出复杂表格导致性能下降，但未定性分析模型在哪些具体结构上犯错（如多层嵌套合并、多列标题等）。
- **应用限制**：模型基于Qwen2.5-VL-3B，若部署到更低资源场景（如手机端）或需要实时推理，可能仍需进一步优化。

（完）
