---
title: "From Query to Logic: Ontology-Driven Multi-Hop Reasoning in LLMs"
title_zh: 从查询到逻辑：本体驱动的大模型多跳推理
authors: "Haonan Bian, Yutao Qi, Rui Yang, Yuanxi Che, Jiaqian Wang, Heming Xia, Ranran Zhen"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.687.pdf"
tags: ["query:mr"]
score: 8.0
evidence: 本体驱动的多跳推理与知识图谱
tldr: 大语言模型在复杂多跳问答中难以捕捉深层概念关系。本文提出ORACLE框架，利用LLM动态构建问题特定知识本体，将其转化为一阶逻辑推理链进行系统推理。实验表明，该方法在多个多跳问答基准上显著超越现有方法，尤其在需要结构化推理的任务中优势明显。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.687/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1564, \"height\": 786, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.687/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 773, \"height\": 482, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.687/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 757, \"height\": 547, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.687/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 770, \"height\": 481, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.687/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1576, \"height\": 412, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.687/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 764, \"height\": 477, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.687/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1579, \"height\": 572, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.687/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 788, \"height\": 697, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.687/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 817, \"height\": 903, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.687/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1382, \"height\": 316, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.687/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1358, \"height\": 268, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.687/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1558, \"height\": 337, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.687/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1620, \"height\": 1112, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.687/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1670, \"height\": 685, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.687/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1676, \"height\": 1032, \"label\": \"Table\"}]"
motivation: 大语言模型在复杂多跳问答中缺乏结构化推理能力，难以处理深层概念关系。
method: 提出ORACLE框架，动态构建问题特定的知识本体并转化为一阶逻辑推理链。
result: 在多个多跳推理基准上，ORACLE显著提升准确率，尤其结构化推理任务。
conclusion: 本体驱动的一阶逻辑链有效增强了LLM在多跳推理中的逻辑一致性。
---

## Abstract
Large Language Models (LLMs), despite their success in question answering, exhibit limitations in complex multi-hop question answering (MQA) tasks that necessitate non-linear, structured reasoning. This limitation stems from their inability to adequately capture deep conceptual relationships between entities. To overcome this challenge, we present ORACLE (Ontology-driven Reasoning And Chain for Logical Elucidation), a training-free framework that combines LLMs’ generative capabilities with the structural benefits of knowledge graphs. Our approach operates through three stages: (1) dynamic construction of question-specific knowledge ontologies using LLMs, (2) transformation of these ontologies into First-Order Logic (FOL) reasoning chains, and (3) systematic decomposition of the original query into logically coherent sub-questions. Extensive experiments across a diverse set of models and standard MQA benchmarks demonstrate that our framework achieves competitive performance while producing more interpretable reasoning chains.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：大语言模型（LLM）在复杂多跳问答（MQA）任务中表现不佳，难以进行非线性、结构化的推理。LLM倾向于依赖训练数据中的“猜测”而非真正的推理，尤其在需要捕捉实体间深层概念关系时失败。
- **研究动机**：现有方法（如Chain-of-Thought提示、检索增强生成RAG、知识图谱路径引导）虽有一定效果，但多聚焦于实体表面提及或静态图谱路径，忽略了实体所属的概念类别及其层次关系。作者认为，复杂推理的本质在于实体背后的“概念”以及概念间的层级结构。
- **整体含义**：本文提出将知识工程中的本体论引入LLM推理过程，通过动态构建问题中心的知识本体，提供结构化的语义骨架，从而引导LLM进行更忠实、可解释的多跳推理。

