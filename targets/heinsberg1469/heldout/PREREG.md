# PREREG — Heinsberg 1469 (cat. Daniel n° 1618, ar-776), LAV NRW Abt. Rheinland, AA 0582 B 2, fol. 120-121
Agent Opus 5.5, 17/11/2026. Written BEFORE any key search, frequency statistic on signs, or decoding.
Done before: blind pass A (sub-agent, travail/passeA) and blind pass B (second sub-agent, travail/passeB), copied to
transcription/. The orchestrating agent looked at the images of both letters while preparing crops (it noticed only
that both letters open with the same two cipher words) and read pass A; it made no decoding.

## 1. Portions
- Training T = letter 1, fol. 120r-v (36 + 12 cipher lines): pass A 2299 signs, pass B 2242. All key search on T only.
- Held-out H = letter 2, fol. 121r (10 lines): pass A 372 signs, pass B 359 (>= 300). No statistic, decoding or
  "reading by sense" of H before the measure. H is frozen under both transcriptions (lines "L2 01".."L2 10" of
  TRANSCRIPTION-A.txt and TRANSCRIPTION-B.txt, SHA below).
- Known shared formula: H line 1 words 1-2 equal T line 1 words 1-2 (seen on the images, not decoded). They are kept in H.

## 2. Normalisation (fixed now)
Pass B codes mapped to pass A codes: Q->B, B->B, D->m, G->g, N->U, E->Le, F->L, 3->3. Then for both passes:
a, E (small o-variants of A) -> o ; b -> B ; F -> L ; "Le" -> E (one sign) ; {del:..} removed ; {ins:..} kept in place ;
marks - / . = removed inside a word (hyphen-joined parts and "="-continued line ends form one word) ; [x|y] -> x ;
"?" kept as unknown (decodes to "#", never in the lexicon).

## 3. Key
Table sign -> value (letter, letter group, or "" for a null), fitted on T only. Possible further merges of signs (e.g. L/I)
decided on T only and written in KEY.tsv. KEY.tsv, the lexicon file LEX.txt and measure.py frozen together by SHA-256
(KEY.sha256) BEFORE the measure.
Gate: T decoded must read as Rhineland German (Ripuarian / Lower Rhine) over >= 3 consecutive lines; else no measure.

## 4. Lexicon (LEX.txt)
LEX = (a) the hand list below, fixed now, before any decoding, plus (b) every decoded word of T (both passes) that the
reading of T accepts as a word (letter 1 only; nothing from H). Matching after: lowercase; v->u, j->i, y->i;
w kept; doubled letters NOT collapsed.
(a) ind inde inne unde und ende de der die dat den dem deme des van vanme vamme zo zu ze tzo up op uf uff in an ane
mit mijt myt ure uwe uwer uwen uch uns unse unsen unser unsme wir wi ir ich he hee hey si sy it et is ist sin syn sijn
sint synt hain haint hait hant han heit hedde hadde sal sall sullen solen sult salt wilt wille willen wil mogen moegen
kunnen konnen niet nyet neit nit nyt ouch och as als also alsus so wat wie wa wan want dan doch noch of off ader eder
bis biss vur vor vore na nae umb om ummer ever mer me nu hie hier dair dar dae daer daromb darumb wail wale gude gut guet
gelt gulden schult schoult brief breve brieve here heren herre grave greve lieve lieven lieue getruwe getruwen gunst
gruss gruys groit groiss dage dach dages tzijt zijt jair jaire sente sint datum anno domini gegeven geschreven under
onder uber over alle allet al eyn ein eyne eynen eyns eyme gein geyn sachen sache saichen saiche lude luden man mann
wort worde schriven laissen laist laiss doin doen deit doit gedain sagen seggen gesacht wissen weist weten heynsberg
heinsberg nassauwe sarbrucken johan johann russebruch hucking huckinck gulich colne coelne aiche aken were wer weir
wurde werden worden wirt weirt kein mynen myn mijn sich sie sij selve selven mallich yeman nyeman ander anders
## 5. Measure (ONE, on H, both passes)
decode H with the frozen key; each H word -> decoded string; S = (sum of lengths of the decoded H words found in LEX) /
(sum of lengths of all decoded H words). Computed for H-passA and H-passB.
200 controls: same table with the values permuted among the sign entries (Python random, seeds 1..200), same H, same LEX.
SUCCESS iff for H-passA AND H-passB: S >= 0.85 AND S >= max(controls) + 0.30. PARTIAL if 0.50 <= S < 0.85 with margin
>= 0.30 on both. Otherwise FAILURE. H is spent in every case.

## 6. After
Reading by sense of both letters (Daniel's 95 % rule, strict count: sure / {probable} / [restored] / <unresolved>),
English translation, then PR (text only; no image or derivative).
