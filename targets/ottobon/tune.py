"""Grid over decoder weights on the synthetic test (dec.sim) and the hand-reading calibration (dec.calib)."""
import sys, os, itertools, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dec
grid = eval(sys.argv[1])       # dict of lists
mode = sys.argv[2] if len(sys.argv) > 2 else 'sim'
for combo in itertools.product(*grid.values()):
    for k, v in zip(grid, combo): dec.P[k] = v
    dec._EXT.clear()
    if mode == 'sim': dec.sim(float(os.environ.get('FLAT', 1.0)))
    else: dec.calib()
    sys.stdout.flush()
