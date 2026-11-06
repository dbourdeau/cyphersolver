"""Find undeciphered cipher notes in the DBNL XML of Briefwisseling van Hugo Grotius; print letter no., header, ms location.
python -I bhg_grep.py <dir with vNN.xml>"""
import re, sys, os, glob
PAT = re.compile(r'niet kunnen (de|ont)c[oi]\w+|niet kunnen oplossen|cijfer is mij onbekend|zonder sleutel niet|betekenis van dit cijfer|niet te ontcijferen|niet ontcijferd|onontcijferd', re.I)
for f in sorted(glob.glob(os.path.join(sys.argv[1], 'v*.xml'))):
    t = open(f, encoding='utf-8').read()
    for m in PAT.finditer(t):
        # find the enclosing letter: last <div ... id="aNNNN"> before
        start = max(t.rfind('id="a', 0, m.start()), 0)
        hdr = re.sub(r'<[^>]+>', ' ', t[start:start + 1500])
        hdr = re.sub(r'\s+', ' ', hdr)[:600]
        ctx = re.sub(r'<[^>]+>', ' ', t[m.start() - 700:m.end() + 200])
        ctx = re.sub(r'\s+', ' ', ctx)
        print('=====', os.path.basename(f), t[start:start+12])
        print('HDR:', hdr)
        print('CTX:', ctx)
