"""Write r1854/profile.json (run from r1854/)."""
import json

D = '2026-09-22'


def doc(i, read, date, year, route, lang, clear, plain, tok, dist, f, notes, src="none", partial=False):
    return {"id": i, "read": read,
            "shelfmark": "Archivio di Stato di Mantova, Archivio Gonzaga (busta not given on DECODE), DECODE R1854 image " + i.split('-')[1][1:],
            "date": date, "year": year, "country": "Mantua", "route": route, "language": lang, "pages": 1,
            "cleartext_in_document": clear,
            "plaintext": {"location": plain, "source": src, "partial": partial},
            "length": {"tokens": tok, "distinct": dist, "unit": "symbols", "measured": True, "file": f},
            "transcription": {"by": "llm from images", "source": "DECODE images via saved session cookie",
                              "image_quality": "fair", "notes": notes}}


docs = [
    doc("R1854-P1", "not read", "22 Apr 1428", 1428, "Rome -> Mantua", "Latin (runs; possibly Italian)", "interspersed", ["none"], 262, 29, "ct_p1.txt",
        "First pass by the model, second pass sign by sign by a subagent (p1v2.txt): 262 signs in 3 runs."),
    doc("R1854-P2", "read", "9 Aug 1428", 1428, "Rome -> Mantua", "Latin", "none", ["none"], 1802, 53, "ct_p2.txt",
        "Two passes by the model at 2-5x; glyph splits (bold/dotted nabla, tailed/plain circle) found by the solver and checked in the image."),
    doc("R1854-P3", "read", "6 Nov 1428", 1428, "Forli -> Mantua", "Italian", "interspersed", ["interlinear"], 894, 56, "ct_p3.txt",
        "Gloss read by one subagent (p3_gloss.md), signs by a second (p3_signs.txt).",
        "Contemporary letter-by-letter interlinear decipherment, faint; about two-thirds legible.", True),
    doc("R1854-P4", "read", "13 Feb 1430", 1430, "Rome -> Mantua", "Latin", "none", ["none"], 1537, 46, "ct_p4.txt",
        "First pass by the model; second pass by a subagent against the image (209 edits)."),
    doc("R1854-P5", "read", "21 Feb 1430", 1430, "Rome -> Mantua", "Latin", "separate passages", ["none"], 199, 31, "ct_p5.txt",
        "Verso, image upside down; three cipher lines re-transcribed by a subagent."),
]
docs[3]["transcription"]["corrections"] = 209

S = [
    ("access", "Fetched R1854 (5 images), the R1853 register (14 images) and DECODE metadata with the saved cookie.", "worked"),
    ("reading", "Viewed the images: four letters to Gianfrancesco Gonzaga (Rome 22 Apr and 9 Aug 1428, Forli 6 Nov 1428, Rome 13/21 Feb 1430), not one; P3 carries an interlinear decipherment; P5 is an upside-down verso.", "worked"),
    ("literature search", "Web search for Pandolfo Malatesta's ciphered letters (Treccani DBI; Falcioni 2015 prints the plaintext of his 1438 cipher letter, ASMn AG b. 1081).", "partial"),
    ("key from source", "Read the R1853 register keys (Malatesta keys on f. 1, 1406-1419 keys): none match the 1428-30 letters.", "failed"),
    ("transcription", "First-pass sign transcription of P2 (37 lines) by the model.", "worked"),
    ("statistics", "P2: IC 0.040, 46 sign types -> homophonic; the triangle precedes sign 17 in 21 of 29 cases -> q/u.", "worked"),
    ("solver", "Homophonic anneal on P2 with the Latin model and q/u fixed: Latin words appear (quod, predicto, ibidem, filium).", "partial"),
    ("transcription", "P2 second pass at 5x separating look-alike glyphs.", "worked"),
    ("solver", "Per-sign and per-occurrence rescoring of P2 finds nulls, the bold/dotted nabla split (s/null) and con/et/rum signs; P2 reads as continuous Latin.", "worked"),
    ("transcription", "First-pass transcription of P4 (28 lines) and P5 (3 lines).", "worked"),
    ("solver", "Latin anneal on P4 gives readable Latin (post recessum, sollicitabo bullam, galeotam); key applied to P5.", "partial"),
    ("transcription", "Subagent second pass of P4 and P5 against the image with the key: 209 edits, glyph splits.", "worked"),
    ("reading", "P4 and P5 read in full apart from four short spots.", "worked"),
    ("reading", "Subagent read P3's faint interlinear gloss (about two-thirds legible) and the three name codes.", "partial"),
    ("transcription", "Subagent transcribed P3's 894 cipher signs with gloss letters attached.", "worked"),
    ("key from source", "P3 key from the gloss (30 sign values) plus rare signs from context; whole letter deciphered from the signs.", "worked"),
    ("transcription", "P1 cipher runs transcribed (266 signs).", "worked"),
    ("solver", "P1 anneals in Latin and Italian, with and without spaces, costed nulls, vowel constraint, reversed orders, split and merged digraphs: no reading.", "failed"),
    ("control", "Solver reads a synthetic 266-letter monoalphabetic Latin text, also with 12% token noise: P1 is not a simple substitution in Latin.", "worked"),
    ("sibling key", "Register key 'cum Malatesta dni Pandulfi' values seeded into the P1 anneal: -4.2/char, no fit.", "failed"),
    ("sibling key", "Opened all other Mantova records on DECODE (R7858-R7888): 16th-17th century keys.", "failed"),
    ("transcription", "Subagent second pass of P1 (262 signs, 3 runs, 3 misreadings fixed) and clear-text transcription.", "worked"),
    ("solver", "P1 re-solved from the second pass in Latin, Italian and modern Italian: no reading.", "failed"),
    ("statistics", "P1: digraphic test (sign-pair IC 0.005, no), periodicity test (column IC flat for periods 2-8, not polyalphabetic), vowel/consonant alternation 0.713 above all 200 shuffles (linear text, not transposed).", "worked"),
    ("solver", "P1 annealed in Spanish, Catalan, French, German, Portuguese, and with order-3 Latin/Italian models over 150 restarts: no reading.", "failed"),
]

