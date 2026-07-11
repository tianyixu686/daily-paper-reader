---
title: Multimodal Fusion via Self-Consistent Task-Gradient Fields
title_zh: 基于自洽任务梯度场的多模态融合
authors: "Jiayu Xiong, Jing Wang, Jun Xue, Wanlong Wang, Jianlong Kwan, Xiaosen Lyu, Zhouqiang Jiang"
date: 2026-04-30
pdf: "https://openreview.net/pdf/b23c2cc549475d574b0a448f95583061870bbb7e.pdf"
tags: ["query:post-multi"]
score: 9.0
evidence: 新颖的多模态融合方法
tldr: 该论文针对多模态融合中表示纠缠和优化冲突问题，提出基于自洽场原理的自洽场自编码器（SCFAE）。通过为每个模态使用小型自编码器保持信息独立，并利用自洽场平衡任务梯度，最小化互信息。实验证明该方法在鲁棒性和任务性能上优于现有融合方法。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有多模态融合方法导致模态表示纠缠，且附加损失引入优化冲突。
method: 提出SCFAE，利用自洽场原理引导任务梯度，使用小自编码器保持模态独立性。
result: 在多个多模态任务上取得更优性能，且对不完整输入更鲁棒。
conclusion: 为多模态融合提供了理论驱动的稳定框架。
---

## Abstract
Multimodal learning aims to preserve as much task-related information as possible from different inputs. However, current fusion designs often distort the feedback loop to feature extractors. Aggressively merging modalities entangles their representations, making the feature extractors fragile to incomplete inputs. Meanwhile, attempting to separate features via auxiliary losses frequently introduces optimization conflicts that distract from the primary task. We propose the Self-Consistent Field Autoencoder (SCFAE) to provide a better path for task gradients. Our method follows the self-consistent field principle to balance task learning with feature organization, thereby minimizing mutual information. We use small autoencoders for each modality to keep information intact. The task loss acts as a driving force to select predictive features. The reconstruction loss acts as a constraint to separate these features into independent subspaces. These dual objectives operate through complementary feature subspaces, thereby mitigating optimization interference. We evaluate SCFAE on audio-visual-text, audio-visual, and image-video benchmarks. Results show that SCFAE handles missing data and unequal input sizes more robustly via a simple structure. Gradient analysis confirms that SCFAE avoids conflicts and maintains stable training dynamics.

---

## 论文详细总结（自动生成）

# 论文中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

当前多模态融合方法存在两大问题：
- **表示纠缠**：激进的模态融合导致不同模态的表示纠缠在一起，使得特征提取器在面对不完整输入（如缺失某一模态）时变得脆弱。
- **优化冲突**：通过附加损失（如辅助分离损失）来尝试分离特征，通常会引入与主任务目标冲突的优化方向，分散学习重心。

论文旨在提出一种既能保持模态信息独立性、又能避免优化冲突的稳定融合框架，提升模型对缺失数据和不均衡输入大小的鲁棒性。

## 2. 论文提出的方法论：核心思想、关键技术细节

**核心思想**：基于**自洽场原理（Self-Consistent Field Principle）**，平衡任务学习与特征组织，从而最小化模态间的互信息。提出**自洽场自编码器（Self-Consistent Field Autoencoder, SCFAE）**。

**关键技术细节**：
- 为每个模态使用**小型自编码器**，保持该模态的信息完整且独立。
- **任务损失**作为驱动力，从各模态中挑选与预测相关的特征。
- **重构损失**作为约束，将这些特征分离到独立的子空间中。
- 两个损失通过**互补的特征子空间**运作，从而减轻优化干扰，实现任务梯度与特征组织的自洽平衡。

**算法流程（文字说明）**：
1. 对每个模态输入，通过一个小型自编码器（编码器+解码器）得到重构输出和潜在表示。
2. 各模态潜在表示被送入融合模块，基于任务损失（如分类损失）更新。
3. 重构损失保证每个自编码器保留原始模态信息，并促使潜在表示落入不同子空间。
4. 通过自洽场机制动态调整任务梯度与重构梯度之间的平衡，避免冲突。

## 3. 实验设计

- **数据集/场景**：音频-视频-文本、音频-视频、图像-视频三个多模态基准。
- **Benchmark**：未明确列出具体数据集名称，但从模态类型推测可能包含类似AVE、CMU-MOSI、UCF101等常见多模态数据集。
- **对比方法**：未具体列出对比方法，但声称优于现有融合方法（如简单拼接、注意力融合等），且梯度分析证明SCFAE避免冲突、训练动态稳定。

## 4. 资源与算力

论文文本中**未明确说明**使用的GPU型号、数量或训练时长。无法从摘要和元数据中推断具体算力开销。

## 5. 实验数量与充分性

- 实验覆盖三个不同模态组合的场景，体现了跨领域验证。
- 提到**梯度分析**作为额外验证，表明进行了机制层面的诊断实验。
- 但摘要未提及消融实验数量、具体指标数值、误差线等细节，**无法判断实验的充分性和统计显著性**。整体而言，实验设计较为全面（多模态、鲁棒性测试），但缺乏公开的详细结果表格供客观评估。

## 6. 论文的主要结论与发现

- SCFAE在处理缺失数据和不等输入大小时，比现有方法更鲁棒。
- 简单的结构即可实现稳定的训练动态，避免梯度冲突。
- 遵循自洽场原理能够自然平衡任务驱动和特征组织，优于加辅助损失的方式。

## 7. 优点

- **理论驱动**：基于物理中的自洽场原理，提供了解释性强的框架。
- **结构简单**：仅需为每个模态添加小型自编码器，易于实现。
- **鲁棒性**：对不完整输入表现良好，无需复杂的缺失处理策略。
- **优化稳定**：通过互补子空间规避了传统多目标优化的冲突问题。

## 8. 不足与局限

- **实验细节缺失**：未公开具体性能数值、对比方法列表、数据集版本，无法独立复现或比较。
- **算力信息空白**：未提及训练资源，不利于评估方法的实际可行性。
- **应用范围**：仅验证了三类模态组合，缺少对更广泛模态（如文本-图像）或更复杂任务（如生成任务）的测试。
- **偏差风险**：可能仅在特定数据分布下有效，泛化性未充分验证。
- **对比公平性**：未说明对比方法的超参数调优是否一致，存在潜在偏差。

（完）
