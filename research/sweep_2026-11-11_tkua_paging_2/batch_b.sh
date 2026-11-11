#!/bin/bash
# second pass: 1640s-1670s envoy relations at 1 image in 4, then the rest at 1 in 8; sheets go to scratch
cd /home/user/cyphersolver/research/sweep_2026-11-11_tkua_paging_2
O=/tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a5b/sh
for b in 261380 261473 261267 261294 261575 261383 261385 260956 260653 261381 260954 261378; do python3 ao.py sheet $b $O 4 400; done
for b in 261415 262098 262100 260652 261291 261292 261490 261377 261574 260651 260649 262105 262102 673416 673415 261584 261593; do python3 ao.py sheet $b $O 8 400; done
