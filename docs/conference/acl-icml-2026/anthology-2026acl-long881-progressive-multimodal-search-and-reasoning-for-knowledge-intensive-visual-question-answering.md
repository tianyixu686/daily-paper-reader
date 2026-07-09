---
title: Progressive Multimodal Search and Reasoning for Knowledge-Intensive Visual Question Answering
title_zh: 面向知识密集型视觉问答的渐进式多模态搜索与推理
authors: "Changin Choi, Wonseok Lee, Jungmin Ko, Wonjong Rhee"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.acl-long.881.pdf"
tags: ["query:mr"]
score: 9.0
evidence: 面向知识密集型VQA的多模态检索增强生成，结合渐进式搜索与推理
tldr: 知识密集型视觉问答需要外部知识，但现有单次检索框架知识获取不足且缺乏纠错机制。PMSR提出渐进式多模态搜索与推理框架，通过双范围查询逐步构建结构化推理轨迹，同时更新历史记录和查询范围。该方法在多个VQA数据集上超越现有多模态RAG方法，特别是在需要多步推理的场景中表现突出。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.881/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1494, \"height\": 557, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.881/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 804, \"height\": 340, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.881/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1378, \"height\": 981, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.881/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1366, \"height\": 976, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.881/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1370, \"height\": 976, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.881/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1299, \"height\": 1031, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.881/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1307, \"height\": 945, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.881/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1265, \"height\": 594, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.881/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 799, \"height\": 580, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.881/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 801, \"height\": 426, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.881/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1647, \"height\": 680, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.881/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 794, \"height\": 308, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.881/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 715, \"height\": 409, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.881/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 807, \"height\": 227, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.881/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 603, \"height\": 250, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.881/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 673, \"height\": 178, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.881/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 805, \"height\": 387, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.881/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 798, \"height\": 334, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.881/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 801, \"height\": 234, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.881/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 778, \"height\": 175, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.881/table-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 633, \"height\": 231, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.881/table-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 794, \"height\": 309, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.881/table-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 484, \"height\": 287, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.881/table-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 796, \"height\": 231, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.881/table-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 797, \"height\": 137, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.881/table-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 798, \"height\": 220, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.881/table-020.webp\", \"caption\": \"\", \"page\": 0, \"index\": 20, \"width\": 798, \"height\": 207, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.881/table-021.webp\", \"caption\": \"\", \"page\": 0, \"index\": 21, \"width\": 797, \"height\": 293, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.881/table-022.webp\", \"caption\": \"\", \"page\": 0, \"index\": 22, \"width\": 798, \"height\": 206, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.881/table-023.webp\", \"caption\": \"\", \"page\": 0, \"index\": 23, \"width\": 797, \"height\": 218, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.881/table-024.webp\", \"caption\": \"\", \"page\": 0, \"index\": 24, \"width\": 620, \"height\": 320, \"label\": \"Table\"}]"
motivation: 现有单次检索框架在知识密集型VQA中知识获取不足，且缺乏推理纠错能力。
method: 提出PMSR，通过双范围查询渐进式构建结构化推理轨迹，同时增强知识获取与合成。
result: 在多个VQA基准上超越现有多模态RAG方法。
conclusion: 渐进式搜索与推理能有效提升多模态RAG在知识密集型任务中的表现。
---

## Abstract
Knowledge-intensive visual question answering (VQA) requires external knowledge beyond image content, demanding precise visual grounding and coherent integration of visual and textual information. Although multimodal retrieval-augmented generation has achieved notable advances by incorporating external knowledge bases, existing approaches largely adopt single-pass frameworks that often fail to acquire sufficient knowledge and lack mechanisms to revise misdirected reasoning. We propose PMSR (Progressive Multimodal Search and Reasoning), a framework that progressively constructs a structured reasoning trajectory to enhance both knowledge acquisition and synthesis. PMSR uses dual-scope queries conditioned on both the latest record and the trajectory to retrieve diverse knowledge from heterogeneous knowledge bases. The retrieved evidence is then synthesized into compact records via compositional reasoning. This design facilitates controlled iterative refinement, which supports more stable reasoning trajectories with reduced error propagation. Extensive experiments across six diverse benchmarks (Encyclopedic-VQA, InfoSeek, MMSearch, LiveVQA, FVQA, and OK-VQA) demonstrate that PMSR consistently improves both retrieval recall and end-to-end answer accuracy.

