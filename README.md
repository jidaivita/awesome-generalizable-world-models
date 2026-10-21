<!-- BEGIN GENERATED RESEARCH MAP -->

<a id="top"></a>
<a id="awesome-generalizable-world-models"></a>

<div align="center">

# 🌐 Awesome Generalizable World Models

[![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome) [![GitHub stars](https://img.shields.io/github/stars/jidaivita/awesome-generalizable-world-models?style=flat-square&color=526d82&label=Stars)](https://github.com/jidaivita/awesome-generalizable-world-models) [![Text: CC BY 4.0](https://img.shields.io/badge/Text-CC_BY_4.0-2679b5?style=flat-square)](LICENSES/CC-BY-4.0.txt) [![Code: MIT](https://img.shields.io/badge/Code-MIT-526d82?style=flat-square)](LICENSES/MIT.txt) [![PRs: welcome](https://img.shields.io/badge/PRs-welcome-2e8b57?style=flat-square)](CONTRIBUTING.md)

**Mechanisms, generalization, and interpretability of learned world models.**

Representation structure, latent dynamics, physical inference, and planning.

<img src="assets/world-models-cover.png" width="100%" alt="Observe, predict, generalize, and interpret: a tabletop pushing example with images, actions, future states, new objects, and representation interventions">

[Research Map](#research-map) · [Reading Guide](docs/reading-guide.md) · [BibTeX](references.bib) · [Related Resources](#related-resources) · [Contributing](CONTRIBUTING.md)

</div>

---

<a id="start-here"></a>
<a id="research-map"></a>
## Contents

| Topic | Coverage | Papers |
| :--- | :--- | ---: |
| 🧭 [Generalization & Adaptation](#m3) | Unseen compositions, dynamics shifts, task transfer, and adaptation. | 11 |
| 🔬 [World Model Interpretability](#m8) | Physical variables, causal interventions, and interpretable model design. | 4 |
| 🧩 [Structured & Compositional Representations](#m1) | Objects, relations, and modular transition mechanisms. | 4 |
| 📐 [Representation Geometry & Symmetry](#m2) | Latent geometry, learned transformations, and symmetry-based dynamics. | 5 |
| 🎯 [Planning & Task-Relevant World Models](#m4) | Goal-directed prediction, task abstraction, and model-based action selection. | 6 |
| 📊 [Evaluation & Benchmarks](#m5) | Compositional prediction, physical inference, and closed-loop validity. | 6 |

36 papers across six topics · 9 supplementary papers · 45 papers in total.

Entries describe the mechanism, evaluation setting, and evidence for each contribution. New papers extend these six topics through a distinct method, analysis, or test of generalization. Each paper has one primary topic and is listed alphabetically within it.

<a id="papers"></a>
## Papers

<a id="m3"></a>
### 🧭 Generalization & Adaptation

Unseen compositions, dynamics shifts, task transfer, and adaptation.

<a id="paper-behavior-invariant-wm"></a>
- **Behavior-Invariant Task Representations** — [Behavior-Invariant Task Representation Learning with Transformer-based World Models for Offline Meta-Reinforcement Learning](https://proceedings.mlr.press/v306/qian26o.html)<br>
  [![ICML: 2026](https://img.shields.io/badge/ICML-2026-526d82?style=flat-square)](https://proceedings.mlr.press/v306/qian26o.html) [![arXiv: 2606.00780](https://img.shields.io/badge/arXiv-2606.00780-b31b1b?style=flat-square)](https://arxiv.org/abs/2606.00780) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/QianFY/MetaSTAR)<br>
  Fuyuan Qian et al. · Learns task representations invariant to behavior policy for offline-to-online adaptation.

<a id="paper-considering-context"></a>
- **Considering Context** — [When World Models Need Context Encoders](https://arxiv.org/abs/2610.06651)<br>
  [![arXiv: 2610.06651](https://img.shields.io/badge/arXiv-2610.06651-b31b1b?style=flat-square)](https://arxiv.org/abs/2610.06651)<br>
  Oleg Smirnov et al. · Measures the prediction information supplied by context beyond an agent's history.

<a id="paper-context-diversity"></a>
- **Context and Diversity Matter** — [The Emergence of In-Context Learning in World Models](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a46b9dcef23e9160f46d800a49a931d0-Abstract-Conference.html)<br>
  [![ICLR: 2026](https://img.shields.io/badge/ICLR-2026-526d82?style=flat-square)](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a46b9dcef23e9160f46d800a49a931d0-Abstract-Conference.html) [![arXiv: 2509.22353](https://img.shields.io/badge/arXiv-2509.22353-b31b1b?style=flat-square)](https://arxiv.org/abs/2509.22353) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/airs-cuhk/airsoul/tree/main/projects/MazeWorld)<br>
  Fan Wang et al. · Distinguishes recognizing familiar environments from learning dynamics through current experience.

<a id="paper-cadm"></a>
- **CaDM** — [Context-aware Dynamics Model for Generalization in Model-Based Reinforcement Learning](https://proceedings.mlr.press/v119/lee20g.html)<br>
  [![ICML: 2020](https://img.shields.io/badge/ICML-2020-526d82?style=flat-square)](https://proceedings.mlr.press/v119/lee20g.html) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/younggyoseo/CaDM) [![Project: Website](https://img.shields.io/badge/Project-Website-2679b5?style=flat-square)](https://sites.google.com/view/cadm)<br>
  Kimin Lee et al. · Infers environment context from interaction history to model changing dynamics.

<a id="paper-curious-replay"></a>
- **Curious Replay** — [Curious Replay for Model-based Adaptation](https://proceedings.mlr.press/v202/kauvar23a.html)<br>
  [![ICML: 2023](https://img.shields.io/badge/ICML-2023-526d82?style=flat-square)](https://proceedings.mlr.press/v202/kauvar23a.html) [![arXiv: 2306.15934](https://img.shields.io/badge/arXiv-2306.15934-b31b1b?style=flat-square)](https://arxiv.org/abs/2306.15934) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/AutonomousAgentsLab/curiousreplay)<br>
  Isaac Kauvar et al. · Prioritizes stored experience using novelty and prediction error to support adaptation.

<a id="paper-dreamweaver"></a>
- **Dreamweaver** — [Learning Compositional World Models from Pixels](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ae82a60c5ce50b5c4d18cfe3214eb684-Abstract-Conference.html)<br>
  [![ICLR: 2025](https://img.shields.io/badge/ICLR-2025-526d82?style=flat-square)](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ae82a60c5ce50b5c4d18cfe3214eb684-Abstract-Conference.html) [![arXiv: 2501.14174](https://img.shields.io/badge/arXiv-2501.14174-b31b1b?style=flat-square)](https://arxiv.org/abs/2501.14174) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/ahn-ml/dreamweaver-release) [![Project: Website](https://img.shields.io/badge/Project-Website-2679b5?style=flat-square)](https://dion-jy.github.io/dreamweaver-website/)<br>
  Junyeob Baek et al. · Learns object and attribute representations for combinations beyond training configurations.

<a id="paper-dynamics-geometries"></a>
- **Latent Dynamics Geometries** — [Dynamics Are Learned, Not Told: Semi-Supervised Discovery of Latent Dynamics Geometries For Zero-Shot Policy Adaptation](https://proceedings.mlr.press/v306/xu26cq.html)<br>
  [![ICML: 2026](https://img.shields.io/badge/ICML-2026-526d82?style=flat-square)](https://proceedings.mlr.press/v306/xu26cq.html) [![arXiv: 2606.02280](https://img.shields.io/badge/arXiv-2606.02280-b31b1b?style=flat-square)](https://arxiv.org/abs/2606.02280) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/Mr-Wonderfool/Latent-Dynamics-Geometries)<br>
  Zhiming Xu et al. · Learns trajectory-based dynamics representations for zero-shot policy adaptation to changed dynamics.

<a id="paper-general-agents"></a>
- **[General agents need world models](https://proceedings.mlr.press/v267/richens25a.html)**<br>
  [![ICML: 2025](https://img.shields.io/badge/ICML-2025-526d82?style=flat-square)](https://proceedings.mlr.press/v267/richens25a.html)<br>
  Jonathan Richens et al. · `Theory` · Relates generalization across goal-directed tasks to predictive models extractable from a policy.

<a id="paper-wm3c"></a>
- **WM3C** — [Modeling Unseen Environments with Language-guided Composable Causal Components in Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2025/hash/79d86433c2acd12b6fa98553435d226e-Abstract-Conference.html)<br>
  [![ICLR: 2025](https://img.shields.io/badge/ICLR-2025-526d82?style=flat-square)](https://proceedings.iclr.cc/paper_files/paper/2025/hash/79d86433c2acd12b6fa98553435d226e-Abstract-Conference.html) [![arXiv: 2505.08361](https://img.shields.io/badge/arXiv-2505.08361-b31b1b?style=flat-square)](https://arxiv.org/abs/2505.08361)<br>
  Xinyue Wang et al. · Uses language-guided causal components to model and adapt to unseen environments.

<a id="paper-howm"></a>
- **HOWM** — [Toward Compositional Generalization in Object-Oriented World Modeling](https://proceedings.mlr.press/v162/zhao22b.html)<br>
  [![ICML: 2022](https://img.shields.io/badge/ICML-2022-526d82?style=flat-square)](https://proceedings.mlr.press/v162/zhao22b.html) [![arXiv: 2204.13661](https://img.shields.io/badge/arXiv-2204.13661-b31b1b?style=flat-square)](https://arxiv.org/abs/2204.13661) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/linfeng-z/HOWM)<br>
  Linfeng Zhao et al. · Formalizes object composition and learns a differentiable world model for unseen combinations.

<a id="paper-wombet"></a>
- **WOMBET** — [World Model-based Experience Transfer for Robust and Sample-efficient Reinforcement Learning](https://proceedings.mlr.press/v331/kim26a.html)<br>
  [![L4DC: 2026](https://img.shields.io/badge/L4DC-2026-526d82?style=flat-square)](https://proceedings.mlr.press/v331/kim26a.html) [![arXiv: 2604.08958](https://img.shields.io/badge/arXiv-2604.08958-b31b1b?style=flat-square)](https://arxiv.org/abs/2604.08958)<br>
  Mintae Kim et al. · Transfers model-generated experience from a source task to target-task fine-tuning.

[Topic overview and comparisons](docs/modules/m3-generalization.md) · [Contents](#research-map)

<a id="m8"></a>
### 🔬 World Model Interpretability

Physical variables, causal interventions, and interpretable model design.

<a id="paper-physically-interpretable"></a>
- **Physically Interpretable World Models** — [Four Principles for Physically Interpretable World Models](https://proceedings.mlr.press/v288/peper25a.html)<br>
  [![NeuS: 2025](https://img.shields.io/badge/NeuS-2025-526d82?style=flat-square)](https://proceedings.mlr.press/v288/peper25a.html) [![arXiv: 2503.02143](https://img.shields.io/badge/arXiv-2503.02143-b31b1b?style=flat-square)](https://arxiv.org/abs/2503.02143) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/Trustworthy-Engineered-Autonomy-Lab/piwm-principles)<br>
  Jordan Peper et al. · Organizes latent representations and supervision around physical meaning.

<a id="paper-interpreting-physics"></a>
- **Interpreting Physics** — [Interpreting Physics in Video World Models](https://proceedings.mlr.press/v306/joseph26a.html)<br>
  [![ICML: 2026](https://img.shields.io/badge/ICML-2026-526d82?style=flat-square)](https://proceedings.mlr.press/v306/joseph26a.html) [![arXiv: 2602.07050](https://img.shields.io/badge/arXiv-2602.07050-b31b1b?style=flat-square)](https://arxiv.org/abs/2602.07050) [![Project: Website](https://img.shields.io/badge/Project-Website-2679b5?style=flat-square)](https://www.soniajoseph.ai/interpreting-ph/)<br>
  Sonia Joseph et al. · Analyzes the organization of physical information through layer-wise probes, subspaces, and interventions.

<a id="paper-probing-rl-world-models"></a>
- **Probing RL World Models** — [What Do World Models Learn in RL? Probing Latent Representations in Learned Environment Simulators](https://openreview.net/forum?id=VE7JJLVKG1)<br>
  [![ICLR: 2026 World Models Workshop](https://img.shields.io/badge/ICLR-2026%20World%20Models%20Workshop-7657a3?style=flat-square)](https://openreview.net/forum?id=VE7JJLVKG1) [![arXiv: 2603.21546](https://img.shields.io/badge/arXiv-2603.21546-b31b1b?style=flat-square)](https://arxiv.org/abs/2603.21546)<br>
  Xinyu Zhang · Probes and intervenes on game-state representations in IRIS and DIAMOND.

<a id="paper-what-found"></a>
- **What Has a Foundation Model Found?** — [What Has a Foundation Model Found? Using Inductive Bias to Probe for World Models](https://proceedings.mlr.press/v267/vafa25a.html)<br>
  [![ICML: 2025](https://img.shields.io/badge/ICML-2025-526d82?style=flat-square)](https://proceedings.mlr.press/v267/vafa25a.html) [![arXiv: 2507.06952](https://img.shields.io/badge/arXiv-2507.06952-b31b1b?style=flat-square)](https://arxiv.org/abs/2507.06952) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/keyonvafa/inductive-bias-probes)<br>
  Keyon Vafa et al. · Probes learned world structure through inductive biases in new tasks.

[Topic overview and comparisons](docs/modules/m8-interpretability.md) · [Contents](#research-map)

<a id="m1"></a>
### 🧩 Structured & Compositional Representations

Objects, relations, and modular transition mechanisms.

<a id="paper-causal-jepa"></a>
- **Causal-JEPA** — [Learning World Models through Object-Level Latent Masking](https://proceedings.mlr.press/v306/nam26c.html)<br>
  [![ICML: 2026](https://img.shields.io/badge/ICML-2026-526d82?style=flat-square)](https://proceedings.mlr.press/v306/nam26c.html) [![arXiv: 2602.11389](https://img.shields.io/badge/arXiv-2602.11389-b31b1b?style=flat-square)](https://arxiv.org/abs/2602.11389) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/galilai-group/cjepa)<br>
  Heejeong Nam et al. · Combines object-level latent masking with joint-embedding predictive learning.

<a id="paper-cswm"></a>
- **C-SWM** — [Contrastive Learning of Structured World Models](https://arxiv.org/abs/1911.12247)<br>
  [![ICLR: 2020](https://img.shields.io/badge/ICLR-2020-526d82?style=flat-square)](https://arxiv.org/abs/1911.12247) [![arXiv: 1911.12247](https://img.shields.io/badge/arXiv-1911.12247-b31b1b?style=flat-square)](https://arxiv.org/abs/1911.12247) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/tkipf/c-swm)<br>
  Thomas Kipf et al. · Learns object-centric representations and relational dynamics with a contrastive objective.

<a id="paper-nri"></a>
- **NRI** — [Neural Relational Inference for Interacting Systems](https://proceedings.mlr.press/v80/kipf18a.html)<br>
  [![ICML: 2018](https://img.shields.io/badge/ICML-2018-526d82?style=flat-square)](https://proceedings.mlr.press/v80/kipf18a.html) [![arXiv: 1802.04687](https://img.shields.io/badge/arXiv-1802.04687-b31b1b?style=flat-square)](https://arxiv.org/abs/1802.04687) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/ethanfetaya/NRI)<br>
  Thomas Kipf et al. · Infers latent interaction graphs from trajectories with a graph-based dynamics decoder.

<a id="paper-spartan"></a>
- **SPARTAN** — [A Sparse Transformer World Model Attending to What Matters](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e2c33c1753e1f1924f5560b11fc4444f-Abstract-Conference.html)<br>
  [![NeurIPS: 2025](https://img.shields.io/badge/NeurIPS-2025-526d82?style=flat-square)](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e2c33c1753e1f1924f5560b11fc4444f-Abstract-Conference.html) [![arXiv: 2411.06890](https://img.shields.io/badge/arXiv-2411.06890-b31b1b?style=flat-square)](https://arxiv.org/abs/2411.06890)<br>
  Anson Lei et al. · Uses sparse, context-dependent interactions to adapt to changes in mechanisms.

[Topic overview and comparisons](docs/modules/m1-structure.md) · [Contents](#research-map)

<a id="m2"></a>
### 📐 Representation Geometry & Symmetry

Latent geometry, learned transformations, and symmetry-based dynamics.

<a id="paper-grwm"></a>
- **GRWM** — [Cloning Deterministic Worlds: The Critical Role of Latent Geometry in Long-Horizon World Models](https://openaccess.thecvf.com/content/CVPR2026/html/Xia_Cloning_Deterministic_Worlds_The_Critical_Role_of_Latent_Geometry_in_CVPR_2026_paper.html)<br>
  [![CVPR: 2026](https://img.shields.io/badge/CVPR-2026-526d82?style=flat-square)](https://openaccess.thecvf.com/content/CVPR2026/html/Xia_Cloning_Deterministic_Worlds_The_Critical_Role_of_Latent_Geometry_in_CVPR_2026_paper.html) [![arXiv: 2510.26782](https://img.shields.io/badge/arXiv-2510.26782-b31b1b?style=flat-square)](https://arxiv.org/abs/2510.26782) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/XiaFire/Clone_Deterministic_Environment) [![Project: Website](https://img.shields.io/badge/Project-Website-2679b5?style=flat-square)](https://xiafire.github.io/grwm-project-page/)<br>
  Zaishuo Xia et al. · Regularizes latent geometry and uses temporal context for long-horizon prediction in deterministic environments.

<a id="paper-flowm"></a>
- **FloWM** — [Flow Equivariant World Models: Structured Memory for Dynamic Environments](https://proceedings.mlr.press/v306/lillemark26a.html)<br>
  [![ICML: 2026](https://img.shields.io/badge/ICML-2026-526d82?style=flat-square)](https://proceedings.mlr.press/v306/lillemark26a.html) [![arXiv: 2601.01075](https://img.shields.io/badge/arXiv-2601.01075-b31b1b?style=flat-square)](https://arxiv.org/abs/2601.01075) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/hlillemark/flowm) [![Project: Website](https://img.shields.io/badge/Project-Website-2679b5?style=flat-square)](https://flowequivariantworldmodels.github.io/)<br>
  Hansen Lillemark et al. · Updates spatial latent memory with self-motion and object-motion flows for prediction under partial observability.

<a id="paper-group-latents"></a>
- **Group-Structured Latents** — [Learning Abstract World Models with a Group-Structured Latent Space](https://arxiv.org/abs/2506.01529)<br>
  [![arXiv: 2506.01529](https://img.shields.io/badge/arXiv-2506.01529-b31b1b?style=flat-square)](https://arxiv.org/abs/2506.01529) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/khanhvu207/world-models-group-latents)<br>
  Thomas Delliaux et al. · Encodes known symmetries, such as translation and rotation, as geometric inductive biases.

<a id="paper-group-structure"></a>
- **Learning Group Structure** — [Learning Disentangled Representations and Group Structure of Dynamical Environments](https://proceedings.neurips.cc/paper/2020/hash/e449b9317dad920c0dd5ad0a2a2d5e49-Abstract.html)<br>
  [![NeurIPS: 2020](https://img.shields.io/badge/NeurIPS-2020-526d82?style=flat-square)](https://proceedings.neurips.cc/paper/2020/hash/e449b9317dad920c0dd5ad0a2a2d5e49-Abstract.html) [![arXiv: 2002.06991](https://img.shields.io/badge/arXiv-2002.06991-b31b1b?style=flat-square)](https://arxiv.org/abs/2002.06991) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/IndustAI/learning-group-structure)<br>
  Robin Quessard et al. · Learns latent group transformations and disentangled subspaces from interaction sequences for long-horizon prediction.

<a id="paper-sen"></a>
- **SEN** — [Learning Symmetric Embeddings for Equivariant World Models](https://proceedings.mlr.press/v162/park22a.html)<br>
  [![ICML: 2022](https://img.shields.io/badge/ICML-2022-526d82?style=flat-square)](https://proceedings.mlr.press/v162/park22a.html) [![arXiv: 2204.11371](https://img.shields.io/badge/arXiv-2204.11371-b31b1b?style=flat-square)](https://arxiv.org/abs/2204.11371) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/jypark0/sen)<br>
  Jung Yeon Park et al. · Learns an observation embedding compatible with known latent symmetries for equivariant transition prediction.

[Topic overview and comparisons](docs/modules/m2-geometry.md) · [Contents](#research-map)

<a id="m4"></a>
### 🎯 Planning & Task-Relevant World Models

Goal-directed prediction, task abstraction, and model-based action selection.

<a id="paper-denoised-mdps"></a>
- **Denoised MDPs** — [Learning World Models Better Than the World Itself](https://proceedings.mlr.press/v162/wang22c.html)<br>
  [![ICML: 2022](https://img.shields.io/badge/ICML-2022-526d82?style=flat-square)](https://proceedings.mlr.press/v162/wang22c.html) [![arXiv: 2206.15477](https://img.shields.io/badge/arXiv-2206.15477-b31b1b?style=flat-square)](https://arxiv.org/abs/2206.15477) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/facebookresearch/denoised_mdp) [![Project: Website](https://img.shields.io/badge/Project-Website-2679b5?style=flat-square)](https://www.tongzhouwang.info/denoised_mdp/)<br>
  Tongzhou Wang et al. · Separates controllable and reward-relevant information from other factors in observations.

<a id="paper-dino-wm"></a>
- **DINO-WM** — [World Models on Pre-trained Visual Features enable Zero-shot Planning](https://proceedings.mlr.press/v267/zhou25t.html)<br>
  [![ICML: 2025](https://img.shields.io/badge/ICML-2025-526d82?style=flat-square)](https://proceedings.mlr.press/v267/zhou25t.html) [![arXiv: 2411.04983](https://img.shields.io/badge/arXiv-2411.04983-b31b1b?style=flat-square)](https://arxiv.org/abs/2411.04983) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/gaoyuezhou/dino_wm) [![Project: Website](https://img.shields.io/badge/Project-Website-2679b5?style=flat-square)](https://dino-wm.github.io/)<br>
  Gaoyue Zhou et al. · Combines frozen visual representations, action-conditioned latent prediction, and goal-directed planning.

<a id="paper-plan2explore"></a>
- **Plan2Explore** — [Planning to Explore via Self-Supervised World Models](https://proceedings.mlr.press/v119/sekar20a.html)<br>
  [![ICML: 2020](https://img.shields.io/badge/ICML-2020-526d82?style=flat-square)](https://proceedings.mlr.press/v119/sekar20a.html) [![arXiv: 2005.05960](https://img.shields.io/badge/arXiv-2005.05960-b31b1b?style=flat-square)](https://arxiv.org/abs/2005.05960) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/ramanans1/plan2explore) [![Project: Website](https://img.shields.io/badge/Project-Website-2679b5?style=flat-square)](https://ramanans1.github.io/plan2explore/)<br>
  Ramanan Sekar et al. · Learns exploration behavior from model disagreement before downstream tasks are specified.

<a id="paper-value-equivalence"></a>
- **Value Equivalence** — [The Value Equivalence Principle for Model-Based Reinforcement Learning](https://proceedings.neurips.cc/paper/2020/hash/3bb585ea00014b0e3ebe4c6dd165a358-Abstract.html)<br>
  [![NeurIPS: 2020](https://img.shields.io/badge/NeurIPS-2020-526d82?style=flat-square)](https://proceedings.neurips.cc/paper/2020/hash/3bb585ea00014b0e3ebe4c6dd165a358-Abstract.html)<br>
  Christopher Grimm et al. · Formalizes models that preserve decision-relevant Bellman updates without reconstructing every world detail.

<a id="paper-vjepa2"></a>
- **V-JEPA 2** — [Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://arxiv.org/abs/2506.09985)<br>
  [![arXiv: 2506.09985](https://img.shields.io/badge/arXiv-2506.09985-b31b1b?style=flat-square)](https://arxiv.org/abs/2506.09985) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/facebookresearch/vjepa2) [![Project: Website](https://img.shields.io/badge/Project-Website-2679b5?style=flat-square)](https://ai.meta.com/research/vjepa/)<br>
  Mido Assran et al. · Combines video representation pretraining with action-conditioned post-training for robot planning.

<a id="paper-jepa-wms"></a>
- **JEPA-WMs** — [What Drives Success in Physical Planning with Joint-Embedding Predictive World Models?](https://openreview.net/forum?id=cHZn5Gdh8e)<br>
  [![TMLR: 2026](https://img.shields.io/badge/TMLR-2026-526d82?style=flat-square)](https://openreview.net/forum?id=cHZn5Gdh8e) [![arXiv: 2512.24497](https://img.shields.io/badge/arXiv-2512.24497-b31b1b?style=flat-square)](https://arxiv.org/abs/2512.24497) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/facebookresearch/jepa-wms)<br>
  Basile Terver et al. · Compares architecture, training objectives, and planners in JEPA world models.

[Topic overview and comparisons](docs/modules/m4-knowledge-use.md) · [Contents](#research-map)

<a id="m5"></a>
### 📊 Evaluation & Benchmarks

Compositional prediction, physical inference, and closed-loop validity.

<a id="paper-physical-law-perspective"></a>
- **A Physical Law Perspective** — [How Far Is Video Generation from World Model: A Physical Law Perspective](https://proceedings.mlr.press/v267/kang25g.html)<br>
  [![ICML: 2025](https://img.shields.io/badge/ICML-2025-526d82?style=flat-square)](https://proceedings.mlr.press/v267/kang25g.html) [![arXiv: 2411.02385](https://img.shields.io/badge/arXiv-2411.02385-b31b1b?style=flat-square)](https://arxiv.org/abs/2411.02385) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/phyworld/phyworld) [![Project: Website](https://img.shields.io/badge/Project-Website-2679b5?style=flat-square)](https://phyworld.github.io/)<br>
  Bingyi Kang et al. · Tests physical prediction under extrapolation and compositional distribution shifts.

<a id="paper-svib"></a>
- **SVIB** — [Imagine the Unseen World: A Benchmark for Systematic Generalization in Visual World Models](https://proceedings.nips.cc/paper_files/paper/2023/hash/58af908d6293810f1a29e69bf723dc48-Abstract-Datasets_and_Benchmarks.html)<br>
  [![NeurIPS: 2023 Datasets & Benchmarks](https://img.shields.io/badge/NeurIPS-2023%20Datasets%20%26%20Benchmarks-526d82?style=flat-square)](https://proceedings.nips.cc/paper_files/paper/2023/hash/58af908d6293810f1a29e69bf723dc48-Abstract-Datasets_and_Benchmarks.html) [![arXiv: 2311.09064](https://img.shields.io/badge/arXiv-2311.09064-b31b1b?style=flat-square)](https://arxiv.org/abs/2311.09064) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/systematic-visual-imagination/svib) [![Project: Website](https://img.shields.io/badge/Project-Website-2679b5?style=flat-square)](https://systematic-visual-imagination.github.io/)<br>
  Yeongbin Kim et al. · Controls training-factor coverage to test visual prediction on unseen combinations.

<a id="paper-physion-pp"></a>
- **Physion++** — [Evaluating Physical Scene Understanding that Requires Online Inference of Different Physical Properties](https://proceedings.nips.cc/paper_files/paper/2023/hash/d3e8011c912e651ab2a76e7935a1e464-Abstract-Datasets_and_Benchmarks.html)<br>
  [![NeurIPS: 2023 Datasets & Benchmarks](https://img.shields.io/badge/NeurIPS-2023%20Datasets%20%26%20Benchmarks-526d82?style=flat-square)](https://proceedings.nips.cc/paper_files/paper/2023/hash/d3e8011c912e651ab2a76e7935a1e464-Abstract-Datasets_and_Benchmarks.html) [![arXiv: 2306.15668](https://img.shields.io/badge/arXiv-2306.15668-b31b1b?style=flat-square)](https://arxiv.org/abs/2306.15668) [![Project: Website](https://img.shields.io/badge/Project-Website-2679b5?style=flat-square)](https://dingmyu.github.io/physion_v2/)<br>
  Hsiao-Yu Tung et al. · Tests physical predictions that require inferring hidden object properties from observed interactions.

<a id="paper-physion"></a>
- **Physion** — [Evaluating Physical Prediction from Vision in Humans and Machines](https://datasets-benchmarks-proceedings.neurips.cc/paper_files/paper/2021/hash/d09bf41544a3365a46c9077ebb5e35c3-Abstract-round1.html)<br>
  [![NeurIPS: 2021 Datasets & Benchmarks](https://img.shields.io/badge/NeurIPS-2021%20Datasets%20%26%20Benchmarks-526d82?style=flat-square)](https://datasets-benchmarks-proceedings.neurips.cc/paper_files/paper/2021/hash/d09bf41544a3365a46c9077ebb5e35c3-Abstract-round1.html) [![arXiv: 2106.08261](https://img.shields.io/badge/arXiv-2106.08261-b31b1b?style=flat-square)](https://arxiv.org/abs/2106.08261) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/cogtoolslab/physics-benchmarking-neurips2021) [![Project: Website](https://img.shields.io/badge/Project-Website-2679b5?style=flat-square)](https://physion-benchmark.github.io/)<br>
  Daniel Bear et al. · Tests future object-contact prediction from video across eight simulated physical scenarios.

<a id="paper-world-in-world"></a>
- **World-In-World** — [World Models in a Closed-Loop World](https://proceedings.iclr.cc/paper_files/paper/2026/hash/5b4263be85820683d78675cc18d2efc7-Abstract-Conference.html)<br>
  [![ICLR: 2026](https://img.shields.io/badge/ICLR-2026-526d82?style=flat-square)](https://proceedings.iclr.cc/paper_files/paper/2026/hash/5b4263be85820683d78675cc18d2efc7-Abstract-Conference.html) [![arXiv: 2510.18135](https://img.shields.io/badge/arXiv-2510.18135-b31b1b?style=flat-square)](https://arxiv.org/abs/2510.18135) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/World-In-World/world-in-world) [![Project: Website](https://img.shields.io/badge/Project-Website-2679b5?style=flat-square)](https://world-in-world.github.io/)<br>
  Jiahan Zhang et al. · Tests action-conditioned world models in closed-loop tasks, varying post-training data and test-time computation.

<a id="paper-worldgym"></a>
- **WorldGym** — [World Model as An Environment for Policy Evaluation](https://proceedings.iclr.cc/paper_files/paper/2026/hash/7f5e909ac0324db03506b380c695ffaf-Abstract-Conference.html)<br>
  [![ICLR: 2026](https://img.shields.io/badge/ICLR-2026-526d82?style=flat-square)](https://proceedings.iclr.cc/paper_files/paper/2026/hash/7f5e909ac0324db03506b380c695ffaf-Abstract-Conference.html) [![arXiv: 2506.00613](https://img.shields.io/badge/arXiv-2506.00613-b31b1b?style=flat-square)](https://arxiv.org/abs/2506.00613) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/world-model-eval/world-model-eval) [![Project: Website](https://img.shields.io/badge/Project-Website-2679b5?style=flat-square)](https://world-model-eval.github.io/abstract.html)<br>
  Julian Quevedo et al. · Tests whether policy success rates and rankings in a learned video environment track real-robot evaluations.

[Topic overview and comparisons](docs/modules/m5-reliability.md) · [Contents](#research-map)

<a id="m6"></a>
<a id="m7"></a>
## Supplementary Reading

[Supplementary Reading](docs/supplementary.md) covers world-model foundations, related representation methods, and simulation or system-identification studies. Each entry states its connection to the main topics.

<details>
<summary>Browse supplementary papers</summary>

<a id="paper-asid"></a>
- **ASID** — [Active Exploration for System Identification in Robotic Manipulation](https://proceedings.iclr.cc/paper_files/paper/2024/hash/ae8afec5dabb07091d8f85128250f2ff-Abstract-Conference.html)<br>
  [![ICLR: 2024](https://img.shields.io/badge/ICLR-2024-526d82?style=flat-square)](https://proceedings.iclr.cc/paper_files/paper/2024/hash/ae8afec5dabb07091d8f85128250f2ff-Abstract-Conference.html) [![arXiv: 2404.12308](https://img.shields.io/badge/arXiv-2404.12308-b31b1b?style=flat-square)](https://arxiv.org/abs/2404.12308) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/WEIRDLabUW/asid) [![Project: Website](https://img.shields.io/badge/Project-Website-2679b5?style=flat-square)](https://weirdlabuw.github.io/asid/)<br>
  Marius Memmel et al. · Combines active interaction with system identification to improve simulation models.

<a id="paper-simpler"></a>
- **SIMPLER** — [Evaluating Real-World Robot Manipulation Policies in Simulation](https://proceedings.mlr.press/v270/li25c.html)<br>
  [![CoRL: 2024 (proceedings 2025)](https://img.shields.io/badge/CoRL-2024%20%28proceedings%202025%29-526d82?style=flat-square)](https://proceedings.mlr.press/v270/li25c.html) [![arXiv: 2405.05941](https://img.shields.io/badge/arXiv-2405.05941-b31b1b?style=flat-square)](https://arxiv.org/abs/2405.05941) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/simpler-env/SimplerEnv) [![Project: Website](https://img.shields.io/badge/Project-Website-2679b5?style=flat-square)](https://simpler-env.github.io/)<br>
  Xuanlin Li et al. · Evaluates whether simulation reliably predicts the relative performance of real-world manipulation policies.

<a id="paper-geoworld"></a>
- **GeoWorld** — [Geometric World Models](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_GeoWorld_Geometric_World_Models_CVPR_2026_paper.html)<br>
  [![CVPR: 2026](https://img.shields.io/badge/CVPR-2026-526d82?style=flat-square)](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_GeoWorld_Geometric_World_Models_CVPR_2026_paper.html) [![arXiv: 2602.23058](https://img.shields.io/badge/arXiv-2602.23058-b31b1b?style=flat-square)](https://arxiv.org/abs/2602.23058) [![Project: Website](https://img.shields.io/badge/Project-Website-2679b5?style=flat-square)](https://steve-zeyu-zhang.github.io/GeoWorld/)<br>
  Zeyu Zhang et al. · `Procedural planning` · Uses hyperbolic latent representations and geometric optimization for procedural planning on CrossTask and COIN.

<a id="paper-smds"></a>
- **SMDS** — [Hypothesis-Driven Feature Manifold Analysis in LLMs via Supervised Multi-Dimensional Scaling](https://openreview.net/forum?id=vCKZ40YYPr)<br>
  [![TMLR: 2026](https://img.shields.io/badge/TMLR-2026-526d82?style=flat-square)](https://openreview.net/forum?id=vCKZ40YYPr) [![arXiv: 2510.01025](https://img.shields.io/badge/arXiv-2510.01025-b31b1b?style=flat-square)](https://arxiv.org/abs/2510.01025) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/UKPLab/tmlr2026-manifold-analysis)<br>
  Federico Tiblias et al. · `LLM analysis` · Compares geometric hypotheses and their functional effects in language-model representations.

<a id="paper-leworldmodel"></a>
- **LeWorldModel** — [Stable End-to-End Joint-Embedding Predictive Architecture from Pixels](https://arxiv.org/abs/2603.19312)<br>
  [![arXiv: 2603.19312](https://img.shields.io/badge/arXiv-2603.19312-b31b1b?style=flat-square)](https://arxiv.org/abs/2603.19312) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/lucas-maes/le-wm) [![Project: Website](https://img.shields.io/badge/Project-Website-2679b5?style=flat-square)](https://le-wm.github.io/)<br>
  Lucas Maes et al. · Learns a compact world model end to end with joint-embedding predictive objectives.

<a id="paper-dreamerv3"></a>
- **DreamerV3** — [Mastering diverse control tasks through world models](https://www.nature.com/articles/s41586-025-08744-2)<br>
  [![Nature: 2025](https://img.shields.io/badge/Nature-2025-526d82?style=flat-square)](https://www.nature.com/articles/s41586-025-08744-2) [![arXiv: 2301.04104](https://img.shields.io/badge/arXiv-2301.04104-b31b1b?style=flat-square)](https://arxiv.org/abs/2301.04104) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/danijar/dreamerv3) [![Project: Website](https://img.shields.io/badge/Project-Website-2679b5?style=flat-square)](https://danijar.com/project/dreamerv3/)<br>
  Danijar Hafner et al. · Learns latent dynamics and actor-critic policies with a shared algorithm and hyperparameters across control tasks.

<a id="paper-poke-strike"></a>
- **Poke and Strike** — [Learning Task-Informed Exploration Policies](https://proceedings.mlr.press/v305/aoyama25a.html)<br>
  [![CoRL: 2025](https://img.shields.io/badge/CoRL-2025-526d82?style=flat-square)](https://proceedings.mlr.press/v305/aoyama25a.html) [![arXiv: 2509.00178](https://img.shields.io/badge/arXiv-2509.00178-b31b1b?style=flat-square)](https://arxiv.org/abs/2509.00178) [![Project: Website](https://img.shields.io/badge/Project-Website-2679b5?style=flat-square)](https://marina-aoyama.github.io/poke-and-strike/)<br>
  Marina Y. Aoyama et al. · Selects exploratory interactions according to task-relevant information.

<a id="paper-rethinking-sim2real"></a>
- **Rethinking Sim2Real** — [Lower Fidelity Simulation Leads to Higher Sim2Real Transfer in Navigation](https://proceedings.mlr.press/v205/truong23a.html)<br>
  [![CoRL: 2022 (proceedings 2023)](https://img.shields.io/badge/CoRL-2022%20%28proceedings%202023%29-526d82?style=flat-square)](https://proceedings.mlr.press/v205/truong23a.html) [![arXiv: 2207.10821](https://img.shields.io/badge/arXiv-2207.10821-b31b1b?style=flat-square)](https://arxiv.org/abs/2207.10821) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/joannetruong/habitat-lab/tree/kin2dyn) [![Project: Website](https://img.shields.io/badge/Project-Website-2679b5?style=flat-square)](https://joannetruong.com/projects/kin2dyn.html)<br>
  Joanne Truong et al. · Examines how simulation fidelity affects transfer in visual navigation.

<a id="paper-origins-manifolds"></a>
- **Representation Manifolds** — [The Origins of Representation Manifolds in Large Language Models](https://arxiv.org/abs/2505.18235)<br>
  [![arXiv: 2505.18235](https://img.shields.io/badge/arXiv-2505.18235-b31b1b?style=flat-square)](https://arxiv.org/abs/2505.18235) [![Code: GitHub](https://img.shields.io/badge/Code-GitHub-2e8b57?style=flat-square)](https://github.com/alexandermodell/Representation-Manifolds)<br>
  Alexander Modell et al. · `LLM analysis` · Relates similarities in learned representations to intrinsic conceptual geometry under a generative model.


</details>

<a id="reading-route"></a>
## Reading Guide

The [12-paper reading path](docs/reading-guide.md) connects evidence about learned structure to composition, geometry, adaptation, planning, and generalization tests. Short topic branches link related methods and evaluation protocols.

[Candidate papers](docs/candidates.md) are listed separately from the main index and its paper counts.

## Related Resources

- [Awesome World Models](https://github.com/knightnemo/Awesome-World-Models) — World-model methods and applications across robotics, games, driving, and science.
- [Awesome World Models for Robotic Policy Learning](https://github.com/NTUMARS/Awesome-World-Model-for-Robotics-Policy) — World models as policies, simulators, and video predictors for robot learning.
- [Learning to Model the World](https://github.com/JiahuaDong/Awesome-World-Models) — A survey repository spanning world-model representations, applications, interpretability, and benchmarks.
- [Awesome World Model Evaluation](https://github.com/gxchris95/awesome-world-model-eval) — Evaluation papers and metrics organized by modality and evaluation dimension.
- [A Survey of World Model Benchmarks](https://github.com/World-Model-Benchmarks/World-Model-Benchmarks) — Benchmarks organized by physical, causal, control, and functional evaluation targets.

## Contributing

Paper suggestions and corrections are welcome through issues or pull requests. See [Contributing](CONTRIBUTING.md) for inclusion criteria and the entry format. Bibliographic records are available in [BibTeX](references.bib).

## License

Original catalog text and illustrations: [CC BY 4.0](LICENSES/CC-BY-4.0.txt). Maintenance code: [MIT](LICENSES/MIT.txt). Linked papers and external resources retain their respective licenses. See [license scope](LICENSE.md).

<!-- END GENERATED RESEARCH MAP -->
