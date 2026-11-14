# neufville1779: Jean de Neufville's syllabic code with Baudouin, Sartine's secretary (Amsterdam-Paris, 1779-1780)

Status: in progress (read in part; folder only, no site page; Daniel is free to write the page or change anything here).

## What it is

The papers of the Amsterdam merchant Jean de Neufville (Jean de Neufville & fils), bound in the Department of State and now
in the Papers of the Continental Congress (National Archives, Record Group 360, microfilm M332 roll 4; free images in the
National Archives Catalog, file unit 464816476; see sources.md), hold a private correspondence in a numeric code:

- **de Neufville's drafts, April-May 1779** (pp.591-609), headed "Mad. d'Arras" or "Chaumont": plain French with code
  numbers written over the syllables (pp.599-603, 606, 608, 609), and one enciphered fair draft (pp.604-606) of the
  letter of 19 April 1779 whose plain text is on p.599;
- **letters from Paris, February 1779 to November 1781** (pp.487-590), addressed to "Monsieur Van Temmel chez Monsieur
  Jean de Neufville, négociant à Amsterdam", signed "Baudouin" and later "Dunoyer", with code groups inside clear
  French; de Neufville wrote the French over many of the groups (pp.516-548, 579), but not over all.

The code: numbers 1 to about 550, one number per letter, syllable, common word or name, with several numbers for common
units (re = 30, 229, 310; que = 22, 23, 278; les = 427, 428, 429). Names include 5 and 106 Le Ray de Chaumont, 529
Vergennes, 328 the Minister of Marine (Sartine), 444, 511 and 213 the Pensionary of Amsterdam, 508 the Stadholder, 500
Mr York (Sir Joseph Yorke), 550 the Ambassador and 417 La Vauguyon, 531 the Spaniards, 464 the States General, 103 the
Amsterdammers, 174 and 169 America, 346 and 347 France, 368 Martinique. key/key_entries.tsv gives every entry and its
source.

## Who read what

- **Jean de Neufville** made the code: Baudouin writes on 30 March 1779 (p.516) that he has received "la lettre ... avec
  le chiffre qui y étoit joint et que j'ay trouvé à merveille". De Neufville enciphered his own letters from his plain
  drafts, and wrote the plain French over many of Baudouin's groups. Those parts were read by him in 1779-1780.
- **Baudouin** read de Neufville's letters in the code (the sent letters are not in this file).
- **The Department of State's clerk** who bound and indexed the volume in the 19th century read the signatures and
  covers (index, below). Fold3's indexers listed the drafts as "Letters from William Lee to John de Neufville and Son ...
  in French with cipher".
- **What this folder adds** (Andrew Beling, with AI agents, 13-14 Nov 2026):
  - the reconstruction of the code from de Neufville's drafts and the glosses;
  - the identification of "Dunoyer" as Baudouin from the leaves;
  - the reading of the bare passages that no one glossed (B573, B491, B492);
  - two blind transcription passes of each bare passage.
  No second agent and no person has rechecked it.

## Identification of the correspondent (checked on the leaves)

- pp.495-497, Paris 25 February 1779, and pp.498-499, Paris Monday 7 March 1779, are signed **"Baudouin"**. The second ends:
  "à l'avenir je signeray un des noms que je prends dans le petit chiffre cy joint".
- From 30 March 1779 the letters in the same hand are signed "Dunoyer"; the covers to "Van Temmel" are docketed "Baudouin".
- The volume's index (p.3, 19th-century hand) reads: "12. Thirty-five . . . Du Noyer, Bowdoin or Mad. D. Arras (Private
  news from Paris, for use U.S. 1779-81.)", folio 148.
- Baudouin is Sartine's secretary at the Ministry of Marine: Papers of Benjamin Franklin 29:5-7, note 4 to Dumas's letter of
  1 March 1779 ("'Baud——' for Sartine's secretary Baudouin"); Baudouin's own notes to Franklin, 5 and 25 May 1779 (PBF 29:438).
- "Mad. d'Arras" as a cover for the same man is an inference, from the index and from the same code being used in both
  directions. It is not stated on any leaf.

## The tests

Each key was frozen (key/FREEZE.txt) and its test plan written (TEST_PLAN.md) before it was run.

| Test | Key | Result | 200 shuffled keys |
|---|---|---|---|
| T1: predict pp.604-605 from drafts pp.600-603, 609 only | K1, 139 numbers | 139 of 146 covered groups as in the writer's draft p.599 | mean 1.8, max 15 |
| T2: ten p.599 pairs held out | K1 + other p.599 pairs | 8 of 10 | mean 0.21, max 3 |
| T3: the whole 6 May 1779 draft (p.608) held out | K2, 170 numbers | 64 of 65 covered groups (the miss: 106 "Chaumont" for "M. de Ch.") | mean 0.6, max 7 |

