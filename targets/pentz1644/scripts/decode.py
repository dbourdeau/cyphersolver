"""Decode the frozen held-out transcription with the frozen key v3 (index-switched; table carried across lines; T1 at start).
usage: python3 -I scripts/decode.py   (run from the target folder) -> decryptions/<doc>.txt"""
import json, pathlib
H = pathlib.Path(__file__).resolve().parent.parent
key = json.loads((H / 'key_history/KEY-v3.json').read_text())
docs = json.loads((H / 'transcriptions/HELDOUT.json').read_text())['docs']
for d, v in docs.items():
    tab = 'T1'; out = []
    for n, line in enumerate(v['lines'], 1):
        s = []
        for g in line:
            if isinstance(g, str): s.append(f' "{g}" '); continue
            if str(g) in key['index']: tab = key['index'][str(g)]; s.append('|'); continue
            if g >= 100: s.append(f'[{g}]'); continue
            s.append(key[tab].get(str(g), f'({g}?)'))
        out.append(f'L{n:02d} ' + ''.join(s).strip())
    (H / 'decryptions' / f'{d}.txt').write_text('\n'.join(out) + '\n')
    print(d); print('\n'.join(out))
