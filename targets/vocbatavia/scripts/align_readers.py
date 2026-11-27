"""Align a blind second reader's number groups with the frozen transcription (difflib on number groups only).
Usage: python3 -I align_readers.py <frozen.txt> <reader.txt> <label>"""
import re, sys, difflib
def frozen_groups(path):
    out = []
    for ln in open(path, encoding='utf-8'):
        if ln.startswith('#') or '|' not in ln: continue
        body = ln.split('|', 1)[1]
        body = re.sub(r'\[[^\]]*\]', ' ', body); body = re.sub(r'<[^>]*>', ' ', body)
        out += re.findall(r'\d+', body)
    return out
def reader_groups(path):
    out = []
    for ln in open(path, encoding='utf-8'):
        if not re.match(r'L\d+:', ln): continue
        body = ln.split(':', 1)[1]
        body = re.sub(r'\[[^\]]*\]', ' ', body)
        out += [m.group(0) for m in re.finditer(r'\d+\??', body)]
    return out
fz, rd = frozen_groups(sys.argv[1]), reader_groups(sys.argv[2])
rdc = [x.rstrip('?') for x in rd]
sm = difflib.SequenceMatcher(None, fz, rdc, autojunk=False)
match = sum(b.size for b in sm.get_matching_blocks())
print(f"{sys.argv[3]}: frozen groups {len(fz)}, reader groups {len(rd)} (doubtful '?': {sum(x.endswith('?') for x in rd)})")
print(f"matched {match} of {len(fz)} frozen groups = {match}/{len(fz)} = {100*match/len(fz):.2f}%")
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op != 'equal':
        print(f"  {op}: frozen[{i1}:{i2}] {fz[i1:i2]} <-> reader[{j1}:{j2}] {rd[j1:j2]}")
