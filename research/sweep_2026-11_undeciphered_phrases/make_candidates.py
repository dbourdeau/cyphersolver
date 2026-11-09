import json
SRC = 'Undeciphered-phrases sweep (Hungaricana regests of the Vienna Hungarian files via Chrome; TNA Discovery API), 9 Nov 2026'
PRIOR_HU = ("known.py on the shelfmark, 'Ungarische Akten Allgemeine' and 'Fasc. N. Konv.' (9 Nov 2026): no hit in catalogue, leads, targets or DECODE; "
            "only AA Fasc. 5 Konv. B (Hofmann 1527, catalogue) is known. Two web searches (Ferdinand I 1529 cipher/Chiffre; Herberstein 1530 Posen "
            "chiffrierter Brief) found no edition or decipherment; the Hungaricana regest does not mention one (unlike its neighbours, which say "
            "'feloldassal' or 'sorkozben feloldva').")
ACC_HU = ("Hungaricana 'Becsi segedletek' regest only (HHStA finding aid, no images on Hungaricana). The original is in the Haus-, Hof- und "
          "Staatsarchiv, Vienna (Ungarische Akten); AIS images not checked for this unit.")


def hu(year, date, title, corr, place, lang, shelf, folio, status, why, imp, sol, diff, bid, label):
    return dict(year=year, date=date, title=title, correspondents=corr, place=place, language=lang, region='Central Europe',
                period='1497-1559', shelfmark=shelf, folio_note=folio, cls='B', status=status, why=why, importance=imp,
                solvability=sol, difficulty=diff,
                score_note='Scored from the Hungaricana regest (Vienna delegation finding aid), 9 Nov 2026; leaf not seen.',
                verify="Order or find the AIS images; check the same Konvolut for a decipherment sheet (neighbouring items are described as deciphered between the lines or on a separate sheet).",
                links=[{'href': 'https://archives.hungaricana.hu/hu/lear/BecsSeg/%s/' % bid, 'label': label}],
                seen='catalogue', source=SRC, prior_art=PRIOR_HU, needs_archive_scan='yes', access_note=ACC_HU)


rows = [
    hu(1529, '1529 (no day)', "Letter 'almost entirely in cipher' filed with Andreas Mihalewyth's letters to Radul, voivode of Wallachia (Latin)",
       "unknown -> Andreas Mihalewyth / Radul (Wallachia), in Ferdinand I's Hungarian files", "unknown", "Latin (cipher text)",
       "HHStA Wien, Ungarische Akten, Allgemeine Akten, Fasc. 13 Konv. C, fol. 3-4", "fol. 3-4; verso names 'Mihalewith'",
       "Hungaricana regest: a letter written almost entirely in cipher (Hungarian: 'szinte teljesen sifrirban irt level'), original Latin; verso only the name Mihalewyth, filed after Mihalewyth's letters to Radul of Wallachia. No decipherment or key noted.",
       "A nearly all-cipher letter from the 1529 Zapolya-Ferdinand war, in the Wallachian/Transylvanian intelligence stream; long ciphertext if the leaf is full.",
       3, 3, 3, 142904, "Hungaricana BecsSeg 142904 (Fasc. 13 Konv. C 3-4)"),
    hu(1529, '1529 (no day)', "Anonymous ciphered letter (Latin), Ferdinand I's Hungarian General Files, Fasc. 13",
       "unknown -> unknown (Ferdinand I's side)", "unknown", "Latin (cipher text)",
       "HHStA Wien, Ungarische Akten, Allgemeine Akten, Fasc. 13 Konv. C, item 20", "item 20",
       "Hungaricana regest: ciphered letter from an unknown person ('sifrirozott level'), original Latin; no decipherment noted.",
       "Sibling of fol. 3-4 in the same Konvolut; two ciphered 1529 pieces from the same stream give two samples for one key.",
       3, 3, 3, 142915, "Hungaricana BecsSeg 142915 (Fasc. 13 Konv. C 20)"),
    hu(1529, '10 Mar 1529', "Anonymous partly ciphered letter to Ferdinand I (Latin)",
       "unknown -> Ferdinand I", "unknown", "Latin (partly cipher)",
       "HHStA Wien, Ungarische Akten, Allgemeine Akten, Fasc. 10 Konv. C, item 31", "item 31",
       "Hungaricana regest: partly ciphered letter of an unknown person to Ferdinand I, original Latin. Items 28-30 of the same Konvolut (10 Mar 1529, Turkish war preparations) are explicitly deciphered between the lines; item 31 carries no such note.",
       "Same day and probably the same hand or cipher as the interlinearly deciphered spy report fol. 28-30, which could serve as a crib source if item 31 is unread.",
       3, 4, 2, 142345, "Hungaricana BecsSeg 142345 (Fasc. 10 Konv. C 31)"),
    hu(1530, '9 Nov 1530', "Sigmund von Herberstein to Ferdinand I, Posen (Poznan): partly ciphered letter on the armistice negotiations",
       "Sigmund von Herberstein -> Ferdinand I", "Poznan", "Latin or German (partly cipher; regest gives only 'orig.')",
       "HHStA Wien, Ungarische Akten, Allgemeine Akten, Fasc. 16 Konv. B, fol. 103-104", "fol. 103-104",
       "Hungaricana regest: Herberstein to Ferdinand, partly ciphered letter about the armistice negotiations. No decipherment noted.",
       "Herberstein's own cipher letter from the autumn 1530 Poznan congress (Zapolya/Ferdinand truce); a named diplomat and a dated event allow checking against the calendared content.",
       4, 3, 3, 164502, "Hungaricana BecsSeg 164502 (Fasc. 16 Konv. B 103-104)"),
    hu(1530, '17 Nov 1530', "Ciphered report from Augsburg to Ferdinand I touching the Turkish question (German)",
       "unknown (Augsburg) -> Ferdinand I", "Augsburg", "German (partly cipher)",
       "HHStA Wien, Ungarische Akten, Allgemeine Akten, Fasc. 16 Konv. B, fol. 46, 49-50", "fol. 46, 49-50",
       "Hungaricana regest: also deals with the Turkish question; cipher; original German. No decipherment noted.",
       "A German-language cipher from the Augsburg Reichstag winter of 1530; the regest does not name the writer, so check the leaf.",
       3, 3, 3, 164480, "Hungaricana BecsSeg 164480 (Fasc. 16 Konv. B 46, 49-50)"),
]
r = hu(1529, '28-29 Nov 1529', "Letters of Bishop Gerendi, Caspar Horvath and Alexius to the ruler from Nagyszeben, partly in secret writing",
       "Bishop Gerendi; Caspar Horvath; Alexius -> Ferdinand I", "Nagyszeben (Hermannstadt)",
       "Regest says 'spanyol' (Spanish) for the original; probably a mis-regest, to be checked on the leaf",
       "HHStA Wien, Ungarische Akten, Miscellanea, Fasc. 431.A (Einzuteilende Nachtraege 1505-1575) Konv. A, fol. 68, 69 (fol. 65, 22 Oct 1529, has a Latin translation at fol. 66)",
       "fol. 68-69 (fol. 65-66 translated)",
       "Hungaricana regest: partly in secret writing ('reszben titkos iras') for fol. 68 (28 Nov 1529) and fol. 69 (29 Nov 1529); for fol. 65 the regest adds that the Latin translation is at fol. 66, but no translation is noted for fol. 68-69.",
       "Transylvanian letters to Ferdinand at the height of the 1529 war, with a translated sibling (fol. 65/66) that could give cribs.",
       3, 3, 3, 154541, "Hungaricana BecsSeg 154541 (Misc. Fasc. 431 fol. 68)")
