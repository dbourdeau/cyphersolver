"""Fetch full MARC21 records from the KB OAI-PMH endpoint and print the readable fields.

    python marc.py 310865956 31084679X ...      (PPNs; cached in raw/marc_<ppn>.xml)

Endpoint: https://services.kb.nl/mdo/oai?verb=GetRecord&identifier=GGC:AC:<ppn>&metadataPrefix=marc21
"""
import os, sys, time, urllib.request
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, 'raw')
KEEP = {'245', '246', '260', '264', '300', '500', '505', '510', '520', '530', '533', '545', '561', '581', '600', '610',
        '650', '651', '700', '710', '773', '852', '856', '505', '541', '546', '555', '563', '590', '650', '690'}


def get(ppn):
    p = os.path.join(RAW, f'marc_{ppn}.xml')
    if not os.path.exists(p):
        url = f'https://services.kb.nl/mdo/oai?verb=GetRecord&identifier=GGC:AC:{ppn}&metadataPrefix=marc21'
        with urllib.request.urlopen(url, timeout=60) as r:
            open(p, 'wb').write(r.read())
        time.sleep(0.4)
    return open(p, 'rb').read()


def fields(xml):
    root = ET.fromstring(xml)
    out = []
    for df in root.iter():
        if df.tag.endswith('datafield') and df.get('tag') in KEEP:
            sub = ' '.join(f'${s.get("code")} {s.text}' for s in df if s.text)
            out.append((df.get('tag'), sub))
    return out


def main():
    for ppn in sys.argv[1:]:
        try:
            fs = fields(get(ppn))
        except Exception as ex:
            print(ppn, 'ERROR', ex)
            continue
        print('=====', ppn)
        for t, s in fs:
            print(' ', t, s[:900])


if __name__ == '__main__':
    main()
