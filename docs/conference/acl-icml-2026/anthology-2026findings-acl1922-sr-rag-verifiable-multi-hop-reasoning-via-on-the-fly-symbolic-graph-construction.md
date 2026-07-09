---
title: "SR-RAG: Verifiable Multi-Hop Reasoning via On-the-fly Symbolic Graph Construction"
title_zh: SR-RAG：通过即时符号图构建实现可验证的多跳推理
authors: "Zehua Wang, Zhaojin Zhang, Boyu Qiu, Xiaolong Weng, Ying Xiong, Buzhou Tang, Min Zhang"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.1922.pdf"
tags: ["query:mr"]
score: 8.0
evidence: 多跳推理RAG与符号图构建
tldr: 现有RAG方法在多跳推理中面临聚合优先的高成本或动态优先的错误累积问题。本文提出SR-RAG符号推理框架，通过动态生成子问题、基于即时图的信息检索和符号编码，融合两类范式的优势。在多个数据集上，SR-RAG在准确性和可验证性上优于现有方法，为多跳RAG提供了更可靠的推理路径。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1922/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 790, \"height\": 1118, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1922/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 816, \"height\": 366, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1922/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 792, \"height\": 473, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1922/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1648, \"height\": 1042, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1922/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 754, \"height\": 583, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1922/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 795, \"height\": 593, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1922/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1620, \"height\": 785, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1922/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1475, \"height\": 2368, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1922/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1562, \"height\": 2140, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1922/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 816, \"height\": 366, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1922/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1649, \"height\": 867, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1922/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 803, \"height\": 410, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1922/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 801, \"height\": 456, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1922/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 797, \"height\": 356, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1922/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 798, \"height\": 350, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1922/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1641, \"height\": 258, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1922/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 792, \"height\": 162, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1922/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1650, \"height\": 850, \"label\": \"Table\"}]"
motivation: 现有的RAG范式在多跳推理中难以兼顾低成本和可靠性，需要一种更鲁棒的推理框架。
method: 提出SR-RAG，动态生成子问题，基于即时图进行检索和符号编码，实现可验证的多跳推理。
result: 在多个基准上，SR-RAG在多跳问答准确性和推理可验证性方面显著优于现有方法。
conclusion: SR-RAG通过符号图有效缓解了错误传播，提升了RAG多跳推理的可靠性。
---

## Abstract
Retrieval-Augmented Generation (RAG) has been widely adopted to enhance large language models (LLMs) by incorporating external knowledge. However, the two main existing paradigms struggle with multi-hop reasoning: aggregate-first approaches suffer from high construction costs and limited adaptability to dynamic knowledge, while dynamic-first approaches rely heavily on LLM reasoning and are prone to error propagation across reasoning steps. To address these limitations, we propose SR-RAG, a symbolic reasoning framework for multi-hop question answering. SR-RAG integrates the advantages of both paradigms by dynamically generating sub-questions, performing information retrieval and symbolic encoding based on an on-the-fly graph, and using a symbolic verifier to formally validate intermediate reasoning steps to ensure the correctness of intermediate answers and the completeness of the reasoning chain . We evaluate SR-RAG on multiple multi-hop benchmarks and a medical dataset. Experimental results demonstrate that it significantly improves both accuracy and robustness.

---

## 论文详细总结（自动生成）

# 论文中文总结：SR-RAG: Verifiable Multi-Hop Reasoning via On-the-fly Symbolic Graph Construction

## 1. 核心问题与整体含义（研究动机和背景）
- **问题**：现有RAG方法在多跳推理中面临两类范式各自的局限：
  - “聚合优先（aggregate-first）”范式（如基于图的RAG）需离线构建知识图谱，成本高、难以适应动态知识。
  - “动态优先（dynamic-first）”范式（如ReAct、plan-then-execute）依赖LLM逐步推理，容易因中间错误导致级联失败。
- **核心缺失**：两类方法均缺乏对中间推理步骤的形式化验证与更新机制，导致可解释性差、错误难以纠正。
- **动机**：融合两类范式的优势——动态适应性与结构约束，并引入显式的符号验证，以实现更可靠的多跳推理。

## 2. 方法论：核心思想、关键技术细节
- **框架名称**：SR-RAG（Symbolic Reasoning RAG）
- **核心思想**：动态生成子问题 → 检索文档 → 即时构建查询特定知识图谱 → 映射为一阶逻辑前提 → 通过外部符号证明器（SWI-Prolog）验证中间答案 → 反馈循环补全缺失事实 → 最终用全局互逆秩融合（GRRF）聚合多步文档生成答案。
- **关键技术细节**：
  - **动态生成器**：两种变体
    - ReAct型：根据历史交替生成子查询。
    - Plan型：首先生成有向无环图（DAG）计划，再按依赖并行/串行执行子查询。
  - **符号验证器**：
    - 将图谱中的实体映射为常量，关系映射为谓词，属性映射为谓词或一元谓词。
    - 子问题解析为目标公式 ψ，证明器寻找替换 θ 使 Π |= ψθ。
    - 若证明失败，利用失败轨迹进行反溯分析，由LLM提出缺失事实，指导图谱更新（反馈循环），最多迭代2次。
  - **答案生成器**：
    - GRRF：对各子查询的检索结果进行稀疏+密集混合检索，按互逆秩评分，去重后选择Top-K文档。
    - 将原始问题、推理历史（子问题-答案-文档）和GRRF选出的文档输入LLM生成最终答案。

