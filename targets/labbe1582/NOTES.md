# Desiderio l'Abbé to Nevers, Prague and Breslau, 1577 — research result

Status: read (7 Oct 2026). Key recovered by AngusRobinson (outside contributor, GitHub PR #20), checked here.
Write-up: https://dbourdeau.github.io/cyphersolver/labbe1582.html

## Result (PR #20, checked 7 Oct 2026)

AngusRobinson recovered the key and deciphered every numerical insertion of nos. 30 and 37/38
(`KEY_AND_DECRYPTION.txt`, `SOLUTION.txt`). His route: three similar figure strings guessed as *l'empereur* /
*empereur* (the word is frequent in the surrounding clear text), which fixed one- and two-figure units with
homophones; the rest of the key followed from decoding other passages. Ciphertext-only (a probable word, no
external plaintext).

**Key.** a=02/04 b=08 c=01 d=03 e=1/11 f=21 g=31 h=09 i(j,y)=3/13 l=23 m=33 n=43 o=5/15 p=25 q=07 r=35 s=45
t=55 u(v)=9/19 x=8/18 z=29; **6 = word space** (the "conspicuous marks after figures ending in 6" noted on
23 Sept are the points that follow the space sign). Pattern: one-digit odd figures and their teen forms are the
vowels; consonants are two-figure groups ending in 1, 3, 5 (or 8/9 for b, h, q, z, with a leading 0).

**Check here (`decode_pr20.py`, output `reading_pr20.txt`).**
- Every one of the 31 token lines decodes with the stated key to the stated plaintext (0 mismatches).
- Transcription: the PR's figure streams agree with this project's independent draft of 23 Sept
  (`runs_dots.txt`, made before the key was known) in 897 of 914 figures (98.1%); the differences are the PR's
  corrections, and the corrected ones make sense.
- Images re-checked here at native size: May, f77 line 1 (`33 02 13 45 6.` = *mais*; `43 1 6. 25 23 11 9 35 1 35
  15 3 11 43 55 6.` = *ne pleureroient*), f77/f79 line 2, and f65 *Les Polonois* `45 15 43 55 6. 03 13 19 13 45 1 45`
  = *sont divises*, *estoient, et iacoit quilz* `33 15 43 45 55 35 1 43 55 6.` = *monstrent*, `11 08 1 35 6. 11 55 6.
  23 11` = *(uue)ber et le*. All match the PR. f77 writes `53 15` where f79 has `35 15` (the 53/35 difference noted
  on 23 Sept): f79 gives *retournoit*, so f77 is a copying slip.
- Shuffle control: fr-1530-despatches LM, per character: key −2.500; 1000 shuffled keys (same tokenisation) mean
  −8.137, sd 0.469, best −6.738; z = 12.0.
- Measured fraction: 536 cipher tokens (spaces included), 2 obscured figures (f64r03 *or[g]ueil*, f64r08
  *reau[l]me*) restored from context, 534 read = 99.6%. Every word is French sense or a name that the clear text
  confirms (*Wastauicio* is written in clear near the cipher *uuarsauicio*).
- Historical consistency: *mondeui* = Vincenzo Lauro, bishop of Mondovì, nuncio in Poland (clear context *Monsieur
  le Nonce*); *sboroschi* = Zborowski; *uuarsauicio* = probably Krzysztof Warszewicki (identification not checked); *dansqui* = Danzig; *batori* =
  Báthory; *uueber*, *trautzen* = Weber and Trautson, both named in clear in the May letter.
- Prior reading: none found. Cryptiana, DECODE and web searches on 23 Sept found nothing; a web search on
  7 Oct found nothing either. No DECODE record is known for BnF fr. 3198 nos. 30/37/38.

**What it says (selection).** Prague, 2 March: *puisse prendre femme en hongrie* ...
*si lempereur* ... *titre de roi* ... *ami de ceste maison* ... *du turc* ... *auoir paix* ... *les Polonois sont
diuises, monstrent bon uisage au batori, aux coeurs est le contraire* ... *de nouuelle election*. Breslau,
2 May, after Weber "suivra encore la Court le temps de deux ans pour estre receu aux affaires d'icelle": *mais
plusieurs ne pleureroient s'il n'y retournoit jamais*.

## Remaining gaps
- f64r03 and f64r08, one figure each under a blot - blocker: illegible; restored from context as *orgueil* and *reaulme*, grade C
- f64r06 *trouer* for *trouver* - blocker: illegible; a writing slip in the cipher, not an unread token (no figure is unread)

## Escalation
- [x] siblings: no. 38 (f79) is the second witness of May and fixes f77's 53/35 slip
- [x] clear-pages: no decipherment on the leaves; the clear text names the people the cipher names
- [x] known-keys: the 1580 Nevers key (fr. 3995) tried 23 Sept, does not fit; the PR key is new
- [x] print: Cryptiana, DECODE, web: nothing (23 Sept and 7 Oct)
- [x] key-rebuild: key complete for every figure that occurs (PR #20)
- [x] retry: all 31 lines decoded with the final key; 0 tokens unread apart from the two blotted figures

---

## Earlier record (23 September 2026, superseded)


**Superseded 23 Sept result:** see [REASSESSMENT.md](REASSESSMENT.md) for the expanded inventory, failed cryptanalytic tests, successful synthetic control, corrections to the clear-text outline and the new February cipher-dispatch lead. No cipher plaintext or key has been validated. This is not a finding of intrinsic impossibility.

The material below is the earlier research record. Its claims of a completed clear reading and absence of the writeup skill are superseded by the reassessment; the clear-text files remain provisional.

## Earlier research record

**Earlier verdict: clear text read; cipher insertions unsolved. Move on pending a contemporary key or decipherment.** The letters are valuable intelligence from Rudolf II's first year as emperor, but the sensitive snippets are short and dispersed through otherwise legible prose. I have not inferred their plaintext from context. The May passage survives twice in cipher, without a clear counterpart. A later Nevers numeric key is demonstrably not the one to apply. The result is a substantial historical reading, not a cryptographic solve.

## 1. Sources and pagination

* BnF français 3198, no. 30, Desiderio l'Abbé to the duke of Nevers, Prague, 2 March 1577: **canvas f63** contains the opening on manuscript fol. 62; the dispatch continues across canvases **f64–f66**, ending with a dated close and postscript on the right of f66. A first inspection starting at f64 missed the opening; this has been corrected.
* Same volume, no. 37, l'Abbé to Nevers, Breslau/Wratislavie, 2 May 1577: manuscript fol. 75, **canvas f77**; the address or reverse is on f78.
* Same volume, no. 38, another copy of the 2 May letter: manuscript fol. 76, canvases **f78–f79**. The BnF catalogue calls no. 37 “avec chiffre” but does not say this of no. 38; the image of no. 38 nevertheless repeats the cipher. It is a second witness, **not** a decipherment.
* Primary Gallica volume: https://gallica.bnf.fr/ark:/12148/btv1b9060073v . Catalogue: https://archivesetmanuscrits.bnf.fr/ark:/12148/cc496591 . The local `images/` directory contains 3000- and 6000-pixel IIIF copies. Enhanced crops and reading tiles were used during inspection, then removed as regenerable scratch files; run `prep_images.py` to reproduce them. `src/manifest.json` is the volume's IIIF manifest.

## 2. What the letters say in clear

The opening Prague page describes L'Abbé's effort to obtain answers to two letters from Nevers and his difficulty at court during an illness and news of unrest in France. He then reports on Báthory and Danzig. The continuation discusses Toruń, restoration of Catholic Mass in a disputed church, the papal nuncio, the Báthory and Transylvanian envoys received by the emperor, Polish suspicion that Báthory will not live long, and imperial pensions and payments to Polish magnates. Later pages report requests for loans to support the Hungarian border, the Silesian estates' resistance on religious grounds, court arrivals, a purported peace proclamation in Brussels, an imperial mission of obedience to the pope, the empress's Toledo revenues, a Swedish–Báthory understanding, and rumours from Constantinople about Ottoman peace with the emperor and war against Persia. A page-by-page reading with primary links is in `prague_reading.md`.

The Breslau letter begins with Nevers's Mantua/Monferrat financial and legal business, including an annual 2,000-écu payment and missing supporting documents. It then reports that Johann Baptist Weber relinquished office three days before the emperor's departure on 27 April and that Dr Siegmund Vieheuser immediately took his place. Weber went to Augsburg to inspect the Krombach lordship and planned to return to Vienna. The cipher follows his plan to attend the court for two further years. The copied letter then names the archdukes, Harrach and Trautson as members of the travelling secret council. A working transcription of the clear passage is in `breslau_reading.md`.

## 3. Cipher evidence and attempts

* The Breslau passage has **77 written digits** in the current transcription, interrupted by the clear word *plusieurs*. The two copies agree closely, though one apparent `53/35` difference near the second line remains. Both show conspicuous marks after figures ending in 6; their function is not yet established. `breslau_cipher_draft.md` preserves the digit stream without silently deciding whether its units are one or two figures.
* Prague contains many short, intercalated numeric stretches, densest on canvas f65. They have not been transcribed end to end. A keyless language-model attack on an unverified stream would be unreliable; visual ambiguities include 2/7 and 3/5, and the unit boundaries are unclear.
* The “Chifre avec Madame” of June 1580 in BnF fr. 3995 fol. 1 was downloaded and read at high resolution (local `src/fr3995_f10.jpg`; Gallica https://gallica.bnf.fr/ark:/12148/btv1b525085665/f10). It is a two-figure homophonic alphabet with word codes and nulls, but the 1577 correspondence repeatedly uses low numbers with no corresponding alphabetic role in that table. Applying its assigned values in context produces no grammatical French. It is a later structural comparison, not the key.
* No relevant published transcription or key turned up in targeted catalogue, Cryptiana, DECODE, and web searches. Historical research on Rudolf II's early court confirms the Weber–Vieheuser transition (Alexander Koller, https://austriaca.at/0xc1aa5572%200x004071b5.pdf), but gives no plaintext for L'Abbé's coded sentence.
* EasyOCR on the enlarged Breslau numeric lines returned unstable, low-confidence digit strings; it cannot replace direct visual transcription. The 6000-pixel scans do make the clear handwriting and most individual digits legible.

## 4. Limit of the reading

This is a **partial decipherment problem but a mostly readable document**. The clear passages supply a substantive account of the imperial court and Polish affairs. The cipher fragments are not securely solved. They may contain precisely L'Abbé's more sensitive judgments, so the clear context must not be presented as their recovered text. To resume cryptanalysis, first transcribe all Prague figure runs at native size with uncertainty flags, then search for an exact contemporary Nevers–L'Abbé key or a manuscript with an interlinear decipherment. The two May copies allow correction of some glyphs but offer no known plaintext. A solver should be attempted only on a checked stream and evaluated against independent held-out runs; the 1580 key should not be used as a crib.

## 5. Research files

* `prague_reading.md` — sequential content reading, March dispatch.
* `breslau_reading.md` — working clear-text transcription, May dispatch.
* `breslau_cipher_draft.md` — both witnesses of the May numeric passage, with differences marked.
* `prep_images.py` — repeatable crop and contrast generation from downloaded IIIF scans.

Earlier claim that the writeup skill was absent: corrected. The attempted/unread page is now prepared with the repository skill; see the current reassessment.
