# Pahala WWTP: process knowledge graph summary

Built from `pahala.pdf` (17 sheets) by pid-to-kg 0.1.0 on 2026-11-10. The graph has 915 nodes and 1343 edges; this summary covers equipment-level flow, instruments and control loops. Query `graph.duckdb` or `graph.json` for pipe-segment and valve detail.

| Equipment | Instruments | Valves & fittings | Pipe segments | Control loops | Off-page links |
|---|---|---|---|---|---|
| 62 | 292 | 138 | 246 | 95 | 44 |

## Sheets

| Page | Drawing | Title | Type |
|---|---|---|---|
| 9 | P-101 | HEADWORKS FACILITY P&ID | pid |
| 10 | P-201 | Anoxic Basin | pid |
| 11 | P-202 | PRE-AERATION BASIN | pid |
| 12 | P-203 | MEMBRANE BIOREACTOR BASIN | pid |
| 13 | P-204 | PERMEATE COLLECTION | pid |
| 14 | P-205 | PRE-AERATION AND MEMBRANE BIOREACTOR TOWERS | pid |
| 15 | P-206 | ACID CLEANING | pid |
| 16 | P-207 | PH ADJUSTMENT | pid |
| 17 | P-208 | EQUIPMENT GALLERY PUMP STATION | pid |
| 18 | P-209 | WAS STORAGE AND STAND-BY BLOWERS | pid |
| 19 | P-210 | WAS STORAGE BASIN | pid |
| 20 | P-211 | WAS PUMP | pid |
| 21 | P-401 | IRRIGATION EQUALIZATION TANK P&ID | pid |
| 22 | P-501 | SUBSURFACE DRIP EFFLUENT DISPOSAL P&ID | pid |
| 23 | P-601 | GENERATOR BULK FUEL STORAGE P&ID | pid |
| 24 | P-602 | GENERATOR DAY TANK P&ID | pid |
| 25 | P-603 | STANDBY GENERATOR P&ID | pid |

## Process flow (equipment to equipment)

Each line reads *upstream → downstream*, with the pipe lines and in-line items between them. Pipes, valves and instruments are collapsed; use `kg_query.py path` for the full route.

