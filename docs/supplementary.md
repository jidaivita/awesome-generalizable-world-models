<!-- BEGIN GENERATED RESEARCH MAP -->

[← Paper index](../README.md#research-map) · [Reading guide](reading-guide.md)

# Supplementary Reading

Background papers and methods from adjacent settings support the six main topics. Entries retain their original evaluation domains and explain their relevance to world-model research.

## World-model foundations

Predictive architectures and model-based RL baselines for implementing representation and planning studies.

<a id="paper-leworldmodel"></a>
### LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels

[![arXiv: 2603.19312](https://img.shields.io/badge/arXiv-2603.19312-b31b1b?style=flat-square)](https://arxiv.org/abs/2603.19312) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/lucas-maes/le-wm) [![Project: Website](https://img.shields.io/badge/Project-Website-2679b5?style=flat-square)](https://le-wm.github.io/)

Lucas Maes et al.

Earlier titles / aliases: LeWM.

- **Method:** The encoder and predictor train jointly from pixels with two losses: next-embedding prediction and a regularizer encouraging Gaussian-distributed embeddings. The resulting compact model supplies latent predictions for planning.
- **Evaluation:** Experiments cover 2D and 3D control tasks, probes of physical quantities, and surprise responses to implausible events. The reported model has approximately 15 million parameters.
- **Relevance:** An end-to-end predictive architecture provides a compact baseline for representation and planning studies.
- **Related topics:** [Representation Geometry & Symmetry](modules/m2-geometry.md) · [Planning & Task-Relevant World Models](modules/m4-knowledge-use.md)

<a id="paper-dreamerv3"></a>
### Mastering diverse control tasks through world models

[![Nature: 2025](https://img.shields.io/badge/Nature-2025-526d82?style=flat-square)](https://www.nature.com/articles/s41586-025-08744-2)

Danijar Hafner et al.

Earlier titles / aliases: DreamerV3.

- **Method:** A recurrent latent world model generates imagined trajectories for actor-critic learning. Normalization, loss balancing, and value transformations stabilize optimization across domains.
- **Evaluation:** More than 150 tasks test a shared algorithm configuration, including Minecraft learning from scratch. Model and policy parameters are learned in each environment; the shared component is the algorithm and its hyperparameters.
- **Relevance:** A broadly applicable model-based RL algorithm provides a control baseline; shared hyperparameters across tasks are distinct from transferring a trained model.
- **Related topics:** [Planning & Task-Relevant World Models](modules/m4-knowledge-use.md)

## Related representation methods

Geometry and analysis methods from language modeling and procedural planning, with their original evaluation domains retained.

<a id="paper-geoworld"></a>
### GeoWorld: Geometric World Models

[![CVPR: 2026](https://img.shields.io/badge/CVPR-2026-526d82?style=flat-square)](https://arxiv.org/abs/2602.23058) [![arXiv: 2602.23058](https://img.shields.io/badge/arXiv-2602.23058-b31b1b?style=flat-square)](https://arxiv.org/abs/2602.23058) [![Project: Website](https://img.shields.io/badge/Project-Website-2679b5?style=flat-square)](https://steve-zeyu-zhang.github.io/GeoWorld/)

Zeyu Zhang et al. · `Procedural planning`

- **Method:** Hyperbolic JEPA embeds states on a hyperbolic manifold to represent hierarchical relations. Geometric Reinforcement Learning optimizes plans on the resulting energy landscape.
- **Evaluation:** CrossTask and COIN evaluate three- and four-step procedural visual planning. This setting tests sequences of instructional actions rather than continuous physical dynamics.
- **Relevance:** Hyperbolic representations support procedural planning on instructional videos; the evaluation differs from physical dynamics prediction.
- **Related topics:** [Representation Geometry & Symmetry](modules/m2-geometry.md) · [Planning & Task-Relevant World Models](modules/m4-knowledge-use.md)

<a id="paper-smds"></a>
### Hypothesis-Driven Feature Manifold Analysis in LLMs via Supervised Multi-Dimensional Scaling

[![TMLR: 2026](https://img.shields.io/badge/TMLR-2026-526d82?style=flat-square)](https://arxiv.org/abs/2510.01025) [![arXiv: 2510.01025](https://img.shields.io/badge/arXiv-2510.01025-b31b1b?style=flat-square)](https://arxiv.org/abs/2510.01025) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/UKPLab/tmlr2026-manifold-analysis)

Federico Tiblias et al. · `LLM analysis`

Earlier titles / aliases: Shape Happens: Automatic Feature Manifold Discovery in LLMs via Supervised Multi-Dimensional Scaling; Shape Happens.

- **Method:** Supervised Multi-Dimensional Scaling fits and compares candidate feature geometries, including circles, lines, and clusters. Temporal reasoning supplies a case study for testing how these structures change with context and support model outputs.
- **Evaluation:** Experiments examine language-model families and sizes, held-out examples, and representation interventions. This is an analysis method from language modeling, included for its relevance to testing geometric hypotheses.
- **Relevance:** Geometric hypothesis testing in language models provides analysis methods for representation studies; the reported experiments do not test physical world models.
- **Related topics:** [Representation Geometry & Symmetry](modules/m2-geometry.md) · [World Model Interpretability](modules/m8-interpretability.md)

<a id="paper-origins-manifolds"></a>
### The Origins of Representation Manifolds in Large Language Models

[![arXiv: 2505.18235](https://img.shields.io/badge/arXiv-2505.18235-b31b1b?style=flat-square)](https://arxiv.org/abs/2505.18235)

Alexander Modell et al. · `LLM analysis`

- **Method:** A theoretical model connects cosine similarity between representations to distances along an underlying feature manifold. It extends a binary feature-direction account to continuous, multidimensional features.
- **Evaluation:** The paper tests its assumptions and predictions on text embeddings and language-model token activations. Its conclusions depend on the stated generative assumptions for those representations.
- **Relevance:** A theoretical account of representation geometry in language models provides background for geometric analysis.
- **Related topics:** [Representation Geometry & Symmetry](modules/m2-geometry.md)

## Simulation, transfer, and system identification

Adjacent studies of policy evaluation, simulator calibration, and task-informed interaction.

<a id="paper-asid"></a>
### ASID: Active Exploration for System Identification in Robotic Manipulation

[![ICLR: 2024](https://img.shields.io/badge/ICLR-2024-526d82?style=flat-square)](https://proceedings.iclr.cc/paper_files/paper/2024/hash/ae8afec5dabb07091d8f85128250f2ff-Abstract-Conference.html)

Marius Memmel et al.

- **Method:** An initial simulator is used to design exploratory interactions. Real observations from those interactions refine simulator parameters, after which the refined model supports control planning.
- **Evaluation:** Robotic manipulation experiments identify properties including articulation and mass and evaluate the resulting sim-to-real controllers. Identification operates within the available simulator and asset model.
- **Relevance:** Active system identification connects information gathering to simulator calibration, providing a related approach to dynamics adaptation.
- **Related topics:** [Generalization & Adaptation](modules/m3-generalization.md)

<a id="paper-simpler"></a>
### Evaluating Real-World Robot Manipulation Policies in Simulation

[![CoRL: 2024 (proceedings 2025)](https://img.shields.io/badge/CoRL-2024%20%28proceedings%202025%29-526d82?style=flat-square)](https://proceedings.mlr.press/v270/li25c.html)

Xuanlin Li et al.

Earlier titles / aliases: SIMPLER.

- **Method:** The benchmark reduces visual and control differences between real and simulated manipulation setups, then evaluates the same policies in both. Its goal is to reproduce policy comparisons and responses to distribution shifts.
- **Evaluation:** More than 1,500 paired evaluations span two robot embodiments and eight task families. The reported evidence is agreement in real and simulated policy performance, rather than training a transferable dynamics model.
- **Relevance:** Simulation-based policy ranking provides evaluation context; the paper does not evaluate generalization of a learned world model.
- **Related topics:** [Evaluation & Benchmarks](modules/m5-reliability.md)

<a id="paper-poke-strike"></a>
### Poke and Strike: Learning Task-Informed Exploration Policies

[![CoRL: 2025](https://img.shields.io/badge/CoRL-2025-526d82?style=flat-square)](https://proceedings.mlr.press/v305/aoyama25a.html)

Marina Y. Aoyama et al.

- **Method:** An exploration policy is rewarded according to how sensitive a privileged task policy is to errors in estimated object properties. An uncertainty criterion determines when to stop probing and execute the task.
- **Evaluation:** Puck striking and CartPole analyze the task relevance of physical properties; a KUKA iiwa setup tests property estimation and adjusted execution on physical objects.
- **Relevance:** Task-informed interaction links physical-property identification to manipulation, providing background on acquiring useful adaptation data.
- **Related topics:** [Generalization & Adaptation](modules/m3-generalization.md) · [Planning & Task-Relevant World Models](modules/m4-knowledge-use.md)

<a id="paper-rethinking-sim2real"></a>
### Rethinking Sim2Real: Lower Fidelity Simulation Leads to Higher Sim2Real Transfer in Navigation

[![CoRL: 2022 (proceedings 2023)](https://img.shields.io/badge/CoRL-2022%20%28proceedings%202023%29-526d82?style=flat-square)](https://proceedings.mlr.press/v205/truong23a.html)

Joanne Truong et al.

- **Method:** A controlled comparison varies simulator fidelity for visual-navigation policy learning. Simple robot-motion models fitted to real data are compared with more detailed simulation physics.
- **Evaluation:** Habitat and iGibson experiments, followed by tests on A1, AlienGo, and Spot robots, examine learning speed, overfitting to simulator errors, and real-world navigation performance.
- **Relevance:** A navigation study isolates simulation-fidelity effects on policy transfer, providing context for evaluation design.
- **Related topics:** [Generalization & Adaptation](modules/m3-generalization.md)

[Back to paper index](../README.md)

<!-- END GENERATED RESEARCH MAP -->
