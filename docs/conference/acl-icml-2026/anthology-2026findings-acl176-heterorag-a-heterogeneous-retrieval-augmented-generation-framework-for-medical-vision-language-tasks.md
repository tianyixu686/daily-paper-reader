---
title: "HeteroRAG: A Heterogeneous Retrieval-Augmented Generation Framework for Medical Vision Language Tasks"
title_zh: HeteroRAG：面向医学视觉语言任务的异构检索增强生成框架
authors: "Zhe Chen, Yusheng Liao, Zhiyuan Zhu, Haolin Li, Hongcheng Liu, Yanfeng Wang, Yu Wang"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.176.pdf"
tags: ["query:mr"]
score: 9.0
evidence: 面向医学视觉语言任务的多模态检索增强生成框架
tldr: 针对医学多模态大模型事实准确性不足、现有RAG系统无法有效检索异构来源的问题，本文构建了包含多模态报告库的 MedAtlas 数据集，并提出 HeteroRAG 框架，通过跨文本、图像等异构源的检索增强生成，显著提升了医学视觉问答的准确性和可解释性。实验证明其优于已有方法。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.176/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 799, \"height\": 424, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.176/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1651, \"height\": 686, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.176/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 797, \"height\": 410, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.176/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 800, \"height\": 548, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.176/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 206, \"height\": 200, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.176/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 208, \"height\": 208, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.176/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 763, \"height\": 570, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.176/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 205, \"height\": 202, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.176/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 213, \"height\": 204, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.176/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 767, \"height\": 1092, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.176/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1647, \"height\": 704, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.176/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 799, \"height\": 478, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.176/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 791, \"height\": 685, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.176/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 797, \"height\": 268, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.176/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1645, \"height\": 798, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.176/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 797, \"height\": 320, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.176/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 800, \"height\": 257, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.176/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 799, \"height\": 247, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.176/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 793, \"height\": 173, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.176/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1642, \"height\": 216, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.176/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1647, \"height\": 221, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.176/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 788, \"height\": 720, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.176/table-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 660, \"height\": 499, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.176/table-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1639, \"height\": 244, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.176/table-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 792, \"height\": 665, \"label\": \"Table\"}]"
motivation: 医学多模态大模型存在事实错误，现有RAG无法有效跨异构源检索。
method: 构建MedAtlas多模态报告库，提出HeteroRAG异构检索框架。
result: 在医学视觉问答任务上准确率和可信度均显著提升。
conclusion: HeteroRAG为医学多模态RAG提供了有效异构检索方案。
---

## Abstract
Medical large vision-language Models (Med-LVLMs) have shown promise in clinical applications but suffer from factual inaccuracies and unreliable outputs, posing risks in real-world diagnostics. While RAG has emerged as a potential solution, current medical multimodal RAG systems are unable to perform effective retrieval across heterogeneous sources. The irrelevance of retrieved reports undermines the factuality of analysis, while insufficient knowledge affects the credibility of clinical decision-making. To bridge the research gap, we construct MedAtlas, which includes extensive multimodal report repositories and diverse text corpora. Based on it, we present HeteroRAG, a novel framework that enhances Med-LVLMs through heterogeneous knowledge sources. The framework introduces Modality-specific CLIPs for effective report retrieval and a Multi-corpora Query Generator for tailoring queries to diverse corpora. Incorporating knowledge from such multifaceted sources, Heterogeneous Knowledge Preference Tuning is performed to achieve cross-modality and multi-source knowledge alignment. Extensive experiments across 11 datasets and 3 modalities demonstrate that HeteroRAG achieves state-of-the-art performance in most medical vision language benchmarks, significantly improving factual accuracy and reliability of Med-LVLMs.

---

## 论文详细总结（自动生成）

# 中文论文总结

## 1. 核心问题与整体含义（研究动机和背景）
- **问题**：医学大视觉语言模型（Med-LVLM）在临床应用中展现出潜力，但存在**事实不准确**和输出不可靠的问题，可能引发误诊风险。检索增强生成（RAG）被视为潜在解决方案，但现有医学多模态RAG系统**无法有效执行跨异构知识源（如影像报告、研究文章、临床指南等）的检索**。检索到的报告不相关会削弱分析的事实性，知识不足则影响临床决策的可信度。
- **目标**：通过构建包含多模态报告库和丰富文本语料的知识库MedAtlas，并设计异构检索与对齐框架HeteroRAG，显著提升Med-LVLMs的事实准确性和可靠性。

## 2. 论文提出的方法论
### 核心思想
- 构建大规模多模态医学知识库MedAtlas（包括放射、眼科、病理图像-报告对，以及研究、百科、教科书、指南、知识图谱五个文本语料库）。
- 提出**HeteroRAG框架**，包含：
  1. **Modality-specific CLIPs (ModCLIPs)**：针对每个模态分别在大规模图像-文本对上微调CLIP模型，用于精确报告检索。
  2. **Multi-corpora Query Generator (MQG)**：两阶段训练（先SFT后DPO）生成针对不同语料库的定制化查询，实现跨语料库的精准文档检索。利用专家Med-LVLM（Lingshu-32B）生成查询并评估文档支持性，以构建正负查询对。
  3. **Heterogeneous Knowledge Preference Tuning (HKPT)**：通过构建偏好数据集（跨模态对齐、知识利用、知识鲁棒性三个维度），使用DPO方法使模型更好地对齐外部异构知识，避免忽视视觉信息或过度依赖检索内容。

