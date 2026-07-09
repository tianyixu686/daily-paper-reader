---
title: "D2Plan: Dual-Agent Dynamic Global Planning for Complex Retrieval-Augmented Reasoning"
title_zh: "D2Plan: 面向复杂检索增强推理的双智能体动态全局规划"
authors: "Kangcheng Luo, Tinglang Wu, Yansong Feng"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.acl-long.216.pdf"
tags: ["query:mr"]
score: 8.0
evidence: 面向复杂检索增强多跳推理的双智能体动态规划
tldr: 针对检索增强的多跳推理中搜索链构建无效和推理被无关证据干扰的问题，提出D2Plan双智能体动态全局规划范式。通过Reasoner和Purifier协作，Reasoner负责搜索链构建，Purifier过滤干扰证据。实验证明在多个多跳推理基准上显著优于现有方法，有效提升了推理准确率。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.216/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1479, \"height\": 891, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.216/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 745, \"height\": 304, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.216/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 678, \"height\": 385, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.216/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 794, \"height\": 418, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.216/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 677, \"height\": 496, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.216/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1661, \"height\": 726, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.216/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 678, \"height\": 252, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.216/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 687, \"height\": 314, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.216/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 591, \"height\": 177, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.216/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 803, \"height\": 363, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.216/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 685, \"height\": 395, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.216/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 723, \"height\": 413, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.216/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1115, \"height\": 291, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.216/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1162, \"height\": 404, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.216/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1190, \"height\": 218, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.216/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 984, \"height\": 221, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.216/table-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1436, \"height\": 222, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.216/table-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1297, \"height\": 384, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.216/table-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 1573, \"height\": 1305, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.216/table-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 1567, \"height\": 1932, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.216/table-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 1577, \"height\": 1064, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.216/table-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 1567, \"height\": 2346, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.216/table-020.webp\", \"caption\": \"\", \"page\": 0, \"index\": 20, \"width\": 1593, \"height\": 885, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.216/table-021.webp\", \"caption\": \"\", \"page\": 0, \"index\": 21, \"width\": 1570, \"height\": 2193, \"label\": \"Table\"}]"
motivation: 现有检索增强推理方法在长上下文下容易构建错误搜索链和被干扰证据误导。
method: 提出Reasoner和Purifier双智能体协作的全局动态规划方法。
result: 在多个多跳推理数据集上取得显著性能提升。
conclusion: 双智能体协作能有效解决检索增强推理中的关键失败模式。
---

## Abstract
Recent search-augmented LLMs trained with reinforcement learning (RL) can interleave searching and reasoning for multi-hop reasoning tasks. However, they face two critical failure modes as the accumulating context becomes flooded with both crucial evidence and irrelevant information: (1) ineffective search chain construction that produces incorrect queries or omits retrieval of critical information, and (2) reasoning hijacking by peripheral evidence that causes models to misidentify distractors as valid evidence.To address these challenges, we propose **D²Plan**, a **D**ual-agent **D**ynamic global **Plan**ning paradigm for complex retrieval-augmented reasoning. D²Plan operates through the collaboration of a *Reasoner* and a *Purifier*: the *Reasoner* constructs explicit global plans during reasoning and dynamically adapts them based on retrieval feedback; the *Purifier* assesses retrieval relevance and condenses key information for the *Reasoner*.We further introduce a two-stage training framework consisting of supervised fine-tuning (SFT) cold-start on synthesized trajectories and RL with plan-oriented rewards to teach LLMs to master the D²Plan paradigm. Extensive experiments demonstrate that D²Plan enables more coherent multi-step reasoning and stronger resilience to irrelevant information, thereby achieving superior performance on challenging QA benchmarks.

---

## 论文详细总结（自动生成）

# 论文总结：D²Plan — 面向复杂检索增强推理的双智能体动态全局规划

## 1. 核心问题与整体含义（研究动机和背景）

**研究动机**：当前基于强化学习的搜索增强大模型（LLM）能够自主交替执行搜索与推理，以应对多跳知识密集型问答任务。然而，随着迭代检索过程中上下文不断累积，模型面临两个核心失败模式：
- **(E1) 无效搜索链构建**：生成的查询序列偏离原问题目标，或遗漏关键信息，导致检索目标漂移。
- **(E2) 推理被外围证据劫持**：模型难以从大量无关信息中区分有效证据，常基于干扰信息得出错误结论。

