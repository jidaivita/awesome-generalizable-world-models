<!-- BEGIN GENERATED RESEARCH MAP -->

[← Research map](../../README.md#research-map) · [Reading route](../reading-guide.md)

# M1 · Structure & Invariance

> Which objects, relations, and stable structures should a model represent?

Start with objects and relations: how can a model turn complex observations into structure useful for dynamics prediction? Ask whether that structure comes from architecture, learning objectives, or data, and under which changes it remains useful.

This module studies representational content and inductive biases. M2 examines its latent organization; M4 examines its actual use.

## Where to start

1. **[Neural Relational Inference for Interacting Systems](#paper-nri)** — Infers latent interaction graphs from trajectories with a graph-based dynamics decoder.
2. **[Contrastive Learning of Structured World Models](#paper-cswm)** — Learns object-centric representations and relational dynamics with a contrastive objective.

## Papers and reading pointers

<a id="paper-causal-jepa"></a>
### Causal-JEPA: Learning World Models through Object-Level Latent Masking

**ICML 2026** · [Paper](https://proceedings.mlr.press/v306/nam26c.html) · [Code](https://github.com/galilai-group/cjepa)

Combines object-level latent masking with joint-embedding predictive learning.

- **Read for:** How object-level latent masking creates structured partial observability and affects the use of relational information.
- **Scope:** Latent masking is not automatically an intervention on a real physical causal mechanism.
- **Connect to:** [M4 · Knowledge Use & Task Abstraction](m4-knowledge-use.md)

<a id="paper-cswm"></a>
### Contrastive Learning of Structured World Models

**ICLR 2020** · [Paper](https://arxiv.org/abs/1911.12247)

Learns object-centric representations and relational dynamics with a contrastive objective.

- **Read for:** The distinct roles of object representations, relational dynamics, and the contrastive objective.
- **Scope:** Success on structured benchmarks does not establish open-world compositional generalization.
- **Connect to:** [M4 · Knowledge Use & Task Abstraction](m4-knowledge-use.md)

<a id="paper-nri"></a>
### Neural Relational Inference for Interacting Systems

**ICML 2018** · [Paper](https://proceedings.mlr.press/v80/kipf18a.html)

Infers latent interaction graphs from trajectories with a graph-based dynamics decoder.

- **Read for:** The latent graph, the graph-based dynamics decoder, and whether relation recovery agrees with predictive performance.
- **Scope:** Recovering relations from observations does not establish causal identification under arbitrary conditions.
- **Connect to:** [M4 · Knowledge Use & Task Abstraction](m4-knowledge-use.md)

<a id="paper-spartan"></a>
### SPARTAN: A Sparse Transformer World Model Attending to What Matters

**NeurIPS 2025** · [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e2c33c1753e1f1924f5560b11fc4444f-Abstract-Conference.html)

Uses sparse, context-dependent interactions to adapt to changes in mechanisms.

- **Read for:** Sparse attention, intervention settings, few-shot adaptation, and the priors available to the model.
- **Scope:** Interpret generalization results in the context of sparse mechanism changes and object-centric assumptions.
- **Connect to:** [M3 · Generalization & In-Context Learning](m3-generalization.md)

## Read together

NRI and C-SWM offer entry points through interaction graphs and object representations. SPARTAN and Causal-JEPA connect structural choices to adaptation or latent prediction. Compare how object information is obtained, whether structure changes with context, and whether recovered relations improve prediction.

## Continue exploring

- [M2 · Representation Geometry & Manifolds](m2-geometry.md) — How is knowledge organized in latent space, and what does that organization do?
- [M3 · Generalization & In-Context Learning](m3-generalization.md) — Does success in a new environment come from knowledge reuse or learning new dynamics?
- [M4 · Knowledge Use & Task Abstraction](m4-knowledge-use.md) — Which information actually supports prediction, planning, and decisions?

[Paper-note template](../../templates/paper-note.md) · [Comparison template](../../templates/comparison-note.md) · [Back to overview ↑](../../README.md)

<!-- END GENERATED RESEARCH MAP -->
