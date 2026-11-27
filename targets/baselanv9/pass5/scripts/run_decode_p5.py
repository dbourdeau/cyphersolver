"""Pass 5: ONE decode of the frozen texts (python3 -I). Checks every hash against FREEZE_P5.txt first.
The checks were done with AI tools and no person checked each record by hand."""
import sys, hashlib, re
R = sys.argv[1].rstrip('/') + '/'
sys.path.insert(0, R + 'scripts')
import decode_p5 as d
frz = open(R + 'FREEZE_P5.txt').read()
for f in ['KEY_V5.tsv','scripts/decode_p5.py','tx/f004r.txt','tx/f004v.txt','tx/f015r_H1r.txt','tx/f159r.txt','tx/f034r_p34.txt','tx/f025r_H4.txt','tx/PENT_S1_v4.txt','tx/PENT_S2_v4.txt','tx/S2_INNER_v5.txt','tx/F054R_v5.txt','tx/F097_v5.txt']:
    assert hashlib.sha256(open(R + f, 'rb').read()).hexdigest() in frz, f
K = d.load_key(R + 'KEY_V5.tsv')
T = [('TRAIN f4r','tx/f004r.txt'),('TRAIN f4v','tx/f004v.txt'),('H1r','tx/f015r_H1r.txt'),('H2','tx/f159r.txt'),('H3','tx/f034r_p34.txt'),('H4','tx/f025r_H4.txt'),('S1','tx/PENT_S1_v4.txt'),('S2','tx/PENT_S2_v4.txt'),('S2i','tx/S2_INNER_v5.txt'),('F54','tx/F054R_v5.txt'),('F97','tx/F097_v5.txt')]
for flag, out in [(False, 'DECODE_P5.txt'), (True, 'DECODE_P5_noC45.txt')]:
    d.NO_C45 = flag
    o = ['# PASS 5: ONE decode, KEY_V5.tsv + scripts/decode_p5.py (RULES_V5.md), NO_C45=%s. "=" word broken at line end; [?] no value; ~ bar, not expanded. No emendation. The checks were done with AI tools and no person checked each record by hand.' % flag]
    for tag, f in T:
        n = u = 0
        for lid, dec in d.decode_file(R + f, K):
            t = ' '.join(dec); o.append('%s %s\t%s' % (tag, lid, t)); n += len(re.sub('[^a-z]', '', t.replace('[?]', ''))); u += t.count('[?]')
        o.append('# %s: decoded letters %d, signs with no value %d' % (tag, n, u))
    open(R + out, 'w').write('\n'.join(o) + '\n')
print('done')
