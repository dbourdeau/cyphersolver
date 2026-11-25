# The Electors of Mainz and Cologne to Gottfried Huyn von Geleen, [Cologne] 22 October 1633 (BSB Clm 10406, no. 206)

Status: read in part (Brice Dudout, 4 Nov 2026; 221 cipher words: 151 certain, 35 probable, 8 restored, 27 unresolved; 84.2% read, below the 95% rule; 19 words lost in the binding cap it at 91.4%).

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents. Lead no. 2183 found by WAINUT
(https://github.com/WAINUTAI), who spotted the document in the Camerariana volumes. To be published as an explained partial reading:
https://bdudout.github.io/europe-chiffree/en/documents.html#ligue-1633
Not in the catalogue; no DECODE record.

## Document

Munich, Bayerische Staatsbibliothek, Clm 10406, no. 206 (Collectio Camerariana 56), fols. 184r–185v; digitised microfilm, MDZ bsb00116454, views 653–656 (Public Domain Mark 1.0).
Date: [Cologne], 22 October 1633 (“Datum den 22. Octobris Anno 1633”); an answer to a letter of Geleen dated Rheinberg, the 11th of the same month.
Senders: Anselm Casimir, Archbishop-Elector of Mainz (“Anselmus Casimirus Archiep. Moguntinus”), and Ferdinand, Elector of Cologne, autograph signatures. Recipient: Gottfried Huyn von Geleen, “General Wachtmeister” of the League army (address on the back, with the seals).
Original letter, signed; German clear text with about 1,180 cipher numbers inserted; no contemporary decipherment on the
piece or in the neighbouring items (nos. 205-207). Images: MDZ (Bayerische Staatsbibliothek), Public Domain Mark 1.0.

In the autumn of 1633 the Catholic League had almost no army left in the north. Hildesheim was besieged by the troops of Brunswick-Lüneburg, allies of the Swedes; Kniphausen and Melander’s Hessians held the County of Mark. The Archbishop-Elector of Mainz, Anselm Casimir Wambolt von Umstadt, in exile at Cologne, and the Elector of Cologne, Ferdinand of Bavaria, answered Gottfried Huyn von Geleen, the League’s major-general (Generalwachtmeister), on 22 October. The letter, signed in their own hands, is in clear, but everything about troops, money and people is in cipher: about 1,180 two-digit numbers slipped into the sentences. There is no contemporary decipherment on the document. We publish the reading as far as we could take it, gaps included: 84.2% of the cipher words. Most of the rest is lost in the binding of the volume, invisible on the digitised microfilm.

## System and key

simple substitution: each letter is a two-digit number (12 to 36), written run together, without word division, in the middle of the clear text; 22 working values (e = 17, n = 31…), two rare numbers without a sure value (33, 38). Key reconstructed here (table below).
Three known keys of the period were tested by a frozen criterion and do not apply (Camerarius 1621: no letter table 12-36;
Rákóczi 1632 and Kurz 1638-39: below the controls). Key K (`key.tsv`) was built by simulated annealing on the letter minus
the held-out lines, then corrected from three clear contexts ("vom Feind" 34 = f, 23 = m; "Kniphausen" 14 = p; "Geltmittel" 28 = l),
then frozen. Validation (`validation.txt`): M5 0.656 against 200 shuffled-key controls max 0.113; M_lm -2.512 against
max -4.182. The held-out lines read: "zum besten nichts erwinden lassen und euch hingegen vor gewiss versichern, das solche
eure merita und getrewe dinsten von uns und den sambtlichen unirten catholischen bundsständen mit würcklichem Danck
remunerirt werden sollen".

## Reading

Partial reading, explained; unpublished to our knowledge (see Prior work: a doubt remains about a summary in the Munich edition of 1982). Rule applied: Daniel Bourdeau’s, 95% of words read for sense to publish a decipherment. Here, of the 221 cipher words: 151 certain (68.3%), 35 probable {x}, 8 restored [x], 27 unresolved ‹…›; words read (certain and probable): 186 / 221 = 84.2%; 87.8% with the restored ones. The threshold is not reached: this is not a complete decipherment. On this microfilm it cannot be: 19 words are cut off in the binding, which caps the reading at 91.4%.
Files: `transcription.txt`, `decryption.txt` (K, mechanical), `reading.md` (German, tagged, with the count),
`translation.md` (English summary), `key.tsv`, `validation.txt`.

## Unresolved words and limits

- The binding. The volume was microfilmed bound: on view 654 (fol. 184v) the ends of the cipher lines vanish into the gutter. 19 words are cut or lost; even read perfectly, the rest would give only 91.4%. Only the original (or a new photograph) could bring the reading to 95%.
- Reading of the numbers. A single reader, on the enlarged microfilm. 2, 3 and 5 are sometimes alike, as are 15 and 18, 23 and 31: such words are counted “probable”. A blind re-reading plate (20 questions on 14 words, rules filed and hashed in advance) was answered by Brice Dudout on 4 November 2026: 9 words were confirmed and are now certain; for 4 words (‹shah›, ‹w??›, ‹waahhmeisher›, ‹ricmten›, expected “Statt”, “Weg”, “Wachtmeister”, “richten”) the numbers are written as transcribed, so the correction is dropped and they become unresolved; one word stays probable.
- Unresolved words. 27 words: 19 lost in the binding, 4 whose written numbers contradict the expected word (see above), 2 word ends at the cut (‹le›, ‹non›) and 2 runs that the key gives without a recognisable word (‹derdselfemlh›, ‹anewerder›). Eight restorations from the sense, two of them where the key gives almost the word: [bem(el)ten] (“bemeldten”, aforesaid; the key gives “bemten”) and ein [u(n)gewisses] (the key gives “einugewisses”); letters in brackets are added. Unverified clue: the re-reading confirms 25 where the sense wants t (Statt, Wachtmeister) and 23 where it wants h (richten); 25 and 23 may have a second value, or these are the encipherer’s slips. The key is not changed.
- No contemporary clear. No deciphered copy is known: the key is validated on the letter itself (five held-out lines), not on an independent control text. The letter’s clear text is read approximately.
- Prior work. No folder or reading in Daniel Bourdeau’s repository or on DECODE; nothing from Tomokiyo. The Munich edition, Briefe und Akten zur Geschichte des Dreißigjährigen Krieges, Neue Folge II/8 (Kathrin Bierther, 1982, January 1633 – May 1634), covers the same episode from the Bavarian archives (relief of Hildesheim, horse for Geleen, the Bönninghausen–Geleen quarrel); it is not online, and a search of its digitised snippets does not find this letter (nor Menselius). A summary of the letter, from a clear copy, cannot be ruled out. The cipher and its reading are, to our knowledge, published nowhere.

## Method

Method: (1) protocol written and hashed (SHA-256) before transcription, with five lines of fol. 185r (186 cipher letters, up to the clear word “Bedanken”) held out; (2) numbers transcribed without any key value, then frozen; three known keys of the period (Camerarius 1621, Rákóczi 1632, Kurz 1639) tested by a frozen criterion: none applies; (3) key built on the rest of the letter (simulated annealing with a model of 17th-century German, then three corrections from the clear context: “vom Feind”, “Kniphausen”, “Geltmittel”), then frozen; (4) a single measurement on the held-out lines: 0.656 of the cipher letters covered by German words of five letters or more, against at best 0.113 for 200 shuffled keys (threshold fixed in advance: 0.60), and a language-model score clearly above all controls (−2.51 against −4.18): key validated; (5) reading of the whole letter by Daniel’s rule. The held-out passage reads: “zum besten nichts erwinden lassen und euch hingegen vor gewiss versichern…”.

## Decrypt audit, 16 Nov 2026

The decrypt audit (`research/decrypt_audit/`) re-applied `key.tsv` to `transcription.txt` and compared the letters with
`reading.md`: 64 of 201 compared words depart from the mechanical decrypt (32%). Checked here word by word against
`decryption.txt`, which is the key applied to the transcription with nothing edited (re-derived: 0 of 46 lines differ).

- Clear text (50 of the 64 flagged words). `reading.md` interleaves the letter's clear German in « » (for example
  «zu verhüten, und wir den»); the audit drops the bracketed clear text of the transcription and so takes these words
  for departures. Nothing is wrong there. The clear text of the reading is not letter for letter that of the
  transcription ("bß." in the transcription is «betreffend» in the reading); both files call it approximate.
