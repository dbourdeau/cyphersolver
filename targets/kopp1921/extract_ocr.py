"""Pull the cipher frames of M316 rolls 40-48 out of the cached NARA OCR into ocr_frames.jsonl.

    python research/nara_reels/reels.py fetch <the nine naIds>
    python targets/kopp1921/extract_ocr.py

One row per frame with at least MIN runs of 4-5 digit tokens: frame file, full OCR text, the digit tokens. The OCR is a
first pass only: it reads 1 as I, 5 as 3, 8 as 3 or 6 on these carbon copies. Anything measured from it is provisional.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, '..', '..', 'research', 'nara_reels', 'cache')
REELS = [604700562, 604701877, 604703234, 604704577, 604705830, 604707113, 604708415, 604709981, 604711297]
MIN = 12
TOK = re.compile(r'\b[0-9IlOo]{4,5}\b')


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    n = g = 0
    with open(os.path.join(HERE, 'ocr_frames.jsonl'), 'w', encoding='utf-8') as out:
        for reel in REELS:
            txt = {str(o['objectId']): o.get('extractedText') or '' for o in
                   json.load(open(os.path.join(CACHE, f'{reel}.txt.json'), encoding='utf-8'))}
            rec = json.load(open(os.path.join(CACHE, f'{reel}.rec.json'), encoding='utf-8'))
            for d in rec['digitalObjects']:
                t = txt.get(str(d['objectId']), '')
                toks = [x for x in TOK.findall(t) if any(c.isdigit() for c in x)]
                if len(toks) < MIN:
                    continue
                toks = [x.replace('I', '1').replace('l', '1').replace('O', '0').replace('o', '0') for x in toks]
                out.write(json.dumps({'file': d['objectFilename'], 'url': d.get('objectUrl'), 'text': t, 'tokens': toks},
                                     ensure_ascii=False) + '\n')
                n += 1
                g += len(toks)
    print(n, 'frames', g, 'tokens')


if __name__ == '__main__':
    main()
