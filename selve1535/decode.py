"""Selve's cipher (Tomokiyo's table, extended on the letters; see NOTES.md "Key").

Signs are written with the Unicode look-alikes used in work/*.md. A sign whose value depends on the word
(the c/d hooks, the curled a/u sign) is written sign:value, e.g. "ℓ:d". Usage:
    python decode.py "S ω ▽ 7 ꝏ ‡ ot"          -> . e n t r e s
    python decode.py --reveal lines.txt out.json
"""
import sys, json

KEY = {
    'z': 'a', '3': 'a', '∂': 'a', 'f': 'b', 'ƀ': 'b', 'ℓ': 'c', 'L': 'd', '‡': 'e', 'o': 'e', 'ω': 'e',
    'ʃ': 'p', 'Ꟙ': 'f', '∽': 'g', '£': 'h', 'p': 'i', 'q': 'i', '/': 'l', 'x': 'm', '▽': 'n', 'ɥ': 'o',
    '4': 'o', 'R': 'o', '6': 'q', 'ꝏ': 'r', 'ot': 's', '7': 't', 'X': 'u', 'Ⴟ': 'u', 'β': 'v', 'Ƶ': 'x',
    'ʒ': 'y', 'Ⓢ': 'z', 'S': '.', '●': '.',
}

def value(sign):
    if ':' in sign and len(sign) > 1:
        return sign.split(':', 1)[1]
    return KEY.get(sign, '?')

def decode(line):
    return [(s, value(s)) for s in line.split()]

if __name__ == '__main__':
    if sys.argv[1] == '--reveal':
        src, out = sys.argv[2], sys.argv[3]
        cfg = json.load(open(src, encoding='utf-8'))
        toks = []
        for item in cfg['lines']:
            if item.startswith('CLEAR '):
                toks.append({'g': '', 'p': item[6:], 'cls': 'plain'})
                continue
            for s, v in decode(item):
                g = s.split(':')[0] if len(s) > 1 and ':' in s else s
                cls = 'null' if v == '.' else ('unk' if v == '?' else '')
                toks.append({'g': g, 'p': '·' if v == '.' else v, 'cls': cls})
        meta = {k: v for k, v in cfg.items() if k != 'lines'}
        meta['tokens'] = toks
        json.dump(meta, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(len(toks), 'tokens ->', out)
    else:
        print(' '.join(v for _, v in decode(sys.argv[1])))
