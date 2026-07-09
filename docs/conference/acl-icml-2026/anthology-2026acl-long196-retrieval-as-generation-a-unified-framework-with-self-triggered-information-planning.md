---
title: "Retrieval as Generation: A Unified Framework with Self-Triggered Information Planning"
title_zh: 检索即生成：具有自触发信息规划的统一框架
authors: "Bo Li, Mingda Wang, Gexiang Fang, Shikun Zhang, Wei Ye"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.acl-long.196.pdf"
tags: ["query:mr"]
score: 6.0
evidence: 通用RAG架构，可扩展到多模态场景
tldr: 传统RAG将检索视为外部干预，导致协调复杂。GRIP提出“检索即生成”范式，将检索控制内嵌到解码过程的token级别，通过控制token发射实现何时检索、如何重写查询和何时终止的自主决策。该框架无需额外控制器，实现端到端规划。尽管目前为文本设计，其自触发信息规划机制可直接迁移到多模态检索增强生成中，为构建统一多模态RAG架构奠定基础。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.196/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1444, \"height\": 835, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.196/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 810, \"height\": 362, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.196/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 644, \"height\": 355, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.196/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 807, \"height\": 427, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.196/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 808, \"height\": 458, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.196/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 797, \"height\": 717, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.196/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 807, \"height\": 635, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.196/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 802, \"height\": 318, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.196/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 806, \"height\": 653, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.196/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 802, \"height\": 733, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.196/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 807, \"height\": 702, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.196/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 643, \"height\": 515, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026.acl-long.196/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1628, \"height\": 834, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.196/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1690, \"height\": 925, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.196/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 805, \"height\": 260, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.196/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 790, \"height\": 253, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.196/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 824, \"height\": 329, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.196/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 802, \"height\": 310, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.196/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 751, \"height\": 373, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.196/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 734, \"height\": 211, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.196/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 804, \"height\": 206, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.196/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 757, \"height\": 312, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.196/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 802, \"height\": 423, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.196/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 775, \"height\": 291, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.196/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 762, \"height\": 275, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.196/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 753, \"height\": 243, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.196/table-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1439, \"height\": 371, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026.acl-long.196/table-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1647, \"height\": 626, \"label\": \"Table\"}]"
motivation: 现有RAG将检索作为外部干预，缺乏端到端协调，需要更内聚的检索--生成融合方式。
method: 提出GRIP框架，在token级别控制检索行为，通过自触发信息规划实现检索与生成的统一。
result: 实验表明GRIP在多个RAG基准上取得优异性能。
conclusion: GRIP证明了将检索内嵌到生成过程中的可行性，为RAG架构提供了新范式。
---

## Abstract
We revisit retrieval-augmented generation (RAG) by embedding retrieval control directly into generation. Instead of treating retrieval as an external intervention, we express retrieval decisions within token-level decoding, enabling end-to-end coordination without additional controllers or classifiers. Under the paradigm of Retrieval as Generation, we propose GRIP ( G eneration-guided R etrieval with I nformation P lanning), a unified framework in which the model regulates retrieval behavior through control-token emission. Central to GRIP is Self-Triggered Information Planning , which allows the model to decide when to retrieve, how to reformulate queries, and when to terminate, all within a single autoregressive trajectory. This design tightly couples retrieval and reasoning and supports dynamic multi-step inference with on-the-fly evidence integration. To supervise these behaviors, we construct a structured training set covering answerable, partially answerable, and multi-hop queries, each aligned with specific token patterns. Experiments on five QA benchmarks show that GRIP surpasses strong RAG baselines and is competitive with GPT-4o while using substantially fewer parameters. Code and resources are provided in the supplementary materials.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机与背景）

- **核心问题**：传统检索增强生成（RAG）将检索视为独立的外部干预步骤，通常采用“一次性检索+固定上下文生成”模式，无法适应逐步推理过程中动态涌现的信息需求，也难以在生成过程中精细控制检索时机、查询重写和终止决策。这种分离导致端到端协调困难、错误归因不透明。
- **整体含义**：论文提出“检索即生成”（Retrieval as Generation）新范式，将检索控制内嵌到语言模型的token级解码过程中，使得检索行为与生成行为在同一个自回归轨迹中统一协调，无需额外控制器或分类器，从而更紧密地耦合检索与推理，实现动态、可控的多步证据整合。

