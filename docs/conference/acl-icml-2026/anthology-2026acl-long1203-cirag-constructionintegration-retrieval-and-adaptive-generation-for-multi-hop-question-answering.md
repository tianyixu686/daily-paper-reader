---
title: "CIRAG: Construction–Integration Retrieval and Adaptive Generation for Multi-hop Question Answering"
title_zh: CIRAG：面向多跳问答的构造-集成检索与自适应生成
authors: "Zili Wei, Yilin Wang, Xiaocui Yang, Shi Feng, Weidong Bao, Daling Wang, Zihan Wang, Yifei Zhang"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.acl-long.1203.pdf"
tags: ["query:mr"]
score: 9.0
evidence: 面向多跳问答的构造-集成检索与自适应生成
tldr: 现有迭代检索方法存在单路径扩展错误传播和证据粒度不匹配问题。CIRAG提出构造-集成迭代模块，通过构建候选三元组并基于历史条件集成，蒸馏核心证据并生成答案。实验证明该方法在多跳问答基准上优于现有iRAG方法，有效缓解了早期错误累积和噪声干扰。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1203/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 818, \"height\": 449, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1203/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1644, \"height\": 1039, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1203/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 802, \"height\": 405, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1203/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 768, \"height\": 578, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1203/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 661, \"height\": 511, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1203/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 688, \"height\": 473, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1203/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 789, \"height\": 530, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.1203/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 823, \"height\": 462, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1203/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1500, \"height\": 603, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1203/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 811, \"height\": 289, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1203/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 814, \"height\": 378, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1203/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 650, \"height\": 470, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1203/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 812, \"height\": 272, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1203/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 814, \"height\": 475, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1203/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 812, \"height\": 475, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.1203/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 809, \"height\": 328, \"label\": \"Table\"}]"
motivation: 现有迭代RAG在多跳问答中受限于单路径扩展和证据粒度不匹配，导致错误传播和噪声。
method: 提出构造-集成迭代模块，构建候选三元组并基于历史条件进行集成，蒸馏核心证据后生成答案。
result: 在多个多跳QA数据集上，CIRAG显著超越iRAG基线，具有更强的鲁棒性和并行证据捕获能力。
conclusion: 构造-集成策略有效解决了多跳RAG中的路径依赖和噪声控制问题。
---

## Abstract
Triple-based Iterative Retrieval-Augmented Generation (iRAG) mitigates document-level noise for multi-hop question answering. However, existing methods still face limitations: (i) greedy single-path expansion, which propagates early errors and fails to capture parallel evidence from different reasoning branches, and (ii) granularity–demand mismatch, where a single evidence representation struggles to balance noise control with contextual sufficiency. In this paper, we propose the Construction–Integration Retrieval and Adaptive Generation model, CIRAG. It introduces an Iterative Construction–Integration module that constructs candidate triples and history-conditionally integrates them to distill core triples and generate the next-hop query. This module mitigates the greedy trap by preserving multiple plausible evidence chains. Besides, to address the granularity–demand mismatch, we propose an Adaptive Cascaded Multi-Granularity Generation module that progressively expands contextual evidence based on the problem requirements, from triples to supporting sentences and full passages. Moreover, we introduce Trajectory Distillation, which distills the teacher model’s integration policy into a lightweight student, enabling efficient and reliable long-horizon reasoning. Extensive experiments demonstrate that CIRAG achieves superior performance compared to existing iRAG methods.

---

## 论文详细总结（自动生成）

### 1. 核心问题与整体含义（研究动机和背景）

- **研究动机**：多跳问答（Multi-hop QA）需要从多个文档中逐步收集并整合证据。现有的迭代检索增强生成（iRAG）方法虽然通过多步检索缓解了单步检索的不足，但仍面临两大挑战：
  - **贪婪单路径扩展**（Greedy Single-Path Expansion）：每一步只选择最优的三元组，早期错误会逐级传播，且无法并行捕获不同推理分支的并行证据，导致推理链不完整。
  - **粒度需求不匹配**（Granularity–Demand Mismatch）：固定使用单一粒度（如三元组、句子或段落）的证据表示，难以同时满足噪声控制与上下文充分性的要求——简单查询需要紧凑三元组以减少噪声，复杂查询则需要更丰富的上下文。
