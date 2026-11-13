"""Build (python reading.py build) or check (python reading.py check) the marked reading of c. 44r.

The marked block of reading_44r_marked.md (reading_44r.md holds the sentences only) is generated from align_44r.txt and key.tsv: each word is the value of its
signs; where the value read in this place differs from the key value the word carries a mark:
  {x/y} the signs give x (key value), read y;  {+a} a added where the sign is a point/null in the key;
  {-x} the signs give x, dropped (sign not explained here).
check: removes the marks back to the signs' values and compares, line by line, with decryption_44r.txt
(the mechanical decryption with key.tsv); prints word counts. Exit 1 on any unmarked departure."""
import sys, os, re, unicodedata
sys.path.insert(0, os.path.dirname(__file__))
from common import read_align, read_key, HERE
sys.stdout.reconfigure(encoding='utf-8')
CODES = {'chu', 'dis', 'qre'}

def marked_words(al, key):
    lines = {}
    for lab, words in sorted(al.items()):
        ws = []
        for w in words:
            parts, kind = [], 'verbatim'
            for tok, val in w:
                kv = key.get(tok, '?')
                if val == '_' and kv == '_': continue
                if val == kv: parts.append(val.replace("+", " "))
                elif val == '?': parts.append('{-%s}' % kv); kind = 'repaired'
                elif kv == '_': parts.append('{+%s}' % val); kind = 'repaired'
                else: parts.append("{%s/%s}" % (kv, val.replace("+", " "))); kind = 'repaired'
            if any(t in CODES for t, _ in w) and kind == 'verbatim': kind = 'code'
            ws.append((''.join(parts), kind))
        lines[lab] = ws
    return lines

def norm(s):
    s = unicodedata.normalize('NFC', s).lower().replace('v', 'u')
    return re.sub(r'[^a-zñ]', '', s)

def to_mech(s):
    s = re.sub(r'\{([^/{}]*)/([^/{}]*)\}', r'\1', s)
    s = re.sub(r'\{\+[^{}]*\}', '', s)
    s = re.sub(r'\{-([^{}]*)\}', r'\1', s)
    return s

if __name__ == '__main__':
    key = read_key(os.path.join(HERE, 'key.tsv')); al = read_align()
    rp = os.path.join(HERE, 'reading_44r_marked.md')
    if sys.argv[1:] == ['build']:
        ml = marked_words(al, key)
        block = '\n'.join(f"{lab}: {' '.join(w for w, _ in ws)}" for lab, ws in ml.items())
        txt = open(rp, encoding='utf-8').read()
        txt = re.sub(r'```marked\n.*?```', '```marked\n' + block + '\n```', txt, flags=re.S)
        txt = txt.replace(' enello', ' en ello')  # one sign (ne) spans the two words
        open(rp, 'w', encoding='utf-8').write(txt); print('built'); sys.exit(0)
    txt = open(rp, encoding='utf-8').read()
    block = re.search(r'```marked\n(.*?)```', txt, re.S).group(1)
    dec = {l.split(':', 1)[0]: l.split(':', 1)[1] for l in open(os.path.join(HERE, 'decryption_44r.txt'), encoding='utf-8') if l.startswith('L')}
    bad = 0; counts = {'verbatim': 0, 'repaired': 0, 'code': 0}
    for ln in block.strip().split('\n'):
        lab, rest = ln.split(':', 1)
        if norm(to_mech(rest)) != norm(dec[lab].replace('-', '')):
            print('UNMARKED DEPARTURE in', lab); print('  reading->signs:', norm(to_mech(rest))); print('  decryption   :', norm(dec[lab].replace('-', ''))); bad += 1
        for w in rest.split():
            counts['repaired' if '{' in w else ('code' if norm(w) in ('tiempo', 'emperador', 'uuestra') else 'verbatim')] += 1
    n = sum(counts.values())
    print(f"words {n}: verbatim from the signs {counts['verbatim']}, code groups {counts['code']}, with a marked repair {counts['repaired']}, holes 0")
    print(f"verbatim share {counts['verbatim']/n:.1%}; verbatim + code {(counts['verbatim']+counts['code'])/n:.1%}")
    # Verbatim words that hold a sign whose key value rests on one place only (key.tsv 'places' = 1): that value
    # comes from the alignment with c. 42r alone, so the word is verbatim by construction (independent review, 13 Nov 2026).
    once = {ln.split('	')[0] for ln in open(os.path.join(HERE, 'key.tsv'), encoding='utf-8')
            if not ln.startswith(('#', 'sign	')) and ln.strip() and ln.split('	')[2] == '1'}
    single = 0
    for lab, ws in marked_words(al, key).items():
        for (w, kind), raw in zip(ws, al[lab]):
            if kind == 'verbatim' and any(tok in once for tok, _ in raw):
                single += 1
    strict = counts['verbatim'] - single
    print(f"of the verbatim words, {single} hold a sign whose value rests on that one place (from c. 42r alone; "
          f"{len(once)} key entries with places = 1); verbatim without them {strict} ({strict/n:.1%})")
    sys.exit(1 if bad else 0)
