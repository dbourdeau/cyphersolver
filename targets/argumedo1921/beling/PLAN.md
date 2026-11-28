# Plan: Argumedo's further letters to Félix Díaz (CEHM-Carso Fondo DCXXI), read with Narváez's table unchanged

Written by an AI agent (Claude Opus 5.5) on 25 Nov 2026, before any run of these letters was decoded, and frozen by
SHA-256 (PLAN.sha256 beside this file). No person has checked it.

What was seen before this plan: the catalogue records (upstream research/latam_mexico/cehm_hits.json) and one look at
image DCXXI.3.235.1.0001 at reduced size, to see whether the letter uses number pairs (it does). On that look I
recognised two runs by eye (35-01-10-05-17-01-23 and 13-34-10-36-04-12, which the table gives as names Narváez
printed for the October letters). That look is declared here; no run was decoded on paper or by script.

## Material

Argumedo letters in Fondo DCXXI that the CEHM catalogue marks "en clave" and that no one has worked (upstream main
1b502a790, 25 Nov 2026: targets/argumedo1921 covers only DCXXI.3.244.1 and 3.250.2):
DCXXI.3.235.1 (9 Sep 1921), 3.296.1 (26 Dec 1921), 4.344.1 (26 Jan 1922), 4.361.1 (5 Feb 1922), 4.378.1 (22 Feb 1922),
5.444.2 (10 Apr 1922), 5.510.1 (9 Jun 1922), and any further Argumedo letter found in the catalogue before decoding
starts (added to this list in an addendum with its time, before its transcription is decoded).
Images: CEHM-Carso public viewer, visor.cehm.org.mx/assets/docx/fondos/jzd/DCXXI/..., raw copies with SHA256SUMS in
sources/raw/narvaez_push_2026-11-25/cehm/ (private study copies, not for the repository).

## Key (frozen)

Narváez's table (2019 book p. 363; 2015 article p. 122) as already in the repository at
targets/argumedo1921/key.tsv (SHA-256 69ce383ff6c3062dd64ab850d6cd28cd02f84564d5071708f816fb577856831e at main
1b502a790): A=34 B=35 C=36 D=37, E=01 ... N=10, Ñ=11, O=12 ... Z=23. Applied unchanged. Codes 24-33 and anything
outside 01-37 are not in the table: they decode to "?" and the word is a hole. No key value is changed or added.

## Transcription

T1: mine, from the full-size images, run by run (run = a hyphen-joined chain of two-digit codes; a separate run starts
after clear text). T2: a helper agent (Opus) working blind (no T1, no key, no decode, no Narváez). Both written to
files and hashed before decoding. Differences are settled on the image without the decode; any still open is kept as
a doubt and both versions are decoded and reported.

## Control

C1 (printed runs): the frozen table applied to Narváez's printed cipher runs in his 2019 book (pp. 359-363, our loan
photos) must give his printed clear: pass if at least 95% of letters agree (the upstream control on the 2015 print gave
88/89).
C2 (chance): the decode of all new runs is scored by Spanish letter-trigram log-likelihood per letter (model built from
the plain Spanish text of the same letters, typed by me from the images, cipher runs excluded; if that is too short,
from the Madero Epistolario word list held locally). The frozen table must score higher than every one of 1,000
random permutations of the same 27 code values (seed 20261125).

## Counting (strict)

- A cipher word is a word of the plain sentence that the run stands for (a run that is a name of three words counts
  three; initials count as words).
- Read: the decode gives the word letter for letter.
- Hole: any letter differs, is "?", or must be supplied, dropped or swapped (a writer's slip, even an obvious one).
  The intended word may be given in braces as for argumedo1921, but it is a hole.
- Unread: no sensible word.
- Per letter: cipher words, read, holes. Read share = read / cipher words.

## Pass mark

The reading of a letter is reported as "read" if C1 and C2 pass and its read share is at least 0.95 (or the
repository's short-text floor applies), "read in part" if C1 and C2 pass and the share is lower. If C1 or C2 fails, the
table is not this letter's key and the result is a miss, reported as a miss.

## Checks after decoding (not part of the pass mark)

Names from the decode are compared with the CEHM catalogue summary of each letter, which names persons the cataloguer
could read in clear. Agreement is reported as "fits", never as proof.

## Addendum 1 (25 Nov 2026, before C1 and C2 were run; T1 and T2 were compared, the settled transcription written, nothing decoded by script)

- C2 model text: the Madero Epistolario named above may not be processed by computer (INEHRM terms; project rule), and
  typing the clear text of the letters was not done. The trigram model is built instead from the public-domain OCR
  text of *Archivo Santander* vol. XIV (Bogotá 1918, Internet Archive archivosantander14bogo), held at
  sources/raw/ill_photo_leads_2026-11-23/archivosantander14bogo/. Accents stripped, Ñ kept, other signs dropped.
- C1 printed runs: taken from the OCR of the loan photos of Narváez 2019 pp. 359-363 (IMG_3228-3230), checked by eye
  against the photo for the runs on p. 360; the clear for each is the one Narváez prints (pp. 362-363).
- More Argumedo letters found in the catalogue (fondo DCXXI, search "Argumedo", 59 records, 25 Nov): 3.296.1 etc. as
  listed; also 4.425.2, 7.655.2, 7.709.2, 7.710.1, 7.726.2 (not marked "en clave"; images fetched, not yet looked at
  for runs). They are outside this round; if they hold runs they get a later addendum before decoding.
