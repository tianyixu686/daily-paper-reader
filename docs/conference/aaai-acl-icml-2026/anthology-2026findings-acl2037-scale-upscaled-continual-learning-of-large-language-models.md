---
title: "SCALE: Upscaled Continual Learning of Large Language Models"
title_zh: SCALE：大语言模型的升级持续学习
authors: "Jin-woo Lee, Junhwa Choi, Bongkyu Hwang, Jinho Choo, Bogun Kim, Jeongseon Yi, Joonseok Lee, DongYoung Jung, Jaeseon Park, Kyoungwon Park, Suk-hoon Jung"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.2037.pdf"
tags: ["query:post-multi"]
score: 7.0
evidence: 持续预训练作为后训练技术
tldr: 大语言模型的持续预训练需要在不遗忘原有能力的前提下扩展知识。本文提出SCALE，一种宽度扩展架构，通过在线性模块中插入轻量扩展并冻结预训练参数，在保持原始功能的同时增加容量。该遵循持久保留和协作适应原则，训练仅扩展组件，实现了高效的增量学习，减少了灾难性遗忘。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.2037/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 631, \"height\": 483, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.2037/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 617, \"height\": 491, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.2037/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1509, \"height\": 915, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.2037/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1227, \"height\": 584, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.2037/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1161, \"height\": 552, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.2037/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 642, \"height\": 474, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.2037/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 590, \"height\": 459, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.2037/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1265, \"height\": 436, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.2037/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1588, \"height\": 606, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.2037/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1647, \"height\": 369, \"label\": \"Table\"}]"
motivation: 持续预训练需要在不损害已有能力的情况下获取新知识。
method: 提出SCALE架构，通过冻结预训练参数并插入轻量宽度扩展模块实现协同适应。
result: 在多个持续学习基准上，SCALE在获取新知识的同时显著减少了遗忘。
conclusion: 宽度扩展的持续学习方法能有效平衡新知识获取与原有能力保持。
---

## Abstract
We revisit continual pre-training for large language models and argue that progress now depends less on scaling parameters than on scaling the right structure. We introduce SCALE, a width upscaling architecture that inserts lightweight expansions into linear modules while freezing all pre-trained parameters, preserving residual and attention topologies and increasing capacity without perturbing the base model’s original functionality. SCALE follows two principles: Persistent Preservation, which maintains the base model’s behavior via preservation-oriented initialization and freezing of the pre-trained weights, and Collaborative Adaptation, which trains only selected expansion components to acquire new knowledge with minimal interference. We instantiate these ideas as SCALE-Preserve (preservation-first), SCALE-Adapt (adaptation-first), and SCALE-Route, an optional routing extension that performs token-level routing between preservation and adaptation heads. On a controlled synthetic biography benchmark, SCALE reduces the severe forgetting seen in depth expansion while still learning new knowledge. In continual pre-training on a Korean corpus, SCALE variants forget less on English evaluations and achieve competitive gains on Korean benchmarks, yielding the best overall stability-plasticity trade-off. We further analyze when preservation holds provably and why combining preservation and adaptation stabilizes optimization relative to standard continual learning.

---

## 论文详细总结（自动生成）

# SCALE：大语言模型的升级持续学习——详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）
- **研究动机**：大语言模型（LLM）的暴力参数缩放时代接近尾声，进一步进步依赖于“缩放正确的结构”而非仅仅是参数或数据。在持续预训练（CPT）中，如何在不破坏已学知识的前提下增加模型容量，是一个关键挑战。
- **核心问题**：现有方法如深度缩放（LLaMA Pro）会扰动原本的表示并触发灾难性遗忘；经典持续学习方法（正则化、回放、参数隔离）虽能改善保留，但通常不增加新容量。
- **整体含义**：提出一种宽度缩放架构SCALE，通过冻结所有预训练参数并在线性模块中插入轻量扩展，在保持原始功能的同时增加自适应容量，从而在稳定性和可塑性之间取得更优平衡。

