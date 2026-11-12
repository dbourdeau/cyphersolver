#!/usr/bin/env python3
"""Share of coded words read, by the README read bar, for the letter readings in beling/letters/.

A word is a hole when it is an unread group ([370], [575.1060], [1466]), a guessed word or part of a word
([?word], sour[?ce]) or carries supplied letters (delay[ed], [going]). Words Morris wrote in clear (*...* or {...})
are left out. Share = 1 - holes / coded words. Written at the integration check of 12 Nov 2026 so that all the
letters are counted by one rule; it reads files and prints, nothing else. Python standard library only.
Run from any folder: python3 word_share.py"""
import pathlib, re

L = pathlib.Path(__file__).resolve().parent / 'beling' / 'letters'
SKIP = ('Morris to Monroe', 'Pedro de Cevallos to', 'Summary and context', 'Conventions')


def share(path):
    t = path.read_text(encoding='utf-8').split('\nNotes.')[0]
    paras = [p for p in re.split(r'\n\s*\n', t) if p.strip() and not p.strip().startswith(SKIP)]
    b = ' '.join(paras)
    b = re.sub(r'\*[^*]*\*', ' ', b)                       # clear text
    b = re.sub(r'\{[^}]*\}', ' ', b)                       # clear text, older notation
    b = re.sub(r'\((?:B:|plain text|Extract)[^)]*\)', ' ', b)   # editorial notes
    b = b.replace('[1407[555]^]', '[1407]')
    b = re.sub(r'\[[^\]]*\]', lambda m: m.group(0).replace(' ', '_'), b)
    words = [w for w in b.split() if re.search(r'[A-Za-z0-9]', w)]
    holes = [w for w in words if '[' in w]
    return len(words), len(holes), holes


if __name__ == '__main__':
    for d in sorted(L.iterdir()):
        f = d / 'reading.txt'
        if f.exists():
            n, h, hs = share(f)
            print(f"{d.name}: coded words {n}, holes {h}, share {1 - h / n:.3f}   {' '.join(hs)}")
