"""Decryption of the runs of DCXXI.6.576.1 and DCXXI.8.731.1 with Narvaez's key 313 (rule only; see NOTES.md),
variant A (the cycle runs on through each run, chosen by the plan for both letters).
python3 -I scripts/decrypt.py   (writes decryption_DCXXI.6.576.1.txt and decryption_DCXXI.8.731.1.txt)"""
import sys, os
from pathlib import Path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from f313 import load, decode
here = Path(__file__).resolve().parent.parent
for doc in ('DCXXI.6.576.1', 'DCXXI.8.731.1'):
    rows = load(here / f'transcription_{doc}.txt')
    with open(here / f'decryption_{doc}.txt', 'w', encoding='utf-8', newline='\n') as f:
        f.write(f'# Mechanical decryption of transcription_{doc}.txt with key 313 (variant A: cycle restarts at each run)\n# id\timage\tdecryption\n')
        for r in rows:
            f.write(f"{r['id']}\t{r['image']}\t{decode(r['run'], 'A')}\n")
print('written')
