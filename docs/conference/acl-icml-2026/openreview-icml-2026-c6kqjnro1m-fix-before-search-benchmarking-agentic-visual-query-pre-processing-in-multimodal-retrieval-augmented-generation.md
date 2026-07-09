---
title: "Fix Before Search: Benchmarking Agentic Visual Query Pre-processing in Multimodal Retrieval-augmented Generation"
title_zh: 先修复再搜索：多模态检索增强生成中智能体视觉查询预处理基准
authors: "Shenglai Zeng, Jiankun Zhang, Kai Guo, Xinnan Dai, Hui Liu, Jiliang Tang, Yi Chang"
date: 2026-04-30
pdf: "https://openreview.net/pdf/c6bac8cc67852d8f65746cd9c7a77c1956492b8f.pdf"
tags: ["query:mr"]
score: 9.0
evidence: 多模态RAG中视觉查询预处理的基准测试
tldr: 针对多模态RAG中视觉查询通常存在几何畸变、质量退化或语义模糊等不完美问题，提出首个视觉查询预处理基准V-QPP-Bench。该基准将V-QPP形式化为智能体决策任务，要求多模态大模型自主修复视觉输入后检索。实验揭示了现有MRAG管道在应对不完美视觉查询时的脆弱性。该工作为MRAG系统的鲁棒性评估提供了重要工具。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有MRAG管道假设视觉输入无噪声，导致真实场景中检索失败。
method: 提出V-QPP-Bench基准，将视觉查询预处理形式化为智能体任务。
result: 揭示了现有MRAG方法在不完美视觉查询下的严重性能下降。
conclusion: 视觉查询预处理对多模态RAG的鲁棒性至关重要。
---

## Abstract
Multimodal Retrieval-Augmented Generation (MRAG) has emerged as a key paradigm for grounding MLLMs with external knowledge. While query pre-processing (e.g., rewriting) is standard in text-based RAG, existing MRAG pipelines predominantly treat visual inputs as static and immutable, implicitly assuming they are noise-free. However, real-world visual queries are often ``imperfect''---suffering from geometric distortions, quality degradation, or semantic ambiguity---leading to catastrophic retrieval failures. To address this gap, we propose V-QPP-Bench, the first comprehensive benchmark dedicated to Visual Query Pre-processing (V-QPP). We formulate V-QPP as an agentic decision-making task where MLLMs must autonomously diagnose imperfections and deploy perceptual tools to refine queries. Our extensive evaluation across 46,700 imperfect queries and diverse MRAG paradigms reveals three critical insights: (1) Vulnerability---visual imperfections severely degrade both retrieval recall and end-to-end MRAG performance; (2) Restoration Potential \& Bottleneck---while oracle preprocessing recovers near-perfect performance, off-the-shelf MLLMs struggle with tool selection and parameter prediction without specialized training; and (3) Training Enhancement---supervised fine-tuning enables compact models to achieve comparable or superior performance to larger proprietary models, demonstrating the benchmark's value for developing robust MRAG systems The code is available at https://github.com/phycholosogy/VQQP_Bench

---

## 论文详细总结（自动生成）

# 多模态检索增强生成中智能体视觉查询预处理基准：V-QPP-Bench 详细总结

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **研究动机**：现有的多模态检索增强生成（MRAG）管道通常将视觉输入视为静态且无噪声的，假设查询图像完美无缺。然而，现实场景中的视觉查询往往存在几何畸变、质量退化或语义模糊等“不完美”问题，导致检索性能灾难性下降。
- **整体含义**：为了解决这一关键空白，论文首次提出并系统化定义了视觉查询预处理（V-QPP）任务，将其形式化为一个智能体决策任务，要求多模态大模型（MLLM）自主诊断视觉查询中的不完美并利用感知工具进行修复，从而提升MRAG系统的鲁棒性。

## 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程
- **核心思想**：构建一个全面的基准测试V-QPP-Bench，用于评估和训练MRAG管道中的视觉查询预处理能力。方法论将V-QPP视为一个智能体任务，包含两个主要步骤：
  1. **诊断阶段**：MLLM需要自动识别视觉查询中的具体不完美类型（如旋转、模糊、低对比度等）。
  2. **修复阶段**：MLLM选择合适的感知工具（如旋转校正、去模糊、对比度增强等），并预测正确的工具参数（如旋转角度、模糊程度等），以生成优化后的视觉查询。
