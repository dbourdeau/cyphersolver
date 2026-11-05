import sys
sys.stdout.reconfigure(encoding='utf-8')
from cand import add
from rows_rik import row
rows = [
    row('R0003533', 'Twx98TOXEaEFk8kcjTgJY3', [18, 20, 22, 23], year=1657, date='Dec 1656 - Mar 1657 (one letter dated 22 Jan 1657 new style)',
        title="Gyorgy II Rakoczi, Prince of Transylvania, to Charles X Gustav of Sweden: Latin letters with sign-cipher passages (Polish campaign of 1657)",
        correspondents='Gyorgy II Rakoczi (Georgius Rakoczy) -> Charles X Gustav, King of Sweden', place='Transylvania (Sarospatak / Kolozsvar?)', language='Latin',
        period='1651-1700', shelfmark='Riksarkivet, Diplomatica Turcica, bihang Transylvanica, SE/RA/2119/2119.5/4 ("Furstarnas av Siebenbürgen Georg I och II Rácóczis originalbrev till Kungl. Maj:t", 1632-1659), images 18, 20, 22, 23',
        folio_note='64 images (R0003533). Images 18 (5 sign lines), 20 (about 6 sign lines in a letter about "Rex Poloniae"), 22 (4 sign lines) and 23 (a full page of about 16 lines of signs, about 500 characters, with a faint Latin gloss between some rows).',
        cls='B',
        status='Catalogue: only "originalbrev" of the two Rakoczi princes; no cipher mentioned. Graphic sign cipher, probably monoalphabetic (the Lang repertory describes the same prince\'s sign systems in MOL E 190 as "not broken"). A few glosses are written between the rows at image 23, so a partial reading was made at the time. Not in Lang\'s repertory (checked pp. 191-330 for Swedish-archive items); keys for the same fonds are held (DECODE R4310 "Siebenbürgen Schauis" number key and R4296, Chifferklaver låda II), but they are number keys, not sign keys.',
        why='Rakoczi\'s alliance with Charles X Gustav against Poland (Jan 1657): the sign-cipher passages carry the secret terms between the two allies.',
        importance=4, solvability=4, difficulty=2,
        verify='View images 18-25 at full size; transcribe the signs, align with the partial glosses on image 23, test as a monoalphabetic sign cipher in Latin; check MOL E 190 sign tables (Lang T.Rag) and the printed Swedish-archive editions of the Rakoczi-Charles X letters.'),
]
for r in rows:
    add(r)
