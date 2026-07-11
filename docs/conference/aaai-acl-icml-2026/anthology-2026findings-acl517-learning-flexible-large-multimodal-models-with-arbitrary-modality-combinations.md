---
title: Learning Flexible Large Multimodal Models with Arbitrary Modality Combinations
title_zh: 学习具有任意模态组合的灵活大型多模态模型
authors: "Xinyu Zhao, Kangqi Ni, Jie Peng, Ang Li, Tianlong Chen"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.517.pdf"
tags: ["query:post-multi"]
score: 8.0
evidence: 处理任意模态组合的灵活多模态大语言模型
tldr: 扩展MLLM到多种模态面临配对数据稀缺和计算开销大的挑战。本文提出通过生成缺失模态的表示来处理任意模态组合，避免了全配对数据需求，同时通过共享参数减少模型更新量。在多种模态缺失设置下保持了良好的跨模态理解性能，提升了多模态学习的灵活性。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.517/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 803, \"height\": 541, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.517/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1649, \"height\": 657, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.517/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1638, \"height\": 360, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.517/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1386, \"height\": 1083, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.517/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1653, \"height\": 346, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.517/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1329, \"height\": 301, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.517/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 813, \"height\": 555, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.517/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 738, \"height\": 317, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.517/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 661, \"height\": 328, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.517/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 815, \"height\": 322, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.517/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 382, \"height\": 488, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.517/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1500, \"height\": 807, \"label\": \"Table\"}]"
motivation: 现有MLLM难以高效扩展至多种新模态，受限于全配对数据和高计算成本。
method: 通过生成缺失模态的表示实现任意模态组合输入，并采用参数共享减少更新量。
result: 在多种模态缺失场景下，模型仍保持较强的跨模态理解能力。
conclusion: 生成式缺失模态处理是一种经济有效的多模态扩展策略。
---

## Abstract
Multimodal Large Language Models (MLLMs) show strong potential for cross-modal understanding by integrating powerful language models with multimodal encoders. However, extending MLLMs to handle a diverse range of modalities introduces two critical and intertwined challenges: (1) the reliance on fully paired multimodal data, often scarce or costly to acquire across all modalities, and (2) the computational inefficiency from processing numerous modality tokens and requiring substantial model updates for each new modality. To address these challenges, we enable MLLMs to handle missing modalities by generating representations for absent inputs. Furthermore, recognizing that an increasing number of modalities leads to linearly scaling token counts and that lengthy generated sequences can hinder performance, we employ a dual-stage compression mechanism. It first reduces the number of tokens per modality and then condenses information from multiple modalities into a single, compact token sequence. This culminates in Flex-M 3 , a novel MLLM framework designed for flexible and efficient learning across arbitrary combinations of modalities. Experiments across diverse multimodal benchmarks and backbones demonstrate that Flex-M 3 robustly handles varied modality inputs and scales efficiently. Notably, Flex-M outperforms its counterpart trained on only full-modality data, with consistent improvements of 2.29%, 3.15%, 11.01% on multimodal reasoning tasks NExT-QA, MUSIC-AVQA, SQA3D . Moreover, Flex-M 3 demonstrates superior robustness during inference, even when a high proportion of modalities are missing from the input samples, showcasing its capacity for complex, data-scarce multimodal applications.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：现有的多模态大语言模型（MLLMs）在处理多种模态时面临两个关键且相互交织的挑战：(1) 对全配对多模态数据的依赖，这类数据往往稀缺或采集成本高昂；(2) 处理大量模态token的计算低效性，以及每引入一种新模态就需要大幅更新模型参数。
- **研究动机**：现实场景中，模态可用性往往是异构且不完整的（如传感器故障、采集成本差异等），而现有MLLM通常要求训练和推理时所有指定模态同时存在，这严重限制了其灵活性和实用性。
- **整体含义**：本文提出“灵活多模态学习”（flexible multimodal learning）概念，旨在使MLLM能够处理任意模态组合的输入样本，其中每个样本可能呈现不同的、甚至不完整的模态组合。

## 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：通过生成缺失模态的表示来恢复信息，并采用两阶段压缩机制避免token爆炸，实现任意模态组合下的高效学习。
- **关键技术细节**：
  1. **缺失模态生成模块**（Missing Modality Generator）：
     - 利用始终可用的锚定模态（文本和视频）作为条件，为每个可能缺失的额外模态生成表示。
     - 包含：一个全局可学习的生成提示（generative prompt）P、模态特定的映射网络（MLP）、以及一个最终生成网络Gₘ′。
     - 生成过程：将文本嵌入Hₜ和视频嵌入Hᵥ通过专用MLP投影，与生成提示P拼接，再由生成MLP映射为Nq个模态token。
     - 训练时使用重建损失（MSE）监督生成质量。
  2. **两阶段压缩机制**：
     - **单模态压缩**（Per-modal Compression）：对每个模态（包括生成的）使用一组可学习查询通过交叉注意力压缩为紧凑表示（Nq=32）。
     - **跨模态压缩**（Cross-modal Compression）：将所有压缩后的模态token拼接，再通过一个压缩模块融合为固定长度的表示，确保无论输入多少模态，最终输入LLM的token数量恒定。
  3. **整体训练目标**：语言建模损失 + λ × 重建损失（λ=0.001）。

## 3. 实验设计

- **数据集与Benchmark**：
  - NExT-QA：视频问答，含5440个视频约52K问题，评估因果、时序、描述性推理。
  - MUSIC-AVQA：音频-视频问答，约9K视频45K问答对，评估音频、视觉、音视频推理。
  - SQA3D：3D场景问答，基于ScanNet 650个场景约33K问题，评估空间语义、常识等。
