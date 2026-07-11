---
title: "Grow-on-Demand: Sparse and Adaptive Expert Expansion for Continual Instruction Tuning"
title_zh: 按需增长：持续指令调优的稀疏自适应专家扩展
authors: "Ying Zhang, Xingyue Guo, Yu Zhao, Xuhui Sui, Baohang Zhou, Xinying Qian, Xiaojie Yuan"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/40077/44038"
tags: ["query:post-multi"]
score: 8.0
evidence: 持续指令调优的稀疏自适应专家扩展
tldr: 针对持续指令调优中平衡可塑性与稳定性的难题，本文提出按需增长框架GoD-MoE，通过稀疏自适应专家模块扩展实现参数共享与按需增长，避免数据重放，高效适应新任务而不遗忘旧知识。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: 现有持续指令调优方法难以平衡可塑性与稳定性，或引发隐私问题与参数膨胀。
method: 提出GoD-MoE框架，采用结构共享策略，仅在必要时扩展专家模块。
result: 在持续指令调优基准上以更少参数取得更好性能。
conclusion: 稀疏自适应专家扩展可有效实现持续指令调优。
---

## Abstract
Continual instruction tuning aims to incrementally adapt large language models to new tasks without forgetting previously acquired knowledge. Existing approaches often struggle to balance plasticity and stability. Replay-based methods retrain on historical data, which raises privacy concerns. Architecture-based methods allocate task-specific components, resulting in significant parameter growth. To address this, we consider a structure-sharing strategy that enables parameter reuse across similar tasks and expands only when necessary, avoiding any data replay. Specifically, we introduce Grow-on-Demand (GoD-MoE), a parameter-efficient framework that is based on sparse and adaptive expert module expansion for continual instruction tuning. GoD-MoE inserts multiple LoRA-based experts into attention layers and dynamically activates a small subset of experts for each task. To avoid redundant parameter growth, we develop an Expert Demand Detector that determines whether new experts are added, facilitating adaptive structural sharing and minimizing parameter overhead. We conduct comprehensive experiments on the TRACE benchmark, demonstrating that GoD-MoE achieves state-of-the-art performance. Furthermore, it effectively mitigates catastrophic forgetting and even outperforms several advanced replay-based baselines.

---

## 论文详细总结（自动生成）

# Grow-on-Demand: 持续指令调优的稀疏自适应专家扩展 —— 论文详细总结

## 1. 核心问题与整体含义（研究动机与背景）

持续指令调优（Continual Instruction Tuning）旨在让大型语言模型（LLMs）在不遗忘旧知识的前提下，增量地适应新任务。然而现有方法难以平衡可塑性与稳定性：
- **重放方法**（如LoRA-RE）需要存储历史数据并重训练，引发隐私问题，实际场景中往往不可行。
- **架构方法**（如为每个任务分配独立隔离的模块）会导致参数随任务数量线性增长，训练效率降低。
- **标准LoRA** 在连续调优中遭受严重灾难性遗忘（图1a验证）。

作者通过CKA相似性分析发现，不同任务（如NumGLUE-ds vs. NumGLUE-cm）之间可能存在高度相似性（图1b），从而启发：**利用任务间共享结构，仅在必要时扩展专家模块，可以避免重放并控制参数增长**。

## 2. 方法论：核心思想、关键技术细节

### 2.1 核心思想：按需增长混合专家（GoD-MoE）
- 在注意力层的Q和V权重中插入多个基于LoRA的专家模块，每个输入仅动态激活少量专家（top-2路由）。
- 训练完每个任务后，冻结最活跃的top-2专家以保留旧知识。
- 新任务到达时，使用**轻量级专家需求检测器**（Expert Demand Detector）判断当前专家集是否足够，仅当现有专家无法充分捕捉新任务特征时才扩展新专家。
- 专家初始化采用现有专家平均参数加高斯噪声，门控权重扩展也基于均值加噪声。

### 2.2 关键技术细节
- **稀疏专家路由**：每层前向为 \( h = W_0x + \sum_{i \in Top2(x)} G_i(x) B_i A_i x \)，门控权重 \( G(x) = \text{Softmax}(Top2(xW_g)) \)。
- **冻结策略**：每个任务后，冻结该层激活频率最高的两个专家；后续任务最多每层允许增加一个冻结专家，以平衡可塑性与稳定性。
- **专家需求检测器**：
  1. 对当前任务随机采样1%训练数据，执行前向与反向传播，得到冻结专家和可训练专家的激活概率分布，拼接为向量 \( P \in \mathbb{R}^N \)。
  2. 定义三种原型模式：
     - 高匹配（主要依赖冻结专家，不添加新专家）
     - 部分匹配（需要部分新专家，添加1个）
     - 低匹配（主要依赖未使用专家，添加2个）
  3. 使用蒙特卡洛Dropout进行M次随机前向，得到 \( P_m \in \mathbb{R}^{N \times M} \)，计算与三种原型的内积，得到均值与方差，用UCB准则（\( \mu_i - \lambda \sigma_i \)）选择最终模式（\(\lambda=1\)）。
- **推理时专家选择**：存储每个任务的最终层表示均值作为参考向量，测试时通过余弦相似度自动匹配最相似任务的路由策略，无需测试任务ID。

### 2.3 无数据重放
全程不依赖历史数据回放，仅使用当前任务1%数据做检测，保护隐私。

## 3. 实验设计

