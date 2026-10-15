"""Write r9416/signs_f263.txt (one cipher sign per token) from r9416/p34_v2.txt (f.263, v2 transcription) for
docs/_check_profile.py --measure. Only the numbered cipher lines; g: gloss lines, clear words [..] and '?' marks
after doubtful signs are dropped. f.262 has no sign transcription (only its gloss, r9416/gloss.txt)."""
import io, os, re
H = os.path.dirname(os.path.abspath(__file__))
out = []
for l in io.open(os.path.join(H, 'r9416', 'p34_v2.txt'), encoding='utf8'):
    m = re.match(r'(\d\d): (.*)', l.rstrip('\n'))
    if not m:
        continue
    s = re.sub(r'\[[^\]]*\]', ' ', m.group(2)).replace('?', '')
    out.append(' '.join(ch for ch in s if not ch.isspace()))
io.open(os.path.join(H, 'r9416', 'signs_f263.txt'), 'w', encoding='utf8').write('\n'.join(out) + '\n')
