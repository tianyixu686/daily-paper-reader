---
title: "S2H-DPO: Hardness-Aware Preference Optimization for Vision–Language Models"
title_zh: S2H-DPO：面向视觉语言模型的难度感知偏好优化
authors: "Nitish Shukla, Surgan Jandial, Arun Ross"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.1825.pdf"
tags: ["query:post-multi"]
score: 8.0
evidence: 针对视觉语言模型对齐的偏好优化方法
tldr: 该论文针对视觉语言模型在多图像推理中对齐能力不足的问题，提出简单到难（S2H）偏好优化框架。系统构建三个层级的多图像偏好数据，逐步训练模型从单图像局部推理到多图像全局搜索与比较。实验证明该方法有效提升了跨图像推理能力，是对RLHF思路在多模态场景的扩展。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1825/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 784, \"height\": 479, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1825/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1642, \"height\": 828, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1825/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1489, \"height\": 827, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1825/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1476, \"height\": 504, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1825/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 486, \"height\": 363, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1825/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 801, \"height\": 736, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1825/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 802, \"height\": 609, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1825/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 799, \"height\": 410, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1825/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 722, \"height\": 202, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1825/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 722, \"height\": 211, \"label\": \"Table\"}]"
motivation: 现有VLM对齐方法仅关注单图像局部推理，缺乏多图像跨图比较能力。
method: 构建层级化多图像偏好数据，采用DPO进行从易到难训练。
result: 显著提升模型在多图像推理基准上的表现。
conclusion: 为VLM的多图像对齐提供有效框架。
---

## Abstract
Vision-Language Models (VLMs) have demonstrated remarkable progress in single-image understanding, yet effective reasoning across multiple images remains challenging. We identify a critical capability gap in existing multi-image alignment approaches: current methods focus primarily on localized reasoning with pre-specified image indices (“Look at Image 3 and...”), bypassing the essential skills of global visual search and autonomous cross-image comparison. To address this limitation, we introduce a Simple-to-Hard (S2H) learning framework that systematically constructs multi-image preference data across three hierarchical reasoning levels requiring an increasing level of capabilities: (1) single-image localized reasoning, (2) multi-image localized comparison, and (3) global visual search. Unlike prior work that relies on model-specific attributes, such as hallucinations or attention heuristics, to generate preference pairs, our approach leverages prompt-driven complexity to create chosen/rejected pairs that are applicable across different models. Through extensive evaluations on LLaVA and Qwen-VL models, we show that our diverse multi-image reasoning data significantly enhances multi-image reasoning performance, yielding significant improvements over baseline methods across benchmarks. Importantly, our approach maintains strong single-image reasoning performance while simultaneously strengthening multi-image understanding capabilities, thus advancing the state of the art for holistic visual preference alignment.

---

## 论文详细总结（自动生成）

# 论文结构化总结

## 1. 核心问题与整体含义（研究动机和背景）
- **问题**：当前视觉-语言模型（VLM）在多图像推理中表现不足，尤其是跨图像搜索和自主比较。现有对齐方法（如MIA-DPO）仅关注**局部化推理**（Level 1：预指定图像索引，例如“请回答图像2中的问题”），跳过了模型需要**自主决定关注哪些图像**的全局搜索能力（Level 3）以及**多图像比较**（Level 2）。
- **动机**：多图像推理能力是层次化的，不同难度需要不同的能力。仅训练Level 1无法泛化到更复杂的场景，且现有方法（如MIA-DPO）依赖模型特有的幻觉来生成偏好对，导致对新模型需要重新生成数据。作者希望提出一种**模型无关、难度层次化**的偏好优化框架，提升多图像推理能力而不牺牲单图像性能。

## 2. 方法论：核心思想、关键技术细节与流程
- **核心思想**：构建从简单到困难（Simple-to-Hard, S2H）的三个推理层级，分别生成对应的**选择-拒绝偏好对**，通过直接偏好优化（DPO）联合训练。
- **三个层级**：
  - **Level 1（单图像局部化）**：给定多张图像，但问题指定具体图像索引（类似MIA-DPO）。选择答案为目标图像的正确回答，拒绝答案为模型产生的错误回答（由幻觉引起）。
  - **Level 2（多图像局部化比较）**：问题涉及多张指定图像，需要比较或组合信息。包含两个子任务：
    - *亲属识别*：给定多张人脸图像，判断关系。根据标签确定性生成文本对（正确/错误陈述）。
    - *视觉算术*：合成图像，每个图像有物体计数，问题要求跨图求和/差等。确定性生成选择/拒绝对。
  - **Level 3（全局视觉搜索）**：问题不指定图像，要求模型在所有图像中找到满足语义约束的那一张（例如“描述含有孔雀的图像”）。生成方式：
    - 从ImageNet选取目标概念和图像，配以N-1张干扰图像（不同类）。
    - 用Qwen2.5-VL-32B生成目标图像的详细描述（**选择**），以及没有指定目标时的通用描述（**拒绝**）。
    - 使用文本编码器（CLIP, MPNet）过滤掉相似度过高的对（保留前四分位），确保对比信号清晰。
