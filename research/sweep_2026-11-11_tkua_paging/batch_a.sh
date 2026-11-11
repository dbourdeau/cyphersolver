#!/bin/bash
# envoy archives first (stride 8), then 17th-century relations (stride 12); sheets go to scratch
cd /home/user/cyphersolver/research/sweep_2026-11-11_tkua_paging
for b in 261576 261577 261583 261587 261588 261590 261578 261386 261387 261389 261388 262200 417522 417523 260773 260774 262107 260706 261580 261589 261592 261591; do python3 ao.py sheet $b /tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a5/sh2 8 400; done
for b in 261575 261473 261490 261377 261380 261383 261385 261267 260954 260956 260652 673416 673415 261415 260649 262098 262100 262105 262102 261584 261593; do python3 ao.py sheet $b /tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a5/sh2 12 400; done
