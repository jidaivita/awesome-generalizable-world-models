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
    rank = {row['id']: i for i, row in enumerate(cfg['route'])}
    def selected(mid):
        return sorted((p for p in papers if p['primary_module'] == mid and p['collection'] == 'seed_v0_2'), key=lambda p: (rank.get(p['id'], 100), p['canonical_title'].casefold()))
    total = sum(p['collection'] == 'seed_v0_2' for p in papers)
    out = {}
    intro = '''<a id="top"></a>
<div align="center">

# Awesome Generalizable World Models

**世界模型研究地图 · 机理、表征几何、泛化与适应**

*How is world knowledge learned, organized, used, and adapted?*

'''
    intro += f'![Curated papers](https://img.shields.io/badge/精选论文-{total}-2563eb?style=flat-square) ![Reading route](https://img.shields.io/badge/阅读路线-{len(cfg["route"])}-0f766e?style=flat-square) ![Research modules](https://img.shields.io/badge/研究模块-{len(modules)}-7c3aed?style=flat-square)\n'
    intro += '''
[开始阅读](#start-here) · [阅读路线](#reading-route) · [七个模块](#research-map) · [全部精选](#papers) · [参与维护](CONTRIBUTING.md)

</div>

---

模型如何从有限经验中形成可迁移的世界知识？这些知识如何组织、如何被使用，又如何在新环境中被修正？

这里整理与这些问题直接相关的世界模型论文，覆盖表征、动态学习、预测、规划和适应。当前重点是 **表征几何 → 泛化与上下文学习 → 知识的实际使用**。每篇都附有收录理由，帮助从一个具体问题进入阅读。

<a id="start-here"></a>
## Start Here · 从两个问题出发

| 01 · 知识怎样组织？ | 02 · 新经验怎样起作用？ |
| :--- | :--- |
'''
    a,b=byid['interpreting-physics'],byid['context-diversity']
    intro += f"| **[{a['canonical_title']}]({a['links']['paper']})** | **[{b['canonical_title']}]({b['links']['paper']})** |\n"
    intro += '''| 从物理量、子空间与干预理解表征的组织和功能。 | 区分识别熟悉环境与从当前经历学习动力学。 |
| **带着问题读：** 可解码的信息，在模型行为中起了什么作用？ | **带着问题读：** 上下文带来的收益，究竟来自什么机制？ |

两篇论文共同提供一个阅读起点：提出明确的解释，寻找能够区分它们的对照，再判断结论覆盖到哪里。

<a id="research-map"></a>
## Research Map · 七个模块

| 模块 | 核心问题 | 精选 | 阅读指引 |
| :--- | :--- | :---: | :---: |
'''
    for m in modules:
        focus=' ★' if m['id'] in ['M2','M3','M4'] else ''
        intro += f"| [{m['id']} · {m['title']}{focus}](#{m['id'].lower()}) | {m['question']} | {len(selected(m['id']))} | [进入模块]({module_path(m)}) |\n"
    intro += '\n★ 近期重点。模块用于组织问题，每篇仅计入一个主模块；关联标签连接其他方向。\n\n'
    intro += '''<a id="reading-route"></a>
## Reading Route · 12 篇问题链

从机制问题出发，经过分析方法，再连接预测、规划与适应。可以按当前疑问选读；这条路线不是开始实践前的必修清单。

| # | 论文 | 这一步关注什么 |
| :---: | :--- | :--- |
'''
    for i,r in enumerate(cfg['route'],1):intro += f"| {i:02d} | [{r['label']}](#paper-{r['id']}) | {r['question']} |\n"
    intro += '\n[查看完整阅读指引与最小产物 →](docs/reading-guide.md)\n\n<a id="papers"></a>\n## Selected Papers · 精选论文\n\n**首读** 为两篇锚点，**路线** 为其余推荐阅读条目。发表状态与来源按条目记录，代码链接表示资源入口。\n\n'
    for m in modules:
        intro += f"<a id=\"{m['id'].lower()}\"></a>\n### {m['id']} · {m['title']}\n\n*{m['english']}*\n\n> {m['question']}\n\n"
        for p in selected(m['id']):
            tag={'anchor':' · **首读**','core':' · **路线**','reference':''}[p['priority']]
            intro += f"<a id=\"paper-{p['id']}\"></a>\n- **[{p['canonical_title']}]({p['links']['paper']})**{tag}<br>\n  {p['publication']['label']} · {resources(p)}<br>\n  {p['annotation']['why']}\n\n"
        intro += f"[阅读重点与论文联系 →]({module_path(m)}) · [返回目录 ↑](#research-map)\n\n"
    intro += '''<a id="notes"></a>
## Notes · 阅读与讨论

完整笔记可以保留在自己的笔记工具中。这里仅链接明确选择公开的内容；私人想法和未发表实验设计保留在私人笔记里。

[精读模板](templates/paper-note.md) · [主题比较模板](templates/comparison-note.md) · [分享模板](templates/sharing-note.md)
'''
    if notes:
        intro+='\n'+''.join(f'- [{title}]({path})\n' for title,path,_ in notes)
    intro+='''
## Contributing · 一起维护

欢迎补充直接相关的论文、修正来源与发表状态，或提出更好的阅读联系。推荐时请说明：**它回答什么问题、最值得看的证据是什么、与哪个模块有关**。

[收录与贡献指南](CONTRIBUTING.md) · [数据与生成说明](docs/maintenance.md) · [来源说明](docs/sources.md)

<sub>关注问题的积累，也关注不同解释之间的联系。精选池会随阅读逐步调整。</sub>
'''
    out['README.md'] = intro
    for m in modules:
        prefix=f"[← 首页](../../README.md#research-map) · [阅读路线](../reading-guide.md)\n\n# {m['id']} · {m['title']}\n\n*{m['english']}*\n\n> {m['question']}\n\n{m['intro']}\n\n{m['scope']}\n\n## 从哪里开始\n\n"
        for i,id in enumerate(m['start'],1):
            p=byid[id];target=f"#paper-{id}" if p['primary_module']==m['id'] else f"../../README.md#paper-{id}"
            prefix+=f"{i}. **[{next((r['label'] for r in cfg['route'] if r['id']==id), p['canonical_title'])}]({target})** — {p['annotation']['why']}\n"
        if m['id']=='M2':
            prefix+='''
## 三条阅读线索

| 线索 | 论文 | 阅读时先区分什么 |
| :--- | :--- | :--- |
| 自然形成的几何与功能 | Interpreting Physics、SMDS、Origins | 观察到的结构、竞争假设与功能证据 |
| 几何先验与动态学习 | GRWM、Group-Structured Latent Space、GeoWorld | 先验来自哪里，以及它独立带来的收益 |
| 几何与环境适应 | [Context and Diversity](m3-generalization.md#paper-context-diversity)、[Dynamics Are Learned](m3-generalization.md#paper-dynamics-geometries) | 环境变化、轨迹信息与可迁移结构 |

**工具按问题补充。** 先掌握 PCA/SVD、线性探针、周期变量编码、子空间比较、基本干预和留出验证；需要时再进入内在维数、拓扑分析或黎曼优化。

例如 `z(θ) = (cos θ, sin θ, cos 2θ, sin 2θ, …)` 由一个自由度控制，却可以占据多个线性方向。环境自由度、向量维度、线性跨度、流形内在维数与干预方向数需要分别理解。这是数学示例，不是模型测量结果。
'''
        prefix+='\n## 精选论文与阅读重点\n\n'
        for p in selected(m['id']):
            prefix+=f"<a id=\"paper-{p['id']}\"></a>\n### {p['canonical_title']}\n\n**{p['publication']['label']}** · {resources(p)}\n\n"
            if p['aliases']:prefix+='旧称／简称：'+ '；'.join(p['aliases'])+'。\n\n'
            prefix+=f"{p['annotation']['why']}\n\n- **重点看：** {p['annotation']['focus']}\n- **适用范围：** {p['annotation']['boundary']}\n"
            if p['secondary_modules']:prefix+='- **关联：** '+' · '.join(f"[{mid} · {bymod[mid]['title']}]({Path(module_path(bymod[mid])).name})" for mid in p['secondary_modules'])+'\n'
            prefix+='\n'
        prefix+=f"## 放在一起读\n\n{m['connections']}\n\n## 继续连接\n\n"
        prefix+='\n'.join(f"- [{mid} · {bymod[mid]['title']}]({Path(module_path(bymod[mid])).name}) — {bymod[mid]['question']}" for mid in m['related'])
        prefix+='\n\n[精读模板](../../templates/paper-note.md) · [主题比较模板](../../templates/comparison-note.md) · [返回首页 ↑](../../README.md)\n'
        out[module_path(m)] = prefix
    route='''[← 首页](../README.md#reading-route)

# 阅读路线 · 从机制问题到实际使用

这条路线连接 12 篇论文。它提供一个建议顺序，也允许按当前问题选读。每一步留下一个足够小、能够说明理解的产物。

## 01—03 · 建立问题

先理解知识的组织、新环境中的学习，以及如何检验底层结构。

'''
    for i,r in enumerate(cfg['route'],1):
        if i==4:route+='## 04—05 · 学习分析与建模方法\n\n从比较几何假设，走向几何诊断和长程预测。\n\n'
        if i==6:route+='## 06—08 · 接到可运行的预测与规划系统\n\n明确表示、动态模型和规划器的接口，再学习控制组件间的混杂因素。\n\n'
        if i==9:route+='## 09—12 · 连接先验、适应、可靠性与探索\n\n把已有理解扩展到环境变化和实际决策所需的信息。\n\n'
        p=byid[r['id']]
        route+=f"### {i:02d} · {r['label']}\n\n**[{p['canonical_title']}]({p['links']['paper']})**\n\n- **读完回答：** {r['question']}\n- **最小产物：** {r['output']}\n- **阅读重点：** [{bymod[p['primary_module']]['title']}]({module_path(bymod[p['primary_module']]).removeprefix('docs/')}#paper-{p['id']})\n\n"
    route+='''## 怎样把阅读变成积累

**索引浏览**只需知道论文在回答什么，以及为何相关。**精读**围绕疑问选择关键章节，留下 1—3 个核心图表或实验的精确定位。两三篇工作有具体联系时，再做一页**主题比较**：它们支持了什么解释，还有什么没有区分清楚。

数学和工具学习由阅读中的障碍驱动。一次阅读结束，只确定一个具体下一步：核对一个实验、弄懂一个定义、查一个资源，或尝试一个小分析。

## 一个可缩放的四周起步节奏

| 阶段 | 阅读重点 | 建议产物 |
| :--- | :--- | :--- |
| 第一周 | 两篇锚点 | 两份主张、证据与适用范围笔记 |
| 第二周 | SMDS 与 GRWM | 一页几何专题比较 |
| 第三周 | What Has a Foundation Model Found 或 DINO-WM | 一个关于信息使用的具体检查标准 |
| 第四周 | 按疑问选择 LeWM、Group-Latents 或 Dynamics-Geometries | 专题总结，或一个带对照的小分析 |

可以以 4—6 篇形成理解的笔记为起步目标，按实际时间调整。实验从已经选定的问题出发；资源条件和代码可用性需要单独确认。

[精读模板](../templates/paper-note.md) · [主题比较模板](../templates/comparison-note.md) · [返回精选列表](../README.md#papers)
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