r['links'].append({'href': 'https://archives.hungaricana.hu/hu/lear/BecsSeg/154542/', 'label': 'Hungaricana BecsSeg 154542 (fol. 69)'})
r['links'].append({'href': 'https://archives.hungaricana.hu/hu/lear/BecsSeg/154538/', 'label': 'Hungaricana BecsSeg 154538 (fol. 65, translated at 66)'})
rows.append(r)
rows.append(dict(
    year=1715, date='23 Oct 1715 (letter) and 23 Nov 1715 (reports)',
    title="Message from 'Nelson' in code, sent to the decipherer John Keill, who could not decode it (1715)",
    correspondents="'Nelson' (informer) -> George Tilson; Keill's reports to Tilson and Townshend", place='Oxford (Keill); sender unknown',
    language='unknown (Keill thought the cipher language "High Dutch")', region='England', period='1701-1800',
    shelfmark='TNA SP 35/4/47 (enclosure: message from Nelson in code), with SP 35/4/61 and SP 35/4/62',
    folio_note='SP 35/4/47 enclosure 1; reports SP 35/4/61 and /62', cls='B',
    status="TNA Discovery: SP 35/4/47 'Keill ... reporting on a paper from Nelson and the possible code to decipher the message. Enclosures: 1. Message from Nelson in code'; SP 35/4/62 (23 Nov 1715): Keill 'believes the cipher to be High Dutch and has found it impossible to decode what is writ in a language he does not understand'. No decipherment recorded in the catalogue.",
    why="A catalogue that itself records a failed contemporary decipherment, by the mathematician-decipherer John Keill, in the months of the 1715 Jacobite rising; a short message, and the hypothesis (German) is a ready first test.",
    importance=3, solvability=3, difficulty=3, score_note='Scored from TNA Discovery descriptions (API), 9 Nov 2026; leaf not seen.',
    verify="Order SP 35/4/47 at Kew; check SP 35/4 for a key or Keill's notes, and BL Add MS decipherers' papers.",
    links=[{'href': 'https://discovery.nationalarchives.gov.uk/details/r/C14915305', 'label': 'TNA SP 35/4/47'},
           {'href': 'https://discovery.nationalarchives.gov.uk/details/r/C14915321', 'label': 'TNA SP 35/4/62'}],
    seen='catalogue', source=SRC,
    prior_art="known.py on 'Keill', 'SP 35/4' (only SP 35/46 matches) and 'Nelson Tilson': no hit. One web search (Keill 1715 cipher Nelson Tilson High Dutch) found Rocher's paper on Jacobite cipher keys and Keill biographies, nothing on this message. The Calendar of State Papers Domestic 1715 was not consulted.",
    needs_archive_scan='yes', access_note='Not digitised on TNA Discovery; order a copy at Kew.'))
json.dump(rows, open('candidates.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(rows))
