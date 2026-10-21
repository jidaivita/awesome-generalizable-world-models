<!-- BEGIN GENERATED RESEARCH MAP -->

[← 首页](../../README.md#research-map) · [阅读路线](../reading-guide.md)

# M5 · 虚实差距与模型可靠性

*Reliability & Sim2Real*

> 哪些模型误差会真正影响决策，模型在什么范围内可信？

把视觉质量、物理预测和任务表现分开检查。通过物理外推、闭环使用和真实／仿真配对评估，理解一个模型何时能够支持可靠选择。

仿真内表现、真实策略排序和实际虚实迁移是不同证据。阅读时明确评估对象与配对方式。

## 从哪里开始

1. **[SIMPLER](#paper-simpler)** — 把仿真价值落实为能否可靠比较真实策略表现，而不只是画面逼真。
2. **[How Far Is Video Generation from World Model: A Physical Law Perspective](#paper-physical-law-perspective)** — 从物理测试区分分布内预测、外推与组合泛化。

## 精选论文与阅读重点

<a id="paper-simpler"></a>
### Evaluating Real-World Robot Manipulation Policies in Simulation

**CoRL 2024（论文集 2025）** · [Paper](https://proceedings.mlr.press/v270/li25c.html)

旧称／简称：SIMPLER。

把仿真价值落实为能否可靠比较真实策略表现，而不只是画面逼真。

- **重点看：** 真实/仿真配对、策略排序、视觉匹配与变体聚合。
- **适用范围：** 只做仿真内扰动不能证明虚实差距缩小；不把真机完整复现作为阅读前提。
- **关联：** [M4 · 知识的实际使用与任务相关抽象](m4-knowledge-use.md)

<a id="paper-physical-law-perspective"></a>
### How Far Is Video Generation from World Model: A Physical Law Perspective

**ICML 2025** · [Paper](https://proceedings.mlr.press/v267/kang25g.html)

从物理测试区分分布内预测、外推与组合泛化。

- **重点看：** 各类分布变化怎样构造，成功与失败是否被视觉质量指标掩盖。
- **适用范围：** 所测模型和数据下的发现，不应上升为所有视频模型的普遍限制。
- **关联：** [M3 · 泛化、迁移与上下文学习](m3-generalization.md)

<a id="paper-rethinking-sim2real"></a>
### Rethinking Sim2Real: Lower Fidelity Simulation Leads to Higher Sim2Real Transfer in Navigation

**CoRL 2022（论文集 2023）** · [Paper](https://proceedings.mlr.press/v205/truong23a.html)

检验“越真实越有用”的常见直觉。

- **重点看：** 哪些导航模拟细节被改变，为什么会影响迁移。
- **适用范围：** 结果限于论文中的导航设置，不是低保真总比高保真好。
- **关联：** [M3 · 泛化、迁移与上下文学习](m3-generalization.md)

<a id="paper-world-in-world"></a>
### World-In-World: World Models in a Closed-Loop World

**ICLR 2026** · [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/5b4263be85820683d78675cc18d2efc7-Abstract-Conference.html)

连接世界模型评估与闭环任务价值。

- **重点看：** 动作可控性、后训练数据和测试时计算如何影响闭环表现。
- **适用范围：** 闭环评估仍有任务覆盖边界；规模化结论须限定在其测试设置。
- **关联：** [M4 · 知识的实际使用与任务相关抽象](m4-knowledge-use.md) · [M7 · 预训练、规模化与基模连接](m7-scaling.md)

## 放在一起读

SIMPLER 关注仿真是否能可靠比较真实策略；Rethinking Sim2Real 检验逼真度与迁移的关系。Physical Law Perspective 与 World-In-World 分别补充物理测试和闭环任务视角。

## 继续连接

- [M3 · 泛化、迁移与上下文学习](m3-generalization.md) — 新环境表现来自复用旧知识，还是从新经验学习？
- [M4 · 知识的实际使用与任务相关抽象](m4-knowledge-use.md) — 什么信息不仅存在，而且真正支持预测、规划与决策？
- [M7 · 预训练、规模化与基模连接](m7-scaling.md) — 可控实验中的认识如何连接更强模型和更大数据？

[精读模板](../../templates/paper-note.md) · [主题比较模板](../../templates/comparison-note.md) · [返回首页 ↑](../../README.md)

<!-- END GENERATED RESEARCH MAP -->
