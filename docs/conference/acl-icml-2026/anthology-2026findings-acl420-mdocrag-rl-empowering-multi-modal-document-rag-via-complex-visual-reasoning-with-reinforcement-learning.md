---
title: "MDocRAG-RL: Empowering Multi-Modal Document RAG via Complex Visual Reasoning with Reinforcement Learning"
title_zh: MDocRAG-RL：通过强化学习赋能多模态文档RAG的复杂视觉推理
authors: Zhongyu Wang
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.420.pdf"
tags: ["query:mr"]
score: 9.0
evidence: 多模态文档RAG与视觉推理
tldr: 多模态RAG中，嵌入质量差且图像利用简单。MDocRAG-RL设计预训练和微调任务，压缩视觉文档表示并对齐图文嵌入，通过强化学习优化检索与推理。在多个多模态文档QA数据集上，该方法在复杂视觉推理任务中显著超越现有RAG系统。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.420/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 790, \"height\": 594, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.420/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1647, \"height\": 628, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.420/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1662, \"height\": 588, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.420/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1666, \"height\": 313, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.420/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 759, \"height\": 397, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.420/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 756, \"height\": 266, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.420/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 794, \"height\": 286, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.420/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1646, \"height\": 733, \"label\": \"Table\"}]"
motivation: 现有MLLM在RAG中视觉嵌入不佳且图像处理粗糙，限制了复杂视觉推理能力。
method: 提出MDocRAG-RL，设计压缩视觉表示的预训练任务，并用强化学习联合优化检索和推理。
result: 在多模态文档QA基准上，MDocRAG-RL在视觉推理准确率上取得领先结果。
conclusion: 强化学习能有效提升多模态RAG的视觉表示和推理能力。
---

## Abstract
While Retrieval-Augmented Generation(RAG) enhances multi-modal large language models(MLLMs) by introducing external knowledge, existing RAG systems still face significant limitations when dealing with complex visual reasoning. On one hand, MLLMs, being generative models, produce suboptimal embeddings for retrieval tasks. On the other hand, existing methods naively insert images into context without adequate visual perception, thereby limiting reasoning capabilities. To address these challenges, we propose MDocRAG-RL, a novel RAG framework for complex visual reasoning. We design specialized pre-training and fine-tuning tasks to enable MLLMs to compress visual document representations and align textual and visual embeddings for improved retrieval efficiency. Additionally, we design a visual perception action space for the generator that allows progressive coarse-to-fine information acquisition from visually-rich documents. Furthermore, we develop a reinforcement learning framework to enhance the complex visual reasoning capability of the RAG system. Extensive experiments on multiple challenging benchmarks demonstrate the significant effectiveness of our approach, achieving state-of-the-art performance across various benchmarks.

---

## 论文详细总结（自动生成）

# 论文总结：MDocRAG-RL：通过强化学习赋能多模态文档RAG的复杂视觉推理

## 1. 核心问题与整体含义（研究动机和背景）

- **研究背景**：检索增强生成（RAG）通过引入外部知识，能缓解多模态大语言模型（MLLM）的幻觉问题并处理复杂任务。然而，传统文本RAG无法有效捕捉视觉信息，尽管近期工作引入MLLM构建了视觉RAG系统，但现有方法仍存在三大核心局限：
  - **检索嵌入质量差**：MLLM作为生成式模型，其优化目标（下一词预测）不适用于检索任务，导致嵌入无法准确表示查询语义和视觉信息，检索效果差。
  - **视觉感知不足**：生成器机械地将图像插入上下文，缺乏渐进、精细的视觉感知，关键视觉信息丢失。
  - **复杂推理能力受限**：视觉信息处理不当导致推理token分配不足，模型难以利用图像中的关键特征。
- **整体含义**：本文旨在解决多模态文档RAG在复杂视觉推理中的瓶颈，提出一个集成了专用检索器预训练、视觉感知动作空间和强化学习框架的综合方案。

## 2. 论文提出的方法论

### 核心思想
构建一个多模态RAG框架，包含两个主要组件：
- **检索器**（基于MLLM的双编码器）：通过自监督预训练和监督微调，将完整文档图像压缩为紧凑的token表示，并对齐文本和视觉嵌入，提升检索效率。
- **生成器**（配备视觉感知动作空间的MLLM）：通过迭代的“思考-动作-观察”循环，实现从粗到精的信息获取，并借助强化学习（GRPO）优化交互策略。

### 关键技术细节
#### 2.1 检索器预训练与微调
- **自监督预训练**（图3(a)）：
  - 对比学习：利用OCR提取的文本对，构建图像-文本对，通过对比损失（公式1）使查询嵌入\(e_q\)与正文档嵌入\(e_d^+\)靠近，与负样本远离。
  - 生成式任务：利用特殊的注意力机制，迫使模型将视觉信息压缩到最后一个token（<EOS>），然后基于该嵌入生成文本，损失为负对数似然（公式2）。总损失 \(L_{pre} = L_{contrast} + L_{generate}\)。
- **监督微调**（图3(b)）：使用标注的查询-文档对，继续用对比学习优化，使检索器能适配真实查询场景。

#### 2.2 生成器视觉感知动作空间
- **动作类型**：
  - **search**：从文档库中检索相关图像。
  - **summarization**：生成中间或最终答案。
  - **visual perception**：通过特殊标记 `<region>` 指定边界框坐标 \([x_{min}, y_{min}, x_{max}, y_{max}]\)，对检索到的图像区域进行裁剪、缩放和重新编码，增加该区域视觉token密度。
- **轨迹数据扩增**：使用大型模型（π_LM）生成高层次的推理流程和动作，并用专门的地面模型（π_EM）精确定位边界框，从而构建高质量的SFT训练数据。

