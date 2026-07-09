---
title: "AED-RAG: Continuous Multi-Granular Context Fusion for Retrieval-Augmented Generation via Adaptive Ensemble Decoding"
title_zh: AED-RAG：通过自适应集成解码实现连续多粒度上下文融合的检索增强生成
authors: "Junzhe Zhou, Fulin Lin, Tairan Cheng, Shaowen Chen, Hongwei Wang"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.1148.pdf"
tags: ["query:mr"]
score: 6.0
evidence: 用于检索增强生成的连续上下文融合
tldr: RAG面临检索粒度粗与生成需求细的不匹配问题。AED-RAG提出自适应集成解码框架，将离散检索与连续解码融合，通过对比学习训练的效用预测器动态平衡内外证据。实验表明，该方法在多个QA数据集上改善了答案质量，为解决RAG粒度问题提供了新思路。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1148/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 805, \"height\": 317, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1148/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1577, \"height\": 866, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1148/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 770, \"height\": 500, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1148/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 782, \"height\": 457, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1148/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1430, \"height\": 679, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1148/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1187, \"height\": 344, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1148/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 796, \"height\": 329, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1148/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 798, \"height\": 416, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1148/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 798, \"height\": 280, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1148/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 816, \"height\": 457, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1148/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 797, \"height\": 381, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1148/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1362, \"height\": 451, \"label\": \"Table\"}]"
motivation: 粗粒度检索引入噪声，离散重排序难以解决粒度不匹配和内外证据平衡问题。
method: 提出AED-RAG，结合离散检索与连续自适应集成解码，并用效用预测器指导融合。
result: 在多个QA基准上，AED-RAG在答案准确性和相关性上优于标准RAG和重排序方法。
conclusion: 连续集成解码是改善RAG生成细粒度的有效途径。
---

## Abstract
Retrieval-Augmented Generation (RAG) enhances Large Language Models (LLMs) yet suffers from a mismatch between coarse retrieval granularity and fine-grained generation needs. Specifically, coarse-grained passages inherently conflate valid context with intra-passage noise that semantic retrieval often fails to filter. Existing alignment strategies, typically relying on discrete reranking, struggle to address this granularity mismatch or effectively balance external evidence with internal knowledge. To bridge this gap, we propose **AED-RAG**, a framework that synergizes discrete retrieval with continuous **A**daptive **E**nsemble **D**ecoding. Specifically, we fine-tune a utility predictor using contrastive perplexity to discern the information density differences between unstructured narrative passages and structured knowledge triplets. During inference, this predictor projects passages, triplets, and the model’s parametric memory into a unified probability space, enabling a soft, token-level fusion that dynamically optimizes information gain. Extensive experiments on four open-domain QA benchmarks demonstrate that AED-RAG significantly outperforms competitive baselines, underscoring the effectiveness of integrating multi-granular contexts.

---

## 论文详细总结（自动生成）

# AED-RAG：通过自适应集成解码实现连续多粒度上下文融合的检索增强生成 – 论文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：标准RAG（检索增强生成）存在两个关键缺陷：
  - **检索粒度不匹配**：粗粒度的段落检索虽然保留叙事连贯性，但不可避免地引入“段落内噪声”（intra-passage noise），例如无关细节使LLM注意力分散，导致“中间丢失”现象。
  - **离散信息瓶颈**：传统“检索-重排序-生成”流水线依赖硬性截断（top-k选择），迫使生成器将选中上下文同等对待，无法动态平衡外部证据与模型内部参数记忆之间的冲突，尤其在二者矛盾时表现不佳。
- **研究背景**：已有方法要么追求细粒度原子命题（如Dense X Retrieval、PropRAG），要么依赖知识图谱结构（如GraphRAG），但牺牲了上下文连贯性或带来高构建成本。对齐策略（如GainRAG）通过对比困惑度（CPPL）量化边际效用，但仍需先进行离散重排序，无法实现连续融合。
- **本文动机**：作者通过分析发现，没有单一信息源能始终最优：约55%查询下段落效用最高，但超过40%情况下三元组或模型内部记忆更优。因此需要一种能够自适应融合多粒度信息（段落、三元组、参数记忆）的连续概率融合机制。

