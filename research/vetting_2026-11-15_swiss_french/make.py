"""Vetting of leads 2766-2782 (sweep_2026-11-15_swiss_french); writes vetting.json and applies it to research/leads.json.
Promotion is done afterwards with docs/_check_catalogue.py --promote (2773, 2774, 2775)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BY = "claude session 15 Nov 2026 (Claude Sonnet 5.5), French-Swiss sweep vetting"
D = "2026-11-15"
out = {}
WEB = ("Web search 15 Nov 2026 (Affry fonds Fribourg Rouille Bernis Choiseul chiffre Lyonet; Marsay Newcastle cipher Mestral; d'Aubigne 'Divers chiffres' Tronchin 148): "
       "nothing on a decipherment, edition or study of these ciphers; only fonds-level pages of the Fribourg archives and the BGE/Tronchin context.")
DEC = "known.py (Cryptoole/DECODE snapshot, views dumps, ledgers, 15 Nov 2026): no DECODE record for these shelfmarks; only this lead and its sweep row."
TOM = "Tomokiyo's Cryptiana has no page on these files in the repo's holdings (known.py); not named."
LAS = "Not named in the GL.htm copy held in targets/gramont1529; Lasry's AI-assisted list (sect. 4) is not held locally, so a reading there is not excluded."
AFFRY = ("Fribourg friXplore (archives.fr.ch, fetched 15 Nov 2026): the fonds has no digital objects ('Multimedias: Sans' for all 331 hits of the Affry set), so the pieces are "
         "not online; the unit records give cote, title, date and a short content note only.")

AF = {
 "2766": "AEF Affry 225 (Rouille to d'Affry, Dec 1755 - Jul 1757; d'Affry's numbered dispatches are also filed here as clear 'Brouillon d'une depeche n. N', about 70 of them). Series 225 lists 'Lettre de Rouille ... n. N' followed by 'Transcription de la depeche ...' for most numbers (225.83, .89, .99, .106 ... .316), so a transcription is filed with each dispatch and the word 'chiffree' is on only a few titles (225.83, .89, .254, .276): not promotable under the bar. Whether the Transcription is contemporary or modern is not stated; content notes (225.242) are summaries. Important for affry1757 (see the sweep report).",
 "2767": "AEF Affry 226 (Bernis to d'Affry, Jul 1757 onward; d'Affry's clear drafts n. 198-400 are filed as 'Brouillon'). Transcription pieces sit beside the letters (226.11, .18/.19, .56, .92, .103, .110, .130). Transcription filed: not promotable. Source for affry1757.",
 "2768": "AEF Affry 227-228 (Choiseul to d'Affry 1759-62): 227.213 'Lettre chiffree' 25 Nov 1759 with 227.214 'Transcription' and 227.215 'deuxieme version'; 228.50/.51 (Praslin n. 320, 27 May 1762) cipher and 'Transcription du chiffre'. Transcription filed with each: not promotable.",
 "2769": "AEF Affry 257 (d'Affry <-> Stainville/Choiseul, Vienna, Apr 1757 - Oct 1758, 29 units): every ciphered dispatch has its 'Transcription' next to it (257.6/.7 23 Sep 1757, .10/.11 5 Nov 1757, .14/.15, .18/.19, .21/.22, .23/.24, .28/.29) and d'Affry's own clear 'Brouillon' letters to Stainville are filed too (257.1, .5 of 4 Sep 1757, .13, .17, .20, .25). 259.12 (17 Mar 1760, partly ciphered) has no transcription listed. Not promotable (transcription filed). Source for affry1757c.",
 "2770": "AEF Affry 238 (Marshal d'Estrees, May-Jun 1757): 238.10 and .14 a/b are 'Transcription du chiffre de la lettre ...' beside the letters. Transcription filed: not promotable.",
 "2771": "AEF Affry 244 (Conflans d'Armentieres, 1759): 244.13 'Lettre chiffree' with 244.14 'Transcription du chiffre', same pattern for the others. Transcription filed: not promotable.",
 "2772": "AEF Affry 266 (Ogier, ambassador at Copenhagen, 1758-60): the whole series was read on friXplore 15 Nov 2026 (84 units); each ciphered or partly ciphered letter has a 'Dechiffrement' piece next to it (266.1/.2, .6/.7, .14/.15, .23/.24, .28/.29, .30/.31, .40/.41, .42/.43, .47/.48, .49/.50, .73-.75, .77/.78); 266.13, .22 and .68 have none listed. Decipherment filed: not promotable.",
}
for i, s in AF.items():
    out[i] = {"unvetted": "Vetting pass 15 Nov 2026 (French-Swiss sweep): " + s + " " + AFFRY}

out["2773"] = {"date": D, "by": BY,
 "seen": {"kind": "not online",
  "where": "Archives de l'Etat de Fribourg, friXplore (archives.fr.ch, fetched 15 Nov 2026): unit records AEF Affry (de Boccard) 267.21 (20 Jun 1758) and 267.8, plus the series listing (35 units of 267 read). Multimedias: none for the whole fonds; reading room or reproduction order needed.",
  "extent": "series 267 holds d'Affry's incoming letters from Louis de Cardevacque, marquis d'Havrincourt, ambassador at Stockholm, Jan 1758 - Dec 1760; the entry is narrowed to the ciphered or partly ciphered letters with no 'Decryptage' piece listed beside them (at least 267.2, .11, .14, .16, .21, .25, .33, .35, .38, .42, .53, .63, .65, .68, .71, .75, .83, .86, .88, .92). Length of each unknown.",
  "cipher": "Archive titles: 'Lettre chiffree du marquis d'Havrincourt' (267.2, .21, .25, .53, .63, .68, .71) and 'Lettre en partie chiffree' (the rest). A 'Decryptage du chiffe de la lettre du ...' piece is filed for only seven letters (267.8 of 11 Apr 1758, .20, .28, .31, .48, .79, .82); the unit record of 267.8 gives a content summary only, not text."},
 "prior_art": {"decode": DEC, "tomokiyo": TOM, "lasry": LAS,
  "edition": "No edition found: the Affry correspondence of 1755-62 is extracted only in Bussemaker's extracts of d'Affry's letters (BMHG 27, 1906), which are d'Affry's own letters to the French government, not Havrincourt's; Havrincourt's Stockholm letters of 1758-60 are not known printed with deciphered passages.",
  "literature": WEB},
 "searches": [{"query": "known.py Havrincourt / Affry (de Boccard) / friXplore", "result": "this lead and its sweep row; the Affry targets cite only Nationaal Archief decipherments"},
  {"query": "friXplore: 'Havrincourt', 'chiffre', 'decryptage' (35 units of series 267 listed)", "result": "20 ciphered letters without a Decryptage piece; 7 with one"},
  {"query": "web: Affry fonds Fribourg Rouille Bernis Choiseul chiffre Lyonet", "result": "nothing on these ciphers"}],
 "key_check": "No key sheet for the Havrincourt cipher is filed in series 267. The 'Decryptage' pieces (7 letters) are cipher/clear pairs from which a key can be rebuilt (the way the affry1757 key was); the fonds also holds two undated key sheets in 280 ('Chiffre avec Botteman', 280.209: numbers 1-60 with a letter each and code names on p. 2; 'Premier chiffre remis par le duc de Choiseul et le chancelier du Muy', 280.210), neither named for Havrincourt, not seen. Nothing tested.",
 "key_in_volume": "Cipher/clear pairs for 7 of the letters (267.8, .20, .28, .31, .48, .79, .82) are in the series; the two key sheets 280.209-210 are in the same fonds and are not shown to belong to this correspondent.",
 "duplicates": "known.py 'Havrincourt', 'Affry', 'Choiseul' (15 Nov 2026): this lead and the sweep row; the catalogue's d'Affry entry is R1071 (affry1757c) only.",
 "verdict": "open",
 "lead_updates": {"title": "Marquis d'Havrincourt's ciphered letters to d'Affry from Stockholm, 1758-60: the letters with no 'Decryptage' filed (about 20 units, AEF Affry 267)",
  "shelfmark": "Archives de l'Etat de Fribourg (AEF), Affry (de Boccard) 267.2, .11, .14, .16, .21, .25, .33, .35, .38, .42, .53, .63, .65, .68, .71, .75, .83, .86, .88, .92",
  "folio_note": "Series 267 (d'Affry <-> Havrincourt): 267.8, .20, .28, .31, .48, .79, .82 are 'Decryptage' pieces beside the letters of 11 Apr, 13 Jun, 11 Jul, 21 Jul, 5 Sep 1758, 5 Aug and 26 Aug 1760 (cipher/clear pairs); 268.19 is L'Hopital's, not Havrincourt's. Siblings with their own cipher: Ogier 266 (Copenhagen), Estrees 238, Conflans 244, Stainville/Choiseul 257/227.",
  "seen": "catalogue", "access_note": "friXplore unit records seen 15 Nov 2026: no digital objects (Multimedias: Sans); reading room or reproduction order at the Archives de l'Etat de Fribourg.",
  "status": "Not online (friXplore records seen 15 Nov 2026; no images). About 20 ciphered letters have no decipherment filed; 7 have one, which gives pairs for the key. Needs reading-room photographs."}}

MARSAY_PRIOR = {"decode": DEC, "tomokiyo": TOM, "lasry": LAS,
  "edition": "No edition of the Marsay correspondence found; the Mestral family papers at the ACV are described in the inventory (davel.vd.ch) and in Vaud local history only. The 1734 Newcastle-Marsay cipher is the subject of catalogue entry 1781 (Waldegrave to Delafaye, TNA SP 78/205/95).",
  "literature": WEB}
out["2774"] = {"date": D, "by": BY,
 "seen": {"kind": "not online",
  "where": "Archives cantonales vaudoises, DAVEL inventory (davel.vd.ch/detail.aspx, ID 723222, Chrome, 15 Nov 2026; plain curl is refused by the cantonal firewall): the unit record has no image link or digital object; access regulation 'Libre' (reading room).",
  "extent": "96 physical pieces in one envelope, 24 Aug 1730 - 18 Nov 1739.",
  "cipher": "Archive's text: 'Certaines lettres sont en code chiffre. Le code est dans le lot.' Language field 'Crypte; Francais'; descriptors cryptage, codage. Nothing says a decipherment is filed."},
 "prior_art": MARSAY_PRIOR,
 "searches": [{"query": "known.py Marsay / Mestral / Saint-Saphorin", "result": "this lead, lead 2775 and the Waldegrave/Newcastle-Marsay entry 1781 only"},
  {"query": "web: Marsay Newcastle cipher letters Mestral ACV", "result": "nothing"}],
 "key_check": "Key in the lot (the archive says 'le code est dans le lot'); not seen, so not tested. No Marsay or Newcastle cipher key is held here or on DECODE.",
 "key_in_volume": "The code is in the same dossier, per the archive; not seen.",
 "duplicates": "known.py 'Marsay', 'P de Mestral' (15 Nov 2026): the sibling lead 2775 (1746-62, its own key) and 1781 (TNA SP 78/205/95, Waldegrave 21 Jul 1734: copy of a Newcastle-to-Marsay cipher letter, so the 1734 letters in this dossier belong to the same correspondence).",
 "verdict": "open",
 "lead_updates": {"seen": "catalogue", "access_note": "DAVEL record viewed 15 Nov 2026: no digital copy; consult at the ACV (access 'Libre').",
  "status": "Not online (DAVEL record seen 15 Nov 2026). Cipher letters with the code in the same dossier, from the British Cabinet to Marsay, 1730-39, so the 1734 cipher of entry 1781 falls in it. Needs reading-room photographs."}}
out["2775"] = {"date": D, "by": BY,
 "seen": {"kind": "not online",
  "where": "Archives cantonales vaudoises, DAVEL inventory (davel.vd.ch/detail.aspx, ID 723224, Chrome, 15 Nov 2026): no image link; access 'Libre'.",
  "extent": "145 physical pieces in one envelope, 6 Oct 1746 - 28 Sep 1762.",
  "cipher": "Archive's text: 'Avec une clef du chiffre - code pour dechiffrer.' Language 'Crypte; Francais'; descriptors codage, cryptage. Nothing says a decipherment is filed."},
 "prior_art": MARSAY_PRIOR,
 "searches": [{"query": "known.py Marsay / Mestral", "result": "this lead, lead 2774 and 1781 only"},
  {"query": "web: Marsay Newcastle cipher letters Mestral ACV", "result": "nothing"}],
 "key_check": "A key sheet is in the dossier per the archive; not seen, not tested; a separate key from 484 is likely since the periods are seven years apart, not shown.",
 "key_in_volume": "'Avec une clef du chiffre': key in the dossier, not seen.",
 "duplicates": "known.py 'Marsay', 'P de Mestral' (15 Nov 2026): sibling 2774 (1730-39) and 1781 only. Marsay's dossiers 483, 485 and 487 are not ciphered per their titles (not opened).",
 "verdict": "open",
 "lead_updates": {"seen": "catalogue", "access_note": "DAVEL record viewed 15 Nov 2026: no digital copy; consult at the ACV (access 'Libre').",
  "status": "Not online (DAVEL record seen 15 Nov 2026). 145 pieces from the British Cabinet to Marsay, 1746-62, with a key sheet in the dossier. Needs reading-room photographs."}}

N = {
 "2776": "ACV P de Mestral II D 4 / D 6/1: not promoted yet. The D 6/1 record (ID 726266) is a series of per-correspondent cipher sheets (18 envelopes, 'Chiffres' on each sub-unit); Wrisberg's letters of 19 Dec 1720 and 6 Jun - 10 Sep 1724 are flagged 'Crypte', but which sub-unit holds Wrisberg's key was not read (the entry must be narrowed to one correspondent and one key under the one-key rule: the Wrisberg letters with their key, or Robethon 1717 with its key). Catalogue lead 1663 (Robethon papers, Flemming letters deciphered at the time by Robethon) is a different series. Not opened beyond the inventory text; no images.",
 "2777": "Not vetted (Valais, outside this pass): Supersaxo II P 74, cipher letter to Schiner c. 1510; finding-aid text only.",
 "2778": "Not vetted (weak, class C).",
 "2779": "Not vetted (weak, class C): a cipher table, no cipher letter.",
 "2780": "BGE Arch. Tronchin 148/56 (record read in Chrome 15 Nov 2026, 48 views): the notebook holds 'divers chiffres employes dans les guerres civiles', i.e. key lists (the clef at f. 150), plus d'Aubigne's letters in clear or as minutes; the archivist's note on f. 146v-147v says the copyist wrote numbers above words to be replaced on the fair copy and that the key at f. 150 corresponds. So the volume holds keys and a partly numbered minute, not a ciphertext as sent: the bar's 'ciphertext seen' is not met, and the images were not viewed. Three of the clear letters are the same as Tronchin 152 and are printed by Reaume and de Caussade (I, p. 135-136, 204, 212-214). Kept as a key lead for Huguenot ciphers 1620-25, not an entry.",
 "2781": "BGE Ms. suppl. 976 (Jacobi-Kloest, 1807-08: ciphered letters with d'Ivernois's decipherment filed, so not promotable), Ms. suppl. 1879 f. 147 (Kleiber's key, no ciphertext named), Ms. suppl. 1004-1006 f. 113-114 (key to d'Ivernois's Vienna correspondence of 1814-15; the cipher letters not named). Three keys: split on promotion; none is ready (ciphertext not seen). The BGE search pages sit behind an Anubis proof-of-work page that cleared itself in the browser.",
 "2782": "Not vetted (weak).",
}
for i, s in N.items():
    out.setdefault(i, {"unvetted": "Vetting pass 15 Nov 2026 (French-Swiss sweep): " + s})
json.dump(out, open(os.path.join(HERE, "vetting.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
sys.path.insert(0, os.path.join(ROOT, "docs"))
import _check_catalogue as C
d, leads = C.load(C.LEADS, "leads")
byid = {str(l["id"]): l for l in leads}
for i, b in out.items():
    l = byid[i]
    if "unvetted" in b:
        l["vetting_note"] = b["unvetted"]; continue
    b = dict(b); l.update(b.pop("lead_updates", {})); l["vetting"] = b
C.save(C.LEADS, d)
print("applied", len(out))
