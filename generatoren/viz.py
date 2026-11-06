import json,numpy as np
from PIL import Image,ImageDraw,ImageFont
from skel import G,raster,S,PAD
ST=json.load(open('strokes.json'))
f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',14)
tiles=[]
for k,g in enumerate(G):
    body=raster(g,[0]);H,W=body.shape
    a=np.full((H,W,3),255,np.uint8);a[body]=(200,215,235);im=Image.fromarray(a);d=ImageDraw.Draw(im)
    x0,y0,_,_=g['bb'];P=lambda x,y:((x-x0+PAD)*S,(y-y0+PAD)*S)
    cols=[(220,30,30),(30,120,220)]
    for si,s in enumerate(ST[k]['s']):
        pts=[P(*p) for p in s];n=len(pts)
        for i in range(n-1):
            t=i/(n-1);c=(int(255*t),int(60+120*(1-t)),int(255*(1-t)))
            d.line([pts[i],pts[i+1]],fill=c,width=4)
        d.ellipse([pts[0][0]-7,pts[0][1]-7,pts[0][0]+7,pts[0][1]+7],fill=(0,170,0))
        d.text((pts[0][0]+8,pts[0][1]-8),str(si+1),fill=(0,120,0),font=f)
        # arrow at end
        e=pts[-1];d.ellipse([e[0]-5,e[1]-5,e[0]+5,e[1]+5],fill=(0,0,0))
    d.text((4,H-18),f"{k} {g['c']}",fill=(0,0,0),font=f)
    tiles.append(im)
for s in range(4):
    ts=tiles[s*7:(s+1)*7];w=sum(t.width for t in ts)+10*len(ts);h=max(t.height for t in ts)
    sh=Image.new('RGB',(w,h),'white');x=0
    for t in ts:sh.paste(t,(x,0));x+=t.width+10
    sh.save(f'route{s}.png')
