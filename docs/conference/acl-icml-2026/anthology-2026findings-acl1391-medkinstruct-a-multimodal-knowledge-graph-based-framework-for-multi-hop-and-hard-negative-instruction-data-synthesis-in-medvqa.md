---
title: "MedKInstruct: A Multimodal Knowledge Graph Based Framework for Multi-Hop and Hard-Negative Instruction Data Synthesis in MedVQA"
title_zh: MedKInstruct：基于多模态知识图谱的多跳与难负例指令数据合成框架
authors: "Yinan Wu, Jihang Jin, Xuhao Bao, Weiyan Zhang, Hanjing Yan, Tong Ruan, ChunMing Wang"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.1391.pdf"
tags: ["query:mr"]
score: 9.0
evidence: 用于医学视觉问答中多跳指令数据合成的多模态知识图谱
tldr: 现有医学VQA指令数据仅关注视觉属性，缺乏知识级多跳推理，本文提出MedKInstruct，从多模态医学知识图谱中自动生成多跳和难负例指令数据，增强LVLM的医学知识学习与推理能力。实验表明微调后的模型在多跳医学VQA中大幅超越传统指令数据方法。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1391/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 806, \"height\": 750, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1391/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1568, \"height\": 691, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1391/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 803, \"height\": 417, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1391/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 805, \"height\": 416, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1391/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 813, \"height\": 418, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1391/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 814, \"height\": 415, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1391/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1646, \"height\": 514, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1391/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 417, \"height\": 309, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1391/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 416, \"height\": 305, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1391/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 801, \"height\": 421, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1391/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1625, \"height\": 832, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1391/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 806, \"height\": 721, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1391/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 728, \"height\": 226, \"label\": \"Table\"}]"
motivation: 现有医学VQA指令数据缺乏知识级多跳推理。
method: 利用多模态医学知识图谱自动生成多跳和难负例指令数据。
result: 微调后模型在多跳医学VQA任务上性能显著提升。
conclusion: MedKInstruct为医学多跳推理提供了高质量数据合成方法。
---

## Abstract
Medical visual question answering (MedVQA) requires models to provide accurate answers given a medical image and a corresponding question. Recently, instruction tuning of general large vision–language models (LVLMs) has become a dominant paradigm for this task, enabling open-ended predictions and effective integration of multimodal information. However, existing methods synthesize instruction data from image–caption pairs that primarily focus on visual attributes, rather than knowledge-level QA generation. This situation limits the model’s ability to learn relevant medical knowledge during training, thereby restricting its performance on MedVQA. Hence, this paper proposes MedKInstruct, which incorporates a multimodal medical knowledge graph (MMKG) to assist LVLMs in synthesizing knowledge-intensive instruction data. Additionally, we design an MMKG path–based reward function to train a stronger MedVQA model through reinforcement learning. Experimental results on the public datasets Slake and VQA-RAD show that MedKInstruct outperforms previous methods by 4.16% and 4.50%. The source code is available at the following link: https://github.com/Sonder-hang/MedKinstruct

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：现有医学视觉问答（MedVQA）的指令数据合成方法主要基于图像-标题对，生成的问答对仅聚焦于视觉属性（如肿瘤大小），缺乏对深层医学知识的推理能力。这限制了模型学习相关医学知识，从而制约了在复杂多跳推理问题上的表现。
- **整体含义**：本文提出利用多模态医学知识图谱（MMKG）来指导LVLM生成知识密集型指令数据，以增强模型的多跳推理和难负例识别能力，从而提升MedVQA系统的准确性和鲁棒性。

## 2. 论文提出的方法论：核心思想、关键技术细节、流程
- **核心思想**：通过MMKG为图像-标题对补充结构化医学知识，并基于此合成多跳和难负例的QA对；同时设计基于MMKG路径的奖励函数，通过强化学习（RL）优化模型推理过程。
- **关键技术细节**：
  - **两阶段知识匹配**：先精确字符串匹配（提取实体如“lung mass”与KG节点匹配），再基于BiomedCLIP的嵌入相似度进行模糊匹配，并用LVLM验证一致性，解决实体对齐问题。
  - **多跳QA生成**：将KG三元组分为短路径（系统级/器官级）和长路径（疾病及属性），分别用于生成简单和复杂的多跳问题。
  - **难负例QA生成**：通过多模态编码器检索与图像中异常最相似的疾病实体作为“硬负例”，插入固定模板生成“是否患某病”的问题，并附加对应KG路径。
  - **RL训练**：使用GRPO算法，奖励函数包含四部分：答案奖励（关键答案是否出现）、MMKG路径奖励（路径实体出现比例）、完整奖励（所有路径实体出现）、格式奖励（输出格式符合要求）。