## 2. 方法论：核心思想、关键技术细节、公式或算法流程
### 核心思想
- **宽度缩放**：在解码器层的每个线性模块（MHA和FFN）中，将原有的矩阵乘法 \(WX\) 扩展为分块矩阵乘法：
  \[
  \begin{bmatrix} W & W_{12} \\ W_{21} & W_{22} \end{bmatrix} \begin{bmatrix} X \\ X_{\text{up}} \end{bmatrix}
  \]
  其中 \(W\) 为原有权重，其余为新增扩展块，\(X_{\text{up}}\) 为输入扩展部分。原始隐藏状态维度不变，扩展部分增加新维度。
- **两个设计原则**：
  - **持久保留（Persistent Preservation）**：将 \(W_{12}\) 零初始化并冻结，确保原始函数 \(WX\) 在训练中完全不变。通过理论证明（定理3.1）保证函数不变性；\(W_{21}\) 和 \(W_{22}\) 可任意初始化（推荐SVD初始化）以促进新任务适应。
  - **协作适应（Collaborative Adaptation）**：仅训练选定的扩展组件（例如仅在较高层或仅在MHA模块中训练 \(W_{12}\)），以最小化对原始知识的干扰。理论分析表明遗忘随保留层数 \(L_{fp}\) 减少而指数增加，且MHA模块的协作比FFN更稳定。

### 三种学习方法
- **SCALE-Preserve**：所有层 \(W_{12}\) 冻结（零初始化），最大化保留，适应能力受限于 \(W_{21},W_{22}\) 的训练。
- **SCALE-Adapt**：所有层 \(W_{12}\) 零初始化但可训练（仅训练新增参数），适应能力强，但遗忘风险略高。
- **SCALE-Route**：在单次前向中并行计算保留路径（Preserve）和适应路径（Adapt）的logits，通过余弦相似度阈值 \(\tau=0.5\) 进行token级路由：若两logits高度一致则使用保留路径，否则使用适应路径。该方法可在一次前向中获得两个logits（因为适应路径可复现保留路径），且理论收敛界优于标准CL（定理4.1）。

## 3. 实验设计
### 数据集/场景
1. **合成传记数据集（Biography Dataset）**：20万条合成个人资料（姓名+6个属性）。预设三个阶段：预训练10万条、微调QA（Task 0，5万条）、应用扩展方法后微调QA（Task 1，2万条未见个体）。监控Task 0的准确率遗忘。
2. **持续预训练（Korean CPT）**：使用FineWeb2的韩语子集（60B token，来自Common Crawl），故意排除英语数据以避免数据回放效应。基模型为LLaMA 3.2-1B，进行一个epoch的CPT。

### 基准方法对比
- FFT（全参数微调）
- LoRA
- Freeze（冻结底部三层+输入嵌入层）
- LLaMA Pro（深度缩放，增加层数）
- SCALE的三个变体

### 评估指标
- 传记：Task 0和Task 1的硬第一个token准确率。
- CPT：英语遗忘困惑度（FineWeb-Edu 30K样本）和韩语学习困惑度（韩语测试集）；英语/韩语下游基准（ARC, HellaSwag, MMLU, TruthfulQA, Winogrande；韩语KoBEST）。

## 4. 资源与算力
- **传记实验**：NVIDIA H100 80GB GPU×1，具体训练时长未说明，但使用了10倍于默认的学习率（5×10⁻⁵）。
- **持续预训练实验**：8×NVIDIA H100 80GB GPU，批量大小512，序列长度8192，训练一个epoch。不同方法分别调整了学习率（SCALE使用1×10⁻³，LLaMA Pro使用2×10⁻⁴，FFT等使用1×10⁻⁵）。
- **注意**：论文未详尽报告每个实验的总训练时长，仅给出关键超参数和所用GPU数量。

