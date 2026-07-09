---
title: "HiKEY: Hierarchical Multimodal Retrieval for Open-Domain Document Question Answering"
title_zh: "HiKEY: 用于开放域文档问答的层级多模态检索"
authors: "Joongmin Shin, Gyuho Shim, Jeongbae Park, Jaehyung Seo, Heui-Seok Lim"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.acl-long.818.pdf"
tags: ["query:mr"]
score: 8.0
evidence: 用于开放域问答的层级树状多模态检索框架
tldr: 针对开放域文档QA中路由失败和证据碎片化问题，提出HiKEY层级树状多模态检索框架。该方法将文档层级结构作为首要检索信号，实现精确文档定位和多模态证据（表格、图表）的有机连接。实验表明其在大规模工业语料上显著提升了检索准确率和答案质量。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.818/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1568, \"height\": 653, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.818/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 742, \"height\": 388, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.818/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 768, \"height\": 714, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.818/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 783, \"height\": 1199, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.818/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1465, \"height\": 686, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.818/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1661, \"height\": 876, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.818/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1664, \"height\": 840, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.818/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 812, \"height\": 716, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.818/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 812, \"height\": 715, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.818/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 818, \"height\": 673, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.818/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 799, \"height\": 1015, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.818/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1662, \"height\": 585, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.818/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 627, \"height\": 775, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.818/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1030, \"height\": 516, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.818/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1658, \"height\": 682, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.818/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 806, \"height\": 848, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.818/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 816, \"height\": 523, \"label\": \"Table\"}]"
motivation: 现有方法难以在大规模语料中精确定位目标文档并整合分散的多模态证据。
method: 提出层级树状多模态检索框架，利用文档结构作为检索信号。
result: 在大规模工业数据集上检索准确率和答案质量均有显著提升。
conclusion: 层级结构和多模态融合能有效解决开放域文档QA的关键瓶颈。
---

## Abstract
Retrieval-augmented generation (RAG) for document-based Open-domain Question Answering (ODQA) on large-scale industrial corpora faces two critical bottlenecks: routing failure in locating the correct document and evidence fragmentation in integrating scattered information. Existing approaches relying on flat text chunks or page-level images inherently struggle to (i) precisely pinpoint the target document among thousands of candidates and (ii) organically connect multimodal evidence, such as tables and figures, within a limited token budget. To address these challenges, we propose HiKEY, a hierarchical tree-based multimodal retrieval framework that elevates document hierarchy to a first-class retrieval signal. Instead of simple chunking, HiKEY reconstructs a logical heterogeneous graph via Document Hierarchical Parsing (DHP), explicitly encoding parent–child relationships. Adopting a hierarchical coarse-to-fine strategy, the framework (1) performs global routing to rapidly prune the search space using hierarchical indexing, and (2) conducts fine-grained retrieval to rank sections by employing a multimodal fusion strategy that captures the most discriminative evidence. Finally, HiKEY assembles a token-efficient evidence subgraph via a hybrid structural-semantic packing strategy. Experiments on ODQA benchmarks demonstrate that HiKEY significantly outperforms page- and chunk-based baselines, improving retrieval recall by up to 12.9% and end-to-end QA performance by up to 6.8%.

---

## 论文详细总结（自动生成）

# 论文总结

## 1. 核心问题与整体含义（研究动机与背景）

开放域文档问答（ODQA）在大规模工业文档语料库上存在两个关键瓶颈：
- **路由失败**：无法在数千个候选文档中精确定位包含答案的正确文档；
- **证据碎片化**：答案证据常分散在不同页面或文档中，且包含表格、图表等多模态内容，现有平坦文本块或整页图像检索无法有效整合这些分散证据。

现有方法（文本块RAG、整页多模态RAG、基于图的RAG）虽各有侧重，但均未将文档**层级结构**视为核心检索信号，导致检索精度低、答案不完整。HiKEY通过将文档层级重建并作为首要检索信号，系统性地缓解上述瓶颈。

