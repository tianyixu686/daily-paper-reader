---
title: "GIFT: Guided Fine-Tuning and Transfer for Enhancing Instruction-Tuned Language Models"
title_zh: GIFT：用于增强指令微调语言模型的引导式微调与迁移
authors: "Zhiwen Ruan, Yichao Du, Jianjie Zheng, Longyue Wang, Yun Chen, Peng Li, Jinsong Su, Yang Liu, Guanhua Chen"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.acl-long.358.pdf"
tags: ["query:post-multi"]
score: 9.0
evidence: 针对指令微调语言模型的微调与迁移方法
tldr: 该论文针对指令微调模型在适配下游任务时直接微调会破坏平衡的问题，提出引导式微调与迁移框架GIFT。在预训练基座上微调低秩适配器，同时利用指令微调模型提供的令牌级置信度信号作为指导。实验表明GIFT能更高效地适配下游任务，且保持原始指令跟随能力。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.358/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1449, \"height\": 582, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.358/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1655, \"height\": 526, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.358/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 722, \"height\": 419, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.358/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1325, \"height\": 1031, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.358/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 797, \"height\": 250, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.358/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1332, \"height\": 254, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.358/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 719, \"height\": 414, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.358/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 641, \"height\": 237, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.358/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 799, \"height\": 379, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.358/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 767, \"height\": 170, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.358/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1325, \"height\": 994, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.358/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1316, \"height\": 212, \"label\": \"Table\"}]"
motivation: 直接微调指令微调模型会破坏其通用指令跟随能力，现有适配器方法将模型视为被动目标。
method: 在基座模型上微调低秩适配器，并利用指令微调模型的置信度信号提供指导。
result: 在多种下游任务上实现更优的迁移效果，保持指令跟随泛化性。
conclusion: 提供了一种兼顾任务适配与通用能力的微调方案。
---

## Abstract
Instruction-tuned large language models (LLMs) exhibit strong instruction-following and generalization abilities, enabled by expensive post-training pipelines. However, adapting them to specific downstream tasks remains challenging: direct fine-tuning often disrupts this delicate balance, while existing adapter-based transfer methods typically treat the instruction-tuned model as a passive target that only participates at the final merging stage. We propose GIFT (Guided Fine-Tuning and Transfer), a simple and efficient framework that incorporates instruction-level guidance into task adaptation. GIFT fine-tunes a low-rank adapter on the pretrained base model using token-level confidence signals derived from the instruction-tuned model. The learned adapter is then merged into the instruction-tuned model, yielding task-specialized models that preserve general instruction-following behavior. We evaluate GIFT on mathematical reasoning and knowledge-intensive benchmarks across multiple model families and scales. Results show that GIFT consistently outperforms direct fine-tuning and representative transfer-based baselines, while maintaining robust generalization and favorable test-time scaling behavior.

---

## 论文详细总结（自动生成）

# 论文中文总结

## 1. 核心问题与整体含义（研究动机和背景）

指令微调（instruction-tuned）的大语言模型（LLMs）通过昂贵的后训练流程获得了强大的指令跟随和零样本泛化能力，但其参数在通用推理、指令遵循和鲁棒性之间保持着微妙的平衡。直接对指令微调模型进行下游任务微调容易破坏这种平衡，导致性能不稳定或退化。现有方法（如 Shadow-FT、Chat Vector）通过在预训练基座上学习任务特定更新，再合并到指令模型中，但这些方法将指令模型视为仅参与最终合并的被动目标，而未在训练过程中提供指导。本文提出 **GIFT（Guided Fine-Tuning and Transfer）**，让指令模型在任务适配阶段发挥更积极的作用。

## 2. 方法论：核心思想、关键技术细节

### 核心思想
在预训练基座模型上微调低秩适配器（LoRA）时，利用指令微调模型产生的令牌级置信度信号作为指导权重，重新分配优化信号：抑制低置信度令牌的更新，强调高置信度令牌，从而学习与指令模型更兼容的任务特定更新。最后将适配器合并回指令模型。

### 关键技术细节
- **离线标注**：对训练集每个样本的每个目标令牌，单次前向传播指令模型得到置信度 \( q_t = p_{\theta_I}(y_t | x, y_{<t}) \)。
- **引导微调损失**：结合置信度的交叉熵损失：
  \[
  \mathcal{L}_{\text{GIFT}}(\phi) = \mathbb{E}_{(x,y)\sim D} \left[ \sum_{t=1}^{T} q_t \cdot (-\log p_{\theta_B,\phi}(y_t | x, y_{<t})) \right]
  \]
  \( q_t \) 直接作为权重，不额外归一化或缩放。