---

## 论文详细总结（自动生成）

# 面向知识密集型视觉问答的渐进式多模态搜索与推理（PMSR）— 论文详细总结

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：知识密集型视觉问答（VQA）需要结合图像内容与外部知识（如百科、新闻等），现有主流方法采用单次检索-生成（retrieve-then-read）管道，但**初始检索往往不充分**，容易遗漏必要知识或引入干扰信息（文本/图像干扰项），且**缺乏对错误推理的修正机制**，导致误差累积和性能下降。
- **研究背景**：多模态大语言模型（MLLM）虽有进步，但面对需要外部知识的问题仍显不足。多模态检索增强生成（RAG）成为自然解决方案，但单次检索局限性明显。近期智能体（agent）方法通过迭代推理和工具调用改进检索，但**依赖完整交互历史**，早期错误容易在无结构的历史中传播并逐渐漂移。
- **整体含义**：本文旨在通过**渐进式构建结构化推理轨迹**，实现知识获取与合成的可控迭代精炼，减少误差传播，提升知识密集型VQA的检索召回和最终回答准确性。

## 2. 论文提出的方法论：核心思想、关键技术细节
### 核心思想
PMSR 维护一个由**紧凑推理记录**组成的结构化推理轨迹，每轮迭代仅基于**新检索的证据**合成新记录（record-isolated updates），并使用**双范围查询**（dual-scope queries）解耦局部细化与全局反思，支持从异质知识库（文本库+多模态库）中检索互补知识。

### 关键技术细节
1. **初始推理记录生成**  
   - 由 MLLM 根据图像和问题生成视觉相关描述 \(d_0\)，拼接为增强查询 \(q_{\text{init}} = [Q; d_0]\)，检索初始候选集 \(D_0\)，再通过推理算子 \(G_{\text{reason}}\) 合成首条记录 \(r_0\)，启动轨迹 \(\langle r_0 \rangle\)。

2. **双范围查询生成（每轮迭代 \(t\)）**  
   - **记录级查询** \(q_{\text{record}}^{(t)} = [Q; r_{t-1}]\)，聚焦于最新推理状态，用于局部细化检索。  
   - **轨迹级查询** \(q_{\text{trajectory}}^{(t)} = G_{\text{trajectory}}(Q, I, \langle r_0,...,r_{t-1} \rangle)\)，基于全局轨迹分析未覆盖缺口或矛盾，生成上下文敏感的查询。  
   - 查询集 \(Q_t = \{ q_{\text{record}}^{(t)}, q_{\text{trajectory}}^{(t)} \}\)。

3. **异质知识库联合搜索**  
   - **文本知识库（Textual KB）**：约21M Wikipedia段落，使用E5-base-v2 进行文本相似度检索（top-20）。  
   - **多模态知识库（Multimodal KB）**：约2M Wikipedia 图像-文本对，使用**解耦相似度**：  
     \[
     S_{\text{mm}} = \lambda \cdot \text{sim}_{\text{text}}(q_t, t_c) + (1-\lambda) \cdot \text{sim}_{\text{img}}(I, I_c), \quad \lambda=0.5
     \]
     图像编码器用 SigLIP2，文本编码器用 Qwen3-Embedding，检索 top-10 图像-文本对。  
   - 每轮均匀分配检索预算（记录级和轨迹级各一半），聚合为候选集 \(D_t\)。

4. **推理记录生成**  
   - 使用 \(r_t = G_{\text{reason}}(Q, I, D_t)\) 仅从**新检索的 \(D_t\)** 生成记录，不直接依赖先前记录。新记录追加到轨迹 \(\langle r_0,...,r_t \rangle\)。