- **3W UTILITY WATER** → **FINE SCREEN (SCREEN 2): inclined screw/auger screen with M drive and spray wash**: through solenoid valve
- **3W UTILITY WATER** → **OTHER USES**
- **FINE SCREEN (SCREEN 2): inclined screw/auger screen with M drive and spray wash** → **BAG OR CONTAINER (screenings)**
- **RS FROM PAHALA** → **Manual bar rack channel (HWWL, inclined rack symbol)**: through Influent flow meter flume/venturi with ultrasonic sensor above it (FIT 100.002), OVERFLOW WEIR
- **RS FROM PAHALA** → **Screening channel (HWWL) with fine screen, inside VENDOR PACKAGE**: through Influent flow meter flume/venturi with ultrasonic sensor above it (FIT 100.002)
- **Manual bar rack channel (HWWL, inclined rack symbol)** → **GRIT REMOVAL TANK**
- **Screening channel (HWWL) with fine screen, inside VENDOR PACKAGE** → **GRIT REMOVAL TANK**
- **Screening channel (HWWL) with fine screen, inside VENDOR PACKAGE** → **Manual bar rack channel (HWWL, inclined rack symbol)**: through OVERFLOW WEIR
- **GRIT REMOVAL TANK** → **TNK-040100** (ANOXIC BASIN AX-01): crosses sheets
- **TNK-040100** (ANOXIC BASIN AX-01) → **Recycle pump (tag not printed, typical for 2 pumps, right)**
- **TNK-040100** (ANOXIC BASIN AX-01) → **Recycle pump (tag not printed, typical for 2 pumps, left)**
- **Recycle pump (tag not printed, typical for 2 pumps, right)** → **TNK-050100** (PA-01 PRE-AERATION BASIN): through check valve, reducer, FE-040141, reducer, gate valve; crosses sheets
- **Recycle pump (tag not printed, typical for 2 pumps, left)** → **TNK-050100** (PA-01 PRE-AERATION BASIN): through reducer, FE-040141, reducer, gate valve; crosses sheets
- **TNK-050100** (PA-01 PRE-AERATION BASIN) → **TNK-070100** (MB-01 MEMBRANE BIOREACTOR BASIN): through WE-050121; crosses sheets
- **TNK-070100** (MB-01 MEMBRANE BIOREACTOR BASIN) → **SMU-070121** (Submerged membrane unit, two stacked tiers)
- **TNK-070100** (MB-01 MEMBRANE BIOREACTOR BASIN) → **SMU-070111** (Submerged membrane unit, two stacked tiers)
- **SMU-070121** (Submerged membrane unit, two stacked tiers) → **PMP-080101** (Permeate pump (boxed marker '4' inside symbol)): through ball valve, butterfly valve, butterfly valve, expansion joint, reducer; crosses sheets
- **SMU-070121** (Submerged membrane unit, two stacked tiers) → **CONTACT BASIN**: through ball valve, butterfly valve, check valve, FE-080141, reducer, FCV-080132, reducer, reducer, reducer; crosses sheets
- **SMU-070111** (Submerged membrane unit, two stacked tiers) → **PMP-080101** (Permeate pump (boxed marker '4' inside symbol)): through ball valve, butterfly valve, butterfly valve, expansion joint, reducer; crosses sheets
- **SMU-070111** (Submerged membrane unit, two stacked tiers) → **CONTACT BASIN**: through ball valve, butterfly valve, check valve, FE-080141, reducer, FCV-080132, reducer, reducer, reducer; crosses sheets
- **PMP-080101** (Permeate pump (boxed marker '4' inside symbol)) → **CONTACT BASIN**: through reducer, expansion joint, check valve, butterfly valve, FE-080141, reducer, FCV-080132, reducer, reducer, reducer; crosses sheets
- **CONTACT BASIN** → **IRRIGATION EQUALIZATION TANK (printed 'TANK'; 'EQUALIZATION TANK' in LAH-402 label)**
- **IRRIGATION EQUALIZATION TANK (printed 'TANK'; 'EQUALIZATION TANK' in LAH-402 label)** → **DRIP ZONE 4**: through FE-403, motor operated valve; crosses sheets
- **IRRIGATION EQUALIZATION TANK (printed 'TANK'; 'EQUALIZATION TANK' in LAH-402 label)** → **DRIP ZONE 3**: through FE-403, motor operated valve; crosses sheets
- **IRRIGATION EQUALIZATION TANK (printed 'TANK'; 'EQUALIZATION TANK' in LAH-402 label)** → **DRIP ZONE 2**: through FE-403, motor operated valve; crosses sheets
- **IRRIGATION EQUALIZATION TANK (printed 'TANK'; 'EQUALIZATION TANK' in LAH-402 label)** → **DRIP ZONE 1**: through FE-403, motor operated valve; crosses sheets
- **Source of bold dashed line at XV-070181 (not drawn)** → **SMU- (FUTURE MEMBRANES)**: lines 3"-A; through XV-070181, manual valve
- **Source of bold dashed line at XV-070181 (not drawn)** → **SMU-070121** (Submerged membrane unit, two stacked tiers): through XV-070181, manual valve
- **Source of bold dashed line at XV-070181 (not drawn)** → **SMU-070111** (Submerged membrane unit, two stacked tiers): through XV-070181, manual valve
- **Source of bold dashed line at XV-070181 (not drawn)** → **TNK-070100** (MB-01 MEMBRANE BIOREACTOR BASIN): through XV-070181
- **SMU- (FUTURE MEMBRANES)** → **PMP-080101** (Permeate pump (boxed marker '4' inside symbol)): through ball valve, butterfly valve, butterfly valve, expansion joint, reducer; crosses sheets
- **SMU- (FUTURE MEMBRANES)** → **CONTACT BASIN**: through ball valve, butterfly valve, check valve, FE-080141, reducer, FCV-080132, reducer, reducer, reducer; crosses sheets
- **UTILITY WATER** → **Chemical injector/eductor symbol on utility water line (acid injection point)**: through ball valve, pressure regulator, XV-170103
- **Chemical injector/eductor symbol on utility water line (acid injection point)** → **PMP-080101** (Permeate pump (boxed marker '4' inside symbol)): through check valve, ball valve, FE-170122, ball valve, butterfly valve, butterfly valve, expansion joint, reducer; crosses sheets
- **Chemical injector/eductor symbol on utility water line (acid injection point)** → **CONTACT BASIN**: through check valve, ball valve, FE-170122, ball valve, butterfly valve, check valve, FE-080141, reducer, FCV-080132, reducer, reducer, reducer; crosses sheets
- **DRAIN FROM EQUIPMENT BLDG** → **TNK-120100** (WW-01 EQUIPMENT GALLERY PUMP STATION wet well)
- **HYPOCHLORITE SOLUTION** → **CONTACT BASIN**
- **TV-070182** (TV-070182 outlet box with telescoping/slide valve stem on basin right wall (text rotated)) → **TNK-190100** (WAS STORAGE BASIN): lines 3"-WAS; through motor operated valve, control valve, FE-070186, motor operated valve, valve in WAS inlet line to basin (diamond/bar symbol, type unclear); crosses sheets
- **TNK-190100** (WAS STORAGE BASIN) → **WAS pump (tag printed as 'PMP-' only, number missing); motor M drawn at drive end**: through valve in WAS outlet line (bow-tie/bar symbol, type unclear), reducer; crosses sheets
- **WAS pump (tag printed as 'PMP-' only, number missing); motor M drawn at drive end** → **WAS TRUCK**: through reducer, check valve, gate valve
- **Inlet filter/silencer (two hatched boxes joined by a pipe loop at blower inlet)** → **BLR-100101** (PRE-AERATION BLOWER 1)
- **BLR-100101** (PRE-AERATION BLOWER 1) → **FBD-050111** (Diffuser grid in basin bottom (FBD-050111; fine bubble diffuser inferred from tag)): through check valve, manual valve, reducer, TP-01; crosses sheets
- **Inlet filter/silencer (two hatched boxes joined by a pipe loop at blower inlet)** → **BLR-090101** (MEMBRANE BIOREACTOR BLOWER 1)
- **BLR-090101** (MEMBRANE BIOREACTOR BLOWER 1) → **SMU-070121** (Submerged membrane unit, two stacked tiers): lines 3"-A; through check valve, manual valve, reducer, butterfly valve, expansion joint; crosses sheets
- **BLR-090101** (MEMBRANE BIOREACTOR BLOWER 1) → **SMU-070111** (Submerged membrane unit, two stacked tiers): lines 3"-A; through check valve, manual valve, reducer, butterfly valve, expansion joint; crosses sheets
- **BLR-090101** (MEMBRANE BIOREACTOR BLOWER 1) → **SMU- (FUTURE MEMBRANES)**: lines 3"-A; through check valve, manual valve, reducer, butterfly valve, expansion joint; crosses sheets
- **TNK-170100** (OXALIC ACID 55 GAL. DRUM) → **Chemical injector/eductor symbol on utility water line (acid injection point)**: through quick connect, flexible hose, quick connect, ball valve, FI-170121
- **PMP-120111** (Submersible pump) → **TNK-040100** (ANOXIC BASIN AX-01): through diamond symbol on pump A riser (coupling/union type not identified), check valve, manual valve, reducer; crosses sheets
- **PMP-120112** (Submersible pump) → **TNK-040100** (ANOXIC BASIN AX-01): through diamond symbol on pump B riser (coupling/union type not identified), check valve, manual valve, reducer; crosses sheets
- **BLR-110101** (WAS STORAGE BLOWER) → **SMU-070121** (Submerged membrane unit, two stacked tiers): lines 3"-A; through vent/silencer-type symbol on blower 110101 discharge (unclear), check valve, butterfly valve, reducer, butterfly valve, manual valve, reducer, butterfly valve, expansion joint; crosses sheets
- **BLR-110101** (WAS STORAGE BLOWER) → **SMU-070111** (Submerged membrane unit, two stacked tiers): lines 3"-A; through vent/silencer-type symbol on blower 110101 discharge (unclear), check valve, butterfly valve, reducer, butterfly valve, manual valve, reducer, butterfly valve, expansion joint; crosses sheets
- **BLR-110101** (WAS STORAGE BLOWER) → **SMU- (FUTURE MEMBRANES)**: lines 3"-A; through vent/silencer-type symbol on blower 110101 discharge (unclear), check valve, butterfly valve, reducer, butterfly valve, manual valve, reducer, butterfly valve, expansion joint; crosses sheets
- **BLR-110101** (WAS STORAGE BLOWER) → **FBD-050111** (Diffuser grid in basin bottom (FBD-050111; fine bubble diffuser inferred from tag)): through vent/silencer-type symbol on blower 110101 discharge (unclear), check valve, butterfly valve, reducer, butterfly valve, manual valve, TP-01; crosses sheets
- **BLR-110101** (WAS STORAGE BLOWER) → **FBD-190103** (Fine bubble diffuser grid): through vent/silencer-type symbol on blower 110101 discharge (unclear), check valve, butterfly valve, reducer, butterfly valve; crosses sheets
- **BLR-110111** (STAND-BY BLOWER) → **SMU-070121** (Submerged membrane unit, two stacked tiers): lines 3"-A; through vent/silencer-type symbol on blower 110111 discharge (unclear), check valve, manual valve, reducer, butterfly valve, expansion joint; crosses sheets
- **BLR-110111** (STAND-BY BLOWER) → **SMU-070111** (Submerged membrane unit, two stacked tiers): lines 3"-A; through vent/silencer-type symbol on blower 110111 discharge (unclear), check valve, manual valve, reducer, butterfly valve, expansion joint; crosses sheets
- **BLR-110111** (STAND-BY BLOWER) → **SMU- (FUTURE MEMBRANES)**: lines 3"-A; through vent/silencer-type symbol on blower 110111 discharge (unclear), check valve, manual valve, reducer, butterfly valve, expansion joint; crosses sheets
- **BLR-110111** (STAND-BY BLOWER) → **FBD-050111** (Diffuser grid in basin bottom (FBD-050111; fine bubble diffuser inferred from tag)): through vent/silencer-type symbol on blower 110111 discharge (unclear), check valve, manual valve, TP-01; crosses sheets
- **TNK-160100** (SODIUM HYDROXIDE 55 GAL. DRUM) → **PMP-160101** (Sodium hydroxide dosing pump (plug-in))
- **PMP-160101** (Sodium hydroxide dosing pump (plug-in)) → **TNK-160100** (SODIUM HYDROXIDE 55 GAL. DRUM): through relief valve
- **PMP-160101** (Sodium hydroxide dosing pump (plug-in)) → **TNK-040100** (ANOXIC BASIN AX-01): crosses sheets
- **T-600,201** (BULK FUEL STORAGE TANK (double-walled, within vendor package)) → **FLT-600,202** (GENERATOR FUEL FILTER): lines 1"-FOS; through strainer, unlabelled inline device with bracket tab on FOS line (type uncertain), manual valve, diamond/bow-tie symbol on FOS line (unlabelled, type uncertain), diamond/bow-tie symbol (unlabelled, type uncertain), manual valve; crosses sheets
- **FLT-600,202** (GENERATOR FUEL FILTER) → **P-600,203** (GENERATOR FUEL TRANSFER PUMP 1 (gear-type symbol)): lines 1"-FOS; through diamond/bow-tie symbol (unlabelled, type uncertain), check valve
- **P-600,203** (GENERATOR FUEL TRANSFER PUMP 1 (gear-type symbol)) → **RELIEF VALVE OUTLET (destination not drawn)**: lines 1"-FOS; through relief valve
- **P-600,203** (GENERATOR FUEL TRANSFER PUMP 1 (gear-type symbol)) → **T-600,204** (GENERATOR DAY TANK (double-walled)): lines 1"-FOS; through inline valve symbol with stem tick (type uncertain), diamond/bow-tie symbol (unlabelled, type uncertain)
- **T-600,204** (GENERATOR DAY TANK (double-walled)) → **P-600,205** (GENERATOR FUEL TRANSFER PUMP 2 (gear-type symbol)): lines 1"-FOS; through strainer, inline device with bracket tab (unlabelled, type uncertain), diamond/bow-tie symbol (unlabelled, type uncertain), check valve
- **T-600,204** (GENERATOR DAY TANK (double-walled)) → **P-600,207** (GENERATOR ONBOARD FUEL PUMP (gear-type symbol)): lines 1"-FOS; through strainer, inline device with bracket tab (unlabelled, type uncertain), manual valve, diamond/bow-tie symbol (unlabelled, type uncertain), diamond/bow-tie symbol (unlabelled, type uncertain), flexible hose; crosses sheets
- **P-600,205** (GENERATOR FUEL TRANSFER PUMP 2 (gear-type symbol)) → **RELIEF VALVE OUTLET (destination not drawn)**: lines 1"-FOR; through relief valve
- **P-600,205** (GENERATOR FUEL TRANSFER PUMP 2 (gear-type symbol)) → **T-600,201** (BULK FUEL STORAGE TANK (double-walled, within vendor package)): lines 1"-FOR; through inline valve symbol with stem tick (type uncertain), manual valve, diamond/bow-tie symbol (unlabelled, type uncertain), diamond/bow-tie symbol on FOR line (unlabelled, type uncertain), manual valve; crosses sheets
- **P-600,207** (GENERATOR ONBOARD FUEL PUMP (gear-type symbol)) → **GEN-600,209** (STANDBY GENERATOR (diesel engine box with generator symbol)): lines 1"-FOS
- **GEN-600,209** (STANDBY GENERATOR (diesel engine box with generator symbol)) → **T-600,204** (GENERATOR DAY TANK (double-walled)): lines 1"-FOR; through flexible hose, diamond/bow-tie symbol (unlabelled, type uncertain), diamond/bow-tie symbol (unlabelled, type uncertain), manual valve; crosses sheets
- **GEN-600,209** (STANDBY GENERATOR (diesel engine box with generator symbol)) → **S-600,210** (GENERATOR EXHAUST SILENCER): lines 12"-EE; through flexible hose
- **S-600,210** (GENERATOR EXHAUST SILENCER) → **EXHAUST (to atmosphere)**: lines 12"-EE

