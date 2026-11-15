import json
SRC = "Omont et al., Catalogue general des manuscrits francais (Paris, 1895-1918), OCR at archive.org (NAF II/III/IV, Ancien Saint-Germain III, Anciens petits fonds I-III), 15 Nov 2026"


def g(a):
    return [{"href": "https://gallica.bnf.fr/ark:/12148/" + a, "label": "Gallica " + a}]


def n(c):
    return {"href": "http://archivesetmanuscrits.bnf.fr/ark:/12148/" + c, "label": "archivesetmanuscrits " + c}


PA = ("open as far as checked (15 Nov 2026): known.py and shelfmark grep against catalogue.json, leads.json, targets and sweeps; "
      "no web, Tomokiyo or Lasry search made in this sweep")
rows = []


def add(**k):
    base = dict(language="French", region="France", period="", source=SRC, seen="catalogue", needs_archive_scan="no",
                prior_art=PA, links=[], cls="B",
                score_note="Scored from the printed Omont entry (OCR) on 15 Nov 2026; the leaf itself not viewed. The OCR heading number was "
                           "checked against Gallica's title where a Gallica record is named.")
    base.update(k)
    rows.append(base)


add(year=1655, date="1651-1660",
    title="Cardinal Mazarin to abbe Fouquet: letters 'originaux chiffres', with a copy of the cipher at ff. 1-2 (Francais 23202)",
    correspondents="Jules Mazarin -> Basile Fouquet (abbe Fouquet); a few letters to others", place="France (court on campaign)",
    period="1601-1700", shelfmark="BnF, Manuscrits, Francais 23202",
    folio_note="Omont: 'Originaux chiffres ou autographes; on y a ajoute (fol. 1-2) une copie du chiffre'; letters from other writers at ff. 217, 289-298, 381-388. "
               "DECODE already holds four records from this volume (R7894 f.67, R7895 f.279, R7896 f.306, R7897 f.350, all marked solved on Cryptoole); the rest of the ciphered originals is the lead.",
    cls="A",
    status="Printed catalogue says the originals are in cipher with the key copied at ff. 1-2; four letters have DECODE records marked solved, the remainder of the volume's ciphered letters not located as read.",
    why="A whole run of one minister's ciphered letters to one correspondent, with the key in the same volume and four solved letters as a check; one key per entry.",
    importance=3, solvability=4, difficulty=2, decode_ids=["7894", "7895", "7896", "7897"],
    verify="Open Gallica btv1b9063488m, list the ciphered leaves and compare with DECODE R7894-R7897; read the key at ff. 1-2.",
    links=g("btv1b9063488m") + [n("cc52504r")],
    folio_gallica="digitised: btv1b9063488m (title checked: Recueil de lettres adressees par le cardinal Mazarin a l'abbe Fouquet (1651-1660))")

add(year=1562, date="1557-1567",
    title="Charles de Danzay, ambassador in Denmark: correspondence 'originale et en partie chiffree', 1557-1567 (Francais 20140 f. 16)",
    correspondents="Charles de Danzay (French envoy in Copenhagen) -> the French court", place="Copenhagen", region="Denmark",
    period="1501-1600",
    shelfmark="BnF, Manuscrits, Francais 20140 (Recueil de pieces relatives a la Suede et au Danemark, 1557-1706), f. 16 ff.",
    folio_note="Omont: 'Correspondance, originale et en partie chiffree, de Charles de Danzay, ambassadeur en Danemark, 1557-1567 (fol. 16)'; volume 56 ff.; Gaignieres 679.",
    cls="B",
    status="Partly ciphered letters, no decipherment noted. Tomokiyo's Danzay to Henry III (1574) is a different letter and period; no key in this volume is named.",
    why="Early Danzay cipher letters of the 1550s-60s; a sibling of the 1574 Danzay cipher on Tomokiyo's list, so the change of cipher can be dated and a key may carry over.",
    importance=2, solvability=3, difficulty=3,
    verify="Open Gallica btv1b52521512h from f. 16; compare the nomenclator with the Danzay 1574 entry (Cryptoole cryptiana:Danzay to Henry III (1574)).",
    links=g("btv1b52521512h") + [n("cc51725m")],
    folio_gallica="digitised: btv1b52521512h and btv1b10782904z (title checked: Recueil de pieces relatives a la Suede et au Danemark. (1557-1706))")

