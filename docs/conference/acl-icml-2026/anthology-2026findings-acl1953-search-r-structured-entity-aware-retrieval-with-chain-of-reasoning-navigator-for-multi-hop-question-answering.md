---
title: "SEARCH-R: Structured Entity-Aware Retrieval with Chain-of-Reasoning Navigator for Multi-hop Question Answering"
title_zh: SEARCH-R：基于链式推理导航的结构化实体感知多跳问答检索
authors: "FU Yuqing, Yimin Deng, Wanyu Wang, Yuhao Wang, Yejing Wang, Hongshi Liu, Yiqi Wang, Xiao Han, Maolin Wang, Guoshuai Zhao, Yi Chang, Xiangyu Zhao"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.1953.pdf"
tags: ["query:mr"]
score: 8.0
evidence: 基于链式推理的结构化实体感知检索用于多跳问答
tldr: 多跳问答中推理路径生成缺乏有效控制且检索易受影响。SEARCH-R提出结构化实体感知检索与链式推理导航器，通过显式控制推理步序和实体检索，提升路径准确性。在多个数据集上，该方法在答案准确性和推理一致性方面取得改善。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1953/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1654, \"height\": 849, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1953/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 565, \"height\": 581, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1953/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 791, \"height\": 438, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1953/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 762, \"height\": 225, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1953/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 841, \"height\": 345, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1953/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1586, \"height\": 737, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1953/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 680, \"height\": 248, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1953/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 753, \"height\": 198, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1953/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 761, \"height\": 978, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1953/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 832, \"height\": 295, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1953/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 603, \"height\": 249, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1953/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 749, \"height\": 397, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1953/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 694, \"height\": 297, \"label\": \"Table\"}]"
motivation: 现有方法对推理路径生成控制不足，且检索易受无关信息干扰，导致错误传播。
method: 提出SEARCH-R，采用链式推理导航器逐步生成子问题，并融合结构化实体感知检索。
result: 在多个多跳QA基准上，SEARCH-R在答案准确性和推理连贯性上显著超越基线。
conclusion: 结构化推理路径控制与实体级检索的结合有效提升了多跳问答的鲁棒性。
---

## Abstract
Multi-hop Question Answering (MHQA) aims to answer questions that require multi-step reasoning. The complexity of user queries, coupled with potential knowledge deficiencies in Large Language Models (LLMs), gives rise to two pivotal challenges that underpin the performance on this task: the correct identification of the reasoning path and the accurate retrieval of essential knowledge. Existing approaches primarily rely on prompt-based methods to generate reasoning paths, which are further combined with traditional sparse or dense retrieval to produce the final answer. However, the generation of reasoning paths commonly lacks effective control over the generative process, thus leading the reasoning astray. Meanwhile, the retrieval methods over-rely on knowledge matching or similarity scores rather than evaluating the practical utility of the information, resulting in retrieving homogeneous or non-useful information. Therefore, we propose a Structured Entity-Aware Retrieval with Chain-of-Reasoning Navigator framework named SEARCH-R. Specifically, SEARCH-R trains an end-to-end reasoning path navigator, which is able to provide a powerful sub-question decomposer by fine-tuning the Llama3.1-8B model. Moreover, a novel dependency tree-based retrieval is designed to evaluate the informational contribution of the document quantitatively. Extensive experiments on three challenging multi-hop datasets validate the effectiveness of the proposed framework. The code and dataset are available at: https://github.com/Applied-Machine-Learning-Lab/ACL2026_SEARCH-R.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究动机**：多跳问答（MHQA）需要模型进行多步推理，从多个文档中整合信息。现有方法存在两大瓶颈：
  - **推理路径生成缺乏有效控制**：基于提示的方法（如Chain-of-Thought）生成的子问题随机性高，容易偏离正确推理轨迹；非提示方法则过度强调逻辑正确性而忽略最终答案准确性。
  - **检索质量不足**：传统稀疏/稠密检索仅依据关键词或语义相似度，容易检索到同质化或无关信息，无法评估文档对当前问题的实际信息贡献。