Drains, vents and overflows (not process flow):
- ATMOSPHERE (tank vents) ← T-600,201, T-600,204
- DRAIN ← Chemical injector/eductor symbol on utility water line (acid injection point), PMP-080101, SMU- (FUTURE MEMBRANES), SMU-070111, SMU-070121
- DRAIN (D) ← S-600,210
- DRAIN (open end) ← T-600,204
- TO DRAIN ← Chemical injector/eductor symbol on utility water line (acid injection point)
- VENT TO ATMOSPHERE (TYP) ← Chemical injector/eductor symbol on utility water line (acid injection point), PMP-080101, SMU- (FUTURE MEMBRANES), SMU-070111, SMU-070121

## Equipment

| Tag | Kind | Description | Fed by | Feeds | Status | Sheets |
|---|---|---|---|---|---|---|
| BAG OR CONTAINER (screenings) | bin | BAG OR CONTAINER (screenings) | FINE SCREEN (SCREEN 2): inclined screw/auger screen with M drive and spray wash |  |  | P-101 |
| BLR-090101 | blower | MEMBRANE BIOREACTOR BLOWER 1 | Inlet filter/silencer (two hatched boxes joined by a pipe loop at blower inlet) | SMU- (FUTURE MEMBRANES), SMU-070111, SMU-070121 |  | P-205 |
| BLR-100101 | blower | PRE-AERATION BLOWER 1 | Inlet filter/silencer (two hatched boxes joined by a pipe loop at blower inlet) | FBD-050111 |  | P-205 |
| BLR-110101 | blower | WAS STORAGE BLOWER |  | FBD-050111, FBD-190103, SMU- (FUTURE MEMBRANES), SMU-070111, SMU-070121 |  | P-209 |
| BLR-110111 | blower | STAND-BY BLOWER |  | FBD-050111, SMU- (FUTURE MEMBRANES), SMU-070111, SMU-070121 |  | P-209 |
| CB 480V (circuit breaker, power feed from MDP-2 to blower 110101 VFD) | other | CB 480V (circuit breaker, power feed from MDP-2 to blower 110101 VFD) |  |  |  | P-209 |
| CB 480V (circuit breaker, power feed from MDP-2 to local control panel) | other | CB 480V (circuit breaker, power feed from MDP-2 to local control panel) |  |  |  | P-211 |
| CHGR-600,211 | other | GENERATOR STARTING BATTERY CHARGER |  |  |  | P-603 |
| CONTACT BASIN | other | CONTACT BASIN | Chemical injector/eductor symbol on utility water line (acid injection point), HYPOCHLORITE SOLUTION, PMP-080101, SMU- (FUTURE MEMBRANES), SMU-070111, SMU-070121 | IRRIGATION EQUALIZATION TANK (printed 'TANK'; 'EQUALIZATION TANK' in LAH-402 label) |  | P-401 |
| Chemical injector/eductor symbol on utility water line (acid injection point) | other | Chemical injector/eductor symbol on utility water line (acid injection point) | TNK-170100, UTILITY WATER | CONTACT BASIN, DRAIN, PMP-080101, TO DRAIN, VENT TO ATMOSPHERE (TYP) |  | P-206 |
| FBD-050111 | other | Diffuser grid in basin bottom (FBD-050111; fine bubble diffuser inferred from tag) | BLR-100101, BLR-110101, BLR-110111 |  |  | P-202 |
| FBD-190103 | other | Fine bubble diffuser grid | BLR-110101 |  |  | P-210 |
| FINE SCREEN (SCREEN 2): inclined screw/auger screen with M drive and spray wash | screen | FINE SCREEN (SCREEN 2): inclined screw/auger screen with M drive and spray wash | 3W UTILITY WATER | BAG OR CONTAINER (screenings) |  | P-101 |
| FLT-600,202 | filter | GENERATOR FUEL FILTER | T-600,201 | P-600,203 |  | P-602 |
| GEN-600,209 | other | STANDBY GENERATOR (diesel engine box with generator symbol) | P-600,207 | S-600,210, T-600,204 |  | P-603 |
| GRIT REMOVAL TANK | tank | GRIT REMOVAL TANK | Manual bar rack channel (HWWL, inclined rack symbol), Screening channel (HWWL) with fine screen, inside VENDOR PACKAGE | TNK-040100 |  | P-101 |
| HTR-600,208 | heater | GENERATOR ENGINE BLOCK HEATER (208V) |  |  |  | P-603 |
| IRRIGATION EQUALIZATION TANK (printed 'TANK'; 'EQUALIZATION TANK' in LAH-402 label) | tank | IRRIGATION EQUALIZATION TANK (printed 'TANK'; 'EQUALIZATION TANK' in LAH-402 label) | CONTACT BASIN | DRIP ZONE 1, DRIP ZONE 2, DRIP ZONE 3, DRIP ZONE 4 |  | P-401 |
| Inlet filter/silencer (two hatched boxes joined by a pipe loop at blower inlet) | filter | Inlet filter/silencer (two hatched boxes joined by a pipe loop at blower inlet) |  | BLR-100101 |  | P-205 |
| Inlet filter/silencer (two hatched boxes joined by a pipe loop at blower inlet) | filter | Inlet filter/silencer (two hatched boxes joined by a pipe loop at blower inlet) |  | BLR-090101 |  | P-205 |
| MXR-040111 | mixer | Anoxic basin mixer |  |  |  | P-201 |
| MXR-190111 | mixer | WAS basin mixer (submersible, motor and propeller) |  |  |  | P-210 |
| Manual bar rack channel (HWWL, inclined rack symbol) | screen | Manual bar rack channel (HWWL, inclined rack symbol) | RS FROM PAHALA, Screening channel (HWWL) with fine screen, inside VENDOR PACKAGE | GRIT REMOVAL TANK |  | P-101 |
| OIT (operator interface terminal) in blower package panel | other | OIT (operator interface terminal) in blower package panel |  |  |  | P-205 |
| OIT (operator interface terminal) in blower package panel | other | OIT (operator interface terminal) in blower package panel |  |  |  | P-205 |
| OIT (operator interface terminal, tag not printed) | other | OIT (operator interface terminal, tag not printed) |  |  |  | P-209 |
| OIT (operator interface terminal, tag not printed) | other | OIT (operator interface terminal, tag not printed) |  |  |  | P-209 |
| P-600,203 | positive_displacement_pump | GENERATOR FUEL TRANSFER PUMP 1 (gear-type symbol) | FLT-600,202 | RELIEF VALVE OUTLET (destination not drawn), T-600,204 |  | P-602 |
| P-600,205 | positive_displacement_pump | GENERATOR FUEL TRANSFER PUMP 2 (gear-type symbol) | T-600,204 | RELIEF VALVE OUTLET (destination not drawn), T-600,201 |  | P-602 |
| P-600,207 | positive_displacement_pump | GENERATOR ONBOARD FUEL PUMP (gear-type symbol) | T-600,204 | GEN-600,209 |  | P-603 |
| PMP-080101 | centrifugal_pump | Permeate pump (boxed marker '4' inside symbol) | Chemical injector/eductor symbol on utility water line (acid injection point), SMU- (FUTURE MEMBRANES), SMU-070111, SMU-070121 | CONTACT BASIN, DRAIN, VENT TO ATMOSPHERE (TYP) |  | P-204 |
| PMP-120111 | sump_pump | Submersible pump |  | TNK-040100 |  | P-208 |
| PMP-120112 | sump_pump | Submersible pump |  | TNK-040100 |  | P-208 |
| PMP-160101 | metering_pump | Sodium hydroxide dosing pump (plug-in) | TNK-160100 | TNK-040100, TNK-160100 |  | P-207 |
| PNL-120100 | other | EQUIPMENT GALLERY PUMP STATION LOCAL CONTROL PANEL |  |  |  | P-208 |
| PNL-190300 | package_unit | LOCAL CONTROL PANEL |  |  |  | P-211 |
| Recycle pump (tag not printed, typical for 2 pumps, left) | centrifugal_pump | Recycle pump (tag not printed, typical for 2 pumps, left) | TNK-040100 | TNK-050100 |  | P-201 |
| Recycle pump (tag not printed, typical for 2 pumps, right) | centrifugal_pump | Recycle pump (tag not printed, typical for 2 pumps, right) | TNK-040100 | TNK-050100 |  | P-201 |
| S-600,210 | other | GENERATOR EXHAUST SILENCER | GEN-600,209 | DRAIN (D), EXHAUST (to atmosphere) |  | P-603 |
| SMU- (FUTURE MEMBRANES) | membrane_filter | SMU- (FUTURE MEMBRANES) | BLR-090101, BLR-110101, BLR-110111, Source of bold dashed line at XV-070181 (not drawn) | CONTACT BASIN, DRAIN, PMP-080101, VENT TO ATMOSPHERE (TYP) | future | P-203 |
| SMU-070111 | membrane_filter | Submerged membrane unit, two stacked tiers | BLR-090101, BLR-110101, BLR-110111, Source of bold dashed line at XV-070181 (not drawn), TNK-070100 | CONTACT BASIN, DRAIN, PMP-080101, VENT TO ATMOSPHERE (TYP) |  | P-203 |
| SMU-070121 | membrane_filter | Submerged membrane unit, two stacked tiers | BLR-090101, BLR-110101, BLR-110111, Source of bold dashed line at XV-070181 (not drawn), TNK-070100 | CONTACT BASIN, DRAIN, PMP-080101, VENT TO ATMOSPHERE (TYP) |  | P-203 |
| Screening channel (HWWL) with fine screen, inside VENDOR PACKAGE | box | Screening channel (HWWL) with fine screen, inside VENDOR PACKAGE | RS FROM PAHALA | GRIT REMOVAL TANK, Manual bar rack channel (HWWL, inclined rack symbol) |  | P-101 |
| T-600,201 | tank | BULK FUEL STORAGE TANK (double-walled, within vendor package) | P-600,205 | ATMOSPHERE (tank vents), FLT-600,202 |  | P-601 |
| T-600,204 | tank | GENERATOR DAY TANK (double-walled) | GEN-600,209, P-600,203 | ATMOSPHERE (tank vents), DRAIN (open end), P-600,205, P-600,207 |  | P-602 |
| TNK-040100 | tank | ANOXIC BASIN AX-01 | GRIT REMOVAL TANK, PMP-120111, PMP-120112, PMP-160101 | Recycle pump (tag not printed, typical for 2 pumps, left), Recycle pump (tag not printed, typical for 2 pumps, right) |  | P-201 |
| TNK-050100 | tank | PA-01 PRE-AERATION BASIN | Recycle pump (tag not printed, typical for 2 pumps, left), Recycle pump (tag not printed, typical for 2 pumps, right) | TNK-070100 |  | P-202 |
| TNK-070100 | tank | MB-01 MEMBRANE BIOREACTOR BASIN | Source of bold dashed line at XV-070181 (not drawn), TNK-050100 | SMU-070111, SMU-070121 |  | P-203 |
| TNK-120100 | sump | WW-01 EQUIPMENT GALLERY PUMP STATION wet well | DRAIN FROM EQUIPMENT BLDG |  |  | P-208 |
| TNK-160100 | tank | SODIUM HYDROXIDE 55 GAL. DRUM | PMP-160101 | PMP-160101 |  | P-207 |
| TNK-170100 | tank | OXALIC ACID 55 GAL. DRUM |  | Chemical injector/eductor symbol on utility water line (acid injection point) |  | P-206 |
| TNK-190100 | tank | WAS STORAGE BASIN | TV-070182 | WAS pump (tag printed as 'PMP-' only, number missing); motor M drawn at drive end |  | P-210 |
| TV-070182 | other | TV-070182 outlet box with telescoping/slide valve stem on basin right wall (text rotated) |  | TNK-190100 |  | P-203 |
| VCP-100 | other | VCP 100, vendor control panel (number clipped on print) |  |  |  | P-101 |
| VCP-600,201 | other | FUEL TANK MONITORING SYSTEM (control panel) |  |  |  | P-601 |
| VCP-600,206 | other | GENERATOR DAY TANK PANEL (control panel, vendor package) |  |  |  | P-602 |
| VCP-600,209 | other | GENERATOR CONTROL PANEL (vendor package) |  |  |  | P-603 |
| VFD-090101 | other | Variable frequency drive |  |  |  | P-205 |
| VFD-100101 | other | Variable frequency drive |  |  |  | P-205 |
| VFD-110101 | other | Variable frequency drive |  |  |  | P-209 |
| VFD-110111 | other | Variable frequency drive |  |  |  | P-209 |
| WAS pump (tag printed as 'PMP-' only, number missing); motor M drawn at drive end | pump | WAS pump (tag printed as 'PMP-' only, number missing); motor M drawn at drive end | TNK-190100 | WAS TRUCK |  | P-211 |

