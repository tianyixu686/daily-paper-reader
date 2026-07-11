---
title: "Multimodal Unlearning Across Vision, Language, Video, and Audio: Survey of Methods, Datasets, and Benchmarks"
title_zh: 跨视觉、语言、视频和音频的多模态遗忘：方法、数据集与基准综述
authors: "Nobin Sarwar, Shubhashis Roy Dipta, Zheyuan Liu, Vaidehi Patil"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.1379.pdf"
tags: ["query:post-multi"]
score: 7.0
evidence: 多模态遗忘综述
tldr: 本文综述了多模态遗忘（unlearning）领域的最新进展，涵盖视觉、语言、视频和音频模态。系统梳理了现有方法、数据集和基准测试，分析了多模态基础模型中遗忘敏感、版权或偏见知识的挑战。指出在当前数据删除请求和隐私法规背景下，多模态遗忘对于模型可维护性的重要性，并总结了开放问题。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1379/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 770, \"height\": 452, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1379/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1598, \"height\": 1189, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1379/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 769, \"height\": 553, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1379/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 795, \"height\": 333, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.1379/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 650, \"height\": 558, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1379/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 803, \"height\": 261, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1379/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1628, \"height\": 890, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1379/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1635, \"height\": 1187, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1379/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1657, \"height\": 2403, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1379/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1592, \"height\": 1970, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.1379/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1622, \"height\": 1232, \"label\": \"Table\"}]"
motivation: 多模态模型可能编码有害或敏感的跨模态关联，且重新训练成本高，亟需系统性综述来指导该领域发展。
method: 以统一视角综述了跨多种模态的遗忘方法，包括基于梯度、表示操作、蒸馏等技术，并整理了相关数据集。
result: 总结了现有方法在图像、文本、视频和音频遗忘任务上的性能对比，指出了可扩展性和评估标准的不足。
conclusion: 该综述为多模态遗忘研究提供了全景参考，有助于推动隐私保护和安全的多模态模型部署。
---

## Abstract
With the growing adoption of VLMs, DMs, LLMs, and AFMs, these multimodal foundation models can inadvertently encode sensitive, copyrighted, biased, or unsafe cross-modal associations that originate from their training data. Retraining after deletion requests or policy updates is often impractical, and targeted forgetting remains difficult because knowledge is distributed across shared representations. Multimodal unlearning addresses this challenge by enabling selective removal across modalities while retaining overall utility. This survey offers a unified, system-oriented view of multimodal unlearning across vision, language, audio, and video, grounded in recent advances, emerging applications, and open problems. Our taxonomy enables systematic comparison across model architectures and modalities, clarifying trade-offs among deletion strength, retention, efficiency, reversibility, and robustness. This survey highlights open problems and practical considerations to support future research and deployment of multimodal unlearning.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究动机**：随着视觉语言模型（VLM）、扩散模型（DM）、大语言模型（LLM）和音频基础模型（AFM）等**多模态基础模型**的广泛应用，这些模型在训练过程中可能无意中编码了敏感、受版权保护、有偏见或不安全的跨模态关联。当面临数据删除请求或政策更新时，**重新训练整个模型成本极高且不切实际**，而由于知识分散在共享表示中，**针对性遗忘（targeted forgetting）** 非常困难。
- **整体含义**：**多模态遗忘（Multimodal Unlearning）** 成为解决这一挑战的核心技术——它能够**选择性地移除特定模态中的知识**（如一张图片、一个概念、一个身份或一段音频），同时在其余数据上保持模型整体效用。本文提供了一篇**统一、系统导向的综述**，覆盖视觉、语言、音频和视频模态，为未来研究和部署提供了结构化的参考。

---

