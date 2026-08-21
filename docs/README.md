<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-08-21
- 运行时间：2026-08-21 20:09:42 UTC
- 运行状态：成功
- 本次总论文数：19
- 精读区：7
- 速读区：12

### 今日简报（AI）
今日聚焦LLM量化与视频推理，精读两篇9分论文，并覆盖GPU共享、多语言模型与长上下文压缩等方向。最值得关注的是SchurQuant的层间量化离散优化，以及Beyond Visual CoT的主动视频推理。建议普通读者优先从这两篇精读入手，理解量化效率与视频推理的前沿进展。
- 详情：[/202608/21/README](/202608/21/README)

### 精读区论文标签
1. [SchurQuant: Groupwise Discrete Optimization for Layer-Wise LLM Quantization](/202608/21/2608.15567v1-schurquant-groupwise-discrete-optimization-for-layer-wise-llm-quantization)  
   标签：评分：9.0/10、query:post-multi
   evidence：直接提出大模型权重的训练后量化（PTQ）优化方法，属于典型后训练技术。
2. [Beyond Visual CoT: Internalized Visual Thinking for Proactive Video Reasoning](/202608/21/2608.15869v1-beyond-visual-cot-internalized-visual-thinking-for-proactive-video-reasoning)  
   标签：评分：9.0/10、query:post-multi
   evidence：面向视觉语言模型的视频推理后训练框架，将视觉思考内化至训练阶段
3. [Scaffolding Minds: Optimizing Latent Visual Target Representations for Multimodal Reasoning](/202608/21/2608.19669v1-scaffolding-minds-optimizing-latent-visual-target-representations-for-multimodal-reasoning)  
   标签：评分：9.0/10、query:post-multi
   evidence：面向多模态推理的潜视觉表征SFT与RL训练
4. [SABET-QA: Temporal Knowledge Graph Question Answering](/202608/21/2608.20083v1-sabet-qa-temporal-knowledge-graph-question-answering)  
   标签：评分：9.0/10、query:mr
   evidence：针对时序知识图谱上的多步查询，通过多轮迭代多跳精化进行推理，直接对应多跳推理需求。
5. [Inject, Align, Recover: Staged Post-Training for Retrieval-Free Document Knowledge Internalization](/202608/21/2608.20281v1-inject-align-recover-staged-post-training-for-retrieval-free-document-knowledge-internalization)  
   标签：评分：9.0/10、query:post-multi
   evidence：面向大语言模型的后训练分阶段方案，与后训练技术需求高度契合
6. [MidTool: Mid-training Data Synthesis for Agentic Tool Use](/202608/21/2608.20314v1-midtool-mid-training-data-synthesis-for-agentic-tool-use)  
   标签：评分：9.0/10、query:post-multi
   evidence：面向大模型中期后训练的数据合成，增强智能体工具使用能力。
7. [MODAL: Multi-Modal Object Re-ID via Model-Driven Sparse Decoupling and Text-Image Differential Filtering](/202608/21/2608.15096v1-modal-multi-modal-object-re-id-via-model-driven-sparse-decoupling-and-text-image-differential-filtering)  
   标签：评分：8.0/10、query:mr
   evidence：多模态目标重识别中的跨模态检索与文本-图像差分过滤

### 速读区论文标签
1. [Rollplex: Cross-Phase GPU Spatial Sharing for Vision Language Model Post-Training](/202608/21/2608.14498v1-rollplex-cross-phase-gpu-spatial-sharing-for-vision-language-model-post-training)  
   标签：评分：8.0/10、query:post-multi
   evidence：面向视觉语言模型强化学习后训练的运行系统，直接涉及VLM后训练
2. [Why Vision Fails as a Universal Bridge: Rectifying Modality Asynchrony in Multilingual MLLMs](/202608/21/2608.15085v1-why-vision-fails-as-a-universal-bridge-rectifying-modality-asynchrony-in-multilingual-mllms)  
   标签：评分：8.0/10、query:post-multi
   evidence：通过机制分析矫正多语言多模态大模型中的模态异步问题
