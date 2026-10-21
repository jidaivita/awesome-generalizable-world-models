<!-- BEGIN GENERATED RESEARCH MAP -->

[← 首页](../README.md#reading-route)

# 阅读路线 · 从机制问题到实际使用

这条路线连接 12 篇论文。它提供一个建议顺序，也允许按当前问题选读。每一步留下一个足够小、能够说明理解的产物。

## 01—03 · 建立问题

先理解知识的组织、新环境中的学习，以及如何检验底层结构。

### 01 · Interpreting Physics

**[Interpreting Physics in Video World Models](https://proceedings.mlr.press/v306/joseph26a.html)**

- **读完回答：** 把“独立物理变量”与“分布式编码”的可检验区别写清楚。
- **最小产物：** 一张主张—证据—边界表。
- **阅读重点：** [表征几何与流形](modules/m2-geometry.md#paper-interpreting-physics)

### 02 · Context and Diversity Matter

**[Context and Diversity Matter: The Emergence of In-Context Learning in World Models](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a46b9dcef23e9160f46d800a49a931d0-Abstract-Conference.html)**

- **读完回答：** 区分认出旧环境、上下文中学习动力学、单纯状态估计。
- **最小产物：** 一张 ER/EL 对照表。
- **阅读重点：** [泛化、迁移与上下文学习](modules/m3-generalization.md#paper-context-diversity)

### 03 · What Has a Foundation Model Found?

**[What Has a Foundation Model Found? Using Inductive Bias to Probe for World Models](https://proceedings.mlr.press/v267/vafa25a.html)**

- **读完回答：** 理解为何既有任务高分不足以说明学会底层规律。
- **最小产物：** 给前两篇补一个替代解释与区分测试。
- **阅读重点：** [知识的实际使用与任务相关抽象](modules/m4-knowledge-use.md#paper-what-found)

## 04—05 · 学习分析与建模方法

从比较几何假设，走向几何诊断和长程预测。

### 04 · SMDS / Shape Happens

**[Hypothesis-Driven Feature Manifold Analysis in LLMs via Supervised Multi-Dimensional Scaling](https://arxiv.org/abs/2510.01025)**

- **读完回答：** 学会比较几何假设，而不是从降维图直接下结论。
- **最小产物：** 列出假设、监督信息、留出评估和干预各自的位置。
- **阅读重点：** [表征几何与流形](modules/m2-geometry.md#paper-smds)

### 05 · GRWM

**[Cloning Deterministic Worlds: The Critical Role of Latent Geometry in Long-Horizon World Models](https://arxiv.org/abs/2510.26782)**

- **读完回答：** 考察几何诊断如何变成改善长程预测的方法。
- **最小产物：** 拆出表征、时序上下文、损失和动态预测器四类因素。
- **阅读重点：** [表征几何与流形](modules/m2-geometry.md#paper-grwm)

## 06—08 · 接到可运行的预测与规划系统

明确表示、动态模型和规划器的接口，再学习控制组件间的混杂因素。

### 06 · DINO-WM

**[DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning](https://proceedings.mlr.press/v267/zhou25t.html)**

- **读完回答：** 把潜在表征接到实际规划用途。
- **最小产物：** 画清编码器—动态模型—规划器接口。
- **阅读重点：** [知识的实际使用与任务相关抽象](modules/m4-knowledge-use.md#paper-dino-wm)

### 07 · LeWorldModel

**[LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels](https://arxiv.org/abs/2603.19312)**

- **读完回答：** 评估一个小模型能否承载后续表征分析。
- **最小产物：** 记录可用数据、代码入口、依赖与待测资源；不直接全量训练。
- **阅读重点：** [预训练、规模化与基模连接](modules/m7-scaling.md#paper-leworldmodel)

### 08 · What Drives Success in JEPA-WMs?

**[What Drives Success in Physical Planning with Joint-Embedding Predictive World Models?](https://arxiv.org/abs/2512.24497)**

- **读完回答：** 学习如何控制架构、目标和规划器等混杂因素。
- **最小产物：** 形成一张公平对照检查表。
- **阅读重点：** [预训练、规模化与基模连接](modules/m7-scaling.md#paper-jepa-wms)

## 09—12 · 连接先验、适应、可靠性与探索

把已有理解扩展到环境变化和实际决策所需的信息。

### 09 · Group-Structured Latent Space

**[Learning Abstract World Models with a Group-Structured Latent Space](https://arxiv.org/abs/2506.01529)**

- **读完回答：** 区分预先给定的对称性和从数据涌现的几何。
- **最小产物：** 写清已知信息、模型先验和未知因素。
- **阅读重点：** [表征几何与流形](modules/m2-geometry.md#paper-group-latents)

### 10 · Dynamics Are Learned, Not Told

**[Dynamics Are Learned, Not Told: Semi-Supervised Discovery of Latent Dynamics Geometries For Zero-Shot Policy Adaptation](https://proceedings.mlr.press/v306/xu26cq.html)**

- **读完回答：** 将几何视角接到新动力学下的适应。
- **最小产物：** 分别记录理论假设和经验评估覆盖范围。
- **阅读重点：** [泛化、迁移与上下文学习](modules/m3-generalization.md#paper-dynamics-geometries)

### 11 · SIMPLER

**[Evaluating Real-World Robot Manipulation Policies in Simulation](https://proceedings.mlr.press/v270/li25c.html)**

- **读完回答：** 理解模型误差何时影响真实选择。
- **最小产物：** 区分视觉相似、预测准确与策略排序可靠。
- **阅读重点：** [虚实差距与模型可靠性](modules/m5-reliability.md#paper-simpler)

### 12 · Poke and Strike

**[Poke and Strike: Learning Task-Informed Exploration Policies](https://proceedings.mlr.press/v305/aoyama25a.html)**

- **读完回答：** 理解如何选择任务真正需要的新经验。
- **最小产物：** 写出探索成本与任务信息价值的关系。
- **阅读重点：** [主动探索、辨识与高效适应](modules/m6-adaptation.md#paper-poke-strike)

## 怎样把阅读变成积累

**索引浏览**只需知道论文在回答什么，以及为何相关。**精读**围绕疑问选择关键章节，留下 1—3 个核心图表或实验的精确定位。两三篇工作有具体联系时，再做一页**主题比较**：它们支持了什么解释，还有什么没有区分清楚。

数学和工具学习由阅读中的障碍驱动。一次阅读结束，只确定一个具体下一步：核对一个实验、弄懂一个定义、查一个资源，或尝试一个小分析。

## 一个可缩放的四周起步节奏

| 阶段 | 阅读重点 | 建议产物 |
| :--- | :--- | :--- |
| 第一周 | 两篇锚点 | 两份主张、证据与适用范围笔记 |
| 第二周 | SMDS 与 GRWM | 一页几何专题比较 |
| 第三周 | What Has a Foundation Model Found 或 DINO-WM | 一个关于信息使用的具体检查标准 |
| 第四周 | 按疑问选择 LeWM、Group-Latents 或 Dynamics-Geometries | 专题总结，或一个带对照的小分析 |

可以以 4—6 篇形成理解的笔记为起步目标，按实际时间调整。实验从已经选定的问题出发；资源条件和代码可用性需要单独确认。

[精读模板](../templates/paper-note.md) · [主题比较模板](../templates/comparison-note.md) · [返回精选列表](../README.md#papers)

<!-- END GENERATED RESEARCH MAP -->
