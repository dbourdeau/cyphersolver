# pawel1624: Carl Pawel to Frederick V, King of Bohemia, 25 Nov 1624 (BSB Clm 10382 n. 46), key of the letter cipher

Status: solved at the time (contemporary interlinear decipherment on the letter); letter key identified as the casimir1629 alphabet moved by 3 and validated on a held-out page (Brice Dudout, 5 Nov 2026; 13 of 13 held-out letters vs 0.154 for the best shuffled key; the held-out part is small). The clear text of the letter is not transcribed here.

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents. Lead no. 2179, located and vetted in the leads review of
4 Nov 2026 (batch b70). Not in the catalogue; no DECODE record.

## Document

Munich, Bayerische Staatsbibliothek, Clm 10382 (Collectio Camerariana 32), n. 46: Carl Pawel's report to the King of Bohemia on
Colonel Fuchs's recruiting in Württemberg (Halm 1874 p. 59, dated there 15 Nov 1624; the leaf reads "den 25 Novemb. 1624", signed
"741 / Carl Pawel"). Digitised microfilm, MDZ bsb00112117, scans 181-182 (Public Domain Mark 1.0; images credited "München,
Bayerische Staatsbibliothek"; none are included here).

| scan | role here |
|---|---|
| 181 | training: the shift of the key was fitted on its glosses (15 letter runs) |
| 182 | held out: looked at only after the key was frozen, measured once (2 letter runs) |

The letter mixes a code of 3-4 digit numbers (2737 Ob. Fuchs, 3515 Stuttgart, 2224 kommen, 1732 Mansfelt, 2389 Liga), a few
signs (a3 = zu, mm = so, rr = und) and runs of two-digit numbers separated by commas, which spell words letter by letter. A
decipherment of the time is written above the lines. The content is therefore not new.

## The key is the casimir1629 alphabet moved by 3 (`key.tsv`)

The letter runs use the same alphabet as `targets/casimir1629` (Johann Casimir to Ludwig Camerarius, 1624-29, same volume): the
same letters, in the same order, each with three homophones in a block of three consecutive numbers. Only the origin differs:
every number here is the casimir1629 number minus 3.

11-13 a, 14-16 g, 17-19 n, 20-22 t, 23-25 b, 26-28 h, 29-31 o, 32-34 u/v, 35-37 c, 38-40 i, 41-43 p, 44-46 w, 47-49 d, 50-52 k,
56-58 x, 59-61 e, 62-64 l, 65-67 r, 68-70 y, 71-73 f, 74-76 m, 77-79 s, 80-82 z. Not seen: 1-10, 53-55, 83 and up.

So the Palatine side seems to have used one letter table with a movable origin, at least for these two correspondents. Other
two-digit letter runs of the Camerarius network can be tried with every shift of this table (we found no fit, from -6 to +6, on
leads 2180, 2181 and 2182, which use other systems).

## Validation (`validation.txt`)

The protocol was written and hashed before scan 182 was looked at. We started from the casimir1629 key as frozen for that target
(SHA-256 unchanged) and fitted one parameter on scan 181 only: the shift. A shift of 3 renders 0.921 of the glossed letters of
scan 181 (next best 0.737, then 0.526; the 22 other shifts 0.42 or less). The key was frozen by SHA-256, then measured once on
scan 182: 2 glossed runs (degen, brauchen), 13 letters, all right, against 0.154 for the best of 200 shuffled keys. The
thresholds, fixed in advance, were >= 0.85 and >= 0.30 above the best control.

**Limit: the held-out part has only 13 letters.** Scan 182 has no more letter runs. Over the 17 runs (102 letters), the decode
differs from the gloss only by the cipher clerk's spellings (vorharret, gunnen for gönnen, scaf, uf), by a gloss written "victix"
for victrix, and by an h the glossator added (rückh). Two numbers of scan 181 were re-read at high magnification after the
measurement (181.14: 20, not 26; 181.15: 38, not 33); both now agree with the glosses, and the key did not change.

## Texts

`transcription.txt` lists each letter run with the gloss written over it, and `decryption.txt` gives our decode with `key.tsv`
beside the gloss. They are a word list, not the letter: the code groups (glossed on the leaf) and the clear German text were not
transcribed.

One run has no gloss (Daniel's count: 1 certain, 0 probable, 0 restored, 0 unresolved): 181.10, `16 59 66 38 20 22 60 17` =
**geritten**. With the sign a3 (zu) and the run before it (ruck), the cipher says "zu ruck geritten"; the glossator wrote
"zu rückh kommen" over the whole passage.

Summary: Carl Pawel reports to Frederick V on Colonel Fuchs's recruiting in Württemberg. Fuchs came to Stuttgart and stayed
until Tuesday the 23rd, accompanied. The letter speaks of the "pars victrix", of someone who rode back, of Mansfeld and the
League, and of men who could be used. This summary is drawn from the glosses and the legible clear text, not from a full
transcription.

## Prior work

- The glosses on the letter are the decipherment of the time (credited `contemporary`, prior solution). Halm 1874 p. 59 already
  says "in Chiffern mit Auflösungen".
- The leads review of 4 Nov 2026 (batch b70) found every group glossed and closed the lead as "read", as a key source with no key
  built.
- No edition found. Not on DECODE. No target, PR or issue for Pawel or Clm 10382 n. 46 in this repository (GitHub API,
  origin/main e4c7843d, 5 Nov 2026). Not opened: Schubert, *Ludwig Camerarius* (1955; 2nd ed. 2013), and Stålhane 1934.

## Limits

- One reader (an agent), on a microfilm 1334 px wide. No human palaeographic check.
- The held-out part is 13 letters. Clm 10373 (Conrad Paulli / Pawel letters to the Camerarii, 1596-1627) was not looked at.