## Instruments

Location is where the instrument senses the process. Pipe locations read `line (upstream item -> downstream item)`.

| Tag | Variable | Function | Mounted | Senses | Loop |
|---|---|---|---|---|---|
| AAH-080001 |  | other | scada |  | A-080001 |
| AAL-050102 |  | other | scada |  | A-050102 |
| AE-050101 |  | other | field | TNK-050100 | A-050101 |
| AE-050102 |  | other | field | TNK-050100 | A-050102 |
| AE-080001 |  | other | field | line (Valve with solid wedge on sample/drain loop (symbol type unclear) -> DRAIN) | A-080001 |
| AI (untagged) | analysis | indicator | plc |  | A-050101 |
| AI (untagged) | analysis | indicator | plc |  | T-050102 |
| AI (untagged) | analysis | indicator | plc |  | A-050102 |
| AI (untagged) | analysis | indicator | plc |  | F-070186 |
| AI (untagged) | analysis | indicator | plc |  | P-080121 |
| AI (untagged) | analysis | indicator | plc |  | F-080141 |
| AI (untagged) | analysis | indicator | plc |  | A-080001 |
| AIR-050101 |  | other | scada |  | A-050101 |
| AIR-050102 |  | other | scada |  | A-050102 |
| AIR-080001 |  | other | scada |  | A-080001 |
| AIT-050101 |  | other | field |  | A-050101 |
| AIT-050102 |  | other | field |  | A-050102 |
| AIT-080001 |  | other | field |  | A-080001 |
| AO (untagged) | analysis | other | plc |  | F-080132 |
| DI (untagged) | density | indicator | plc |  | Z-070181 |
| DI (untagged) | density | indicator | plc |  | Z-070181 |
| DI (untagged) | density | indicator | plc |  | Y-070181 |
| DI (untagged) | density | indicator | plc |  | L-070101 |
| DI (untagged) | density | indicator | plc |  | L-070102 |
| DI (untagged) | density | indicator | plc |  | Y-080111 |
| DI (untagged) | density | indicator | plc |  | Y-080112 |
| DI (untagged) | density | indicator | plc |  | Y-080101 |
| DI (untagged) | density | indicator | plc |  | Y-080101 |
| DI (untagged) | density | indicator | plc |  | Z-080132 |
| DO (untagged) | density | other | plc |  | Y-070181 |
| DO (untagged) | density | other | plc |  | X-080111 |
| DO (untagged) | density | other | plc |  | X-080112 |
| DO (untagged) | density | other | plc |  | Y-080101 |
| FAL-040141 |  | other | scada |  | F-040141 |
| FAL-070186 |  | other | scada |  | F-070186 |
| FC-080132 |  | other | scada |  | F-080132 |
| FE-040141 |  | other | field | in-line on line (reducer -> reducer) | F-040141 |
| FE-070186 |  | other | field | in-line on 3"-WAS (control valve -> motor operated valve) | F-070186 |
| FE-080141 |  | other | field | in-line on line (check valve -> reducer) | F-080141 |
| FE-170122 |  | other | field | in-line on line (ball valve -> ACID WASH TO MB-01) | F-170122 |
| FE-403 | flow | element | field | in-line on line (IRRIGATION EQUALIZATION TANK (printed 'TANK'; 'EQUALIZATION TANK' in LAH-402 label) -> TO EFFLUENT DISPOSAL REF SHT P-501) | F-403 |
| FI-090101 |  | other | field | line (check valve -> manual valve) |  |
| FI-100.002 |  | other | dcs |  | F-100002 |
| FI-100101 |  | other | field | line (check valve -> manual valve) |  |
| FI-110101 |  | other | local_panel | line (BLR-110101 -> vent/silencer-type symbol on blower 110101 discharge (unclear)) |  |
| FI-110111 |  | other | local_panel | line (BLR-110111 -> vent/silencer-type symbol on blower 110111 discharge (unclear)) |  |
| FI-170121 |  | other | field | in-line on line (ball valve -> Chemical injector/eductor symbol on utility water line (acid injection point)) |  |
| FIC-040121 |  | other | scada |  | F-040121 |
| FIR-040141 |  | other | scada |  | F-040141 |
| FIR-070186 |  | other | scada |  | F-070186 |
| FIR-403 | flow | indicator | scada |  | F-403 |
| FIT-040141 |  | other | field |  | F-040141 |
| FIT-070186 |  | other | field |  | F-070186 |
| FIT-080141 |  | other | field |  | F-080141 |
| FIT-100.002 |  | other | field | Influent flow meter flume/venturi with ultrasonic sensor above it (FIT 100.002) | F-100002 |
| FIT-170122 |  | other | field |  | F-170122 |
| FIT-403 | flow | transmitter | field | in-line on line (IRRIGATION EQUALIZATION TANK (printed 'TANK'; 'EQUALIZATION TANK' in LAH-402 label) -> TO EFFLUENT DISPOSAL REF SHT P-501) | F-403 |
| FQIR-080141 |  | other | scada |  | F-080141 |
| FQIR-170122 |  | other | scada |  | F-170122 |
| HMI (untagged) | hand | hand_switch | local_panel |  |  |
| HS-040111 |  | other | mcc |  |  |
| HS-040121 |  | other | mcc |  |  |
| HS-070181 |  | other | field |  | H-070181 |
| HS-080101 |  | other | field |  | H-080101 |
| HS-080111 |  | other | field |  | H-080111 |
| HS-080112 |  | other | field |  | H-080112 |
| HS-170103 |  | other | field |  | H-170103 |
| HS-190111 |  | other | local_panel |  | H-190111 |
| HS-500,101 |  | other | field |  | H-500101 |
| HS-600,201F |  | other | field |  | H-600201F |
| JS-040111 |  | other | mcc |  | J-040111 |
| JS-080101 |  | other | field |  | J-080101 |
| JS-190111 |  | other | local_panel |  |  |
| LAH (untagged) | level | alarm | dcs |  |  |
| LAH-001@P-101 | level | alarm | scada |  | L-001@P-101 |
| LAH-001@P-401 | level | alarm | scada |  | L-001@P-401 |
| LAH-040101 |  | other | scada |  | L-040101 |
| LAH-040103 |  | other | scada |  | L-040103 |
| LAH-070102 |  | other | scada |  | L-070102 |
| LAH-100.125 |  | other | dcs |  |  |
| LAH-190102 |  | other | scada |  | L-190102 |
| LAH-402 | level | alarm | dcs |  | L-402 |
| LAH-600,201B |  | other | plc |  | L-600201B |
| LAH-600,201C |  | other | plc |  | L-600201C |
| LAH-600,204A |  | other | plc |  | L-600204A |
| LAH-600,204D |  | other | plc |  | L-600204D |
| LAL-001@P-101 | level | alarm | scada |  | L-001@P-101 |
| LAL-001@P-401 | level | alarm | scada |  | L-001@P-401 |
| LAL-040101 |  | other | scada |  | L-040101 |
| LAL-040102 |  | other | scada |  | L-040102 |
| LAL-070101 |  | other | scada |  | L-070101 |
| LAL-190102 |  | other | scada |  | L-190102 |
| LAL-600,201A |  | other | plc |  | L-600201A |
| LAL-600,204B |  | other | plc |  | L-600204B |
| LCH-001@P-101 | level | controller | scada |  | L-001@P-101 |
| LCH-001@P-401 | level | controller | scada |  | L-001@P-401 |
| LCH-001@P-401#2 | level | controller | scada |  | L-001@P-401#2 |
| LCL-001@P-101 | level | controller | scada |  | L-001@P-101 |
| LCL-001@P-401 | level | controller | scada |  | L-001@P-401 |
| LCL-001@P-401#2 | level | controller | scada |  | L-001@P-401#2 |
| LCL-001@P-401#3 | level | controller | scada |  | L-001@P-401#3 |
| LDAH-100.115 |  | other | dcs |  | L-100115 |
| LDAH-100.124 |  | other | dcs |  | L-100124 |
| LDI-100.124 |  | other | scada |  | L-100124 |
| LE-040101 |  | other | field | TNK-040100 | L-040101 |
| LE-120101 |  | other | field | TNK-120100 | L-120101 |
| LE-190102 |  | other | field | TNK-190100 | L-190102 |
| LE-401 | level | element | field | IRRIGATION EQUALIZATION TANK (printed 'TANK'; 'EQUALIZATION TANK' in LAH-402 label) | L-401 |
| LI-001@P-101 | level | indicator | scada | Influent flow meter flume/venturi with ultrasonic sensor above it (FIT 100.002) | L-001@P-101 |
| LI-001@P-401 | level | indicator | scada | IRRIGATION EQUALIZATION TANK (printed 'TANK'; 'EQUALIZATION TANK' in LAH-402 label) | L-001@P-401 |
| LI-100.124A |  | other | scada |  | L-100124 |
| LI-100.124B |  | other | scada |  | L-100124 |
| LI-401 | level | indicator | dcs |  | L-401 |
| LI-402 | level | indicator | local_panel | IRRIGATION EQUALIZATION TANK (printed 'TANK'; 'EQUALIZATION TANK' in LAH-402 label) | L-402 |
| LI-600,201B |  | other | plc |  | L-600201B |
| LIR-040101 |  | other | scada |  | L-040101 |
| LIR-190102 |  | other | scada |  | L-190102 |
| LIT-100.114A |  | other | field | Screening channel (HWWL) with fine screen, inside VENDOR PACKAGE | L-100114 |
| LIT-100.114B |  | other | field | Screening channel (HWWL) with fine screen, inside VENDOR PACKAGE | L-100114 |
| LIT-600,201A |  | other | field | T-600,201 | L-600201A |
| LIT-600,204C |  | other | field | T-600,204 | L-600204C |
| LSH (untagged) | level | switch | field | Manual bar rack channel (HWWL, inclined rack symbol) |  |
| LSH-040103 |  | other | field | TNK-040100 | L-040103 |
| LSH-070102 |  | other | field | TNK-070100 | L-070102 |
| LSH-100.115 |  | other | field | Screening channel (HWWL) with fine screen, inside VENDOR PACKAGE | L-100115 |
| LSH-120103 |  | other | field | TNK-120100 | L-120103 |
| LSH-402 | level | switch | field | IRRIGATION EQUALIZATION TANK (printed 'TANK'; 'EQUALIZATION TANK' in LAH-402 label) | L-402 |
| LSH-600,201B |  | other | field | T-600,201 | L-600201B |
| LSH-600,201D |  | other | field | T-600,201 | L-600201D |
| LSH-600,204A |  | other | field | T-600,204 | L-600204A |
| LSH-600,204D |  | other | field | T-600,204 | L-600204D |
| LSL-040102 |  | other | field | TNK-040100 | L-040102 |
| LSL-070101 |  | other | field | TNK-070100 | L-070101 |
| LSL-120102 |  | other | field | TNK-120100 | L-120102 |
| LSL-600,201C |  | other | field | T-600,201 | L-600201C |
| LSL-600,204B |  | other | field | T-600,204 | L-600204B |
| LT-040101 |  | other | field | TNK-040100 | L-040101 |
| LT-120101 |  | other | field |  | L-120101 |
| LT-190102 |  | other | field | TNK-190100 | L-190102 |
| MAH-040111 |  | other | scada |  | M-040111 |
| MAH-040121 |  | other | scada |  | M-040121 |
| MAH-190111 |  | other | scada |  | M-190111 |
| ME-040111 |  | other | field | MXR-040111 |  |
| ME-040121 |  | other | field | Recycle pump (tag not printed, typical for 2 pumps, left) |  |
| ME-040122 |  | other | field | Recycle pump (tag not printed, typical for 2 pumps, right) |  |
| ME-120111 |  | other | field | PMP-120111 | M-120111 |
| ME-120112 |  | other | field | PMP-120112 | M-120112 |
| ME-190111 |  | other | field | MXR-190111 | M-190111 |
| MS-040111 |  | other | plc |  | M-040111 |
| MS-040121 |  | other | plc |  | M-040121 |
| MS-190111 |  | other | local_panel |  | M-190111 |
| MY-040111 |  | other | plc |  | M-040111 |
| MY-040121 |  | other | plc |  | M-040121 |
| MY-190111 |  | other | local_panel |  | M-190111 |
| PAH-080121 |  | other | scada |  | P-080121 |
| PG-080101A |  | other | field | line (butterfly valve -> expansion joint) | P-080101 |
| PG-080101B |  | other | field | line (expansion joint -> check valve) | P-080101 |
| PG-170111 |  | other | field | line (XV-170103 -> Chemical injector/eductor symbol on utility water line (acid injection point)) |  |
| PG-170112 |  | other | field | line (Chemical injector/eductor symbol on utility water line (acid injection point) -> check valve) |  |
| PI-600,203A |  | other | field | 1"-FOS (check valve -> P-600,203) |  |
| PI-600,203B |  | other | field | 1"-FOS (inline valve symbol with stem tick (type uncertain) -> diamond/bow-tie symbol (unlabelled, type uncertain)) |  |
| PI-600,205 |  | other | local_panel |  |  |
| PI-600,205A |  | other | field | 1"-FOS (check valve -> P-600,205) |  |
| PI-600,205B |  | other | field | 1"-FOR (inline valve symbol with stem tick (type uncertain) -> manual valve) |  |
| PIR-080121 |  | other | scada |  | P-080121 |
| PT-080121 |  | other | field | line (UPPER PERMEATE FROM MB-01 REF SHT P203 -> check valve) | P-080121 |
| SC-090101 |  | other | field |  | S-090101 |
| SC-100101 |  | other | field |  | S-100101 |
| SC-110101 |  | other | local_panel |  | S-110101 |
| SC-110111 |  | other | local_panel |  | S-110111 |
| SS-040121 |  | other | mcc |  | S-040121 |
| TAH-040111 |  | other | scada |  | T-040111 |
| TAH-040121 |  | other | scada |  | T-040121 |
| TAH-190111 |  | other | scada |  | T-190111 |
| TAL-050102 |  | other | scada |  | T-050102 |
| TIR-050102 |  | other | scada |  | T-050102 |
| TIT-050102 |  | other | field |  | T-050102 |
| TSH-040111 |  | other | field | MXR-040111 |  |
| TSH-040121 |  | other | field | Recycle pump (tag not printed, typical for 2 pumps, left) |  |
| TSH-040122 |  | other | field | Recycle pump (tag not printed, typical for 2 pumps, right) |  |
| TSH-120111 |  | other | field | PMP-120111 | T-120111 |
| TSH-120112 |  | other | field | PMP-120112 | T-120112 |
| TSH-190111 |  | other | field | MXR-190111 | T-190111 |
| TSH-190301 |  | other | field | WAS pump (tag printed as 'PMP-' only, number missing); motor M drawn at drive end | T-190301 |
| TY-040111 |  | other | mcc |  | T-040111 |
| TY-040121 |  | other | mcc |  | T-040121 |
| TY-190111 |  | other | local_panel |  | T-190111 |
| UA-120100 |  | other | scada |  |  |
| VFD-040121 |  | other | mcc |  | F-040121 |
| XC-080111 |  | other | scada |  | X-080111 |
| XC-080112 |  | other | scada |  | X-080112 |
| XC-090101A |  | other | field |  | X-090101 |
| XC-090101B |  | other | field |  | X-090101 |
| XC-090101C |  | other | field |  | X-090101 |
| XC-100101A |  | other | field |  | X-100101 |
| XC-100101B |  | other | field |  | X-100101 |
| XC-100101C |  | other | field |  | X-100101 |
| XC-110101A |  | other | local_panel |  | X-110101 |
| XC-110101B |  | other | local_panel |  | X-110101 |
| XC-110101C |  | other | local_panel |  | X-110101 |
| XC-110111A |  | other | local_panel |  | X-110111 |
| XC-110111B |  | other | local_panel |  | X-110111 |
| XC-110111C |  | other | local_panel |  | X-110111 |
| YA-001@P-101 | event/state | alarm | scada |  | L-001@P-101 |
| YA-001@P-401 | event/state | alarm | scada |  | L-001@P-401 |
| YA-007 | event/state | alarm | scada |  |  |
| YA-090101A |  | other | field | BLR-090101 | Y-090101 |
| YA-090101B |  | other | field | BLR-090101 | Y-090101 |
| YA-100101A |  | other | field | BLR-100101 | Y-100101 |
| YA-100101B |  | other | field | BLR-100101 | Y-100101 |
| YA-110101A |  | other | local_panel |  | Y-110101 |
| YA-110101B |  | other | local_panel |  | Y-110101 |
| YA-110111A |  | other | local_panel |  | Y-110111 |
| YA-110111B |  | other | local_panel |  | Y-110111 |
| YA-500,101 |  | other | plc |  | Y-500101 |
| YA-600,009C |  | other | plc |  | Y-600009C |
| YA-600,201D |  | other | plc |  |  |
| YA-600,203 |  | other | plc |  |  |
| YA-600,204A |  | other | plc |  | Y-600204A |
| YA-600,204E |  | other | plc |  |  |
| YA-600,205 |  | other | plc |  |  |
| YC-040111 |  | other | scada |  | Y-040111 |
| YC-040121 |  | other | scada |  | Y-040121 |
| YC-070181 |  | other | scada |  | Y-070181 |
| YC-080101 |  | other | scada |  | Y-080101 |
| YC-160101 |  | other | scada |  | Y-160101 |
| YC-170103 |  | other | scada |  | Y-170103 |
| YC-190111 |  | other | scada |  | Y-190111 |
| YI (untagged) | event/state | indicator | scada |  |  |
| YI (untagged) | event/state | indicator | scada |  |  |
| YI-040111A |  | other | scada |  | Y-040111 |
| YI-040111B |  | other | scada |  | Y-040111 |
| YI-040121A |  | other | scada |  | Y-040121 |
| YI-040121B |  | other | scada |  | Y-040121 |
| YI-070181 |  | other | scada |  | Y-070181 |
| YI-080101A |  | other | scada |  | Y-080101 |
| YI-080101B |  | other | scada |  | Y-080101 |
| YI-080111 |  | other | scada |  | Y-080111 |
| YI-080112 |  | other | scada |  | Y-080112 |
| YI-090101A |  | other | field | BLR-090101 | Y-090101 |
| YI-090101B |  | other | field | BLR-090101 | Y-090101 |
| YI-090101C |  | other | field | BLR-090101 | Y-090101 |
| YI-090101D |  | other | field | BLR-090101 | Y-090101 |
| YI-100101A |  | other | field | BLR-100101 | Y-100101 |
| YI-100101B |  | other | field | BLR-100101 | Y-100101 |
| YI-100101C |  | other | field | BLR-100101 | Y-100101 |
| YI-100101D |  | other | field | BLR-100101 | Y-100101 |
| YI-110101A |  | other | local_panel |  | Y-110101 |
| YI-110101B |  | other | local_panel |  | Y-110101 |
| YI-110101C |  | other | local_panel |  | Y-110101 |
| YI-110101D |  | other | local_panel |  | Y-110101 |
| YI-110111A |  | other | local_panel |  | Y-110111 |
| YI-110111B |  | other | local_panel |  | Y-110111 |
| YI-110111C |  | other | local_panel |  | Y-110111 |
| YI-110111D |  | other | local_panel |  | Y-110111 |
| YI-170103 |  | other | scada |  | Y-170103 |
| YI-190111A |  | other | scada |  | Y-190111 |
| YI-190111B |  | other | scada |  | Y-190111 |
| YI-500,101 |  | other | plc |  | Y-500101 |
| YI-600,009C |  | other | plc |  | Y-600009C |
| YI-600,201E |  | other | field |  |  |
| YI-600,204A |  | other | plc |  | Y-600204A |
| YI-600,204B |  | other | plc |  |  |
| ZA-040101 |  | other | scada |  |  |
| ZA-040121 |  | other | scada |  |  |
| ZA-070181 |  | other | scada |  | Z-070181 |
| ZA-080101 |  | other | scada |  |  |
| ZA-080132 |  | other | scada |  | Z-080132 |
| ZA-170103 |  | other | scada |  | Z-170103 |
| ZA-190111 |  | other | scada |  |  |
| ZCC-500,101 |  | other | plc |  | Z-500101 |
| ZCO-500,101 |  | other | plc |  | Z-500101 |
| ZIC-070181 |  | other | scada |  | Z-070181 |
| ZIC-080132 |  | other | scada |  | Z-080132 |
| ZIC-170103 |  | other | scada |  | Z-170103 |
| ZIC-500,101 |  | other | plc |  | Z-500101 |
| ZIO-070181 |  | other | scada |  | Z-070181 |
| ZIO-170103 |  | other | scada |  | Z-170103 |
| ZIO-500,101 |  | other | plc |  | Z-500101 |
| ZSC-070181 |  | other | field | XV-070181 | Z-070181 |
| ZSC-080132 |  | other | field | FCV-080132 | Z-080132 |
| ZSC-170103 |  | other | field | XV-170103 | Z-170103 |
| ZSC-500,101 |  | other | field | motor operated valve | Z-500101 |
| ZSC-500,201 |  | other | field | motor operated valve | Z-500201 |
| ZSC-500,201#2 |  | other | field | motor operated valve | Z-500201#2 |
| ZSC-500,301 |  | other | field | motor operated valve | Z-500301 |
| ZSO-070181 |  | other | field | XV-070181 | Z-070181 |
| ZSO-170103 |  | other | field | XV-170103 | Z-170103 |
| ZSO-500,101 |  | other | field | motor operated valve | Z-500101 |
| ZSO-500,201 |  | other | field | motor operated valve | Z-500201 |
| ZSO-500,201#2 |  | other | field | motor operated valve | Z-500201#2 |
| ZSO-500,301 |  | other | field | motor operated valve | Z-500301 |

