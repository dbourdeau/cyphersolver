"""Wave 11: narrow leads 2867-2876 to letters with no filed decipherment and no Calendar of State Papers entry, write the
vetting block (access 'archive', 'not online'), ready for `_check_catalogue.py --promote`."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
LP = os.path.join(ROOT, 'research', 'leads.json')
leads = json.load(open(LP, encoding='utf-8')); L = leads if isinstance(leads, list) else leads['leads']
M = json.load(open(os.path.join(HERE, 'match_result.json'), encoding='utf-8'))
by = {e['id']: e for e in L}
CSP_PRIOR = {
    2867: 'CSP Spain vol. 3 (1525-29)', 2868: 'CSP Spain vol. 3 (1525-29)', 2869: 'CSP Spain vol. 3 (1525-26)',
    2870: 'CSP Spain vol. 2-3 (1522-27)', 2871: 'CSP Spain vol. 2 (1522-23)', 2872: 'CSP Spain vol. 2 (1522-24)',
    2873: 'CSP Spain vol. 2 (1522-23)', 2876: 'CSP Spain vol. 2-3 (1521-25)'}
NO_CSP = 'No Calendar of State Papers Spain volume covers 1650-56'
WHO = 'claude session 15 Nov 2026 (Claude Sonnet 5.5), Chrome wave 11 vetting'
WHERE = ("Badator (artxibo.euskadi.eus) 'Exportar Busqueda' CSV of the RAH Salazar y Castro index, run in Chrome 15 Nov 2026 "
         "(wave 10 export of 'cifra', wave 11 exports of cifrado, cifrada, cifradas, cifras, clave, descifrado, descifrar); each record quotes "
         "the index's own remark. Not online: the leaves are in the RAH volumes.")
NOTE_RULE = ("Rule applied 15 Nov 2026: the vetting bar accepts 'not online' for an archive item (access 'archive') that quotes the archive's "
             "description, provided no decipherment of the same text is filed with it; wave 10's 'ciphertext is in the RAH volumes' was not a bar "
             "failure. Narrowed to the letters whose index record has no decipherment (marginal, interlinear or a 'Texto descifrado' leaf) and, "
             "where a calendar exists, which the Calendar of State Papers Spain does not print.")
QUOTE = {
    2867: "'Original, en cifra' (index remark), e.g. 1526-09-12 A-38 f.289",
    2868: "'Original, en cifra', 'Original, en italiano, en cifra'",
    2869: "'Original, en cifra'",
    2870: "'Original, en cifra' (the index says of A-29 f.41 'cuyo texto descifrado no sigue a continuacion')",
    2871: "'Original, en cifra' (one letter four folios wholly in cipher)",
    2872: "'Original, en cifra'", 2873: "'Original, en cifra'", 2874: "'Original, en cifra' (A-98)", 2875: "'Original, en cifra' (A-92)",
    2876: "'Original, en su mayor parte en cifra' (A-27 ff.45-48, 453-456), 'gran parte en cifra, muy estropeado' (A-22 f.200)"}
KEYS = {
    2867: ("Lasry's partial reconstruction of the Perez-Charles V cipher of 1527 (BnF fr. 3022 f.12, 24 Sep 1527; GL.htm) is a lead to the key: "
           "three-letter codes unidentified; whether it is the cipher of these RAH letters is not tested. A key does not block (3 Nov rule)."),
    2868: ("Caracciolo's 1537 cipher is Luo's Cifrario 38 (targets/caracciolo1537), a different cipher; the filed decipherments of his 1525-29 "
           "letters are the plaintext/ciphertext pairs of this key. Not tested."),
    2870: "Kolosova (2017, pp. 251-277) is said to print Lannoy's own cipher as viceroy of Naples (per Tomokiyo); not held, not tested.",
    2873: "Compare Kolosova's Adrian VI letter no. 31 (a different letter); no key tested."}
DUPT = {
    2867: ['Juan Perez', 'A-40'], 2868: ['Caracciolo', 'A-36'], 2869: ['Herrera', 'A-37'], 2870: ['Lannoy', 'A-29'], 2871: ['Colonna', 'A-27'],
    2872: ['Adorno', 'A-23'], 2873: ['Adrian VI', 'A-26'], 2874: ['Trivulzio', 'Tribulcis', 'A-98'], 2875: ['Leopold Wilhelm', 'A-92'],
    2876: ['Marin abad de Najera', 'Fernando Marin']}


def main():
    for lid in range(2867, 2877):
        e = by[lid]
        if lid <= 2875:
            rows = M[str(lid)]
            keep = [x for x in rows if x[3] != 'CAL']
            cal = [x for x in rows if x[3] == 'CAL']
            flist = '; '.join('%s %s f.%s' % (x[0], x[1], x[2]) for x in keep)
            clist = '; '.join('%s %s f.%s' % (x[0], x[1], x[2]) for x in cal) or 'none'
            e['folio_note'] = ("After wave 11 narrowing: %d letters with no filed decipherment in the index and no Calendar of State Papers entry: %s. "
                               "Left out: %d index-open letters that the CSP prints (%s), the letters with a filed decipherment, and duplicate copies of those."
                               % (len(keep), flist, len(rows) - len(keep), clist))
            if 'without a filed decipherment' in e['title']:
                e['title'] = e['title'].replace('without a filed decipherment', '%d letters without a filed decipherment or CSP entry' % len(keep), 1)
            e['status'] = "Index description only (Badator export, 15 Nov 2026): archive item, not online; no image linked from the Badator record."
            n_open = len(keep)
        else:
            n_open = 12
        e['access'] = 'archive'
        e['access_note'] = "RAH Salazar y Castro volumes (Madrid); Badator record read in Chrome 15 Nov 2026, no image linked. " + NOTE_RULE
        e['scored'] = 'vetted'
        csp = CSP_PRIOR.get(lid, NO_CSP)
        if lid in CSP_PRIOR:
            edition = (csp + ": letters it prints are excluded from this lead (a calendar entry means the editor read the letter); letters it marks "
                       "'Contemporary deciphering on separate sheet' are filed decipherments and excluded.")
        else:
            edition = csp + "; no edition of these letters found (web search 15 Nov 2026)."
        e['vetting'] = dict(
            date='2026-11-15', by=WHO,
            seen=dict(kind='not online', where=WHERE, extent='%d letters (index records), RAH Salazar y Castro' % n_open,
                      cipher=("Archive text: %s. No decipherment is filed on or with these records: the index would say 'texto descifrado', "
                              "'descifrado al margen' or 'entre renglones' otherwise (remarks like 'cuyo texto descifrado no sigue' count as not filed); "
                              "records with one are excluded." % QUOTE[lid])),
            prior_art=dict(
                decode=("known.py, the DECODE dumps and the Cryptoole snapshot searched for the sender and shelfmarks (15 Nov 2026): no DECODE record "
                        "for the RAH letters (the dumps are partial, so 'not on DECODE' is as far as they go)."),
                tomokiyo=("Tomokiyo's Cryptiana, web search 15 Nov 2026: " + (
                    "the Juan Perez 1527 unsolved letter in his Charles V article is a BnF letter, not these RAH leaves." if lid == 2867
                    else "nothing on these RAH letters under this sender.")),
                lasry=("GL.htm (Lasry's list, repo copy and web search 15 Nov 2026): " + (
                    "'Perez-Charles V Cipher (1527)', partial reconstruction from BnF fr. 3022 and Clair. 326, different letters; no entry for the RAH letters."
                    if lid == 2867 else "no entry for this sender or these shelfmarks.") + " Lasry's papers: nothing found."),
                edition=edition,
                literature="web search 15 Nov 2026 (sender, 'cifra', Salazar y Castro): no study of these letters' cipher"),
            searches=[dict(query="Calendar of State Papers Spain (British History Online): every 'Salazar, A. N, f. M' reference in vols 2-4 harvested and cross-matched by volume and folio",
                           result="%d index-open letters checked; those calendared are excluded (see folio_note)" % (len(M[str(lid)]) if str(lid) in M else 0))],
            key_check=KEYS.get(lid, "No key known; the filed decipherments of the same sender's other letters are the plaintext pairs. Not tested."),
            duplicates=("known.py " + ", ".join("'%s'" % t for t in DUPT[lid]) + " (15 Nov 2026): only this lead and its wave 10/11 sweep records; "
                        "the catalogue's Lannoy, Adrian VI and Salazar y Castro A-7/A-10 entries are different letters, and the targets "
                        "lannoy1527, sanchez1522, soria1523 are other senders."),
            verdict='open')
        if lid in KEYS:
            e['vetting']['key_held'] = KEYS[lid]
    json.dump(leads, open(LP, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    open(LP, 'a').write('\n')


main()
