<!-- BEGIN GENERATED RESEARCH MAP -->

[← 首页](../../README.md#research-map) · [阅读路线](../reading-guide.md)

# M7 · 预训练、规模化与基模连接

*Pretraining & Scaling*

> 可控实验中的认识如何连接更强模型和更大数据？

通过预训练视频模型、端到端 JEPA 和通用世界模型学习算法，理解表示、动态模型、动作接口和规划器之间的关系。也为小规模机制分析寻找合适载体。

大规模表征预训练与可执行的规划系统有不同训练阶段；统一算法不等于一个检查点跨所有环境直接使用。

## 从哪里开始

1. **[LeWorldModel](#paper-leworldmodel)** — 可选轻量实验载体：不依赖大型冻结编码器的端到端 JEPA。
2. **[What Drives Success in JEPA-WMs?](#paper-jepa-wms)** — 组件级受控比较范例，帮助区分几何之外的架构、损失和规划器因素。

## 精选论文与阅读重点

<a id="paper-leworldmodel"></a>
### LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels

**arXiv 2026；正式主会/期刊归属未在本条确认** · [Paper](https://arxiv.org/abs/2603.19312) · [Code](https://github.com/lucas-maes/le-wm) · [Project](https://le-wm.github.io/)

旧称／简称：LeWM。

可选轻量实验载体：不依赖大型冻结编码器的端到端 JEPA。

- **重点看：** 预测损失、潜在分布正则、规划接口及物理探针；先看小模型能否支撑所需分析。
- **适用范围：** 作者报告约 15M 参数、单 GPU 数小时；本轮未独立运行，不能承诺用户机器的耗时和显存。
- **关联：** [M2 · 表征几何与流形](m2-geometry.md) · [M4 · 知识的实际使用与任务相关抽象](m4-knowledge-use.md)

<a id="paper-jepa-wms"></a>
### What Drives Success in Physical Planning with Joint-Embedding Predictive World Models?

**TMLR 2026** · [Paper](https://arxiv.org/abs/2512.24497) · [Code](https://github.com/facebookresearch/jepa-wms)

组件级受控比较范例，帮助区分几何之外的架构、损失和规划器因素。

- **重点看：** 架构、训练目标、规划算法与数据规模的对照是否匹配。
- **适用范围：** 实验结论针对被测 JEPA-WM 家族，不自动代表所有世界模型。
- **关联：** [M4 · 知识的实际使用与任务相关抽象](m4-knowledge-use.md)

<a id="paper-dreamerv3"></a>
### Mastering diverse control tasks through world models

**Nature 2025** · [Paper](https://www.nature.com/articles/s41586-025-08744-2)

旧称／简称：DreamerV3。

理解世界模型学习算法在不同任务上的稳健性与可扩展性。

- **重点看：** 哪些超参数和算法设计共享，哪些参数仍按环境训练。
- **适用范围：** 统一算法及超参数不等于一个预训练检查点能处处零样本泛化。
- **关联：** [M4 · 知识的实际使用与任务相关抽象](m4-knowledge-use.md)

<a id="paper-vjepa2"></a>
### V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning

**arXiv technical report 2025** · [Paper](https://arxiv.org/abs/2506.09985)

了解大规模观察视频表征与动作条件预测、规划的连接。

- **重点看：** 被动预训练和动作条件后训练各学到什么，以及评估接口。
- **适用范围：** 表征预训练不是完整规划系统；动作接口仍依赖相应交互数据。
- **关联：** [M4 · 知识的实际使用与任务相关抽象](m4-knowledge-use.md)

## 放在一起读

LeWorldModel 提供端到端小模型路线，JEPA-WMs 组件研究帮助拆分架构、目标和规划算法的影响。V-JEPA 2 与 DreamerV3 则提供扩大数据和任务范围后的参照。

## 继续连接

- [M2 · 表征几何与流形](m2-geometry.md) — 知识在潜在空间中如何组织，这种组织怎样影响模型行为？
- [M4 · 知识的实际使用与任务相关抽象](m4-knowledge-use.md) — 什么信息不仅存在，而且真正支持预测、规划与决策？
- [M5 · 虚实差距与模型可靠性](m5-reliability.md) — 哪些模型误差会真正影响决策，模型在什么范围内可信？

[精读模板](../../templates/paper-note.md) · [主题比较模板](../../templates/comparison-note.md) · [返回首页 ↑](../../README.md)

<!-- END GENERATED RESEARCH MAP -->
