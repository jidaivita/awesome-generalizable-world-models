# Contributing

Suggestions, corrections, and pull requests are welcome.

## Scope

This list covers learned world representations, dynamics, generalization, adaptation, and the use of world models for prediction and decisions. Mechanistic analyses, modeling methods, theory, and evaluation studies are all in scope.

Work from adjacent fields can be included when it provides a directly relevant method. Describe the connection and keep findings tied to the setting in which they were established.

## Suggest a paper

Include:

- The paper title and an official publication or author-hosted link.
- The topic it belongs to.
- A brief description of its contribution.
- Code and project links, if available.

Explain what the paper adds to the existing list. Corrections to titles, links, publication information, and descriptions are equally useful.

## Entry format

```markdown
- **[Paper title](paper-url)**
  Venue Year · [Code](code-url) · [Project](project-url)
  One sentence describing the contribution.
```

Use one primary topic per paper. Keep earlier titles as aliases, and merge preprint and published versions rather than creating duplicate entries. Use formal proceedings, journal pages, author preprints, and official project repositories as sources. Leave unknown metadata unset.

## Editing the source

Paper records are stored in `data/papers.json`; topic guides and the reading path are defined in `data/map.json`. Update these files and regenerate the Markdown pages:

```bash
python3 scripts/validate.py
python3 scripts/build.py
python3 -m unittest discover -s tests
python3 scripts/build.py --check
```

The generated regions are marked in each file. Text outside these regions is preserved.

[Maintenance reference](docs/maintenance.md) · [Overview](README.md)
