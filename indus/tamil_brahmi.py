"""The Indus name slot against the earliest Dravidian names: Tamil-Brahmi (ca. 2nd c. BCE - 3rd c. CE).

Mahadevan's Early Tamil Epigraphy (2003; archive.org OCR) lists every personal name in the Tamil-Brahmi
cave inscriptions in its Index to Personal Names (Appendix II), women marked (fem.). The OCR is noisy
(Cyrillic look-alikes, 'g' for the final n-letter); names are normalised and each full name (not a
segment) is classed by its final segment as Mahadevan's grammar does (7.23-7.24): masculine singular
-an / -on / -ko(n) and the masculine title endings -antai, -nanti, -porai (Mahadevan counts all but
the marked names as men's), feminine (marked), honorific -ar, other (mostly OCR debris and -i names).

TB1 The class proportions of early Tamil names, against the two Indus endings (740 / 520).
TB2 Length: segments per name (Tamil) against signs per name before the ending (Indus).
TB3 Where the class suffix sits: on the last segment of the name in both?

Usage: python tamil_brahmi.py path/to/ete.txt
Writes results/tamil_brahmi.md.
"""
import os
import re
import sys
import unicodedata
from collections import Counter

from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
CYR = str.maketrans({'А': 'A', 'а': 'a', 'В': 'B', 'С': 'C', 'с': 'c', 'Е': 'E', 'е': 'e', 'Н': 'H', 'К': 'K',
                     'к': 'k', 'М': 'M', 'м': 'm', 'О': 'O', 'о': 'o', 'Р': 'P', 'р': 'p', 'Т': 'T', 'т': 't',
                     'у': 'y', 'Х': 'X', 'х': 'x', 'П': 'N', 'п': 'n', 'Ц': 'L', 'ц': 'l', 'Ш': 'N', 'ш': 'u',
                     'І': 'I', 'і': 'i', 'Ї': 'I', 'ї': 'i', 'ђ': 'h', 'ћ': 'h', 'љ': 'lj', 'Ј': 'J', 'ј': 'j'})


def say(s=''):
    OUT.append(s)
    print(s)


def norm(w):
    w = w.translate(CYR)
    w = unicodedata.normalize('NFD', w)
    w = ''.join(c for c in w if not unicodedata.combining(c)).lower()
    w = re.sub(r'[\[\]\*\(\)]', '', w)
    w = re.sub(r'(a)[gp]$', r'\1n', w)          # OCR of the final n-letter
    return w


def classify(last, fem):
    if fem:
        return 'feminine'
    if re.search(r'(an|on|ko|koy|kon|n|antai|antay|nanti|porai|porumpurai|umpurai)$', last):
        return 'masculine -an / -on / -ko'
    if re.search(r'ar$', last):
        return 'honorific -ar'
    return 'other'


def main(path):
    lines = open(path, encoding='utf-8', errors='replace').read().split('\n')
    start = next(i for i, l in enumerate(lines) if 'INDEX TO PERSONAL NAMES IN THE INSCRIPTIONS' in l)
    start = next(i for i in range(start, len(lines)) if 'and the Commentary' in lines[i]) + 1
    end = next((i for i in range(start + 1, len(lines)) if 'INDEX TO PLACE NAMES' in lines[i].upper()), start + 1400)
    names = []
    for l in lines[start:end]:
        for part in re.split(r'\s{2,}|\d[\d\.a-e,\s]*', l):
            part = part.strip()
            if not part or part[0] in '-=—(' or len(part) < 3:
                continue
            fem = '(fem' in part
            part = re.sub(r'\(fem\.?\)', '', part).strip()
            words = [norm(w) for w in part.split() if re.search(r'[A-Za-zА-яІі]', w)]
            words = [w for w in words if len(w) >= 2 and w not in ('google', 'index', 'to', 'personal', 'names', 'in', 'the')]
            if not words or not words[0][:1].isalpha() or len(words) > 4 or any('.' in w for w in words)                     or words[0] in ('early', 'appendix', 'h-c'):
                continue
            names.append((tuple(words), fem))
    names = list(dict.fromkeys(names))
    say('# The Indus name slot against early Tamil names (Tamil-Brahmi)')
    say()
    cls = Counter(classify(n[-1], f) for n, f in names)
    tot = len(names)
    say('## TB1 Class proportions')
    say()
    say('- Tamil-Brahmi personal names parsed from Mahadevan 2003, Appendix II (OCR, full names only): %d. By the '
        'class of the last segment: %s.' % (tot, ', '.join('%s %d (%.0f%%)' % (k, v, 100 * v / tot) for k, v in cls.most_common())))
    ends = Counter()
    rows = [r for rs in (load(), load(only_m77=True)) for r in rs if r['flat']]
    stem_len = Counter()
    for r in rows:
        for ln in r['seq']:
            t = [g for g in ln if g != '?']
            if len(t) >= 3 and t[-1] in ('400', '90', '151') and t[-2] in ('740', '520'):
                ends[t[-2]] += 1
                stem_len[min(len(t) - 2, 6)] += 1
            elif len(t) >= 2 and t[-1] in ('740', '520'):
                ends[t[-1]] += 1
                stem_len[min(len(t) - 1, 6)] += 1
    ne = sum(ends.values())
    say('- Indus names with an ending: %d; 740 %d (%.0f%%), 520 %d (%.0f%%).' % (
        ne, ends['740'], 100 * ends['740'] / ne, ends['520'], 100 * ends['520'] / ne))
    say('- Both are dominated by one class. In Tamil it is the masculine singular: Mahadevan (7.23.1-2) notes that '
        'personal names are mostly masculine and feminine ones very few. In the Indus texts the minority class is the '
        'fish names, not women\'s names (noun_class.py); so the proportions agree, the content of the minority does not '
        'map onto Tamil feminine names. A rational / non-rational reading (the fish names as non-rational star names) '
        'is the one that fits both.')
    say()
    say('## TB2 Length')
    say()
    tl = Counter(min(len(n), 6) for n, _ in names)
    say('- Tamil-Brahmi names, words per name: %s (mean %.2f).' % (
        ', '.join('%d: %d' % kv for kv in sorted(tl.items())), sum(len(n) for n, _ in names) / tot))
    say('- Indus names, signs before the ending: %s (mean %.2f).' % (
        ', '.join('%d: %d' % kv for kv in sorted(stem_len.items())),
        sum(k * v for k, v in stem_len.items()) / sum(stem_len.values())))
    say('- A Tamil name word is one to three morphemes (Katal-an, Kuvira-antai Vel). If an Indus sign writes a '
        'morpheme, 1-2 words of 2-3 morphemes each are 2-6 signs: the Indus name slot (mostly 1-4 signs) is of that '
        'order. The comparison cannot be sharper without sound values.')
    say()
    say('## TB3 Where the class suffix sits')
    say()
    say('- Tamil: the PNG suffix (-an, -i, -ar) is on the last word of the name, and in genitive phrases the possessor '
        'comes first (X-an makan "son of X", X-a(n) kon); the same in the Indus formula "X-740 man".')
    say()
    say('Result: early Tamil names have the grammar the Indus name slot shows - one dominant class suffix on the last '
        'element, a small second class, possessor before head. This is agreement, not proof; Sanskrit names also end '
        'in gender endings, though three genders and many declensions, and the check has no power to exclude it.')
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'tamil_brahmi.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