## 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程
- **核心思想**：ORACLE（Ontology-driven Reasoning And Chain for Logical Elucidation）是一个无需训练的框架，结合LLM的生成能力与知识图谱的结构优势，通过三个阶段实现结构化推理。
- **关键技术细节**：
  - **阶段一：本体提取（Ontology Extraction）**：LLM从自然语言问题中动态提取问题特定的轻量级本体（O_Q），包括实体类（C_Q）和关系（R_Q）。关键点是侧重提取实体类别（如 `type(m, Monarch)`），并预测答案实体的类别。例如问题 `“What government followed the monarch who retranslated the Reflections into French from the country that allied with America after the Battle of Saratoga?”` 中提取出类（Book, Monarch, Country, Government）和关系（retranslated, rulerOf, alliedWith, finished, followed）。
  - **阶段二：FOL构建（FOL Construction）**：将本体转换为精确的一阶逻辑公式（Φ）。关系映射为谓词，实体类别作为变量的类型约束。例如 `∃ans, m, c ∧ retranslated(m, The Reflections, French) ∧ rulerOf(m, c) ∧ alliedWith(c, America) ∧ finished(Saratoga, America) ∧ followed(c, ans)`，并附上类型声明。
  - **阶段三：子问题分解（Sub-question Decomposition）**：基于原问题、本体和FOL公式，LLM生成有序的子问题序列（Q_1, ..., Q_n）。每个子问题答案通过检索和推理获得，前一步的答案通过占位符注入到后续子问题，形成连贯推理链。算法流程见Algorithm 1（使用LLM生成本体→FOL→子问题，然后循环执行每个子问题）。
- **公式/算法**：文中给出了本体提取公式 `O_Q = (C_Q, R_Q) = f_LLM(Q)`，以及FOL公式的符号化表示。整体算法通过伪代码描述（Algorithm 1），明确各阶段输入输出。

## 3. 实验设计：数据集、基准、对比方法
- **数据集**：HotPotQA（500 samples from dev set）、2WikiMQA（500 samples from dev set）、MuSiQue（500 samples，按2:2:1比例混合2跳、3跳、4跳问题）。作者指出HotPotQA存在推理捷径，MuSiQue侧重检索，而2WikiMQA更纯推理，因此是最佳测试床。
- **基准（metrics）**：Exact Match (EM) 和 F1 Score。
- **对比方法**：
  - **NoCoT**：直接回答，无额外推理。
  - **CoT**：链式思考（“Think step by step”）。
  - **RAG**：利用检索到的上下文直接回答。
  - **ReAct**：循环生成思考与动作（搜索/查找/结束）。
  - **LPKG**：从知识图谱学习分解模式，生成代码格式的计划。
  - **NoCoT (DeepSeek-R1)**：仅作为参考上限（灰色显示）。
- **额外实验**：还包括跨模型比较（GPT-4o-mini、Gemini-2.5-Flash、Qwen2.5系列7B/14B/32B/72B），以及GraphRAG-Bench医学子集上的泛化实验（Complex Reasoning和Fact Retrieval两类）。

## 4. 资源与算力
- **文中未明确说明使用的GPU型号、数量或训练时长**。原因是ORACLE是一个无需训练的框架，主实验使用GPT-3.5-turbo API，LLM作为推理引擎，不涉及模型微调。检索器使用数据集提供的黄金上下文（gold context）而非全量Wikipedia，以降低计算资源消耗。作者提到“Due to computational constraints, we relied on gold contexts”，但未给出具体硬件规格。

## 5. 实验数量与充分性
- **实验数量**：丰富且多维度。
  - 主实验在三个数据集上的性能对比（表1）。
  - 消融实验：去除本体提取（w/o Ontology）和去除FOL模块（w/o FOL）在三个数据集上的影响（表2）。
  - 细粒度分析：按2WikiMQA的推理类型（compositional, comparison, bridge_comparison, inference）对比F1分数（图2）。
  - 推理路径质量分析：计算Reasoning F1（定义在附录A.5），并分高/低质量组展示路径质量分布（图3-5）。
  - 跨模型评估：在7种不同模型上对比LPKG和ORACLE（表3）。
  - 效率分析：比较平均token消耗（表4）。
  - 提示敏感性分析：三种变体（原版、重述、重排）下EM/F1/Reasoning F1的变异系数<10%（表5）。
  - GraphRAG泛化实验：医学子集上对比Naive RAG和ORACLE（表6）。
  - 子问题数量偏差分析：与真实步数偏差对F1的影响（图6）。
  - 案例研究（表7-9）。
