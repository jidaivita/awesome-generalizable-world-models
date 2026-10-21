<!-- BEGIN GENERATED RESEARCH MAP -->

[← 首页](../../README.md#research-map) · [阅读路线](../reading-guide.md)

# M3 · 泛化、迁移与上下文学习

*Generalization & In-Context Learning*

> 新环境表现来自复用旧知识，还是从新经验学习？

围绕环境变化理解知识复用和适应。先明确变化发生在哪里：对象组合、隐藏环境参数、动力学规则，还是可观测性；再看上下文究竟提供了什么信息。

环境识别、动力学学习和状态估计可能共同影响表现。上下文带来收益本身不足以判断是哪一种机制。

## 从哪里开始

1. **[Context and Diversity Matter](#paper-context-diversity)** — 研究审美锚点：把“新环境表现不错”拆成环境识别与从经验学习两类机制。
2. **[Dynamics Are Learned, Not Told](#paper-dynamics-geometries)** — 连接潜在几何与适应：轨迹上下文的平滑性怎样影响动力学偏移下的策略。

## 精选论文与阅读重点

<a id="paper-context-diversity"></a>
### Context and Diversity Matter: The Emergence of In-Context Learning in World Models

**ICLR 2026** · [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a46b9dcef23e9160f46d800a49a931d0-Abstract-Conference.html) · [Code](https://github.com/airs-cuhk/airsoul/tree/main/projects/MazeWorld)

研究审美锚点：把“新环境表现不错”拆成环境识别与从经验学习两类机制。

- **重点看：** ER/EL 的定义和理论前提，环境多样性与上下文长度，以及实验能否排除旧环境匹配。
- **适用范围：** 理论并非对所有神经网络内部算法的穷尽分类；也须排除状态估计和记忆带来的改善。
- **关联：** [M2 · 表征几何与流形](m2-geometry.md) · [M6 · 主动探索、辨识与高效适应](m6-adaptation.md)

<a id="paper-dynamics-geometries"></a>
### Dynamics Are Learned, Not Told: Semi-Supervised Discovery of Latent Dynamics Geometries For Zero-Shot Policy Adaptation

**ICML 2026** · [Paper](https://proceedings.mlr.press/v306/xu26cq.html) · [Code](https://github.com/Mr-Wonderfool/Latent-Dynamics-Geometries)

连接潜在几何与适应：轨迹上下文的平滑性怎样影响动力学偏移下的策略。

- **重点看：** 轨迹动态编码器、Lipschitz 假设、多正样本对比目标，以及未建模动力学变化测试。
- **适用范围：** 这是强化学习策略适应工作；不能直接当作通用视频预测世界模型的几何定理。
- **关联：** [M2 · 表征几何与流形](m2-geometry.md) · [M6 · 主动探索、辨识与高效适应](m6-adaptation.md)

<a id="paper-cadm"></a>
### Context-aware Dynamics Model for Generalization in Model-Based Reinforcement Learning

**ICML 2020** · [Paper](https://proceedings.mlr.press/v119/lee20g.html) · [Code](https://github.com/younggyoseo/CaDM)

了解从历史推断环境上下文的经典做法，为理解环境识别提供基线。

- **重点看：** 历史编码、前向/后向预测目标、训练测试动力学分布。
- **适用范围：** 上下文表示有效不自动证明学到了新规律；区分隐藏参数推断与直接参数输入。
- **关联：** [M6 · 主动探索、辨识与高效适应](m6-adaptation.md)

<a id="paper-dreamweaver"></a>
### Dreamweaver: Learning Compositional World Models from Pixels

**ICLR 2025** · [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ae82a60c5ce50b5c4d18cfe3214eb684-Abstract-Conference.html)

了解从像素学习可重新组合的对象与属性表征。

- **重点看：** 哪些因素被分解，训练和测试的未见组合怎样定义。
- **适用范围：** 生成未见组合不自动等于闭环规划、未知物理机制或真实迁移成功。
- **关联：** [M1 · 结构化表征、关系与不变性](m1-structure.md)

## 放在一起读

CaDM 是理解历史上下文编码的基础参照；Context and Diversity 提供环境识别与环境学习的区分；Dynamics Are Learned 把轨迹表征的几何接到策略适应。Dreamweaver 补充对象和属性组合的视角。

## 继续连接

- [M1 · 结构化表征、关系与不变性](m1-structure.md) — 哪些对象、关系与稳定结构值得被表示？
- [M2 · 表征几何与流形](m2-geometry.md) — 知识在潜在空间中如何组织，这种组织怎样影响模型行为？
- [M6 · 主动探索、辨识与高效适应](m6-adaptation.md) — 面对未知环境，应该采集、复用什么经验？

[精读模板](../../templates/paper-note.md) · [主题比较模板](../../templates/comparison-note.md) · [返回首页 ↑](../../README.md)

<!-- END GENERATED RESEARCH MAP -->
