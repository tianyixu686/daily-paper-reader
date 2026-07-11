---
title: Can Post-Training Transform LLMs into Causal Reasoners?
title_zh: 后训练能将大语言模型转变为因果推理者吗？
authors: "Junqi Chen, Sirui Chen, Chaochao Lu"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.839.pdf"
tags: ["query:post-multi"]
score: 9.0
evidence: 评估包括RLHF在内的后训练对因果推理的影响
tldr: 针对后训练能否提升大语言模型因果推理能力的问题，构建CausalGym基准，系统评估SFT、DPO、KTO、PPO和GRPO五种后训练方法，实验表明适当的后训练能使小型LLM在因果任务上达到甚至超越大型模型，揭示后训练在因果推理中的作用。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.839/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 779, \"height\": 1136, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.839/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 649, \"height\": 684, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.839/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 650, \"height\": 671, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.839/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 648, \"height\": 685, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.839/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 649, \"height\": 689, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.839/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 781, \"height\": 785, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.839/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 796, \"height\": 1056, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.839/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1457, \"height\": 692, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.839/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1453, \"height\": 733, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.839/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1437, \"height\": 655, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.839/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1448, \"height\": 855, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.839/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1458, \"height\": 1023, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.839/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1310, \"height\": 542, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.839/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 775, \"height\": 287, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.839/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1426, \"height\": 613, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.839/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 769, \"height\": 357, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.839/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 750, \"height\": 417, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.839/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1408, \"height\": 160, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.839/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1659, \"height\": 856, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.839/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1654, \"height\": 897, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.839/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1638, \"height\": 212, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.839/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1653, \"height\": 900, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.839/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1651, \"height\": 899, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.839/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1603, \"height\": 115, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.839/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1538, \"height\": 288, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.839/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1341, \"height\": 244, \"label\": \"Table\"}]"
motivation: 后训练对因果推理能力的影响尚未被充分探索。
method: 构建CausalGym数据集并系统评估五种后训练方法。
result: 适当后训练显著提升因果推理，小型模型媲美大型模型。
conclusion: 后训练是增强LLM因果推理的有效手段。
---

## Abstract
Causal inference is essential for decision-making but remains challenging for non-experts. While large language models (LLMs) show promise in this domain, their precise causal estimation capabilities are still limited, and the impact of post-training on these abilities is insufficiently explored. This paper examines the extent to which post-training can enhance LLMs’ capacity for causal inference. We introduce CausalGym, a comprehensive dataset comprising seven core causal tasks for training and five diverse test sets. Using this dataset, we systematically evaluate five post-training approaches: SFT, DPO, KTO, PPO, and GRPO. Across five in-domain and four existing benchmarks, our experiments demonstrate that appropriate post-training enables smaller LLMs to perform causal inference competitively, often surpassing much larger models. Our 14B-parameter model achieves 93.5% accuracy on the CaLM benchmark, compared to 55.4% by OpenAI o3. Furthermore, the post-trained LLMs exhibit strong generalization and robustness under real-world conditions such as distribution shifts and noisy data. Collectively, these findings provide the first systematic evidence that targeted post-training can produce reliable and robust LLM-based causal reasoners.

---

## 论文详细总结（自动生成）

# 论文总结：Can Post-Training Transform LLMs into Causal Reasoners?

## 1. 核心问题与整体含义（研究动机和背景）

- **研究动机**：因果推理是决策的核心，但非专家难以正确使用现有因果推断库（如DoWhy）。大语言模型（LLM）虽然展现了推理潜力，但在精确的因果效应估计上仍存在局限，尤其缺乏对后训练方法（如SFT、RLHF）如何影响因果推理能力的系统研究。
- **核心问题**：**后训练能否将LLM转变为有效的因果推理者？** 即通过后训练，是否能让小型LLM在因果推理任务上达到甚至超越大型LLM（如OpenAI o3、DeepSeek-R1 671B）的水平？
- **整体含义**：首次系统性地探究了主流后训练方法（监督微调、离线RL、在线RL）对LLM因果推断能力的影响，并证明通过适当的在线RL（尤其是GRPO）可以在14B参数的小模型上实现顶尖的因果推理性能，使因果推断更易用、可审计。

