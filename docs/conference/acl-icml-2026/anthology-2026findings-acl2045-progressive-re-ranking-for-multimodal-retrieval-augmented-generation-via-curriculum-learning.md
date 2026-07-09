---
title: Progressive Re-ranking for Multimodal Retrieval-Augmented Generation via Curriculum Learning
title_zh: 通过课程学习实现多模态检索增强生成的渐进重排序
authors: "Zhu Min, Yanchao Hao, Jian Liu, Shizhu He (何世柱), Xi Chen"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.2045.pdf"
tags: ["query:mr"]
score: 9.0
evidence: 面向多模态检索增强生成的渐进重排序
tldr: 多模态RAG中单一检索器难以捕捉细粒度语义，且视觉相似实体可能误导生成。本文提出渐进式重排序框架，通过课程学习分两阶段：细粒度段落级重排序和多模态段落再评估，逐步优化检索结果。在多个多模态基准上，该方法显著提升了RAG的生成质量和检索准确性。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.2045/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 796, \"height\": 399, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.2045/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1590, \"height\": 564, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.2045/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 765, \"height\": 583, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.2045/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 835, \"height\": 273, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.2045/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1666, \"height\": 536, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.2045/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1683, \"height\": 617, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.2045/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 752, \"height\": 175, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.2045/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 844, \"height\": 221, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.2045/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 735, \"height\": 323, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.2045/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 796, \"height\": 172, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.2045/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1376, \"height\": 227, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.2045/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 816, \"height\": 145, \"label\": \"Table\"}]"
motivation: 多模态RAG中粗粒度检索丢失细粒度语义，重排序需对齐多模态查询。
method: 提出渐进式两阶段重排序框架，结合课程学习从粗到细优化多模态检索结果。
result: 在多个多模态QA数据集上，该方法在答案准确性和检索精度上优于现有重排序方法。
conclusion: 渐进式课程学习有效提升了多模态RAG的检索质量和生成可靠性。
---

## Abstract
Retrieval-augmented generation (RAG) can enhance large language models (LLMs) by providing external knowledge and helping reduce hallucinations. In multimodal RAG, however, retrieval remains challenging because a single retriever may fail to capture fine-grained multimodal semantics, and visually or semantically similar entities may still contain misleading information for answer generation. We propose a progressive multimodal re-ranking framework with curriculum learning to improve CLIP-based visual coarse-grained retrieval. Our framework progressively refines retrieval results through two stages: fine-grained section-level re-ranking and multimodal section reassessment. To better align re-ranking with multimodal queries, we introduce a curriculum-learning strategy that trains the model with hard negatives that are visually or semantically similar but contain misleading information. Experiments on InfoSeek and Enc-VQA show that our method achieves state-of-the-art answer accuracy and competitive retrieval performance.

---

## 论文详细总结（自动生成）

# 论文总结：Progressive Re-ranking for Multimodal Retrieval-Augmented Generation via Curriculum Learning

## 1. 核心问题与整体含义（研究动机和背景）

- **研究动机**：多模态检索增强生成（Multimodal RAG）中，现有CLIP等全局对齐模型进行视觉粗粒度检索时，难以捕捉细粒度多模态语义；且视觉或语义相似的实体可能包含误导信息，导致LLM生成幻觉。

- **背景**：知识型VQA任务（如InfoSeek、Enc-VQA）要求模型从大规模Wikipedia多模态语料库中检索精确段落来回答关于实体属性的问题。现有方法（如EchoSight、OMGM）采用多阶段检索，但检索质量仍有提升空间，且检索与生成阶段存在目标不匹配。

- **整体含义**：旨在通过渐进式、多粒度的重排序框架，结合课程学习策略，提升多模态检索的精确度，从而增强生成答案的事实准确性，减少幻觉。

## 2. 方法论：核心思想、关键技术细节

### 核心思想
构建渐进式两阶段重排序框架，在CLIP粗粒度视觉检索的基础上，依次进行**细粒度段落级重排序**和**多模态段落再评估**，并通过课程学习训练轻量化重排序模块，使其能区分视觉/语义相似但含误导信息的负样本。

