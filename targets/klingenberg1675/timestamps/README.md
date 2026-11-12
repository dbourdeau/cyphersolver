# Timestamps

Three RFC 3161 tokens from the Sectigo public time-stamping service (`MANIFEST.sha256.tsr`, query `.tsq`) and OpenTimestamps proofs (`.ots`, pending when taken), each over a SHA-256 manifest of our working files. Checked on 12 Nov 2026: every manifest line was recomputed from the file on disk.

| stamp | TSA time (GMT) | files | sha256 of the manifest | lines matching the files on disk |
|---|---|---|---|---|
| 20261111T210815Z_klingenberg1675 | 11 Nov 2026 21:08:16 | 64 | 61c9a80c7a850b646fb09407d827c9d5bdec7d9b73fb0995d4e1ce647bea5d58 | 64 of 64 |
| 20261111T212944Z_biermann1675_b69_v4_final | 11 Nov 2026 21:29:44 | 103 | bcc47de9017233ab62c91471c7f5f4beba14efdd1301fdb239c1974625106d49 | 103 of 103 |
| 20261111T214321Z_biermann1675_v4_trueheldout | 11 Nov 2026 21:43:21 | 150 | c04cd914b7cdf0c0cad20bef88a57e1ce6ab73834cf9a7521bc809b844d326e8 | 150 of 150 |

The first stamp is the one named in issue 424 (4 May letter, map v3, the 17 transcriptions); its text files are copied under its `stamped/` folder (images, the German quadgram model and compiled files left out). The second covers the seven further copybook letters and map v4; the third the three drafts. A stamp of 21:29:31 GMT (manifest 5c0b5664...) preceded the second by 13 seconds, before a two-line log edit, and is not included.

Not verified by us: the certificate chain of the tokens and the OpenTimestamps proofs (not upgraded). The times show that the files existed then; they do not show who was first.

Not stamped: everything made on 12 Nov 2026 for this folder (corrected 4 May transcription, decryptions, readings, translations, counts.txt, key.tsv, emendations.tsv, holes.md, scripts/count.py).

## Files of this folder that are byte-identical to a stamped file

