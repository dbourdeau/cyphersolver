# Split the pass-1 files per document, write pass 2 (the second reading of fresh crops: only the lines where it
# differed are changed) and the reconciled transcription. Run once; prints every pass1/pass2 disagreement.
import re, pathlib, sys
sys.stdout.reconfigure(encoding='utf-8')
R = pathlib.Path(__file__).resolve().parent.parent
FW, WA = R / 'friedrichwilhelm1655', R / 'waldeck1655'
def load(p):
    out = {}
    for l in p.read_text(encoding='utf-8').splitlines():
        m = re.match(r'^(\d{3}\.\w+):\s?(.*)$', l)
        if m: out[m.group(1)] = m.group(2)
    return out
p1 = load(R / 'work/raw_pass1/transcription_cosliln_pass1.txt'); p1.update(load(R / 'work/raw_pass1/transcription_postscript717_pass1.txt')); p1.update(load(R / 'work/raw_pass1/transcription_waldeck_pass1.txt'))
# umlaut marks written in pass 1 prose as 3" are encoded 3: (u umlaut) and 1: (o umlaut)
p1['819.04'] = '"zu correspondiren und die" 12.1.7.9.2.16.2.5. 20.3.12.'
p1['819.05'] = '1.7.2.3.7.14.2.8.4.7. "Absonderlich aber der itzt besa-"'
p1['819.06'] = '"gte Fürst Radziwil, zu verstehen gegeben," 9.2.4. 33.3.'
p1['819.07'] = '9.23.4.7. 15.4.2.7.4.7. 8.5.17.23. 5.16.9. 11.5.9. 9.2.'
p1['819.08'] = '4.9.2.12.17. 3.7.23.4.8. 3.7.9.4.8.4. 22.8.1.23.4.'
p1['819.09'] = '12.23.2.1.7. 14.4.10.4.7. 6.3:.9.23.4.7. 4.9.33.4.'
p1['819.10'] = '8.4. 5.10.4.8. 7.1:.23.2.14. 11.5.9. 4.2.7. 5.16.14.4.'
p1['819.11'] = '6.4.2.7.4.8. 22.8.4.3:.9.9.2.9.12.17.4.8. 16.5.7.13.'
p1['819.12'] = '23.5.14. 11.3.8.12.17. 11.4.7. 10.2.9.12.17.1.13.3.1.7.'
p1['819.13'] = '4.8.6.16.5.7.11. 5.3.9.14.4.9.12.17.8.2.4.10.4.7. 3.3.'
p1['819.14'] = '3:.8.12.4. "und" 33.2.8. 9.4.16.10.2.14.4.7. 11.5.20.3.'
p1['819.15'] = '11.2.9.22.1.7.2.8.23.4.7. "Wir haben demnach bey"'
# second pass: the readings of the fresh half-width crops that differ from pass 1
p2 = dict(p1)
p2['793.03'] = '2.17.8.4.7.6.5. [blot] 8.12.17.10.2.9.17."ier." "nach Cößlin fort-"'
p2['793.07'] = '17.3.16.13.4.4?.7.7.4.8.17.5.16.10.20.4.17.4.7. 23.5.14.4.7.'
p2['793.09'] = '23.4.17.4.7. 14.4.14.4.7. "selbige" 20.4.2.23. 33.4.8."det"'
p2['793.10'] = '2.17.8. "mit" 4.33.8.4."n". 23.8.1.3.22.22.4.7. "und" 20.33.'
p2['795.03'] = '20.3.8.3.15.16.5.9.9.4.7. "und die" 5.8.23. 2.16.16.4.8.2.4.'
p2['795.15'] = '11.4.9.1.8.23.9. "zu" 23.8.5.6?.23.2.8.4.7. "und sein" 14.3.'
p2['797.12'] = '"Uns" 13.1.16.14.4.7. 9.1.16.16.4.7. "Ihr kom̄et auch"'
p2['797.20'] = '"oder" 8.4.9.23.8.5.7.14.4.6.4.7.23. [clear word not read] 4.23.33.5.'
p2['814.01'] = '"Magnus ist gestern" 3.1.7. 23.17.1.8.7?. 33.2.4.11.4.8.'
p2['814.05'] = '3.3.4.8.12.15. 10.4.14.8.2.13.13.4.7. 3.6.10. 6.2?.23. 11.|'
p2['814.06'] = '5.7.23.20.2.14.4. 6?.10.2.7.14. 3.7.11. 11.4.7. 11.8.4.|'
p2['814.07'] = '3.3.1.19. 3.3.1.11.4.7. 5.7. 11.4.8. 3.3.4.2.9.9.4.16. 4?|'
p2['814.11'] = '12.17. 11.5.9.9.2.4. 7.2.12.17.23. 3.7.14.4.7.4.2.|'
docs = {FW: {'c793': ('793', '794', '795'), 'ps797': ('797', '798'), 'ps717': ('717',), 'l819': ('819',)},
        WA: {'w787': ('787', '788', '789'), 'w813': ('813', '814')}}
HEAD = ('# Labels: scan.line. Numbers dot-separated as written; a space is a visible word gap; clear text in double quotes;\n'
        '# N: = N with a diaeresis (umlaut) over it; N^ = N with a bar (doubling); N? = sign not certain; | = rest of the line\n'
        '# lost in the binding; [..] = note, not text. See SIGN_CONVENTIONS.md.\n')
for fold, dd in docs.items():
    for d, scans in dd.items():
        labs = [k for k in p1 if k.split('.')[0] in scans]
        for name, src in (('pass1', p1), ('pass2', p2), (None, p2)):
            fn = fold / (f'transcription_{d}_{name}.txt' if name else f'transcription_{d}.txt')
            fn.write_text(HEAD + ''.join(f'{k}\t{src[k]}\n' for k in labs), encoding='utf-8')
        for k in labs:
            if p1[k] != p2[k]: print(d, k, '\n  p1:', p1[k], '\n  p2:', p2[k])
