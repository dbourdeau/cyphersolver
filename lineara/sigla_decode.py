"""Read SigLA's public serialized dataset without executing JavaScript.

Binary format: OCaml runtime/caml/intext.h (5.3). Positional layout was
identified using Tsirkas's extract_sigla.py as a guide, then retained explicitly
for validation against SigLA's interface. This is not an independent discovery
of that layout. Unsupported encodings fail closed.

SigLA data/drawings: Salgarella & Castellan, CC BY-NC-SA 4.0.
"""
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re
import struct
import urllib.request

ROOT = Path(__file__).resolve().parent

@dataclass
class Node:
    tag: int
    fields: list

class Reader:
    def __init__(self, raw):
        magic, length, objects, _, _ = struct.unpack('>5I', raw[:20])
        assert magic == 0x8495A6BE and len(raw) == length+20
        self.raw, self.pos, self.objects, self.expected = raw, 20, [], objects

    def take(self, n):
        end = self.pos+n
        if end > len(self.raw):
            raise ValueError('truncated Marshal object')
        b, self.pos = self.raw[self.pos:end], end
        return b

    def number(self, n, signed=False):
        return int.from_bytes(self.take(n), 'big', signed=signed)

    def block(self, size, tag):
        node = Node(tag, [])
        if size:
            self.objects.append(node)
        node.fields.extend(self.value() for _ in range(size))
        return node

    def string(self, size):
        s = self.take(size).decode('utf8')
        self.objects.append(s)
        return s

    def value(self):
        code = self.number(1)
        if code >= 128:
            return self.block((code >> 4) & 7, code & 15)
        if code >= 64:
            return code & 63
        if code >= 32:
            return self.string(code & 31)
        if code in range(4):
            return self.number(2**code, signed=True)
        if code in (4, 5, 6, 20):
            n = self.number({4:1,5:2,6:4,20:8}[code])
            assert 0 < n <= len(self.objects)
            return self.objects[-n]
        if code in (8, 19):
            h = self.number(4 if code == 8 else 8)
            return self.block(h >> 10, h & 255)
        if code in (9, 10, 21):
            return self.string(self.number({9:1,10:4,21:8}[code]))
        if code in (11, 12):
            v = struct.unpack(('>' if code == 11 else '<')+'d', self.take(8))[0]
            self.objects.append(v)
            return v
        raise ValueError(f'Unsupported Marshal code {code:#x}, offset {self.pos-1}')

    def read(self):
        value = self.value()
        assert self.pos == len(self.raw), (self.pos,len(self.raw))
        assert len(self.objects) == self.expected, (len(self.objects),self.expected)
        return value

def load(path):
    source = Path(path).read_text(encoding='utf8')
    blobs = {}
    for key in ['signs','data']:
        body = re.search(r"var\s+"+key+r"\s*=\s*'(.*?)';", source, re.S)[1]
        assert re.sub(r'\\\\[0-9]{3}', '', body) == '""'
        raw = bytes(int(x) for x in re.findall(r'\\\\([0-9]{3})',body))
        blobs[key] = Reader(raw).read()
    return blobs

def items(tree):
    if tree == 0:
        return
    assert isinstance(tree,Node) and tree.tag == 0 and len(tree.fields)==5
    left,key,value,right,height = tree.fields
    yield from items(left)
    yield key,value
    yield from items(right)

def plain(v):
    if isinstance(v,Node):
        return {'tag':v.tag,'fields':[plain(x) for x in v.fields]}
    return v

def extract():
    dest = ROOT/'data/sigla_database.js'
    url = 'https://sigla.phis.me/database.js'
    if not dest.exists():
        dest.write_bytes(urllib.request.urlopen(url,timeout=30).read())
    blobs = load(dest)
    out = []
    for name,wrapped in items(blobs['data'].fields[0]):
        document = wrapped.fields[0]
        meta = document.fields[0]
        attestations = []
        for att in document.fields[4].fields:
            assert len(att.fields)==8
            sign_id,confidence,values = None,None,[]
            label = att.fields[1]
            variant = None
            if isinstance(label,Node):
                spec,confidence = label.fields
                sign,variant = spec.fields
                series,number,pronunciations = sign.fields[:3]
                sign_id = f'{series}{number:03d}'
                values = plain(pronunciations)
            attestations.append({'n':att.fields[2], 'sign_id':sign_id,
                'confidence_raw':confidence, 'variant_raw':plain(variant),
                'values_raw':values, 'function_or_bounds_raw':plain(att.fields[3]),
                'erasure_raw':att.fields[4], 'flag5_raw':att.fields[5],
                'ghost_raw':att.fields[6], 'bbox_raw':plain(att.fields[7])})
        out.append({'name':name,'kind_raw':meta.fields[0], 'site':meta.fields[2],
                    'period_raw':plain(meta.fields[7]), 'path_raw':plain(document.fields[1]),
                    'attestations':attestations})
    (ROOT/'data/sigla_decoded.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
    receipt = {'url':url,'access_date':'2026-09-23',
        'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),
        'attribution':'Ester Salgarella and Simon Castellan, SigLA',
        'license':'CC BY-NC-SA 4.0', 'license_url':'https://creativecommons.org/licenses/by-nc-sa/4.0/',
        'documents':len(out),'attestations':sum(len(d['attestations']) for d in out),
        'decoder_validation':'Byte lengths and declared object counts verified for both Marshal blobs; semantic interpretation of positional fields requires additional checks.',
        'layout_prior_source':'https://github.com/ChristosTsirkas/corpus-validation-for-undeciphered-scripts-linear-a/blob/main/src/extract_sigla.py'}
    (ROOT/'sigla_manifest.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
    print(json.dumps(receipt,indent=2))

if __name__ == '__main__':
    extract()
