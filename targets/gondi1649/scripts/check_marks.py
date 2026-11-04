"""Check reading_marked_c1r.txt against the signs. Exit 1 on any unmarked departure.
The decryption is rebuilt from transcription_c1r.txt and key.tsv (scripts/decode.py), then each reading line is walked
unit by unit (one unit = one letter sign, one consonant pair, or one code group):
  plain letter    must be one of the unit's values, and the unit must not be doubtful
  {+x}            no sign under it (restored)
  {a/b}           one unit, whose values include b (changed)
  {?x}            one unit marked doubtful in the transcription; x must be one of its values
  [G text]        one code unit with group G; [G ?text] = value from context only
Every unit of the line must be consumed. Also prints word counts and runs the held-out test.
"""
import pathlib, re, sys, unicodedata
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import decode

ITEM = re.compile(r'\[[^\]]*\]|\{[^}]*\}|[^\W\d_]', re.UNICODE)


def plain(c):
    return unicodedata.normalize('NFD', c)[0].lower()


def reading():
    out = {}
    for l in (decode.ROOT / 'reading_marked_c1r.txt').read_text(encoding='utf8').splitlines():
        if l.startswith('L'):
            ln, _, t = l.partition('\t'); out[ln] = t
    return out


ASSIGNED = {}


def check(key):
    bad, words = [], {'verbatim': 0, 'marked': 0, 'context': 0}
    rd = reading()
    for ln, toks in decode.signs():
        us = decode.units(toks, key); k = 0; t = rd.get(ln, '')
        for it in ITEM.findall(t):
            if it.startswith('['):
                g, _, txt = it[1:-1].partition(' ')
                if k >= len(us) or us[k][0] != g:
                    bad.append(f'{ln}: code {it} but signs give {us[k][0] if k < len(us) else "end"}')
                ASSIGNED[(ln, k)] = '[' + txt.lstrip('?') + ']'
                k += 1
            elif it.startswith('{+'):
                pass
            elif it.startswith('{?'):
                x = plain(it[2])
                if k >= len(us) or not us[k][2] or x not in us[k][1]:
                    bad.append(f'{ln}: {it} not on a doubtful sign with that value ({us[k] if k < len(us) else "end"})')
                ASSIGNED[(ln, k)] = x
                k += 1
            elif it.startswith('{'):
                a, _, b = it[1:-1].partition('/')
                if k >= len(us) or b not in [v.strip('[]') for v in us[k][1]]:
                    bad.append(f'{ln}: {it} but signs give {us[k][1] if k < len(us) else "end"}')
                ASSIGNED[(ln, k)] = b if not us[k][1][0].startswith('[') else '[' + b + ']'
                k += 1
            else:
                x = plain(it)
                if k >= len(us):
                    bad.append(f'{ln}: letter {it} past the end of the signs'); continue
                if x not in us[k][1]:
                    bad.append(f'{ln}: unmarked departure: reading {it}, signs {us[k][0]}={us[k][1]}')
                elif us[k][2]:
                    bad.append(f'{ln}: letter {it} rests on doubtful sign {us[k][0]} without {{?}}')
                ASSIGNED[(ln, k)] = x
                k += 1
        if k != len(us):
            bad.append(f'{ln}: {len(us) - k} sign units not covered by the reading')
        # words: codes count as one word; a split word (x- / -y) counts once, on the line where it starts
        t2 = re.sub(r'\[([^\] ]*) ([^\]]*)\]', lambda m: '[' + m[1] + '_' + m[2].replace(' ', '_') + ']', t)
        for w in t2.split():
            if w.startswith('-'):
                continue
            if '?' in w and '[' in w and '_?' in w:
                words['context'] += 1
            elif '{' in w:
                words['marked'] += 1
            else:
                words['verbatim'] += 1
    return bad, words


def heldout():
    """Units of L07-L13 (grouped as in the decryption); for each, the frozen key's values are compared with the
    value the reading gives that unit. Run after check()."""
    fk, full = decode.load_key(frozen_only=True), decode.load_key()
    tot = agree = 0; notes = []
    for ln, toks in decode.signs():
        if ln < 'L07':
            continue
        for k, (g, vals, d) in enumerate(decode.units(toks, full)):
            tot += 1
            r = ASSIGNED.get((ln, k))
            fv = fk.get(g)
            if fv is None:
                notes.append(f'{ln}: {g} -> {r}: no frozen value')
            elif r in fv or r.strip('[]') in [x for v in fv for x in v.strip('[]').split('/')]:
                agree += 1
            else:
                notes.append(f'{ln}: {g} -> {r}: frozen key gives {"|".join(fv)}')
    return tot, agree, notes


def main():
    bad, words = check(decode.load_key())
    for b in bad:
        print('FAIL', b)
    n = sum(words.values())
    print(f"words in the cipher reading: {n}; verbatim from the signs {words['verbatim']}; "
          f"with a marked repair {words['marked']}; context-only codes {words['context']}")
    tot, agree, misses = heldout()
    print(f'held-out L07-L13: {tot} sign units; frozen key agrees with the reading on {agree} ({100*agree/tot:.1f}%); others:')
    for m in misses:
        print('   ', m)
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
