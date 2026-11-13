#!/bin/bash
cd /home/user/cyphersolver/research/sweep_2026-11-13_tkua_paging_5
for b in "$@"; do python3 ao.py sheet $b /tmp/claude-0/-home-user-cyphersolver/6cad9ef2-f4c1-5b63-a0df-f48b5a524c6f/scratchpad/tkua5/sh 8 400 4 5; done
