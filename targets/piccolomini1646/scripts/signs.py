"""Sign counts for the 2358 transcriptions (the figures in NOTES.md). Standard library only.

    python scripts/signs.py

For each reconciled transcription: signs (one per token; [?] counts as one, a doubt mark '?' as none), even digits
and zero by digit, plain vowel letters and w by letter, and class tokens S and G.
"""
import collections, pathlib, re, sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from decrypt import tokens

for doc in ('24874', '24876'):
    toks = []
    for line in (ROOT / f'transcription_{doc}.txt').read_text(encoding='utf-8').splitlines():
        m = re.match(r'^L\d\d\t(.*)$', line)
        if m:
            for w in m.group(1).split():
                toks += tokens(w)
    c = collections.Counter(toks)
    even = {d: c[d] for d in '24680' if c[d]}
    plain = {v: c[v] for v in 'aeiouwxy' if c[v]}
    print(f'{doc}: signs {len(toks)}; even digits and zero {sum(even.values())} {even}; '
          f'plain vowel letters and w {sum(plain.values())} {plain}; S {c["S"]}, G {c["G"]}, 5 {c["5"]}')
