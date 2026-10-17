"""Recount the supplied CTTS transcription, draw the key and verify one short excerpt.

Run with Python 3 and Pillow. No full mechanical decipherment is generated.
Italian readings follow the contributor's current edited files. English translations
were revised for this publication. Only five physical cipher lines are deciphered here.
"""
from pathlib import Path
from collections import Counter, defaultdict
import base64
import hashlib
import html
import json
import re
import unicodedata

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SLUG = 'siena2023'


def load_key():
    key = {}
    for line in (HERE / 'key.txt').read_text(encoding='utf-8-sig').splitlines():
        if ' - ' not in line:
            continue
        signs, value = line.split(' - ', 1)
        for sign in signs.split('|'):
            assert sign not in key, sign
            key[sign] = value
    assert key['#'] == '[Tartaglia?]'  # a real cipher sign, not a comment
    return key


def rows(record):
    return [[x for x in line.split(';') if x] for line in
            (HERE / f'R{record}_transcription.txt').read_text(encoding='utf-8-sig').splitlines()
            if line.strip() and not line.startswith('# ')]


def normalize(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text.lower().replace('u', 'v'))
                   if c in 'abcdefghijklmnopqrstuvwxyz')


def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8', newline='\n')


def is_cipher(sign):
    return sign != '.' and not sign.startswith('CLEAR')


def build():
    key = load_key()
    counts = Counter()
    docs = {}
    for rid in (4808, 4811):
        rr = rows(rid)
        cc = Counter(x for row in rr for x in row)
        counts.update(cc)
        cipher = {x: n for x, n in cc.items() if is_cipher(x)}
        docs[str(rid)] = {
            'lines': len(rr), 'selections': cc.total(),
            'excluded_punctuation_or_cleartext': sum(n for x,n in cc.items() if not is_cipher(x)),
            'cipher_tokens': sum(cipher.values()), 'distinct_cipher_signs': len(cipher),
            'null_tokens': sum(n for x, n in cipher.items() if key.get(x) == '_'),
            'unmapped': {x: n for x, n in cipher.items() if x not in key},
            'bracketed_assignments': {x: n for x, n in cipher.items() if key.get(x, '').startswith('[')},
        }
        # Prefix prevents the repository counter from treating the '#' sign as a comment.
        encoded = [' '.join('g:' + x for x in row if is_cipher(x)) for row in rr]
        (HERE / f'R{rid}_cipher_tokens.txt').write_text('\n'.join(encoded) + '\n', encoding='utf-8', newline='\n')
    letter_counts = Counter(value for sign, value in key.items() if re.fullmatch('[A-Z]', value))
    allcipher = {x: n for x, n in counts.items() if is_cipher(x)}
    summary = {
        'documents': docs, 'total_selections': counts.total(),
        'cipher_tokens': sum(allcipher.values()), 'distinct_cipher_signs': len(allcipher),
        'null_signs': sorted(x for x in allcipher if key.get(x) == '_'),
        'null_tokens': sum(n for x, n in allcipher.items() if key.get(x) == '_'),
        'letter_signs': sum(letter_counts.values()), 'homophones_per_letter': dict(sorted(letter_counts.items())),
        'certain_multiletter_assignments': {s: v for s, v in key.items() if is_cipher(s) and len(v) > 1 and v.isalpha()},
        'bracketed_assignments': {s: v for s, v in key.items() if is_cipher(s) and v.startswith('[')},
        'unread_signs': {s: n for s,n in allcipher.items() if key.get(s) == '?'},
        'unmapped': {s: n for s, n in allcipher.items() if s not in key},
        'note': 'Counts describe the supplied transcription and working key, not independently verified reading accuracy.'
    }
    write_json(HERE / 'counts.json', summary)

    # The only decoded passage: exactly five physical lines, no. 23 CTTS L6-L10.
    excerpt = []
    for ln, row in enumerate(rows(4811), 1):
        for item, sign in enumerate(row, 1):
            if 6 <= ln <= 10:
                value = key[sign]
                assert value == '_' or re.fullmatch('[A-Z]+', value), (ln, item, sign, value)
                excerpt.append({'line': ln, 'item': item, 'sign': sign, 'value': value})
    display = '\n'.join(''.join(e['value'] for e in excerpt if e['line']==ln and e['value']!='_') for ln in range(6,11))
    decoded = ''.join(e['value'] for e in excerpt if e['value'] != '_')
    assert decoded.lower() == normalize(display)
    assert normalize(display) in normalize((HERE / 'R4811_reading.txt').read_text(encoding='utf-8'))
    (HERE / 'excerpt.txt').write_text(display + '\n', encoding='utf-8', newline='\n')
    write_json(HERE / 'excerpt.json', {
        'record': 'R4811', 'range': 'CTTS lines 6–10, complete physical lines',
        'display': display, 'tokens': excerpt,
        'normalization': 'Literal uppercase key values, V for u/v, provisional nulls omitted. Physical line breaks retained. No spelling correction, spacing, letter substitution or gap filling. Lines begin/end within words.'
    })
    (HERE / 'validation.tsv').write_text(
        '# model: it-cinquecento\n# source: excerpt.json ONLY, R4811 L6-L10\n'
        '# note: Selected agreement excerpt; not a validation of both complete readings or the whole key.\n' +
        ''.join(f'g:{e["sign"]}\t{"-" if e["value"] == "_" else e["value"].lower()}\n' for e in excerpt), encoding='utf-8', newline='\n')
    write_json(ROOT / 'docs/reveal/siena2023.json', {
        'slug': SLUG, 'anchor': 'excerpt', 'title': 'Five physical lines checked against the current edition',
        'caption': 'No. 23, CTTS L6-L10. Only these five lines are mechanically deciphered. The complete readable editions retain editorial interventions.',
        'unit': 'sign', 'key_note': 'Literal key values use V for u/v; provisional nulls have no sound. No letters are corrected or supplied.',
        'tokens': [{'g': e['sign'], 'p': '' if e['value'] == '_' else e['value'],
                    'cls': 'null' if e['value'] == '_' else ''} for e in excerpt]
    })
    draw_key(key, counts)
    print(json.dumps(summary, ensure_ascii=False, indent=1))
    print('Excerpt verified:', len(excerpt), 'cipher signs;', len(decoded), 'letters. No complete mechanical decipherment written.')


