# Catherine de’ Medici to Paul de Foix
PROPOSED PARTIAL DECIPHERMENT  |  PRELIMINARY REVIEW 1.0

Four encrypted extracts in British Library Add MS 4136, ff.148v-149 (DECODE R9241), copied under 15 January 1563. Prepared 3 October 2026 from research audit v0.9 / source-key v13. [S1-S3]

**Lawrence Beck, with the assistance of ChatGPT**
Photographs, prior source identification and earlier transcriptions: Daniel Bourdeau.

### Finding offered for independent checking

A proposed mixed substitution/nomenclator key produces connected French in all four extracts. The most substantial completed clause concerns an apparent intention to induce expenditure and the speaker’s stated lack of intention to make it. The current key, source groupings and reading remain provisional. [S3]

> que son but seroit de nous faire entrer en quelque debourssement de deniers, dont nous n’avons nule intention

*“That his aim would be to draw us into some expenditure of money, which we have no intention of making.”*

The clause covers source positions D1:13-D4:12: 75 recorded units producing 90 letters. No extra plaintext letters or occurrence-specific overrides are used within this clause. That establishes a consistent reading under the proposed key, not independent authentication of the key or handwriting. [S3]

### What is not claimed

No complete decipherment of any of the four extracts; no authenticated original key or matched independent plaintext; no independently verified completion percentage; no first-decipherment priority; and no identification of the people discussed inside the encrypted passages.

The source/key mapping is unchanged from the last accepted research reading. Audits v0.8-v0.9 added tests and source leads, not new plaintext. This report consolidates the result for review rather than announcing a further break. [S3]

## The witness and the working method
SOURCE, SCOPE AND ACCOUNTING

### A copied set of extracts, not two complete letters

The target begins below the rule on the first supplied photograph (folio marked 148v) and continues through numbered extracts (2), (3) and (4) above the lower rule on the second photograph (folio marked 149). Material elsewhere on those pages belongs to other correspondence. The A-D labels and source IDs are modern research identifiers. [S1-S2]

The copied heading identifies the Queen Mother, M. de Foix in England and 15 January 1563. The date is retained as written; no modern redating or inferred speaker identification is adopted. The wider catalogue item also includes separately deciphered Coligny material, which is outside this contribution. [S2]

### How the partial reading was developed

The recorded investigation combined computational candidate generation, comparison with Bourdeau’s earlier transcriptions, inspection of the supplied photographs, and testing of fixed sign values in different contexts. Distinctions among similar-looking signs and recognition of multi-letter or word-valued entries supplied the later advances. No matching historical key or exact plaintext counterpart was obtained. [S2-S3]

Each current source label has one fixed expansion: a letter, several letters, a proposed null, or an explicit unknown. The working description is homophonic substitution with nomenclature. It is not a demonstrated universal rule that a particular crossbar, crown or capital letter must indicate a word or a null. [S3]

| Current category | Label classes | Occurrences |
|---|---|---|
| One-letter proposals | 49 | 869 |
| Multi-letter proposals | 20 | 90 |
| Candidate nulls | 8 | 47 |
| Explicit separator | 1 | 7 |
| Unassigned | 18 | 25 |
| Total | 96 | 1,038 |

These are transcription-accounting totals, not the proportion of correct plaintext. The current 1,038 units preserve all 1,041 source origins from v9; regrouping changes the current count. Assigned signs still produce malformed words. [S3]

### Limits of the evidence

Image review was informed by the emerging French, not blind or independent paleographic review. Several numerical scoring tests did not rank the adopted readings first. The source appearances and connected grammar, with contrary cases retained, form the basis of the proposals. Replay and hash checks cannot establish historical correctness. [S3]

## Three reproducible readings
ANCHORS AND THEIR DEPENDENCIES

### 1. Opening of extract A

> Et en ceste uisitation passerent entre eulx quelques ...

*“And during this visit, there passed between them some ...”*

A0:1-A2:11: 43 units, 45 emitted letters. This is an opening fragment; the following noun phrase remains unread. It uses proposed nulls and multi-letter entries, including the repeated que expansion. [S3]

### 2. Judgment of the intention

> L’intention, ie la vous laisse a iuger.

*“I leave it to you to judge the intention.”*

A6:25-A7:20: 25 units, 30 emitted letters. The g in iuger follows a source reclassification to the crossed-4 family. The ie value remains proposed; whose intention is being discussed is not established. [S3]

### 3. The financial clause

D1:13-D4:12, quoted at the start of this report, relies particularly on these shared entries. All applicable occurrences are published, including the incomplete ones. [S3]

