<!-- BEGIN GENERATED RESEARCH MAP -->

[← Paper index](../../README.md#research-map) · [Reading guide](../reading-guide.md)

# Exploration & Experience Replay

Exploration determines which experience to collect; replay determines which experience to reuse. The papers study information gain, system identification, task sensitivity, and replay selection.

Parameter identification within a model class, learning missing mechanisms, active collection, and experience replay have different assumptions and costs.

## Papers

<a id="paper-asid"></a>
### ASID: Active Exploration for System Identification in Robotic Manipulation

Marius Memmel et al. · **ICLR 2024** · [Paper](https://proceedings.iclr.cc/paper_files/paper/2024/hash/ae8afec5dabb07091d8f85128250f2ff-Abstract-Conference.html)

Combines active interaction with system identification to improve simulation models.

- **Method and analysis:** How informative actions are chosen and how identified quantities enter the subsequent model.
- **Evaluation scope:** Estimating parameters within a given model class differs from discovering missing mechanisms.
- **Related topics:** [Evaluation & Sim-to-Real Transfer](m5-reliability.md)

<a id="paper-curious-replay"></a>
### Curious Replay for Model-based Adaptation

Isaac Kauvar et al. · **ICML 2023** · [Paper](https://proceedings.mlr.press/v202/kauvar23a.html)

Prioritizes stored experience using novelty and prediction error to support adaptation.

- **Method and analysis:** The roles of novelty, prediction error, and replay prioritization.
- **Evaluation scope:** Replaying stored experience differs from actively choosing new physical interactions.
- **Related topics:** [Generalization & Context-Based Adaptation](m3-generalization.md)

<a id="paper-plan2explore"></a>
### Planning to Explore via Self-Supervised World Models

Ramanan Sekar et al. · **ICML 2020** · [Paper](https://proceedings.mlr.press/v119/sekar20a.html)

Learns exploration behavior from model disagreement before downstream tasks are specified.

- **Method and analysis:** Model disagreement, predictive novelty, and subsequent task learning.
- **Evaluation scope:** General novelty does not necessarily identify the information most valuable for a particular task.
- **Related topics:** [Planning & Task-Relevant Representations](m4-knowledge-use.md)

<a id="paper-poke-strike"></a>
### Poke and Strike: Learning Task-Informed Exploration Policies

Marina Y. Aoyama et al. · **CoRL 2025** · [Paper](https://proceedings.mlr.press/v305/aoyama25a.html)

Selects exploratory interactions according to task-relevant information.

- **Method and analysis:** Task sensitivity, exploration rewards, stopping criteria, and privileged information available during training.
- **Evaluation scope:** The exploration policy uses privileged task information during training; this information is unavailable to the deployed policy.
- **Related topics:** [Planning & Task-Relevant Representations](m4-knowledge-use.md)

## Method comparisons

Plan2Explore studies exploration before tasks are known; ASID connects interaction to identification; Poke and Strike focuses on task-relevant information; Curious Replay studies reuse. They use different criteria to value information and measure its benefit to a task.

## Related topics

- [Generalization & Context-Based Adaptation](m3-generalization.md)
- [Planning & Task-Relevant Representations](m4-knowledge-use.md)
- [Evaluation & Sim-to-Real Transfer](m5-reliability.md)

[Paper-note template](../../templates/paper-note.md) · [Comparison template](../../templates/comparison-note.md) · [Back to overview ↑](../../README.md)

<!-- END GENERATED RESEARCH MAP -->
