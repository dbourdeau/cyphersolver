"""Count the supplied CTTS snapshot; render its key; decode only five manuscript lines.

Python 3 + Pillow. No full mechanical decipherment is produced. The edited text
and translation are immutable contributor inputs, not output of this script.
"""
from pathlib import Path
from collections import Counter
import base64
import html
import json
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

def dump(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1)+'\n', encoding='utf-8')

def load():
    key = {}
    for line in (HERE/'key.txt').read_text(encoding='utf-8-sig').splitlines():
        if line.startswith('#') or ' - ' not in line:
            continue
        signs, value = line.split(' - ', 1)
        for sign in signs.split('|'):
            assert sign not in key
            key[sign] = value
    rows = [[x for x in line.split(';') if x] for line in
            (HERE/'transcription.txt').read_text(encoding='utf-8-sig').splitlines()
            if line.strip() and not line.startswith('#')]
    return key, rows

def build():
    key, rows = load()
    counts = Counter(x for row in rows for x in row)
    dates = {'285', 'd13'}
    nulls = {k for k,v in key.items() if v == '_'}
    codes = {k for k,v in key.items() if v.startswith('[code')}
    letters = {k for k,v in key.items() if len(v) == 1 and v.isalpha()}
    info = dict(rows=len(rows), selections=sum(counts.values()),
                cipher_elements=sum(n for c,n in counts.items() if c not in dates),
                distinct_cipher_elements=len(set(counts)-dates),
                date_numerals=sum(counts[c] for c in dates),
                letter_occurrences=sum(counts[c] for c in letters),
                letter_assignments=len(letters), observed_letter_types=len(set(counts)&letters),
                null_classes_in_key=len(nulls), observed_null_classes=len(set(counts)&nulls),
                null_occurrences=sum(counts[c] for c in nulls),
                unresolved_codes={c:counts[c] for c in sorted(codes)},
                unused_key_assignments=sorted(set(key)-set(counts)),
                occurrences=dict(sorted(counts.items())))
    assert (info['selections'],info['cipher_elements'],info['distinct_cipher_elements']) == (463,461,40)
    assert set(counts) <= set(key)
    dump(HERE/'counts.json',info)
    (HERE/'cipher_tokens.txt').write_text('\n'.join(' '.join(x for x in row if x not in dates) for row in rows)+'\n',encoding='utf-8')
    excerpt = []
    tokens = []
    for lineno,row in enumerate(rows[:5],1):
        values = [key[x] for x in row]
        plain = ''.join(v for v in values if v != '_')
        excerpt.append({'line':lineno,'cipher':row,'literal':plain})
        tokens.extend({'g':x,'p':'' if key[x]=='_' else key[x],
                       'cls':'null' if key[x]=='_' else ''} for x in row)
    literal = '\n'.join(e['literal'] for e in excerpt)+'\n'
    assert len(literal.strip().splitlines()) == 5
    (HERE/'mechanical_excerpt.txt').write_text(literal,encoding='utf-8')
    dump(HERE/'mechanical_excerpt.json',{'scope':'CTTS lines 1–5, complete lines, in manuscript order','lines':excerpt})
    (HERE/'validation.tsv').write_text('# model: nl-modern\n# source: mechanical_excerpt.json, CTTS lines 1–5 only\n# note: 62 literal letters; below the validator 80-letter threshold.\n'+''.join(t['g']+'\t'+(t['p'] or '-')+'\n' for t in tokens),encoding='utf-8')
    dump(ROOT/'docs/reveal/sweden4306.json',dict(slug='sweden4306',anchor='mechanical',
         title='Five manuscript lines, mechanically deciphered',
         caption='R4306, CTTS lines 1–5. Literal values only; nulls omitted. The edited reading is supplied separately.',
         unit='number',key_note='No spelling correction, word spacing, u/v normalization or gap filling.',tokens=tokens))

    glyphs=json.loads((HERE/'glyphs.json').read_text(encoding='utf-8'))
    groups=[('Alphabet — one number per letter; 45=q and 51=x are unobserved predictions',sorted(letters,key=int)),
            ('Nulls — 15 observed classes; 13 is in the working key but absent from this snapshot',sorted(nulls,key=int)),
            ('Unidentified nomenclator codes — five occurrences of four codes',sorted(codes,key=int)),
            ('Date numerals — excluded from the cipher-element count',['285','d13'])]
    width=1360
    height=230+sum(50+((len(cs)+7)//8)*142 for _,cs in groups)+55
    im=Image.new('RGB',(width,height),'#f2f3ff')
    d=ImageDraw.Draw(im)
    def font(size,bold=False):
        choices=[Path('C:/Windows/Fonts/arialbd.ttf' if bold else 'C:/Windows/Fonts/arial.ttf'),Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')]
        for p in choices:
            if p.exists(): return ImageFont.truetype(str(p),size)
        return ImageFont.load_default()
    title,head,small=font(31,True),font(21,True),font(16)
    d.text((18,16),'Sweden DECODE R4306 — reconstructed working key',font=title,fill='#17244f')
    for y,text in [(60,'George Lasry · transcribed with CTTS, then solved with Opus 5.5 · 17 October 2026'),
                   (88,'Belongs to: Riksarkivet key-box and Oxenstierna ciphers'),
                   (116,'461 cipher elements · 40 observed cipher types · 2 date-numeral selections excluded'),
                   (144,'23 alphabet positions, 21 observed; no j/v/z assignment. The source header’s “24-letter” count is incorrect.'),
                   (172,'Unresolved words and code identities remain. Numerical labels reproduce the CTTS snapshot.')]:
        d.text((18,y),text,font=small,fill='#344570')
    yy=210
    cards=[]
    for label,cs in groups:
        d.rectangle((16,yy,width-16,yy+35),fill='#dfe4ff')
        d.text((22,yy+6),label,font=head,fill='#2343a0')
        yy+=45
        for i,c in enumerate(cs):
            x=16+(i%8)*167; y=yy+(i//8)*142
            d.rectangle((x,y,x+159,y+132),fill='white',outline='#b7c4e5')
            value=key[c]
            labelvalue='NULL' if value=='_' else ('?' if c in codes else value)
            d.text((x+9,y+7),labelvalue,font=head,fill='#2343a0')
            if c in glyphs:
                path=HERE/glyphs[c]['file']
                crop=Image.open(path).convert('RGB')
                crop.thumbnail((133,66))
                im.paste(crop,(x+(159-crop.width)//2,y+38+(66-crop.height)//2))
                graphic='<img src="data:image/png;base64,'+base64.b64encode(path.read_bytes()).decode()+'" alt="Cipher '+html.escape(c)+'">'
            else:
                d.text((x+10,y+55),c+' (unseen)',font=small,fill='#6c6c7a')
                graphic='<p>Not observed; working-key entry</p>'
            d.text((x+8,y+110),f'{c} · {counts[c]} uses',font=small,fill='#344570')
            cards.append(f'<article><strong>{html.escape(labelvalue)}</strong>{graphic}<p>{html.escape(c)} · {counts[c]} uses</p></article>')
        yy+=((len(cs)+7)//8)*142+5
    d.text((18,height-35),'Glyphs: Riksarkivet, Chifferklaver låda II:133, via DECODE R4306; samples from the supplied scan.',font=small,fill='#344570')
    im.save(HERE/'visual_key.png')
    (HERE/'visual_key.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><title>R4306 — visual key</title><style>body{font:16px system-ui;margin:24px;color:#17244f;background:#f2f3ff}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px}article{background:white;padding:12px;text-align:center;border:1px solid #b7c4e5}img{display:block;max-width:130px;height:65px;object-fit:contain;margin:auto}strong{color:#2343a0}</style><h1>Sweden DECODE R4306 — visual key</h1><p>George Lasry. Transcribed with CTTS, then solved with Opus 5.5.</p><p>Belongs to: Riksarkivet key-box and Oxenstierna ciphers.</p><p>23 alphabet positions, 21 observed; 15 observed null classes; four unresolved nomenclator codes. 45=q, 51=x and null 13 are unobserved key entries. The CTTS identifiers 285 and d13 represent date numerals 23 and 13, excluded from the cipher count. Null means omitted, not a space.</p><main>'+''.join(cards)+'</main><p>Source glyphs: Riksarkivet, Chifferklaver låda II:133, via DECODE R4306. The source key is preserved separately; its “24-letter alphabet” header is a counting error.</p></html>',encoding='utf-8')
    print(json.dumps(info,ensure_ascii=False))
    print(literal)

if __name__=='__main__':
    build()
