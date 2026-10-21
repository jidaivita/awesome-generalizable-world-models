<!-- BEGIN GENERATED RESEARCH MAP -->

[← Paper index](../../README.md#research-map) · [Reading guide](../reading-guide.md)

# Representation Geometry & Analysis

The papers examine geometry that emerges during training and geometry imposed through model design. They relate latent structure to physical variables, prediction error, and planning performance.

Emergent geometry, imposed geometry, and task benefits are distinct claims. A projection can suggest a hypothesis; additional evidence is needed to establish its role.

## Three lines of inquiry

| Line of inquiry | Papers | Key distinction |
| :--- | :--- | :--- |
| Emergent geometry and function | Interpreting Physics, SMDS, Origins | Observed structure, competing hypotheses, and functional evidence |
| Geometric priors and dynamics learning | GRWM, Group-Structured Latent Space, GeoWorld | Where the prior comes from and what it independently contributes |
| Geometry and adaptation | [Context and Diversity](m3-generalization.md#paper-context-diversity), [Dynamics Are Learned](m3-generalization.md#paper-dynamics-geometries) | Environment shifts, trajectory information, and transferable structure |

**Methods used in these studies:** PCA/SVD, linear probes, periodic-variable encodings, subspace comparisons, interventions, held-out evaluation, intrinsic-dimension estimation, and Riemannian optimization.

For example, `z(θ) = (cos θ, sin θ, cos 2θ, sin 2θ, …)` has one underlying degree of freedom while spanning multiple linear directions. Physical degrees of freedom, vector dimension, linear span, intrinsic manifold dimension, and the number of intervention directions are different quantities. This is a mathematical illustration, not a measurement from a trained model.

## Papers

<a id="paper-grwm"></a>
### Cloning Deterministic Worlds: The Critical Role of Latent Geometry in Long-Horizon World Models

Zaishuo Xia et al. · **CVPR 2026** · [Paper](https://arxiv.org/abs/2510.26782) · [Code](https://github.com/XiaFire/Clone_Deterministic_Environment) · [Project](https://xiafire.github.io/grwm-project-page/)

Earlier titles / aliases: Clone Deterministic 3D Worlds with Geometrically-Regularized World Models; Clone Deterministic 3D Worlds.

Regularizes latent geometry and uses temporal context for long-horizon prediction in deterministic environments.

- **Method and analysis:** Ground-truth state oracle comparisons, temporal-context encoders, slowness and uniformity regularization, and the corresponding ablations.
- **Evaluation scope:** Evaluated in deterministic environments with fixed rules, with separate ablations for geometric regularization and temporal context.
- **Related topics:** [Planning & Task-Relevant Representations](m4-knowledge-use.md) · [Evaluation & Sim-to-Real Transfer](m5-reliability.md)

<a id="paper-geoworld"></a>
### GeoWorld: Geometric World Models

Zeyu Zhang et al. · **CVPR 2026** · [Paper](https://arxiv.org/abs/2602.23058) · [Project](https://steve-zeyu-zhang.github.io/GeoWorld/)

Uses hyperbolic latent representations and geometric optimization for procedural planning on CrossTask and COIN.

- **Method and analysis:** The separate contributions of Hyperbolic JEPA and geometric optimization, including matched Euclidean comparisons.
- **Evaluation scope:** The main tasks are multi-step procedural visual planning on CrossTask and COIN, rather than continuous physical dynamics or demonstrated real-robot transfer.
- **Related topics:** [Planning & Task-Relevant Representations](m4-knowledge-use.md)

<a id="paper-smds"></a>
### Hypothesis-Driven Feature Manifold Analysis in LLMs via Supervised Multi-Dimensional Scaling

Federico Tiblias et al. · **TMLR 2026** · [Paper](https://arxiv.org/abs/2510.01025) · [Code](https://github.com/UKPLab/tmlr2026-manifold-analysis)

Earlier titles / aliases: Shape Happens: Automatic Feature Manifold Discovery in LLMs via Supervised Multi-Dimensional Scaling; Shape Happens.

Compares geometric hypotheses and their functional effects in language-model representations.

- **Method and analysis:** How SMDS uses supervision to compare circular, linear, and clustered hypotheses; held-out evaluation and intervention evidence.
- **Evaluation scope:** This is supervised, hypothesis-driven analysis, not discovery without priors. Its LLM results are not established findings about world models.
- **Related topics:** [Planning & Task-Relevant Representations](m4-knowledge-use.md)

<a id="paper-interpreting-physics"></a>
### Interpreting Physics in Video World Models

Sonia Joseph et al. · **ICML 2026** · [Paper](https://proceedings.mlr.press/v306/joseph26a.html)

Analyzes the organization of physical information through layer-wise probes, subspaces, and interventions.

- **Method and analysis:** Layer-wise differences in speed and direction; circular population codes; what probes, attention ablations, and directional steering each establish.
- **Evaluation scope:** Changing a decoded direction does not establish improved native prediction or planning. Linear subspace dimension and intrinsic manifold dimension are different quantities.
- **Related topics:** [Planning & Task-Relevant Representations](m4-knowledge-use.md)

<a id="paper-group-latents"></a>
### Learning Abstract World Models with a Group-Structured Latent Space

Thomas Delliaux et al. · **arXiv 2025** · [Paper](https://arxiv.org/abs/2506.01529) · [Code](https://github.com/khanhvu207/world-models-group-latents)

Encodes known symmetries, such as translation and rotation, as geometric inductive biases.

- **Method and analysis:** How group actions correspond to latent transitions and how structured and unstructured information coexist.
- **Evaluation scope:** Using known symmetries is different from discovering physical laws from data.
- **Related topics:** [Object-Centric & Relational Models](m1-structure.md)

<a id="paper-origins-manifolds"></a>
### The Origins of Representation Manifolds in Large Language Models

Alexander Modell et al. · **arXiv 2025** · [Paper](https://arxiv.org/abs/2505.18235)

Relates similarities in learned representations to intrinsic conceptual geometry under a generative model.

- **Method and analysis:** The generative assumptions, the relation between cosine similarity and intrinsic geometry, and testable predictions.
- **Evaluation scope:** The results rely on explicit assumptions about text representations; they are not universal laws for arbitrary networks or world models.

## Method comparisons

Interpreting Physics analyzes physical information in video-model representations. SMDS compares supervised geometric hypotheses in language models; GRWM regularizes latent geometry for prediction. The Origins of Representation Manifolds supplies a theoretical account of geometry in text representations.

## Related topics

- [Generalization & Context-Based Adaptation](m3-generalization.md)
- [Planning & Task-Relevant Representations](m4-knowledge-use.md)
- [Predictive Architectures & Pretraining](m7-scaling.md)

[Paper-note template](../../templates/paper-note.md) · [Comparison template](../../templates/comparison-note.md) · [Back to overview ↑](../../README.md)

<!-- END GENERATED RESEARCH MAP -->
