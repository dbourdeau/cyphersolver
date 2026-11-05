"""Create notes, worklog and profile for the three sibling targets vaudreuil1759a/b/c (run from the repository root after the folders hold transcription.txt, ct.txt, decode.txt, key/).
usage: PYTHONUTF8=1 python targets/vaudreuil1760/tools/make_sib_targets.py"""
import json, copy, os, re, subprocess, sys

sys.path.insert(0, 'targets/vaudreuil1760/tools')
import decode

os.chdir('targets/vaudreuil1760'); K = decode.load(); os.chdir('../..')
T = [
 dict(slug='vaudreuil1759a', cat=1388, date='8 Apr 1759', year=1759, sm='ANOM, COL C11A 104, ff.54-66 (CABAC_PIAF_60891)', img='LAC e000874955-e000874967 (13 images)', rec='https://nouvelle-france.org/eng/item/details?id=27478', pages=13,
      summ="Vaudreuil reports to the minister on the winter and the defence plan: famine and loss of draught animals, a British army of about 20-25 000 against Niagara, Fort Duquesne evacuated, Montcalm's absence, and numbered requests for battalions, munitions and provisions."),
 dict(slug='vaudreuil1759b', cat=1389, date='10 Apr 1759', year=1759, sm='ANOM, COL C11A 104, ff.68-72 (CABAC_PIAF_60892)', img='LAC e000874969-e000874973 (5 images)', rec='https://nouvelle-france.org/eng/item/details?id=27479', pages=5,
      summ="Vaudreuil sends the minister Montcalm's letter with his own reflections: Montcalm's way of thinking had become public among officers, bourgeois and soldiers; Vaudreuil asks that the officers who spread such talk be sent to France."),
 dict(slug='vaudreuil1759c', cat=1390, date='16 Apr 1759', year=1759, sm='ANOM, COL C11A 104, ff.75-76 (CABAC_PIAF_60895)', img='LAC e000874976-e000874977 (2 images)', rec='https://nouvelle-france.org/eng/item/details?id=27482', pages=2,
      summ="Vaudreuil asks the minister to have the munitionnaire's correspondents in France pay the freight of the ships in Canada, and presses for a supply convoy on which the colony's conservation depends."),
]
base = json.load(open('targets/vaudreuil1760/profile.json', encoding='utf8'))

