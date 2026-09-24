# Testing decipherments of the Indus script: a validated bench, the structure of the texts, and what they say about the language

*Draft article. Daniel Bourdeau, with Claude (Anthropic). September 2026. A standalone study, not part of the
LLM-performance paper data.*
*Every number is produced by a script in `indus/`; the working record is `indus/NOTES.md`.*

## Abstract

Claims to have deciphered the Indus script appear every year, and a prize announced in 2025 has multiplied them.
They are hard to assess because a fitted key can make almost any short corpus "read". We built a test that any
proposed sign key can be run through: the key's reading of the corpus in its claimed language is compared with 100–200
copies of the same key whose values are shuffled among signs of similar frequency, in six candidate languages, and
with the sign = image equations of the Mohenjo-daro copper tablets. We ran it first on two accepted decipherments. The
Linear Elamite key beats its shuffles with vowels kept (4 of 100 as good) but not with consonants only; the Linear B
key beats them in no setting (11-41 of 100). The test cannot reliably recognise a correct decipherment. Under the validated version none of five published keys
(Yajnadevam 2024, Fairservis 1992, Parpola 1994, and the small keys of Mahadevan and Kak) reads its own language better
than its shuffles. Blindly fitted keys read about 93% of the corpus in any language and even carry over to unseen
texts in every language, so reading rates identify nothing. On the structure of the texts, replicated on an
independent sample and on a fuller corpus of 4,578 objects: the two terminal signs ('jar' and 'arrow') are fixed per
name (5 of 881 names take both against 46 by chance), the arrow class is closed (names ending in a fish sign), the
seal formula is 'X-jar man' with the head last, and foreign names written in Indus signs on Gulf seals leave the
endings out (11% of lines against 43%), which ties them to the language rather than the script. Combined with a
class-suffix test, only Dravidian passes both grammar tests outright; and of thirty-seven predictions registered before
testing, sixteen held and twenty-one failed; the held ones are structural (head-final names, bound pairs kept whole
across line breaks, free signs in foreign names); a Linear B-calibrated shortlist of candidate sound signs failed
its three tests. No sound value is established. We describe what the corpus supports and what
evidence a decipherment would need.

## 1. Introduction

The Indus script (c. 2600–1900 BCE) survives in about 4,500 short inscriptions, mostly on seals, with a mean of about
five signs and no bilingual. Parpola (1994) and Mahadevan (1977, 1998, 2014) built the main Dravidian case; many
other languages have been proposed. Farmer, Sproat and Witzel (2004) doubted that the signs write language at all;
statistical work since (Rao et al. 2009; Yadav et al. 2010) argued for linguistic structure without identifying the
language. This paper asks two questions: how can a proposed decipherment be tested fairly, and what does the corpus
itself establish, without sound values?

## 2. Data

- The ICIT-derived corpus distributed with the indus-website project (2,543 objects; Wells/ICIT sign numbers), with
  reading order established.
- Mahadevan's 1977 concordance (2,906 texts), mapped to ICIT numbers by aligning the texts both contain (96% of lines
  agree); 1,664 texts absent from the first corpus are used as a held-out sample.
- A fuller ICIT-derived corpus (4,578 objects), found embedded in a public website; used only locally, and not
  redistributed pending the data holders' agreement.
- CISI vol. 1 photographs; Parpola 1994 for the copper-tablet groups; Fairservis 1992 (sign identifications and a
  Dravidian key, transcribed from the page images); lexicons: Monier-Williams, DEDR, ePSD2, JAMBU (Munda), Tamil
  Lexicon entries citing Sangam works, Berger and Yoshioka (Burushaski); the Elamicon Linear Elamite corpus and
  Hallock's Achaemenid Elamite glossary.

## 3. The bench

A key maps signs to values. Readings are reduced to consonant classes with three vowel classes kept, parsed into
dictionary words (plus one case-ending consonant), and scored as the share of the text covered by words of three or
more segments. The same is done for 100–200 shuffles of the key's values within frequency bands. The key is also
scored on the copper-tablet anchors and on how it treats the numerals and endings. Controls:
(a) a planted key on a synthetic corpus beats its shuffles by about ten points; (b) a key fitted to the corpus
by hill-climbing reads about 93% of it in any language; (c) the real Linear Elamite key beats its shuffles only when
vowels are kept; (d) **the real Linear B key does not beat its shuffles in any setting** (11-41 of 100 as good), even with
the Greek list adjusted to Linear B spelling. The test therefore cannot reliably recognise a correct key: its null
results for the published Indus keys show that their reading rates prove nothing, not that the keys are wrong.

Results for published keys (vowels kept, own language): Yajnadevam 2024, 53.0% against 44.8% (10 of 100 shuffles as
good; the edge disappears without his values for the two endings); Fairservis 1992, below its shuffles; Parpola 1994,
below its shuffles. The Yajnadevam key does beat its shuffles clearly in *Dravidian* (0 of 100): a key tuned by its
author to give pronounceable syllables keeps that advantage on any lexicon of short consonant-vowel words. Beating the
shuffles is therefore necessary, not sufficient. Fitted keys also generalise to unseen texts in every language, and
with lexicons matched in size the language ranking is inconclusive (cf. Raghavendra 2026 on synthetic data).

## 4. What the texts show