### 关键技术细节
- **ModCLIPs**：初始化为BiomedCLIP，每个模态独立训练，训练数据规模远大于以往工作（放射1.1M、眼科0.11M、病理1.51M对）。
- **MQG**：查询探索阶段生成6个查询/语料库；判断阶段以Lingshu-32B作为评判者（人工验证准确率0.836，F1 0.855）。SFT损失和DPO损失如式(1)(2)。
- **HKPT**：算法1详细描述了从训练集中构造偏好样本的过程。跨模态对齐中构造正负样本（使用最不相似图像）；多源知识对齐包括知识利用（移除知识后失败）和鲁棒性（移除知识后正确，加入后错误）两方面。最终使用DPO损失统一训练。

## 3. 实验设计
### 数据集
- **医学VQA**：VQA-RAD、SLAKE、OMVQA-Rad（放射）、DME-VQA（眼科）、OMVQA-Oph（眼科）、PathMMU、PathVQA、Quilt-VQA（病理）。其中OMVQA-Rad、OMVQA-Oph、Quilt-VQA为**领域外（OOD）** 数据集。
- **医学报告生成**：MIMIC-CXR、IU-Xray（放射）、Harvard-FairVLMed（眼科）。
- 确保所有测试样本在ModCLIPs训练和报告检索库中**不可见**，避免数据泄露。

### Benchmark
- 评价指标：VQA用准确率；报告生成放射用BLEU、ROUGE-L、RaTEScore；眼科用BLEU、ROUGE-L、METEOR。

### 对比方法
- **解码方法**：Beam Search、DoLa、VCD、AVISC、M3ID。
- **报告检索方法**：MedDr、FactMM-RAG、RULE、MMed-RAG。
- **文档检索方法**：MKGF、K-LLaVA。
- **报告+文档方法**：MIRA。
- **大型Med-LVLM**：LLaVA-Med-7B、MedGemma-4B、HuatuoGPT-V-34B、HealthGPT-32B、Lingshu-32B。
- 所有基线使用相同的可检索报告和文档，医学CLIP也保持一致（ModCLIPs的影响单独分析）。

## 4. 资源与算力
- **文中未明确说明**使用的GPU型号、数量、训练总时长。仅提供了训练超参数（学习率、批次大小、epoch数等），但未提及具体硬件配置和运行时间。需要指出这一点。

## 5. 实验数量与充分性
- **实验组数**：主结果表（表1：VQA、表4：报告生成）共覆盖11个数据集；消融实验包括：知识源消除（表2）、检索器对比（表3）、MQG组件消融（表5）、HKPT组件消融（图4）、兼容性实验（表6）、与更大模型对比（图3）、报告图像融合分析（表7）、去除检索分析（表8）、查询多样性和相似性分析（表9-10）、错误类型分析（表11）、计算开销（表12）等。
- **充分性评估**：实验设计**全面且客观**。数据集覆盖三个模态、领域内外场景；对比方法涵盖多种类型（解码、检索、大模型）；消融实验验证了每个核心组件的贡献；进行了公平性控制（检索源一致、数据不重叠）。实验数量**充分**，足以支撑主要结论。

## 6. 论文的主要结论与发现
- **HeteroRAG在大多数医学VQA和报告生成基准上达到SOTA**，显著优于各类基线方法。
- **跨异构源的知识检索与对齐**是提升Med-LVLM事实准确性和可靠性的关键。
- 7B参数的HeteroRAG能够**超越4-5倍参数**的公开Med-LVLM（如34B、32B模型），证明了有效知识集成和调优的价值。
- 组件贡献：ModCLIPs大幅提升了报告检索精度（Recall@5远高于其他检索器）；MQG比零样本重写和CLIP检索生成更相关、更多样的查询；HKPT有效降低了跨模态失调、知识失调和知识干扰。
- 框架对不同Med-LVLM（LLaVA-Med、HuatuoGPT-V、Lingshu）具有良好兼容性。

## 7. 优点
- **方法创新性**：提出了针对医学多模态RAG的完整解决方案，包括模态专用检索器、查询生成器、多维度偏好对齐，覆盖从检索到集成的全流程。
- **知识库构建**：MedAtlas规模大、来源广（16个数据集、270万+图像-报告对、5类文本语料），为后续研究提供基础。
- **实验严谨**：严格控制数据泄露，使用多种基线并在公平条件下对比；消融实验设计清晰，充分验证每个模块的贡献。
- **可泛化性**：在OOD数据集和不同骨干模型上均表现优异，体现了框架的通用性。
- **可视化分析**：提供了定性案例（图5-6），展示了模型如何利用或克服冲突信息，增强可解释性。

## 8. 不足与局限
- **检索策略**：仅采用一步检索，未探索多轮工具使用或链式推理（如OpenAI o3风格），未来可扩展。
- **未覆盖的方面**：未涉及公平性、隐私、安全等实际部署中的重要问题。
- **计算成本**：MQG的数据构建阶段需要专家模型进行查询探索和判断，离线构建开销较大（文中表12显示单样本离线构建耗时约21.6秒）。在线推理检索延迟约0.4-0.5秒，尚可接受，但在大规模实时场景下可能需要优化。
- **错误分析**：表11显示“知识对齐失败”仍是主要错误类型（约63%），表明即使高质量检索，模型整合多源知识仍有挑战，需进一步提升推理能力。
- **依赖大模型评判**：MQG训练依赖Lingshu-32B作为评判者，尽管人工验证可信，但评判质量可能影响数据构建的鲁棒性。

（完）
