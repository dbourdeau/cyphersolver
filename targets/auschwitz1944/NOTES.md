# auschwitz1944 — Clandestine message (gryps) from the Auschwitz camp resistance, 4 September 1944

Source: Auschwitz-Birkenau State Museum, « A fragment of a secret message sent from Auschwitz » (4 Sept. 1944), consulted on Google Arts & Culture: https://artsandculture.google.com/asset/a-fragment-of-a-secret-message-sent-from-auschwitz/CgGwLMf2NO_MsA (no shelfmark given). **No image, crop or derivative is included or linked here**: screenshots were used for private study only. No snip, portrait or reveal can be made for a write-up page for that reason.

Polish clear text with about thirty words written as runs of numbers 1–30 (points 7 to 9); signed (signature not read).

## Prior solution (found after the attempt, not used)
The message is printed, decoded, in I. Paczyńska (ed.), *Grypsy z Konzentrationslager Auschwitz Józefa Cyrankiewicza i
Stanisława Kłodzińskiego* (Kraków, WUJ, 2013), p. 439. L. Sadzikowska, *Identität und Fremdheit* (V&R unipress 2022, open
access, DOI 10.14220/9783737015165), p. 120 and note 240, quotes point 8 in German with that reference ("Jasia aus dem
TWL [Truppenwirtschaftslager] Rajsko", the Gärtnerei, Józek the gardener), and attributes the message to Cyrankiewicz
and Kłodziński. Both were pointed out by Daniel Bourdeau in his review of #1010 (27 Nov 2026), after our reading was
made; neither was used for it. We have not seen p. 439 itself, so Paczyńska's readings of points 7 and 9 are not
compared with ours. From Sadzikowska (p. 120), as reported in that review: G6 *twl* is TWL, Truppenwirtschaftslager;
*Paprzycy* is a surname, Ludwik Paprzyca, a released prisoner; and "jaki może mieć kontakt z wami" is taken as "what
contact can she have with you".

## Prior art searched before the reading
Before the print was found, we noted that this message very probably appears in I. Paczyńska (ed.), *Grypsy z Konzentrationslager Auschwitz Józefa Cyrankiewicza i Stanisława Kłodzińskiego* (Kraków, WUJ, 2013), which edits and decodes the clandestine letters of Cyrankiewicz and Kłodziński; A. Paszek's thesis (*Komunikowanie się w warunkach ekstremalnych…*, UPJPII Kraków, 2025, §5.4 p. 170) decodes at least one message of this system. Neither was available to us (the public PDF of the thesis stops at p. 141; the free WUJ extract covers neither the key table nor this message). Our reading was made without either. Kłodziński's instruction of 16 Jan 1943 (Paczyńska pp. 33–34, gryps no. 49, quoted by Paszek p. 127) reads in full: « Nazwiska i ważne rzeczy szyfrem: „Kto się w opiekę podda Pany swemu” itd. a więc: k= 1, t=2, o=3, s=4, i=5, ę=6, w=7, o=3, p=9, i=10, e=11, k=1, ę=6, p=9, itd. cały alfabet, bez szcz, cz, rz, itd. » **The key of this 1944 message differs from it** (p=8, e=9, not p=9, e=11). Either the system was simplified into a compact table between 1943 and 1944 (Cyrankiewicz, 23 Jan 1944: « zrobić alfabet z odnośnymi cyframi », Paszek p. 127), or the quotation is imprecise; neither is shown.

Signature: it looks like « Stakło », Kłodziński's pseudonym, which signs the gryps of 6 Sept 1944 (Piper, *Dzieje Najnowsze* LI, 2019, 3, pp. 216-218); not established.

Context (sourced): Rada Wojskowa Oświęcim formed in mid-1944 by the Kampfgruppe Auschwitz and the AK to prepare armed action if the SS tried to kill the prisoners as the front approached (Piper 2019, p. 214); on 6 Sept 1944 Kłodziński and Cyrankiewicz reported plans to liquidate Birkenau (Piper pp. 216-218); Kłodziński's channel through the Rajsko gardening kommando (Paszek p. 135). The message does not say what the explosives were for; no source links it to the Sonderkommando revolt of 7 Oct 1944.

## Transcription
Two blind passes by agents without any key (`blind/PASSE-A.md`, `blind/PASSE-B.md`, in French), then a blind arbiter working from the image only (`transcription.txt`, SHA-256 a83492f6…, frozen 26 Nov 2026 23:57 CET before any test; `blind/SHA256.txt` lists it under its working name TRANSCRIPTION-GELEE.txt). 39 groups, 183 numbers plus one « ? » sign. Doubts (a?b, a retained) are listed in `transcription.txt` § DOUTES.

## Measures (both reported)
1. **PREREG 1** (`prereg/PREREG.md`, SHA-256 88f909c8…): six keys (song read position by position in three text versions, first-appearance numbering with « całym », « Komu w opiekę », an offset). Dev G1–G19, validation G20–G39, lexicon of 4,352 Polish forms built from the thesis text (hash in the prereg; the list itself is not included), 200 permuted controls. **Failed**: no key beat its controls; validation 0/18. G20–G39 burnt.
2. **Exploration on the burnt groups only** (declared in PREREG-2): *kontakt* (twice), *materjały wybuchowe*, *przez*, *ogrodnika*, *prasę* give the first-appearance order of the hymn with « A całem sercem szczerze ufa jemu ». This is the **church version** (Śpiewnik kościelny, Mioduszewski 1838), not Kochanowski's 1579 text (« A całem prawie sercem ufa Jemu »), which gives r17 f18 j19 …; PREREG-2 wrongly called it Kochanowski 1579 and quoted an unattested 4th line (« Nie przypadnie na mię… »; the hymn has « Nie przyjdzie na mnie żadna straszna trwoga », giving the same y27). h28 and ó30 were set from one burnt word each (*wybuchowe*, *Józka*); they fall at their rank in **stanza 2** of the hymn (h *łowczych*, ź *zaraźliwem*, ó *pióry*), which we had not looked at: an independent confirmation (found by the hostile reviewer).
3. **PREREG 2** (`prereg/PREREG-2.md`, SHA-256 53ab2d1f…, hashed 27 Nov 2026 00:12:46 CET before running `prereg/mesure2.py`): five variants listed in advance, chosen on the burnt groups, one measure on G1–G19 (88 numbers): mean Polish bigram log-likelihood −2.766 against best of 200 permuted controls −4.073 (p < 0.005), and 10 of 16 groups of length ≥ 2 clear Polish words (≥ 50 % required). **Passed.**
   - **Weaknesses, declared**: the fresh portion is small (88 numbers); and G1–G19 had been seen decoded under the six wrong keys of PREREG 1 (F2 matches the final key on values 1–16) before PREREG 2. This weakens the validation, even though the gap is wide.
   - The controls are weak: plain permutations of the same table lose to any table that yields Polish; no near-miss keys (e.g. the 1579 text) were measured. `prereg/mesure2.py` was not hashed (written one second after the PREREG-2 hash); timestamps are local file times only.
   - The bigram model and lexicon come from the public part of Paszek's thesis (text not included).

## Joined groups
- G8+G9 *ob|sługuje*, G10+G11 *SS|manów*, G13+G14 *budy|nku*, G24+G25 *lag|rem*, G28+G29 *tamtejsz(z)e|go*: each join falls at a line end or a « |? » boundary of the transcription; the joins are interpretation.

## Transcription doubts
- G2 pos. 8 (5 against 15) - read: 5 written (i), c by sense, word {większych}; checked: image (blind arbiter, an agent; blind shape sheet by a person, 5 chosen), transcription (two blind passes), decode; word stays probable.
- G3 pos. 8 (3 against 9, overwritten digit) - read: 9, word {przesyłek}; checked: image (blind arbiter, an agent), transcription (two blind passes), decode; word stays probable.
- G28 pos. 1 (« ? »-shaped sign against 2/7) and the doubled 18 (one overwritten) - read: 2 (t), one 18 dropped, word {tamtejszego} (probable for the extra z); checked: image (blind arbiter, an agent; blind shape sheet by a person, 2 chosen), transcription (two blind passes), decode.
- G31 pos. 3 (15 against « 1,5 ») - read: « 1,5 », word jaki (sure); checked: image (blind arbiter, an agent; blind shape sheet by a person, « 1, » with comma chosen, remark « 1,5 dans le cadre »), transcription (two blind passes), decode.
- G33 pos. 4 (21 = ś; group cut at the margin) - read: {mieć}, from sense (ć does not occur in the first two stanzas, so the writer had no number for it); checked: image (blind arbiter, an agent), transcription (two blind passes), decode.
- G38 pos. 9 (22 against 27) - read: 27, word materjały (sure); checked: image (blind arbiter, an agent; blind shape sheet by a person, 27 chosen), transcription (two blind passes), decode.
- G7 pos. 1 (17 against 18, overwritten) - read: 17 (*Rajsko*; 18 gives *zajsko*); checked: image (blind arbiter, an agent), transcription (two blind passes), decode, repeat G17.
- G20 pos. 2 (12 against 17; passes A and B read 17, the arbiter 12) - read: 12, word ona (sure; 17 gives *ora*); checked: image (blind arbiter and hostile reviewer, agents; blind shape sheet by a person, 12 chosen), transcription (two blind passes), decode.
- G6 *twl* - read: TWL (sure); checked: image (blind arbiter, an agent), transcription (two blind passes), decode, edition (Sadzikowska 2022 p. 120, quoting Paczyńska 2013 p. 439: "aus dem TWL [Truppenwirtschaftslager] Rajsko"); the three numbers 2-7-22 give t-w-l with nothing supplied.
- 2/7, 1/7, 9/3, 1/4, 20/70, 23/73, 27/77 elsewhere - read: as retained in transcription.txt § DOUTES; checked: image (blind arbiter, an agent), decode, transcription (two blind passes); every alternative tried decodes to no Polish word.
- G1 *paprzycy* - read: Paprzycy (sure), genitive of the surname Paprzyca; checked: image (blind arbiter, an agent), decode, transcription (two blind passes); Sadzikowska 2022 p. 120 names Ludwik Paprzyca, a released prisoner (not identified by us).
- Clear text of point 6 (L1–L2), one word of point 9 (« prz‹?›bli‹?› ») and the signature - read: as transcribed, {doubtful}; checked: image (two blind passes and arbiter, low resolution), decode (not applicable: clear text).

## Blind digit-shape sheet (27 Nov 2026)
Brice Dudout answered a blind sheet: each doubtful number boxed in its line, options were clean shapes of the same hand cut from sure places, labelled « forme N », with three hidden controls (7, 27, 17). The selection rule was hashed before any thumbnail was cut (`blind/sheet-2711/REGLE-SELECTION.md`, SHA-256 6685162f…, in French). His answers are kept byte for byte (`blind/sheet-2711/reponses-auschwitz-gryps-2711.json`, SHA-256 cf2e6d32…), with the revealed key (`cle-revelee.json`) and `SHA256SUMS`. The thumbnails are not included (images under rights).
- Controls: 3 of 3 recognised, so the sheet is conclusive under the rule.
- Effect: *ona* (12), *jaki* (« 1,5 ») and *materjały* (27) become sure. *tamtejszego* is read with t (2) and stays probable (extra z). *większych* stays probable (5 confirmed; c by sense).
- Count: 29 sure, 4 probable, 1 unread (was 26 / 7 / 1).

## TWL (27 Nov 2026)
G6 *twl* (2-7-22) decodes to t-w-l with nothing supplied; it was counted unread because we did not know the word. The
edition (Sadzikowska 2022, p. 120 and note 240, quoting Paczyńska 2013, p. 439) gives TWL, Truppenwirtschaftslager.
Counts on the 34 cipher words: before, 29 sure, 4 probable, 1 unread (5 holes, 0.853); after, 30 sure, 4 probable,
0 unread (4 holes, 0.882). The text has fewer than 40 cipher words, so the short-text floor applies (README Conventions,
19 Nov 2026: at most 2 holes); with 4 holes the message stays read in part under the floor.

## Stanza 2 values
- h28 (*łowczych*), ź29 (*zaraźliwem*), ó30 (*pióry*): from stanza 2 of the hymn; h and ó were first set from *wybuchowe* and *Józka* and then found at their rank. 19, 25, 29 never occur.

## Remaining gaps
- Comparison with the printed decoding of points 7 and 9 (Paczyńska 2013, p. 439; Paszek 2025 §5.4) - blocker: needs-physical-access; the book and the full thesis are not available to us online.
- Four probable words ({większych}, {przesyłek}, {tamtejszego}, {mieć}) - blocker: illegible; doubtful or overwritten digits on a low-resolution reproduction, and ć has no number in the key.
- Clear text of point 6, one word of point 9, signature - blocker: illegible (low-resolution reproduction).
- Human check of the other doubtful digits (G3 pos. 8, G7 pos. 1 and the faint 2/7, 1/7, 9/3 doubts) - blocker: not-attempted (the blind sheet covered the five that decide words).

## Escalation
- [x] siblings: none available to us (other grypsy of the same system: Paczyńska 2013, not seen).
- [x] clear-pages: the clear Polish around the cipher words agrees with the decode (« uskutecznić ewentualnie … przesyłek », « Czy macie już u siebie przygotowane … materjały wybuchowe »).
- [x] known-keys: Kłodziński's 1943 instruction (agrees for 1-7 only); hymn texts tried in PREREG 1 and 2; the church version (1838) gives the key.
- [x] print: web search and public PDFs (Paszek 2025 to p. 141, WUJ free extract, museum pages), 26-27 Nov 2026, found no reading; after the reading, Daniel Bourdeau found the print (Paczyńska 2013 p. 439, quoted by Sadzikowska 2022 p. 120 n. 240); p. 439 not seen (see Remaining gaps).
- [n/a] key-rebuild: key rebuilt from the song; it reads both halves.
- [x] retry: every doubtful digit of transcription.txt § DOUTES retried with the key (alternatives decode to no Polish word except those adopted as probable). A person checked five doubtful numbers on a blind sheet; the others are still open (Remaining gaps).

## Credits
Brice Dudout set the protocol; Claude Opus agents (Anthropic) transcribed blind, arbitrated, wrote and ran both pre-registrations and read. AI decipherment; Brice Dudout checked five doubtful numbers on a blind shape sheet, not the other digits. An independent hostile reading (agent) checked the transcription, key and reading against the images and sources; its corrections are applied. The checks « image » above are by the blind arbiter, an AI agent working from the screenshots; no person has checked the digits on the image yet.
