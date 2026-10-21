<!-- BEGIN GENERATED RESEARCH MAP -->

[← Paper index](../../README.md#research-map) · [Reading guide](../reading-guide.md) · [Supplementary reading](../supplementary.md)

# Structured & Compositional Representations

Object and relation structure factorizes a world model into entities and interactions. These methods infer interaction graphs, learn object-specific visual features, or restrict which components participate in a transition.

Structure may be supplied by the input, learned from observations, or encouraged by a prediction objective. Relation recovery and compositional transfer are reported as separate outcomes.

## Objects and interaction mechanisms

<a id="paper-causal-jepa"></a>
### Causal-JEPA: Learning World Models through Object-Level Latent Masking

Heejeong Nam et al. · **ICML 2026** · [Paper](https://proceedings.mlr.press/v306/nam26c.html) · [Code](https://github.com/galilai-group/cjepa)

- **Method:** The predictor reconstructs masked object embeddings from the remaining object context. This training objective limits direct access to the target object and makes relational information useful for prediction.
- **Evaluation:** Visual question answering tests counterfactual reasoning, while control experiments compare planning with object-level and patch-level latent inputs. The structured partial observability comes from training-time masking.
- **Related topics:** [Planning & Task-Relevant World Models](m4-knowledge-use.md)

<a id="paper-cswm"></a>
### Contrastive Learning of Structured World Models

Thomas Kipf et al. · **ICLR 2020** · [Paper](https://arxiv.org/abs/1911.12247)

- **Method:** Each image is encoded as a set of object embeddings. A graph neural network predicts their transitions, trained with a contrastive loss that separates predicted future states from negative samples instead of reconstructing pixels.
- **Evaluation:** Evaluations cover independently manipulated objects, simple Atari games, and multi-object physics simulations, comparing structured latent predictions with reconstruction-based models.
- **Related topics:** [Planning & Task-Relevant World Models](m4-knowledge-use.md)

<a id="paper-nri"></a>
### Neural Relational Inference for Interacting Systems

Thomas Kipf et al. · **ICML 2018** · [Paper](https://proceedings.mlr.press/v80/kipf18a.html)

- **Method:** A variational encoder infers a latent interaction graph from observed trajectories; a graph neural network decoder predicts how the interacting entities move. The graph and dynamics are learned jointly without relation labels.
- **Evaluation:** Tests recover known interactions in simulated physical systems and predict trajectories in motion-capture and sports-tracking data. Relation recovery is evaluated where a reference graph is available.
- **Related topics:** [Planning & Task-Relevant World Models](m4-knowledge-use.md)

<a id="paper-spartan"></a>
### SPARTAN: A Sparse Transformer World Model Attending to What Matters

Anson Lei et al. · **NeurIPS 2025** · [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e2c33c1753e1f1924f5560b11fc4444f-Abstract-Conference.html)

- **Method:** Sparsity regularization on attention between object-factored tokens produces context-dependent interaction graphs. An adaptation procedure updates the model after sparse changes to environmental mechanisms with unknown intervention targets.
- **Evaluation:** Observation-based environments test interaction-graph recovery, few-shot adaptation to dynamics changes, and robustness to distractors under the object-centric modeling setup.
- **Related topics:** [Generalization & Adaptation](m3-generalization.md)

## Method comparisons

NRI infers relations between observed entities. C-SWM learns object embeddings and relational transitions from pixels. SPARTAN sparsifies context-dependent interactions to adapt to mechanism changes. Causal-JEPA makes missing object-level information the prediction target. HOWM and WM3C, listed under Generalization & Adaptation, directly evaluate how composable dynamics support new configurations or environments.

## Related topics

- [Generalization & Adaptation](m3-generalization.md)
- [World Model Interpretability](m8-interpretability.md)
- [Representation Geometry & Symmetry](m2-geometry.md)

[Back to paper index](../../README.md)

<!-- END GENERATED RESEARCH MAP -->
