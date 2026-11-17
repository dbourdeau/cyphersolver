"""Build the classical Arabic poetry corpus for the ar-classical-poetry model.

Source: the Ashaar dataset (arbml/Ashaar_dataset on Hugging Face, about 130,000 poems scraped from aldiwan.net, with the
poet's era). Only poems of the pre-modern eras are kept, Mamluk first: Mamluk, Ayyubid, Fatimid, Abbasid, Andalusian,
Maghrib and al-Andalus, Umayyad, the two dynasties' interval, early Islamic, mukhadram, pre-Islamic. Modern, Ottoman
and undated poems are dropped. Each verse is one line, the two hemistichs joined by a space. The vowel signs stay in
the file; lm.norm(..., 'arabic28') reduces it to the 28 letters.

Output: lang/corpora/ar-classical-poetry.txt (git-ignored).  Run: python -m lang.build_ar_poetry
Needs pyarrow (pip install pyarrow).
"""
import os, sys, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'corpora', 'ar-classical-poetry.txt')
BASE = 'https://huggingface.co/datasets/arbml/Ashaar_dataset/resolve/main/data/'
FILES = ['train-00000-of-00002.parquet', 'train-00001-of-00002.parquet']
ERAS = ['العصر المملوكي', 'العصر الأيوبي', 'العصر الفاطمي', 'العصر العباسي', 'العصر الأندلسي', 'المغرب والأندلس',
        'العصر الأموي', 'عصر بين الدولتين', 'العصر الإسلامي', 'المخضرمين', 'العصر الجاهلي', 'قبل الإسلام']


def main(src_dir=None):
    import pyarrow.parquet as pq
    tmp = src_dir or os.path.join(HERE, 'corpora', '_ashaar')
    os.makedirs(tmp, exist_ok=True)
    lines = []
    for f in FILES:
        p = os.path.join(tmp, f)
        if not os.path.exists(p):
            req = urllib.request.Request(BASE + f, headers={'User-Agent': 'Mozilla/5.0 (research script)'})
            open(p, 'wb').write(urllib.request.urlopen(req, timeout=600).read())
        t = pq.read_table(p, columns=['poet_era', 'poem_verses'])
        for era, verses in zip(t.column('poet_era').to_pylist(), t.column('poem_verses').to_pylist()):
            if era not in ERAS or not verses:
                continue
            for a, b in zip(verses[0::2], verses[1::2]):
                lines.append(f'{a} {b}')
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    print(f'{OUT}: {len(lines)} verses')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else None)