- **整体含义**：本文旨在设计一种更鲁棒、自适应的迭代检索框架，通过模拟人类认知中的“构造-集成”过程来保留多路径证据，并通过自适应粒度扩展来匹配不同问题的信息需求，从而提升多跳问答的准确性。

---

### 2. 方法论：核心思想、关键技术细节、算法流程

- **核心思想**：受认知心理学中的 Construction-Integration（CI）模型启发，将多跳检索分解为“构造”与“集成”两个交替阶段，并结合自适应多粒度生成与轨迹蒸馏。

- **关键技术细节**：
  - **Iterative Construction-Integration (ICI) Retrieval 模块**：
    - **构造阶段**：每一步根据当前查询 `a_t` 从检索文档中提取候选三元组，并通过重排序保留 top-N 候选。
    - **集成阶段**：使用知识判别器（KD，通过轨迹蒸馏训练）基于原始问题、历史上下文和候选三元组，过滤出核心三元组 `˜T_t`，生成推理轨迹 `r_t`，并合成下一跳查询 `a_{t+1}`。同时记录三元组到句子/文档的溯源映射，逐步累积多粒度证据池。
  - **Adaptive Cascaded Multi-Granularity Generation (ACMG) 模块**：
    - 按照粒度从细到粗的顺序（三元组 → 句子 → 段落）逐级尝试生成答案。每一级若模型返回的答案不是预定义的“Unanswerable”，则停止扩展；否则升级到更粗粒度。最终输出最小充分粒度的答案。
  - **Trajectory Distillation**：
    - 以强教师模型（Qwen-max）生成完整的推理轨迹，然后通过监督学习将集成策略蒸馏到轻量学生模型（Qwen2.5-7B）中，使学生模型能以较低计算成本复现教师的分步集成决策。

- **算法流程**（文字描述）：
  1. 初始查询为原始问题，历史上下文为空。
  2. 重复以下步骤直至 `a_{t+1}=∅` 或达到最大迭代步 L：
     - 构造：根据当前查询检索 top-K 文档，提取三元组并重排序得到候选集。
     - 集成：KD 模型根据原始问题、历史上下文和候选集，输出核心三元组、推理轨迹和下一跳查询。
     - 更新累积证据池。
  3. 在 ACMG 模块中，依次尝试用三元组、句子、段落级别的累积证据生成答案，选择第一个满足充分性的结果输出。

---

### 3. 实验设计

- **数据集**：
  - 多跳 QA 主数据集：HotpotQA、2WikiMultiHopQA（2WikiMQA）、MuSiQue（各随机采样 1000 条验证集问题）。
  - 单跳 QA 数据集：NQ、WebQA（各 500 条测试问题）。
  - 检索语料：将数据集中所有支持段落与不支持段落混合构建。

- **Benchmark 与对比方法**：
  - 对比方法分为三类：
    - 单次检索：NativeRAG。
    - 文本迭代检索：IRCoT、FLARE、MetaRAG、DualRAG（含微调变体 DualRAG-FT）。
    - 三元组迭代检索：KiRAG。
  - 所有方法使用相同的检索器（bge-Small-env1.5 或 nvidia/NVEmbed-v2）和相同骨干模型（Qwen2.5-7B-Instruct 或 Qwen-max-2025-01-25）。

- **评估指标**：
  - 检索性能：R@3、R@5（针对三元组、句子、段落各粒度）。
  - QA 性能：Exact Match (EM) 和 F1。

---

### 4. 资源与算力

- 文中明确说明：
  - 训练使用 **4 张 NVIDIA A6000 48GB GPU**。
  - 学生模型 LoRA 微调（rank=64），训练约 **3 小时**。
  - 教师模型使用 Qwen-max API（温度=0），未说明具体 GPU 数量。
