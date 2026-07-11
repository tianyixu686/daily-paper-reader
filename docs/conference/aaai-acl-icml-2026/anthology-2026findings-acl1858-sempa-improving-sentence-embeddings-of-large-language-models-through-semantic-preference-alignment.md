---
title: "SemPA: Improving Sentence Embeddings of Large Language Models through Semantic Preference Alignment"
title_zh: "SemPA: 通过语义偏好对齐提升大语言模型的句子嵌入"
authors: "Ziyang Chen, Zhenxuan Huang, Yile Wang, Weiqin Wang, Lu Yin, Hui Huang"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.1858.pdf"
tags: ["query:post-multi"]
score: 6.0
evidence: 使用直接偏好优化对齐句子嵌入
tldr: 针对基于生成式LLM的句子嵌入方法无法兼顾性能与生成能力的问题，本文提出SemPA，利用句子级直接偏好优化进行语义偏好对齐，在提升嵌入质量的同时保持模型的生成能力。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1858/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 772, \"height\": 729, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1858/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1606, \"height\": 726, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1858/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 811, \"height\": 431, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1858/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 795, \"height\": 1008, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1858/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1652, \"height\": 622, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1858/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1651, \"height\": 811, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1858/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 806, \"height\": 314, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1858/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1644, \"height\": 332, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1858/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1614, \"height\": 439, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1858/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 802, \"height\": 472, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1858/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1329, \"height\": 253, \"label\": \"Table\"}]"
motivation: 现有LLM嵌入方法要么性能有限要么损害生成能力。
method: 采用句子级直接偏好优化进行语义偏好对齐。
result: 在嵌入任务上取得提升，且不降低生成能力。
conclusion: 语义偏好对齐可同时优化句子嵌入与生成能力。
---

## Abstract
Traditional sentence embedding methods employ token-level contrastive learning on non-generative pre-trained models. Recently, there have emerged embedding methods based on generative large language models (LLMs). These methods either rely on fixed prompt templates or involve modifications to the model architecture. The former lacks further optimization of the model and results in limited performance, while the latter alters the internal computational mechanisms of the model, thereby compromising its generative capabilities. We propose SemPA, a novel approach that boosts the sentence representations while preserving the generative ability of LLMs via semantic preference alignment. We leverage sentence-level Direct Preference Optimization (DPO) to efficiently optimize LLMs on a paraphrase generation task, where the model learns to discriminate semantically equivalent sentences while preserving inherent generative capacity. Theoretically, we establish a formal connection between DPO and contrastive learning under the Plackett-Luce model framework. Empirically, experimental results on both semantic textual similarity tasks and various benchmarks for LLMs show that SemPA achieves better semantic representations without sacrificing the inherent generation capability of LLMs.

---

## 论文详细总结（自动生成）

# 论文核心问题与整体含义（研究动机和背景）

- **研究动机**：现有句子嵌入方法主要依赖非生成式预训练模型（如 BERT）的 token 级对比学习；近期基于大语言模型（LLM）的嵌入方法分为两类：一是基于固定 prompt 模板（如 PromptEOL），性能有限且无法进一步优化；二是修改模型架构（如 Token Prepending），虽提升嵌入质量但严重损害 LLM 的生成能力。因此，亟需一种既能增强语义表示又不丧失生成能力的方法。
- **核心问题**：如何在保持 LLM 原生文本生成能力的前提下，通过轻量级优化获得高质量的句子嵌入？
- **整体含义**：论文提出 SemPA，利用直接偏好优化（DPO）在释义生成任务上进行句子级语义偏好对齐，使 LLM 学会区分语义等价句子，同时保持其生成能力，为 LLM 嵌入研究提供了新范式。

# 论文提出的方法论

- **核心思想**：通过句子级 DPO 优化 LLM 对语义偏好的区分能力，从而间接改善模型内部语义表示，无需修改模型架构或破坏生成能力。
- **关键技术细节**：
  1. **数据构建**：使用自然语言推理（NLI）数据集（SimCSE 所用 275K 三元组），将前提作为锚点句子，蕴涵（entailment）句子作为正例（preferred），矛盾（contradiction）句子作为负例（rejected），构建释义生成偏好三元组。
  2. **释义生成模板**：将锚点句子填入 `T_para` 模板：“Keep the same meaning of this sentence: ‘x*’, while making some changes.” 作为 DPO 输入。
  3. **DPO 训练**：采用 LoRA 微调（rank=8, alpha=32，仅可训练 0.3% 参数）对 LLM 进行偏好优化，目标函数为标准 DPO loss：
     \[
     L_{DPO}(\pi_\theta; \pi_{ref}) = -E_{(x, y_w, y_l)}\left[\log\sigma\left(\beta\log\frac{\pi_\theta(y_w|x)}{\pi_{ref}(y_w|x)} - \beta\log\frac{\pi_\theta(y_l|x)}{\pi_{ref}(y_l|x)}\right)\right]
     \]
  4. **嵌入提取**：微调后，使用 PromptEOL 模板：“This sentence: ‘S’ means in one word:” 输入模型，取最后层最后一个 token 的隐藏状态作为句子嵌入。
- **理论连接**：论文证明 DPO 与对比学习均可统一为 Plackett-Luce 模型框架下的排序概率形式，对比学习的得分函数为相似度函数，DPO 为生成概率比值，从而解释 DPO 为何能改进语义表示。