The misses in T1 and T2 are the writer's own variants (86 ne/na, 263 i/j, and the word "ménagera", which p.599 glosses
96 86 36 92 = mé na ge ra while his other drafts use 36 = ra, 92 = la).

Statistical validation (docs/_validate.py, validation.tsv: the drafts' own plain units plus the bare passages read with
key_full_r3): pass, z 9.1 against random keys, 4.1 against refits to shuffled text.

## The bare passages

Decoded with key/key_full_r3.json (204 numbers). In the readings, [n] marks a hole and {x} a unit settled by the word, not
by the key.

**B573, "Dunoyer" (Baudouin) to "Van Temmel" (de Neufville), 24 January 1780 (p.573).** 43 numbers, 39 read (91%).
"Il est certain que le patriarche et la bande joyeuse feront tous leurs efforts pour faire avaler la dernière pilule,
mais ... cela couvrira **les États Généraux** d'opprobre et de ridicule. Il y a longtemps que [3] **a retiré aux
[58]rands** l'affaire de **l'emprunt** ... d'ouvrir **un emprunt** où personne ne se soucie de **[227]er son ar{g}ent**,
cela ne peut que faire beaucoup de tort **au crédit du [349]**." He then advises de Neufville to speak to "M. du Fresne".
- In English: the pro-British party will make the Republic swallow the last pill, to the shame of the States General.
  Someone [3] long ago took the loan business away from the [58]rands and gave it up when de Neufville met obstacles. A loan
  nobody will put money into only hurts the credit of [349].
- Open numbers and candidates (holes in the text):
  - 3: a person. The only gloss of 3 is the numeral 3 (p.529), which does not parse here.
  - 58: an initial. "Grands" (the Grand bankers) fits if 58 = G, and so does 30 = g in B492 "{G}rand".
  - 227: "plac-", "hasard-" or "risqu-".
  - 349: "Congrès".
- 30 is read "g" here because the word "argent" forces it; in de Neufville's drafts 30 is "re". So 30 is either a homophone
  or a writer's slip.

**B491, the same to the same, 18 January [1780] (p.491).** 18 numbers, 12 read (67%; 86% if the four likely nulls are left out).
"Je pense absolument comme M. Leerding sur le compte du **Stadhouder** [507] [501] [405 387 390 447] **Stadhouder** ...
il se pare **à la cour** de son savoir-faire et de ses succès, qu'il ne doit qu'à **Monsieur le Pensionnaire des
Amsterdammois**."
- Pass 2 (from the end backward) corrected one number of pass 1 (206 to 204, "le").
- 405, 387, 390 and 447 are probably nulls. Each occurs in de Neufville's fair draft pp.604-605 only at places where his
  cipher has a number with no counterpart in his own plain draft, and none has a reading anywhere in the file. This is
  evidence, not proof.
- 507 also heads both unglossed lines of p.527, struck through by the writer each time, and 501 is unglossed on p.529.
  Both are open.

**B492, second page of the same letter (p.492).** 7 numbers, 5 read (71%; one unit by the word only).
"On a déjà proposé plusieurs fois à ma tante d'acheter son [143] ... il y a certainement du tripotage au sujet de **ce**
[162] entre V. Vort et **{G}rand**."
- The gloss over 143 on p.534 may read "vaisseau(x)", but it is too faint to enter in the key; 143 stays a hole.
- "Ma tante", "le saint homme", "V. Vort", "le patriarche", "l'ami du cœur" and "M. du Fresne" are covers used in clear.
  Du Fresne is Chaumont: de Neufville glossed "Mr de Fresne" with "Chaumont" on p.579. The others are not identified.

**B527, two unglossed lines in the letter of 9 April 1779 (p.527).** Decoded to syllables but not read.
- Line 1: "[327] [441] ca do s s", followed in clear by "sucre brut et blanc, caffé &c.". "cadeaux" is possible but not
  forced.
- Line 2: "Vergennes [400] fi su ca in in s ta", followed by "au surplus". It does not parse.

## Inventory of the file (all 808 images checked at readable size)

Code numbers occur only on pp.487-609. Classes:
- (a) de Neufville's drafts with numbers over the French: pp.599, 600-603, 604-606, 608, 609. About 1,100 numbers.
- (b) Baudouin's letters glossed by de Neufville: pp.516, 526-528, 529, 530-531, 534-535, 547-548, 579. About 380 numbers.
- (c) Bare: pp.491-492, the two lines on p.527, p.573. About 90 numbers.

What this folder contains of each:
- the (a) items as aligned pairs: transcriptions/p604-606_cipher_with_p599_draft.tsv, key/heldout_p608_truth.tsv,
  key/key_source_pairs_pp600-603_609.tsv;
