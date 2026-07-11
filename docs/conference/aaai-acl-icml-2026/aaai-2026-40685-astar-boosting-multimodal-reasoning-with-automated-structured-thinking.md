---
title: "AStar: Boosting Multimodal Reasoning with Automated Structured Thinking"
title_zh: AStar：通过自动结构化思维增强多模态推理
authors: "Jinyang Wu, Mingkuan Feng, Guocheng Zhai, Shuai Zhang, Zheng Lian, Fangrui Lv, Pengpeng Shao, Ruihan Jin, Zhengqi Wen, Jianhua Tao"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/40685/44646"
tags: ["query:post-multi"]
score: 8.0
evidence: 结构化思维增强多模态推理
tldr: 本文提出AStar，一种免训练的自动结构化思维范式，用于增强多模态大模型的复杂视觉推理能力。通过引入轻量级高阶推理模式库“思维卡片”，无需搜索或后训练即可引导模型进行结构化推理。实验表明，AStar在多个视觉推理基准上显著提升了推理准确性和效率，避免了后训练的不稳定和搜索的高代价。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: 现有基于搜索或后训练的多模态推理方法效率低或训练不稳定，需要一种训练免费且高效的推理增强方案。
method: 提出自动结构化思维范式，利用从样本中抽象出的高层次推理模式（思维卡片）引导模型逐步推理。
result: 在多个多模态推理任务上，AStar在减少计算开销的同时取得了超越搜索方法和后训练方法的性能。
conclusion: 该工作为多模态推理提供了轻量级、即插即用的增强工具，有望推广至更多视觉语言应用。
---

## Abstract
Multimodal large language models excel across diverse domains but struggle with complex visual reasoning tasks. To enhance their reasoning capabilities, current approaches typically rely on explicit search or post-training techniques. However, search-based methods suffer from computational inefficiency due to extensive solution space exploration, while post-training methods demand substantial data, computational resources, and often exhibit training instability. To address these challenges, we propose **AStar**, a training-free, **A**utomatic **S**tructured **t**hinking paradigm for multimod**a**l **r**easoning. Specifically, we introduce novel "thought cards", a lightweight library of high-level reasoning patterns abstracted from prior samples. For each test problem, AStar adaptively retrieves the optimal thought cards and seamlessly integrates these external explicit guidelines with the model’s internal implicit reasoning capabilities. Compared to previous methods, AStar eliminates computationally expensive explicit search and avoids additional complex post-training processes, enabling a more efficient reasoning approach. Extensive experiments demonstrate that our framework achieves 53.9% accuracy on MathVerse (surpassing GPT-4o's 50.2%) and 32.7% on MathVision (outperforming GPT-4o's 30.4%). Further analysis reveals the remarkable transferability of our method: thought cards generated from mathematical reasoning can also be applied to other reasoning tasks, even benefiting general visual perception and understanding. AStar serves as a plug-and-play test-time inference method, compatible with other post-training techniques, providing an important complement to existing multimodal reasoning approaches.

---

## 论文详细总结（自动生成）

# 论文《AStar：通过自动结构化思维增强多模态推理》中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：多模态大模型（MLLMs）在复杂视觉推理任务上表现不佳。现有增强方法（搜索式、后训练式）存在计算效率低、资源需求大、训练不稳定等缺陷。
- **研究动机**：希望在不进行显式搜索或大量后训练的前提下，提升MLLMs的推理能力，同时保持高效和灵活性。
- **整体含义**：提出一种**免训练、自动结构化思维**范式（AStar），利用从少量先验样本中抽象出的高层推理模式（“思维卡片”）引导模型推理，实现性能与效率的平衡，并具备跨任务迁移能力。

## 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程

### 核心思想
- 构建轻量级的“思维卡片”库，存储抽象的高层推理模式（如动作序列）。
- 测试时根据问题特征（复杂度和语义）自适应检索最相关的思维卡片，作为显式外部指导，与模型内在隐式推理能力结合，生成候选解并进行验证。

### 关键技术细节
1. **视觉推理动作定义**：定义6种推理动作：视觉解析（VP）、系统分析（SA）、单步思考（OST）、链式思考（CoT）、分治（DC）、自我反思（SR）。
2. **思维卡片构建**（分两阶段）：
   - Phase 1：使用蒙特卡洛树搜索（MCTS）在500个种子样本上生成高质量推理路径。MCTS包含选择（UCT公式）、扩展、模拟、反向传播四个操作，节点价值通过自洽性投票似然作为奖励。
   - Phase 2：从树搜索获得的路径中，通过VOC（Value of Computation）启发式指标选择最优路径（平衡奖励与推理成本），并按照问题复杂度和文本-图像语义聚类，提炼为抽象思维卡片。每个卡片包含高层模板（动作序列）及平均复杂度和语义嵌入。
