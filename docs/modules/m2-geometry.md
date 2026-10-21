<!-- BEGIN GENERATED RESEARCH MAP -->

[← Paper index](../../README.md#research-map) · [Reading guide](../reading-guide.md) · [Supplementary reading](../supplementary.md)

# Representation Geometry & Symmetry

Latent geometry and transformation structure determine which changes a world model can represent. These papers study geometric regularization, learned group actions, equivariant transitions, and dynamic memory under partial observability.

The comparisons distinguish supplied symmetry priors, learned observation mappings, and learned transformation parameters. Long-horizon prediction, equivariance probes, and downstream planning provide different tests of the resulting representations.

## Learning group structure and equivariant transitions

<a id="paper-group-structure"></a>
### Learning Disentangled Representations and Group Structure of Dynamical Environments

Robin Quessard et al. · **NeurIPS 2020** · [Paper](https://proceedings.neurips.cc/paper/2020/hash/e449b9317dad920c0dd5ad0a2a2d5e49-Abstract.html) · [Code](https://github.com/IndustAI/learning-group-structure)

- **Method:** An encoder maps observations to a spherical latent space, and learned rotation matrices represent the effects of interactions. A regularizer encourages each transformation to act on a small subset of latent dimensions, separating factors of change.
- **Evaluation:** Experiments use explicitly symmetric environments and evaluate long-horizon prediction and latent disentanglement. The method learns the transformation parameters from interaction sequences under an orthogonal latent-transition parameterization.
- **Related topics:** [Structured & Compositional Representations](m1-structure.md) · [World Model Interpretability](m8-interpretability.md)

<a id="paper-sen"></a>
### Learning Symmetric Embeddings for Equivariant World Models

Jung Yeon Park et al. · **ICML 2022** · [Paper](https://proceedings.mlr.press/v162/park22a.html)

- **Method:** A symmetric embedding network maps observations with a difficult-to-specify group action into features with a prescribed transformation rule. It is trained jointly with an equivariant transition network using a contrastive prediction objective.
- **Evaluation:** Transition-prediction experiments compare learned embeddings with fully equivariant and non-equivariant baselines across three forms of symmetry. The latent group action is specified; the learned component connects complex observations to that representation.
- **Related topics:** [Generalization & Adaptation](m3-generalization.md)

<a id="paper-group-latents"></a>
### Learning Abstract World Models with a Group-Structured Latent Space

Thomas Delliaux et al. · **arXiv 2025** · [Paper](https://arxiv.org/abs/2506.01529) · [Code](https://github.com/khanhvu207/world-models-group-latents)

- **Method:** Known symmetries determine the latent manifold and the group actions used for transitions. Additional latent variables retain information that does not follow the prescribed symmetry.
- **Evaluation:** Transition prediction and downstream reinforcement learning are tested in environments with translation and rotation, including first-person 3D views. The symmetry is supplied as prior knowledge.
- **Related topics:** [Structured & Compositional Representations](m1-structure.md)

## Geometric regularization and dynamic memory

<a id="paper-grwm"></a>
### Cloning Deterministic Worlds: The Critical Role of Latent Geometry in Long-Horizon World Models

Zaishuo Xia et al. · **CVPR 2026** · [Paper](https://arxiv.org/abs/2510.26782) · [Code](https://github.com/XiaFire/Clone_Deterministic_Environment) · [Project](https://xiafire.github.io/grwm-project-page/)

Earlier titles / aliases: Clone Deterministic 3D Worlds with Geometrically-Regularized World Models; Clone Deterministic 3D Worlds.

- **Method:** A temporal-context encoder and geometric regularization based on slowness and uniformity reshape the latent space before dynamics prediction. State-oracle comparisons and component ablations isolate representation quality from predictor capacity.
- **Evaluation:** Long-horizon rollouts are evaluated in deterministic environments with fixed rules. The experiments distinguish geometric regularization from the contribution of temporal context.
- **Related topics:** [Planning & Task-Relevant World Models](m4-knowledge-use.md) · [Evaluation & Benchmarks](m5-reliability.md)

<a id="paper-flowm"></a>
### Flow Equivariant World Models: Structured Memory for Dynamic Environments

Hansen Lillemark et al. · **ICML 2026** · [Paper](https://proceedings.mlr.press/v306/lillemark26a.html) · [Project](https://flowequivariantworldmodels.github.io/)

Earlier titles / aliases: Flow Equivariant World Models: Memory for Partially Observed Dynamic Environments.

- **Method:** A spatial latent memory stores observations in velocity channels that move with inferred object dynamics. An action-dependent transformation aligns this memory with the agent's motion, maintaining information about regions outside the current view.
- **Evaluation:** Partially observed 2D and 3D environments test long-horizon prediction, with a goal-directed planning task and representation probes in 3D Block World. The 3D encoder is learned rather than analytically equivariant; experiments examine temporal extrapolation in these environments.
- **Related topics:** [Planning & Task-Relevant World Models](m4-knowledge-use.md) · [World Model Interpretability](m8-interpretability.md)

## Method comparisons

Group Structure learns latent transformations and disentangled subspaces from interaction sequences. Group-Structured Latent Space supplies the symmetry and latent manifold; SEN learns an observation mapping compatible with a prescribed latent group action. GRWM regularizes geometry and temporal context for deterministic rollouts. FloWM maintains moving spatial memory under partial observability, with long-horizon prediction, probes, and a planning experiment. These methods make different assumptions about known transformations and the information available in each observation.

## Candidate papers

- [JEPA-Bisim: Learning Robust Visual Representations for Planning with Joint-Embedding Predictive World Models](../candidates.md#paper-jepa-bisim) · arXiv 2026

## Related topics

- [World Model Interpretability](m8-interpretability.md)
- [Generalization & Adaptation](m3-generalization.md)
- [Planning & Task-Relevant World Models](m4-knowledge-use.md)

[Back to paper index](../../README.md)

## Entries in related sections

<a id="paper-interpreting-physics"></a>
- [Interpreting Physics in Video World Models](m8-interpretability.md#paper-interpreting-physics)
<a id="paper-smds"></a>
- [Hypothesis-Driven Feature Manifold Analysis in LLMs via Supervised Multi-Dimensional Scaling](../supplementary.md#paper-smds)
<a id="paper-origins-manifolds"></a>
- [The Origins of Representation Manifolds in Large Language Models](../supplementary.md#paper-origins-manifolds)
<a id="paper-geoworld"></a>
- [GeoWorld: Geometric World Models](../supplementary.md#paper-geoworld)

<!-- END GENERATED RESEARCH MAP -->