- **合并阶段**：直接将训练好的适配器参数合并到指令模型：\( \theta'_I = \theta_I + M(\phi^*) \)。
- 与知识蒸馏不同，GIFT 不最小化教师与学生分布间的散度，仅使用标量权重重加权标准交叉熵。

## 3. 实验设计

- **任务与数据集**：
  - **数学推理**：训练集为 NuminaMath-CoT 的 2000 样本，评估集包括 Math500、Minerva Math、OlympiadBench、AIME 2024、AMC 2023。
  - **知识密集型（医疗QA）**：训练集为 MedMCQA 的 10000 样本，评估集包括 MedQA、MMLU-medical、MedMCQA 测试集。
  - 额外测试：Super-NaturalInstructions 的摘要类任务（8个任务，800样本）。
- **模型**：Llama3.1-8B、Llama3.2-3B、Qwen2.5-7B、DeepSeek-Math-7B 及其对应的指令版本；扩展实验包括 Qwen2.5 全系列（0.5B-32B）和 Qwen3-8B。
- **对比方法**：
  - 原始指令模型（Instruct Model）
  - 直接微调指令模型（Instruct-SFT）
  - Shadow-FT / Chat Vector（基座微调后合并）
  - Re-Adapt / Task Arithmetic（线性组合基座、指令偏移、任务参数）
  - LoRE-Adapt（低秩版本 Re-Adapt）
  - 消融中还包括 GIFT-BaseT（用基座模型作教师）
- **评价指标**：数学任务使用 Average@16（16次随机解码平均准确率），医疗QA使用多项选择准确率。

## 4. 资源与算力

论文仅在离线标注的计算开销中明确提到：使用单张 RTX 4090 24GB GPU，批大小1，对2000条 NuminaMath-CoT 样本进行标注耗时约2分11秒，峰值显存小于22GB，结果文件约11.91MB。对于训练阶段（LoRA 微调）的训练算力（GPU型号、数量、时长）未作明确说明。实验部分提到所有方法使用相同的 LoRA 配置（全局批大小256、1个epoch等），但未报告具体硬件和训练时间。因此资源细节不够完整。

## 5. 实验数量与充分性

论文进行了丰富且系统的实验，包括：
- **主实验**：4种模型 × 5个数学基准 + 1个模型 × 3个医疗基准，共约23组结果。
- **消融实验**：在 Qwen2.5-7B 上对比 SFT+Merge、GIFT-BaseT、GIFT，明确隔离了教师信号的作用。
- **测试时缩放分析**：在 Llama3.1-8B 上展示 Pass@N（N从1到10）曲线。
- **通用能力评估**：在 MMLU 和 IFEval 上检测指令跟随和知识覆盖。
- **指令任务泛化**：Super-NaturalInstructions 摘要任务。
- **模型规模缩放**：Qwen2.5 系列 0.5B 到 32B。
- **附加实验**：Qwen3-8B 数学结果、置信度令牌分析、难度层面分析等。

这些实验覆盖了多模型族、多规模、多任务类型，消融和对比充分，控制变量做得好（相同LoRA参数、解码条件），实验设计公平客观。不足在于缺乏与更多最新方法的比较（如更先进的合并策略 TIES、DARE 虽被提及但未纳入主要基线对比），以及缺乏真实世界场景的评估。

## 6. 主要结论与发现

- GIFT 在所有模型、任务上一致优于直接微调、Shadow-FT、Re-Adapt 等基线。在数学基准上平均提升1.6～5.2个百分点，医疗QA提升6.2个百分点。
- GIFT 在强基线 Qwen2.5-7B-Instruct 上仍能继续提升，而 Shadow-FT 在此模型上效果有限。
- GIFT 的增益来源于指令模型提供的置信度信号，而非简单的重加权（消融中 GIFT-BaseT 无显著提升）。
- GIFT 在测试时扩展（Pass@N）中表现更优，采样越多优势越稳定。
- 合并 GIFT 适配器后，通用知识（MMLU）和指令跟随（IFEval）能力几乎不变或略有提升，说明未破坏原有能力。
- 模型规模越大，GIFT 增益仍保持，不随容量增大而消失。
- 训练信号分析显示 GIFT 将梯度从低置信度令牌重新分配给高置信度令牌，更聚焦于任务关键结构。

## 7. 优点

- **方法简洁高效**：仅需一次离线标注，不改变标准 LoRA 训练流程，易于集成。
- **通用性强**：在数学推理、医疗QA、指令跟随等多任务上有效，跨模型族、规模均有效。
- **保持原有能力**：合并后不损害通用知识和指令跟随，解决了微调指令模型的一大痛点。
- **实验充分且规范**：控制变量严格，多角度分析（消融、缩放、信号分布）支撑结论可靠性。
- **资源友好**：离线标注成本低，训练与标准 LoRA 相同，无需额外内存。

## 8. 不足与局限

- **离线标注开销**：尽管轻量，但对超大规模数据集仍会引入预处理时间，论文未探讨在线近似方法。
- **实验资源信息不充分**：训练阶段的具体GPU和耗时未报告，影响可复现性评估。
- **基线覆盖有限**：未与 TIES-Merging、DARE 等先进的合并技术结合（论文指出可互补，但未实验量化）。
- **任务范围**：主要集中在数学和医疗两个领域，缺乏对多轮对话、代码生成等场景的验证。
- **置信度信号源**：仅使用一个指令模型，未研究教师模型质量、不同温度缩放等对结果的影响。
- **潜在偏差**：置信度高并不总意味着令牌正确或关键，指令模型可能对某些模式过度自信，引入噪声风险。

（完）
