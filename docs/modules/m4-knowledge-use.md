<!-- BEGIN GENERATED RESEARCH MAP -->

[← Research map](../../README.md#research-map) · [Reading route](../reading-guide.md)

# M4 · Knowledge Use & Task Abstraction

> Which information actually supports prediction, planning, and decisions?

Connect internal representations to behavior. Study what information a task needs and how predictions, plans, or learning tendencies reveal whether that information is being used.

Decodability, use, and task value require separate evidence. Whether an abstraction transfers to a new task depends on what it preserves.

## Where to start

1. **[What Has a Foundation Model Found?](#paper-what-found)** — Probes learned world structure through inductive biases in new tasks.
2. **[DINO-WM](#paper-dino-wm)** — Combines frozen visual representations, action-conditioned latent prediction, and goal-directed planning.

## Papers and reading pointers

<a id="paper-denoised-mdps"></a>
### Denoised MDPs: Learning World Models Better Than the World Itself

**ICML 2022** · [Paper](https://proceedings.mlr.press/v162/wang22c.html)

Separates controllable and reward-relevant information from other factors in observations.

- **Read for:** The decomposition by controllability and reward relevance, and its effect on learning.
- **Scope:** Information irrelevant to the current task may matter for another task. The decomposition relies on structural assumptions.
- **Connect to:** [M1 · Structure & Invariance](m1-structure.md)

<a id="paper-dino-wm"></a>
### DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning

**ICML 2025** · [Paper](https://proceedings.mlr.press/v267/zhou25t.html)

Combines frozen visual representations, action-conditioned latent prediction, and goal-directed planning.

- **Read for:** The frozen visual encoder, action-conditioned patch prediction, and the planning objective in goal space.
- **Scope:** Zero-shot planning still relies on dynamics training with trajectories from the relevant domain.
- **Connect to:** [M7 · Pretraining & Scaling](m7-scaling.md)

<a id="paper-value-equivalence"></a>
### The Value Equivalence Principle for Model-Based Reinforcement Learning

**NeurIPS 2020** · [Paper](https://proceedings.neurips.cc/paper/2020/hash/3bb585ea00014b0e3ebe4c6dd165a358-Abstract.html)

Formalizes models that preserve decision-relevant Bellman updates without reconstructing every world detail.

- **Read for:** The policy and value-function classes over which Bellman updates remain equivalent.
- **Scope:** Equivalence is relative to specified function and policy classes; it does not guarantee suitability for arbitrary future tasks.
- **Connect to:** [M5 · Reliability & Sim2Real](m5-reliability.md)

<a id="paper-what-found"></a>
### What Has a Foundation Model Found? Using Inductive Bias to Probe for World Models

**ICML 2025** · [Paper](https://proceedings.mlr.press/v267/vafa25a.html)

Probes learned world structure through inductive biases in new tasks.

- **Read for:** How hypothesized world models generate diagnostic tasks and how learning behavior reveals inductive bias.
- **Scope:** The probe measures inductive bias, rather than ordinary linear decodability. Conclusions remain tied to the tested tasks and hypotheses.
- **Connect to:** [M3 · Generalization & In-Context Learning](m3-generalization.md)

## Read together

What Has a Foundation Model Found probes world structure through inductive bias on new tasks. DINO-WM makes the representation-to-planning interface concrete. Denoised MDPs and Value Equivalence help specify which details of the world need to be retained.

## Continue exploring

- [M2 · Representation Geometry & Manifolds](m2-geometry.md) — How is knowledge organized in latent space, and what does that organization do?
- [M3 · Generalization & In-Context Learning](m3-generalization.md) — Does success in a new environment come from knowledge reuse or learning new dynamics?
- [M5 · Reliability & Sim2Real](m5-reliability.md) — Which model errors matter for decisions, and when is a model trustworthy?

[Paper-note template](../../templates/paper-note.md) · [Comparison template](../../templates/comparison-note.md) · [Back to overview ↑](../../README.md)

<!-- END GENERATED RESEARCH MAP -->
