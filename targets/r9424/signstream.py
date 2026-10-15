"""Write r9424/signs.txt (one cipher sign per token) from r9424/transcription.txt for docs/_check_profile.py --measure.
Only the L.. lines; clear text [..], struck runs {struck:..}, comments after three spaces, '?' and '^' marks, '.', ','
and brackets are dropped; '/' (a slash written inside words) is a sign in the legend, so it is kept. The margin
nomenclator table on f.273v is left out."""
import io, os, re
H = os.path.dirname(os.path.abspath(__file__))
out = []
for l in io.open(os.path.join(H, 'r9424', 'transcription.txt'), encoding='utf8'):
    m = re.match(r'L\d\d (.*)', l.rstrip('\n'))
    if not m:
        continue
    s = re.split(r'\s{3,}\(', m.group(1))[0]
    s = re.sub(r'\[[^\]]*\]', ' ', s)
    s = re.sub(r'\{[^}]*\}', ' ', s)
    s = re.sub(r'[?^.,()]', '', s)
    out.append(' '.join(ch for ch in s if not ch.isspace()))
io.open(os.path.join(H, 'r9424', 'signs.txt'), 'w', encoding='utf8').write('\n'.join(out) + '\n')
