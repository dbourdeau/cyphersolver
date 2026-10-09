"""Write the DECODE decryption files and the key table for the Vienna -> Schenck letters.

decode_updates/decryptions/R74xx.txt (R7486-R7500): each transcribed line with every run of the letter table replaced
by its decoding (word-divided as in transcr/RUNS_FINAL.txt), known codes as {value}, open codes as <nnn>, dotted
signs as <o.> etc.; transcriber comments dropped. key_table.json: the letter table plus the five code values.
For the unprinted Sieniawski letters it writes the contemporary decipherment (G lines of sien/R74xx.txt), or for
R7476 the syllabary decoding (K lines).
"""
import json, os, re, glob, collections
from key import ALPH, letter
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(ROOT, 'decode_updates', 'decryptions')
codes = json.load(open(os.path.join(HERE, 'codes_key.json'), encoding='utf-8'))
CODEVAL = {'189': 'Baron Schenck', '190': 'King of Sweden', '150': 'King Augustus', '208': 'der Kayser', '100': 'kaiserlicher Hof'}

def key_table():
    t = {}
    for i, c in enumerate(ALPH):
        for n in range(7 + 3 * i, 10 + 3 * i): t[str(n)] = c
    t['70'] = 'w'; t['76'] = t['77'] = t['78'] = 'y'; t['79'] = 'z'
    for k, v in CODEVAL.items(): t[k] = v + ' (from context)'
    json.dump(t, open(os.path.join(HERE, 'key_table.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)

def final_runs():
    R = collections.defaultdict(list)
    for l in open(os.path.join(HERE, 'transcr', 'RUNS_FINAL.txt'), encoding='utf-8'):
        if not l.startswith('R74'): continue
        f = [x.strip() for x in l.split('|')]
        if len(f) < 5 or 'not a run' in f[4]: continue
        nums = re.findall(r'\d+', f[1])
        m = re.search(r'"([^"]*)"', f[3])
        R[f[0].split()[0]].append((nums, f[2]))
    return R

def schenck(rec, runs_unused):
    """Every cipher passage in its sentence, word-divided as in transcr/RUNS_FINAL.txt (field 4), by page and line."""
    out = ['[The letter is in clear German; below, each passage with letter-table cipher, in its sentence.]']
    for l in open(os.path.join(HERE, 'transcr', 'RUNS_FINAL.txt'), encoding='utf-8'):
        if not l.startswith(rec + ' '): continue
        f = [x.strip() for x in l.split('|')]
        if len(f) < 5 or 'not a run' in f[4]: continue
        where = f[0].split(None, 1)[1]
        m = re.findall(r'"([^"]*)"', re.sub(r'~~[^~]*~~', '', f[3]))
        ctx = ' / '.join(m) if m else f[2]
        if f[2] in ('gutswor', 'sollwiglaufeenden', 'is', 'lceth', 'be', 'datmseyihm', 'iwzo', 't', 'ditlan'):
            ctx += ' [cipher letters: ' + f[2] + '; no sense]'
        def code(mm):
            v = mm.group(1)
            return '{%s}' % CODEVAL[v] if v in CODEVAL else '<%s>' % v
        ctx = re.sub(r'(?<![\w<{])(\d{1,3})\.?(?![\w>}])', code, ctx)
        ctx = re.sub(r'(?<=\s)(oo+|[obLdefgcmp])\.(?=\s)', r'<\1>', ' ' + ctx + ' ').strip()
        out.append('[%s] %s' % (where, ctx))
    return '\n'.join(out) + '\n'

def sien(rec, tag):
    p = os.path.join(HERE, 'sien', rec + '.txt')
    out = []
    for l in open(p, encoding='utf-8'):
        if l.startswith('=='):
            out.append('[' + re.sub(r'\(.*', '', l).strip('= \n') + ']')
        m = re.match(r'\s*%s:\s*(.*)' % tag, l)
        if m and 'syllabary.tsv' not in l and 'value' not in m.group(1)[:6]:
            t = re.sub(r'\([^)]*\)', '', m.group(1))
            t = re.sub(r'\[[^\]]*\]', lambda x: x.group(0) if x.group(0) in ('[?]', '[...]') else '', t).strip()
            out.append(t.replace('^', ''))
    body = '\n'.join(out).strip()
    if tag == 'G':
        body = '[contemporary decipherment, written between the lines:]\n' + body
    return body + '\n'

def main():
    key_table()
    R = final_runs()
    os.makedirs(OUT, exist_ok=True)
    for rec in ['R%d' % r for r in range(7486, 7501)]:
        open(os.path.join(OUT, rec + '.txt'), 'w', encoding='utf-8').write(schenck(rec, R[rec]))
    for rec, tag in [('R7475', 'G'), ('R7476', 'K'), ('R7481', 'G'), ('R7482', 'G'), ('R7484', 'G'), ('R7485', 'G')]:
        open(os.path.join(OUT, rec + '.txt'), 'w', encoding='utf-8').write(sien(rec, tag))
    print('written')

if __name__ == '__main__':
    main()
