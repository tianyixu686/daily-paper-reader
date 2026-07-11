---
title: "Compressing then Matching: An Efficient Pre-training Paradigm for Multimodal Embedding"
title_zh: 压缩再匹配：多模态嵌入的高效预训练范式
authors: "Da Li, Yuxiao Luo, Keping Bi, Jiafeng Guo (嘉丰 郭), Wei Yuan, Biao Yang, Yan Wang, Fan Yang, Tingting Gao, Guorui Zhou"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.acl-long.169.pdf"
tags: ["query:post-multi"]
score: 8.0
evidence: 高效多模态嵌入预训练范式
tldr: 针对多模态大语言模型嵌入学习，本文提出“压缩再匹配”两阶段预训练范式，将语义保留与判别特征解耦。第一阶段压缩语义，第二阶段通过对比学习匹配，在跨模态检索等任务上取得更高效且更优的性能。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.169/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1579, \"height\": 872, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.169/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1664, \"height\": 349, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.169/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 781, \"height\": 303, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.169/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 792, \"height\": 313, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.169/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 800, \"height\": 399, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.169/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 808, \"height\": 559, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.169/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1650, \"height\": 892, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.169/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 807, \"height\": 264, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.169/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1641, \"height\": 2110, \"label\": \"Table\"}]"
motivation: 现有MLLM嵌入学习方法需要同时优化两个互补目标，效率低。
method: 将语义保留与判别特征解耦，先压缩语义再通过大规模对比学习匹配。
result: 在跨模态检索、聚类、分类任务上取得更优效果。
conclusion: 解耦两目标可实现更高效的多模态嵌入学习。
---

## Abstract
Multimodal Large Language Models advance multimodal representation learning by acquiring transferable semantic embeddings, thereby substantially enhancing performance across a range of vision-language tasks, including cross-modal retrieval, clustering, and classification. An effective embedding is expected to comprehensively preserve the semantic content of the input while simultaneously emphasizing features that are discriminative for downstream tasks. Recent approaches demonstrate that MLLMs can be adapted into competitive embedding models via large-scale contrastive learning, enabling the simultaneous optimization of two complementary objectives. We argue that the two aforementioned objectives can be decoupled: a comprehensive understanding of the input enables the embedding model to achieve superior performance on downstream tasks via contrastive learning. In this paper, we propose CoMa, a compressed pre-training phase, which serves as a warm-up stage for contrastive learning. Experiments demonstrate that with only a small amount of pre-training data, we can transform an MLLM into a competitive embedding model. CoMa achieves new state-of-the-art results among MLLMs of comparable size on the MMEB, realizing optimization in both efficiency and effectiveness. Our project is available at https://github.com/Trustworthy-Information-Access/CoMa.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

多模态嵌入是AI的核心研究方向，旨在将文本、图像等异构数据统一表示为富含语义的向量，支撑跨模态检索、RAG、VQA等下游任务。现有方法主要分为两类：

- **CLIP类双编码器**：对齐全局语义但忽略局部细粒度对应，导致在视觉定位、属性检索等任务上表现不足。
- **MLLM类（如Qwen-VL、LLaVA）**：通过交错的图文序列输入，能捕捉细粒度语义对应。但MLLM原本为自回归生成设计，与嵌入应用的任务范式存在根本差异。现有通过大规模对比学习将其适配为嵌入模型（如VLM2Vec、GME）的方法依赖海量高质量数据，效率低下且缺乏方法论支撑。

论文认为，一个好的嵌入应具备两个关键特性：**（1）全面信息覆盖**（尽可能保留输入语义）和**（2）判别特征**（突出与匹配相关的信息）。先前方法试图通过对比学习同时优化这两个目标，导致数据需求大。本文提出**解耦**策略：先通过压缩预训练阶段让模型学会全面理解输入，再通过对比学习凸显匹配相关特征，从而大幅提升效率。

## 2. 方法论（核心思想、关键技术细节）

### 核心思想：压缩再匹配（CoMa: Compress then Match）

将多模态嵌入的学习分解为两个阶段：
- **阶段一：压缩预训练（Compression Pretraining）**——让MLLM学会从图像中提取全面信息，压缩到少量可学习token中。
- **阶段二：对比学习（Contrastive Learning）**——利用压缩token的表示进行对比学习，聚焦匹配相关特征。

### 关键技术细节

1. **输入序列构造**：对于图像I、问题Q和答案A，在图像之后插入K个压缩token C（K=32，远小于图像token数）。序列为：`[图像pad]..., [C1],..., [CK], [Question], [Answer]`。
2. **注意力掩码修改**：利用因果注意力的特性，但强制对话部分（Q和A）只能依赖压缩token，而不能直接看到图像token。具体做法是将对话部分与图像部分之间的下三角注意力得分置零（图1(e)）。这样压缩token必须从图像中提取足够信息才能正确生成答案。
3. **预训练损失**：最大化条件概率 \(P(A | C \oplus Question; \theta)\)，采用交叉熵损失（Next Token Prediction）。
4. **压缩token的使用**：预训练后，提取压缩token对应的最终层隐藏状态，进行均值池化作为输入的整体表示，用于后续对比学习。
5. **自动数据生成**：为减少对高质量数据的依赖，利用Qwen2.5-VL-7B自动为每张图像生成3-5个多轮问答对，覆盖不同维度的视觉信息。最终构建约22.2万条预训练数据（来自MMEB-V1训练集的子集）。

## 3. 实验设计