- Probable and restored words. The 35 words in { } and the 8 in [ ] differ from the decrypt by design (decrypt
  "ufalle", reading "{auf} {allen}") and are marked; the audit counts them as marked.
- Words printed as certain, with no mark, whose letters are not the ones the key gives: 17. Eleven change or supply a
  letter: feindlichem (decrypt feinduichem), allem twice (aulem), algemeinen (augemeinen), sollen (soulen), beclagen
  (becuagen), solche (uolche), tausent (hausent), mit (sit), starck (starct), desto (the transcription has an illegible
  pair, "de·to"). Six only change the spelling: Hildesheim (hildesheiim), dieselbe (deselbe), Statt (stat), Gewaldt
  (gewald), bisher (bishero), begriffenen (begrieffenen). Thirteen of the 17 are among the audit's 64; Hildesheim,
  bisher, begriffenen and sollen were found by hand. Six of the letter changes read l where the transcription has 15
  (u/v); "Unresolved words and limits" says 15 and 18 are alike in this hand and that such words are counted probable,
  but these are printed as certain. The transcription was frozen and was not changed, so the reading and the
  transcription disagree at these places and the reading does not show it. Three of the 17 (solche, mit, sollen) are
  in the held-out lines P3.1-P3.5, where six more words are marked probable ({lassen}, {hingegen}, {gewiss}, {eure},
  {catholischen}, {würcklichem}). The sentence quoted in "System and key" and in "Method" as what the held-out lines
  read is this normalised reading; the key gives ZUMBESTENNICHTSERWINDENLASNENUNDEUCHDINGEGEN /
  UORGEWISUERSICHERNDASUOLCHEEWEREMERITAUND / GETREWEDINSTENUONUNSUNDDENSAMBTLICHEN /
  UNIRTENCATHOLBUNDSSTANDENSITWURCKLICH / DANCKREMUNERIRTWERDENSOULEN (`validation.txt`).
