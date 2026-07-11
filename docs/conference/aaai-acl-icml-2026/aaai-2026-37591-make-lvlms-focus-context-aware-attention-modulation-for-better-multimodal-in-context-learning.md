---
title: "Make LVLMs Focus: Context-Aware Attention Modulation for Better Multimodal In-Context Learning"
title_zh: 让LVLM聚焦：用于更好多模态上下文学习的上下文感知注意力调制
authors: "Yanshu Li, Jianjiang Yang, Ziteng Yang, Bozheng Li, Ligong Han, Hongyang He, Zhengtao Yao, Yingjie Victor Chen, Songlin Fei, Dongfang Liu, Ruixiang Tang"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/37591/41553"
tags: ["query:post-multi"]
score: 8.0
evidence: 改进大型视觉语言模型的多模态上下文学习能力
tldr: 该论文分析大型视觉语言模型（LVLM）在上下文学习中的自注意力缺陷，提出上下文感知注意力调制方法。通过识别两种关键注意力弱点并针对性地调整，提升了LVLM对上下文示范的利用效率，无需参数更新即可更稳定地适应新任务。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: LVLM的上下文学习性能不稳定，即使示范匹配也表现不佳，现有方法未触及内部注意力机制。
method: 分析自注意力弱点，提出上下文感知注意力调制，在不更新参数情况下改善注意力分布。
result: 在多个多模态任务上稳定提升上下文学习性能。
conclusion: 揭示了注意力机制对多模态上下文学习的关键影响。
---

## Abstract
Multimodal in-context learning (ICL) is becoming a key capability that allows large vision-language models (LVLMs) to adapt to novel tasks without parameter updates, which expands their usefulness in many real-world applications. However, ICL performance remains unstable even when the in-context demonstrations (ICDs) are well matched, showing that LVLMs still struggle to make full use of the provided context. While existing work mainly focuses on prompt engineering or post-hoc logit calibration, we study the attention mechanisms inside LVLMs to address their inherent limitations. We identify two important weaknesses in their self-attention that hinder effective ICL. To address these weaknesses, we propose Context-Aware Modulated Attention (CAMA), a training-free and plug-and-play method that dynamically adjusts attention logits based on the input in-context sequence. CAMA uses a two-stage modulation process that strengthens attention to semantically important tokens, especially visual ones. Across four LVLMs and seven benchmarks, CAMA consistently outperforms vanilla models and baselines, showing clear effectiveness and generalization. It can also activate the intended benefits of prompt engineering methods and remains robust across different sequence configurations. Therefore, CAMA opens up new directions for improving multimodal reasoning through a deeper understanding of attention dynamics.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）
大型视觉语言模型（LVLM）在多模态上下文学习（ICL）中表现出不稳定性：即使上下文示范（ICD）与查询样本匹配良好，模型仍难以充分利用语境信息。现有方法主要集中于提示工程或后处理逻辑校准，但未触及模型内部的注意力机制。该论文旨在揭示LVLM在多模态ICL中自注意力机制的固有缺陷，并提出一种无训练、即插即用的方法来改善注意力分布，从而提升ICL性能。

## 2. 论文提出的方法论：核心思想、关键技术细节

### 核心思想
提出**上下文感知调制注意力（CAMA）**，通过动态调整模型内部的注意力对数（attention logits），引导模型关注与上下文最相关的令牌（尤其是视觉令牌），无需参数更新。

### 关键技术细节
CAMA采用**两阶段调制**，分别作用于浅层和中层解码器层：

- **阶段I：ICD内部接地（Intra-ICD Grounding）**  
  作用于浅层（第2-3层）。对每个ICD，利用其问答中的锚定令牌（问题首令牌、答案首令牌和答案末令牌）计算各图像令牌的注意力分布，并基于**动态注意力增量**（非负前向增益 \( c_1, c_2 \)）识别与文本语义最匹配的关键图像令牌。然后放大这些令牌的注意力对数，并加入位置衰减因子 \( (n - i + 1)/n \) 以缓解序列位置偏差。

- **阶段II：查询中心路由（Query-Centric Routing）**  
  作用于中层（第7至第19层每隔一层）。先根据查询样本文本向上下文的注意力流强度筛选出**查询中心头**（比例 \( k_{II}=20\% \)），然后计算每个ICD与查询样本的余弦相似度（基于阶段I最终层的联合嵌入），得到查询中心分数 \( w_i \)。在查询中心头中，按该分数放大对应ICD所有令牌的注意力对数，同样施加位置衰减。

- 两层调制均保持所有其他层注意力不变，实现无训练、即插即用。

## 3. 实验设计

### 数据集/场景
- **主要VQA基准**：VQAv2、VizWiz、OK-VQA、GQA、TextVQA、CLEVR子集（来自VL-ICL bench）、MMStar，共7个。
- **额外任务**（跨任务泛化）：图像描述（Flickr30k、MSCOCO）、图像分类（Hateful memes）、视觉故事生成（L-I-VST），共4个。

