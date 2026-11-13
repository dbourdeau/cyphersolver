"""Contact sheets of Rigsarkivet units: python3 dksheets.py stride <bsid> ... (5x4 frames of 400 px) -> scratch/dk/"""
import sys, ao
out = '/tmp/claude-0/-home-user-cyphersolver/6cad9ef2-f4c1-5b63-a0df-f48b5a524c6f/scratchpad/nordic/dk'
st = int(sys.argv[1])
for b in sys.argv[2:]:
    ao.sheet(b, out, stride=st, width=400, cols=5, rows=4)
