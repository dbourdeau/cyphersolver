"""python waitprep.py <tag> <first> <last> : wait until the background fetch has saved frame <last>, then run prep."""
import os, sys, glob, time, subprocess
here = os.path.dirname(os.path.abspath(__file__)); tag, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
t = time.time()
while not glob.glob(os.path.join(here, 'img', tag, '%03d_*.jpg' % b)) and time.time() - t < 540: time.sleep(5)
time.sleep(2)
subprocess.run([sys.executable, '-I', '-X', 'utf8', os.path.join(here, 'prep.py'), tag, str(a), str(b)])