## 2. 方法论：核心思想、关键技术细节

**核心思想**：将文档逻辑层级结构（如章节、子章节、标题路径）作为第一类检索信号，实现从粗到细的层级检索和证据打包。

**关键技术细节**：

- **离线阶段：层级感知的图与索引构建**
  - 使用文档层级解析模块（Document Hierarchical Parsing, DHP）从原始PDF中恢复逻辑层级树 T(d)（基于M3DocDep方法，LVLM驱动）。
  - 每个文档构建两种索引卡片：
    - `Doc_card`：包含标题 + 所有章节路径，用于全局路由。
    - `Sec_card`：存储一个章节内的多模态单元（文本段落、表格、图像），每个单元通过DHP树获得祖先路径（如“Title > Section 5 > 5.3”）。
  - 对无标题的图像/表格单元，通过遍历DHP树获取逻辑上相邻的上文文本作为`Upper Context`，减少视觉模糊性。

- **在线检索：层级粗到细检索**
  - **Stage-1: 层级文档路由**：利用混合评分（BM25+dense文本）对`Doc_card`排序，选出候选文档集合 ˆDq。评分公式：S<sub>doc</sub>(d,q) = α·mm(s<sub>lex</sub>(x<sub>d</sub>,q)) + (1-α)·mm(s<sub>text</sub>(x<sub>d</sub>,q))。
  - **Stage-2: 层级章节MaxSim评分**：在候选文档内对所有`Sec_card`评分。每个单元c的得分s(c,q)根据类型决定：文本单元用文本语义编码；表格/图像单元用视觉编码（SigLIP）和上文上下文的混合得分（γ·s<sub>vis</sub> + (1-γ)·s<sub>hybrid</sub>(ctx))。章节最终得分取单元最大得分，并融合文档级得分：S<sub>final</sub>(s,q)=λS<sub>doc</sub>(doc(s),q) + (1-λ)S<sub>sec</sub>(s,q)。

- **层级子图组装**：在固定token预算B<sub>tok</sub>下，采用祖先感知打包算法：
  - Phase 1：添加锚点单元（得分最高的单元）及其祖先标题（Governing Headers）。
  - Phase 2：添加与锚点同父章节的兄弟单元（结构关联）。
  - Phase 3：添加与锚点语义相似的跨章节视觉单元（语义关联）。
  - 最终序列化子图包含每个单元的祖先路径、类型和内容。

**无显式跨块链接建模**：HiKEY不预测或构建除DHP树之外的跨单元链接，所有证据关联由组装策略确定性处理。

## 3. 实验设计

- **数据集与场景**：
  - **M3DocVQA**：多页、多文档、多模态QA基准，需从全语料库定位文档并整合表格/图表证据。
  - **FRAMES**：原始Wikipedia文本基准，作者重新渲染为多页PDF（FRAMES-PDF），引入视觉和结构复杂性，测试多文档路由能力。

- **基准方法**：分为四类共12种对比方法：
  - 文本块RAG：Page, Length chunking, LumberChunker, Meta Chunker, Structural chunking, MultiDocFusion
  - 文本图RAG：RAPTOR, HopRAG
  - 整页多模态RAG：M3DocRAG, VDocRAG
  - 多模态图RAG：MoLoRAG, SimpleDoc

- **评估指标**：
  - 检索：Recall@K, MRR@K, Hit@K, All@K（K=1..10 平均）
  - 最终QA：EM, ANLS, ROUGE-L, METEOR

- **公平性控制**：所有方法使用相同Reader（Qwen2.5-VL-7B-Instruct）、相同文档渲染/OCR源、相同输入token预算（16K）。

## 4. 资源与算力

