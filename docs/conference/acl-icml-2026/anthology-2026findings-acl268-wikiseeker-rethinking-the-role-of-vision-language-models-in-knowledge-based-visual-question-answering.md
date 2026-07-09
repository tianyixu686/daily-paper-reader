---
title: "WikiSeeker: Rethinking the Role of Vision-Language Models in Knowledge-Based Visual Question Answering"
title_zh: WikiSeeker：重新思考视觉语言模型在知识型视觉问答中的作用
authors: "Yingjian Zhu, Xinming Wang, Kun Ding, Ying Wang, Bin Fan, Shiming Xiang"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.268.pdf"
tags: ["query:mr"]
score: 9.0
evidence: 利用VLM智能体的多模态RAG用于知识型视觉问答
tldr: 现有知识库视觉问答中多模态RAG过度依赖图像检索且未充分利用VLM能力，本文提出WikiSeeker，将VLM赋予精炼器和检查器两种角色，分别用于改写查询文本和验证证据相关性，结合多模态检索器，显著提升了开放知识问答的准确性和解释性。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.268/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 722, \"height\": 576, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.268/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1647, \"height\": 700, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.268/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 804, \"height\": 411, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.268/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 791, \"height\": 527, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.268/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1493, \"height\": 480, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.268/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 793, \"height\": 529, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.268/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 398, \"height\": 443, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.268/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 383, \"height\": 477, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.268/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 409, \"height\": 347, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.268/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 408, \"height\": 348, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.268/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 72, \"height\": 65, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.268/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 417, \"height\": 404, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.268/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 68, \"height\": 64, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.268/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 66, \"height\": 65, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.268/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 64, \"height\": 62, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.268/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 66, \"height\": 65, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.268/fig-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 64, \"height\": 63, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.268/fig-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 65, \"height\": 64, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.268/fig-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 61, \"height\": 62, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.268/fig-020.webp\", \"caption\": \"\", \"page\": 0, \"index\": 20, \"width\": 64, \"height\": 62, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.268/fig-021.webp\", \"caption\": \"\", \"page\": 0, \"index\": 21, \"width\": 359, \"height\": 475, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.268/fig-022.webp\", \"caption\": \"\", \"page\": 0, \"index\": 22, \"width\": 360, \"height\": 493, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.268/fig-023.webp\", \"caption\": \"\", \"page\": 0, \"index\": 23, \"width\": 357, \"height\": 470, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.268/fig-024.webp\", \"caption\": \"\", \"page\": 0, \"index\": 24, \"width\": 359, \"height\": 474, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.268/fig-025.webp\", \"caption\": \"\", \"page\": 0, \"index\": 25, \"width\": 356, \"height\": 494, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.268/fig-026.webp\", \"caption\": \"\", \"page\": 0, \"index\": 26, \"width\": 357, \"height\": 470, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.268/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 816, \"height\": 141, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.268/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 809, \"height\": 252, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.268/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1654, \"height\": 311, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.268/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1656, \"height\": 623, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.268/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 663, \"height\": 178, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.268/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1652, \"height\": 673, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.268/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 670, \"height\": 281, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.268/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 766, \"height\": 287, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.268/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 738, \"height\": 369, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.268/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 676, \"height\": 384, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.268/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 783, \"height\": 286, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.268/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 806, \"height\": 203, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.268/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1656, \"height\": 261, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.268/table-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1657, \"height\": 260, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.268/table-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 797, \"height\": 184, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.268/table-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 796, \"height\": 158, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.268/table-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 1656, \"height\": 319, \"label\": \"Table\"}]"
motivation: 现有方法未充分利用VLM在Multi-modal RAG中的潜力。
method: 将VLM分为精炼器和检查器，改写查询并验证证据。
result: 在KB-VQA基准上达到最新最优结果。
conclusion: WikiSeeker展示了VLM在RAG中的新角色范式。
---