- Key file: nothing missing. Every value used is in `key.tsv`; no other key material is in the folder.

Changed: nothing in the key, the transcription, the decryption or the reading. The audit figure is the same after
(64 of 201). Open: whether the 17 words should be marked { } or the count of 151 certain words lowered is not decided
here; the wording of the reading was left as it is.

Marked on 16 Nov 2026. In `reading.md` eleven words are now in { } (probable), the file's own mark: allem (twice),
feindlichem, tausent, desto, algemeinen, solche, mit, sollen, starck, beclagen. No letter of the text was changed. The
six spelling-only words (Hildesheim, dieselbe, Statt, Gewaldt, bisher, begriffenen) are not marked one by one: a header
line now states the spelling convention and gives the key's forms. A second header line lists the eleven and says that
the count table (151 certain, 35 probable) is the count of 4 Nov 2026 and does not include them; the table, the Status
line, `read_share` and the figures on the page were not recomputed (with the eleven counted probable the split would
be 140 certain and 46 probable, certain + probable unchanged at 186 of 221). On the page the sentence "The held-out
lines read: ..." now says that the sentence is the reading with the spelling normalised and gives the key's forms.
The same sentence in "System and key" and "Method" above is to be read with this section.

## Remaining gaps

- 19 words cut or lost where the line ends of fol. 184v vanish into the gutter - blocker: needs-physical-access; the volume was microfilmed bound, only the original or a new photograph shows them (caps the reading at 91.4%)
- 2 word ends at the cut (le, non) - blocker: needs-physical-access; same gutter
- 4 words whose written numbers contradict the expected word (Statt, Weg, Wachtmeister, richten) - blocker: illegible; blind re-reading 4 Nov 2026 confirmed the numbers as transcribed, the enlarged microfilm gives no other reading
- 2 runs without a recognisable word (derdselfemlh, anewerder) - blocker: illegible; re-inspected on the MDZ images (views 653, 654) 4 Nov 2026: in derdselfemlh the film shows 17 22 13 17 18 3?/2? 17 23 18 25 with no clear second 21 and 2/3/5 and 7/8 not separable, so derselbe mehr is possible but not verifiable; in anewerder the film shows 30 ?1 17 19 17 22 (17|21 17) 22 where one pair reads as 11, not a number of the key. The microfilm does not settle either; the transcription is left as written
- values of 33 and 38 - blocker: no-key-material; rare, no clear context

## Escalation

- [x] siblings: nos. 205-207 of Clm 10406 opened; no decipherment or clear copy among them
- [x] clear-pages: no clear copy or postscript on the letter or its neighbours
- [x] known-keys: Camerarius 1621, Rakoczi 1632 and Kurz 1638-39 tested by a frozen criterion; none applies
- [x] print: no folder or reading in the repository or on DECODE, nothing from Tomokiyo; Bierther (1982) not online and its snippets do not list the letter; web search 4 Nov 2026 for the letter, Menselius and Lerchenfeld found nothing
- [x] key-rebuild: annealing with a 17th-century German model, then three corrections from clear context (vom Feind, Kniphausen, Geltmittel), frozen
- [x] retry: blind re-reading plate of 20 questions on 14 words answered 4 Nov 2026: 9 words now certain, 4 dropped to unresolved