## 2. 论文提出的方法论：核心思想、关键技术细节

### 2.1 整体框架（AED-RAG）

- **核心思想**：将离散检索与连续自适应集成解码相结合，把段落、三元组和模型内部记忆投影到统一概率空间，通过token级软融合动态优化信息增益。
- **两大模块**：Triplet-Enhanced Preference Alignment（三元组增强偏好对齐） + Adaptive Ensemble Decoding（自适应集成解码）。

### 2.2 三元组增强偏好对齐

- **对比困惑度（CPPL）**：定义从上下文c中获得的边际信息增益。通过对比由上下文c和仅查询q生成的logits，突出外部检索的贡献。
- **数据构建**：
  - 使用三元组提取器Ψ(·)将离线语料库中的每个段落分解为结构化知识三元组（头实体、关系、尾实体）。
  - 对每个查询q，构建混合候选集`U_mix`，包含：原始检索段落`D_ret`、对应三元组集合`T_ret`、以及LLM自生成段落`d_gen`（作为内部参数记忆的表示）。
- **效用预测器**：基于预训练Cross-Encoder（BGE-reranker-base）初始化，通过最小化KL散度蒸馏LLM的CPPL偏好到预测器，使其学会区分段落（上下文丰富）和三元组（事实精确）之间的信息密度差异。

### 2.3 自适应集成解码（推理阶段）

- **顺序效用计算**：对检索到的段落和三元组，分别取top-m的效用分数，使用衰减系数β（可见性系数）计算聚合效用`U_D`和`U_T`。
- **自足段落**：将LLM自生成段落`d_ss`视为内部参数记忆，其效用直接为预测器得分`U_ss`。
- **自适应权重**：通过Softmax将`U_D`、`U_T`、`U_ss`归一化为权重向量`w`。
- **Token级融合**：下一token通过最大化加权对数概率和选择：`yt = argmax Σ w_ζ log P(v|q, ζ, y<t)`，其中ζ ∈ {D, T, d_ss}。
- **优势**：该策略在计算上可通过批处理三路数据流保持与单流生成相当的延迟；当权重w_T=w_ss=0时退化为标准离散流水线。

## 3. 实验设计

- **数据集**：四个广泛使用的开放域QA基准：
  - **HotpotQA**（多跳推理）
  - **Natural Questions (NQ)**（真实用户查询）
  - **TriviaQA**（复杂问答）
  - **WebQuestions (WebQ)**（实体中心问答）
- **评估指标**：Exact Match (EM) 和 F1，并报告两者的平均值以平衡长度偏差。
- **对比方法**（共6类基线）：
  1. Naive Generation（仅LLM内部知识）
  2. Standard RAG（k=1/5直接检索）
  3. RECOMP（压缩检索文档）
  4. REPLUG（黑盒集成解码）
  5. BGE-Reranker（重排序）
  6. GainRAG（基于CPPL偏好对齐的重排序）
- **设置**：统一使用Contriever作为检索器、BGE-reranker-base作为重排序器、Qwen3-8B作为骨干LLM。默认初始检索k=10，最终选用top-m=2段落和top-m=2三元组。

## 4. 资源与算力

- 论文明确说明：
  - **效用预测器**初始化为BGE-reranker-base，在**2块RTX Pro 6000 GPU**上训练。
  - 训练数据来自HotpotQA训练集，过滤后得到19,291条唯一查询，每个样本候选集41项（但训练时仅取top-32高效用项目）。
  - 批大小：8；学习率：6e-5；warmup比例：0.1；固定随机种子。
- **未说明**训练总时长（epoch数）、推理时GPU型号及具体耗时（但附录F给出了延迟对比表，表明AED-RAG与标准RAG延迟相当）。
- 总体算力中等，未使用大规模集群。

## 5. 实验数量与充分性

