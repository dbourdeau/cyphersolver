#!/bin/sh
# sample every 10th canvas of the digitised Barberini Germania volumes
for n in 6929 6930 6931 6935 6939 6943 6944 6946 6948 6964 6985 6986 7004 7005 7006 7007 7017 7025 7029 7045 7046 7050 7053 7060 7063; do python3 man.py /tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a8 Barb.lat.$n || exit 1; python3 sheet.py /tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a8 Barb.lat.$n --step 10 --from 6; done
