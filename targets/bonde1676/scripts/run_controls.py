# run_controls.py: runs every shuffled-key control of this folder and writes controls/shuffle.txt.
#   python3 -I scripts/run_controls.py FRENCH_CORPUS_DIR
# FRENCH_CORPUS_DIR: the four Project Gutenberg texts listed in controls/CORPUS.txt (not in git; any copy of the same
# ebooks will do, the script asserts 'Language: French' in each file).
import os, sys, subprocess
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(HERE, *a)
corpus = sys.argv[1]
S = P('scripts', 'shuffle_control.py')
T = lambda p: P('transcriptions', p + '.txt')
fresh = ['f306r_321R', 'f306v_322L', 'f307r_322R', 'f307v_323L', 'f308r_323R', 'f309v_325L', 'f310r_325R', 'f310v_326L', 'f311r_326R']
b101 = fresh[3:]; b104 = fresh[:3]
jobs = [('key.tsv', 'ABFP', '20261112', [p]) for p in fresh]
jobs += [('key.tsv', 'ABFP', s, b101) for s in ('20261112', '7')]
jobs += [('key.tsv', 'ABFP', s, b104) for s in ('20261112', '7')]
jobs += [('key.tsv', 'ABFP', s, fresh) for s in ('20261112', '7')]
out = ['# Shuffled-key controls, 5,000 keys each, French 4-gram model (scripts/shuffle_control.py). Written by scripts/run_controls.py.',
       '# key v3 = key.tsv, tiers A B F P scored. Lines: page(s); runs; tokens; distinct numbers; true score; shuffled keys >= true; best; median; seed.']
for key, tiers, seed, pages in jobs:
    r = subprocess.run([sys.executable, '-I', S, P(key), tiers, corpus, 'French', seed] + [T(p) for p in pages], capture_output=True, text=True, check=True)
    out.append(r.stdout.strip()); print(out[-1], flush=True)
# first test on image 324: key v2, tiers A B F (b99 shuffle.py)
for seed in ('20261112', '7'):
    r = subprocess.run([sys.executable, '-I', S, P('gloss', 'KEY_v2.tsv'), 'ABF', corpus, 'French', seed, T('f308v-309r_324_heldout_v2')], capture_output=True, text=True, check=True)
    out.append('[key v2] ' + r.stdout.strip()); print(out[-1], flush=True)
# blind second transcription, key v3
for seed in ('20261112',):
    r = subprocess.run([sys.executable, '-I', S, P('key.tsv'), 'ABFP', corpus, 'French', seed] + [P('second_transcription', 'blindR_%s.txt' % p) for p in ('f307v_323L', 'f309v_325L')], capture_output=True, text=True, check=True)
    out.append('[blind] ' + r.stdout.strip()); print(out[-1], flush=True)
open(P('controls', 'shuffle.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
