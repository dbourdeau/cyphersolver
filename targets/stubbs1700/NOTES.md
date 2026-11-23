# stubbs1700 — Letter in three ciphers to George Stubbs, University College, Oxford (SAL THO/57/127), c. 1698–1701

Source: Society of Antiquaries of London, archives, THO/57/127 (Thorpe Bequest; THO/57 = original letters mainly to John Thorpe senior, 1684–1768). Catalogue: « Letter or letters in three different cyphers addressed to George Stubbs, University College, Oxford », 18th c. Images © Society of Antiquaries of London, read from its online catalogue (see Conditions of use of the images): **not distributed, no crop or derivative included**. Cite « Society of Antiquaries of London, archives ».

## Prior art
None found: DECODE (Stubbs, Stubbes, Thorpe, Antiquaries: no record; Oxford: only Civil War items), cyphersolver catalogue/leads/issues, web search. First reading.

## Addressee and date
George Stubbes, son of John of Hinton (Wilts), clergyman; matriculated University College 31 March 1697/8 aged 15; fellow of Exeter 1701–25 (Foster, *Alumni Oxonienses 1500–1714*, p. 1438). The address « University College » therefore points to 1698–1701. The letter mentions dining with a lady who wrote « Fatal Friendship » (Catharine Trotter's tragedy, 1698), consistent with that window. The shelf position in THO/57 (alphabetical by correspondent, Ellis 1816) gives no date. John Thorpe senior (University College, 1704) was a college contemporary: the piece probably passed to him from Stubbs.

## The ciphers
Three pages, three simple-substitution alphabets of invented signs for English, no word division, no homophones, no nomenclator:
- p. 1 — small boxes with wedges at up to 8 positions (pigpen-like); three margin columns written sideways (same alphabet rotated 90°).
- p. 2 — horizontal bars with ticks up, down or crossing; four margin columns.
- p. 3 — letter-like glyphs (look-alikes of digits, Latin and Greek letters); two margin rows.
The text runs on continuously from p. 1 to p. 3 (one letter, changing alphabet at each page).

## Protocol and measure (prereg/)
- Transcription: two blind passes (Opus agents, codebooks in blind/) and a blind arbiter per page and for the margins.
- Keys built by simulated annealing (English quadgrams, bijective swaps) on a training portion only; frozen with SHA-256 together with the protocol and the scorer (score.py) before the measure.
- Measure: lexical coverage (max-coverage segmentation over an 18th-c. English lexicon, sources hashed in prereg/lexicon_SOURCES.sha256) of the decoded held-out portion; 200 permuted-key controls. Criterion ≥ 0.85 and ≥ best control + 0.30. One measure per page; portions burnt.

| Page | Held-out | Signs | Score | Best control | Mean control | Verdict |
|---|---|---|---|---|---|---|
| p. 1 | lines 33–41 | 315 | 0.848 | 0.479 | 0.290 | **fail** (threshold missed by 0.002) |
| p. 2 | lines 61–68 | 304 | 0.915 | 0.500 | 0.259 | pass |
| p. 3 | lines 28–34 | 327 | 0.976 | 0.551 | 0.327 | pass |

The p. 1 key is reported as **not validated**, as pre-registered, although its decryption reads as continuous English (held-out portion: « …being come to my inn after I had refreshed myself a little… »).

## Reading (rule of #728)
Words of the clear text (the cipher has no word division); sure = every letter given as is by the frozen key on the arbitrated transcription; probable = one sign corrected; restored = two or more; unresolved = not read. Margins included.

| Page | Words | Sure | Probable | Restored | Unresolved | Share sure |
|---|---|---|---|---|---|---|
| p. 1 | 363 | 278 | 62 | 12 | 11 | 0.766 |
| p. 2 | 671 | 557 | 87 | 18 | 9 | 0.830 |
| p. 3 | 422 | 370 | 41 | 6 | 5 | 0.877 |
| **Total** | 1,456 | 1,205 | 190 | 36 | 25 | **0.828** |

Read in part (below 95 %). Most probable words are single transcription slips (similar signs), not key doubts. Notes in reading_P*.md are in French.

## Content
An Oxford student (« my most dearly beloved alma mater ») writes to Stubbs from Salisbury at assize time: the night ride, Cupid keeping him awake, the cathedral spire (« pyramid ») and Harnham Hill; he delivers Stubbs's letters, meets an old gentleman who praises Stubbs, his friend George Hayward, the coffee house, verses on a smock race given to Tom Hill by Mr Taylor; the fop Elderton, Peg Kingsman's shop, Betty Bachelour, the cathedral sermon, « my dearest Mrs Horrell »; dinner with a witty lady author of « Fatal Friendship »; ten men hanged at the assizes; closes « atque hic finis erat ». Latin: « semper eum magna iuvenum stipante caterva » (Virgil, *Aen.* 1.497); « iam monte petitus rideo anhelantem dura ad fastigia turbam » (as deciphered; source not identified). Sender not named in what was read.

## Remaining gaps
- P1 key not validated (held-out 0.848 < 0.85) - blocker: no-key-material; no fresh held-out portion of the p. 1 cipher remains for a second measure (the portion is burnt, and the rest of the page served as training)
- P3 glyphs (γ-like 7 merged with 7; h/k not separated in the margin rows) - blocker: illegible; separating them needs a new look at the original or a higher-resolution image
- Whether the images may be analysed with an AI assistant - blocker: not-attempted; not asked of the Society of Antiquaries (see Conditions of use of the images)

## Escalation
- [n/a] siblings: one letter; the three pages are in three different alphabets
- [n/a] clear-pages: no clear copy or decipherment with the letter
- [n/a] known-keys: no key sheet known for these ciphers
- [x] print: DECODE, the cyphersolver catalogue, leads and issues, and a web search found no earlier reading (Prior art above)
- [x] key-rebuild: one key per page by annealing on a training portion; one measure per page
- [ ] retry: p. 1 would need a fresh held-out portion; none left in this letter

## Conditions of use of the images
- The four images (three pages and the address) were read from the Society of Antiquaries of London's online catalogue, https://collections.sal.org.uk/tho.57.127, where the pages carry the notice "All images are copyright of the Society of Antiquaries and must not be reproduced without prior permission." We treat that as study only (the "Private study only" wording is our summary of it, as in issue #754, not a phrase of the Society's). No images, crops or derivatives are in this pull request.
- The Society's archivist pointed us to the letters on 23 Nov 2026 ("already digitised and can be seen on our catalogue") and wrote that she would be "very keen to see them become part of your project". That is welcome of the decipherment, not a permission to reproduce images, and it says nothing about AI.
- On 23 Nov 2026 Brice Dudout wrote back with this result and asked whether the Society would allow one image on L'Europe chiffrée, with credit; no answer yet. Nobody has signed or agreed to any further condition; the only terms we know are the catalogue notice.
- AI analysis was not raised with the archive: neither the Society's messages nor ours mention it, so the Society has not agreed to AI transcription or analysis. The transcription and reading were done with AI assistants on the strength of the catalogue's study use alone.

## Doubts
- p. 1 key not validated (0.848).
- p. 3: a γ-like variant of glyph 7 (probably p) was merged with 7 (o) in the frozen transcription, so some p read as o; h/k not separated in the margin rows.
- p. 1 margin: one rotation artefact (h read g) in the sideways columns.
- Sender unidentified; date from internal evidence only.
