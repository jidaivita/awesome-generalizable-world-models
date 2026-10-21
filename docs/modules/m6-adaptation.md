<!-- BEGIN GENERATED RESEARCH MAP -->

[← Paper index](../../README.md#research-map) · [Reading guide](../reading-guide.md)

# Exploration & Experience Replay

Agents can improve their models by choosing informative interactions and by selecting which stored transitions to revisit. These papers cover anticipated novelty, simulator-parameter identification, task-sensitive probing, and prioritized replay.

The approaches value experience by different criteria: model disagreement, parameter information, sensitivity of task success, or prediction difficulty.

## Papers

<a id="paper-asid"></a>
### ASID: Active Exploration for System Identification in Robotic Manipulation

Marius Memmel et al. · **ICLR 2024** · [Paper](https://proceedings.iclr.cc/paper_files/paper/2024/hash/ae8afec5dabb07091d8f85128250f2ff-Abstract-Conference.html)

- **Method:** An initial simulator is used to design exploratory interactions. Real observations from those interactions refine simulator parameters, after which the refined model supports control planning.
- **Evaluation:** Robotic manipulation experiments identify properties including articulation and mass and evaluate the resulting sim-to-real controllers. Identification operates within the available simulator and asset model.
- **Related topics:** [Evaluation & Sim-to-Real Transfer](m5-reliability.md)

<a id="paper-curious-replay"></a>
### Curious Replay for Model-based Adaptation

Isaac Kauvar et al. · **ICML 2023** · [Paper](https://proceedings.mlr.press/v202/kauvar23a.html)

- **Method:** Curiosity-based replay priorities favor experience that is novel or poorly predicted when training a world model. The intervention changes which stored transitions are reused, complementing action-based exploration.
- **Evaluation:** An exploration-and-adaptation setting and Crafter test the replay rule, with DeepMind Control Suite used to check performance on established control tasks.
- **Related topics:** [Generalization & Context-Based Adaptation](m3-generalization.md)

<a id="paper-plan2explore"></a>
### Planning to Explore via Self-Supervised World Models

Ramanan Sekar et al. · **ICML 2020** · [Paper](https://proceedings.mlr.press/v119/sekar20a.html)

- **Method:** An ensemble of latent predictors supplies a disagreement signal, and an exploration policy plans actions that seek expected future disagreement. Downstream task policies are then learned using the collected world model.
- **Evaluation:** Visual control tasks evaluate reward-free exploration followed by zero- or few-shot task adaptation. Tasks can be specified after the exploration phase.
- **Related topics:** [Planning & Task-Relevant Representations](m4-knowledge-use.md)

<a id="paper-poke-strike"></a>
### Poke and Strike: Learning Task-Informed Exploration Policies

Marina Y. Aoyama et al. · **CoRL 2025** · [Paper](https://proceedings.mlr.press/v305/aoyama25a.html)

- **Method:** An exploration policy is rewarded according to how sensitive a privileged task policy is to errors in estimated object properties. An uncertainty criterion determines when to stop probing and execute the task.
- **Evaluation:** Puck striking and CartPole analyze the task relevance of physical properties; a KUKA iiwa setup tests property estimation and adjusted execution on physical objects.
- **Related topics:** [Planning & Task-Relevant Representations](m4-knowledge-use.md)

## Method comparisons

Plan2Explore chooses actions before a downstream reward is specified. ASID chooses interactions to refine a simulator, while Poke and Strike weights identification errors by their consequences for a particular task. Curious Replay operates on already collected experience, changing the data used to update the model rather than the actions used to collect it.

## Related topics

- [Generalization & Context-Based Adaptation](m3-generalization.md)
- [Planning & Task-Relevant Representations](m4-knowledge-use.md)
- [Evaluation & Sim-to-Real Transfer](m5-reliability.md)

[Paper-note template](../../templates/paper-note.md) · [Comparison template](../../templates/comparison-note.md) · [Back to overview ↑](../../README.md)

<!-- END GENERATED RESEARCH MAP -->
