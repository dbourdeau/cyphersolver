from PIL import Image, ImageDraw, ImageFont
import json,sys
L=json.load(open('lines_auto.json'))
def build(n,rot,centers,tag,per=3):
    im=Image.open(n+'.png').convert('RGB')
    if rot: im=im.rotate(rot)
    W=im.size[0]; mid=W//2
    halves=[(60,mid+100),(mid-100,W-40)]
    for hi,(x0,x1) in enumerate(halves):
        for g in range(0,len(centers),per):
            grp=centers[g:g+per]; H=160
            out=Image.new('RGB',(x1-x0+50,H*len(grp)),(255,255,255))
            d=ImageDraw.Draw(out)
            for j,c in enumerate(grp):
                out.paste(im.crop((x0,c-80,x1,c+80)),(50,j*H))
                d.text((5,j*H+70),str(g+j+1),fill=(0,0,0))
                d.line([(0,j*H),(out.size[0],j*H)],fill=(0,0,0),width=2)
            xm=mid-x0+50
            d.line([(xm,0),(xm,out.size[1])],fill=(255,0,0),width=2)
            out.save(f'strips/{tag}_L{g+1:02d}_{"ab"[hi]}.png')
if __name__=='__main__':
    import glob,os
    for f in glob.glob('strips/*.png'): os.remove(f)
    build('p16170_P1',0,L['p16170_P1'][0],'p1')