## 2. 方法论

### 2.1 核心思想

- **Retrieval as Generation**：不将检索器内化到LLM中，而是将检索控制动作（触发检索、查询重写、终止决策）作为生成轨迹中的显式控制令牌，由模型自主发射。
- **自触发信息规划（Self-Triggered Information Planning）**：模型在解码过程中自行评估信息充分性，通过发射四种控制令牌实现动态检索循环。

### 2.2 关键技术细节

- **控制令牌集**：引入四个特殊令牌：
  - `[RETRIEVE]`：请求外部证据
  - `[INTERMEDIARY]`：输出部分中间状态
  - `[ANSWER]`：开始最终答案
  - `[SOLVED]`：终止生成
- **规划流程**：
  1. 初始决策：模型判断内部知识是否足够 → 若足够，直接发射`[ANSWER]`+答案+`[SOLVED]`；否则发射`[INTERMEDIARY]`+`[RETRIEVE]`并生成新查询。
  2. 检索与查询生成：利用原始或新查询检索，将结果加入上下文后重新评估。
  3. 多步规划：若仍不足，继续发射`[INTERMEDIARY]`→`[RETRIEVE]`，生成更聚焦的后续查询。
  4. 终止：当模型识别到充分信息后，发射`[ANSWER]`+`[SOLVED]`完成。默认最大检索轮次为3（可调整）。

### 2.3 结构化监督与训练

- **四类训练样本**（Type-α/β/γ/θ），对应不同检索行为模式，每个样本带有特定的控制令牌序列（如图2所示）。
- **训练阶段**：
  1. **监督微调（SFT）**：40,000个结构化样本，使用标准自回归交叉熵损失，训练模型学习控制令牌模式。
  2. **强化学习（RL）**：5,000个样本，使用DAPO算法，结合两个奖励信号：
     - 答案保真度奖励（BLEU分数）
     - 控制准确性奖励（正确发射控制令牌得分）
  最终奖励 $R = r_{\text{ans}} + r_{\text{ctrl}}$。

### 2.4 算法流程（文字描述）

- 解码时，模型逐步生成令牌，遇到`[INTERMEDIARY]`后若下一个令牌是`[RETRIEVE]`，则生成新查询 → 检索 → 将结果添加到上下文 → 继续解码。若遇到`[ANSWER]`则生成最终答案并结束。若达到最大检索预算，则强制输出答案。整个过程无需置信度阈值或外部分类器。

## 3. 实验设计

### 3.1 数据集与基准

- **五个QA基准**：HotpotQA（多跳）、PopQA（开放域）、Natural Questions（NQ）、WebQuestions（WebQ）、TriviaQA（阅读理解）。另外在附录中补充了领域数据集BioASQ。
- **评估指标**：Exact Match (EM)、ROUGE（1/2/L平均）、token-level F1；还使用CoverEM进行语义覆盖分析。

### 3.2 对比方法

- **训练-free方法**：Instruct（直接提示）、GPT-3.5 Turbo、GPT-4o、Single RAG、FLARE、DRAGIN、ETC。
- **训练-based方法**：SFT-RAG、Self-RAG、INFO-RAG、RobustRAG、GainRAG、R1-Searcher、RetRobust、InstrucRAG。
- **设置**：统一使用LLaMA3-8B背面（部分变体用Qwen2.5-7B），Wikipedia语料库，BM25检索器（top-3；附录L也测试了DPR和混合检索器），所有开源基线均使用官方代码和检查点复现，三次随机种子平均结果。

### 3.3 实验数量与充分性