### 对比方法
- **Vanilla**：原始模型
- **+Inst**：添加指令（“先学习示例，然后回答问题”）
- **CD**（Contrastive Decoding）：用空白图像替换ICD图像校准logits
- **VE**（Visual Enhancement）：手动在ICD图像上画红色框标注相关区域
- **SoFA**（SoFt Attention）：插入双向注意力掩码缓解位置偏差

### 使用的模型
LLaVA-NeXT-7B、Idefics2-8B、InternVL2.5-8B、Qwen2.5VL-7B，共4种LVLM。

### 实验设置
- 每个查询样本从训练集随机检索8个ICD，构成8-shot序列。
- Stage I 作用于第2-3层，Stage II 作用于第7-19层每隔一层。
- 所有实验在NVIDIA H200 GPU上进行。

## 4. 资源与算力
论文中仅提及“所有实验在NVIDIA H200 GPU上运行”，但**未明确说明使用的GPU数量、总训练/推理时长**。由于CAMA是无训练方法，仅需推理时前向传播，算力消耗相对较低，但具体数值未提供。

## 5. 实验数量与充分性
- **主实验**：4个LVLM × 7个VQA基准 × 8种方法（包括CAMA及其组合），共28组对比，报告了准确率。
- **跨任务实验**：4个额外任务 × 5种方法（包括CAMA），共20组结果。
- **消融实验**：在5个VQA基准上对4个LVLM进行平均，测试了：
  - 移除Stage I / Stage II
  - 禁用动态注意力增量
  - 不使用top-\( k \)选择（对全部图像令牌/全部头部调制）
  - 移除位置衰减因子
  - 不同层选择、不同超参数 \( k_I, k_{II} \)
- **其他分析**：不同shot数（2/4/8/16）、不同序列配置策略（随机、CLIP相似度、IQ2IQ、TACO）等，共约10+组子实验。

**充分性评价**：实验覆盖了多样化的模型、任务（VQA + 非VQA）、增强方法对比、消融、超参数敏感性和配置适应性，总体较为充分。但所有实验均固定为8-shot（主实验），未在其他shot数下系统对比所有方法；跨任务泛化实验仅在Idefics2-8B上报告（见表2），未在所有模型上重复。**存在一定的偏差风险**：部分分析仅基于LLaVA-NeXT和Idefics2，且仅对VQAv2进行注意力分析，可能影响结论的泛化性。

## 6. 论文的主要结论与发现
1. **LVLM注意力缺陷**：浅层缺乏图像-文本对齐，中层缺乏查询引导的ICD优先级分配；且位置靠前的ICD缺陷更严重。
2. **CAMA有效性**：在全部28组主实验中CAMA均取得最高准确率，平均提升2.96%；更强的模型获益更大（InternVL2.5提升3.61%，Qwen2.5VL提升3.15%）。
3. **激活提示方法**：CAMA能激活如+Inst、VE等提示工程的潜在收益，使其从微小提升变为显著增益（如CLEVR上提升可达6.67%）。
4. **跨任务泛化**：在图像描述、分类、故事生成任务上同样优于所有基线。
5. **稳健性**：对shot数、序列配置、层选择、超参数变化均保持稳定；位置衰减因子对长序列尤为重要。

## 7. 优点
- **无训练、即插即用**：无需额外数据和参数更新，直接插入推理过程，计算开销低。
- **深入机制**：基于对注意力动态的细致分析（两层次缺陷），设计有针对性的调制，而非简单启发式。
- **广泛适用**：在4种不同架构的LVLM、7个VQA基准及3个非VQA任务上均有效，且能与提示工程方法互补。
- **实验设计全面**：包含主实验、消融、超参数分析、配置适应性、位置偏差等，验证了方法的鲁棒性。
- **提出位置衰减因子**：有效缓解多图像序列中的位置偏差，符合注意力分析结论。

## 8. 不足与局限
- **依赖手工标注**：在注意力分析阶段，需要人工标注ICD图像的边界框以计算 \( s_{\text{align}} \)，存在主观性和成本。
- **跨任务泛化实验不完整**：仅对Idefics2-8B报告了4个额外任务的结果，未在所有模型上验证，削弱了泛化结论的强度。
- **shot数公平性缺失**：主实验固定8-shot，未在其他shot数下比较所有基线（仅CAMA与vanilla比较了2/4/8/16，但未与CD、VE等对比）。
- **超参数选择依赖经验**：\( k_I, k_{II} \) 设定为20%，阶段层选择（2-3, 7-19隔层）虽经鲁棒性验证，但未提供系统搜索过程。
- **算力消耗未量化**：缺乏推理时间或额外计算成本的定量报告，影响实际部署评估。
- **注意力分析仅基于两个模型**：LLaVA-NeXT-7B和Idefics2-8B，可能无法完全代表其他LVLM（如InternVL2.5）的注意力模式。

（完）
