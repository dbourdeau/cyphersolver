# decode_once.py FOLDER  (python3 -I; standard library only)
# One mechanical decode of FOLDER/BLIND.tsv with the frozen Petkum key (_key_frozen/key_v5.tsv = key.tsv v3 rows
# plus the v4/v5 additions; upstream dbourdeau/cyphersolver 89e25ef7, targets/petkum1665).
# Value mapping is upstream scripts/decode.py dec_run(), unchanged: tier A/B and value <= 3 letters and not 'et' -> value;
# tier A/B longer or 'et' -> {value}; any other tier (A2, A3, A4, C, G) -> (value?). Same as upstream *_v5 decryptions.
# Local rules (task brief): '~' and '?' stripped for lookup only, noted; token not in key: number -> [n], label -> '_'.
# 'T T' decoded as written (two T tokens). Verifies hashes first and stops on any mismatch.
import sys, os, re, hashlib, datetime, collections

HERE = os.path.dirname(os.path.abspath(__file__))
KEYDIR = os.path.join(HERE, '_key_frozen')
KEY_SHA = {'key.tsv': '546d7dda8c3c65bd0c0f29ed786e5f1b433169b8433ec1259faa091cb1668494',
           'key_v5.tsv': '1d0cf98298f269ef3b6079ef9a61f6c12dfa66d6021df63b3ade5e2e7549eeee'}

def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()

def load_key(path):  # upstream decode.py load_key, unchanged
    key = {}
    for l in open(path, encoding='utf8'):
        if l.startswith('#') or not l.strip():
            continue
        p = l.rstrip('\n').split('\t')
        key[p[0]] = (p[1], p[2])
    return key

def dec_tok(t, k):  # upstream dec_run body for one token, unchanged
    v, tier = k[t]
    return v if tier in 'AB' and len(v) <= 3 and v not in ('et',) else ('{' + v + '}' if tier in 'AB' else '(' + v + '?)')

def main():
    F = os.path.abspath(sys.argv[1])
    blind = os.path.join(F, 'BLIND.tsv')
    # 1. verify
    fb = open(os.path.join(F, 'FREEZE_blind.txt'), encoding='utf8').read().split()
    if sha(blind) != fb[0]: sys.exit('STOP: BLIND.tsv sha256 mismatch')
    fz = open(os.path.join(F, 'FREEZE.txt'), encoding='utf8').read()
    for n, h in KEY_SHA.items():
        if h not in fz or sha(os.path.join(KEYDIR, n)) != h: sys.exit('STOP: key mismatch ' + n)
    key = load_key(os.path.join(KEYDIR, 'key_v5.tsv'))
    # 2. decode once
    out = ['# decode_once.txt: %s/BLIND.tsv with _key_frozen/key_v5.tsv; upstream decode.py marks. image\tline\tdecode\tdoubt notes' % os.path.basename(F)]
    c = collections.Counter(); holes = collections.Counter()
    for l in open(blind, encoding='utf8'):
        if l.startswith('#') or not l.strip() or l.startswith('image\t'):
            continue
        img, ln, toks = l.rstrip('\n').split('\t')[:3]
        dec = []; notes = []
        for raw in toks.split():
            t = raw.replace('~', '').replace('?', '')
            if t != raw: notes.append(raw)
            c['tokens'] += 1
            if t in key:
                dec.append(dec_tok(t, key)); c['valued'] += 1
            elif re.fullmatch(r'\d+', t):
                dec.append('[' + t + ']'); c['hole_number'] += 1; holes[t] += 1
            else:
                dec.append('_'); c['hole_label'] += 1; holes[raw] += 1
        c['doubt_marked'] += len(notes)
        out.append('%s\t%s\t%s\t%s' % (img, ln, '·'.join(dec), ('doubt: ' + ' '.join(notes)) if notes else ''))
    open(os.path.join(F, 'decode_once.txt'), 'w', encoding='utf8').write('\n'.join(out) + '\n')
    run = ['DECODE_RUN for %s' % os.path.basename(F),
           'time UTC: %s' % datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
           'script: decode_once.py sha256 %s' % sha(os.path.abspath(__file__)),
           'BLIND.tsv sha256 %s (matches FREEZE_blind.txt)' % sha(blind),
           'key.tsv sha256 %s ; key_v5.tsv sha256 %s (match FREEZE.txt); decode key = key_v5.tsv' % (KEY_SHA['key.tsv'], KEY_SHA['key_v5.tsv']),
           'decode_once.txt sha256 %s' % sha(os.path.join(F, 'decode_once.txt')),
           'tokens %d = valued %d + hole numbers %d + hole labels %d ; doubt-marked tokens %d' % (c['tokens'], c['valued'], c['hole_number'], c['hole_label'], c['doubt_marked']),
           'holes: %s' % ', '.join('%s x%d' % kv for kv in sorted(holes.items()))]
    assert c['tokens'] == c['valued'] + c['hole_number'] + c['hole_label']
    open(os.path.join(F, 'DECODE_RUN.txt'), 'w', encoding='utf8').write('\n'.join(run) + '\n')
    print('\n'.join(run)); print('\n'.join(out[1:]))

if __name__ == '__main__':
    main()
