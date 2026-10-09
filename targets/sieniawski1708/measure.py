"""Measure the Vienna -> Schenck reading.

Cipher tokens = numbers of the 2-digit letter cipher (transcr/RUNS_FINAL.txt, entries marked ok or doubtful)
              + code numbers (3-digit codes counted by extract.py in codes.json, plus the small codes 83, "3.", "2.").
Read          = letter numbers in runs that give sense: marked ok, or doubtful only for a writer's slip of one
                letter (NO_SENSE lists the runs that give no sense; they count as unread)
              + code tokens whose value is in codes_key.json.
Letter signs with a dot (o., b., L., d., e., f., g., c., m., p., oo, ooo) are counted apart as probable nulls.
"""
import json, os, re, glob, collections
HERE = os.path.dirname(os.path.abspath(__file__))

NO_SENSE = {'gutswor', 'sollwiglaufeenden', 'is', 'lceth', 'be', 'datmseyihm', 'iwzo', 't', 'ditlan'}

def main():
    ok = dbt = 0
    per = collections.Counter(); per_ok = collections.Counter()
    for l in open(os.path.join(HERE, 'transcr', 'RUNS_FINAL.txt'), encoding='utf-8'):
        if not l.startswith('R74'): continue
        f = [x.strip() for x in l.split('|')]
        if len(f) < 5 or 'not a run' in f[4]: continue
        n = len(re.findall(r'\d+', f[1]))
        rec = f[0].split()[0]
        per[rec] += n
        if f[2] not in NO_SENSE: ok += n; per_ok[rec] += n
        else: dbt += n
    codes = json.load(open(os.path.join(HERE, 'codes.json'), encoding='utf-8'))
    known = json.load(open(os.path.join(HERE, 'codes_key.json'), encoding='utf-8'))
    ctot = sum(len(v) for v in codes.values())
    cknown = sum(len(v) for k, v in codes.items() if k in known)
    small = 0
    for p in glob.glob(os.path.join(HERE, 'transcr', 'R*.txt')):
        for l in open(p, encoding='utf-8'):
            if not re.match(r'\[P\w+ l\.', l): continue
            body = re.sub(r'\([^)]*\)', '', l)
            small += len(re.findall(r'(?<![\d.])\b(?:83|[235])\.(?=\s)', body))
    letters = ok + dbt
    total = letters + ctot + small
    read = ok + cknown
    print('letter-cipher numbers', letters, 'read (runs giving sense)', ok, 'doubtful', dbt, 'coherent %.3f' % (ok / letters))
    print('code tokens', ctot, '+ small codes', small, 'identified', cknown, 'distinct codes', len(codes), 'identified', len([k for k in codes if k in known]))
    print('all cipher tokens', total, 'read', read, 'fraction %.3f' % (read / total))
    for r in sorted(per): print(' ', r, per[r], per_ok[r])

if __name__ == '__main__':
    main()