(All replicated on the held-out M77 texts and on the fuller corpus.)

1. **Endings fixed per name.** A name takes the jar (740) or the arrow (520) and almost never both: 5 of 881 against a
   median 46 when the endings are shuffled among lines (fuller corpus: 9 of 1,014 against 69). An unsupervised word
   segmenter binds them to the preceding sign as suffixes.
2. **The arrow class is closed.** Names ending in a fish sign take the arrow in 61–62% of lines; names ending in anything
   identified as a person, tool, plant, building or landscape in 24 of 754. Titles such as 'he of the bow' take the jar:
   the class follows the referent, not the last word.
3. **Order.** The 'man' sign follows the jar 112 times and opens a name-and-ending text once: possessor first, head
   last (Parpola 1994 made this argument against Sumerian and Elamite).
4. **The heading** (817/820/861 + strokes) is one formula in three variants, in the same proportions at the two main
   sites (Mahadevan 1970; our earlier site effect came from a few Lothal sealings), and hardly chosen by the name
   that follows.
5. **Numerals.** Short and long strokes precede different signs (Jensen-Shannon 0.61 bits, 0 of 500 permutations), the
   split of Proto-Elamite's counting and capacity systems; the long strokes go with the pot on Harappa tablets. The
   numbers do not follow the Harappan weight system.
6. **Over time** (the excavators' periods at Mohenjo-daro and Harappa): headings and endings do not change (z = 0.0 and
   0.2 against period-label permutations); the numerals do (z = 3.7 and 3.2).
7. **Foreign names.** The 20 West Asian texts use common Indus signs (84% of tokens) but end in the jar or arrow in 11%
   of lines against 43% at home (p = 0.007), never use the heading, and only 45% of their sign pairs occur at home (70%
   for home texts): the endings belong to the Indus language, not to the script.
8. **Restoration.** 157 broken texts have an intact twin that fixes the lost sign. A grammar-only model, with every text
   containing the legible part withheld, restores it in 27% of cases at the first guess (55% within five) against 6% for
   the commonest sign; lost endings in 10 of 13.
9. **Meanings.** The copper-tablet equations (Parpola 1994) stand; two further candidates are provisional (347 with the
   multi-headed animal, 460 with a tree). Of Parpola's numeral + fish star names only 6 + fish (the Pleiades) is
   enriched (4.7–11.5 times across samples); 3 + fish is not.

## 5. The language

A two-way class suffix on the singular noun that separates persons from star names, and possessor-before-head order:
Dravidian passes both; Indo-Aryan in part; Sumerian and Elamite fail the order; Munda (whose grammars count heavenly
bodies as animate and mark animacy only by number, Hoffmann 1903) and Burushaski fail the class test. Early Tamil names
(Tamil-Brahmi) have the same shape. But the Dravidian model, asked in advance for a rational plural sign and for less
alternation in the non-rational class, got both wrong (`PREDICTIONS.md`). Witzel's (1999) alternative, a prefixing
Para-Munda language in the north and a non-Dravidian 'Meluhhan' in the south, could not be tested: his Meluhhan is a
handful of reconstructed forms, and a sound-pattern model cannot separate Dravidian from Munda in Sanskrit spelling even
for his own Dravidian loans. Outside evidence is almost nil: two probable Meluhhan names in cuneiform (Nanaza and Samar,
three tablets of one year), no further names in 223 CDLI texts, and no object with both Indus signs and readable text.

## 6. Discussion

The structure of the Indus texts is richer and more stable than a random symbol system and behaves like the morphology
of a head-final language with a two-way noun class, most compatible with Dravidian. That is a constraint on
decipherment, not a decipherment. No published key survives a test that recognises a real decipherment, and no
statistical fitting procedure can supply sound values from this corpus. The most useful contributions are therefore
negative and methodological: a public bench, validated on a real script, that any claimant can run; the demonstration
that consonant-only scoring and fitted keys prove nothing; and a list of structural facts, replicated on independent
data, that any reading has to account for.

## 7. What is new

See `DOSSIER.md` section 7 and `results/lit_check.md`. In short: much of the structural ground is earlier work
(Hunter; Mahadevan 1970-1998; Parpola 1994-2015; Wells 2006; Rao et al. 2009; Yadav et al. 2010). New here: the
per-name fixedness measurement, the closed arrow class, the class-suffix test, the numeral + fish test, the missing
endings on foreign seals, grammar against numerals over time, restoration scored against intact twins, the shuffle
bench validated on Linear Elamite, and the registered predictions (sixteen held, twenty-one failed). Wells (2006) preferred Munda
on word structure: his prefix and insertion arguments do not survive a test on the corpus (the heading is not a
prefix, there is no prefix set, insertions are attribute + head). Mahadevan (1970) said the openers have the same
proportions everywhere: he was right, and our earlier site effect is withdrawn.

## 8. Limitations

The corpus is small and the texts short; sign identifications follow the ICIT list; the fuller corpus's provenance must
be cleared before publication; Tamil-Brahmi names were taken from a scanned copy of Mahadevan 2003 whose status is
unclear; several relevant works (Wells 2011/2015, Fuls, Mahadevan 1986, Parpola 2015) were not read in full; the
analysis was done with an LLM (Claude), and every step is recorded in `indus/NOTES.md`.
