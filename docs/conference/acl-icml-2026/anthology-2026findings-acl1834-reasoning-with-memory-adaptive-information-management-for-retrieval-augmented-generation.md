---
title: "Reasoning with Memory: Adaptive Information Management for Retrieval-Augmented Generation"
title_zh: 记忆推理：检索增强生成的自适应信息管理
authors: "Hieu Man, Ro-ee Tal, Abhishek Kumar, Jaejin Cho, Benjamin Hsu"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.1834.pdf"
tags: ["query:mr"]
score: 9.0
evidence: 基于工作记忆的多跳推理RAG方法
tldr: 多跳推理是RAG系统的核心挑战，现有方法难以保持长链推理的中间状态一致。本文提出State-Aware RAG，引入显式的工作记忆作为动态推理空间，通过路径-结果双重奖励机制训练一个轻量提取器来主动过滤和更新记忆。实验表明该方法在多个基准上显著提升多跳推理准确率，且与现有RAG系统即插即用。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1834/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1608, \"height\": 613, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1834/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 724, \"height\": 702, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1834/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 807, \"height\": 256, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1834/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 804, \"height\": 247, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1834/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1651, \"height\": 1068, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1834/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 649, \"height\": 530, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1834/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 651, \"height\": 672, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1834/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1353, \"height\": 1113, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1834/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 665, \"height\": 680, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1834/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 492, \"height\": 575, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1834/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 442, \"height\": 285, \"label\": \"Table\"}]"
motivation: 现有RAG系统在长链条多跳推理中难以维持中间状态一致性，缺乏动态推理工作空间。
method: 提出State-Aware RAG框架，采用显式工作记忆和路径-结果双重奖励训练提取器，实现自适应信息过滤与更新。
result: 在多个多跳问答数据集上，该方法相较基线取得显著提升，并保持即插即用兼容性。
conclusion: 工作记忆机制有效增强了RAG系统的多跳推理能力，为模块化RAG设计提供新方向。
---

## Abstract
Multi-hop reasoning remains a fundamental challenge for Retrieval-Augmented Generation (RAG) systems. Recent approaches—from adaptive retrieval to agentic pipelines—struggle to maintain coherent intermediate reasoning states as chains grow longer. We introduce State-Aware RAG, a framework that addresses this limitation through an explicit working memory that serves as a dynamic cognitive workspace for reasoning. Our modular architecture features a lightweight, trainable extractor that learns to actively filter, consolidate, and update this working memory via a novel Path-Outcome Dual Reward paradigm, which balances local coherence with global strategy. The retriever and generator remain frozen, enabling plug-and-play flexibility. Experiments on eight QA benchmarks demonstrate state-of-the-art results, on average achieving +8.6% over the best memory-augmented baseline and +9.3% over the best RL-enhanced baseline. Our architecture generalizes seamlessly to stronger generators and retrievers without retraining, establishing dynamic memory management as a critical yet underexplored dimension for advancing RAG systems.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）
论文聚焦于**检索增强生成（RAG）系统中的多跳推理**这一核心难题。现有RAG方法（如标准RAG、迭代检索、规划增强等）虽然改进了信息获取（查询重写、检索策略等），但忽视了**信息管理**机制——即如何对已检索内容进行主动策展、整合和维护。随着推理链增长，静态累积的上下文导致噪声、冗余、矛盾信息累积，造成推理漂移和性能退化。  
**整体含义**：将认知科学中的工作记忆（Working Memory）概念引入RAG，把推理过程视为一个需要动态、持久、主动管理的信息加工过程，而非无状态的文档拼接。

## 2. 方法论
### 核心思想
- **显式工作记忆**：一个跨推理步持久存在、持续更新的动态知识状态，充当推理的“认知工作空间”。
- 系统由三个模块化组件构成：**检索器（Retriever）**、**生成器（Generator）** 和 **提取器（Extractor）**。仅提取器通过强化学习训练，其余冻结，保证即插即用。

### 关键技术细节
1. **状态表示**：每个推理状态 \(S_i = (q_i, r_i, M_i)\)，其中工作记忆 \(M_i\) 是在第 \(i\) 步后被主动更新的知识表征。
2. **提取器功能**：两步操作：
   - **合并（Consolidation）**：从查询、当前记忆和检索文档中提取相关信息 \(I_i\)，完成相关性过滤、矛盾解决和冗余消除。
   - **记忆更新（Memory Update）**：在生成回答后，整合新问题-回答对和提取信息到工作记忆中。
3. **路径-结果双重奖励（Path-Outcome Dual Reward）**：
   - **路径奖励 \(R_p\)**：评估每一步提取的信息是否与子问题相关、充分、逻辑连贯且事实准确（LLM逐维打分）。
   - **结果奖励 \(R_o\)**：评估最终答案相对于原问题和真实答案的正确性。
   - 训练目标：最大化 \( \frac{1}{n-1}\sum_{i=1}^{n-1} R_p(q_i, r_i) + \lambda R_o(y, x, y^*) \)，\(\lambda=2\)。
