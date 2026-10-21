#!/usr/bin/env python3
"""Build the public research map using only explicit public fields and paths."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BEGIN = '<!-- BEGIN GENERATED RESEARCH MAP -->'
END = '<!-- END GENERATED RESEARCH MAP -->'


def read_sources(root=ROOT):
    papers = json.loads((root / 'data/papers.json').read_text())
    config = json.loads((root / 'data/map.json').read_text())
    manifest = json.loads((root / 'publish-manifest.json').read_text())
    return papers, config, manifest


def module_path(m):
    return f"docs/modules/{m['id'].lower()}-{m['slug']}.md"


def resources(p):
    pairs = [('Paper', p['links']['paper']), ('Code', p['code']['url']), ('Project', p['links']['project']), ('Note', p['public_note'])]
    return ' · '.join(f'[{label}]({url})' for label, url in pairs if url)


def public_note_paths(root, manifest):
    """No directory scanning: only manifest-listed Markdown under public_notes/."""
    result = []
    for item in manifest['notes']:
        rel = Path(item['path'])
        full = (root / rel).resolve()
        if rel.is_absolute() or '..' in rel.parts or not rel.parts or rel.parts[0] != 'public_notes' or rel.suffix != '.md':
            raise ValueError('Public note paths must be explicit Markdown files under public_notes/')
        if not full.is_relative_to((root / 'public_notes').resolve()) or not full.is_relative_to(root.resolve()):
            raise ValueError('Public note escapes the public directory')
        if not full.is_file():
            raise ValueError('Manifest note does not exist')
        result.append((item['title'], rel.as_posix(), full))
    return result


def render(root=ROOT):
    papers, cfg, manifest = read_sources(root)
    modules = cfg['modules']; byid = {p['id']: p for p in papers}; bymod = {m['id']: m for m in modules}
    notes = public_note_paths(root, manifest)
    def selected(mid):
        return sorted((p for p in papers if p['primary_module'] == mid and p['collection'] == 'seed_v0_2'), key=lambda p: p['canonical_title'].casefold())
    total = sum(p['collection'] == 'seed_v0_2' for p in papers)
    out = {}
    intro = '''<a id="top"></a>
<div align="center">

# Awesome Generalizable World Models

**Representations · Dynamics · Generalization · Planning**

![A research map connecting representation geometry, generalization, and knowledge use](assets/research-map.svg)

'''
    intro += f'![Papers](https://img.shields.io/badge/Papers-{total}-2563eb?style=flat-square) ![Reading path](https://img.shields.io/badge/Reading_path-{len(cfg["route"])}-0f766e?style=flat-square) ![Research modules](https://img.shields.io/badge/Modules-{len(modules)}-7c3aed?style=flat-square)\n'
    intro += '''
[Start Here](#start-here) · [Contents](#research-map) · [Reading Path](#reading-route) · [Paper List](#papers) · [Contribute](CONTRIBUTING.md)

</div>

---

Papers and reading guides on world-model representations, generalization, adaptation, and planning.

<a id="start-here"></a>
## Start Here

Two papers on representation and adaptation:

| 01 · How is knowledge organized? | 02 · What does new experience change? |
| :--- | :--- |
'''
    a,b=byid['interpreting-physics'],byid['context-diversity']
    intro += f"| **[{a['canonical_title']}]({a['links']['paper']})** | **[{b['canonical_title']}]({b['links']['paper']})** |\n"
    intro += '''| Physical variables, subspaces, and interventions reveal how information is represented. | Environment recognition and environment learning offer different explanations for adaptation. |
| **Ask:** Does decodable information actually influence model behavior? | **Ask:** What mechanism explains the benefit of context? |

<a id="research-map"></a>
## Contents

| Topic | Papers | Reading guide |
| :--- | :---: | :--- |
'''
    for m in modules:
        intro += f"| [{m['title']}](#{m['id'].lower()}) | {len(selected(m['id']))} | [Overview & connections]({module_path(m)}) |\n"
    intro += '\nPapers are listed alphabetically within each topic. The guides link related work across topics.\n\n'
    intro += '''<a id="reading-route"></a>
## Reading Path

The [12-paper reading path](docs/reading-guide.md) covers model mechanisms, representation geometry, planning, and adaptation.

<details>
<summary>View the 12-paper reading path</summary>


| # | Paper | Research question |
| :---: | :--- | :--- |
'''
    for i,r in enumerate(cfg['route'],1):intro += f"| {i:02d} | [{r['label']}](#paper-{r['id']}) | {r['question']} |\n"
    intro += '\n</details>\n\n[Read the guide →](docs/reading-guide.md)\n\n<a id="papers"></a>\n## Papers\n\nEntries include a paper link, publication information, available code or project links, and a short description.\n\n'
    for m in modules:
        intro += f"<a id=\"{m['id'].lower()}\"></a>\n### {m['title']}\n\n> {m['question']}\n\n"
        for p in selected(m['id']):
            intro += f"<a id=\"paper-{p['id']}\"></a>\n- **[{p['canonical_title']}]({p['links']['paper']})**<br>\n  {p['publication']['label']} · {resources(p)}<br>\n  {p['annotation']['why']}\n\n"
        intro += f"[Reading notes and connections →]({module_path(m)}) · [Back to map ↑](#research-map)\n\n"
    intro += """## Related Lists

