# Afonso VI to the Count of Vila Flor, four cipher letters, 13-26 May 1663 (catalogue 391)

Status: read in part (16 Nov 2026, recounted over cipher words: 13 May 132 of 147, 89.8%, under the bar; 15 May 106 of 111, 26 May 136 of 139; 15 May long letter not split). Was read (Brice Dudout, 27 Oct 2026; four letters, counted in signs, not words: 26 May, 633 of 633 signs read in their sense, 632 certain, 1 restored ([p]ara); 15 May (risk of a battle), 509 of 509 signs read, 5 slips settled by the second copy; 15 May (reinforcements), two copies of 2,213 and 2,357 signs agreeing with the established text at 98.7% and 99.0%; 13 May, 636 signs, about 97% read, about 15 signs corrected from the sense, 2 passages unresolved; probable signs not counted separately; Daniel Bourdeau's 95% rule).

Contributed by Brice Dudout (Europe chiffrée), 27 Oct 2026. Write-up:
https://bdudout.github.io/europe-chiffree/en/documents.html#vilaflor-1663

## Document

ANTT, Luís de Miranda Pereira, liv. 2 (PT/TT/LMP/0002), DigitArq https://digitarq.arquivos.pt/documentDetails/8e069ec117cb4177a02c2f8f79fee294 (images not reproduced: no
reuse licence). Catalogue 391 gives 1661; all the cipher letters in the volume are of May 1663. Leaves m0057 and
m0059 are swapped in the binding.

In spring 1663 Don John Joseph of Austria invaded the Alentejo and besieged Évora. From Lisbon, the court governed by the Count of Castelo Melhor in the name of the young Afonso VI wrote almost daily to the general of the Portuguese army, the Count of Vila Flor. Four of these letters, in cipher, are read here in order: on 13 May, news of the cavalry sent as reinforcements; on 15 May, the day after Évora was invested, a long letter on the reinforcements, the money and the King’s plan to come to Setúbal, then a note carrying the order to relieve it “a todo o risco”, even at the cost of a battle; on 26 May, four days after the city surrendered, the same resolution, now “final”. On 8 June Vila Flor and Schomberg defeated Don John at Ameixial.

## System and keys

Monoalphabetic substitution with homophones on Portuguese: digits and letter-like signs, word divisions partly kept.
Three states of the key are used across the four letters (`key_K1.tsv`, `key_K2.tsv`, `key_K3.tsv`).

## Reading

- 13 May 1663: the cavalry sent as reinforcements: First published decipherment to our knowledge. 636 signs; reading ≈ 97%: about fifteen signs are corrected from the sense (letters omitted by the encipherer, 30 written for 3, Ӿ for x), and two passages remain uncertain (the sign ʒ, used once, and “Lo[bo] ‹aal› de Agalega”, where the encipherer struck out two signs). This is the letter used for the blind test of the key: transcribed without the key, it was decoded with the K1 key frozen on the letter of 26 May. Its additional homophones were then established on the letter itself (see “Additional homophones”).
- 15 May 1663, the other letter: reinforcements, money, and the King at Setúbal: First published decipherment to our knowledge. The letter survives in two signed copies (the original and the “via”), with the same passages in clear but enciphered independently, with other homophones and other line breaks (2,213 and 2,357 signs). In the bound volume their third leaves are swapped: copy 1 reads images 53 → 54 → 59, copy 2 images 55 → 56 → 57, as the continuity of the cipher proves (“estam r|[ec]olhidos” across the leaves). Each copy, deciphered with the frozen K3 key, agrees with the established text at 98.7% and 99.0%; the two copies, deciphered separately, agree at 0.927, a
- 15 May 1663: “at the risk of a battle”: First published decipherment to our knowledge. 509 signs, all read. The encipherer made five slips (one doubtful sign, two omitted letters, two signs written for others); the second copy (image 71), enciphered with other homophones and other line breaks, gives the same text and resolves them all. This letter was transcribed with the key already known: it is not a blind test, but the frozen K1 key decodes it at a likelihood score (−2.25 per character) far above the controls (at best −4.72), and the second copy is an independent check.
- 26 May 1663: First published decipherment to our knowledge. The letter carries no decipherment, and no key survives in the volume. Of 633 signs, all are read except one, lost in the tear of the right margin and restored from the sense ([p]ara); the encipherer once wrote “parecor” for parecer. The second ciphered copy (image 39), written with other homophones, confirms the two doubtful signs of the first. The key, built on this letter alone, was frozen and then validated on another ciphered letter in the same volume held out for the purpose (13 May 1663). The Count of Ericeira mentions the King’s “repeated 

Validation: key checked on a held-out letter, on duplicate copies (0.93 agreement for the 15 May letter, against
0.13 for unrelated text) and on a sentence left in clear in one copy and enciphered in the other. Ericeira's
*Portugal Restaurado* does not print these letters.

## Method