- **实验组数**：
  - **主表（Table 1）**：在4个数据集上对比7种基线方法的多个设置（k=1/5, n=1/5, m=1/2），共约20+个条件。
  - **消融实验（Table 2）**：在HotpotQA和NQ上逐步去除AED（三元组、自足段落、完整AED、且去除三元组重排序），共4个变体。
  - **可见性系数β影响（Figure 3）**：在HotpotQA和NQ上测试β从0到50的8个取值。
  - **对齐必要性验证（Figure 4）**：将预测器替换为原始BGE-reranker分数进行集成解码，对比4个数据集。
  - **跨模型迁移性（Table 3）**：将基于Qwen3-8B训练的预测器直接用于Qwen3-1.7B、Qwen2.5-7B、Qwen3-14B，在HotpotQA和NQ上评估。
  - **三元组影响分析（Table 4）**：对比标准RAG和BGE-reranker在使用纯三元组、段落+三元组拼接时的表现。
  - **附录**：延迟对比（Table 7）和输入token开销（Table 8）。
- **充分性评价**：实验覆盖全面，既包括主性能对比，也有消融、超参数分析、跨模型迁移、组件必要性验证。基线选择合理且为当前SOTA。公平性方面，统一了检索器、重排序器和LLM，提示模板一致。但注意仅训练于HotpotQA，其余数据集仅为评估，可能存在领域偏差，但论文将此作为泛化能力的正面证据。

## 6. 论文的主要结论与发现

1. **AED-RAG达到SOTA**：在所有四个数据集上，EM、F1及平均值均优于所有基线，包括最新偏好对齐方法GainRAG。
2. **自适应集成解码优于离散重排序**：即使移除AED组件（仅保留效用预测器进行重排序），性能仍优于GainRAG，说明三元组结构本身带来增益；但全集成的AED版本进一步提升。
3. **三元组和内部记忆均不可或缺**：消融实验表明，去除三元组或自足段落均导致性能下降，说明两者提供互补信息。
4. **偏好对齐是集成解码的前提**：直接用预训练BGE-reranker原始分数进行集成解码反而降低性能，说明未校准的分数不适合融合。
5. **跨模型可迁移**：在同一模型系列内（Qwen3/2.5），预测器可直接迁移至不同规模模型，带来一致增益。
6. **三元组单独作为检索单元无优势**：仅使用三元组或简单拼接段落与三元组到标准RAG中并不提升效果，说明AED-RAG的增益来自效用预测和集成解码的协同，而非三元组本身的信息优势。

## 7. 优点

- **方法创新性**：提出“连续融合”替代传统离散重排序，将冲突解决从路由问题转化为概率融合问题，思路新颖。
- **轻量高效**：训练代价低（仅2块GPU），推理时可批处理，延迟与标准RAG相当，无需额外推理阶段（如多轮辩论、自反思）。
- **模块化设计**：三元组提取离线预处理、效用预测器可独立训练和迁移，便于集成到现有RAG流水线。
- **充分的消融与诊断**：不仅消融组件，还验证对齐必要性、超参数敏感性、跨模型迁移性，实验设计严谨。
- **泛化能力强**：仅在HotpotQA上训练，但在NQ、TriviaQA、WebQ上均取得最佳，表明方法不限于单数据集。

## 8. 不足与局限

- **实验覆盖局限**：
  - 仅使用英文开放域QA数据集，未涉及多语言、专业领域（如医学、法律）或生成任务（如对话、摘要）。
  - 检索数量m固定为2，未探索动态自适应检索数量。
  - 三元组提取依赖现成的开源工具（Fang et al. 2024），其质量可能影响最终效果；未对三元组提取错误进行鲁棒性分析。
- **偏差风险**：
  - 效用预测器在HotpotQA上训练，虽然在其他QA数据集上泛化良好，但训练集过滤了低效用样本（最大效用接近1），可能引入选择偏差，忽略本来难以解决的查询。
  - CPPL的α参数固定为0.5，但不同任务或模型可能需要调整，论文未做敏感性分析。
- **方法论限制**：
  - 当前仅考虑单个段落与对应三元组，未探索段落间的组合上下文（如多跳推理中需要跨段落证据融合），作者也承认这是未来方向。
  - 自足段落生成依赖于LLM自身，若模型对查询完全无知或产生幻觉，可能引入错误先验；论文未评估此情况下的鲁棒性。
- **应用限制**：需要离线三元组提取，对语料库更新时间有要求；若语料频繁更新，维护成本较高。此外，框架对骨干LLM的兼容性在跨系列模型（如Llama或GPT）上未验证。

（完）
