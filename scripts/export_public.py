#!/usr/bin/env python3
"""Explicit public field/path export; never recursively copies repository content."""
import argparse
from pathlib import Path
from build import ROOT, BEGIN, END, public_note_paths, read_sources, render

STATIC = ('templates/paper-note.md', 'templates/comparison-note.md', 'templates/sharing-note.md',
          'CONTRIBUTING.md', 'docs/maintenance.md',
          'assets/research-map.svg', 'assets/world-models-cover.png', 'assets/README.md',
          'LICENSE.md', 'LICENSES/CC-BY-4.0.txt', 'LICENSES/MIT.txt')


def export(root, output):
    from validate import validate_data
    validate_data(root)
    output=Path(output).resolve()
    if output==root.resolve() or root.resolve().is_relative_to(output):
        raise ValueError('Export destination must not contain the source repository')
    if output.exists() and any(output.iterdir()):
        raise ValueError('Use a new or empty export directory to avoid mixing private or stale files')
    payload={k:v for k,v in render(root).items()}
    for rel in STATIC:
        payload[rel]=(root/rel).read_bytes()
    _,_,manifest=read_sources(root)
    for _,rel,path in public_note_paths(root,manifest):payload[rel]=path.read_text()
    for rel,content in payload.items():
        p=output/rel;p.parent.mkdir(parents=True,exist_ok=True)
        if isinstance(content,bytes):p.write_bytes(content)
        else:p.write_text(content)
    return sorted(payload)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True,type=Path)
    args=parser.parse_args();print(f'Exported {len(export(ROOT,args.output))} public files')
