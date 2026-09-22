# BnF fr. 3092 ff. 101-107, three "Mémoires chiffrés" (DECODE R3699-R3701) — NOTES

Status: no write-up (unpublished 22 Sept 2026 at George Lasry's request: he and a historian have deciphered and analysed these letters for their own publication; do not publish or send to DECODE without his word). Read 22 Sept 2026. Key: Lasry 2023 (fr. 3029 cipher), applied unchanged. Two name signs tentative.

## What it is

- BnF, Français 3092 (anc. 8617), a Robertet dossier of 1520-21 letters and news. BnF inventory
  (archivesetmanuscrits cc49555w): no. 43 "Mémoire chiffré", f. 101; no. 44 "Autre mémoire chiffré", f. 103; no. 46
  "Mémoire chiffré", f. 107. Neighbours are dated 1521: Langeac's instructions (Troyes, 6 Sept 1521), Pamplona news
  (31 July), Nassau's army, Mouzon (21 Aug 1521), J. Breton de Villandry "de Callais, 8 novembre" (no. 24).
- DECODE R3699 (f. 101, 1 p.), R3700 (ff. 103-104, 3 pp.), R3701 (f. 107, 2 pp.): "Non-decrypted", unknown
  sender/recipient, date "1520-01-11/1540", images login-only. Images fetched with the DECODE cookie
  (`img/`, git-ignored): R3699 P2 = f.101r (P1 = opening f.100v/101r); R3700 P2 = f.103r, P3 = f.103v, P5 = f.104r
  (P1, P4 openings); R3701 P3 = f.107r, P4 = f.107v (P1, P2 openings).
- Catalogue entry 182 ("Unknown sender to unknown recipient, 3 ciphertexts, 11 Jan 1520", class C, scored by rule).

## Prior work

- Tomokiyo, cryptiana GL.htm ("De la Tremoille's(?) Cipher (??1520-1521): BnF fr.3029, BnF fr.3092"; local copy
  `gramont1529/GL.htm` l. 255 ff.) lists fr. 3092 ff. 101, 103, 107 in the cipher broken by George Lasry (and Norbert
  Biermann) in 2023, and prints an edited text of Lasry's raw decipherment of "fr.3092, f.100": it is the whole of
  f.101r (26 lines) here. Tomokiyo suggested the "royne d'Angleterre" and "Cardinal en Flandres" might point to
  Elizabeth I and Granvelle; the reading here fixes it in 1521 (below).
- ff. 103-104 and f. 107 have no published text anywhere found (GL.htm, francis.htm, DECODE). Read here first.
- Sister leaf fr. 3029 f. 134 read with the same key in `fr3029f134/`.

## Key

Lasry's table for the fr. 3029 cipher (`../fr3029f134/key_f67.png`, `../fr3029f134/key.md`), unchanged: one sign per
letter, six nulls, name signs Nom 1-4 and Place 1. Hand notes: this writer often draws O as a circle on a plain stem
(the key's L shape) and x with or without a stroke for both M and N; both read by French. No value changed.

## Reading

`transcription_f101.txt` (read by me), `transcription_f103.txt`, `transcription_f107.txt` (two transcription agents,
spot-checked against the image: 107r18-21 sign for sign). `build_signs.py` -> `signs.txt`: 4,549 signs = 4,521
letters + 15 nulls + 13 name signs, 0 unread (the two blotted signs in [?] are struck and not counted). Read bar:
4,536/4,549 = 0.997 have a value; all letter text reads as French. `lang.lm.best_language`: fr-1600-letters first
(-1.93, fr-modern -2.12). Text in `reading.md`.

- **f.101r** (R3699): the English say the Imperialists should not glory before the end; what "the Cardinal" did in
  Flanders; the Emperor's aunt and the queen of England; talks to be kept going "jusques au dixiesme de ce mois"; the
  "evesque de Lin" walking "moy chancelier" through the town says ‹N4› is "ung merveilleux esprit" seeking peace with
  the King through another hand. Writer = the chancellor, Antoine Duprat.
- **ff.103r-104r** (R3700): a servant of the grenetier of Dieppe says the duke of Albany has secretly left for
  Scotland from Honfleur on a ship victualled by his master; if the English learn it they will declare against the
  King; asks that he be stopped, or a gentleman sent to ‹N1› and the Cardinal to excuse the King.
- **f.107r-v** (R3701): after dinner the Cardinal talked alone with the chancellor of Flanders (Gattinara), then took
  the writer into his wardrobe, all familiarity; English jealousy and the people "tout enclin a ceste maison de
  Flandres"; "domp prevost" had told the Emperor that Francis hated him, and the Cardinal had him put out of the
  Emperor's council; others reported that Francis called the Emperor "idiot, meseau, ignorant"; the Germans egg him
  on; he should be sent to Spain; a truce would disperse his troops; the Cardinal says he cannot yet bring his master
  to assist Francis.

## Dating and persons

All three are despatches of the French commissioners at the Calais conference (Aug-Nov 1521) with Wolsey ("le
Cardinal") and Gattinara ("chancelier de Flandres"): Wolsey's visit to Charles V at Bruges (Aug 1521) is "ce que le
Cardinal avoit fait en Flandres"; Albany left France for Scotland in autumn 1521 (landed mid-Nov 1521). f.101 is after
Wolsey's return from Bruges (late Aug 1521); ff.103-104 before Albany's landing; f.107 during the conference. Sender
of f.101 and probably f.107 (first person singular): Duprat. Recipient: Francis I (addressed "vous" on ff.101, 107).
DECODE's "11 Jan 1520" is wrong. "Lin" = Lincoln? (unconfirmed; M). "Monsieur du Tour", "domp prevost" not identified.

Name signs (Lasry leaves all unidentified), graded from the 13 uses here plus 9 on fr. 3029 f.134:
- ‹N3› (8 here) = "roy", generic: Francis (du consentement du roy; declareront contre le roy) and Henry (sans le roy et
  cardinal) alike; fits f.134 "promectre au roy". Grade C.
- ‹N2› (4 here) = the Emperor, Charles V: "celuy ‹N2› et de sa tante et puis la royne d'Angleterre"; "le conseil du
  ‹N2›"; to be sent to Spain. f.134 "la court du ‹N2›", poisoning rumour. Grade C.
- ‹N1› (1 here) = probably the King of England: "envoye icy quelque gentilhomme par devers ‹N1› et cardinal". Grade M.
- ‹N4› (1 here) = unidentified; "un merveilleux esprit" negotiating peace separately; perhaps Leo X. Grade I.

## Remaining gaps

- name sign N1 (104r09) and N4 (101r19), 2 tokens - blocker: open-codes; one use each here, identity graded M and I from context; no key or decipherment names them
- blotted sign 103r23 end and 104r09 start - blocker: illegible; struck through by the writer, not counted

## Escalation

- [x] siblings: fr. 3029 f.134 (fr3029f134/) read with the same key; its 9 name tokens used to grade N1-N4; other fr. 3029 leaves have no printed text
- [x] clear-pages: openings P1/P4 (R3699, R3700, R3701) viewed: no decipherment, only show-through and a folio number
- [x] known-keys: Lasry's table reads every letter sign; no other key needed
- [x] print: GL.htm (f.101 text = Lasry/Tomokiyo), francis.htm, BnF inventory; no text of ff.103-107 found
- [n/a] key-rebuild: letter key complete; name signs are whole-word codes, too few uses to rebuild from frequency
- [x] retry: doubtful spots re-cropped (101r01 glorifier, 101r09 nulls, 103v10 N3, 107r18-21)