add(year=1705, date="1700-1713",
    title="Pere Roslet (Minim) to Cardinal de Noailles, letters with 'des clefs des chiffres employes' at the head of vol. I (Francais 23227-23228)",
    correspondents="Pere Roslet, minime -> Louis-Antoine, cardinal de Noailles", place="France", period="1701-1800",
    shelfmark="BnF, Manuscrits, Francais 23227-23228 (Noailles papers 23210-23229)",
    folio_note="Omont: tome I ff. 1-6 'des clefs des chiffres employes'; tome II f. 253 two letters of Pere Francoeur. The OCR garbles the leaf counts and the heading of the series; "
               "the numbers 23227-23228 are taken from the printed line 'XVIII-XIX (23227-23228)'. No Gallica record found for 23227 (SRU, 15 Nov).",
    cls="A",
    status="The cardinal's correspondent writes with ciphers whose keys are in the volume; not stated that the letters are deciphered. Whether all or only some letters are enciphered is not said.",
    why="Keys in the same volume as a run of letters, 1700-13: a small cipher corpus with its key.",
    importance=2, solvability=4, difficulty=2, needs_archive_scan="yes",
    verify="Confirm the shelfmark and digitisation; check whether the letters are in cipher.")

add(year=1615, date="1601-1630",
    title="Chanvallon and Breval to the duke of Lorraine and his secretary Voillot, three volumes of autograph letters, 'differents chiffres' added at the end of vol. II (NAF 3145-3146 bis)",
    correspondents="MM. de Chanvallon and de Breval -> Duke of Lorraine / Voillot", place="Lorraine", region="Lorraine",
    period="1601-1700", shelfmark="BnF, Manuscrits, Nouvelles acquisitions francaises 3145, 3146, 3146 bis",
    folio_note="Omont: 'A la fin du tome II sont ajoutes differents chiffres'; 425 + 244 + 349 ff. Only the key sheets are mentioned, not ciphered letters.",
    cls="B", status="Ciphers with letters of two Lorraine agents; whether any letters are ciphered is unknown. No decipherment noted.",
    why="Lorraine's diplomatic cipher in use 1601-30 with keys at the end of vol. II; a chance of ciphered passages.",
    importance=2, solvability=3, difficulty=3, needs_archive_scan="yes",
    verify="Find out whether the NAF volumes are digitised (no Gallica record found by SRU on 15 Nov; the NAF source string may differ).")

add(year=1585, date="1585",
    title="'Lettres, en chiffres' addressed to 'Conraden Breiffenstein, oder Laurentzen Riedet' at Delft, within a Low Countries miscellany (NAF 22330 f. 107)",
    correspondents="unnamed -> Conrad Breiffenstein or Laurent Riedet", place="Delft", language="not stated (German-addressed)",
    region="Netherlands", period="1501-1600", shelfmark="BnF, Manuscrits, Nouvelles acquisitions francaises 22330, f. 107",
    folio_note="Omont: 'Fol. 107. Lettres, en chiffres, adressees a Conraden Breiffenstein, oder Laurentzen Riedet, a Delft, etc.' in 'Melanges sur l'histoire des Pays-Bas'; the preceding item is dated 1585.",
    cls="B", status="Small cipher letters from the Dutch Revolt; no decipherment noted.",
    why="Short, unusual German-addressed ciphers of 1585 at Delft; probably few leaves.",
    importance=2, solvability=2, difficulty=3, needs_archive_scan="yes",
    verify="Order or find NAF 22330 f. 107; number of ciphered leaves unknown.")

