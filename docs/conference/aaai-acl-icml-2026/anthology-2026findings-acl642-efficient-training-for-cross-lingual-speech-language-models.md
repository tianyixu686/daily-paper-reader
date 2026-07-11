---
title: Efficient Training for Cross-lingual Speech Language Models
title_zh: 跨语言语音语言模型的高效训练
authors: "Yan Zhou, Qingkai Fang, Yun Hong, Yang Feng"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.642.pdf"
tags: ["query:post-multi"]
score: 7.0
evidence: 语音-文本多模态学习与指令微调
tldr: 构建端到端语音大模型面临数据稀缺和多语言扩展难题。本文提出跨语言语音语言模型CSLM，基于离散语音令牌，通过持续预训练实现跨模态和跨语言对齐，再结合语音文本交错链式模态生成的指令微调细化对齐。该方法在多个语言上提升了语音理解与生成能力，为多模态语音模型训练提供了高效方案。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.642/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 803, \"height\": 287, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.642/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1645, \"height\": 662, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026.findings-acl.642/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 813, \"height\": 352, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.642/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 808, \"height\": 567, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.642/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1654, \"height\": 298, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.642/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1363, \"height\": 379, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.642/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 805, \"height\": 387, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.642/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 807, \"height\": 453, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.642/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 807, \"height\": 460, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.642/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 803, \"height\": 237, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.642/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 803, \"height\": 180, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.642/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 807, \"height\": 474, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026.findings-acl.642/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 806, \"height\": 918, \"label\": \"Table\"}]"
motivation: 端到端语音大模型训练因数据有限和多语言扩展困难而具有挑战性。
method: 提出CSLM，采用离散语音令牌和持续预训练对齐，结合链式模态生成的指令微调。
result: 在多个语言上，CSLM在语音理解和生成任务上取得有效提升。
conclusion: 离散令牌和链式模态生成能高效实现跨语言语音语言模型训练。
---

## Abstract
Currently, large language models (LLMs) predominantly focus on the text modality. To enable more natural human-AI interaction, speech LLMs are emerging, but building effective end-to-end speech LLMs remains challenging due to limited data and the difficulty in expanding to more languages. In this paper, we introduce C ross-lingual S peech L anguage M odel ( CSLM ), an efficient training method for cross-lingual speech LLMs based on discrete speech tokens. We propose a novel alignment strategy that achieves cross-modal and cross-lingual alignment through continual pre-training. By conducting instruction fine-tuning following a speech-text interleaved chain-of-modality generation process, we enhance modal alignment at a finer granularity, thereby improving generation quality and reducing latency. CSLM aligns different modalities and languages simultaneously without the need for massive speech data, thus exhibiting good language scalability. Evaluations on cross-modal tasks, mono-lingual conversational tasks, and cross-lingual conversational tasks demonstrate CSLM’s strong cross-modal alignment capabilities and general task abilities.

---

## 论文详细总结（自动生成）

### 论文中文总结

#### 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究动机**：当前大型语言模型（LLM）主要聚焦于文本模态，而要实现更自然的人机交互，需要发展语音LLM。然而，构建端到端的语音LLM面临两大挑战：一是语音数据相较于文本数据极为稀缺，尤其是对于许多语言；二是扩展至更多语言时，跨语言与跨模态的对齐非常困难。
- **整体含义**：论文旨在提出一种**高效训练方法**，使得语音LLM能够同时实现跨模态（语音↔文本）和跨语言（如中英）的对齐，且无需依赖海量语音数据，从而具备良好的语言可扩展性。

#### 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：基于**离散语音令牌（discrete speech tokens）**，通过两阶段训练——**持续预训练**与**指令微调**——实现跨模态和跨语言对齐。具体采用“文本桥接”策略：同一语言内对齐语音与文本，不同语言间通过文本模态（机器翻译）间接对齐。
- **关键技术细节**：
  - **模型架构**：由三部分组成：
    - **语音分词器**：使用CosyVoice-300M-25Hz（词汇量4096，频率25Hz），将语音波形转为离散令牌，并合并连续重复令牌以提高效率。
    - **语音-文本联合LLM**：将语音令牌词汇与文本LLM（基于Llama-3.1-8B-Instruct）词汇合并，实现联合建模。
    - **语音解码器**：包含时长预测器（卷积模块）、条件流匹配模型和HiFi-GAN声码器，将生成的语音令牌合成波形。
  - **持续预训练**：使用三类数据：
    - **跨模态数据**：ASR（语音→文本）和TTS（文本→语音）数据（英：MLS、GigaSpeech；中：WenetSpeech、WenetSpeech4TTS）。
    - **跨语言数据**：WMT17中英双向翻译数据（长度适中）。
    - **单语言文本指令数据**：Infinity-Instruct（中英文）。
  - **指令微调**：提出**语音-文本交错链式模态生成**方法。利用CTC对齐器将语音与文本在词块级别（chunk size=7）对齐，生成形如 **TQ → TA₁ → SA₁ → TA₂ → SA₂ → ...** 的交错序列。相比传统完整链式（TQ→完整TA→完整SA），此方法：
    - 更细粒度地对齐模态；
    - 允许生成与播放重叠（流式输出），显著降低延迟。
- **公式/算法**：CTC对齐路径通过动态规划求解最优对齐，并据此切分文本块。

#### 3. 实验设计：数据集、benchmark、对比方法