3. [SEER: Long-Context Reasoning via Selective Visual-Text Compression](/202608/21/2608.15962v1-seer-long-context-reasoning-via-selective-visual-text-compression)  
   标签：评分：8.0/10、query:mr
   evidence：通过视觉扫描与按需文本检索实现多模态长上下文推理，属于典型多模态检索增强推理架构。
4. [Multi-Granularity Sentiment Integration for LLM-Based Multimodal Sentiment Analysis](/202608/21/2608.16201v1-multi-granularity-sentiment-integration-for-llm-based-multimodal-sentiment-analysis)  
   标签：评分：8.0/10、query:post-multi
   evidence：一种基于LLM的多模态情感分析多粒度集成方法，改善跨模态对齐与多模态学习。
5. [When Is a Task Vector Enough? An Empirical Theory of Implicit Multimodal ICL](/202608/21/2608.13385v1-when-is-a-task-vector-enough-an-empirical-theory-of-implicit-multimodal-icl)  
   标签：评分：7.0/10、query:post-multi
   evidence：针对隐式多模态上下文学习提出选择-实现假说，揭示任务向量等干预的作用机制。
6. [Fine-Grained Action Recognition with Cross-Attentive Latent Sparse Experts](/202608/21/2608.13458v1-fine-grained-action-recognition-with-cross-attentive-latent-sparse-experts)  
   标签：评分：7.0/10、query:post-multi
   evidence：通过交叉注意力和稀疏专家混合实现多模态融合
7. [FZ-VLM: A Two Stage Florence-Zephyr Vision Language Model Framework for Pulmonary Nodule Characterization and Clinical Decision Making](/202608/21/2608.15004v1-fz-vlm-a-two-stage-florence-zephyr-vision-language-model-framework-for-pulmonary-nodule-characterization-and-clinical-decision-making)  
   标签：评分：7.0/10、query:post-multi
   evidence：两阶段视觉语言模型训练框架，与视觉语言模型训练需求相关
8. [Quantum Models with Multi-Stage Training for Compositional Concept Generalization](/202608/21/2608.15601v1-quantum-models-with-multi-stage-training-for-compositional-concept-generalization)  
   标签：评分：7.0/10、query:post-multi
   evidence：使用张量与变分量子电路，面向多模态学习中的组合概念泛化提出多阶段训练方法。
9. [ERSkill: Evolving for Skill-Guided Adaptive Memory Retrieval](/202608/21/2608.12720v1-erskill-evolving-for-skill-guided-adaptive-memory-retrieval)  
   标签：评分：6.0/10、query:mr
   evidence：LLM智能体自适应记忆检索，技能引导证据构造，与RAG架构相关。
10. [A Comprehensive Empirical Evaluation of Vector Database Systems for Approximate Nearest Neighbor Search: Performance, Quality, and Resource Trade-offs](/202608/21/2608.12812v1-a-comprehensive-empirical-evaluation-of-vector-database-systems-for-approximate-nearest-neighbor-search-performance-quality-and-resource-trade-offs)  
   标签：评分：6.0/10、query:mr
   evidence：系统评估七种向量数据库在ANN检索上的性能与质量，为RAG（含多模态）提供检索基础设施选型依据
11. [GLaQ: Grounding Latent Queries in Visual Evidence for Multimodal Reasoning](/202608/21/2608.15517v2-glaq-grounding-latent-queries-in-visual-evidence-for-multimodal-reasoning)  
   标签：评分：6.0/10、query:mr
   evidence：通过潜在查询锚定视觉证据改进多模态推理，并解决潜在推理中的信息重复问题，与多跳推理相关。
12. [Can Retrievers Find the Same Paper from Different Aspects? A Multi-Aspect Full-Paper Scientific Retrieval Benchmark](/202608/21/2608.15624v1-can-retrievers-find-the-same-paper-from-different-aspects-a-multi-aspect-full-paper-scientific-retrieval-benchmark)  
   标签：评分：6.0/10、query:mr
   evidence：基于多模态内容的全论文检索基准，可用于评估RAG中的检索环节


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
