---
title: Collaborative Chain-of-Agents for Parametric-Retrieved Knowledge Synergy
title_zh: 参数与检索知识协同的协作式智能体链
authors: "Yi Jiang, Sendong Zhao, Jianbo Li, Haochun Wang, Lizhe Zhang, Yan Liu, Bing Qin (秦兵)"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.acl-long.167.pdf"
tags: ["query:mr"]
score: 4.0
evidence: 提出用于参数与检索知识协同的多智能体RAG框架
tldr: 针对RAG中模型内部参数知识与外部检索知识协同不足的问题，提出协作式智能体链（CoCoA）框架。该方法通过多智能体协作实现条件知识归纳，增强两种知识的融合。实验证明其能有效提升知识密集型任务的生成质量。该工作为RAG中的知识协同提供了新的范式。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.167/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 792, \"height\": 369, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.167/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1602, \"height\": 678, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.167/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 714, \"height\": 228, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.167/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 728, \"height\": 386, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.167/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 722, \"height\": 270, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.167/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 802, \"height\": 295, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.167/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 780, \"height\": 338, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.167/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1585, \"height\": 330, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.167/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1537, \"height\": 1784, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.167/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1553, \"height\": 1857, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.167/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1531, \"height\": 1791, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.167/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1614, \"height\": 909, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.167/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 792, \"height\": 349, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.167/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 791, \"height\": 278, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.167/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 773, \"height\": 234, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.167/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 755, \"height\": 294, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.167/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1462, \"height\": 471, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.167/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1544, \"height\": 393, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.167/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1509, \"height\": 716, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.167/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1502, \"height\": 361, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.167/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1661, \"height\": 2053, \"label\": \"Table\"}]"
motivation: 当前RAG方法未能充分利用参数知识与检索知识的协同作用。
method: 提出CoCoA框架，通过多智能体协作进行条件知识归纳。
result: 实验表明该方法显著提升了知识密集型任务的性能。
conclusion: 多智能体协作能有效增强RAG中参数与检索知识的协同。
---

## Abstract
Retrieval-Augmented Generation (RAG) enhances Large Language Models (LLMs), especially for knowledge-intensive tasks. Despite its advantages, current RAG methods often struggle to fully exploit knowledge during generation. In particular, the synergy between the model’s internal parametric knowledge and external retrieved knowledge remains limited. Retrieved contents may sometimes mislead generation, while certain generated content can guide the model toward more accurate outputs. In this work, we propose Collaborative Chain-of-Agents, a framework designed to enhance explicitly synergy over both parametric and retrieved knowledge. Specifically, we first introduce CoCoA-zero, a multi-agent RAG framework that first performs conditional knowledge induction and then reasons answers. Building on this, we develop CoCoA, a long-chain training strategy that synthesizes extended multi-agent reasoning trajectories from CoCoA-zero to fine-tune the LLM. This strategy enhances the model’s capability to explicitly integrate and jointly leverage parametric and retrieved knowledge. Experimental results demonstrate the superiority of CoCoA in open-domain QA and multi-hop QA.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：现有检索增强生成（RAG）方法在生成过程中未能充分协同利用模型内部的参数知识（parametric knowledge）与外部的检索知识（retrieved knowledge），存在两种知识互相干扰或未被有效融合的问题。例如，检索的噪声内容可能误导生成，而仅依赖参数知识也可能因过时或幻觉产生错误答案。
- **研究动机**：观察到在某些场景下，直接生成（不使用检索）的性能甚至优于RAG，而简单地将内部生成内容与检索内容拼接（“Merge”方法）虽能提升但效果不稳定。这表明需要更精细的协同机制来联合利用两类知识，实现优势互补。

## 二、论文提出的方法论

### 2.1 核心思想
- 提出 **CoCoA（Collaborative Chain-of-Agents）** 框架，通过多智能体协作和长链训练，显式增强参数知识与检索知识的协同。
- 框架分为两个阶段：**CoCoA-zero（无训练的多智能体推理框架）** 和 **CoCoA（基于CoCoA-zero的长链训练策略）**。

### 2.2 关键技术细节

#### CoCoA-zero（多智能体推理框架）
- **阶段一：知识归纳（Knowledge Induction）**  
  - **内部知识智能体**：基于问题直接生成候选答案 \(a_{in}\)，再根据问题与答案生成内部知识段落 \(s_{in}\)（条件归纳）。  
  - **外部知识智能体**：先检索相关段落 \(C\)，基于问题与 \(C\) 生成外部候选答案 \(a_{ex}\)，再生成外部知识段落 \(s_{ex}\)。
- **阶段二：高层决策（High-level Decision Making）**  
  - **决策智能体**：输入问题、内部知识段落与候选、外部知识段落与候选，采用链式思考（CoT）推理，输出最终答案 \(\hat{a}\) 及推理路径。

#### CoCoA（长链训练策略）
- **监督微调（SFT）**：将CoCoA-zero的中间结果（\(s_{in}, s_{ex}, cot_a, \hat{a}\)）拼接成统一长回答 \(y\)，以端到端方式微调LLM，损失函数为：
  \[
  L_{SFT} = -\mathbb{E}_{(x,y)\sim D} \left[ \log P_\theta(s_{in}, s_{ex}, cot_a, \hat{a} \mid q, d) \right]
  \]
- **偏好优化（DPO）**：将CoCoA-zero的输出作为正样本 \(y_+\)，将零样本单智能体变体的输出作为负样本 \(y_-\)，使用DPO+RPO损失进行对齐，鼓励模型偏好协作式输出。

