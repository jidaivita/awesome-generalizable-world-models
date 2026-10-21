# Maintenance

[← Overview](../README.md)

The catalog uses Python 3.9 or later, JSON, and Markdown. No additional Python packages are required.

## Source layout

| Content | File |
| :--- | :--- |
| Paper metadata, links, and descriptions | `data/papers.json` |
| Topic guides, reading path, candidates, and related resources | `data/map.json` |
| Bibliographic export | `references.bib` |
| Page generation | `scripts/build.py` |
| Public note manifest | `publish-manifest.json` |
| Header illustration | `assets/research-map.svg` |

The README, six topic overviews, supplementary page, reading path, and BibTeX export share the same data source. Bibliographic records include the ordered author list, cited-edition year, source URL, and metadata verification date. The bibliography uses a generated-file header; unmarked files are not overwritten. The generator replaces only the region between its `BEGIN GENERATED RESEARCH MAP` and `END GENERATED RESEARCH MAP` markers. It preserves text outside the markers and refuses to overwrite an existing unmarked file.

## Build and validate

```bash
python3 scripts/build.py
python3 scripts/validate.py
python3 -m unittest discover -s tests
python3 scripts/build.py --check
```

Validation covers stable IDs, duplicate titles and aliases, arXiv identity, topic assignments, reading-path references, local links, and anchors. Repeated builds are deterministic.

## Metadata

Use stable IDs even when titles change. Store earlier titles in `aliases` and arXiv identifiers without version suffixes. Distinguish preprints, workshop papers, conference publications, and journal articles. Conference year and proceedings year may differ.

`source_review` records the date and depth of a source check. A successful HTTP request is not a content review. `reproduction` records execution evidence separately; a code link does not establish reproducibility.

The catalog retains all 30 original records alongside subsequent additions. Each paper has one primary topic or a supplementary assignment. Topic groups are validated against those assignments. Original IDs and previous topic-page anchors remain available after reclassification.

The reading path contains 12 papers from the main topics, with short branches for additional comparisons. Update the route and section descriptions together. Supplementary records require a group and a relevance statement; they remain part of the bibliography and public export. Candidate papers have a separate page and are excluded from catalog counts and the bibliography. Candidate identities are checked against catalog titles, aliases, and arXiv identifiers.

## Notes and exports

Public notes may be added under `public_notes/` and explicitly listed in the manifest. The export command copies only the explicitly listed pages, bibliography, templates, assets, licenses, and manifest-listed notes:

```bash
python3 scripts/export_public.py --output /absolute/path/to/export
```

Use a new or empty destination. The exporter does not copy source data, local state, tests, or arbitrary files from the working directory.

## Check external links

```bash
python3 scripts/check_links.py --output /absolute/path/to/link-report.json
```

The check records HTTP responses and redirects. A 403, 429, or timeout is marked for review; it does not automatically remove an entry or change source-review dates.
