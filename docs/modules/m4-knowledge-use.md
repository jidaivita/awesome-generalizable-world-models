<!-- BEGIN GENERATED RESEARCH MAP -->

[← Paper index](../../README.md#research-map) · [Reading guide](../reading-guide.md)

# Planning & Task-Relevant Representations

The papers relate internal representations to prediction, planning, and task performance. They examine which information a task requires and how model behavior reveals its use.

Decodability, use, and task value require separate evidence. Whether an abstraction transfers to a new task depends on what it preserves.

## Papers

<a id="paper-denoised-mdps"></a>
### Denoised MDPs: Learning World Models Better Than the World Itself

Tongzhou Wang et al. · **ICML 2022** · [Paper](https://proceedings.mlr.press/v162/wang22c.html)

Separates controllable and reward-relevant information from other factors in observations.

- **Method and analysis:** The decomposition by controllability and reward relevance, and its effect on learning.
- **Evaluation scope:** Information irrelevant to the current task may matter for another task. The decomposition relies on structural assumptions.
- **Related topics:** [Object-Centric & Relational Models](m1-structure.md)

<a id="paper-dino-wm"></a>
### DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning

Gaoyue Zhou et al. · **ICML 2025** · [Paper](https://proceedings.mlr.press/v267/zhou25t.html)

Combines frozen visual representations, action-conditioned latent prediction, and goal-directed planning.

- **Method and analysis:** The frozen visual encoder, action-conditioned patch prediction, and the planning objective in goal space.
- **Evaluation scope:** Zero-shot planning still relies on dynamics training with trajectories from the relevant domain.
- **Related topics:** [Predictive Architectures & Pretraining](m7-scaling.md)

<a id="paper-value-equivalence"></a>
### The Value Equivalence Principle for Model-Based Reinforcement Learning

Christopher Grimm et al. · **NeurIPS 2020** · [Paper](https://proceedings.neurips.cc/paper/2020/hash/3bb585ea00014b0e3ebe4c6dd165a358-Abstract.html)

Formalizes models that preserve decision-relevant Bellman updates without reconstructing every world detail.

- **Method and analysis:** The policy and value-function classes over which Bellman updates remain equivalent.
- **Evaluation scope:** Equivalence is relative to specified function and policy classes; it does not guarantee suitability for arbitrary future tasks.
- **Related topics:** [Evaluation & Sim-to-Real Transfer](m5-reliability.md)

<a id="paper-what-found"></a>
### What Has a Foundation Model Found? Using Inductive Bias to Probe for World Models

Keyon Vafa et al. · **ICML 2025** · [Paper](https://proceedings.mlr.press/v267/vafa25a.html)

Probes learned world structure through inductive biases in new tasks.

- **Method and analysis:** How hypothesized world models generate diagnostic tasks and how learning behavior reveals inductive bias.
- **Evaluation scope:** The probe measures inductive bias, rather than ordinary linear decodability. Conclusions remain tied to the tested tasks and hypotheses.
- **Related topics:** [Generalization & Context-Based Adaptation](m3-generalization.md)

## Method comparisons

What Has a Foundation Model Found tests world structure through inductive bias on new tasks. DINO-WM uses latent predictions for goal-directed planning. Denoised MDPs decomposes observations by controllability and reward relevance; Value Equivalence characterizes models through their Bellman updates.

## Related topics

- [Representation Geometry & Analysis](m2-geometry.md)
- [Generalization & Context-Based Adaptation](m3-generalization.md)
- [Evaluation & Sim-to-Real Transfer](m5-reliability.md)

[Paper-note template](../../templates/paper-note.md) · [Comparison template](../../templates/comparison-note.md) · [Back to overview ↑](../../README.md)

<!-- END GENERATED RESEARCH MAP -->
