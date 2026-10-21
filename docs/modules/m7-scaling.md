<!-- BEGIN GENERATED RESEARCH MAP -->

[← Paper index](../../README.md#research-map) · [Reading guide](../reading-guide.md)

# Predictive Architectures & Pretraining

World-model architectures divide representation learning, dynamics prediction, and policy optimization in different ways. This section covers video pretraining, end-to-end joint-embedding prediction, component studies, and control learned through imagined trajectories.

The comparisons separate transferable pretrained encoders from environment-specific predictors and policies.

## Papers

<a id="paper-leworldmodel"></a>
### LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels

Lucas Maes et al. · **arXiv 2026** · [Paper](https://arxiv.org/abs/2603.19312) · [Code](https://github.com/lucas-maes/le-wm) · [Project](https://le-wm.github.io/)

Earlier titles / aliases: LeWM.

- **Method:** The encoder and predictor train jointly from pixels with two losses: next-embedding prediction and a regularizer encouraging Gaussian-distributed embeddings. The resulting compact model supplies latent predictions for planning.
- **Evaluation:** Experiments cover 2D and 3D control tasks, probes of physical quantities, and surprise responses to implausible events. The reported model has approximately 15 million parameters.
- **Related topics:** [Representation Geometry & Analysis](m2-geometry.md) · [Planning & Task-Relevant Representations](m4-knowledge-use.md)

<a id="paper-dreamerv3"></a>
### Mastering diverse control tasks through world models

Danijar Hafner et al. · **Nature 2025** · [Paper](https://www.nature.com/articles/s41586-025-08744-2)

Earlier titles / aliases: DreamerV3.

- **Method:** A recurrent latent world model generates imagined trajectories for actor-critic learning. Normalization, loss balancing, and value transformations stabilize optimization across domains.
- **Evaluation:** More than 150 tasks test a shared algorithm configuration, including Minecraft learning from scratch. Model and policy parameters are learned in each environment; the shared component is the algorithm and its hyperparameters.
- **Related topics:** [Planning & Task-Relevant Representations](m4-knowledge-use.md)

<a id="paper-vjepa2"></a>
### V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning

Mido Assran et al. · **arXiv technical report 2025** · [Paper](https://arxiv.org/abs/2506.09985)

- **Method:** Action-free joint-embedding prediction pretrains a video encoder on internet video. A subsequent action-conditioned model, V-JEPA 2-AC, is trained with robot trajectories and used to plan toward image goals.
- **Evaluation:** Evaluation spans motion understanding, action anticipation, video question answering, and pick-and-place planning on Franka robots in two labs. Robot planning uses action-conditioned post-training on DROID data.
- **Related topics:** [Planning & Task-Relevant Representations](m4-knowledge-use.md)

<a id="paper-jepa-wms"></a>
### What Drives Success in Physical Planning with Joint-Embedding Predictive World Models?

Basile Terver et al. · **TMLR 2026** · [Paper](https://arxiv.org/abs/2512.24497) · [Code](https://github.com/facebookresearch/jepa-wms)

- **Method:** A component study varies world-model architecture, training objective, and planning algorithm within the joint-embedding predictive family. The resulting configuration combines the empirically favorable choices.
- **Evaluation:** Simulated environments and real robotic data support navigation and manipulation comparisons with DINO-WM and V-JEPA 2-AC. The study attributes planning performance to specific modeling and optimization choices.
- **Related topics:** [Planning & Task-Relevant Representations](m4-knowledge-use.md)

## Method comparisons

V-JEPA 2 separates broad video pretraining from action-conditioned robot modeling; LeWorldModel jointly learns its encoder and predictor from pixels. JEPA-WMs compares choices within this predictive family. DreamerV3 instead couples an environment-specific world model to actor-critic learning, sharing its algorithm configuration across tasks.

## Related topics

- [Representation Geometry & Analysis](m2-geometry.md)
- [Planning & Task-Relevant Representations](m4-knowledge-use.md)
- [Evaluation & Sim-to-Real Transfer](m5-reliability.md)

[Paper-note template](../../templates/paper-note.md) · [Comparison template](../../templates/comparison-note.md) · [Back to overview ↑](../../README.md)

<!-- END GENERATED RESEARCH MAP -->