## Abstract
Multi-modal Retrieval-Augmented Generation (RAG) has emerged as a highly effective paradigm for Knowledge-Based Visual Question Answering (KB-VQA). Despite recent advancements, prevailing methods still primarily depend on images as the retrieval key, and often overlook or misplace the role of Vision-Language Models (VLMs), thereby failing to leverage their potential fully. In this paper, we introduce WikiSeeker, a novel multi-modal RAG framework that bridges these gaps by implementing a multi-modal retriever and redefining the role of VLMs. Rather than serving merely as answer generators, we assign VLMs two specialized agents: a Refiner and an Inspector. The Refiner utilizes the capability of VLMs to rewrite the textual query according to the input image, significantly improving the performance of the multimodal retriever. The Inspector facilitates a decoupled generation strategy by selectively routing reliable retrieved context to another LLM for answer generation, while relying on the VLM’s internal knowledge when retrieval is unreliable. Extensive experiments on EVQA, InfoSeek, and M2KR demonstrate that WikiSeeker achieves state-of-the-art performance, with substantial improvements in both retrieval accuracy and answer quality.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **研究动机**：知识型视觉问答（KB-VQA）需要利用外部知识库来回答图像中无法直接获取的问题。现有的多模态检索增强生成（Multi-modal RAG）方法存在两个关键局限：(1) 仅依赖图像作为检索键（visual-only retrieval），忽略了用户文本查询中的语义信息，导致视觉内容模糊时检索效果差；(2) 将视觉语言模型（VLM）仅作为答案生成器，但实验表明VLM在从检索文本中提取答案的能力不如纯文本大语言模型（LLM），这种角色错位未能充分发挥VLM的潜力。
- **整体含义**：本文提出WikiSeeker，通过重新定义VLM在RAG中的角色（赋予其“精炼器”和“检查器”两种智能体），并引入多模态检索，显著提升了KB-VQA的检索准确率和答案质量，在三个基准上达到最优性能。

## 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程
- **核心思想**：将VLM从简单的答案生成器转变为两个专用智能体——**Refiner（精炼器）**和**Inspector（检查器）**，并构建多模态知识库进行加权稠密检索。
- **关键技术细节**：
  - **多模态知识库构建**：将知识库中的每个图像与其对应文本段落构成<image, section>对，分别用视觉编码器 Φ_vis 和文本编码器 Φ_text 提取特征，拼接为索引向量 v_i = Concat[Φ_vis(I_kb), Φ_text(T_kb)]。
  - **多模态检索**：对输入查询，用VLM Refiner改写后的问题 T_q 与图像 I_q 进行加权拼接得到查询向量 v_q = Concat[α·Φ_vis(I_q), (1-α)·Φ_text(T_q)]，α为超参数控制模态权重。然后计算余弦相似度检索top-k段落。
  - **VLM作为Refiner**：通过强化学习（GRPO）优化VLM，使其能基于图像视觉线索生成链式推理（CoT），然后输出结构化的精炼查询。奖励函数包括格式奖励（正确XML标签和JSON格式）和检索奖励（根据命中实体的排名映射得分，见表1）。
  - **VLM作为Inspector**：评估检索到的上下文是否足以回答问题且与图像一致。若通过（PASS），则使用纯文本LLM生成答案；若失败（FAIL），则Inspector直接利用自身参数知识回答。形式化为：s, A_internal = M_ins(I_q, Q, S_rerank)，最终答案A根据s选择。
  - **解耦生成策略**：将视觉感知（VLM）与阅读理解（LLM）分离，避免视觉token干扰文本提取。

## 3. 实验设计：数据集、基准、对比方法
- **数据集**：
  - **Encyclopedic VQA (EVQA)**：约100万样本，基于iNaturalist和Google Landmarks，知识库为WikiWeb2M的200万篇文章。
  - **InfoSeek**：130万训练样本，人类标注8900个评估样本，使用EchoSight提供的10万实体过滤知识库。
  - **M2KR**：统一多模态检索基准，包含EVQA、OKVQA（常识知识）、OVEN（开放域实体识别）三个子任务。
- **基准（Benchmark）**：官方评估指标——EVQA用BEM分数；InfoSeek用VQA准确率（标准/宽松）；M2KR用Recall@K和Pseudo Recall@K。
- **对比方法**：包括CLIP I-T、Wiki-LLaVA、LLM-RA、mR²AG、ReflectiVA、EchoSight、CoRe-MMRAG、OMGM等主流多模态RAG方法，以及PreFLMR在M2KR上的变体。对比时考虑是否微调了生成器或检索器。

