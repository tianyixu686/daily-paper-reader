---
title: Multi-Hop Knowledge Editing via Critic-Guided Multi-Agent Reasoning
title_zh: 通过批评指导的多智能体推理进行多跳知识编辑
authors: "Xudong Li, Yuhang Tian, Dandan Song, Zhijing Wu, Shuhao Zhang, Jun Yang, Yongyu Huo, Changzhi Zhou, Xinyu Zhang, Chenhao Li, Huipeng Ma, Luan Zhang, Yan Xu, Qian Liu"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.853.pdf"
tags: ["query:mr"]
score: 8.0
evidence: 批评指导的多智能体多跳推理用于知识编辑
tldr: 多跳知识编辑要求模型在更新事实后正确传播推理链，现有单向流水线易因早期错误导致级联失败。本文提出批评指导的多智能体推理框架，通过多个智能体合作与批评机制实现灵活的多跳推理和错误恢复。实验表明该方法在知识编辑基准上显著优于现有方法，尤其长链传播的鲁棒性突出。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.853/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 730, \"height\": 465, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.853/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1515, \"height\": 718, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.853/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 742, \"height\": 957, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.853/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 791, \"height\": 509, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.853/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1658, \"height\": 1239, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.853/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1656, \"height\": 366, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.853/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 808, \"height\": 331, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.853/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 813, \"height\": 559, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.853/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 818, \"height\": 219, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.853/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 814, \"height\": 494, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.853/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 581, \"height\": 336, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.853/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 831, \"height\": 524, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.853/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 805, \"height\": 260, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.853/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 810, \"height\": 147, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.853/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1455, \"height\": 223, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.853/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 446, \"height\": 294, \"label\": \"Table\"}]"
motivation: 多跳知识编辑中现有单向流水线在早期跳错误后无法恢复，鲁棒性差。
method: 提出批评指导的多智能体推理框架，利用多个智能体协作并设置批评机制进行错误纠正。
result: 在多个知识编辑基准上，该方法在准确性和鲁棒性上均大幅超越基线。
conclusion: 多智能体批评机制能有效提升多跳知识编辑的稳健性和长链传播能力。
---

## Abstract
Knowledge within large language models (LLMs) inevitably lags behind an evolving world, motivating knowledge editing methods that update facts without expensive retraining. In multi-hop knowledge editing, models must not only recall updated facts but also correctly propagate them through multi-step reasoning chains. However, most existing approaches rely on unidirectional, feed-forward pipelines, decomposing questions and retrieving edited facts in a rigid hop-wise sequence. This design is brittle: a minor retrieval error or logical mismatch at an early hop can become a silent failure that cascades to the final answer without an explicit recovery mechanism. To address this limitation, we propose Critic-Guided Multi-Agent Reasoning for Knowledge Editing (CARE), a framework for closed-loop post-edit reasoning. A Critic agent performs chain-level verification by checking both global coherence and step-wise correctness, and triggers bounded backtracking for iterative self-correction, while a Selector agent supplies high-fidelity, low-noise candidate pools from the edit store to enable effective revision. Experiments on MQuAKE-2002 and MQuAKE-hard demonstrate that CARE effectively mitigates error propagation, achieving a new state-of-the-art.

---

## 论文详细总结（自动生成）

# 论文中文总结

## 1. 核心问题与整体含义（研究动机与背景）

- **背景**：大型语言模型（LLM）依赖静态参数化知识，但现实世界知识不断变化，导致模型输出过时或错误。知识编辑（KE）旨在无需昂贵重训练即可更新事实。多跳知识编辑（MHKE）进一步要求模型在更新后正确传播多跳推理链。
- **核心问题**：现有主流方法采用单向、前馈流水线（如逐跳分解与检索），早期跳中的微小检索错误或逻辑不匹配会变成“沉默失败”，逐级级联到最终答案，而没有任何显式恢复机制。这种设计是脆弱的，缺乏对中间步骤的验证与修正。

## 2. 论文提出的方法论

### 核心思想
提出**CARE**（Critic-Guided Multi-Agent Reasoning for Knowledge Editing）——一种用于后编辑推理的闭环框架。通过多智能体协作（Planner、Selector、Critic）和受限回溯，实现链级验证与自纠正，阻断错误传播。

### 关键技术细节

1. **Post-Edit Graph Construction with EATR**  
   - 对编辑描述进行三元组提取，采用**Edit-Anchored Triple Refinement (EATR)** 进行去噪：
     - **端点对齐**：头尾实体必须精确匹配编辑锚定三元组中的 subject 和 new object。
     - **关系一致性**：候选关系与锚定关系的余弦相似度 ≥ δ_rel（实验中 δ_rel=0.80）。
   - 使用 REBEL-LARGE 抽取候选三元组，BGE-M3 编码关系文本计算相似度。
   - 构建更干净、低噪声的后编辑图 GE，为 Selector 提供高质量候选池。

2. **Multi-Agent Collaborative Reasoning**

   - **Planner**：将多跳查询 Q 分解为有序子问题序列 {q_i}，使用占位符 [ENT] 表示跳间桥接实体。通过微调 LLaMA-2-7B 生成分解计划（优化自回归损失 L_plan）。

   - **Selector**：针对每个子问题 q_i，先在 GE 中检索当前实体的一跳邻居，使用 BM25 获取 top-K（K=3），再基于证据句子进行四维语义评分（实体对齐、证据蕴含、关系匹配、结构有效性），得到过滤并排序的候选池 P_i。拒绝使用参数记忆，仅依赖外部证据。

   - **Critic**：对组装好的推理链进行四步验证（局部相关性、桥接一致性、事实根据、最终推导），若发现错误跳 ˆi，触发**受限回溯**（retry budget τ_max=2）：
     - 策略1：要求 Selector 丢弃当前错误候选，选择池中下一最佳候选。
     - 策略2：若候选池耗尽，回退为基于局部证据的 LLM 生成。
   - 验证协议严格禁止使用参数知识，仅依据证据句子。

