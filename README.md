# Pahala WWTP P&ID knowledge graph

A machine-extracted process knowledge graph of the 17 P&ID sheets (PDF pages 9-25) in the public
*Pahala Wastewater Treatment Plant Design/Build Drawings* (Brown and Caldwell for County of Hawaii,
EPA submission, July 2021). It was built with
[pid-to-kg](https://github.com/ScottDuncanAI/PID-to-Knowledge-Graph) (MIT), a Claude skill, as a trial
of that tool on a public drawing set listed in
[public-chemical-manufacturing-datasets](https://github.com/ScottDuncanAI/public-chemical-manufacturing-datasets).

## Contents

| Path | What it is |
|---|---|
| `graph/graph.json`, `graph/graph.duckdb` | The full graph (925 nodes, 1330 edges) |
| `graph/summary.md` | Readable plant overview, suitable as LLM context |
| `graph/qa_report.md` | Everything the QA pass flagged |
| `extractions/page_NN.json` | Per-sheet extractions the graph is built from |
| `manifest.json` | Page classification from the probe step |

The drawings themselves are **not** included. They are third-party engineering work; get the PDF from the
EPA: https://www.epa.gov/system/files/documents/2021-08/pahala-wwtp-design-build-drawings-2021-07-23.pdf

## Quality: read before using

**Not reviewed by an engineer.** Sheets were read by Claude models (one by hand, the rest by four
parallel subagents), not checked against the drawings by a person.

- Built with 0 structural errors but many warnings, see `graph/qa_report.md`.
- Some valve and fitting symbols have no legend; their types are guesses at confidence 0.4-0.6.
- Several pumps and tanks carry no printed tag; ids such as `PMPA` or `EQ-TANK` are placeholders.
- Pahala's 6-digit tags (e.g. `LT-040101`) do not parse as ISA-5.1, so the tool built no loops from them.
  Loop ids were set by hand on each instrument.
- Tag numbering restarts on sheet P-401 (`LCH-001`, `LAH-001`...), so same-named tags on P-101 and P-401
  were merged although they are different items (6 `name_conflict` warnings).
- Page 10 (P-201) was a partial first pass; check `tiles_reviewed` in each extraction file.
- Not suitable for design, operations, MOC, HAZOP or LOPA without engineering review.

## Query

```bash
python skills/pid-to-kg/scripts/kg_query.py graph/ downstream TNK-040100 --equipment
```
(from a clone of pid-to-kg). Example: the Anoxic Basin feeds the Pre-Aeration Basin, then the MBR basin.