- **流程说明**：
  1. 知识增强数据集准备：从图像-标题对提取实体，匹配MMKG获得相关三元组。
  2. 多模态指令数据合成：使用GPT-4o基于KG路径生成多跳QA和难负例QA，再处理成RL样本（提取关键答案和路径实体集）。
  3. MedVQA模型训练：先SFT（负对数似然损失），再RL（GRPO+上述奖励函数）。

## 3. 实验设计：数据集、基准、对比方法
- **数据集**：Slake（642张放射图像，7033个QA对，英文版）和VQA-RAD（315张放射图像，3515个QA对）。
- **基准与对比方法**：
  - 分类：LLaVA-Med-Instruct、PMC-Instruct（基于标题）；Huatuo-Instruct、Lingshu-Instruct（基于图像+标题）。
  - 基模型：LLaVA-v1.5-7B（通用VLM）和HuatuoGPT-Vision-7B（医学预训练VLM）。
  - 评估指标：封闭式问题（Accuracy）、开放式问题（Recall）。
- **实验设置**：所有方法统一为每个图像-标题对生成10个QA对；采用LoRA微调，rank=16，epoch=8，batch=4，lr=1e-4，温度0.0。

## 4. 资源与算力
- **未明确说明**：论文未披露具体GPU型号、数量或训练时长。仅提到“因GPU资源限制，RL实验仅在7B模型上进行”（7B-scale），且使用LoRA以减少显存。推测可能使用普通科研级GPU（如A100 40GB或类似），但无具体数据。

## 5. 实验数量与充分性
- **实验数量**：共进行了多组实验，包括：
  - 主实验（Table 2）：两种基模型 × 五种对比方法 + MedKInstruct(SFT/RL) = 14个配置。
  - 消融实验（Table 3）：对RL奖励组件、MMKG、图像模态的消融（4种变体）。
  - 难负例分析（Figure 3）：w/o HN、w/ Random、Ours对比。
  - 知识稀疏性分析（Figure 4）：不同KG比例（0%,40%,70%,100%）。
  - 匹配策略分析（Figure 5）：w/o FZM（去掉模糊匹配）、w/o MMKG、Ours。
  - 泛化能力分析（Figure 6）：跨数据集测试（训练集→测试集互换），对比Lingshu和人工标注。
- **充分性与公平性**：
  - 对照组设置全面，消融实验覆盖了关键组件（MMKG、路径奖励、完整奖励、图像模态）。
  - 所有生成方法均控制QA数量，评估指标统一，基模型一致，参数公开。
  - 客观性：使用公开数据集，代码开源，prompt在附录中提供。
  - 可能不足：仅测试7B模型，未验证更大规模模型；数据集仅涉及11个主要人体系统，缺乏细粒度场景（如胆囊）。

## 6. 论文的主要结论与发现
- MedKInstruct在Slake和VQA-RAD上分别提升4.16%和4.50%（HuatuoGPT-Vision-7B），优于所有现有指令数据合成方法。
- MMKG引入的知识级QA对显著增强了模型推理能力，尤其体现在多跳和难负例问题上。
- RL阶段（GRPO+路径奖励）相比仅SFT带来约2%的额外提升，证明细粒度中间推理监督有效。
- 难负例必须基于相似疾病检索才能获益，随机选择无效果。
- 知识图谱完整的比例越高，性能越好，说明整体知识覆盖度是关键。
- 两阶段匹配（精确+模糊）均不可或缺，模糊匹配进一步提升了召回率。
- 该方法在不同数据集间具有良好的泛化性（跨数据集训练测试）。

## 7. 优点：方法或实验设计上的亮点
- **创新性**：首次将MMKG系统性地融入指令数据合成全过程，同时覆盖多跳和难负例生成，且设计了基于路径的RL奖励函数。
- **实用性**：无需人工标注，全程自动化，且开源代码和提示词，易于复现和扩展。
- **实验设计的严谨性**：消融实验逐步解耦各组件贡献，对比基线涵盖主流方法，泛化测试验证鲁棒性。
- **奖励函数设计**：同时考虑答案、路径实体、完整性和格式，促使模型在推理中显式利用医学知识，增强可解释性。

## 8. 不足与局限
- **实验覆盖有限**：仅针对11个人体主要系统，未在更多细粒度医学领域（如消化、内分泌）验证，通用性受限。
- **模型规模限制**：因GPU资源仅测试7B模型，未探索更大规模（如32B）上的效果，无法判断缩放规律。
- **依赖外部MMKG**：知识图谱的质量和规模直接影响数据合成质量，当前MMKG可能不够完整，导致部分实体无法匹配。
- **模糊匹配的LVLM校验**：依赖GPT-4o等闭源模型进行一致性判断，可能引入额外成本和不稳定性。
- **RL训练的成本**：GRPO虽有效，但需要多次采样和推理，在更大模型上可能面临计算瓶颈。
- **偏差风险**：合成数据由GPT-4o生成，可能继承其内部偏差或知识错误，影响最终模型可靠性。

（完）