## Control loops

| Loop | Type | Sensor(s) | Controller(s) | Final element(s) | Description |
|---|---|---|---|---|---|
| A-050101 | monitoring |  |  |  | Monitoring loop A-050101 (analysis). |
| A-050102 | monitoring |  |  |  | Monitoring loop A-050102 (analysis). |
| A-080001 | monitoring |  |  |  | Monitoring loop A-080001 (analysis). |
| F-040121 | on_off |  |  | Recycle pump (tag not printed, typical for 2 pumps, left) | On off loop F-040121 (flow). Acts on Recycle pump (tag not printed, typical for 2 pumps, left). |
| F-040141 | monitoring |  |  |  | Monitoring loop F-040141 (flow). |
| F-070186 | monitoring |  |  |  | Monitoring loop F-070186 (flow). |
| F-080132 | on_off |  |  | FCV-080132 | On off loop F-080132 (flow). Acts on FCV-080132. |
| F-080141 | monitoring |  |  |  | Monitoring loop F-080141 (flow). |
| F-100002 | monitoring |  |  |  | Monitoring loop F-100002 (flow). |
| F-170122 | monitoring |  |  |  | Monitoring loop F-170122 (flow). |
| F-403 | monitoring | FE-403, FIT-403 |  |  | Monitoring loop F-403 (flow). Sensed by FE-403, FIT-403 (in-line on line (IRRIGATION EQUALIZATION TANK (printed 'TANK'; 'EQUALIZATION TANK' in LAH-402 label) -> TO EFFLUENT DISPOSAL REF SHT P-501)). |
| H-070181 | on_off |  |  | XV-070181 | On off loop H-070181 (hand). Acts on XV-070181. |
| H-080101 | on_off |  |  | PMP-080101 | On off loop H-080101 (hand). Acts on PMP-080101. |
| H-080111 | on_off |  |  | XV-080111 | On off loop H-080111 (hand). Acts on XV-080111. |
| H-080112 | on_off |  |  | XV-080112 | On off loop H-080112 (hand). Acts on XV-080112. |
| H-170103 | on_off |  |  | XV-170103 | On off loop H-170103 (hand). Acts on XV-170103. |
| H-190111 | on_off |  |  | MXR-190111 | On off loop H-190111 (hand). Acts on MXR-190111. |
| H-500101 | on_off |  |  | motor operated valve | On off loop H-500101 (hand). Acts on motor operated valve. |
| H-600201F | on_off |  |  | VCP-600,201 | On off loop H-600201F (hand). Acts on VCP-600,201. |
| J-040111 | on_off |  |  | MXR-040111 | On off loop J-040111 (power). Acts on MXR-040111. |
| J-080101 | on_off |  |  | PMP-080101 | On off loop J-080101 (power). Acts on PMP-080101. |
| L-001@P-101 | control |  | LCH-001@P-101, LCL-001@P-101 |  | Control loop L-001@P-101 (level). Controlled by LCH-001@P-101, LCL-001@P-101 (scada). |
| L-001@P-401 | control |  | LCH-001@P-401, LCL-001@P-401 |  | Control loop L-001@P-401 (level). Controlled by LCH-001@P-401, LCL-001@P-401 (scada). |
| L-001@P-401#2 | control |  | LCH-001@P-401#2, LCL-001@P-401#2 |  | Control loop L-001@P-401#2 (level). Controlled by LCH-001@P-401#2, LCL-001@P-401#2 (scada). |
| L-001@P-401#3 | control |  | LCL-001@P-401#3 |  | Control loop L-001@P-401#3 (level). Controlled by LCL-001@P-401#3 (scada). |
| L-040101 | monitoring |  |  |  | Monitoring loop L-040101 (level). |
| L-040102 | monitoring |  |  |  | Monitoring loop L-040102 (level). |
| L-040103 | monitoring |  |  |  | Monitoring loop L-040103 (level). |
| L-070101 | monitoring |  |  |  | Monitoring loop L-070101 (level). |
| L-070102 | monitoring |  |  |  | Monitoring loop L-070102 (level). |
| L-100114 | on_off |  |  | VCP-100 | On off loop L-100114 (level). Acts on VCP-100. |
| L-100115 | on_off |  |  | VCP-100 | On off loop L-100115 (level). Acts on VCP-100. |
| L-100124 | monitoring |  |  |  | Monitoring loop L-100124 (level). |
| L-120101 | on_off |  |  | PNL-120100 | On off loop L-120101 (level). Acts on PNL-120100. |
| L-120102 | on_off |  |  | PNL-120100 | On off loop L-120102 (level). Acts on PNL-120100. |
| L-120103 | on_off |  |  | PNL-120100 | On off loop L-120103 (level). Acts on PNL-120100. |
| L-190102 | monitoring |  |  |  | Monitoring loop L-190102 (level). |
| L-401 | monitoring | LE-401 |  |  | Monitoring loop L-401 (level). Sensed by LE-401 (IRRIGATION EQUALIZATION TANK (printed 'TANK'; 'EQUALIZATION TANK' in LAH-402 label)). |
| L-402 | monitoring | LI-402, LSH-402 |  |  | Monitoring loop L-402 (level). Sensed by LI-402, LSH-402 (IRRIGATION EQUALIZATION TANK (printed 'TANK'; 'EQUALIZATION TANK' in LAH-402 label)). |
| L-600201A | on_off |  |  | VCP-600,201 | On off loop L-600201A (level). Acts on VCP-600,201. |
| L-600201B | on_off |  |  | VCP-600,201 | On off loop L-600201B (level). Acts on VCP-600,201. |
| L-600201C | on_off |  |  | VCP-600,201 | On off loop L-600201C (level). Acts on VCP-600,201. |
| L-600201D | on_off |  |  | VCP-600,201 | On off loop L-600201D (level). Acts on VCP-600,201. |
| L-600204A | on_off |  |  | VCP-600,206 | On off loop L-600204A (level). Acts on VCP-600,206. |
| L-600204B | on_off |  |  | VCP-600,206 | On off loop L-600204B (level). Acts on VCP-600,206. |
| L-600204C | on_off |  |  | VCP-600,206 | On off loop L-600204C (level). Acts on VCP-600,206. |
| L-600204D | on_off |  |  | VCP-600,206 | On off loop L-600204D (level). Acts on VCP-600,206. |
| M-040111 | monitoring |  |  |  | Monitoring loop M-040111 (moisture). |
| M-040121 | monitoring |  |  |  | Monitoring loop M-040121 (moisture). |
| M-120111 | on_off |  |  | PNL-120100 | On off loop M-120111 (moisture). Acts on PNL-120100. |
| M-120112 | on_off |  |  | PNL-120100 | On off loop M-120112 (moisture). Acts on PNL-120100. |
| M-190111 | monitoring |  |  |  | Monitoring loop M-190111 (moisture). |
| P-080101 | monitoring |  |  |  | Monitoring loop P-080101 (pressure). |
| P-080121 | monitoring |  |  |  | Monitoring loop P-080121 (pressure). |
| S-040121 | on_off |  |  | Recycle pump (tag not printed, typical for 2 pumps, left) | On off loop S-040121 (speed/frequency). Acts on Recycle pump (tag not printed, typical for 2 pumps, left). |
| S-090101 | on_off |  |  | VFD-090101 | On off loop S-090101 (speed/frequency). Acts on VFD-090101. |
| S-100101 | on_off |  |  | VFD-100101 | On off loop S-100101 (speed/frequency). Acts on VFD-100101. |
| S-110101 | on_off |  |  | VFD-110101 | On off loop S-110101 (speed/frequency). Acts on VFD-110101. |
| S-110111 | on_off |  |  | VFD-110111 | On off loop S-110111 (speed/frequency). Acts on VFD-110111. |
| T-040111 | monitoring |  |  |  | Monitoring loop T-040111 (temperature). |
| T-040121 | monitoring |  |  |  | Monitoring loop T-040121 (temperature). |
| T-050102 | monitoring |  |  |  | Monitoring loop T-050102 (temperature). |
| T-120111 | on_off |  |  | PNL-120100 | On off loop T-120111 (temperature). Acts on PNL-120100. |
| T-120112 | on_off |  |  | PNL-120100 | On off loop T-120112 (temperature). Acts on PNL-120100. |
| T-190111 | interlock |  |  | MXR-190111 | Interlock loop T-190111 (temperature). Acts on MXR-190111. |
| T-190301 | interlock |  |  | WAS pump (tag printed as 'PMP-' only, number missing); motor M drawn at drive end | Interlock loop T-190301 (temperature). Acts on WAS pump (tag printed as 'PMP-' only, number missing); motor M drawn at drive end. |
| X-080111 | on_off |  |  | XV-080111 | On off loop X-080111 (unclassified). Acts on XV-080111. |
| X-080112 | on_off |  |  | XV-080112 | On off loop X-080112 (unclassified). Acts on XV-080112. |
| X-090101 | on_off |  |  | BLR-090101 | On off loop X-090101 (unclassified). Acts on BLR-090101. |
| X-100101 | on_off |  |  | BLR-100101 | On off loop X-100101 (unclassified). Acts on BLR-100101. |
| X-110101 | on_off |  |  | BLR-110101 | On off loop X-110101 (unclassified). Acts on BLR-110101. |
| X-110111 | on_off |  |  | BLR-110111 | On off loop X-110111 (unclassified). Acts on BLR-110111. |
| Y-040111 | monitoring |  |  |  | Monitoring loop Y-040111 (event/state). |
| Y-040121 | monitoring |  |  |  | Monitoring loop Y-040121 (event/state). |
| Y-070181 | on_off |  |  | XV-070181 | On off loop Y-070181 (event/state). Acts on XV-070181. |
| Y-080101 | on_off |  |  | PMP-080101 | On off loop Y-080101 (event/state). Acts on PMP-080101. |
| Y-080111 | monitoring |  |  |  | Monitoring loop Y-080111 (event/state). |
| Y-080112 | monitoring |  |  |  | Monitoring loop Y-080112 (event/state). |
| Y-090101 | monitoring |  |  |  | Monitoring loop Y-090101 (event/state). |
| Y-100101 | monitoring |  |  |  | Monitoring loop Y-100101 (event/state). |
| Y-110101 | monitoring |  |  |  | Monitoring loop Y-110101 (event/state). |
| Y-110111 | monitoring |  |  |  | Monitoring loop Y-110111 (event/state). |
| Y-160101 | on_off |  |  | PMP-160101 | On off loop Y-160101 (event/state). Acts on PMP-160101. |
| Y-170103 | on_off |  |  | XV-170103 | On off loop Y-170103 (event/state). Acts on XV-170103. |
| Y-190111 | on_off |  |  | MXR-190111 | On off loop Y-190111 (event/state). Acts on MXR-190111. |
| Y-500101 | on_off |  |  | motor operated valve | On off loop Y-500101 (event/state). Acts on motor operated valve. |
| Y-600009C | monitoring |  |  |  | Monitoring loop Y-600009C (event/state). |
| Y-600204A | monitoring |  |  |  | Monitoring loop Y-600204A (event/state). |
| Z-070181 | monitoring |  |  |  | Monitoring loop Z-070181 (position). |
| Z-080132 | monitoring |  |  |  | Monitoring loop Z-080132 (position). |
| Z-170103 | monitoring |  |  |  | Monitoring loop Z-170103 (position). |
| Z-500101 | on_off |  |  | motor operated valve | On off loop Z-500101 (position). Acts on motor operated valve. |
| Z-500201 | monitoring |  |  |  | Monitoring loop Z-500201 (position). |
| Z-500201#2 | monitoring |  |  |  | Monitoring loop Z-500201#2 (position). |
| Z-500301 | monitoring |  |  |  | Monitoring loop Z-500301 (position). |