- **额外模态提取**：从视频中提取光流、深度图、表面法向量作为辅助模态（使用ZoeDepth、Unimatch、NLL-AngMF等工具）。对于MUSIC-AVQA还使用音频编码器（BEATs）；SQA3D使用3D点云（按3D-LLM方法）。
- **模型骨干**：BLIP-2（冻结编码器和LLM，仅更新压缩器和生成器，使用LoRA）和 LLaVA（微调所有组件除编码器外）。
- **对比方法**：
  - Essential Modalities Only：仅用文本和视频，全数据训练。
  - Full Modalities with Incomplete Data：标准MLLM在完整模态数据子集上训练（每种模态组合仅1/2ᴹ数据）。
  - Learnable Padding（Padding）：用可学习的[PAD] token代表缺失模态。
  - Flex-MoE Bank（附录A.4）：使用全局可学习token bank。
  - 随机基线（Random）：余弦相似度对比。
- **评估设置**：在测试集上报告准确率，包括不同模态组合、不同问题类型。

## 4. 资源与算力

- **未明确说明具体GPU型号、数量及训练时长**。论文附录A.2提供了训练超参数（batch size、学习率、梯度累积步数等），例如BLIP-2在NExT-QA上使用batch size 8~16，学习率1e-4，训练10 epoch；LLaVA使用batch size 2，学习率2e-5，训练2 epoch。但并未提及使用的GPU具体型号（如A100、V100）和数量，也未给出总训练时长。
- **计算开销**：附录A.1表5显示，Flex-M³的额外参数量和GFLOPs非常小（例如BLIP-2从2.47K GFLOPs增加到2.60K；LLaVA保持在11.35K），说明生成和压缩模块是轻量级的。

## 5. 实验数量与充分性

- **实验数量**：相当充分，包括：
  - 主实验：在3个数据集上，分别以BLIP-2和LLaVA为骨干，测试不同模态组合（V；V,F；V,F,D；V,F,D,N等）的性能。
  - 消融实验：生成损失权重（λ）、生成token数量（Nq）、各组件贡献（生成、单模态压缩、跨模态压缩）。
  - 鲁棒性实验：测试推理时随机缺失不同比例模态（缺失率MR从10%到70%）。
  - 生成质量评估：计算生成嵌入与真实嵌入的余弦相似度，并与Padding、随机基线对比。
  - 锚定模态分析：测试不同锚定组合（有无视频）的影响。
  - 与Flex-MoE Bank的对比（附录A.4）。
- **充分性与公平性**：实验设计较为全面，对比了多个基线，涵盖不同骨干和模态组合。控制变量（如不同缺失处理机制）设计合理。但未提供统计显著性检验（如p值），也未在更多骨干（如Gemini）上验证。此外，仅使用3个数据集，覆盖视频、音频、3D场景，但未涉及其他模态（如热成像、表格式数据）。

## 6. 论文的主要结论与发现

- **Flex-M³显著优于所有基线**：在NExT-QA上，Flex-M³（BLIP-2）在V,F,D,N设置下平均准确率74.82%，高于Padding（74.22%）和Full w/ Inc. Data（72.30%）。在LLaVA骨干上提升更显著（+10.83%）。
- **泛化到非视觉模态**：在MUSIC-AVQA上提升11%，在SQA3D上提升3.15%，证明方法适用于音频、3D点云等。
- **推理阶段鲁棒性强**：当缺失比例高达70%时，Flex-M³性能保持稳定甚至略有提升，而Padding大幅下降。
- **生成质量高**：生成嵌入与真实嵌入余弦相似度平均达0.89（NExT-QA）、0.63（MUSIC-AVQA）、0.80（SQA3D），证实生成模块产生语义有效的表示。
- **参数量与计算开销极小**：生成和压缩模块仅增加不到1%的参数量（BLIP-2）或极少的GFLOPs。

## 7. 优点：方法或实验设计上的亮点

- **创新性**：首次提出针对MLLM的灵活多模态学习框架，同时解决缺失模态建模和token爆炸问题，具有实用价值。
- **高效性**：两阶段压缩确保无论输入多少模态，最终token数固定，显著降低计算成本；生成模块仅依赖文本和视频两个锚定，无需全配对数据。
- **通用性**：可集成到不同MLLM骨干（BLIP-2、LLaVA），且生成和压缩模块即插即用，不改变预训练权重。
- **鲁棒性验证充分**：在多种缺失比例下测试，证明了实际场景中处理不完整数据的能力。
- **消融实验深入**：分别评估生成模块、压缩模块、损失权重、token数量等超参数的影响，提供了设计选择的依据。

## 8. 不足与局限

- **锚定模态依赖**：至少需要文本和视频两个始终可用的锚定来生成缺失模态。若所有信息模态同时缺失或剩余模态极弱，方法无效。
- **额外组件与超参数**：虽然轻量，但仍引入了生成模块和压缩模块，需要调优（如λ、Nq），增加工程复杂度。
- **实验覆盖有限**：仅在三种视频相关数据集上验证，未涉及图像、语音、生物标志物、表格等其他模态；骨干仅用了BLIP-2和LLaVA，未在Gemini、Qwen-VL等流行模型上测试。
- **缺乏统计显著性检验**：报告的是单一准确率数值，未提供多次重复实验的方差或置信区间。
- **模态提取依赖外部工具**：光流、深度等辅助模态由第三方模型（ZoeDepth等）提取，这些工具的质量可能影响最终性能，但论文未分析该影响。
- **训练假设**：假设缺失模态在训练时随机模拟，但真实数据缺失模式可能有偏，未讨论这种分布偏移的影响。

（完）