- **主实验**：表1报告了5个数据集×3指标（EM、ROUGE、F1）共15个数值，以及平均分，全面对比了10+个基线。
- **消融与分析实验**（共约8组）：检索深度自适应性（表2、3）、检索调用次数分析（表4）、查询生成质量分析（图3）、检索预算控制（表5）、教师替换实验（表6）、通用能力保持（表7、8）、奖励指标消融（表F）、检索器消融（表L）、行为分析（图8）、案例研究（附录H）、失败案例分析（附录I）、潜在可视化（图12）。
- **额外领域实验**：BioASQ（附录B）。
- **不同骨干网络验证**：Qwen2.5-7B和Qwen-3-4B（附录P）。

**充分性评价**：实验非常充分，涵盖了多数据集、多基线、多维度分析、消融、通用能力、领域迁移、骨干通用性、检索器鲁棒性等，对比公平（相同骨干、检索器、语料库和top-k）。但未测试极大规模模型（如7B以上）或长尾检索场景，且默认检索预算固定。

## 4. 资源与算力

- **GPU型号与数量**：8张A800 GPU。
- **训练时长**：
  - SFT阶段：8个epoch，微批次大小每GPU 4，总批次大小32。
  - RL阶段：1个epoch，学习率1×10⁻⁷。
- **论文未明确说明总训练时间（小时）**，也未说明数据处理和推理时间，但提供了超参数细节。
- **备注**：论文提到使用LLaMA3-8B为骨干，该模型可在消费级GPU上微调，但8张A800资源较大。

## 5. 主要结论与发现

1. **性能领先**：GRIP在五个QA基准上平均得分41.0，显著优于所有开源RAG基线，并接近GPT-4o（41.4），而参数量仅为GPT-4o的零头。
2. **检索深度自适应**：GRIP能够根据任务和样本调节检索次数（HotpotQA:1.44，NQ:0.76），显著低于固定检索的基线，且在需要更多检索的困难子集上表现更好。
3. **查询生成质量提升**：GRIP生成的新查询比原始查询检索覆盖率高（图3），说明中间推理有助于生成更聚焦的查询。
4. **预算可扩展**：即使在训练中最多只见过3步检索，增加测试预算到10仍能平稳提升效果，表明学到了何时需要更多证据的原则，而非固定模式。
5. **教师依赖低**：即使将GPT-4o-mini替换为Qwen3-32B等开源教师，性能仍接近（40.3 vs 41.0），说明框架本身而非特定教师是增益主因。
6. **通用能力保持良好**：在MMLU、MBPP和CNN/DailyMail总结任务上下降微弱，说明学习检索控制并未损害模型基础能力。

## 6. 优点

- **概念创新**：将检索决策内置到生成解码中，实现了真正的端到端联合优化，无需外部模块或启发式信号。
- **方法简洁**：仅通过4个控制令牌即可实现复杂检索规划（时机、查询、终止），算法伪代码清晰。
- **训练数据自动构建**：通过模型自身和检索器过滤自动生成四类结构化样本，无需人工标注，且对教师依赖弱。
- **适应性强大**：模型在推理时能自动调节检索深度，且预算可灵活调整，实现准确率与成本的权衡。
- **全面验证**：实验覆盖多数据集、多基线、多指标、消融、通用能力、领域迁移等，分析深入（如PCA可视化、检索分布、案例研究）。

## 7. 不足与局限

- **检索接口固定**：当前使用固定的BM25检索器、top-3、文档切分策略，未探索更自适应的证据预算和上下文结构，可能限制泛化性。
- **最大检索预算为硬编码**：虽然可调整，但未学习动态预算；默认3步可能不足应对极复杂问题。
- **骨干规模有限**：仅在8B模型上实验，未验证在更大模型（如70B）上的行为，虽提出可用于更大模型，但无实际证据。
- **领域单一**：主要只涉及知识问答，未在更开放的任务（如对话、摘要中的事实增强）或低资源语言上验证。
- **RL阶段奖励设计较简单**：使用BLEU和控制令牌精确匹配，可能不适用于生成任务更具表达性的评估。
- **训练资源需求较高**：8×A800 GPU和全参数微调，对于资源受限的团队可能不友好。
- **潜在偏差风险**：训练数据主要来自TriviaQA和NQ，可能存在领域偏差；教师模型（GPT-4o-mini）标注可能引入系统偏差，尽管教师替换实验减轻了部分担忧。

（完）