- **核心问题**：如何生成高质量的推理路径，并检索到真正有助于回答问题的知识，从而提升MHQA系统的准确性和鲁棒性。

### 2. 论文提出的方法论

- **整体框架（SEARCH-R）**：一个三阶段多跳问答框架，包括推理路径生成、知识检索、答案生成。

- **阶段一：推理路径生成（Reasoning Path Generation）**
  - **数据构造**：利用LLM（如GPT-4o-mini）为每个复杂问题生成多条不同的子问题序列（推理路径），根据最终答案与真实答案的一致性筛选出高质量路径（仅保留正确路径）。
  - **监督微调（SFT）**：使用筛选出的300对高质量“问题-子问题”数据微调Llama3.1-8B模型作为初始子问题分解器。
  - **强化学习（PPO）**：进一步训练一个奖励模型，以F1分数作为奖励信号，使用PPO算法优化策略网络，使模型学会生成更优的子问题（兼顾逻辑正确性和答案导向性）。
  - **关键公式**：
    - 奖励模型损失：\( L_{RM} = \frac{1}{N}\sum (r_p - r_t)^2 \)，其中 \( r_t = \text{F1}(a_f, a_g) \)。
    - PPO优化目标：\( L^{CLIP}(\theta) = \mathbb{E}[\min(r_t(\theta)\hat{A}_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)\hat{A}_t)] \)。

- **阶段二：知识检索（Knowledge Retrieval）**
  - **实体信息量度量（QIR）**：基于依存句法树，计算文档中每个实体在句子中的最大子节点数（max_child），累加得到实体的重要性得分。对所有实体排序得到列表 \( M_r \)，文档的信息量得分 \( s_{doc} = \sum_{e_q \in E_q} \frac{1}{M_r(e_q)} \)。
  - **双路径检索**：融合基于实体信息量的top-k文档（实验选定k=15）和基于稠密相似度的top-10文档，共同作为后续回答的上下文。

- **阶段三：答案生成（Answer Generation）**
  - 迭代处理每个子问题：先判断是否需要重写子问题（根据已获得的答案填充缺失实体），然后结合检索到的知识回答问题，最终整合所有子答案得出最终答案。

### 3. 实验设计

- **数据集**：三个多跳问答基准数据集：
  - **MuSiQue**（约2.5万问题，1-4跳），**HotpotQA**（约9万问题，Wikipedia），**2WikiMQA**（约16.7万问题，Wikipedia三元组）。
  - 使用与ChainRAG一致的数据划分与预处理方式。
- **基准方法（Baselines）**：NativeRAG（单次RAG）、Iter-RetGen（迭代检索生成）、HippoRAG（图记忆）、ChainRAG（句子图检索）、Search-R1（基于强化学习的代理方法）。还尝试了GraphRAG但表现差被排除。
- **骨干模型**：Llama3.1-8B、DeepSeek-V3、GPT-4o-mini（用于最终答案生成或全流程）。
- **指标**：F1分数和精确匹配（EM）分数。
- **主要实验结果**（表2）：
  - 在MuSiQue上，SEARCH-R（GPT-4o-mini作为答案生成器）取得F1=55.68%，EM=45.00%，超越所有基线。
  - 在HotpotQA上，F1=60.06%，EM=44.00%；在2Wiki上，F1=63.86%，EM=52.50%。
- **消融实验**（表3）：分别移除子问题分解器（Dec.）、定量信息检索（QIR）、PPO微调，均导致性能下降，验证各模块有效性。
- **额外分析**：超参数（k值）影响（图3）、QIR模块单独作用与噪声鲁棒性（表7）、PPO vs 仅SFT数据扩展（表4）、小模型vs大模型分解能力对比（表5）、推理时间对比（表10表）。

