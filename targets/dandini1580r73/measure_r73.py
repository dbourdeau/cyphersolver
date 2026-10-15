"""Measure R73 (14 Oct 2026, one-key split) from George Lasry's decryption file DOC_R72_D3191 (filed on DECODE under
R72, but it is KaJo's R73 transcription of ff. 89r-90r with Lasry's values written under each group).
Unread: '?' (illegible in the transcription), nomenclator groups he left as <NNN^>, and groups he marked NN?.
With --reveal START N it prints a docs/reveal JSON for N groups from token START (Lasry's values, unchanged)."""
import json, re, sys
L = open('decode/DOC_R72_D3191_3191.txt', encoding='utf-8').read().split('\n')
pairs = []
for i, line in enumerate(L[:-1]):
    s = line.strip()
    if s.endswith('|') and re.match(r'^[\d?]', s):
        codes = s.rstrip('|').split()
        # values sit under the codes, aligned by column: split the value line at the code columns
        val = L[i + 1]
        starts = [m.start() for m in re.finditer(r'\S+', line.rstrip('| \n'))]
        for j, c in enumerate(codes):
            a = starts[j]; b = starts[j + 1] if j + 1 < len(starts) else len(val)
            pairs.append((c, val[a:b].replace('|', '').strip()))
total = len(pairs)
unread = [p for p in pairs if p[0] == '?' or p[1].startswith('<') or re.match(r'^\d+\?$', p[1]) or p[1] == '']
if len(sys.argv) > 2 and sys.argv[1] == '--reveal':
    a, n = int(sys.argv[2]), int(sys.argv[3])
    toks = []
    for c, v in pairs[a:a + n]:
        if c == '?': toks.append({'g': '?', 'p': '?', 'cls': 'unk'})
        elif v.startswith('<') or re.match(r'^\d+\?$', v) or not v: toks.append({'g': c, 'p': '?', 'cls': 'unk'})
        elif c.endswith('^'): toks.append({'g': c, 'p': v, 'cls': 'code'})
        else: toks.append({'g': c, 'p': v.replace('u/v', 'u'), 'cls': ''})
    print(json.dumps(toks, ensure_ascii=False))
else:
    print(f'{total} groups; unread {len(unread)} (illegible {sum(1 for p in unread if p[0] == "?")}); '
          f'{total - len(unread)} of {total} have a value ({(total - len(unread)) / total:.1%})')
