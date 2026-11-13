"""Held-out measure for 1410,115. The frozen key (K_P2) was built by Brice Dudout on other letters of AGS Estado 1410,
so every line of this letter is held out. Measure: character agreement (difflib ratio) between the mechanical
decryption of each line and the marked reading resolved to its read text, summed over lines; the same for 200 control
keys (100 with the consonant values permuted, 100 with the vowel-mark values permuted together with the vowels).
    python -I scripts/heldout.py
"""
import difflib, pathlib, random, re, sys, unicodedata
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
import decrypt  # noqa: E402

def norm(s):
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c)).lower().replace('v', 'u')
    return re.sub(r'[^a-z]', '', s)

def read_text(marked):
    s = re.sub(r'\{\?([^{}]*)\}', r'\1', marked)
    s = re.sub(r'\{([^/{}]*)/([^/{}]*)\}', r'\2', s)
    s = re.sub(r'\{\+([^{}]*)\}', r'\1', s)
    s = re.sub(r'\{-[^{}]*\}', '', s)
    s = re.sub(r'\[\?([^=\]]*)=[^\]]*\]', r'\1', s)
    s = s.replace('[...]', '')
    return s

k = decrypt.load(ROOT / 'key_frozen.tsv')
lines = [l.rstrip('\n') for l in open(ROOT / "transcription_1410_115.txt", encoding='utf-8') if l.strip() and not l.startswith('#')]
block = re.search(r'```marked\n(.*?)```', (ROOT / 'marked_1410_115.md').read_text(encoding='utf-8'), re.S).group(1)
ref = [norm(read_text(re.sub(r'^L\d+:\s*', '', l))) for l in block.splitlines() if l.strip()]

refw = [[norm(w) for w in read_text(re.sub(r'^L\d+:\s*', '', l)).split() if norm(w)]
        for l in block.splitlines() if l.strip()]

def score(key):
    """Characters: difflib matching blocks. Words: share of read words of 3+ letters found, in order, in the
    line's mechanical decryption (spaces removed)."""
    a = b = hit = tot = 0
    for tl, r, ws in zip(lines, ref, refw):
        d = norm(decrypt.dec_line(tl, key))
        sm = difflib.SequenceMatcher(None, d, r, autojunk=False)
        a += sum(m.size for m in sm.get_matching_blocks()); b += max(len(r), 1)
        pos = 0
        for w in ws:
            if len(w) < 3:
                continue
            tot += 1
            j = d.find(w, pos)
            if j >= 0:
                hit += 1; pos = j + len(w)
    return a / b, hit / tot, tot

real, rw, nw = score(k)
random.seed(1577)
ctrl = []
for i in range(200):
    kk = {x: dict(y) for x, y in k.items()}
    if i < 100:
        ks = list(kk['cons']); vs = [kk['cons'][x] for x in ks]; random.shuffle(vs); kk['cons'] = dict(zip(ks, vs))
    else:
        ms = list(kk['mark']); vs = [kk['mark'][x] for x in ms]; random.shuffle(vs); kk['mark'] = dict(zip(ms, vs))
        ks = list(kk['vowel']); vs = [kk['vowel'][x] for x in ks]; random.shuffle(vs); kk['vowel'] = dict(zip(ks, vs))
    ctrl.append(score(kk)[:2])
print(f'frozen key: chars {real:.3f}, words (3+ letters) {rw:.3f} of {nw} ({len(lines)} lines)')
print(f'controls (200 keys): chars max {max(c[0] for c in ctrl):.3f}, words max {max(c[1] for c in ctrl):.3f}, '
      f'words mean {sum(c[1] for c in ctrl)/len(ctrl):.3f}')
