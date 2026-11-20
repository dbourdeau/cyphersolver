from pathlib import Path
from PIL import Image
here = Path(__file__).resolve().parent
raw = here.parents[3] / 'sources/raw/codex_2026-11-17b/modena34r_native'
band = Image.new('RGB',(4240,670))
for i,x in enumerate((920,1980,3040,4100)):
    with Image.open(raw/f'band_{x}.jpg') as tile:
        assert tile.size == (1060,670)
        band.paste(tile,(1060*i,0))
scale = 5504/1200
first,stop = round(210*scale),round(1110*scale)
for tag,y,height in [('a',162,54),('b',216,54)]:
    strip = Image.new('RGB',(stop-first,round(height*scale)))
    for absolute in range(first,stop):
        fraction = (absolute-first)/(stop-first-1)
        top = round((y-18*fraction)*scale)-620
        left = absolute-920
        strip.paste(band.crop((left,top,left+1,top+strip.height)),(absolute-first,0))
    strip.save(here/f'row_{tag}.png')
    strip.thumbnail((1032,160))
    strip.save(here/f'preview_{tag}.png')
