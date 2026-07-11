---
title: Vision-language Incremental Learning with Dual Class-individual Memory
title_zh: 双类个体记忆的视觉语言增量学习
authors: "Fuhai Chen, Feng Zhang, XiaoGuang Ma, Yiyi Zhou, Jiarong Liu, Xuri Ge"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/37273/41235"
tags: ["query:post-multi"]
score: 8.0
evidence: 双类个体记忆的视觉语言增量学习
tldr: 针对视觉语言增量学习中图像与文本模态特性导致的内存瓶颈，提出双类个体记忆框架DCIM，分别管理类别级和场景级知识，缓解灾难性遗忘并实现高效知识迁移，在多个增量学习基准上取得最优性能。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: 现有增量学习忽略视觉与语言模态的差异导致内存分配问题。
method: 提出DCIM框架，包含双类个体记忆分别处理模态特性。
result: 在多个VLIL基准上达到最优，有效缓解遗忘。
conclusion: 双记忆设计是视觉语言增量学习的有效方案。
---

## Abstract
The emergence of multimodal technologies has propelled Vision-Language Incremental Learning (VLIL) into a research spotlight. Current VLIL approaches predominantly inherit unimodal paradigms, failing to address fundamental distinctions between visual and linguistic modalities. Crucially, the semantic gap between images and text creates divergent learning dynamics: visual data exhibits rich, distributed information while textual representations remain explicit and compact. Consequently, textual elements align with class-specific tasks, whereas individual images inherently span multiple such tasks, creating dual bottlenecks in class-level memory allocation and scene-level knowledge transfer. To overcome these challenges, we propose DCIM (Dual Class-Individual Memory), a novel framework featuring complementary mechanisms for vision-language continual learning. For class-level constraints, our Hierarchical Class Memory Management (HCMM) strategy dynamically allocates memory resources across object categories. It employs forgetting simulation to identify and preserve the most vulnerable samples, ensuring robust long-term knowledge retention. For scene-level adaptation, the Scene Reconstruction Memory(SRM) module captures generalized environmental representations, enabling contextual transfer to novel classes and disambiguation of semantically related concepts within shared scenes.Extensive experiments on two vision-language tasks, i.e., visual question answering (VQA) and Image captioning (IC), demonstrate the effectiveness and excellent generalization ability of our approach, achieving superior performance under continual learning settings.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **研究背景**：视觉-语言模型（VLMs）在静态基准上表现优异，但在动态场景中难以持续学习新知识，存在灾难性遗忘问题。
- **核心问题**：现有视觉语言增量学习（VLIL）方法直接继承单模态范式，忽视了视觉与文本模态的根本差异。文本特征紧凑且语义明确，适合类级任务；而视觉特征分布稀疏、上下文依赖强，导致**类级记忆分配**和**场景级知识迁移**两个瓶颈。实际应用中，新对象类别不断出现（如动物→人→地点），且同一场景中多个对象共存，模型需同时区分已知和未知类别并利用共同视觉上下文。
- **核心挑战**：如何同时管理类级遗忘（保持旧类知识）和场景级知识迁移（利用共享视觉上下文学习新类），防止知识混淆。

## 2. 论文提出的方法论：核心思想、关键技术细节
### 2.1 核心思想
提出**双类个体记忆（DCIM）**框架，包含两个互补模块：
- **层级类记忆管理（HCMM）**：通过动态内存分配和遗忘模拟策略，优化有限缓冲区的类级知识保存。
- **场景重建记忆（SRM）**：提取并保留场景级视觉特征，实现跨类知识迁移，同时通过自适应融合机制处理分布外输入。

### 2.2 关键技术细节
#### (1) 层级类记忆管理（HCMM）
- **动态内存分配**：基于每个旧类过去的平均遗忘率 \( \bar{F}_i \) 动态调整内存空间。权重计算：
  \[
  w_i = \frac{1/(\bar{F}_i + \epsilon)}{\sum_{j=1}^{t-1} 1/(\bar{F}_j + \epsilon)}
  \]
  更新后的内存分配：
  \[
  M_i^{new} = M_i^{current} - \frac{M_{total}}{t} \cdot w_i
  \]
  使得低遗忘率的类贡献更多内存给新类。
- **遗忘模拟策略**：三阶段损失测量：
  1. 初始损失 \( L_{init} \)（未训练模型）；
  2. 训练后损失 \( L_{trained} \)（当前任务学习后）；
  3. 模拟回放损失 \( L_{replay} \)（使用旧类内存样本训练后）。
  学习分数 \( S_{learn}=L_{init}-L_{trained} \)，遗忘分数 \( S_{forget}=L_{replay}-L_{trained} \)。
  综合优先级：\( \text{Priority} = \alpha \cdot S_{learn} + (1-\alpha) \cdot S_{forget} \)，保留高优先级样本。

#### (2) 场景重建记忆（SRM）
- **场景编码器**：将高维视觉特征 \( F_v \) 压缩为低维场景表示 \( F_{scene} \)：
  \[
  F_{scene} = \phi_2(W_2 \cdot LN(\phi_1(W_1 \cdot F_v)))
  \]
