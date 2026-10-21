<!-- BEGIN GENERATED RESEARCH MAP -->

[← Research map](../../README.md#research-map) · [Reading path](../reading-guide.md)

# M5 · Reliability & Sim2Real

> Which model errors matter for decisions, and when is a model trustworthy?

Visual quality, physical accuracy, and task performance measure different aspects of reliability. The papers study physical extrapolation, closed-loop evaluation, and paired real and simulated policy tests.

Performance within simulation, agreement in real-world policy rankings, and successful transfer are different forms of evidence.

## Where to start

1. **[SIMPLER](#paper-simpler)** — Evaluates whether simulation reliably predicts the relative performance of real-world manipulation policies.
2. **[How Far Is Video Generation from World Model: A Physical Law Perspective](#paper-physical-law-perspective)** — Tests physical prediction under extrapolation and compositional distribution shifts.

## Papers and reading pointers

<a id="paper-simpler"></a>
### Evaluating Real-World Robot Manipulation Policies in Simulation

**CoRL 2024 (proceedings 2025)** · [Paper](https://proceedings.mlr.press/v270/li25c.html)

Earlier titles / aliases: SIMPLER.

Evaluates whether simulation reliably predicts the relative performance of real-world manipulation policies.

- **Read for:** Paired real and simulated evaluations, policy rankings, visual matching, and variant aggregation.
- **Scope:** Perturbations within simulation alone do not demonstrate a reduced reality gap.
- **Related topics:** [M4 · Knowledge Use & Task Abstraction](m4-knowledge-use.md)

<a id="paper-physical-law-perspective"></a>
### How Far Is Video Generation from World Model: A Physical Law Perspective

**ICML 2025** · [Paper](https://proceedings.mlr.press/v267/kang25g.html)

Tests physical prediction under extrapolation and compositional distribution shifts.

- **Read for:** How distribution shifts are constructed and whether visual-quality metrics obscure physical successes or failures.
- **Scope:** The findings concern the tested models and datasets, rather than universal limitations of all video models.
- **Related topics:** [M3 · Generalization & In-Context Learning](m3-generalization.md)

<a id="paper-rethinking-sim2real"></a>
### Rethinking Sim2Real: Lower Fidelity Simulation Leads to Higher Sim2Real Transfer in Navigation

**CoRL 2022 (proceedings 2023)** · [Paper](https://proceedings.mlr.press/v205/truong23a.html)

Examines how simulation fidelity affects transfer in visual navigation.

- **Read for:** Which navigation simulation details are changed and how they affect transfer.
- **Scope:** The findings concern the navigation settings studied; they do not imply that lower fidelity is always preferable.
- **Related topics:** [M3 · Generalization & In-Context Learning](m3-generalization.md)

<a id="paper-world-in-world"></a>
### World-In-World: World Models in a Closed-Loop World

**ICLR 2026** · [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/5b4263be85820683d78675cc18d2efc7-Abstract-Conference.html)

Evaluates world models through closed-loop task performance.

- **Read for:** How action controllability, post-training data, and test-time computation affect closed-loop performance.
- **Scope:** Closed-loop evaluations still have task-coverage limits. Scaling claims should remain tied to the evaluated settings.
- **Related topics:** [M4 · Knowledge Use & Task Abstraction](m4-knowledge-use.md) · [M7 · Pretraining & Scaling](m7-scaling.md)

## Read together

SIMPLER asks whether simulation can reliably compare real-world policies; Rethinking Sim2Real examines fidelity and transfer. Physical Law Perspective and World-In-World add physical testing and closed-loop evaluation.

## Related topics

- [M3 · Generalization & In-Context Learning](m3-generalization.md) — Does success in a new environment come from knowledge reuse or learning new dynamics?
- [M4 · Knowledge Use & Task Abstraction](m4-knowledge-use.md) — Which information actually supports prediction, planning, and decisions?
- [M7 · Pretraining & Scaling](m7-scaling.md) — How do controlled insights connect to stronger models and larger datasets?

[Paper-note template](../../templates/paper-note.md) · [Comparison template](../../templates/comparison-note.md) · [Back to overview ↑](../../README.md)

<!-- END GENERATED RESEARCH MAP -->
