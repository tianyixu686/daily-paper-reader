---
title: "From Selection to Refinement: Iterative Optimization for Instruction Data"
title_zh: 从筛选到精炼：指令数据的迭代优化
authors: "Hang Hu, Ziyan Liu, Rujie Wen, Ruihui Hou, Xueyan Wu, Mu Zhang, Jianxing Yu, Tong Ruan, Jingping Liu"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.acl-long.1889.pdf"
tags: ["query:post-multi"]
score: 8.0
evidence: 指令数据的迭代优化框架
tldr: 针对指令微调数据集优化中粗筛丢失有价值数据及修订引入噪声的问题，本文提出自动化迭代框架，先进行质量区分，再对低质量数据执行“评估-修正-反馈”循环，显著提升指令微调效果。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1889/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 804, \"height\": 664, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1889/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1653, \"height\": 1013, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1889/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 807, \"height\": 710, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1889/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 788, \"height\": 915, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1889/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 759, \"height\": 722, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1889/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 777, \"height\": 709, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1889/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1653, \"height\": 1156, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1889/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1646, \"height\": 349, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1889/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1647, \"height\": 352, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1889/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1659, \"height\": 390, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1889/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1654, \"height\": 543, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1889/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 801, \"height\": 664, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1889/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1599, \"height\": 273, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1889/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1662, \"height\": 751, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1889/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1651, \"height\": 276, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1889/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1623, \"height\": 408, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1889/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1617, \"height\": 316, \"label\": \"Table\"}]"
motivation: 现有指令数据优化方法存在不合理裁剪与修订噪声问题。
method: 提出指令质量区分与反馈驱动的迭代精炼机制。
result: 在多个指令微调基准上提升模型性能。
conclusion: 迭代质量区分与精炼能有效优化指令数据。
---

## Abstract
Instruction tuning plays a crucial role in enhancing large language models (LLMs) to better understand complex user instructions. While various data selection and revision methods have been explored to optimize instruction tuning datasets, they face two main challenges: unreasonable pruning of potentially valuable low-quality data and the persistence of noise or semantic drift during revision. To address these issues, we propose a novel automated iterative framework for instruction data optimization. Our framework introduces Instruction Quality Differentiation to identify valuable high-quality and low-quality data across multiple dimensions. For low-quality data, we propose a Feedback-driven Iterative Refinement mechanism with an "evaluate-refine-review" process and design an Output Alignment module to improve data quality. Experiments on seven public benchmark datasets show that our framework outperforms state-of-the-art methods, achieving 2.09% and 2.60% improvements on the Alpaca and Dolly datasets, respectively, with high data efficiency. Our code and data are available at the anonymous link https://github.com/surihuhang/From-Selection-to-Refinement–Iterative-Optimization-for-Instruction-Data.

---

## 论文详细总结（自动生成）

# 论文总结

## 1. 核心问题与整体含义（研究动机和背景）

指令微调（Instruction Tuning）是提升大语言模型（LLMs）理解复杂用户指令能力的关键技术。高质量指令数据是有效微调的前提，但现有数据优化方法面临两大挑战：

- **不合理裁剪**：数据选择方法（如基于质量、多样性或难度的筛选）会丢弃潜在有价值但存在缺陷的数据，导致数据浪费。
- **修订噪声与语义漂移**：数据修订方法（如规则填充、教师模型蒸馏、偏好引导修订）常采用“单次重写”策略，无法充分修正错误，反而可能引入噪声和语义漂移。

因此，论文提出一种自动化的迭代框架，通过先区分高/低质量数据，再对低质量数据进行反馈驱动的迭代精炼，从而在保留高质量数据的同时，有效修复低质量样本，提升指令微调的整体效果。

## 2. 方法论

### 核心思想
构建“分选→精炼→对齐”的自动化流水线：先对原始指令数据进行多维度质量区分，识别出有价值的高质量数据和需要修复的低质量数据；然后对低质量数据执行“评估-修正-审查”（evaluate-refine-review）的迭代循环，并结合输出对齐模块，确保修正后指令-输入-输出的语义一致性。

### 关键技术细节

#### （1）指令质量区分（Instruction Quality Differentiation, IQD）
- **专家引导的样本标注**：利用强LLM（Llama3.1-70B）设计提示词，判断样本是否包含推理步骤，并依据正确性、完整性、清晰度、指令一致性、逻辑推理五个维度分配初始质量标签（高/低）。
- **聚类与难度感知评分**：为避免单一LLM偏好偏差，使用K-means聚类将样本按语义相似性分组；在每个簇内计算IFD分数（衡量指令难度），然后按初始标签和IFD排名，选择Top-K样本作为高质量数据，其余归为低质量数据。

#### （2）反馈驱动的迭代精炼（Feedback-driven Iterative Refinement, FIR）
- 对于每个低质量样本，先用LLM生成对原指令-输入对的响应`out_p1`。
- **评估专家**：比较`out_p1`与原输出`out`，识别差异并生成详细反馈（如模糊指令、缺失信息）。
- **修正专家**：基于反馈及原始样本，修正指令和输入，得到新对`(Ins_new, in_new)`。
- **审查专家**：比较原始对+`out_p1`与新对+新响应`out_p2`，若新对更优则接受，否则保留原对，并将失败反馈累积到反馈集，引导下一轮迭代。迭代上限设为3轮（实验确定最优）。

#### （3）输出对齐（Output Alignment, OA）
- 对修正后的指令-输入对，利用LLM识别关键关键词，根据关键词精炼原始输出，确保输出与修正后的指令-输入在语义和逻辑上一致。

最终将优化后的低质量数据与高质量数据合并，形成最终训练集。

