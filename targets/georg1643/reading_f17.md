# D 4 Nr. 113/9 fol. 17r: the councillors at Giessen to Landgrave Georg II, Giessen, 18 Nov 1643 - the two cipher blocks

Source: HStA Darmstadt D 4 Nr. 113/9, image `hstad_d_4_nr_113--9_015.jpg` (right page, fol. 17r), via the DDB record
TCBURTSGQ4OBSTU5J46D5KLXPGENSYUE. Cipher: `c_f17.txt` (216 groups). Key: `key_f17.json`. Raw decode: `decode_f17.txt`
(`python3 scripts/decode_f17.py c_f17.txt key_f17.json`). The clear text around the blocks is summarised in NOTES.md.

Word division, capitals and punctuation are added; spelling is the decode's. The one code sign is given as
`[?Landgraf Johann]`, its probable value from the writer's margin note; it counts as a hole.

## Reading

zu ewerer fürstl. gn. es sich eilends wider hinaus gen Darmstatt erheben und mit ihro von ainigen wichtigen und
erheblichen puncten persönlich comuniciren.

dero herr bruder [?Landgraf Johann] übermorgen montags abends, gelibts gott, bey ewr fürstl. gnad. zu Darmstat anlangen
werden.

## Line by line

| line | cipher (groups) | decode |
|---|---|---|
| 17.1.1 | 39 34 12 33 12 28 12 28 9 34 28 26 8+ 13 : 20 23 : 12 26 14 5 16 12 14 13 12 23 17 26 | zu ewerer furstl: gn: es sich eilends |
| 17.1.2 | 33 14 17 12 28 16 14 23 10 34 26 20 12 23 17 10 28 24 26 8+ 10 32 12 28 16 12 11 12 23 | wider hinaus gen darmstat erheben |
| 17.1.3 | 34 23 17 24 14 32 14 16 28 30 31 30 23 10 14 23 14 20 12 23 33 14 5 16 8+ 14 20 12 23 | und mit ihro von ainigen wichtigen |
| 17.1.4 | 34 23 17 12 28 16 12 11 13 14 5 16 12 23 29 34 23 5 8+ 12 23 29 12 28 26 30 23 13 14 5 16 | und erheblichen puncten personlich |
| 17.1.5 | 5 30 22 34 23 14 5 14 28 12 23 | comuniciren |
| 17.2.1 | 17 12 28 30 16 12 28 28 11 28 34 17 12 28 Z\| 34 11 12 28 | dero herr bruder [code] uber |
| 17.2.2 | 24 30 28 20 12 23 24 30 23 8+ 10 20 26 10 11 12 23 17 26 20 12 13 14 11 8+ 26 | morgen montags abends gelibts |
| 17.2.3 | 20 30 32 11 12 38 12 33 28 : 9 34 28 26 8+ 13 : 20 23 10 17 : 39 34 17 10 28 24 | got bey ewr: furstl: gnad: zu darm |
| 17.2.4 | 26 8+ 10 32 10 23 13 10 23 20 12 23 33 12 28 17 12 23 | stat anlangen werden |

## The writer's margin notes (paraphrases of the blocks, not letter-for-letter)

- Block 1: "# Zu Ew. Fr. Gn. sich eilendt wieder hinaus gen Darmstatt erheben, und mit Ihro bey einigen wichtigen und
  erheblichen fremden Personen sich communiciren." (read from the image; "eilendt" and "fremden Personen" doubtful)
- Block 2: "# Ihr Herr Bruder H. Landg. Johann zu [?Giessen] übermorgen montags abends geliebts Gott bey Ew. Fr. Gn. zu
  Darmbstatt anlangen werden."

## Count

Counted by `research/reading_audit/v10_relabel.share` on the Reading section: 39 words read, 2 holes (the code sign's
probable two-word value `[?Landgraf Johann]` counts as two). Read share **0.951**. Every one of the 216 number groups
has a value; the only open item is the code sign.

## English translation

(... the President, Vice-Chancellor and councillors report that His Princely Grace has thought fit) to betake himself
again in all haste out to Darmstadt to Your Princely Grace, and to confer with you in person on some weighty and
considerable points.

(... and that) his lord brother [?Landgrave Johann] will, God willing, arrive the day after tomorrow, Monday evening,
with Your Princely Grace at Darmstadt.
