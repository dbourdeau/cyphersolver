"""Build docs/reveal/rangone1530.json from cipher.txt and key.json (the 24 Dec 1529 passage)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
key = json.load(open(os.path.join(HERE, 'key.json'), encoding='utf8'))
G = {'hex': '✡', 'pi': 'Π', 'I': 'ɪ', 'l': 'l', 'k': 'K', 'p': 'ρ', 'phi': 'ɸ', 'J': 'ʃ', 'ob': 'δb', 'theta': 'θ',
     'Th': 'Θ', 'L': 'L', 'y': 'ɤ', 'S': '✱', 'S2': '⚹', 'V': 'V', 'P': 'P', 'Z': 'Ƶ', 'w': 'ω', '6': 'б', 't': 'ƫ',
     'oo': '∞', 'xi': 'ξ', 'N': 'N', 'E': '-∋', 'E2': '∋', 'r': 'ɾ', 'x': 'x', 'G': 'ɕ', '8': '8', 'W': '≈', 'q': 'ϙ',
     'oc': '❂', 'X': 'Ж', '+': '+', 'g': 'ʓ', 'U': 'ȣ', 'm': 'mƶ', 'O': '⊙', '#': '#', 'e': 'ℯ', 'xo': 'ꭕ', 'M': 'M',
     'B': 'ㅌ', 'A': '✳', 'vt': 'ϑ', 'a': 'a', 'iii': 'ııı', 'c': 'e', 'd': '∂', '9': '9', 'D': 'D', 'D2': 'Δ',
     'dv': '÷'}
lines = {l.split(':')[0]: l.split(':', 1)[1].split() for l in open(os.path.join(HERE, 'cipher.txt'), encoding='utf8')
         if l[:1] in 'AB' and l[1].isdigit()}
UNC = {'a', 'c', 'd', '9', 'e', 'vt'}


def run(toks, template):
    out, ti = [], 0
    words = template.split(' ')
    for wi, wd in enumerate(words):
        for _ in wd:
            t = toks[ti]; ti += 1
            v = key[t]
            d = {'g': G[t], 'p': '?' if v == '?' else ('·' if v == '.' else v)}
            if v == '?':
                d['cls'] = 'unk'
            elif v == '.':
                d['cls'] = 'null'
            elif t in UNC:
                d['cls'] = 'unc'
            out.append(d)
        if wi < len(words) - 1:
            out.append({'g': '', 'p': ' ', 'cls': 'plain'})
    assert ti == len(toks), (ti, len(toks))
    return out


tok = [{'g': '', 'p': '… haura visto sua bona voluntade ', 'cls': 'plain'}]
tok += run(lines['B1'], 'il fre.goso')
tok += [{'g': '', 'p': ' li giorni passati con spada et cappa ', 'cls': 'plain'}]
b = lines['B2'] + lines['B3'] + lines['B4'] + lines['B5']
tok += run(b, 'tolse fare la cosa de?en mai piu olse r???a le cose ben disposte in casa e hara il f da rouiare e ho una '
              'pratica di lei mi dispiacera')
tok += [{'g': '', 'p': '. Qui ancora si trovara l’Orator del Turco …', 'cls': 'plain'}]
R = {"slug": "rangone1530", "anchor": "the-letter-of-24-december-1529",
     "title": "Venice, 24 December 1529: the Fregoso passage",
     "caption": "The cipher of Rangone’s letter of 24 December 1529 (BnF Français 3082 f. 42r), decoded sign by sign "
                "with the key rebuilt here. Unread signs show ?, doubtful ones are marked, ϑ is a null.",
     "unit": "signs",
     "key_note": "Homophonic key rebuilt ciphertext-only (rangone1530/key.json); the glyphs are typographic stand-ins "
                 "for the drawn signs.",
     "tokens": tok}
json.dump(R, open(os.path.join(HERE, '..', 'docs', 'reveal', 'rangone1530.json'), 'w', encoding='utf8'),
          ensure_ascii=False, indent=1)
print(len(tok), 'tokens')
