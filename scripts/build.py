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
    return m["path"] if "path" in m else f"docs/modules/{m['id'].lower()}-{m['slug']}.md"


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
    import posixpath
    papers, cfg, manifest = read_sources(root)
    modules = cfg['modules']; supplement = cfg['supplement']
    byid = {p['id']: p for p in papers}
    bymod = {m['id']: m for m in [*modules, supplement]}
    notes = public_note_paths(root, manifest)
    out = {}

    def selected(mid):
        return sorted((p for p in papers if p['primary_module'] == mid), key=lambda p: p['canonical_title'].casefold())

    def relative(target, source):
        return posixpath.relpath(target, posixpath.dirname(source) or '.')

    def paper_location(p):
        return module_path(bymod[p['primary_module']]) + '#paper-' + p['id']

    def linked_paper(pid, source):
        p = byid[pid]
        return f"[{p['canonical_title']}]({relative(paper_location(p), source)})"

    def entry(p, source, detailed=False):
        tag = f" · `{p['domain_label']}`" if p.get('domain_label') else ''
        text = f'<a id="paper-{p["id"]}"></a>\n'
        if detailed:
            text += f"### {p['canonical_title']}\n\n{author_label(p)} · **{p['publication']['label']}**{tag} · {resources(p)}\n\n"
            if p['aliases']:
                text += 'Earlier titles / aliases: ' + '; '.join(p['aliases']) + '.\n\n'
            text += f"- **Method:** {p['annotation']['focus']}\n- **Evaluation:** {p['annotation']['boundary']}\n"
            if p.get('supplement_reason'):
                text += f"- **Relevance:** {p['supplement_reason']}\n"
            if p['secondary_modules']:
                text += '- **Related topics:** ' + ' · '.join(f"[{bymod[mid]['title']}]({relative(module_path(bymod[mid]), source)})" for mid in p['secondary_modules']) + '\n'
        else:
            text += f"- **{p['canonical_title']}**<br>\n  {author_label(p)} · **{p['publication']['label']}**{tag} · {resources(p)}<br>\n  {p['annotation']['why']}\n"
        return text + '\n'

    core_count = sum(p['primary_module'] != supplement['id'] for p in papers)
    intro = '''<a id="top"></a>

# Awesome Generalizable World Models

A focused paper index on the mechanisms, generalization, and interpretability of learned world models. It connects representation structure and latent geometry to adaptation, physical prediction, and planning.

<p align="center"><img src="assets/research-map.svg" width="620" alt="Latent representations, transfer across environments, and planning"></p>

[Topics](#research-map) · [Reading Guide](docs/reading-guide.md) · [Supplementary Reading](docs/supplementary.md) · [BibTeX](references.bib) · [Contributing](CONTRIBUTING.md)

<a id="start-here"></a>
<a id="research-map"></a>
## Contents

| Topic | Coverage | Papers |
| :--- | :--- | ---: |
'''
    for m in modules:
        intro += f"| [{m['title']}](#{m['id'].lower()}) | {m['summary']} | {len(selected(m['id']))} |\n"
    intro += f"\n{core_count} papers across six topics · {len(selected(supplement['id']))} supplementary papers · {len(papers)} papers in total.\n\n"
    intro += 'Entries describe the mechanism, evaluation setting, and evidence for each contribution. New papers extend these six topics through a distinct method, analysis, or test of generalization. Each paper has one primary topic and is listed alphabetically within it.\n\n<a id="papers"></a>\n## Papers\n\n'
    for m in modules:
        intro += f"<a id=\"{m['id'].lower()}\"></a>\n### {m['title']}\n\n{m['summary']}\n\n"
        intro += ''.join(entry(p, 'README.md') for p in selected(m['id']))
        intro += f"[Topic overview and comparisons]({module_path(m)}) · [Contents](#research-map)\n\n"
    intro += '''<a id="m6"></a>
<a id="m7"></a>
## Supplementary Reading

[Supplementary Reading](docs/supplementary.md) covers world-model foundations, related representation methods, and simulation or system-identification studies. Each entry states its connection to the main topics.

<details>
<summary>Browse supplementary papers</summary>

'''
    for p in selected(supplement['id']):
        intro += f'<a id="paper-{p["id"]}"></a>\n- {linked_paper(p["id"], "README.md")} · {p["publication"]["label"]}\n'
    intro += '''
</details>

<a id="reading-route"></a>
## Reading Guide

The [12-paper reading path](docs/reading-guide.md) connects evidence about learned structure to composition, geometry, adaptation, planning, and generalization tests. Short topic branches link related methods and evaluation protocols.

[Candidate papers](docs/candidates.md) are listed separately from the main index and its paper counts.

## Related Resources

RESOURCE_LINKS

## Contributing

Paper suggestions and corrections are welcome through issues or pull requests. See [Contributing](CONTRIBUTING.md) for inclusion criteria and the entry format. Bibliographic records are available in [BibTeX](references.bib).

## License

Original catalog text and illustrations: [CC BY 4.0](LICENSES/CC-BY-4.0.txt). Maintenance code: [MIT](LICENSES/MIT.txt). Linked papers and external resources retain their respective licenses. See [license scope](LICENSE.md).
'''
    resource_links = '\n'.join(f"- [{r['title']}]({r['url']}) — {r['description']}" for r in cfg['resources'])
    intro = intro.replace('RESOURCE_LINKS', resource_links)
    if notes:
        intro += '\n## Community Notes\n\n' + ''.join(f'- [{title}]({path})\n' for title, path, _ in notes)
    out['README.md'] = intro
    for m in modules:
        path = module_path(m)
        body = f"[← Paper index](../../README.md#research-map) · [Reading guide](../reading-guide.md) · [Supplementary reading](../supplementary.md)\n\n# {m['title']}\n\n{m['intro']}\n\n{m['scope']}\n\n"
        if m['id'] == 'M3':
            body += '''## Evaluation settings

| Change | Examples in this topic | Outcome to distinguish |
| :--- | :--- | :--- |
| Object composition | HOWM; Dreamweaver; WM3C | Prediction on unseen combinations versus control in new tasks |
| Dynamics or latent context | CaDM; Context and Diversity; Dynamics Are Learned; Considering Context | Context inference, prediction accuracy, and policy adaptation |
| Data or task distribution | Curious Replay; Behavior-Invariant Task Representation Learning; WOMBET | Update efficiency and target-task performance |
| Goals in a formal task family | General agents need world models | The predictive information required by the stated task assumptions |

Zero-shot transfer, inference from interaction history, and parameter-updating adaptation specify different deployment protocols. They are reported separately from the type of distribution shift.

'''
        if m['id'] == 'M8':
            body += '''## Forms of evidence

| Approach | Evidence | Interpretation |
| :--- | :--- | :--- |
| Representation probing | A variable can be recovered from activations | The representation contains accessible information |
| Interventions and ablations | Modifying a representation changes predictions | The modified computation influences the measured output |
| Behavioral transfer tests | Adaptation favors or rejects a proposed world structure | Learning behavior reflects a particular inductive bias |
| Interpretable model design | Latent variables are aligned with physical semantics | Interpretability is encouraged through model and supervision choices |

A probe's accuracy alone does not establish that the native predictor or planner uses the decoded variable. Intervention studies specify the output affected and the controls used.

'''
        if m.get('comparison_table'):
            table = m['comparison_table']
            body += f"## {table['title']}\n\n| " + ' | '.join(table['columns']) + ' |\n'
            body += '| ' + ' | '.join(':---' for _ in table['columns']) + ' |\n'
            body += ''.join('| ' + ' | '.join(row) + ' |\n' for row in table['rows']) + '\n'
        for group in m['groups']:
            body += f"## {group['title']}\n\n"
            group_ids = group['ids'] if group.get('order') == 'listed' else sorted(group['ids'], key=lambda pid: byid[pid]['canonical_title'].casefold())
            body += ''.join(entry(byid[pid], path, True) for pid in group_ids)
        body += f"## Method comparisons\n\n{m['connections']}\n\n"
        if m.get('candidate_ids'):
            candidate_byid = {c['id']: c for c in cfg['candidates']}
            body += '## Candidate papers\n\n'
            for cid in m['candidate_ids']:
                c = candidate_byid[cid]
                body += f"- [{c['title']}](../candidates.md#paper-{cid}) · {c['publication']}\n"
            body += '\n'
        body += '## Related topics\n\n'
        body += ''.join(f"- [{bymod[mid]['title']}]({relative(module_path(bymod[mid]), path)})\n" for mid in m['related'])
        body += '\n[Back to paper index](../../README.md)\n'
        out[path] = body
    path = module_path(supplement)
    body = '''[← Paper index](../README.md#research-map) · [Reading guide](reading-guide.md)

# Supplementary Reading

Background papers and methods from adjacent settings support the six main topics. Entries retain their original evaluation domains and explain their relevance to world-model research.

'''
    for group in supplement['groups']:
        body += f"## {group['title']}\n\n{group['intro']}\n\n"
        body += ''.join(entry(p, path, True) for p in selected(supplement['id']) if p['supplement_group'] == group['id'])
    out[path] = body + '[Back to paper index](../README.md)\n'

    # Keep previous topic URLs and paper anchors usable after reclassification.
    for legacy in cfg['legacy_pages']:
        path = legacy['path']
        moved = [pid for pid in legacy['papers'] if paper_location(byid[pid]).split('#')[0] != path]
        if not moved:
            continue
        if path not in out:
            out[path] = f"[← Paper index](../../README.md#research-map)\n\n# {legacy['title']}\n\nThese papers are now organized by their contribution to adaptation, planning, or supplementary background.\n\n"
        else:
            out[path] += '\n## Entries in related sections\n\n'
        for pid in moved:
            out[path] += f'<a id="paper-{pid}"></a>\n- {linked_paper(pid, path)}\n'
        out[path] += '\n'

    path = 'docs/reading-guide.md'
    route = '''[← Paper index](../README.md#papers) · [Supplementary reading](supplementary.md)

# Reading Path

Twelve papers connect evidence about learned world structure to composition, geometry, adaptation, planning, and explicit generalization tests. The four sections can also be read independently. Topic branches below the main path compare additional mechanisms and evaluation protocols.

'''
    sections = {s['start']: s for s in cfg['route_sections']}
    for i, r in enumerate(cfg['route'], 1):
        if i in sections:
            s = sections[i]; route += f"## {s['title']}\n\n{s['intro']}\n\n"
        p = byid[r['id']]
        route += f"### {i:02d} · {r['label']}\n\n**[{p['canonical_title']}]({p['links']['paper']})**\n\n{author_label(p)} · **{p['publication']['label']}**\n\n"
        route += f"**Method:** {p['annotation']['focus']}\n\n**Evaluation:** {p['annotation']['boundary']}\n\n**Connection:** {r['connection']}\n\n"
        route += f"[Topic: {bymod[p['primary_module']]['title']}]({relative(paper_location(p), path)})\n\n"
    route += '''## Further reading

'''
    for branch in cfg['route_extensions']:
        route += f"- **{branch['label']}:** " + '; '.join(linked_paper(pid, path) for pid in branch['ids']) + '. ' + branch['connection'] + '\n'
    route += '\n[Candidate papers](candidates.md) · [All six topics](../README.md#research-map) · [Supplementary reading](supplementary.md)\n'
    out[path] = route

    candidates = '[← Paper index](../README.md#research-map) · [Reading guide](reading-guide.md)\n\n# Candidate Papers\n\nThese papers are listed separately from the main catalog and are excluded from its counts and bibliography.\n\n'
    for c in cfg['candidates']:
        candidates += f"<a id=\"paper-{c['id']}\"></a>\n## {c['title']}\n\n{author_label({'bibliography': {'authors': c['authors']}})} · **{c['publication']}** · [Paper]({c['url']})\n\n"
        if c['aliases']:
            candidates += 'Earlier titles: ' + '; '.join(c['aliases']) + '.\n\n'
        candidates += f"- **Method:** {c['method']}\n- **Evaluation:** {c['evaluation']}\n- **Related topic:** [{bymod[c['module']]['title']}]({relative(module_path(bymod[c['module']]), 'docs/candidates.md')})\n\n"
    out['docs/candidates.md'] = candidates
    out['docs/sources.md'] = '''[← Overview](../README.md)

# Sources and Acknowledgments

## Paper information

Each record links to a formal publication page or author preprint. Where available, entries also include official code and project pages. Earlier titles are retained as aliases.

Entries describe contributions, methods, and evaluation scope. Background papers and methods from adjacent fields appear in [Supplementary Reading](supplementary.md). [Candidate papers](candidates.md) remain separate from the main catalog.

## Related resources

''' + resource_links + '''

## Visual assets

The [header illustration](../assets/research-map.svg) is an original vector composition for this repository. It depicts latent structure, transfer across environments, and planning. See the [asset notes](../assets/README.md).
'''
    out['references.bib'] = bibliography(papers)
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