#### 2.3 强化学习框架
- **奖励函数**（公式7-12）：由三部分组成：
  - **检索质量奖励**（\(r_{ret}\)）：基于DCG（折损累计增益），鼓励早期检索到相关文档。
  - **动作合规奖励**（\(r_{act}\)）：确保轨迹遵循预定义的思考-动作格式，训练初期使用。
  - **答案质量奖励**（\(r_{ans}\)）：使用奖励模型评估生成答案与真实答案的语义相似性和事实正确性。
  - 最终奖励：\(r_{\phi} = \alpha r_{ret} + \beta r_{ans} + \gamma r_{act}\)。
- **优化算法**：采用GRPO（Group Relative Policy Optimization），对每个查询生成多条轨迹，利用相对性能计算策略梯度，并包含KL散度约束以保持稳定性。

## 3. 实验设计

### 数据集
- **检索器预训练**：DocStruct4M（500k无标注文档图像+OCR文本）。
- **检索器微调**：Open-DocVQA。
- **生成器训练**：基于约70k视觉文档构建的数据集（用于RL训练）。
- **评估基准**：三个挑战性基准：
  - SlideVQA（幻灯片文档QA）
  - ViDoSeek（视觉文档检索QA）
  - MMLongBench（长文档多模态理解，包含表格、图表、布局等）
    - 评价指标：各基准的准确率（Overall，以及各子类别）。

### 对比方法
- **传统方法**：ReAct（推理+行动框架）。
- **视觉文档RAG**：Vanilla RAG、VDocRAG、ViDoRAG。
- **强化学习增强RAG**：Search-R1-VL、VRAG-RL。
- 所有对比均基于两种规模的MLLM：Qwen2.5-VL-3B-Instruct和Qwen2.5-VL-7B-Instruct。

### 实验数量与充分性
- **主实验**（表1）：在3个基准上，针对2种模型大小，共报告3×2=6组对比，每个方法均有数据。MDocRAG-RL在所有设置下均取得最佳或显著优于baselines。
- **消融实验**（表2）：在Qwen2.5-VL-7B-Instruct上进行，逐步验证：
  - 基线（无预训练、无视觉动作、无RAG奖励）→ +检索器预训练 → +视觉动作 → +RAG奖励（完整模型）。
  - 同时包含“Retriever Reward Generator Acc”列，进一步验证各模块的独立和组合效果。
- **额外分析**（图5、图6）：检索性能分析、延迟分析。

**充分性评估**：实验设计较为全面，覆盖多个数据集和模型规模，消融实验清晰验证了各组件贡献。但缺少跨领域泛化实验、大规模多样本测试。

## 4. 资源与算力

- **基础模型**：Phi3V（检索器）、Qwen2.5-VL-3B/7B（生成器）。
- **训练框架**：llama-factory（SFT）、verl（RL）。
- **硬件**：8张H100 GPU。
- **训练细节**：
  - 检索器预训练：1 epoch，LoRA，AdamW，FlashAttention加速。
  - 生成器SFT：全参数微调，余弦学习率调度，warmup比例0.1。
  - GRPO：组大小5，KL损失系数0.01（冷启动时为0）。
- **说明**：文中未明确给出总训练时长或能耗，但提供了框架和配置。

## 5. 主要结论与发现

1. **MDocRAG-RL大幅领先现有方法**：在SlideVQA、ViDoSeek、MMLongBench上，使用7B模型时Overall准确率分别达75.9%、50.3%、66.2%（以Qwen2.5-VL-7B为骨干），超越所有baseline。
2. **各组件的有效性**：
   - 检索器预训练带来3.9个点提升，证明压缩视觉表示和对齐文本/视觉嵌入有助于检索。
   - 视觉感知动作空间提升性能，尤其在结合RAG奖励时效果更显著。
   - RAG特定奖励函数比普通RL奖励（如仅答案奖励）更优，能同时优化检索质量和生成质量。
3. **强化学习学习高效交互策略**：模型学会更早检索相关文档，减少冗余搜索，同时合理使用视觉感知动作进行精细分析。
4. **延迟-准确率权衡**：尽管引入多步推理和视觉动作，但强化学习优化了检索策略，延迟增加有限，准确率大幅提升。

## 6. 优点

- **方法创新**：首次专门为多模态文档RAG设计检索器预训练任务（同时对比+生成），解决了MLLM嵌入不匹配问题。
- **动作空间设计合理**：视觉感知动作（裁剪/缩放）使生成器能动态聚焦信息密集区域，模拟人类读图过程。
- **强化学习奖励函数全面**：结合检索质量、答案质量和动作合规，有利于学习高效的推理路径。
- **实验扎实**：在多个挑战性基准上验证，消融实验系统，且对比了多种先进RAG方法（包括RL增强方法）。
- **模块化框架**：检索器和生成器可独立训练和优化，便于后续扩展。

## 7. 不足与局限

- **延迟开销**：尽管有优化，但相比传统RAG仍有额外延迟（图6所示），在实时性要求高的场景可能受限。
- **动作空间有限**：当前仅支持裁剪、搜索、总结三种动作，相比人类处理复杂文档的多样化操作仍显不足。
- **依赖训练数据**：预训练需要大量文档图像+OCR文本（500k），且RL训练也需要70k文档，数据获取成本较高。
- **跨领域泛化未验证**：仅测试了幻灯片、文档等场景，未涉及自然图像、医疗影像等异质模态。
- **模型规模限制**：实验中最大模型为7B，未探索更大规模（如70B）效果，可能无法反映可扩展性。
- **未严格公平性讨论**：未分析模型对图像噪声、布局变化的鲁棒性。

（完）