# 实验设计

- **数据集与场景**：
  - **训练**：NLI 数据集（275K 三元组，实际采样 40K~80K 子集）。
  - **语义相似度评估**：7 个标准 STS 数据集（STS12-16、STS-B、SICK-R），指标为 Spearman 相关系数。
  - **生成能力评估**：GSM8K（数学推理）、MMLU（多任务理解）、HellaSwag（常识推理）、DROP（阅读理解）、TruthfulQA（响应可靠性）。
- **Benchmark 与对比方法**：
  - **传统编码器**：BERT-avg、Sentence-T5-avg、PromptBERT、SBERT（base/large）。
  - **LLM 嵌入方法**：LLM2Vec、Echo Embedding、PromptEOL、Contrastive Prompting、Token Prepending。
  - 使用 LLaMA2-7B 和 LLaMA3-8B 作为基础模型。
- **实验数量与充分性**：共进行约 6 类实验（主结果、数据规模、嵌入空间可视化、模板消融、对齐 token 分析、生成能力评估），覆盖多个数据集和基线，设置了不同随机种子验证稳定性，消融实验包括 5 种释义模板、2 种提取模板、不同训练数据量等，实验设计较为全面、客观、公平。

# 资源与算力

- **GPU 型号与数量**：4 块 NVIDIA RTX 5090 GPU。
- **训练配置**：LoRA 微调，有效 batch size = 256（per-step batch size 8 × gradient accumulation steps 8），AdamW 优化器，学习率峰值 1e-4，线性预热 + 余弦退火。
- **训练时长**：论文未明确说明具体训练时长，但基于数据集规模（40K~80K 样本）和 LoRA 的轻量特性，可推测训练时间较短。

# 实验数量与充分性

- **总体实验组数**：约 7 组主要实验（主结果表、数据规模曲线、嵌入可视化、模板消融、对齐 token 分析、生成能力对比、随机种子稳定性），外加 GAR 分数计算。
- **充分性评价**：
  - **正面**：覆盖了主要 STS 基准和多种 LLM 基线；同时验证生成能力保持；消融实验包含模板、数据量、模型规模等多个维度；使用两个不同规模的 LLaMA 模型（7B/8B），结论具有泛化性；统计分析（标准差）显示结果稳定。
  - **不足**：未比较不同 DPO 变体（如 IPO、KTO）或列表级偏好优化（如 LiPO）；仅使用英文 NLI 数据，未评估跨语言或领域外场景；未在更大模型（如 70B）上验证可扩展性。

# 论文的主要结论与发现

1. **嵌入性能提升**：SemPA 在 7 个 STS 任务上平均 Spearman 达到 77.69（LLaMA2-7B）和 78.10（LLaMA3-8B），优于所有基于 prompt 和架构修改的 LLM 方法，与专用嵌入模型（SBERT-large）相近或更高。
2. **生成能力保持**：在 5 个生成能力基准上，SemPA 仅轻微下降（如 GSM8K 降低 2~4%），而对比学习方法导致显著下降（平均降低 7~17%）。甚至 TruthfulQA 提升 9~10%。
3. **数据高效**：仅使用 40K~80K 训练样本即可达到最优性能，远超对比学习所需的大规模数据。
4. **嵌入空间改善**：SemPA 显著缓解各向异性，均匀性和各向同性分数均优于 PromptEOL 和平均池化。
5. **理论统一**：将 DPO 与对比学习在 Plackett-Luce 框架下统一，解释了偏好对齐用于表示学习的合理性。

# 优点

- **轻量级且非侵入**：仅使用 LoRA 微调 0.3% 参数，无需修改模型架构或计算流程，原始生成能力零损失。
- **数据成本低**：直接利用已有 NLI 数据集（SimCSE），无需额外人工标注或模型生成偏好数据。
- **理论创新**：首次从 Plackett-Luce 视角联结 DPO 与对比学习，为偏好对齐在表示学习中的应用提供了理论依据。
- **实验设计全面**：不仅评估 STS，还系统评估生成能力变化，打消对偏好对齐破坏生成能力的顾虑。
- **可推广性**：在 LLaMA2 和 LLaMA3 上均有效，且性能随基础模型增强而提升。

# 不足与局限

1. **偏好优化形式局限**：仅使用二元 DPO，未探索列表级偏好优化（如 LiPO），后者可能利用多候选间更丰富的排序信息。
2. **数据依赖**：依赖 NLI 数据的偏好标签（蕴涵/矛盾），但 NLI 数据可能不覆盖所有语义关系（如中性句），且仅用英文。
3. **模板敏感性**：部分模板组合下性能波动（特别是 LLaMA2 结合 CoT 提取模板），鲁棒性有待提升。
4. **理论深度**：虽然建立了 DPO 与对比学习的统一形式，但并未深入分析为何偏好对齐比直接对比学习更优的机制。
5. **实验覆盖范围**：未在更大模型（如 70B、Chat 版本）或跨语言/跨域任务上验证。
6. **推理效率**：仍依赖 PromptEOL 模板进行嵌入提取，需额外提示工程，且嵌入维度与隐藏状态相关，未讨论存储和效率问题。

（完）
