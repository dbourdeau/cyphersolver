"""Build docs/reveal/rota1624.json from transcription.txt and the key in decode.py (lines 4-20 of the letter)."""
import io, json, os, re
d = os.path.dirname(os.path.abspath(__file__))
L = {'10':'a','90':'e','30':'i','40':'o','50':'u','21':'f','22':'r','31':'b','32':'n','41':'c','51':'g',
     '71':'h','81':'l','91':'m','92':'t','94':'s','20':'n','70':'o'}
UNC = {'20', '70'}
S = {'q':'che','t':'non','p':'per','&':'et',"p'":'però'}
lines = [l for l in io.open(os.path.join(d, 'transcription.txt'), encoding='utf-8') if not l.startswith('#')]
toks = []; pfx = False
for line in lines[4:21]:
    for t in line.split():
        m = re.fullmatch(r"(\d\d)(['^]?)", t); s = re.fullmatch(r"\{(.+)\}", t)
        if m:
            g, mark = m.groups()
            if mark or pfx or g == '64': toks.append({'g': g + ("'" if mark == "'" else ''), 'p': '?', 'cls': 'unk'})
            elif g in L: toks.append({'g': g, 'p': L[g], **({'cls': 'unc'} if g in UNC else {})})
            else: toks.append({'g': g, 'p': '?', 'cls': 'unk'})
        elif s:
            k = s.group(1)
            if k in S: toks.append({'g': k, 'p': S[k], 'cls': 'code'})
            elif k == 'z': toks.append({'g': 'z', 'p': 'se', 'cls': 'unc'})
            else: toks.append({'g': k, 'p': '?', 'cls': 'unk'})
        else: toks.append({'g': '', 'p': t, 'cls': 'plain'})
        pfx = t in ('{g}', '{c}', '{m}')
out = {'slug': 'rota1624', 'anchor': 'the-key',
       'title': 'Lines 4 to 20 of the letter, decoded with the letter key',
       'caption': 'Each two-digit number is one letter; clear words are shown as written. Question marks are code numbers (ticked, or after g, c, m), numbers with no value and single signs that were not read. 20 as n, 70 as o and z as se are plausible only.',
       'unit': 'groups', 'key_note': 'key.tsv', 'tokens': toks}
io.open(os.path.join(d, '..', '..', 'docs', 'reveal', 'rota1624.json'), 'w', encoding='utf-8', newline='\n').write(json.dumps(out, ensure_ascii=False, indent=1) + '\n')
print(len(toks), sum(1 for t in toks if t['g']))
