"""Load the block transcriptions as token lists (clear text and '?' marks stripped)."""
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
FILES = {b: f'transcription/{b.lower()}_transcription.txt' for b in 'ABCD'}

def lines(block):
    out = []
    for l in (ROOT / FILES[block]).read_text(encoding='utf-8').splitlines():
        if l[:1] == block and l[1:3].isdigit():
            body = re.sub(r'\[\[.*?\]\]', '', l.split(None, 1)[1])
            out.append((l[:3], [t.rstrip('?.') for t in body.split() if t.rstrip('?.')]))
    return out

def blocks():
    return {b: [t for _, ts in lines(b) for t in ts] for b in FILES}

NOT_CODE = {'gto'}   # a letter sign (one in Lannoy's alphabet too, Kolosova 2017 p. 65; here t), not a code word

def is_code(t):
    return re.fullmatch(r'[a-z]{3}', t) is not None and t not in NOT_CODE
