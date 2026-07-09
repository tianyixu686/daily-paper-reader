---
title: "Scaling Beyond Context: A Survey of Multimodal Retrieval-Augmented Generation for Document Understanding"
title_zh: 超越上下文规模：面向文档理解的多模态检索增强生成综述
authors: "Sensen Gao, Shanshan Zhao, Xu Jiang, Lunhao Duan, Yong Xien Chng, Qing-Guo Chen, Weihua Luo, Kaifu Zhang, Jia-Wang Bian, Mingming Gong"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.acl-long.204.pdf"
tags: ["query:mr"]
score: 9.0
evidence: 多模态检索增强生成的近期进展综述
tldr: 随着文档理解需求的增长，多模态RAG成为整合文本、表格、图表等多种模态的关键技术。本综述系统梳理了多模态RAG的架构设计、检索策略、推理方法以及评估基准，覆盖了从基于OCR的管道模型到原生多模态LLM的各种方案，并指出了当前挑战和未来研究方向。该工作为研究人员提供了全面的技术地图。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.204/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 700, \"height\": 1167, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.204/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 762, \"height\": 767, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.204/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 757, \"height\": 585, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.204/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 753, \"height\": 508, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.204/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 768, \"height\": 711, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.204/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 797, \"height\": 141, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.204/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1627, \"height\": 1488, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.204/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 795, \"height\": 813, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.204/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1659, \"height\": 1563, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.204/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1638, \"height\": 514, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.204/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1641, \"height\": 2302, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.204/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1638, \"height\": 2425, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.204/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1639, \"height\": 2177, \"label\": \"Table\"}]"
motivation: 文档理解中多模态信息复杂，现有RAG方法缺乏系统梳理。
method: 系统综述多模态RAG的相关工作，分类比较架构、检索、推理等方面。
result: 提供全面的技术分类和未来方向。
conclusion: 多模态RAG是文档理解的重要方向，仍存在诸多开放挑战。
---

## Abstract
Document understanding is critical for applications from financial analysis to scientific discovery. Current approaches, whether OCR-based pipelines feeding Large Language Models (LLMs) or native Multimodal LLMs (MLLMs), face key limitations: the former loses structural detail, while the latter struggles with context modeling. Retrieval-Augmented Generation (RAG) helps ground models in external data, but documents’ multimodal nature, i.e., combining text, tables, charts, and layout, demands a more advanced paradigm: Multimodal RAG. This approach enables holistic retrieval and reasoning across all modalities, unlocking comprehensive document intelligence. Recognizing its importance, this paper presents a systematic survey of Multimodal RAG for document understanding. We propose a taxonomy based on domain, retrieval modality, and granularity, and review advances involving graph structures and agentic frameworks. We also summarize key datasets, benchmarks, and applications, and highlight open challenges in efficiency, fine-grained representation, and robustness, providing a roadmap for future progress in document AI.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：当前文档理解方法存在根本性局限。基于OCR的流水线会丢失结构细节，而原生多模态大语言模型（MLLM）在处理超长文档（数百至数千页）时受限于上下文窗口并容易产生幻觉。现有的检索增强生成（RAG）虽能利用外部知识，但文档的多模态特性（文本、表格、图表、布局等）要求更先进的**多模态RAG**范式，以实现跨模态的全面检索与推理。
- **研究动机**：尽管多模态RAG在文档理解领域发展迅速（2024–2025年论文数量激增），但缺乏将其与文档理解明确连接的系统性综述。现有RAG综述或侧重文本、或对文档理解覆盖有限，而文档理解综述则很少涉及多模态RAG。本文旨在填补这一空白，提供首个聚焦“多模态RAG + 文档理解”的全面综述。

## 2. 论文提出的方法论：核心思想、关键技术细节

- **分类法**：基于**领域**（开放域 vs. 封闭域）、**检索模态**（纯图像 vs. 图像+文本）、**检索粒度**（页面级 vs. 元素级）对现有方法进行归类，并额外分析**图结构增强**和**智能体增强**两种混合范式。
- **形式化定义**：给出了多模态RAG的通用数学框架（公式1–4）：
  - **视觉仅检索**：仅用图像编码器计算查询与文档图像间的相似度，选取top-K页面。
  - **联合视觉-文本检索**：
    - 置信加权分数融合：为每个文档计算图像置信度λᵢ，融合图像分数和文本分数。
    - 模态专用页并集：分别用图像和文本检索，取各自top-K的并集，再经排序融合（如RRF）。
  - **生成**：生成器以原始查询和检索到的上下文（Ximg、Xconf或X∪）为条件生成最终回答。
