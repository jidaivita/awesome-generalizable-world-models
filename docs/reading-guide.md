<!-- BEGIN GENERATED RESEARCH MAP -->

[← Overview](../README.md#reading-route)

# Reading Path

Twelve papers on model mechanisms, representation geometry, planning, and adaptation, grouped by research question.

## 01–03 · Representations and adaptation

These papers examine physical information in representations, learning from context, and tests of learned world structure.

### 01 · Interpreting Physics

**[Interpreting Physics in Video World Models](https://proceedings.mlr.press/v306/joseph26a.html)**

- **Question:** What distinguishes independent physical variables from distributed encoding?
- **Reading pointers:** [Representation Geometry & Manifolds](modules/m2-geometry.md#paper-interpreting-physics)

### 02 · Context and Diversity Matter

**[Context and Diversity Matter: The Emergence of In-Context Learning in World Models](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a46b9dcef23e9160f46d800a49a931d0-Abstract-Conference.html)**

- **Question:** How can environment recognition, dynamics learning, and state estimation be distinguished?
- **Reading pointers:** [Generalization & In-Context Learning](modules/m3-generalization.md#paper-context-diversity)

### 03 · What Has a Foundation Model Found?

**[What Has a Foundation Model Found? Using Inductive Bias to Probe for World Models](https://proceedings.mlr.press/v267/vafa25a.html)**

- **Question:** Why can strong task performance be insufficient evidence of learned world structure?
- **Reading pointers:** [Knowledge Use & Task Abstraction](modules/m4-knowledge-use.md#paper-what-found)

## 04–05 · Geometry and prediction

SMDS compares geometric hypotheses; GRWM studies latent geometry and long-horizon prediction.

### 04 · SMDS / Shape Happens

**[Hypothesis-Driven Feature Manifold Analysis in LLMs via Supervised Multi-Dimensional Scaling](https://arxiv.org/abs/2510.01025)**

- **Question:** How can competing geometric hypotheses be compared beyond a projection plot?
- **Reading pointers:** [Representation Geometry & Manifolds](modules/m2-geometry.md#paper-smds)

### 05 · GRWM

**[Cloning Deterministic Worlds: The Critical Role of Latent Geometry in Long-Horizon World Models](https://arxiv.org/abs/2510.26782)**

- **Question:** How can geometric diagnosis become a method for better long-horizon prediction?
- **Reading pointers:** [Representation Geometry & Manifolds](modules/m2-geometry.md#paper-grwm)

## 06–08 · World-model architectures and planning

DINO-WM, LeWorldModel, and JEPA-WMs examine visual encoders, predictive objectives, and planning algorithms.

### 06 · DINO-WM

**[DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning](https://proceedings.mlr.press/v267/zhou25t.html)**

- **Question:** How does a latent representation support planning?
- **Reading pointers:** [Knowledge Use & Task Abstraction](modules/m4-knowledge-use.md#paper-dino-wm)

### 07 · LeWorldModel

**[LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels](https://arxiv.org/abs/2603.19312)**

- **Question:** How can end-to-end learning support prediction and planning with a compact model?
- **Reading pointers:** [Pretraining & Scaling](modules/m7-scaling.md#paper-leworldmodel)

### 08 · What Drives Success in JEPA-WMs?

**[What Drives Success in Physical Planning with Joint-Embedding Predictive World Models?](https://arxiv.org/abs/2512.24497)**

- **Question:** How can architecture, objective, and planner effects be separated?
- **Reading pointers:** [Pretraining & Scaling](modules/m7-scaling.md#paper-jepa-wms)

## 09–12 · Transfer and information gathering

These papers cover symmetry priors, changing dynamics, simulation-based policy evaluation, and task-informed exploration.

### 09 · Group-Structured Latent Space

**[Learning Abstract World Models with a Group-Structured Latent Space](https://arxiv.org/abs/2506.01529)**

- **Question:** What is supplied as a symmetry prior, and what is learned from data?
- **Reading pointers:** [Representation Geometry & Manifolds](modules/m2-geometry.md#paper-group-latents)

### 10 · Dynamics Are Learned, Not Told

**[Dynamics Are Learned, Not Told: Semi-Supervised Discovery of Latent Dynamics Geometries For Zero-Shot Policy Adaptation](https://proceedings.mlr.press/v306/xu26cq.html)**

- **Question:** How does latent geometry connect to adaptation under changing dynamics?
- **Reading pointers:** [Generalization & In-Context Learning](modules/m3-generalization.md#paper-dynamics-geometries)

### 11 · SIMPLER

**[Evaluating Real-World Robot Manipulation Policies in Simulation](https://proceedings.mlr.press/v270/li25c.html)**

- **Question:** When do model errors change real-world policy choices?
- **Reading pointers:** [Reliability & Sim2Real](modules/m5-reliability.md#paper-simpler)

### 12 · Poke and Strike

**[Poke and Strike: Learning Task-Informed Exploration Policies](https://proceedings.mlr.press/v305/aoyama25a.html)**

- **Question:** Which new experience is valuable for the task?
- **Reading pointers:** [Exploration & Efficient Adaptation](modules/m6-adaptation.md#paper-poke-strike)

## Comparing papers

When reading across these topics, distinguish three questions:

- **Representation:** What information or structure can be recovered from the model?
- **Function:** What changes when that information is manipulated or removed?
- **Transfer:** Which results hold under new tasks, environments, or dynamics?

Comparisons depend on the supervision available to each model, whether the encoder and predictor are fixed or updated, and the evaluation conditions.

[Paper-note template](../templates/paper-note.md) · [Comparison template](../templates/comparison-note.md) · [Back to papers](../README.md#papers)

<!-- END GENERATED RESEARCH MAP -->
