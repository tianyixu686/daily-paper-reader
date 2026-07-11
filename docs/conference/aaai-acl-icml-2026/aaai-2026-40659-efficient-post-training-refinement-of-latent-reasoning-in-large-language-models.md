---
title: Efficient Post-Training Refinement of Latent Reasoning in Large Language Models
title_zh: 大语言模型潜在推理的高效后训练细化
authors: "Xinyuan Wang, Dongjie Wang, Wangyang Ying, Haoyue Bai, Nanxu Gong, Sixun Dong, Kunpeng Liu, Yanjie Fu"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/40659/44620"
tags: ["query:post-multi"]
score: 9.0
evidence: 大语言模型后训练细化潜在推理
tldr: 针对大语言模型潜在推理后训练中推理嵌入更新困难的问题，提出轻量级后训练框架，通过两种新策略优化潜在推理轨迹，在不增加显式推理步骤情况下提升推理准确性，实验验证其有效性。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: 潜在推理无需显式步骤但后训练阶段难以有效更新推理嵌入。
method: 提出轻量级后训练框架，包含两种策略优化潜在推理轨迹。
result: 提升模型在推理任务上的准确率，且计算开销小。
conclusion: 后训练可有效增强潜在推理能力。
---

## Abstract
Reasoning is a key component of language understanding in Large Language Models. While Chain-of-Thought prompting enhances performance via explicit intermediate steps, it suffers from sufficient token overhead and a fixed reasoning trajectory, preventing step-wise refinement. Recent advances in latent reasoning address these limitations by refining internal reasoning processes directly in the model’s latent space, without producing explicit outputs. However, a key challenge remains: how to effectively update reasoning embeddings during post-training to guide the model toward more accurate solutions. To overcome this challenge, we propose a lightweight post-training framework that refines latent reasoning trajectories using two novel strategies: (1) Contrastive reasoning feedback, which compares reasoning embeddings against strong and weak baselines to infer effective update directions via embedding enhancement; (2) Residual embedding refinement, which stabilizes updates by progressively integrating current and historical gradients, enabling fast yet controlled convergence. Extensive experiments and case studies are conducted on five reasoning benchmarks to demonstrate the effectiveness of the proposed framework. Notably, a +5% accuracy gain on MathQA without additional training.

---

## 论文详细总结（自动生成）

# 大语言模型潜在推理的高效后训练细化 —— 论文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究动机**：大语言模型（LLM）的推理能力是核心，但现有方法如 Chain-of-Thought（CoT）虽提升了性能，却存在显式推理步骤带来的高 token 开销和推理轨迹固定无法逐步修正的问题。近期潜在推理（Latent Reasoning，如 Coconut）直接在模型隐空间进行推理，避免了显式 token 生成，但面临两个关键挑战：推理嵌入缺乏明确的更新方向指导，以及递归嵌入更新不稳定，影响鲁棒性和准确性。
- **核心问题**：如何在**后训练阶段**有效且高效地更新推理嵌入，引导模型走向更准确的解。
- **整体含义**：提出一个轻量级、无需训练的后训练框架，通过对比反馈和残差细化两种策略，在隐空间中优化推理轨迹，提升推理性能且不增加额外训练成本。

## 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：借鉴 RLHF 中的相对比较思想和动量优化思想，在推理的隐空间中进行 post-training 的细化，无需修改模型参数或架构。
- **关键技术细节**：
  - **对比推理反馈搜索（Contrastive Reasoning Feedback Search）**：在每一推理步，将当前隐状态分别输入一个“弱模型”和一个“强模型”（均为 CoT 训练过程中的中间 checkpoint，相对强弱，且都比最终模型弱），得到两个输出嵌入。通过对比损失（MSE 差）计算梯度，指导当前嵌入向强模型方向更新、远离弱模型方向。更新公式：$h_t^{updated} = h_t + \eta \cdot \nabla_{h_t}[ \text{MSE}(h_t^{good}, h_t) - \text{MSE}(h_t^{bad}, h_t) ]$。该过程仅通过前向传播和嵌入级梯度计算，无需参数更新。
  - **残差嵌入细化（Residual Embedding Refinement）**：为避免多步递归更新中的语义漂移，融合当前步输出与上一步隐状态：$h_t = \alpha \cdot h_{t-1} + (1-\alpha) \cdot f(h_{t-1})$，其中 $\alpha$ 为固定记忆率（超参数）。该机制保留历史信息，稳定轨迹。
  - **整体流程**：在 Coconut 的每一推理步后，先进行残差混合，再进行对比搜索，两者均只涉及前向计算，无需训练。

## 3. 实验设计：数据集、基准、对比方法

- **数据集**：5 个推理基准，涵盖数学、常识、多跳推理：
  - GSM8K（数学）、MathQA（数学）、AQUA-RAT（数学/符号）、StrategyQA（常识）、ProsQA（结构化逻辑推理）。