- [Awesome World Models](https://github.com/knightnemo/Awesome-World-Models) — broader coverage of world-model applications.
- [Awesome Deep Learning Papers](https://github.com/terryum/awesome-deep-learning-papers) — influential deep-learning papers organized by topic.
- [Awesome Machine Learning](https://github.com/josephmisiti/awesome-machine-learning) — machine-learning libraries and resources.

## Contributing

To suggest a paper or correct an entry, open an issue or pull request. See the [contribution guide](CONTRIBUTING.md) for scope and entry format.
"""
    if notes:
        intro += '\n## Community Notes\n\n' + ''.join(f'- [{title}]({path})\n' for title,path,_ in notes)
    first = intro.index('<a id="start-here"></a>')
    contents = intro.index('<a id="research-map"></a>')
    route_start = intro.index('<a id="reading-route"></a>')
    intro = intro[:first] + intro[contents:route_start] + intro[first:contents] + intro[route_start:]
    out['README.md'] = intro
    for m in modules:
        prefix=f"[← Research map](../../README.md#research-map) · [Reading path](../reading-guide.md)\n\n# {m['id']} · {m['title']}\n\n> {m['question']}\n\n{m['intro']}\n\n{m['scope']}\n\n## Where to start\n\n"
        for i,id in enumerate(m['start'],1):
            p=byid[id];target=f"#paper-{id}" if p['primary_module']==m['id'] else f"../../README.md#paper-{id}"
            prefix+=f"{i}. **[{next((r['label'] for r in cfg['route'] if r['id']==id), p['canonical_title'])}]({target})** — {p['annotation']['why']}\n"
        if m['id']=='M2':
            prefix+='''
## Three lines of inquiry

| Line of inquiry | Papers | Key distinction |
| :--- | :--- | :--- |
| Emergent geometry and function | Interpreting Physics, SMDS, Origins | Observed structure, competing hypotheses, and functional evidence |
| Geometric priors and dynamics learning | GRWM, Group-Structured Latent Space, GeoWorld | Where the prior comes from and what it independently contributes |
| Geometry and adaptation | [Context and Diversity](m3-generalization.md#paper-context-diversity), [Dynamics Are Learned](m3-generalization.md#paper-dynamics-geometries) | Environment shifts, trajectory information, and transferable structure |

**Methods used in these studies:** PCA/SVD, linear probes, periodic-variable encodings, subspace comparisons, interventions, held-out evaluation, intrinsic-dimension estimation, and Riemannian optimization.

For example, `z(θ) = (cos θ, sin θ, cos 2θ, sin 2θ, …)` has one underlying degree of freedom while spanning multiple linear directions. Physical degrees of freedom, vector dimension, linear span, intrinsic manifold dimension, and the number of intervention directions are different quantities. This is a mathematical illustration, not a measurement from a trained model.
'''
        prefix+='\n## Papers and reading pointers\n\n'
        for p in selected(m['id']):
            prefix+=f"<a id=\"paper-{p['id']}\"></a>\n### {p['canonical_title']}\n\n**{p['publication']['label']}** · {resources(p)}\n\n"
            if p['aliases']:prefix+='Earlier titles / aliases: '+ '; '.join(p['aliases'])+'.\n\n'
            prefix+=f"{p['annotation']['why']}\n\n- **Read for:** {p['annotation']['focus']}\n- **Scope:** {p['annotation']['boundary']}\n"
            if p['secondary_modules']:prefix+='- **Related topics:** '+' · '.join(f"[{mid} · {bymod[mid]['title']}]({Path(module_path(bymod[mid])).name})" for mid in p['secondary_modules'])+'\n'
            prefix+='\n'
        prefix+=f"## Read together\n\n{m['connections']}\n\n## Related topics\n\n"
        prefix+='\n'.join(f"- [{mid} · {bymod[mid]['title']}]({Path(module_path(bymod[mid])).name}) — {bymod[mid]['question']}" for mid in m['related'])
        prefix+='\n\n[Paper-note template](../../templates/paper-note.md) · [Comparison template](../../templates/comparison-note.md) · [Back to overview ↑](../../README.md)\n'
        out[module_path(m)] = prefix
    route='''[← Overview](../README.md#reading-route)

# Reading Path

Twelve papers on model mechanisms, representation geometry, planning, and adaptation, grouped by research question.

## 01–03 · Representations and adaptation

These papers examine physical information in representations, learning from context, and tests of learned world structure.

'''
    for i,r in enumerate(cfg['route'],1):
        if i==4:route+='## 04–05 · Geometry and prediction\n\nSMDS compares geometric hypotheses; GRWM studies latent geometry and long-horizon prediction.\n\n'
        if i==6:route+='## 06–08 · World-model architectures and planning\n\nDINO-WM, LeWorldModel, and JEPA-WMs examine visual encoders, predictive objectives, and planning algorithms.\n\n'
        if i==9:route+='## 09–12 · Transfer and information gathering\n\nThese papers cover symmetry priors, changing dynamics, simulation-based policy evaluation, and task-informed exploration.\n\n'
        p=byid[r['id']]
        route+=f"### {i:02d} · {r['label']}\n\n**[{p['canonical_title']}]({p['links']['paper']})**\n\n- **Question:** {r['question']}\n- **Reading pointers:** [{bymod[p['primary_module']]['title']}]({module_path(bymod[p['primary_module']]).removeprefix('docs/')}#paper-{p['id']})\n\n"
    route+='''## Comparing papers

When reading across these topics, distinguish three questions:

- **Representation:** What information or structure can be recovered from the model?
- **Function:** What changes when that information is manipulated or removed?
- **Transfer:** Which results hold under new tasks, environments, or dynamics?

Comparisons depend on the supervision available to each model, whether the encoder and predictor are fixed or updated, and the evaluation conditions.

[Paper-note template](../templates/paper-note.md) · [Comparison template](../templates/comparison-note.md) · [Back to papers](../README.md#papers)
'''
    out['docs/reading-guide.md']=route
    return out


def write_outputs(root=ROOT, check=False):
    changed=[]
    for rel, body in render(root).items():
        path=root/rel
        block=BEGIN+'\n\n'+body.rstrip()+'\n\n'+END+'\n'
        if path.exists():
            old=path.read_text()
            if old.count(BEGIN)!=1 or old.count(END)!=1 or old.index(BEGIN)>old.index(END):
                raise ValueError(f'Refusing to overwrite unmarked or malformed file: {rel}')
            new=old.split(BEGIN)[0]+block.rstrip('\n')+old.split(END)[1]
        else:new=block
        if not path.exists() or path.read_text()!=new:
            changed.append(rel)
            if not check:
                path.parent.mkdir(parents=True,exist_ok=True);path.write_text(new)
    return changed


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
    changed=write_outputs(check=args.check)
    print(('Stale' if args.check else 'Updated')+f': {len(changed)} generated pages')
    if args.check and changed:raise SystemExit(1)