**整体含义**：现有方法缺乏对检索增强推理过程的全局感知和精细控制，亟需一种能动态规划搜索路径并抵抗无关信息干扰的范式。论文提出**D²Plan**，通过双智能体协作和显式动态全局规划，增强模型的多步搜索推理能力，提升复杂问答任务的准确性和鲁棒性。

## 2. 方法论

### 2.1 核心思想
D²Plan 采用双智能体架构：
- **Reasoner（推理者）**：负责构建全局问题分解计划（有序的子问题序列），依次解决每个子问题，并根据检索反馈动态调整计划（包括子问题精炼和全局重规划）。
- **Purifier（净化者）**：对每次检索返回的文档进行相关性判断，若相关则精确提取关键信息，否则提供简要摘要；将净化后的结果和相关性评价反馈给Reasoner，避免无关信息污染推理上下文。

### 2.2 关键技术细节
1. **动态全局规划流程**：
   - 初始计划：Reasoner根据问题复杂度分解为子问题（单跳无需分解，多跳分解为有序序列）。
   - 迭代求解：逐个解决子问题，每次检索前生成查询，Purifier净化检索结果。成功获取相关信息后，Reasoner精炼后续子问题（填充占位符，使其更具体自包含）。
   - 计划适应：若某子问题多次检索均失败（达到最大尝试次数K），Reasoner触发全局重规划，修改剩余子问题以探索新路径。
2. **两阶段训练框架**：
   - **SFT冷启动**：使用强教师模型（qwen-max-latest）按D²Plan流程合成推理轨迹，过滤正确且包含检索的轨迹；分别构建Reasoner和Purifier的训练数据。Reasoner训练目标为连贯推理链，Purifier训练目标为相关性判断与信息提取。
   - **SPLAN RL**：冻结Purifier，使用GRPO算法优化Reasoner，引入**计划导向奖励**：
     - **初始规划奖励 Rp**：单跳不分解得1分，多跳子问题数量与标注跳数匹配得1分，否则0分。
     - **计划适应奖励 Ra** = 精炼奖励 R_refine + 重规划奖励 R_revise。精炼奖励：所有依赖前序的子问题均成功精炼且无占位符得1分。重规划奖励：由时机奖励 Rt（仅在达到最大尝试次数后触发重规划得1分）和质量奖励 Rq（重规划后第一个子问题检索成功得1分）组成，并引入折扣系数 λ（论文设为0.5），对答案错误但尝试重规划的轨迹给予部分过程奖励。
     - **答案奖励 Rans**：预测答案与标准答案的F1分数。
     - **格式奖励 Rf**：确保输出符合预设标签格式（如<plan>、<replan>、<answer>等），满足则得1分，否则0分。
   - **总奖励**：R_total = Rf · (α·Rp + β·Ra + Rans)，其中α=β=0.1。

### 2.3 公式与算法（文字说明）
论文通过算法伪代码（Algorithm 1-5）详细描述了D²Plan的推理流程和轨迹合成策略。核心步骤：
- 推理者评估问题复杂度。
- 对多跳问题：分解为子问题列表 → 循环处理每个子问题 → 调用迭代检索（最多K次），Purifier返回相关性及净化信息 → 若成功则精炼下一子问题，若失败则触发重规划（最多M次） → 所有子问题解决后生成最终答案。
- 迭代检索内部：生成查询 → 检索 → Purifier净化 → 若相关则返回成功，否则重写查询重复尝试。

## 3. 实验设计

### 3.1 数据集与场景
- **训练集**：从NQ、HotpotQA、MuSiQue的training split中采样，SFT使用4000条推理轨迹（Reasoner）和11255条（Purifier），RL使用29762条（不重叠）。
- **测试集**：共6个开放域QA基准，涵盖单跳和多跳：
  - 单跳/简单：Natural Questions (NQ), SimpleQA
  - 多跳：HotpotQA, 2WikiMultihopQA (2Wiki), MuSiQue (MSQ), FRAMES
- **评价指标**：Exact Match (EM) 和 LLM-as-a-Judge (LasJ)（使用qwen-plus判断答案正确性）。

### 3.2 基准方法
对比了6种代表性RL-based检索增强方法：
- Search-R1、ReSearch、AutoRefine、ZeroSearch、R1-Searcher、StepSearch
- 所有基线在相同环境下复现推理结果。

### 3.3 实验配置
- 骨干模型：Qwen2.5-3B/7B-Instruct
- 检索器：E5嵌入模型 + 2018 Wikipedia dump，top-5 passage
- SFT教师模型：qwen-max-latest
- RL算法：GRPO，实现自verl框架
- 最大检索尝试次数K=3，最大重规划次数M=1

