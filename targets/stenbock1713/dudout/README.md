Status: read in part (Brice Dudout, 15 Nov 2026; Stenbock's petition to Charles XII: 844 of 1,014 cipher groups sure or probable outside the held-out p. 705 = 83.2%, 974 of 1,192 over the whole petition = 81.7%, only 59.9% sure; Daniel Bourdeau's 95% rule not met. Lit. L letters: period decipherment by Erlund, verified, not claimed).

# stenbock1713: Erlund's Lit. L checked, and Stenbock's petition to Charles XII read in part (Brice Dudout)

Write-up (published as it stands, limits stated): https://bdudout.github.io/europe-chiffree/en/copenhague-1714.html

## Source

C. C. Erlund, *Geheime Nachrichten von dem Schwedischen Grafen M. Stenbock* (Sonderburg 1732), Riksarkivet,
Manuskriptsamlingen SE/RA/760004/42, IIIF R0000422 (388 images, public domain mark). No image is included here.

## 1. Lit. L letters (Stenbock to Malmberg, 1714): existing decipherment, verified

Erlund broke the captivity cipher in 1714 and wrote his German decipherment between the lines (Lit. L, pp. 377 ff.,
images 144-149). We transcribed his key (Lit. F, p. 160, image 86: `key_litF.json`) and checked it on two lines of the
letter of 21 July 1714: 62/63 clear signs agree (0.984). See `litL_check.md`. Not a first decipherment.

## 2. Stenbock's petition to Charles XII, [1 May] 1714: read in part

A long draft "Stormäktigste Konung", seized among Stenbock's papers and copied by Erlund (pp. 697-707, images 305-309), is
in a different code, which Erlund glossed only in part (whole lines of dots). We rebuilt it:

- **one-part chancery dictionary**: words about 450-1087 in alphabetical order (danske 473, folk 547, Konung 653, och 764,
  til 997, Wismar 1064); small numbers = letters and syllables with homophones; repeated-letter codes for countries
  (eee Holstein, AAA Schleswig, CCC Stettin, ggg Sweden, nn Finland, ff France).
- **validation on a held-out page** (C03, p. 705): 14 of the 16 words Erlund had read there predicted (0.875; permuted
  control 0.11; threshold 0.80 written before). A second proposal of values was measured once on the same page on 11 Nov
  2026 against 200 shuffled tables, with a pre-registered protocol (W 0.213 vs best control 0.067; Erlund's glosses 8/10).
- **crib**: O. Malmström, *Magnus Stenbock i fångenskapen* (1901) quotes four passages of the same letter, dated
  1 May 1714, from the Danish copy: 115 of 139 groups right, 10 wrong, 14 unresolved under the frozen table (92%).
- **count, group by group** (`petition_groups.tsv` -> `petition_counts.txt`): all pages 974/1,192 S+P (81.7%: 714 sure,
  260 probable, 218 unresolved); outside p. 705 844/1,014 (83.2%); p. 705 after the second proposal 70/86 words (81.4%).
  **Read in part.**

Files: `petition_transcription.txt` (two passes, Brice Dudout's blind rereading integrated), `petition_groups.tsv`,
`petition_counts.txt`, `petition_reading_sv.md` (established Swedish text), `petition_translation.md` (English).

## Prior art and limits

- Malmström 1901 quotes about 12% of the petition from the Danish Rigsarkivet copy ("Handlingar rörande Fredrik IV:s
  historia"); a complete period Danish decipherment very probably exists in Copenhagen. **Not seen.**
- A Danish print of 1716 against Stenbock is reported (Kraack catalogue), not located; A. Marklund, *Stenbock. Ära och
  ensamhet i Karl XII:s tid* (2008), not consulted.
- Open values: 115, 165, 93, 36, 130 in Erlund's copy (homophones or copying slips).

Credits: Daniel Bourdeau (catalogue 455; location of the letters and of key E 4698; Erlund as the period decipherer);
C. C. Erlund (period decipherment); O. Malmström (1901 quotations); S. C. Pedersen, "Postspionen" (enigma.dk).
