"""Decrypt a Muzio transcription with key.tsv and count the units by class. Standard library only.

    python scripts/decrypt.py <folder> c3r      writes decryption_c3r.txt, units_c3r.tsv, counts_c3r.txt
    python scripts/decrypt.py <folder> c5       writes decryption_c5.txt, units_c5.tsv, counts_c5.txt

Classes per unit: S letter by key; S0 null by key; E emended (emendations_c3r.tsv); N unread sign (no key value);
CM code confirmed by the c. 5v margin; CC code with a value from context only; CO code with no value.
In the decryption line: . = null, {..} = code, <..> = sign with no key value, x = struck by the writer.
"""
import sys, collections, pathlib

def load_key(p):
    K = {}
    for l in p.read_text(encoding='utf-8').splitlines():
        if l.startswith('# ') or not l.strip(): continue      # comment lines start "# "; the sign # has its own row
        f = l.split('\t'); K[f[0]] = (f[1], f[2])
    return K

def load_tx(p):
    out = []
    for l in p.read_text(encoding='utf-8').splitlines():
        if l.startswith('#') or not l.strip(): continue
        f = l.split(); out.append((f[0], f[1:]))
    return out

def load_emend(p):
    E = {}
    if p.exists():
        for l in p.read_text(encoding='utf-8').splitlines():
            if l.startswith('#') or not l.strip(): continue
            f = l.split('\t'); E[(f[0], int(f[1]))] = (f[2], f[3], f[5])
    return E

def main(folder, doc):
    d = pathlib.Path(folder)
    K = load_key(d / 'key.tsv')
    E = load_emend(d / f'emendations_{doc}.tsv')
    cnt = collections.Counter(); rows = []; dec = []
    for lab, toks in load_tx(d / f'transcription_{doc}.txt'):
        raw = ''; i = -1
        for t in toks:
            if t == '/': continue
            if t == '[x]': raw += 'x'; continue
            t = t.rstrip('?'); i += 1
            val, status = K.get(t, ('', 'open'))
            if status == 'key':
                c = 'S0' if val == '-' else 'S'; shown = '.' if val == '-' else val; read = '' if val == '-' else val
            elif status in ('margin', 'context'):
                c = 'CM' if status == 'margin' else 'CC'; shown = '{' + t.lstrip('C') + '}' if t != 'CE' else '{CE}'; read = '[' + val + ']'
            elif t.startswith('C') and len(t) > 1 and t != 'CE':
                c = 'CO'; shown = '{' + t[1:] + '}'; read = '[' + t[1:] + ']'
            else:
                c = 'N'; shown = '<' + t + '>'; read = '[?]'
            if (lab, i) in E:
                sign, cls, v = E[(lab, i)]
                assert sign == t, (lab, i, sign, t)
                c = cls; read = v
            cnt[c] += 1; raw += shown; rows.append((lab, i, t, c, shown, read))
        dec.append((lab, toks, raw))
    with open(d / f'units_{doc}.tsv', 'w', encoding='utf-8') as f:
        f.write('# line\tunit (0-based, struck signs and dividers skipped)\tsign\tclass\tdecryption by key\tvalue read\n')
        for r in rows: f.write('\t'.join(map(str, r)) + '\n')
    with open(d / f'decryption_{doc}.txt', 'w', encoding='utf-8') as f:
        f.write(f'# Sign-by-sign decryption of transcription_{doc}.txt with key.tsv, unrepaired. Written by scripts/decrypt.py.\n')
        f.write('# . = null   {..} = code group   <..> = sign with no key value   x = sign struck by the writer\n')
        f.write('# The emendations are NOT applied here: they are listed in emendations_c3r.tsv and marked in the reading.\n')
        for lab, toks, raw in dec:
            f.write(f'{lab} cipher : {" ".join(toks)}\n{lab} decrypt: {raw}\n')
    n = sum(cnt.values())
    letters = cnt['S']; nulls = cnt['S0']; codes = cnt['CM'] + cnt['CC'] + cnt['CO']
    L = [f'units {n}: ' + ', '.join(f'{k} {cnt[k]}' for k in ('S', 'S0', 'E', 'N', 'CM', 'CC', 'CO')),
         f'read by key (letters S + nulls S0): {letters + nulls}/{n} = {100 * (letters + nulls) / n:.2f}%',
         f'letters only, nulls left out: {letters}/{n - nulls} = {100 * letters / (n - nulls):.2f}%',
         f'codes counted apart (S + S0 over units that are not codes): {letters + nulls}/{n - codes} = {100 * (letters + nulls) / (n - codes):.2f}%',
         f'with the codes confirmed by the c. 5v margin counted as read: {letters + nulls + cnt["CM"]}/{n} = {100 * (letters + nulls + cnt["CM"]) / n:.2f}%',
         f'emended E {cnt["E"]}; unread signs N {cnt["N"]}; codes: margin CM {cnt["CM"]}, context only CC {cnt["CC"]}, no value CO {cnt["CO"]}']
    (d / f'counts_{doc}.txt').write_text('\n'.join(L) + '\n', encoding='utf-8')
    print('\n'.join(L))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