- **场景解码器**：从 \( F_{scene} \) 重建原始视觉特征 \( F_{recon} = \tanh(W_4 \cdot LN(\phi_3(W_3 \cdot F_{scene}))) \)
- **重建损失**：\( L_{recon} = \|F_v - F_{recon}\|_2^2 \)，用于训练时引导场景表示学习，推理时作为置信度指标。
- **自适应场景融合**：置信门控 \( g = \sigma(W_g \cdot [F_{scene}; L_{recon}; \text{sim}(F_{scene}, P^*)]) \) 动态结合重建场景特征与最近的原型表示（类别原型、场景原型），得到最终场景特征 \( F_{scene}^{final} = g \cdot F_{scene} + (1-g) \cdot F_{proto} \)。

## 3. 实验设计
### 数据集与基准
- **VQA任务**：VQA2.0数据集；**IC任务**：MS-COCO数据集。
- **类增量学习基准**：按对象超类划分8个顺序任务；并设计了两种划分策略：
  - **Taxonomy-Driven Division (TDD)**：类内具有语义关联（如所有动物）。
  - **Diverse-Driven Division (DDD)**：类随机分布。
- 同时评估了**反向任务顺序**（R-VQA2.0-TDD, R-VQA2.0-DDD, R-COCO-CIL），以消除顺序偏差。

### 对比方法
- 上界（UB）：同时访问所有任务数据。
- 下界（SFT）：顺序微调无防遗忘机制。
- 基准方法：iCaRL、ER、DER、TAM-CL、VQACL、DECO、GaB。DCIM还提供了加入知识蒸馏的变体DCIM(KD)。

### 评价指标
- 平均性能（AP）、遗忘度量（F）、相对遗忘度量（RF）。

## 4. 资源与算力
- **硬件**：两块NVIDIA RTX 3090 GPU。
- **超参数**：每个任务训练3个epoch，batch size 128，Adam优化器，初始学习率1e-4，内存缓冲区固定1000个样本。
- **资源消耗**（表3）：DCIM训练时内存12.8 GB，速度1.78秒/迭代（batch=128）；DCIM(KD)内存21.9 GB，速度2.86秒/迭代。说明DCIM在未使用知识蒸馏时是轻量的。
- **未明确说明**：总训练时长或具体GPU小时数。

## 5. 实验数量与充分性
- **主要实验**：包括VQA-CIL和IC-CIL两个任务，每个任务两种划分策略（TDD/DDD）及反向顺序，共4个设置（VQA有TDD、R-TDD、DDD、R-DDD；IC有COCO-CIL、R-COCO-CIL）。每个设置下与7-8种方法对比。
- **消融实验**（表4）：系统评估HCMM内部组件（动态内存分配DMA、遗忘模拟FSS、场景重建SR）的单独及组合贡献，共8种配置。
- **定性分析**：使用GradCAM可视化注意力图，展示了跨类知识迁移（如利用人物羽绒服特征学习“winter”概念）。
- **总结**：实验覆盖了不同任务、不同划分策略、不同顺序，消融充分，对比方法全面，公平性较好（统一内存大小、评价指标）。但仅限于VQA和IC两个任务，未涉及其他VLIL任务（如视觉推理、多模态检索）。

## 6. 论文的主要结论与发现
- DCIM框架在VQA和IC两个类增量学习基准上，平均性能（AP）全面优于现有方法，且遗忘更低。
- 关键发现：场景级知识迁移（SR模块）贡献最大（+1.87% AP，-0.75% F），说明利用共享视觉上下文对缓解灾难性遗忘至关重要。
- 遗忘模拟策略和动态内存分配具有协同作用，组合后效果优于单独使用。
- 可视化证明模型在增量学习中能够保留旧类注意力，并利用已知场景特征辅助新类学习。

## 7. 优点
- **方法亮点**：
  - 首次专门针对视觉-语言增量学习中的模态差异提出双记忆机制。
  - 遗忘模拟策略设计巧妙（利用旧内存样本模拟未来干扰），无需访问未来数据。
  - 场景重建与原型自适应融合，有效处理分布外场景，增强鲁棒性。
- **实验设计亮点**：
  - 建立了标准化类增量学习基准（TDD/DDD及反向顺序），更贴近真实场景。
  - 对比方法涵盖经典和最新SOTA，包括基于知识蒸馏的变体。
  - 消融实验全面，验证了各组件贡献。
  - 提供代码开源（github链接）。
- **效率亮点**：DCIM（无KD）在性能领先的同时资源消耗较低，具备实际部署潜力。

## 8. 不足与局限
- **实验覆盖局限**：仅评估了VQA和IC两个任务，未涵盖其他视觉-语言任务（如视觉推理、指代表达理解、多模态对话）。
- **模型规模局限**：仅使用VL-T5作为骨干，未验证对更大规模模型（如BLIP、LLaVA）的适用性。
- **语言模式假设**：设定语言模式稳定（仅新对象类出现），实际场景中问题和caption格式也可能演变，论文未讨论。
- **遗忘模拟策略**：依赖旧内存样本进行模拟，若初始内存样本质量差或分布偏差大，可能影响优先级计算。
- **评估指标**：AP和F对顺序敏感，虽引入反向顺序但未系统分析顺序效应大小。
- **可扩展性**：缓冲区固定1000样本，未探讨更大缓冲区或更少样本场景的性能。
- **实际应用限制**：未在真实连续数据流（如视频流）上验证，仅基于离线拆分的数据集。

（完）
