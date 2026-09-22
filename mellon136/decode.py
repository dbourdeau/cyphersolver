"""Mellon MS 136: turn transcription.txt into sign tokens and a reading.

The transcription writes each cipher sign as its key value (key of p. 83). This script maps every token back to
the grid sign it stands for, so the passages can be shown sign by sign, and counts signs, words and unread signs.

    python decode.py            # per-passage reading and counts
    python decode.py --signs    # sign stream only (for measuring)
    python decode.py --reveal p76a   # write docs/reveal/mellon136.json from one passage
"""
import json, re, sys, pathlib

HERE = pathlib.Path(__file__).parent

# key of p. 83: cell shape, and whether the letter is the dotted one
GRID = {'a': '┘', 'b': '┘·', 'c': '⊔', 'd': '⊔·', 'e': '└', 'f': '└·', 'g': '⊐', 'h': '⊐·', 'i': '□',
        'l': '⊏', 'm': '⊏·', 'n': '┐', 'o': '┐·', 'p': '⊓', 'q': '⊓·', 'r': '┌', 's': '┌·',
        't': 'V', 'u': 'V·', 'v': '>', 'w': '>·', 'y': '<·', 'z': 'Λ', 'k': '□·'}
LIG = {'ae': '┴', 'oe': 'ᒣ̈', 'ue': 'ᗜ', 'ch': '⊐̆', 'ck': '□̆', 'sch': '┌̆', 'ss': '┌̃', 'st': '┌ˇ',
       'th': 'ɐ', 'und': 'V̆', 'll': '⊏″', 'nn': '┐″', 'tt': 'V″', 'ff': '└″'}
LIG_TEXT = {'ae': 'ä', 'oe': 'ö', 'ue': 'ü', 'und': 'und'}


def passages():
    cur, out = None, {}
    for line in (HERE / 'transcription.txt').read_text(encoding='utf-8').splitlines():
        if not line.strip() or line.startswith('#'):
            continue
        m = re.match(r'^(p\d+[a-z]?)\b(.*)$', line)
        if m:
            cur = m.group(1)
            out[cur] = ''
            continue
        out[cur] += ' ' + line.strip()
    return out


def tokens(text):
    """Yield (sign, value, cls) for one passage; word breaks as (None, ' ', 'sp')."""
    for word in text.replace('|', ' ').split():
        i = 0
        while i < len(word):
            ch = word[i]
            if ch == '(':
                j = word.index(')', i)
                yield ('', word[i + 1:j], 'plain'); i = j + 1
            elif ch == '[':
                j = word.index(']', i)
                lig = word[i + 1:j]
                yield (LIG[lig], LIG_TEXT.get(lig, lig), ''); i = j + 1
            elif ch == '{':
                j = word.index('}', i)
                yield ('?', '?', 'unk'); i = j + 1
            elif ch in GRID:
                yield (GRID[ch], ch, ''); i += 1
            else:  # '=' hyphen, punctuation
                i += 1
        yield (None, ' ', 'sp')


def main():
    ps = passages()
    if '--reveal' in sys.argv:
        pid = sys.argv[sys.argv.index('--reveal') + 1]
        toks = []
        for g, p, cls in tokens(ps[pid]):
            if g is None:
                if toks:
                    toks[-1]['p'] += ' '
                continue
            toks.append({'g': g, 'p': p, 'cls': cls})
        data = {'slug': 'mellon136', 'anchor': 'reading',
                'title': 'Page 76, sign by sign',
                'caption': 'Mellon MS 136 p. 76: each grid sign is replaced by its value in the book’s own key '
                           '(p. 83). Dotted signs are the second letter of their cell; the water sign ∇ is clear.',
                'unit': 'sign', 'key_note': 'Key: the figure on p. 83 of the manuscript, used unchanged.',
                'tokens': toks}
        out = HERE.parent / 'docs' / 'reveal' / 'mellon136.json'
        out.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print('wrote', out, len(toks), 'tokens')
        return
    tot_signs = tot_unk = tot_words = 0
    for pid, text in ps.items():
        signs = [t for t in tokens(text) if t[0]]
        unk = sum(1 for t in signs if t[2] == 'unk')
        reading = ''.join(v if g is not None else ' ' for g, v, c in tokens(text))
        reading = re.sub(r' +', ' ', reading).strip()
        words = len([w for w in reading.split() if re.search('[a-zäöü]', w)])
        tot_signs += len(signs); tot_unk += unk; tot_words += words
        if '--signs' in sys.argv:
            print(''.join(t[1] for t in signs if t[2] != 'unk'))
        else:
            print(f'{pid:5} {len(signs):4} signs {unk} unread | {reading}')
    if '--signs' not in sys.argv:
        print(f'total: {tot_signs} cipher signs, {tot_unk} unread, {tot_words} cipher words')


if __name__ == '__main__':
    main()
