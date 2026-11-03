"""Grep Yale finding-aid PDFs (ead-pdfs.library.yale.edu/<resource id>.pdf) for cipher words.

archives.yale.edu answers 403 even in a real browser, but the PDFs of the same finding aids are open to scripts.
    python pdf_grep.py <ids.txt: one resource id per line> <cache dir> <out.tsv>
"""
import os, re, sys, time, urllib.request

import pymupdf

RE = re.compile(r'(?i)\b(in|partly in|partially in|part in|written in|mostly in|largely in)\s+(a\s+)?(cipher|cypher|code)\b|'
                r'\b(ciphers?|cyphers?|ciphered|cyphered|enciphered|deciphered|decipherment|undeciphered|undecoded|cryptogram|'
                r'coded letter|code letter|secret code|encrypted|encoded)\b')
NOISE = re.compile(r'(?i)cipher ?book|ciphering|cyphering|monogram|royal cypher|bacon|shakespeare|encoded by|encoded in ead')
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) Chrome/130'}


def main(ids, cache, out):
    os.makedirs(cache, exist_ok=True)
    with open(out, 'w', encoding='utf-8') as w:
        for i in [x.strip() for x in open(ids, encoding='utf-8') if x.strip()]:
            p = os.path.join(cache, i + '.pdf')
            if not os.path.exists(p):
                time.sleep(1.5)
                try:
                    data = urllib.request.urlopen(urllib.request.Request(
                        f'https://ead-pdfs.library.yale.edu/{i}.pdf', headers=UA), timeout=120).read()
                except Exception as x:
                    print('ERR', i, x, flush=True)
                    continue
                open(p, 'wb').write(data)
            try:
                d = pymupdf.open(p)
            except Exception as x:
                print('BAD', i, x, flush=True)
                continue
            title = re.sub(r'\s+', ' ', d[0].get_text())[:90]
            n = 0
            for pno, page in enumerate(d):
                t = re.sub(r'\s+', ' ', page.get_text())
                for m in RE.finditer(t):
                    c = t[max(0, m.start() - 170):m.end() + 130]
                    if NOISE.search(c):
                        continue
                    w.write(f'{i}\t{pno + 1}\t{title}\t{c}\n')
                    n += 1
            w.flush()
            print(i, n, title[:60], flush=True)


if __name__ == '__main__':
    main(*sys.argv[1:4])
