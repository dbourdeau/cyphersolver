"""Rebuild the mechanical decryption from the marked reading and compare it with decrypt(transcription, key.tsv).
Marks: {x/y} mechanical x read as y; {+a} letter a added; [...|abc] hole over mechanical abc; [?word|abc] guess over abc.
Fails (exit 1) on any unmarked departure."""
import json, re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from decrypt import load_key, decrypt, HERE
TOK = re.compile(r'\{([a-z])/([a-z])\}|\{\+([a-z])\}|\[(?:\.\.\.|\?[^|\]]*)\|([a-z]+)\]|([a-z])|(\s)')

def mech_from_reading(r):
    out, pos = [], 0
    for m in TOK.finditer(r):
        if m.start() != pos: raise ValueError(f'unparsed text at {pos}: {r[pos:m.start()]!r}')
        pos = m.end()
        if m.group(1): out.append(m.group(1))
        elif m.group(4): out.append(m.group(4))
        elif m.group(5): out.append(m.group(5))
    if pos != len(r): raise ValueError(f'unparsed tail {r[pos:]!r}')
    return ''.join(out)

if __name__ == '__main__':
    kw, sv = load_key()
    bad = 0
    for doc, run, signs, reading, *_ in json.load(open(HERE / 'runs.json', encoding='utf8')):
        mech = decrypt(signs, kw, sv)
        got = mech_from_reading(reading)
        ok = got == mech
        bad += not ok
        print(('OK  ' if ok else 'FAIL'), run, '' if ok else f'\n   mech {mech}\n   read {got}')
    print('all marks accounted for' if not bad else f'{bad} run(s) with unmarked departures')
    sys.exit(1 if bad else 0)
