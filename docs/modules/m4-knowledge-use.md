<!-- BEGIN GENERATED RESEARCH MAP -->

[← 首页](../../README.md#research-map) · [阅读路线](../reading-guide.md)

# M4 · 知识的实际使用与任务相关抽象

*Knowledge Use & Task Abstraction*

> 什么信息不仅存在，而且真正支持预测、规划与决策？

把内部表征连接到模型行为。既考察任务需要保留哪些信息，也考察如何通过模型的预测、规划或学习倾向，判断知识是否发挥作用。

可读出、被使用、具有任务价值需要分别讨论。某个任务中的有效抽象能否迁移到新任务，还取决于它保留了什么。

## 从哪里开始

1. **[What Has a Foundation Model Found?](#paper-what-found)** — 与两篇锚点同样匹配：用模型适应新任务的倾向检验是否学到了底层规律。
2. **[DINO-WM](#paper-dino-wm)** — 把“保留多少世界信息才够用”落到实际潜在空间规划。

## 精选论文与阅读重点

<a id="paper-what-found"></a>
### What Has a Foundation Model Found? Using Inductive Bias to Probe for World Models

**ICML 2025** · [Paper](https://proceedings.mlr.press/v267/vafa25a.html)

与两篇锚点同样匹配：用模型适应新任务的倾向检验是否学到了底层规律。

- **重点看：** 怎样从假设世界模型生成新任务，并通过学习行为测量归纳偏置。
- **适用范围：** 这里的 probe 是归纳偏置检验，不是普通线性解码器；结论仍限于被测任务和假设。
- **关联：** [M3 · 泛化、迁移与上下文学习](m3-generalization.md)

<a id="paper-dino-wm"></a>
### DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning

**ICML 2025** · [Paper](https://proceedings.mlr.press/v267/zhou25t.html)

把“保留多少世界信息才够用”落到实际潜在空间规划。

- **重点看：** 冻结视觉表征、动作条件 patch 预测，以及目标空间的规划目标。
- **适用范围：** zero-shot planning 不等于不需要相应领域的动力学轨迹训练。
- **关联：** [M7 · 预训练、规模化与基模连接](m7-scaling.md)

<a id="paper-denoised-mdps"></a>
### Denoised MDPs: Learning World Models Better Than the World Itself

**ICML 2022** · [Paper](https://proceedings.mlr.press/v162/wang22c.html)

直接研究决策型世界模型应当舍弃哪些信息。

- **重点看：** 可控性与奖励相关性两个分解维度，及其对学习的作用。
- **适用范围：** 当前任务无关的信息在新任务中可能变得重要；分解结论有结构前提。
- **关联：** [M1 · 结构化表征、关系与不变性](m1-structure.md)

<a id="paper-value-equivalence"></a>
### The Value Equivalence Principle for Model-Based Reinforcement Learning

**NeurIPS 2020** · [Paper](https://proceedings.neurips.cc/paper/2020/hash/3bb585ea00014b0e3ebe4c6dd165a358-Abstract.html)

给“模型不必完整还原世界也能支持决策”一个精确定义。

- **重点看：** 相对于哪些策略和价值函数保持 Bellman 更新等价。
- **适用范围：** 等价性依赖指定函数与策略集合，不保证任意未来任务。
- **关联：** [M5 · 虚实差距与模型可靠性](m5-reliability.md)

## 放在一起读

What Has a Foundation Model Found 从新任务中的归纳偏置检验底层结构；DINO-WM 给出表征到规划的具体接口。Denoised MDPs 与 Value Equivalence 则帮助精确定义哪些世界细节值得保留。

## 继续连接

- [M2 · 表征几何与流形](m2-geometry.md) — 知识在潜在空间中如何组织，这种组织怎样影响模型行为？
- [M3 · 泛化、迁移与上下文学习](m3-generalization.md) — 新环境表现来自复用旧知识，还是从新经验学习？
- [M5 · 虚实差距与模型可靠性](m5-reliability.md) — 哪些模型误差会真正影响决策，模型在什么范围内可信？

[精读模板](../../templates/paper-note.md) · [主题比较模板](../../templates/comparison-note.md) · [返回首页 ↑](../../README.md)

<!-- END GENERATED RESEARCH MAP -->
