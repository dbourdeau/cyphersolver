# ENA 4100.7b: secret passage in a letter from Qus (catalogue 2883)

Status: in progress

Jewish Theological Seminary Library, ENA 4100.7b, recto (Princeton Geniza Project 11951). Letter of a son in Qus to
his mother, Judaeo-Arabic in Hebrew script, undated. PGP: lines 7-12 are "a cipher ... probably this is also in
Judaeo-Arabic ... Needs examination/decipherment" (noticed by Oded Zinger). No reading is known (prior-art check of
15 Nov 2026 in the catalogue entry; PGP page re-read 17 Nov 2026, still no transcription).

Image: `https://iiif-cloud.princeton.edu/iiif/2/9b%2Fdc%2Fd9%2F9bdcd9be1aed4b108412a7faffee4438%2Fintermediate_file/full/full/0/default.jpg`
(5428 x 7230 px, plain curl). Images are not kept in the repository.

## Session 17 Nov 2026: first attempt, not solved

### Transcription (`transcription.txt`), a first reading, NOT reliable

Read by the model from full-resolution crops. The hand is large and crude. The passage starts in the second half of
my line 7 (after the stain) and ends with my line 12; line 13 onward is clear text again ("... and we have had no
letter from you since the day Abu Mansur left ...").

    7b  אדגך אתגלב
    8   אים אוחעך ל אורכבר – תכור א
    9   אלכררקאנך אל אדיר ( אן אלמרלד
    10  אל סנאר אן אלמרדנה אולדן האגה
    11  אזג אולגי אן יאני פרגרווג יו
    12  אוירן ערך אל אועלג אי טג אלה

Known weak points of this reading:

- ת in this hand looks like ר plus a short stroke, or like ה (compare כתאבי in line 1 and כתאב in line 14). So
  אתגלב may be ארוגלב or אולגלב, תכור may be הכור / הבור, אורכבר may be אתכבר, האגה may be תאגה.
- ש looks like ע or like ין (the clear line 13 opens ואיש, which I first read ואין). So אוחעך may be אוחשך and
  אועלג may be אושלג.
- ר / ד / final ך, ב / כ, ו / ז / נ are often not separable. אלמרדנה may be אלמדינה.
- I could not read the clear lines 1-6 and 13-16 fluently either, which is the measure of how far this
  transcription can be trusted. A reader of Geniza semi-cursive must redo it before any test below counts.

### What the reading shows, as far as it goes

- 31 words, 22 of them beginning with א; the others begin with ה/ת, י, ע, ס, ט, פ.
- אל (five or six times, both as the ligature joined to the next word and as a separate word) and אן (three or four
  times) stand where the Arabic article and the particle "that" would stand. The frame looks like Arabic syntax with
  the content words replaced.
- Five words have the shape או + three letters + one more letter: אוחעך, אולגי, אולדן, אוירן, אועלג.
- Letters: ל, ר and ג are each near 10 % of the passage, far above their share in Arabic; ת, ש, פ, צ, ק, ח, ס, ז, ט
  are absent or occur once. If this holds on a better transcription, the content words are not Arabic words with
  their letters rearranged.

### Hypotheses tried (by hand, on the reading above)

| Hypothesis | Result |
|---|---|
| Each word reversed | No Arabic. The או- words become words ending in -וא, like plural verbs, but the roots are not words. |
| Whole lines reversed | No Arabic. |
| First letter replaced by א and moved to the end (or last letter moved to the front) | No Arabic beyond chance hits (רדי, גד). |
| א as a null, removed everywhere | No Arabic. |
| Letter rearrangement of any kind | Unlikely on the letter counts (above). |
| Monoalphabetic substitution | Unlikely: 70 % of words would begin with one plaintext letter (Elbaum's point). |
| Another language in Hebrew letters: Coptic, Berber, Nubian, Greek, Persian, Turkic, Romance, Tulu | Single words can be matched in several of them (which shows how weak such matches are); none gives a phrase, and the near absence of t, s, sh and p/f fits no natural language I know. |
| Ordinary colloquial Judaeo-Arabic, misread | Not excluded for parts: אים אוחשך could be a phrase of longing. Zinger and Elbaum, who read such hands daily, call it a cipher. |

No test was run by script: the transcription is too uncertain for a wordlist test to mean anything.

## Same day, second pass: tests on a word list, a second transcription, and a Berber hypothesis

### Scripted tests (negative)

A Judaeo-Arabic word list was built from the Princeton Geniza Project's public text corpus
(`github.com/princetongenizalab/pgp-text`, 4,443 Judaeo-Arabic files, 1.35 M words, 98,000 types; PGP 11951 itself is
not in it). In that corpus 22 % of words begin with א; in the passage about 70 % do. About 75 rules (reversal,
rotations, alef stripped, alef as a null, atbash, albam, 21 alphabet shifts with and without א and ל fixed) were
applied over a letter-confusion lattice of the first reading and scored against the list, with shuffled-letter
controls. No rule scores above its control (best 13 hits of 21 against 8.5 by chance, with implausible words).
Web searches for a later reading, for the Bohak-Zinger-Elbaum publication and for an Arabic word game of this
shape found nothing.

### Second transcription (`transcription_b.txt`)

An independent reading by a subagent, with alternatives. What it changes:

- The hooked S-shaped letter I read as ג is ג in אלגמע but is also the **word-final alef** of the clear lines
  (סוא, נרא, שא). The surplus of ג in my first reading is therefore not real.
- The short word I read אל in lines 9 and 10 has no ascender: it is **אר**.
- Line 12 ends in plain Arabic: **אין שא אללה**, "God willing". The secret stretch ends just before it.
- A horizontal stroke follows a letter four times (lines 8, 9, 10); kept as a possible divider.

### Hypothesis: the passage is Berber written in Hebrew letters (NOT verified)

With those corrections, and ע / ג standing for gh, the end of the passage gives a connected sentence in Berber
(Tamazight of the Moroccan type):

| Hebrew letters | Berber | Meaning |
|---|---|---|
| אזן (line 11; ז/ו and נ/ג uncertain) | azn | send (imperative) |
| אודאי | uday | a Jew |
| אן יאוי | a(n) yawi | who will bring / to bring |
| פרגר... | ? | object, unread |
| אויתן (line 12; the fourth letter is ר, ה or ת) | awi-tn | take them / keep them |
| ערך | ghr-k | with you, at your place |
| אל | al | until |
| אועלג | ughulgh | I return |
| אין שא אללה | in sha Allah | God willing (Arabic) |

"Send a Jew to bring [...]; keep them with you until I return, God willing." Other words fit Berber particles: אדאך
(line 7) = ad ak, future particle with "to you"; אר (lines 9, 10) = ar, the present-tense particle or "until";
איס (line 8) = is, "that / is it that". This also explains the alef-initial words (Berber particles a(d), ar, is, al, verbs
and nouns beginning with a vowel) without any cipher.

Against it, and to be checked: it rests on about 12 of 31 words; lines 8 to 10 are not read; my Berber is from
general knowledge, with no dictionary or grammar opened; Berber should show many t and n, which the transcriptions
show only if several ר are ת (possible in this hand, not shown); a Jewish family letter in Berber of this period
would be very unusual, so the claim needs a Berberist and a Geniza palaeographer before it is stated anywhere as a
reading. Single-word matches were found for other languages in the first pass; what is different here is one connected clause
that suits the letter (a son away from home, a mother keeping goods).

## Remaining gaps

- The whole passage (about 31 words, 127 letters) is unread. Blocker for this session: no reliable transcription.
  Not an outside blocker; the image is good.

## Escalation

Next steps, in order:

0. Test the Berber hypothesis: a Berberist (Tashelhit / Tamazight, ideally with medieval Berber, e.g. the Arabic-script
   Berber of the Almohad period) reads `transcription_b.txt` against the image; check each proposed word in a
   dictionary (Taifi, Destaing); look in PGP for other Berber or Sijilmasa / Dar'a family letters.

1. A transcription by a reader of Geniza hands (ask the Princeton Geniza Project: Zinger, Elbaum; the 15 Nov sweep
   notes also ask that PGP be written to before anything on this fragment is published).
2. Read the clear lines and the verso fully for names and subject (Abu Mansur; what the son could want hidden).
3. With a firm text: test content words against a Judaeo-Arabic word list under each word-game rule, and check the
   Hebrew-jargon reading (Hebrew words with the Arabic article, the "lashon" of Geniza merchants).
4. Search the literature on medieval Arabic argots (Banu Sasan vocabulary, al-Jawbari) for a rule that yields
   alef-initial words.
5. Siblings: other letters by this hand or family in ENA 4100 and PGP (none found in the 15 Nov sweep).
