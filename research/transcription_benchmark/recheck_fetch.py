"""Re-check of model-made transcriptions in the corpus: fetch page images of DECODE records into decode_cache/R<rec>/.
Usage: python recheck_fetch.py COOKIE_FILE REC [REC ...]"""
import sys
import time

import draw2

cookie = open(sys.argv[1]).read().strip().replace("\n", "").replace("\r", "")
for rec in sys.argv[2:]:
    meta = draw2.record_page(rec, cookie)
    d = draw2.CACHE / f"R{rec}"
    d.mkdir(parents=True, exist_ok=True)
    n = 0
    for name in meta["images"]:
        p = d / name
        if p.exists() and p.stat().st_size > 20000:
            n += 1
            continue
        data = draw2.get(f"https://de-crypt.org/decrypt-custom/filesrv/?file={name}", cookie)
        if len(data) == 17947 and data[:4] == b"\x89PNG":
            print("forbidden placeholder:", name)
            continue
        p.write_bytes(data)
        n += 1
        time.sleep(2)
    print(f"R{rec}: {n}/{len(meta['images'])} images; docs {[x['label'] for x in meta['docs']]}", flush=True)
    time.sleep(1)
