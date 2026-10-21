<!-- BEGIN GENERATED RESEARCH MAP -->

<a id="top"></a>

# Awesome Generalizable World Models

Papers on learned world models and their generalization across object configurations, environments, dynamics, and tasks. The list covers structured representations, latent geometry, context-based adaptation, planning, and evaluation, with related analysis methods from language models labeled separately.

<p align="center"><img src="assets/research-map.svg" width="620" alt="Representation geometry, transfer across environments, and planning"></p>

[Topics](#research-map) · [Reading Guide](docs/reading-guide.md) · [BibTeX](references.bib) · [Contributing](CONTRIBUTING.md)

<a id="start-here"></a>
<a id="research-map"></a>
## Contents

- [Object-Centric & Relational Models](#m1)
- [Representation Geometry & Analysis](#m2)
- [Generalization & Context-Based Adaptation](#m3)
- [Planning & Task-Relevant Representations](#m4)
- [Evaluation & Sim-to-Real Transfer](#m5)
- [Exploration & Experience Replay](#m6)
- [Predictive Architectures & Pretraining](#m7)

30 papers · 7 topics · Listed alphabetically within each topic.

<a id="papers"></a>
## Papers

<a id="m1"></a>
### Object-Centric & Relational Models

<a id="paper-causal-jepa"></a>
- **Causal-JEPA: Learning World Models through Object-Level Latent Masking**<br>
  Heejeong Nam et al. · **ICML 2026** · [Paper](https://proceedings.mlr.press/v306/nam26c.html) · [Code](https://github.com/galilai-group/cjepa)<br>
  Combines object-level latent masking with joint-embedding predictive learning.

<a id="paper-cswm"></a>
- **Contrastive Learning of Structured World Models**<br>
  Thomas Kipf et al. · **ICLR 2020** · [Paper](https://arxiv.org/abs/1911.12247)<br>
  Learns object-centric representations and relational dynamics with a contrastive objective.

<a id="paper-nri"></a>
- **Neural Relational Inference for Interacting Systems**<br>
  Thomas Kipf et al. · **ICML 2018** · [Paper](https://proceedings.mlr.press/v80/kipf18a.html)<br>
  Infers latent interaction graphs from trajectories with a graph-based dynamics decoder.

<a id="paper-spartan"></a>
- **SPARTAN: A Sparse Transformer World Model Attending to What Matters**<br>
  Anson Lei et al. · **NeurIPS 2025** · [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e2c33c1753e1f1924f5560b11fc4444f-Abstract-Conference.html)<br>
  Uses sparse, context-dependent interactions to adapt to changes in mechanisms.

[Topic overview and comparisons](docs/modules/m1-structure.md) · [Contents](#research-map)

<a id="m2"></a>
### Representation Geometry & Analysis

<a id="paper-grwm"></a>
- **Cloning Deterministic Worlds: The Critical Role of Latent Geometry in Long-Horizon World Models**<br>
  Zaishuo Xia et al. · **CVPR 2026** · [Paper](https://arxiv.org/abs/2510.26782) · [Code](https://github.com/XiaFire/Clone_Deterministic_Environment) · [Project](https://xiafire.github.io/grwm-project-page/)<br>
  Regularizes latent geometry and uses temporal context for long-horizon prediction in deterministic environments.

<a id="paper-geoworld"></a>
- **GeoWorld: Geometric World Models**<br>
  Zeyu Zhang et al. · **CVPR 2026** · `Procedural planning` · [Paper](https://arxiv.org/abs/2602.23058) · [Project](https://steve-zeyu-zhang.github.io/GeoWorld/)<br>
  Uses hyperbolic latent representations and geometric optimization for procedural planning on CrossTask and COIN.

<a id="paper-smds"></a>
- **Hypothesis-Driven Feature Manifold Analysis in LLMs via Supervised Multi-Dimensional Scaling**<br>
  Federico Tiblias et al. · **TMLR 2026** · `LLM analysis` · [Paper](https://arxiv.org/abs/2510.01025) · [Code](https://github.com/UKPLab/tmlr2026-manifold-analysis)<br>
  Compares geometric hypotheses and their functional effects in language-model representations.

<a id="paper-interpreting-physics"></a>
- **Interpreting Physics in Video World Models**<br>
  Sonia Joseph et al. · **ICML 2026** · [Paper](https://proceedings.mlr.press/v306/joseph26a.html)<br>
  Analyzes the organization of physical information through layer-wise probes, subspaces, and interventions.

<a id="paper-group-latents"></a>
- **Learning Abstract World Models with a Group-Structured Latent Space**<br>
  Thomas Delliaux et al. · **arXiv 2025** · [Paper](https://arxiv.org/abs/2506.01529) · [Code](https://github.com/khanhvu207/world-models-group-latents)<br>
  Encodes known symmetries, such as translation and rotation, as geometric inductive biases.

<a id="paper-origins-manifolds"></a>
- **The Origins of Representation Manifolds in Large Language Models**<br>
  Alexander Modell et al. · **arXiv 2025** · `LLM analysis` · [Paper](https://arxiv.org/abs/2505.18235)<br>
  Relates similarities in learned representations to intrinsic conceptual geometry under a generative model.

[Topic overview and comparisons](docs/modules/m2-geometry.md) · [Contents](#research-map)

<a id="m3"></a>
### Generalization & Context-Based Adaptation

<a id="paper-context-diversity"></a>
- **Context and Diversity Matter: The Emergence of In-Context Learning in World Models**<br>
  Fan Wang et al. · **ICLR 2026** · [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a46b9dcef23e9160f46d800a49a931d0-Abstract-Conference.html) · [Code](https://github.com/airs-cuhk/airsoul/tree/main/projects/MazeWorld)<br>
  Distinguishes recognizing familiar environments from learning dynamics through current experience.

<a id="paper-cadm"></a>
- **Context-aware Dynamics Model for Generalization in Model-Based Reinforcement Learning**<br>
  Kimin Lee et al. · **ICML 2020** · [Paper](https://proceedings.mlr.press/v119/lee20g.html) · [Code](https://github.com/younggyoseo/CaDM)<br>
  Infers environment context from interaction history to model changing dynamics.

<a id="paper-dreamweaver"></a>
- **Dreamweaver: Learning Compositional World Models from Pixels**<br>
  Junyeob Baek et al. · **ICLR 2025** · [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ae82a60c5ce50b5c4d18cfe3214eb684-Abstract-Conference.html)<br>
  Learns object and attribute representations for combinations beyond training configurations.

<a id="paper-dynamics-geometries"></a>
- **Dynamics Are Learned, Not Told: Semi-Supervised Discovery of Latent Dynamics Geometries For Zero-Shot Policy Adaptation**<br>
  Zhiming Xu et al. · **ICML 2026** · [Paper](https://proceedings.mlr.press/v306/xu26cq.html) · [Code](https://github.com/Mr-Wonderfool/Latent-Dynamics-Geometries)<br>
  Learns trajectory-based dynamics representations for zero-shot policy adaptation to changed dynamics.

[Topic overview and comparisons](docs/modules/m3-generalization.md) · [Contents](#research-map)

<a id="m4"></a>
### Planning & Task-Relevant Representations

<a id="paper-denoised-mdps"></a>
- **Denoised MDPs: Learning World Models Better Than the World Itself**<br>
  Tongzhou Wang et al. · **ICML 2022** · [Paper](https://proceedings.mlr.press/v162/wang22c.html)<br>
  Separates controllable and reward-relevant information from other factors in observations.

<a id="paper-dino-wm"></a>
- **DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning**<br>
  Gaoyue Zhou et al. · **ICML 2025** · [Paper](https://proceedings.mlr.press/v267/zhou25t.html)<br>
  Combines frozen visual representations, action-conditioned latent prediction, and goal-directed planning.

<a id="paper-value-equivalence"></a>
- **The Value Equivalence Principle for Model-Based Reinforcement Learning**<br>
  Christopher Grimm et al. · **NeurIPS 2020** · [Paper](https://proceedings.neurips.cc/paper/2020/hash/3bb585ea00014b0e3ebe4c6dd165a358-Abstract.html)<br>
  Formalizes models that preserve decision-relevant Bellman updates without reconstructing every world detail.

<a id="paper-what-found"></a>
- **What Has a Foundation Model Found? Using Inductive Bias to Probe for World Models**<br>
  Keyon Vafa et al. · **ICML 2025** · [Paper](https://proceedings.mlr.press/v267/vafa25a.html)<br>
  Probes learned world structure through inductive biases in new tasks.

[Topic overview and comparisons](docs/modules/m4-knowledge-use.md) · [Contents](#research-map)

<a id="m5"></a>
### Evaluation & Sim-to-Real Transfer

<a id="paper-simpler"></a>
- **Evaluating Real-World Robot Manipulation Policies in Simulation**<br>
  Xuanlin Li et al. · **CoRL 2024 (proceedings 2025)** · [Paper](https://proceedings.mlr.press/v270/li25c.html)<br>
  Evaluates whether simulation reliably predicts the relative performance of real-world manipulation policies.

<a id="paper-physical-law-perspective"></a>
- **How Far Is Video Generation from World Model: A Physical Law Perspective**<br>
  Bingyi Kang et al. · **ICML 2025** · [Paper](https://proceedings.mlr.press/v267/kang25g.html)<br>
  Tests physical prediction under extrapolation and compositional distribution shifts.

<a id="paper-rethinking-sim2real"></a>
- **Rethinking Sim2Real: Lower Fidelity Simulation Leads to Higher Sim2Real Transfer in Navigation**<br>
  Joanne Truong et al. · **CoRL 2022 (proceedings 2023)** · [Paper](https://proceedings.mlr.press/v205/truong23a.html)<br>
  Examines how simulation fidelity affects transfer in visual navigation.

<a id="paper-world-in-world"></a>
- **World-In-World: World Models in a Closed-Loop World**<br>
  Jiahan Zhang et al. · **ICLR 2026** · [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/5b4263be85820683d78675cc18d2efc7-Abstract-Conference.html)<br>
  Tests action-conditioned world models in closed-loop tasks, varying post-training data and test-time computation.

[Topic overview and comparisons](docs/modules/m5-reliability.md) · [Contents](#research-map)

<a id="m6"></a>
### Exploration & Experience Replay

<a id="paper-asid"></a>
- **ASID: Active Exploration for System Identification in Robotic Manipulation**<br>
  Marius Memmel et al. · **ICLR 2024** · [Paper](https://proceedings.iclr.cc/paper_files/paper/2024/hash/ae8afec5dabb07091d8f85128250f2ff-Abstract-Conference.html)<br>
  Combines active interaction with system identification to improve simulation models.

<a id="paper-curious-replay"></a>
- **Curious Replay for Model-based Adaptation**<br>
  Isaac Kauvar et al. · **ICML 2023** · [Paper](https://proceedings.mlr.press/v202/kauvar23a.html)<br>
  Prioritizes stored experience using novelty and prediction error to support adaptation.

<a id="paper-plan2explore"></a>
- **Planning to Explore via Self-Supervised World Models**<br>
  Ramanan Sekar et al. · **ICML 2020** · [Paper](https://proceedings.mlr.press/v119/sekar20a.html)<br>
  Learns exploration behavior from model disagreement before downstream tasks are specified.

<a id="paper-poke-strike"></a>
- **Poke and Strike: Learning Task-Informed Exploration Policies**<br>
  Marina Y. Aoyama et al. · **CoRL 2025** · [Paper](https://proceedings.mlr.press/v305/aoyama25a.html)<br>
  Selects exploratory interactions according to task-relevant information.

[Topic overview and comparisons](docs/modules/m6-adaptation.md) · [Contents](#research-map)

<a id="m7"></a>
### Predictive Architectures & Pretraining

<a id="paper-leworldmodel"></a>
- **LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels**<br>
  Lucas Maes et al. · **arXiv 2026** · [Paper](https://arxiv.org/abs/2603.19312) · [Code](https://github.com/lucas-maes/le-wm) · [Project](https://le-wm.github.io/)<br>
  Learns a compact world model end to end with joint-embedding predictive objectives.

<a id="paper-dreamerv3"></a>
- **Mastering diverse control tasks through world models**<br>
  Danijar Hafner et al. · **Nature 2025** · [Paper](https://www.nature.com/articles/s41586-025-08744-2)<br>
  Learns latent dynamics and actor-critic policies with a shared algorithm and hyperparameters across control tasks.

<a id="paper-vjepa2"></a>
- **V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning**<br>
  Mido Assran et al. · **arXiv technical report 2025** · [Paper](https://arxiv.org/abs/2506.09985)<br>
  Combines video representation pretraining with action-conditioned post-training for robot planning.

<a id="paper-jepa-wms"></a>
- **What Drives Success in Physical Planning with Joint-Embedding Predictive World Models?**<br>
  Basile Terver et al. · **TMLR 2026** · [Paper](https://arxiv.org/abs/2512.24497) · [Code](https://github.com/facebookresearch/jepa-wms)<br>
  Compares architecture, training objectives, and planners in JEPA world models.

[Topic overview and comparisons](docs/modules/m7-scaling.md) · [Contents](#research-map)

<a id="reading-route"></a>
## Reading Guide

The [12-paper reading path](docs/reading-guide.md) connects representation analysis, predictive architectures, planning, and adaptation. Each entry summarizes the method, evaluation setting, and connections to the other papers.

## Related Resources

- [Awesome World Models](https://github.com/knightnemo/Awesome-World-Models) — world-model research across application domains.
- [Awesome Deep Learning Papers](https://github.com/terryum/awesome-deep-learning-papers) — a historical deep-learning paper list; no longer maintained.
- [Awesome Machine Learning](https://github.com/josephmisiti/awesome-machine-learning) — machine-learning libraries and resources.

## Contributing

Paper suggestions and corrections are welcome through issues or pull requests. See [Contributing](CONTRIBUTING.md) for inclusion criteria and the entry format. Bibliographic records are available in [BibTeX](references.bib).

## License

Original catalog text and illustrations: [CC BY 4.0](LICENSES/CC-BY-4.0.txt). Maintenance code: [MIT](LICENSES/MIT.txt). Linked papers and external resources retain their respective licenses. See [license scope](LICENSE.md).

<!-- END GENERATED RESEARCH MAP -->
