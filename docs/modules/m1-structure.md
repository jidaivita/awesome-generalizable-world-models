<!-- BEGIN GENERATED RESEARCH MAP -->

[← Paper index](../../README.md#research-map) · [Reading guide](../reading-guide.md)

# Object-Centric & Relational Models

Object-centric representations and interaction graphs encode structure for dynamics prediction. The papers examine how this structure is learned and which architectural or training assumptions support it.

Object decomposition, interaction graphs, and sparse attention provide different structural assumptions for dynamics prediction.

## Papers

<a id="paper-causal-jepa"></a>
### Causal-JEPA: Learning World Models through Object-Level Latent Masking

Heejeong Nam et al. · **ICML 2026** · [Paper](https://proceedings.mlr.press/v306/nam26c.html) · [Code](https://github.com/galilai-group/cjepa)

Combines object-level latent masking with joint-embedding predictive learning.

- **Method and analysis:** How object-level latent masking creates structured partial observability and affects the use of relational information.
- **Evaluation scope:** Latent masking is not automatically an intervention on a real physical causal mechanism.
- **Related topics:** [Planning & Task-Relevant Representations](m4-knowledge-use.md)

<a id="paper-cswm"></a>
### Contrastive Learning of Structured World Models

Thomas Kipf et al. · **ICLR 2020** · [Paper](https://arxiv.org/abs/1911.12247)

Learns object-centric representations and relational dynamics with a contrastive objective.

- **Method and analysis:** The distinct roles of object representations, relational dynamics, and the contrastive objective.
- **Evaluation scope:** Success on structured benchmarks does not establish open-world compositional generalization.
- **Related topics:** [Planning & Task-Relevant Representations](m4-knowledge-use.md)

<a id="paper-nri"></a>
### Neural Relational Inference for Interacting Systems

Thomas Kipf et al. · **ICML 2018** · [Paper](https://proceedings.mlr.press/v80/kipf18a.html)

Infers latent interaction graphs from trajectories with a graph-based dynamics decoder.

- **Method and analysis:** The latent graph, the graph-based dynamics decoder, and whether relation recovery agrees with predictive performance.
- **Evaluation scope:** Recovering relations from observations does not establish causal identification under arbitrary conditions.
- **Related topics:** [Planning & Task-Relevant Representations](m4-knowledge-use.md)

<a id="paper-spartan"></a>
### SPARTAN: A Sparse Transformer World Model Attending to What Matters

Anson Lei et al. · **NeurIPS 2025** · [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e2c33c1753e1f1924f5560b11fc4444f-Abstract-Conference.html)

Uses sparse, context-dependent interactions to adapt to changes in mechanisms.

- **Method and analysis:** Sparse attention, intervention settings, few-shot adaptation, and the priors available to the model.
- **Evaluation scope:** Generalization is evaluated under sparse mechanism changes with object-centric modeling assumptions.
- **Related topics:** [Generalization & Context-Based Adaptation](m3-generalization.md)

## Method comparisons

NRI infers interaction graphs, while C-SWM learns object representations with a contrastive objective. SPARTAN uses sparse attention; Causal-JEPA masks object-level latents. These methods differ in how object information is obtained and how relations enter the predictor.

## Related topics

- [Representation Geometry & Analysis](m2-geometry.md)
- [Generalization & Context-Based Adaptation](m3-generalization.md)
- [Planning & Task-Relevant Representations](m4-knowledge-use.md)

[Paper-note template](../../templates/paper-note.md) · [Comparison template](../../templates/comparison-note.md) · [Back to overview ↑](../../README.md)

<!-- END GENERATED RESEARCH MAP -->