## Off-page connections

| Sheet | Connector | Direction | Other drawing | Linked to |
|---|---|---|---|---|
| P-101 | TO MBR | out |  | SCREENED INFLT FROM HEADWORKS (P-201) |
| P-201 | EQUIPMENT CAL PS INFLUENT | in | P208 | EQUIP. GALLERY PS TO AX-01 (P-208) |
| P-201 | SCREENED INFLT FROM HEADWORKS | in | P101 | TO MBR (P-101) |
| P-201 | pH ADJUSTMENT | in | P207 | pH ADJUSTMENT TO AX-01 (P-207) |
| P-201 | RECYCLE TO PA-01 | out | P202 | RECYCLE FROM AX-01 REF SHT P201 (P-202) |
| P-202 | PROCESS AIR FROM BLOWERS REF SHT P205 | in | P205 | PROCESS AIR TO PA-01 (P-205) |
| P-202 | RECYCLE FROM AX-01 REF SHT P201 | in | P201 | RECYCLE TO PA-01 (P-201) |
| P-202 | OVERFLOW TO MBR BASIN REF SHT P203 | out | P203 | OVERFLOW FROM PRE-AERATION BASIN REF SHT P202 (P-203) |
| P-203 | OVERFLOW FROM PRE-AERATION BASIN REF SHT P202 | in | P202 | OVERFLOW TO MBR BASIN REF SHT P203 (P-202) |
| P-203 | ACID WASH REF SHT P206 | in | P206 | ACID WASH TO MB-01 (P-206) |
| P-203 | PROCESS AIR FROM BLOWERS REF SHT P205 | in | P205 | PROCESS AIR TO MB-01 (P-205) |
| P-203 | UPPER PERMEATE TO COLLECTION REF SHT P204 | out | P204 | UPPER PERMEATE FROM MB-01 REF SHT P203 (P-204) |
| P-203 | LOWER PERMEATE TO COLLECTION REF SHT P204 | out | P204 | LOWER PERMEATE FROM MB-01 REF SHT P203 (P-204) |
| P-203 | WAS TO WAS-01 REF SHT P210 | out | P210 | WAS FROM MB-01 REF SHT P203 (P-210) |
| P-204 | UPPER PERMEATE FROM MB-01 REF SHT P203 | in | P203 | UPPER PERMEATE TO COLLECTION REF SHT P204 (P-203) |
| P-204 | LOWER PERMEATE FROM MB-01 REF SHT P203 | in | P203 | LOWER PERMEATE TO COLLECTION REF SHT P204 (P-203) |
| P-204 | PERMEATE TO DISINFECTION | out |  | FROM PERMEATE COLLECTION REF SHT P-204 (P-401) |
| P-205 | PROCESS AIR FROM STD-BY BLR. | in | P-209 | PROCESS AIR TO PA&MB BLRs REF SHT P205 (P-209) |
| P-205 | PROCESS AIR TO MB-01 | out | P-203 | PROCESS AIR FROM BLOWERS REF SHT P205 (P-203) |
| P-205 | PROCESS AIR TO PA-01 | out | P-202 | PROCESS AIR FROM BLOWERS REF SHT P205 (P-202) |
| P-206 | ACID WASH TO MB-01 | out | P203 | ACID WASH REF SHT P206 (P-203) |
| P-207 | pH ADJUSTMENT TO AX-01 | out | P201 | pH ADJUSTMENT (P-201) |
| P-208 | EQUIP. GALLERY PS TO AX-01 | out | P201 | EQUIPMENT CAL PS INFLUENT (P-201) |
| P-209 | PROCESS AIR WAS-01 REF SHT P210 | out | P210 | PROCESS AIR FROM BLOWERS REF SHT P205 (P-210) |
| P-209 | PROCESS AIR TO PA&MB BLRs REF SHT P205 | out | P205 | PROCESS AIR FROM STD-BY BLR. (P-205) |
| P-210 | PROCESS AIR FROM BLOWERS REF SHT P205 | in | P209 | PROCESS AIR WAS-01 REF SHT P210 (P-209) |
| P-210 | WAS TO WAS PUMPS REF SHT P211 | out | P211 | WAS FROM WAS-01 REF SHT P210 (P-211) |
| P-210 | WAS FROM MB-01 REF SHT P203 | in | P203 | WAS TO WAS-01 REF SHT P210 (P-203) |
| P-211 | WAS FROM WAS-01 REF SHT P210 | in | P210 | WAS TO WAS PUMPS REF SHT P211 (P-210) |
| P-401 | FROM PERMEATE COLLECTION REF SHT P-204 | in | P-204 | PERMEATE TO DISINFECTION (P-204) |
| P-401 | TO EFFLUENT DISPOSAL REF SHT P-501 | out | P-501 | FROM IRRIGATION EQUALIZATION TANK (P-501) |
| P-501 | FROM IRRIGATION EQUALIZATION TANK | in | P-401 | TO EFFLUENT DISPOSAL REF SHT P-501 (P-401) |
| P-601 | FOR DAY TANK | in | P-602 | FOR BULK FUEL STORAGE TANK (P-602) |
| P-601 | FOS A DAY TANK | out | P-602 | FOS BULK FUEL STORAGE TANK (P-602) |
| P-601 | HIGH LEVEL LOW LEVEL DAY TANK PANEL | out | P-602 | HIGH LEVEL LOW LEVEL BULK TANK PANEL (P-602) |
| P-602 | FOR GENERATOR | in | P-603 | FOR DAY TANK (P-603) |
| P-602 | FOS BULK FUEL STORAGE TANK | in | P-601 | FOS A DAY TANK (P-601) |
| P-602 | FOS GENERATOR | out | P-603 | FOS DAY TANK (P-603) |
| P-602 | FOR BULK FUEL STORAGE TANK | out | P-601 | FOR DAY TANK (P-601) |
| P-602 | HIGH LEVEL LOW LEVEL BULK TANK PANEL | in | P-601 | HIGH LEVEL LOW LEVEL DAY TANK PANEL (P-601) |
| P-602 | LOW LEVEL GEN CONTROL PANEL | out | P-603 | LOW LEVEL C DAY TANK CONTROL PANEL (P-603) |
| P-603 | FOS DAY TANK | in | P-602 | FOS GENERATOR (P-602) |
| P-603 | FOR DAY TANK | out | P-602 | FOR GENERATOR (P-602) |
| P-603 | LOW LEVEL C DAY TANK CONTROL PANEL | in | P-602 | LOW LEVEL GEN CONTROL PANEL (P-602) |

## Data quality

0 errors, 10 warnings and 352 informational items; see `qa_report.md`. Every node carries `confidence` and the sheet region it was read from (`provenance`). This graph was machine-extracted from drawings and must be verified by a qualified engineer before use in design, operations or safety work.
