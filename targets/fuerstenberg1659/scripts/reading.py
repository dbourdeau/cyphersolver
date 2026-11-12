"""Reading check for fuerstenberg1659. Standard library only.

    python scripts/reading.py check

Strips the marks from the marked block of reading_fuerstenberg1659.md back to what the signs give ({x/y} -> x) and
compares, letter for letter, with decryption_fuerstenberg1659.txt run by run. Any difference that is not marked
fails. A letter from an uncertain sign ('?' in the transcription and the decryption) must be marked {x?} in the
reading at the same place, or the check fails. Prints word counts: verbatim (and how many of them rest on an
uncertain sign), with a marked repair, from a gloss only (none here), holes.
"""
import pathlib, re, sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(__file__).resolve().parent.parent
md = (ROOT / 'reading_fuerstenberg1659.md').read_text(encoding='utf-8')
block = md.split('```marked')[1].split('```')[0]
dec = {}
for line in (ROOT / 'decryption_fuerstenberg1659.txt').read_text(encoding='utf-8').splitlines():
    if line.startswith('#'):
        continue
    lab, run, ct, pt = line.split('\t')
    dec[run] = dec.get(run, '') + pt
bad = 0
words = verb = doubt = rep = holes = 0
norm = lambda s: re.sub(r'[^a-z?]', '', s.lower().replace('j', 'i').replace('v', 'u'))
for line in block.strip().splitlines():
    run, txt = [x.strip() for x in line.split(':', 1)]
    undone = re.sub(r'\{\+[a-z]+\}', '', txt)
    undone = re.sub(r'\{([a-z])\?\}', r'\1?', undone)
    undone = re.sub(r'\{([a-z]*)/([a-z]*)\}', r'\1', undone)
    signs = norm(undone)
    if signs != dec[run]:
        bad += 1
        print(f'FAIL {run}: reading (marks undone) differs from the decryption')
        print('   reading :', signs); print('   decrypt :', dec[run])
    else:
        print(f'{run}: marks undone = mechanical decryption')
    for w in re.findall(r'[^\s,.;:]+', txt):
        words += 1
        if re.search(r'\[\.\.\.\]|\[\?|\[\d+\]', w):
            holes += 1
        elif re.search(r'\{[a-z]*/', w):
            rep += 1
        else:
            verb += 1
            if re.search(r'\{[a-z]\?\}', w):
                doubt += 1
print(f'words {words}: verbatim {verb} ({100*verb/words:.1f}%; {doubt} of them on an uncertain sign), '
      f'marked repair {rep}, gloss only 0, holes {holes}')
sys.exit(1 if bad else 0)
