"""Count the share of cipher signs that read as sense. A cipher word is unread when its decode is not an Italian word
(or name) that fits its sentence; the lists below are the judgements made on draft252.txt / draft142.txt, 6 Nov 2026."""
import csv
from build_key import merge
UNREAD = {
 't252.tsv': '1.1 1.6 1.7 2.1 2.2 2.3 2.4 2.6 2.7 2.12 2.13 3.5 3.6 3.7 3.8 3.9 3.10 3.11 4.4 4.7 5.3 6.3 6.6 6.7 6.8 6.9 6.10 '
             '7.1 7.4 7.6 9.5 9.6 9.7 9.10 10.1 10.3 10.4 10.5 10.6 11.3 11.4 11.6 12.11 13.1 13.3 14.1 14.2 14.4 14.5',
 't142.tsv': '2.5 2.6 3.2 5.4 7.4 7.7 9.9 9.10 10.5 10.6 10.9 11.7 15.8 15.12 16.1 16.5 16.8 17.2 18.11 19.1 20.5 21.2 21.4 '
             '22.4 22.5 23.12 23.13 23.14 26.7 26.8 26.10 27.2 28.9 29.2 29.3 29.4 29.10 30.1 30.2 31.3 31.8 35.2 36.8',
}
tot = rd = 0
for f, u in UNREAD.items():
    u = set(u.split())
    t = r = w = wr = 0
    for row in csv.DictReader(open(f, encoding='utf-8'), delimiter='\t'):
        if row['kind'] != 'C' or not row['text'].strip():
            continue
        n = len(merge(row['text'].split()))
        k = f"{row['line']}.{row['pos']}"
        t += n; w += 1
        if k not in u:
            r += n; wr += 1
    print(f'{f}: {wr}/{w} cipher words, {r}/{t} signs read = {r / t:.1%}')
    tot += t; rd += r
if __name__ == '__main__': print(f'both: {rd}/{tot} signs = {rd / tot:.1%}')
