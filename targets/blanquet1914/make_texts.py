"""Write the group-by-group decryption of Blanquet's telegram of 19 May 1914 with Clave núm. 109.

The key is Brice Dudout's transcription in targets/rubio1913/key.tsv, read in place (not copied). Each cipher run of
the frozen transcription is printed with the unedited key output underneath. '?' is an illegible group or a group the
key does not give.

    python3 -I targets/blanquet1914/make_texts.py      (from the repository root)
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
KEY = HERE.parent / 'rubio1913' / 'key.tsv'

k = {}
for line in KEY.read_text(encoding='utf-8').splitlines():
    if not line.strip() or line.startswith('#'): continue
    p = line.split('\t')
    if p[0].strip().isdigit() and len(p) > 1 and p[1].strip():
        k[str(int(p[0]))] = p[1].strip()
lines = ['# Group-by-group decryption. CEHM DLXXIII.2.41.22-41, Blanquet to Rubio, 19 May 1914; key ../rubio1913/key.tsv '
         '(Clave núm. 109, transcribed by Brice Dudout), unchanged.',
         '# One cipher run per pair of lines; clear Spanish between runs is not shown. ? = illegible or not in the key.', '']
for i, line in enumerate((HERE / 'may19.runs').read_text(encoding='utf-8').split('\n'), 1):
    g = line.split()
    if not g: continue
    lines += [f'<< run {i} >>', ' '.join(g), ' '.join(k.get(x, '?') if x != '?' else '?' for x in g)]
(HERE / 'decryption_may19.txt').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('decryption_may19.txt written')
