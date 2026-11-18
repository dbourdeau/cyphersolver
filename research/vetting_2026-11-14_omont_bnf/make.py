"""Vetting of leads 2724-2744 (sweep_2026-11-14_omont_bnf); writes vetting.json and applies it to research/leads.json.
Promotion/closing is then done with docs/_check_catalogue.py."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BY = "claude session 14 Nov 2026 (Claude Sonnet 5.5), Omont BnF sweep vetting"
D = "2026-11-14"
IIIF = "openapi.bnf.fr IIIF images of Gallica ark %s, 14 Nov 2026"
out = {}

out["2732"] = {"date": D, "by": BY,
 "seen": {"kind": "scan",
  "where": IIIF % "btv1b9060066q (BnF fr. 3027, 123 views; the Gallica description opens with letters of admiral Bonnivet to the marshal de Montmorency, which confirms the shelfmark)",
  "extent": "One letter looked at: view 69 (Omont's no. 34, 'f. 67'; Omont's folio numbers are an older foliation and do not match the modern stamp, see the 2996 note) is a letter written in cipher signs (about 20 lines of symbols run together with a few plain words), addressed on a following view 'A monsr le mareschal de Montmorency'. The other places Omont names (nos. 49, 70, 72; ff. 100-202) were not opened.",
  "cipher": "Symbol cipher in a 16th-century cursive hand, the plain-text passages interleaved; no interlinear or marginal decipherment on the leaf and no clear copy on the facing view."},
 "prior_art": {
  "decode": "decode_search.py, 14 Nov 2026: 'Bonnivet' 0 records; 'Montmorency' returns only BnF NAF 4206 (Dinteville and du Bellay, R9467-9477), none from fr. 3027 (the DECODE id 3027 in the Cryptoole snapshot is an unrelated British Library record).",
  "tomokiyo": "Tomokiyo's GL.htm page (copy in targets/gramont1529) lists Lasry's deciphered Montmorency-period ciphers in fr. 3015, 3022, 3029, 3092 and fr. 2996; fr. 3027 is not named there. Web search for 'fr. 3027' with Bonnivet/Montmorency (14 Nov 2026) found nothing.",
  "lasry": "Not in the GL.htm copy held here; the AI-assisted list (sect. 4) is not held locally and was not re-read, so a reading there is not excluded.",
  "edition": "No printed edition of the Bonnivet-Montmorency letters of fr. 3027 found; Omont's catalogue lists the pieces 'en chiffre' without a decipherment.",
  "literature": "Nothing found by web search (14 Nov 2026)."},
 "searches": [{"query": "decode_search.py Bonnivet; Montmorency", "result": "0; and NAF 4206 only."},
  {"query": "Tomokiyo cryptiana fr.3027 Montmorency Bonnivet", "result": "nothing"}],
 "key_check": "No key known. Neighbouring volumes of the Montmorency papers (fr. 3015, 3022) carry deciphered ciphers of the same years that could be tried; not tested.",
 "duplicates": "known.py 'fr. 3027', 'Bonnivet' (14 Nov 2026): only this lead and its sweep row.",
 "verdict": "open",
 "lead_updates": {"access": "online", "seen": "scan",
  "status": "Cipher letter seen on Gallica (openapi IIIF view 69 of fr. 3027). Omont's folio numbers use the older foliation: find the ciphers by item, not folio.",
  "folio_note": "fr. 3027: Omont nos. 34, 49, 70, 72 (his ff. 67, 100-105, 182, 186-202); cipher letter seen at view 69."}}

out["2734"] = {"verdict": "read", "closed": "The Morvillier despatch from Venice of 24 Jan 1546 is the 'de Morvillier's cipher (1546)' deciphered on Tomokiyo's GL.htm page (BnF fr. 2996 f. 52 no. 25, Gallica; Lasry's key), so its decipherment exists. Seen on Gallica views 98-99 of ark btv1b9060087w: a full-page symbol cipher letter, Omont's 'f. 33' being the old foliation (modern view 60 is a plain letter stamped 33). The fr. 3137 despatch of 12 Nov 1549 (same ambassador, key letter said to be in fr. 3138 f. 70) was not opened; a separate lead may be made for it if it is not covered. (14 Nov 2026)"}

N = {
 "2724": "SHELFMARK DOUBTFUL. Gallica fr. 3231 (btv1b90602383) is a collection of letters of the cardinals of Guise to the duke of Nemours; views 36, 83, 88 checked at Omont's ff. 35, 82, 87 are plain French letters (f. 35 signed by a Gonzague/Nevers hand), no cipher and no Birago. Omont's heading number for the Birago volume is probably an OCR misreading; Birago letters of 1571 sit in fr. 3252 (catalogue 318 and Lasry's list). Re-identify the volume before vetting.",
 "2725": "SHELFMARK WRONG. Gallica fr. 3057 (btv1b9060031h) is a volume of Francis I letters to La Fayette (views 11, 59, 92 plain French); the Mary Stuart / Philip II volume of the printed catalogue is not fr. 3057, so the sweep's correction of 3657 to 3057 was wrong. Probably fr. 3657 (no Gallica ark found).",
 "2726": "Not online (no ark found for fr. 3652/3339). Shelfmarks unconfirmed: other rows of this sweep proved OCR numbers wrong.",
 "2727": "Gallica fr. 3374 (btv1b9059610x) matches (Nevers / Cabriani 1585). Views 144 and 146 (Omont ff. 143, 145) failed to download; view 5 gave no cipher. Not viewed at the cipher places; fr. 4697/4691 not online.",
 "2728": "Not online; shelfmark unconfirmed.",
 "2729": "Not online; shelfmarks unconfirmed.",
 "2730": "Not online; shelfmarks unconfirmed.",
 "2731": "SHELFMARK DOUBTFUL. Gallica fr. 2986 item 1 is a letter of Berne (views 3-23 plain). DECODE has Ranzo ciphers at fr. 2988 f. 1, 2, 9-11 (R2323, R2294, R2295, mostly Non-decrypted) and fr. 3019 f. 73-74 (R2293), and Raince 1526 at fr. 3040 f. 21 (R4228, decrypted): the Ranzo/Raince items are almost certainly fr. 2988, already on DECODE. Check fr. 2988 and R2293-2323 before any entry.",
 "2733": "Not online; shelfmark unconfirmed; DECODE 'Salviati' not searched.",
 "2735": "Gallica fr. 3043 (btv1b90598808, Renee de France 1540, Montmorency papers) plausible; DECODE has Cenalis at fr. 20506 f. 96 (R4815, decrypted) and a Venice letter at fr. 3045 f. 36 (R4231, 1530-39, decrypted), which may be this letter under the number 3045 (OCR). Not viewed; likely duplicate.",
 "2736": "SHELFMARK DOUBTFUL. Gallica fr. 3086 (btv1b9060039t) opens with Charles V letters of grace of 1539, not Ventadour 1597; fr. 3373 (btv1b9059612r, 63 views) is Bellievre 1587. The Ventadour letters are in some other volume. Not vetted.",
 "2737": "SHELFMARK WRONG. Gallica fr. 3638 (btv1b9059321p) opens with Marguerite de Valois to Montmorency (1530s), not Monteleon 1617. Probably a nearby number; no ark known.",
 "2738": "Not online; shelfmark unconfirmed.",
 "2739": "Not online; shelfmarks unconfirmed.",
 "2740": "Not online; shelfmark unconfirmed.",
 "2741": "Gallica fr. 4137 (btv1b9060192j) matches (Sabran copies 1629-45, year 1637). Copies, not originals; the 'memoire en chiffre' at f. 128 not viewed here. Sabran's cipher is deciphered by Tomokiyo/Lasry for fr. 4134-4135 (GL.htm), so this may be readable with that key: check before entry.",
 "2742": "Not online; shelfmark unconfirmed.",
 "2743": "Not online; shelfmark unconfirmed.",
 "2744": "Not online; no Gallica ark; overlaps lead 1577 (Rance 1629): resolve with that lead.",
}
for i, s in N.items():
    out.setdefault(i, {"unvetted": "Vetting pass 14 Nov 2026 (Omont sweep): " + s +
       " General warning: Omont's volume numbers are OCR readings and his folio numbers an older foliation, so check each row against the Gallica title before use."})
json.dump(out, open(os.path.join(HERE, "vetting.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
sys.path.insert(0, os.path.join(ROOT, "docs"))
import _check_catalogue as C
d, leads = C.load(C.LEADS, "leads")
byid = {str(l["id"]): l for l in leads}
for i, b in out.items():
    l = byid[i]
    if "unvetted" in b:
        l["vetting_note"] = b["unvetted"]; continue
    if b["verdict"] != "open":
        v = l.setdefault("vetting", {}); v.update(verdict=b["verdict"], closed=b["closed"], date=D); continue
    b = dict(b); l.update(b.pop("lead_updates", {})); l["vetting"] = b
C.save(C.LEADS, d)
print("applied", len(out))
