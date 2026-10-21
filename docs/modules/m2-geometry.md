<!-- BEGIN GENERATED RESEARCH MAP -->

[← Research map](../../README.md#research-map) · [Reading route](../reading-guide.md)

# M2 · Representation Geometry & Manifolds

> How is knowledge organized in latent space, and what does that organization do?

Study both the geometry that trained models develop and the effects of deliberately imposing geometric structure. Identify which question a paper addresses before connecting a geometric observation to model behavior.

Emergent geometry, imposed geometry, and task benefits are distinct claims. A projection can suggest a hypothesis; additional evidence is needed to establish its role.

## Where to start

1. **[Interpreting Physics](#paper-interpreting-physics)** — Analyzes the organization of physical information through layer-wise probes, subspaces, and interventions.
2. **[SMDS / Shape Happens](#paper-smds)** — Compares geometric hypotheses and their functional effects in language-model representations.
3. **[GRWM](#paper-grwm)** — Connects representation geometry and temporal context to long-horizon prediction error.

## Three lines of inquiry

| Line of inquiry | Papers | Key distinction |
| :--- | :--- | :--- |
| Emergent geometry and function | Interpreting Physics, SMDS, Origins | Observed structure, competing hypotheses, and functional evidence |
| Geometric priors and dynamics learning | GRWM, Group-Structured Latent Space, GeoWorld | Where the prior comes from and what it independently contributes |
| Geometry and adaptation | [Context and Diversity](m3-generalization.md#paper-context-diversity), [Dynamics Are Learned](m3-generalization.md#paper-dynamics-geometries) | Environment shifts, trajectory information, and transferable structure |

**Methods used in these studies:** PCA/SVD, linear probes, periodic-variable encodings, subspace comparisons, interventions, held-out evaluation, intrinsic-dimension estimation, and Riemannian optimization.

For example, `z(θ) = (cos θ, sin θ, cos 2θ, sin 2θ, …)` has one underlying degree of freedom while spanning multiple linear directions. Physical degrees of freedom, vector dimension, linear span, intrinsic manifold dimension, and the number of intervention directions are different quantities. This is a mathematical illustration, not a measurement from a trained model.

## Papers and reading pointers

<a id="paper-grwm"></a>
### Cloning Deterministic Worlds: The Critical Role of Latent Geometry in Long-Horizon World Models

**CVPR 2026** · [Paper](https://arxiv.org/abs/2510.26782) · [Code](https://github.com/XiaFire/Clone_Deterministic_Environment) · [Project](https://xiafire.github.io/grwm-project-page/)

Earlier titles / aliases: Clone Deterministic 3D Worlds with Geometrically-Regularized World Models; Clone Deterministic 3D Worlds.

Connects representation geometry and temporal context to long-horizon prediction error.

- **Read for:** Ground-truth state oracle comparisons, temporal-context encoders, slowness and uniformity regularization, and the corresponding ablations.
- **Scope:** The main evidence concerns deterministic environments with fixed rules. Separate geometric regularization from history-based disambiguation; neither establishes general open-world robustness.
- **Connect to:** [M4 · Knowledge Use & Task Abstraction](m4-knowledge-use.md) · [M5 · Reliability & Sim2Real](m5-reliability.md)

<a id="paper-geoworld"></a>
### GeoWorld: Geometric World Models

**CVPR 2026** · [Paper](https://arxiv.org/abs/2602.23058) · [Project](https://steve-zeyu-zhang.github.io/GeoWorld/)

Studies non-Euclidean latent spaces and geometric optimization for procedural visual planning.

- **Read for:** The separate contributions of Hyperbolic JEPA and geometric optimization, including matched Euclidean comparisons.
- **Scope:** The main tasks are multi-step procedural visual planning on CrossTask and COIN, rather than continuous physical dynamics or demonstrated real-robot transfer.
- **Connect to:** [M4 · Knowledge Use & Task Abstraction](m4-knowledge-use.md)

<a id="paper-smds"></a>
### Hypothesis-Driven Feature Manifold Analysis in LLMs via Supervised Multi-Dimensional Scaling

**TMLR 2026** · [Paper](https://arxiv.org/abs/2510.01025) · [Code](https://github.com/UKPLab/tmlr2026-manifold-analysis)

Earlier titles / aliases: Shape Happens: Automatic Feature Manifold Discovery in LLMs via Supervised Multi-Dimensional Scaling; Shape Happens.

Compares geometric hypotheses and their functional effects in language-model representations.

- **Read for:** How SMDS uses supervision to compare circular, linear, and clustered hypotheses; held-out evaluation and intervention evidence.
- **Scope:** This is supervised, hypothesis-driven analysis, not discovery without priors. Its LLM results are not established findings about world models.
- **Connect to:** [M4 · Knowledge Use & Task Abstraction](m4-knowledge-use.md)

<a id="paper-interpreting-physics"></a>
### Interpreting Physics in Video World Models

**ICML 2026** · [Paper](https://proceedings.mlr.press/v306/joseph26a.html)

Analyzes the organization of physical information through layer-wise probes, subspaces, and interventions.

- **Read for:** Layer-wise differences in speed and direction; circular population codes; what probes, attention ablations, and directional steering each establish.
- **Scope:** Changing a decoded direction does not establish improved native prediction or planning. Linear subspace dimension and intrinsic manifold dimension are different quantities.
- **Connect to:** [M4 · Knowledge Use & Task Abstraction](m4-knowledge-use.md)

<a id="paper-group-latents"></a>
### Learning Abstract World Models with a Group-Structured Latent Space

**arXiv 2025** · [Paper](https://arxiv.org/abs/2506.01529) · [Code](https://github.com/khanhvu207/world-models-group-latents)

Encodes known symmetries, such as translation and rotation, as geometric inductive biases.

- **Read for:** How group actions correspond to latent transitions and how structured and unstructured information coexist.
- **Scope:** Using known symmetries is different from discovering physical laws from data.
- **Connect to:** [M1 · Structure & Invariance](m1-structure.md)

<a id="paper-origins-manifolds"></a>
### The Origins of Representation Manifolds in Large Language Models

**arXiv 2025** · [Paper](https://arxiv.org/abs/2505.18235)

Relates similarities in learned representations to intrinsic conceptual geometry under a generative model.

- **Read for:** The generative assumptions, the relation between cosine similarity and intrinsic geometry, and testable predictions.
- **Scope:** The results rely on explicit assumptions about text representations; they are not universal laws for arbitrary networks or world models.

## Read together

Interpreting Physics provides an entry point into physical information in representations; SMDS offers a method for comparing geometric hypotheses; GRWM connects diagnosis to long-horizon prediction. Read them together while keeping their model families, supervision, and functional evidence distinct.

## Continue exploring

- [M3 · Generalization & In-Context Learning](m3-generalization.md) — Does success in a new environment come from knowledge reuse or learning new dynamics?
- [M4 · Knowledge Use & Task Abstraction](m4-knowledge-use.md) — Which information actually supports prediction, planning, and decisions?
- [M7 · Pretraining & Scaling](m7-scaling.md) — How do controlled insights connect to stronger models and larger datasets?

[Paper-note template](../../templates/paper-note.md) · [Comparison template](../../templates/comparison-note.md) · [Back to overview ↑](../../README.md)

<!-- END GENERATED RESEARCH MAP -->
