<!-- BEGIN GENERATED RESEARCH MAP -->

<a id="top"></a>
<div align="center">

# Awesome Generalizable World Models

**世界模型研究地图 · 机理、表征几何、泛化与适应**

*How is world knowledge learned, organized, used, and adapted?*

![Curated papers](https://img.shields.io/badge/精选论文-30-2563eb?style=flat-square) ![Reading route](https://img.shields.io/badge/阅读路线-12-0f766e?style=flat-square) ![Research modules](https://img.shields.io/badge/研究模块-7-7c3aed?style=flat-square)

[开始阅读](#start-here) · [阅读路线](#reading-route) · [七个模块](#research-map) · [全部精选](#papers) · [参与维护](CONTRIBUTING.md)

</div>

---

模型如何从有限经验中形成可迁移的世界知识？这些知识如何组织、如何被使用，又如何在新环境中被修正？

这里整理与这些问题直接相关的世界模型论文，覆盖表征、动态学习、预测、规划和适应。当前重点是 **表征几何 → 泛化与上下文学习 → 知识的实际使用**。每篇都附有收录理由，帮助从一个具体问题进入阅读。

<a id="start-here"></a>
## Start Here · 从两个问题出发

| 01 · 知识怎样组织？ | 02 · 新经验怎样起作用？ |
| :--- | :--- |
| **[Interpreting Physics in Video World Models](https://proceedings.mlr.press/v306/joseph26a.html)** | **[Context and Diversity Matter: The Emergence of In-Context Learning in World Models](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a46b9dcef23e9160f46d800a49a931d0-Abstract-Conference.html)** |
| 从物理量、子空间与干预理解表征的组织和功能。 | 区分识别熟悉环境与从当前经历学习动力学。 |
| **带着问题读：** 可解码的信息，在模型行为中起了什么作用？ | **带着问题读：** 上下文带来的收益，究竟来自什么机制？ |

两篇论文共同提供一个阅读起点：提出明确的解释，寻找能够区分它们的对照，再判断结论覆盖到哪里。

<a id="research-map"></a>
## Research Map · 七个模块

| 模块 | 核心问题 | 精选 | 阅读指引 |
| :--- | :--- | :---: | :---: |
| [M1 · 结构化表征、关系与不变性](#m1) | 哪些对象、关系与稳定结构值得被表示？ | 4 | [进入模块](docs/modules/m1-structure.md) |
| [M2 · 表征几何与流形 ★](#m2) | 知识在潜在空间中如何组织，这种组织怎样影响模型行为？ | 6 | [进入模块](docs/modules/m2-geometry.md) |
| [M3 · 泛化、迁移与上下文学习 ★](#m3) | 新环境表现来自复用旧知识，还是从新经验学习？ | 4 | [进入模块](docs/modules/m3-generalization.md) |
| [M4 · 知识的实际使用与任务相关抽象 ★](#m4) | 什么信息不仅存在，而且真正支持预测、规划与决策？ | 4 | [进入模块](docs/modules/m4-knowledge-use.md) |
| [M5 · 虚实差距与模型可靠性](#m5) | 哪些模型误差会真正影响决策，模型在什么范围内可信？ | 4 | [进入模块](docs/modules/m5-reliability.md) |
| [M6 · 主动探索、辨识与高效适应](#m6) | 面对未知环境，应该采集、复用什么经验？ | 4 | [进入模块](docs/modules/m6-adaptation.md) |
| [M7 · 预训练、规模化与基模连接](#m7) | 可控实验中的认识如何连接更强模型和更大数据？ | 4 | [进入模块](docs/modules/m7-scaling.md) |

★ 近期重点。模块用于组织问题，每篇仅计入一个主模块；关联标签连接其他方向。

<a id="reading-route"></a>
## Reading Route · 12 篇问题链

从机制问题出发，经过分析方法，再连接预测、规划与适应。可以按当前疑问选读；这条路线不是开始实践前的必修清单。

| # | 论文 | 这一步关注什么 |
| :---: | :--- | :--- |
| 01 | [Interpreting Physics](#paper-interpreting-physics) | 把“独立物理变量”与“分布式编码”的可检验区别写清楚。 |
| 02 | [Context and Diversity Matter](#paper-context-diversity) | 区分认出旧环境、上下文中学习动力学、单纯状态估计。 |
| 03 | [What Has a Foundation Model Found?](#paper-what-found) | 理解为何既有任务高分不足以说明学会底层规律。 |
| 04 | [SMDS / Shape Happens](#paper-smds) | 学会比较几何假设，而不是从降维图直接下结论。 |
| 05 | [GRWM](#paper-grwm) | 考察几何诊断如何变成改善长程预测的方法。 |
| 06 | [DINO-WM](#paper-dino-wm) | 把潜在表征接到实际规划用途。 |
| 07 | [LeWorldModel](#paper-leworldmodel) | 评估一个小模型能否承载后续表征分析。 |
| 08 | [What Drives Success in JEPA-WMs?](#paper-jepa-wms) | 学习如何控制架构、目标和规划器等混杂因素。 |
| 09 | [Group-Structured Latent Space](#paper-group-latents) | 区分预先给定的对称性和从数据涌现的几何。 |
| 10 | [Dynamics Are Learned, Not Told](#paper-dynamics-geometries) | 将几何视角接到新动力学下的适应。 |
| 11 | [SIMPLER](#paper-simpler) | 理解模型误差何时影响真实选择。 |
| 12 | [Poke and Strike](#paper-poke-strike) | 理解如何选择任务真正需要的新经验。 |

[查看完整阅读指引与最小产物 →](docs/reading-guide.md)

<a id="papers"></a>
## Selected Papers · 精选论文

**首读** 为两篇锚点，**路线** 为其余推荐阅读条目。发表状态与来源按条目记录，代码链接表示资源入口。

<a id="m1"></a>
### M1 · 结构化表征、关系与不变性

*Structure & Invariance*

> 哪些对象、关系与稳定结构值得被表示？

<a id="paper-causal-jepa"></a>
- **[Causal-JEPA: Learning World Models through Object-Level Latent Masking](https://proceedings.mlr.press/v306/nam26c.html)**<br>
  ICML 2026 · [Paper](https://proceedings.mlr.press/v306/nam26c.html) · [Code](https://github.com/galilai-group/cjepa)<br>
  把对象级结构与 JEPA 学习联系起来。

<a id="paper-cswm"></a>
- **[Contrastive Learning of Structured World Models](https://arxiv.org/abs/1911.12247)**<br>
  ICLR 2020 · [Paper](https://arxiv.org/abs/1911.12247)<br>
  对象分解与非像素重建式动态学习的基础入口。

<a id="paper-nri"></a>
- **[Neural Relational Inference for Interacting Systems](https://proceedings.mlr.press/v80/kipf18a.html)**<br>
  ICML 2018 · [Paper](https://proceedings.mlr.press/v80/kipf18a.html)<br>
  从轨迹推断交互关系，连接“学到什么结构”和“结构能否用于预测”。

<a id="paper-spartan"></a>
- **[SPARTAN: A Sparse Transformer World Model Attending to What Matters](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e2c33c1753e1f1924f5560b11fc4444f-Abstract-Conference.html)**<br>
  NeurIPS 2025 · [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e2c33c1753e1f1924f5560b11fc4444f-Abstract-Conference.html)<br>
  研究稀疏、随上下文变化的交互结构如何支持机制变化后的适应。

[阅读重点与论文联系 →](docs/modules/m1-structure.md) · [返回目录 ↑](#research-map)

<a id="m2"></a>
### M2 · 表征几何与流形

*Representation Geometry & Manifolds*

> 知识在潜在空间中如何组织，这种组织怎样影响模型行为？

<a id="paper-interpreting-physics"></a>
- **[Interpreting Physics in Video World Models](https://proceedings.mlr.press/v306/joseph26a.html)** · **首读**<br>
  ICML 2026 · [Paper](https://proceedings.mlr.press/v306/joseph26a.html)<br>
  研究审美锚点：用层级、子空间与干预区分物理信息的组织方式。

<a id="paper-smds"></a>
- **[Hypothesis-Driven Feature Manifold Analysis in LLMs via Supervised Multi-Dimensional Scaling](https://arxiv.org/abs/2510.01025)** · **路线**<br>
  TMLR 2026 · [Paper](https://arxiv.org/abs/2510.01025) · [Code](https://github.com/UKPLab/tmlr2026-manifold-analysis)<br>
  方法桥梁：从“画出形状”转向比较竞争几何假设并测试功能。

<a id="paper-grwm"></a>
- **[Cloning Deterministic Worlds: The Critical Role of Latent Geometry in Long-Horizon World Models](https://arxiv.org/abs/2510.26782)** · **路线**<br>
  CVPR 2026 · [Paper](https://arxiv.org/abs/2510.26782) · [Code](https://github.com/XiaFire/Clone_Deterministic_Environment) · [Project](https://xiafire.github.io/grwm-project-page/)<br>
  连接表征诊断与方法：改善潜在几何能否减少长程预测误差。

<a id="paper-group-latents"></a>
- **[Learning Abstract World Models with a Group-Structured Latent Space](https://arxiv.org/abs/2506.01529)** · **路线**<br>
  arXiv 2025；正式主会/期刊归属未在本条确认 · [Paper](https://arxiv.org/abs/2506.01529) · [Code](https://github.com/khanhvu207/world-models-group-latents)<br>
  用平移、旋转等已知结构建立可操作的几何归纳偏置。

<a id="paper-geoworld"></a>
- **[GeoWorld: Geometric World Models](https://arxiv.org/abs/2602.23058)**<br>
  CVPR 2026 · [Paper](https://arxiv.org/abs/2602.23058) · [Project](https://steve-zeyu-zhang.github.io/GeoWorld/)<br>
  方法参照：研究选择非欧几何空间能带来哪些规划收益。

<a id="paper-origins-manifolds"></a>
- **[The Origins of Representation Manifolds in Large Language Models](https://arxiv.org/abs/2505.18235)**<br>
  arXiv 2025；正式主会/期刊归属未在本条确认 · [Paper](https://arxiv.org/abs/2505.18235)<br>
  理论桥梁：理解表征距离为何可能反映概念空间的内在关系。

[阅读重点与论文联系 →](docs/modules/m2-geometry.md) · [返回目录 ↑](#research-map)

<a id="m3"></a>
### M3 · 泛化、迁移与上下文学习

*Generalization & In-Context Learning*

> 新环境表现来自复用旧知识，还是从新经验学习？

<a id="paper-context-diversity"></a>
- **[Context and Diversity Matter: The Emergence of In-Context Learning in World Models](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a46b9dcef23e9160f46d800a49a931d0-Abstract-Conference.html)** · **首读**<br>
  ICLR 2026 · [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a46b9dcef23e9160f46d800a49a931d0-Abstract-Conference.html) · [Code](https://github.com/airs-cuhk/airsoul/tree/main/projects/MazeWorld)<br>
  研究审美锚点：把“新环境表现不错”拆成环境识别与从经验学习两类机制。

<a id="paper-dynamics-geometries"></a>
- **[Dynamics Are Learned, Not Told: Semi-Supervised Discovery of Latent Dynamics Geometries For Zero-Shot Policy Adaptation](https://proceedings.mlr.press/v306/xu26cq.html)** · **路线**<br>
  ICML 2026 · [Paper](https://proceedings.mlr.press/v306/xu26cq.html) · [Code](https://github.com/Mr-Wonderfool/Latent-Dynamics-Geometries)<br>
  连接潜在几何与适应：轨迹上下文的平滑性怎样影响动力学偏移下的策略。

<a id="paper-cadm"></a>
- **[Context-aware Dynamics Model for Generalization in Model-Based Reinforcement Learning](https://proceedings.mlr.press/v119/lee20g.html)**<br>
  ICML 2020 · [Paper](https://proceedings.mlr.press/v119/lee20g.html) · [Code](https://github.com/younggyoseo/CaDM)<br>
  了解从历史推断环境上下文的经典做法，为理解环境识别提供基线。

<a id="paper-dreamweaver"></a>
- **[Dreamweaver: Learning Compositional World Models from Pixels](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ae82a60c5ce50b5c4d18cfe3214eb684-Abstract-Conference.html)**<br>
  ICLR 2025 · [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ae82a60c5ce50b5c4d18cfe3214eb684-Abstract-Conference.html)<br>
  了解从像素学习可重新组合的对象与属性表征。

[阅读重点与论文联系 →](docs/modules/m3-generalization.md) · [返回目录 ↑](#research-map)

<a id="m4"></a>
### M4 · 知识的实际使用与任务相关抽象

*Knowledge Use & Task Abstraction*

> 什么信息不仅存在，而且真正支持预测、规划与决策？

<a id="paper-what-found"></a>
- **[What Has a Foundation Model Found? Using Inductive Bias to Probe for World Models](https://proceedings.mlr.press/v267/vafa25a.html)** · **路线**<br>
  ICML 2025 · [Paper](https://proceedings.mlr.press/v267/vafa25a.html)<br>
  与两篇锚点同样匹配：用模型适应新任务的倾向检验是否学到了底层规律。

<a id="paper-dino-wm"></a>
- **[DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning](https://proceedings.mlr.press/v267/zhou25t.html)** · **路线**<br>
  ICML 2025 · [Paper](https://proceedings.mlr.press/v267/zhou25t.html)<br>
  把“保留多少世界信息才够用”落到实际潜在空间规划。

<a id="paper-denoised-mdps"></a>
- **[Denoised MDPs: Learning World Models Better Than the World Itself](https://proceedings.mlr.press/v162/wang22c.html)**<br>
  ICML 2022 · [Paper](https://proceedings.mlr.press/v162/wang22c.html)<br>
  直接研究决策型世界模型应当舍弃哪些信息。

<a id="paper-value-equivalence"></a>
- **[The Value Equivalence Principle for Model-Based Reinforcement Learning](https://proceedings.neurips.cc/paper/2020/hash/3bb585ea00014b0e3ebe4c6dd165a358-Abstract.html)**<br>
  NeurIPS 2020 · [Paper](https://proceedings.neurips.cc/paper/2020/hash/3bb585ea00014b0e3ebe4c6dd165a358-Abstract.html)<br>
  给“模型不必完整还原世界也能支持决策”一个精确定义。

[阅读重点与论文联系 →](docs/modules/m4-knowledge-use.md) · [返回目录 ↑](#research-map)

<a id="m5"></a>
### M5 · 虚实差距与模型可靠性

*Reliability & Sim2Real*

> 哪些模型误差会真正影响决策，模型在什么范围内可信？

<a id="paper-simpler"></a>
- **[Evaluating Real-World Robot Manipulation Policies in Simulation](https://proceedings.mlr.press/v270/li25c.html)** · **路线**<br>
  CoRL 2024（论文集 2025） · [Paper](https://proceedings.mlr.press/v270/li25c.html)<br>
  把仿真价值落实为能否可靠比较真实策略表现，而不只是画面逼真。

<a id="paper-physical-law-perspective"></a>
- **[How Far Is Video Generation from World Model: A Physical Law Perspective](https://proceedings.mlr.press/v267/kang25g.html)**<br>
  ICML 2025 · [Paper](https://proceedings.mlr.press/v267/kang25g.html)<br>
  从物理测试区分分布内预测、外推与组合泛化。

<a id="paper-rethinking-sim2real"></a>
- **[Rethinking Sim2Real: Lower Fidelity Simulation Leads to Higher Sim2Real Transfer in Navigation](https://proceedings.mlr.press/v205/truong23a.html)**<br>
  CoRL 2022（论文集 2023） · [Paper](https://proceedings.mlr.press/v205/truong23a.html)<br>
  检验“越真实越有用”的常见直觉。

<a id="paper-world-in-world"></a>
- **[World-In-World: World Models in a Closed-Loop World](https://proceedings.iclr.cc/paper_files/paper/2026/hash/5b4263be85820683d78675cc18d2efc7-Abstract-Conference.html)**<br>
  ICLR 2026 · [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/5b4263be85820683d78675cc18d2efc7-Abstract-Conference.html)<br>
  连接世界模型评估与闭环任务价值。

[阅读重点与论文联系 →](docs/modules/m5-reliability.md) · [返回目录 ↑](#research-map)

<a id="m6"></a>
### M6 · 主动探索、辨识与高效适应

*Exploration & Efficient Adaptation*

> 面对未知环境，应该采集、复用什么经验？

<a id="paper-poke-strike"></a>
- **[Poke and Strike: Learning Task-Informed Exploration Policies](https://proceedings.mlr.press/v305/aoyama25a.html)** · **路线**<br>
  CoRL 2025 · [Paper](https://proceedings.mlr.press/v305/aoyama25a.html)<br>
  把主动探索从“识别所有参数”转向“识别任务真正需要的信息”。

<a id="paper-asid"></a>
- **[ASID: Active Exploration for System Identification in Robotic Manipulation](https://proceedings.iclr.cc/paper_files/paper/2024/hash/ae8afec5dabb07091d8f85128250f2ff-Abstract-Conference.html)**<br>
  ICLR 2024 · [Paper](https://proceedings.iclr.cc/paper_files/paper/2024/hash/ae8afec5dabb07091d8f85128250f2ff-Abstract-Conference.html)<br>
  理解主动交互、参数辨识和模拟器改进的闭环。

<a id="paper-curious-replay"></a>
- **[Curious Replay for Model-based Adaptation](https://proceedings.mlr.press/v202/kauvar23a.html)**<br>
  ICML 2023 · [Paper](https://proceedings.mlr.press/v202/kauvar23a.html)<br>
  把经验利用纳入适应研究，不仅关注采集更多数据。

<a id="paper-plan2explore"></a>
- **[Planning to Explore via Self-Supervised World Models](https://proceedings.mlr.press/v119/sekar20a.html)**<br>
  ICML 2020 · [Paper](https://proceedings.mlr.press/v119/sekar20a.html)<br>
  探索如何在下游任务未知时主动积累有用经验。

[阅读重点与论文联系 →](docs/modules/m6-adaptation.md) · [返回目录 ↑](#research-map)

<a id="m7"></a>
### M7 · 预训练、规模化与基模连接

*Pretraining & Scaling*

> 可控实验中的认识如何连接更强模型和更大数据？

<a id="paper-leworldmodel"></a>
- **[LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels](https://arxiv.org/abs/2603.19312)** · **路线**<br>
  arXiv 2026；正式主会/期刊归属未在本条确认 · [Paper](https://arxiv.org/abs/2603.19312) · [Code](https://github.com/lucas-maes/le-wm) · [Project](https://le-wm.github.io/)<br>
  可选轻量实验载体：不依赖大型冻结编码器的端到端 JEPA。

<a id="paper-jepa-wms"></a>
- **[What Drives Success in Physical Planning with Joint-Embedding Predictive World Models?](https://arxiv.org/abs/2512.24497)** · **路线**<br>
  TMLR 2026 · [Paper](https://arxiv.org/abs/2512.24497) · [Code](https://github.com/facebookresearch/jepa-wms)<br>
  组件级受控比较范例，帮助区分几何之外的架构、损失和规划器因素。

<a id="paper-dreamerv3"></a>
- **[Mastering diverse control tasks through world models](https://www.nature.com/articles/s41586-025-08744-2)**<br>
  Nature 2025 · [Paper](https://www.nature.com/articles/s41586-025-08744-2)<br>
  理解世界模型学习算法在不同任务上的稳健性与可扩展性。

<a id="paper-vjepa2"></a>
- **[V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://arxiv.org/abs/2506.09985)**<br>
  arXiv technical report 2025 · [Paper](https://arxiv.org/abs/2506.09985)<br>
  了解大规模观察视频表征与动作条件预测、规划的连接。

[阅读重点与论文联系 →](docs/modules/m7-scaling.md) · [返回目录 ↑](#research-map)

<a id="notes"></a>
## Notes · 阅读与讨论

完整笔记可以保留在自己的笔记工具中。这里仅链接明确选择公开的内容；私人想法和未发表实验设计保留在私人笔记里。

[精读模板](templates/paper-note.md) · [主题比较模板](templates/comparison-note.md) · [分享模板](templates/sharing-note.md)

## Contributing · 一起维护

欢迎补充直接相关的论文、修正来源与发表状态，或提出更好的阅读联系。推荐时请说明：**它回答什么问题、最值得看的证据是什么、与哪个模块有关**。

[收录与贡献指南](CONTRIBUTING.md) · [数据与生成说明](docs/maintenance.md) · [来源说明](docs/sources.md)

<sub>关注问题的积累，也关注不同解释之间的联系。精选池会随阅读逐步调整。</sub>

<!-- END GENERATED RESEARCH MAP -->
