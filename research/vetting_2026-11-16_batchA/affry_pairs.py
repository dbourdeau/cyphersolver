"""Pair the letters with Transcription/Décryptage pieces in AEF Affry 225-228 and 238 (raw/affry_rows.json).
A letter counts as paired when a transcription piece has the same date or the same dispatch number.
Writes raw/affry_summary.json."""
import json, re
r = json.load(open('raw/affry_rows.json', encoding='utf8'))
TR = re.compile(r'transcription|d[ée]cryptage|d[ée]chiffr|mis en clair|traduction', re.I)
def n(t): return set(re.findall(r'n[°o]\.?\s*(\d+)', t))
summ = {}
for ser in (225, 226, 227, 228, 238):
    items = sorted([(k, v) for k, v in r.items() if v['series'] == ser], key=lambda kv: int(re.match(r'\d+', kv[1]['num']).group()))
    tr = [(k, v) for k, v in items if TR.search(v['title'])]
    letters = [(k, v) for k, v in items if not TR.search(v['title']) and re.search(r'lettre|dépêche|document', v['title'], re.I)
               and not re.search(r'brouillon', v['title'], re.I)]
    trd = {v['date'][:10] for k, v in tr}; trn = set().union(*[n(v['title']) for k, v in tr]) if tr else set()
    ciph = [(k, v) for k, v in letters if re.search(r'chiffr', v['title'], re.I)]
    bare = [(k, v['date'], v['title'][:110]) for k, v in ciph if v['date'][:10] not in trd and not (n(v['title']) & trn)]
    summ[ser] = {"pieces_harvested": len(items), "transcription_pieces": len(tr), "letters": len(letters),
                 "letters_titled_chiffre": len(ciph), "chiffre_letters_without_matching_transcription": bare,
                 "transcription_examples": [(k, v['date'], v['title'][:100]) for k, v in tr[:6]]}
    print(ser, {k: (len(v) if isinstance(v, list) else v) for k, v in summ[ser].items()})
    for b in bare: print('    bare?', b)
json.dump(summ, open('raw/affry_summary.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
