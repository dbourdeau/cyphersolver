# Draft email to Ahmet Safa Yıldırım and Yunus Emre Aydın (unsent)

Drafted 27 Nov 2026, revised 28 Nov 2026 to name Ibn al-Durayhim as the probable compiler and Ibn Faḍl Allāh as the
patron (`identity_ibn_durayhim.md`). Addresses are the ones printed on their GTTAD article (vol. 8, no. 18, p. 1013).

**To:** ahmet.yildirim@atauni.edu.tr, yunusemre.aydin@atauni.edu.tr
**Subject:** Your article "Mu'ammâyı Çöz": a Mamluk cipher manuscript (Penn LJS 51), probably by Ibn al-Durayhim

---

Dear Dr. Yıldırım, dear Dr. Aydın,

I read your article "'Mu'ammâyı Çöz': Memlûkler Devletinde Şifreli Yazışmalar ve Îmâlar Üzerinden Gizliliğin İnşası"
(GTTAD 8/18, 2026) with great interest. I am writing because a manuscript I am working on bears directly on the
limitation you name in your conclusion, that no Mamluk taʿmiya document survives. We think it may have been compiled by
one of the cryptologists you discuss.

I run cyphersolver (https://dbourdeau.github.io/cyphersolver/), a project that works on historical ciphers with AI
models (Anthropic's Claude) doing transcription and cryptanalysis, and people checking the results. The work is being
written up with the cryptologist George Lasry as a study of how such models perform on historical ciphers. Every target
keeps a public record of its method, its sources and what is still open.

**The manuscript.** University of Pennsylvania, Kislak Center, LJS 51 (ff. 1r-106v, images on OPenn:
https://openn.library.upenn.edu/Data/0001/ljs51/). It is a first-person account of the enciphered verses the compiler
exchanged with his patron and colleagues. After each cipher he usually writes that he solved it ("fa-ḥalaltuhu fī l-ḥāl
bi-ḥuḍūrihi") and gives the verses in clear. Penn dates the manuscript to the 15th century, possibly Syria, and the
library descriptions name no compiler.

**What we have so far:**
- A page-by-page survey of all 212 pages found about 209 cipher blocks. About 200 of them are followed by the compiler's
  own plaintext, so the book is a corpus of some 200 cipher/plaintext pairs in invented sign alphabets with word dividers.
  This is the kind of system Qalqashandī describes and you discuss in §2.6.
- **The compiler: probably Tāj al-Dīn ʿAlī b. Muḥammad Ibn al-Durayhim (712-762/1312-1361),** whom you list in your
  Table 1. The evidence so far:
  - on f. 102v the compiler refers to "my book *Miftāḥ al-kunūz fī ḥall al-marmūz*", which is the title of Ibn
    al-Durayhim's treatise, with *ḥall* where the known copies have *īḍāḥ*;
  - on ff. 49v-50r he argues, in the first person, over a Dunaynīr/Durayhim pun on his own name;
  - on f. 38v a correspondent sends him, in cipher, a verse praising "Tāj al-Dīn, scion of al-Durayhim" for *ḥall
    al-mutarjam*;
  - his movements between Aleppo, Damascus and Cairo, the people around him, and a second book he cites (*al-Ajwiba
    al-Shāmiyya*) agree with Ṣafadī's account in *Aʿyān al-ʿaṣr*.

  He never names himself outright in the passages read so far, and some of these readings still have to be checked on
  the master images. So we hold this as probable, not proven.
- **The patron.** The compiler calls him "al-maqarr al-sharīf al-makhdūmī al-ʿAlāʾī". We identify him as ʿAlāʾ al-Dīn
  ʿAlī b. Yaḥyā Ibn Faḍl Allāh, head of the Cairo chancery. On f. 62r the compiler mentions the death of the patron's
  brother, the emir Ṣalāḥ al-Dīn Mūsā, and Ṣafadī dates that death to Ṣafar 760.
- **Your article led to a further identification.** The compiler's most frequent correspondent is "al-Shaykh Shihāb
  al-Dīn al-Mutarjim". He is named in about ten cipher exchanges, and on f. 59r as "Shihāb al-Dīn Aḥmad al-Mutarjim".
  Following your reference to Ṣafadī, *al-Wāfī* vol. 7, pp. 94-95, we believe he is Aḥmad b. ʿAbd Allāh b. Dāwūd,
  Shihāb al-Dīn al-Baghdādī al-Mutarjim, the man tested in the Damascus Dīwān al-inshāʾ. A grandson of "al-Shihāb Maḥmūd",
  the chancery head of that story, also brings the compiler a cipher (f. 60r).
- The last cipher (f. 106v) has no surviving plaintext, because the manuscript breaks off. We recovered its key from a red
  gloss over the first five signs and from the metre (ṭawīl): 20 of its 21 words are read. Alan Elbaum kindly corrected
  our reading of the sender's name (Ibn al-Qabāqibī) and several words. The compiler's note under it, that the sender
  wrote lām-alif as a single sign, matches Qalqashandī's advice in your Table 8. Write-up:
  https://dbourdeau.github.io/cyphersolver/qaysarani1350.html
- Still in progress: transcribing every cipher at the sign level and rebuilding each key from its plaintext. Also open
  is a "tree script" on f. 63v, where 79 tree figures stand for the 79 letters of a verse. That looks like the plant-name
  method of your §2.4.

If the identification holds, LJS 51 is a working record of the cipher exchanges of Ibn al-Durayhim, kept with the head
of the Cairo chancery and the secretaries around him, mostly from the middle decades of the 14th century. That would
join the treatise tradition you describe to the chancery practice you argue for.

None of the LJS 51 corpus work is published yet. We hold it until it has been checked, so please treat the details
above as work in progress.

**Would you be willing to help?** Your knowledge of the Mamluk chancery, its people and the inshāʾ literature is what
this work most needs. In particular, we would value:
1. a critical check of the Ibn al-Durayhim, Ibn Faḍl Allāh and al-Mutarjim identifications, and of the other people the
   book names;
2. checking our readings of the Arabic plaintext passages, especially the ones the identification rests on (ff. 49v-50r,
   62r, 102v). These readings come from high-resolution images, but they are machine-assisted drafts;
3. comparing the book's techniques and terms with Qalqashandī, the *Miftāḥ al-kunūz* and the other treatises edited by
   Mrayati, Mir Alam and al-Tayyan.

Any help would be fully credited in the write-up and in the paper, in whatever form you prefer, and nothing involving
your contribution would be published without your review. I would be glad to send our transcriptions, translations and
notes for any part of the manuscript you would like to look at. I am also happy to correspond in English or through
Turkish if that is easier.

With best regards,

Daniel Bourdeau
cyphersolver, https://dbourdeau.github.io/cyphersolver/
