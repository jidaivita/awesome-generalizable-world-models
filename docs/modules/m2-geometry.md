<!-- BEGIN GENERATED RESEARCH MAP -->

[← Paper index](../../README.md#research-map) · [Reading guide](../reading-guide.md)

# Representation Geometry & Analysis

Latent geometry can be measured after training or imposed through the model architecture and objective. These papers connect geometric structure to physical variables, transition prediction, and procedural planning.

Language-model studies are included as analysis methods and labeled separately from physical world-model results.

## Approaches to geometry

| Approach | Papers | Evidence |
| :--- | :--- | :--- |
| Analyze learned representations | Interpreting Physics; SMDS; Origins of Representation Manifolds | Physical-variable probes, tests of geometric hypotheses, and theory of feature similarity; the latter two study language models |
| Regularize the representation | GRWM | State-oracle comparisons and ablations of geometric regularization in long-horizon prediction |
| Specify the latent manifold | Group-Structured Latent Space; GeoWorld | Symmetry-based transitions for control, and hyperbolic representations for procedural planning |

[Context and Diversity](m3-generalization.md#paper-context-diversity) and [Dynamics Are Learned](m3-generalization.md#paper-dynamics-geometries) connect representation structure to adaptation under environmental changes.

## Papers

<a id="paper-grwm"></a>
### Cloning Deterministic Worlds: The Critical Role of Latent Geometry in Long-Horizon World Models

Zaishuo Xia et al. · **CVPR 2026** · [Paper](https://arxiv.org/abs/2510.26782) · [Code](https://github.com/XiaFire/Clone_Deterministic_Environment) · [Project](https://xiafire.github.io/grwm-project-page/)

Earlier titles / aliases: Clone Deterministic 3D Worlds with Geometrically-Regularized World Models; Clone Deterministic 3D Worlds.

- **Method:** A temporal-context encoder and geometric regularization based on slowness and uniformity reshape the latent space before dynamics prediction. State-oracle comparisons and component ablations isolate representation quality from predictor capacity.
- **Evaluation:** Long-horizon rollouts are evaluated in deterministic environments with fixed rules. The experiments distinguish geometric regularization from the contribution of temporal context.
- **Related topics:** [Planning & Task-Relevant Representations](m4-knowledge-use.md) · [Evaluation & Sim-to-Real Transfer](m5-reliability.md)

<a id="paper-geoworld"></a>
### GeoWorld: Geometric World Models

Zeyu Zhang et al. · **CVPR 2026** · `Procedural planning` · [Paper](https://arxiv.org/abs/2602.23058) · [Project](https://steve-zeyu-zhang.github.io/GeoWorld/)

- **Method:** Hyperbolic JEPA embeds states on a hyperbolic manifold to represent hierarchical relations. Geometric Reinforcement Learning optimizes plans on the resulting energy landscape.
- **Evaluation:** CrossTask and COIN evaluate three- and four-step procedural visual planning. This setting tests sequences of instructional actions rather than continuous physical dynamics.
- **Related topics:** [Planning & Task-Relevant Representations](m4-knowledge-use.md)

<a id="paper-smds"></a>
### Hypothesis-Driven Feature Manifold Analysis in LLMs via Supervised Multi-Dimensional Scaling

Federico Tiblias et al. · **TMLR 2026** · `LLM analysis` · [Paper](https://arxiv.org/abs/2510.01025) · [Code](https://github.com/UKPLab/tmlr2026-manifold-analysis)

Earlier titles / aliases: Shape Happens: Automatic Feature Manifold Discovery in LLMs via Supervised Multi-Dimensional Scaling; Shape Happens.

- **Method:** Supervised Multi-Dimensional Scaling fits and compares candidate feature geometries, including circles, lines, and clusters. Temporal reasoning supplies a case study for testing how these structures change with context and support model outputs.
- **Evaluation:** Experiments examine language-model families and sizes, held-out examples, and representation interventions. This is an analysis method from language modeling, included for its relevance to testing geometric hypotheses.
- **Related topics:** [Planning & Task-Relevant Representations](m4-knowledge-use.md)

<a id="paper-interpreting-physics"></a>
### Interpreting Physics in Video World Models

Sonia Joseph et al. · **ICML 2026** · [Paper](https://proceedings.mlr.press/v306/joseph26a.html)

- **Method:** Layer-wise linear probes, patch-level decoding, subspace analysis, and attention ablations locate physical information in video encoders. Motion direction forms a circular population code spread over many linear directions, while speed and acceleration become accessible earlier.
- **Evaluation:** Probes and targeted steering characterize encoded physical variables and changes in decoded direction. These measurements concern representation geometry; they do not directly measure gains in closed-loop control.
- **Related topics:** [Planning & Task-Relevant Representations](m4-knowledge-use.md)

<a id="paper-group-latents"></a>
### Learning Abstract World Models with a Group-Structured Latent Space

Thomas Delliaux et al. · **arXiv 2025** · [Paper](https://arxiv.org/abs/2506.01529) · [Code](https://github.com/khanhvu207/world-models-group-latents)

- **Method:** Known symmetries determine the latent manifold and the group actions used for transitions. Additional latent variables retain information that does not follow the prescribed symmetry.
- **Evaluation:** Transition prediction and downstream reinforcement learning are tested in environments with translation and rotation, including first-person 3D views. The symmetry is supplied as prior knowledge.
- **Related topics:** [Object-Centric & Relational Models](m1-structure.md)

<a id="paper-origins-manifolds"></a>
### The Origins of Representation Manifolds in Large Language Models

Alexander Modell et al. · **arXiv 2025** · `LLM analysis` · [Paper](https://arxiv.org/abs/2505.18235)

- **Method:** A theoretical model connects cosine similarity between representations to distances along an underlying feature manifold. It extends a binary feature-direction account to continuous, multidimensional features.
- **Evaluation:** The paper tests its assumptions and predictions on text embeddings and language-model token activations. Its conclusions depend on the stated generative assumptions for those representations.

## Method comparisons

Interpreting Physics and SMDS measure structure in trained representations, while Origins of Representation Manifolds derives a model of feature similarity. GRWM changes the training objective to improve rollout accuracy; Group-Structured Latent Space and GeoWorld choose non-Euclidean structure before learning. These are different roles for geometry: an observed property, a regularizer, or an architectural constraint.

## Related topics

- [Generalization & Context-Based Adaptation](m3-generalization.md)
- [Planning & Task-Relevant Representations](m4-knowledge-use.md)
- [Predictive Architectures & Pretraining](m7-scaling.md)

[Paper-note template](../../templates/paper-note.md) · [Comparison template](../../templates/comparison-note.md) · [Back to overview ↑](../../README.md)

<!-- END GENERATED RESEARCH MAP -->