| Proposed entry | Every occurrence | Evidence limit |
|---|---|---|
| H_BAR_WORD = faire | C1:10; D2:4 | Two grammatical settings; the C noun remains unread. |
| Z_CROWN_WORD = nous | D2:3; D3:15 | Object and subject uses; same proposed crowned family. |
| VEE = ont | C0:2; D3:14 | Both follow d to form dont; repeats the same word. |

Bourdeau’s earlier transcription distinguished the certain hb and zt shapes before these plaintext values were proposed. That supports the graphical distinction, not the meaning. The uncertain hb? lookalike in B6 was checked separately and was not forced into the faire family. [S2-S3]

The financial clause also uses inherited nulls at D1:23, D2:5, D3:23 and D4:2. They remain source positions with empty proposed expansions, not silently removed observations. The complete token proof is in data/claims.json. [S3]

**Interpretive limit:** seroit is conditional. The passage does not identify a bribe, a formal payment demand, a completed transaction or the person concerned. [S3]

## Critical reading: extracts A and B
PROPOSED FRENCH AND ENGLISH WITH THE SAME GAPS

**Conventions.** [gap] and [literal ...] retain unread or malformed text; [26] and similar numbers remain unresolved code labels. * marks tentative values. [RX?] identifies the disputed global RX assignment. {word?} is an editorial restoration, not literal output. Spacing, punctuation and English syntax are editorial. [S3]

### A - French

Et en ceste uisitation passerent entre eulx quelques [gap: prolizgnaulx] des termes ou questions* de la paix [gap: de la quelmme il a assez cgnoistre]. Il a tousiours eu envie de se meler* ou pour le [DAMAGE_A6_9] moins estre de la partie*. L’intention, ie* la vous laisse a iuger, aiant [40] [gap through A9:20].

Le personnaige* que* vous scavez assez, et en somme [RX?] [literal pruoiant], que la negotiation pr[DAMAGE_A11_18]end quelque traict duquel [literal in] sentira une partie* de l’incommodite [RX?], s’est laisse entendre et que [unresolved syntax] infinies foiz [gap through A14] peust auoir [34] de faueur que [gap through A16:16] il esperoit [gap] promptement la reconciliation necessaire entre ces deux {royaulmes?}.

### A - English

And during this visit, there passed between them some [unread wording] concerning the terms or questions* of peace [unread wording]. He has always wanted to get involved* or, at least [damaged position], to take part*. I leave it to you to judge the intention, having [40] [unread wording].

The person* you know well enough, and, in sum [RX?], [unread word, pruoiant], that the negotiation [damaged verb] some course or development, from which [unresolved pronoun, in] will feel part* of the inconvenience or disadvantage [RX?], has let it be understood [subject and clause attachment unresolved], and that [unread syntax] countless times [gap] could have [34] of favour [gap], he hoped [gap] promptly, the reconciliation necessary between these two {kingdoms?}.

### B - French

Auecques grande abondance [gap in the langai... M_SWASH cluster] la dexterite de son esperit ... essaie de tirer de moi les moiens et le [literal cresin, unresolved] que i actendoie de lui, lequel ie* scai n’estre ignorant de tout ce qui* est passé. Et toutesfois il n’en eut autre cose sinon ce que vous a esté ia [34] escript.

### B - English

With great abundance [gap], the dexterity of his mind ... tries to draw from me the means and the [unread noun] that I expected from him, whom I know not to be ignorant of everything that* has happened. And nevertheless he obtained nothing other than what has already been [34] written to you.

The B ending depends on grouping two signs as 34. The separate-sign rival produces srescript; rescript/prescript remain different conjectural repairs. No meaning for 34 or completed noun for cresin is supplied. [S3]

## Critical reading: extracts C and D
THE CONNECTED FINANCIAL CLAUSE AND UNRESOLVED CONTEXT

### C - French

Dont* ie* ueoi [26] qui* seroit [26: proposed grouping] aise de faire* son [literal prou[N_MONOGRAM]ice, noun unresolved] de ce roiaulme [unresolved aie] la lui feiz ie* [26] entendre pour lui oster ceste {esperance?}.

### C - English

From which* I* [verb ueoi, not settled] [26], who/which* would be [26: grouping uncertain] pleased to make* his [noun unresolved] of this kingdom [unresolved words and pronoun attachment]. I made him [26] understand, in order to take this {hope?} from him.

The later audit notes that ie ueoi may represent je veoy, “I see,” as a spelling interpretation. It is not a new cipher value or a determination of 26. The original extra r remains in ersperance, and N is not expanded to ff in the literal key. [S3]

### D - French