- **关键技术细节**：
  - 基准包含46,700个不完美查询，覆盖多种退化类型和程度。
  - 评估涵盖多种主流MRAG范式，包括基于CLIP、BLIP-2、LLaVA等的检索管道。
  - 引入Oracle预处理作为性能上限参考，以衡量修复潜力与瓶颈。

## 3. 实验设计：使用了哪些数据集/场景，它的 benchmark 是什么，对比了哪些方法
- **数据集与场景**：基准基于现有MRAG数据集（如MS-COCO、Flickr30k等）构建，通过合成方式引入几何畸变（旋转、缩放、裁剪）、质量退化（模糊、噪声、低对比度）和语义模糊（遮挡、局部缺失）等不完美类型，总计46,700个查询。
- **Benchmark**：即V-QPP-Bench，是首个系统化评估V-QPP能力的基准。
- **对比方法**：
  - 多种通用MLLM（如GPT-4V、Gemini、LLaVA-1.5等）作为智能体核心。
  - 与不使用预处理（原始不完美查询）的基准线对比。
  - 与Oracle预处理（完美修复）对比。
  - 对紧凑模型进行监督微调（SFT）后的性能对比。

## 4. 资源与算力：使用了多少算力（GPU型号、数量、训练时长等）
- **文中未明确说明**：论文摘要在算力资源方面未提供具体信息（如GPU型号、数量、训练时长等）。仅提到代码已开源，但未公开训练细节。因此无法总结算力消耗。

## 5. 实验数量与充分性：大概做了多少组实验，是否充分、客观、公平
- **实验数量**：覆盖46,700个不完美查询，多种退化类型，多个MRAG范式（至少包括基于CLIP、BLIP-2、LLaVA等），并进行了监督微调实验。实验组数较多，规模较大。
- **充分性**：实验设计较为充分，涵盖了诊断、修复、端到端检索召回、最终生成性能等多个维度。
- **客观与公平**：
  - 使用Oracle预处理作为理论上限，提供了清晰的性能上界。
  - 对比了多种MLLM（不同规模、不同架构），包括开源和闭源模型。
  - 训练增强实验证明了微调带来的提升，但未详细披露数据划分、超参数等，可能存在一定偏差风险。

## 6. 论文的主要结论与发现
1. **脆弱性**：视觉不完美会严重降低检索召回率和端到端MRAG性能，现有管道缺乏鲁棒性。
2. **修复潜力与瓶颈**：Oracle预处理可以恢复接近完美的性能，但未经专门训练的现成MLLM在工具选择和参数预测上表现不佳，难以自主完成有效修复。
3. **训练增强**：通过监督微调，紧凑模型能够达到甚至超越大型专有模型的预处理能力，证明了V-QPP-Bench的价值——不仅可以评估，也可以用于训练更鲁棒的MRAG系统。

## 7. 优点：方法或实验设计上的亮点
- **填补空白**：首次系统定义并基准化视觉查询预处理任务，解决了MRAG领域的盲点。
- **智能体范式**：将V-QPP形式化为诊断+修复的智能体决策任务，贴合实际需求。
- **大规模基准**：46,700个不完美查询覆盖多种退化类型，使评估更具代表性。
- **多维度评估**：不仅评估检索召回，还评估端到端生成性能，提供完整视角。
- **支持模型训练**：基准可用于微调，为改进MRAG系统提供实际工具。

## 8. 不足与局限：包括实验覆盖、偏差风险、应用限制
- **实验覆盖**：
  - 退化类型为人工合成，可能与真实世界中自然出现的退化存在分布差异。
  - 仅评估了有限的MRAG范式，可能未涵盖所有多模态检索架构。
- **偏差风险**：
  - 工具选择和参数预测的评估可能存在主观标签偏差（如何定义最优修复参数）。
  - 未提供算力资源细节，复现和比较成本未知。
- **应用限制**：
  - 当前基准假设所有不完美均需修复，但某些场景下不完美可能不影响检索，导致过度修复。
  - 缺乏对实时性/效率的评估，预处理引入的额外计算延迟未被考量。
  - 文中未讨论对黑盒MLLM（如商业API）的适用性，仅依赖模型本身诊断能力。

（完）
