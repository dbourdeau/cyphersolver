"""Sign counts for profile.json length. Standard library only.   python scripts/signs.py transcription_<doc>.txt
Counts the cipher signs outside clear script <...>: one token per capital code, '?' (unread sign) and '&' (heavy
looped sign, not identified) count as one token each; distinct counts the capital codes only. Figures (59, 60, 68)
are clear script and are counted apart."""
import collections, re, sys
sys.stdout.reconfigure(encoding='utf-8')
toks, figs = [], []
for l in open(sys.argv[1], encoding='utf-8'):
    m = re.match(r'(L\d+):\s?(.*)$', l.rstrip('\n'))
    if not m: continue
    for part in re.split(r'(<[^>]*>)', m.group(2)):
        if part.startswith('<'): figs += re.findall(r'\b(59|60|68)\b', part); continue
        toks += [c for c in part if c.isupper() or c in '?&']
c = collections.Counter(t for t in toks if t.isalpha())
print(f'tokens {len(toks)} (of which unread ? {toks.count("?")}, & {toks.count("&")}); distinct codes {len(c)}; '
      f'code numbers {len(figs)} occurrences, {len(set(figs))} distinct: {dict(collections.Counter(figs))}')
