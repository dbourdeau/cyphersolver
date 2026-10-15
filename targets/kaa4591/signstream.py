"""Write sysA2/<rec>_signs.txt (one sign per token) from the System A' code streams sysA2/<rec>.tok, for
docs/_check_profile.py --measure (written 15 Oct 2026). The .tok files hold one character per sign after a line
label ("P1.01 "); r9410b.tok is the Latin letter on ff. 246-247 of R9410."""
import io, os
H = os.path.dirname(os.path.abspath(__file__))
for rec in ('r9408', 'r9409', 'r9410', 'r9410b', 'r9413', 'r9427'):
    out = []
    for l in io.open(os.path.join(H, 'sysA2', rec + '.tok'), encoding='utf8'):
        p = l.rstrip('\n').split(' ', 1)
        if len(p) == 2:
            out.append(' '.join(ch for ch in p[1] if not ch.isspace()))
    io.open(os.path.join(H, 'sysA2', rec + '_signs.txt'), 'w', encoding='utf8').write('\n'.join(out) + '\n')