### 算法流程（文字说明）
1. 原始数据`D_raw`通过IQD模块分为`D_high_raw`和`D_low_raw`。
2. 对`D_low_raw`中每个样本，执行最多T轮的FIR循环，得到优化后的指令-输入对。
3. 通过OA模块，将优化后的指令-输入对与原输出对齐，得到新输出。
4. 合并`D_high_raw`和优化后的低质量样本，得到最终数据集`D_opt`。
5. 用`D_opt`微调LLM，在多个下游任务上评估。

## 3. 实验设计

### 数据集
- **训练数据集**：Alpaca（52K GPT-3生成的样本）、Dolly（15K人工编写样本）。优化后分别生成35K和12K高质量样本。
- **基准测试**：7个公开数据集，覆盖三类任务：
  - 知识理解：C-Eval、ARC
  - 数学与代码：HumanEval、GSM8K、GPQA
  - 知识推理：TriviaQA、Winogrande

### 对比方法
- **数据选择**：IFD、ALPAGASUS、NUGGETS、Superfiltering、MoDS
- **数据修订**：WizardLM、DoAug、CoachLM

### 评估指标
准确率（C-Eval、ARC、GSM8K、TriviaQA、Winogrande）、Pass@1（HumanEval）、平均Pass@1（GPQA）。

### 实现细节
- 所有专家模型：Llama3.1-70B-Instruct（默认，除IQD标注外）；默认微调骨干：Llama3.1-8B-Instruct。
- 微调超参：初始学习率1e-6，cosine衰减，warm-up比例0.1，3个epoch，推理温度0.7，top-p=0.1。

## 4. 资源与算力

论文在附录F中提供了详细的资源统计。以Alpaca数据集（52K样本）为例，运行环境为三块NVIDIA A100 GPU（80GB）。

- IQD模块：初始标签标注使用2×A100（<10min），聚类与难度评分使用1×A100（<20min）。
- FIR模块：专家评估使用3×A100（<20min），指令输入修正使用2×A100（每轮约20min，共3轮<60min），专家审查使用3×A100。
- OA模块：输出修正使用2×A100（<25min）。
- 完整流水线总耗时约135分钟。

因此，该框架离线处理效率较高，但迭代过程消耗较多计算资源。

## 5. 实验数量与充分性

论文进行了多组实验，包括：
- 在两个数据集（Alpaca、Dolly）上与8种基线方法对比的主实验结果（表1）。
- 主模块消融实验（表2）：依次去除IQD、FIR、OA模块。
- IQD子维度消融实验（表3）：去除初始质量标签、多样性、难度维度。
- 迭代轮次敏感性分析（表4）：T=1~5。
- 不同骨干模型泛化性实验（表5）：Llama3.1-8B、Mistral-7B-v0.3、Qwen2.5-7B/14B/32B。
- 人类评估：随机抽取200样本进行盲比（图3）。
- 指令跟随能力评估（附录表7）：IFEval、AlpacaEval。
- 超参数敏感性分析（附录表8）：聚类数C和高质量占比K。
- 数据统计分析（附录）：困惑度、文本长度、语义多样性。
- 计算效率与成本分析（附录表10、11）。

实验覆盖了主流基线、多种模型架构、多个维度的消融和参数分析，且结果经过三次运行取平均，具有较好的统计可靠性。实验设计较为充分、客观。

## 6. 主要结论与发现

1. **框架有效性**：提出的迭代优化框架在Alpaca和Dolly上均超越所有基线，平均性能分别提升2.09%和2.60%，且数据量更少（35K vs 70K，12K vs 59K），数据效率高。
2. **各模块均贡献**：消融实验显示去除任何模块都会导致性能下降，其中OA对代码任务影响最大，FIR对数学推理影响最大，IQD防止无效数据引入。
3. **迭代轮次最优为3**：T=3时性能最佳，更多轮次因过度编辑导致下降。
4. **跨模型泛化性强**：在Llama3.1、Mistral、Qwen2.5系列（7B~32B）上均一致提升。
5. **质量提升明显**：人类评估表明优化后数据在指令-输入和输出上均有显著改善。

## 7. 优点

- **方法创新**：将数据选择与迭代修订有机结合，先区分后精炼，避免了单次重写和盲目裁剪。
- **多维度质量区分**：综合专家标注、语义聚类和难度评估，提高区分可靠性。
- **反馈驱动的迭代“评估-修正-审查”机制**：模拟人类评审流程，逐步修正错误，减少语义漂移。
- **输出对齐模块**：确保修正后的指令-输入与输出逻辑一致，对代码等需精确对齐的任务提升显著。
- **数据效率高**：用更少数据达到更优性能，降低训练成本。
- **实验全面**：涵盖多种基线、模型架构、消融分析、人类评估和超参数敏感性，结论可靠。

## 8. 不足与局限

- **计算开销**：迭代过程（尤其FIR模块）需要多次调用强大LLM（70B），离线处理时间较长（约2小时处理52K样本），相比单次修订方法更耗资源。
- **迭代轮次选择依赖经验**：最优轮次T=3通过实验确定，不同数据集可能需重新调优，缺乏理论指导。
- **对强教师模型依赖**：质量区分和修订均依赖Llama3.1-70B作为专家，若更换较弱教师可能影响效果；且未充分讨论专家模型偏差。
- **实验场景有限**：仅在Alpaca和Dolly两个数据集上验证，且骨干模型多为7B~32B，未覆盖更大模型（如70B+）或更多样化的指令数据集（如代码、数学专项）。
- **未与其他更强基线对比**：如Star-Agents仅在相关工作中提到，主实验未包含，可能不是近期最新SOTA。
- **应用限制**：框架设计为离线优化，不适合在线或实时场景；且对硬件要求较高（多块A100 GPU）。

（完）
