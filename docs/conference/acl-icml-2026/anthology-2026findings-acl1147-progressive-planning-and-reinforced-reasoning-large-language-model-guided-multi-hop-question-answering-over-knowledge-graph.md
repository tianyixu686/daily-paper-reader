---
title: "Progressive Planning and Reinforced Reasoning: Large Language Model-Guided Multi-hop Question Answering over Knowledge Graph"
title_zh: 渐进规划与强化推理：大模型引导的知识图谱多跳问答
authors: "Xiang Li, Runhai Jiao, Ruifan Li, Dongnan Wu, Ruojiao Qiao, Lei Liu"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.1147.pdf"
tags: ["query:mr"]
score: 8.0
evidence: 大模型引导规划的多跳知识图谱问答
tldr: 知识图谱上的多跳问答中，强化学习代理缺乏中间指导和长期预见能力。本文提出PPRR框架，利用大语言模型作多跳推理规划器，将复杂问题分解为子目标，引导代理渐进式探索。实验结果显示，PPRR在多个KGQA基准上大幅提升准确率和效率，有效缓解了无效探索问题。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1147/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 589, \"height\": 599, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1147/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1220, \"height\": 822, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1147/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1087, \"height\": 1030, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1147/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 790, \"height\": 408, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1147/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1298, \"height\": 733, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1147/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 724, \"height\": 399, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1147/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 732, \"height\": 407, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1147/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1272, \"height\": 874, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1147/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 793, \"height\": 212, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1147/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 795, \"height\": 260, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1147/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 795, \"height\": 345, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1147/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 639, \"height\": 334, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1147/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 791, \"height\": 311, \"label\": \"Table\"}]"
motivation: 强化学习代理在多跳知识图谱问答中缺乏有效中间指导和长期预见，导致无效探索。
method: 提出PPRR框架，利用大语言模型生成分解计划，引导强化学习代理渐进推理。
result: 在多个KGQA基准上，PPRR显著提升准确率并减少无效探索步骤。
conclusion: 大模型作为规划器能有效提升知识图谱上多跳推理的稳定性和效率。
---

## Abstract
Reinforcement learning, with its interpretable path reasoning, has emerged as a promising paradigm for multi-hop question answering over knowledge graphs. However, existing approaches suffer from two inherent limitations: (1) lacking effective intermediate guidance, agents often fall into aimless exploration when confronted with complex multi-hop questions; and (2) policy networks focus on local neighborhood information, making it difficult to anticipate the long-term consequences of decisions. To address these challenges, we propose a Progressive Planning and Reinforced Reasoning (PPRR) framework. Specifically, we introduce large language models as multi-hop reasoning planners, converting decomposed sub-question sequences into stepwise decision guidance and thereby granting the agent human-like, step-by-step problem-solving capabilities. In addition, we design a structure-aware lookahead policy network, which explicitly models inter-node dependencies along the multi-hop reasoning process and performs lookahead value evaluations for candidate actions, thereby enhancing the agent’s global state awareness and decision foresight in complex environments. Finally, we conducted extensive experiments on four public multi-hop question answering benchmarks and one domain-specific dataset. The results demonstrate that our framework surpasses state-of-the-art methods while demonstrating strong generalization.

---

## 论文详细总结（自动生成）

好的，这是对您提供的论文《Progressive Planning and Reinforced Reasoning: Large Language Model-Guided Multi-hop Question Answering over Knowledge Graph》的详细中文总结。

## 1. 核心问题与整体含义（研究动机和背景）
- **核心问题**：现有基于强化学习（RL）的知识图谱多跳问答（KGQA）方法面临两大固有缺陷：
    1.  **缺乏有效的中间指导**：在没有明确规划的情况下，智能体在复杂多跳问题上容易陷入盲目探索，导致学习过程不稳定（如图1所示，性能出现先升后降的“崩塌”现象）和收敛缓慢。
    2.  **缺乏长期预见能力**：策略网络通常仅依赖局部邻域信息做出决策，无法预判当前动作的长期后果，导致在复杂查询中产生无效的探索。
- **研究动机**：大型语言模型（LLM）具备强大的常识推理和规划能力，而RL擅长在结构化环境中进行探索。将两者结合，利用LLM为RL提供宏观的、分步骤的决策指导，有望克服上述局限。

## 2. 方法论：PPRR框架
- **核心思想**：提出一种“渐进规划与强化推理”（PPRR）框架，将LLM的“宏观语义规划”与RL的“微观路径推理”紧密耦合。
- **关键技术细节**：
    1.  **渐进规划**：
        - 利用LLM（如GPT-4）将原始复杂问题分解为有序的**子问题序列**。子问题与知识图谱上的多跳路径语义对齐（如问题“杀死比尔”中演员出演电影的语言 → 子问题：1. 演员是谁？2. 出演的电影？3. 电影的语言？）。
        - **对齐验证**：对每个子问题，计算其与KG中候选关系的相似度，若低于阈值（τ=0.6），则触发重新分解，以缓解LLM的幻觉问题。
        - **训练专用**：子问题分解仅在模型训练阶段使用，以将“规划思维”内化到策略网络中，测试时无需调用LLM，从而保证推理效率。
    2.  **强化推理**：
        - 将多跳问答建模为马尔可夫决策过程（MDP）。状态包含问题、起始实体、当前实体和历史路径；动作为选择当前实体节点的出边（关系-实体对）。
        - **混合奖励设计**：
            - **中间奖励**：计算当前所选关系与对应子问题的预选最优关系之间的余弦相似度，形成逐跳的指导信号（公式 1-2）。
            - **最终奖励**：利用知识图嵌入（KGE）模型的评分函数（而非简单的0/1）提供更稠密的最终奖励（公式 3），缓解奖励稀疏问题。
    3.  **结构感知的前瞻策略网络 (LEGAT)**：
        - **核心**：每个动作的权重不再是单纯的局部注意力，而是用一个“前瞻分数”代替。
        - **前瞻分数计算**：通过一个轻量级神经网络，对候选动作的长期价值进行评估。该分数不仅考虑当前子问题的匹配度，还预估了候选实体的下一跳（出边）质量（公式 8-10）。
        - **作用**：能够在决策之前就预先筛选出“局部看似正确但全局无效”的路径（如图 3、图 5 的案例所示），从而实现**预决策剪枝**，显著减少盲目探索。
