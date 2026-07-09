---
title: "MegaRAG: Multimodal Knowledge Graph-Based Retrieval Augmented Generation"
title_zh: "MegaRAG: 基于多模态知识图谱的检索增强生成"
authors: "Chi-Hsiang Hsiao, Yi-Cheng Wang, Tzung-Sheng Lin, Yi-Ren Yeh, Chu-song Chen"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.acl-long.2218.pdf"
tags: ["query:mr"]
score: 9.0
evidence: 基于多模态知识图谱的检索增强生成用于长文档深度推理
tldr: 针对RAG在长文档深度推理中缺乏高层概念理解和整体把握的问题，提出MegaRAG框架，将多模态知识图谱与RAG结合。该方法利用实体中心结构和层级摘要，融合文本和图像的互补信息，支持跨模态推理。实验表明其在长文档问答和概念理解任务上优于纯文本RAG方法。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.2218/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1393, \"height\": 899, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.2218/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1152, \"height\": 1879, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.2218/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1143, \"height\": 1917, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.2218/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 838, \"height\": 2026, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.2218/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1156, \"height\": 1548, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.2218/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1116, \"height\": 508, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.2218/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 990, \"height\": 1991, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.2218/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 990, \"height\": 1987, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2218/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1656, \"height\": 671, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2218/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1656, \"height\": 670, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2218/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 808, \"height\": 204, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2218/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1655, \"height\": 701, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2218/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 804, \"height\": 577, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2218/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 806, \"height\": 223, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2218/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 802, \"height\": 677, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2218/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1650, \"height\": 264, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2218/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1651, \"height\": 1072, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2218/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 827, \"height\": 248, \"label\": \"Table\"}]"
motivation: 现有基于知识图谱的RAG局限于文本，无法利用图像信息。
method: 构建多模态知识图谱，整合实体层级结构用于长文档推理。
result: 在长文档问答任务上显著超越纯文本基线方法。
conclusion: 多模态知识图谱能有效增强RAG在长文本上的推理能力。
---

## Abstract
Retrieval-augmented generation (RAG) enables large language models (LLMs) to dynamically access external information, which is powerful for answering questions over previously unseen documents. Nonetheless, they struggle with high-level conceptual understanding and holistic comprehension due to limited context windows, which constrain their ability to perform deep reasoning over long-form, domain-specific content such as full-length books. To solve this problem, knowledge graphs (KGs) have been leveraged to provide entity-centric structure and hierarchical summaries, offering more structured support for reasoning. However, existing KG-based RAG solutions remain restricted to text-only inputs and fail to leverage the complementary insights provided by other modalities such as vision. On the other hand, reasoning from visual documents requires textual, visual, and spatial cues into structured, hierarchical concepts. To address this issue, we introduce a multimodal knowledge graph-based RAG that enables cross-modal reasoning for better content understanding. Our method incorporates visual cues into the construction of knowledge graphs, the retrieval phase, and the answer generation process. Experimental results across both global and fine-grained question answering tasks show that our approach consistently outperforms existing approaches on both textual and multimodal benchmarks.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义

- **研究动机**：大型语言模型（LLMs）和多模态大模型（MLLMs）在处理长文档（如整本书）时受限于上下文窗口，难以进行高层概念理解和全局推理。传统RAG方法通过检索外部知识缓解了部分问题，但现有基于知识图谱（KG）的RAG（如GraphRAG、LightRAG）仅支持纯文本，无法利用视觉文档中的图像、图表等互补信息。此外，独立分块提取实体容易导致图结构碎片化，丢失跨块关系和关键实体。
- **整体含义**：本文提出**MegaRAG**，一种自动构建多模态知识图谱（MMKG）的RAG方法，将文本、图像、布局等模态信息融合到统一的知识结构中，实现跨模态推理，提升对长文档（尤其是视觉密集型文档）的深度理解能力。

## 2. 论文提出的方法论

- **核心思想**：基于MLLM自动从多模态文档中构建MMKG，并通过两阶段（初始构建+全局子图引导的细化）提升图结构完整性和跨模态对齐。检索阶段采用实体/关系双级检索与页面检索并行，生成阶段采用两阶段解耦策略（分别从KG和页面图像生成中间答案，再融合）以减少模态偏差。
- **关键技术细节**：
  1. **MMKG构建**：
     - 对文档的每一页提取四种内容：文本`T_i`、图`F_i`、表`B_i`、全页渲染图`I_i`。
     - **初始图构建**：使用MLLM（GPT-4o-mini）逐页并行提取实体和关系（`(E,R)_i^0 = G(P_i)`），合并去重得到初始MMKG `G_0`。
     - **细化阶段**：对每一页，从其初始输出中提取关键词检索`G_0`中的子图`G_0^i`（通过GME编码匹配），并扩展一跳邻居，然后使用细化提示`R(P_i, G_0^i)`让MLLM识别缺失的跨模态关系（如文本实体与图实体之间的“illustrates”关系）和新实体，得到`(E,R)_i^1`，合并得到细化后的MMKG `G_1`。
  2. **索引与检索**：
     - 使用统一多模态编码器**GME**（Qwen2-VL-2B）对实体（名称+描述）、关系（关键词+源目标+描述）和页面图像分别编码，存入向量库。
     - **图检索**：从用户查询中提取低层（具体实体）和高层（抽象概念）关键词，编码后检索top-k实体和关系，并扩展一跳邻居。
     - **页面检索**：同时检索top-m最相关页面图像。
  3. **答案生成**：
     - **两阶段生成**：第一阶段并行生成两个中间答案——一个基于检索到的子图，一个基于检索到的页面图像；第二阶段用MLLM融合两个中间答案，得到最终答案。
