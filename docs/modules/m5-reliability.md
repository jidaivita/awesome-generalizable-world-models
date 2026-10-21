<!-- BEGIN GENERATED RESEARCH MAP -->

[← Paper index](../../README.md#research-map) · [Reading guide](../reading-guide.md) · [Supplementary reading](../supplementary.md)

# 📊 Evaluation & Benchmarks

Evaluation connects a world model's predictions to explicit tests of generalization and physical inference. The protocols here cover unseen combinations, extrapolation, future events, hidden physical properties, and closed-loop outcomes.

Each protocol specifies what the model observes, what changes at test time, and which outcome is measured. World-model-based policy evaluation is included when correspondence with real outcomes is tested; adjacent policy-only simulation studies appear in Supplementary Reading.

## Evaluation targets

| Protocol | Measured outcome | Scope of evidence |
| :--- | :--- | :--- |
| SVIB | One-step prediction on held-out factor combinations | Systematic visual composition |
| A Physical Law Perspective | Prediction under interpolation, extrapolation, and composition | Physical generalization in a controlled 2D testbed |
| Physion / Physion++ | Future physical-event judgments | Event prediction; Physion++ additionally requires latent-property inference |
| World-In-World | Task success using action-conditioned world models | Closed-loop usefulness under the tested interfaces and planners |
| WorldGym | Agreement with real policy success rates and rankings | Validity of a learned policy-evaluation environment |

## Compositional prediction and physical extrapolation

<a id="paper-physical-law-perspective"></a>
### How Far Is Video Generation from World Model: A Physical Law Perspective

[![ICML: 2025](https://img.shields.io/badge/ICML-2025-526d82?style=flat-square)](https://proceedings.mlr.press/v267/kang25g.html) [![arXiv: 2411.02385](https://img.shields.io/badge/arXiv-2411.02385-b31b1b?style=flat-square)](https://arxiv.org/abs/2411.02385) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/phyworld/phyworld) [![Project: Website](https://img.shields.io/badge/Project-Website-2679b5?style=flat-square)](https://phyworld.github.io/)

Bingyi Kang et al.

- **Method:** Diffusion video models are trained on a deterministic 2D testbed of motion and collisions. Separate splits test interpolation, extrapolation, and new combinations of familiar physical factors.
- **Evaluation:** Scaling improves in-distribution and some combinatorial predictions, while the tested models struggle with out-of-distribution physical scenarios. Additional experiments examine which appearance and motion factors drive case-based predictions.
- **Related topics:** [Generalization & Adaptation](m3-generalization.md)

<a id="paper-svib"></a>
### Imagine the Unseen World: A Benchmark for Systematic Generalization in Visual World Models

[![NeurIPS: 2023 Datasets & Benchmarks](https://img.shields.io/badge/NeurIPS-2023%20Datasets%20%26%20Benchmarks-526d82?style=flat-square)](https://proceedings.nips.cc/paper_files/paper/2023/hash/58af908d6293810f1a29e69bf723dc48-Abstract-Datasets_and_Benchmarks.html) [![arXiv: 2311.09064](https://img.shields.io/badge/arXiv-2311.09064-b31b1b?style=flat-square)](https://arxiv.org/abs/2311.09064) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/systematic-visual-imagination/svib) [![Project: Website](https://img.shields.io/badge/Project-Website-2679b5?style=flat-square)](https://systematic-visual-imagination.github.io/)

Yeongbin Kim et al.

- **Method:** The Systematic Visual Imagination Benchmark formulates world modeling as one-step image-to-image prediction under latent dynamics. Training splits vary the fraction of factor combinations observed, while different rendering settings vary perceptual difficulty.
- **Evaluation:** Held-out combinations test whether models compose familiar factors in new configurations. The protocol isolates systematic visual generalization in one-step predictions; it does not measure long-horizon physical rollouts or closed-loop control.
- **Related topics:** [Generalization & Adaptation](m3-generalization.md) · [Structured & Compositional Representations](m1-structure.md)

## Physical-event prediction: the Physion family

<a id="paper-physion"></a>
### Physion: Evaluating Physical Prediction from Vision in Humans and Machines

[![NeurIPS: 2021 Datasets & Benchmarks](https://img.shields.io/badge/NeurIPS-2021%20Datasets%20%26%20Benchmarks-526d82?style=flat-square)](https://datasets-benchmarks-proceedings.neurips.cc/paper_files/paper/2021/hash/d09bf41544a3365a46c9077ebb5e35c3-Abstract-round1.html) [![arXiv: 2106.08261](https://img.shields.io/badge/arXiv-2106.08261-b31b1b?style=flat-square)](https://arxiv.org/abs/2106.08261) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/cogtoolslab/physics-benchmarking-neurips2021) [![Project: Website](https://img.shields.io/badge/Project-Website-2679b5?style=flat-square)](https://physion-benchmark.github.io/)

Daniel Bear et al.

- **Method:** The Object Contact Prediction task presents a video prefix and asks whether two designated objects will contact later. A common readout protocol compares visual and physically structured models with human judgments across eight types of simulated physical events.
- **Evaluation:** The benchmark compares future-event accuracy and human prediction patterns across scenarios including collision, support, containment, and deformation. It evaluates predictive physical information through event readout rather than generated-video appearance.
- **Related topics:** [Structured & Compositional Representations](m1-structure.md) · [World Model Interpretability](m8-interpretability.md)

<a id="paper-physion-pp"></a>
### Physion++: Evaluating Physical Scene Understanding that Requires Online Inference of Different Physical Properties

[![NeurIPS: 2023 Datasets & Benchmarks](https://img.shields.io/badge/NeurIPS-2023%20Datasets%20%26%20Benchmarks-526d82?style=flat-square)](https://proceedings.nips.cc/paper_files/paper/2023/hash/d3e8011c912e651ab2a76e7935a1e464-Abstract-Datasets_and_Benchmarks.html) [![arXiv: 2306.15668](https://img.shields.io/badge/arXiv-2306.15668-b31b1b?style=flat-square)](https://arxiv.org/abs/2306.15668) [![Project: Website](https://img.shields.io/badge/Project-Website-2679b5?style=flat-square)](https://dingmyu.github.io/physion_v2/)

Hsiao-Yu Tung et al.

- **Method:** Physion++ constructs physical-event prediction problems whose outcomes depend on latent mass, friction, elasticity, or deformability. These properties must be inferred from observed motion and interactions before predicting the event.
- **Evaluation:** Physical prediction models with different representations and built-in knowledge are compared with human judgments. Relative to Physion, the added requirement is online inference of hidden physical properties, rather than prediction from visible scene configuration alone.
- **Related topics:** [Generalization & Adaptation](m3-generalization.md) · [World Model Interpretability](m8-interpretability.md)

## Closed-loop tasks and policy-evaluation validity

<a id="paper-world-in-world"></a>
### World-In-World: World Models in a Closed-Loop World

[![ICLR: 2026](https://img.shields.io/badge/ICLR-2026-526d82?style=flat-square)](https://proceedings.iclr.cc/paper_files/paper/2026/hash/5b4263be85820683d78675cc18d2efc7-Abstract-Conference.html) [![arXiv: 2510.18135](https://img.shields.io/badge/arXiv-2510.18135-b31b1b?style=flat-square)](https://arxiv.org/abs/2510.18135) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/World-In-World/world-in-world) [![Project: Website](https://img.shields.io/badge/Project-Website-2679b5?style=flat-square)](https://world-in-world.github.io/)

Jiahan Zhang et al.

- **Method:** A shared action interface and online planning strategy connect heterogeneous world models to closed-loop environments. This makes task outcomes comparable across models with different generation interfaces.
- **Evaluation:** Four environments measure task success and examine action-conditioned post-training data and inference-time computation. The study contrasts these results with open-loop visual-quality measures.
- **Related topics:** [Planning & Task-Relevant World Models](m4-knowledge-use.md)

<a id="paper-worldgym"></a>
### WorldGym: World Model as An Environment for Policy Evaluation

[![ICLR: 2026](https://img.shields.io/badge/ICLR-2026-526d82?style=flat-square)](https://proceedings.iclr.cc/paper_files/paper/2026/hash/7f5e909ac0324db03506b380c695ffaf-Abstract-Conference.html) [![arXiv: 2506.00613](https://img.shields.io/badge/arXiv-2506.00613-b31b1b?style=flat-square)](https://arxiv.org/abs/2506.00613) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/world-model-eval/world-model-eval) [![Project: Website](https://img.shields.io/badge/Project-Website-2679b5?style=flat-square)](https://world-model-eval.github.io/abstract.html)

Julian Quevedo et al.

- **Method:** An autoregressive action-conditioned video model provides a learned environment for policy rollouts. Monte Carlo evaluations begin from real-robot images, and a vision-language model assigns rewards to the generated interactions.
- **Evaluation:** Experiments compare simulated and real-world success rates and relative rankings across VLA policy versions, sizes, and checkpoints, with additional novel-task and environment tests. The target is policy-evaluation validity in a learned environment; realistic object interaction remains a reported limitation.
- **Related topics:** [Planning & Task-Relevant World Models](m4-knowledge-use.md) · [Generalization & Adaptation](m3-generalization.md)

## Method comparisons

SVIB tests unseen combinations in one-step visual prediction; A Physical Law Perspective isolates interpolation, extrapolation, and compositional physical prediction. Physion measures future object-contact judgments. Physion++ extends that family with events requiring inference of hidden physical properties. World-In-World compares world models in closed-loop tasks, whereas WorldGym checks whether policy outcomes and rankings in a learned environment agree with real-robot evaluations.

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