## 4. 资源与算力
- **显式说明**：所有实验在**4块NVIDIA A800 40GB SXM4 GPU**上完成。
- **细节**：Refiner基于Qwen2.5-VL-3B-Instruct，使用GRPO训练，全局batch size=32，学习率1e-6，视觉塔冻结，组大小=5，rollout温度0.7，训练600步。Generator微调13,640/10,000样本，Inspector微调38,000样本，均通过LlaMA-Factory框架。训练时未提供具体时长，只说明总步数。

## 5. 实验数量与充分性
- **实验数量**：
  - 主要检索结果表：EVQA和InfoSeek的R@1/5/10/20（表3）；M2KR三个子任务多深度Recall（表4、12-14）。
  - VQA结果表：EVQA和InfoSeek的准确率对比（表6），包括零样本和微调设置。
  - 消融实验：Refiner和Inspector的贡献（表7）；不同查询策略（表8）；模态权重α、重排序权重β1、β2的参数搜索（附录图4-6）；解耦生成策略的oracle分析（表9）；Inspector有效性（表10）；SNR实验（表15）；路由混淆矩阵（表17）；效率分析（表16）。
- **充分性与公平性**：
  - 覆盖了三个主流数据集，对比方法包含近两年所有强基线，且标注了是否微调检索器/生成器，确保公平对比。
  - 进行了全面的消融（组件、查询形式、超参数、路由策略），验证了每个设计的必要性。
  - 实验设计客观：使用固定重排序器（EchoSight的），冻结权重；检索器对比了有无Refiner；生成器对比了LLM vs VLM vs 解耦。
  - 不足：未在更多多样化场景（如多跳问题、长尾实体）上验证，但已在开放域实体识别（OVEN）上表现良好。

## 6. 论文的主要结论与发现
- WikiSeeker在EVQA、InfoSeek和M2KR三个基准上均达到**最先进（SOTA）**性能，尤其在EVQA上超过OMGM 5.45个百分点。
- **Refiner**的强化学习训练显著提升了检索质量：在M2KR的EVQA、OKVQA、OVEN子集上，Recall@1分别提升2.72、6.92、11.66个百分点。
- **Inspector**的解耦生成策略有效：通过路由成功检索的查询到LLM、失败到VLM，相比单一模型（VLM或LLM）均有提升，接近oracle上界。
- VLM作为答案生成器不如LLM准确，但在检索失败时依靠内部知识仍能提供合理答案，因此Inspector的协同至关重要。

## 7. 优点
- **方法创新性**：重新定义了VLM在RAG中的角色，从单一生成器转为多功能智能体（Refiner+Inspector），充分利用VLM的视觉理解能力，同时避免其在文本提取上的劣势。
- **技术细节扎实**：使用强化学习（GRPO）优化Refiner，奖励函数同时考虑格式和检索性能，训练数据通过自动采样构造，无需人工标注；Inspector的微调数据通过多种策略生成（GT匹配、LLM辅助验证），保证了质量。
- **实验全面且深入**：不仅报告了主结果，还进行了详尽的消融、超参数搜索、效率分析、路由策略可视化，并提供了大量附录材料，可复现性强。
- **开源承诺**：代码将在GitHub上发布，利于后续研究。
- **性能提升显著**：在三个数据集上全面超越现有方法，尤其在检索和生成两个阶段均有改进。

## 8. 不足与局限
- **硬路由策略**：当前Inspector采用“成功→LLM，失败→VLM”的硬路由规则，不一定最优（论文也指出此点），未来可探索更灵活的协作机制。
- **仅支持单跳检索**：无法处理多跳问题，限制了在复杂推理场景中的应用。
- **知识库依赖**：知识库构建依赖Wikipedia文章，对非百科类知识（如常识）的覆盖有限，但在OKVQA上仍有提升。
- **训练数据构造复杂**：Refiner需要根据命中排名采样训练数据，Inspector需要大量混合标签（PASS/FAIL），对标注要求较高。
- **计算资源消耗**：虽然使用了4卡A800，但多阶段训练（Retriever+Refiner+Generator+Inspector）整体开销较大，未与基线进行公平的FLOPs对比。
- **实验覆盖的局限性**：未在更多视觉语言任务（如图文推理、视觉对话）上验证方法的通用性。

（完）
