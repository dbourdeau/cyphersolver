#!/bin/bash
# third pass: the 23 second-loop units (and the rest of 261383) at 1 image in 4, 20 frames a sheet (400 px); sheets go to scratch
cd /home/user/cyphersolver/research/sweep_2026-11-11_tkua_paging_3
O=/tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a5c/sh
for b in 260652 260653 260954 260956 261415 262098 261378 261385 261291 261292 261381 261377 260649 260651 262100 262102 262105 261490 261574 673416 673415 261584 261593; do python3 ao.py sheet $b $O 4 400 4 5; done
python3 ao.py sheet 261383 $O 4 400 4 5 192
