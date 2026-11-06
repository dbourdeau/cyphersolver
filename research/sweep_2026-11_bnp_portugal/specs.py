"""Hand-written row fields for build_rows.py (one dict per BNP catalogue record)."""

SPECS = [
 dict(bib=2224639, year=1645, date='1643-1648', period='1611-1650',
      title='António Teles da Silva, governor-general of Brazil → Fernão Teles de Meneses and others: letters from Bahia, parts in cipher',
      corr='António Teles da Silva (governor-general of Brazil 1642-47) → Fernão Teles de Meneses and unidentified recipients',
      place='Salvador da Bahia', region='Americas',
      folio='1 volume, [8 + 1 br.] f., 5 documents; "Partes do texto em cifra"',
      why='Cipher passages from the governor of Brazil during the Pernambuco insurrection against the Dutch (1645) and the War of Restoration.',
      imp=4, sol=2, dif=3, cls='B', known=' on Teles da Silva / Bahia / A.T. 128',
      prior='open as far as checked (5 Nov 2026: DECODE and repo via known.py: nothing; Dinnissen & Araújo, HistoCrypt 2022, "Prey to a Privateer. Two Portuguese Ciphertexts from 1649" read two later Teles da Silva ciphers (NA The Hague, WIC, with keys) and say ciphers were issued in Portuguese Brazil from 1638 on: those keys are the first to try; no reading of these BNP letters found)',
      shelfmark='Biblioteca Nacional de Portugal, Arquivo dos Condes de Tarouca, A.T. 128',
      status='Originals (?) with signatures; Arquivo dos Condes de Tarouca (bought 1971).',
      verify='Order scans of the 5 documents (8 f.); compare the Portuguese royal ciphers of 1643-48 (Vieira, Sousa Coutinho) and the 1646 Dutch-Brazil spy cipher (HistoCrypt 2024, "Mirror for all traitors")'),
 dict(bib=2225064, year=1645, date='1643-1647', period='1611-1650',
      title='Padre Nuno da Cunha (Portuguese agent at the Curia) ↔ João IV: memoranda and letters from Rome, some text in cipher',
      corr='Padre Nuno da Cunha ↔ King João IV', place='Rome', region='Papacy',
      folio='1 volume, [62] f., 31 documents (copies); "Algum texto em cifra"',
      why="João IV's secret negotiation at the Curia for the bishoprics and recognition of the Braganza dynasty, which Rome refused until 1668.",
      imp=4, sol=2, dif=3, known=' on Nuno da Cunha / A.T. 140',
      shelfmark='Biblioteca Nacional de Portugal, Arquivo dos Condes de Tarouca, A.T. 140',
      prior='open as far as checked (5 Nov 2026: DECODE and repo via known.py on Nuno da Cunha / A.T. 140: nothing; web search found the Tempos Históricos 2019 article on Nuno da Cunha and the Holy See 1640-69, not seen, which may quote these papers; no edition of the ciphers found)',
      status='Copies, Arquivo dos Condes de Tarouca.',
      verify='Order scans; check whether the cipher passages are the same as in the Nisa/Vidigueira and Sousa Coutinho Restoration ciphers (BNP COD. 7162, 2666)'),
 dict(bib=2168524, year=1835, date='1831-1845', period='1801-1900', cls='A',
      title="António Ribeiro Saraiva's diary 1831-1845 with its own 'Cifra do diário'",
      corr='António Ribeiro Saraiva (Miguelist agent in London), private diary', place='London', lang='Portuguese',
      folio='13 maços, [635] f.; n.º 13 is "[Cifra do diário]" (the key of the diary); which entries are enciphered is not stated',
      why="The diary of Dom Miguel's agent in London through the civil war and exile; a key filed with it suggests enciphered entries.",
      imp=3, sol=3, dif=1, known=' on Ribeiro Saraiva (lead 1237 covers his correspondence, not the diary)',
      status='The key is bound in as n.º 13; no decipherment noted for the diary entries.',
      verify='View n.º 13 and sample diary years to see how much is enciphered; read with the key in n.º 13'),
 dict(bib=2289236, year=1873, date='29 Mar 1873', period='1801-1900',
      title="Letter partly in cipher to Fontes Pereira de Melo ('amanhã vou a Z ... o enteado de O')",
      corr='unidentified (Elvas) → António Maria de Fontes Pereira de Melo (prime minister)', place='Elvas',
      shelfmark='Biblioteca Nacional de Portugal, Arquivo Fontes Pereira de Melo, FPM-Cx. 01, n. 83',
      folio='[2] f.; partly in cipher (letters standing for names, e.g. "Z", "O")',
      why='A political informer writing to the Regenerador prime minister in 1873 with ciphered names and passages.',
      imp=2, sol=2, dif=2, known=' on Fontes Pereira de Melo / FPM',
      status='Bought at the Pedro de Azevedo auction, 2004.',
      verify='Order a scan; the cipher may be a simple letter code for persons and places'),
 dict(bib=2289754, year=1871, date='1871-1872', period='1801-1900',
      title='Duke of Saldanha (minister in London) → Fontes Pereira de Melo: official telegrams, the first in cipher',
      corr='João Carlos de Saldanha, duke of Saldanha → Fontes Pereira de Melo', place='London → Lisbon',
      shelfmark='Biblioteca Nacional de Portugal, Arquivo Fontes Pereira de Melo, FPM-Cx. 01, n. 127',
      folio='2 telegrams, [4] f.; "Texto cifrado (primeiro telegrama)"',
      why="Saldanha's ciphered telegram from the London legation; Portuguese diplomatic telegraph cipher of the 1870s.",
      imp=2, sol=2, dif=3, known=' on Saldanha / FPM',
      status='Received at the Santa Isabel telegraph station; bought at auction 2004.',
      verify='Order a scan; compare Portuguese MNE telegraph codes of the 1870s (ANTT, AHD)'),
 dict(bib=2290608, year=1859, date='2 Dec 1859', period='1801-1900',
      title='Conde da Lousã (civil governor of Viana) → Fontes Pereira de Melo: official confidential telegram, the first part in cipher',
      corr='Conde da Lousã → Fontes Pereira de Melo (minister of the Kingdom)', place='Viana do Castelo → Lisbon',
      shelfmark='Biblioteca Nacional de Portugal, Arquivo Fontes Pereira de Melo, FPM-Cx. 02, n. 38',
      folio='[4] f.; "Texto cifrado (primeiro telegrama)"',
      why="An early Portuguese government telegraph cipher (1859).", imp=1, sol=2, dif=3, known=' on Lousã / FPM',
      status='Bought at auction 2004.',
      verify='Order a scan; likely a short ministry telegraph code'),
 dict(bib=2259117, year=1915, date='[1900-1930]', period='1901-1950',
      title="Carlos Augusto Tavares de Andrade: artist's notebook written in an invented alphabet 'so as not to be deciphered'",
      corr='Carlos Augusto Tavares de Andrade (1884-1930), personal notebook', place='Portugal (Lisbon?)',
      shelfmark='Biblioteca Nacional de Portugal, Área de Música, EMUS13 27 (Espólio Carlos Augusto Tavares de Andrade)',
      folio='10 f., 23 x 12 cm, whole text in an invented alphabet',
      why='A self-contained secret-script manifesto (technical notes, form and gesture, an essay on art) by a Portuguese composer/artist; a likely monoalphabetic script.',
      imp=1, sol=3, dif=2, known=' on Tavares de Andrade / EMUS13',
      status='The catalogue summarises its content (technical notes, reflection on form, gesture and process, essay on art), so the cataloguer may have read it; no transcription is cited.',
      verify='Order a scan; check with the BNP music area whether a transcription exists',
      access='Not digitised; BNP Área de Música (access "Normal")'),
 dict(bib=2231302, year=1770, date='[1750]-1826', period='1701-1800',
      title='Casa Pombal bundle: papers on the 1st marquês de Pombal, part of the text in cipher',
      corr='Casa Pombal (1st and 2nd marquês de Pombal, King José I and others)', place='Lisbon, Ajuda, Pombal',
      shelfmark='Biblioteca Nacional de Portugal, Arquivo da Casa Pombal, AP/Mc. 110',
      folio='1 maço, 136 documents, [761] f.; "Parte do texto em cifra" (which document not stated)',
      why="Pombal's own papers, incl. the king's letters to him (1769-75) and 'Observações secretíssimas'; a cipher piece in this bundle is unidentified.",
      imp=3, sol=1, dif=3, known=' on Casa Pombal / AP/Mc',
      status='Mixed originals and copies.',
      verify='Ask the BNP which document of the 136 carries cipher; then order that scan'),
 dict(bib=2225661, year=1734, date='1734', period='1701-1800',
      title='Diogo de Mendonça Corte-Real (secretary of state) → conde de Tarouca (Vienna): letters and despatches of 1734, one in cipher',
      corr='Diogo de Mendonça Corte-Real → João Gomes da Silva, 4th conde de Tarouca', place='Lisbon → Vienna',
      shelfmark='Biblioteca Nacional de Portugal, Arquivo dos Condes de Tarouca, A.T. 109a',
      folio='1 livro, [161] f., 82 documents; "Texto em cifra (f. [145])"',
      why='Lisbon\'s instructions to the Vienna embassy in the War of the Polish Succession year 1734.',
      imp=3, sol=2, dif=3, known=' on Tarouca / A.T. 109a / Corte-Real',
      status='Originals signed by Corte-Real, and copies.',
      verify='Order a scan of f. [145]; the Tarouca copy-books (A.T. 26//16-18) may hold the same despatch in clear'),
 dict(bib=2223640, year=1730, date='24 Jan 1723 - 27 Feb 1736', period='1701-1800',
      title='Diogo de Mendonça Corte-Real → conde de Tarouca: correspondence on relations with Castile, England, France and the Empire; a letter with cipher (f. 30v-33)',
      corr='Diogo de Mendonça Corte-Real → João Gomes da Silva, 4th conde de Tarouca', place='Lisbon → The Hague / Vienna',
      shelfmark='Biblioteca Nacional de Portugal, Arquivo dos Condes de Tarouca, A.T. 180//2',
      folio='1 livro, 187 f., 52 documents; "Carta com cifra (f. 30 v.-33)"',
      why='Portuguese secretary of state to his chief diplomat in the 1720s-30s (Colónia do Sacramento, the Spanish crisis of 1735).',
      imp=3, sol=2, dif=3, known=' on Tarouca / A.T. 180 / Corte-Real',
      verify='Order a scan of f. 30v-33'),
 dict(bib=2221826, year=1727, date='1726-1729', period='1701-1800',
      title='Marquês de Abrantes (ambassador in Madrid) → conde de Tarouca: letters on the Madrid mission and the double royal marriage, parts in cipher',
      corr='Rodrigo Eanes de Sá Almeida e Meneses, marquês de Abrantes → João Gomes da Silva, 4th conde de Tarouca', place='Madrid; Lisbon',
      shelfmark='Biblioteca Nacional de Portugal, Arquivo dos Condes de Tarouca, A.T. 157',
      folio='[195] f., 79 documents; "Partes do texto cifrado"',
      why='The 1727-29 negotiation of the Portuguese-Spanish double marriage (the Exchange of the Princesses), from the ambassador in Madrid to his colleague in Vienna.',
      imp=3, sol=2, dif=3, known=' on Abrantes / Tarouca / A.T. 157',
      status='Originals signed, and copies.',
      verify='Order sample scans; the reply side is A.T. 159'),
 dict(bib=2222832, year=1728, date='1727-1729', period='1701-1800',
      title='Conde de Tarouca → marquês de Abrantes: letters on treaties and the Vienna and Hanover alliances, parts in cipher',
      corr='João Gomes da Silva, 4th conde de Tarouca → marquês de Abrantes', place='Vienna → Madrid',
      shelfmark='Biblioteca Nacional de Portugal, Arquivo dos Condes de Tarouca, A.T. 159',
      folio='[128] f., 95 documents; "partes em cifra"',
      why='Tarouca\'s side of the A.T. 157 exchange (Vienna 1727-29).',
      imp=3, sol=2, dif=3, known=' on Abrantes / Tarouca / A.T. 159',
      status='Originals (?) with revisions and corrections (drafts).',
      verify='Order sample scans; drafts may give the clear text beside the cipher'),
 dict(bib=2222958, year=1731, date='1726-1736', period='1701-1800',
      title='Conde de Tarouca → D. Luís da Cunha: copies of letters on European negotiations, parts in cipher',
      corr='João Gomes da Silva, 4th conde de Tarouca → D. Luís da Cunha', place='Vienna → The Hague / Paris',
      shelfmark='Biblioteca Nacional de Portugal, Arquivo dos Condes de Tarouca, A.T. 165',
      folio='1 livro, [123] f., 81 documents (copies, with revisions); "partes do texto em cifra"',
      why='Correspondence between the two leading Portuguese diplomats of João V in the years of the Vienna alliance and the Polish Succession war.',
      imp=3, sol=2, dif=3, known=' on Tarouca / Luís da Cunha / A.T. 165',
      verify='Order sample scans; compare BNP COD. 4417 / COD. 1750 (Cunha letters with cipher, lead 1242)'),
 dict(bib=2223643, year=1736, date='23 Dec 1735 - 9 Nov 1737', period='1701-1800',
      title='Secretaries of state (Corte-Real, António Guedes Pereira) ↔ conde de Tarouca: correspondence on the 1735-37 crisis with Castile and the British/French/Dutch mediation, letters with cipher',
      corr='Diogo de Mendonça Corte-Real, António Guedes Pereira and others ↔ João Gomes da Silva, 4th conde de Tarouca',
      place='Lisbon; Elvas; Madrid → Vienna',
      shelfmark='Biblioteca Nacional de Portugal, Arquivo dos Condes de Tarouca, A.T. 180//3',
      folio='1 livro, 157 f., 73 documents; "Cartas com cifras (f. 3-6 v., 111-114)"',
      why='The Luso-Spanish crisis of 1735-37 (the Madrid embassy incident, the siege of Colónia do Sacramento) seen from Lisbon by the new secretaries of state.',
      imp=3, sol=2, dif=3, known=' on Tarouca / A.T. 180 / Guedes Pereira',
      verify='Order scans of f. 3-6v and 111-114'),
]


