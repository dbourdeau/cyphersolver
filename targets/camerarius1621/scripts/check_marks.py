#!/usr/bin/env python3
"""Rebuild the decryption of one letter from its transcription and key.tsv; check every mark; count words.

    python scripts/check_marks.py n194            writes n194/decryption_n194.txt, prints counts, exit 1 on any failure

Inputs in <doc>/: transcription_<doc>.txt (lines "NN text", code groups as digits with a dot) and code_groups_<doc>.tsv
(seq, scan, line, pass1, pass2, gloss, context, reading). Rules, each a failure:
  - the code groups found in the transcription, in order and by line, must be exactly those of code_groups_<doc>.tsv;
  - pass1 and pass2 must agree;
  - an unmarked reading must equal the value in key.tsv, and that value must not have status 'doubt';
  - a group missing from the key, with a 'doubt' key value, or with a doubtful sign (note in context) must be marked [?..];
  - a mark must sit on a real doubt (key doubt or missing, doubtful sign, or no legible gloss on the page).
Counts: clear-text words (marked [?..], [...] or [slip] = not read), code groups (marked = not read), total.
Standard library only."""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
doc = sys.argv[1]
D = ROOT / doc


def tsv(path):
    for l in path.read_text(encoding='utf8').splitlines():
        if l and not l.startswith('#') and not l.startswith(('seq\t', 'group\t')):
            yield l.split('\t')


key = {f[0]: (f[1], f[2]) for f in tsv(ROOT / 'key.tsv')}
groups = list(tsv(D / f'code_groups_{doc}.tsv'))
lines = [l for l in (D / f'transcription_{doc}.txt').read_text(encoding='utf8').splitlines()
         if re.match(r'^\d+ ', l)]
GROUP = re.compile(r'(?<![\d\w])(\d{2,4})\.')   # a code group: 2-4 digits followed by a dot
DATE = re.compile(r'\b(1622|1621|100m)\b')
fail = []
found = []
for l in lines:
    n, text = l.split(' ', 1)
    for m in GROUP.finditer(text):
        if DATE.fullmatch(m.group(1)) or re.search(r'\d+\.\s*(Maij|Junij)', text[m.start():m.start() + 12]):
            continue
        found.append((int(n), m.group(1)))
exp = [(int(g[2]), g[3]) for g in groups]
if found != exp:
    fail.append(f'code groups in transcription {len(found)} vs table {len(exp)}; first difference at '
                f'{next((i for i, (a, b) in enumerate(zip(found, exp)) if a != b), min(len(found), len(exp)))}')
read_g = 0
val = {}
for g in groups:
    seq, scan, line, p1, p2, gloss, ctx, r = g[:8]
    if p1 != p2:
        fail.append(f'{seq}: passes differ {p1}/{p2}')
    kv, ks = key.get(p1, (None, None))
    sign_doubt = 'slip' in ctx or 'possibly' in ctx
    if r.startswith('[?'):
        if not (kv is None or ks == 'doubt' or sign_doubt or gloss.strip() in ('-', '?') or gloss.startswith('?')):
            fail.append(f'{seq}: mark on {p1} with a clear key value, clear sign and legible gloss')
    else:
        read_g += 1
        if kv is None:
            fail.append(f'{seq}: {p1} not in key, reading unmarked')
        elif r != kv:
            fail.append(f'{seq}: unmarked departure: {p1} reads "{r}", key "{kv}"')
        elif ks == 'doubt':
            fail.append(f'{seq}: key value of {p1} is doubtful, reading unmarked')
        if sign_doubt:
            fail.append(f'{seq}: doubtful sign {p1}, reading unmarked')
    val.setdefault(int(line), []).append((p1, r))
# decryption: replace groups in order on each line
out = [f'# decryption of transcription_{doc}.txt with key.tsv (built by scripts/check_marks.py). <group=value>; [?x] = not read']
words = unread_w = 0
for l in lines:
    n, text = l.split(' ', 1)
    q = list(val.get(int(n), []))
    def rep(m):
        if DATE.fullmatch(m.group(1)) or not q or q[0][0] != m.group(1):
            return m.group(0)
        g, r = q.pop(0)
        return f'<{g}={r}>'
    out.append(f'{n} ' + GROUP.sub(rep, text))
    clear = GROUP.sub(' ', re.sub(r'\[\?[^\]]*\]|\[\.\.\.\]|\[slip\][^\s]*', ' X ', text))
    toks = [t for t in re.split(r'\s+', clear) if re.search(r'[A-Za-zÄÖÜäöüß]', t) or t == 'X']
    words += len(toks)
    unread_w += sum(1 for t in toks if t == 'X')
(D / f'decryption_{doc}.txt').write_text('\n'.join(out) + '\n', encoding='utf8', newline='\n')
ng = len(groups)
tot, ok = words + ng, (words - unread_w) + read_g
print(f'{doc}: clear-text words {words}, not read {unread_w}; code groups {ng}, read {read_g}; '
      f'all tokens {tot}, read {ok} ({100 * ok / tot:.1f}%)')
for x in fail:
    print('FAIL', x)
print('result:', 'ok' if not fail else 'FAIL')
sys.exit(1 if fail else 0)
