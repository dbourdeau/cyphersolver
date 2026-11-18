"""Write the per-letter text files from readings/runs_533.tsv (Codex 533) and bare/bare_transcriptions.tsv (Codex 534
and 531), and the token-by-token validation.tsv. Run from the target folder: python scripts/make_texts.py

The first letter (L01, ff. 1r-1v) has hand-written reading and translation files (readings/L01_it.txt, L01_en.txt,
from the independent verifier's continuous text); this script writes only its groups and decode files.
"""
import json, re, pathlib

HERE = pathlib.Path('.')
OUT = HERE / 'readings'

def load(fn):
    return {k: v for k, v in json.load(open(fn, encoding='utf-8')).items() if not k.startswith('_')}

k3 = load('key/key_v3.json'); kc = load('key/key_v3_context.json')

rows = []
for l in open(OUT / 'runs_533.tsv', encoding='utf-8'):
    if l.startswith('#') or l.startswith('doc\t'):
        continue
    c = l.rstrip('\n').split('\t')
    c += [''] * (11 - len(c))
    rows.append(dict(zip('doc run folio line clear groups letters italian english read notes'.split(), c)))

docs = {}
for r in rows:
    docs.setdefault(r['doc'], []).append(r)

def mark(letters):
    return ' '.join(letters.split())

val = ['# model: it-modern', '# source: readings/runs_533.tsv (Codex 533, runs read whole or in part) and bare/bare_transcriptions.tsv (Codex 534 ff. 114r-116v, Codex 531 f. 4r)',
       '# note: one cipher group per line as written (no emendation applied to the token); reading = the letter the reading gives it; ? = unread or code number. Letters resting on context-only values (ww = o, 62 = q) are included.']

for d, rr in docs.items():
    g = [f"# {d}: cipher groups of Codex 533, run by run (transcription/reconciled_533_v2.tsv, paired as in decode/decode_rec2_v3ctx.tsv)"]
    dec = [f"# {d}: decode with key v3 + context values. Marks: x* = emended or reinterpreted digit; x+ = context-only value (ww = o, 62 = q); ? = no value. Then the normalized Italian."]
    it = [f"# {d}: the cipher runs normalized, each after the clear words that precede it on the page (clear text in lower case as transcribed, cipher in CAPITALS; [..] = hole). The rest of the clear text of the letter is not transcribed."]
    en = [f"# {d}: English of the cipher runs (cipher words in CAPITALS); [..] = hole."]
    for r in rr:
        g.append(f"# {r['run']} ({r['folio']}, line {r['line']})"); g.append(r['groups'])
        dec.append(f"{r['run']}: {mark(r['letters'])}  =>  {r['italian']}  [{r['read']}]")
        if r['read'] != 'none':
            it.append(f"{r['run']}: {r['clear']} {r['italian'].upper()}")
            en.append(f"{r['run']}: {r['english'].upper()}")
        else:
            it.append(f"{r['run']}: {r['clear']} [..]")
            en.append(f"{r['run']}: [..]")
        # validation pairs, only for runs read whole or in part
        if r['read'] in ('whole', 'most', 'part') and r['run'] != '53r a':
            for tok, let in zip(r['groups'].split(), r['letters'].split()):
                let = let.rstrip('*+')
                val.append(f"{tok}\t{let if let != '?' else '?'}")
    (OUT / f'{d}_groups.txt').write_text('\n'.join(g) + '\n', encoding='utf-8')
    (OUT / f'{d}_decode.txt').write_text('\n'.join(dec) + '\n', encoding='utf-8')
    if d != 'L01':
        (OUT / f'{d}_it.txt').write_text('\n'.join(it) + '\n', encoding='utf-8')
        (OUT / f'{d}_en.txt').write_text('\n'.join(en) + '\n', encoding='utf-8')

# bare passages: group tokens and their letters with key v3 + context; '+' joined signs split as the clerk shared them
key = dict(k3); key.update(kc)
for l in open('bare/bare_transcriptions.tsv', encoding='utf-8'):
    if l.startswith('passage'):
        continue
    c = l.rstrip('\n').split('\t')
    for tok in c[4].split():
        for t in tok.split('+'):
            t = t.lstrip('?')
            if t == '##':
                val.append('??\t?'); continue
            val.append(f"{t}\t{key.get(t, '?')}")

(HERE / 'validation.tsv').write_text('\n'.join(val) + '\n', encoding='utf-8')
print('docs', len(docs), 'validation tokens', sum(1 for v in val if not v.startswith('#')))
