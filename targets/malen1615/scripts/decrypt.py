"""Mechanical decryption for the Van Malen letters. Standard library only.
    python decrypt.py transcription_<doc>.txt key_frozen.tsv
Transcription lines 'Lnn: ...'; clear script in <...> is copied as is; cipher signs are one capital code each;
'?' (unread sign) and '&' (heavy looped sign, not identified) print '?'; a code not in the key prints '?'.
Punctuation is copied."""
import re, sys
sys.stdout.reconfigure(encoding='utf-8')
key = {}
for l in open(sys.argv[2], encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    c, p = l.rstrip('\n').split('\t')[:2]; key[c] = p
for l in open(sys.argv[1], encoding='utf-8'):
    m = re.match(r'(L\d+):\s?(.*)$', l.rstrip('\n'))
    if not m: continue
    parts = re.split(r'(<[^>]*>)', m.group(2))
    out = ''.join(p if p.startswith('<') else ''.join(key.get(c, '?') if (c.isupper() or c in '?&') else c for c in p) for p in parts)
    print(f'{m.group(1)}: {out}')
