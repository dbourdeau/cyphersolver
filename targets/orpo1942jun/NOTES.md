# Ordnungspolizei Doppelkasten radiogram A115, Mogilev, 16 June 1942: Bletchley's decrypt (the Borki report)

Split on 14 Oct 2026 from `../orpo1942/` under the one-key rule (George Lasry, 14 Oct 2026). A115 is in the daily
key of 16 June 1942 (discriminator ARTTN); the five messages of 27 February 1942 in `../orpo1942/` are in another
daily key, a different cipher with its own page (`docs/orpo1942.html`). This entry's page is `docs/orpo1942jun.html`.
The shared material stays in `../orpo1942/`: `msgs.txt` (all six ciphertexts), `dk.py` (reference implementation),
`kpsolve.cs` (known-plaintext solver), `mksyn.py`, the manuals, Weierud's PDF and the NSA articles.

Outcome: read from existing decipherment. Bletchley read it at the time; nothing was deciphered here, and the
key-free alignment of the decrypt to the ciphertext failed, so the key was not recovered.

## The message

Source: Frode Weierud, *German Police Doppelkastenschlüssel Messages* (CryptoCellar, 5 Aug 2020), from NARA RG 457
HCC Boxes 1386 and 202. A115 = BMR serial; SQF (Mogilev, HSSPF Russland Mitte) Nr 14, handed in 2325, 228 letters
by the preamble, to ALQ via DQH Berlin, 3742 kHz; stations 51 and 43 both copied it. Discriminator ARTTN.
`a115.txt` holds its 223 letters (from `../orpo1942/msgs.txt`, discriminator removed).

## The decrypt

Bletchley's decrypt, entry 21 of the day's German police decrypts, typed in German (`hsspf_decrypt_1.png`,
reproduced in Hanyok, *Eavesdropping on Hell*, NSA 2005): "An Rf SS und Chef Orpo. An Strasse BOBRUISK-MOGILEW,
Partisanenkampf: 16 Mann von Pol. Batl. 51 gefallen. Das Dorf BORKI, in dem Waffen und Munition gefunden wurden,
wurde dem Erdboden gleichgemacht. Die Einwohnerschaft liquidiert. Von Höheren SS und Pol.führer Russland Mitte."

Hanyok leaves Borki unlocated; it is Borki, Kirovsk district, Mogilev region, destroyed with six neighbouring
settlements on 15 June 1942 by the Dirlewanger battalion, Einsatzkommando 8 and police after partisan attacks on the
Mogilev-Bobruisk road (Dirlewanger's report: 2,027 dead; memorial on the site). Zhukov, *Okhotniki za partizanami.
Brigada Dirlevangera* (military.wikireading.ru/62640), gives the same 16 dead of Pol. Batl. 51. Pointed out by Ilya
(reader email, Sept 2026); also mogilev-region.gov.by and partizany.by/battles/tak-pogibla-derevnya. Schmeh's 2021
list of WWII ciphers marks the group "partially solved" because of this decrypt.

## The odd count

The 228-letter count in both intercepts and in the German header leaves 223 after the discriminator. That is odd,
so the German clerk added or dropped a letter. The ciphertext only pairs up if the stray letter is among the first
~9. Counted from the end, it has 25 repeated digraphs (19 digraph types repeat); counted from the start it has 8,
which is chance level.

## The alignment attempt

Aligning Bletchley's text to its ciphertext, key-free (`align115c.py`, `align115h.py`; repeated cipher pairs ⇔
repeated plaintext pairs; exact backtracking over spellings, X separators, numbers, address/signature placement,
Borki/Mohilew/Bobruiisk variants, 222 or 224 letters, L = 1–24): **no consistent alignment**. The same search
recovers a synthetic spelling in 35 s. So the enciphered wording differs from Bletchley's typed text (abbreviations,
order, or extra matter), or the police layout differs from both manuals. With the exact wording, about 80 pairs
would let `../orpo1942/kpsolve.exe` recover the boxes (it solves 111/111 synthetic pairs, 68/80 at 80 pairs).

Run: `python targets/orpo1942jun/align115c.py targets/orpo1942/msgs.txt 17 0` (the scripts find `dk.py` and
`msgs.txt` in `../orpo1942/`).

## Remaining gaps
- the decrypt checked letter by letter against the 223 cipher letters, and the boxes - blocker: no-key-material; no consistent alignment of the typed decrypt, and no other plaintext of the 16 June key

## Escalation
- [x] siblings: the other five Weierud messages are the 27 Feb key (and C43), a different key
- [x] clear-pages: the Red Forms and teleprinter copies carry only the preamble
- [x] known-keys: no key of 16 June 1942 is known; kpsolve needs about 80 pairs
- [x] print: Hanyok 2005 (the decrypt), Weierud 2020, Schmeh 2020/2021
- [x] key-rebuild: key-free alignment over spellings, layouts and lengths (align115c.py, align115h.py): no fit
- [n/a] retry: no key was recovered, so there is nothing to rerun on the letters