for t in T:
    d = 'targets/' + t['slug']
    flag = part = 0
    for l in open(d + '/transcription.txt', encoding='utf8'):
        if l.startswith('#') or l.startswith('@'): continue
        for x in re.findall(r'\d+[?~^]*', re.sub(r'\[[^\]]*\]', '', l)):
            if x.endswith('~'): part += 1
            elif K[int(x.rstrip('?^'))].endswith('?'): flag += 1
    m = json.loads(subprocess.run([sys.executable, 'docs/_check_profile.py', '--measure', d + '/ct.txt'], capture_output=True, text=True).stdout)
    n, dist = m['tokens'], m['distinct']
    unread = flag + part; frac = round((n - unread) / n, 3)
    p = copy.deepcopy(base)
    p['target'] = t['slug']
    p['title'] = f"Vaudreuil to the minister of the Marine, cipher letter, Montréal, {t['date']}, {t['sm']} (catalogue {t['cat']})"
    doc = p['documents'][0]
    doc.update(shelfmark=f"{t['sm']}; {t['img']}", date=t['date'], year=t['year'], pages=t['pages'])
    doc['plaintext'] = {"location": ["none"], "source": "No decipherment, clear copy or edition found (catalogue vetting 3 Nov 2026; not searched again here).", "partial": False}
    doc['length'] = {"tokens": n, "distinct": dist, "unit": "code groups", "measured": True, "file": "ct.txt"}
    doc['transcription'] = {"by": "llm from images", "source": f"LAC microfilm images, {t['img']}", "corrections": 0, "image_quality": "good",
                            "notes": "Transcribed 5 Nov 2026 from enlarged half-spread crops; " + (f"{part} groups at the gutter are cut ('~' in transcription.txt, digits kept in ct.txt)." if part else "no group is cut at the gutter.")}
    doc['read'] = "read in part"
    p['system']['nomenclator']['unread_groups'] = unread
    p['system']['distinct_symbols'] = dist
    p['system']['sibling_key'] = "Key found for catalogue 1391 (vaudreuil1760): the 1757 Vaudreuil table ANOM COL C11E 10 f.289 (LAC e001295274); it fits this letter from the first line."
    p['conditions']['prior_solution'] = {"exists": "no", "found": "not found", "used": False}
    p['conditions']['inputs'] = ["images", "transcription", "key from archive", "sibling key"]
    p['conditions']['attack'] = "key from archive"
    p['conditions']['human_role'] = "Asked for the sibling letters of catalogue 1391 to be decoded and then made into targets of their own."
    p['solution'] = [
        {"date": "2026-11-05", "kind": "sibling key", "technique": ["key matching"], "what": "Table found for catalogue 1391 (same hand, same office, months apart) tried on this letter: function words fall in place.", "result": "worked"},
        {"date": "2026-11-05", "kind": "access", "what": "Images fetched from the LAC image server with curl -L (about half the requests need a retry).", "result": "worked"},
        {"date": "2026-11-05", "kind": "transcription", "what": f"Whole letter transcribed ({n} groups).", "result": "worked"},
        {"date": "2026-11-05", "kind": "reading", "technique": ["key matching", "contextual inference"], "what": f"Decoded with the table and its context-corrected cells (key/overrides.json); {flag} groups sit on a cell still doubtful and {part} are cut at the gutter; the decode reads as French throughout but no reader has reviewed it as sentences.", "result": "partial"},
    ]
    o = p['outcome']
    o['method'] = "read after matching with key from external sources"
    o['method_basis'] = "The 1757 Vaudreuil table (ANOM COL C11E 10, LAC e001295274), found to fit catalogue 1391 of the same hand, applied to this letter."
    o['contribution'] = ["transcription", "key extended or corrected"]
    o['fraction_read'] = frac; o['fraction_read_method'] = "measured"
    o['fraction_read_source'] = "transcription.txt decoded with key/key274.json + key/overrides.json (tools/decode.py): cipher groups with a settled table value; groups on a doubtful cell or cut at the gutter counted unread. Sense not yet reviewed by a reader."
    gaps = []
    if part: gaps.append({"item": f"{part} groups cut by the binding", "blocker": "illegible", "detail": "microfilm image; a clear copy would restore them"})
    if flag: gaps.append({"item": f"{flag} groups on table cells still doubtful", "blocker": "open-codes", "detail": "cells read from a small image of the table; the alphabetical key sheets e001295267/69 are not yet used to settle them"})
    gaps.append({"item": "reader review and English translation of the whole letter", "blocker": "not-attempted", "detail": "not yet done"})
    o['gaps'] = gaps
    o['verification'] = ["historical consistency"]
    o['codes_open'] = {"open": 0, "total": 0, "tokens_open": 0}
    o['texts'] = [{"doc": "A", "label": t['sm'], "transcription": ["transcription.txt", "ct.txt"], "decryption": "decode.txt", "state": "decoded, not read", "summary": t['summ'], "language": "fr", "read_share": frac}]
    o['key_file'] = ["key/key274.json", "key/overrides.json"]
    o['notes'] = "Mechanical decode with the syllabic spelling left as written; no English translation and no reader review yet. The table cells were read from the images of the volume by the same model."
    o['key'] = "partial"
    o['credits'] = [{"who": "contemporary", "role": "key or decipherment used", "note": "Vaudreuil 1757 numerical table, ANOM COL C11E 10 f.289 (LAC e001295274)"}]
    json.dump(p, open(d + '/profile.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)

    gl = ''.join(f"- {g['item']} - blocker: {g['blocker']}; {g['detail']}\n" for g in gaps)
    notes = f"""# Vaudreuil to the minister (Berryer), cipher letter, Montréal, {t['date']}

Status: in progress

Catalogue {t['cat']}. {t['sm']}; {t['img']}; [record]({t['rec']}). Pierre de Rigaud de Vaudreuil de Cavagnial, governor of New France, to the minister of the Marine. French.
{n} number groups ({dist} distinct); in clear: Monseigneur, the closing formula.

## What the document is

{t['summ']}

## System and key

Syllabary-nomenclator of 700 numbered entries (words, names, syllables, letters), the same table as catalogue 1391 (`targets/vaudreuil1760/`, where the table, its
transcription and the context corrections are described). The key is the 1757 Vaudreuil table, ANOM COL C11E 10 f.289 (LAC e001295274), copied here as
`key/key274.json` and `key/overrides.json`. It fits this letter from the first line; no group falls outside the table.

## The reading

`transcription.txt` (groups), `decode.txt` (decode, syllabic spelling as written), `ct.txt` (groups only), `tools/decode.py`. Outcome method: **external key matched**.
Measured: {frac*100:.1f}% of groups carry a settled value ({n-unread} of {n}); {flag} sit on a doubtful table cell and {part} are cut at the gutter. The decode reads as French
throughout; no reader has yet reviewed it as sentences and there is no English translation.

## Remaining gaps
{gl}
## Escalation
- [x] siblings: the other cipher letters of the same hand (cat. 1388-1391) decoded with the same table; 1392 (Trémais) uses another code
- [x] clear-pages: no clear copy or decipherment found on the leaves of this record
- [x] known-keys: both numerical sheets of C11E 10 tried; sheet e001295274 fits
- [x] print: only the catalogue's vetting (NY Colonial Documents vol. 10, web searches); nothing found
- [x] key-rebuild: table cells corrected from context across the four letters (key/overrides.json)
- [n/a] retry: the unread groups are on cells that need the alphabetical sheets; not retried here

## Files

`transcription.txt`, `decode.txt`, `ct.txt`, `key/`, `tools/`, `WORKLOG.md`, `profile.json`. Images are fetched, not stored: `curl -L "https://central.bac-lac.gc.ca/.item?id=<id>&op=img&app=nf"`.
Image credit: Library and Archives Canada (LAC) / Archives nationales d'outre-mer (ANOM), via New France Archives.
"""
    open(d + '/NOTES.md', 'w', encoding='utf8').write(notes)
    open(d + '/WORKLOG.md', 'w', encoding='utf8').write(f"""# WORKLOG {t['slug']} (catalogue {t['cat']})

5 Nov 2026.

- Split from `targets/vaudreuil1760/`: the 1757 table found for catalogue 1391 was tried on this letter (same office, 1759) and fits.
- Fetched the images from the LAC image server (curl -L; retry the requests that return nothing).
- Transcribed the whole letter ({n} groups) into `transcription.txt`; decoded it into `decode.txt`; measured `ct.txt` with `docs/_check_profile.py --measure`.
- Doubtful cells met here: {flag} group(s); {part} group(s) cut at the gutter. Cells settled on the four letters together: 452 fret, 301 trou, 133 oit, 367 crai, 195 vrai, 613 cas.
- Not done: reader review of the decode as sentences, English translation, the alphabetical key sheets for the doubtful cells, a clear copy.
""")
    open(d + '/.gitignore', 'w').write("img/\n")
    print(t['slug'], n, dist, 'flag', flag, 'part', part, 'frac', frac)
