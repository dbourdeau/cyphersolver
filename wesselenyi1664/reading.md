# R674 — reading

Cipher runs in **bold**, deciphered with the key in `key.py` (reversed alphabet, 24=a … 1=z, vowel homophones 25=a,
26=e, 28=o, 29=u; the alphabet of DECODE key R672). Clear text transcribed from the image; `(?)` marks a doubtful
clear-text word. Struck words in ⟦ ⟧. Codes left as [60], [64].

Heading (top centre): "S…zzi" (?), not read with confidence; perhaps a name or "Secreti(?)".

> Castrorum(?) mutationes etiam necessariae essent, quo facto, si Dominus **Generalis [60]** regimenta Dominorum
> **Haster, Snaidau** et **Spork** coniungeret, possent ad minimum **tria millia hominum constituere**, quibus
> **si adiungerentur** adhuc **duo millia peditum**, ut cum illis **nos ad [64] in castris** collo-caremus, quam
> necessitatem videns **[64]** forte promptius **praesidium Maiestatis Vestrae reciperent**. Quod si vero illud
> **sponte et benevole acceptare nollent**, extunc de ulterioribus faciendis **actionibus temporis occasioni nos**
> accommodari ⟦…⟧ debebimus, quia hoc est certum(?), quod ista **nux** ⟦tandem aliquando necessario⟧
> **durissima** tandem aliquando necessario **frangi** debet. Alioquin non esset bonum, si hoc modo **ab indusio**
> quoque nostro **timere et formidare** deberemus.

## Translation

> Changes of camp would also be necessary; this done, if the Lord General [60] were to join the regiments of Messrs
> Heister, Schneidau and Sporck, they could make up at least three thousand men; if two thousand foot were added to
> them, so that with them we might set ourselves in camp at [64], seeing that necessity [64] would perhaps the more
> readily receive Your Majesty's garrison. But if they would not accept it of their own free will and goodwill,
> then for the further actions to be taken we shall have to adapt ourselves to the occasion of the time, for this
> is certain, that this very hard nut must at last, of necessity, be cracked. Otherwise it would not be good if in
> this way we had to fear and dread even our own shirt.

## Notes on the cipher words

- `hastersnaidau` = Haster + Snaidau: the imperial colonels Heister and Schneidau, spelled by ear. 26 (e) occurs only
  here; its value is the vowel slot "Be" of R672 and the only reading that gives a name.
- `spork` is written 7 9 11 8 15: in the reversed alphabet 9 is q and 10 is p; the writer slipped one place (10 is
  used for p everywhere else: presidium, sponte, acceptare, temporis, peditum).
- `nux` (12 29 3): 3 = x in R672; "ista nux durissima … frangi debet", this very hard nut must be cracked.
- `ab indusio quoque nostro timere`: indusium, an undershirt; afraid even of our own shirt.
- The writer duplicated `14` in "millia" (line 5) and struck it: a draft.

## Measurement

244 cipher tokens (`python docs/_check_profile.py --measure wesselenyi1664/transcription.txt`). Read as sense: 241
(all letter tokens, including the slip 9 for p). Unread: code 60 (once), code 64 (twice). 241/244 = 0.988.
Grades: H 239 (letters on the reversed alphabet confirmed by DECODE key R672 and by sense), M 2 (26=e, once, in
"Haster"; the slip 9 for p in "Spork"); the 3 code tokens unread.
