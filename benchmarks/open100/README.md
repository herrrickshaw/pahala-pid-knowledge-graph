# pid-to-kg scored on PID2Graph OPEN100 (2026-11-11)

Twelve real P&ID sheets from the OPEN100 reactor design, with ground-truth graphs from
[PID2Graph](https://zenodo.org/records/14803338) (Stürmer et al., CC BY-SA 4.0). The images and ground truth are
not copied here; fetch `PID2Graph/Complete/PID2Graph OPEN100/` from the Zenodo zip (11 MB, readable with HTTP
range requests). `extractions/` holds our per-sheet extractions, `score.py` the scorer, `results.txt` full output.

**Setup.** pid-to-kg's workflow, with three Claude subagents reading four sheets each (every tile opened) and writing
extraction files. They were told not to read the ground truth, and did not. They were told to record every drawn
symbol with a tight bbox, and valve tag bubbles were recorded as separate instruments, matching how PID2Graph counts
symbols. About 1.2M subagent tokens in all.

**Scoring.** PID2Graph labels pixel-level primitives (connector, crossing, arrow) between symbols. `score.py`
collapses it into symbol-to-symbol connections (a primitive-only region joins every symbol touching it) and matches
our items to ground-truth symbols of the same class by bbox centre within 1-4% of image width. Results barely change
across that range; numbers below are at 2%.

| Class | Ground truth | Ours | Precision | Recall | F1 |
|---|---|---|---|---|---|
| Valve | 257 | 249 | 1.00 | 0.96 | 0.98 |
| Instrument bubble | 350 | 358 | 0.98 | 1.00 | 0.99 |
| Inlet/outlet flag | 96 | 95 | 1.00 | 0.99 | 0.99 |
| Tank / pump / other symbol (merged) | 285 | 157 | 0.73 | 0.40 | 0.52 |
| Process connections (no instruments), matched nodes | | | 0.82 | 0.98 | 0.89 |
| All connections, matched nodes | | | 0.60 | 0.83 | 0.70 |

**Reading this.**
- Valves, instrument bubbles and flags are essentially solved on these sheets: 99% F1 for flags and bubbles.
- Equipment and in-line parts are the weak class. 162 of the 234 ground-truth "general" symbols are small fittings
  (nozzles, flanges, reducers, steam traps) that we did not record, and ground-truth labels are noisy (some pumps are
  labelled tank). Recall of 0.40 reflects that, not necessarily errors.
- Connections: when both ends are matched, 98% of ground-truth process connections are present in ours (recall), and
  82% of ours exist in the ground truth (precision). Recall against all ground-truth connections is 0.58 because of
  the unmatched fittings above. Instrument connections are less certain (precision 0.60).
- Treating junctions strictly as adjacent pairs gives precision 0.90 but recall 0.31 (`adj` rows in `results.txt`),
  so the "all pairs at a junction" convention is the fairer one.

**Caveats.**
- The scorer's first version treated "crossing" nodes as pass-through and gave edge precision of 0.13. That was a bug:
  in PID2Graph most crossing nodes are corners and tee junctions (only 2 of 734 have four connections). The numbers
  above are after the fix. The collapse rules and class mapping (valve kinds, boundaries excluded from the flag class,
  merged equipment class) were chosen by me after seeing early results, so treat them as post hoc.
- Our bounding boxes are model estimates. The 1-4% radius test shows localisation is not the limit here.
- OPEN100 sheets are clean CAD renders of about 2,300-3,300 px. The Pahala drawings are more complex and had no ground
  truth, so these numbers do not transfer directly.
- Twelve sheets, one drawing set, one run: no confidence intervals.
