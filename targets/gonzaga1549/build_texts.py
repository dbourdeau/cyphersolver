# Builds, from the sign files: one decryption file per letter (sign values line by line), validation.tsv
# (pairs for docs/_validate.py) and counts.json. Run from this folder.
import collections, json

DOCS = {
    '14nov1549': ['14nov1549_60r_block1.tsv', '14nov1549_60r_block2.tsv', '14nov1549_60v.tsv', '14nov1549_61r.tsv',
                  '14nov1549_61v.tsv', '14nov1549_62r.tsv'],
    '20nov1549': ['20nov1549_64r.tsv', '20nov1549_64v.tsv'],
    '30sep1549': ['30sep1549_50r.tsv'],
    '13may1549': ['13may1549_30r.tsv'],
    '23dec1549': ['23dec1549_76r.tsv'],
}


def rows(f):
    for l in open(f, encoding='utf8'):
        if l.startswith('#') or not l.strip():
            continue
        p = l.rstrip('\n').split('\t')
        if len(p) >= 3:
            yield p[0], p[1], p[2]


def kind(sign, v):
    if sign == 'clear':
        return 'clear'
    if v == '?':
        return 'unread'
    if v.startswith('null'):
        return 'null'
    return 'doubtful' if v.endswith('?') else 'value'


counts = {}
pairs = ['# model: es-golden-age', '# source: the sign files of the five letters, read by eye',
         '# note: clear code words left out (reading ?); null? signs as nulls; doubtful values as read']
for doc, files in DOCS.items():
    c = collections.Counter()
    out = [f'# {doc}: sign values line by line, from the sign files. [.] unread, (x?) doubtful, {{x}} clear in the cipher, nulls dropped.']
    for f in files:
        out.append('')
        out.append('## ' + f)
        cur, buf = None, []
        for ln, sign, v in rows(f):
            k = kind(sign, v)
            c[k] += 1
            if ln != cur:
                if buf:
                    out.append(f'{cur}\t' + ' '.join(buf))
                cur, buf = ln, []
            if k == 'clear':
                buf.append('{' + v + '}')
                pairs.append('clear\t?')
            elif k == 'unread':
                buf.append('[.]')
                pairs.append(f'{sign}\t?')
            elif k == 'null':
                pairs.append(f'{sign}\t-')
            else:
                buf.append(v if k == 'value' else f'({v})')
                pairs.append(f"{sign}\t{v.rstrip('?')}")
        if buf:
            out.append(f'{cur}\t' + ' '.join(buf))
    open(f'{doc}_decryption_signs.txt', 'w', encoding='utf8').write('\n'.join(out) + '\n')
    counts[doc] = dict(c, total=sum(c.values()))
all_ = collections.Counter()
for c in counts.values():
    all_.update({k: v for k, v in c.items()})
counts['all'] = dict(all_)
open('validation.tsv', 'w', encoding='utf8').write('\n'.join(pairs) + '\n')
json.dump(counts, open('counts.json', 'w', encoding='utf8'), indent=1)
print(json.dumps(counts))