### 4. 资源与算力

- **硬件**：4块 Intel Xeon Gold 6348 CPU（2.60GHz） + 4块 NVIDIA A800-80GB GPU。
- **训练时长**：
  - SFT微调与奖励模型训练：各少于1小时。
  - PPO训练：约3小时。
- **备注**：论文明确说明了GPU型号、数量和训练耗时。

### 5. 实验数量与充分性

- **数量**：主要实验涵盖3个数据集×1-4种骨干组合×多种基线；消融实验包括3个模块移除（表3）；还有超参数分析（图3）、QIR深入分析（表7）、PPO vs SFT数据对比（表4）、GPT-4o对比（表5）、时间分析（表10）等。
- **充分性与公平性**：
  - 实验设计较为全面：对比了当前主流方法（包括代理型方法Search-R1、图方法ChainRAG等），且在多个骨干上验证。
  - 消融实验回答了各组件贡献；PPO对比了等量数据SFT，控制了变量。
  - 不足之处：训练数据仅从MuSiQue中抽取300个样本，虽然表现泛化，但未必充分覆盖其他领域的复杂性；未在更多领域（如医学、金融）验证；基线运行环境是否完全一致未明确说明（如ChainRAG的原始报告数据 vs 自己复现的结果有差异）。

### 6. 论文的主要结论与发现

- **子问题分解能力可以高效学习**：仅用8B参数的小模型通过SFT+PPO训练后，分解质量可超越无专门训练的GPT-4o（表5）。
- **PPO优于仅SFT**：PPO优化后的分解器无论在逻辑连贯性还是最终答案准确度上均优于仅SFT模型，且增益不能简单通过增加SFT数据量达到（表4）。
- **实体信息量检索提升检索质量**：融合依存句法树的文档信息量评分与稠密检索，能有效补充相似度检索的不足，尤其当识别实体部分失败时仍具鲁棒性（表7）。
- **双路径检索协同效应**：单独移除QIR或稠密检索均导致F1下降，联合使用最佳。
- **泛化能力**：仅在MuSiQue训练，在HotpotQA和2Wiki上同样有显著提升，说明分解器学到的是通用分解技能而非数据拟合。

### 7. 优点

- **方法论亮点**：
  - 端到端训练推理路径导航器，替代手工提示，控制更强。
  - 创新性地利用依存句法树量化实体对文档的信息贡献，超越传统语义相似度。
  - 将PPO用于生成子问题优化，奖励信号直接关联最终答案正确性，目标明确。
- **实验设计亮点**：
  - 多骨干、多数据集验证，展示方法通用性。
  - 消融实验设计清晰（移除每个模块），并提供额外的PPO vs SFT对比，分析严谨。
  - 对QIR进行了实体识别失败的鲁棒性测试，考虑实际应用风险。
- **效率**：小模型（8B）在低算力下完成训练（GPU小时数少），推理时间合理（每问题约18.8秒），优于需要构建句子图的ChainRAG。

### 8. 不足与局限

- **文献中已提及的局限**：
  - 检索模块依赖外部依存解析器和NER工具，可能引入流水线误差和领域适应性限制。
  - 训练数据质量受初始LLM生成质量影响，若生成多样性不足，上限将受限。
- **实验覆盖不足**：
  - 仅使用三个公开数据集，未涉及其他领域（如医学、法律）或更大规模数据。
  - 未对伪相关反馈或不同解析器进行灵敏度分析。
- **偏差风险**：训练数据仅从MuSiQue采样300条，虽表现泛化，但可能隐含对特定句子结构和实体类型的偏好。
- **应用限制**：框架中“重写子问题”的机制依赖上一答案，若生成错误答案，错误会累积传播。实验未专门分析错误传播情况。
- **复现细节**：几个基线（如ChainRAG）的原始报告结果与作者自己复现结果有差异（表9注），可能影响公平比较的标准一致性。

（完）
