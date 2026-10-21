<!-- BEGIN GENERATED RESEARCH MAP -->

[← Paper index](../../README.md#research-map) · [Reading guide](../reading-guide.md)

# Generalization & Context-Based Adaptation

A model deployed in a new environment may face different object combinations, hidden physical parameters, or changed transition rules. These papers study compositional representations and the use of interaction history to predict or control under those shifts.

The comparisons distinguish recognition of familiar environments, learning from new context, and adaptation through learned trajectory embeddings.

## Papers

<a id="paper-context-diversity"></a>
### Context and Diversity Matter: The Emergence of In-Context Learning in World Models

Fan Wang et al. · **ICLR 2026** · [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a46b9dcef23e9160f46d800a49a931d0-Abstract-Conference.html) · [Code](https://github.com/airs-cuhk/airsoul/tree/main/projects/MazeWorld)

- **Method:** The analysis separates environment recognition, which identifies a familiar environment, from environment learning, which estimates dynamics from the current context. Error bounds link these mechanisms to context length and training-environment diversity.
- **Evaluation:** World-model experiments vary context, data diversity, and architecture to test the theoretical predictions. The distinction concerns how prediction improves with experience while model weights remain fixed.
- **Related topics:** [Representation Geometry & Analysis](m2-geometry.md) · [Exploration & Experience Replay](m6-adaptation.md)

<a id="paper-cadm"></a>
### Context-aware Dynamics Model for Generalization in Model-Based Reinforcement Learning

Kimin Lee et al. · **ICML 2020** · [Paper](https://proceedings.mlr.press/v119/lee20g.html) · [Code](https://github.com/younggyoseo/CaDM)

- **Method:** A history encoder estimates a context vector for local dynamics. Forward and backward prediction losses train the context to retain environment-specific information, and the next-state predictor conditions on this vector.
- **Evaluation:** Simulated robotics and control tasks test prediction and policy performance across different dynamics. Adaptation uses recent interaction history as evidence about the current environment.
- **Related topics:** [Exploration & Experience Replay](m6-adaptation.md)

<a id="paper-dreamweaver"></a>
### Dreamweaver: Learning Compositional World Models from Pixels

Junyeob Baek et al. · **ICLR 2025** · [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ae82a60c5ce50b5c4d18cfe3214eb684-Abstract-Conference.html)

- **Method:** A Recurrent Block-Slot Unit decomposes raw video into objects and their attributes. Predicting multiple future frames encourages the representation to retain dynamic as well as static factors.
- **Evaluation:** Disentanglement is measured with the DCI framework across video datasets. Recombining attributes of previously observed objects tests compositional video generation without auxiliary text, masks, or bounding boxes.
- **Related topics:** [Object-Centric & Relational Models](m1-structure.md)

<a id="paper-dynamics-geometries"></a>
### Dynamics Are Learned, Not Told: Semi-Supervised Discovery of Latent Dynamics Geometries For Zero-Shot Policy Adaptation

Zhiming Xu et al. · **ICML 2026** · [Paper](https://proceedings.mlr.press/v306/xu26cq.html) · [Code](https://github.com/Mr-Wonderfool/Latent-Dynamics-Geometries)

- **Method:** A trajectory encoder learns a dynamics context using a multi-positive InfoNCE objective. The analysis relates encoder smoothness to target-domain regret, motivating a latent geometry that supports adaptation without privileged physical-parameter labels.
- **Evaluation:** MuJoCo experiments test severe dynamics shifts, including structural failures outside the explicit parameterization used by identification baselines, alongside in-distribution policy stability.
- **Related topics:** [Representation Geometry & Analysis](m2-geometry.md) · [Exploration & Experience Replay](m6-adaptation.md)

## Method comparisons

CaDM conditions a predictor on recent history; Context and Diversity analyzes when context identifies a familiar environment and when it supports learning new dynamics. Dynamics Are Learned shapes the trajectory embedding used for policy adaptation. Dreamweaver addresses a separate axis of generalization: recombining object attributes to generate new futures.

## Related topics

- [Object-Centric & Relational Models](m1-structure.md)
- [Representation Geometry & Analysis](m2-geometry.md)
- [Exploration & Experience Replay](m6-adaptation.md)

[Paper-note template](../../templates/paper-note.md) · [Comparison template](../../templates/comparison-note.md) · [Back to overview ↑](../../README.md)

<!-- END GENERATED RESEARCH MAP -->
