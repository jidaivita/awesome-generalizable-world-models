<!-- BEGIN GENERATED RESEARCH MAP -->

[← Research map](../../README.md#research-map) · [Reading path](../reading-guide.md)

# M7 · Pretraining & Scaling

> How do controlled insights connect to stronger models and larger datasets?

The papers examine video pretraining, joint-embedding predictive learning, and world-model-based control at different data and model scales. Their architectures separate representation learning, dynamics prediction, and planning in different ways.

Large-scale representation pretraining and executable planning involve different stages. A shared algorithm does not imply one checkpoint that works in every environment.

## Where to start

1. **[LeWorldModel](#paper-leworldmodel)** — Learns a compact world model end to end with joint-embedding predictive objectives.
2. **[What Drives Success in JEPA-WMs?](#paper-jepa-wms)** — Compares architecture, training objectives, and planners in JEPA world models.

## Papers and reading pointers

<a id="paper-leworldmodel"></a>
### LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels

**arXiv 2026** · [Paper](https://arxiv.org/abs/2603.19312) · [Code](https://github.com/lucas-maes/le-wm) · [Project](https://le-wm.github.io/)

Earlier titles / aliases: LeWM.

Learns a compact world model end to end with joint-embedding predictive objectives.

- **Read for:** The predictive loss, latent-distribution regularization, planning interface, and physical probes.
- **Scope:** The reported model has about 15M parameters. Training-time figures depend on the hardware, dataset, and optimization setup.
- **Related topics:** [M2 · Representation Geometry & Manifolds](m2-geometry.md) · [M4 · Knowledge Use & Task Abstraction](m4-knowledge-use.md)

<a id="paper-dreamerv3"></a>
### Mastering diverse control tasks through world models

**Nature 2025** · [Paper](https://www.nature.com/articles/s41586-025-08744-2)

Earlier titles / aliases: DreamerV3.

Studies a shared world-model learning algorithm and hyperparameters across diverse tasks.

- **Read for:** Which hyperparameters and algorithmic choices are shared, and which model parameters are trained per environment.
- **Scope:** A shared algorithm and hyperparameters do not imply a single pretrained checkpoint that generalizes everywhere without training.
- **Related topics:** [M4 · Knowledge Use & Task Abstraction](m4-knowledge-use.md)

<a id="paper-vjepa2"></a>
### V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning

**arXiv technical report 2025** · [Paper](https://arxiv.org/abs/2506.09985)

Connects observational video pretraining with action-conditioned prediction and planning.

- **Read for:** What passive pretraining and action-conditioned post-training each learn, and the interfaces used in evaluation.
- **Scope:** Representation pretraining alone is not a complete planning system. The action interface requires relevant interaction data.
- **Related topics:** [M4 · Knowledge Use & Task Abstraction](m4-knowledge-use.md)

<a id="paper-jepa-wms"></a>
### What Drives Success in Physical Planning with Joint-Embedding Predictive World Models?

**TMLR 2026** · [Paper](https://arxiv.org/abs/2512.24497) · [Code](https://github.com/facebookresearch/jepa-wms)

Compares architecture, training objectives, and planners in JEPA world models.

- **Read for:** Matched comparisons of architectures, training objectives, planning algorithms, and data scale.
- **Scope:** The findings concern the evaluated JEPA world-model family, not every type of world model.
- **Related topics:** [M4 · Knowledge Use & Task Abstraction](m4-knowledge-use.md)

## Read together

LeWorldModel provides a small end-to-end route. JEPA-WMs component studies separate architecture, objective, and planning effects. V-JEPA 2 and DreamerV3 offer broader references for data and task scaling.

## Related topics

- [M2 · Representation Geometry & Manifolds](m2-geometry.md) — How is knowledge organized in latent space, and what does that organization do?
- [M4 · Knowledge Use & Task Abstraction](m4-knowledge-use.md) — Which information actually supports prediction, planning, and decisions?
- [M5 · Reliability & Sim2Real](m5-reliability.md) — Which model errors matter for decisions, and when is a model trustworthy?

[Paper-note template](../../templates/paper-note.md) · [Comparison template](../../templates/comparison-note.md) · [Back to overview ↑](../../README.md)

<!-- END GENERATED RESEARCH MAP -->
