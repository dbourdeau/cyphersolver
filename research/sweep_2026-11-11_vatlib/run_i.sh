#!/bin/sh
# after run_h: page-by-page passes of one Germania cifre volume and of the Mancini volume
while pgrep -f "run_g.sh|run_h.sh" >/dev/null; do sleep 20; done
python3 sheet.py /tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a8 Barb.lat.7029; python3 sheet.py /tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a8 Barb.lat.9848
