"""Write r9367/signs.txt (one cipher sign per token) from r9367/transcription.txt for docs/_check_profile.py --measure.
Only the L.. and P. lines; clear text [..], comments in (..) and after three spaces, '?' and '.' marks dropped."""
import io, os, re
H = os.path.dirname(os.path.abspath(__file__))
out = []
for l in io.open(os.path.join(H, 'r9367', 'transcription.txt'), encoding='utf8'):
    m = re.match(r'(?:L\d\d|P\d) (.*)', l.rstrip('\n'))
    if not m:
        continue
    s = re.split(r'\s{3,}\(', m.group(1))[0]
    s = re.sub(r'\[[^\]]*\]', ' ', s)
    s = re.sub(r'\([^)]*\)', ' ', s)
    s = re.sub(r'[?.\]]', '', s)
    out.append(' '.join(ch for ch in s if not ch.isspace()))
io.open(os.path.join(H, 'r9367', 'signs.txt'), 'w', encoding='utf8').write('\n'.join(out) + '\n')
