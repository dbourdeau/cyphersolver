# decode_v2.py: the second-pass decode. TRANSCRIPTION_v2.tsv with the first-pass key KEY.tsv (unchanged), once, through
# decode_once.dec_token. Run from targets/ercole1547:  python3 -I decode_v2.py   No emendation. Writes DECODE_v2.txt.
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import decode_once as d1
key = d1.load_key(os.path.join(HERE, 'KEY.tsv'))
rows = d1.decode(key, os.path.join(HERE, 'TRANSCRIPTION_v2.tsv'))
h = lambda f: hashlib.sha256(open(os.path.join(HERE, f), 'rb').read()).hexdigest()
with open(os.path.join(HERE, 'DECODE_v2.txt'), 'w') as f:
    f.write('# ercole1547 SECOND-PASS decode (v2; not the figure of record). KEY.tsv sha256 %s; TRANSCRIPTION_v2.tsv sha256 %s\n' % (h('KEY.tsv'), h('TRANSCRIPTION_v2.tsv')))
    f.write('# page line [BUILD|HELD-OUT] units separated by spaces; ? = no value; {L4s} = unresolved code sign\n')
    for pg, ln, u in rows:
        f.write('%s\t%d\t%s\t%s\n' % (pg, ln, 'HELD-OUT' if ln >= 7 else 'BUILD', ' '.join(x for x in u if x)))
        f.write('%s\t%d\t%s\t%s\n' % (pg, ln, 'joined', ''.join(u)))
print(open(os.path.join(HERE, 'DECODE_v2.txt')).read())
