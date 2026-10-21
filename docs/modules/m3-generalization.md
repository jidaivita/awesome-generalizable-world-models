<!-- BEGIN GENERATED RESEARCH MAP -->

[← Paper index](../../README.md#research-map) · [Reading guide](../reading-guide.md) · [Supplementary reading](../supplementary.md)

# Generalization & Adaptation

World models encounter changes in object configurations, transition dynamics, observations, and goals. These papers study how learned structure transfers and how interaction history or parameter updates support adaptation.

Each entry specifies the tested shift and outcome. Prediction transfer, policy transfer, adaptation from context, and fine-tuning are different evaluation settings.

## Evaluation settings

| Change | Examples in this topic | Outcome to distinguish |
| :--- | :--- | :--- |
| Object composition | HOWM; Dreamweaver; WM3C | Prediction on unseen combinations versus control in new tasks |
| Dynamics or latent context | CaDM; Context and Diversity; Dynamics Are Learned; Considering Context | Context inference, prediction accuracy, and policy adaptation |
| Data or task distribution | Curious Replay; Behavior-Invariant Task Representation Learning; WOMBET | Update efficiency and target-task performance |
| Goals in a formal task family | General agents need world models | The predictive information required by the stated task assumptions |

Zero-shot transfer, inference from interaction history, and parameter-updating adaptation specify different deployment protocols. They are reported separately from the type of distribution shift.

## Compositional generalization

<a id="paper-dreamweaver"></a>
### Dreamweaver: Learning Compositional World Models from Pixels

Junyeob Baek et al. · **ICLR 2025** · [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ae82a60c5ce50b5c4d18cfe3214eb684-Abstract-Conference.html)

- **Method:** A Recurrent Block-Slot Unit decomposes raw video into objects and their attributes. Predicting multiple future frames encourages the representation to retain dynamic as well as static factors.
- **Evaluation:** Disentanglement is measured with the DCI framework across video datasets. Recombining attributes of previously observed objects tests compositional video generation without auxiliary text, masks, or bounding boxes.
- **Related topics:** [Structured & Compositional Representations](m1-structure.md)

<a id="paper-wm3c"></a>
### Modeling Unseen Environments with Language-guided Composable Causal Components in Reinforcement Learning

Xinyue Wang et al. · **ICLR 2025** · [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/79d86433c2acd12b6fa98553435d226e-Abstract-Conference.html)

Earlier titles / aliases: WM3C.

- **Method:** WM3C uses language to organize latent dynamics into composable components. A masked autoencoder, mutual-information constraints, and adaptive sparsity regularization separate transition mechanisms.
- **Evaluation:** Numerical simulations and robotic manipulation test latent-process identification, policy learning, and transfer to unseen tasks. Identifiability results depend on the stated modeling assumptions.
- **Related topics:** [Structured & Compositional Representations](m1-structure.md) · [World Model Interpretability](m8-interpretability.md)

<a id="paper-howm"></a>
### Toward Compositional Generalization in Object-Oriented World Modeling

Linfeng Zhao et al. · **ICML 2022** · [Paper](https://proceedings.mlr.press/v162/zhao22b.html)

Earlier titles / aliases: HOWM.

- **Method:** An algebraic formulation defines compositional generalization in object-oriented environments. HOWM implements a differentiable, soft form of composition to share dynamics across object configurations.
- **Evaluation:** Two instances of the Object Library environment compare methods with exact, approximate, or absent compositional guarantees under a common evaluation pipeline.
- **Related topics:** [Structured & Compositional Representations](m1-structure.md)

## Dynamics shifts and context-based adaptation

<a id="paper-considering-context"></a>
### Considering Context: When World Models Need Context Encoders

Oleg Smirnov et al. · **arXiv 2026** · [Paper](https://arxiv.org/abs/2610.06651)

- **Method:** Predictive sufficiency separates context-dependent prediction gains into information recoverable from history, residual information requiring true context, and error attributable to a finite model.
- **Evaluation:** Experiments vary identification difficulty and priors over environments. The same task can leave different prediction headroom depending on whether the agent's behavior already identifies its context.
- **Related topics:** [Evaluation & Benchmarks](m5-reliability.md)

<a id="paper-context-diversity"></a>
### Context and Diversity Matter: The Emergence of In-Context Learning in World Models

Fan Wang et al. · **ICLR 2026** · [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a46b9dcef23e9160f46d800a49a931d0-Abstract-Conference.html) · [Code](https://github.com/airs-cuhk/airsoul/tree/main/projects/MazeWorld)

- **Method:** The analysis separates environment recognition, which identifies a familiar environment, from environment learning, which estimates dynamics from the current context. Error bounds link these mechanisms to context length and training-environment diversity.
- **Evaluation:** World-model experiments vary context, data diversity, and architecture to test the theoretical predictions. The distinction concerns how prediction improves with experience while model weights remain fixed.
- **Related topics:** [Representation Geometry & Symmetry](m2-geometry.md)

<a id="paper-cadm"></a>
### Context-aware Dynamics Model for Generalization in Model-Based Reinforcement Learning

Kimin Lee et al. · **ICML 2020** · [Paper](https://proceedings.mlr.press/v119/lee20g.html) · [Code](https://github.com/younggyoseo/CaDM)

- **Method:** A history encoder estimates a context vector for local dynamics. Forward and backward prediction losses train the context to retain environment-specific information, and the next-state predictor conditions on this vector.
- **Evaluation:** Simulated robotics and control tasks test prediction and policy performance across different dynamics. Adaptation uses recent interaction history as evidence about the current environment.

<a id="paper-curious-replay"></a>
### Curious Replay for Model-based Adaptation

Isaac Kauvar et al. · **ICML 2023** · [Paper](https://proceedings.mlr.press/v202/kauvar23a.html)

- **Method:** Curiosity-based replay priorities favor experience that is novel or poorly predicted when training a world model. The intervention changes which stored transitions are reused, complementing action-based exploration.
- **Evaluation:** An exploration-and-adaptation setting and Crafter test the replay rule, with DeepMind Control Suite used to check performance on established control tasks.
- **Related topics:** [Planning & Task-Relevant World Models](m4-knowledge-use.md)

<a id="paper-dynamics-geometries"></a>
### Dynamics Are Learned, Not Told: Semi-Supervised Discovery of Latent Dynamics Geometries For Zero-Shot Policy Adaptation

Zhiming Xu et al. · **ICML 2026** · [Paper](https://proceedings.mlr.press/v306/xu26cq.html) · [Code](https://github.com/Mr-Wonderfool/Latent-Dynamics-Geometries)

- **Method:** A trajectory encoder learns a dynamics context using a multi-positive InfoNCE objective. The analysis relates encoder smoothness to target-domain regret, motivating a latent geometry that supports adaptation without privileged physical-parameter labels.
- **Evaluation:** MuJoCo experiments test severe dynamics shifts, including structural failures outside the explicit parameterization used by identification baselines, alongside in-distribution policy stability.
- **Related topics:** [Representation Geometry & Symmetry](m2-geometry.md)

## Task and experience transfer

<a id="paper-behavior-invariant-wm"></a>
### Behavior-Invariant Task Representation Learning with Transformer-based World Models for Offline Meta-Reinforcement Learning

Fuyuan Qian et al. · **ICML 2026** · [Paper](https://proceedings.mlr.press/v306/qian26o.html)

- **Method:** Information-theoretic task representation learning extracts latent variables that are invariant to behavior policy. A Transformer-based stochastic world model supplies imagined rollouts with conservative value penalties to limit exploitation of model errors.
- **Evaluation:** Offline meta-RL experiments evaluate adaptation under context and policy distribution shifts, including out-of-distribution and sparse-reward settings.
- **Related topics:** [Planning & Task-Relevant World Models](m4-knowledge-use.md)

<a id="paper-wombet"></a>
### WOMBET: World Model-based Experience Transfer for Robust and Sample-efficient Reinforcement Learning

Mintae Kim et al. · **L4DC 2026** · [Paper](https://proceedings.mlr.press/v331/kim26a.html)

- **Method:** A source-task world model generates trajectories through uncertainty-penalized planning. Return and epistemic-uncertainty filters select offline experience, which is mixed adaptively with online data during target-task fine-tuning.
- **Evaluation:** Continuous-control benchmarks measure sample efficiency and final performance. The analysis bounds return and decomposes distribution-mismatch and approximation errors; the transfer procedure includes online updates.
- **Related topics:** [Planning & Task-Relevant World Models](m4-knowledge-use.md)

## Theory of goal generalization

<a id="paper-general-agents"></a>
### General agents need world models

Jonathan Richens et al. · **ICML 2025** · `Theory` · [Paper](https://proceedings.mlr.press/v267/richens25a.html)

- **Method:** A formal construction extracts an environment predictor from a policy capable of solving a specified class of multi-step goals. The required prediction accuracy increases with performance and goal complexity.
- **Evaluation:** The theoretical result connects goal generalization to extractable predictive information under the paper's formal task assumptions.
- **Related topics:** [Planning & Task-Relevant World Models](m4-knowledge-use.md)

## Method comparisons

HOWM and Dreamweaver study composition; WM3C uses language-guided causal components for unseen environments.

CaDM conditions dynamics on history, while Context and Diversity and Considering Context examine what that history reveals. Dynamics Are Learned shapes a trajectory embedding for policy adaptation.

Curious Replay changes the data used for updates; WOMBET generates source-task experience for target-task fine-tuning. Behavior-Invariant Task Representation Learning addresses changes in offline behavior and online interaction.

General agents need world models supplies a formal connection between goal generalization and prediction.

## Related topics

- [Structured & Compositional Representations](m1-structure.md)
- [World Model Interpretability](m8-interpretability.md)
- [Planning & Task-Relevant World Models](m4-knowledge-use.md)
- [Evaluation & Benchmarks](m5-reliability.md)

[Back to paper index](../../README.md)

<!-- END GENERATED RESEARCH MAP -->
