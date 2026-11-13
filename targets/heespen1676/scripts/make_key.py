"""Build key.tsv and gloss/attestations_by_code.tsv from the frozen key and gloss-pair files (own code, standard library).
usage: python3 -I make_key.py <folder>
key.tsv: one row per single code in KEY_HB_v1 or KEY_HB_v2, with both values, their attestation counts, conflicts, and the
provenance of every value as gloss references (unit 262098, image number, page side L/R, line strip). Every value in both keys
comes from the chancery's interlinear gloss; none is from context or built from ciphertext. Phrase rows are not included
(they are not used by the decoder). The last column counts the code's tokens in the 537L transcription.
attestations_by_code.tsv: every gloss pair that names a single-code value, grouped by code, with the gloss word written over it."""
import sys, collections, pathlib, re
d = pathlib.Path(sys.argv[1])
def key(p):
    rows = {}
    for ln in open(p, encoding='utf-8'):
        if ln.startswith('#') or not ln.strip(): continue
        f = ln.rstrip('\n').split('\t')
        if f[0] in ('tok', 'tie'): rows[f[1]] = f
    return rows
k1, k2 = key(d / 'gloss/KEY_HB_v1.tsv'), key(d / 'gloss/KEY_HB_v2.tsv')
tx = [ln.split() for ln in open(d / 'transcriptions/heespen_1676-04-17_537L.txt', encoding='utf-8') if ln.strip() and not re.search(r'[a-z]{4,}', ln)]  # same line rule as decode.py: the margin line starts with the token '#'
n537 = collections.Counter(t for l in tx for t in l)
def ref(r):
    return f'img {r[:3].lstrip("0")} {"left" if r[3] == "L" else "right"} line {r[4:]}'
def sortkey(c):
    return (0, int(c)) if c.isdigit() else (1, c)
out = ['#code\tv1_value\tv1_attest\tv2_value\tv2_attest\tv2_status\tconflicts_v2\tbasis\tprovenance_v2 (Rigsarkivet unit 262098; image, side, line)\ttokens_in_537L']
for c in sorted(set(k1) | set(k2), key=sortkey):
    a, b = k1.get(c), k2.get(c)
    st = 'valued' if b and b[0] == 'tok' else ('tie, left unvalued' if b else 'absent')
    prov = '; '.join(ref(r) for r in b[5].split(',')) if b and b[5] != '-' else (('v1 only: ' + '; '.join(ref(r) for r in a[5].split(','))) if a else '-')
    out.append('\t'.join([c, a[2] if a else '-', a[3] if a else '-', b[2] if b else '-', b[3] if b else '-', st,
                          b[4] if b else '-', 'gloss', prov, str(n537.get(c, 0))]))
(d / 'key.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
att = collections.defaultdict(list)
for ln in open(d / 'gloss/gloss_pairs_v2_all.tsv', encoding='utf-8'):
    if ln.startswith('#') or not ln.strip(): continue
    f = ln.rstrip('\n').split('\t')
    if len(f) < 4: continue
    for seg in f[3].split(';'):
        if '=' in seg:
            c, v = seg.split('=', 1); att[c.strip()].append((f[0], v.strip(), f[2], f[1]))
lines = ['#code\tvalue_attested\timage_side_line\tgloss_word\tgroup_tokens\tagrees_with_v2']
nconf = 0
for c in sorted(att, key=sortkey):
    for img, v, w, toks in att[c]:
        v2 = k2.get(c)
        ok = 'yes' if v2 and v2[0] == 'tok' and v2[2] == v else ('tie' if v2 and v2[0] == 'tie' else 'NO')
        nconf += ok != 'yes'
        lines.append('\t'.join([c, v, img, w, toks, ok]))
(d / 'gloss/attestations_by_code.tsv').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(f'key.tsv: {len(out) - 1} codes (v1 {len(k1)}, v2 {len(k2)}); attestations {len(lines) - 1}, not agreeing with v2 value {nconf}')