## 2. 方法论：核心思想、关键技术细节、公式/算法流程

- **核心思想**：构建一个覆盖7种因果任务的训练集（CauGym），采用**冷启动（Cold Start）** + **后训练**的两阶段策略。冷启动使用少量SFT数据使模型初步具备因果推理基础，然后分别应用SFT、DPO、KTO、PPO、GRPO等五种后训练方法，对比其效果。
- **关键技术细节**：
  - **训练数据生成**：基于随机生成的10节点DAGs，通过语义化节点（真实、随机、假名三种方式）和单层感知机构建结构因果模型（SCM），然后采样生成概率，结合DoWhy识别后门调整集和中介集，生成7种因果任务（ATE, CDE, ETT, NDE, NIE, PN, PS）的问题-答案-符号解。
  - **后训练方法**：
    - **SFT**：使用大模型（DeepSeek-R1-0528-671B）重述的正确推理轨迹作为监督数据。
    - **离线RL（DPO/KTO）**：构建正负样本对（正样本：重述的正确推理；负样本：无指导的错误推理或缺失关键步骤的推理），使用DPO/KTO目标优化。
    - **在线RL（PPO/GRPO）**：仅需问题和最终答案的奖励（最终答案正确性+格式），无需标注推理过程。PPO使用独立评论家网络估计优势，GRPO使用当前策略生成响应的平均奖励作为基线。
  - **公式（文字说明）**：
    - SFT：最大化正确回答的似然。
    - DPO：直接偏好优化，利用正负样本对优化策略与参考策略的比值。
    - KTO：基于前景理论的优化，区分期望和厌恶样本。
    - PPO/GRPO：最大化带裁剪的策略梯度目标，其中PPO用评论家网络估计优势，GRPO用组平均奖励代替。

## 3. 实验设计

- **数据集/场景**：
  - **训练**：CauGym训练集，包含3500个问题，覆盖7种因果任务。
  - **测试**：
    - **域内**：CaLM（lite版，包含7种数值因果任务）。
    - **泛化测试**：CauGym-rephrased（重述问题）。
    - **内化测试**：CauGym-omitted（省略任务指示）、CauGym-deconfounding（仅可通过后门准则解决）。
    - **鲁棒性测试**：CauGym-redundant（多余条件）、CauGym-insufficient（缺少必要条件）。
    - **外部数学基准**：Math 500、Minerva Math、AMC 2023。
- **对比方法**：
  - 基线模型：Llama-3.3-70B, Qwen3-235B, DeepSeek-R1-0528-671B, Gemini 2.5 Pro, OpenAI o3, DeepSeek-R1-Distill-Qwen-14B（base）。
  - 后训练方法：Cold Start Base（仅冷启动）、SFT、DPO、KTO、PPO、GRPO（均在DeepSeek-R1-Distill-Qwen-14B上训练）。
- **评估指标**：准确率（精确匹配），每个实验5次独立运行取均值。
- **消融实验**：
  - 基模型消融：Mistral-7B、DeepSeek-R1-Distill-Llama-8B。
  - 模型规模消融：7B、14B、32B（DeepSeek-R1-Distill-Qwen系列）。
  - GRPO变体消融：无思考格式奖励、仅使用真实语义变量名称的训练数据。

## 4. 资源与算力

- 论文未明确说明使用的GPU型号、数量以及训练时长等具体算力信息。仅提及在14B模型上使用LoRA进行SFT训练3个epoch，其他训练（DPO、KTO、PPO、GRPO）也均为3个epoch。实验细节中未提供训练时间或硬件配置。这一点是论文的缺失。

## 5. 实验数量与充分性

