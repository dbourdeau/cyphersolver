# run_controls.py: shuffled-key controls of this folder -> controls/shuffle.txt
#   python3 -I scripts/run_controls.py SWEDISH_CORPUS_DIR
# SWEDISH_CORPUS_DIR: the four Project Gutenberg texts of controls/CORPUS.txt (not in git); 'Language: Swedish' is asserted.
# Tiers scored: A B F P Q T G (letter values of key v9); word codes (H, W) and numbers without a value break the runs.
import os, sys, subprocess
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(HERE, *a)
corpus = sys.argv[1]
out = ['# Shuffled-key controls, 5,000 keys each, Swedish 4-gram model, w folded to v (scripts/shuffle_control.py). Written by scripts/run_controls.py.']
for label, f in (('first', P('transcriptions', 'despatch_1677-11-24_489R.txt')), ('blind', P('second_transcription', 'blindR_489R.txt'))):
    for seed in ('20261112', '7'):
        r = subprocess.run([sys.executable, '-I', P('scripts', 'shuffle_control.py'), P('key.tsv'), 'ABFPQTG', corpus, 'Swedish', seed, f], capture_output=True, text=True, check=True)
        out.append('[%s] %s' % (label, r.stdout.strip())); print(out[-1], flush=True)
open(P('controls', 'shuffle.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
