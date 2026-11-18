"""Vetting of leads 2783-2807 (sweep_2026-11-15_tna_discovery); writes vetting.json and applies it to research/leads.json.
Promotion is done afterwards with docs/_check_catalogue.py --promote (2784, 2788, 2792, 2797)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BY = "claude session 15 Nov 2026 (Claude Sonnet 5.5), TNA Discovery sweep vetting"
D = "2026-11-15"
DEC = "known.py (Cryptoole/DECODE snapshot, DECODE views dumps, ledgers, targets, 15 Nov 2026): no DECODE record for this shelfmark; only this lead and its sweep row."
TOM = "Tomokiyo's Cryptiana: a site search for Kerguelen / Batavia 1811 / Stapleton returned nothing; no page on this item in the repo's holdings (known.py)."
LAS = "Not named in the GL.htm copy held in targets/gramont1529; Lasry's AI-assisted list (sect. 4) is not held locally, so a reading there is not excluded."
ACC = "TNA Discovery record read through the API (details/C-id, 15 Nov 2026): 'digitised' false; no image on Discovery. State Papers Online (Gale) is a subscription product and not checked for images; ADM 1 is not on Gale SPO. Archive item: Kew reading room or a reproduction order."
out = {}

out["2784"] = {"date": D, "by": BY,
 "seen": {"kind": "not online",
  "where": "TNA Discovery record ADM 1/1808/193 (C12759093), API details read 15 Nov 2026; digitised: false. " + ACC,
  "extent": "Folios 521-526: three original letters 'en chiffre' numbered un, deux, trois (two leaves each), undated, illegible signature; ff. 519-520 are the sealed envelope(s) addressed to the Ministre de la Marine et des Colonies, Paris, from the Governor-General of the Indies.",
  "cipher": "Archive text: 'Original lettre en chiffre, numero un / deux / trois' (ff. 521-526), enclosures of Capt. Justice Finley's letter of 8 Dec 1811 (HMS Rover took the French corvette Comte Regnaud, which left Batavia on 7 Aug 1811). The description mentions no decipherment, translation or decode among the enclosures."},
 "prior_art": {"decode": DEC, "tomokiyo": TOM, "lasry": LAS,
  "edition": "Not found: the Admiralty copies of the Governor-General's 1811 despatch are not printed in the Java-campaign literature seen (web search 15 Nov 2026: HMS Rover / Comte Regnaud / Batavia 1811 gave only ship histories).",
  "literature": "Web search 15 Nov 2026 (HMS Rover Finley Comte Regnaud Batavia 1811 captured letters Janssens Minister of Marine cipher): the capture is confirmed in ship histories (HMS Rover 1808, ex-Vincejo corvette); nothing on a decipherment of the captured letters."},
 "searches": [{"query": "known.py ADM 1/1808, Batavia, Finley, Janssens, Rover", "result": "this lead and sweep row only; Batavian-period targets (batavia1800, toulon1803, hogendorp) are different texts"},
  {"query": "web: HMS Rover Finley 1811 Batavia Comte Reynaud captured letters cipher", "result": "capture confirmed; nothing on the cipher"},
  {"query": "Discovery API details C12759093", "result": "description quoted above; no decipher named"}],
 "key_check": "No key for the 1811 Governor-General to Minister cipher is held here. targets/batavia1800 NOTES (siblings line) records that the 1811 Janssens despatches in Nationaal Archief 2.01.27.05 inv. 12 use another system (numeric code, French), not Smissaert's 1800 cipher; those are a possible key or clear-text source, not seen or tested.",
 "duplicates": "known.py 'ADM 1/1808', 'Batavia', 'Finley', 'Janssens' (15 Nov 2026): only this lead; not the same as batavia1800 (Smissaert to Prediger, 1800).",
 "verdict": "open",
 "lead_updates": {"seen": "catalogue", "access_note": ACC, "status": "Not online (Discovery record read 15 Nov 2026; no image). Three original numerical-cipher letters of the Governor-General of the Indies (Janssens) to the Minister of Marine, Batavia, c. Aug 1811, captured on the Comte Regnaud; no decipherment named. Needs Kew photographs."}}

KG = ("Archive text: 'encoded' / 'enciphered' / 'partially encoded' letters from Stapleton de Laurence ('Mimi') to Yves-Joseph de Kerguelen at Saumur, c. 1770-86 (SP 46/146, 148), "
      "read in Discovery 15 Nov 2026: 65-66 ('Encoded letter'), 71-72 and 89-90 ('partially enciphered/encoded'), SP 46/148/99-100 ('enciphered love letter'); SP 46/148/196-197 is as given by the sweep and was not re-read here.")
out["2788"] = {"date": D, "by": BY,
 "seen": {"kind": "not online",
  "where": "TNA Discovery records SP 46/146/65-66 (C7712677), /71-72 (C7712680), /89-90 (C7712689), SP 46/148/99-100 (C7713246), API details read 15 Nov 2026; digitised: false. " + ACC,
  "extent": "five to six short love letters (two leaves each) with covers, c. 1770-86, plus SP 46/146/63-64 as the crib (see key_in_volume).",
  "cipher": KG},
 "prior_art": {"decode": DEC, "tomokiyo": TOM, "lasry": LAS,
  "edition": "No edition: the Kerguelen papers (SP 46/146-148) are described only in the TNA catalogue; web search 15 Nov 2026 (Kerguelen Stapleton de Laurence Mimi cipher; French variant) found no mention of the ciphered letters in Kerguelen biographies or the catalogue pages indexed.",
  "literature": "Web search 15 Nov 2026 (two queries, one Cryptiana-restricted): nothing on a cipher in the Kerguelen-Stapleton letters."},
 "searches": [{"query": "known.py Kerguelen, SP 46/146, Stapleton", "result": "this lead only"},
  {"query": "web: Kerguelen Stapleton de Laurence Mimi cipher SP 46 (EN and FR)", "result": "nothing on the ciphered letters"},
  {"query": "Discovery API SP 46/146/63-90, SP 46/148/99-103", "result": "descriptions above; only 63-64 carries a decipher"}],
 "key_check": "No key held. SP 46/146/63-64 is an 'Encoded letter deciphered between the lines in Kerguelen's hand' (first page missing): a cipher/clear pair from the same writer, so a key can be rebuilt from it; it is excluded from the text to be read and kept as the crib.",
 "key_in_volume": "SP 46/146/63-64: interlinear decipher in Kerguelen's hand (crib for the whole correspondence); not seen.",
 "duplicates": "known.py 'Kerguelen', 'Stapleton de Laurence', 'SP 46/146' (15 Nov 2026): only this lead.",
 "verdict": "open",
 "lead_updates": {"title": "Stapleton de Laurence ('Mimi') to Kerguelen at Saumur: enciphered and partly enciphered love letters, c. 1770-86 (SP 46/146 and 148; the interlinear 63-64 kept as the crib)",
  "shelfmark": "TNA SP 46/146/65-66, 71-72, 89-90; SP 46/148/99-100, /196-197 (crib: SP 46/146/63-64)",
  "seen": "catalogue", "access_note": ACC,
  "status": "Not online (Discovery records read 15 Nov 2026; no image). Five or six enciphered or partly enciphered letters of one writer to one recipient; one other letter of hers (63-64) is deciphered between the lines by Kerguelen, a crib. Needs Kew photographs."}}


out["2792"] = {"date": D, "by": BY,
 "seen": {"kind": "not online",
  "where": "TNA Discovery record SP 31/3/117 (C18485520), API details read 15 Nov 2026; digitised: false. " + ACC,
  "extent": "Folio 207, one letter in cipher, same hand as the cryptic letter on f. 206, with a postscript 'Cut off this and deliver it to my friend'. Narrowed from the sweep row (ff. 206-207) to f. 207, because f. 206 is plain English in trade language.",
  "cipher": "Archive text: 'Folio 207. A letter in cipher.' of April 1687, 'PD' to William Benson at the apothecary's in the Strand (SP 31, Domestic Entry Book-type series, James II). No decipherment mentioned."},
 "prior_art": {"decode": DEC, "tomokiyo": TOM, "lasry": LAS,
  "edition": "The Calendar of State Papers Domestic, James II, 1686-87 was not searched item by item (no OCR of that volume held here); a grep of the repo ledgers on Benson / Bromwick finds nothing. A calendar entry that prints the clear text would be the first sign of a reading: not checked, so recorded as open.",
  "literature": "No web search run for this item beyond the Discovery text; nothing found in repo holdings."},
 "searches": [{"query": "known.py SP 31/3, Benson, Bromwick", "result": "this lead only"}],
 "key_check": "No key held or named.",
 "duplicates": "known.py 'SP 31/3' (15 Nov 2026): only this lead.",
 "verdict": "open",
 "lead_updates": {"title": "Letter in cipher from 'PD' to William Benson, London, 5 Apr 1687 (SP 31/3/117 f. 207)",
  "shelfmark": "TNA SP 31/3/117 (f. 207)", "folio_note": "f. 206 is the plain-language covering letter in the same hand",
  "seen": "catalogue", "access_note": ACC,
  "status": "Not online (Discovery record read 15 Nov 2026; no image). One letter in cipher, f. 207; no decipherment named. Needs Kew photographs."}}

out["2797"] = {"date": D, "by": BY,
 "seen": {"kind": "not online",
  "where": "TNA Discovery record SP 46/97 fo. 47-47d (C7709925), API details read 15 Nov 2026; digitised: false. " + ACC,
  "extent": "one leaf with verso, a contemporary copy of part of Beverning's letter; the length of the coded part is not stated.",
  "cipher": "Archive text: 'Beverning at Westminster to Newport at the Hague. Report of a conversation, part in code. Copy.', 12 Aug 1653. No decipherment named."},
 "prior_art": {"decode": DEC, "tomokiyo": TOM + " (Beverning 1653 appears in the repo only for the Thurloe State Papers letter to Boreel, targets/thurloe).",
  "lasry": LAS,
  "edition": "Not found: Thurloe State Papers i. 435 prints Beverning and Vande Perre's letter to Boreel (22 Aug/1 Sept 1653), a different letter; the Newport letter of 12 Aug is not known printed.",
  "literature": "Repo NOTES targets/thurloe, vandeperre1653, colbert and research/qa/key_split_audit.md checked (15 Nov 2026): the Beverning 1653 systems are unread."},
 "searches": [{"query": "known.py Beverning, SP 46/97", "result": "targets/thurloe (Beverning 1653 to Boreel, unread), vandeperre1653, colbert; none cover this letter"}],
 "key_check": "No key held. targets/thurloe tried every 1653-60 period key on the Beverning/Vande Perre cipher without a fit; whether the Newport letter uses that system is not shown. A separate entry from thurloe (one key per entry).",
 "duplicates": "known.py 'Beverning', 'SP 46/97', 'Nieupoort' (15 Nov 2026): the thurloe family is a different letter and recipient.",
 "verdict": "open",
 "lead_updates": {"seen": "catalogue", "access_note": ACC,
  "status": "Not online (Discovery record read 15 Nov 2026; no image). One contemporary copy with a coded part; no decipherment named. Short; sibling of targets/thurloe (different letter). Needs Kew photographs."}}

N = {
 "2783": "SP 87/2/49 and /51 (C8950289, C8950291, read 15 Nov 2026): the catalogue calls both 'Cipher with interlinear decodement', i.e. the clear text is written between the lines. A decipherment is on the item, so it fails the bar ('no decipherment on or with it'); it is a ready crib pair for other Marlborough number letters in SP 87 (SP 87/4/133 is a lead). No literature on the decode found (web search 15 Nov 2026). Candidate to close as 'read from existing decipherment' once the image shows the decode covers every group.",
 "2785": "ADM 1/1948/97 (C12820601, read 15 Nov 2026): ff. 251-254 are two enciphered reports 'which has been deciphered at the Admiralty'; the description paraphrases the decoded text at length. Decipher on file: fails the bar. Crib pair only.",
 "2786": "ADM 1/1665/176 (C18550506): 'Written in cypher code and decrypted', one line; decipher on file: fails the bar.",
 "2787": "ADM 1/2253/132 (C12835255): Osborn forwards 'extracts of a letter (which is in code)' of Rainier; ff. 316-321 a letter 'in code' of 15 May 1799 and ff. 314-315 the East India House cover. Not clear that ciphertext (rather than a code-name text) is present, nor whether the extracts are the decoded text; not vetted further.",
 "2789": "SP 54/41/27A-C (C6820317 for 27C, read 15 Nov 2026): 27C is a list of names 'thought to be given in code' in 27B, made by the intercepting side. The letter is a code-name letter rather than a cipher, and the list is an attempted decode on file. Fails the bar; no key; web search 15 Nov 2026 found no Andrew Clerck item.",
 "2790": "SP 32/14/51 (C17475303): f. 99 is an 'Extract' from the ciphered letter on ff. 100-101, i.e. a clear gist is filed with it; dated range 1689-1702 only. Decipher beside it: fails the bar.",
 "2791": "PRO 30/24/7/505 (C6756450, Shaftesbury Papers): 'Draft of letter ... in cypher' with an endorsement that these are to be entered in the letter book. Unclear whether the item is ciphertext or a clear draft of letters sent in cipher; the letter book may hold the clear text. Not vetted further.",
 "2793": "SP 90/2 (Raby to Hedges 1704; C6554786 /262 'Explains cipher of f.266', C6554815 /356 'Additions to cipher'): Discovery gives full summaries of the content, which suggests the letters were deciphered in the volume or at the time (the 28 Oct sweep recorded deciphers written over such SP volumes). Not vetted further; narrow to one folio and check for a decipher before promotion. The explanations on f. 262 and 356 would be a key in the volume.",
 "2794": "SP 35/72/17 (C15416206): a copy of Kelly's pocket-book with 'various references, some in code' (names, payments); SP 35/39/21 BY1 (C15416469) is a 'Cipher-key' among Layer's papers (the Atterbury plot): the key is in the volume but the coded parts of the pocket-book are not shown to use it. Weak; not promoted.",
 "2795": "SP 35/30/31 (C17209745): an intercepted letter translated, 'all the names are still in cypher in the translation': a translation is filed and names only are coded. Fails the bar.",
 "2796": "SP 36/60/365 (C7768166): content fully summarised in the description (French 'partly in cypher'), so a clear text exists; fails the bar.",
 "2798": "SP 46/124 fo. 60d (C7694233): an 1548 account 'in code' on the verso of a merchant account: probably merchant's shorthand, not a cipher; not vetted further.",
 "2799": "Parliamentary Archives Braye MS.3 (YPIC/P/301to399/374-375), 'Intercepted note in code from the Duke of York', two pages: Discovery record only, not at TNA; not read or vetted further.",
 "2800": "HO 42/15/21 (C11805737): 'a section apparently in code' in a dead letter of 1789; not shown to be a cipher; weak, not vetted further.",
 "2801": "HO 42/73/71 (C17045965): 'cryptic letter partly in code', weak, not vetted further.",
 "2802": "HO 33/2/21 (C9712187): refers to places in code; weak, not vetted further.",
 "2803": "CSP Domestic Charles I 1644 (Williams to Digby, preface and p. 690): the editor partly analysed the scheme and printed an attempt; the SP 16 volume and folio are not identified, and the Digby/Williams royalist family is heavily worked (repo hits: targets/rupert, hm1645, sp106r931). Not vetted; identify the SP 16 piece first.",
 "2804": "CSP Domestic Elizabeth 1598-1601 (p. 495; Donavillis to Feselaw): the calendar says the cipher passages are 'undeciphered'; SP 12/275 volume number not verified, folio unknown. Not vetted.",
 "2805": "CSP Domestic Elizabeth 1598-1601 item 79 (Holt to Owen and Bayley, name-numbers undeciphered): SP 12/275 not verified; the Parsons/Owen keys known on DECODE (catalogue note for Hugh Owen) are the route. Not vetted.",
 "2806": "CSP Domestic James I 1619-23 (Dover): author and recipient unknown, 'partly in cipher, undeciphered'; the shelfmark SP 14/116 is the printed volume number only. Not vetted.",
 "2807": "CSP Domestic Charles II 1663-64 nos. 17-18 (Thorne-Lawrence plot): the calendar says the decypher is filed beside it, so a decipher is on file: fails the bar; the SP 29 volume is not identified.",
}
for i, s in N.items():
    out.setdefault(i, {"unvetted": "Vetting pass 15 Nov 2026 (TNA Discovery sweep): " + s})
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
