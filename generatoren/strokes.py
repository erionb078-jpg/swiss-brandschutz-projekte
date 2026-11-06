import json,numpy as np,networkx as nx
from skimage.morphology import skeletonize
from scipy import ndimage as ndi
from skel import G,raster,S,PAD
# waypoints per letter (font units, y negative = up); list of strokes
W={
0:[[(174,-670),(124,-12)]],
1:[[(660,-410),(690,-190),(320,-90),(115,-305)]],
2:[[(690,-430),(700,-170),(300,-60),(100,-305)]],
3:[[(680,-420),(690,-140),(300,-60),(110,-320)]],
4:[[(100,-300),(620,-350),(340,-290),(120,0),(330,230),(600,170)]],
5:[[(100,-310),(620,-360),(340,-300),(120,0),(330,240),(600,160)]],
6:[[(90,-300),(620,-330),(370,-280),(80,50),(330,190),(600,170)]],
7:[[(275,-450),(330,-140),(40,-175)]],
8:[[(300,-460),(330,-170),(50,-200)]],
9:[[(245,-400),(300,0),(-70,90)]],
10:[[(240,-400),(290,0),(-30,100)]],
11:[[(955,-400),(920,-150),(790,-300),(725,-160),(485,-260),(500,0),(250,170),(65,-110)]],
12:[[(950,-390),(915,-140),(770,-290),(720,-150),(470,-270),(480,0),(250,180),(55,-110)]],
13:[[(520,-110),(800,-330),(1000,-180),(700,-50),(520,-90),(470,-260),(480,20),(100,190),(60,-90)]],
14:[[(510,-110),(800,-330),(980,-180),(700,-60),(510,-90),(470,-270),(460,60),(200,175),(40,-100)]],
15:[[(290,-200),(530,-330),(680,-200),(500,-60),(230,-60),(40,-140)],[(240,-670),(290,-200)]],
16:[[(290,-200),(530,-330),(680,-200),(500,-60),(230,-60),(40,-140)],[(240,-670),(290,-200)]],
17:[[(380,-348),(248,-415),(120,-278),(238,-145),(466,-258),(238,-145),(333,238),(613,190)]],
18:[[(350,-330),(90,-300),(210,-170),(440,-280),(210,-170),(100,150),(300,280),(570,230)]],
19:[[(753,-281),(640,-285),(540,-370),(616,-456),(735,-380),(753,-281),(306,-61),(118,-316)]],
20:[[(548,-104),(400,-115),(290,-190),(413,-302),(525,-220),(548,-104),(243,188),(93,-99)]],
21:[[(500,-690),(520,-170),(100,-75),(45,-140)]],
22:[[(490,-700),(490,-50),(250,180),(100,-100)]],
23:[[(110,-230),(220,-330),(360,-180),(430,-180),(360,-170),(120,-90),(70,310)]],
24:[[(500,-260),(520,-50),(250,190),(60,-140)]],
25:[[(280,-500),(330,-390),(480,-310),(560,-130),(440,-90),(310,-110),(350,-220),(340,-380),(230,-330),(200,-230),(250,-120),(40,-120)]],
26:[[(408,-96),(260,-95),(156,-171),(276,-301),(400,-200),(408,-96),(206,134),(66,72)]],
27:[[(560,-270),(480,-330),(260,-120),(440,0),(220,180),(70,-100)]],
}
def rdp(pts,eps):
    if len(pts)<3:return pts
    a=np.array(pts[0]);b=np.array(pts[-1]);ab=b-a;L=np.hypot(*ab) or 1e-9
    d=[(abs(ab[0]*(p[1]-a[1])-ab[1]*(p[0]-a[0]))/L if L>1 else np.hypot(p[0]-a[0],p[1]-a[1])) for p in pts[1:-1]];i=int(np.argmax(d))+1
    if d[i-1]>eps:return rdp(pts[:i+1],eps)[:-1]+rdp(pts[i:],eps)
    return [pts[0],pts[-1]]
out=[];report=[]
for k,g in enumerate(G):
    body=raster(g,[0]);sk=skeletonize(body);dist=ndi.distance_transform_edt(body)
    ys,xs=np.nonzero(sk);Gr=nx.Graph()
    pts=set(zip(ys.tolist(),xs.tolist()))
    for (y,x) in pts:
        for dy in(-1,0,1):
            for dx in(-1,0,1):
                if (dy or dx) and (y+dy,x+dx) in pts:Gr.add_edge((y,x),(y+dy,x+dx),weight=np.hypot(dy,dx))
    x0,y0,_,_=g['bb']
    tofont=lambda y,x:(x/S+x0-PAD,y/S+y0-PAD)
    topx=lambda fx,fy:((fy-y0+PAD)*S,(fx-x0+PAD)*S)
    arr=np.array(list(pts))
    strokes=[];maxw=0;err=0
    for st in W[k]:
        nodes=[]
        for fx,fy in st:
            py,px=topx(fx,fy);i=np.argmin((arr[:,0]-py)**2+(arr[:,1]-px)**2);n=tuple(arr[i]);nodes.append(n)
            err=max(err,np.hypot(n[0]-py,n[1]-px)/S)
        path=[nodes[0]]
        for a,b in zip(nodes,nodes[1:]):
            p=nx.shortest_path(Gr,a,b,weight='weight');path+=p[1:]
        maxw=max(maxw,max(dist[y,x] for y,x in path))
        # smooth
        P=np.array([[x,y] for y,x in path],float)
        if len(P)>5:
            K=5;Pp=np.pad(P,((K,K),(0,0)),mode='edge');P2=np.array([Pp[i:i+2*K+1].mean(0) for i in range(len(P))]);P2[0]=P[0];P2[-1]=P[-1];P=P2
        simp=rdp([tuple(p) for p in P],0.6)
        strokes.append([[round(x/S+x0-PAD),round(y/S+y0-PAD)] for x,y in simp])
    covered=None
    w=round(2*maxw/S*1.12+8)
    out.append({"s":strokes,"w":w});report.append((k,g['c'],round(err),w,[len(s) for s in strokes]))
json.dump(out,open('strokes.json','w'),separators=(',',':'))
for r in report:print(r)