- the (b) glosses as pairs: key/key_pairs_classB_glosses.tsv. The glossed letters are not transcribed in full, and
  doubtful glosses were left out;
- every (c) passage in full: letters/B*.

p.504 is de Neufville's list of four signal numbers. 7, 8, 14 and 15 mean "Spain will declare the independence of America",
"... will go to war with England", "... will make the general peace" and "Spain will stay quiet".

## History and significance

Kept apart: what the letters say; established history, with the reference checked in this work; and inference.

**What the letters say.**
- De Neufville was passing Paris news to the Pensionary of Amsterdam. Baudouin was asking about Spanish intentions, the
  Amsterdam Pensionary and the French ambassador, and he advised on de Neufville's dealings with Chaumont ("M. du Fresne").
- In January 1780 Baudouin judged that the American loan de Neufville was trying to raise in Amsterdam would harm "the
  credit of [349]", and that the pro-British party would make the States General swallow a humiliation.
- De Neufville's draft of 19 April 1779 reports that he passed news of Spain to the Pensionary and could not yet sound
  him about a direct correspondence.

**Established history (checked here).**
- In September 1778, at Aix-la-Chapelle, de Neufville negotiated a plan of a treaty of amity and commerce with William Lee,
  acting for the Pensionary and burgomasters of Amsterdam. His 1792 petition to Congress for compensation was rejected on
  Jefferson's report of 26 November 1792 (Papers of Thomas Jefferson 24:664-667, which cites Schulte Nordholt, *The Dutch
  Republic and American Independence*, 1982, pp.64-69).
- The pro-American Pensionary of Amsterdam was Engelbert François van Berckel ("notre ami" in Dumas's letters). The
  French ambassador at The Hague was the duc de La Vauguyon, the British ambassador Sir Joseph Yorke, and the Stadholder
  William V was generally pro-British (PBF 29:5-7 n.4).
- John Paul Jones's squadron lay in the Texel in October-December 1779. Yorke demanded the Serapis, and de Neufville & fils
  supplied the squadron. This file holds the letters (pp.127-345, among them Yorke's memorial of 8 October 1779 at p.299).

**Background not checked in this work.**
- Spain entered the war in June 1779.
- The British seizure of the Dutch convoy under Bylandt on 31 December 1779 - 1 January 1780 is very probably the "last
  pill" of B573.
- De Neufville's loan for Congress in 1780-81 failed. Van Winter's *American Finance and Dutch Investment* was not
  consulted.

**Inference.** A merchant's private code channel into the office of the Minister of Marine shows the French ministry
using an Amsterdam banker to work on the Amsterdam regents beside, and perhaps around, its ambassador. The letters'
worry about La Vauguyon's "confidences" (p.526 glosses) points that way. This is a reading of a few letters, not a
finding of the literature.

## Provenance (how the papers reached the government)

- **Documented:** the volume, with the index page "Diplomatic Letters" cross-referenced to "Dep. Correspondence Vol. II", was
  bound with the Continental Congress papers in the Department of State. Jefferson's 1792 report says he "examined the
  records of the Department of State". The National Archives Catalog gives no accession note. Butler's *Index to the
  Papers of the Continental Congress* (1978) indexes "Van Temmel".
- **Conjecture:** the papers came in with de Neufville's own claims, his 1792 petition or his widow's of 1797. They may
  also have been handed over earlier as intelligence "for use U.S.", as the index puts it. Neither route is documented
  here. The Journals of Congress and the American State Papers (Claims) were not searched.

## In print

Nothing of this correspondence, its content or its code was found in print.
- Founders Online: "Neufville Baudouin" finds only Dumas's letters with the abbreviation note; "Dunoyer" and "Temmel" find
  nothing relevant.
- HathiTrust full text: "Van Temmel" Neufville finds only Butler's index. Wharton's *Revolutionary Diplomatic
  Correspondence* is full text there, and it does not match.
- Cryptiana: nothing found.
- Schulte Nordholt and van Winter are in copyright and were not read.

## Remaining gaps

- Numbers 3, 58, 227, 349, 507, 501, 143 and 162, the two lines of p.527, and the likely nulls 405, 387, 390 and 447.
- The glossed letters pp.516-548 are transcribed as pairs only.
- Baudouin's letters of February 1779 to November 1781 (pp.487-590) contain more clear intelligence that is not
  summarised here.

## Escalation

Tried for the open numbers:
- every glossed letter and draft in the file (all 808 images paged);
- the code's own thematic neighbours (names sit at 500-550, but there is no alphabetical run that settles 3, 58, 227 or 349);
- Founders Online, HathiTrust full text and Cryptiana.

Not tried:
- the Archives nationales Marine series (B4, B7) or Sartine's papers, where Baudouin's office copies or de Neufville's
  sent letters may survive;
- Dutch archives (the Stadsarchief Amsterdam's van Berckel papers).
