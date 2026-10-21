<!-- BEGIN GENERATED RESEARCH MAP -->

[← Paper index](../../README.md#research-map) · [Reading guide](../reading-guide.md) · [Supplementary reading](../supplementary.md)

# Evaluation & Benchmarks

Evaluation protocols expose failures that average prediction scores can hide. These papers test physical-law extrapolation, combinations absent from training, and action-conditioned world models used in closed-loop tasks.

Results depend on the training distribution, the tested change, the information available at deployment, and the measured outcome. Simulation-based policy evaluation is linked separately in Supplementary Reading.

## Physical prediction and closed-loop tasks

<a id="paper-physical-law-perspective"></a>
### How Far Is Video Generation from World Model: A Physical Law Perspective

Bingyi Kang et al. · **ICML 2025** · [Paper](https://proceedings.mlr.press/v267/kang25g.html)

- **Method:** Diffusion video models are trained on a deterministic 2D testbed of motion and collisions. Separate splits test interpolation, extrapolation, and new combinations of familiar physical factors.
- **Evaluation:** Scaling improves in-distribution and some combinatorial predictions, while the tested models struggle with out-of-distribution physical scenarios. Additional experiments examine which appearance and motion factors drive case-based predictions.
- **Related topics:** [Generalization & Adaptation](m3-generalization.md)

<a id="paper-world-in-world"></a>
### World-In-World: World Models in a Closed-Loop World

Jiahan Zhang et al. · **ICLR 2026** · [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/5b4263be85820683d78675cc18d2efc7-Abstract-Conference.html)

- **Method:** A shared action interface and online planning strategy connect heterogeneous world models to closed-loop environments. This makes task outcomes comparable across models with different generation interfaces.
- **Evaluation:** Four environments measure task success and examine action-conditioned post-training data and inference-time computation. The study contrasts these results with open-loop visual-quality measures.
- **Related topics:** [Planning & Task-Relevant World Models](m4-knowledge-use.md)

## Method comparisons

A Physical Law Perspective isolates interpolation, extrapolation, and compositional physical prediction. World-In-World evaluates action-conditioned models in closed-loop tasks while varying post-training data and test-time computation. The former diagnoses prediction under distribution shift; the latter measures consequences for interaction.

## Related topics

- [Generalization & Adaptation](m3-generalization.md)
- [Planning & Task-Relevant World Models](m4-knowledge-use.md)
- [World Model Interpretability](m8-interpretability.md)

[Back to paper index](../../README.md)

## Entries in related sections

<a id="paper-simpler"></a>
- [Evaluating Real-World Robot Manipulation Policies in Simulation](../supplementary.md#paper-simpler)
<a id="paper-rethinking-sim2real"></a>
- [Rethinking Sim2Real: Lower Fidelity Simulation Leads to Higher Sim2Real Transfer in Navigation](../supplementary.md#paper-rethinking-sim2real)

<!-- END GENERATED RESEARCH MAP -->