- **实验数量**：相当充分。
  - 主实验：在CaLM基准上对比7种后训练方法与多个基线（5个后训练变体 + 冷启动 + 多个外部大模型）。
  - 泛化测试：1个数据集（CauGym-rephrased）。
  - 内化测试：2个数据集（omitted, deconfounding）。
  - 鲁棒性测试：2个数据集（redundant, insufficient）。
  - 数学能力测试：3个数学基准。
  - 基模型消融：2种其他基模型。
  - 模型规模消融：3种规模（7B, 14B, 32B）。
  - GRPO变体消融：2种变体。
  - 失败分析：对GRPO、SFT、Cold Start模型在3个测试集上按错误类型（任务识别、SCM识别、公式识别、公式应用、数值计算、意外行为）进行分布分析。
  - 与其他因果推理基准对比：CLadder、CLEAR、CausalProbe-E。
- **充分性与公平性**：
  - 实验设计较为全面，覆盖了泛化、内化、鲁棒性等多个维度，消融实验考虑了模型架构、规模和方法变体。
  - 对比基线包括当前最强模型（o3, DeepSeek-R1-671B, Gemini 2.5 Pro等），具有代表性。
  - 但未说明重复运行的具体方差（仅提均值），且数学基准上的性能提升不明显，可能表明因果推理能力的提升并未严重损害数学能力（但也没显著提升，这可能是合理的）。
  - 总体而言，实验较为充分，结论有支撑，但缺少资源消耗对比和统计显著性检验。

## 6. 主要结论与发现

- **后训练能显著提升小模型的因果推理能力**：14B的DeepSeek-R1-Distill-Qwen-14B通过GRPO后训练，在CaLM上达到93.5%准确率，远超o3（55.4%）和DeepSeek-R1-671B（57.0%）。
- **在线RL方法（GRPO, PPO）优于离线RL（DPO, KTO）和SFT**：GRPO在几乎所有测试集上取得最佳结果，PPO次之。离线RL方法提升有限，DPO甚至只比冷启动高1.4%。
- **后训练模型展现出强泛化、内化和鲁棒性**：
  - 对问题重述（CauGym-rephrased）性能下降很小。
  - 在省略任务指示（CauGym-omitted）下，在线RL方法仍能识别任务类型，离线RL和SFT大幅下降。
  - 在必须使用后门准则（CauGym-deconfounding）时，GRPO表现最好，而大型模型（DeepSeek-R1-671B）表现差。
  - 对冗余和缺失信息（CauGym-redundant, insufficient）也表现出良好鲁棒性。
- **后训练不会显著降低数学推理能力**：在三个数学基准上，后训练模型性能与基础模型基本持平。
- **GRPO的成功不依赖于特定的奖励设计**：无思考格式奖励的GRPO变体性能仅轻微下降，表明训练框架本身更重要。

## 7. 优点

- **系统性与首创性**：首次系统评估了五种主流后训练方法对因果推理的影响，填补了领域空白。
- **全面的测试维度**：不仅测试域内性能，还从泛化、内化、鲁棒性三个角度设计了专门的测试集，使评估更深入。
- **控制变量与消融充分**：进行了基模型、模型规模、RL变体等多种消融，结果可靠。
- **数据集构建方法可复现**：基于随机SCM和数据生成流程，可扩展。
- **小模型超越大模型**：实验证明了算法选择比模型规模更关键，具有实际指导意义。

## 8. 不足与局限

- **算力资源未披露**：没有提及GPU型号、数量、训练时长等，不利于其他研究者复现成本评估。
- **训练数据仅基于合成SCM**：可能无法完全反映真实世界的因果结构复杂性，现实应用中的噪声、非线性、混淆因素未充分测试。
- **任务范围有限**：仅涉及7种标准因果效应估计，未覆盖更复杂的因果发现、工具变量、断点回归等方法。
- **离线RL方法表现不佳的原因未充分分析**：论文指出了DPO/KTO效果差，但未深入探讨为何在线RL更适合因果推理任务。
- **数学基准性能持平而非提升**：虽然未下降是好事，但也意味着因果推理能力提升可能并未显著泛化到其他推理领域。
- **未评估部署时的推理成本**：后训练可能增加了模型在因果任务上的准确率，但未比较推理速度或计算开销。
- **仅使用单一基模型（DeepSeek系列）进行主要实验**：虽然消融中用了Mistral-7B和Llama-8B，但主实验只基于一个模型族，可能存在偏置。
- **统计显著性未报告**：仅提供均值，未给出置信区间或误差棒。

（完）
