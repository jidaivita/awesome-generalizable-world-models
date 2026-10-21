<!-- BEGIN GENERATED RESEARCH MAP -->

[← 首页](../../README.md#research-map) · [阅读路线](../reading-guide.md)

# M1 · 结构化表征、关系与不变性

*Structure & Invariance*

> 哪些对象、关系与稳定结构值得被表示？

从对象与关系出发，理解模型如何把复杂观测分解为可用于动态预测的结构。重点看结构来自模型先验、学习目标还是数据，以及这种结构在什么变化下保持有效。

M1 关注表示的内容和归纳偏置；M2 进一步研究这些内容在潜在空间里的组织；M4 检查它们是否被任务实际使用。

## 从哪里开始

1. **[Neural Relational Inference for Interacting Systems](#paper-nri)** — 从轨迹推断交互关系，连接“学到什么结构”和“结构能否用于预测”。
2. **[Contrastive Learning of Structured World Models](#paper-cswm)** — 对象分解与非像素重建式动态学习的基础入口。

## 精选论文与阅读重点

<a id="paper-causal-jepa"></a>
### Causal-JEPA: Learning World Models through Object-Level Latent Masking

**ICML 2026** · [Paper](https://proceedings.mlr.press/v306/nam26c.html) · [Code](https://github.com/galilai-group/cjepa)

把对象级结构与 JEPA 学习联系起来。

- **重点看：** 对象级潜在掩码如何制造结构化部分可观测性，是否促进关系信息的利用。
- **适用范围：** 潜在掩码不自动等于对真实物理因果机制实施干预。
- **关联：** [M4 · 知识的实际使用与任务相关抽象](m4-knowledge-use.md)

<a id="paper-cswm"></a>
### Contrastive Learning of Structured World Models

**ICLR 2020** · [Paper](https://arxiv.org/abs/1911.12247)

对象分解与非像素重建式动态学习的基础入口。

- **重点看：** 对象表示、关系动态与对比目标各自承担什么功能。
- **适用范围：** 结构化基准中的成功不能直接推广为开放世界组合泛化。
- **关联：** [M4 · 知识的实际使用与任务相关抽象](m4-knowledge-use.md)

<a id="paper-nri"></a>
### Neural Relational Inference for Interacting Systems

**ICML 2018** · [Paper](https://proceedings.mlr.press/v80/kipf18a.html)

从轨迹推断交互关系，连接“学到什么结构”和“结构能否用于预测”。

- **重点看：** 潜在图、图神经网络动态解码器，以及关系恢复和预测结果是否一致。
- **适用范围：** 观察性关系恢复不等于任意条件下的真实因果图识别。
- **关联：** [M4 · 知识的实际使用与任务相关抽象](m4-knowledge-use.md)

<a id="paper-spartan"></a>
### SPARTAN: A Sparse Transformer World Model Attending to What Matters

**NeurIPS 2025** · [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e2c33c1753e1f1924f5560b11fc4444f-Abstract-Conference.html)

研究稀疏、随上下文变化的交互结构如何支持机制变化后的适应。

- **重点看：** 稀疏注意力、干预设置、少样本适应，以及模型借助了哪些先验。
- **适用范围：** 必须结合稀疏机制变化与对象化假设解释泛化结论。
- **关联：** [M3 · 泛化、迁移与上下文学习](m3-generalization.md)

## 放在一起读

NRI 与 C-SWM 分别从交互关系和对象表示进入；SPARTAN 与 Causal-JEPA 则把结构选择连接到适应或潜在预测。比较时关注对象信息如何获得、结构是否随上下文变化，以及关系恢复与预测表现是否一致。

## 继续连接

- [M2 · 表征几何与流形](m2-geometry.md) — 知识在潜在空间中如何组织，这种组织怎样影响模型行为？
- [M3 · 泛化、迁移与上下文学习](m3-generalization.md) — 新环境表现来自复用旧知识，还是从新经验学习？
- [M4 · 知识的实际使用与任务相关抽象](m4-knowledge-use.md) — 什么信息不仅存在，而且真正支持预测、规划与决策？

[精读模板](../../templates/paper-note.md) · [主题比较模板](../../templates/comparison-note.md) · [返回首页 ↑](../../README.md)

<!-- END GENERATED RESEARCH MAP -->