[37] r [70] est [10] ie* n’en [DAMAGE_D0_13] espere riens et [literal ueti] [26] que son but seroit de nous* faire* entrer en quelque debourssement de deniers, dont* nous* n’avons nule intention.

Vous uerez si la dessus vous pourrez aprendre quelque chose* et m’en [literal aduertdrez alssi, unresolved] de [70] ce qui* se sera [literal r[N_MONOGRAM]ert, unresolved] depuis le partement* du [10] [literal de marissriuere, unresolved name-like ending].

### D - English

[Unread opening code sequence] I* [damaged position] expect nothing from it. And [unread wording, including 26] that his aim would be to draw us* into some expenditure of money, which* we* have no intention of making.

You will see whether, on that matter, you can learn something*, and [verb unresolved] [malformed connective] about [70] what* will have [verb unresolved] since the departure* of the [10] [unread name-like ending].

### What this supports

The connected money clause links a described conditional aim with a statement of the speaker’s lack of intention to make the expenditure. The surrounding instructions, referents and final name-like sequence remain unresolved. The first-person pronouns do not, by themselves, establish whether a speaker is Catherine or someone quoted in omitted context. [S3]

No fluent reconstruction of either whole extract is promoted into the literal edition. All 41 literal lines, including failures, appear in the appendix and machine-readable files.

## Unresolved readings and reviewer questions
CONTRADICTIONS ARE PART OF THE SUBMITTED RESULT

| Problem | Current position | What remains open |
|---|---|---|
| RX | Global mm preferred; global l rival supplied | mm reads en somme/incommodite but leaves quelmme. l repairs de la quelle and damages the other two contexts. No local override. |
| 26 | Four preferred groupings; no value | bien, aussi and assez remain candidates. C0 compound-126 and C1 separate-sign interpretations survive. |
| 34 | Two preferred occurrences; no value | B7 grouping gives [34] escript; separate signs give srescript. tant/bien/autant/plus are not adopted. |
| 70 and 10 | Unassigned, twice each in D | tout and sieur are conjectures. The name-like ending does not establish a person. |
| M and N | Different monograms, neither assigned | N=ff still yields prouffice/rffert, requiring two further source interventions for the guessed words. |
| Ordinary signs | ueoi/ueti, cresin, aduertdrez, alssi | Close image checks did not establish the convenient corrections. Period spelling and copying error remain alternatives. |
| Marked signs / nulls | ZBAR heterogeneous; TF/MM proposed nulls | The broad null rule repairs esperance but damages vous uerez. Narrower or control rules are not established. |

These are recorded limitations, not proof that the remaining words are unrecoverable. A second manuscript witness, matched key or better source classification could alter the result. [S3]

### Questions that would materially help

**Source audit:** Do the hb/zt distinctions supporting faire/nous hold against the original images, including lookalikes in readable passages? Can the RX and marked-sign groupings be independently confirmed or corrected?

**Code boundaries:** Are the proposed 26/34/32 groups numerals or adjacent alphabetic signs? Can a consistent entry be established without repairing its neighbouring letters to fit?

**Documentary evidence:** Is there an earlier decipherment, a recipient’s copy, an original dispatch or a demonstrably related key? The 1565 de Foix leaves and Potter-associated letter are precise leads, not inspected matches. [S4]

## Reproduction, credit and submission scope
A REVIEW CONTRIBUTION, NOT A SOLVED-TARGET UPDATE

### Self-contained checks

From the contribution directory, use Python 3 with its standard library. No private images, network access or old nested checkpoint is required for the public replay checks.

```text
python scripts/verify.py
python scripts/decode.py
python scripts/decode.py --span D1:13 D4:12 --tokens
```

The checker compares hashes; replays the proposed key; verifies all 41 lines, 1,038 current units and 1,041 v9 origins; checks 25 unresolved occurrences; reconstructs the three anchor spans and the RX=l rival; and derives the complete key register and token replay from every recorded occurrence. It is not a discovery solver or a test of historical truth.

### Photographic review without public image redistribution

Run the verifier to generate review.html, a local label/expansion ledger. Use data/line_coordinates.json with separately obtained source photographs. The viewer contains no source images and does not contact a server. No manuscript photographs or crops are included in the public report.

This omission reflects the project’s unestablished image-redistribution rights. It also means that the public files alone cannot authenticate the handwriting. Daniel already supplied the source photographs; other reviewers require their own authorized access. [S1]

### Attribution and integration

Lawrence Beck initiated and directed the project. ChatGPT performed the source comparison, computational work, candidate development, translations and drafting described in the research checkpoints. Daniel Bourdeau supplied the photographs, prior source identification and earlier transcriptions. No independent reviewer has endorsed this result. [S2-S3]

