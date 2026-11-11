#!/bin/sh
# after run_h: Low Countries / Cologne volumes (Pasture) and 16th-century letter volumes, 10 canvases each
while pgrep -f "run_h.sh" >/dev/null; do sleep 20; done
for n in 6744 6764 6767 6728 6812 6906 6521 6260 6261 6207 6099 6024 5701 5708 5713 5717 5721 5723 5724 5726 5744 5781; do python3 man.py /tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a8 Barb.lat.$n || exit 1; python3 sheet.py /tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a8 Barb.lat.$n --n 10 --from 8; done