- 推理时使用了同一硬件环境（Intel Xeon Gold 6326 CPU + 单张 A6000），但未给出单次推理具体耗时。

---

### 5. 实验数量与充分性

- **实验数量**：
  - 主表（Table 1）：在 3 个多跳 QA 数据集上，基线与 CIRAG 在两种骨干模型（7B 和 max）下的比较。
  - 消融实验（Table 2-3）：分别验证轨迹蒸馏、重排序器、不同粒度组合的影响。
  - 检索性能评估（Table 5）：在 2WikiMQA 上手工标注 100 个问题，对比 CIRAG 与其他方法的召回率。
  - 效率实验（Figure 6）：延迟 vs. F1 散点图。
  - 迭代步数敏感性（Figure 7）：在 2WikiMQA 上改变 L 从 2 到 8。
  - 候选三元组数量敏感性（Figure 8）：N 从 10 到 100。
  - 跨数据集验证（Table 4）：在 WebQA 和 NQ 上测试单跳性能。
  - 跨骨干/检索器补充实验（Table 6-7）：使用 Llama-3-8B 和 bge-Small。
  - 轨迹数量影响（Table 8）：从 1k 到 4k 轨迹。

- **充分性与公平性**：
  - 充分：覆盖了主流多跳、单跳数据集，多种骨干/检索器，多种消融维度，几乎无遗漏。
  - 公平：所有方法使用相同检索器、相同骨干模型、相同语料库，超参数尽量对齐。主实验重复随机采样并报告平均性能。
  - 客观：公开代码，结果可复现。

---

### 6. 主要结论与发现

1. **CIRAG 在所有多跳 QA 数据集上显著优于现有 iRAG 方法**（平均 F1 提升 4.3%～10.3%），尤其在 2WikiMQA 和 MuSiQue 上提升最大。
2. **ICI 模块有效缓解贪婪路径扩展**：通过保留多路径候选并历史条件集成，避免早期错误累积。
3. **ACMG 模块自适应匹配粒度**：约 76% 的 2WikiMQA 问题和 57% 的 MuSiQue 问题仅需三元组即可回答，证明大多数复杂问题确实可由紧凑结构表示。
4. **轨迹蒸馏显著提升轻量模型集成能力**：去除蒸馏后，模型倾向于使用更粗粒度证据，性能大幅下降。
5. **CIRAG 效率较高**：离线缓存三元组后，推理延迟仅略高于基线，但 F1 显著更高；ACMG 平均仅需 1.2~1.6 次 LLM 调用。

---

### 7. 优点

- **方法设计巧妙**：将认知科学中的 CI 模型引入检索，同时解决路径依赖和粒度匹配两大问题，理论基础扎实。
- **模块化、可解释**：ICI 和 ACMG 各自职责明确，集成阶段输出推理轨迹和核心三元组，可追踪。
- **蒸馏策略实用**：将教师策略高效迁移至轻量模型，降低算力需求，保持推理质量。
- **实验全面、结论可靠**：覆盖多数据集、多骨干、多检索器，消融实验充分，敏感性分析细致。
- **效率与性能平衡**：离线缓存和自适应粒度检查避免了不必要计算。

---

### 8. 不足与局限

- **构造阶段依赖提示式开放信息抽取**：在专业领域或关系隐晦的场景下，抽取可能遗漏关键三元组，影响下游集成。
- **级联生成顺序增加额外延迟**：虽然平均调用次数少，但最坏情况下需依次尝试三级，导致延迟波动。
- **未在更多语言/领域验证**：当前仅使用英文数据集（HotpotQA、NQ 等），对其他语言或特定领域（如生物医学）的泛化性未知。
- **硬件资源未充分披露**：仅给出训练 GPU 型号和数量，未给出推理峰值显存、推理总时间等细节，不利于直接复用在其他硬件。
- **轨迹蒸馏仅基于 Qwen-max**：未探索其他强教师模型（如 GPT-4）的效果，可能限制蒸馏上限。

（完）
