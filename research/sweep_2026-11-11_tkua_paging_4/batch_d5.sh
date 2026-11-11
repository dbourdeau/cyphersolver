#!/bin/bash
cd /home/user/cyphersolver/research/sweep_2026-11-11_tkua_paging_4
for b in 261295 261296 261297 261298 261299 261301 261303 261305 261418 261419 261420 261421 261422 261425 261427 261429; do python3 ao.py sheet $b /tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a5d/sh 8 400 4 5; done
