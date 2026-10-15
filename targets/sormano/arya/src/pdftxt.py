"""Minimal PDF text extractor: inflate FlateDecode streams, pull strings from Tj/TJ operators."""
import re, zlib, sys

def texts(path):
    d = open(path,'rb').read()
    out = []
    for m in re.finditer(rb'stream\r?\n?', d):
        s = m.end()
        e = d.find(b'endstream', s)
        if e < 0: continue
        raw = d[s:e]
        try:
            dec = zlib.decompress(raw)
        except Exception:
            try: dec = zlib.decompressobj().decompress(raw)
            except Exception: continue
        if b'Tj' not in dec and b'TJ' not in dec: continue
        out.append(dec)
    return out

def unescape(b):
    b = re.sub(rb'\\([0-7]{1,3})', lambda m: bytes([int(m.group(1),8)&0xFF]), b)
    for a,c in ((rb'\\n',b'\n'),(rb'\\r',b'\r'),(rb'\\t',b'\t'),(rb'\\\(',b'('),(rb'\\\)',b')'),(rb'\\\\',b'\\')):
        b = re.sub(a, lambda m, c=c: c, b)
    return b

def page_text(dec):
    parts=[]
    for m in re.finditer(rb'\((?:[^()\\]|\\.)*\)', dec):
        parts.append(unescape(m.group(0)[1:-1]))
    return b' '.join(parts)

if __name__ == '__main__':
    blobs = texts(sys.argv[1])
    print(f'# {len(blobs)} content streams', file=sys.stderr)
    all_t = []
    for b in blobs:
        t = page_text(b)
        try: t = t.decode('latin-1')
        except Exception: t = str(t)
        all_t.append(t)
    full = '\n'.join(all_t)
    open(sys.argv[2],'w',encoding='utf-8').write(full)
    print(f'# {len(full)} chars written to {sys.argv[2]}', file=sys.stderr)