- **公式/算法流程**：伪代码已在方法部分描述，核心为`(E,R)_i^1 = R(P_i, G_0^i)`以及合并得到`G_1`。

## 3. 实验设计

- **数据集与场景**：
  - **全局QA（全书级别）**：
    - 纯文本基准：UltraDomain（4个子集：Agriculture、Legal、Computer Science、Mix），共约10M tokens。
    - 多模态基准：自行构建的4个文档——World History（788页，历史教科书）、Environmental Report（422页，企业报告）、DLCV（1984页，深度学习课件）、GenAI（594页，生成式AI课件）。
  - **局部QA（页面/幻灯片级别）**：
    - SlideVQA（子集2k幻灯片，含约14.5k问题）
    - RealMMBench（4个子集：FinReport、FinSlides、TechReport、TechSlides）
- **对比方法**：
  - 文本RAG基线：NaiveRAG、GraphRAG、LightRAG。
  - 多模态RAG基线：VisRAG、GME（通用多模态嵌入）、ColQwen。
  - 额外对比：Query-driven MMKG（最近的多模态GraphRAG）。
- **评测指标**：全局QA无标注答案，采用LLM法官（GPT-4.1-mini）两两比较并计算胜率（含四个维度：全面性、多样性、赋能性、总体）；局部QA有参考答案，LLM判断语义等价，报告准确率。

## 4. 资源与算力

- 论文中明确提到：
  - MMKG构建使用GPT-4o-mini（API调用），无本地训练。
  - 编码阶段使用**GME-Qwen2-VL-2B**（2B参数）在单张**NVIDIA RTX 3090（24GB VRAM）**上本地运行，编码一张页面图像平均约0.97秒。
  - 推理阶段同样使用单张RTX 3090，端到端延迟约42秒/问题（含双阶段生成）。未提及具体GPU数量或训练时长（因为无需训练）。
  - 与GME基线对比：GME延迟约26.4秒/问题，MegaRAG多出约15.6秒。

## 5. 实验数量与充分性

- **实验数量**：相当充分。
  - 全局QA：在4个文本子集+4个多模态文档上进行了详尽的胜率对比（每个文档125个问题×多个基线）。
  - 局部QA：5个数据集（SlideVQA子集+4个RealMMBench子集）上的准确率对比。
  - 与多模态RAG的对比：4个文档上的胜率对比。
  - 消融实验：3类消融（文本仅图、去掉图检索、去掉两阶段生成）在2个多模态文档上评估。
  - 与Query-driven MMKG对比：2个文档。
  - 额外：使用不同法官模型（Gemini-3-Flash）验证鲁棒性；检查位置偏差（交换顺序双评估）；对比无检索的纯MLLM。
- **充分性**：实验设计较全面，覆盖了纯文本、多模态、全局、局部多种场景，消融验证了各组件贡献，并分析了位置偏差和模型偏差，结果报告了胜率、准确率、Cohen's kappa等，评估较为客观公平。

## 6. 论文的主要结论与发现

- 在全局QA（文本+多模态）和局部QA任务上，MegaRAG**一致显著优于**所有基线，包括GraphRAG、LightRAG、VisRAG、GME、ColQwen等。
- 在纯文本UltraDomain上，MegaRAG平均胜率（总体）约71.8%，远超NaiveRAG（约8-16%）、GraphRAG（约12-22%）、LightRAG（约12-20%）。
- 在多模态全局QA上，MegaRAG平均总体胜率约89.5%，尤其在幻灯片型文档（DLCV、GenAI）上优势最大（>90%）。
- 在局部QA上，MegaRAG在SlideVQA（2k）上准确率64.85%是最好基线LightRAG（27.66%）的两倍以上；在RealMMBench各子集上领先8-45个点。
- 消融表明，**图检索是核心贡献**（去掉后性能下降最剧），视觉输入和两阶段生成提供补充提升。
- 计算开销方面，MMKG构建约1.4× GraphRAG的token量，但属于一次性离线成本；推理延迟约42秒/问题，比强多模态RAG（GME）多15.6秒，但换取显著性能提升。

## 7. 优点

- **创新性**：首次提出自动构建**多模态知识图谱**用于RAG，突破了现有KG-RAG仅限文本的限制。
- **方法设计巧妙**：两阶段构建（初始+全局子图引导细化）有效恢复跨模态和跨页关系；两阶段生成减少模态偏差；使用统一多模态编码器GME实现灵活检索。
- **实验全面且扎实**：覆盖文本/多模态、全局/局部多种任务，与多个强基线对比，且做了充分的消融、偏差分析、不同法官验证。
- **无需微调**：完全基于现成MLLM（GPT-4o-mini）和预训练编码器，易于部署。
- **代码开源**：提供完整代码和prompt格式，可复现。

## 8. 不足与局限

- **图构建局限于单文档**：实验集中在单本书/报告内，未探索跨文档问答。
- **多模态数据集规模有限**：由于计算和预处理成本，多模态数据集（如DLCV等）相对较小。
- **视觉实体粗粒度**：每个图仅作为一个实体，可能丢失图中细粒度对象（如多个子图、子对象）。
- **幻觉风险**：自动构建的MMKG可能包含MLLM产生的幻觉（错误实体/关系），且会传播到下游回答。论文承认这一点，但未提供检测/修正机制。
- **计算成本较高**：相比纯文本方法，MMKG构建需要处理大量图像token（1.4× GraphRAG token量），推理延迟增加约60%（42s vs 26.4s），对资源要求更高。
- **未讨论跨语言场景**：仅涉及中英文文档，其他语言未验证。
- **评估依赖LLM法官**：尽管做了偏差控制，但LLM评判仍可能存在偏好，且全局QA无标准答案，可靠性依赖法官模型。

（完）