- **基准（Baseline）**：
  - **No-CoT**：直接生成答案，无中间步骤。
  - **Chain-of-Thought (CoT)**：标准显式推理链。
  - **Coconut**：纯潜在推理，无搜索和细化。
  - **Ours**：提出的框架（对比搜索 + 残差细化）。
- **对比方法**：主要对比上述三种 baseline，并进行了消融实验（仅残差、仅对比搜索、两者组合）、训练 vs 推理模式对比、不同模型规模对比等。

## 4. 资源与算力

- **文中明确说明**：
  - 主要实验使用 **GPT-2 base (117M)** 进行。另使用 **Qwen-2.5 1.5B** 和 **LLaMA-3.2 3B** 验证泛化性。
  - **训练耗时**：GPT-2 约 18.95 分钟，Qwen 约 95.80 分钟（LoRA），LLaMA 约 78.38 分钟（LoRA）。
  - **训练显存**：约 45.6 GB（GPT-2），其余使用 LoRA 约 45.3-45.7 GB。
  - **推理显存**：所有模型推理在 24 GB 以内。
  - **模型参数数量**：GPT-2 117M、Qwen 1.5B、LLaMA 3B。
  - **未说明 GPU 型号**，但推断为常见服务器 GPU（如 A100/RTX 4090 等）。

## 5. 实验数量与充分性

- **实验数量**：
  - 总体性能对比（Q1）：5 个数据集，4 种方法。
  - 训练vs推理对比（Q2）：1 个数据集（ProsQA），4 种设置。
  - 消融实验（Q3）：1 个数据集（MathQA），4 个变体。
  - 案例研究（Q4）：1 个具体实例。
  - 超参数敏感性（Q5）：2 个数据集，2 个参数（记忆率、搜索步长）。
  - 跨模型泛化（Q6）：3 个不同架构/规模模型，1 个数据集。
  - Token 效率对比：2 个数据集，2 种方法。
- **充分性评价**：实验覆盖了不同任务类型（数学、常识、逻辑）、不同模型规模、不同组件贡献、超参数影响以及资源消耗分析，设计较为全面。但各实验仅报告了 3 个随机种子的平均准确率，未提供方差或显著性检验；消融实验仅在 MathQA 上进行，未在所有数据集验证。总体而言，实验较充分，但统计严谨性可进一步加强。

## 6. 论文的主要结论与发现

- **主要结论**：
  - 提出的后训练细化框架在 5 个基准上均优于纯潜在推理（Coconut），尤其 MathQA 提升 +5.10%，ProsQA 提升 +3.67%，AQUA 提升 +2.76%。
  - **训练-free**：仅在推理时应用，相比继续训练（需 54+ 分钟、39 GB 显存），推理时应用更高效（24 秒、31 GB 显存），且性能更好（+4.47% vs +1.63%）。
  - 对比搜索和残差细化均重要：单独使用残差提升 +4.63%，单独对比搜索提升 +4.03%，组合提升 +5.10%。
  - 不同任务对超参数敏感度不同：数学任务依赖高记忆率，常识任务依赖适度搜索步长。
  - 方法可跨模型泛化（GPT-2, Qwen, LLaMA），且 token 使用减少超过 92%。

## 7. 优点：方法或实验设计上的亮点

- **方法创新**：首次将对比学习和残差连接引入潜在推理的后训练阶段，无需训练即可动态调整推理轨迹，既轻量又有效。
- **训练-free 设计**：完全基于前向传播，无反向传播或参数更新，易于部署在资源受限或冻结模型场景。
- **高效性**：推理时仅需少量额外计算（前向 + 嵌入梯度），无显式 token 生成， token 开销大幅降低。
- **可解释性**：通过案例研究展示了嵌入更新如何导向正确预测。
- **实验覆盖全面**：从性能、消融、超参数、跨模型、资源开销等多个维度评估，且对比了训练 vs 推理两种部署方式，论证清晰。

## 8. 不足与局限

- **实验局限**：
  - 所有实验基于较小模型（最大 3B），未验证在更大模型（如 7B/13B/70B）上的效果。
  - 消融实验仅在一个数据集（MathQA）上进行，未在所有数据集验证组件的普适性。
  - 仅报告平均准确率，未提供标准差或显著性检验，统计可靠性不足。
  - 对比的“强/弱模型”来自 CoT 训练过程的中间 checkpoint，其普适性依赖于 checkpoint 选择，未系统研究不同选择的影响。
- **方法局限**：
  - 在需要精确符号计算的数学任务（如 GSM8K）上表现不如 CoT，说明纯潜在推理仍难以处理长链算术。
  - 对比搜索需要两个辅助模型（强/弱），增加了额外存储和推理时的计算开销（尽管较小）。
  - 记忆率 $\alpha$ 和搜索步长 $\eta$ 为固定超参数，未实现自适应调整，对任务敏感。
  - 未讨论方法在开放域生成或对话等更广泛 NLP 任务中的适用性。
- **潜在偏差风险**：强/弱模型的相对定义可能引入偏差，若两个模型差距过大或过小，对比方向可能不准确。

（完）
