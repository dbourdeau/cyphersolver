import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = 'Siblings sweep (Het Utrechts Archief Huis Amerongen via archieven.nl OAI-PMH oai_ead), 9 Nov 2026'
rows = []
def row(**k):
    k.setdefault('seen', 'catalogue'); k.setdefault('needs_archive_scan', 'yes'); k.setdefault('source', SRC)
    rows.append(k)

row(year=1742, date='1742 (after 15 [month])', 
    title="Hyndford's letters from Breslau to Reinhard van Reede (Huis Amerongen), 'grotendeels in code' (mostly in code)",
    correspondents='Hyndford ("generaal", te Breslau; presumably John Carmichael, 3rd earl of Hyndford, British envoy to Frederick II) -> Reinhard van Reede (Amerongen)',
    place='Breslau', language='unknown (English or French)', region='Low Countries', period='1701-1800',
    shelfmark='Het Utrechts Archief, toegang 1001 Huis Amerongen, inv. nr. 3534 (old ref. I, 456-467)',
    folio_note='1 omslag (folder), "(>15)" letters; within 3517-3534 "Ingekomen brieven afkomstig van buitenlandse vertegenwoordigers, 1730-1742"; scope note: "De brieven van Hyndford grotendeels in code."',
    cls='B',
    status='Inventory scope note: the letters of Hyndford are mostly in code. No decipherment mentioned; not scanned online as far as the inventory says. Sibling of the Torck volumes (inv. 3486-3488) in the same fonds, which are already a lead (catalogue 2446) but this is a different correspondent and a plainly "mostly code" item.',
    why='First Silesian War, spring 1742: the British envoy who mediated the Breslau preliminaries (June 1742) writing to the Dutch statesman Van Reede; the British side of the same traffic is already a lead (Robinson to Hyndford, 9 May 1742, TNA SP 87/8, in the catalogue). Over 15 letters, "mostly in code", in one folder; the fonds also holds code tables (inv. 3577), so a key may be on file.',
    importance=4, solvability=3, difficulty=3,
    score_note='Scored from the EAD scope note in the archieven.nl OAI-PMH harvest (inv. 3534, 9 Nov 2026); not viewed',
    verify='Request scans of inv. 3534 from Het Utrechts Archief; compare the code with the Cijfercodes in inv. 3577 and with the British Hyndford/Robinson keys in TNA SP 106/20-21; check whether "generaal" Hyndford is the earl (Carmichael was not a general).',
    links=[{'href': 'https://hetutrechtsarchief.nl/collectie/609C5B993DA84642E0534701000A17FD', 'label': 'Het Utrechts Archief record (inv. 3534)'},
           {'href': 'https://harvest.archieven.nl/OAI/OAIHandler?verb=GetRecord&metadataPrefix=oai_ead&identifier=609C5B99657D4642E0534701000A17FD', 'label': 'OAI-PMH EAD of 1001 Huis Amerongen (record id of the whole fonds; inv. 3534 is component 609C5B993DA84642E0534701000A17FD)'}],
    access_note='description only in the inventory; scans on request or reading room at Het Utrechts Archief (the inventory pages need JavaScript; the EAD is open data via OAI-PMH)',
    prior_art='open as far as checked (9 Nov 2026): known.py (Hyndford, Reinhard van Reede, Amerongen) finds only the TNA Robinson-Hyndford lead and the Torck lead; two web searches (Hyndford Breslau 1742 Van Reede code; Reinhard van Reede cijfercodes) found nothing on a decipherment or edition.')

row(year=1736, date='1736-10-13', 
    title="Letter in code from Berlin, 13 Oct 1736, filed with cipher tables for the secret correspondence of Reinhard van Reede (Huis Amerongen)",
    correspondents='unknown writer at Berlin -> Reinhard van Reede (Amerongen); possibly the Dutch agent Demeraet (inv. 3531, Berlin 1736-37) or the British secretary Guy Dickens (inv. 3532)',
    place='Berlin', language='unknown (Dutch, French or German)', region='Low Countries', period='1701-1800',
    shelfmark='Het Utrechts Archief, toegang 1001 Huis Amerongen, inv. nr. 3577 (old ref. I, 714; II, 361)',
    folio_note='1 omslag: "Cijfercodes voor de geheime correspondentie, z.j., met een in code geschreven brief uit Berlijn, 1736 okt. 13"; inventory adds "Het stuk is digitaal beschikbaar"',
    cls='B',
    status='Inventory title names both the cipher tables ("cijfercodes", undated) and one letter written in code from Berlin on 13 Oct 1736; the item is flagged as digitised (viewer not reachable without a browser, so not viewed). No decipherment mentioned.',
    why='A ciphertext filed with its own code tables is the ideal small case: a Dutch diplomatic code of the 1730s with the key in the same folder. The tables may also serve the Torck volumes (inv. 3486-3488, "enkele in cijferschrift") and the Hyndford letters (inv. 3534).',
    importance=3, solvability=4, difficulty=2,
    score_note='Scored from the EAD item title in the archieven.nl OAI-PMH harvest (9 Nov 2026); the item is marked digitised but the images were not opened (Het Utrechts Archief viewer needs JavaScript)',
    verify='Open inv. 3577 in the Het Utrechts Archief online viewer (hetutrechtsarchief.nl, 1001 Huis Amerongen, inv. 3577); decipher the Berlin letter with the tables; test the same tables on inv. 3486-3488 and 3534.',
    links=[{'href': 'https://hetutrechtsarchief.nl/collectie/609C5B9975934642E0534701000A17FD', 'label': 'Het Utrechts Archief record (inv. 3577)'}],
    access_note='marked "digitaal beschikbaar" by the archive; the viewer is a JavaScript application, images not reachable by curl',
    prior_art='open as far as checked (9 Nov 2026): known.py (Reinhard van Reede, Amerongen, Demeraet, Hyndford) finds no entry for inv. 3577; two web searches (Reinhard van Reede 1736 Berlijn code; Huis Amerongen cijfercodes) found only the inventory itself.')

json.dump(rows, open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(rows))
