import sys, os, shutil, json
from PIL import Image
R = sys.argv[1]; G2 = sys.argv[2]; out = sys.argv[3]
regions = {  # image: (file, y0, y1)
 '0019': ('0019_502968547.jpg', 1030, 1450),
 '0027': ('0027_502968555.jpg', 400, 1490),
 '0035': ('0035_502968563.jpg', 0, 2110),
 '0041': ('0041_502968569.jpg', 700, 2134),
 '0042': ('0042_502968570.jpg', 0, 560),
 '0122': ('0122_502968650.jpg', 1870, 2142),
 '0123': ('0123_502968651.jpg', 0, 1600),
 '0183': ('0183_502968711.jpg', 880, 1780),
}
# sections in the order shown to the readers; seeds are gloss2 strips
batches = {
 'batch1': [('sec01', ['seed:S09']), ('sec02', ['0027']), ('sec03', ['0019']), ('sec04', ['seed:S06']), ('sec05', ['0035'])],
 'batch2': [('sec06', ['0122','0123']), ('sec07', ['seed:S31']), ('sec08', ['0041','0042']), ('sec09', ['0183']), ('sec10', ['seed:S18'])],
}
H, OV = 360, 80
key = []
for b, secs in batches.items():
    os.makedirs(os.path.join(out, b), exist_ok=True)
    for sec, parts in secs:
        n = 0
        for p in parts:
            if p.startswith('seed:'):
                n += 1; name = f'{sec}_s{n:02d}.png'
                shutil.copy(os.path.join(G2, p[5:] + '.png'), os.path.join(out, b, name))
                key.append((b, name, p, '', '')); continue
            f, y0, y1 = regions[p]
            im = Image.open(os.path.join(R, f))
            y = y0
            while True:
                ye = min(y + H, y1)
                n += 1; name = f'{sec}_s{n:02d}.png'
                im.crop((0, y, im.width, ye)).save(os.path.join(out, b, name))
                key.append((b, name, p, y, ye))
                if ye >= y1: break
                y = ye - OV
with open(os.path.join(out, 'strip_key.tsv'), 'w') as fh:
    fh.write('batch\tstrip\tsource\ty0\ty1\n')
    for r in key: fh.write('\t'.join(map(str, r)) + '\n')
print(len(key))
