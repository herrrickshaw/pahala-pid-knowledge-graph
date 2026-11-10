# QA report: Pahala WWTP

Generated 2026-11-10T23:55:00+00:00 by pid-to-kg 0.1.0.

**0 errors, 10 warnings, 352 info.**

Errors must be fixed in the page extraction files before the graph is trusted. Warnings are things to re-check on the drawing (the *Re-check* column names the tiles). Info items are for the record.

| Severity | Code | Count |
|---|---|---|
| warning | `component_not_connected` | 1 |
| warning | `duplicate_tag` | 5 |
| warning | `loop_no_final_element` | 4 |
| info | `inferred_flow_direction` | 1 |
| info | `isolated_instrument` | 2 |
| info | `loop_no_sensor` | 4 |
| info | `low_confidence` | 92 |
| info | `non_isa_tag` | 241 |
| info | `tag_reused` | 12 |

## Details

| Severity | Page | Code | Item | Message | Re-check |
|---|---|---|---|---|---|
| warning |  | `loop_no_final_element` | LOOP:L-001@P-101 | control loop L-001@P-101 has a controller but no final element |  |
| warning |  | `loop_no_final_element` | LOOP:L-001@P-401 | control loop L-001@P-401 has a controller but no final element |  |
| warning |  | `loop_no_final_element` | LOOP:L-001@P-401#2 | control loop L-001@P-401#2 has a controller but no final element |  |
| warning |  | `loop_no_final_element` | LOOP:L-001@P-401#3 | control loop L-001@P-401#3 has a controller but no final element |  |
| warning | 21 | `duplicate_tag` | LCH-001@P-401#2 | tag 'LCH-001@P-401' is used by more than one item on this sheet; the copy 'LCH-001-LEAD' was kept separate as 'LCH-001@P-401#2' | r1c2 |
| warning | 21 | `duplicate_tag` | LCL-001@P-401#2 | tag 'LCL-001@P-401' is used by more than one item on this sheet; the copy 'LCL-001-LAG' was kept separate as 'LCL-001@P-401#2' | r1c2 |
| warning | 21 | `duplicate_tag` | LCL-001@P-401#3 | tag 'LCL-001@P-401' is used by more than one item on this sheet; the copy 'LCL-001-STOP' was kept separate as 'LCL-001@P-401#3' | r1c2 |
| warning | 22 | `duplicate_tag` | ZSO-500,201#2 | tag 'ZSO-500,201' is used by more than one item on this sheet; the copy 'ZSO-Z4' was kept separate as 'ZSO-500,201#2' | r3c2, r3c3 |
| warning | 22 | `duplicate_tag` | ZSC-500,201#2 | tag 'ZSC-500,201' is used by more than one item on this sheet; the copy 'ZSC-Z4' was kept separate as 'ZSC-500,201#2' | r3c2, r3c3 |
| warning | 23 | `component_not_connected` | P23.OV1 | component overfill prevention valve with float on tank top is not on any line (add it to a line 'path') | r2c2, r2c3 |
| info |  | `inferred_flow_direction` |  | 164 flow edges have inferred (not drawn) direction |  |
| info |  | `loop_no_sensor` | LOOP:L-001@P-101 | control loop L-001@P-101 has a controller but no sensor |  |
| info |  | `loop_no_sensor` | LOOP:L-001@P-401 | control loop L-001@P-401 has a controller but no sensor |  |
| info |  | `loop_no_sensor` | LOOP:L-001@P-401#2 | control loop L-001@P-401#2 has a controller but no sensor |  |
| info |  | `loop_no_sensor` | LOOP:L-001@P-401#3 | control loop L-001@P-401#3 has a controller but no sensor |  |
| info | 9 | `non_isa_tag` | FIT-100.002 | instrument tag 'FIT-100.002' does not parse as ISA-5.1 | r2c1 |
| info | 9 | `non_isa_tag` | FI-100.002 | instrument tag 'FI-100.002' does not parse as ISA-5.1 | r1c1 |
| info | 9 | `non_isa_tag` | LI-100.124A | instrument tag 'LI-100.124A' does not parse as ISA-5.1 | r1c2 |
| info | 9 | `non_isa_tag` | LI-100.124B | instrument tag 'LI-100.124B' does not parse as ISA-5.1 | r1c2, r1c3 |
| info | 9 | `non_isa_tag` | LDI-100.124 | instrument tag 'LDI-100.124' does not parse as ISA-5.1 | r1c2, r1c3 |
| info | 9 | `non_isa_tag` | LAH-100.125 | instrument tag 'LAH-100.125' does not parse as ISA-5.1 | r1c2 |
| info | 9 | `non_isa_tag` | LDAH-100.124 | instrument tag 'LDAH-100.124' does not parse as ISA-5.1 | r1c2 |
| info | 9 | `non_isa_tag` | LDAH-100.115 | instrument tag 'LDAH-100.115' does not parse as ISA-5.1 | r1c2 |
| info | 9 | `non_isa_tag` | LSH-100.115 | instrument tag 'LSH-100.115' does not parse as ISA-5.1 | r2c2, r3c2 |
| info | 9 | `non_isa_tag` | LIT-100.114A | instrument tag 'LIT-100.114A' does not parse as ISA-5.1 | r2c2 |
| info | 9 | `non_isa_tag` | LIT-100.114B | instrument tag 'LIT-100.114B' does not parse as ISA-5.1 | r2c2, r2c3 |
| info | 9 | `tag_reused` | LAH-001@P-101 | 'LAH-001' identifies different items on different sheets; kept as 'LAH-001@P-101' | r1c1, r1c2 |
| info | 9 | `tag_reused` | LAL-001@P-101 | 'LAL-001' identifies different items on different sheets; kept as 'LAL-001@P-101' | r1c2 |
| info | 9 | `tag_reused` | LCH-001@P-101 | 'LCH-001' identifies different items on different sheets; kept as 'LCH-001@P-101' | r1c1 |
| info | 9 | `tag_reused` | LCL-001@P-101 | 'LCL-001' identifies different items on different sheets; kept as 'LCL-001@P-101' | r1c2 |
| info | 9 | `tag_reused` | LI-001@P-101 | 'LI-001' identifies different items on different sheets; kept as 'LI-001@P-101' | r1c3 |
| info | 9 | `tag_reused` | YA-001@P-101 | 'YA-001' identifies different items on different sheets; kept as 'YA-001@P-101' | r1c2, r1c3 |
| info | 10 | `low_confidence` | P10.VB1 | check valve was read with confidence 0.50 | r2c3 |
| info | 10 | `low_confidence` | P10.LB.1 | LB [1/2] was read with confidence 0.50 |  |
| info | 10 | `low_confidence` | P10.LB.2 | LB [2/2] was read with confidence 0.50 |  |
| info | 10 | `non_isa_tag` | LE-040101 | instrument tag 'LE-040101' does not parse as ISA-5.1 | r3c3 |
| info | 10 | `non_isa_tag` | LT-040101 | instrument tag 'LT-040101' does not parse as ISA-5.1 | r2c3 |
| info | 10 | `non_isa_tag` | LSL-040102 | instrument tag 'LSL-040102' does not parse as ISA-5.1 | r2c2, r2c3 |
| info | 10 | `non_isa_tag` | LSH-040103 | instrument tag 'LSH-040103' does not parse as ISA-5.1 | r2c3 |
| info | 10 | `non_isa_tag` | TSH-040121 | instrument tag 'TSH-040121' does not parse as ISA-5.1 | r2c3 |
| info | 10 | `non_isa_tag` | ME-040121 | instrument tag 'ME-040121' does not parse as ISA-5.1 | r2c3 |
| info | 10 | `non_isa_tag` | TSH-040122 | instrument tag 'TSH-040122' does not parse as ISA-5.1 | r2c3, r2c4 |
| info | 10 | `non_isa_tag` | ME-040122 | instrument tag 'ME-040122' does not parse as ISA-5.1 | r2c3, r2c4 |
| info | 10 | `non_isa_tag` | TSH-040111 | instrument tag 'TSH-040111' does not parse as ISA-5.1 | r2c2 |
| info | 10 | `non_isa_tag` | ME-040111 | instrument tag 'ME-040111' does not parse as ISA-5.1 | r2c2 |
| info | 10 | `non_isa_tag` | FE-040141 | instrument tag 'FE-040141' does not parse as ISA-5.1 | r2c4 |
| info | 10 | `non_isa_tag` | FIT-040141 | instrument tag 'FIT-040141' does not parse as ISA-5.1 | r2c4 |
| info | 10 | `non_isa_tag` | FIR-040141 | instrument tag 'FIR-040141' does not parse as ISA-5.1 | r1c4 |
| info | 10 | `non_isa_tag` | FAL-040141 | instrument tag 'FAL-040141' does not parse as ISA-5.1 | r1c4 |
| info | 10 | `non_isa_tag` | LIR-040101 | instrument tag 'LIR-040101' does not parse as ISA-5.1 | r1c3 |
| info | 10 | `non_isa_tag` | LAL-040102 | instrument tag 'LAL-040102' does not parse as ISA-5.1 | r1c2, r1c3 |
| info | 10 | `non_isa_tag` | LAH-040103 | instrument tag 'LAH-040103' does not parse as ISA-5.1 | r1c3 |
| info | 10 | `non_isa_tag` | FIC-040121 | instrument tag 'FIC-040121' does not parse as ISA-5.1 | r1c3 |
| info | 10 | `non_isa_tag` | VFD-040121 | instrument tag 'VFD-040121' does not parse as ISA-5.1 | r1c3, r2c3 |
| info | 10 | `non_isa_tag` | YI-040111A | instrument tag 'YI-040111A' does not parse as ISA-5.1 | r1c2 |
| info | 10 | `non_isa_tag` | YC-040111 | instrument tag 'YC-040111' does not parse as ISA-5.1 | r1c2 |
| info | 10 | `non_isa_tag` | YI-040111B | instrument tag 'YI-040111B' does not parse as ISA-5.1 | r1c2 |
| info | 10 | `non_isa_tag` | TAH-040111 | instrument tag 'TAH-040111' does not parse as ISA-5.1 | r1c2 |
| info | 10 | `non_isa_tag` | MAH-040111 | instrument tag 'MAH-040111' does not parse as ISA-5.1 | r1c2 |
| info | 10 | `non_isa_tag` | ZA-040101 | instrument tag 'ZA-040101' does not parse as ISA-5.1 | r1c2 |
| info | 10 | `non_isa_tag` | JS-040111 | instrument tag 'JS-040111' does not parse as ISA-5.1 | r1c2, r2c2 |
| info | 10 | `non_isa_tag` | HS-040111 | instrument tag 'HS-040111' does not parse as ISA-5.1 | r1c2, r2c2 |
| info | 10 | `non_isa_tag` | TY-040111 | instrument tag 'TY-040111' does not parse as ISA-5.1 | r1c2, r2c2 |
| info | 10 | `non_isa_tag` | MY-040111 | instrument tag 'MY-040111' does not parse as ISA-5.1 | r2c2 |
| info | 10 | `non_isa_tag` | MS-040111 | instrument tag 'MS-040111' does not parse as ISA-5.1 | r2c2, r2c3 |
| info | 10 | `non_isa_tag` | LAH-040101 | instrument tag 'LAH-040101' does not parse as ISA-5.1 | r1c3 |
| info | 10 | `non_isa_tag` | LAL-040101 | instrument tag 'LAL-040101' does not parse as ISA-5.1 | r1c3 |
| info | 10 | `non_isa_tag` | YI-040121A | instrument tag 'YI-040121A' does not parse as ISA-5.1 | r1c3 |
| info | 10 | `non_isa_tag` | YC-040121 | instrument tag 'YC-040121' does not parse as ISA-5.1 | r1c3, r1c4 |
| info | 10 | `non_isa_tag` | YI-040121B | instrument tag 'YI-040121B' does not parse as ISA-5.1 | r1c3, r1c4 |
| info | 10 | `non_isa_tag` | TAH-040121 | instrument tag 'TAH-040121' does not parse as ISA-5.1 | r1c3, r1c4 |
| info | 10 | `non_isa_tag` | MAH-040121 | instrument tag 'MAH-040121' does not parse as ISA-5.1 | r1c4 |
| info | 10 | `non_isa_tag` | ZA-040121 | instrument tag 'ZA-040121' does not parse as ISA-5.1 | r1c3, r1c4 |
| info | 10 | `non_isa_tag` | SS-040121 | instrument tag 'SS-040121' does not parse as ISA-5.1 | r1c3, r2c3 |
| info | 10 | `non_isa_tag` | HS-040121 | instrument tag 'HS-040121' does not parse as ISA-5.1 | r1c3, r1c4 |
| info | 10 | `non_isa_tag` | TY-040121 | instrument tag 'TY-040121' does not parse as ISA-5.1 | r1c3, r1c4 |
| info | 10 | `non_isa_tag` | MY-040121 | instrument tag 'MY-040121' does not parse as ISA-5.1 | r2c4 |
| info | 10 | `non_isa_tag` | MS-040121 | instrument tag 'MS-040121' does not parse as ISA-5.1 | r2c4 |
| info | 11 | `low_confidence` | P11.L-DRN.1 | L-DRN was read with confidence 0.50 |  |
| info | 11 | `non_isa_tag` | AE-050101 | instrument tag 'AE-050101' does not parse as ISA-5.1 | r2c3, r3c3 |
| info | 11 | `non_isa_tag` | AIT-050101 | instrument tag 'AIT-050101' does not parse as ISA-5.1 | r2c3, r3c3 |
| info | 11 | `non_isa_tag` | AIR-050101 | instrument tag 'AIR-050101' does not parse as ISA-5.1 | r1c3 |
| info | 11 | `non_isa_tag` | AE-050102 | instrument tag 'AE-050102' does not parse as ISA-5.1 | r2c3, r3c3 |
| info | 11 | `non_isa_tag` | TIT-050102 | instrument tag 'TIT-050102' does not parse as ISA-5.1 | r2c3, r3c3 |
| info | 11 | `non_isa_tag` | AIT-050102 | instrument tag 'AIT-050102' does not parse as ISA-5.1 | r2c3, r3c3 |
| info | 11 | `non_isa_tag` | TIR-050102 | instrument tag 'TIR-050102' does not parse as ISA-5.1 | r1c3 |
| info | 11 | `non_isa_tag` | AIR-050102 | instrument tag 'AIR-050102' does not parse as ISA-5.1 | r1c3 |
| info | 11 | `non_isa_tag` | TAL-050102 | instrument tag 'TAL-050102' does not parse as ISA-5.1 | r1c3 |
| info | 11 | `non_isa_tag` | AAL-050102 | instrument tag 'AAL-050102' does not parse as ISA-5.1 | r1c3 |
| info | 12 | `low_confidence` | P12.VD1 | manual valve was read with confidence 0.50 | r2c2, r2c3 |
| info | 12 | `low_confidence` | P12.VD2 | manual valve was read with confidence 0.50 | r2c3 |
| info | 12 | `low_confidence` | P12.VD4 | manual valve was read with confidence 0.50 | r2c3, r2c4 |
| info | 12 | `low_confidence` | P12.CV-WAS | control valve was read with confidence 0.50 | r3c4 |
| info | 12 | `low_confidence` | BOUNDARY:SOURCE OF BOLD DASHED LINE AT XV-070181 NOT DRAWN | Source of bold dashed line at XV-070181 (not drawn) was read with confidence 0.40 | r2c2 |
| info | 12 | `low_confidence` | P12.L-XV.1 | L-XV [1/2] was read with confidence 0.40 |  |
| info | 12 | `low_confidence` | P12.L-XV.2 | L-XV [2/2] was read with confidence 0.40 |  |
| info | 12 | `low_confidence` | P12.L-XV1.1 | L-XV1 [1/2] was read with confidence 0.40 |  |
| info | 12 | `low_confidence` | P12.L-XV1.2 | L-XV1 [2/2] was read with confidence 0.40 |  |
| info | 12 | `low_confidence` | P12.L-XV2.1 | L-XV2 [1/2] was read with confidence 0.40 |  |
| info | 12 | `low_confidence` | P12.L-XV2.2 | L-XV2 [2/2] was read with confidence 0.40 |  |
| info | 12 | `low_confidence` | P12.L-XV3.1 | 3"-A [1/2] was read with confidence 0.35 |  |
| info | 12 | `low_confidence` | P12.L-XV3.2 | 3"-A [2/2] was read with confidence 0.35 |  |
| info | 12 | `low_confidence` | P12.L-DRN.1 | L-DRN was read with confidence 0.50 |  |
| info | 12 | `non_isa_tag` | ZSO-070181 | instrument tag 'ZSO-070181' does not parse as ISA-5.1 | r2c2 |
| info | 12 | `non_isa_tag` | ZSC-070181 | instrument tag 'ZSC-070181' does not parse as ISA-5.1 | r2c2 |
| info | 12 | `non_isa_tag` | HS-070181 | instrument tag 'HS-070181' does not parse as ISA-5.1 | r1c2 |
| info | 12 | `non_isa_tag` | ZIC-070181 | instrument tag 'ZIC-070181' does not parse as ISA-5.1 | r1c2 |
| info | 12 | `non_isa_tag` | ZIO-070181 | instrument tag 'ZIO-070181' does not parse as ISA-5.1 | r1c2 |
| info | 12 | `non_isa_tag` | YC-070181 | instrument tag 'YC-070181' does not parse as ISA-5.1 | r1c2 |
| info | 12 | `non_isa_tag` | YI-070181 | instrument tag 'YI-070181' does not parse as ISA-5.1 | r1c2, r1c3 |
| info | 12 | `non_isa_tag` | ZA-070181 | instrument tag 'ZA-070181' does not parse as ISA-5.1 | r1c2 |
| info | 12 | `non_isa_tag` | LSL-070101 | instrument tag 'LSL-070101' does not parse as ISA-5.1 | r2c3, r2c4 |
| info | 12 | `non_isa_tag` | LSH-070102 | instrument tag 'LSH-070102' does not parse as ISA-5.1 | r2c3, r2c4 |
| info | 12 | `non_isa_tag` | LAL-070101 | instrument tag 'LAL-070101' does not parse as ISA-5.1 | r1c3, r1c4 |
| info | 12 | `non_isa_tag` | LAH-070102 | instrument tag 'LAH-070102' does not parse as ISA-5.1 | r1c3, r1c4 |
| info | 12 | `non_isa_tag` | FE-070186 | instrument tag 'FE-070186' does not parse as ISA-5.1 | r3c4 |
| info | 12 | `non_isa_tag` | FIT-070186 | instrument tag 'FIT-070186' does not parse as ISA-5.1 | r2c4, r3c4 |
| info | 12 | `non_isa_tag` | FIR-070186 | instrument tag 'FIR-070186' does not parse as ISA-5.1 | r1c4 |
| info | 12 | `non_isa_tag` | FAL-070186 | instrument tag 'FAL-070186' does not parse as ISA-5.1 | r1c4 |
| info | 13 | `low_confidence` | P13.VS | Valve with solid wedge on sample/drain loop (symbol type unclear) was read with confidence 0.50 | r2c4 |
| info | 13 | `non_isa_tag` | XC-080111 | instrument tag 'XC-080111' does not parse as ISA-5.1 | r1c1 |
| info | 13 | `non_isa_tag` | HS-080111 | instrument tag 'HS-080111' does not parse as ISA-5.1 | r1c1, r1c2 |
| info | 13 | `non_isa_tag` | YI-080111 | instrument tag 'YI-080111' does not parse as ISA-5.1 | r1c1, r1c2 |
| info | 13 | `non_isa_tag` | XC-080112 | instrument tag 'XC-080112' does not parse as ISA-5.1 | r1c3 |
| info | 13 | `non_isa_tag` | HS-080112 | instrument tag 'HS-080112' does not parse as ISA-5.1 | r1c3, r1c4 |
| info | 13 | `non_isa_tag` | YI-080112 | instrument tag 'YI-080112' does not parse as ISA-5.1 | r1c3, r1c4 |
| info | 13 | `non_isa_tag` | YI-080101A | instrument tag 'YI-080101A' does not parse as ISA-5.1 | r1c2, r1c3 |
| info | 13 | `non_isa_tag` | YC-080101 | instrument tag 'YC-080101' does not parse as ISA-5.1 | r1c2, r1c3 |
| info | 13 | `non_isa_tag` | YI-080101B | instrument tag 'YI-080101B' does not parse as ISA-5.1 | r1c3 |
| info | 13 | `non_isa_tag` | ZA-080101 | instrument tag 'ZA-080101' does not parse as ISA-5.1 | r1c3 |
| info | 13 | `non_isa_tag` | HS-080101 | instrument tag 'HS-080101' does not parse as ISA-5.1 | r1c2, r1c3 |
| info | 13 | `non_isa_tag` | JS-080101 | instrument tag 'JS-080101' does not parse as ISA-5.1 | r1c3, r2c3 |
| info | 13 | `non_isa_tag` | PG-080101A | instrument tag 'PG-080101A' does not parse as ISA-5.1 | r2c2, r2c3 |
| info | 13 | `non_isa_tag` | PG-080101B | instrument tag 'PG-080101B' does not parse as ISA-5.1 | r2c3 |
| info | 13 | `non_isa_tag` | PT-080121 | instrument tag 'PT-080121' does not parse as ISA-5.1 | r2c2 |
| info | 13 | `non_isa_tag` | PIR-080121 | instrument tag 'PIR-080121' does not parse as ISA-5.1 | r1c2 |
| info | 13 | `non_isa_tag` | PAH-080121 | instrument tag 'PAH-080121' does not parse as ISA-5.1 | r1c2 |
| info | 13 | `non_isa_tag` | FIT-080141 | instrument tag 'FIT-080141' does not parse as ISA-5.1 | r2c3, r2c4 |
| info | 13 | `non_isa_tag` | FE-080141 | instrument tag 'FE-080141' does not parse as ISA-5.1 | r2c3, r2c4 |
| info | 13 | `non_isa_tag` | FQIR-080141 | instrument tag 'FQIR-080141' does not parse as ISA-5.1 | r1c3, r1c4 |
| info | 13 | `non_isa_tag` | AE-080001 | instrument tag 'AE-080001' does not parse as ISA-5.1 | r2c4 |
| info | 13 | `non_isa_tag` | AIT-080001 | instrument tag 'AIT-080001' does not parse as ISA-5.1 | r2c4 |
| info | 13 | `non_isa_tag` | AIR-080001 | instrument tag 'AIR-080001' does not parse as ISA-5.1 | r1c4 |
| info | 13 | `non_isa_tag` | AAH-080001 | instrument tag 'AAH-080001' does not parse as ISA-5.1 | r1c4 |
| info | 13 | `non_isa_tag` | ZSC-080132 | instrument tag 'ZSC-080132' does not parse as ISA-5.1 | r2c4 |
| info | 13 | `non_isa_tag` | FC-080132 | instrument tag 'FC-080132' does not parse as ISA-5.1 | r1c4 |
| info | 13 | `non_isa_tag` | ZIC-080132 | instrument tag 'ZIC-080132' does not parse as ISA-5.1 | r1c4 |
| info | 13 | `non_isa_tag` | ZA-080132 | instrument tag 'ZA-080132' does not parse as ISA-5.1 | r1c4 |
| info | 14 | `low_confidence` | P14.INL1 | Inlet filter/silencer (two hatched boxes joined by a pipe loop at blower inlet) was read with confidence 0.50 | r1c1, r2c1 |
| info | 14 | `low_confidence` | P14.INL2 | Inlet filter/silencer (two hatched boxes joined by a pipe loop at blower inlet) was read with confidence 0.50 | r2c1, r3c1 |
| info | 14 | `low_confidence` | P14.BO1 | vent was read with confidence 0.50 | r1c2, r2c2 |
| info | 14 | `low_confidence` | P14.V1 | manual valve was read with confidence 0.50 | r1c2, r2c2 |
| info | 14 | `low_confidence` | P14.BO2 | vent was read with confidence 0.50 | r2c2, r3c2 |
| info | 14 | `low_confidence` | P14.V2 | manual valve was read with confidence 0.50 | r2c2, r3c2 |
| info | 14 | `low_confidence` | P14.R1 | reducer was read with confidence 0.50 | r1c2, r2c2 |
| info | 14 | `low_confidence` | P14.R2 | reducer was read with confidence 0.50 | r2c2, r2c3 |
| info | 14 | `low_confidence` | P14.SV1 | manual valve was read with confidence 0.50 | r2c2, r2c3 |
| info | 14 | `low_confidence` | P14.SV2 | manual valve was read with confidence 0.50 | r2c2, r2c3 |
| info | 14 | `low_confidence` | P14.LIN1.1 | LIN1 was read with confidence 0.50 |  |
| info | 14 | `low_confidence` | P14.LIN2.1 | LIN2 was read with confidence 0.50 |  |
| info | 14 | `low_confidence` | P14.L5.1 | L5 was read with confidence 0.50 |  |
| info | 14 | `low_confidence` | P14.L6.1 | L6 was read with confidence 0.50 |  |
| info | 14 | `non_isa_tag` | YI-100101A | instrument tag 'YI-100101A' does not parse as ISA-5.1 | r1c1, r2c1 |
| info | 14 | `non_isa_tag` | YI-100101B | instrument tag 'YI-100101B' does not parse as ISA-5.1 | r1c1, r2c1 |
| info | 14 | `non_isa_tag` | YI-100101C | instrument tag 'YI-100101C' does not parse as ISA-5.1 | r1c1, r2c1 |
| info | 14 | `non_isa_tag` | YI-100101D | instrument tag 'YI-100101D' does not parse as ISA-5.1 | r1c1, r2c1 |
| info | 14 | `non_isa_tag` | YA-100101A | instrument tag 'YA-100101A' does not parse as ISA-5.1 | r1c1, r2c1 |
| info | 14 | `non_isa_tag` | YA-100101B | instrument tag 'YA-100101B' does not parse as ISA-5.1 | r1c1, r1c2 |
| info | 14 | `non_isa_tag` | XC-100101A | instrument tag 'XC-100101A' does not parse as ISA-5.1 | r1c1, r1c2 |
| info | 14 | `non_isa_tag` | XC-100101B | instrument tag 'XC-100101B' does not parse as ISA-5.1 | r1c2, r2c2 |
| info | 14 | `non_isa_tag` | XC-100101C | instrument tag 'XC-100101C' does not parse as ISA-5.1 | r1c2, r2c2 |
| info | 14 | `non_isa_tag` | SC-100101 | instrument tag 'SC-100101' does not parse as ISA-5.1 | r1c2, r2c2 |
| info | 14 | `non_isa_tag` | FI-100101 | instrument tag 'FI-100101' does not parse as ISA-5.1 | r1c2, r2c2 |
| info | 14 | `non_isa_tag` | YI-090101A | instrument tag 'YI-090101A' does not parse as ISA-5.1 | r2c1, r3c1 |
| info | 14 | `non_isa_tag` | YI-090101B | instrument tag 'YI-090101B' does not parse as ISA-5.1 | r2c1, r3c1 |
| info | 14 | `non_isa_tag` | YI-090101C | instrument tag 'YI-090101C' does not parse as ISA-5.1 | r2c1, r3c1 |
| info | 14 | `non_isa_tag` | YI-090101D | instrument tag 'YI-090101D' does not parse as ISA-5.1 | r2c1, r3c1 |
| info | 14 | `non_isa_tag` | YA-090101A | instrument tag 'YA-090101A' does not parse as ISA-5.1 | r2c1, r3c1 |
| info | 14 | `non_isa_tag` | YA-090101B | instrument tag 'YA-090101B' does not parse as ISA-5.1 | r2c1, r2c2 |
| info | 14 | `non_isa_tag` | XC-090101A | instrument tag 'XC-090101A' does not parse as ISA-5.1 | r2c1, r2c2 |
| info | 14 | `non_isa_tag` | XC-090101B | instrument tag 'XC-090101B' does not parse as ISA-5.1 | r2c2, r3c2 |
| info | 14 | `non_isa_tag` | XC-090101C | instrument tag 'XC-090101C' does not parse as ISA-5.1 | r2c2, r3c2 |
| info | 14 | `non_isa_tag` | SC-090101 | instrument tag 'SC-090101' does not parse as ISA-5.1 | r2c2, r3c2 |
| info | 14 | `non_isa_tag` | FI-090101 | instrument tag 'FI-090101' does not parse as ISA-5.1 | r2c2, r3c2 |
| info | 15 | `non_isa_tag` | ZSO-170103 | instrument tag 'ZSO-170103' does not parse as ISA-5.1 | r1c2, r2c2 |
| info | 15 | `non_isa_tag` | ZSC-170103 | instrument tag 'ZSC-170103' does not parse as ISA-5.1 | r1c2, r2c2 |
| info | 15 | `non_isa_tag` | PG-170111 | instrument tag 'PG-170111' does not parse as ISA-5.1 | r2c2 |
| info | 15 | `non_isa_tag` | PG-170112 | instrument tag 'PG-170112' does not parse as ISA-5.1 | r2c2 |
| info | 15 | `non_isa_tag` | FI-170121 | instrument tag 'FI-170121' does not parse as ISA-5.1 | r2c2, r3c2 |
| info | 15 | `non_isa_tag` | FE-170122 | instrument tag 'FE-170122' does not parse as ISA-5.1 | r2c3 |
| info | 15 | `non_isa_tag` | FIT-170122 | instrument tag 'FIT-170122' does not parse as ISA-5.1 | r2c3 |
| info | 15 | `non_isa_tag` | HS-170103 | instrument tag 'HS-170103' does not parse as ISA-5.1 | r1c2 |
| info | 15 | `non_isa_tag` | ZIC-170103 | instrument tag 'ZIC-170103' does not parse as ISA-5.1 | r1c2 |
| info | 15 | `non_isa_tag` | ZIO-170103 | instrument tag 'ZIO-170103' does not parse as ISA-5.1 | r1c2 |
| info | 15 | `non_isa_tag` | YC-170103 | instrument tag 'YC-170103' does not parse as ISA-5.1 | r1c2 |
| info | 15 | `non_isa_tag` | YI-170103 | instrument tag 'YI-170103' does not parse as ISA-5.1 | r1c2 |
| info | 15 | `non_isa_tag` | ZA-170103 | instrument tag 'ZA-170103' does not parse as ISA-5.1 | r1c2 |
| info | 15 | `non_isa_tag` | FQIR-170122 | instrument tag 'FQIR-170122' does not parse as ISA-5.1 | r1c3 |
| info | 16 | `non_isa_tag` | YC-160101 | instrument tag 'YC-160101' does not parse as ISA-5.1 | r1c3 |
| info | 17 | `low_confidence` | P17.DA | diamond symbol on pump A riser (coupling/union type not identified) was read with confidence 0.40 | r2c3, r3c3 |
| info | 17 | `low_confidence` | P17.DB | diamond symbol on pump B riser (coupling/union type not identified) was read with confidence 0.40 | r2c3, r3c3 |
| info | 17 | `low_confidence` | P17.HV1 | manual valve was read with confidence 0.50 | r2c3, r3c3 |
| info | 17 | `low_confidence` | P17.R1 | reducer was read with confidence 0.50 | r2c3, r3c3 |
| info | 17 | `non_isa_tag` | LSL-120102 | instrument tag 'LSL-120102' does not parse as ISA-5.1 | r2c2, r3c2 |
| info | 17 | `non_isa_tag` | LSH-120103 | instrument tag 'LSH-120103' does not parse as ISA-5.1 | r2c2, r3c2 |
| info | 17 | `non_isa_tag` | LT-120101 | instrument tag 'LT-120101' does not parse as ISA-5.1 | r2c2, r3c2 |
| info | 17 | `non_isa_tag` | LE-120101 | instrument tag 'LE-120101' does not parse as ISA-5.1 | r3c2 |
| info | 17 | `non_isa_tag` | TSH-120111 | instrument tag 'TSH-120111' does not parse as ISA-5.1 | r2c3, r3c3 |
| info | 17 | `non_isa_tag` | ME-120111 | instrument tag 'ME-120111' does not parse as ISA-5.1 | r2c3, r3c3 |
| info | 17 | `non_isa_tag` | TSH-120112 | instrument tag 'TSH-120112' does not parse as ISA-5.1 | r2c3, r3c3 |
| info | 17 | `non_isa_tag` | ME-120112 | instrument tag 'ME-120112' does not parse as ISA-5.1 | r2c3, r3c3 |
| info | 17 | `non_isa_tag` | UA-120100 | instrument tag 'UA-120100' does not parse as ISA-5.1 | r1c2 |
| info | 18 | `low_confidence` | P18.SIL1 | vent/silencer-type symbol on blower 110101 discharge (unclear) was read with confidence 0.50 | r1c2, r2c2 |
| info | 18 | `low_confidence` | P18.BV1 | butterfly valve was read with confidence 0.50 | r1c2, r2c2 |
| info | 18 | `low_confidence` | P18.SIL2 | vent/silencer-type symbol on blower 110111 discharge (unclear) was read with confidence 0.50 | r2c2 |
| info | 18 | `low_confidence` | P18.XV1 | butterfly valve was read with confidence 0.50 | r2c2, r2c3 |
| info | 18 | `non_isa_tag` | YI-110101A | instrument tag 'YI-110101A' does not parse as ISA-5.1 | r1c1, r2c1 |
| info | 18 | `non_isa_tag` | YI-110101B | instrument tag 'YI-110101B' does not parse as ISA-5.1 | r1c1, r2c1 |
| info | 18 | `non_isa_tag` | YI-110101C | instrument tag 'YI-110101C' does not parse as ISA-5.1 | r1c1, r2c1 |
| info | 18 | `non_isa_tag` | YI-110101D | instrument tag 'YI-110101D' does not parse as ISA-5.1 | r1c1, r2c1 |
| info | 18 | `non_isa_tag` | YA-110101A | instrument tag 'YA-110101A' does not parse as ISA-5.1 | r1c1, r2c1 |
| info | 18 | `non_isa_tag` | YA-110101B | instrument tag 'YA-110101B' does not parse as ISA-5.1 | r1c1, r1c2 |
| info | 18 | `non_isa_tag` | XC-110101A | instrument tag 'XC-110101A' does not parse as ISA-5.1 | r1c1, r1c2 |
| info | 18 | `non_isa_tag` | XC-110101B | instrument tag 'XC-110101B' does not parse as ISA-5.1 | r1c2, r2c2 |
| info | 18 | `non_isa_tag` | XC-110101C | instrument tag 'XC-110101C' does not parse as ISA-5.1 | r1c2, r2c2 |
| info | 18 | `non_isa_tag` | SC-110101 | instrument tag 'SC-110101' does not parse as ISA-5.1 | r1c2, r2c2 |
| info | 18 | `non_isa_tag` | FI-110101 | instrument tag 'FI-110101' does not parse as ISA-5.1 | r1c2, r2c2 |
| info | 18 | `non_isa_tag` | YI-110111A | instrument tag 'YI-110111A' does not parse as ISA-5.1 | r2c1 |
| info | 18 | `non_isa_tag` | YI-110111B | instrument tag 'YI-110111B' does not parse as ISA-5.1 | r2c1 |
| info | 18 | `non_isa_tag` | YI-110111C | instrument tag 'YI-110111C' does not parse as ISA-5.1 | r2c1 |
| info | 18 | `non_isa_tag` | YI-110111D | instrument tag 'YI-110111D' does not parse as ISA-5.1 | r2c1 |
| info | 18 | `non_isa_tag` | YA-110111A | instrument tag 'YA-110111A' does not parse as ISA-5.1 | r2c1 |
| info | 18 | `non_isa_tag` | YA-110111B | instrument tag 'YA-110111B' does not parse as ISA-5.1 | r2c1, r2c2 |
| info | 18 | `non_isa_tag` | XC-110111A | instrument tag 'XC-110111A' does not parse as ISA-5.1 | r2c1, r2c2 |
| info | 18 | `non_isa_tag` | XC-110111B | instrument tag 'XC-110111B' does not parse as ISA-5.1 | r2c2 |
| info | 18 | `non_isa_tag` | XC-110111C | instrument tag 'XC-110111C' does not parse as ISA-5.1 | r2c2 |
| info | 18 | `non_isa_tag` | SC-110111 | instrument tag 'SC-110111' does not parse as ISA-5.1 | r2c2 |
| info | 18 | `non_isa_tag` | FI-110111 | instrument tag 'FI-110111' does not parse as ISA-5.1 | r2c2 |
| info | 19 | `low_confidence` | P19.VIN | valve in WAS inlet line to basin (diamond/bar symbol, type unclear) was read with confidence 0.50 | r2c2, r3c2 |
| info | 19 | `low_confidence` | P19.VAIR | butterfly valve was read with confidence 0.50 | r2c2, r3c2 |
| info | 19 | `low_confidence` | P19.VOUT | valve in WAS outlet line (bow-tie/bar symbol, type unclear) was read with confidence 0.50 | r3c3 |
| info | 19 | `non_isa_tag` | LE-190102 | instrument tag 'LE-190102' does not parse as ISA-5.1 | r3c2 |
| info | 19 | `non_isa_tag` | LT-190102 | instrument tag 'LT-190102' does not parse as ISA-5.1 | r2c2, r3c2 |
| info | 19 | `non_isa_tag` | LIR-190102 | instrument tag 'LIR-190102' does not parse as ISA-5.1 | r1c2 |
| info | 19 | `non_isa_tag` | LAH-190102 | instrument tag 'LAH-190102' does not parse as ISA-5.1 | r1c2 |
| info | 19 | `non_isa_tag` | LAL-190102 | instrument tag 'LAL-190102' does not parse as ISA-5.1 | r1c2 |
| info | 19 | `non_isa_tag` | TSH-190111 | instrument tag 'TSH-190111' does not parse as ISA-5.1 | r2c3, r3c3 |
| info | 19 | `non_isa_tag` | ME-190111 | instrument tag 'ME-190111' does not parse as ISA-5.1 | r2c3, r3c3 |
| info | 19 | `non_isa_tag` | YI-190111A | instrument tag 'YI-190111A' does not parse as ISA-5.1 | r1c3 |
| info | 19 | `non_isa_tag` | YC-190111 | instrument tag 'YC-190111' does not parse as ISA-5.1 | r1c3 |
| info | 19 | `non_isa_tag` | YI-190111B | instrument tag 'YI-190111B' does not parse as ISA-5.1 | r1c3 |
| info | 19 | `non_isa_tag` | TAH-190111 | instrument tag 'TAH-190111' does not parse as ISA-5.1 | r1c3 |
| info | 19 | `non_isa_tag` | MAH-190111 | instrument tag 'MAH-190111' does not parse as ISA-5.1 | r1c3 |
| info | 19 | `non_isa_tag` | ZA-190111 | instrument tag 'ZA-190111' does not parse as ISA-5.1 | r1c3 |
| info | 19 | `non_isa_tag` | JS-190111 | instrument tag 'JS-190111' does not parse as ISA-5.1 | r1c3, r2c3 |
| info | 19 | `non_isa_tag` | HS-190111 | instrument tag 'HS-190111' does not parse as ISA-5.1 | r1c3, r2c3 |
| info | 19 | `non_isa_tag` | TY-190111 | instrument tag 'TY-190111' does not parse as ISA-5.1 | r1c3, r2c3 |
| info | 19 | `non_isa_tag` | MY-190111 | instrument tag 'MY-190111' does not parse as ISA-5.1 | r1c3, r2c3 |
| info | 19 | `non_isa_tag` | MS-190111 | instrument tag 'MS-190111' does not parse as ISA-5.1 | r1c3, r2c3 |
| info | 20 | `isolated_instrument` | P20.HMI1 | HMI (untagged) has no connections at all | r2c2 |
| info | 20 | `non_isa_tag` | TSH-190301 | instrument tag 'TSH-190301' does not parse as ISA-5.1 | r2c2, r3c2 |
| info | 21 | `tag_reused` | LAH-001@P-401 | 'LAH-001' identifies different items on different sheets; kept as 'LAH-001@P-401' | r1c1, r1c2 |
| info | 21 | `tag_reused` | LAL-001@P-401 | 'LAL-001' identifies different items on different sheets; kept as 'LAL-001@P-401' | r1c2 |
| info | 21 | `tag_reused` | LCH-001@P-401 | 'LCH-001' identifies different items on different sheets; kept as 'LCH-001@P-401' | r1c1, r1c2 |
| info | 21 | `tag_reused` | LCL-001@P-401 | 'LCL-001' identifies different items on different sheets; kept as 'LCL-001@P-401' | r1c1, r1c2 |
| info | 21 | `tag_reused` | LI-001@P-401 | 'LI-001' identifies different items on different sheets; kept as 'LI-001@P-401' | r1c2 |
| info | 21 | `tag_reused` | YA-001@P-401 | 'YA-001' identifies different items on different sheets; kept as 'YA-001@P-401' | r1c2 |
| info | 22 | `non_isa_tag` | ZIO-500,101 | instrument tag 'ZIO-500,101' does not parse as ISA-5.1 | r1c1, r1c2 |
| info | 22 | `non_isa_tag` | ZIC-500,101 | instrument tag 'ZIC-500,101' does not parse as ISA-5.1 | r1c1, r1c2 |
| info | 22 | `non_isa_tag` | YA-500,101 | instrument tag 'YA-500,101' does not parse as ISA-5.1 | r1c1, r1c2 |
| info | 22 | `non_isa_tag` | YI-500,101 | instrument tag 'YI-500,101' does not parse as ISA-5.1 | r1c2 |
| info | 22 | `non_isa_tag` | ZCO-500,101 | instrument tag 'ZCO-500,101' does not parse as ISA-5.1 | r1c2 |
| info | 22 | `non_isa_tag` | ZCC-500,101 | instrument tag 'ZCC-500,101' does not parse as ISA-5.1 | r1c2 |
| info | 22 | `non_isa_tag` | HS-500,101 | instrument tag 'HS-500,101' does not parse as ISA-5.1 | r1c2, r2c2 |
| info | 22 | `non_isa_tag` | ZSO-500,101 | instrument tag 'ZSO-500,101' does not parse as ISA-5.1 | r2c2 |
| info | 22 | `non_isa_tag` | ZSC-500,101 | instrument tag 'ZSC-500,101' does not parse as ISA-5.1 | r2c2 |
| info | 22 | `non_isa_tag` | ZSO-500,201 | instrument tag 'ZSO-500,201' does not parse as ISA-5.1 | r2c2, r3c2 |
| info | 22 | `non_isa_tag` | ZSC-500,201 | instrument tag 'ZSC-500,201' does not parse as ISA-5.1 | r2c2, r3c2 |
| info | 22 | `non_isa_tag` | ZSO-500,301 | instrument tag 'ZSO-500,301' does not parse as ISA-5.1 | r2c2, r3c2 |
| info | 22 | `non_isa_tag` | ZSC-500,301 | instrument tag 'ZSC-500,301' does not parse as ISA-5.1 | r2c2, r3c2 |
| info | 22 | `non_isa_tag` | ZSO-500,201 | instrument tag 'ZSO-500,201' does not parse as ISA-5.1 | r2c2, r3c2 |
| info | 22 | `non_isa_tag` | ZSC-500,201 | instrument tag 'ZSC-500,201' does not parse as ISA-5.1 | r2c2, r3c2 |
| info | 23 | `low_confidence` | P23.DIAM1 | diamond/bow-tie symbol on FOR line (unlabelled, type uncertain) was read with confidence 0.50 | r2c2, r3c2 |
| info | 23 | `low_confidence` | P23.FSV1 | manual valve was read with confidence 0.50 | r2c2, r3c2 |
| info | 23 | `low_confidence` | P23.OV1 | overfill prevention valve with float on tank top was read with confidence 0.50 | r2c2, r2c3 |
| info | 23 | `low_confidence` | P23.DEV1 | unlabelled inline device with bracket tab on FOS line (type uncertain) was read with confidence 0.40 | r2c3 |
| info | 23 | `low_confidence` | P23.FSV2 | manual valve was read with confidence 0.50 | r2c3, r3c3 |
| info | 23 | `low_confidence` | P23.DIAM2 | diamond/bow-tie symbol on FOS line (unlabelled, type uncertain) was read with confidence 0.50 | r2c3, r3c3 |
| info | 23 | `low_confidence` | BOUNDARY:ATMOSPHERE TANK VENTS | ATMOSPHERE (tank vents) was read with confidence 0.50 |  |
| info | 23 | `low_confidence` | P23.L3.1 | L3 [1/2] was read with confidence 0.55 |  |
| info | 23 | `low_confidence` | P23.L3.2 | L3 [2/2] was read with confidence 0.55 |  |
| info | 23 | `low_confidence` | P23.L4.1 | L4 [1/2] was read with confidence 0.55 |  |
| info | 23 | `low_confidence` | P23.L4.2 | L4 [2/2] was read with confidence 0.55 |  |
| info | 23 | `low_confidence` | P23.L5.1 | L5 [1/2] was read with confidence 0.55 |  |
| info | 23 | `low_confidence` | P23.L5.2 | L5 [2/2] was read with confidence 0.55 |  |
| info | 23 | `non_isa_tag` | LIT-600,201A | instrument tag 'LIT-600,201A' does not parse as ISA-5.1 | r2c2, r3c2 |
| info | 23 | `non_isa_tag` | LSH-600,201B | instrument tag 'LSH-600,201B' does not parse as ISA-5.1 | r2c2, r2c3 |
| info | 23 | `non_isa_tag` | LSL-600,201C | instrument tag 'LSL-600,201C' does not parse as ISA-5.1 | r2c3, r3c3 |
| info | 23 | `non_isa_tag` | LSH-600,201D | instrument tag 'LSH-600,201D' does not parse as ISA-5.1 | r2c3, r3c3 |
| info | 23 | `non_isa_tag` | YI-600,201E | instrument tag 'YI-600,201E' does not parse as ISA-5.1 | r1c2, r2c2 |
| info | 23 | `non_isa_tag` | HS-600,201F | instrument tag 'HS-600,201F' does not parse as ISA-5.1 | r2c2 |
| info | 23 | `non_isa_tag` | LI-600,201B | instrument tag 'LI-600,201B' does not parse as ISA-5.1 | r1c2 |
| info | 23 | `non_isa_tag` | LAL-600,201A | instrument tag 'LAL-600,201A' does not parse as ISA-5.1 | r1c2 |
| info | 23 | `non_isa_tag` | LAH-600,201B | instrument tag 'LAH-600,201B' does not parse as ISA-5.1 | r1c2, r1c3 |
| info | 23 | `non_isa_tag` | LAH-600,201C | instrument tag 'LAH-600,201C' does not parse as ISA-5.1 | r1c2, r1c3 |
| info | 23 | `non_isa_tag` | YA-600,201D | instrument tag 'YA-600,201D' does not parse as ISA-5.1 | r1c3 |
| info | 24 | `low_confidence` | P24.DF1 | diamond/bow-tie symbol (unlabelled, type uncertain) was read with confidence 0.50 | r2c1, r3c1 |
| info | 24 | `low_confidence` | P24.FVF | manual valve was read with confidence 0.50 | r2c1, r3c1 |
| info | 24 | `low_confidence` | P24.DA1 | diamond/bow-tie symbol (unlabelled, type uncertain) was read with confidence 0.50 | r2c1, r3c1 |
| info | 24 | `low_confidence` | P24.FVA | manual valve was read with confidence 0.50 | r2c1, r3c1 |
| info | 24 | `low_confidence` | P24.DA2 | diamond/bow-tie symbol (unlabelled, type uncertain) was read with confidence 0.50 | r2c1, r3c1 |
| info | 24 | `low_confidence` | P24.CHK1 | check valve was read with confidence 0.50 | r2c1, r3c1 |
| info | 24 | `low_confidence` | P24.UV1 | inline valve symbol with stem tick (type uncertain) was read with confidence 0.40 | r2c2, r3c2 |
| info | 24 | `low_confidence` | P24.DA3 | diamond/bow-tie symbol (unlabelled, type uncertain) was read with confidence 0.50 | r2c2, r3c2 |
| info | 24 | `low_confidence` | P24.DRN1 | drain was read with confidence 0.50 | r3c3 |
| info | 24 | `low_confidence` | P24.STRA | strainer was read with confidence 0.55 | r3c3 |
| info | 24 | `low_confidence` | P24.BOX1 | inline device with bracket tab (unlabelled, type uncertain) was read with confidence 0.40 | r2c3, r3c3 |
| info | 24 | `low_confidence` | P24.FVG | manual valve was read with confidence 0.50 | r2c4, r3c4 |
| info | 24 | `low_confidence` | P24.DG | diamond/bow-tie symbol (unlabelled, type uncertain) was read with confidence 0.50 | r2c4, r3c4 |
| info | 24 | `low_confidence` | P24.STRB | strainer was read with confidence 0.55 | r3c3 |
| info | 24 | `low_confidence` | P24.BOX2 | inline device with bracket tab (unlabelled, type uncertain) was read with confidence 0.40 | r2c3, r3c3 |
| info | 24 | `low_confidence` | P24.DB | diamond/bow-tie symbol (unlabelled, type uncertain) was read with confidence 0.50 | r2c3, r3c3 |
| info | 24 | `low_confidence` | P24.CHK2 | check valve was read with confidence 0.50 | r2c3, r3c3 |
| info | 24 | `low_confidence` | P24.UV2 | inline valve symbol with stem tick (type uncertain) was read with confidence 0.40 | r2c3, r2c4 |
| info | 24 | `low_confidence` | P24.FVR | manual valve was read with confidence 0.50 | r2c4, r3c4 |
| info | 24 | `low_confidence` | P24.DR | diamond/bow-tie symbol (unlabelled, type uncertain) was read with confidence 0.50 | r2c4, r3c4 |
| info | 24 | `low_confidence` | BOUNDARY:RELIEF VALVE OUTLET DESTINATION NOT DRAWN | RELIEF VALVE OUTLET (destination not drawn) was read with confidence 0.40 |  |
| info | 24 | `low_confidence` | BOUNDARY:DRAIN OPEN END | DRAIN (open end) was read with confidence 0.50 |  |
| info | 24 | `low_confidence` | P24.L4.1 | L4 [1/2] was read with confidence 0.50 |  |
| info | 24 | `low_confidence` | P24.L4.2 | L4 [2/2] was read with confidence 0.50 |  |
| info | 24 | `low_confidence` | P24.L5.1 | L5 [1/2] was read with confidence 0.55 |  |
| info | 24 | `low_confidence` | P24.L5.2 | L5 [2/2] was read with confidence 0.55 |  |
| info | 24 | `low_confidence` | P24.L6.1 | L6 [1/2] was read with confidence 0.55 |  |
| info | 24 | `low_confidence` | P24.L6.2 | L6 [2/2] was read with confidence 0.55 |  |
| info | 24 | `low_confidence` | P24.L7.1 | L7 [1/2] was read with confidence 0.50 |  |
| info | 24 | `low_confidence` | P24.L7.2 | L7 [2/2] was read with confidence 0.50 |  |
| info | 24 | `low_confidence` | P24.L11.1 | L11 [1/2] was read with confidence 0.50 |  |
| info | 24 | `low_confidence` | P24.L11.2 | L11 [2/2] was read with confidence 0.50 |  |
| info | 24 | `non_isa_tag` | PI-600,203A | instrument tag 'PI-600,203A' does not parse as ISA-5.1 | r2c1, r2c2 |
| info | 24 | `non_isa_tag` | PI-600,203B | instrument tag 'PI-600,203B' does not parse as ISA-5.1 | r2c2, r3c2 |
| info | 24 | `non_isa_tag` | PI-600,205A | instrument tag 'PI-600,205A' does not parse as ISA-5.1 | r2c3, r3c3 |
| info | 24 | `non_isa_tag` | PI-600,205B | instrument tag 'PI-600,205B' does not parse as ISA-5.1 | r2c3, r2c4 |
| info | 24 | `non_isa_tag` | LSH-600,204A | instrument tag 'LSH-600,204A' does not parse as ISA-5.1 | r2c2, r2c3 |
| info | 24 | `non_isa_tag` | LSL-600,204B | instrument tag 'LSL-600,204B' does not parse as ISA-5.1 | r2c2, r2c3 |
| info | 24 | `non_isa_tag` | LIT-600,204C | instrument tag 'LIT-600,204C' does not parse as ISA-5.1 | r2c3, r3c3 |
| info | 24 | `non_isa_tag` | LSH-600,204D | instrument tag 'LSH-600,204D' does not parse as ISA-5.1 | r3c3 |
| info | 24 | `non_isa_tag` | LAL-600,204B | instrument tag 'LAL-600,204B' does not parse as ISA-5.1 | r1c2 |
| info | 24 | `non_isa_tag` | LAH-600,204D | instrument tag 'LAH-600,204D' does not parse as ISA-5.1 | r1c2, r1c3 |
| info | 24 | `non_isa_tag` | LAH-600,204A | instrument tag 'LAH-600,204A' does not parse as ISA-5.1 | r1c2, r1c3 |
| info | 24 | `non_isa_tag` | YA-600,204E | instrument tag 'YA-600,204E' does not parse as ISA-5.1 | r1c3 |
| info | 24 | `non_isa_tag` | YA-600,203 | instrument tag 'YA-600,203' does not parse as ISA-5.1 | r1c3 |
| info | 24 | `non_isa_tag` | YA-600,205 | instrument tag 'YA-600,205' does not parse as ISA-5.1 | r1c3 |
| info | 25 | `isolated_instrument` | PI-600,205 | PI-600,205 has no connections at all | r1c2, r2c2 |
| info | 25 | `low_confidence` | P25.DFS | diamond/bow-tie symbol (unlabelled, type uncertain) was read with confidence 0.50 | r2c1, r3c1 |
| info | 25 | `low_confidence` | P25.DRV | drain was read with confidence 0.50 | r2c3, r2c4 |
| info | 25 | `low_confidence` | P25.DRR | diamond/bow-tie symbol (unlabelled, type uncertain) was read with confidence 0.50 | r2c3, r2c4 |
| info | 25 | `non_isa_tag` | PI-600,205 | instrument tag 'PI-600,205' does not parse as ISA-5.1 | r1c2, r2c2 |
| info | 25 | `non_isa_tag` | YI-600,009C | instrument tag 'YI-600,009C' does not parse as ISA-5.1 | r1c1, r1c2 |
| info | 25 | `non_isa_tag` | YA-600,009C | instrument tag 'YA-600,009C' does not parse as ISA-5.1 | r1c1, r1c2 |
| info | 25 | `non_isa_tag` | YI-600,204B | instrument tag 'YI-600,204B' does not parse as ISA-5.1 | r1c1, r1c2 |
| info | 25 | `non_isa_tag` | YI-600,204A | instrument tag 'YI-600,204A' does not parse as ISA-5.1 | r1c2 |
| info | 25 | `non_isa_tag` | YA-600,204A | instrument tag 'YA-600,204A' does not parse as ISA-5.1 | r1c2 |
