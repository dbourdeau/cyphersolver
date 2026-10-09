"""Build reading_r8572.txt from reading_words.txt (hand word division) + the token stream, with the measure on top."""
import re, os, sys, collections
sys.argv = [sys.argv[0]]
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
src = open('decode_r8572.py', encoding='utf-8').read().split("if __name__")[0]
exec(src)
L = dict(load_lines())
ORDER = ['P1', 'P2', 'P7', 'P3', 'P5', 'P4', 'P6', 'P8', 'P9']
FOL = {'P1':'f.214r','P2':'f.214v','P7':'f.215r','P3':'f.215v','P5':'f.216r','P4':'f.216v','P6':'f.217r','P8':'f.217v','P9':'f.218r'}
W = {}
for l in open('reading_words.txt', encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    i, t = l.rstrip('\n').split('\t', 1); W[i] = t

def cipher_tokens(toks):
    out = []
    for t in toks:
        if t.startswith('{') or t.startswith('[del'): continue
        if t.startswith('[above:'): out += t[7:-1].split(); continue
        out.append(t)
    return out

tot = nul = letters = 0; chars = 0
for lid, toks in L.items():
    for t in cipher_tokens(toks):
        u = t.rstrip('?'); tot += 1
        v = KEY.get(u, (None,))[0]
        if v == '': nul += 1
        elif v: letters += 1; chars += len(re.sub(r'<[^>]*>', 'x', v.split('/')[0]))
avg = chars / letters
unread = dub_tok = 0; dub_words = []; UN = []
for lid, w in W.items():
    body = re.sub(r'\{[^}]*\}', '', w)
    ct = set(t.rstrip('?') for t in cipher_tokens(L[lid]))
    for m in re.finditer(r'\[([^\]=]+)\]', body):
        if m.group(1) in ct: unread += 1; UN.append(f'{lid}:{m.group(1)}')
    for m in re.finditer(r"([\w'<>]+)\(\?\)", body):
        wd = re.sub(r'<[^>]*>|\W', '', m.group(1))
        n = max(1, round(len(wd) / avg)); dub_tok += n; dub_words.append(m.group(1))
read = tot - nul - unread - dub_tok
sys.path.insert(0, os.path.join(HERE, '..', '..', '..'))
from lang import lm as _lm
_t = ' '.join(re.sub(r'\{[^}]*\}|\[[^\]]*\]|\(\?\)|<|>', '', w) for w in W.values()).replace('- ', '')
_lmscore = _lm.load('it-cinquecento').per_char(_lm.norm(_t, 'early'))
hdr = f"""R8572 reading (BL Cotton Vesp. C IV ff.214-218; "el Gilino" to Francesco II Sforza; Paredes, 15 Sept 1527)
Key: DECODE R5258 (ASMi Carteggio Sforzesco cart. 1591 no. 24) + context values (key_r8572.tsv). Built by build_reading.py.

MEASURE
  cipher tokens (transcription after corrections, writer's deletions excluded): {tot}
  nulls (sheet null row or position, dropped):                                {nul}
  significant tokens:                                                         {tot-nul}
  unread tokens (left as [token]):                                            {unread}
  tokens in doubtful words (marked (?), estimated at {avg:.2f} letters/token): {dub_tok}  ({len(dub_words)} words)
  significant tokens read as sense:                                           {read}  = {100*read/(tot-nul):.1f}% of significant tokens
  LM check (it-cinquecento, mean log-prob/char of the word-divided cipher text; real text -1.1..-1.8): {_lmscore:.2f}
  all tokens accounted for (read as sense or as nulls):                       {read+nul} = {100*(read+nul)/tot:.1f}%

CONVENTIONS: one line per MS cipher line, in reading order (DECODE image order is not folio order; see NOTE).
  Spelling as deciphered (the writer's a/o and i/e confusions kept), with a normalised form in [square brackets]
  where needed; <x> = letter supplied; word(?) = doubtful; [tok] = token left unread; {{...}} = clear text in the MS.
NOTE: reading order P1 (214r) - P2 (214v) - P7 (215r) - P3 (215v) - P5 (216r) - P4 (216v) - P6 (217r) - P8 (217v)
  - P9 (218r); P3, P4, P8 are versos (fore-edge on the left in the scans); the joins are textual
  (P7 "...ha portato" / P3 "una letra di propria mano del papa"; P3 "...che lo prati-" / P5 "-cava";
  P5 clear (French ambassadors) / P4 "Ambidoi ..."; P4 "...el detto aratore" / P6 "veneto").
"""
out = [hdr]
for p in ORDER:
    out.append(f'\n=== {p} = {FOL[p]} ===')
    for lid in [k for k in W if k.split('.')[0] == p]:
        out.append(f'{lid:7s} {W[lid]}')
open('reading_r8572.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(hdr.split('CONVENTIONS')[0]); print('unread:', ' '.join(UN)); print('doubtful:', ', '.join(dub_words))
