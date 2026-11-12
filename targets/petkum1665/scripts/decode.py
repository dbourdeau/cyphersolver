# decode.py KEY TRANSCRIPTION > DECRYPTION
# Decodes one frozen transcription with one key, once, line by line. Standard library only; run with python3 -I.
# This is the decode mode of the contributor's decode_v2.py (b94, 12 Nov 2026), unchanged in logic:
#   transcription lines are 'LINEID|text', cipher runs stand in <...>, tokens are split by '.';
#   key rows are token<TAB>value<TAB>tier<TAB>source (tier A = read under a chancery gloss, B = row rule, C = one-anchor row).
# Output marks: value of three letters or fewer = printed as is; longer value or 'et' = {code word};
#   tier C = (value?); token not in the key = [token]. Each cipher run is printed between guillemets, tokens joined by a middle dot.
import sys, re, collections

def load_key(path):
    key = {}
    for l in open(path, encoding='utf8'):
        if l.startswith('#') or not l.strip():
            continue
        p = l.rstrip('\n').split('\t')
        key[p[0]] = (p[1], p[2])
    return key

def load_lines(path):
    lines = []
    for l in open(path, encoding='utf8'):
        if l.startswith('#') or '|' not in l:
            continue
        lid, body = l.rstrip('\n').split('|', 1)
        lines.append((lid, body))
    return lines

def dec_run(run, k):
    out = []
    for t in run.split('.'):
        t = t.strip()
        if not t:
            continue
        if t in k:
            v, tier = k[t]
            out.append(v if tier in 'AB' and len(v) <= 3 and v not in ('et',) else ('{' + v + '}' if tier in 'AB' else '(' + v + '?)'))
        else:
            out.append('[' + t + ']')
    return out

def main():
    keyf, tx = sys.argv[1], sys.argv[2]
    key = load_key(keyf)
    lines = load_lines(tx)
    toks = [t.strip() for lid, b in lines for r in re.findall(r'<([^>]*)>', b) for t in r.split('.') if t.strip()]
    c = collections.Counter(toks)
    nA = sum(n for t, n in c.items() if t in key and key[t][1] == 'A')
    nB = sum(n for t, n in c.items() if t in key and key[t][1] == 'B')
    nC = sum(n for t, n in c.items() if t in key and key[t][1] == 'C')
    nU = sum(n for t, n in c.items() if t not in key)
    print('# tokens total %d = tierA %d + tierB %d + tierC %d + unknown %d ; distinct %d' % (len(toks), nA, nB, nC, nU, len(c)))
    print('# unknown tokens:', sorted((t, n) for t, n in c.items() if t not in key))
    for lid, body in lines:
        s = re.sub(r'<([^>]*)>', lambda m: ' «' + '·'.join(dec_run(m.group(1), key)) + '» ', body)
        print(lid + '|' + re.sub(r' +', ' ', s).strip())

if __name__ == '__main__':
    main()
