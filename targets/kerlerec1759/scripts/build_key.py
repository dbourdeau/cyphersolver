"""Build the manuscript key from the clerk's pairs, compare it with Pusch 2008 Table 2, and merge.
Usage: python3 -I build_key.py <pairs.tsv> <pusch_table.tsv> <outdir>
Writes: key_manuscript.tsv, key_merged.tsv, compare_pusch.tsv, compare_summary.txt"""
import csv, os, sys
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kcommon import load_table, norm

pairs = list(csv.DictReader(open(sys.argv[1], encoding='utf-8'), delimiter='\t'))
pusch = load_table(sys.argv[2])
pusch_raw = {}
for l in open(sys.argv[2], encoding='utf-8'):
    c, v = l.rstrip('\n').split('\t')[:2]
    pusch_raw[int(c)] = v
out = sys.argv[3]

ms = defaultdict(list)  # code -> [(plain, loc)]
for r in pairs:
    if not r['code'] or r['how'] == 'empty' or not r['clerk_plain']:
        continue
    loc = '%s %s l.%s g.%s' % (r['despatch'][:5], r['folio'], r['line'], r['pos'])
    ms[int(r['code'])].append((r['clerk_plain'], loc))
    if r['top']:
        ms[int(r['top'])].append((r['clerk_plain'], loc + ' (upper homophone)'))


def spelling_variant(a, b):
    """True when two readings differ only as period spelling does (present/presen, quoi/quoy, traite/traitte)."""
    if a == b:
        return True
    a2, b2 = a.replace('y', 'i'), b.replace('y', 'i')
    if a2 == b2:
        return True
    import difflib
    return difflib.SequenceMatcher(None, a, b).ratio() >= 0.8 and abs(len(a) - len(b)) <= 2


mkey = {}
rows = []
agree = conflict = variant = only_m = 0
for c in sorted(ms):
    cnt = Counter(p for p, _ in ms[c])
    # most frequent clerk reading; on a tie prefer the one Pusch also has
    val = max(cnt, key=lambda v: (cnt[v], v in pusch.get(c, [])))
    mkey[c] = val
    locs = '; '.join(l for _, l in ms[c][:3])
    if c in pusch:
        if val in pusch[c]:
            st = 'agree' if len(cnt) == 1 else 'agree (another pair differs)'; agree += 1
        elif any(spelling_variant(val, p) for p in pusch[c]):
            st = 'spelling variant'; variant += 1
        else:
            st = 'conflict'; conflict += 1
    else:
        st = 'only in manuscript pairs'; only_m += 1
    rows.append((c, val, len(ms[c]), dict(cnt), pusch_raw.get(c, ''), st, locs))

with open(os.path.join(out, 'key_manuscript.tsv'), 'w', encoding='utf-8') as f:
    f.write('code\tclerk_value\tn_pairs\tall_readings\tpusch_value\tstatus\tfirst_locations\n')
    for r in rows:
        f.write('\t'.join(str(x) for x in r) + '\n')

# merged key: manuscript value when it agrees, is a spelling variant (keep the manuscript spelling), or the code is
# absent from Pusch; on a substantive conflict keep Pusch's value unless the manuscript reading occurs >= 2 times
# with no pair supporting Pusch; codes only in Pusch are taken from Pusch and marked 'P'.
merged = {}
src = {}
for c, val, n, cnt, pv, st, _ in rows:
    if st in ('agree', 'spelling variant', 'only in manuscript pairs'):
        merged[c] = val; src[c] = 'M' if st == 'only in manuscript pairs' else 'M+P'
    else:
        if n >= 2 and not any(v in pusch[c] for v in cnt):
            merged[c] = val; src[c] = 'M (conflicts with P)'
        else:
            merged[c] = pusch[c][0]; src[c] = 'P (one manuscript pair differs)'
for c in pusch:
    if c not in merged:
        merged[c] = pusch[c][0] if '?' not in pusch_raw[c] else norm(pusch_raw[c].replace('?', 'e'))
        src[c] = 'P'
with open(os.path.join(out, 'key_merged.tsv'), 'w', encoding='utf-8') as f:
    f.write('# Kerlerec 1755-62 nomenclator, code -> plaintext (normalised: lower case, no accents).\n')
    f.write('# source: M = from the clerk\'s interlinear decipherments transcribed here (pairs/pairs_build.tsv);\n')
    f.write('#         M+P = also so in Pusch 2008 Table 2; P = Pusch 2008 Table 2 only (Louisiana History 49:477-480).\n')
    for c in sorted(merged):
        f.write('%d\t%s\t%s\n' % (c, merged[c], src[c]))

only_p = sorted(set(pusch) - set(ms))
summ = ['codes with manuscript pairs: %d (from %d pair rows)' % (len(ms), sum(len(v) for v in ms.values())),
        'agree with Pusch: %d' % agree, 'spelling variants of Pusch: %d' % variant,
        'substantive conflicts with Pusch: %d' % conflict, 'only in manuscript pairs (not in Pusch): %d' % only_m,
        'only in Pusch (no manuscript pair here): %d' % len(only_p),
        'merged key size: %d' % len(merged)]
open(os.path.join(out, 'compare_summary.txt'), 'w').write('\n'.join(summ) + '\n')
with open(os.path.join(out, 'compare_pusch.tsv'), 'w', encoding='utf-8') as f:
    f.write('code\tclerk_value\tn_pairs\tpusch\tstatus\n')
    for r in rows:
        if r[5] != 'agree' and r[5] != 'agree (another pair differs)' or len(r[3]) > 1:
            f.write('%s\t%s\t%s\t%s\t%s\n' % (r[0], r[1], r[2], r[4], r[5]))
print('\n'.join(summ))
