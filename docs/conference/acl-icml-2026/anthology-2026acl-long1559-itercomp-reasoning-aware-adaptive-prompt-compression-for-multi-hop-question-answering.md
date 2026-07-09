---
title: "IterCOMP: Reasoning-aware Adaptive Prompt Compression for Multi-hop Question Answering"
title_zh: IterCOMP：面向多跳问答的推理感知自适应提示压缩
authors: "JungMin Yun, Youngbin Kim"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.acl-long.1559.pdf"
tags: ["query:mr"]
score: 8.0
evidence: 面向多跳问答的推理感知提示压缩
tldr: 多跳问答中检索增强生成系统常因长而嘈杂的上下文降低效率和准确性。现有提示压缩方法针对单轮查询，无法捕捉推理步骤间依赖。本文提出IterCOMP，将多跳推理融入迭代压缩循环，通过分解文档、评估可回答性和生成后续问题逐步整合关键证据。实验显示IterCOMP在多个多跳QA基准上显著提升准确率并降低推理成本。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1559/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 767, \"height\": 451, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1559/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1625, \"height\": 632, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1559/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 789, \"height\": 535, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1559/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 802, \"height\": 228, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1559/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 802, \"height\": 233, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1559/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1568, \"height\": 655, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1559/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 719, \"height\": 236, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1559/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 798, \"height\": 417, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1559/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 795, \"height\": 316, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1559/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 796, \"height\": 284, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1559/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1407, \"height\": 668, \"label\": \"Table\"}]"
motivation: 现有提示压缩方法忽略多跳推理步骤间依赖，导致噪声累积和效率低下。
method: 提出IterCOMP框架，在迭代压缩循环中融入多跳推理，分解文档并生成后续问题逐步整合证据。
result: 在多个多跳QA数据集上，IterCOMP显著提升RAG系统的准确率并减少推理延迟。
conclusion: 推理感知的提示压缩能有效提升多跳QA中RAG系统的效率和可靠性。
---

## Abstract
Multi-hop question answering requires complex reasoning across multiple evidence segments, which often overwhelms retrieval-augmented generation systems with lengthy and noisy contexts, thereby undermining both efficiency and accuracy. While existing prompt compression methods attempt to address this issue, they are typically designed for single-turn queries and fail to capture interdependent reasoning steps. We propose IterCOMP, a unified, training-free prompt compression framework that incorporates multi-hop reasoning within an iterative compression loop. IterCOMP decomposes documents into evidence segments, evaluates question answerability, and generates targeted follow-up questions to iteratively integrate essential evidence, producing a compact, reasoning-oriented prompt. Experiments on MusiQue, 2WikiMultiHopQA, and HotpotQA demonstrate that IterCOMP achieves substantial improvements in Exact Match and F1 scores while reducing the token budget, outperforming existing baselines and exhibiting robustness as reasoning complexity increases.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **研究动机**：多跳问答要求模型跨多个证据片段进行复杂推理，而检索增强生成系统在提供大量检索文档时，往往因上下文过长、包含噪声而降低效率和准确性。现有提示压缩方法多针对单轮查询设计，无法捕捉多跳推理步骤间的依赖关系，导致信息丢失或错误累积。
- **背景**：检索增强生成（RAG）虽能引入外部知识，但长输入带来高延迟、高成本以及“迷失在中间”的位置偏差。多跳问答中，中间推理线索往往隐含在初始问题中，单次查询难以覆盖全部所需证据。因此，需要一种能够动态、迭代地压缩和整合跨文档证据的方法。

## 2. 论文提出的方法论：核心思想、关键技术细节
- **核心思想**：将多跳推理显式嵌入提示压缩过程，通过迭代循环逐步收集必需证据，构建一个紧凑、面向推理的提示。
- **关键技术细节**：
  - **文档分解**：将检索文档按句子切分为证据片段。
  - **相关证据筛选**：采用双方面相关度评分，结合**语义相似度**（稠密向量内积）和**词汇相似度**（基于M3-Embedding的加权词重叠），按百分位数阈值保留高相关片段。
  - **可回答性判断与缺失信息识别**：利用LLM判断当前候选证据是否足以回答原始问题；若不足，LLM生成一个有针对性的后续问题，用于下一轮筛选。
  - **迭代循环**：后续问题再次触发证据筛选→可回答性判断，直到证据充足或达到最大迭代次数（论文设为5）。
- **公式/算法流程（文字说明）**：
  - 输入：初始问题 q₀，检索文档集 D。
  - 步骤1：句子级分解，得到证据片段集合 {eᵢⱼ}。
  - 步骤2：对每个片段计算双重相关度 S_dual = λ·S_sem + (1-λ)·S_lex，按百分位数 k 保留片段。
  - 步骤3：LLM 判断当前候选集 Ecand 是否可回答 q₀。
    - 若可回答，则输出压缩提示 P_comp = Ecand，送入读者模型生成答案。
    - 若不可回答，LLM 生成后续问题 q_h，回到步骤2。
  - 重复直到满足条件或达最大迭代次数。

