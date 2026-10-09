# doc2tr.py R#### : DECODE DOC file -> transcr/R####.txt, one line per DOC line, KEEPING the group lines that start
# with a <CLEARTEXT ...> paragraph tag (parse.py drops those whole lines: 7 lines in R1064, 12 in R1065).
# A leading 0 is written as 8 (looped-8 hand, see NOTES); doubtful tokens are listed in a comment after the line.
import re, sys, glob
r = sys.argv[1]
f = glob.glob(f'decode/DOC_{r}_*.txt')[0]
out = [f'# {r} from {f} (DECODE transcription), converted 5 Oct 2026 by doc2tr.py: leading 0 -> 8; lines tagged',
       '# with paragraph marks kept. Lines marked "#img" were then checked against the image.']
for line in open(f, encoding='utf8', errors='replace'):
    if line.startswith('#IMAGE NAME'): out.append('# --- ' + line[1:].strip()); continue
    if line.startswith('#'): continue
    tags = re.findall(r'<[^>]*>', line); body = re.sub(r'<[^>]*>', ' ', line)
    if re.search(r'[A-Za-z]', body): continue
    toks = []; doubt = []
    for tok in body.replace(' ', '').split('.'):
        t = re.sub(r'[^0-9?/]', '', tok)
        if not t: continue
        d = re.sub(r'/\d+\??', '', t).replace('?', '')
        if not d: continue
        if d[0] == '0' and len(d) > 1: d = '8' + d[1:]
        if '?' in t or '/' in t: doubt.append(t)
        toks.append(d)
    from view import fix
    toks = [str(x) for x in fix([int(t) for t in toks])]
    if toks:
        if tags: out.append('# tag: ' + ' '.join(tags))
        out.append(' '.join(toks) + ('   ' if False else ''))
        if doubt: out.append('# doubtful in DECODE: ' + ' '.join(doubt))
open(f'transcr/{r}.txt', 'w', encoding='utf8').write('\n'.join(out) + '\n')
print(sum(len(l.split()) for l in out if not l.startswith('#')))
