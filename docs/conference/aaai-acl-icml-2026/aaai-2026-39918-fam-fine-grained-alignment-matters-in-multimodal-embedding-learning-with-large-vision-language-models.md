---
title: "FAM: Fine-Grained Alignment Matters in Multimodal Embedding Learning with Large Vision-Language Models"
title_zh: "FAM: 在多模态嵌入学习中利用大型视觉语言模型实现细粒度对齐至关重要"
authors: "Tianhang Xiang, Yirui Li, Lizhao Liu, Hongyan Zhi, Chuanshen Chen, Qing Du, Mingkui Tan"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/39918/43879"
tags: ["query:post-multi"]
score: 8.0
evidence: 基于大型视觉语言模型的细粒度多模态对齐
tldr: FAM针对直接使用大型视觉语言模型（LVLM）进行多模态嵌入学习时存在的视觉表示不足和对齐粗糙问题，提出细粒度对齐方法，显著提升检索等下游任务性能。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: 直接适配LVLM到嵌入模型存在视觉表示不足和粗粒度对齐问题。
method: 提出细粒度对齐方法，增强视觉表示并改进跨模态对齐。
result: 在视觉-文本检索等任务上超越了基于CLIP和直接LVLM的方法。
conclusion: 细粒度对齐是提升LVLM嵌入模型性能的关键。
---

## Abstract
Learning multimodal representation is a fundamental task that supports a wide range of applications such as visual-text retrieval. While pioneering approaches e.g., CLIP paves the way by learning separated encoders for different modalities, they struggle to model complex interactions between modalities, resulting in inferior vision and language representation. Recently, researchers have begun to leverage powerful Large Vision-Language Models (LVLMs) for unimodal or multimodal encoding, showing substantial improvement over separated encoder methods. However, we find that directly adapting LVLMs to embedding models suffers from insufficient visual representation and coarse multimodal alignment. To address these issues, we propose a simple yet effective Fine-grained Alignment Matters (FAM) method to achieve fine-grained vision-language embedding learning with LVLMs. First, to close the gap between the pure generation and multimodal embedding using LVLMs, we propose Multi-granularity Aligned Contrastive (MAC) to explicitly learn and align fine-grained modality representations at multiple granularity levels using image-text pairs. Second, to mitigate the insufficiency of visual representation during adapting LVLMs to downstream embedding tasks, we propose a Vision Embedding Inversion Training (VEIN) strategy to encourage the extracted embeddings to preserve fine-grained visual features. Extensive experiments demonstrate the effectiveness of our method, which achieves superior performance on various downstream multimodal datasets.

---

## 论文详细总结（自动生成）

# 论文总结：FAM：细粒度对齐在多模态嵌入学习中至关重要

## 1. 核心问题与整体含义（研究动机与背景）

- **研究动机**：多模态表示学习（如图文检索）是重要基础任务。早期方法（如CLIP）采用分离编码器，难以建模模态间复杂交互；近期研究利用大型视觉语言模型（LVLM）进行统一编码，性能显著提升。
- **关键问题**：作者发现直接将生成式LVLM适配到嵌入模型存在两大缺陷：
  - **视觉表示不足**：LVLM偏向语言模态，对图像局部细节表征弱。
  - **粗粒度模态对齐**：仅在高语义层面进行实例级对齐，缺乏细粒度跨模态对应。
- **研究目标**：提出FAM（Fine-grained Alignment Matters）方法，通过多粒度对齐和视觉增强训练，改善LVLM嵌入学习中的视觉表示与模态对齐。

## 2. 方法论：核心思想、关键技术细节

- **整体范式**：采用“先对齐后适配”的两阶段训练。
  - **阶段一：多粒度对齐（Multi-granularity Aligned Contrastive, MAC）**
    - 使用图像-文本对数据（LLAVA-595K），设计三种对比损失：
      - **粗粒度（Coarse）**：实例级嵌入对比（InfoNCE损失）。
      - **粗到细（Coarse-to-Fine）**：图像嵌入与文本token特征、文本嵌入与图像patch特征的双向对比。
      - **细粒度（Fine）**：图像patch与文本token的平均相似度对比。
    - 总损失：\(L_{\text{align}} = L_c + L_{c2f} + L_f\)。
  - **阶段二：视觉增强适配（Visual-enhanced Adaptation）**
    - 在MMEB数据集上继续训练，任务损失\(L_{\text{task}}\)为标准对比损失。
    - **视觉嵌入反转训练（Vision Embedding Inversion, VEIN）**：
      - 在LVLM的视觉中心层随机遮蔽部分视觉token，用嵌入向量引导解码器重建被遮蔽的视觉特征。
      - 添加重建损失\(L_{\text{rec}}\)（余弦相似度），鼓励嵌入保留细粒度视觉信息。
      - VEIN仅在适配阶段使用，推理时不增加额外开销。
