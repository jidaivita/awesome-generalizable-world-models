<!-- BEGIN GENERATED RESEARCH MAP -->

[← Paper index](../../README.md#research-map) · [Reading guide](../reading-guide.md)

# Generalization & Context-Based Adaptation

Generalization can involve new object combinations, hidden environment parameters, or changes in dynamics. The papers examine what information context provides and how models use it to adapt.

Environment recognition, dynamics learning, and state estimation can all affect performance. Benefits from a longer context do not alone identify the mechanism.

## Papers

<a id="paper-context-diversity"></a>
### Context and Diversity Matter: The Emergence of In-Context Learning in World Models

Fan Wang et al. · **ICLR 2026** · [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a46b9dcef23e9160f46d800a49a931d0-Abstract-Conference.html) · [Code](https://github.com/airs-cuhk/airsoul/tree/main/projects/MazeWorld)

Distinguishes recognizing familiar environments from learning dynamics through current experience.

- **Method and analysis:** Definitions and assumptions behind environment recognition and environment learning; environment diversity, context length, and controls for familiar-environment matching.
- **Evaluation scope:** The framework is not an exhaustive classification of all neural algorithms. State estimation and memory may also explain improvements.
- **Related topics:** [Representation Geometry & Analysis](m2-geometry.md) · [Exploration & Experience Replay](m6-adaptation.md)

<a id="paper-cadm"></a>
### Context-aware Dynamics Model for Generalization in Model-Based Reinforcement Learning

Kimin Lee et al. · **ICML 2020** · [Paper](https://proceedings.mlr.press/v119/lee20g.html) · [Code](https://github.com/younggyoseo/CaDM)

Infers environment context from interaction history to model changing dynamics.

- **Method and analysis:** History encoding, forward and backward prediction objectives, and the training and test dynamics distributions.
- **Evaluation scope:** Environment context is inferred from interaction history. The evaluation concerns adaptation within the specified dynamics distributions.
- **Related topics:** [Exploration & Experience Replay](m6-adaptation.md)

<a id="paper-dreamweaver"></a>
### Dreamweaver: Learning Compositional World Models from Pixels

Junyeob Baek et al. · **ICLR 2025** · [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ae82a60c5ce50b5c4d18cfe3214eb684-Abstract-Conference.html)

Learns object and attribute representations for combinations beyond training configurations.

- **Method and analysis:** Which factors are decomposed and how unseen combinations are defined in training and evaluation.
- **Evaluation scope:** Generating unseen combinations does not by itself establish closed-loop planning, adaptation to unknown physical mechanisms, or real-world transfer.
- **Related topics:** [Object-Centric & Relational Models](m1-structure.md)

<a id="paper-dynamics-geometries"></a>
### Dynamics Are Learned, Not Told: Semi-Supervised Discovery of Latent Dynamics Geometries For Zero-Shot Policy Adaptation

Zhiming Xu et al. · **ICML 2026** · [Paper](https://proceedings.mlr.press/v306/xu26cq.html) · [Code](https://github.com/Mr-Wonderfool/Latent-Dynamics-Geometries)

Learns trajectory-based dynamics representations for zero-shot policy adaptation to changed dynamics.

- **Method and analysis:** Trajectory dynamics encoders, Lipschitz assumptions, multi-positive contrastive learning, and tests of unmodeled dynamics changes.
- **Evaluation scope:** This work studies reinforcement-learning policy adaptation; its theory is not automatically a theorem about general video world models.
- **Related topics:** [Representation Geometry & Analysis](m2-geometry.md) · [Exploration & Experience Replay](m6-adaptation.md)

## Method comparisons

CaDM provides background on history-based context encoding. Context and Diversity distinguishes environment recognition from environment learning; Dynamics Are Learned connects trajectory geometry to policy adaptation. Dreamweaver adds a view of object and attribute composition.

## Related topics

- [Object-Centric & Relational Models](m1-structure.md)
- [Representation Geometry & Analysis](m2-geometry.md)
- [Exploration & Experience Replay](m6-adaptation.md)

[Paper-note template](../../templates/paper-note.md) · [Comparison template](../../templates/comparison-note.md) · [Back to overview ↑](../../README.md)

<!-- END GENERATED RESEARCH MAP -->