### 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：采用**系统优先（system-first）** 的分类视角，按**干预阶段和控制路径**组织方法，而不是传统的算法中心分类。主要分为**数据侧干预、训练时编辑、架构约束、无训练遗忘、解码时控制**五大类（图2）。
- **关键技术细节**：
  - **数据侧干预**：修改输入数据（如添加扰动、清洗数据、规范化提示）来降低目标样本的可学习性，而不改变模型权重。例如：`Unlearnable Clusters`、`CleanCLIP`。
  - **训练时编辑**：在训练过程中通过梯度直接优化或约束更新来抑制遗忘集的同时保持保留集性能。包括直接梯度方法（如`MultiDelete`）、约束更新（如`MUNBa`）、掩码驱动的选择性遗忘（如`SalUn`）、蒸馏（如`SSD`）。
  - **架构约束**：通过修改网络结构（剪枝、冻结、重新生长）或限制层范围来定位和移除目标概念。例如：`FreezeAsGuard`、`SLUG`。
  - **无训练遗忘**：在参数空间或表示空间中进行闭式编辑，无需迭代训练。包括权重空间线性操作（如`Task Arithmetic`、`NegMerge`）和表示投影（如`Safe-CLIP`、`CURE`）。
  - **解码时控制**：在生成阶段改变采样轨迹或条件信号，而不改变模型参数。如`Dynamic Negative Guidance`、`SteerDiff`。
- **公式化框架**：
  - **通用遗忘目标**：$\min_\theta J(\theta) = F_{\text{forget}}(\theta; D_f) + \lambda F_{\text{retain}}(\theta; D_r)$，其中第一项抑制遗忘集关联，第二项保留保留集效用。
  - **差分隐私等价标准**：定义 $(\varepsilon,\delta)$ 遗忘准则，保证遗忘后模型分布与重新训练的模型分布不可区分。
  - **VLM遗忘**：使用概念铰链损失和掩码更新 $\Delta\theta = -\eta S \odot \nabla_\theta (L_{\text{forget}} + \lambda L_{\text{retain}})$。
  - **扩散模型遗忘**：教师引导损失使去噪器在目标概念上对齐无条件或安全教师，同时保持保留集生成质量。

---

### 3. 实验设计：使用的数据集/场景、benchmark、对比方法

- **数据集**：综述整理了多模态遗忘常用的数据集，按应用场景分组（见表2、4、5、6），例如：
  - **身份遗忘**：CelebA、VGGFace2、VoxCeleb1（音频）。
  - **情感与视频遗忘**：EmoSet、UCF101。
  - **版权遗忘**：CPDM、MusicCaps（音频）。
  - **知识QA与指令探测**：VQA v2、OK-VQA、ScienceQA。
  - **语音遗忘**：Speech Commands、LibriSpeech。
  - **安全鲁棒性遗忘**：I2P、SneakyPrompt、SafeSora。
  - **类别遗忘**：ImageNet、CIFAR、Stanford Cars。
- **Benchmark**：综述专门整理了多模态遗忘基准（表3），包括：
  - **MU-Bench**（多任务多模态）、**MLLMU-Bench**（VLM隐私）、**PEBench**（合成身份与事件）、**UMU-Bench**、**CLEAR**、**FIUBench**、**UnSLU-BENCH**（音频）、**CPDM**、**UnlearnCanvas**、**Holistic Unlearning**、**Six-CD**、**MMUBench**、**UnLOK-VQA**、**SafeEraser**。
- **对比方法**：作为综述，本身不进行实验对比，而是系统对比了上述各类方法的效果、干预点、遗忘强度、保留能力、效率等维度。本文不提供新的实验结果。

---

### 4. 资源与算力

- **论文明确说明**：作为综述，本文**没有进行任何新的训练或实验**，因此未报告具体的算力资源（GPU型号、数量、训练时长等）。仅在附录B.6中提及**计算与环境预算**，指出近年来研究开始报告**GPU墙时（WCT）、峰值内存、FLOPs**以及**碳排放（CO₂e）** 等指标，但未汇总全局算力。
- **总结**：资源与算力细节**未给出**，因为本文是对现有工作的系统性文献综述。

---

### 5. 实验数量与充分性