### 3.1 数据集与基准
- **TRACE benchmark**（Wang et al. 2023b）：包含8个多样任务，按顺序：C-STANCE（立场检测）、FOMC（货币政策）、MeetingBank（会议摘要）、Py150（代码完成）、ScienceQA（科学问答）、NumGLUE-cm（数学推理）、NumGLUE-ds（数学推理）、20Minuten（德语）。每个任务5000训练样本。
- **通用LLM评测**：MMLU、GSM、BBH、BoolQ、PIQA，评估持续学习后模型通用能力。
- **评估指标**：Last i（每任务最终准确率）、Avg（平均准确率）、BWT（后向迁移，衡量遗忘程度）。

### 3.2 对比方法
- **基础参考**：Few-shot（6-shot上下文学习，冻结模型）、Multi-task（所有任务联合训练，视为上界）。
- **传统持续学习方法**：EWC（正则化）、L2P（可视化提示）、PP（渐进提示）。
- **先进持续指令调优方法**：O-LoRA（正交子空间）、I-LoRA（重放）、PMoE（渐进混合专家+重放）、HiDe-LLaVA（层次解耦）。
- **直接调优方法**：Full-FT（全参数微调）、LoRA、LoRA-RE（1%数据重放）、MoE-LoRA（多专家但不自适应）。

### 3.3 实现细节
- 骨干模型：LLaMA2-7B。
- 超参数：batch size=128，学习率3e-4，LoRA秩8，缩放因子16，每个任务训练5个epoch，初始专家数4，每任务后冻结top-2。检测器λ=1，M次蒙特卡洛前向（文中未明确M值，但实现代码中可能有）。
- 运行环境：NVIDIA RTX A6000（48GB内存）。

## 4. 资源与算力

文中明确提到：所有实验在NVIDIA RTX A6000 GPU（48GB内存）上进行。未说明具体GPU数量、总训练时长或功耗。仅提及单卡可运行，但多任务序列需要一定时间（每个任务5 epoch，8个任务，具体时间未给出）。总体算力水平属于常见单卡实验室配置。

## 5. 实验数量与充分性

论文进行了多组实验，覆盖以下方面：
- **主实验**（表1）：在TRACE上对比9种基线（不含Multi-task共14种方法），报告Last、Avg、BWT三种指标，充分展示了各方法性能。
- **通用能力评测**（表2）：在5个标准基准上比较，验证持续学习后模型通用能力未严重下降。
- **知识保持与知识获取分析**（图3、图4）：对比LoRA、MoE-LoRA和GoD-MoE在训练过程中对前序任务和当前任务的表现，可视化遗忘曲线。
- **专家重用与扩展分析**（图5）：展示每个任务后的专家数变化及相似度分数，证明早期增加专家后后期可复用。
- **可视化**（图6）：专家选择频率热力图，显示任务间共享模式。
- **效率对比**（表3）：与总是添加专家的变体（AAE）比较性能与参数量，证明稀疏扩展节省35.3%参数且性能几乎无损。
- **任务顺序鲁棒性**（表4）：在三种不同任务顺序下Avg和BWT稳定性验证。

**充分性评价**：实验设计全面，覆盖主流对比方法、消融、可视化、鲁棒性测试。但缺少对更大模型（如7B以上）或更多任务的扩展实验，也未提供显著性检验。主观上充分且公平，因为对比方法均采用相同骨干和统一设置。

## 6. 主要结论与发现

1. GoD-MoE在TRACE基准上达到最佳平均性能（Avg=55.7），BWT=-3.6，显著优于除PMoE（变种有重放）之外的所有非重放基线，甚至优于多个带重放的基线（如I-LoRA、HiDe-LLaVA）。
2. 无需数据重放即可有效缓解灾难性遗忘，且专家按需扩展机制使参数增长率远低于线性（最终模型仅冻结少量专家）。
3. 专家共享策略有效：相似任务（如NumGLUE-cm和ds）激活几乎相同的专家，不同任务（如ScienceQA vs 20Minuten）激活完全不同专家，表明学习到了有意义的任务相关专家表征。
4. 稀疏自适应扩展与总是添加专家的变体性能接近，但节省35.3%参数，证明检测器有效。
5. 对不同任务顺序鲁棒，性能稳定。

## 7. 优点

- **创新性**：首次在持续指令调优中引入按需专家扩展的检测机制，避免了传统方法中固定专家数或总是添加的低效。
- **实用性**：完全无数据重放，保护隐私；参数效率高，仅使用LoRA专家模块，适合资源受限场景。
- **可解释性**：通过CKA分析和专家激活可视化，揭示了专家与任务之间的语义关联，提供了理解模型行为的窗口。
- **实验严谨**：在标准化基准上对比多个前沿方法，并进行了消融、鲁棒性、效率等多维度分析。

## 8. 不足与局限

- **检测器设计依赖原型模式**：三种原型模式是手动构造的（高匹配/部分匹配/低匹配），可能无法覆盖所有复杂情形；UCB的λ超参数固定为1，无灵敏度分析。
- **采样率影响**：检测器仅使用1%数据，虽然轻量，但可能对小样本或噪声敏感；文中未分析不同采样率的影响。
- **模型规模限制**：仅测试了LLaMA2-7B，未在更大模型（如13B、70B）或不同架构（如Mistral、Qwen）上验证通用性。
- **任务顺序实验**：虽做了3种顺序，但未说明顺序选择策略，且结果仅用Avg和BWT简要报告，缺乏细粒度任务级对比。
- **缺失统计显著性**：未报告多次跑的平均值和标准差，性能对比可能受单次结果影响。
- **应用限制**：需要每个任务有小量数据（1%）做检测，若任务级数据极度稀疏（如仅有几十个样本）可能失效；门控和路由计算增加前向开销，但在可控范围。

（完）
