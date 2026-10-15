"""R9325 (BayHStA KAA 4591 f.129) with key R9324, from r9325/reading.txt (written 15 Oct 2026 when the entry was split
from kaa4591). Decodes each cipher line of the transcription with the key alphabet of NOTES.md and compares it with
the plain column; writes r9325/signs.txt (one sign per token, for docs/_check_profile.py --measure) and
docs/reveal/fulda1576.json (the whole note, sign by sign).

Transcription codes (header of reading.txt): x=a t=b o=c p=d z=e k=f y=g n=h a=i L=l d=m i=n c=o D=p Q=q R=r S=s T=t
w=u X=x; C=cc, Y=ss, v=bb; {..} a nomenclator code of R9324; [..] and g nulls; 7 the Tironian et written in clear."""
import io, os, re, json
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(H))
KEY = dict(x='a', t='b', o='c', p='d', z='e', k='f', y='g', n='h', a='i', L='l', d='m', i='n', c='o', D='p', Q='q',
           R='r', S='s', T='t', w='u', X='x', C='cc', Y='ss', v='bb')
lines = []
for l in io.open(os.path.join(H, 'r9325', 'reading.txt'), encoding='utf8'):
    m = re.match(r'(\d+) (.*?)\s{2,}(\S.*)$', l.rstrip('\n'))
    if m:
        lines.append((int(m.group(1)), m.group(2), m.group(3)))
signs, toks, mism = [], [], 0
for no, ct, pt in lines:
    ct = ct.replace('Dciz? -> ', '')          # line 4: the transcriber's first reading, corrected to siwz
    pw = [re.sub(r'\(.*?\)', '', w) for w in pt.replace('.', ' ').split()]
    words, cur = [], []
    for t in re.findall(r'\{[^}]*\}|\[[^\]]*\]|\s+|\S', ct):
        if t.isspace():
            if cur: words.append(cur); cur = []
        elif t != '?':
            cur.append(t)
    if cur: words.append(cur)
    wi = 0
    for w in words:
        if len(w) == 1 and (w[0].startswith('[') or w[0] == 'g'):
            signs.append(w[0].strip('[]')); toks.append({'g': w[0].strip('[]'), 'p': '', 'cls': 'null'}); continue
        target = pw[wi] if wi < len(pw) else ''
        wi += 1
        if len(w) == 1 and w[0].startswith('{'):
            signs.append('#' + w[0][1:-1].replace(' ', '_'))
            toks.append({'g': w[0][1:-1], 'p': w[0][1:-1], 'cls': 'code'})
            parts = w[0][1:-1].split()
            if len(parts) > 1 and wi < len(pw) and pw[wi].lower().startswith(parts[1][:3].lower()):
                wi += 1                            # a two-word name in the plain column (Consiliarii Caesaris)
        else:
            dec = ''
            for t in w:
                if t.startswith('[') or t == 'g':
                    signs.append(t.strip('[]')); toks.append({'g': t.strip('[]'), 'p': '', 'cls': 'null'}); continue
                if t == '7':
                    toks.append({'g': '', 'p': 'et', 'cls': 'plain'}); continue
                v = KEY.get(t, '?')
                signs.append(t)
                tok = {'g': t, 'p': v, 'cls': '' if t in KEY else 'unk'}
                if t in KEY and target[len(dec):len(dec) + len(v)].lower() != v:
                    tok['cls'] = 'unc'; mism += 1
                dec += v
                toks.append(tok)
        toks.append({'g': '', 'p': ' ', 'cls': 'plain'})
print('signs differing from the plain column:', mism)
io.open(os.path.join(H, 'r9325', 'signs.txt'), 'w', encoding='utf8').write(' '.join(signs) + '\n')
while toks and toks[-1]['p'] == ' ':
    toks.pop()
out = {
 'slug': 'fulda1576',
 'anchor': 'reading',
 'title': 'The Fulda note of 1576, deciphered with key R9324',
 'caption': 'The whole of R9325 (BayHStA Kurbayern Äußeres Archiv 4591 f. 129), sign by sign with the key filed a few leaves earlier (R9324, ff. 124–127): “Protestatus abbas secreto coactum ad litem acceptare Pontificis inhibitionem …”. Names and offices are single nomenclator signs of the key; small marks between words are nulls. The writer\'s slips are kept: “secrto”, “iuxilio”, “uoluid”.',
 'unit': 'signs',
 'key_note': 'One sign per letter, signs for doubled letters (cc, ss), several nulls, and a nomenclator of the Fulda affair. Signs are shown as the transcription codes of r9325/reading.txt.',
 'tokens': toks,
}
json.dump(out, io.open(os.path.join(ROOT, 'docs', 'reveal', 'fulda1576.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(signs), 'signs')
print(''.join(t['p'] if t['cls'] != 'code' else '{' + t['p'] + '}' for t in toks))
