# Contributing

Suggestions, corrections, and pull requests are welcome.

## Scope

The list covers learned world models and their generalization across object configurations, environments, dynamics, and tasks. Entries may contribute a modeling method, representation analysis, theoretical result, or evaluation protocol. Each paper should have a clear connection to at least one of the six topics.

Papers should identify a reusable representation, a transfer or adaptation mechanism, evidence about what a world model learns, a connection to task performance, or an evaluation of generalization. Negative results and formal limits are within scope.

General-purpose architectures, language-model analysis methods, and policy-only simulation studies belong in [Supplementary Reading](docs/supplementary.md) when they provide useful background. State the connection and retain the original evaluation setting.

Describe the distribution shift and evaluation outcome when available. Distinguish zero-shot transfer, adaptation from context, and parameter updates; distinguish prediction accuracy from downstream policy performance. A structured latent space or an accurate probe alone does not establish causal use of the represented information.

## Suggest a paper

Include:

- The paper title, authors, publication year, and an official publication or author-hosted link.
- The topic it belongs to.
- A brief description of its contribution.
- Code and project links, if available.

Explain what the paper adds to the existing list. Corrections to titles, links, publication information, and descriptions are equally useful.

## Entry format

```markdown
- **Paper title**<br>
  First Author et al. · **Venue Year** · [Paper](paper-url) · [Code](code-url) · [Project](project-url)<br>
  One sentence describing the method, analysis, or evaluation.
```

Use one primary topic per paper. Keep earlier titles as aliases, and merge preprint and published versions rather than creating duplicate entries. Use formal proceedings, journal pages, author preprints, and official project repositories as sources. Leave unknown optional metadata unset. Verify author order and the year of the cited edition from the source. The full author list is used in `references.bib`; the index displays the first author.

## Editing the source

Paper records are stored in `data/papers.json`; topic guides and the reading path are defined in `data/map.json`. Update these files and regenerate the Markdown pages:

```bash
python3 scripts/build.py
python3 scripts/validate.py
python3 -m unittest discover -s tests
python3 scripts/build.py --check
```

The generated regions are marked in each file. Text outside these regions is preserved.

[Maintenance reference](docs/maintenance.md) · [Overview](README.md)

## Licensing

Contributions to catalog text and illustrations are included under CC BY 4.0; maintenance code is included under MIT. See [License](LICENSE.md).
