"""Build the Hebrew corpus for the he-tanakh model: the Hebrew Bible (consonantal text with points) from the Sefaria API.

Sefaria's Hebrew Tanakh text is the Miqra al-Masorah edition (public domain text). Fetches the books below, one API call
per book, one verse per line. Output: lang/corpora/he-sefaria-tanakh.txt (git-ignored).  Run: python -m lang.build_he_tanakh
"""
import json, os, re, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'corpora', 'he-sefaria-tanakh.txt')
BOOKS = ['Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy', 'Joshua', 'Judges', 'I_Samuel', 'II_Samuel',
         'I_Kings', 'II_Kings', 'Isaiah', 'Jeremiah', 'Ezekiel', 'Psalms', 'Proverbs', 'Job', 'Ecclesiastes', 'Esther',
         'Daniel', 'Ezra', 'Nehemiah', 'I_Chronicles', 'II_Chronicles']


def flat(x):
    if isinstance(x, str):
        yield x
    else:
        for y in x:
            yield from flat(y)


def main():
    lines = []
    for b in BOOKS:
        n = 1
        c = 1
        while c <= n:
            u = f'https://www.sefaria.org/api/texts/{b}.{c}?lang=he&context=0&commentary=0'
            d = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0 (research script)'}), timeout=120).read())
            n = d.get('length') or n
            for v in flat(d['he']):
                v = re.sub(r'<[^>]+>', ' ', v)
                v = re.sub(r'&[a-z]+;', ' ', v)
                lines.append(v.strip())
            c += 1
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    print(OUT, len(lines), 'verses')


if __name__ == '__main__':
    main()