prof = {
    "schema_version": 1, "target": "r1854",
    "title": "Four cipher letters to Gianfrancesco Gonzaga, Rome and Forli 1428-1430 (DECODE R1854, Mantova)",
    "documents": docs,
    "system": {
        "types": ["homophonic", "nomenclator"],
        "summary": "Three different homophonic substitutions in graphic signs with nulls, syllable signs (con, et, -rum) and a few name codes (P2, P3, P4-5); P1 a letter-like sign system not identified.",
        "symbol_kind": "digits and symbols", "distinct_symbols": "unknown", "diacritics": {"used": False},
        "homophones": {"used": True}, "nomenclator": {"present": True, "kinds": ["names", "titles"]},
        "nulls": {"present": True}, "key_order": "not applicable", "word_division": "none",
        "sibling_key": "none (DECODE R1853 is the c. 1401-1420 register; no 1428-30 key)",
        "notes": "P2: bold nabla = s, dotted nabla = null. P3: code signs for signor Malatesta, fiol del s. marchese, papa. P4-5: x written cx; et/con/-rum signs."},
    "conditions": {
        "prior_solution": {"exists": "partial", "where": "P3 only: contemporary interlinear decipherment on the letter. DECODE status 'Partially decrypted' with no transcription.",
                           "found": "before attempt", "used": True},
        "inputs": ["images", "cleartext context"], "attack": "ciphertext-only",
        "human_role": "Project-level: DECODE login cookie and /goal target setting. No target-specific intervention.",
        "tools": ["PIL (crops)", "r1854/solve.py homophonic annealer on lang/ models", "refine.py and occ.py rescoring"],
        "models": ["claude-opus-5-5", "subagents for transcription passes"],
        "sessions": 1, "first_date": D, "last_date": D},
    "solution": [{"date": D, "kind": k, "what": w, "result": r} for k, w, r in S],
    "outcome": {
        "class": "read in part", "fraction_read": 0.915, "fraction_read_method": "measured",
        "fraction_read_source": "Cipher signs read as sense per letter: P2 1740/1802, P3 869/894, P4 1486/1537, P5 199/199, P1 0/262 -> 4294/4694 = 0.915 (tokens measured with _check_profile.py on ct_p*.txt; doubtful spans hand-counted in reading_p2/p3/p4.md).",
        "verification": ["contemporary decipherment", "historical consistency", "key confirms"],
        "key": "partial", "codes_open": {"open": 1, "total": 6, "tokens_open": 1},
        "notes": "Three of the four letters read (P2, P3, P4+P5). P1, Pandolfo Malatesta's 22 April 1428 runs, not read: an unidentified system, no key.",
        "gaps": [
            {"item": "P1 Pandolfo Malatesta 22 Apr 1428, 262 signs", "blocker": "no-key-material",
             "detail": "not a simple or homophonic substitution; register keys do not fit; key material likely ASMn AG b. 1081 c. 159-160 (1438 cipher letter) with b. 840 c. 95 (its translation), not online"},
            {"item": "P2 code ARO and doubtful spans", "blocker": "too-short", "detail": "single occurrences"},
            {"item": "P3 signs Z, fk", "blocker": "too-short", "detail": "unglossed, 1-2 occurrences"},
            {"item": "P4 L04, L14, L20 spots", "blocker": "illegible", "detail": "786-px scan"}]}}

with open('profile.json', 'w', encoding='utf-8') as fh:
    json.dump(prof, fh, indent=1, ensure_ascii=False)
    fh.write('\n')