- **充分性与公平性**：实验设计较全面。但存在一定局限性：检索器使用数据集提供的黄金上下文而非全量Wikipedia，可能过滤掉噪声，但作者认为这有利于评估推理逻辑而非检索瓶颈。跨模型评估中未包含推理专用模型（如GPT-o1-mini），因为格式不符合要求。总体而言，实验充分性较好，但开放域设置下的泛化性未验证。

## 6. 论文的主要结论与发现
1. **ORACLE在多跳QA基准上达到最优或竞争性性能**：在HotPotQA、2WikiMQA和MuSiQue上，ORACLE平均EM最高（0.340），尤其在2WikiMQA上显著领先（EM 0.468，F1 0.547）。
2. **本体和FOL模块均不可或缺**：消融实验表明，去除FOL模块在所有数据集上性能下降最显著（尤其是复杂多跳任务）；去除本体模块在2WikiMQA上伤害更大，说明实体锚定对防止幻觉至关重要。
3. **推理路径质量更高且更忠实**：ORACLE产生的推理路径（Reasoning F1）更高（0.648 vs LPKG的0.611），且高质量路径（F1>0.5）占比更大；同时ORACLE的最终答案质量与推理路径质量正相关，而LPKG出现“路径虽差但答案正确”的情况，说明其依赖参数记忆而非忠实推理。
4. **跨模型泛化性强**：除Qwen2.5-7B外，ORACLE在多数模型上领先LPKG，说明对于足够强大的LLM，本体引导比静态知识注入更鲁棒。
5. **效率与性能良好平衡**：ORACLE的token消耗仅为LPKG的一半，性能却显著提升；比ReAct略高开销但效果大幅超越。
6. **细粒度优势**：在comparison、bridge_comparison、inference等复杂推理类型上优势明显，尤其在compositional问题上90.83%的路径达到高质量。

## 7. 优点：方法或实验设计上的亮点
- **方法创新**：
  - 首次将知识工程中的本体论引入LLM多跳推理，动态构建问题特定的轻量级本体，避免了静态KG的局限性。
  - 结合一阶逻辑(FOL)使得推理步骤显式化，增强可解释性和逻辑严谨性。
  - 无需模型训练，即插即用，适用于任意黑盒LLM。
- **实验设计亮点**：
  - 设计了“推理路径F1”度量，衡量模型生成路径与标准路径的吻合度，揭示了LLM推理忠实性的问题。
  - 细致的消融实验和跨模型评估验证了各组件的贡献和方法的泛化性。
  - 对比了token消耗，证明了效率优势。
  - 利用2WikiMQA的高质量推理标注进行细粒度分析，提供了深入的定性洞察。

## 8. 不足与局限
- **实验覆盖**：
  - 检索器使用数据集提供的黄金上下文而非全量Wikipedia，这可能导致高估推理能力（因去除了检索噪声）。作者明确承认此局限性，并建议未来扩展到开放域检索。
  - 未与GraphRAG等结构化检索系统进行全面端到端比较，仅给予补充实验（医学子集）。
  - 在较小型模型（如Qwen2.5-7B）上表现不如LPKG，表明本体抽象可能对弱模型有益但需注意参数容量限制。
- **偏差风险**：
  - 本体构建完全依赖LLM的参数量，缺乏外部验证，在专业领域可能失败。
  - 中间错误检测与恢复机制尚未设计，本体提取失败可能导致错误传播。
- **应用限制**：
  - 需要LLM具有足够的能力进行本体提取和FOL构建，对弱模型可能不友好。
  - 论文报告了token消耗作为计算成本，但未提供端到端延迟、API调用次数等更全面的效率分析。
  - 数值和时序推理仍然脆弱（如复合关系“mother-in-law”被简化为“mother”），表明当前LLM对微妙关系理解有限。
- **其他**：未包含推理专用模型（如o1）的对比，因为格式要求不符合；但提供了DeepSeek-R1作为参考。

（完）