- **硬件**：4× NVIDIA H100 80GB GPU。
- **离线索引时间**：每文档约8-9秒/页（包括高分辨率布局检测、OCR、视觉嵌入等），其中DHP解析仅占~0.1秒/页。索引成本一次分摊，在线检索不重复计算。
- **推理设置**：Reader使用贪心解码（temperature=0.0），生成长度限制256 tokens，上下文窗口16K tokens。
- 未明确报告总训练时长或在线推理延迟，但附录提供了离线索引的详细耗时表（Table 13）。

## 5. 实验数量与充分性

实验覆盖多个维度的全面评估：
- **两大ODQA基准**：M3DocVQA（2441问）和FRAMES（824问），覆盖不同复杂度。
- **检索性能**：报告K=1..10平均召回率、MRR、Hit、All，并分析Top-K敏感性、token预算敏感性（0.5K~2K）。
- **端到端QA**：四个指标对比12种基线。
- **细粒度分析**：按证据类型（Text/Table/Image）和跳数（1-hop~4+）分解ANLS。
- **消融实验**：分别验证层级索引策略、路由策略、多模态融合策略的贡献（Table 6）。
- **定性案例与失败模式分析**（附录H）。

实验充分且公平：所有基线在相同Reader和预算下比较，检索和QA指标均报告，差异显著。但未在更多域（如金融、法律）或弱结构文档（如幻灯片、纯文本）上验证，泛化性有限。

## 6. 主要结论与发现

- **检索显著提升**：M3DocVQA上Recall@avg 84.9（best baseline 83.0），FRAMES上73.3（baseline 65.4）；严格All@K指标提升更大（FRAMES +11.4点）。
- **端到端QA提升**：M3DocVQA上EM 27.5（best 25.6），FRAMES上EM 10.5（best 7.8）。
- **层级结构是关键**：消融表明，将层级作为独立字段（而非简单拼接）带来+4.0点R@10增益；粗到细路由优于仅文档或仅章节路由。
- **多模态融合有效**：混合视觉信号（SigLIP）在表格/图像查询上带来额外提升，且保持文本优势。
- **资源效率**：在极低token预算（0.5K）下仍领先，证明祖先感知打包的信息密度优势。
- **基线失败原因**：文本块RAG路由能力弱，整页多模态RAG噪声大且预算固定，图RAG忽略表格/图像作为检索单元。HiKEY通过层级路由、块级多模态单元和祖先感知打包分别解决。

## 7. 优点

- **创新性**：首次将文档层级结构作为首要检索信号，而非被动元数据，填补了平坦检索与复杂结构之间的鸿沟。
- **方法论完整性**：从离线解析到在线检索再到证据打包，形成全链路框架，各模块设计环环相扣。
- **实验严谨性**：控制变量严格（相同Reader、预算、OCR），对比基线覆盖主流四大类，消融实验分解贡献。
- **可解释性**：通过定性案例（Apollo 11）和失败模式分析，清晰展示为什么基线失败、HiKEY如何改善。
- **资源友好**：在线检索不重复运行DHP，索引成本可分摊；打包算法可在固定预算下高效运行。

## 8. 不足与局限

- **预计算开销大**：离线DHP解析依赖OCR和布局检测，高精度设置下每页8-9秒，不适用于频繁更新的语料库。
- **依赖上游模块质量**：OCR或布局解析错误会导致错误章节路径，进而路由失败或证据错误。虽然DHP有一定鲁棒性，但在严重退化扫描件或手写体上可能失效。
- **结构性假设**：仅适用于具有显式逻辑层级（章节、标题）的文档，对于扁平文本、收据、无结构幻灯片等场景，层级路由和祖先打包的优势有限。
- **评估范围局限**：仅测试一个Reader（Qwen2.5-VL-7B）和16K预算，未在其他系列/更大模型或不同预算下验证；检索增益与QA增益之间的差距（up to 12.9% vs 6.8%）说明后检索环节（OCR fidelity, evidence materialization, reader calibration）仍有优化空间，但HiKEY本身不解决这些问题。
- **缺乏跨域验证**：虽在Wikipedia-style和工业文档基准上测试，但未在金融、法律等垂直领域完整评估。

（完）