add(year=1768, date="4 Aug 1768",
    title="Abelard's epistle to Heloise 'transcrite en caracteres cryptographiques' by Villette, 15 ff. (NAF 11238)",
    correspondents="Villette (copyist); a literary text copied in cipher", place="France", period="1701-1800",
    shelfmark="BnF, Manuscrits, Nouvelles acquisitions francaises 11238",
    folio_note="Omont: 'Epitre d'Abailard a Heloise, transcrite en caracteres cryptographiques. A la fin: Fait par Villette, ce 4 aoust l'annee 1768.' 15 ff., 202 x 145 mm. research/sweep_2026-11_arabic mentions NAF 11238 only as a non-script item, not as a lead.",
    cls="C",
    status="A known text (an Abelard/Heloise epistle, in some French version) written in a substitution script; no decipherment noted.",
    why="A crib-able plaintext (the epistle, in one of a few French versions) over 15 leaves with the copyist's own date: the easiest kind of cipher once the version is matched.",
    importance=2, solvability=5, difficulty=1, needs_archive_scan="yes",
    verify="Order NAF 11238; identify the version (18th-century French renderings of Pope's Eloisa and the Latin letters) and test.")

add(year=1746, date="1746",
    title="Audibert (music master, Lyon): use of musical notation to cipher despatches, in Le Dran's musical papers (NAF 4543 f. 180)",
    correspondents="Audibert, maitre de musique de l'Academie du roi a Lyon -> Le Dran (Affaires etrangeres)", place="Lyon / Paris",
    period="1701-1800", shelfmark="BnF, Manuscrits, Nouvelles acquisitions francaises 4543 (Le Dran, Memoires musicaux, tome I), f. 180",
    folio_note="Omont: 'Papiers d'Audibert ... relatifs a l'emploi de la notation musicale pour chiffrer les depeches (1746)'. A proposal and perhaps specimens, not a correspondence.",
    cls="C", status="A music-notation cipher; any specimens are in the volume; no decipherment noted. A system, not a field correspondence.",
    why="A cipher disguised as music from the Affaires etrangeres, with its explanation in the same papers.",
    importance=3, solvability=3, difficulty=3, needs_archive_scan="yes",
    verify="Order NAF 4543 f. 180; check for a sample and explanation.")

add(year=1530, date="c. 1520s-1540s",
    title="Gaignieres vol. VII: letters to the Grand-master Anne de Montmorency, 'depeches chiffrees' relating to Italy (Francais 20506, 250 ff.)",
    correspondents="J. de Langeac (bp of Avranches), Claude Dodieu de Velly, G. de Selve (bp of Lavaur), Francisque (count of Pontremoli), Gregorio Casali, Annebault, Saint-Blancard and others -> Anne de Montmorency",
    place="Italy", region="Italy", period="1501-1600", shelfmark="BnF, Manuscrits, Francais 20506 (Gaignieres 394)",
    folio_note="Omont: 'Lettres adressees au grand-maitre Anne de Montmorency, depeches chiffrees et pieces diverses, relatives surtout a l'Italie' (250 ff.). Parts are already in the repo: Dodieu de Velly ff. 49 and 52 (Tomokiyo, catalogue 308), the Ranzo copy ff. 136-138 (DECODE R4450); NAF 4206 holds keys for Dodieu and Du Bellay. Other ciphered leaves are unidentified. The dates are not given in the printed line.",
    cls="A",
    status="Volume already touched by the repo, but the printed entry says despatches are enciphered throughout and the other leaves are not claimed anywhere.",
    why="A 250-leaf volume of Italian despatches in cipher with Friedmann's keys (NAF 4206) and Tomokiyo's Dodieu cipher as ready keys.",
    importance=3, solvability=4, difficulty=2, decode_ids=["4450"],
    verify="Walk the Gallica volume leaf by leaf; list ciphered leaves beyond ff. 49, 52, 136-138 and match them to NAF 4206 keys.",
    links=g("btv1b525047581") + [n("cc518506/cd0e635")],
    folio_gallica="digitised: btv1b525047581 (title checked: Recueil de lettres et pieces originales des XVIe et XVIIe siecles forme par Gaignieres. VII Lettres)",
    prior_art="partly known: fr. 20506 ff. 49, 52 (Tomokiyo Dodieu cipher 1) and ff. 136-138 (R4450) are in CATALOGUE.md / SOLVED_CATALOGUE.md; the rest open as far as checked (15 Nov 2026, repo grep only)")