## 3. 实验设计

### 数据集
- **MQuAKE-2002**：2002 个实例，平均 2.7 跳，2.2 个编辑，无冲突。
- **MQuAKE-hard**：429 个实例，全部为 4 跳，4 个编辑，无冲突（最难子集）。
- 编辑场景：1-edited、100-edited、All-edited（不同编辑存储大小）。

### 评估指标
- **多跳准确率（Acc）**：最终答案是否匹配黄金答案。
- **逐跳准确率（Hop-Acc）**：每跳是否选择了正确的中间实体/事实。

### 对比方法
- **参数编辑类**：FT、ROME、MEMIT（及其 CoT 变体）
- **参数保留推理类**：MeLLo、DeepEdit、PokeMQA、IRAKE
- **基于图的编辑**：KEDKG（最强图基线）
- 省略 “Reason-KE”（需训练骨干网）

### 骨干模型
- 主实验：LLaMA-3-8B、GPT-4o-mini
- 泛化性实验：LLaMA-2-7B、Qwen2.5-7B、DeepSeek-V3.2、GPT-4o

## 4. 资源与算力

- **GPU**：8 × NVIDIA RTX A6000。
- **Planner 训练**：基于 LLaMA-2-7B，在 MQuAKE-CF 数据上微调 3 epochs，学习率 1e-5，batch size 1，使用 AdamW 优化器。
- **推理开销**：CARE 相比前馈基线增加了约 2 倍延迟和 5 倍 token 消耗（平均每问题 30s 延迟，6978 tokens vs KEDKG 的 14s 和 1310 tokens），但换取了大幅提升的准确性。
- **未明确说明**：Planner 训练的具体 GPU 小时数或整体训练时间。

## 5. 实验数量与充分性

实验充分且客观，包含以下多组分析：

| 实验类型 | 内容 |
|----------|------|
| **主实验** | 两个数据集 × 三种编辑规模 × 两种骨干模型，与全部基线对比。 |
| **消融实验** | 分别移除 EATR、Selector、Critic 模块，在 MQuAKE-2002 和 MQuAKE-hard 上验证各组件贡献。 |
| **鲁棒性分析** | 按跳数（2/3/4-hop）分组，对比 Acc 和 Hop-Acc 下降趋势。 |
| **链忠实度分析** | 可视化 Acc 与 Hop-Acc 之间的差距（4-hop 查询），证明 CARE 更少依赖“碰运气”的中间步骤。 |
| **Critic 机制分析** | 按跳数报告错误检测精度（82.9% overall）和有效纠正率（63.5% overall）。 |
| **泛化性实验** | 在 LLaMA-2-7B、Qwen2.5-7B、DeepSeek-V3.2、GPT-4o 上对比 KEDKG，CARE 一致领先。 |
| **超参数敏感性** | 回溯预算 τ_max（1/2/3）和 EATR 阈值 δ_rel（0.5~0.9）的调参。 |
| **检索器消融** | 对比 BM25、SimCSE、Contriever 及不同 top-K，证明 BM25+K=3 是最优配置。 |

- 所有对比均在同一设置下进行，公平客观。
- 数据集经过严格去冲突（MQuAKE-2002 和 MQuAKE-hard 无冲突），避免编辑干扰。

## 6. 论文的主要结论与发现

- **CARE 在所有设置下达到新 SOTA**：在 MQuAKE-hard All-edited 上 Acc 达 93.01%，比 KEDKG 提升 24.48%；Hop-Acc 提升 29.38%。
- **有效缓解错误传播**：Acc 与 Hop-Acc 紧密对齐，表明推理链更忠实，而非依赖脆弱的中间步骤。
- **对推理深度鲁棒**：随着跳数增加，CARE 的退化速度远慢于基线，闭环验证和回溯机制是关键。
- **强泛化性**：在 4 种不同骨干模型上均显著优于 KEDKG，是即插即用的解决方案。

## 7. 优点

- **创新设计**：首个将闭环验证与受限回溯引入多跳知识编辑的框架，突破单向前馈范式。
- **模块化多智能体**：Planner、Selector、Critic 分工明确，分别处理分解、检索/过滤、验证/纠正，可独立优化。
- **EATR 去噪**：利用编辑锚点三元组进行端点对齐与关系一致性过滤，显著提高后编辑图质量。
- **证据驱动**：Selector 和 Critic 严格禁止使用参数记忆，仅依赖外部证据，提升可解释性和可控性。
- **分析全面**：从多角度（深度、忠实度、纠正机制、泛化性、超参数）深入剖析，验证了设计合理性。

## 8. 不足与局限

- **额外推理开销**：闭环多智能体设计与回溯带来更高的延迟和 token 消耗（约 2 倍延迟，5 倍 token），在实际部署中需权衡成本。
- **依赖候选池质量**：Critic 无法生成新事实，纠正成功率（63.5%）受限于 Selector 提供的候选池是否包含正确选项。
- **领域覆盖有限**：仅在 MQuAKE 系列数据集（基于 Wikidata 的事实编辑）上评估，未涉及金融、法律等高危领域，通用性待验证。
- **未评估纯参数编辑场景**：CARE 是参数保留型方法，与参数编辑方法的对比仅在消融实验中涉及 CoT 变体，未深入融合。
- **回溯预算固定**：τ_max=2 为经验值，极端情况可能需要更多回溯轮次，但增加轮次收益递减（τ_max=3 时准确率反而下降），需进一步探索自适应策略。

（完）
