#!/usr/bin/env python3
"""Held-out tests of key_frozen.tsv (built from the Coslin letter c793 only). Standard library only.
    python scripts/heldout.py > heldout.txt
1. Scan 819: mechanical decryption of the cipher with the frozen key against the summary decipherment written in the
   margin at the time (gloss_819_margin.txt): word alignment and letter agreement.
2. Scan 797: the two interlinear glosses against the frozen-key decryption of the groups under them.
3. Documents not used to build the key (ps797, ps717, l819, w787, w813): units not in the frozen key."""
import difflib, re, sys, pathlib, unicodedata
sys.stdout.reconfigure(encoding='utf-8')
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parent
sys.path.insert(0, str(HERE)); import decrypt
K = decrypt.key(ROOT / 'key_frozen.tsv')
def norm(s):
    s = unicodedata.normalize('NFD', s); s = ''.join(c for c in s if not unicodedata.combining(c)).lower()
    s = s.replace('v', 'u').replace('j', 'i').replace('uu', 'w').replace('ß', 'ss')
    return re.findall(r'[a-z]+', s)
def cipher_only(t):
    return ' '.join(x for x in decrypt.TOK.findall(t) if not x.startswith(('"', '[')) and x != '|')
tr = [l.split('\t', 1) for l in (ROOT / 'transcription_l819.txt').read_text(encoding='utf-8').splitlines() if not l.startswith('#')]
mech = ' '.join(decrypt.dec(cipher_only(t), K) for _, t in tr)
gloss = ' '.join(l for l in (ROOT / 'gloss_819_margin.txt').read_text(encoding='utf-8').splitlines() if not l.startswith('#'))
a, b = ''.join(norm(mech)), ''.join(norm(gloss))
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
match = sum(m.size for m in sm.get_matching_blocks())
print('1. scan 819, frozen key vs margin decipherment of the time')
print('   mechanical (cipher groups only):', mech)
print('   margin note:                    ', gloss)
print(f'   letters of the note matched in order by the mechanical decryption: {match}/{len(b)} = {match / len(b):.3f}')
gw = norm(gloss); mw = ''.join(norm(mech))
hit = [w for w in gw if w in mw]
print(f'   note words found letter for letter in the decryption: {len(hit)}/{len(gw)} = {len(hit) / len(gw):.3f}')
print('   note words not found:', [w for w in gw if w not in mw])
print('2. scan 797, interlinear glosses')
for groups, g in (('9.1. 11.5.16.11.', 'so bald'), ('20.3.7.4.11.8.1.', 'zu dero')):
    d = decrypt.dec(groups, K)
    r = difflib.SequenceMatcher(None, d.replace(' ', ''), g.replace(' ', '')).ratio()
    print(f'   {groups:18} -> {d!r:12} gloss {g!r:10} letter ratio {r:.2f}')
print('3. units not in the frozen key, documents not used to build it')
for f in ['transcription_ps797.txt', 'transcription_ps717.txt', 'transcription_l819.txt', 'transcription_w787.txt', 'transcription_w813.txt']:
    n = miss = 0; odd = []
    for l in (ROOT / f).read_text(encoding='utf-8').splitlines():
        if l.startswith('#'): continue
        for x in re.findall(r'(?<![\w"])(\d+)', re.sub(r'"[^"]*"|\[[^\]]*\]', ' ', l.split('\t', 1)[1])):
            n += 1
            if x not in K: miss += 1; odd.append(x)
    print(f'   {f}: {n} numbers, {miss} not in the frozen key {sorted(set(odd))}')
