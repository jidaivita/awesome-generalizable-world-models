<!-- BEGIN GENERATED RESEARCH MAP -->

<a id="top"></a>
<div align="center">

# Awesome Generalizable World Models

**Representations · Dynamics · Generalization · Planning**

![A research map connecting representation geometry, generalization, and knowledge use](assets/research-map.svg)

![Papers](https://img.shields.io/badge/Papers-30-2563eb?style=flat-square) ![Reading route](https://img.shields.io/badge/Reading_route-12-0f766e?style=flat-square) ![Research modules](https://img.shields.io/badge/Modules-7-7c3aed?style=flat-square)

[Start Here](#start-here) · [Contents](#research-map) · [Reading Path](#reading-route) · [Paper List](#papers) · [Contribute](CONTRIBUTING.md)

</div>

---

**How do models learn transferable world knowledge from limited experience—and how is that knowledge organized, used, and revised?**

Papers on learned world representations, dynamics, generalization, and planning. The list covers how models organize physical information, adapt to unfamiliar environments, and use learned knowledge for prediction and decisions.

<a id="research-map"></a>
## Contents

| Topic | Papers | Reading guide |
| :--- | :---: | :--- |
| [Structure & Invariance](#m1) | 4 | [Overview & connections](docs/modules/m1-structure.md) |
| [Representation Geometry & Manifolds](#m2) | 6 | [Overview & connections](docs/modules/m2-geometry.md) |
| [Generalization & In-Context Learning](#m3) | 4 | [Overview & connections](docs/modules/m3-generalization.md) |
| [Knowledge Use & Task Abstraction](#m4) | 4 | [Overview & connections](docs/modules/m4-knowledge-use.md) |
| [Reliability & Sim2Real](#m5) | 4 | [Overview & connections](docs/modules/m5-reliability.md) |
| [Exploration & Efficient Adaptation](#m6) | 4 | [Overview & connections](docs/modules/m6-adaptation.md) |
| [Pretraining & Scaling](#m7) | 4 | [Overview & connections](docs/modules/m7-scaling.md) |

Papers are listed alphabetically within each topic. The guides link related work across topics.

<a id="start-here"></a>
## Start Here

Two complementary entry points into the central questions:

| 01 · How is knowledge organized? | 02 · What does new experience change? |
| :--- | :--- |
| **[Interpreting Physics in Video World Models](https://proceedings.mlr.press/v306/joseph26a.html)** | **[Context and Diversity Matter: The Emergence of In-Context Learning in World Models](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a46b9dcef23e9160f46d800a49a931d0-Abstract-Conference.html)** |
| Physical variables, subspaces, and interventions reveal how information is represented. | Environment recognition and environment learning offer different explanations for adaptation. |
| **Ask:** Does decodable information actually influence model behavior? | **Ask:** What mechanism explains the benefit of context? |

<a id="reading-route"></a>
## Reading Path

**Mechanisms → geometry → planning → adaptation.** The [reading guide](docs/reading-guide.md) connects 12 papers across these topics.

<details>
<summary>View the 12-paper reading path</summary>


| # | Paper | Question to take away |
| :---: | :--- | :--- |
| 01 | [Interpreting Physics](#paper-interpreting-physics) | What distinguishes independent physical variables from distributed encoding? |
| 02 | [Context and Diversity Matter](#paper-context-diversity) | How can environment recognition, dynamics learning, and state estimation be distinguished? |
| 03 | [What Has a Foundation Model Found?](#paper-what-found) | Why can strong task performance be insufficient evidence of learned world structure? |
| 04 | [SMDS / Shape Happens](#paper-smds) | How can competing geometric hypotheses be compared beyond a projection plot? |
| 05 | [GRWM](#paper-grwm) | How can geometric diagnosis become a method for better long-horizon prediction? |
| 06 | [DINO-WM](#paper-dino-wm) | How does a latent representation support planning? |
| 07 | [LeWorldModel](#paper-leworldmodel) | How can end-to-end learning support prediction and planning with a compact model? |
| 08 | [What Drives Success in JEPA-WMs?](#paper-jepa-wms) | How can architecture, objective, and planner effects be separated? |
| 09 | [Group-Structured Latent Space](#paper-group-latents) | What is supplied as a symmetry prior, and what is learned from data? |
| 10 | [Dynamics Are Learned, Not Told](#paper-dynamics-geometries) | How does latent geometry connect to adaptation under changing dynamics? |
| 11 | [SIMPLER](#paper-simpler) | When do model errors change real-world policy choices? |
| 12 | [Poke and Strike](#paper-poke-strike) | Which new experience is valuable for the task? |

</details>

[Read the guide →](docs/reading-guide.md)

<a id="papers"></a>
## Papers

Entries include a paper link, publication information, available code or project links, and a short description.

<a id="m1"></a>
### Structure & Invariance

> Which objects, relations, and stable structures should a model represent?

<a id="paper-causal-jepa"></a>
- **[Causal-JEPA: Learning World Models through Object-Level Latent Masking](https://proceedings.mlr.press/v306/nam26c.html)**<br>
  ICML 2026 · [Paper](https://proceedings.mlr.press/v306/nam26c.html) · [Code](https://github.com/galilai-group/cjepa)<br>
  Combines object-level latent masking with joint-embedding predictive learning.

<a id="paper-cswm"></a>
- **[Contrastive Learning of Structured World Models](https://arxiv.org/abs/1911.12247)**<br>
  ICLR 2020 · [Paper](https://arxiv.org/abs/1911.12247)<br>
  Learns object-centric representations and relational dynamics with a contrastive objective.

<a id="paper-nri"></a>
- **[Neural Relational Inference for Interacting Systems](https://proceedings.mlr.press/v80/kipf18a.html)**<br>
  ICML 2018 · [Paper](https://proceedings.mlr.press/v80/kipf18a.html)<br>
  Infers latent interaction graphs from trajectories with a graph-based dynamics decoder.

<a id="paper-spartan"></a>
- **[SPARTAN: A Sparse Transformer World Model Attending to What Matters](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e2c33c1753e1f1924f5560b11fc4444f-Abstract-Conference.html)**<br>
  NeurIPS 2025 · [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e2c33c1753e1f1924f5560b11fc4444f-Abstract-Conference.html)<br>
  Uses sparse, context-dependent interactions to adapt to changes in mechanisms.

[Reading notes and connections →](docs/modules/m1-structure.md) · [Back to map ↑](#research-map)

<a id="m2"></a>
### Representation Geometry & Manifolds

> How is knowledge organized in latent space, and what does that organization do?

<a id="paper-grwm"></a>
- **[Cloning Deterministic Worlds: The Critical Role of Latent Geometry in Long-Horizon World Models](https://arxiv.org/abs/2510.26782)**<br>
  CVPR 2026 · [Paper](https://arxiv.org/abs/2510.26782) · [Code](https://github.com/XiaFire/Clone_Deterministic_Environment) · [Project](https://xiafire.github.io/grwm-project-page/)<br>
  Connects representation geometry and temporal context to long-horizon prediction error.

<a id="paper-geoworld"></a>
- **[GeoWorld: Geometric World Models](https://arxiv.org/abs/2602.23058)**<br>
  CVPR 2026 · [Paper](https://arxiv.org/abs/2602.23058) · [Project](https://steve-zeyu-zhang.github.io/GeoWorld/)<br>
  Studies non-Euclidean latent spaces and geometric optimization for procedural visual planning.

<a id="paper-smds"></a>
- **[Hypothesis-Driven Feature Manifold Analysis in LLMs via Supervised Multi-Dimensional Scaling](https://arxiv.org/abs/2510.01025)**<br>
  TMLR 2026 · [Paper](https://arxiv.org/abs/2510.01025) · [Code](https://github.com/UKPLab/tmlr2026-manifold-analysis)<br>
  Compares geometric hypotheses and their functional effects in language-model representations.

<a id="paper-interpreting-physics"></a>
- **[Interpreting Physics in Video World Models](https://proceedings.mlr.press/v306/joseph26a.html)**<br>
  ICML 2026 · [Paper](https://proceedings.mlr.press/v306/joseph26a.html)<br>
  Analyzes the organization of physical information through layer-wise probes, subspaces, and interventions.

<a id="paper-group-latents"></a>
- **[Learning Abstract World Models with a Group-Structured Latent Space](https://arxiv.org/abs/2506.01529)**<br>
  arXiv 2025 · [Paper](https://arxiv.org/abs/2506.01529) · [Code](https://github.com/khanhvu207/world-models-group-latents)<br>
  Encodes known symmetries, such as translation and rotation, as geometric inductive biases.

<a id="paper-origins-manifolds"></a>
- **[The Origins of Representation Manifolds in Large Language Models](https://arxiv.org/abs/2505.18235)**<br>
  arXiv 2025 · [Paper](https://arxiv.org/abs/2505.18235)<br>
  Relates similarities in learned representations to intrinsic conceptual geometry under a generative model.

[Reading notes and connections →](docs/modules/m2-geometry.md) · [Back to map ↑](#research-map)

<a id="m3"></a>
### Generalization & In-Context Learning

> Does success in a new environment come from knowledge reuse or learning new dynamics?

<a id="paper-context-diversity"></a>
- **[Context and Diversity Matter: The Emergence of In-Context Learning in World Models](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a46b9dcef23e9160f46d800a49a931d0-Abstract-Conference.html)**<br>
  ICLR 2026 · [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a46b9dcef23e9160f46d800a49a931d0-Abstract-Conference.html) · [Code](https://github.com/airs-cuhk/airsoul/tree/main/projects/MazeWorld)<br>
  Distinguishes recognizing familiar environments from learning dynamics through current experience.

<a id="paper-cadm"></a>
- **[Context-aware Dynamics Model for Generalization in Model-Based Reinforcement Learning](https://proceedings.mlr.press/v119/lee20g.html)**<br>
  ICML 2020 · [Paper](https://proceedings.mlr.press/v119/lee20g.html) · [Code](https://github.com/younggyoseo/CaDM)<br>
  Infers environment context from interaction history to model changing dynamics.

<a id="paper-dreamweaver"></a>
- **[Dreamweaver: Learning Compositional World Models from Pixels](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ae82a60c5ce50b5c4d18cfe3214eb684-Abstract-Conference.html)**<br>
  ICLR 2025 · [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ae82a60c5ce50b5c4d18cfe3214eb684-Abstract-Conference.html)<br>
  Learns object and attribute representations for combinations beyond training configurations.

<a id="paper-dynamics-geometries"></a>
- **[Dynamics Are Learned, Not Told: Semi-Supervised Discovery of Latent Dynamics Geometries For Zero-Shot Policy Adaptation](https://proceedings.mlr.press/v306/xu26cq.html)**<br>
  ICML 2026 · [Paper](https://proceedings.mlr.press/v306/xu26cq.html) · [Code](https://github.com/Mr-Wonderfool/Latent-Dynamics-Geometries)<br>
  Connects trajectory geometry with policy adaptation under changing dynamics.

[Reading notes and connections →](docs/modules/m3-generalization.md) · [Back to map ↑](#research-map)

<a id="m4"></a>
### Knowledge Use & Task Abstraction

> Which information actually supports prediction, planning, and decisions?

<a id="paper-denoised-mdps"></a>
- **[Denoised MDPs: Learning World Models Better Than the World Itself](https://proceedings.mlr.press/v162/wang22c.html)**<br>
  ICML 2022 · [Paper](https://proceedings.mlr.press/v162/wang22c.html)<br>
  Separates controllable and reward-relevant information from other factors in observations.

<a id="paper-dino-wm"></a>
- **[DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning](https://proceedings.mlr.press/v267/zhou25t.html)**<br>
  ICML 2025 · [Paper](https://proceedings.mlr.press/v267/zhou25t.html)<br>
  Combines frozen visual representations, action-conditioned latent prediction, and goal-directed planning.

<a id="paper-value-equivalence"></a>
- **[The Value Equivalence Principle for Model-Based Reinforcement Learning](https://proceedings.neurips.cc/paper/2020/hash/3bb585ea00014b0e3ebe4c6dd165a358-Abstract.html)**<br>
  NeurIPS 2020 · [Paper](https://proceedings.neurips.cc/paper/2020/hash/3bb585ea00014b0e3ebe4c6dd165a358-Abstract.html)<br>
  Formalizes models that preserve decision-relevant Bellman updates without reconstructing every world detail.

<a id="paper-what-found"></a>
- **[What Has a Foundation Model Found? Using Inductive Bias to Probe for World Models](https://proceedings.mlr.press/v267/vafa25a.html)**<br>
  ICML 2025 · [Paper](https://proceedings.mlr.press/v267/vafa25a.html)<br>
  Probes learned world structure through inductive biases in new tasks.

[Reading notes and connections →](docs/modules/m4-knowledge-use.md) · [Back to map ↑](#research-map)

<a id="m5"></a>
### Reliability & Sim2Real

> Which model errors matter for decisions, and when is a model trustworthy?

<a id="paper-simpler"></a>
- **[Evaluating Real-World Robot Manipulation Policies in Simulation](https://proceedings.mlr.press/v270/li25c.html)**<br>
  CoRL 2024 (proceedings 2025) · [Paper](https://proceedings.mlr.press/v270/li25c.html)<br>
  Evaluates whether simulation reliably predicts the relative performance of real-world manipulation policies.

<a id="paper-physical-law-perspective"></a>
- **[How Far Is Video Generation from World Model: A Physical Law Perspective](https://proceedings.mlr.press/v267/kang25g.html)**<br>
  ICML 2025 · [Paper](https://proceedings.mlr.press/v267/kang25g.html)<br>
  Tests physical prediction under extrapolation and compositional distribution shifts.

<a id="paper-rethinking-sim2real"></a>
- **[Rethinking Sim2Real: Lower Fidelity Simulation Leads to Higher Sim2Real Transfer in Navigation](https://proceedings.mlr.press/v205/truong23a.html)**<br>
  CoRL 2022 (proceedings 2023) · [Paper](https://proceedings.mlr.press/v205/truong23a.html)<br>
  Examines how simulation fidelity affects transfer in visual navigation.

<a id="paper-world-in-world"></a>
- **[World-In-World: World Models in a Closed-Loop World](https://proceedings.iclr.cc/paper_files/paper/2026/hash/5b4263be85820683d78675cc18d2efc7-Abstract-Conference.html)**<br>
  ICLR 2026 · [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/5b4263be85820683d78675cc18d2efc7-Abstract-Conference.html)<br>
  Evaluates world models through closed-loop task performance.

[Reading notes and connections →](docs/modules/m5-reliability.md) · [Back to map ↑](#research-map)

<a id="m6"></a>
### Exploration & Efficient Adaptation

> What experience should an agent acquire or reuse in an unfamiliar environment?

<a id="paper-asid"></a>
- **[ASID: Active Exploration for System Identification in Robotic Manipulation](https://proceedings.iclr.cc/paper_files/paper/2024/hash/ae8afec5dabb07091d8f85128250f2ff-Abstract-Conference.html)**<br>
  ICLR 2024 · [Paper](https://proceedings.iclr.cc/paper_files/paper/2024/hash/ae8afec5dabb07091d8f85128250f2ff-Abstract-Conference.html)<br>
  Combines active interaction with system identification to improve simulation models.

<a id="paper-curious-replay"></a>
- **[Curious Replay for Model-based Adaptation](https://proceedings.mlr.press/v202/kauvar23a.html)**<br>
  ICML 2023 · [Paper](https://proceedings.mlr.press/v202/kauvar23a.html)<br>
  Prioritizes stored experience using novelty and prediction error to support adaptation.

<a id="paper-plan2explore"></a>
- **[Planning to Explore via Self-Supervised World Models](https://proceedings.mlr.press/v119/sekar20a.html)**<br>
  ICML 2020 · [Paper](https://proceedings.mlr.press/v119/sekar20a.html)<br>
  Learns exploration behavior from model disagreement before downstream tasks are specified.

<a id="paper-poke-strike"></a>
- **[Poke and Strike: Learning Task-Informed Exploration Policies](https://proceedings.mlr.press/v305/aoyama25a.html)**<br>
  CoRL 2025 · [Paper](https://proceedings.mlr.press/v305/aoyama25a.html)<br>
  Selects exploratory interactions according to task-relevant information.

[Reading notes and connections →](docs/modules/m6-adaptation.md) · [Back to map ↑](#research-map)

<a id="m7"></a>
### Pretraining & Scaling

> How do controlled insights connect to stronger models and larger datasets?

<a id="paper-leworldmodel"></a>
- **[LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels](https://arxiv.org/abs/2603.19312)**<br>
  arXiv 2026 · [Paper](https://arxiv.org/abs/2603.19312) · [Code](https://github.com/lucas-maes/le-wm) · [Project](https://le-wm.github.io/)<br>
  Learns a compact world model end to end with joint-embedding predictive objectives.

<a id="paper-dreamerv3"></a>
- **[Mastering diverse control tasks through world models](https://www.nature.com/articles/s41586-025-08744-2)**<br>
  Nature 2025 · [Paper](https://www.nature.com/articles/s41586-025-08744-2)<br>
  Studies a shared world-model learning algorithm and hyperparameters across diverse tasks.

<a id="paper-vjepa2"></a>
- **[V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://arxiv.org/abs/2506.09985)**<br>
  arXiv technical report 2025 · [Paper](https://arxiv.org/abs/2506.09985)<br>
  Connects observational video pretraining with action-conditioned prediction and planning.

<a id="paper-jepa-wms"></a>
- **[What Drives Success in Physical Planning with Joint-Embedding Predictive World Models?](https://arxiv.org/abs/2512.24497)**<br>
  TMLR 2026 · [Paper](https://arxiv.org/abs/2512.24497) · [Code](https://github.com/facebookresearch/jepa-wms)<br>
  Compares architecture, training objectives, and planners in JEPA world models.

[Reading notes and connections →](docs/modules/m7-scaling.md) · [Back to map ↑](#research-map)

## Related Lists

- [Awesome World Models](https://github.com/knightnemo/Awesome-World-Models) — broader coverage of world-model applications.
- [Awesome Deep Learning Papers](https://github.com/terryum/awesome-deep-learning-papers) — influential deep-learning papers organized by topic.
- [Awesome Machine Learning](https://github.com/josephmisiti/awesome-machine-learning) — machine-learning libraries and resources.

## Contributing

To suggest a paper or correct an entry, open an issue or pull request. See the [contribution guide](CONTRIBUTING.md) for scope and entry format.

<!-- END GENERATED RESEARCH MAP -->