- **数据集**：
  - **持续预训练**：
    - 英文ASR/TTS：MLS English（44.7K小时）、GigaSpeech（10K小时）
    - 中文ASR：WenetSpeech（10K小时）；TTS：WenetSpeech4TTS（12.8K小时）
    - 跨语言：WMT17 zh-en（0.6B文本令牌）
    - 单语言文本：Infinity-Instruct（1.9B文本令牌）
  - **指令微调**：
    - 单语言语音指令：InstructS2S-200K（英）及其中文翻译，用CosyVoice合成语音。
    - 跨语言语音指令：Alpaca英文+中文翻译，双向指令/响应对（104K条）。
    - 额外文本指令与翻译数据用于记忆保留。
- **Benchmark**：
  - **基本任务**：英文ASR（LibriSpeech test-clean）、TTS（LibriSpeech、LibriTTS、VCTK）；中文ASR（AISHELL-1/2/3）、TTS（同数据集）。
  - **对话任务**：
    - 英文：InstructS2S-Eval（199条，源自AlpacaEval）。
    - 中文：BELLE-eval-S2S（250条，源自BELLE评估集）。
    - 跨语言：同上但指示用另一语言回答。
- **对比方法**：
  - 基本任务：Whisper large-v3（ASR），CosyVoice-300M-SFT（TTS），SpeechGPT, AnyGPT, GLM-4-Voice, Moshi（均为离散令牌语音LLM）。其中Moshi和GLM-4-Voice使用大量数据（>7000小时、>10000小时），CSLM仅用77K小时（但文本令牌量可观，实际语音数据量约为他们的1%）。
  - 对话任务：SpeechGPT，GLM-4-Voice。
- **评估指标**：
  - ASR/TTS：词错误率（WER）/字符错误率（CER），通过ASR转录生成语音得到。
  - 对话：GPT-4o评分（内容质量）、UTMOS（语音自然度）、ASR-ER（语音-文本一致性）、脱靶率（语言准确性）。
  - 人评：双盲评分C-MOS（内容）和A-MOS（声学）。

#### 4. 资源与算力

- **GPU**：24块NVIDIA H800 80G GPU。
- **训练框架**：DeepSpeed ZeRO Stage 1。
- **训练时长**：文中未明确说明具体训练时长（如小时数）。仅提及持续预训练1个epoch（batch size 288），指令微调1个epoch（batch size 48）。时长未提供。
- **其他**：时长预测器使用LJSpeech（13.1K条）和中文标准普通话语料（10K条）训练15个epoch。

#### 5. 实验数量与充分性

- **实验组数**：
  - **基本任务**：英文3个TTS数据集+1个ASR数据集，中文3个ASR+3个TTS数据集（共10个测试集）。
  - **对话任务**：单语言英、单语言中、跨语言英→中、跨语言中→英（4个场景）。
  - **消融实验**：
    - 跨模态对齐效能（表示相似性分析，对比SpeechGPT、GLM-4-Voice）。
    - MT数据影响（有/无MT数据）。
    - 链式模态形式（chunk size=4 vs. 完整链式 vs. 无文本问题）。
  - **人评**：对4个方向（En→En, En→Zh, Zh→Zh, Zh→En）评估C-MOS和A-MOS。
- **充分性评估**：
  - 实验较充分：基本任务覆盖英中，对比多种基线（包括数据量大的模型）。
  - 消融实验验证了每个设计组件的必要性（MT数据、交错链式模态、文本问题）。
  - 但未包含更多语言（如日、法、德）的扩展实验，也未与近期其他微型高效方法（如Mini-Omni）对比。
  - 公平性方面：基线模型的数据量差异大，但作者已指出CSLM在更少数据下达到可比性能，对比是合理的。

#### 6. 论文的主要结论与发现

- CSLM在**数据量远小于**GLM-4-Voice、Moshi（仅约1%的语音数据量）的情况下，在ASR/TTS任务上达到**可比的性能**（WER/CER接近）。
- 在单语言和跨语言对话任务中，CSLM表现出**极低的脱靶率**（<1%）、良好的内容质量和语音自然度，优于或接近使用大数据的模型。
- **交错链式模态生成**相比完整链式，平均加速**×2.93**，且内容质量略有提升（更细粒度对齐）。
- **MT数据**对跨语言对话性能至关重要（移除后内容评分下降约0.3-0.5分）。
- **文本问题（TQ）** 在跨语言场景中不可或缺，因为跨语言对齐通过文本模态桥接（与设计一致）。

#### 7. 优点

- **数据高效**：通过精心设计的对齐策略（桥接式、持续预训练），仅需约77K小时语音数据即可获得强性能，远低于同类模型。
- **语言可扩展性**：依赖离散令牌+翻译数据，理论上可轻松加入新语言。
- **创新方法**：提出语音-文本交错链式模态生成，既提升模态对齐细粒度，又通过流式输出降低延迟。
- **全面评估**：自动+人工评测，多个维度（内容、声学、一致性、语言准确率），消融实验完整。

#### 8. 不足与局限

- **语言覆盖有限**：当前仅支持中英，未实验其他语言（如日、法、德），可扩展性仅理论论证。
- **数据规模限制**：受资源和计算限制，未在大规模语料（如100K+小时）上验证CSLM的潜力，可能限制泛化能力。
- **依赖外部模型**：分词器、CTC对齐器、TTS合成均使用预训练模型（CosyVoice、wav2vec2等），误差可能累积。
- **延迟估计简化**：加速比计算基于平均总时间，未考虑实际网络传输和播放缓冲等，实际端到端延迟可能更高。
- **未与最先进的多模态模型（如Qwen-Audio、LLaMA-Omni）对比**，仅对比了同类离散令牌模型。
- **训练时长未公开**，影响可复现性评估。

（完）
