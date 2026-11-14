# Intercepted royalist letters, May 1646 (BL Add MS 72438 ff. 9-10): key identified, partial reading

**Status:** open. The cipher is identified and about 45 of its values are fixed, but the surviving evidence is not enough for a full decipherment. Work of 2026-09-16.

**Item:** two intercepted letters in cipher among the papers of Georg Rudolph Weckherlin, secretary for foreign tongues to Parliament: f. 10, 13 May 1646, "May it please your Majesty", signed in cipher, to Charles I; and f. 9, 21 May 1646, "My Lord". Listed as unsolved on Satoshi Tomokiyo's Cryptiana page. DECODE records 8624 and 8623, status "Non-decrypted". Images were obtained through the DECODE project with permission and are not redistributed; `f10_ct.txt` and `f9_ct.txt` are our own transcriptions from them.

## What the volume contains

Add MS 72438 is Weckherlin's collection of cipher keys and intercepted correspondence, 81 DECODE records. Two pages explain most of it:

- **f. 25** is a contemporary index headed "Cyphers taken in the Lord Digby's cabinet" (Sherburn, October 1645), numbering the captured keys 80 to 139. Each key page in the volume carries its index number in the margin: f. 27 is no. 84 (Bennet), f. 52 no. 113 (Digby and Vavasour), f. 70 no. 125 ("Mr Browne's cypher", the big 700-entry key of the Paris resident Richard Browne), f. 78 no. 130 (Col. Hurleston, a syllabary), f. 82 no. 132 (Sir Kenelm Digby), and so on.
- **f. 77** carries no. 129, which the index describes as "without name, from the Queen's Court". Only one page survives: names 559 to 580 (Marquis of Newcastle, Lord Digby, Daniel O'Neale, Davenant 562, the Dutch ambassadors Boreel, Renswoude and Joachimi, the Brederodes, Mme Dona, Mlle Coignet, Mme Vantelet, "Mylord" 572, "Madame" 573, Prince Maurice, Exeter, Scarborough, Jersey, Guernsey). Every other record in the volume was checked; the rest of key 129 is not there.

## The cipher of f. 10 is key 129

Three independent fits:

1. f. 10 uses 562 twice and 572 once, in positions where "Davenant" and "Mylord" read naturally ("to 329 Davenant to", "of the Mylord 496 and express").
2. The King's letters to Sir Edward Nicholas of 24 June and 16 August 1646, printed with Nicholas's interlinear decipherments in Evelyn, *Diary and Correspondence* (1857) vol. 4 pp. 178-179, use the same values: and 112, be 121, I 209, if 213, left 234, me 250, my 251, nor 269, not 270, of 280, or 281, send 341, to 360, with 409, where 412, which 413, write 422, you 429, Earl 503, Marquis 550, Hertford 520. All of these fit f. 10 ("having not 596d a word", "your Majesty" five times once 430 and 543 are read that way, "to send ... to your Majesty ... for which ... having").
3. The 1857 OCR is unreliable for the numbers (it prints 122 for 422, drops values); we read the archive.org page scans directly.

So f. 10 is a letter to the King in the cipher the Queen's court and the King shared in 1646, written a fortnight after the King left Oxford. Parliament's Commons Journal for 25 May 1646 records Fairfax's packet of "several intercepted Letters in Characters" being sent to Sir Walter Erle to decipher; on 30 May Erle reported one of them (Nicholas to Ashburnham, 15 May). The Journals print no decipherment of the 13 May letter.

## Structure

- 0 to 99: letter homophones, roughly three or four per letter. Fixed from Evelyn: s 56, i 40 and 63, r 17 and 18, e 67 and 69, w 78, o 31, d 81, c 90, b 27, n 7.
- 100 to about 430: a word list grouped by initial letter but not strictly alphabetical within a letter (with 409, where 412, which 413).
- 431 to about 580: names and places. 449 is glossed "I.H." by Nicholas.
- Higher numbers (f. 10 uses up to 697) are unexplained; the signature is 555 697 496.
- 370 is probably a syllable code: "d i r e c 370" occurs twice, i.e. "direction". The King's cipher also uses two-letter symbols ("or", "at", "if", "he"), none visible in f. 10.

`key129.txt` holds every value we consider fixed; `apply_key.py key129.txt f10_ct.txt` renders the partial reading.

## What failed

`solve.py` anneals the 218 spelled-letter tokens (61 symbols, 12 fixed) against a character 5-gram model built from Bruce's *Charles I in 1646*, Evelyn vol. 4 and the Nicholas Papers (since 18 Sept 2026 fetched by `cipherkit.corpora` en; `uv run python solve.py key129.txt f10_ct.txt 4 1`). Output is vowel soup. **The matched control says this negative is uninformative:** `solve.py --control`, a synthetic text with the same letter-run lengths and 61 symbols enciphered from the corpus, reads at 0.07 to 0.12 token-weighted key recovery on three seeds. The solver cannot read anything of this shape, so f.10's failure says nothing about f.10; only a key or a contemporary decipher will read it. The original diagnosis stands for a different reason: the spelled runs are mostly suffixes ("596 d", "585 s") and two- or three-letter fragments between word codes, and the word codes (413 tokens, 173 distinct) are a word-substitution problem with no constraint beyond the initial letter.

Also negative: every other key in the volume against f. 10 (Browne no. 125, the Bennet, Digby, Hurleston, Nicholas-circle and French keys); Bruce 1856, which prints the King's 1646 letters to the Queen from deciphered copies with no cipher numbers.

## What would finish it

The contemporary decipherment, or the rest of key 129. Neither is online. Places to look: Add MS 72438 f. 11 (not a DECODE record, so probably plaintext, possibly Weckherlin's decipher of f. 10); Bodleian Tanner MSS 59-60 (intercepted letters of 1646); TNA SP 16/514. The British Library's digitised-manuscripts viewer has been offline since the 2023 cyber attack.

## f. 9

Not attacked beyond noting that it uses a different, smaller key (max value 343) in which 226 reads "London" by the key recovered from the deciphered f. 4 intercept of 1645.

## Sources

- DECODE database (de-crypt.org), records 8623, 8624, 8627, 8694, 8701 and the rest of BL Add MS 72438.
- Evelyn, *Diary and Correspondence*, ed. Bray (1857), vol. 4, pp. 178-179; archive.org item diarycorresponde41evel, leaves 186-187.
- Bruce (ed.), *Charles I in 1646: Letters of King Charles the First to Queen Henrietta Maria*, Camden Society 1856.
- Journal of the House of Commons vol. 4, 25 and 30 May 1646 (British History Online).
- Satoshi Tomokiyo, [Unsolved Historical Ciphers](https://cryptiana.web.fc2.com/code/unsolved.htm).