# ---- Arquivo dos Condes de Tarouca: one row per volume whose record says cipher (generated) ----
import re as _re

_SERIES = {
 'A.T. 164': ('Conde de Tarouca → his brother Fernando Teles da Silva, 2nd marquês de Alegrete: letters of {y}, parts in cipher',
              'João Gomes da Silva, 4th conde de Tarouca → Fernando Teles da Silva, 2nd marquês de Alegrete (and his nephew the 3rd marquês)',
              "Tarouca's private-political letters to his brother at court from the Utrecht congress, The Hague and Vienna; the cipher hides court and diplomatic news."),
 'A.T. 163': ('2nd marquês de Alegrete → his brother the conde de Tarouca: letters of {y} from the court, parts in cipher',
              'Fernando Teles da Silva, 2nd marquês de Alegrete → João Gomes da Silva, 4th conde de Tarouca',
              "Court news and politics from Lisbon to the plenipotentiary abroad; the reply side of A.T. 164."),
 'A.T. 26': ('Conde de Tarouca ↔ secretary of state Diogo de Mendonça Corte-Real: copy-book of correspondence, {y}, parts in cipher',
             'João Gomes da Silva, 4th conde de Tarouca ↔ Diogo de Mendonça Corte-Real (secretary of state)',
             "Tarouca's official letter-book as plenipotentiary at Utrecht, The Hague and Vienna; cipher passages in the official despatches."),
 'A.T. 229': ('Negociações políticas nas cortes de Heidelberg, Viena e Madrid (Alegrete, Tarouca, Cunha Brochado, Guedes Pereira): volume of despatches {y}, parts in cipher',
              'Marquês de Alegrete, conde de Tarouca, José da Cunha Brochado, António Guedes Pereira ↔ King Pedro II / João V and the secretaries of state',
              "Portuguese embassy papers from Heidelberg (the 1686-87 marriage of Pedro II), Vienna and Madrid; cipher passages in the despatches."),
}