- **关键创新**：
  - **开放域/封闭域**：开放域从大规模文档库检索知识（如M3DocRAG）；封闭域对单文档进行页级检索（如SV-RAG），减少输入长度和幻觉。
  - **检索模态**：纯图像方法（ColPali, VisRAG）直接编码页面图像；图像+文本方法（VisDoMRAG, ViDoRAG）融合OCR或VLM生成的摘要，提升细粒度文本线索。
  - **检索粒度**：从页面级向元素级（表格、图表、文本块）演进，如VRAG-RL使用强化学习定位区域，MG-RAG实现多粒度索引。
  - **混合增强**：
    - **图结构**：构建多模态知识图（mKG-RAG）或文档拓扑图（MoLoRAG, RECON），支持跨页实体关联和多跳推理。
    - **智能体**：多智能体协作（ViDoRAG, HM-RAG），进行查询分解、模态并行检索、一致性验证和迭代细化。

## 3. 实验设计：数据集、基准、对比方法

- **数据集与基准**：综述总结了当前最常用的24个数据集/基准（见表3），覆盖文本、表格、图表、幻灯片等类型。代表性数据集包括：
  - 经典文档VQA：DocVQA, InfoVQA, SlideVQA, MMLongBench-Doc
  - 多文档RAG专用：M3DocVQA, VisDoMBench, OpenDocVQA, ViDoSeek, UniDoc-Bench, BBox-DocVQA
- **对比方法**：表4汇总了30余种方法在DocVQA、SlideVQA、InfoVQA、MMLongBench-Doc上的检索和生成评价结果。检索指标包括Top-5/10 Accuracy, R@10, MRR@10, nDCG@5/10；生成指标包括EM, ANLS, PNLS, G-Acc等。
- **评价指标**：附录B详细定义了检索指标（Recall, Precision, F1, MRR, nDCG）和生成指标（BLEU, ROUGE, METEOR, EM, ANLS, PNLS, G-Acc, BERTScore等）。

## 4. 资源与算力

- **未明确说明**：作为综述论文，本文未进行新模型的训练或实验，因此不涉及算力消耗（GPU型号、数量、训练时长等）。仅在讨论工业部署时提及开源工具（RAGFlow, LlamaIndex等）的可用性，但未提及具体硬件需求。

## 5. 实验数量与充分性

- **方法覆盖充分**：综述系统比较了40多种多模态RAG方法（表2），并按域、模态、粒度、图/智能体增强进行多维度分类，涵盖了近两年（2024–2025）该领域的主要进展。
- **基准对比丰富**：表4提供了4个常用基准上的检索与生成性能，虽部分方法未覆盖全部基准，但整体对比清晰。此外，附录A、B、C补充了数据集细节、评价指标和训练损失，分析全面。
- **客观性与公平性**：作者直接引用了各原始论文的数据，未进行新实验，因此不存在主观偏差。同时，他们也指出当前基准的局限性（如数据污染、饱和），并呼吁更细粒度和更逼真的评估协议。
- **不足之处**：由于是新兴领域，部分方法仅出现在预印本中（如ArXiv），尚缺乏同行评审验证；基准之间存在不一致（如不同方法使用不同top-K），虽然作者在表4中尽量对齐，但仍存在轻微不可比性。

## 6. 论文的主要结论与发现

- **主要发现**：多模态RAG在文档理解中显著优于纯文本或纯视觉方法，能有效融合布局、表格、图表等异构信息。图结构和智能体增强进一步提升了多跳推理和细粒度定位能力。
- **开放挑战**：效率（视觉令牌压缩）、细粒度表示（元素级检索）、安全鲁棒（跨模态攻击）、评估基准的规模与多样性等亟待解决。
- **未来方向**：需发展专用文档视觉编码器、超越MaxSim的令牌交互机制、大规模开放域细粒度基准、以及隐私保护和可验证生成。

## 7. 优点

- **首次桥接**：将多模态RAG与文档理解明确关联，弥补了以往综述的空白。
- **结构化分类**：提出基于域、模态、粒度、混合增强的系统分类，便于研究者定位方法。
- **全面资料**：汇总了40+方法、20+数据集/基准、详细的性能对比（表4），并提供评价指标和训练损失总结（附录C），实用性强。
- **前瞻性分析**：不仅总结现状，还深入讨论挑战（附录D）、批判性分析（附录E）和工业部署（附录F），提供发展路线图。

## 8. 不足与局限

- **部署分析初步**：对真实世界部署的用户中心评估、系统集成等讨论较浅，有待深入。
- **数据质量待深究**：虽列出数据集，但未系统分析标注一致性、跨域迁移性和评估对齐问题。
- **领域快速演进**：作为2026年综述，后续新方法、新基准会持续涌现，作者通过开放仓库进行更新。
- **伦理风险提及**：仅简要提及偏见、虚假信息等风险，未展开具体缓解措施。
- **实验覆盖的细微遗漏**：部分近期方法（如M2IO-R1、SERVAL等）仅有预印本，未经历正式审稿，可能影响结论的稳定性。

（完）
