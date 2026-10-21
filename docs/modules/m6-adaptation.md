<!-- BEGIN GENERATED RESEARCH MAP -->

[← Research map](../../README.md#research-map) · [Reading path](../reading-guide.md)

# M6 · Exploration & Efficient Adaptation

> What experience should an agent acquire or reuse in an unfamiliar environment?

Exploration determines which experience to collect; replay determines which experience to reuse. The papers study information gain, system identification, task sensitivity, and replay selection.

Parameter identification within a model class, learning missing mechanisms, active collection, and experience replay have different assumptions and costs.

## Where to start

1. **[Poke and Strike](#paper-poke-strike)** — Selects exploratory interactions according to task-relevant information.
2. **[Planning to Explore via Self-Supervised World Models](#paper-plan2explore)** — Learns exploration behavior from model disagreement before downstream tasks are specified.

## Papers and reading pointers

<a id="paper-asid"></a>
### ASID: Active Exploration for System Identification in Robotic Manipulation

**ICLR 2024** · [Paper](https://proceedings.iclr.cc/paper_files/paper/2024/hash/ae8afec5dabb07091d8f85128250f2ff-Abstract-Conference.html)

Combines active interaction with system identification to improve simulation models.

- **Read for:** How informative actions are chosen and how identified quantities enter the subsequent model.
- **Scope:** Estimating parameters within a given model class differs from discovering missing mechanisms.
- **Related topics:** [M5 · Reliability & Sim2Real](m5-reliability.md)

<a id="paper-curious-replay"></a>
### Curious Replay for Model-based Adaptation

**ICML 2023** · [Paper](https://proceedings.mlr.press/v202/kauvar23a.html)

Prioritizes stored experience using novelty and prediction error to support adaptation.

- **Read for:** The roles of novelty, prediction error, and replay prioritization.
- **Scope:** Replaying stored experience differs from actively choosing new physical interactions.
- **Related topics:** [M3 · Generalization & In-Context Learning](m3-generalization.md)

<a id="paper-plan2explore"></a>
### Planning to Explore via Self-Supervised World Models

**ICML 2020** · [Paper](https://proceedings.mlr.press/v119/sekar20a.html)

Learns exploration behavior from model disagreement before downstream tasks are specified.

- **Read for:** Model disagreement, predictive novelty, and subsequent task learning.
- **Scope:** General novelty does not necessarily identify the information most valuable for a particular task.
- **Related topics:** [M4 · Knowledge Use & Task Abstraction](m4-knowledge-use.md)

<a id="paper-poke-strike"></a>
### Poke and Strike: Learning Task-Informed Exploration Policies

**CoRL 2025** · [Paper](https://proceedings.mlr.press/v305/aoyama25a.html)

Selects exploratory interactions according to task-relevant information.

- **Read for:** Task sensitivity, exploration rewards, stopping criteria, and privileged information available during training.
- **Scope:** The method uses privileged information during training; evaluation should distinguish training access from information available to the deployed policy.
- **Related topics:** [M4 · Knowledge Use & Task Abstraction](m4-knowledge-use.md)

## Read together

Plan2Explore studies exploration before tasks are known; ASID connects interaction to identification; Poke and Strike focuses on task-relevant information; Curious Replay studies reuse. They use different criteria to value information and measure its benefit to a task.

## Related topics

- [M3 · Generalization & In-Context Learning](m3-generalization.md) — Does success in a new environment come from knowledge reuse or learning new dynamics?
- [M4 · Knowledge Use & Task Abstraction](m4-knowledge-use.md) — Which information actually supports prediction, planning, and decisions?
- [M5 · Reliability & Sim2Real](m5-reliability.md) — Which model errors matter for decisions, and when is a model trustworthy?

[Paper-note template](../../templates/paper-note.md) · [Comparison template](../../templates/comparison-note.md) · [Back to overview ↑](../../README.md)

<!-- END GENERATED RESEARCH MAP -->