### 2.3 算法流程（文字说明）
1. 对于每个查询 \(q\)，CoCoA-zero执行：
   - 内部智能体：生成 \(a_{in}\) → 条件归纳得 \(s_{in}\)。
   - 检索文档 \(C\) → 外部智能体：生成 \(a_{ex}\) → 条件归纳得 \(s_{ex}\)。
   - 决策智能体：基于 \(s_{in}, a_{in}, s_{ex}, a_{ex}\) 推理得到最终答案 \(\hat{a}\)。
2. 若进行训练，则将上述所有中间结果拼接成 \(y\)，用于SFT或DPO训练。

## 三、实验设计

### 3.1 数据集与任务
- **开放域问答（Open-domain QA）**：WebQuestions、TriviaQA。
- **多跳问答（Multi-hop QA）**：2WikiMultiHopQA、HotpotQA。
- 训练数据：从HotpotQA、2WikiMultiHopQA、WebQuestions训练集中各抽取子集，经CoCoA-zero合成并基于正确答案过滤，得到6.8k SFT样本；DPO数据从零样本错误的1151个样本中获得。

### 3.2 评估指标
- Exact Match (EM)、F1分数（非严格EM）。

### 3.3 对比方法
- **无训练方法**：StandardRAG、CoT、GenRead、CoN、SURE、CoCoA-zero。
- **训练方法**：Self-RAG（7B/13B）、DeepSeek-R1-Distill-8B、InstructRAG-8B、CoCoA-SFT-8B、CoCoA-DPO-8B。
- 所有检索方法均使用top-5文档（Contriever检索器）。

## 四、资源与算力
- **模型**：LLaMA3.1-8B，使用LoRA微调（r=16，α=16，dropout=0.05）。
- **训练**：
  - SFT：5个epoch，学习率3e-5，batch size=1，梯度累积4。
  - DPO：β=0.2，α=0.2（RPO），学习率5e-6。
- **硬件**：单张A100 GPU（80GB或40GB内存）。未明确说明训练时长，但表明使用vLLM进行加速推理。

## 五、实验数量与充分性

### 主要实验
1. **主实验结果（Table 1）**：在四个数据集上对比10+种方法，CoCoA-DPO在多数指标上取得最优或次优。
2. **消融实验一（Table 2）**：分析CoCoA-zero中各组件（内部/外部归纳、决策）的影响，验证每个模块的必要性。
3. **消融实验二（Table 3）**：对比长链训练（Long-DPO/SFT）与短链训练（Short-SFT、独立训练）的效果。
4. **内部条件归纳分析（Figure 3）**：展示内部知识生成的成功与失败比例。
5. **定性分析（Figure 4）**：分析CoCoA-zero在不同回答组合下的表现。
6. **K值鲁棒性分析（Figure 6）**：将文档数量从1变到20，考察性能变化。
7. **推理效率分析（Table 4）**：对比平均输入/输出token数与平均分数。
8. **非QA任务泛化性（Figure 5）**：在事实验证（PubHealth）和选择题（ARC-C）上测试性能变化。
9. **不同模型规模（Figure 7）**：验证CoCoA-zero在不同参数量LLM上的表现。
10. **不同检索器（Figure 8）**：使用BM25、DPR、Contriever、E5进行鲁棒性验证。

### 充分性评价
实验覆盖了多种数据集、多类基线（包括无训练/有训练、不同规模）、多个消融维度，并分析了鲁棒性、泛化性和效率，设计较为充分。所有比较均尽力保证公平（如使用相同检索器、相同top-k等）。

## 六、论文的主要结论与发现
1. **知识协同必要性**：参数知识与检索知识各有优劣，需要显式协同而非简单拼接。
2. **多智能体框架有效**：CoCoA-zero在无训练下已显著优于StandardRAG及其他无训练方法。
3. **长链训练提升显著**：CoCoA (SFT/DPO) 在多数数据集上达到SOTA，尤其2WikiMultiHopQA上EM提升15.2%。
4. **泛化性好**：在非QA任务上性能未下降，对检索器数量、检索器类型具有鲁棒性。
5. **推理效率权衡**：输出token量约为CoT的3倍，但远少于推理模型（如DeepSeek-R1），性能提升显著。

## 七、优点
- **方法创新性**：首次提出显式协同参数知识与检索知识的多智能体链式框架，并结合长链训练进行端到端优化。
- **框架灵活性**：CoCoA-zero既可独立使用，也可作为数据合成管道产生监督信号。
- **消融实验全面**：解耦了内部/外部知识归纳、决策机制、训练策略等组件，验证各自贡献。
- **鲁棒性强**：在不同检索器、文档数量、模型规模下表现稳定。
- **实用导向**：提供推理效率分析，说明在性能和计算开销之间的良好平衡。

## 八、不足与局限
- **应用场景局限**：当前设计针对特定智能体协作模式（内部+外部+决策），未探讨更复杂或替代的多智能体架构。
- **规模探索不足**：仅验证8B模型，未系统研究更大模型（如70B）或更大数据量下的scaling behavior。
- **推理开销**：虽然优于推理模型，但输出token消耗比常规RAG方法大（约600 tokens），实际部署时仍需关注。
- **训练数据依赖**：训练数据来自CoCoA-zero合成并过滤，质量依赖原始数据集和注释器，可能存在偏差。
- **未考虑多语言/跨语言场景**：实验仅在英文数据集上进行。
- **长期知识更新问题**：框架依赖固定检索库，未探讨动态知识更新或增量学习情况。

（完）
