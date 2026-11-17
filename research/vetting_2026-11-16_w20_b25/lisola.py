"""build proposals for the Pribram/Lisola leads from their vetting_held blocks plus today's re-checks"""
import json, subprocess, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
L = {x['id']: x for x in json.loads((ROOT/'research/leads.json').read_text(encoding='utf-8'))['leads']}
quote = {
 2511: ("no. XXIX, note at p. 148", "J Ein Bericht vom 3. Mürz ist nicht dechiffrirt [sic OCR for März]"),
 2508: ("no. LX, notes at pp. 284-285", "Zum Theile nicht dechiffrirt ... Folgt eine halbe Seite nicht dechiffrirt ... Folgt ungefähr eine nicht dechiffrirte Seite ... Folgen zwei Zeilen nicht dechiffrirt"),
 2509: ("no. LXXV, note at p. 316", "2 1/2 Seiten nicht dechiffrirt"),
 2510: ("no. LXXVI, note at p. 317", "Folgt noch eine nicht dechiffrirte Seite"),
 2512: ("no. CLX, note at p. 547", "Folgt eine nicht dechiffrirte Stelle"),
}
TODAY = ("Re-checked 16 Nov 2026: both archive.org OCR copies of Pribram, AÖG 70 (1887) downloaded (bub_gb_oIkJAAAAIAAJ_djvu.txt and "
         "bub_gb_tZ_NAAAAMAAJ_djvu.txt) and every 'dechiffrirt' note listed; the note for this report reads, in bub_gb_tZ_NAAAAMAAJ, ")
for i, (where, q) in quote.items():
    e = L[i]
    v = json.loads(json.dumps(e.get('vetting_held') or {}))
    v.pop('searches', None)
    for k in ('date', 'by'): v.pop(k, None)
    if not v:   # 2512 has no held block: build it from 2510's and change the specifics
        v = json.loads(json.dumps(L[2510]['vetting_held'])); v.pop('searches', None); v.pop('date'); v.pop('by')
        v['seen'] = {
            'kind': 'not online',
            'where': 'Pribram, Die Berichte des kaiserlichen Gesandten Franz von Lisola 1655-1660, AÖG 70 (1887), no. CLX, p. 547 (archive.org bub_gb_oIkJAAAAIAAJ and bub_gb_tZ_NAAAAMAAJ OCR); original HHStA StAbt Polen I 74 (Karton assigned from the AIS date range 07.1659-02.1660), not online',
            'extent': 'One passage of cipher without decipherment; the editor gives no length',
            'cipher': ''}
        for k in v['prior_art']:
            v['prior_art'][k] = v['prior_art'][k].replace('the Königsberg report of 11 Sept 1657', 'the Lisola reports of 1655-60').replace('no. LXXVI', 'no. CLX')
        v['prior_art']['edition'] = 'Pribram 1887 is the edition and was opened at no. CLX (Danzig, 6 Feb 1660, p. 547): it prints the readable text and states that a passage is not deciphered. No other edition of the report was found.'
        v['prior_art']['literature'] = 'Web searches for Lisola cipher reports 1656-60 (11 and 16 Nov 2026, including Lisola 1656 1657 1660 Berichte Chiffre entschlüsselt / deciphered Pribram) returned nothing on a decipherment of any Lisola report; Oliva congress literature not searched separately.'
    v['seen']['where'] = TODAY + "'" + q + "' (" + where + '). ' + v['seen']['where']
    v['seen']['cipher'] = ("No item-level archive description exists (AIS lists the Karton only, no scan). The editor, who printed from the original in the Staatsarchiv, describes the cipher: '" + q +
                           "'. In the same volume he prints the ciphered passages of sibling reports between asterisks ('Die zwischen Sternen stehenden Stellen sind im Original chiffrirt'), i.e. with their contemporary decipherment, so 'nicht dechiffrirt' means no decipherment was with this piece and he made none. Cipher system not stated.")
    v['prior_art']['tomokiyo'] = 'Tomokiyo unsolved list (cryptiana unsolved.htm, fetched 15 Nov 2026) searched for Lisola: 0 hits. Earlier check (11 Nov): cryptiana index and variable3.htm name Lisola only inside a c. 1657-59 Porcia key; no page on Lisola reports of 1655-60.'
    v['prior_art']['lasry'] = "Lasry list (cryptiana GL.htm, fetched 15 Nov 2026) searched for Lisola: 0 hits; no Lasry paper on Lisola in the web searches of 11 and 16 Nov 2026; known.py 'Lisola' shows no Lasry item in the repo."
    v['duplicates'] = ("known.py 'Lisola' (16 Nov 2026): only catalogue entries for Lisola 1643 and 1667 (Spanien Varia / 20-4-10) and the DECODE 1669-74 records (R1915-R1918, R2040); no catalogue entry or other lead for this report. The other Lisola reports of 1655-60 that Pribram marks 'nicht dechiffrirt' are separate leads (2508-2512), each a different date; "
                       "Pribram has two further 'nicht dechiffrirte Stelle' notes (after the Rangstreit report, cf. 24 July 1657, and at p. 543) that are not in this batch.")
    v['verdict'] = 'open'
    prop = {'verdict': 'open', 'confidence': 'medium',
            'note': f"Editor's note confirmed today in both OCR copies of Pribram 1887 ({where}): '{q}'. No decipherment printed or found anywhere; follows the catalogue precedent for editor-described undeciphered passages (e.g. entries 899, 1026, 1034). Not seen: the Karton is assigned from AIS date ranges, the leaf is not itemised.",
            'access': 'archive',
            'access_note': 'HHStA reading room or a scan order; AIS describes StAbt Polen I by Karton only (no scan); if not in the Polen I Karton, try Geheime Staatsregistratur 35-30 and Brandenburgica/Suecica of the same months.',
            'vetting': v}
    p = pathlib.Path(__file__).with_name('p') / f'{i}.json'
    p.write_text(json.dumps(prop, ensure_ascii=False, indent=1), encoding='utf-8')
    subprocess.run([sys.executable, '-I', '-X', 'utf8', str(pathlib.Path(__file__).with_name('add.py')), str(i), str(p)])
