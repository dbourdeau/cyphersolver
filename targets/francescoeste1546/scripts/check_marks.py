"""Check reading_marked_c42r.txt against transcription_c42r.txt and key_c42r.tsv. Exit 1 on any unmarked departure.
- the units of each line, joined, must give exactly the signs of the transcription line (in order);
- unit=x must have x among the unit's key values seen at least twice, and must not rest on a doubtful sign;
- {unit=x} (value seen once or not in the key), {?unit=x} (doubtful sign), {+x} (no sign) and [unit?] are marks.
- the letters of each line, joined in order, must equal the letters of that line in clear_c42r.txt (so a letter of the
  clear cannot be dropped, added or changed silently).
Counts words of the clear (between |) as verbatim (no mark), marked (some mark), and runs of [unit?] as unread groups.
Also prints the held-out result written by scripts/read42r.py."""
import re, sys, collections, pathlib
R = pathlib.Path(__file__).resolve().parent.parent
key = {}
for l in (R / 'key_c42r.tsv').read_text(encoding='utf8').splitlines():
    if l.startswith('#') or l.startswith('unit\t'): continue
    u, v = l.split('\t')[:2]
    key[u.replace(' ', '_')] = {x.split(':')[0] for x in v.split() if int(x.split(':')[1]) >= 2}
C = {l.split('	')[0]: re.sub(r'[^a-z]', '', l.split('	')[1].lower()) for l in (R / 'clear_c42r.txt').read_text(encoding='utf8').splitlines() if l.startswith('c0')}
T = {l.split('\t')[0]: l.split('\t')[1].split() for l in (R / 'transcription_c42r.txt').read_text(encoding='utf8').splitlines() if l.startswith('c0')}
bad = []; W = collections.Counter()
for l in (R / 'reading_marked_c42r.txt').read_text(encoding='utf8').splitlines():
    if not l.startswith('c0'): continue
    n, t = l.split('\t'); signs = T[n]; i = 0
    words = [[]]; got = ''
    for tok in t.split():
        if tok == '|': words.append([]); continue
        if tok.startswith('{+') and '=' not in tok: words[-1].append('m'); got += tok[2:-1]; continue
        mu = re.fullmatch(r'\[(.+)\?\]', tok)
        if mu:
            u = mu[1]; kind = 'u'
        else:
            body = tok.strip('{}'); kind = 'm' if tok.startswith('{') else 'p'
            if body.startswith('?'): body = body[1:]; kind = 'd'
            u, _, x = body.partition('='); got += x
        parts = u.split('_'); seg = signs[i:i + len(parts)]; i += len(parts)
        if [s.rstrip('?') for s in seg] != parts: bad.append(f'{n}: unit {u} does not match signs {seg}'); continue
        dq = any(s.endswith('?') for s in seg)
        if kind == 'p':
            if x not in key.get(u, ()): bad.append(f'{n}: unmarked departure {u}={x} (key: {sorted(key.get(u, ()))})')
            if dq: bad.append(f'{n}: {u}={x} rests on a doubtful sign without {{?}}')
        if kind == 'd' and not dq: bad.append(f'{n}: {{?{u}}} but the sign is not doubtful')
        words[-1].append(kind)
    if got != C.get(n, ''): bad.append(f'{n}: letters of the reading "{got}" differ from the clear "{C.get(n, "")}"')
    if i != len(signs): bad.append(f'{n}: {len(signs) - i} signs not covered')
    for w in words:
        if not w: continue
        core = [k for k in w if k != 'u']
        if core: W['verbatim' if all(k == 'p' for k in core) else 'marked'] += 1
    W['unread_groups'] += len(re.findall(r'(?:\[\S+\?\]\s*)+', t))
for b in bad: print('FAIL', b)
print('clear words carried by the cipher:', W['verbatim'] + W['marked'], f"(verbatim {W['verbatim']}, with a marked sign {W['marked']}); "
      f"runs of signs not covered by the clear: {W['unread_groups']}")
print((R / 'validation' / 'heldout_c42r.txt').read_text(encoding='utf8').strip())
sys.exit(1 if bad else 0)