### 关键技术细节
1. **第一阶段：CLIP视觉粗粒度检索**  
   使用EVA-CLIP-8B对查询图像和问题生成全局嵌入，结合LLaVA生成的图像标签，通过FAISS索引检索top-20相关Wikipedia文章。

2. **第二阶段：细粒度段落级重排序**  
   - 将top-20文章分割为段落候选集S。  
   - 使用Q-Former提取图像token嵌入(32个)和文本token嵌入(512个)，并通过F-Adapter（小型聚合模块，含可学习查询和交叉注意力层）将文本token聚集为32个嵌入。  
   - 采用**ColBERT式后期交互（Late Interaction）**计算多模态查询与段落之间的相似度得分：  
     \[
     \text{sim}_s(e_q, e_s) = \sum_{i=1}^{l_q} \max_{1 \le j \le l_s} \mathbf{e}_q^i \cdot (\mathbf{e}_s^j)^\top
     \]  
     其中\(e_q\)由图像token和问题侧文本token拼接而成（共64个），\(e_s\)为段落侧文本token（32个）。  
   - 最终得分加权融合视觉相似度\(\text{sim}_p\)与段落相似度\(\text{sim}_s\)：  
     \[
     \text{sim}_{\text{total}} = \lambda \cdot \text{sim}_p + (1-\lambda) \cdot \text{sim}_s
     \]  
     \(\lambda\)为数据集依赖的超参数。

3. **第三阶段：多模态段落再评估**  
   - 取上一阶段top-5段落对应的文章封面图像，构成图像-段落对。  
   - 使用预训练多模态重排序模型（bge-qwen-vl-2b）计算全局余弦相似度，结合投票策略选择最终段落输入生成器。

4. **课程学习训练策略**  
   - **简单负样本**：从视觉粗检索中随机选取k1=24个段落（无直接语义关联）。  
   - **困难负样本**：基于**解码排名扰动（Decoding Rank Perturbation）**，利用LLM（仅文本）评估给定段落时生成正确答案的平均对数似然排名；选择排名差异大的段落作为硬负样本（k2=4），训练重排序模块。  
   - 训练流程：先在全部900k训练样本上训练6个epoch（仅简单负样本），再在100k子集上训练1个epoch（加入硬负样本），实现课程式难度递增。

## 3. 实验设计

### 数据集
- **InfoSeek**：130万图像-问题对，覆盖11,000+视觉实体，知识源为100k Wikipedia文章。采用官方验证集（分为Unseen Question和Unseen Entity子集）。  
- **Enc-VQA**：22.1万问题-答案对，200万Wikipedia文章，图像来自iNaturalist和Google Landmarks。评价单跳和多答案问题，排除两跳问题。

### 评估指标
- **检索**：Recall@K (K=1,5,20)，要求精确字符串匹配Wikipedia链接。  
- **VQA准确率**：InfoSeek使用VQA准确率（字符串/时间）和松弛准确率（数值）；Enc-VQA使用BERT Matching (BEM) 和IoU（多答案）。

### 对比方法
- 检索过程优化：RoRA-VLM、Wiki-LLaVA、EchoSight、OMGM（基于ChatGPT摘要的检索）。  
- 生成过程优化：mR2AG、ReflectiVA、MMKB-RAG。  
- 基线包括CLIP-based检索、EchoSight的剪影等。  
- 所有方法均在相同LLM骨干（LLaMA3-8B或LLaVA-1.5-7B）下比较。

## 4. 资源与算力

- **GPU型号**：2块 NVIDIA H20 80GB GPU。  
- **训练时长**：每个训练epoch约30小时（训练阶段共6+1=7个epoch）。  
- **显存需求**：未明确给出峰值显存，但训练采用batch size=8，单个H20 80GB可支持。  
- **注意**：论文未提及完整的训练总时长（如数据预处理、生成推理时间），但给出了关键训练参数。