The proposed contribution adds only targets/foix1563/beck-preliminary/. It does not alter existing research, Coligny’s separate result, catalogue measures, the solved status or the live website. SITE_NOTE.md supplies optional introductory wording for the maintainer after review. Work on the remaining cipher continues.

### Source register

**[S1]** British Library Add MS 4136, ff.148v-149; DECODE R9241; photographs supplied by Daniel Bourdeau. Exact file hashes and dimensions: data/provenance.json.

**[S2]** Bourdeau, targets/foix1563/NOTES.md and earlier transcription files. Connected repository checked 3 October 2026; NOTES blob 3f4c8db8670fdae7d3d66f022d65922e5782e962.

**[S3]** Supplied Catherine research checkpoints, principally v0.6-v0.9; frozen public source/key copied from v13. The original v0.9 verifier was rerun during preparation and returned PASS (32 checks).

**[S4]** Uninspected counterpart/key leads: BnF Francais 15971, ff.21 and 26 (de Foix, 11 October 1565); Potter (2019), DOI 10.1017/S0960116319000289, notes 204-205 and author-upload listing. Full URLs, access distinctions and source genealogy are in SOURCES.md. No values are transferred from these leads.

## Appendix: complete literal replay
NO WORD DIVISION, SILENT REPAIR OR FLUENT GAP-FILLING

This is the fixed-key output copied unchanged from audit v0.9 / source-key v13. Square brackets retain unknown labels. Candidate nulls and separators emit no letters here but remain explicit in data/source.json and the token ledger. Source line breaks are preserved. [S3]

```text
A0 etenc
A1 esteuisitationpasserenten
A2 treeulxquelquesprolizgnaulxde
A3 stermesouquestionsdelapaixd
A4 elaquelmmeilaassezcgnoist
A5 reilatousiourseuenuiedeseme
A6 leroupourle[DAMAGE_A6_9]moinsestredelapartielinte
A7 ntionielavouslaisseaiugeraiant[40]
A8 leseaulx[20]ancemensdelaiuejeeti
A9 ouedurantnoztrouble[COLON]lepersonna
A10 igequevousscauezassezetensommepruoian
A11 tquelanegotiationpr[DAMAGE_A11_18]endquelquetraic
A12 tduquelinsentiraunepartiedelinco
A13 mmoditesestlaisseentendreetquein
A14 finiesfoizquesionuoulrigniuiret[82]
A15 peustauoir[34]defaueurquedesineramoii
A16 [MINIM_UNCERTAIN_A16]lauoitmoienluquelilesperoitis
A17 ortirpromptementlareconciliat
A18 ionnecessaireentrecesdeuxroial
A19 lmes
B0 auecquesgrandeabon
B1 dancedelangai[SWASH_2]ea[CAP_D_BOWL]ompain[DAMAGE_B1_23][M_SWASH]del
B2 adexteritedesonesperitessaied
B3 etirerdemoilesmoiensetlecresinquei
B4 actendoiedeluilequeliescainestre
B5 ignorantdetoutcequiestpasseettou
B6 tesfoisilneneutautrecosesi
B7 noncequevousaesteia[34]escript
C0 dontieueoi[26]quiseroi
C1 t[26]aisedefairesonprou[N_MONOGRAM]icedeceroiau
C2 lmeaielaluifeizie[26]entendrepour
C3 luiostercesteersperance
D0 [37]r[70]est[10]ienen[DAMAGE_D0_13]esperer
D1 iensetueti[26]quesonbutseroit
D2 denousfaireentrerenquelquedebourssem
D3 entdedeniersdontnousnavonsnu
D4 leintentionvousuerezsilade
D5 ssusvouspourrezaprendrequelquecho
D6 seetmenaduertdrezalsside[70]ce
D7 quiseserar[N_MONOGRAM]ertdepuislepartem
D8 entdu[10]demarissriuere
```

The full proposed key, every occurrence, qualitative evidence notes, all three anchor proofs and complete French/English reading layers are supplied as separate version-control-friendly files. RX retains a separate complete l-valued replay; the preferred text above does not conceal its A4 contradiction.

## Repository transport note

The full source is stored losslessly as data/source.seed.xz. The decoder and verifier reconstruct data/source.json and verify its original SHA-256. Derived review.html, KEY_REGISTER.md, data/key_register.json and results/token_replay.json are generated locally, not separately stored. All research source observations, key values, evidence notes and reading layers are preserved. This is packaging, not new decipherment.