3. **自适应推理与验证**：
   - 对测试问题，计算其复杂度和CLIP语义嵌入，与卡片库进行最近邻匹配（分别按语义相似度和复杂度差异排序，综合排名选前5）。
   - 实例化5张卡片得到5个候选解，通过自洽性检查和文本领域奖励模型选择最优解。

### 算法流程（文字说明）
1. 初始化动作空间和卡片库。
2. 对每个种子问题，用MCTS获取推理路径，选出最佳路径存入库。
3. 从路径库中蒸馏出抽象思维卡片。
4. 对于测试问题，通过卡片匹配选出5张最相关卡片。
5. 对每张卡片实例化推理，得到候选解，用自洽性+奖励模型选出最终答案。

## 3. 实验设计：数据集、基准、对比方法

### 数据集
- **数学推理**：MathVista、MathVerse、MathVision
- **一般推理**：MMMU
- **领域特定科学推理**：GAOKAO-MM
- **视觉感知与理解**：ChartQA、MMStar、BLINK

### 基准（baselines）
- **开源通用MLLMs**：MiniGPT4-7B、LLaVA-1.5-13B、SPHINX-8x7B、InternVL2-8B、Qwen2-VL-7B等
- **开源推理MLLMs**：Math-LLaVA-13B、Math-PUMA-7B、MultiMath-7B、URSA-8B（SFT）、R1-VL-7B（GRPO）、LMM-R1-3B（PPO）、MM-Eureka-7B（GRPO）
- **搜索方法**：Mulberry-7B
- **闭源模型**：GPT-4o

### 评价指标
各数据集官方评估指标（准确率）。

## 4. 资源与算力

- **训练过程**：AStar**完全免训练**，不涉及参数更新。
- **预处理**：仅需500个种子样本，约50分钟生成思维卡片（图2为例）。
- **数据量**：相比Mulberry（260K）、URSA-8B（1100K），AStar仅需0.5K，数据量减少520~2200倍。
- **硬件**：未明确说明具体GPU型号和数量，但强调资源需求小。

## 5. 实验数量与充分性

- **实验覆盖**：在4个领域8个数据集上进行了广泛评估，包括数学推理、通用推理、科学推理、视觉感知等。
- **对比方法**：涵盖四大类（通用、推理专用、搜索、闭源），共十余个模型，对比充分。
- **消融实验**：系统消融了思维卡片、卡片匹配、验证策略等组件。
- **额外分析**：种子数据集大小影响、pass@16结果、灵活性（与后训练结合）、跨领域迁移性、弱到强泛化等。
- **公平性**：使用相同骨干模型（Qwen2.5-7B、Qwen2-VL-2/7B）对比，但不同基线模型训练数据量和算力不同，可能存在不公平，但论文已点明优势在于效率与性能平衡。

**评估**：实验数量较多，覆盖全面，消融完整，结论可信。但部分对比如GPT-4o为闭源，无法控制完全相同条件。

## 6. 论文的主要结论与发现

- AStar显著提升多模态推理性能：在MathVerse上以7B模型超越GPT-4o（53.9% vs 50.2%），MathVision上32.7% vs 30.4%。
- **高效**：仅需0.5K样本和50分钟预处理，远少于其他方法。
- **灵活**：可作为即插即用的测试时推理方法，与SFT、RL（PPO/GRPO）结合进一步提升性能。
- **可迁移**：数学领域构造的思维卡片可迁移至科学推理、视觉感知等非数学任务，甚至增强GPT-4o。
- **核心机制有效**：思维卡片（抽象结构化模式）是性能提升关键，自适应卡片匹配优于随机选择。

## 7. 优点

- **方法创新**：提出“思维卡片”这一轻量级抽象推理库，结合外显指导和内隐推理，无需训练。
- **效率突出**：相比搜索和后训练方法，数据需求和计算成本大幅降低。
- **迁移性良好**：跨任务、跨模型（甚至增强更强模型）展现通用性。
- **即插即用**：可兼容多种后训练技术，实用性强。
- **实验充分**：多维度评估，消融验证各组件贡献。

## 8. 不足与局限

- **依赖种子数据**：思维卡片提取依赖少量高质量推理路径，若种子数据偏差可能影响泛化。
- **通用性验证不足**：虽然展示了跨领域迁移，但仅验证了从数学到其他任务，未探索反向迁移或其他来源。
- **视觉验证模型缺失**：验证环节依赖文本域奖励模型，缺乏专门视觉验证机制，可能遗漏视觉误导问题。
- **基准对比公平性**：部分基线（如GPT-4o）为闭源，评估条件不完全一致；搜索方法（Mulberry）可能因使用不同骨干而难以直接对比。
- **可扩展性**：目前仅尝试6种推理动作，未来可能需扩展更丰富动作集。
- **未讨论失败案例**：未深入分析性能下降或错误模式。

（完）
