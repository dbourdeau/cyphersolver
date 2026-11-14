"""Write the draft profile.json (Dan's schema, copied in form from targets/ralamb1657/profile.json)."""
import json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from decrypt import load_key, cipher_letters, HERE

kw, sv = load_key()
rows = json.load(open(HERE / 'runs.json', encoding='utf8'))


def L(d):
    t = ''.join(cipher_letters(r[2], sv) for r in rows if r[0] == d)
    return len(t), len(set(t))


t119, t120 = L('119'), L('120')
c121 = ''.join(l.split('\t')[2].strip() for l in open(HERE / 'transcription_121_pass1.txt', encoding='utf8').read().splitlines()
               if l and not l.startswith('#')).replace('ð', 'f')
SRC = "HStAD Arcinsys digitalisate, https://digitalisate-he.arcinsys.de/hstad/d_4/487--4/hstad_d_4_nr_487--4_NNN.jpg"


def doc(i, read, shelf, date, pages, src_note, tok, file, notes, frm="unknown"):
    return {"id": i, "read": read, "shelfmark": shelf, "date": date, "year": 1792, "country": "Germany",
            "route": "Hofrat Jähring -> Georg Karl of Hesse-Darmstadt", "places": {"from": frm, "to": "unknown"},
            "language": "German", "cleartext_in_document": "interspersed", "pages": pages,
            "plaintext": {"location": ["none"], "source": src_note},
            "length": {"tokens": tok[0], "distinct": tok[1], "unit": "letters", "measured": True, "file": file},
            "transcription": {"by": "llm from images", "source": SRC, "image_quality": "fair", "notes": notes}}


