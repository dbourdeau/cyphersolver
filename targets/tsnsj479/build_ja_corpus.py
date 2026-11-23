"""Build a Judaeo-Arabic stand-in corpus for T-S NS J479 (20 Nov 2026): Arabic texts written letter for letter in the
22 Hebrew letters, the way Geniza scribes spelt Arabic (ث→ת, خ→כ, ذ→ד, ض→צ, ظ→ט, غ→ג, ة→ה, ى→י), then coded one
Latin letter per Hebrew letter so the shared lang/ engine can use it:
  א a  ב b  ג g  ד d  ה h  ו w  ז z  ח c  ט v  י y  כ k  ל l  מ m  נ n  ס s  ע e  פ f  צ x  ק q  ר r  ש j  ת t
Sources (local, git-ignored): the Tanzil Qur'an text and the Arabic Papyrology Database editions fetched for
targets/vindob11016 (tr/tanzil_simple_clean.txt, tr/apd_corpus.txt). The papyrus letters are weighted x3: they are
closer to a private Egyptian hand than the Qur'an. Output: corpus/ja_translit.txt (registered in lang/sources.json).
Usage: build_ja_corpus.py"""
import re, sys
sys.stdout.reconfigure(encoding='utf-8')
AR2C = {'ا':'a','أ':'a','إ':'a','آ':'a','ٱ':'a','ب':'b','ت':'t','ث':'t','ج':'g','ح':'c','خ':'k','د':'d','ذ':'d','ر':'r',
        'ز':'z','س':'s','ش':'j','ص':'x','ض':'x','ط':'v','ظ':'v','ع':'e','غ':'g','ف':'f','ق':'q','ك':'k','ل':'l','م':'m',
        'ن':'n','ه':'h','ة':'h','و':'w','ؤ':'w','ي':'y','ى':'y','ئ':'y'}
def conv(t):
    return ' '.join(''.join(AR2C.get(ch, '') for ch in w) for w in t.split())
V = '../vindob11016/tr/'
qur = ' '.join(l.split('|', 2)[2] for l in open(V + 'tanzil_simple_clean.txt', encoding='utf-8') if l.count('|') >= 2)
apd = ' '.join(l.split('|', 2)[2] for l in open(V + 'apd_corpus.txt', encoding='utf-8') if l.count('|') >= 2)
q, a = conv(qur), conv(apd)
q = ' '.join(w for w in q.split() if w); a = ' '.join(w for w in a.split() if w)
open('corpus/ja_translit.txt', 'w', encoding='utf-8').write((a + '\n') * 3 + q + '\n')
print('qur words', len(q.split()), 'apd words', len(a.split()))
