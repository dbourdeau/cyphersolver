"""Pass 4 crops (python3 -I). Rebuilds the reference crops in pass4/crops/ from the full-size IIIF image of the key leaf
(canvas 205, keyleaf/IMAGE_FETCH.tsv) and from the unwraps made by keyleaf/scripts/unwrap2.py. Boxes are pixel boxes.
The checks were done with AI tools and no person checked each record by hand."""
import sys
from PIL import Image
LEAF, UNW, OUT = sys.argv[1], sys.argv[2], sys.argv[3]   # c205 full jpg, unwrap folder, output folder
im = Image.open(LEAF)
im.crop((2400,3800,3700,4150)).resize((1040,280)).save(OUT+'/f099r_ru_rum.jpg', quality=88)
im.crop((650,1950,2850,2350)).resize((1100,200)).save(OUT+'/f099r_looped_as_es_is_os_us.jpg', quality=88)
def c(p, box, out, s):
    x = Image.open(UNW+'/'+p+'.jpg').crop(box); x = x.resize((x.size[0]*s, x.size[1]*s)); x.save(OUT+'/'+out, quality=90)
c('c075_p5', (560,20,971,170), 'S1-019_sanguinis_end.jpg', 2)
c('c079_p1', (0,380,260,520), 'S1-027_timebis_end.jpg', 2)
c('c073_p4', (250,180,971,350), 'S1-012_word5.jpg', 1)
c('c095_p5', (700,180,971,350), 'S1-079_tus_a.jpg', 1)
c('c095_p5', (0,360,300,534), 'S1-079_tus_b.jpg', 1)