## 3. 实验设计：数据集、基准、对比方法
- **数据集**：三个广泛使用的多跳QA基准：
  - MuSiQue（2-4跳）
  - 2WikiMultiHopQA（最多5跳）
  - HotpotQA
  均使用开发集（dev set），其中MuSiQue仅保留可回答样本。
- **基准（Oracle和Raw Documents）**：
  - Oracle：仅提供金标准支持文档，作为压缩上限。
  - Raw Documents：拼接所有检索文档无压缩，作为无压缩基线。
- **对比方法**：硬提示压缩与抽取式压缩方法，包括：
  - Selective-Context、RECOMP (extractive)、LLMLingua、LLMLingua-2、LongLLMLingua、R2C
  - 额外报告了抽象式RECOMP和CompAct（因长度控制不一致，未作为主要对比）。
- **读者模型**：统一使用 LLaMA-3-8B 作为下游读者模型。
- **超参数**：λ=0.6，百分位数 k 按数据集调整（MuSiQue/HotpotQA: 90，2WikiMultiHopQA: 85），最大迭代次数5。

## 4. 资源与算力
- 论文未明确说明使用的GPU型号、数量或训练时长。因为IterCOMP是**training-free框架**，无需额外训练，仅需离线运行LLM推理和嵌入计算。
- 在效率分析中，使用了API商业模型（GPT-3.5-Turbo、GPT-4o、Gemini-2.5-Flash/Pro、Claude-4.5）测量成本降低和加速比，但未披露具体硬件配置。

## 5. 实验数量与充分性
- **实验组数**：
  - 主实验：3个数据集 × 对比8种基线（加上Oracle和Raw），完整报告EM、F1、压缩比。
  - 不同跳数分析：在MuSiQue上按2/3/4跳分组报告性能、迭代次数和压缩后长度。
  - 消融实验：去除迭代精炼、去除可回答性判断、仅使用语义相似度、仅使用词汇相似度。
  - 百分位数 k 影响分析：在MuSiQue上测试k=50~95。
  - 效率分析：5种API模型 × 500个样本，计算成本降低百分比和加速比。
- **充分性评价**：实验设计较为全面，覆盖了主要对比方法、消融、超参数敏感性以及经济可行性。但仅限通用领域的多跳QA（Wikipedia来源），未在专业领域或非英语数据集上验证，且缺少与软提示压缩方法的对比（因软提示不可迁移至API模型）。

## 6. 论文的主要结论与发现
- IterCOMP在所有三个数据集上均取得最佳EM和F1，显著优于现有压缩方法，例如在MuSiQue上F1从19.92提升至27.36，压缩约7倍。
- 与Oracle（上限）相比，IterCOMP在HotpotQA上弥合了53.2%的性能差距。
- 随着推理跳数增加，性能自然下降，但IterCOMP能动态调整迭代次数和证据长度，体现自适应能力。
- 消融实验表明，迭代精炼环节最为关键，可回答性判断和双方面评分均贡献显著。
- 效率分析显示，压缩后可降低75.5%~79.4%的API调用成本，并加速1.13×~2.01×。

## 7. 优点
- **训练免费**：无需任何微调，可直接应用于封闭API模型，实用性强。
- **推理感知**：将多跳推理显式融入压缩循环，通过后续问题生成弥补信息缺口，克服单次查询的局限。
- **自适应压缩**：根据问题复杂度和证据充分性自动调整迭代次数和保留信息量，避免过度压缩或不足。
- **双方面评分**：语义+词汇协同，提升相关证据召回准确率。
- **全面的实验验证**：在三个标准数据集上对比多种基线，包含详细消融和效率分析，结论可信度高。

## 8. 不足与局限
- **依赖LLM推理能力**：可回答性判断和后续问题生成依赖底层LLM，若模型能力不足可能导致错误传播（过早终止或噪声累积）。
- **额外压缩开销**：迭代过程比单次压缩方法耗时更多，虽可后续优化但论文未提供详细延迟对比。
- **超参数敏感**：百分位数k和λ需针对数据集手动调节，缺乏自动自适应机制。
- **评分模块简单**：语义+词汇的组合方式较基础，未尝试更先进的交互式评分。
- **实验域有限**：仅测试Wikipedia来源的多跳QA，未扩展到专业领域、多语言或非抽取式推理任务。
- **未与软提示压缩对比**：因适应性限制，但可补充理论分析说明其局限性。

（完）
