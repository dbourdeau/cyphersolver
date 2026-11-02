# Sanguszko archive 1662: anonymous enciphered letter, 31 July 1662 (catalogue 443)

Status: read (Brice Dudout, 29 Oct 2026; 71 of 71 words read in their sense, 67 certain, 3 probable, 1 restored, 0 unresolved; Daniel Bourdeau's 95% rule).

Contributed by Brice Dudout (Europe chiffrée), 29 Oct 2026. Published write-up (local, to be pushed when the GitHub account is restored):
https://bdudout.github.io/europe-chiffree/en/documents.html#asang-1662

## Document

Kraków, Archiwum Narodowe, Archiwum Sanguszków, teka 134/8; 2 pages; DECODE R7513
31 July 1662 (“Ultima Julij A° 1662”, in clear at the head). not stated; the writer is in a region “towards the sea” where the Elector of Brandenburg is expected (Prussia?).
Sender: unknown (a few clear words at the end: “… MM Pan”, a form of address). Recipient: unknown (a lord, “MM Pan”).
Images: DECODE R7513 (https://de-crypt.org/decrypt-web/RecordsView/7513), reproduction from the Archiwum Narodowe w Krakowie; not included.

An unsigned Polish letter, dated in clear on the last day of July 1662, enciphered throughout with 23 composite sign groups. No contemporary decipherment, no key. We broke it from the ciphertext alone, checked it on the held-out reverse, and read it in full.

## System and key

Simple substitution: each letter is written as a composite group of three or four strokes (digits, letters, squares, triangles: ☐78O = t, 15☐c = e, 50lF = i, 83yΔ = o…); 23 groups, no word division, punctuation kept; a cross over a marks ą.

`key.tsv` = key K443; `signs.md` = the 23 group shapes and their code letters used in `transcription.txt`.

## Validation

Method. Atlas of the 23 groups frozen before any computation; protocol written and hashed before computation; front (21 lines, 254 groups) for learning, reverse (6 lines, 66 groups) held out and never decoded before the key was frozen. Broken by simulated annealing on a Polish letter model (Latin, French, German and Italian score clearly lower); the Polish reads at once; two values corrected from the reading of the front only (g and k).

Validation. One measurement on the reverse: 97% of groups have a value; 86% of letters fall in words of the Polish lexicon (segmentation fixed in advance), against at most 58% for 200 permuted keys and at most 70% for 200 shuffled texts. The held-out reverse is short (66 groups): we say so.

## Reading

First published decipherment, to our knowledge. 320 groups, 71 words. Published under Daniel Bourdeau’s rule: 95% of words read as sense, counted on the enciphered part only. Here: 71 of 71 words read as sense (100%): 67 certain (94.4%), 3 probable (4.2%), 1 restored from the sense (1.4%), 0 unresolved. Reasons in the notes.

Files: `transcription.txt`, `decryption.txt`, `reading.md`, `translation.md`, `key.tsv`, `signs.md`.

## Notes

- The moment. In 1662 Sweden held Riga and Livonia under the Peace of Oliva (1660). The writer reads the public prayers and fasts ordered in Sweden as the herald of a war. The Crown army was then in the south-east, around Lwów, where the confederation of unpaid soldiers (1661–1663) occupied the country: hence the advice not to strip “the side towards the sea” (Royal Prussia, Gdańsk). “Kurfirst” is the Elector of Brandenburg, Frederick William, duke in Prussia; he came to Königsberg in the autumn of 1662 to bring the Prussian estates to heel. Where the writer was is not stated: Prussia is a hypothesis.
- “Do not believe every spirit.” First Epistle of John 4:1, “nie każdemu duchowi wierzcie” in the Wujek Bible (1599): a warning against false rumours.
- Probable words and the restored word. {kogs}: letters certain; we take it as “kogoś” (someone), written short; a proper name is not excluded. kozdem{u} and Cur{f}irst: on the reverse, two groups occur only once and were not in the key drawn from the front: Ꝑt33, a variant of ϕt33 (u), and Mig4, f from the sense (Curfirst = Kurfürst). zapowiedzie[i]li: one group is partly covered by an ink blot; place and sense give i.
- Punctuation. Stops and commas are the cipher’s own; “Gd. anska” is written with a stop in the middle (“do Gdańska”). Between “Sam” and “zdrowie” the writer left a few words in clear (“… MM Pan”), not transcribed in full here (uncertain reading) and not counted.