- **实验数量**：本文无原始实验，但**覆盖了截至2026年2月的超过100篇相关论文的实证结论**，并在多个表格中总结了数据集、基准和方法。
- **充分性**：
  - **全面性高**：覆盖视觉、语言、视频、音频四大模态，并涉及隐私、安全、版权、公平性、后门防御等多种应用场景。
  - **系统性强**：从方法、数据集、基准、评估指标四个维度进行结构化组织，且提供了统一分类法，便于对比。
  - **客观性**：不进行自身实验，但基于已发表论文的排名和结果进行归纳，保持了相对客观。
  - **潜在不足**：
    - 一些快速发展的子领域（如音频、视频遗忘）的论文数量相对较少，覆盖可能不如视觉-语言充分。
    - 文中提到部分基准可能仅基于单一架构或合成数据，外推性受限。
    - 由于综述范围广，深度有限，未对每个方法的性能做定量meta分析。

---

### 6. 论文的主要结论与发现

- **多模态遗忘是可行的，但挑战巨大**：目前已有多种干预策略（数据、训练、架构、无训练、解码时）能够实现选择性遗忘，但每种方法都在**遗忘强度、效用保留、效率、鲁棒性和可逆性**之间存在权衡。
- **评估仍然不成熟**：现有基准和指标多为代理信号，难以证明真正的“遗忘”；许多方法在对抗攻击下失效（如遗忘的概念可以通过精心构造的提示重新激活）。
- **跨模态泛化和可扩展性不足**：大多数方法仅在特定模型、少量概念或单一模态上评估，未见对大规模多模态基础模型的系统性验证。
- **关键开放问题**：包括理论保证（无正式删除证明）、评估可靠性、对抗鲁棒性、效用-遗忘权衡、统一基准的缺失等。
- **未来方向**：时间动态模态、在线连续遗忘、细粒度控制、推理时防御、跨模态泄漏缓解等。

---

### 7. 优点

1. **系统性视角**：采用**系统优先（干预点和控制路径）的分类法**，比传统的算法中心分类更有利于理解实际部署中的权衡和设计选择。
2. **跨模态覆盖广**：同时涵盖图像、文本、视频和音频，是首个统一综述多模态遗忘（而不只是文本-图像）的工作。
3. **资源丰富**：提供了详尽的**数据集表格**（表2,4,5,6）和**基准表格**（表3），并维护了开源仓库（Awesome-Multimodal-Unlearning）。
4. **理论框架清晰**：给出了统一的数学形式化（如 $(\varepsilon,\delta)$ 遗忘准则、通用优化目标），便于不同模态方法进行比较。
5. **问题导向**：清晰指出了当前评估的不可靠性、对抗脆弱性、缺乏理论保证等核心问题，并给出了未来研究路线图。
6. **实用性**：附录中包含了详细的评估指标定义（附录B）和应用场景描述（附录E），对从业者具有直接参考价值。

---

### 8. 不足与局限

1. **作为综述的固有局限**：虽然覆盖内容广，但**没有进行原创实验或定量对比**，无法提供不同方法在同一基准上的直接性能排序。
2. **部分领域覆盖较浅**：音频和视频遗忘的相关工作仍然较少，综述对这些模态的讨论深度不如视觉-语言。
3. **算法细节深度有限**：受篇幅限制，并未深入每一种方法的具体算法公式和优化细节，读者需查阅原始论文。
4. **基准碎片化问题仍然存在**：尽管列出了多个benchmark，但这些基准本身在任务、概念集、评估指标上不一致，难以实现公平比较。
5. **时效性**：由于该领域发展迅速，截至截稿日期后的新方法可能未被包含，作者承认“保持完全最新具有挑战性”。
6. **未涵盖的数据类型**：明确排除了时间序列、表格、传感器等结构化或流式数据，限制了结论的通用性。
7. **理论保证部分薄弱**：虽然提出了 $(\varepsilon,\delta)$ 框架，但大部分现有方法并未提供此类保证，综述也承认“多数方法仍然是启发式的”。

（完）