5. **自适应终止**  
   - 计算**饱和度分数**：\(\delta_{\text{query}}^{(t)} = \max_{q \in Q_t, q' \in Q_j, j<t} \text{sim}_{\text{text}}(q, q')\)，当超过阈值 \(\tau=0.9\) 时停止。  
   - 最终回答由 MLLM 基于原始问答和完整推理轨迹生成。

### 算法流程（文字说明）
1. 输入图像 \(I\) 和问题 \(Q\) → 用 MLLM 生成初始描述，构造增强查询，检索初始候选，生成首条推理记录 \(r_0\)。  
2. 循环（第1轮到自适应终止）：  
   - 根据最新记录和轨迹生成记录级和轨迹级两个查询。  
   - 联合搜索文本 KB 和多模态 KB，获得候选集。  
   - 仅用此候选集合成新推理记录，追加到轨迹。  
   - 用查询相似度判断是否饱和，是则终止。  
3. 最终 MLLM 依据轨迹和原输入生成答案。

## 3. 实验设计：数据集、基准、对比方法
### 使用的数据集（共6个）
- **InfoSeek**（验证集 M2KR 5K 子集，实体检索与准确率）  
- **Encyclopedic-VQA (E-VQA)**（单跳问题测试集）  
- **OK-VQA**（验证集 5K）  
- **FVQA-test**（2K 问题，强调事实推理）  
- **InfoSeek Human**（2K，开放域检索）  
- **MMSearch**（视觉子集 171 题，搜索导向）  
- **LiveVQA**（3,602 题预览集，时间敏感新闻）

### 基准（Benchmarks）
- 检索召回：InfoSeek 和 E-VQA 的 R@5/10/20，OK-VQA 的 PRR@5/10。  
- 准确率：E-VQA 使用 BEM（BERT matching），InfoSeek 使用 Exact Match 或 CEM，其他使用 LLM-as-Judge（GPT-4o）。

### 对比方法
- **单次检索方法**：Wiki-LLaVA、LLM-RA、mR²AG、ReflectiVA、EchoSight、OMGM、ReAuSE、Pre-FLMR、MMKB-RAG、Wiki-PRF 等。  
- **智能体方法**：OmniSearch、MMSearch-R1、WebWatcher、DeepEyesV2。  
- **自己的模型**：使用 Qwen3-VL-4B/8B、Qwen2.5-VL-7B、Gemini-2.5-Flash 作为推理后端，最终答案生成用 LLaVA-MORE-8B（对 InfoSeek 保持一致）。

## 4. 资源与算力
- **未明确说明训练算力**：论文聚焦推理阶段，未提及模型训练使用的 GPU 型号、数量或时长。  
- **推理延迟分析**（附录 P）：  
  - 在单张 RTX 3090 上，每轮迭代顺序执行约 17.20 秒。  
  - 通过并发检索降低至 11.61 秒/轮；使用 H100 GPU 加速 VLM 解码后可降至 4.33 秒/轮。  
  - 自适应终止平均 3.5 轮，端到端约 15.15 秒/样本（H100 下）。  
- **检索器**：使用固定预训练编码器（SigLIP2、E5-base-v2、Qwen3-Embedding），不需要额外训练。

## 5. 实验数量与充分性
- **主实验**：在 3 个知识密集型 VQA 基准（InfoSeek, E-VQA, OK-VQA）上报告检索召回和准确率，在 4 个搜索导向基准（FVQA-test, InfoSeek Human, MMSearch, LiveVQA）上报告准确率，涵盖**6个不同数据集**。  
- **对比方法**：与 10+ 种近期 SOTA 方法对比，包括单次 RAG 和智能体方法，且对智能体方法尽量使用相同骨干（如 Qwen2.5-VL-7B）确保公平。  
- **消融实验**（Section 5）：  
  - 迭代次数影响（1-4 轮，单调递增）  
  - 组件消融（双范围查询、异质知识库、迭代）  
  - 自适应终止 vs. 固定迭代（效率和性能平衡）  