json.dump(rows, open('candidates.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(rows))

keys = [
    dict(shelfmark="BnF, Francais 20974", what="Clefs de la correspondance chiffree de Francois, duc de Guise, avec quelques lettres de lui (1556); keys for Dalbeyne (f. 8), comte de La Mirandole (f. 12), Dominique Du Gabre bp of Lodeve (ff. 16, 40), Anne d'Este and others. Catalogue 194 / DECODE R2276 is pp. 1-3 of this volume (read in part). Gallica btv1b9062131g, title checked.", links=g("btv1b9062131g")),
    dict(shelfmark="BnF, Francais 20975", what="'Steganographie, chiffres et dechiffremens', alphabets and grilles for secret writing, 17th c., 79 ff. Gallica btv1b90619093, title checked. A manual, not a letter.", links=g("btv1b90619093")),
    dict(shelfmark="BnF, NAF 4206", what="Friedmann's key collection (21 ff.) for Dodieu, Du Bellay, Dinteville, Selve, Ferrara 1528-49; points to fr. 3000, 3019, 3020, 3045, 3077, 3096, 3126 and Dupuy 265, 547. Already in the ledgers (DECODE R9467, R9481). fr. 3029 and fr. 3092 are not named in the entry."),
    dict(shelfmark="BnF, NAF 8431 (453), ff. 173-221", what="'Recueil de chiffres diplomatiques du XVIe siecle': keys of Annebaut (Piedmont 1542), G. d'Armagnac (Rodez 1544), Fresse and Richer (Denmark 1543-46), La Croix, Lyves, Botieres, Lestrange, Dampierre, Monluc (Venice), and common keys for Portugal, the Emperor, Rome, England, Venice, Germany, Italy; 49 ff. inside a patents volume. No ciphertext. Heading as printed."),
    dict(shelfmark="BnF, NAF 5371 f. 49", what="'Chiffres communs' of the prince of Monaco (Rome), Tallard (London) and Bonrepaux (The Hague), copy, 1702. Key only."),
    dict(shelfmark="BnF, NAF Renaudot papers, volume after NAF 7494, f. 143", what="'Chiffres donnes a differents ministres du Roy', copy by E. Renaudot, late 17th c. The OCR heading ('1603') is wrong and the volume number is not established. Key only."),
    dict(shelfmark="BnF, Francais 23026 p. 203; Francais 23594-23596 f. 403", what="La Boderie's cipher for his London despatches (1606-11). Relevant to the repo's laboderie1608 and jeannin1607 targets. No Gallica record found by SRU for 23026 and 23594 on 15 Nov."),
    dict(shelfmark="BnF, Francais 20746 ff. 47-50", what="'Des chiffres pour la correspondance' in the abbe Le Tellier's Italian journey papers, 1667-68; the letters themselves apparently clear. No Gallica record found by SRU."),
    dict(shelfmark="BnF, NAF 10760-10761", what="'Vocabulaire cryptographique' (1699, Latin title 'Signorum in numeris et speciebus institutio'): a code vocabulary for military and political signals, 340 + 335 ff. A code book, no ciphertext."),
    dict(shelfmark="BnF, NAF 22336 f. 97", what="'Chiffre adresse par un anonyme, au mois de juin 1781, a M. Hauy, abbe de l'Academie royale d'ecriture': a second copy or sibling of lead 1195 (BULAC MS.ARA.52 item 14, 'Texte chiffre' sent to Hauy). Check it is the same cipher and add this shelfmark to lead 1195 at merge."),
    dict(shelfmark="BnF, Ancien Saint-Germain francais 18985 f. 47", what="'Dechiffrement de lettres adressees a Francois I par les princes d'Allemagne' in a 1275-1636 German-relations miscellany: a decipherment, so a pointer for a key hunt; the ciphered letters may sit in the same or a neighbouring volume."),
]
json.dump(keys, open('key_leads.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
