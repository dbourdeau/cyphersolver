#!/bin/sh
# after run_h: Chigi nunciature volumes (every 16th canvas), then page-by-page passes of Barb. lat. 7029 and 9848
while pgrep -f "run_g.sh|run_h.sh" >/dev/null; do sleep 20; done
for n in A.II.33 A.II.34 A.II.35 A.II.38 A.II.44 A.II.47 A.II.27 A.II.28 A.II.30 A.I.4 A.I.6 A.I.7 A.I.23; do python3 man.py /tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a8 Chig.$n || exit 1; python3 sheet.py /tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a8 Chig.$n --step 16 --from 8; done
python3 sheet.py /tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a8 Barb.lat.7029; python3 sheet.py /tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a8 Barb.lat.9848
