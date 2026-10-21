#!/usr/bin/env python3
"""Offline schema, identity, reference, URL and local-link checks."""
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit
from build import ROOT, public_note_paths, read_sources, render


def require(condition, message):
    if not condition:
        raise ValueError(message)


def valid_url(value):
    if value is None:
        return
    u=urlsplit(value)
    require(u.scheme in {'https','http'} and bool(u.hostname) and not u.username and not u.password, f'Invalid URL: {value}')
    require(not any(t in u.hostname.lower() for t in ['feishu','larksuite','localhost','127.0.0.1','corp.']), 'Private/internal URLs must not enter public records')
    require(not any(k in u.query.lower() for k in ['token=','secret=','password=','api_key=']), 'Credential-like URL query is forbidden')


def validate_data(root=ROOT):
    papers,cfg,manifest=read_sources(root)
    mods={m['id'] for m in cfg['modules']}
    require(mods=={f'M{i}' for i in range(1,8)}, 'Expected seven modules')
    ids=[p['id'] for p in papers]
    require(len(ids)==len(set(ids)), 'Duplicate paper ID')
    selected=[p for p in papers if p['collection']=='seed_v0_2']
    require(len(selected)==30, 'Expected 30 papers')
    require(Counter(p['primary_module'] for p in selected)==dict(zip(sorted(mods),[4,6,4,4,4,4,4])), 'Module counts changed')
    route=[r['id'] for r in cfg['route']]
    require(len(route)==len(set(route))==12 and set(route)<=set(ids),'Invalid reading route')
    seen_titles={};seen_arxiv={}
    for p in papers:
        require(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',p['id']), 'Invalid stable ID')
        require(p['primary_module'] in mods,'Invalid primary module')
        secondary=p['secondary_modules']
        require(len(secondary)<=2 and len(set(secondary))==len(secondary) and set(secondary)<=mods and p['primary_module'] not in secondary,'Invalid cross references')
        for title in [p['canonical_title']]+p['aliases']:
            key=re.sub(r'\W','',title.casefold())
            require(key not in seen_titles or seen_titles[key]==p['id'],f'Duplicate title/alias: {title}')
            seen_titles[key]=p['id']
        aid=p['arxiv_id']
        if aid:
            key=re.sub(r'v\d+$','',aid)
            require(key not in seen_arxiv,'Duplicate arXiv identity')
            require(key==aid,'Store arXiv IDs without version suffix')
            seen_arxiv[key]=p['id']
        bib=p['bibliography']
        require(isinstance(bib['authors'],list) and bool(bib['authors']) and all(isinstance(a,str) and a.strip() for a in bib['authors']), 'Missing verified authors')
        require(isinstance(bib['year'],int) and 1900<=bib['year']<=2100, 'Invalid bibliographic year')
        require(bib['entry_type'] in {'misc','article','inproceedings'}, 'Invalid bibliography entry type')
        require(re.fullmatch(r'\d{4}-\d{2}-\d{2}',bib['verified_on']), 'Invalid bibliography review date')
        if bib['entry_type']=='article': require(bool(bib.get('journal')), 'Missing journal')
        if bib['entry_type']=='inproceedings': require(bool(bib.get('booktitle')), 'Missing proceedings title')
        valid_url(bib['source_url'])
        require(p['priority'] in {'anchor','core','reference'},'Invalid priority')
        require(p['reproduction']['status'] in {'not_run','attempted','verified'},'Invalid run status')
        if p['reproduction']['status']=='verified':
            require(all(p['reproduction'].get(k) for k in ['command','environment','log']),'Verified runs need evidence')
        for key in ['why','focus','boundary']:require(bool(p['annotation'][key].strip()),f'Missing annotation: {key}')
        require(re.fullmatch(r'\d{4}-\d{2}-\d{2}',p['source_review']['date']), 'Invalid source date')
        for value in [*p['links'].values(),p['publication']['source_url'],p['code']['url'],p['public_note']]:valid_url(value)
    for m in cfg['modules']:
        require(set(m['start'])<=set(ids),'Invalid module starting paper')
        require(set(m['related'])<=mods,'Invalid related module')
    public_note_paths(root,manifest)
    return len(papers)


def anchors(text):
    result=set(re.findall(r'<a\s+id="([^"]+)"',text))
    for title in re.findall(r'^#{1,6}\s+(.+)$',text,re.M):
        title=re.sub(r'\[([^\]]+)\]\([^)]*\)',r'\1',title)
        result.add(re.sub(r'[^\w\- ]','',title.lower()).replace(' ','-'))
    return result


def validate_links(root=ROOT):
    generated=render(root)
    docs={**{str(p.relative_to(root)):p.read_text() for p in root.glob('*.md')},**{str(p.relative_to(root)):p.read_text() for folder in ['docs','templates'] for p in (root/folder).rglob('*.md')},**generated}
    checked=0
    for rel,body in docs.items():
        body=re.sub(r'^```[^\n]*\n.*?^```[ \t]*$', '', body, flags=re.M | re.S)
        targets=re.findall(r'!?\[[^\]]+\]\(([^\s)]+)\)',body)
        targets += re.findall(r'<img\b[^>]*\bsrc=[\"\']([^\"\']+)[\"\']',body)
        for href in targets:
            if urlsplit(href).scheme:continue
            path,_,fragment=unquote(href).partition('#')
            dest=(root/rel).parent/path if path else root/rel
            dest=dest.resolve()
            require(dest.is_relative_to(root.resolve()),f'Link escapes repository: {rel}: {href}')
            key=dest.relative_to(root.resolve()).as_posix()
            require(key in docs or dest.is_file(),f'Missing local link: {rel}: {href}')
            if fragment:
                content=docs.get(key,dest.read_text() if dest.exists() else '')
                require(fragment in anchors(content),f'Missing anchor: {rel}: {href}')
            checked+=1
    return checked


if __name__=='__main__':
    n=validate_data();links=validate_links()
    print(f'OK: {n} papers; 7 modules; 12 route entries; {links} local links/anchors')
