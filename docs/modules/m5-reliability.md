<!-- BEGIN GENERATED RESEARCH MAP -->

[← Paper index](../../README.md#research-map) · [Reading guide](../reading-guide.md)

# Evaluation & Sim-to-Real Transfer

Visual quality, physical accuracy, and task performance measure different aspects of reliability. The papers study physical extrapolation, closed-loop evaluation, and paired real and simulated policy tests.

Performance within simulation, agreement in real-world policy rankings, and successful transfer are different forms of evidence.

## Papers

<a id="paper-simpler"></a>
### Evaluating Real-World Robot Manipulation Policies in Simulation

Xuanlin Li et al. · **CoRL 2024 (proceedings 2025)** · [Paper](https://proceedings.mlr.press/v270/li25c.html)

Earlier titles / aliases: SIMPLER.

Evaluates whether simulation reliably predicts the relative performance of real-world manipulation policies.

- **Method and analysis:** Paired real and simulated evaluations, policy rankings, visual matching, and variant aggregation.
- **Evaluation scope:** Perturbations within simulation alone do not demonstrate a reduced reality gap.
- **Related topics:** [Planning & Task-Relevant Representations](m4-knowledge-use.md)

<a id="paper-physical-law-perspective"></a>
### How Far Is Video Generation from World Model: A Physical Law Perspective

Bingyi Kang et al. · **ICML 2025** · [Paper](https://proceedings.mlr.press/v267/kang25g.html)

Tests physical prediction under extrapolation and compositional distribution shifts.

- **Method and analysis:** How distribution shifts are constructed and whether visual-quality metrics obscure physical successes or failures.
- **Evaluation scope:** The findings concern the tested models and datasets, rather than universal limitations of all video models.
- **Related topics:** [Generalization & Context-Based Adaptation](m3-generalization.md)

<a id="paper-rethinking-sim2real"></a>
### Rethinking Sim2Real: Lower Fidelity Simulation Leads to Higher Sim2Real Transfer in Navigation

Joanne Truong et al. · **CoRL 2022 (proceedings 2023)** · [Paper](https://proceedings.mlr.press/v205/truong23a.html)

Examines how simulation fidelity affects transfer in visual navigation.

- **Method and analysis:** Which navigation simulation details are changed and how they affect transfer.
- **Evaluation scope:** The findings concern the navigation settings studied; they do not imply that lower fidelity is always preferable.
- **Related topics:** [Generalization & Context-Based Adaptation](m3-generalization.md)

<a id="paper-world-in-world"></a>
### World-In-World: World Models in a Closed-Loop World

Jiahan Zhang et al. · **ICLR 2026** · [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/5b4263be85820683d78675cc18d2efc7-Abstract-Conference.html)

Tests action-conditioned world models in closed-loop tasks, varying post-training data and test-time computation.

- **Method and analysis:** How action controllability, post-training data, and test-time computation affect closed-loop performance.
- **Evaluation scope:** The reported scaling results cover the tasks and computation ranges included in the evaluation.
- **Related topics:** [Planning & Task-Relevant Representations](m4-knowledge-use.md) · [Predictive Architectures & Pretraining](m7-scaling.md)

## Method comparisons

SIMPLER asks whether simulation can reliably compare real-world policies; Rethinking Sim2Real examines fidelity and transfer. Physical Law Perspective and World-In-World add physical testing and closed-loop evaluation.

## Related topics

- [Generalization & Context-Based Adaptation](m3-generalization.md)
- [Planning & Task-Relevant Representations](m4-knowledge-use.md)
- [Predictive Architectures & Pretraining](m7-scaling.md)

[Paper-note template](../../templates/paper-note.md) · [Comparison template](../../templates/comparison-note.md) · [Back to overview ↑](../../README.md)

<!-- END GENERATED RESEARCH MAP -->
