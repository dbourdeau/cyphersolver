"""Pass 17 (2026-10-03): values from pooling the open groups of R9873, R9898 and R9660 (sessa1523, read only);
each value is checked on every occurrence (key_working.md pass 17). Idempotent. Run after apply_pass16.py."""
import re
VALUES = {
    'cas': 'tiene', 'boz': 'io', 'var': 'agora', 'rac': 'dize', 'pam': 'paga', 'Jir': 'paga', 'xoc': 'socorr',
    'leg': 'mucho', 'sur': 'parte', 'len': 'buen', 'lon': 'buen', '3ar': 'aca', 'yer': 'Florencia',
    'gig': 'quisie', 'nuf': 'gente', 'rul': 'dia', 'foh': 'ha', 'Jam': 'llam',
    'lep': 'ni', 'ius': 'pasa', 'yeg': 'antes', 'cer': 'ten', 'fe': 'fue', 'pus': 'florentines', 'sir': 'supli',
    'gal': 'embia', 'kif': 'Lombardia', 'luc': 'parte', 'qu': 'o', 'gob': 'ello', 'gul': 'si', 'cox': 'cobra',
    'hut': 'primer', 'tt3': 'r', 'tt sur': 's parte', 'ꝑan': 'ex', 'ler': 'no', '⅄r': 'obligas', 'gli': 'eni',
}
FIX = [('[net=toma]', '[net=halla]'), ('toma-r-a en c-a-n-t-i-da-d', '[net=halla]-r-a en c-a-n-t-i-da-d'),
       ('[kif=Lombardia?]', '[kif=Lombardia]'), ('[pus=florentines?]', '[pus=florentines]'),
       ('[gul=si?]', '[gul=si]'), ('de su [boz=io]', 'de su-[boz=io]'), ('[yod=amigo]-[tt]', '[yod=amigo]-[tt=s]'),
       ('[gal=embi-]-va', '[gal=embia]-va'), ('[fed=rey de Francia?]', '[fed=rey de Francia]'),
       ('[gal]-r-a (embiara)', '[gal=embia]-r-a')]
for path in ('r9873_cipher.txt', 'r9898_cipher.txt'):
    out = []
    for ln in open(path, encoding='utf-8').read().splitlines():
        if re.match(r'\s*\d+[bd]\s', ln):
            for a, b in FIX:
                ln = ln.replace(a, b)
            ln = re.sub(r'\[([^\]=]+)\]', lambda m: '[' + m.group(1) + '=' + VALUES[m.group(1)] + ']'
                        if m.group(1) in VALUES else m.group(0), ln)
        out.append(ln)
    open(path, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('ok')