## 5. 实验数量与充分性

### 实验数量
- **主要实验**：两张性能对比表（VQA准确率、Recall@K），包含多个SOTA方法。  
- **消融实验**：  
  - 不同检索阶段对VQA准确率的贡献（表3）。  
  - 细粒度后期交互 vs. CLS嵌入（表4）。  
  - 负采样策略影响：随机 vs. 视觉相似 vs. 生成器反馈（表5）。  
  - 硬负样本数量对召回的影响（表6）。  
  - 效率与性能对比（表7）。  
- **定量案例分析**：展示了生成示例对比GPT-4o和Claude 3.5 Sonnet。  
- **附录**：提供了更细粒度的InfoSeek类别分析（表9）。

### 客观性与公平性
- 对比方法均引用公开论文，使用相同评估协议。  
- 消融实验设计合理，逐步验证各组件贡献。  
- 注意：部分对比方法（如OMGM）使用了ChatGPT生成摘要，属于预处理，论文明确指出自己的粗检索方法仅基于图像，具有可比性。  
- 训练数据与测试集采用官方划分，避免信息泄露。  
- 但InfoSeek缺乏段落级标注，采用零样本迁移，可能影响可重复性。

## 6. 主要结论与发现

1. **渐进式重排序有效提升准确率**：在Enc-VQA上VQA准确率达50.32%（LLaMA3-8B零样本），在InfoSeek上达35.07%，均超过所有SOTA方法。  
2. **课程学习显著改善检索**：硬负样本采样使Recall@1提升至59.0%（InfoSeek），优于随机采样（53.5%）。  
3. **后期交互优于CLS嵌入**：在InfoSeek Recall@1上，后期交互（59.0%）优于CLS嵌入（57.2%）。  
4. **效率与性能平衡**：渐进式重排序仅引入约0.496秒/查询，显著提升VQA得分（vs. EchoSight：0.429秒/查询，VQA 41.8% vs. 50.32%）。  
5. **多模态再评估进一步精化**：第三阶段的视觉知识引入对特定问题有帮助。

## 7. 优点

- **方法设计**：  
  - 渐进式多粒度策略（粗→细→多模态）符合人类认知规律，有效缓解单一检索器不足。  
  - 轻量化重排序模块（F-Adapter仅需少量可学习参数），便于训练和部署。  
  - 课程学习策略合理利用解码排名扰动，自动挖掘高质量硬负样本，无需人工标注。  
- **实验充分**：涵盖了检索和生成两阶段的全面评估，消融实验覆盖核心设计点。  
- **结果显著**：在多个基准上取得SOTA，且效率可接受。  
- **通用性**：可适配不同LLM（LLaMA3、LLaVA），且对未见实体和未见问题均有鲁棒性。

## 8. 不足与局限

- **上界受限于粗检索质量**：第一阶段CLIP检索若无法召回相关实体，后续重排序无法弥补（论文指出仅保留top-20，未大幅扩展）。  
- **硬负采样计算成本高**：基于LLM推理的解码排名扰动需要大量计算，难以扩展到全训练集（仅使用100k子集），且当前为静态采样，无法动态适应模型更新。  
- **实验覆盖局限**：  
  - 仅评估两个数据集（InfoSeek和Enc-VQA），且均基于Wikipedia语料，未在开放域或非英语场景验证。  
  - 未与基于多模态嵌入的端到端检索系统（如使用交叉编码器全面重排序）直接比较效率。  
  - 未分析重排序模块在不同LLM backbone上的泛化性（仅测试了LLaMA3-8B和LLaVA-1.5-7B）。  
- **潜在偏差**：使用LLaVA生成的图像标签可能引入噪音；bge-qwen-vl-2b多模态模型的性能可能影响第三阶段结果。  
- **可重复性**：InfoSeek因缺少段落级标注，采用零样本迁移，其他研究者难以精确复现该设置；附录中提供的Prompt模板有助于复现，但数据预处理细节（如Wikipedia文章图像下载）未完全描述。

（完）