## 5. 实验数量与充分性
- **传记实验**：仅对比了FFT、LLaMA Pro和SCALE-Route（图8），未报告SCALE-Preserve和SCALE-Adapt的结果。实验量较少，但聚焦于证明SCALE-Route在防止遗忘上的优势。
- **持续预训练实验**：对比了7种方法（含基线），报告了困惑度曲线（图9）和下游基准表（表1）。此外，对SCALE内部机制进行了多组消融研究：
  - 宽度缩放 vs. 深度缩放的表示遗忘分析（图4）
  - \(W_{21},W_{22}\) 初始化策略比较（图5）
  - \(L_{fp}\)（保留层数）对遗忘-学习权衡的影响（图6）
  - MHA vs. FFN协作的遗忘缩放分析（图7）
- **充分性评价**：实验设计较为系统，消融充分覆盖了原则的关键变量，但下游基准仅测试了韩语（KoBEST三个任务），英语基准使用标准集。整体可控实验（传记+域内CPT）较好地支持了论文主张，但缺少更广泛的域（如其他语言、指令微调场景）的验证。

## 6. 主要结论与发现
1. **宽度缩放优于深度缩放**：在传记任务中，SCALE-Route的Task 0准确率在前4000步保持100%，最终36.9%，而FFT和LLaMA Pro在200步后即骤降至约15%。
2. **持久保留原则有效**：零初始化并冻结 \(W_{12}\) 可完美保持原始函数，由此得到的遗忘困惑度远低于深度缩放。
3. **协作适应原则可控**：上层MHA模块的协作是最佳选择，遗忘与扩展权重的平均范数近似线性相关，且MHA比FFN稳定得多。
4. **SCALE-Route实现最佳权衡**：CPT中SCALE变体在英语遗忘困惑度上低于所有基线，韩语学习困惑度与其他方法（除SCALE-Preserve外）相当，且在下游基准上保持了最高的英语性能（接近原始LLaMA-3.2-1B），韩语性能接近FFT/LoRA。
5. **理论支撑**：定理证实零初始化 \(W_{12}\) 是函数保留的必要条件；遗忘随保留层数减少指数增加；路由方法收敛界优于标准CL。

## 7. 优点
- **方法创新**：宽度缩放架构不改变残差拓扑和注意力结构，插入轻量扩展块，计算开销小；结合持久保留与协作适应，提供可调节的稳定性-可塑性前沿。
- **理论分析与实证结合**：提供了定理证明（函数保留、遗忘界、收敛界）与大量消融实验，设计决策（如SVD初始化、MHA优先）有明确依据。
- **路由机制简洁高效**：通过余弦相似度阈值在单次前向中同时获得保留和适应logits，几乎无额外开销；可自适应选择路径，避免手动调参。
- **强实验结果**：在传记任务中几乎完全避免突发遗忘，在CPT中英语遗忘最小且韩语适应有竞争力，且无需数据回放，隐私友好。

## 8. 不足与局限
- **实验覆盖有限**：仅在合成传记和单一语言（韩语）CPT上验证，未在更多语言、域内混合数据或指令微调场景下测试；下游基准只包含英语和韩语，缺少其他语言或任务的泛化能力评估。
- **参数与计算开销**：宽度缩放增加了隐藏维度和注意力头数，同时路由逻辑带来微小额外计算，但整体相比全微调仍节省参数；不过仍需要设计与调优（如扩展大小、路由阈值），可能增加工程复杂度。
- **安全与伦理风险未评估**：论文未讨论扩展后模型的行为变化（如偏见、毒性、隐私泄漏或意外能力变化），这在实际部署前需要对齐和红队评估。
- **学习率敏感性**：不同方法需单独调学习率（SCALE比LLaMA Pro高5倍），说明其强保留特性可能使新知识学习更慢；此参数敏感性问题可能限制自动化调参。
- **理论假设强度**：收敛分析依赖于凸性、平滑性和路由器固定等假设，实践中可能不严格成立，但提供了有用的直觉。

（完）