P = {
    "schema_version": 1, "target": "jahring1792",
    "title": "Hofrat Jähring to Georg Karl of Hesse-Darmstadt, 1792 (catalogue 2030): Porta table with the keyword "
             "\"constantinopolitanus\" written over the cipher by a second hand; the runs of the letter of 1 June 1792 "
             "deciphered, the upper runs of the report \"Unterthänigster Bericht\" read in part, its long cipher block "
             "decoded in fragments only",
    "documents": [
        doc("img119_jun1792", "read in part", "HStAD D 4 Nr. 487/4, image 119 (both pages); the letter ends on image 120, left page",
            "1 June 1792 (dated and signed on image 120, left page)", 3,
            "No decipherment on these pages. The keyword is written by a second hand over the cipher of images 120 (foot) and 121 of the same volume.",
            t119, "transcription_119.txt",
            "Two passes from crops at about 3x and 2.8-4x; differences settled on the image and listed in transcription_119_pass2.txt. Same agent both passes. A blind reviewer copied 119.5, 119.6 and 119.13 from the image (13 Nov 2026); two letters corrected after it (q read as g in 119.5 and 119.13), stated in the file header.",
            "Darmstadt"),
        doc("img120_bericht_upper", "read in part",
            "HStAD D 4 Nr. 487/4, image 120, right page, upper half (report \"Unterthänigster Bericht\", continued on image 121)",
            "undated (filed after the letter of 1 June 1792; marked \"B R 12/5\")", 1,
            "No decipherment of these four runs on the page.", t120, "transcription_120.txt",
            "Two passes (2x, then 4x for disputed letters); differences in transcription_120_pass2.txt. Same agent both passes. A blind reviewer copied all four runs from the image (13 Nov 2026); three letters corrected after it (q read as g in 120.1 and 120.3, as y in 120.2), stated in the file header."),
        doc("img120_121_bericht_block", "not read",
            "HStAD D 4 Nr. 487/4, image 120, right page, foot (run 120.5) and image 121, left page (cipher block)",
            "undated (same report as img120_bericht_upper)", 2,
            "A second hand wrote the keyword over every cipher letter and \"chandeltsnt\" under run 120.5; no other decipherment.",
            (len(c121), len(set(c121))), "transcription_121_pass1.txt",
            "One pass only, four line fragments; the lines are overwritten by the key letters and strokes of the second hand. Not reconciled."),
    ],
    "system": {
        "types": ["polyalphabetic"],
        "summary": "Porta table with a running keyword, constantinopolitanus. The key letter picks one of 13 reciprocal alphabets "
                   "(pairs ab, cd, ..., yz). The keyword starts again with each cipher run and runs on across line breaks. Latin "
                   "lower-case letters inside clear German written in Kurrent; word division not kept. The looped upright d-shape "
                   "is f; a heavy dot opening two runs on image 119 is a blotted o.",
        "symbol_kind": "letters", "distinct_symbols": 26, "diacritics": {"used": False}, "homophones": {"used": False},
        "nomenclator": {"present": False}, "nulls": {"present": "unknown"}, "key_order": "keyword-derived", "word_division": "none",
        "notes": "Table chosen by testing Porta, Vigenère, Beaufort and variant on the first 22 letters of run 120.5 at all 20 "
                 "offsets; only Porta at offset 0 read (\"ernicht\"). Frozen, then applied to all other runs (held out).",
    },
    "conditions": {
        "prior_solution": {"exists": "no",
                           "where": "No edition or decipherment found: two web searches (12 Nov 2026) returned only finding-aid entries "
                                    "for the Jähring letter series; the vetting of 3 Nov 2026 found nothing in DECODE, Tomokiyo or Lasry. "
                                    "The only decipherment work on the leaves is the contemporary keyword alignment by a second hand on images 120-121.",
                           "found": "not found", "used": False},
        "inputs": ["images", "key from archive", "cleartext context"],
        "attack": "key from archive",
        "human_role": "WAINUT set the task (catalogue 2030) and the rules; AI language-model agents transcribed, chose and froze the "
                      "table, ran the held-out test, read and checked. No target-specific human intervention. No human palaeographer checked the text.",
        "tools": ["Arcinsys digitalisate images", "scripts in this folder (decryption, held-out test, mark check, reading counts)"],
        "models": ["AI language-model agents (WAINUT), viewing the images"],
        "first_date": "2026-11-12", "last_date": "2026-11-13",
    },
    "solution": [
        {"date": "2026-11-12", "kind": "access",
         "what": "Images 119-122 of HStAD D 4 487/4 fetched at full size from digitalisate-he.arcinsys.de, one at a time, 2 s apart.", "result": "worked"},
        {"date": "2026-11-12", "kind": "key from source",
         "what": "Keyword \"constantinopolitanus\" taken from the second hand's writing over the cipher of images 120-121. Porta, Vigenère, "
                 "Beaufort and variant tested on the first 22 letters of run 120.5; Porta at offset 0 read. Key frozen (key_frozen.tsv).", "result": "worked"},
        {"date": "2026-11-12", "kind": "transcription",
         "what": "Sign conventions written first; runs of images 119 and 120 (upper) in two passes from fresh crops; run 120.5 and four "
                 "lines of 121 in one rough pass.", "result": "partial"},
        {"date": "2026-11-12", "kind": "control", "technique": ["key matching", "other"],
         "what": "All 16 runs of 119 and 120 (upper) held out. Frozen key as frozen: 303/346 letters (0.876) match the final reading; with "
                 "the two sign values set after the freeze (looped d = f, dot = o): 330/348 (0.948). Vigenère and Beaufort with the same "
                 "keyword: at most 4/346 (0.012). Figures after the five letter corrections of the blind review; before them 298/346 (0.861) "
                 "and 325/348 (0.934).", "result": "worked"},
        {"date": "2026-11-12", "kind": "reading",
         "what": "Runs decrypted mechanically and read as German with every departure marked; scripts/check_marks.py passes. Dan's reading "
                 "checker on the German sentences: 0.70 (image 119) and 0.857 (image 120, upper runs); whole files 0.541 and 0.500 with "
                 "the English notes counted.", "result": "worked"},
        {"date": "2026-11-12", "kind": "literature search",
         "what": "Two web searches on Jähring, Georg Karl, Darmstadt, 1792 and cipher: finding-aid entries only.", "result": "partial"},
        {"date": "2026-11-13", "kind": "verification",
         "what": "Blind review by one independent AI language-model agent: about 230 cipher letters in 7 of the 16 runs and 14 letters of "
                 "121 copied from its own crops before seeing ours, about 93% letter agreement; five letters (q read as g or y) taken over, "
                 "removing five marked changes; check_marks.py, the decryption and the held-out figures reproduced; the four sentences of "
                 "image 120 read against the translation, 4 of 4 hold.", "result": "worked"},
    ],
    "outcome": {
        "class": "read in part", "key": "recovered", "method": "read with known key",
        "method_basis": "Keyword written by a contemporary second hand over the cipher of images 120-121; table (Porta) identified on 22 "
                        "letters of run 120.5, frozen and tested on the 16 other runs.",
        "contribution": ["transcription", "key recovered"],
        "fraction_read": 0.03, "fraction_read_method": "estimated",
        "fraction_read_source": "Images 119-121 of a 226-image volume; the rest of the volume was not paged through for cipher, so the share "
                                "is a rough estimate. Within images 119-121, under half of the cipher letters are in read runs; the block of 121 is not transcribed.",
        "verification": ["independent verification", "contemporary decipherment", "matched control", "historical consistency"],
        "provenance": "contributed",
        "credits": [
            {"who": "contemporary", "role": "key or decipherment used",
             "note": "the keyword \"constantinopolitanus\" written by a second hand over the cipher letters of images 120 (foot) and 121",
             "date": "1792", "source": "HStAD D 4 Nr. 487/4, images 120-121"},
            {"who": "lccompany", "role": "solution",
             "note": "Porta table identified and frozen, tested on 16 held-out runs; runs of 119 deciphered, upper runs of 120 read in part, "
                     "fragments of 120.5 and 121 decoded", "date": "2026-11-12"},
            {"who": "lccompany", "role": "transcription",
             "note": "runs of images 119 and 120 in two passes; four lines of 120.5 and 121 in one pass", "date": "2026-11-12"},
            {"who": "lccompany", "role": "verification",
             "note": "one independent AI reader, blind: about 230 cipher letters in 7 of the 16 runs copied from the image, the marks, decryption "
                     "and held-out figures reproduced, the image 120 reading checked as sentences; no human palaeographer", "date": "2026-11-13"},
        ],
        "key_file": ["key.tsv", "key_frozen.tsv"],
        "gaps": [
            {"item": "Run 120.5 (about 4 lines) and the cipher block of image 121 (about 10 lines)", "blocker": "not-attempted",
             "detail": "Overwritten by the second hand's key letters and strokes; only four line fragments transcribed, in one pass. The key "
                       "works on all four and the key letters give each line's offset, so a careful transcription should read them."},
            {"item": "Holes: 119L.2 (6 letters), the middle of 119.7 (6), the end of 119.13 (3), nine letters of 120.2", "blocker": "not-attempted",
             "detail": "The decryption does not read there; the transcription of these letters should be checked against the image."},
            {"item": "120.1, line 2, fourth letter (s or the looped d-shape)", "blocker": "needs-physical-access",
             "detail": "Undecided on this image; s gives the a of \"anstatt\", the looped d-shape would give x. Kept as s."},
            {"item": "Images 1-118 and 122-226 of 487/4, and 487/6", "blocker": "not-attempted",
             "detail": "Not paged through for further cipher; short runs elsewhere were seen only on contact sheets."},
        ],
        "texts": [
            {"doc": "img119_jun1792", "label": "Image 119, letter of 1 June 1792: 12 short cipher runs",
             "transcription": "transcription_119.txt", "decryption": "decryption_119.txt", "reading": "reading_119.md",
             "translation": "translation_119.md", "language": "de", "state": "not prose",
             "summary": "Business letter of 1 June 1792: the building goes slowly, the cash box, constant withdrawals of credit, people try "
                        "to harm \"our credit\" but \"we keep it all the same\"; the correspondents \"are well disposed\"; Jacobi and a thousand guilders.",
             "note": "Not prose: 12 runs of one to five words (28 words) inside a letter in clear German; each completes a clear sentence. "
                     "Words: 19 verbatim from the signs, 6 with a marked change (14 Nov 2026: three r read as v on the image), 3 holes (119L.2, part of 119.7, end of 119.13). Clean share "
                     "of the German sentences 0.70 (10 sentences); whole file 0.541. The clear frame is an approximate working transcription."},
            {"doc": "img120_bericht_upper", "label": "Image 120 right, report \"Unterthänigster Bericht\": the four upper runs",
             "transcription": "transcription_120.txt", "decryption": "decryption_120.txt", "reading": "reading_120.md",
             "translation": "translation_120.md", "language": "de", "state": "read in part",
             "summary": "The fair ended \"gloriously\" instead of getting stuck, as Jähring had feared; \"he\" made them a cash fund of 7,000 "
                        "guilders at the fair; the prince is asked to say gracious things to him when he sees him.",
             "note": "Four clause-length runs (37 words): 29 verbatim from the signs, 7 with a marked change, 1 hole (nine letters of 120.2). "
                     "Clean share of the German sentences 0.857 (7 sentences); whole file 0.500. The clear frame is an approximate working transcription.",
             "reading_review": {"grade": "B", "by": "independent AI language-model agent (blind review)", "date": "2026-11-13",
                                "note": "Read as sentences against translation_120.md: 4 of 4 sentences hold, the second with one 9-letter hole, and the "
                                        "translation matches with the holes kept. 37 cipher words checked; the agent's own copy of the four runs from the "
                                        "image gave five letter corrections, none of which changes a word."}},
            {"doc": "img120_121_bericht_block", "label": "Run 120.5 and image 121: the rest of the report",
             "transcription": "transcription_121_pass1.txt", "decryption": "decryption_121.txt", "reading": "reading_121.md",
             "translation": "translation_121.md", "language": "de", "state": "decoded, not read",
             "summary": "Fragments only: \"er nicht\", \"[...] aber er [hat] alles auf die verbindlichste Art gethan\", \"Kuppel ist gut\", \"vortheilhafte\".",
             "note": "About 14 cipher lines, overwritten by the second hand's key letters; only four line fragments transcribed in one pass. "
                     "The words of the fragment reading cover 52 of the 98 transcribed letters (7/35, 20/25, 12/17, 13/21, changed letters "
                     "included); the lines are not yet read. Whole-file clean share 0.286."},
        ],
    },
}
json.dump(P, open(HERE / 'profile.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('profile.json written', t119, t120, len(c121))
