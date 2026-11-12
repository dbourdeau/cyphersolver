"""Locate candidate cipher figures in an archive.org djvu.txt (OCR). Standard library only.

Usage: python3 -I scripts/find_figures.py <djvu.txt> [<djvu.txt> ...]
Prints file, line number and line for (a) runs of two or more figure-like tokens, (b) a single figure-like token right
after "M.", "de", "a"/"à", "par", "avec", "que", "le", "la", "du", "au" or "sieur", followed by a full stop, comma or a
word. OCR often prints 1 as l or I and 0 as o, so tokens of digits mixed with l, I, o, O are accepted when they contain a
digit. Dates, sums and page references are not removed: every hit has to be read on the page image.
"""
import re
import sys

TOK = r'(?=[\dlIoO]{0,3}\d)[\dlIoO]{1,4}'
RUN = re.compile(r'(?<![\w,])(' + TOK + r')(\s*[.,]\s*|\s+)(' + TOK + r')\s*[.,]')
SINGLE = re.compile(r'\b(M\.|de|a|à|par|avec|que|le|la|du|au|sieur|aulx|envers|des)\s+(' + TOK + r')\s*[.,;]?\s+[a-zé]')
SKIP = re.compile(r'\b(1[5-6]\d\d|liv|livres|escus|mil|janvier|febvrier|fevrier|mars|avril|apvril|may|mai|juin|juillet|'
                  r'aoust|septembre|octobre|novembre|decembre|décembre|p\.|pag|tom|chap|art|fol)\b', re.I)


def main():
    for path in sys.argv[1:]:
        lines = open(path, encoding='utf-8', errors='replace').read().split('\n')
        for i, l in enumerate(lines):
            kind = None
            if RUN.search(l):
                kind = 'RUN'
            elif SINGLE.search(l):
                kind = 'ONE'
            if kind:
                flag = ' (date/sum word on line)' if SKIP.search(l) else ''
                print(f'{path.rsplit("/", 1)[-1]}:{i + 1}:{kind}{flag}: {l[:170]}')


if __name__ == '__main__':
    main()
