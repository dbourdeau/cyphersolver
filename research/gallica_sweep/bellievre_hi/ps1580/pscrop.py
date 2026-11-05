from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS=None
L=[3142,3252,3368,3479,3591,3713,3842,3955,4093,4207,4344,4475,4604,4729,4864,5005,5140]
R=[3127,3233,3361,3466,3591,3695,3818,3937,4066,4187,4339,4466,4598,4712,4848,4993,5125]
im=Image.open('a_c095.jpg')
x0,x1=840,4130; n=3; w=(x1-x0)/n
for i,(l,r) in enumerate(zip(L,R)):
    for k in range(n):
        a=int(x0+k*w)-40; b=int(x0+(k+1)*w)+40
        t=(k+0.5)/n; yc=int(l+(r-l)*((a+b)/2-1500)/2000)
        c=im.crop((a,yc-62,b,yc+58))
        c=ImageOps.autocontrast(c,cutoff=1).resize(((b-a)*2,240),Image.LANCZOS)
        c.save(f'ps1580/p{i+1:02d}_{k}.jpg')
