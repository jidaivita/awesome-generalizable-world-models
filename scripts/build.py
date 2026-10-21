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


def author_label(p):
    authors = p['bibliography']['authors']
    first = authors[0]
    if ', ' in first:
        family, given = first.split(', ', 1)
        first = given + ' ' + family
    return first + (' et al.' if len(authors) > 1 else '')


def bib_escape(text):
    replacements = {'&': r'\&', '%': r'\%', '_': r'\_', '#': r'\#', '$': r'\$'}
    return ''.join(replacements.get(char, char) for char in str(text))


def bibliography(papers):
    result = '% Generated from verified bibliographic fields in data/papers.json.\n% UTF-8; years refer to the cited edition.\n\n'
    for p in sorted(papers, key=lambda p: p['id']):
        b = p['bibliography']
        fields = {'title': '{' + bib_escape(p['canonical_title']) + '}',
                  'author': ' and '.join(bib_escape(a) for a in b['authors']),
                  'year': str(b['year'])}
        for key in ('booktitle', 'journal', 'volume', 'pages', 'publisher', 'doi'):
            if b.get(key): fields[key] = bib_escape(b[key])
        if b.get('eprint'):
            fields['eprint'] = b['eprint']; fields['archivePrefix'] = 'arXiv'
        if b['entry_type'] == 'misc' and not p['publication']['label'].startswith('arXiv'):
            fields['note'] = bib_escape(p['publication']['label'])
        fields['url'] = b['source_url']
        result += '@' + b['entry_type'] + '{' + p['id'] + ',\n'
        result += ',\n'.join('  ' + key + ' = {' + value + '}' for key, value in fields.items())
        result += '\n}\n\n'
    return result


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

# Awesome Generalizable World Models

Papers on learned world models and their generalization across object configurations, environments, dynamics, and tasks. The list covers structured representations, latent geometry, context-based adaptation, planning, and evaluation, with related analysis methods from language models labeled separately.

<p align="center"><img src="assets/research-map.svg" width="620" alt="Representation geometry, transfer across environments, and planning"></p>

