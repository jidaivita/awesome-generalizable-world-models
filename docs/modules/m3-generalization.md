<!-- BEGIN GENERATED RESEARCH MAP -->

[← Research map](../../README.md#research-map) · [Reading path](../reading-guide.md)

# M3 · Generalization & In-Context Learning

> Does success in a new environment come from knowledge reuse or learning new dynamics?

Generalization can involve new object combinations, hidden environment parameters, or changes in dynamics. The papers examine what information context provides and how models use it to adapt.

Environment recognition, dynamics learning, and state estimation can all affect performance. Benefits from a longer context do not alone identify the mechanism.

## Where to start

1. **[Context and Diversity Matter](#paper-context-diversity)** — Distinguishes recognizing familiar environments from learning dynamics through current experience.
2. **[Dynamics Are Learned, Not Told](#paper-dynamics-geometries)** — Connects trajectory geometry with policy adaptation under changing dynamics.

## Papers and reading pointers

<a id="paper-context-diversity"></a>
### Context and Diversity Matter: The Emergence of In-Context Learning in World Models

**ICLR 2026** · [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a46b9dcef23e9160f46d800a49a931d0-Abstract-Conference.html) · [Code](https://github.com/airs-cuhk/airsoul/tree/main/projects/MazeWorld)

Distinguishes recognizing familiar environments from learning dynamics through current experience.

- **Read for:** Definitions and assumptions behind environment recognition and environment learning; environment diversity, context length, and controls for familiar-environment matching.
- **Scope:** The framework is not an exhaustive classification of all neural algorithms. State estimation and memory may also explain improvements.
- **Related topics:** [M2 · Representation Geometry & Manifolds](m2-geometry.md) · [M6 · Exploration & Efficient Adaptation](m6-adaptation.md)

<a id="paper-cadm"></a>
### Context-aware Dynamics Model for Generalization in Model-Based Reinforcement Learning

**ICML 2020** · [Paper](https://proceedings.mlr.press/v119/lee20g.html) · [Code](https://github.com/younggyoseo/CaDM)

Infers environment context from interaction history to model changing dynamics.

- **Read for:** History encoding, forward and backward prediction objectives, and the training and test dynamics distributions.
- **Scope:** Useful context representations alone do not demonstrate learning new laws. Distinguish hidden-parameter inference from directly supplied parameters.
- **Related topics:** [M6 · Exploration & Efficient Adaptation](m6-adaptation.md)

<a id="paper-dreamweaver"></a>
### Dreamweaver: Learning Compositional World Models from Pixels

**ICLR 2025** · [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ae82a60c5ce50b5c4d18cfe3214eb684-Abstract-Conference.html)

Learns object and attribute representations for combinations beyond training configurations.

- **Read for:** Which factors are decomposed and how unseen combinations are defined in training and evaluation.
- **Scope:** Generating unseen combinations does not by itself establish closed-loop planning, adaptation to unknown physical mechanisms, or real-world transfer.
- **Related topics:** [M1 · Structure & Invariance](m1-structure.md)

<a id="paper-dynamics-geometries"></a>
### Dynamics Are Learned, Not Told: Semi-Supervised Discovery of Latent Dynamics Geometries For Zero-Shot Policy Adaptation

**ICML 2026** · [Paper](https://proceedings.mlr.press/v306/xu26cq.html) · [Code](https://github.com/Mr-Wonderfool/Latent-Dynamics-Geometries)

Connects trajectory geometry with policy adaptation under changing dynamics.

- **Read for:** Trajectory dynamics encoders, Lipschitz assumptions, multi-positive contrastive learning, and tests of unmodeled dynamics changes.
- **Scope:** This work studies reinforcement-learning policy adaptation; its theory is not automatically a theorem about general video world models.
- **Related topics:** [M2 · Representation Geometry & Manifolds](m2-geometry.md) · [M6 · Exploration & Efficient Adaptation](m6-adaptation.md)

## Read together

CaDM provides background on history-based context encoding. Context and Diversity distinguishes environment recognition from environment learning; Dynamics Are Learned connects trajectory geometry to policy adaptation. Dreamweaver adds a view of object and attribute composition.

## Related topics

- [M1 · Structure & Invariance](m1-structure.md) — Which objects, relations, and stable structures should a model represent?
- [M2 · Representation Geometry & Manifolds](m2-geometry.md) — How is knowledge organized in latent space, and what does that organization do?
- [M6 · Exploration & Efficient Adaptation](m6-adaptation.md) — What experience should an agent acquire or reuse in an unfamiliar environment?

[Paper-note template](../../templates/paper-note.md) · [Comparison template](../../templates/comparison-note.md) · [Back to overview ↑](../../README.md)

<!-- END GENERATED RESEARCH MAP -->
