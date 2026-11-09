# pawel1624: Carl Pawel to Frederick V, King of Bohemia, 25 Nov 1624 (BSB Clm 10382 n. 46), key of the letter cipher

Status: solved at the time (contemporary interlinear decipherment on the letter); letter key identified as the casimir1629 alphabet moved by 3 and validated on a held-out page (Brice Dudout, 5 Nov 2026; 13 of 13 held-out letters vs 0.154 for the best shuffled key; the held-out part is small). The clear text of the letter is not transcribed here. Second document (9 Nov 2026): BSB Clm 10419, Andreas Pawel to Rusdorf, read in part with the same key, unchanged; second held-out test 70/77 = 0.909 vs 0.221.

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

## Second document: BSB Clm 10419, Andreas Pawel to Rusdorf, 1622-24 (added 9 Nov 2026)

Munich, Bayerische Staatsbibliothek, Clm 10419 (Collectio Camerariana; provenance "Nachlass Familie Camerarius"): letters in
French from Andreas Pawel to Johann Joachim von Rusdorf, the Palatine envoy in London, 1622-1624. Digitised microfilm, MDZ
bsb00116467, https://www.digitale-sammlungen.de/en/view/bsb00116467 (Public Domain Mark 1.0, credit "München, Bayerische
Staatsbibliothek"; the IIIF manifest was checked on 9 Nov 2026). No image or crop is included here. Pointer first given in #359.

The same cipher. The runs of two-digit numbers read with `key.tsv` **as it stands**, with no change: the cipher table of Carl
Pawel's letter of 1624 (Clm 10382 n. 46) is also the one of Andreas Pawel's letters to Rusdorf. The two-letter signs are the same
kind (here kk = son; in n. 46 mm = so, rr = und, a3 = zu). The 3-4 digit code groups look like one nomenclator filed by the German
word (2224 kommen, 2226 Royne = Königin, 2228 R. d'Angl. = König v. England, 2255 guerre = Krieg, 2878 Palatinat = Pfalz,
3225 ruiner, 3515 Stuttgart): a hypothesis only, with exceptions (1732 Mansfelt, 3166 Westmr).

Second held-out test (`validation.txt`, second part). Protocol hashed; numbers of scans 283-284 transcribed and hashed before
their glosses were read; one measurement: 15 glossed runs, 77 letters, **0.909 (70/77) against 0.221** for the best of 200
shuffled keys (margin 0.688; thresholds >= 0.85 and >= 0.30). **Declared leak:** fragments of the gloss were glimpsed on 4 runs
while the line bands were being cropped; without them the score is 0.879 on 58 letters. Two of the seven misses are 78 glossed i:
probably 38 (= i) misread, since Pawel's 3 and 7 look alike at 1296 px; the key was not changed. An earlier, very small test
(scan 181, 6 letters: 0.833 vs 0.333) is superseded by this one.

Texts: `clm10419_transcription.txt` and `clm10419_decryption.txt` (word list, not prose). Unglossed runs (Daniel's count):
225 "leur 71.32.78.22" = **fust**; 284.13 "il bien 23.29.17" = **bon**; 284.12 59.56.4?.65.61.77 = **ex[p]res** (p restored
from the sense); 283.03 15?.32.65.11 = **?ura** (15 doubtful). Total: 15 letters certain, 0 probable, 1 restored, 1 unresolved.
Scans 98, 175, 190, 199 and 240, which a low-resolution survey had taken as bare, are glossed throughout at full resolution.

Code values read from the glosses (not validated): 3230 = Rusdorf (glossed "Rustorff" on scan 190; bare on 225),
3801/3812 = Vice-Cantzler Ulmer, 3811 = Ulm, 1759 = Friderich, 2228 = R. d'Angl., 2813 = Papistes, 788 = Mayence,
1877 = Dresden, 2966 = pretexte, 2979 = les Princes Protestans. Codes 3049, 188 and 3931 (scan 40) have no gloss and stay unread.

**Date anomaly (scan 40).** The subscription reads "Ce premier jour de l'an 1624. st. vet." (11 January 1624 new style), but the
letter is bound among letters of 1623 (scan 38: received 18 June 1623; scan 52: 28 August 1623). Either the leaf is misbound or
the year is a slip (1623?). Not decided; we draw no date from it.

Summary (scan 284; date not read): Pawel writes to Rusdorf of a setback ("l'eschec") in January, of resources, "diplomata" and
something "irreconcilable"; he speaks of the burghers, the Swiss and the peace, of troops "tant à pied qu'à cheval", and says that
the King of England (code 2228) "en fit le mesme". Scans 131 and 181: Nancy, Spanish alarm, the King of England's war and
Parliament, the Palatinate, Count Digby's recall; the Duke of Bavaria and the Electoral College, Mainz, Dresden, the Papists.
Drawn from the glosses and the legible clear text, not from a full transcription.

Prior work: nothing on Clm 10419 or bsb00116467 in this repository's targets, catalogue, leads, issues or PRs apart from our
pointer #359 (GitHub API, 9 Nov 2026). Not on DECODE as far as we know. The glosses are the decipherment of the time (credited
`contemporary`).

Limits: one reader (an agent), on 1296-px microfilm images; most of the 300 scans not transcribed; the nomenclator has no key.