[Topics](#research-map) · [Reading Guide](docs/reading-guide.md) · [BibTeX](references.bib) · [Contributing](CONTRIBUTING.md)

<a id="start-here"></a>
<a id="research-map"></a>
## Contents

'''
    for m in modules:
        intro += f"- [{m['title']}](#{m['id'].lower()})\n"
    intro += f"\n{total} papers · {len(modules)} topics · Listed alphabetically within each topic.\n\n<a id=\"papers\"></a>\n## Papers\n\n"
    for m in modules:
        intro += f"<a id=\"{m['id'].lower()}\"></a>\n### {m['title']}\n\n"
        for p in selected(m['id']):
            tag=f" · `{p['domain_label']}`" if p.get('domain_label') else ''
            intro += f"<a id=\"paper-{p['id']}\"></a>\n- **{p['canonical_title']}**<br>\n  {author_label(p)} · **{p['publication']['label']}**{tag} · {resources(p)}<br>\n  {p['annotation']['why']}\n\n"
        intro += f"[Topic overview and comparisons]({module_path(m)}) · [Contents](#research-map)\n\n"
    intro += '''<a id="reading-route"></a>
## Reading Guide

The [12-paper reading path](docs/reading-guide.md) connects representation analysis, predictive architectures, planning, and adaptation. Each entry links to a topic overview and identifies the research question it addresses.

## Related Resources

- [Awesome World Models](https://github.com/knightnemo/Awesome-World-Models) — world-model research across application domains.
- [Awesome Deep Learning Papers](https://github.com/terryum/awesome-deep-learning-papers) — a historical deep-learning paper list; no longer maintained.
- [Awesome Machine Learning](https://github.com/josephmisiti/awesome-machine-learning) — machine-learning libraries and resources.

## Contributing

Paper suggestions and corrections are welcome through issues or pull requests. See [Contributing](CONTRIBUTING.md) for inclusion criteria and the entry format. Bibliographic records are available in [BibTeX](references.bib).

## License

Original catalog text and illustrations: [CC BY 4.0](LICENSES/CC-BY-4.0.txt). Maintenance code: [MIT](LICENSES/MIT.txt). Linked papers and external resources retain their respective licenses. See [license scope](LICENSE.md).
'''
    if notes:
        intro += '\n## Community Notes\n\n' + ''.join(f'- [{title}]({path})\n' for title,path,_ in notes)
    out['README.md'] = intro
    for m in modules:
        prefix=f"[← Paper index](../../README.md#research-map) · [Reading guide](../reading-guide.md)\n\n# {m['title']}\n\n{m['intro']}\n\n{m['scope']}\n"
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
        prefix+='\n## Papers\n\n'
        for p in selected(m['id']):
            prefix+=f"<a id=\"paper-{p['id']}\"></a>\n### {p['canonical_title']}\n\n{author_label(p)} · **{p['publication']['label']}** · {resources(p)}\n\n"
            if p['aliases']:prefix+='Earlier titles / aliases: '+ '; '.join(p['aliases'])+'.\n\n'
            prefix+=f"{p['annotation']['why']}\n\n- **Method and analysis:** {p['annotation']['focus']}\n- **Evaluation scope:** {p['annotation']['boundary']}\n"
            if p['secondary_modules']:prefix+='- **Related topics:** '+' · '.join(f"[{bymod[mid]['title']}]({Path(module_path(bymod[mid])).name})" for mid in p['secondary_modules'])+'\n'
            prefix+='\n'
        prefix+=f"## Method comparisons\n\n{m['connections']}\n\n## Related topics\n\n"
        prefix+='\n'.join(f"- [{bymod[mid]['title']}]({Path(module_path(bymod[mid])).name})" for mid in m['related'])
        prefix+='\n\n[Paper-note template](../../templates/paper-note.md) · [Comparison template](../../templates/comparison-note.md) · [Back to overview ↑](../../README.md)\n'
        out[module_path(m)] = prefix
    route='''[← Paper index](../README.md#papers)

# Reading Path

A sequence of twelve papers connecting representation analysis, prediction, planning, and adaptation. The guide assumes familiarity with representation learning and model-based reinforcement learning; its four sections can also be read independently.

## 01–03 · Representations and adaptation

These papers examine physical information in representations, learning from context, and tests of learned world structure.

'''
    for i,r in enumerate(cfg['route'],1):
        if i==4:route+='## 04–05 · Geometry and prediction\n\nSMDS compares geometric hypotheses; GRWM studies latent geometry and long-horizon prediction.\n\n'
        if i==6:route+='## 06–08 · World-model architectures and planning\n\nDINO-WM, LeWorldModel, and JEPA-WMs examine visual encoders, predictive objectives, and planning algorithms.\n\n'
        if i==9:route+='## 09–12 · Transfer and information gathering\n\nThese papers cover symmetry priors, changing dynamics, simulation-based policy evaluation, and task-informed exploration.\n\n'
        p=byid[r['id']]
        route+=f"### {i:02d} · {r['label']}\n\n**[{p['canonical_title']}]({p['links']['paper']})**\n\n- **Question:** {r['question']}\n- **Topic overview:** [{bymod[p['primary_module']]['title']}]({module_path(bymod[p['primary_module']]).removeprefix('docs/')}#paper-{p['id']})\n\n"
    route+='''## Comparing papers

The comparisons address three questions:

- **Representation:** What information or structure can be recovered from the model?
- **Function:** What changes when that information is manipulated or removed?
- **Transfer:** Which results hold under new tasks, environments, or dynamics?

Comparisons depend on the supervision available to each model, whether the encoder and predictor are fixed or updated, and the evaluation conditions.

[Paper-note template](../templates/paper-note.md) · [Comparison template](../templates/comparison-note.md) · [Back to papers](../README.md#papers)
'''
    out['docs/reading-guide.md']=route
    out['references.bib']=bibliography(papers)
    return out


def write_outputs(root=ROOT, check=False):
    changed=[]
    for rel, body in render(root).items():
        path=root/rel
        if rel.endswith('.bib'):
            if path.exists() and not path.read_text().startswith('% Generated from verified bibliographic fields'):
                raise ValueError(f'Refusing to overwrite unmarked bibliography: {rel}')
            if not path.exists() or path.read_text()!=body:
                changed.append(rel)
                if not check: path.write_text(body)
            continue
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
