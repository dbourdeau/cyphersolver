"""Post-decode diagnosis only (does not change the figure of record): word-level diff of DECODE.txt against the clear
references, listing every decoded word that differs from its clear word."""
import re, difflib
D = '/home/claude/keyless/round40c/basel_anv9/'
def norm(s):
    s = re.sub(r'\[[^\]]*\]', lambda m: m.group(0)[1:-1], s).lower().replace('j', 'i').replace('v', 'u').replace('y', 'i')
    return re.sub('[^a-z? ]', ' ', s).split()
def dec(prefix):
    t = ''
    for ln in open(D + 'DECODE.txt'):
        if ln.startswith('#') or not ln.strip(): continue
        k, x = ln.rstrip('\n').split('\t')
        if k.startswith(prefix + ' '): t += x + ' '
    return norm(t.replace('= ', ''))
def clear(f, keyed):
    t = ''
    for ln in open(D + f):
        if ln.startswith('#') or not ln.strip(): continue
        t += (ln.rstrip('\n').split('\t')[-1] if keyed else ln) + ' '
    return norm(t)
out = []
for h, f, keyed in (('H1', 'score/CLEAR_H1_f109v.txt', False), ('H2', 'score/CLEAR_H2_f167r.txt', True), ('H3', 'score/CLEAR_H3_f123r.txt', True)):
    a, b = dec(h), clear(f, keyed)
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    same = sum(bl.size for bl in sm.get_matching_blocks())
    out.append('## %s: decoded words %d, clear words %d, identical words in order %d (%.1f%% of clear words)' % (h, len(a), len(b), same, 100.0 * same / len(b)))
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != 'equal':
            out.append('  %-8s decode: %-40s clear: %s' % (op, ' '.join(a[i1:i2]), ' '.join(b[j1:j2])))
print('\n'.join(out)); open(D + 'score/worddiff_out.txt', 'w').write('\n'.join(out) + '\n')
