"""Held-out test: apply key_frozen.tsv (built from 9922, 9929, 9930 only) to the code words of 9926 and compare each
value with the value the contemporary translation of 9926 (9927/9928) gives at that place (key.tsv, which records that alignment).
exact = same code word in the frozen key; stem = same first five letters (the code keeps Spanish endings).
agree = the first four letters of the two values match after accents are removed and a leading 'se ' is dropped."""
from common import HERE, read_lines, read_key, decrypt_tokens, strip_acc
frozen = read_key(HERE / 'key_frozen.tsv')
full = read_key(HERE / 'key.tsv')
lines = read_lines(HERE / 'transcription_9926.txt')
def norm(v):
    v = strip_acc(v.lower())
    return v[3:] if v.startswith('se ') else v
rows, n_code = [], 0
for lab, toks in lines:
    for code, val in decrypt_tokens(toks, full):
        if val is None:
            continue
        n_code += 1
        how, fv = None, None
        if code in frozen:
            how, fv = 'exact', frozen[code]
        else:
            st = [k for k in frozen if len(code) >= 5 and k[:5] == code[:5]]
            if st:
                how, fv = 'stem', frozen[st[0]] + ' (' + st[0] + ')'
        if how:
            ok = norm(fv)[:4] == norm(val)[:4]
            rows.append((lab, code, how, fv, val, 'agree' if ok else 'DISAGREE'))
hits = len(rows); agree = sum(r[5] == 'agree' for r in rows)
out = ['# Held-out test of key_frozen.tsv on CDLIV.1a.1883.38.9926 (scripts/heldout.py)',
       f'# code-word tokens in 9926: {n_code}; covered by the frozen key: {hits} ({sum(r[2]=="exact" for r in rows)} exact, {sum(r[2]=="stem" for r in rows)} by stem); agree with the contemporary translation: {agree}/{hits}',
       'line\tcode\tmatch\tfrozen value\ttranslation value\tresult']
out += ['\t'.join(r) for r in rows]
open(HERE / 'heldout_9926.tsv', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('\n'.join(out))