Method: (1) the letter of 26 May was transcribed sign by sign (633 signs, 30 distinct signs). (2) The K1 key was built on this letter alone, from expected vocabulary (que, exercito, cartas, risco…), then frozen (SHA-256 fingerprint recorded) before any validation. (3) Validation fixed in advance: another ciphered letter in the volume, of 13 May 1663 (636 signs, transcribed without the key), decoded with K1, is scored by a Portuguese language model (log-likelihood per character). It scores −2.61; the controls reach at best −4.52 (same letter, signs shuffled) and −5.52 (keys with permuted values, 200 trials), while a Portuguese text enciphered with K1 with 3% simulated errors scores −2.58. K1 covers 92.8% of the signs of that letter, which uses a few more homophones. (4) The second copy of the 26 May letter (image 39), enciphered with other homophones, was used to check the doubtful signs.

Prior work, checked on 27 October 2026: Daniel Bourdeau’s catalogue lists no. 391 as open. The Count of Ericeira, Historia de Portugal Restaurado, part II (1698), book VIII, narrates the loss of Évora and the march to Ameixial and mentions only “the King’s repeated orders and the urgent pressure of the Count of Castelo Melhor”: he does not quote the letter (full text consulted, as well as the 1751 edition). The blog Guerra da Restauração, which publishes documents of the 1663 campaign, gives Vila Flor’s letter of 26 May, not the King’s. António Álvares da Cunha’s account, Campanha de Portugal pella provincia do Alentejo na primavera do anno de 1663 (Lisbon, 1663), is not digitised to our knowledge and has not been checked in full text. A web search (Portuguese, English) found nothing. We know of no edition of this letter.

## Read share over cipher words only (16 Nov 2026)

README Conventions now count the read share over the words written in cipher, holes by words, sure words only, and a
letter corrected in a key rebuilt here is a hole. In each short letter the greeting (before the cipher) and the date
line with the signature and address are clear; the decryption files start at the first word after the greeting and end
with the last body word, so the cipher words are the body of each reading. By hand, the reading's body words aligned to
`texts/*_decryption.txt` (difflib) to find the words whose letters differ from the decrypted ones, then each checked:

- **13 May**: 147 cipher words (the five written numerals 10, 9, 203, 56, 55 are clear and left out), **15 holes**:
  hav{e}r, pod[e]ria, t{o}mar-se, {es}te (the sign used once), Manoe[l], d{e}, q[u]e, Be{i}ra, pod{e}reis, fazer (h for
  z), {c}hegar, cav[a]los, Lo[bo], the struck-out ‹aal›, {c}oreio. The three `q[ue]` where the decryption has `q`
  alone are the writer's abbreviation expanded, not holes. **132 of 147 = 0.898** (was about 0.97, counted in signs),
  so this letter is **read -> read in part**. One copy only, so nothing settles the slips.
- **15 May ("a todo o risco")**: 111 cipher words, 5 holes (espera{i}s, a[o], conse[q]uencias, d{o}, q{ue}), **106 of
  111 = 0.955**, stays read. The second copy (image 71) settles all five on the contributor's record, but it is not
  transcribed here, so they are counted as holes; counted as read the share is 1.0.
- **26 May**: 139 cipher words, 3 holes (parec{e}r, q[u]e, the restored [p]ara), **136 of 139 = 0.978**, stays read.
- **15 May, the long letter**: **not split.** Its reading mixes clear and cipher passages that no mark separates in
  the files (the summary names the greeting, the doctrine and the daily-courier request as clear), and only a
  174-symbol passage of its cipher is transcribed here, so the cipher words can be neither separated nor checked
  against a decryption. No share is recorded for it; the tool's 0.991 is over the whole reading, clear included.

Over the three counted letters 374 of 397 cipher words (94.2%). The target class goes **read -> read in part**: one
letter is under the bar and the long letter cannot be measured. The old 0.999 counted transcribed signs. The key stays
recovered. `v10_relabel.py` (dry run) gives 0.943, 0.973 and 0.966 for 13 May, 15 May and 26 May and 0.991 for the long
letter: it cannot reproduce the counts, because the greeting and closing are not marked in the files and it cannot tell
an abbreviation expansion from a supplied letter or a corrected one.

## Remaining gaps

- 13 May: the 15 words whose letters are supplied, corrected or probable (listed above), the sign used once and the struck-out name - blocker: too-short; one copy only of this letter, so no second enciphered copy settles the slips, and the sign used once and the struck-out name cannot be checked on the 1060 px DigitArq images
- 15 May five slips (settled by the second copy on the contributor's record only, not transcribed here), 26 May [p]ara and parec{e}r, and the long 15 May letter's cipher beyond its 174 transcribed symbols - blocker: illegible; DigitArq serves 1060 px images only, so the symbols cannot be re-read at higher resolution

## Escalation

- [n/a] siblings: second copies exist for 26 May, 15 May and the long letter and were used; no second copy of the 13 May letter is recorded in the notes
- [n/a] clear-pages: the greeting, the date and the signature are the only clear text of each short letter; no clear copy of the body is recorded
- [x] known-keys: K1, built on the 26 May letter, was frozen and applied to the others; K2 and K3 add homophones established on the letters themselves
- [x] print: Ericeira's Portugal Restaurado (full text and the 1751 edition) and the Guerra da Restauração blog checked on 27 Oct 2026, nothing; Cunha's 1663 Campanha de Portugal not digitised, not checked; not repeated in this recount
- [x] key-rebuild: K1 from the 26 May letter, additional homophones K2 and K3 set on the 13 May and long 15 May letters
- [n/a] retry: not rerun in this recount; the 13 May slips have no second copy to retry them against
