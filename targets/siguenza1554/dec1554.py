"""Decode the Sigüenza 1554 cipher (catalogue 855) with the rebuilt key.

Usage: python3 dec1554.py transcription/d1_transcription.md

Reads the tab-separated lines (label, decipherment of the time, cipher signs) of a transcription file and prints,
for each line, the decipherment and the signs decoded with the key below. No hand corrections: a sign with more
than one value prints them all (a/b); a sign without a value prints in brackets; `.` dots are dropped; `[x]` is a
clear word written inside the cipher and is printed as (x).
"""
import sys

KEY = {}
for pair in """c=que q=de o-o=no tt=e ŧt=e ꝗ̊=o ȯ=s Ω=n ─x─=de ∃ꝶ=sa A=po A̤=po u=co ụ=co ∂=lo ꝯ=(h)a ─a=a
∃=si ─1─=se ─ꝺ─=le ─f°─=pue ꝗ̣=pro
ʒ=yo/do ꝺ+=me ∇ꝶ=ha aꝶ̶=ll ∘=o ɛ=a h=r 8=co oʒ=n b°=fu bꝶ=fa ʔ=so r=e b=s ꝺ̶=te/de ─ꝺ=ti ꝺꝶ=ta ꝺ̨=to ϑ=l q·=de aꝶ=ra ◻=tra
ꝓ=da 5=d 3z=dinero ϟ=do ꝗ̶=ve ─ℓ=ne t=s ȯ-o=ni
4=y ◻=tra 5ſ=va ċ=qui g=qui ẋ=pli ꝸ=re ꝙ̇=me ꝺ̵=se ─ℓ=ne
43b=ducados M=a ─1=se ɔ°=su ụ=co/ci ꝸ=re/co
oo=ne ꝶ=a 8°=cu ∂°=lu 5°=bu f°=pu z=ge ʃ=pe q̇=di ꝗ̇=di x=y ꝙ=que ʒ̇=yo 8ſ=ca ꝺ=l
ꝗ=que/vo ∂ꝶ=la ꝺ̵=se/si 43=ducado d°=mu n̄ꝶ=ga ɼ=d
6=l de=aqui ꝗſ=qua ∂̶=le f̶=po h̤=mo n°=gu ─ı=ssi ┼=im ʒ̵=re σ=gen q̊=lo ɤ̶=sa
⊐ſ=sa ◻̇=tro
a=re/ri o=u so=ve/vi ∇=o n=g r°=du ─e=ne gua=armada troꝶ=guerra s=dri ɀꝶ=da ⁊=gra si=amigos ɓ=fo ιos=su_Md ros=su_Md ─ꝗ─=ve gſ=va ꞃ̇=pre ụʒ=Sena D=m ꝺ̇=se z̄=zi ꝶ̶=z 8̊=to d=mi
ɀ=do ƶ=rr b̄=s ḥ=o
dꝶ=ma ꝸꝶ=na ꝺ°=tu R=pre/y -d=mi Ƶ=zi/rri ꞃꝶ=da ɼꝶ=da fꝶ=pa G=b T=cre nꝶ=ga Ƶ̊=ro ꝸ̶=ze S=bu 42=duque 36=duque_de_Florencia ιoz=su_Santidad iz=cardenal ꝗz=Ingalaterra 5ı=españoles ge=alemanes 25=vallos""".split():
    k, v = pair.split('=', 1)
    KEY[k] = v


def decode(tokens):
    out = []
    for t in tokens.split():
        if t in ('.', ',', '|', '/'):
            continue
        if t.startswith('[') and t.endswith(']'):
            out.append('(' + t[1:-1] + ')')
        else:
            out.append(KEY.get(t, '[' + t + ']'))
    return ' '.join(out)


for line in open(sys.argv[1], encoding='utf-8'):
    parts = line.rstrip('\n').split('\t')
    if len(parts) != 3:
        continue
    label, gloss, tokens = parts
    print(f'{label:4} {gloss}')
    print(f'     {decode(tokens)}')