- **技术细节**：
  - 使用LoRA（秩=8）高效微调，混合精度bfloat16。
  - 对齐阶段图像分辨率672×672，批大小512；适配阶段336×336，批大小256。
  - VEIN插入位置：通过注意力分析将层分为文本中心层和视觉中心层，VEIN仅应用于视觉中心层（如Qwen2-VL-2B用最后3层，7B和Phi-3.5-V用最后1层）。

## 3. 实验设计

- **数据集与基准**：
  - 对齐阶段：LLAVA-595K（BLIP-2精炼字幕）。
  - 适配阶段：MMEB（Massive Multimodal Embedding Benchmark），包含20个域内数据集（分类、VQA、检索、视觉定位）和16个域外数据集，共36个。
- **对比方法**：
  - 双编码器模型（零样本和微调）：CLIP、BLIP2、SigLIP、OpenCLIP、UniIR、MagicLens。
  - LVLM基模型：E5-V（LLaVA-NeXT-8B）、VLM2Vec（作者复现版本，使用Qwen2-VL 2B/7B、Phi-3.5-V）。
- **评价指标**：各元任务上的Precision@1，以及域内/域外/总体平均分数。

## 4. 资源与算力

- **文中提及**：所有实验在NVIDIA A100 GPU（80GB）上运行。未明确说明使用的GPU数量、小时数或总计算量。
- **备注**：基于LoRA高效微调，对算力需求相对可控，但未提供具体训练时间。

## 5. 实验数量与充分性

- **实验组数**：丰富且系统。
  - 主表（Table 1）对比了14种方法（含不同骨干），3个骨干下FAM均优于VLM2Vec。
  - 消融实验：
    - MAC和VEIN的独立与联合消融（Table 2）。
    - 训练策略消融（增加同等数据量对比，Table 3）。
    - 不同粒度损失逐步添加的效果（Table 4）。
    - VEIN掩码比例影响（Fig. 4）。
    - VEIN插入位置影响（Table 5）。
  - 定性示例（Fig. 5）展示检索和定位效果。
- **充分性与公平性**：
  - 消融设计合理，分离了数据和策略的影响。
  - 复现VLM2Vec时采用低分辨率（336×336）公平比较。
  - 实验覆盖多个骨干（2B/7B）和多种下游任务。
  - 不足：未进行跨数据集泛化分析（如视频检索），也未在更高分辨率下验证。

## 6. 主要结论与发现

- **主要结论**：直接适配LVLM存在视觉表示不足和粗粒度对齐问题；FAM通过多粒度对比对齐和视觉嵌入反转训练有效缓解，显著提升性能。
- **量化结果**：
  - Qwen2-VL-2B骨干：总体平均分数从55.0提升至57.3（+2.3）。
  - Qwen2-VL-7B骨干：从60.5提升至61.9（+1.4）。
  - Phi-3.5-V骨干：从57.5提升至58.7（+1.2）。
  - 主要增益来自检索和视觉定位任务，验证了细粒度视觉表示改善。
- **消融发现**：
  - MAC和VEIN各自贡献增益，联合使用最佳。
  - VEIN掩码比例在0.3左右最优，过高有害；插入视觉中心层比全层插入更有效。

## 7. 优点

- **问题洞察明确**：首次系统识别LVLM适配嵌入时的视觉表征不足与对齐粗糙问题，并通过定量分析（Fig. 1）和注意力分析（Fig. 3）加以证实。
- **方法简洁有效**：MAC仅需额外图像-文本对（不增加任务数据量），VEIN在训练中增强视觉信息且无推理开销。
- **实验严谨**：消融实验排除数据量干扰，复现基线保证公平，多骨干验证泛化性。
- **实用性**：基于LoRA高效微调，适合资源有限场景。

## 8. 不足与局限

- **数据集依赖**：对齐阶段仅使用LLAVA-595K，未探索更大规模或更高质量的对齐数据影响。
- **实验覆盖有限**：未在视频检索、图文生成等更广泛任务上验证；未测试更高分辨率（如672×672）下的适配效果。
- **计算资源未透明**：未报告训练时间、GPU数量等，不利于复现和比较效率。
- **理论深度欠缺**：对视觉中心层选取的动机是基于经验观察，缺乏严格理论分析。
- **潜在偏差风险**：MMEB基准可能偏向特定场景，FAM在其他领域（如医学、遥感）的泛化性未知。

（完）
