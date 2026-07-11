---
title: "Beyond Fully Random Masking: Attention-Guided Denoising and Optimization for Diffusion Language Models"
title_zh: 超越完全随机掩码：扩散语言模型的注意力引导去噪与优化
authors: "Jia Deng, Junyi Li, Wayne Xin Zhao, Jinpeng Wang, Hongyu Lu, Ji-Rong Wen"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.acl-long.2060.pdf"
tags: ["query:post-multi"]
score: 9.0
evidence: 针对扩散语言模型的后训练方法
tldr: 该论文针对扩散语言模型后训练中随机掩码策略忽略令牌依赖的问题，提出注意力引导的去噪与优化框架AGDO。通过注意力结构决定去噪顺序，并强调关键令牌在推理中的作用。实验证明该方法在多个任务上优于现有随机掩码后训练方法，提升了生成稳定性和推理质量。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.2060/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1612, \"height\": 838, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.2060/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 709, \"height\": 469, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.2060/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 796, \"height\": 406, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.2060/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 803, \"height\": 406, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.2060/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 801, \"height\": 408, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.2060/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 630, \"height\": 471, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.2060/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 793, \"height\": 792, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2060/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 633, \"height\": 189, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2060/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1578, \"height\": 866, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2060/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 796, \"height\": 560, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2060/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 828, \"height\": 604, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2060/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 674, \"height\": 231, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2060/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 721, \"height\": 230, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2060/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 850, \"height\": 327, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2060/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 804, \"height\": 234, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2060/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 688, \"height\": 631, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.2060/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 634, \"height\": 187, \"label\": \"Table\"}]"
motivation: 现有扩散语言模型后训练依赖随机掩码，未利用令牌间依赖关系，导致次优生成。
method: 提出AGDO，利用注意力得分指导去噪顺序，并在优化中突出注意力关键令牌。
result: 在多个文本生成任务上显著优于随机掩码后训练基线。
conclusion: 注意力引导的后训练能更有效地对齐扩散模型的生成过程。
---

## Abstract
Diffusion large language models (dLLMs) offer an efficient alternative to autoregressive models through parallel decoding, yet existing post-training methods largely rely on random masking strategies that overlook intrinsic token dependencies. In this work, we present an empirical analysis of attention in dLLMs and show that tokens attending more strongly to revealed context exhibit greater generation stability and play a critical role in reasoning. Motivated by these findings, we propose AGDO, an attention-guided denoising and optimization framework that aligns both training and optimization with attention-derived dependencies. AGDO determines the denoising order based on attention structure and emphasizes attention-critical tokens during supervised fine-tuning and reinforcement learning. Experiments on mathematical and coding benchmarks demonstrate that AGDO consistently improves reasoning performance, outperforming state-of-the-art post-training methods for dLLMs.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

扩散大语言模型（dLLMs）通过并行解码成为自回归模型的高效替代方案，但现有后训练方法（如监督微调 SFT、强化学习 RL）大多采用**随机掩码**策略来定义训练时的去噪过程。这种策略忽略了令牌之间**内在的注意力依赖关系**，导致训练与推理过程中的去噪轨迹不匹配，限制了模型在复杂推理任务上的性能。本文旨在揭示 dLLMs 中注意力模式的关键特性，并据此设计一种**与注意力结构对齐**的后训练框架，以提升生成稳定性和推理质量。

## 2. 论文提出的方法论：核心思想、关键技术细节

### 2.1 核心思想
- 通过实证发现：dLLMs 的注意力在去噪过程中呈现**稀疏性**和**时间一致性**；那些对已去噪令牌分配更高注意力（即有效注意力得分 \( S \) 高）的令牌，生成概率更稳定。
- 基于此，提出 **AGDO**（Attention-Guided Denoising and Optimization），将去噪顺序和优化目标均与注意力导出的依赖关系对齐。

### 2.2 关键技术细节

1. **注意力引导的去噪顺序（Attention-Guided Denoising Order）**  
   - 在最后一步去噪时执行一次前向传播，获得最后一层的注意力矩阵。  
   - 定义有效注意力得分 \( S_i = \sum_{k \in U} \frac{1}{H} \sum_{h} A_{i,k}^{(L,h)} \)，其中 \( U \) 是已去噪令牌集合。  
   - 每步选择 \( S_i \) 最高的 \( n \) 个令牌进行去噪，递归直到所有令牌被分配步骤。  
   - 算法细节见附录 Algorithm 1。

2. **监督微调（AGDO-SFT）**  
   - 按照上述顺序在训练时仅掩码当前步骤应去噪的令牌，使训练条件与推理轨迹一致。  
   - 定义**影响力得分** \( I_k = \sum_i \frac{1}{H} \sum_h A_{i,k}^{(L,h)} \)，衡量令牌 \( k \) 被其他令牌关注的总量。  
   - 损失函数加权：\( -\mathbb{E}[\frac{1}{|U_t|} \sum_{k \in U_t} (1 + \gamma I_k) \log f_\theta(x_k^0 | x_t)] \)，突出注意力枢纽令牌。

