"""After the measure: align the 1553 decode (key.tsv, our ARB) to the enclosure, word by word (post hoc, for the reading).
A word is SURE when the decoded letters equal the enclosure word under the project's spelling fold (compare_readings.py
norm: v=u, y=i, j=i, z=c, x=s, h dropped, doubled letters single); the word is then written in the CIPHER's spelling; otherwise the
enclosure's word is shown [restored] and our decoded letters are given beside it. Holes '?' in the decode are never sure."""
import difflib, importlib.util, re, sys, json
from pathlib import Path
REPO, WORK = Path(sys.argv[1]), Path(sys.argv[2])
spec = importlib.util.spec_from_file_location('m', WORK / 'mesure_c09.py'); 
sys.argv = [sys.argv[0], str(REPO), str(WORK)]
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
key, cw = m.load_key(), m.load_crosswalk()
seq = m.labels_of(m.read_arb('1553'), cw)
segs = [[x for x in seq if m.para_of(x[0]) == i] for i in range(6)]
body = (REPO / 'beling_march1553/spanish_enclosure.txt').read_text(encoding='utf8').split('[37r]\n')[1].replace('[37v]', '').replace('[38r]', '')
chunks = [s.strip() for s in re.split(r'\n\s*\n', body) if s.strip()]
paras = [chunks[0], chunks[1], chunks[2] + ' ' + chunks[3], chunks[4] + ' ' + chunks[5], chunks[6], chunks[7]]
out, stats = [], {'sure': 0, 'restored': 0, 'words': 0, 'chars_sure': 0}
for i, (sg, ref) in enumerate(zip(segs, paras)):
    dec = ''.join('?' if w is None else '' if w == '' else key.get(w, '?') for _, w in sg)
    dec = dec.replace('?', '#')
    words = [w for w in re.findall(r"[^\s,.;:()]+", ref)]
    nw = [m.norm(re.sub(r'\[\?\]|\[|\]', '', w)) for w in words]
    def fold(t):
        t = t.replace('v', 'u').replace('y', 'i').replace('j', 'i').replace('z', 'c').replace('x', 's').replace('h', '')
        return re.sub(r'(.)\1', r'\1', t)
    nw = [fold(n) for n in nw]
    refs = ''.join(nw)
    dec_raw = dec
    dmap = [k for k, ch in enumerate(dec_raw)]
    folded, back = '', []
    prev = ''
    for k, ch in enumerate(dec_raw):
        c = {'v': 'u', 'y': 'i', 'j': 'i', 'z': 'c', 'x': 's'}.get(ch, ch)
        if c == 'h' or c == prev:
            continue
        folded += c; back.append(k); prev = c
    dec = folded
    sm = difflib.SequenceMatcher(None, refs, dec, autojunk=False)
    mp = {}
    for a, b, n in sm.get_matching_blocks():
        for k in range(n): mp[a + k] = b + k
    pos, line = 0, []
    for w, n in zip(words, nw):
        if not n: continue
        ok = all((pos + k) in mp for k in range(len(n)))
        if ok:  # contiguous?
            idx = [mp[pos + k] for k in range(len(n))]
            ok = idx == list(range(idx[0], idx[0] + len(n)))
        stats['words'] += 1
        if ok:
            a0, a1 = back[idx[0]], back[idx[-1]] + 1
            if a0 > 0 and dec_raw[a0 - 1] == 'h' and m.norm(w).startswith('h'):
                a0 -= 1
            while a1 < len(dec_raw) and dec_raw[a1] == dec_raw[a1 - 1] and m.norm(w)[-2:] == dec_raw[a1 - 1] * 2:
                a1 += 1
            stats['sure'] += 1; stats['chars_sure'] += len(n); line.append(dec_raw[a0:a1])
        else:
            stats['restored'] += 1; line.append('[' + w + ']')
        pos += len(n)
    out.append(f'¶{i+1}: ' + ' '.join(line))
    out.append(f'   decode: {dec_raw}')
stats['share_sure'] = round(stats['sure'] / stats['words'], 4)
(WORK / 'lecture_1553_auto.txt').write_text('\n'.join(out) + '\n', encoding='utf8')
print(json.dumps(stats))