| file here | sha256 | stamp | path in the manifest |
|---|---|---|---|
| evidence/words_evidence_v4.tsv | 22a8ae519e04c75d63774f9fb1de51e47d115fa7a39c7bfada615b90a1de8077 | 20261111T212944Z | b69_biermann_finish/work/words_evidence_v4.tsv |
| maps/table_M3.json | 7f2112e36372248c2ba4d30089f1906881d112a57de98aacb211891ed72542e2 | 20261111T214321Z | b73_biermann_v4_heldout/frozen/table_M3.json |
| maps/words_v1.json | 294c53a60acbd52a058ad4fcff1daca7ec440b27f6f9c68b54835a20e425eeae | 20261111T210815Z | b53_klingenberg_wordcode/frozen/words_FROZEN_v1.json |
| maps/words_v2.json | 050cd1d730e526502d649544a2f4de18ee8390195f110d99cce382211b5d0557 | 20261111T210815Z | b61_klingenberg_push/frozen/words_FROZEN_v2.json |
| maps/words_v3.json | cf804c280f82639592b6cf8b04b1780013dfffde755d68230ba807e2f0823cfc | 20261111T212944Z | b69_biermann_finish/frozen/words_FROZEN_v3.json |
| maps/words_v4.json | 9ac253c22179babd427969909008cae61265f57c07210c66ad1d423591cf5784 | 20261111T214321Z | b73_biermann_v4_heldout/frozen/words_FROZEN_v4.json |
| maps/words_v4_plus_tentative.json | a11456488bfe80b7ff549f26832253e30744616efdcb3a3cb967c9cf9ed8aa30 | 20261111T212944Z | b69_biermann_finish/frozen/words_v4_plus_tent.json |
| scripts/original/kt2.py | 44d732ebb943679760314dde4aa9ff2dd74fe68755c9b17c528cda93c58006d8 | 20261111T214321Z | b73_biermann_v4_heldout/scripts/kt2.py |
| scripts/original/ledger.py | 9e4655973e36d4d2d6a6ebc646a52fd1f15081e158eda866426d5445ea655978 | 20261111T214321Z | b73_biermann_v4_heldout/scripts/ledger.py |
| scripts/original/mkgloss.py | 50481ca5b0b9df8c622b10b367bafd909f3d90416f11553a897e0071b14d07dc | 20261111T214321Z | b73_biermann_v4_heldout/scripts/mkgloss.py |
| scripts/original/sense2.py | 185b10f8fbe66fc06483e70939f89e8f84b822237169fde0f438ae7c410a0986 | 20261111T214321Z | b73_biermann_v4_heldout/scripts/sense2.py |
| scripts/original/shuffle_words.py | a1f6218c979b1c0b72f8174f77c342df3dffe77185daed441440d928dcd4363e | 20261111T214321Z | b73_biermann_v4_heldout/scripts/shuffle_words.py |
| texts/1675-02-06_klingenberg_transcription.txt | 8733619245bf9475e5b89aac17c56d7fe6ad5d2a3aca690ec5ba92dc2f3bd561 | 20261111T210815Z | b61_klingenberg_push/tx/kl_0206_tx.txt |
| texts/1675-02-23_klingenberg_transcription.txt | 33c0d6eeb5f8f082cf165bb57938e460f536167089d5316e8bec3833cb9bd3cd | 20261111T210815Z | b61_klingenberg_push/tx/kl_0223_tx.txt |
| texts/1675-03-02_klingenberg_transcription.txt | 397ce6e1f1f7d02ac7961aaf5b7d88aeffd3d5e87c329fd1cd5b6e3253d42099 | 20261111T210815Z | b61_klingenberg_push/tx/kl_0302_tx.txt |
| texts/1675-03-06_klingenberg_transcription.txt | e3f0f5b5e3b829d8ea2bb283fd669a8ea52c040b31bf593417a7a43e0db5612f | 20261111T210815Z | b61_klingenberg_push/tx/kl_0306_tx.txt |
| texts/1675-03-09_klingenberg_transcription.txt | fcd73db1e9509276c557874638120087a9bb859d39982e3f5e2f58d195937a04 | 20261111T210815Z | b61_klingenberg_push/tx/kl_0309_tx.txt |
| texts/1675-03-13_klingenberg_transcription.txt | cbf62b49298cb21a3286c47e8567c1e595c93aec4eab3687398d10e2953f29ba | 20261111T210815Z | b61_klingenberg_push/tx/kl_0313_tx.txt |
| texts/1675-03-16_klingenberg_gloss.tsv | 66dc893948f220bcf9e834b6fb0a7aec511cfde5c3ee0c7ff073f9cb10227844 | 20261111T210815Z | b47_klingenberg_moonshot/work/gloss_0316.tsv |
| texts/1675-03-16_klingenberg_transcription.txt | bb9baa56990b2edea254a53220cd540c345b498c0421f7e8ec6b6ad6831cb124 | 20261111T210815Z | b61_klingenberg_push/tx/kl_0316_tx.txt |
| texts/1675-03-20_klingenberg_gloss.tsv | fc6ab14b7e0b67ae728c175f641c57d00484efb03ab5aff1f4c2625611e94d9d | 20261111T210815Z | b47_klingenberg_moonshot/work/gloss_0320.tsv |
| texts/1675-03-20_klingenberg_transcription.txt | a0ef23a5e27f464b6b422a75973a7404b0edb6cd8f6b848eb8daea71cbbd3bde | 20261111T210815Z | b61_klingenberg_push/tx/kl_0320_tx.txt |
| texts/1675-04-13_klingenberg_transcription.txt | 1361323f71848ccab4f168780b6f8519431f5ac5ea6c1e309d60d1e6acd32b90 | 20261111T210815Z | b61_klingenberg_push/tx/kl_0413_tx.txt |
| texts/1675-04-17_klingenberg_transcription.txt | cd348bdd05dd77a63f73488a3755bd801a58e1f8699b34493437aa5c0e49e573 | 20261111T210815Z | b61_klingenberg_push/tx/kl_0417_tx.txt |
| texts/1675-04-20_klingenberg_transcription.txt | 44c850516c360223afdeab1ff74769b0ade1bf5bed400278e758e9d0030a2405 | 20261111T210815Z | b61_klingenberg_push/tx/kl_0420_tx.txt |
| texts/1675-04-24_klingenberg_transcription.txt | 5cbe2560b0cec2329f7f7983c93be3867f65b0df488eb67d6154e1ff3264756d | 20261111T210815Z | b61_klingenberg_push/tx/kl_0424_tx.txt |
| texts/1675-04-27_klingenberg_transcription.txt | 23007e0608d50e3d75cd3f7cb57575c110061285e83d1d9ddfef2da28c8f9924 | 20261111T210815Z | b61_klingenberg_push/tx/kl_0427_tx.txt |
| texts/1675-05-01_klingenberg_transcription.txt | 4ba2f53216620784b5ad41ebfc0ae29f1180669a730ac5b5f588557db9efbd16 | 20261111T210815Z | b61_klingenberg_push/tx/kl_0501_tx.txt |
| texts/1675-05-04_klingenberg_transcription_frozen.txt | b955413c65422526cb827582d6c3a39b7e6c3511cbdb874a456d9dea6945c549 | 20261111T210815Z | b61_klingenberg_push/tx/kl_0504_tx.txt |
| texts/1675-05-08_klingenberg_gloss.tsv | 4722908a636f2d68c2ef65ce2622b5f9c7d95de44556ed3d02e6f84b60828252 | 20261111T212944Z | b69_biermann_finish/work/gloss_0508.tsv |
| texts/1675-05-08_klingenberg_gloss_v4.tsv | 75470f104197c920c4b9e1179d25d68a69914ce5f836ffa29cfc01be27d4faad | 20261111T212944Z | b69_biermann_finish/work/gloss_0508_v4.tsv |
| texts/1675-05-08_klingenberg_transcription.txt | cf4a86277db356a8e935fa4838a5e94fdc77cb29778f5b64d94b0742838b3e30 | 20261111T212944Z | b69_biermann_finish/tx/kl_0508_tx.txt |
| texts/1675-05-11_klingenberg_gloss.tsv | 2c823befe22a63ee2c29e1c943118f7977cca52b32ba6a57d688edd211e3c222 | 20261111T212944Z | b69_biermann_finish/work/gloss_0511.tsv |
| texts/1675-05-11_klingenberg_gloss_v4.tsv | c37336aaaf81eba756c4e2f2be87c49eec2b8d5ca5b49f47ff8a4e708a0a1864 | 20261111T212944Z | b69_biermann_finish/work/gloss_0511_v4.tsv |
| texts/1675-05-11_klingenberg_transcription.txt | 50c8e92e6903eedee41dfd4cabbd76c65f1e7b0108eb381689ef1eaa4ca09b10 | 20261111T212944Z | b69_biermann_finish/tx/kl_0511_tx.txt |
| texts/1675-05-29_klingenberg_transcription.txt | 487cb21eea804cf3382d292eed24955490a2d07a41487c95de849be25a3ff087 | 20261111T210815Z | b61_klingenberg_push/tx/kl_0529_tx.txt |
| texts/1675-06-01_klingenberg_gloss.tsv | c79814d657f35c177da1dcaa2ff09ec86f9fdafbe747bb8c4acf1f912f4e041b | 20261111T212944Z | b69_biermann_finish/work/gloss_0601_v4.tsv |
| texts/1675-06-01_klingenberg_gloss_v4.tsv | c79814d657f35c177da1dcaa2ff09ec86f9fdafbe747bb8c4acf1f912f4e041b | 20261111T212944Z | b69_biermann_finish/work/gloss_0601_v4.tsv |
| texts/1675-06-01_klingenberg_transcription.txt | 2ced119291b359fe651cb34efbfff373092266a91f56f9ecf870790e3fc40576 | 20261111T212944Z | b69_biermann_finish/tx/kl_0601_tx.txt |
| texts/1675-06-05_klingenberg_gloss.tsv | da9521543d1592d6ee40b2d54741218f69d3fe32bdb1c20e0ef7e00d3267422f | 20261111T212944Z | b69_biermann_finish/work/gloss_0605.tsv |
| texts/1675-06-05_klingenberg_gloss_v4.tsv | 1e2a5e33bd7bad7b3d930e081b80b45d13cf41138d7dc8cd5da3f989393e35ac | 20261111T212944Z | b69_biermann_finish/work/gloss_0605_v4.tsv |
| texts/1675-06-05_klingenberg_transcription.txt | f359698f5fcc6e1009ee81c6fa7d4f90fdd3ea258ef5e1e2aed8f40731565b5f | 20261111T212944Z | b69_biermann_finish/tx/kl_0605_tx.txt |
| texts/1675-06-08_klingenberg_gloss.tsv | 58c92842a003577d89d2bed5e537b09e671a74dcf7d48692aeadc048b288612a | 20261111T212944Z | b69_biermann_finish/work/gloss_0608.tsv |
| texts/1675-06-08_klingenberg_gloss_v4.tsv | d8e3f046ab7f999987bbc8265b488a9871cdd8be68e399ee67420fe331d5cb07 | 20261111T212944Z | b69_biermann_finish/work/gloss_0608_v4.tsv |
| texts/1675-06-08_klingenberg_transcription.txt | 75809ba4391ff8d4ca0a587a6781f2dcbe6dce4cdc7d334cd35b81929748809c | 20261111T212944Z | b69_biermann_finish/tx/kl_0608_tx.txt |
| texts/1675-06-12_klingenberg_gloss.tsv | e93ff0764a865756e18cfb5a0bcaf1099f7fccf9a4257b2866a61f3ec049337f | 20261111T212944Z | b69_biermann_finish/work/gloss_0612.tsv |
| texts/1675-06-12_klingenberg_gloss_v4.tsv | c429825c94e47023c437d191efa7b00c0b6cb5a8fadf5aff5ececb47f6288bff | 20261111T212944Z | b69_biermann_finish/work/gloss_0612_v4.tsv |
| texts/1675-06-12_klingenberg_transcription.txt | b624f0a116275982c26f12c0ebf834b75de9f5a891c2908771e0dceb300df306 | 20261111T212944Z | b69_biermann_finish/tx/kl_0612_tx.txt |
| texts/1675-06-21_klingenberg_transcription.txt | 36e1b2be13d8a73ea09ad568ff7e4ca88ddf351e6c83540465fa296d182d6430 | 20261111T210815Z | b61_klingenberg_push/tx/kl_0621_tx.txt |
| texts/1675-06-24_klingenberg_gloss.tsv | 07126e459a1dd12e8f43c38877366ff8477e9a36d14e6da246b1b3326461c3df | 20261111T212944Z | b69_biermann_finish/work/gloss_0624.tsv |
| texts/1675-06-24_klingenberg_gloss_v4.tsv | 210596f8c5b3c7c6889c28ceb1bf4e546ff8eeddef1a83c057d78a2efbe368fa | 20261111T212944Z | b69_biermann_finish/work/gloss_0624_v4.tsv |
| texts/1675-06-24_klingenberg_transcription.txt | 51c1cbc08f5ca053917703eb7f1ad53dda72c4e3b5e053c3b09bc8dcffa2700a | 20261111T212944Z | b69_biermann_finish/tx/kl_0624_tx.txt |
| texts/1675-06-28_klingenberg_gloss.tsv | 6c1bef90d1968e3e9fa2abf5b19f70b1a82b4b15e7a61cf0278409fc7529aaed | 20261111T214321Z | b73_biermann_v4_heldout/work/gloss_0628_v4.tsv |
| texts/1675-06-28_klingenberg_transcription.txt | 2d6673680621adf8e5c36313662a62e0e0a97569aac0d4d9cfbf9fef2734e72d | 20261111T214321Z | b73_biermann_v4_heldout/tx/kl_0628_tx.txt |
| texts/1675-07-00b_klingenberg_gloss.tsv | d501373326d77c83f827200bfb24cbd2fdc8ead90e01c853079a0bf23a6737dd | 20261111T214321Z | b73_biermann_v4_heldout/work/gloss_07B_v4.tsv |
| texts/1675-07-00b_klingenberg_transcription.txt | 92ab4833beabc119a7e71ec6ece9acf1959c9b37a4b2087236aea3b9986cf997 | 20261111T214321Z | b73_biermann_v4_heldout/tx/kl_07B_tx.txt |
| texts/1675-07-00c_klingenberg_gloss.tsv | 176f48a340b0eec19acfff9c0c17766dc9ef1a6a0ba478fe8bd731ab9d7ec1ea | 20261111T214321Z | b73_biermann_v4_heldout/work/gloss_07C_v4.tsv |
| texts/1675-07-00c_klingenberg_transcription.txt | b149860f6e883bd019d64ec2c4438e6f07e38d4bd0ba6dce5596ff6f4bae7745 | 20261111T214321Z | b73_biermann_v4_heldout/tx/kl_07C_tx.txt |

58 files. The 4 May transcription that was stamped is `texts/1675-05-04_klingenberg_transcription_frozen.txt`.