3. **强化学习（AGDO-RL）**  
   - 基于 GRPO 框架，同样使用注意力引导的去噪顺序。  
   - 调整优势函数：\( \hat{A}'_k = \hat{A}_k + \text{sign}(\hat{A}_k) \cdot \delta \cdot I_k \)，强化对影响力高令牌的优化。  
   - 目标函数为标准 GRPO 加上 KL 散度项，公式见论文 Eq. (10)。  
   - 算法细节见附录 Algorithm 2 和 Algorithm 3。

## 3. 实验设计

### 3.1 数据集与场景
- **数学推理**：MATH-500、GSM8K、Minerva（难度递进）。  
- **代码生成**：LiveBench、LiveCodeBench-v2（动态执行评估）。  
- **通用 NLP**（仅验证无退化）：HellaSwag、CommonsenseQA。

### 3.2 基准模型与对比方法
- **基础 dLLMs**：Dream-v0-Instruct-7B（主要）、LLaDA-8B-Instruct（泛化验证）。  
- **SFT 基线**：标准 SFT（随机掩码）、Blockwise SFT（半自回归顺序）。  
- **RL 基线**：Diff-GRPO、Coupled RL、TraceRL；LLaDA 上另对比 d1-LLaDA、wd1、LLaDA-1.5。  
- **自回归 LLM 参考**：Llama3.1-8B-Instruct、Qwen2.5-7B-Instruct（仅作规模参考）。

### 3.3 公平性控制
- 对每个实验重复 8 次取平均精度。  
- 通过数据增广（如对标准 SFT 使用 35 次独立随机掩码）确保各方法平均前向次数近似相等。  
- 推理采用静态解码（温度 0.1，每次解掩一个令牌，最大长度 1024/512）。

## 4. 资源与算力

- **GPU**：8 块 NVIDIA H20。  
- **RL 迭代开销**（以 Dream-v0-Instruct-7B 为例）：  
  - 单次 RL 迭代总时间 ≈ 402 秒，其中注意力分析仅占 12 秒（约 3%）。  
- **训练配置**：  
  - SFT：学习率 1e-6，batch size 128，训练 1 epoch。  
  - RL：每步采样 32 个 prompt，每个 prompt 生成 8 个响应，batch size 512，学习率 1e-6，温度 1.0。  
- **未明确信息**：总训练时长（GPU 小时数）、完整训练步数（仅 RL 图显示约 100 步），因此算力消耗细节不够完整。

## 5. 实验数量与充分性

- 共进行 **10 组以上**实验，涵盖：  
  - 主结果（Table 2，6 个基准 × 多种方法）。  
  - 超参数消融（γ、δ，Figure 4）。  
  - 不同采样配置（预定义长度 512、不同 block size，Table 3）。  
  - 模型泛化（LLaDA，Table 4、Figure 5）。  
  - 组件消融（层选择 Table 5、头聚合 Table 6、顺序 vs 加权 Table 7）。  
  - 内部机制分析（S 分布变化，Figure 6）。  
  - 计算成本（Table 8）。  
  - 通用 NLP 任务（Table 9）。  
- **充分性评价**：实验设计较为全面，覆盖了主流推理任务、多种基线、消融分析，并通过重复实验和训练成本对比保证了公平性。但通用 NLP 任务仅包含两个基准，覆盖尚可；未在更大规模模型（如 70B）或不同架构（如块注意力）上验证。

## 6. 论文的主要结论与发现

- 注意力引导的去噪顺序显著优于随机掩码：单独使用顺序（γ=0）即可在 MATH-500 上提升约 1%。  
- AGDO-SFT 和 AGDO-RL 均持续超越现有 SFT 和 RL 基线，在数学和代码任务上平均提升 2-5%。  
- AGDO 促使模型内化注意力对齐策略：训练后模型的有效注意力得分分布右移，生成更稳定。  
- 额外的注意力分析开销极低（约 3% 的 rollout 时间），具有实际可行性。

## 7. 优点

- **问题导向明确**：从实证注意力分析出发，揭示随机掩码的固有缺陷，提出针对性方案。  
- **方法统一且轻量**：框架同时适用于 SFT 和 RL，仅需一次额外前向传播提取注意力，不显著增加训练负担。  
- **性能提升显著**：在多个 challenging 基准上达到 SOTA，消融实验验证各组件贡献。  
- **泛化性验证**：在 Dream 和 LLaDA 两种架构上均有效，且不损害通用 NLP 能力。  
- **分析深入**：通过 S 分布变化等内部机制分析，论证了方法的内在合理性。

## 8. 不足与局限

- **模型范围有限**：仅测试 7B/8B 规模全注意力 dLLMs，未探索更大模型（如 70B）或块注意力架构（如 Mercury），结论通用性待验证。  
- **通用 NLP 基准不足**：仅用 HellaSwag 和 CommonsenseQA，缺乏更多样化任务（如文本分类、摘要、翻译）的退化测试。  
- **超参数敏感**：δ 过大时性能下降（如 δ=20），需谨慎调参，可能限制实际应用。  
- **注意力分析依赖于最后一层**：虽经消融验证最优，但不同模型的最优层可能不同，需进一步探索自适应选择。  
- **训练时间未完整报告**：缺乏总 GPU 小时数等细节，影响可复现性评估。  
- **未与推理时动态策略（如重掩码优化）结合**：文中仅采用静态采样，而 AGDO 的注意力引导可与推理策略互补，但未讨论。

（完）