## 3. 实验设计
- **数据集**：HotpotQA、2WikiMultiHopQA、MuSiQue、Bamboogle（均为开放域多跳QA），以及一个医疗数据集（来自GraphRAG-Bench，含4076个问题）。
- **评估指标**：Acc@R（答案包含黄金答案关键信息）和Acc@L（LLM评价语义和事实一致性）。
- **对比方法**：
  - 聚合优先：Vanilla RAG, RAPTOR, LightRAG, HippoRAG1&2, GFM-RAG, LinearRAG。
  - 动态优先：CoT, Self-ASK, IRCoT, Iter-RetGen, Plan*RAG, GenGround, IterKey。
- **实现细节**：基于GPT-4o-mini，retriever和知识库与LinearRAG相同，每个子查询检索3篇文档。

## 4. 资源与算力
- 论文未明确提及GPU型号、数量、训练时长等硬件资源信息。
- 仅说明使用GPT-4o-mini作为基础LLM，所有baseline也在相同模型上实现；retriever使用BM25、all-mpnet-base-v2、jina-embedding-v3等通用模型。
- 未涉及模型训练，因此算力主要来自推理阶段。

## 5. 实验数量与充分性
- **实验数量充分**：包括
  - 主要对比实验：5个数据集上对比10+种方法，每个报告Acc@R和Acc@L。
  - 消融实验：分别针对符号验证器（替换为LLM直接输出或直接使用文档）、反馈循环（比较反馈次数0/1/2）、答案生成器组件（替换GRRF为Top-5、移除相关文档、移除推理历史）进行验证。
  - 符号验证有效性分析：报告Valid Prolog Rate (VPR)和Trigger Rate (TR)。
  - 噪声鲁棒性分析：在HotpotQA和MuSiQue上采样200例，添加0%-80%噪声。
  - 失败案例分析：对50个基线失败样本进行人工分析，统计SR-RAG的修正情况。
  - 推理时间分析：分阶段统计延迟。
- **公平性与客观性**：使用统一LLM、统一检索库，所有baseline按原论文复现或引用已有结果，消融设计合理，对比方法涵盖两类范式的主要代表。

## 6. 主要结论与发现
- SR-RAG在所有数据集上一致优于所有基线，平均Acc@R和Acc@L均最高。
- ReAct型变体在多数数据集上表现更好，Plan型在HotpotQA上略优，提示不同策略适用于不同问题结构。
- 符号验证器对性能提升关键：直接依赖LLM或文档均导致明显下降。
- 反馈循环显著提高符号验证的触发率（TR提升6%-41%），从而提升整体准确率。
- GRRF优于简单Top-5检索；移除推理历史或相关文档均降低性能。
- 噪声鲁棒性分析显示SR-RAG在高噪声下性能下降幅度远小于动态优先方法（性能差距+24.5%）。
- 失败分析表明SR-RAG主要修正了检索不完整（21/36）和LLM幻觉（8/14）问题。

## 7. 优点
- **创新性**：首次将符号验证显式集成到动态RAG的多步推理中，形式化保证中间答案逻辑一致性。
- **兼容性**：融合聚合优先的结构约束和动态优先的自适应，且不依赖离线预建图谱。
- **可解释性**：推理链由显式逻辑步骤组成，可追溯、可验证（见图6案例）。
- **鲁棒性**：符号验证和反馈循环有效抑制错误传播，噪声场景下表现稳健。
- **实验全面性**：覆盖多种数据集、多类基线、多维度消融和鲁棒性分析，结论可靠。

## 8. 不足与局限
- **依赖抽取质量**：符号验证的效果受限于信息抽取（实体/关系提取）的准确性；抽取错误可能导致不完备或过约束的前提。
- **反馈机制局限**：极端情况下（如检索文档高度不相关或矛盾），反馈循环仍可能失败。
- **计算开销**：在线构建图谱和执行Prolog证明带来延迟（约4.5s/迭代，反馈后约6.9s），虽低于静态图构建，但在实时场景下仍需优化。
- **通用性问题**：当前瓶颈在通用LLM生成速度，未探索专用轻量模型或并行化加速；领域适应性（如医疗）还需进一步验证。
- **训练信息缺失**：论文未提及模型训练细节及硬件配置，不利于复现和扩展。

（完）