4. **推理模式**：
   - **苏格拉底式规划（Socratic Planning）**：单链分解-回答，高效。
   - **蒙特卡洛树搜索（MCTS）**：对复杂任务进行系统探索，支持5种动作（分解并回答、合并、细化、重定向、结束），且工作记忆跨分支共享。

## 3. 实验设计
### 数据集
- **多跳QA**：2WikiMultihopQA、HotpotQA、MuSiQue、Bamboogle（全量125例）。
- **单跳QA**：SimpleQA、Natural Questions、TriviaQA、PopQA。
- 从每个数据集随机采样1000例（Bamboogle除外），共计约8000+测试样本。

### 基准（Baselines）
7个类别，共18+种方法：
- 直接生成（Qwen3-8B, CoT）
- 标准RAG（RAG, RAG+Rerank）
- 迭代检索（IR-CoT, FLARE, Search-o1）
- 查询重写（Self-RAG, RaFe）
- 规划增强（MCTS-RAG, RAG-Star）
- RL增强（Search-R1, S3）
- 记忆增强（MemoRAG, HippoRAG, HippoRAG 2）

### 指标
- **Sub-EM**：子串精确匹配（严格）
- **Acc**：LLM-as-a-Judge（Claude 3.7 Sonnet）评估语义等价。

## 4. 资源与算力
文中在实验设置部分未明确说明所使用的GPU型号、数量及训练时长。仅在附录中给出了训练超参数（学习率、批量大小、序列长度等），并提及使用**Axolotl**和**verl**框架、**vLLM**推理引擎。训练数据规模：871个种子问题，合成约10K推理路径（70K状态-动作对）。**算力细节缺失**，无法据此评估复现成本。

## 5. 实验数量与充分性
- **主要实验**：表1涵盖8个数据集，对比18+基线，在Sub-EM和Acc两个指标上全面超越。
- **消融实验**（表2、表3）：
  - 记忆管理组件消融（去掉提取器、去掉记忆更新、去掉合并）。
  - 训练策略消融（纯提示、仅SFT、仅结果奖励、仅路径奖励、双奖励、Claude 3.7作为提取器上界）。
- **组件缩放实验**（图3）：更换生成器（Qwen3-8B → 30B → Claude 3.7）和检索器（E5-base → Qwen3-Embedding-4B → Google搜索），验证通用性。
- **推理超参数分析**（图4）：对苏格拉底模式和MCTS，分别变化最大推理步数(3-15)和rollout数(3-15)。
- **充分性**：实验设计完整、对比公平（控制生成器规模在7-14B间匹配），消融覆盖核心模块，组件缩放提供了强有力的通用性证据。不足之处在于**训练算力开销未报告**，且仅在QA场景评估，领域泛化性未验证。

## 6. 主要结论与发现
1. **动态工作记忆管理是关键**：State-Aware RAG在多跳任务平均准确率58.0%，比最佳记忆增强基线（HippoRAG 2）高8.6%；单跳任务平均72.7%，比最佳RL增强基线（S3）高9.3%。
2. **路径-结果双重奖励优于单一奖励**：双奖励在苏格拉底模式比仅结果奖励高1.1% Acc，比仅路径奖励高1.5%；在MCTS模式下优势更明显。
3. **提取器通用性**：无需重新训练，即可利用更强生成器（Claude 3.7带来+16.5%）和更强检索器（Google搜索带来+22.2%）。
4. **检索质量仍是主要瓶颈**：即使最优记忆管理也无法弥补信息缺失，替换为Web搜索后性能大幅提升。
5. **MCTS vs 苏格拉底**：MCTS在高rollout时优势扩大（+4.1%），但成本高（～7×生成器调用），适用于复杂任务。

## 7. 优点
- **模块化设计**：仅训练轻量提取器（Qwen3-4B），检索器和生成器冻结，实现即插即用，与任意组件通用。
- **认知启发的创新**：将工作记忆概念系统化引入RAG，填补了“信息管理”空白。
- **奖励机制巧妙**：路径奖励提供密集局部信号，结果奖励提供全局导向，两者平衡避免了局部过优或稀疏反馈问题。
- **推理模式灵活**：苏格拉底模式高效、MCTS模式探索性强，适应不同复杂度。
- **消融实验严谨**：逐一剥离记忆管理组件，定量验证每个设计的必要性。

## 8. 不足与局限
- **训练成本高**：LLM-as-a-Judge计算路径和结果奖励需要大量额外LLM调用，限制了训练规模。
- **检索质量仍是天花板**：静态Wikipedia语料限制性能，替换为Web搜索后收益极大，说明记忆管理不能完全补偿检索缺陷。
- **领域泛化未验证**：仅评测QA，未涉及科学文献、企业文档等现实场景或多步推理以外的任务（如事实验证、对话）。
- **MCTS推理开销大**：约7倍生成器调用只换来小幅度提升（2.6% Acc），不适合延迟敏感应用。
- **数据合成依赖强oracle**：使用DeepSeek-R1作为Oracle提取器合成训练轨迹，可能引入噪音或分布偏移。
- **实验可复现性受限**：未公布GPU型号、训练耗时等关键算力信息，影响复现信心。

（完）
