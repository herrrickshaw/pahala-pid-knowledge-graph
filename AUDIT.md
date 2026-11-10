# Accuracy audit

How the graph was checked against the drawings (2026-11-11). Nobody has yet checked the graph by hand.

**Method.** 584 claims were sampled from the extractions (tags, process flow, signal lines, what an instrument
measures, off-page flags). 136 of them (23%) are deliberate false claims (altered tag digits, reversed flow,
unrelated bubbles joined). They were shuffled in. Four verifier agents, who were not shown the extractions or
the graph, judged each claim against the page images as correct, wrong or unclear, and also looked for tagged
items missing from the graph. Files: `audit/claims_NN.json`, `result_NN.json`, `key/`, `score.py`.

| Claim type | True claims | Confirmed | Unclear | Contradicted | False claims rejected |
|---|---|---|---|---|---|
| Tag exists | 155 | 155 (100%) | 0 | 0 | 50 / 50 |
| Off-page flag | 44 | 44 (100%) | 0 | 0 | n/a |
| Process flow | 68 | 64 (94%) | 4 | 0 | 40 / 43 |
| Instrument measures | 43 | 40 (93%) | 3 | 0 | n/a |
| Signal line | 138 | 121 (88%) | 15 | 2 | 33 / 43 |
| **All** | **448** | **424 (94.6%)** | **22** | **2** | **123 / 136 (90.4%)** |

**What this shows.**
- Tags, flags, flow and measurement claims held up. No true flow claim was contradicted. The one false flow claim
  that was accepted (P-207 pump to tank) is in fact true through the pump's relief line, so it was a bad decoy.
- Signal lines are the weak spot. Verifiers accepted 8 of 43 false signal claims because bubbles on one shared
  dashed bus look connected, and they accepted one reversed direction. So the 88% for signals is an upper bound,
  and signal direction is not well verified. P-209 (blower panel bus) alone had 10 unclear claims.
- The only two true claims contradicted were P-501 signals from YI to ZCO/ZCC (confidence 0.5). They were removed.
- Recall: no tagged item was found missing except four bubbles on P-101 whose numbers are clipped on the print,
  an element label FE-170121 on P-206, and TP-03 on P-203 (all already noted as unreadable), plus basin name labels
  (AX-01, PA-01, MB-01) that the graph keeps as names, and MCP 600,101, which is deliberately a sheet note.

**Limits.** The verifiers are models reading the same renderings as the extractors, so shared misreadings
(for example a symbol type with no legend) would not be caught. The 448 true claims cover about 57% of the roughly 791 facts in the extractions, capped at 10 per claim type per sheet and chosen at random; the population is (tags 307, lines 107, signals 251, measures 82, flags 44). A tag-by-tag check against the PDF text layer was possible only for pages 21 and
23-25, where tag numbers are real text (all matched); on the other sheets the text is outlined.

## Follow-up: shared signal buses (P-205 and P-209)

The audit showed the blower panels on P-205 (page 14) and P-209 (page 18) were drawn as one multi-drop bus,
with no individual line from each bubble to the blower. The graph had drawn point-to-point signals between
the blower and each bubble, which the drawing does not show. Each panel now has a `BUS-<blower>` node
(part of the panel's OIT). Bubbles attach to the bus, and the bus attaches to the blower at 0.5 confidence.
The SC-to-VFD signals are kept at 0.4 because the VFD is not on the bus and no direct line was seen. The 15
loops on those sheets still build, but the on/off loops there now read as acting on the bus rather than on the
blower. On the other sheets (P-101, P-401, P-601 to P-603) the graph does not join peer bubbles to each other,
so the bus-peer verdicts there were verifier leniency, not graph errors. Signal direction is still not well
verified anywhere on the shared buses.
