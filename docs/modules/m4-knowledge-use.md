<!-- BEGIN GENERATED RESEARCH MAP -->

[← Paper index](../../README.md#research-map) · [Reading guide](../reading-guide.md) · [Supplementary reading](../supplementary.md)

# 🎯 Planning & Task-Relevant World Models

World models support action selection through predicted futures or representations that preserve decision-relevant quantities. These papers connect latent dynamics to planning, task abstraction, and task-agnostic experience collection.

The evaluation target can be goal-reaching, reward, or the quantities needed for policy evaluation. Task success is interpreted in the tested environment and transfer protocol.

## Latent prediction and planning

<a id="paper-dino-wm"></a>
### DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning

[![ICML: 2025](https://img.shields.io/badge/ICML-2025-526d82?style=flat-square)](https://proceedings.mlr.press/v267/zhou25t.html)

Gaoyue Zhou et al.

- **Method:** A dynamics predictor learns to forecast frozen DINOv2 spatial patch features from offline state-action trajectories. At test time, action sequences are optimized to bring predicted features close to the features of an image goal.
- **Evaluation:** Six environments include varied maze layouts, pushing with different object shapes, and multi-particle settings. Goal-directed planning uses neither a learned reward model nor an inverse-dynamics model.

<a id="paper-vjepa2"></a>
### V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning

[![arXiv: 2506.09985](https://img.shields.io/badge/arXiv-2506.09985-b31b1b?style=flat-square)](https://arxiv.org/abs/2506.09985)

Mido Assran et al.

- **Method:** Action-free joint-embedding prediction pretrains a video encoder on internet video. A subsequent action-conditioned model, V-JEPA 2-AC, is trained with robot trajectories and used to plan toward image goals.
- **Evaluation:** Evaluation spans motion understanding, action anticipation, video question answering, and pick-and-place planning on Franka robots in two labs. Robot planning uses action-conditioned post-training on DROID data.
- **Related topics:** [Generalization & Adaptation](m3-generalization.md)

<a id="paper-jepa-wms"></a>
### What Drives Success in Physical Planning with Joint-Embedding Predictive World Models?

[![TMLR: 2026](https://img.shields.io/badge/TMLR-2026-526d82?style=flat-square)](https://arxiv.org/abs/2512.24497) [![arXiv: 2512.24497](https://img.shields.io/badge/arXiv-2512.24497-b31b1b?style=flat-square)](https://arxiv.org/abs/2512.24497) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/facebookresearch/jepa-wms)

Basile Terver et al.

- **Method:** A component study varies world-model architecture, training objective, and planning algorithm within the joint-embedding predictive family. The resulting configuration combines the empirically favorable choices.
- **Evaluation:** Simulated environments and real robotic data support navigation and manipulation comparisons with DINO-WM and V-JEPA 2-AC. The study attributes planning performance to specific modeling and optimization choices.
- **Related topics:** [Representation Geometry & Symmetry](m2-geometry.md) · [Evaluation & Benchmarks](m5-reliability.md)

## Task-relevant abstraction

<a id="paper-denoised-mdps"></a>
### Denoised MDPs: Learning World Models Better Than the World Itself

[![ICML: 2022](https://img.shields.io/badge/ICML-2022-526d82?style=flat-square)](https://proceedings.mlr.press/v162/wang22c.html)

Tongzhou Wang et al.

- **Method:** The latent state is factored according to controllability and reward relevance. The control model retains the controllable, reward-relevant component while modeling nuisance variation separately.
- **Evaluation:** DeepMind Control Suite variants and RoboDesk test policy learning under distractors; joint-position regression tests retained physical information. The abstraction is defined relative to the training reward.
- **Related topics:** [Structured & Compositional Representations](m1-structure.md)

<a id="paper-value-equivalence"></a>
### The Value Equivalence Principle for Model-Based Reinforcement Learning

[![NeurIPS: 2020](https://img.shields.io/badge/NeurIPS-2020-526d82?style=flat-square)](https://proceedings.neurips.cc/paper/2020/hash/3bb585ea00014b0e3ebe4c6dd165a358-Abstract.html)

Christopher Grimm et al.

- **Method:** Two models are value equivalent for a specified set of policies and functions when they produce the same Bellman updates. This defines model learning by the computations needed for value-based planning.
- **Evaluation:** Theoretical results characterize how the equivalent-model class shrinks as policy and function sets expand. Experiments compare value-equivalent learning with maximum-likelihood modeling; equivalence is relative to those sets.
- **Related topics:** [Evaluation & Benchmarks](m5-reliability.md)

## Experience collection for downstream tasks

<a id="paper-plan2explore"></a>
### Planning to Explore via Self-Supervised World Models

[![ICML: 2020](https://img.shields.io/badge/ICML-2020-526d82?style=flat-square)](https://proceedings.mlr.press/v119/sekar20a.html)

Ramanan Sekar et al.

- **Method:** An ensemble of latent predictors supplies a disagreement signal, and an exploration policy plans actions that seek expected future disagreement. Downstream task policies are then learned using the collected world model.
- **Evaluation:** Visual control tasks evaluate reward-free exploration followed by zero- or few-shot task adaptation. Tasks can be specified after the exploration phase.
- **Related topics:** [Generalization & Adaptation](m3-generalization.md)

## Method comparisons

DINO-WM plans in frozen visual features; V-JEPA 2 connects video pretraining to action-conditioned prediction and robot planning. JEPA-WMs separates encoder, objective, and planner choices. Denoised MDPs isolates controllable and reward-relevant factors, while Value Equivalence formalizes the model information needed for Bellman updates. Plan2Explore collects experience through disagreement between predictors before downstream rewards are specified.

## Related topics

- [Generalization & Adaptation](m3-generalization.md)
- [Representation Geometry & Symmetry](m2-geometry.md)
- [Evaluation & Benchmarks](m5-reliability.md)

[Back to paper index](../../README.md)

## Entries in related sections

<a id="paper-what-found"></a>
- [What Has a Foundation Model Found? Using Inductive Bias to Probe for World Models](m8-interpretability.md#paper-what-found)

<!-- END GENERATED RESEARCH MAP -->
