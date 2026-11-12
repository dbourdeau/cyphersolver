import sys
from PIL import Image, ImageDraw
IT=[(1,'21r',1927,2903),(2,'21r',996,3353),(3,'25r',885,2850),(4,'25r',1735,3229),(5,'25r',1089,3812),(6,'25r',1018,3998),(7,'25v',2886,1383),(8,'25v',3650,2472),
(9,'35r',3000,2703),(12,'35r',915,3324),(13,'35r',3225,4177),(14,'35v',1608,1968),(15,'35v',2783,1968),(16,'35v',3507,2530),(17,'35v',2141,3317),(18,'35v',1192,3543),(19,'35v',2747,3744),
(20,'36r',1967,1642),(21,'36r',3316,2561),(22,'36r',3765,2741),(23,'36r',1571,3142),(24,'36r',1059,3547),(25,'36r',1751,3741),(26,'36r',1553,3957),
(27,'36v',1197,1820),(28,'36v',2481,2373),(29,'36v',2265,2571),(30,'36v',3852,2924),(31,'23r',1989,2572),(32,'23r',1268,3800),(33,'23v',3440,4474)]
cache={}
def crop(n,p,x,y):
    if p not in cache: cache[p]=Image.open('/home/claude/en/trackB/b70_selvatico_read/img/%s.jpg'%p)
    im=cache[p]; b=(max(0,x-480),y-140,min(im.width,x+480),y+125); c=im.crop(b)
    c.save('crops/adj_%02d_%s.jpg'%(n,p),quality=90)
    t=Image.new('RGB',(960,c.height+26),'white'); t.paste(c,(0,26)); d=ImageDraw.Draw(t); d.text((4,6),'#%d %s centre x=%d y=%d (target near middle)'%(n,p,x,y),fill='red'); d.line((480-c.width//2+ (x-b[0]) ,26,480-c.width//2+(x-b[0]),34),fill='red',width=3)
    return t
per=6
for s in range(0,len(IT),per):
    ims=[crop(*i) for i in IT[s:s+per]]
    m=Image.new('RGB',(960,sum(i.height for i in ims)),'white'); y=0
    for i in ims: m.paste(i,(0,y)); y+=i.height
    m.save('crops/adjsheet_%d.jpg'%(s//per+1),quality=88); print(s//per+1,m.size)
