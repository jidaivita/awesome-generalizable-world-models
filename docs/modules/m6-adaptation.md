<!-- BEGIN GENERATED RESEARCH MAP -->

[← 首页](../../README.md#research-map) · [阅读路线](../reading-guide.md)

# M6 · 主动探索、辨识与高效适应

*Exploration & Efficient Adaptation*

> 面对未知环境，应该采集、复用什么经验？

研究经验的选择和利用：什么动作能揭示有用信息，何时已有经验值得重放，以及这些信息如何帮助后续任务。

给定模型类内的参数辨识、缺失机制的学习、主动采集和已有经验回放各有不同假设与成本。

## 从哪里开始

1. **[Poke and Strike](#paper-poke-strike)** — 把主动探索从“识别所有参数”转向“识别任务真正需要的信息”。
2. **[Planning to Explore via Self-Supervised World Models](#paper-plan2explore)** — 探索如何在下游任务未知时主动积累有用经验。

## 精选论文与阅读重点

<a id="paper-poke-strike"></a>
### Poke and Strike: Learning Task-Informed Exploration Policies

**CoRL 2025** · [Paper](https://proceedings.mlr.press/v305/aoyama25a.html)

把主动探索从“识别所有参数”转向“识别任务真正需要的信息”。

- **重点看：** 任务敏感性、探索奖励和探索停止条件；哪些信息是训练时特权信息。
- **适用范围：** 完整操作系统有资源与训练前提；先学习问题定义，不直接承诺轻量真机复现。
- **关联：** [M4 · 知识的实际使用与任务相关抽象](m4-knowledge-use.md)

<a id="paper-asid"></a>
### ASID: Active Exploration for System Identification in Robotic Manipulation

**ICLR 2024** · [Paper](https://proceedings.iclr.cc/paper_files/paper/2024/hash/ae8afec5dabb07091d8f85128250f2ff-Abstract-Conference.html)

理解主动交互、参数辨识和模拟器改进的闭环。

- **重点看：** 如何选择有信息量的动作，辨识结果怎样进入后续模型。
- **适用范围：** 给定模型类内估参不同于发现缺失机制；真实机器人链路不属于初版实现任务。
- **关联：** [M5 · 虚实差距与模型可靠性](m5-reliability.md)

<a id="paper-curious-replay"></a>
### Curious Replay for Model-based Adaptation

**ICML 2023** · [Paper](https://proceedings.mlr.press/v202/kauvar23a.html)

把经验利用纳入适应研究，不仅关注采集更多数据。

- **重点看：** 新颖性、预测误差和回放优先级的作用。
- **适用范围：** 回放已有经验不等于主动选择新的物理交互。
- **关联：** [M3 · 泛化、迁移与上下文学习](m3-generalization.md)

<a id="paper-plan2explore"></a>
### Planning to Explore via Self-Supervised World Models

**ICML 2020** · [Paper](https://proceedings.mlr.press/v119/sekar20a.html)

探索如何在下游任务未知时主动积累有用经验。

- **重点看：** 模型分歧、预测新颖性与后续任务学习。
- **适用范围：** 通用新颖性不一定对应某个任务最值得辨识的信息。
- **关联：** [M4 · 知识的实际使用与任务相关抽象](m4-knowledge-use.md)

## 放在一起读

Plan2Explore 从任务未知时的探索出发，ASID 将主动交互接到辨识，Poke and Strike 强调任务所需的信息，Curious Replay 关注已有经验的再次利用。比较它们优化的信息价值和使用条件。

## 继续连接

- [M3 · 泛化、迁移与上下文学习](m3-generalization.md) — 新环境表现来自复用旧知识，还是从新经验学习？
- [M4 · 知识的实际使用与任务相关抽象](m4-knowledge-use.md) — 什么信息不仅存在，而且真正支持预测、规划与决策？
- [M5 · 虚实差距与模型可靠性](m5-reliability.md) — 哪些模型误差会真正影响决策，模型在什么范围内可信？

[精读模板](../../templates/paper-note.md) · [主题比较模板](../../templates/comparison-note.md) · [返回首页 ↑](../../README.md)

<!-- END GENERATED RESEARCH MAP -->
