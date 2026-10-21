<!-- BEGIN GENERATED RESEARCH MAP -->

[← Paper index](../../README.md#research-map) · [Reading guide](../reading-guide.md) · [Supplementary reading](../supplementary.md)

# Representation Geometry & Symmetry

Geometric structure determines how states and transitions are represented in latent space. These papers study regularization for long-horizon prediction and symmetry-based constraints on learned dynamics.

Observed geometry, imposed symmetry, and improved rollout accuracy are distinct claims. Physical-variable probing is covered under World Model Interpretability; language-model geometry and procedural planning appear in Supplementary Reading.

## Geometric regularization and symmetry priors

<a id="paper-grwm"></a>
### Cloning Deterministic Worlds: The Critical Role of Latent Geometry in Long-Horizon World Models

Zaishuo Xia et al. · **CVPR 2026** · [Paper](https://arxiv.org/abs/2510.26782) · [Code](https://github.com/XiaFire/Clone_Deterministic_Environment) · [Project](https://xiafire.github.io/grwm-project-page/)

Earlier titles / aliases: Clone Deterministic 3D Worlds with Geometrically-Regularized World Models; Clone Deterministic 3D Worlds.

- **Method:** A temporal-context encoder and geometric regularization based on slowness and uniformity reshape the latent space before dynamics prediction. State-oracle comparisons and component ablations isolate representation quality from predictor capacity.
- **Evaluation:** Long-horizon rollouts are evaluated in deterministic environments with fixed rules. The experiments distinguish geometric regularization from the contribution of temporal context.
- **Related topics:** [Planning & Task-Relevant World Models](m4-knowledge-use.md) · [Evaluation & Benchmarks](m5-reliability.md)

<a id="paper-group-latents"></a>
### Learning Abstract World Models with a Group-Structured Latent Space

Thomas Delliaux et al. · **arXiv 2025** · [Paper](https://arxiv.org/abs/2506.01529) · [Code](https://github.com/khanhvu207/world-models-group-latents)

- **Method:** Known symmetries determine the latent manifold and the group actions used for transitions. Additional latent variables retain information that does not follow the prescribed symmetry.
- **Evaluation:** Transition prediction and downstream reinforcement learning are tested in environments with translation and rotation, including first-person 3D views. The symmetry is supplied as prior knowledge.
- **Related topics:** [Structured & Compositional Representations](m1-structure.md)

## Method comparisons

GRWM regularizes an encoder using geometric information and temporal context to improve deterministic rollouts. Group-Structured Latent Space specifies a symmetry-based latent manifold and transition operations. Dynamics Are Learned, listed under Generalization & Adaptation, instead shapes an inferred context embedding to support policies under dynamics shifts.

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
