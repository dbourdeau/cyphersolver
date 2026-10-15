"""Apply one of George Lasry's reconstructed SP 106/10 keys (DECODE record file) to one letter's cipher groups,
and compare group by group with his interlinear plaintext.

  python apply_key.py <key file> <letter section> <interlinear file> [--reveal out.json N0 N1 slug anchor title caption]

<letter section> is the folio label of the section in Lasry's interlinear file (e.g. 0247, 0213-0215).
The DECODE files are Lasry's and DECODE's and stay git-ignored in decode/ (fetched with the shared cookie).
"""
import sys, re, json, pathlib

def load_key(path):
    key = {}
    for l in pathlib.Path(path).read_text(encoding='utf-8', errors='replace').splitlines():
        if l.startswith('#'):
            if re.match(r'#{6,}', l) or l.startswith('#CIPHERTEXT'): break
            continue
        m = re.match(r'\s*([0-9a-z|]+)\s+-\s+(.+?)\s*$', l)
        if m:
            for g in m.group(1).split('|'): key[g] = m.group(2)
    return key

def section_pairs(path, sec):
    cur, lines = None, []
    for l in pathlib.Path(path).read_text(encoding='utf-8', errors='replace').splitlines():
        m = re.match(r'#{6,}\s*tna[ _]sp106.(\S+?)(\.txt)?\s*$', l)
        if m: cur = m.group(1); continue
        if l.startswith('#KEY'): cur = None; continue
        if cur == sec: lines.append(l)
    body = [l for l in lines if l.strip() and not l.lstrip().startswith(('#', '<CLEAR'))]
    pairs, mism = [], 0
    for i in range(0, len(body) - 1, 2):
        c = body[i].rstrip().rstrip('|').split(); p = body[i + 1].rstrip().rstrip('|').split()
        if len(c) != len(p): mism += 1; p = [None] * len(c)   # columns do not line up: no group-by-group comparison
        pairs += list(zip(c, p))
    return pairs, mism

if __name__ == '__main__':
    key = load_key(sys.argv[1]); pairs, mism = section_pairs(sys.argv[3], sys.argv[2])
    n = len(pairs); dec = sum(1 for g, _ in pairs if g in key)
    comp = [(g, p) for g, p in pairs if g in key and p is not None]
    agree = sum(1 for g, p in comp if key[g] == p)
    print(f'key entries {len(key)}; groups {n}; given a value by the key {dec} ({dec / n:.4f}); '
          f'compared with Lasry (lines whose columns line up) {len(comp)}, agree {agree} ({agree / max(1, len(comp)):.4f}); lines with column mismatch {mism}')
    if '--reveal' in sys.argv:
        a = sys.argv[sys.argv.index('--reveal') + 1:]
        out, n0, n1, slug, anchor, title, caption = a[0], int(a[1]), int(a[2]), a[3], a[4], a[5], a[6]
        toks = []
        for g, p in pairs[n0:n1]:
            v = key.get(g)
            if v is None: toks.append({'g': g, 'p': '?', 'cls': 'unk'})
            else:
                t = {'g': g, 'p': v.lower() if len(v) == 1 else v.lower() + ' '}
                if len(v) > 1 or not v.isalpha(): t['cls'] = 'code'
                if p is not None and p != v: t['cls'] = 'unc'
                toks.append(t)
        json.dump({'slug': slug, 'anchor': anchor, 'title': title, 'caption': caption, 'unit': 'figures',
                   'key_note': "George Lasry's reconstructed key (DECODE, 23 Oct 2020), applied here group by group to "
                               "Sofia Pettersson's transcription; ? = a group the key gives no value (nomenclator number "
                               "or a figure Lasry left open).",
                   'tokens': toks}, open(out, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
        print('reveal', out, len(toks), 'tokens')