def draw_key(key, counts):
    from PIL import Image, ImageDraw, ImageFont
    glyphs = json.loads((HERE / 'glyphs.json').read_text(encoding='utf-8'))
    groups = defaultdict(list)
    for sign in counts:
        if not is_cipher(sign):
            continue
        value = key.get(sign, '?')
        group = 'Alphabet' if re.fullmatch('[A-Z]', value) else 'Nulls (provisional)' if value == '_' else 'Words and letter groups' if value.isalpha() else 'Uncertain and unidentified'
        groups[group].append((value, sign))
    ordered = ['Alphabet', 'Words and letter groups', 'Nulls (provisional)', 'Uncertain and unidentified']
    width, cell_w, cell_h, top = 1440, 176, 150, 186
    height = top + sum(48 + ((len(groups[g]) + 7) // 8) * cell_h for g in ordered) + 70
    canvas = Image.new('RGB', (width, height), '#f6f7fc')
    d = ImageDraw.Draw(canvas)
    def font(size, bold=False):
        choices = [Path('C:/Windows/Fonts') / ('arialbd.ttf' if bold else 'arial.ttf'),
                   Path('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')]
        return ImageFont.truetype(str(next(p for p in choices if p.exists())), size)
    f, small, big = font(20, True), font(15), font(34, True)
    d.text((20, 16), 'Siena 20 & 23 · DECODE R4808 / R4811', font=big, fill='#101d54')
    total=sum(n for s,n in counts.items() if is_cipher(s))
    distinct=sum(is_cipher(s) for s in counts)
    for y, text in [(66, 'George Lasry · transcribed with CTTS, then solved by GPT-6 Astra · working key: 17 October 2026'),
                    (96, f'{total:,} cipher selections · {distinct} sign classes · brackets and ? mark unresolved values'),
                    (126, 'Paolo Orsini, Sforza and Tartaglia are tentative identifications. # and e may refer to different people.'),
                    (153, 'Counts and glyphs are from the supplied CTTS snapshot. Null assignments remain provisional.')]:
        d.text((20, y), text, font=small, fill='#374368')
    cards = []
    yy = top
    for group in ordered:
        d.rectangle((16, yy, width-16, yy+35), fill='#e2e7fb')
        d.text((25, yy+5), group, font=f, fill='#173db2')
        yy += 48
        for i, (value, sign) in enumerate(sorted(groups[group])):
            x, y = 16+(i%8)*cell_w, yy+(i//8)*cell_h
            d.rectangle((x, y, x+cell_w-8, y+cell_h-9), fill='white', outline='#bcc6e6')
            label = 'NULL?' if value == '_' else value
            d.text((x+10, y+6), label, font=f if len(label)<13 else small, fill='#173db2')
            iconpath = HERE / glyphs[sign]['file']
            icon = Image.open(iconpath).convert('RGBA')
            icon.thumbnail((78,78), Image.Resampling.LANCZOS)
            canvas.paste(icon, (x+(cell_w-8-icon.width)//2,y+33+(78-icon.height)//2), icon)
            d.text((x+9,y+116), f'{sign} · {counts[sign]} uses', font=small, fill='#374368')
            encoded = base64.b64encode(iconpath.read_bytes()).decode()
            cards.append(f'<article><b>{html.escape(label)}</b><img src="data:image/png;base64,{encoded}" alt="CTTS sign {html.escape(sign)}"><p>{html.escape(sign)} · {counts[sign]} uses</p></article>')
        yy += ((len(groups[group])+7)//8)*cell_h
    d.text((20, height-54), 'Glyphs: Archivio di Stato di Siena, Concistoro 2308 fasc. 2 nos. 20, 23, via DECODE; CTTS samples.', font=small, fill='#374368')
    d.text((20, height-30), 'CLEAR1-CLEAR4 are original clear-script passages and are excluded. Name3-Name6 and erased text remain unresolved.', font=small, fill='#374368')
    canvas.save(HERE / 'visual_key.png')
    (HERE / 'visual_key.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><title>Siena 20 &amp; 23 — visual key</title><style>body{font:16px system-ui;margin:24px;color:#172044;background:#f6f7fc}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px}article{background:white;border:1px solid #bcc6e6;text-align:center;padding:12px}article img{display:block;width:85px;height:85px;object-fit:contain;margin:auto}b{color:#173db2}</style><h1>Siena 20 &amp; 23 — visual key</h1><p>George Lasry. Transcribed with CTTS, then solved by GPT-6 Astra. Working key of 17 October 2026. '+f'{total:,} cipher selections, {distinct} sign classes.'+'</p><p>Bracketed names are hypotheses; NULL? is provisional. # and e may name different people. CLEAR1-CLEAR4 are original clear-script passages and are excluded from this chart.</p><main>'+''.join(cards)+'</main><p>Glyphs: Archivio di Stato di Siena, Concistoro 2308 fasc. 2 nos. 20 and 23, via DECODE R4808/R4811; CTTS samples. Full manuscript images are not included.</p></html>', encoding='utf-8', newline='\n')


if __name__ == '__main__':
    build()
