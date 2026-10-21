<!-- BEGIN GENERATED RESEARCH MAP -->

[← Paper index](../../README.md#research-map) · [Reading guide](../reading-guide.md)

# Predictive Architectures & Pretraining

The papers examine video pretraining, joint-embedding predictive learning, and world-model-based control at different data and model scales. Their architectures separate representation learning, dynamics prediction, and planning in different ways.

Large-scale representation pretraining and executable planning involve different stages. A shared algorithm does not imply one checkpoint that works in every environment.

## Papers

<a id="paper-leworldmodel"></a>
### LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels

Lucas Maes et al. · **arXiv 2026** · [Paper](https://arxiv.org/abs/2603.19312) · [Code](https://github.com/lucas-maes/le-wm) · [Project](https://le-wm.github.io/)

Earlier titles / aliases: LeWM.

Learns a compact world model end to end with joint-embedding predictive objectives.

- **Method and analysis:** The predictive loss, latent-distribution regularization, planning interface, and physical probes.
- **Evaluation scope:** The reported model has about 15M parameters. Training-time figures depend on the hardware, dataset, and optimization setup.
- **Related topics:** [Representation Geometry & Analysis](m2-geometry.md) · [Planning & Task-Relevant Representations](m4-knowledge-use.md)

<a id="paper-dreamerv3"></a>
### Mastering diverse control tasks through world models

Danijar Hafner et al. · **Nature 2025** · [Paper](https://www.nature.com/articles/s41586-025-08744-2)

Earlier titles / aliases: DreamerV3.

Learns latent dynamics and actor-critic policies with a shared algorithm and hyperparameters across control tasks.

- **Method and analysis:** Which hyperparameters and algorithmic choices are shared, and which model parameters are trained per environment.
- **Evaluation scope:** A shared algorithm and hyperparameters do not imply a single pretrained checkpoint that generalizes everywhere without training.
- **Related topics:** [Planning & Task-Relevant Representations](m4-knowledge-use.md)

<a id="paper-vjepa2"></a>
### V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning

Mido Assran et al. · **arXiv technical report 2025** · [Paper](https://arxiv.org/abs/2506.09985)

Combines video representation pretraining with action-conditioned post-training for robot planning.

- **Method and analysis:** What passive pretraining and action-conditioned post-training each learn, and the interfaces used in evaluation.
- **Evaluation scope:** Representation pretraining alone is not a complete planning system. The action interface requires relevant interaction data.
- **Related topics:** [Planning & Task-Relevant Representations](m4-knowledge-use.md)

<a id="paper-jepa-wms"></a>
### What Drives Success in Physical Planning with Joint-Embedding Predictive World Models?

Basile Terver et al. · **TMLR 2026** · [Paper](https://arxiv.org/abs/2512.24497) · [Code](https://github.com/facebookresearch/jepa-wms)

Compares architecture, training objectives, and planners in JEPA world models.

- **Method and analysis:** Matched comparisons of architectures, training objectives, planning algorithms, and data scale.
- **Evaluation scope:** The findings concern the evaluated JEPA world-model family, not every type of world model.
- **Related topics:** [Planning & Task-Relevant Representations](m4-knowledge-use.md)

## Method comparisons

LeWorldModel trains an encoder and predictor jointly. JEPA-WMs compares architectures, objectives, and planners. V-JEPA 2 separates video pretraining from action-conditioned post-training, while DreamerV3 learns world models and policies within each environment.

## Related topics

- [Representation Geometry & Analysis](m2-geometry.md)
- [Planning & Task-Relevant Representations](m4-knowledge-use.md)
- [Evaluation & Sim-to-Real Transfer](m5-reliability.md)

[Paper-note template](../../templates/paper-note.md) · [Comparison template](../../templates/comparison-note.md) · [Back to overview ↑](../../README.md)

<!-- END GENERATED RESEARCH MAP -->