- **算法流程**：训练时，智能体在子问题指导下逐步探索KG，每一步由LEGAT策略网络选择动作，并根据混合奖励进行更新（REINFORCE算法，公式 12-13）。

## 3. 实验设计
- **数据集与场景**：
    - **公开基准**：在4个标准KGQA数据集上进行评估：WebQSP, PathQuestion (PQ), PathQuestion-Large (PQL), MetaQA。这些数据集包含不同跳数（如Mix, 3H）的复杂查询。
    - **领域数据集**：自建一个电力领域的QA数据集（故障诊断，>3跳），用于评估框架的**领域泛化能力**。
- **基准方法 (Baselines)**：
    - 对比了3大类共15种方法：
        - **神经网络类**：KVMemNN, IRN, EmbedKGQA, DRN, BSEM。
        - **图神经网络类**：PullNet, 2HR-DR, HyperTransformer, Compath。
        - **强化学习类**：SRN, ARN, AR2N, HRN, SCR, CRF。
    - 同时与**纯LLM代理方法**（如ToG, PoG, DoG）进行对比。

## 4. 资源与算力
- 论文在**实现细节**部分明确说明：
    - **GPU 型号与数量**：2块 NVIDIA A40 GPU。
    - **训练时长**：论文未给出具体的训练总时长。

## 5. 实验数量与充分性
- **实验数量**：非常充分。论文共报告了以下类型实验：
    - **主实验**：在4个公开数据集上与15种基线方法进行对比。
    - **纯LLM方法对比**：与4种最先进的LLM代理方法进行准确率和效率对比。
    - **消融实验**：分别移除“渐进规划 (PP)”和“前瞻策略网络 (LEGAT)”两个核心组件，观察性能变化。
    - **效率分析**：绘制了收敛曲线，与基线方法SCR对比。
    - **案例研究**：展示了模型在实际案例中的推理路径和注意力权重，直观验证其有效性。
    - **领域适用性实验**：在电力领域数据集上进行测试。
    - **超参数分析**：对中间奖励系数λ进行了详细分析。
    - **不同LLM分析**：测试了使用Llama3, Deepseek, ChatGPT, GPT-4作为规划器时的性能差异。
    - **少样本研究 (Few-shot)**：在仅20%训练数据的情况下测试性能。
- **充分性与公平性**：实验设计**非常充分和客观**。涵盖了主流公开数据集和领域数据，对比了最前沿的SOTA方法，并通过消融、案例、超参数等多角度验证了方法的有效性和鲁棒性。其公平性体现在对比基线时涵盖了多个技术流派，并直接对比了计算延迟。

## 6. 主要结论与发现
1.  **性能领先**：PPRR在4个公开基准数据集上均取得了最优的Hits@1指标，大幅超越所有基线方法（如在最难的WebQSP上比第二名CRF高出5%）。
2.  **效率与效果兼具**：与纯LLM方法相比，PPRR在推理速度上具有压倒性优势（0.17秒/样本 vs. 8.5秒/样本），同时在MetaQA-3H上取得了更高的准确率。
3.  **消融实验验证**：移除了“渐进规划”或“前瞻网络”后，模型性能显著下降，验证了两者都是PPRR成功的关键组成部分。
4.  **成功内化规划能力**：通过训练，RL智能体成功将LLM的规划能力内化为自身的推理策略，这体现在测试时无LLM引导仍能保持高性能。
5.  **领域泛化能力强**：在电力领域的特定数据集上，PPRR依然能稳定超越所有对比的基线方法。

## 7. 优点（亮点）
- **方法上的创新**：
    - 将LLM视为“规划器”而非“评分器”，实现了从宏观语义到微观动作的**渐进式、对齐式指导**，思路清晰且有效。
    - 提出的**LEGAT前瞻策略网络**是核心亮点。它通过显式建模“动作的长期价值”进行预决策剪枝，跳出了传统RL“走一步看一步”的局部最优陷阱，实现了真正的“思考后再行动”。
- **实验上的亮点**：
    - 实验设计非常全面，评估维度丰富，置信度高。
    - 通过与纯LLM方法的对比，突出强调了PPRR在**准确率与推理效率**之间的优越平衡，极具实用价值。
    - 在多个不同场景（公开数据、领域数据、少样本）下的验证，有力地证明了方法的鲁棒性和泛化能力。

## 8. 不足与局限
- **依赖KG结构**：当前方法的规划和推理效果仍在一定程度上依赖底层知识图谱的**结构完整性**。对于高度不完整的KG，其推理路径可能会受到限制。
- **复杂逻辑查询的处理**：论文指出，该方法在处理**多约束比较性查询**（如“谁主演了比电影A和电影B都老的电影？”）时，可能需要更精细的语义规划与动作执行的协调机制。
- **未见关系的泛化**：论文未系统性地评估该框架在**未见关系**上的泛化能力。对于一个全新的、从未在训练集中出现的关系，模型是否能有效处理，尚待验证。
- **LLM依赖**：虽然只在训练时使用LLM，但其生成的子问题质量依然直接影响模型性能。论文中虽设置了验证机制，但并不能完全消除LLM输出中的偏差或错误带来的风险。

（完）