- **训练**：使用DPO损失函数，温度参数β=0.1，学习率5e-5，训练3个epoch。每个层级生成20K样本。模型：LLaVA-v1.5-7B、Qwen2.5-VL-7B、Qwen3-VL-2B。

## 3. 实验设计：数据集、基准与对比方法
- **多图像基准**：
  - BLINK（跨领域知识）
  - MANTIS（交错的视觉推理）
  - NLVR2（自然语言视觉推理）
- **单图像基准**（验证能力保持）：
  - MMStar
  - POPE（物体幻觉评估）
- **对比方法**：
  - 基线模型：LLaVA-v1.5-7B、Qwen2.5-VL-7B、Qwen3-VL-2B（原始或SFT后）
  - 偏好优化方法：LLaVA-RLHF、HA-DPO、POVID、MIA-DPO
  - 额外实验：GRPO（组相对策略优化）作为一种on-policy RL替代

## 4. 资源与算力
- 论文**未明确说明**使用的GPU型号、数量及训练时长。仅提及模型在三个层级各20K样本上训练3个epoch。对于小型模型（7B、2B），这通常可在单卡或少量GPU完成，但具体细节文中未提供。

## 5. 实验数量与充分性
- **主要实验**（表1、表2）：在三个多图像基准和两个单图像基准上，对比了多个基线，评估了三个模型（LLaVA-7B、Qwen2.5-VL-7B、Qwen3-VL-2B），共约30个结果行。
- **消融实验**（表3-5及图5）：
  - 课程学习 vs 直接训练（flat training）：发现flat训练优于从简单到复杂的课程学习，因为课程学习导致模型过度依赖局部化提示。
  - SFT vs DPO：DPO更优。
  - 干扰物数量（图5）：在2~5个图像中选择，3个干扰物效果最佳。
  - L3能力验证：在ImageNet验证集上构造500个L3问题，S2H-DPO准确率比基线提升6.94%。
  - 使用GRPO（表5）验证数据生成策略：GRPO在部分基准上更好但BLINK上下降，证明数据高质量但优化方法敏感。
- **充分性评价**：实验较充分，覆盖了多模型、多基准、多种消融和替代方法，公平对比了当前最先进的偏好优化方法。但缺少更大规模图像集（如>6张）或更多样化任务（如时间推理）的测试。

## 6. 主要结论与发现
- S2H-DPO在三个多图像基准上显著优于MIA-DPO及其他基线，且在单图像基准上保持或提升原有性能。
- 直接训练（flat training）比课程式逐步训练效果更好，原因在于课程训练鼓励模型关注局部化提示而非全局理解。
- DPO优于SFT，说明偏好信号比正向监督信号更强的学习指导。
- 三个干扰物是最优配置，过多干扰物引入噪声。
- S2H训练能有效提升Level 3（全局视觉搜索）能力。
- 方法可迁移到不同模型（LLaVA、Qwen2.5-VL、Qwen3-VL）且无需为每个模型重新生成数据。

## 7. 优点
- **模型无关性**：偏好对的生成不依赖模型特定属性（如幻觉），因此同一数据集可应用于多种VLM，无需重复生成。
- **系统性能力层次设计**：通过明确划分三个推理层级并选择代表性任务，覆盖了多图像推理的核心技能（局部化、比较、全局搜索）。
- **数据质量保证**：Level 3中使用语义过滤确保选择-拒绝对具有足够判别性，提高学习信号。
- **实验全面**：在多个模型、多个基准上均验证有效性，消融实验设计合理。

## 8. 不足与局限
- **依赖已有数据集与caption模型**：Level 3依赖于ImageNet标签和Qwen2.5-VL-32B生成caption，可能继承其偏见或误差。此偏差风险未被实验分析。
- **图像数量有限**：实验最多使用6张图像（包括干扰物），未测试更大规模（如20+）的多图像场景下的注意力与效率问题。
- **能力覆盖不全**：未涉及时序、因果推理或跨模态学习等更复杂的多图像推理模式。
- **优化方法敏感性**：针对相同数据，GRPO在部分基准上优于DPO但另一些下降，表明算法稳定性仍有改进空间，论文未深入分析原因。
- **算力资源未报告**：缺少训练所需硬件、时间等详细信息，影响可复现性评估。

（完）
