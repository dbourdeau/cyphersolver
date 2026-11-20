"""Reconcile readers A and B, including their prose qualifications."""
import csv
import re
from collections import Counter
from pathlib import Path

out = Path(__file__).resolve().parent
qualifications_a = {
    ("A01", 1): "618 or 678",
    ("A08", 9): "tentative",
    ("A09", 8): "tentative",
    ("A10", 15): "possible overwrite",
    ("B03", 15): "uncertain, heavy ink",
    ("B06", 1): "880 or 980",
}


def parse(path):
    lines = {}
    for line in path.read_text().splitlines():
        match = re.fullmatch(r'([abAB])(\d+) (.*)', line)
        if not match:
            continue
        label = match[1].upper() + match[2].zfill(2)
        row = []
        for value in match[3].split():
            if value == '—':
                row[-1] += '~'
            else:
                row.append(value.replace('^', ''))
        lines[label] = row
    return lines


a, b = [parse(out.parent / f"vienna_reader_{r}.txt") for r in ('a','b')]
assert list(a) == list(b) and len(a) == 21
rows = []
for label in a:
    assert len(a[label]) == len(b[label])
    for idx,(first,second) in enumerate(zip(a[label],b[label]),1):
        read = re.fullmatch(r'(\d+)([o:+v#])(~?)',first)
        assert read
        check = re.fullmatch(r'(.+?)([o:+v#])(~?)',second)
        assert check
        note = qualifications_a.get((label,idx),'')
        num = read[1] if read[1] == check[1] and not note else '?'
        mark = read[2] if read[2] == check[2] else '?'
        stroke = read[3] if read[3] == check[3] else '?'
        key = num + mark + stroke if '?' not in (num,mark,stroke) else '?'
        rows.append([len(rows)+1,label,idx,first,second,note,num,mark,stroke,key])
with (out/'vienna_groups.tsv').open('w') as f:
    writer = csv.writer(f,delimiter='\t',lineterminator='\n')
    writer.writerow(('ordinal','line','position','reader_a','reader_b','a_note','digits','superscript','trailing_stroke','strict_key'))
    writer.writerows(rows)
print('slots',len(rows),'complete',sum(r[-1]!='?' for r in rows),'distinct complete',len(set(r[-1] for r in rows if r[-1]!='?')))
print('by mark',dict(Counter(r[7] for r in rows)))
print('holes',[(r[1],r[2]) for r in rows if r[-1]=='?'])
print('old sample corrected',[(r[2],r[6]) for r in rows[:10]])
