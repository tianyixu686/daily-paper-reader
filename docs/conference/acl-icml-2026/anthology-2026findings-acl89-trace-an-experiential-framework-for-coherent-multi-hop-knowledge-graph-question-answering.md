---
title: "TRACE: An Experiential Framework for Coherent Multi-hop Knowledge Graph Question Answering"
title_zh: TRACE：用于连贯多跳知识图谱问答的经验框架
authors: "Yingxu Wang, Jiaxin Huang, Mengzhu Wang, Nan Yin"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.89.pdf"
tags: ["query:mr"]
score: 8.0
evidence: 连贯的多跳知识图谱问答
tldr: 多跳知识图谱问答中推理碎片化和重复探索问题严重。TRACE提出经验框架，将推理路径动态转化为自然语言叙事以保持语义连贯，并抽象探索先验指导后续步骤。在多个KGQA数据集上，TRACE提升了推理连贯性和答案准确性，展示了经验重用对多跳推理的价值。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.89/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1647, \"height\": 484, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.89/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1569, \"height\": 345, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.89/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 658, \"height\": 236, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.89/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 803, \"height\": 1179, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.89/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 799, \"height\": 263, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.89/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 792, \"height\": 300, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.89/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 776, \"height\": 302, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.89/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1613, \"height\": 1169, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.89/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1659, \"height\": 978, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.89/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 778, \"height\": 247, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.89/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1611, \"height\": 1306, \"label\": \"Table\"}]"
motivation: 现有KGQA方法对各推理步独立建模，缺乏经验利用，导致推理碎片化和重复探索。
method: 提出TRACE框架，用动态叙事保持语义连续，并整合探索先验增强推理连贯性。
result: 在多个KGQA数据集上，TRACE在路径连贯性和答案F1上优于现有方法。
conclusion: 经验框架有效提升了多跳KGQA的推理质量，可推广至其他多跳场景。
---

## Abstract
Multi-hop Knowledge Graph Question Answering (KGQA) requires coherent reasoning across relational paths, yet existing methods often treat each reasoning step independently and fail to effectively leverage experience from prior explorations, leading to fragmented reasoning and redundant exploration. To address these challenges, we propose Trajectoryaware Reasoning with Adaptive Context and Exploration priors (TRACE), an experiential framework that unifies LLM-driven contextual reasoning with exploration prior integration to enhance the coherence and robustness of multihop KGQA. Specifically, TRACE dynamically translates evolving reasoning paths into natural language narratives to maintain semantic continuity, while abstracting prior exploration trajectories into reusable experiential priors that capture recurring exploration patterns. A dualfeedback re-ranking mechanism further integrates contextual narratives with exploration priors to guide relation selection during reasoning. Extensive experiments on multiple KGQA benchmarks demonstrate that TRACE consistently outperforms state-of-the-art baselines.

---

## 论文详细总结（自动生成）

# TRACE: 用于连贯多跳知识图谱问答的经验框架 — 详细总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：多跳知识图谱问答（KGQA）要求在关系路径上进行连贯的推理，但现有方法通常独立处理每个推理步骤，未能有效利用先前探索的经验，导致推理碎片化和冗余探索。
- **研究动机**：如何设计一个经验驱动的 KGQA 框架，既能保持多跳推理的语义连贯性，又能从历史探索中学习并避免重复错误。
- **整体含义**：提出 TRACE 框架，通过将推理路径动态转化为自然语言叙事来维持语义连续性，并通过抽象先验探索轨迹为可重用经验先验来指导后续步骤，从而显著提升推理的连贯性和鲁棒性。

## 2. 论文提出的方法论

### 2.1 核心思想
- **动态上下文生成**：在每一步将已探索的关系序列转化为自然的语言描述，使关系选择始终基于累积的推理上下文而非孤立决策。
- **探索泛化**：当推理轨迹终止（达到最大步长或无法扩展）时，利用 LLM 总结该轨迹，并进一步从多个轨迹中抽象出通用的探索模式，形成可重用的经验先验。
- **双反馈重排序**：先由 LLM 检索器基于上下文叙事选出 top-k 候选关系，再结合当前路径关系序列和经验先验对候选关系重新评分，保留超过置信阈值 ζ 的关系进行分支扩展。

### 2.2 关键技术细节
- **公式**：
  - 上下文叙事生成：C<sup>(t)</sup><sub>q</sub> = f<sub>ctx</sub>(q, R<sup>(t)</sup><sub>q</sub>)
  - 候选检索：C<sub>t</sub> = f<sub>ret</sub>(q, C<sup>(t)</sup><sub>q</sub>, N(e<sub>t</sub>))
  - 重排序分数：s(r) = f<sub>rank</sub>(q, R<sup>(t)</sup><sub>q</sub>, r, F)
  - 路径扩展：R<sup>(t+1)</sup><sub>q</sub> = (R<sup>(t)</sup><sub>q</sub> ⊕ r | r ∈ C<sub>t</sub>, s(r) ≥ ζ)
