# Longlée to Henri IV, duplicate of a dispatch from Madrid [December 1589 - February 1590] (BNE Mss/994, ff. 67r-67v)

Status: read in part (Brice Dudout, 2 Nov 2026; 480 cipher words: 313 certain, 99 probable, 7 restored, 61 unresolved (estimated); 85.8% read, below the 95% rule).

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents. Published there as an explained partial reading:
https://bdudout.github.io/europe-chiffree/en/documents.html#longlee-1590
Not in the catalogue. DECODE record R2253 (https://de-crypt.org/decrypt-web/RecordsView/2253); the DECODE images are not
reproduced here or on the site (DECODE terms).

## Document

Madrid, Biblioteca Nacional de España, Mss/994, item 6, ff. 67r–67v (“Dupp. d’une despesche”); study images DECODE R2253 (views 4 and 5), not reproduced. Ff. 64–65v and 68–69 of the same volume are the letters of 1 April and 3 March 1590, edited by A. Mousset, Dépêches diplomatiques de M. de Longlée, résident de France en Espagne (1582-1590), Paris, 1912, pp. 394–396 and 390–392, from the originals (AE, Mémoires et documents, Espagne 237).
Date: undated; between December 1589 and February 1590: Longlée has had no dispatch from the King “depuis le troisiesme de nouembre”, and an envoy arrived “le vingtuniesme de ce mois”. Probably the duplicate of the dispatch of 25 February 1590, cited in the letter of 12 March 1590 (Mousset 1912), whose original is missing from the Foreign Office archives.
Sender: Pierre de Ségusson, sieur de Longlée, French resident with Philip II. Recipient: Henry IV (“Vre Mate”); on the back of the bundle: “a Monsr. de Vendosme Principe de Bearne, que despues fue Rey de Francia”.
The volume's heading (f. 64) says the letters were read without a counter-key by Luis Valle de la Cerda; no
contemporary decipherment is in the DECODE images. The other two letters of the piece are already in print (Mousset 1912):
ff. 64-65v = 1 April 1590 (pp. 394-396), ff. 68-69 = 3 March 1590 (pp. 390-392). This one is not.

Pierre de Ségusson, sieur de Longlée, the French resident at Madrid, wrote in cipher to Henry IV early in 1590. The packet was intercepted: its copy, “Dupp. d’une despesche”, is now in the Biblioteca Nacional de España, with two other letters of Longlée that the Spaniards had deciphered by Luis Valle de la Cerda. Those two letters (3 March and 1 April 1590) were edited by Albert Mousset in 1912 from the originals at the French Foreign Office; this one was not, and no contemporary decipherment accompanies the copy. We publish the reading as far as we could take it, gaps included: 85.8% of the words, below the 95% threshold we hold ourselves to. It shows an envoy of the Duke of Mercœur at Madrid asking that Philip II declare openly against Henry IV and seize the goods of royalist Frenchmen.

## System and key

Longlée’s nomenclator: an alphabet of homophonic signs (letters, digits, symbols) and a few signs for short words; the same hand as the two edited letters of the volume. Starting point: the table printed by Mousset (pp. lviii–lix), corrected on the hand of these copies.
Key K4 (`key_K4.tsv`): Mousset's printed table (K0) calibrated on the hand of these copies, then corrected on the edited
letters only (3 March whole, 1 April f. 64r-64v). Validated by a single measurement on the reserved part of the 1 April
letter against Mousset: characters 0.874 against at best 0.361 for 200 shuffled-key controls; words
0.647 (`validation.txt`). The key was never changed for the reading of ff. 67r-67v.

## Reading

Partial reading, explained; unpublished to our knowledge. Rule applied: Daniel Bourdeau’s, 95% of words read for sense to publish a decipherment. Here, of 480 cipher words: 313 certain (65.2%), 99 probable {x} (20.6%), 7 restored [x] (1.5%), 61 unresolved ‹…› (12.7%, the number of words estimated for each segment); certain + probable: 412 / 480 = 85.8% (87.3% counting the restored ones). Below the 95% threshold: this is not a complete decipherment. Words are simply missing: each unresolved one stays visible in place, with the letters the key gives. F. 67r reads at 88.6%, f. 67v at 80.6%.
Files: `transcription.txt` (sign labels), `decryption.txt` (K4, mechanical), `reading.md` (French, tagged, with the
count), `translation.md` (English summary), `key_K4.tsv`, `validation.txt`.

## Unresolved words, contamination and limits

- Unresolved words. Mostly segments where the transcription of the signs is probably wrong: rare or hesitant shapes (Ω, 9 and ϱ hard to tell apart, small attached loops). Examples: f. 67r ‹parestassntlaisaslr›, ‹iossassea?aermar›, ‹austuoernee› (perhaps “au gouvernement”); f. 67v ‹salegathonidemorera›, ‹certpressedupartitent›, ‹ptinueot› (perhaps “continuent”). None is completed by conjecture; only seven restorations that conflict with no certain letter: [de] ×2, [affaires] ×2, [depesche], [m’estendrai], [catholique].
- Declared contamination. Decodings of this letter with earlier keys (K1) and with K4 were seen before the last shape corrections (re-reading against the image on 2 November, Brice’s plate): any word that depends on a shape corrected after a decoding counts at best as probable. The edited texts of 3 March and 1 April were read at the outset for identification; for the measurement, it is the cipher of the reserved portion that had never been looked at, not Mousset’s text (see “Method”).
- No contemporary plain text for this letter. The key is validated on another letter in the same hand and cipher (1 April 1590), not on this one; Mousset edits the Foreign Office original, while the BNE holds the duplicate.
- Prior work. Mousset (1912) edits nothing between 15 October 1588 and 3 March 1590 and does not cite the BNE; Satoshi Tomokiyo (Cryptiana) notes the three letters in BNE Ms. 994, ff. 64–70, without a reading; no entry for R2253 in Daniel Bourdeau’s catalogue; a quick search of Ruble and the Calendar of State Papers, Foreign (1589–1596, not read page by page) found nothing. Unpublished to our knowledge.
- To reach 95% about 44 more words would have to be read; the validated key is not at fault: it is the legibility of the signs in this copy.

## Method

Method: (1) protocol written and hashed (SHA-256) before any computation, at every stage; (2) starting key: Mousset’s table; key adjusted to the hand of these copies by calibration on the edited letters (3 March and the beginning of 1 April); atlas of sign shapes frozen; (3) keys K1 to K3 were not validated; key K4 is validated by a single measurement on a portion never looked at before the measurement (letter of 1 April 1590, f. 65r and f. 65v ll. 1–13: 45 lines, 1,561 letters), transcribed by shape and frozen, compared with the text edited by Mousset (pp. 394–396): character agreement 0.874 against at best 0.361 for 200 shuffled-key controls (mean 0.305); word agreement 0.647 (controls ≤ 0.154); criterion fixed in advance: ≥ 0.85 and ≥ best control + 0.30; (4) the letter read here was transcribed by shape, the transcription frozen before each decoding, then decoded mechanically with K4, never retouched; (5) sign-shape re-reading by Brice Dudout on a plate of 12 doubtful signs (pick the shape seen, no value or gloss shown), with rules of application pre-registered and hashed before the answers; three signs turned out to be double, segmentation corrected and declared; (6) reading and count under Daniel’s rule, each unresolved segment counted for the number of words it covers (estimated), not as one. All SHA-256 fingerprints are in the working folder.
