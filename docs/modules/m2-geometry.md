<!-- BEGIN GENERATED RESEARCH MAP -->

[← 首页](../../README.md#research-map) · [阅读路线](../reading-guide.md)

# M2 · 表征几何与流形

*Representation Geometry & Manifolds*

> 知识在潜在空间中如何组织，这种组织怎样影响模型行为？

既研究模型自然形成的几何，也研究主动引入几何约束能否改善动态学习。阅读时先辨认论文在做哪一类工作，再看几何现象如何连接到模型功能。

自然形成的结构、预先施加的结构、结构带来的任务收益是三个不同问题。二维投影可以帮助提出假设，结论还需要其他证据。

## 从哪里开始

1. **[Interpreting Physics](#paper-interpreting-physics)** — 研究审美锚点：用层级、子空间与干预区分物理信息的组织方式。
2. **[SMDS / Shape Happens](#paper-smds)** — 方法桥梁：从“画出形状”转向比较竞争几何假设并测试功能。
3. **[GRWM](#paper-grwm)** — 连接表征诊断与方法：改善潜在几何能否减少长程预测误差。

## 三条阅读线索

| 线索 | 论文 | 阅读时先区分什么 |
| :--- | :--- | :--- |
| 自然形成的几何与功能 | Interpreting Physics、SMDS、Origins | 观察到的结构、竞争假设与功能证据 |
| 几何先验与动态学习 | GRWM、Group-Structured Latent Space、GeoWorld | 先验来自哪里，以及它独立带来的收益 |
| 几何与环境适应 | [Context and Diversity](m3-generalization.md#paper-context-diversity)、[Dynamics Are Learned](m3-generalization.md#paper-dynamics-geometries) | 环境变化、轨迹信息与可迁移结构 |

**工具按问题补充。** 先掌握 PCA/SVD、线性探针、周期变量编码、子空间比较、基本干预和留出验证；需要时再进入内在维数、拓扑分析或黎曼优化。

例如 `z(θ) = (cos θ, sin θ, cos 2θ, sin 2θ, …)` 由一个自由度控制，却可以占据多个线性方向。环境自由度、向量维度、线性跨度、流形内在维数与干预方向数需要分别理解。这是数学示例，不是模型测量结果。

## 精选论文与阅读重点

<a id="paper-interpreting-physics"></a>
### Interpreting Physics in Video World Models

**ICML 2026** · [Paper](https://proceedings.mlr.press/v306/joseph26a.html)

研究审美锚点：用层级、子空间与干预区分物理信息的组织方式。

- **重点看：** 速度与方向的层级差异；圆周型群体编码；探针、注意力消融和方向 steering 分别能证明什么。
- **适用范围：** 改变解码方向不等于已经改善模型原生预测或规划；线性子空间维度不等于流形内在维数。
- **关联：** [M4 · 知识的实际使用与任务相关抽象](m4-knowledge-use.md)

<a id="paper-smds"></a>
### Hypothesis-Driven Feature Manifold Analysis in LLMs via Supervised Multi-Dimensional Scaling

**TMLR 2026** · [Paper](https://arxiv.org/abs/2510.01025) · [Code](https://github.com/UKPLab/tmlr2026-manifold-analysis)

旧称／简称：Shape Happens: Automatic Feature Manifold Discovery in LLMs via Supervised Multi-Dimensional Scaling；Shape Happens。

方法桥梁：从“画出形状”转向比较竞争几何假设并测试功能。

- **重点看：** SMDS 如何利用监督信息比较圆、线、簇等假设；留出评估与干预证据。
- **适用范围：** 这是有监督、假设驱动分析，不是无先验自动发现；LLM 结果不是世界模型中的既有结论。
- **关联：** [M4 · 知识的实际使用与任务相关抽象](m4-knowledge-use.md)

<a id="paper-grwm"></a>
### Cloning Deterministic Worlds: The Critical Role of Latent Geometry in Long-Horizon World Models

**CVPR 2026** · [Paper](https://arxiv.org/abs/2510.26782) · [Code](https://github.com/XiaFire/Clone_Deterministic_Environment) · [Project](https://xiafire.github.io/grwm-project-page/)

旧称／简称：Clone Deterministic 3D Worlds with Geometrically-Regularized World Models；Clone Deterministic 3D Worlds。

连接表征诊断与方法：改善潜在几何能否减少长程预测误差。

- **重点看：** 真实状态 oracle 对照；带时序上下文的编码器；slowness/uniformity 正则；对应消融。
- **适用范围：** 主要证据来自固定规则的确定性环境；不能据此宣称解决开放世界 OOD，且需区分几何正则与历史消歧的贡献。
- **关联：** [M4 · 知识的实际使用与任务相关抽象](m4-knowledge-use.md) · [M5 · 虚实差距与模型可靠性](m5-reliability.md)

<a id="paper-group-latents"></a>
### Learning Abstract World Models with a Group-Structured Latent Space

**arXiv 2025；正式主会/期刊归属未在本条确认** · [Paper](https://arxiv.org/abs/2506.01529) · [Code](https://github.com/khanhvu207/world-models-group-latents)

用平移、旋转等已知结构建立可操作的几何归纳偏置。

- **重点看：** 群作用如何对应潜在转移，结构化与非结构化信息如何共存。
- **适用范围：** 使用已知对称性不等于从数据中自行发现规律；不把投稿记录当主会录用。
- **关联：** [M1 · 结构化表征、关系与不变性](m1-structure.md)

<a id="paper-geoworld"></a>
### GeoWorld: Geometric World Models

**CVPR 2026** · [Paper](https://arxiv.org/abs/2602.23058) · [Project](https://steve-zeyu-zhang.github.io/GeoWorld/)

方法参照：研究选择非欧几何空间能带来哪些规划收益。

- **重点看：** Hyperbolic JEPA 与几何优化的独立作用；和欧氏空间的公平对照。
- **适用范围：** 主要实验为 CrossTask/COIN 的多步视觉程序规划，不等于连续物理动力学或真机虚实迁移已被验证。
- **关联：** [M4 · 知识的实际使用与任务相关抽象](m4-knowledge-use.md)

<a id="paper-origins-manifolds"></a>
### The Origins of Representation Manifolds in Large Language Models

**arXiv 2025；正式主会/期刊归属未在本条确认** · [Paper](https://arxiv.org/abs/2505.18235)

理论桥梁：理解表征距离为何可能反映概念空间的内在关系。

- **重点看：** 生成假设、余弦相似度与内在几何的联系，以及理论预测如何检验。
- **适用范围：** 定理有明确假设；文本表征结果不是任意网络或世界模型的普遍定律。本轮未确认正式发表状态。

## 放在一起读

Interpreting Physics 提供物理信息组织的分析入口；SMDS 提供比较几何假设的方法；GRWM 把诊断连接到长程预测。三者适合连续阅读，但分析对象、监督信息和任务证据各不相同。

## 继续连接

- [M3 · 泛化、迁移与上下文学习](m3-generalization.md) — 新环境表现来自复用旧知识，还是从新经验学习？
- [M4 · 知识的实际使用与任务相关抽象](m4-knowledge-use.md) — 什么信息不仅存在，而且真正支持预测、规划与决策？
- [M7 · 预训练、规模化与基模连接](m7-scaling.md) — 可控实验中的认识如何连接更强模型和更大数据？

[精读模板](../../templates/paper-note.md) · [主题比较模板](../../templates/comparison-note.md) · [返回首页 ↑](../../README.md)

<!-- END GENERATED RESEARCH MAP -->
