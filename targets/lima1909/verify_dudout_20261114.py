"""lima1909: independent check (Brice Dudout, Claude Opus 5.5, 14 Nov 2026).

Part 1 reads ONLY code_values.tsv and the m*_transcription.txt files: it extracts the code groups of each telegram,
looks each up in code_values.tsv, and compares group by group with the group column of m*_decryption.txt
(the published group-by-group decode), then compares the looked-up value with the gloss given there.
Part 2 counts, in each m*_reading.md, the bracket marks that the read-bar script (v10_relabel.share) turns into holes,
and splits them into open/doubtful items ([?], "[x?]", "?") and editorial supplements (articles or prepositions
supplied by the editor, expansions of abbreviations such as P[residente da]), which are not unread code.

    python3 verify_dudout_20261114.py [target_dir]
"""
import re, sys, pathlib

T = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
DOCS = ['m0001', 'm0005', 'm0007', 'm0009', 'm0011', 'm0014', 'm0018', 'm0020']

# --- the key: group -> list of values
key = {}
for line in (T / 'code_values.tsv').read_text(encoding='utf8').splitlines()[1:]:
    f = line.split('\t')
    key[f[0]] = [v.strip() for v in f[1].split('|')]



def groups_of_transcription(p):
    out = []
    for line in p.read_text(encoding='utf8').splitlines():
        if line.startswith('#'): continue
        for tok in re.split(r'[\s=]+', line):
            tok = tok.strip('.,-+')
            if re.fullmatch(r'\d{2,6}\?*', tok): out.append(tok)
    return out


def groups_of_decryption(p):
    out = []
    for line in p.read_text(encoding='utf8').splitlines():
        if line.startswith('#') or line.startswith('(clear)') or not line.strip(): continue
        g, _, rest = line.partition(' ')
        out.append((g, rest.strip()))
    return out


def norm(s):
    s = s.split('   ')[0]   # drop the notes column
    s = re.sub(r'\[[^\]]*\]', '', s).replace('?', '').strip().lower()
    return s.strip('- ')

tot = agree = 0
print('PART 1  transcription + code_values.tsv  vs  m*_decryption.txt')
for d in DOCS:
    tg = groups_of_transcription(T / f'{d}_transcription.txt')
    dg = groups_of_decryption(T / f'{d}_decryption.txt')
    issues = []
    if len(tg) != len(dg): issues.append(f'count {len(tg)} vs {len(dg)}')
    for i, (a, (b, gloss)) in enumerate(zip(tg, dg)):
        if a.rstrip('?') != b.rstrip('?'):
            issues.append(f'#{i+1} transcription {a} / decryption {b}')
            continue
        vals = key.get(a.rstrip('?')) or key.get(a)
        if vals is None: issues.append(f'#{i+1} {a} not in code_values.tsv'); continue
        g = norm(gloss)
        ok = any(norm(v) and (norm(v) == g or norm(v).replace(' ', '') == g.replace(' ', '')) for v in vals) \
            or (g == '' and any('[' in v for v in vals))
        tot += 1; agree += ok
        if not ok: issues.append(f'#{i+1} {a}: key {vals} / decryption "{gloss}"')
    print(f'{d}: {len(tg)} groups in transcription, {len(dg)} in decryption; ' + ('agree' if not issues else '; '.join(issues)))
print(f'value agreement: {agree}/{tot}\n')

print('PART 2  bracket marks in m*_reading.md')
try:   # optional: the repository's read-bar script (needs numpy; run from inside the repository clone)
    ROOT = T.resolve().parents[1]
    sys.path[:0] = [str(ROOT / 'research' / 'reading_audit'), str(ROOT / 'docs')]
    import os; cwd = os.getcwd(); os.chdir(ROOT)
    import v10_relabel
    os.chdir(cwd)
    def share(text):
        w, h, d = v10_relabel.share(text); return w, h, d, round(1 - (h + d) / (w + h), 3)
except Exception as e:
    print('(v10_relabel not loaded:', e, ')'); share = None
for d in DOCS:
    body = '\n'.join(l for l in (T / f'{d}_reading.md').read_text(encoding='utf8').splitlines() if not l.startswith('#'))
    marks = re.findall(r'\w*\[[^\]]*\]\w*', body)
    openm = [m for m in marks if '?' in m]
    edit = [m for m in marks if '?' not in m]
    doubt = re.findall(r'\(\?\)', body)
    print(f'{d}: open or doubtful {len(openm)} {openm}; editorial supplements {len(edit)} {edit}')
    if share:
        w, h, dd, rs = share(body)
        # same body with the editorial supplements unbracketed (abbreviation expansions) or dropped (supplied words)
        adj = re.sub(r'(\w+)\[([^\]?]*)\]', r'\1\2', body)                      # P[residente da] -> Presidente da
        adj = re.sub(r'\[([^\]?]*)\](\w*)', lambda m: m.group(1) + m.group(2) if m.group(2) else ' ', adj)
        w2, h2, d2, rs2 = share(adj)
        print(f'      v10 as published {rs} ({w} words, {h} holes, {dd} doubtful); '
              f'editorial supplements not counted {rs2} ({w2} words, {h2} holes, {d2} doubtful)')