- **分析实验**（Section 6）：  
  - 推理轨迹类型分布（稳定正确、纠正、冲突、持续失败）  
  - 自适应终止后的额外迭代数  
  - 检索器规模缩放、Top-k 敏感性、多模态权重敏感性  
  - 噪声敏感性分析（加入干扰项后准确率下降）  
  - 跨领域测试（HotpotQA，文本多跳 QA）  
- **充分性评价**：实验设计全面，涵盖了不同任务类型、不同评估指标、不同骨干模型，消融和控制实验充分，对比公平（尽量统一检索器、知识库、评估协议）。但缺失与更强智能体（如使用实时网页搜索）在同等条件下的对比（部分方法使用不同工具集）。

## 6. 论文的主要结论与发现
1. **PMSR 在检索召回上显著优于现有方法**：在 InfoSeek 上达到 94.6% 累积召回（8B 模型），较先前最佳（86.4%）提升超过 8 个百分点；在 E-VQA 上达 67.3%，提升 8.6 个百分点。  
2. **端到端答案准确率也大幅提升**：在 E-VQA 上，使用 Gemini-2.5-Flash 可达 59.9% BEM，超过前最好的 51.2%；在搜索导向基准上，使用 Qwen2.5-VL-7B 也全面超过或持平各智能体方法。  
3. **渐进式迭代比单次检索更有效**：即使经过简单的一轮迭代，准确率即可提升 5 个百分点以上；加上双范围查询和异质知识库，性能进一步提升。  
4. **结构化轨迹减少误差传播**：轨迹分析显示，“纠正”型轨迹比例（30.1% 在 E-VQA）高于“冲突”型（17.3%），表明框架更多地从早期错误中恢复。  
5. **自适应终止在不牺牲性能前提下大幅减少迭代次数**（从固定 5 轮降至平均 3.3-3.5 轮）。

## 7. 优点：方法或实验设计上的亮点
- **方法论亮点**：  
  - **记录隔离更新**：每轮记录仅由新检索知识生成，避免过去错误直接污染后续推理，解决了智能体方法中历史误差累积的问题。  
  - **双范围查询**：同时支持局部细化（记录级）和全局反思（轨迹级），使检索更全面且更少冗余。  
  - **异质知识库利用**：联合文本库和多模态库，互补图像和文本知识，提升覆盖度。  
  - **自适应终止**：基于查询饱和度，在保证知识充分的同时提升效率。  
- **实验设计亮点**：  
  - 多维度评估（召回、EM、BEM、CEM、LLM-as-Judge），确保结论稳健。  
  - 在多个搜索导向基准上，使用相同骨干与最先进智能体公平比较。  
  - 控制最终答案生成模型（使用 LLaVA-MORE-8B），避免推理记录生成差异带来的混淆。  
  - 详尽的消融和分析实验，验证每个组件的贡献及轨迹动态。

## 8. 不足与局限
- **计算开销**：尽管自适应终止减少了迭代次数，但每轮仍需多次检索和 MLLM 推理，整体延迟仍高于单次 RAG，在资源受限场景下可能不适用。  
- **依赖检索质量**：性能受限于基础检索器（E5、SigLIP2）的准确度；虽然本文集成 MLLM 检索器（Qwen3-VL-Embedding）后未见明显提升，但更优的检索方案可能进一步提升。  
- **MLLM 能力瓶颈**：较小骨干（如 4B 模型）在视觉定位和组合推理上仍有困难，限制了记录质量；本文仅通过更换更强骨干部分缓解。  
- **实验覆盖局限**：未在实时网页搜索、多轮对话等更动态的场景下验证；跨领域测试（HotpotQA）仅初步展示，缺乏多模态以外的系统评估。  
- **仅评估推理阶段**：未讨论训练过程能耗或微调成本，在实际部署中可能需要考虑模型更新。  
- **偏差与公平性**：未分析模型对不同实体类别、长尾知识或文化偏见的公平性，存在潜在偏差风险。

（完）