def auto(REC, have):
    out = []
    for bib, r in sorted(REC.items()):
        ex = _re.sub(r'^Exemplares\|Cota\|(Fasciculo\|)?Colecao\|Tipo Acesso\|Estado\|', '', r['exemplares'])
        c = ex.split('|')[0]
        m = _re.match(r'(A\.T\. \d+)(//\d+)?$', c)
        if not m or m.group(1) not in _SERIES or bib in have:
            continue
        f = r['fields']
        txt = ' '.join(f.get(k, '') for k in ('NOTAS', 'CONTEM'))
        if not _re.search(r'cifr', txt, _re.I):
            continue
        if _re.search(r'decifrad', txt, _re.I):
            continue                      # carries its own decipherment: left out (README)
        if not m.group(2) and m.group(1) in ('A.T. 164',):
            continue                      # the series record; its volumes are rowed one by one
        prod = f.get('PRODUÇÃO', '')
        ys = [int(y) for y in _re.findall(r'1[67]\d\d', prod)]
        if not ys:
            continue
        y = ys[0] if len(set(ys)) == 1 else f'{min(ys)}-{max(ys)}'
        t, corr, why = _SERIES[m.group(1)]
        place = prod.split(',')[0] if ',' in prod else 'unknown'
        fol = f.get('DESCR.FÍSICA', '')
        mm = _re.findall(r'[^.;/]*cifr[^.;/]*', txt, _re.I)
        out.append(dict(bib=bib, year=min(ys), date=prod.split(',', 1)[-1].strip() or str(y), period='1701-1800' if min(ys) > 1700 else '1651-1700',
                        title=t.format(y=y), corr=corr, place=place.strip(),
                        shelfmark=f'Biblioteca Nacional de Portugal, Arquivo dos Condes de Tarouca, {c}',
                        folio=f"{fol}; catalogue: {{PHRASE}}",
                        why=why, imp=3, sol=2, dif=3, known=' on Tarouca / Alegrete / Corte-Real / ' + c,
                        verify='Order sample scans of the cipher letters; the Tarouca embassy key of 1707-09 is in BNP COD. 4418, f. 16-23 ("Cifra por que se hade escrever"), and part of a key is bound in A.T. 164//11: try them first',
                        cls='B'))
    return out