## 4. 资源与算力

论文在正文及附录中**未明确说明**使用的GPU具体型号、数量及训练时长。仅在附录G中提及“使用vLLM server模式部署在8×A800节点上”用于Purifier推理效率分析，但未给出SFT和RL训练阶段的具体硬件配置和耗时。因此无法准确评估算力开销。

## 5. 实验数量与充分性

实验设计比较充分，包括：
- **主实验结果（表1）**：在6个数据集、2种模型规模（3B/7B）上与6个基线对比，报告LasJ和EM，共12组对比。
- **消融实验（表2）**：在3个多跳数据集上分别对SFT和SFT+RL阶段移除规划组件（w/o Plan&Adapt、w/o Adapt）以及移除计划奖励（w/o Rp、w/o Ra）进行深入分析。
- **检索质量分析（表3）**：统计有效/无效检索次数、子答案覆盖率，验证规划适应性。
- **初始规划奖励影响（表4）**：按跳数分组对比去除Rp的效果。
- **计划适应奖励影响（表5）**：对比去除Ra后的首次检索有效率和最终准确率。
- **双智能体架构效果（表6）**：对比使用/不使用Purifier在不同跳数下的性能、检索次数、上下文长度。
- **错误类型分布（图4）**：在FRAMES和MuSiQue上针对Search-R1、StepSearch和D²Plan分析E1、E2.1、E2.2、E3的比例。
- **额外分析**：附录中还包括不同Purifier对比（表8）、Purifier移植基线（表9）、单智能体对比（表10）、奖励权重敏感性（表11）、误差迁移矩阵（表12-13）、token消耗（表14）等，实验丰富。

**充分性与客观性**：
- 在多个数据集上覆盖了单跳和多跳，且区分了in-domain和out-of-domain，确保泛化能力。
- 消融实验设计严谨，分别考虑SFT和RL阶段各组件贡献。
- 错误分析手动标注并计算Cohen's Kappa (0.72)，验证了可靠度。
- 所有基线在相同环境下复现，保证公平。

## 6. 主要结论与发现

1. **D²Plan显著优于所有基线**：在3B和7B规模上，平均LasJ分别比最强基线AutoRefine提高1.34%、比R1-Searcher提高3.83%；在复杂多跳任务（如FRAMES）上相对提升达58.3%。
2. **动态全局规划是核心**：消融实验表明，移除规划或适应机制后性能大幅下降，证明显式计划比单纯SFT蒸馏更关键。
3. **计划导向奖励有效**：初始规划奖励防止过度分解，计划适应奖励引导正确重规划，提升检索有效率和最终准确率。
4. **Purifier同时提升精度和效率**：将上下文长度减少63.6%，推理时间降低约12%，在困难问题上增益更显著。
5. **错误迁移分析**：D²Plan显著降低E1和E2.1错误，剩余错误（E2.2）主要源于检索系统限制（如语料缺失），而非模型推理缺陷。

## 7. 优点

- **问题诊断精准**：明确指出现有方法的两大失败模式（E1、E2），并为之设计了针对性解决方案。
- **架构创新**：双智能体分离“规划-推理”与“净化-评估”职责，减轻Reasoner负担，增强抗干扰能力。
- **训练方法有效**：SFT冷启动提供基础能力，RL阶段通过计划奖励精细化指导模型学习动态调整策略，避免依赖昂贵的细粒度标注。
- **实验全面且一致**：覆盖多种数据集、多模型规模、多基线，消融和错误分析深入，结论可信。
- **效率意识**：虽然引入额外Purifier，但因减少上下文长度，实际端到端推理时间下降。

## 8. 不足与局限

- **模型规模局限**：仅在3B和7B上实验，未在更大模型（如70B）上验证，大规模下的效果和复杂度未知。
- **检索器依赖**：使用本地稠密检索器+静态Wikipedia，而非更强大的商业搜索引擎；论文指出E2.2失败中相当比例源于语料缺失，限制了下界。
- **教师模型依赖**：SFT阶段需强大教师模型（如qwen-max-latest）合成轨迹，若无法访问此类模型，方法适用性受限。
- **未提及详细算力成本**：缺乏SFT和RL训练的GPU型号、数量及时长信息，难以评估方法的经济可复现性。
- **可能的偏差风险**：RL训练数据来自NQ、HotpotQA、MuSiQue的训练集，虽然测试集涵盖领域外数据，但训练数据分布可能影响模型泛化到更开放式场景（如实时信息搜索）。

（完）