- **算法流程**（文字说明）：
  1. 初始化探索先验 F 为空，从主题实体开始推理路径。
  2. 对于每次迭代（最多 I=30 次）：
     - 对每个当前路径，循环至多 L=4 步：
       - 生成上下文叙事。
       - 检索 top-k 候选关系（WebQSP 取 k=3，CWQ 取 k=4）。
       - 双反馈重排序，保留分数 ≥ ζ=0.5 的关系，扩展新分支。
     - 若路径终止，生成轨迹摘要并更新 F。
  3. 从得分最高的最终路径预测答案。

## 3. 实验设计

- **数据集**：WebQSP（2848 训练/250 验证/1639 测试）和 CWQ（27639 训练/3519 验证/3531 测试）。
- **Benchmark 设置**：从每个数据集测试集中随机采样 1000 个问题进行评估。
- **对比方法**：
  - 语义解析：KV-Mem、EmbedKGQA、QGG、NSM、TransferNet、KGT5、DECAF
  - 检索方法：GraftNet、PullNet、SR+NSM、SR+NSM+E2E
  - 通用 LLM：Flan-T5-xl、Alpaca-7B、Llama3-8B、Qwen2.5-7B、ChatGPT、ChatGPT+CoT
  - LLM+KG：UniKGQA、KD-CoT、Nutrea、ToG、RoG、KAPING、ReasoningLM、FiDeLis、GNN-RAG、DoG、DualR、DP、RwT
- **评估指标**：Hits@1 和 F1 分数。

## 4. 资源与算力

- **论文未明确说明**使用的 GPU 型号、数量及训练时长。
- 推理时以 GPT-4.1 作为骨干 LLM（用于上下文生成、检索、重排序和总结），并报告了平均 token 消耗和 LLM 调用次数（WebQSP：8782 tokens, 14.2 calls；CWQ：16414 tokens, 27.8 calls）。
- 未提及自有训练资源或消融实验中的具体硬件配置。

## 5. 实验数量与充分性

- **实验数量**：主结果表（表2）在两个数据集上与 20+ 基线对比；不同 LLM 骨干对比（表3，4种骨干）；消融实验（表4，3种变体）；超参数敏感性分析（图2，k、L、ζ 各4个值）；计算消耗分析（表5，4种方法对比）；案例研究（表6、表8，各5个模型输出对比）。
- **充分性**：覆盖了主流基线、关键组件验证、超参数调优、效率评估和可视化分析，实验设计较为全面。
- **客观性与公平性**：使用标准数据集和评测指标，对比基线收录了近年代表性方法，结果呈现清晰，消融实验证实了各组件的必要性。

## 6. 论文的主要结论与发现

- TRACE 在 WebQSP 和 CWQ 上均超越所有对比方法，Hits@1 分别达 91.6% 和 76.9%，F1 分别达 81.7% 和 72.9%。
- 动态上下文生成和探索泛化两个模块缺一不可，同时移除时性能下降最大，说明它们互补协作。
- 即使在较弱骨干（Llama2-13B）下，TRACE 仍优于强基线（如 RwT、FiDeLis），表明框架具有较强的鲁棒性。
- 在计算消耗方面，TRACE 的 token 消耗和 LLM 调用次数均低于同类方法（如 RwT），实现了更高效的推理。

## 7. 优点

- **方法创新性**：将推理路径转化为自然语言叙事保持语义连贯，并首次系统地将历史探索抽象为可重用先验指导后续推理。
- **设计合理**：双反馈机制巧妙整合局部上下文和全局经验，既保留了探索广度又提升了选择精度。
- **实验充分**：在两个标准数据集上进行了全面的对比、消融、敏感性和效率分析，结果可信度高。
- **实用性强**：相较基线方法，在提升性能的同时降低了计算成本，具备更好的可扩展性。

## 8. 不足与局限

- **依赖手工提示**：框架中使用的提示模板和探索先验均需人工设计，可能限制对异构或噪声知识图谱的适应能力。
- **推理成本较高**：尽管优于部分方法，但仍需要多次 LLM 调用（平均 14-28 次），在实时场景或资源受限设备上部署可能仍有挑战。
- **领域泛化未验证**：实验仅针对 Freebase 上的 KGQA 任务，未在科学发现、多智能体协作等更广泛领域验证，方法的通用性尚未证实。
- **缺乏训练资源细节**：论文未报告模型训练或推理时的具体硬件配置和时长，不利于复现和公平比较。
- **超参数敏感**：置信阈值 ζ 和候选数量 k 对性能影响较大，默认值依赖人工调优，缺乏自适应机制。

（完）