### 数据集
- **预训练数据**：从MMEB-V1训练集中随机采样约22万条，基于其中的图像自动生成问答对（多轮对话格式）。数据来源包括CIRR、HatefulMemes、MSCOCO、N24News、SUN397、VOC2007、Visual7W、WebQA等9个数据集。
- **对比学习数据**：MMEB-V1训练集（全量或子集，主实验使用全量，消融实验用50万条）。
- **评估基准**：MMEB-V1，包含36个评测数据集，分为4个元任务：分类（10个）、VQA（10个）、检索（12个）、视觉定位（4个）。其中20个为分布内（IND），16个为分布外（OOD）。

### 对比方法
- **无预训练方法**：CLIP (ViT-L)、OpenCLIP、GME (Qwen2-VL)、UNITE (Qwen2-VL)、VLM2Vec、E5-V、MMRet、CAFe、mmE5等。
- **有预训练方法**：UniME、MoCa（均为先进预训练方法）。
- 对比基于相同或相近规模的MLLM骨干（如Qwen2.5-VL 3B/7B、LLaVA-1.6 7B等）。

### 评估指标
Precision@1（强调top-1结果）。

## 4. 资源与算力

论文明确提及以下算力信息：
- 采用LoRA（rank=16）微调，大幅减少参数。
- 预训练阶段batch size=256，对比学习阶段通过GradCache扩展到1024。
- **GPU需求仅为MoCa的四分之一**（未给出具体GPU型号与数量，也未说明训练时长）。
- 预训练阶段仅使用3亿token，而MoCa需要300亿token。对比学习阶段仅使用MMEB-V1一半的训练数据、更小的batch size即达到SOTA。

因此，CoMa在资源使用上显著低于同类预训练方法，但**具体GPU型号、数量、训练时长未报告**。

## 5. 实验数量与充分性

论文进行了多组实验，具体包括：

1. **主实验（Table 2）**：对比9个以上baseline，在36个数据集上报告4个元任务及总体得分。CoMa-7B取得72.2总体分（SOTA），CoMa-3B取得67.5分。
2. **压缩token数量影响（Figure 2）**：对比1、8、16、32、64个token，发现32最优。
3. **相似性分析（Figure 3）**：可视化不同数量压缩token间的相似性，解释为何过多token引入冗余信息。
4. **预训练格式消融（Table 3）**：对比多轮对话 vs 单轮、描述 vs 标题；对比交叉熵 vs KL散度损失。结果表明多轮对话+交叉熵最优。
5. **表示演化可视化（Figure 4）**：PCA展示基模型、预训练后、对比学习后三个阶段查询与目标的表示分布，证明预训练拉近了与最终目标的距离。
6. **损失分布分析（Figure 5）**：对比交叉熵和KL散度在不同token上的损失分布，说明交叉熵更聚焦于关键答案token。

**充分性评价**：实验覆盖了不同骨干、不同预训练方法、不同数据格式、不同损失函数、不同压缩token数量，并提供可视化分析，整体设计客观且充分。但缺少对更大规模数据（如使用全部MMEB训练数据）的对比实验，以及与其他模态（视频、纯文本）的扩展验证。

## 6. 主要结论与发现

1. **解耦有效**：将“全面理解”和“匹配判别”分离，先通过压缩预训练让模型学会全面提取信息，再通过对比学习聚焦匹配特征，可显著提升效率与效果。
2. **数据效率高**：仅需约3亿token预训练数据（其他方法需300亿）、更少的对比学习数据，即可达到SOTA。
3. **压缩token数量敏感**：32个token为最佳，过多（64）引入冗余，过少（1-16）信息容量不足。
4. **多轮对话格式优于单轮**：多问题迫使模型平衡压缩哪些信息、丢弃哪些信息，减少针对单一细节的过度关注。
5. **交叉熵优于KL散度**：KL散度要求完全一致，对压缩这种有损任务过于严格，限制了泛化能力。
6. **预训练作为对比学习的有效预热**：可视化和损失分布均表明预训练缩小了指令模型与嵌入模型之间的差距。

## 7. 优点

- **创新性**：首次提出将嵌入的两个目标解耦为压缩预训练+对比学习的训练范式，简单且有效。
- **高效性**：仅需极少量预训练数据和计算资源（LoRA、小batch）即可获得SOTA，显著降低了MLLM转嵌入的门槛。
- **自动化数据生成**：利用MLLM自身自动生成多样化问答对，减少对外部高质量数据的依赖。
- **分析深入**：通过token相似性、表示演化、损失分布等多角度分析揭示了方法生效的内在机制。
- **可复现性**：开源代码。

## 8. 不足与局限

- **实验资源未透明**：未给出具体GPU型号、数量、训练时长，不利于其他研究者复现对比。
- **数据规模有限**：预训练和对比学习均基于MMEB-V1子集（约22万预训练+500K/1.1M对比学习），未探索更大数据下的性能上限。
- **模态限制**：当前仅验证了图像-文本模态，未处理纯文本、视频等其他模态，虽然论文声称可扩展但无实验证据。
- **泛化性验证不足**：仅在一个benchmark（MMEB-V1）上评测，且未对不同领域（如医疗、遥感）进行测试，存在领域偏差风险。
- **性能波动**：在部分OOD任务上（如Country-211）得分明显低于mmE5等模型，说明压缩预训练可能在某些细粒度场景下仍有不足。
- **压缩机制依赖因果注意力**：当前设计基于因果注意力，若换成双向注意力可能需要重新设计注意力掩码，通用性受限。

（完）
