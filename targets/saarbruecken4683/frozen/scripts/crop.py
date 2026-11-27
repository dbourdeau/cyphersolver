# crop.py <folio> x0 y0 x1 y1 (fractions) out [maxdim]  -- PIL (déclaré), lit l'original pleine résolution
import sys, os
from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS=None
R="/Volumes/SPOF_2/Archives-Veille-cyber/RECUS-ARCHIVES/saarla-nassau-saarbruecken-ii-4683-2026-11-26/images"
fol=sys.argv[1]; x0,y0,x1,y1=map(float,sys.argv[2:6]); out=sys.argv[6]
md=int(sys.argv[7]) if len(sys.argv)>7 else 1600
im=Image.open(os.path.join(R,f"SaarLA_A01-002-04683_fol. {fol}.jpg")).convert('L')
W,H=im.size
im=im.crop((int(x0*W),int(y0*H),int(x1*W),int(y1*H)))
im=ImageOps.autocontrast(im,cutoff=(1,0.3))
im=im.point(lambda v:int(255*((v/255)**1.6)))
im.thumbnail((md,md)); im.save(out,quality=85)
