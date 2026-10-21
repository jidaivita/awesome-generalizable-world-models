<!-- BEGIN GENERATED RESEARCH MAP -->

[← Paper index](../../README.md#research-map) · [Reading guide](../reading-guide.md)

# Evaluation & Sim-to-Real Transfer

Evaluation protocols determine whether a model supports reliable decisions beyond its training conditions. These papers test physical extrapolation, closed-loop task performance, and agreement between simulated and real policy outcomes.

The unit of evaluation ranges from a predicted trajectory to a complete policy; the comparisons make those differences explicit.

## Papers

<a id="paper-simpler"></a>
### Evaluating Real-World Robot Manipulation Policies in Simulation

Xuanlin Li et al. · **CoRL 2024 (proceedings 2025)** · [Paper](https://proceedings.mlr.press/v270/li25c.html)

Earlier titles / aliases: SIMPLER.

- **Method:** The benchmark reduces visual and control differences between real and simulated manipulation setups, then evaluates the same policies in both. Its goal is to reproduce policy comparisons and responses to distribution shifts.
- **Evaluation:** More than 1,500 paired evaluations span two robot embodiments and eight task families. The reported evidence is agreement in real and simulated policy performance, rather than training a transferable dynamics model.
- **Related topics:** [Planning & Task-Relevant Representations](m4-knowledge-use.md)

<a id="paper-physical-law-perspective"></a>
### How Far Is Video Generation from World Model: A Physical Law Perspective

Bingyi Kang et al. · **ICML 2025** · [Paper](https://proceedings.mlr.press/v267/kang25g.html)

- **Method:** Diffusion video models are trained on a deterministic 2D testbed of motion and collisions. Separate splits test interpolation, extrapolation, and new combinations of familiar physical factors.
- **Evaluation:** Scaling improves in-distribution and some combinatorial predictions, while the tested models struggle with out-of-distribution physical scenarios. Additional experiments examine which appearance and motion factors drive case-based predictions.
- **Related topics:** [Generalization & Context-Based Adaptation](m3-generalization.md)

<a id="paper-rethinking-sim2real"></a>
### Rethinking Sim2Real: Lower Fidelity Simulation Leads to Higher Sim2Real Transfer in Navigation

Joanne Truong et al. · **CoRL 2022 (proceedings 2023)** · [Paper](https://proceedings.mlr.press/v205/truong23a.html)

- **Method:** A controlled comparison varies simulator fidelity for visual-navigation policy learning. Simple robot-motion models fitted to real data are compared with more detailed simulation physics.
- **Evaluation:** Habitat and iGibson experiments, followed by tests on A1, AlienGo, and Spot robots, examine learning speed, overfitting to simulator errors, and real-world navigation performance.
- **Related topics:** [Generalization & Context-Based Adaptation](m3-generalization.md)

<a id="paper-world-in-world"></a>
### World-In-World: World Models in a Closed-Loop World

Jiahan Zhang et al. · **ICLR 2026** · [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/5b4263be85820683d78675cc18d2efc7-Abstract-Conference.html)

- **Method:** A shared action interface and online planning strategy connect heterogeneous world models to closed-loop environments. This makes task outcomes comparable across models with different generation interfaces.
- **Evaluation:** Four environments measure task success and examine action-conditioned post-training data and inference-time computation. The study contrasts these results with open-loop visual-quality measures.
- **Related topics:** [Planning & Task-Relevant Representations](m4-knowledge-use.md) · [Predictive Architectures & Pretraining](m7-scaling.md)

## Method comparisons

SIMPLER holds policies fixed and tests agreement between simulated and real evaluations; Rethinking Sim2Real changes the simulator used for policy training and measures transfer. Physical Law Perspective tests predicted motion on controlled distribution shifts. World-In-World evaluates the full model-and-planner loop through task success.

## Related topics

- [Generalization & Context-Based Adaptation](m3-generalization.md)
- [Planning & Task-Relevant Representations](m4-knowledge-use.md)
- [Predictive Architectures & Pretraining](m7-scaling.md)

[Paper-note template](../../templates/paper-note.md) · [Comparison template](../../templates/comparison-note.md) · [Back to overview ↑](../../README.md)

<!-- END GENERATED RESEARCH MAP -->
