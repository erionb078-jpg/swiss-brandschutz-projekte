import json,math,os,html
W='/tmp/claude-0/-home-claude/133ba4ae-4316-560e-9041-7dc80082bb1c/scratchpad/fontwork'
G=json.load(open(W+'/glyphs.json'));STK=json.load(open(W+'/strokes.json'))
L=[("ا","Alif","ā"),("ب","Ba","b"),("ت","Ta","t"),("ث","Tha","th"),("ج","Dschim","dsch"),("ح","Ḥa","ḥ"),("خ","Kha","kh"),("د","Dal","d"),("ذ","Dhal","dh"),("ر","Ra","r"),("ز","Zay","z"),("س","Sin","s"),("ش","Schin","sch"),("ص","Ṣad","ṣ"),("ض","Ḍad","ḍ"),("ط","Ṭa","ṭ"),("ظ","Ẓa","ẓ"),("ع","ʿAin","ʿ"),("غ","Ghain","gh"),("ف","Fa","f"),("ق","Qaf","q"),("ك","Kaf","k"),("ل","Lam","l"),("م","Mim","m"),("ن","Nun","n"),("ه","Ha","h"),("و","Waw","w"),("ي","Ya","y")]
HEAVY="خصضغطقظ";NC="ادذرزو"
FW={"ا":[["أسد","Löwe"]],"ب":[["بيت","Haus"]],"ت":[["تمر","Datteln"]],"ث":[["ثوب","Gewand"]],"ج":[["جبل","Berg"]],"ح":[["حليب","Milch"]],"خ":[["خبز","Brot"]],"د":[["دار","Haus"]],"ذ":[["ذهب","Gold"]],"ر":[["رجل","Mann"]],"ز":[["زيت","Öl"]],"س":[["سمك","Fisch"]],"ش":[["شمس","Sonne"]],"ص":[["صبر","Geduld"]],"ض":[["ضوء","Licht"]],"ط":[["طير","Vogel"]],"ظ":[["ظل","Schatten"]],"ع":[["عين","Auge"]],"غ":[["غيم","Wolken"]],"ف":[["فيل","Elefant"]],"ق":[["قلم","Stift"]],"ك":[["كلب","Hund"]],"ل":[["لبن","Milch"]],"م":[["ماء","Wasser"]],"ن":[["نور","Licht"]],"ه":[["هلال","Mondsichel"]],"و":[["ورد","Rosen"]],"ي":[["يد","Hand"]]}
TW="ـ"
def forms(c):
    nc=c in NC
    return [("Allein",c),("Anfang",c if nc else c+TW),("Mitte",TW+c if nc else TW+c+TW),("Ende",TW+c)]
def vb(i,pad=60,minh=760):
    x0,y0,x1,y1=G[i]['bb'];w=x1-x0+2*pad;h=max(y1-y0+2*pad,minh)
    return f"{x0-pad} {y0-pad-(h-(y1-y0+2*pad))/2} {w} {h}"
def outline(i):
    return f'<svg class="olet" viewBox="{vb(i)}">'+"".join(f'<path d="{d}" fill="#fff" stroke="#1d1d1d" stroke-width="14" stroke-linejoin="round"/>' for d in G[i]['p'])+'</svg>'
def trace(i,guide=True):
    k=STK[i];s=f'<svg class="tr" viewBox="{vb(i,90,820)}">'
    s+="".join(f'<path d="{d}" fill="#ececec"/>' for d in G[i]['p'])
    for st in k['s']:
        d="M"+"L".join(f"{x} {y}" for x,y in st)
        s+=f'<path d="{d}" fill="none" stroke="#7a7a7a" stroke-width="16" stroke-dasharray="2 34" stroke-linecap="round" stroke-linejoin="round"/>'
    if guide:
        for n,st in enumerate(k['s']):
            (x,y)=st[0];j=min(len(st)-1,3);(x2,y2)=st[j];a=math.atan2(y2-y,x2-x)
            ax,ay=x+math.cos(a)*90,y+math.sin(a)*90
            s+=f'<circle cx="{x}" cy="{y}" r="30" fill="#2bb673"/><text x="{x}" y="{y+13}" text-anchor="middle" font-size="40" font-weight="800" fill="#fff" font-family="Baloo2">{n+1}</text>'
            s+=f'<path d="M{x+math.cos(a)*40} {y+math.sin(a)*40}L{ax} {ay}" stroke="#2bb673" stroke-width="10" stroke-linecap="round"/><path d="M{ax} {ay}l{math.cos(a+2.5)*30} {math.sin(a+2.5)*30}M{ax} {ay}l{math.cos(a-2.5)*30} {math.sin(a-2.5)*30}" stroke="#2bb673" stroke-width="10" stroke-linecap="round"/>'
    return s+'</svg>'
def stars(n=5):
    return "".join('<svg class="st" viewBox="0 0 24 24"><path d="M12 2.8l2.8 5.8 6.3.9-4.6 4.4 1.1 6.3L12 17.2l-5.6 3 1.1-6.3L2.9 9.5l6.3-.9z" fill="#fff" stroke="#1d1d1d" stroke-width="1.2"/></svg>' for _ in range(n))
qalam=open('qalam.svg').read().replace('class="nuri"','class="mascot"')
fox=open('fox.svg').read().replace('<svg','<svg class="mascot"',1)
def color_me(svg):
    import re
    svg=re.sub(r'fill="(?!none)[^"]*"','fill="#fff"',svg)
    svg=re.sub(r'stroke="[^"]*"','stroke="#1d1d1d"',svg)
    return svg.replace('<svg','<svg style="--x:1" ',1).replace('class="mascot"','class="mascot cm"')
import base64
LOGO='data:image/png;base64,'+base64.b64encode(open('logo/l-002.png','rb').read()).decode()
LG=f'<img class="lg" src="{LOGO}" alt="Abrar Institute">'
pages=[]
def page(body,cls=""):
    pages.append(f'<section class="page {cls}">{body}<div class="foot"><b style=\"color:#6b2150\">abrar</b> · Harf für Harf · Übungsblätter · kostenlos zum Ausdrucken – nicht zum Verkauf</div></section>')
# cover
page(f'''<div class="cover">{LG}<div class="cvq">{color_me(qalam)}</div><h1>Harf für Harf</h1><h2>Übungsblätter zum Ausmalen,<br>Nachspuren und Lernen</h2>
<div class="arbig">حُرُوف</div><p class="nm">Dieses Heft gehört: ______________________________</p>
<div class="how"><b>So geht's:</b><ol><li>Male den großen Buchstaben bunt aus.</li><li>Spure ihn nach – fang beim grünen Punkt an und folge dem Pfeil.</li><li>Schreibe ihn selbst – von rechts nach links.</li><li>Male ein Bild zum Beispielwort.</li></ol></div>
<p class="note">Tipp: Sprich jeden Buchstaben beim Schreiben laut. Die Aussprache übst du am besten mit deinem Lehrer.</p></div>''',"cvp")
for i,(c,n,snd) in enumerate(L):
    w,mean=FW[c][0]
    tags=[]
    if c in HEAVY: tags.append('<span class="tag hv">schwerer Buchstabe – male ihn blau!</span>')
    if c in NC: tags.append('<span class="tag">verbindet sich nicht nach links</span>')
    fr="".join(f'<div class="fm"><span class="ar">{f}</span><small>{lab}</small></div>' for lab,f in forms(c))
    page(f'''<div class="hdr">{LG}<span class="num">{i+1}/28</span><span>Name: ____________________</span><span>Datum: __________</span></div>
<div class="top"><div class="big">{outline(i)}</div><div class="info"><h1>{n}</h1><p class="snd">Laut: <b>{html.escape(snd)}</b></p>{"".join(tags)}<p class="lbl">Male mich aus!</p><div class="stars">{stars(3)}</div></div></div>
<h3>1 · Spure nach <small>Fang beim grünen Punkt an</small></h3>
<div class="row trace">{trace(i)}{trace(i,False)}{trace(i,False)}{trace(i,False)}</div>
<h3>2 · Schreibe selbst <small>von rechts nach links ←</small></h3>
<div class="lines"><div></div><div></div></div>
<h3>3 · So sieht er im Wort aus</h3>
<div class="forms">{fr}</div>
<div class="word"><div class="wl"><span class="ar w">{w}</span><span>„{mean}“ – hier steht {n} am Anfang.<br>Umkreise {n} im Wort!</span></div><div class="draw"><small>Male hier: {mean}</small></div></div>''')
# harakat coloring
import random;random.seed(7)
V=[("َ","a","rot"),("ِ","i","blau"),("ُ","u","grün")]
cells=[]
for k in range(30):
    c=random.choice([x[0] for x in L if x[0]!="ا"]);v=random.choice(V);cells.append(f'<div class="cell"><span class="ar">{c}{v[0]}</span></div>')
page(f'''<div class="hdr">{LG}<span>Name: ____________________</span></div><h1 class="t">Fatha, Kasra oder Dhamma?</h1>
<p class="lead">Male jedes Feld in der richtigen Farbe aus:</p>
<div class="legend"><span><i class="sw r"></i><b class="ar">بَ</b> Fatha = rot</span><span><i class="sw b"></i><b class="ar">بِ</b> Kasra = blau</span><span><i class="sw g"></i><b class="ar">بُ</b> Dhamma = grün</span></div>
<div class="grid6">{"".join(cells)}</div><p class="lead">Lies danach jede Silbe laut!</p>''')
# heavy/light
cl="".join(f'<div class="cell"><span class="ar">{c}</span></div>' for c in random.sample([x[0] for x in L],28))
page(f'''<div class="hdr">{LG}<span>Name: ____________________</span></div><h1 class="t">Schwer oder leicht?</h1>
<p class="lead">Die 7 schweren Buchstaben klingen dunkel. Male sie <b>blau</b> aus – alle leichten Buchstaben male <b>gelb</b>.</p>
<div class="legend"><span><i class="sw b"></i> schwer = blau</span><span><i class="sw y"></i> leicht = gelb</span></div>
<div class="grid7">{cl}</div><p class="lead">Merksatz: <span class="ar" style="font-size:22pt">خُصَّ ضَغْطٍ قِظْ</span></p>''')
# matching
sel=random.sample(L,8);rights=random.sample(sel,8)
lr="".join(f'<div class="mrow"><span class="mname">{r[1]}</span><span class="dot"></span><span class="gap"></span><span class="dot"></span><span class="ar mlet">{l[0]}</span></div>' for l,r in zip(sel,rights))
page(f'''<div class="hdr">{LG}<span>Name: ____________________</span></div><h1 class="t">Verbinde!</h1><p class="lead">Ziehe eine Linie vom Buchstaben zu seinem Namen.</p><div class="match">{lr}</div>''')
# kaaba coloring
kaaba='''<svg viewBox="0 0 600 520" class="scene"><path d="M0 470h600" stroke="#1d1d1d" stroke-width="4"/><path d="M40 470c40-60 100-80 160-60" fill="none" stroke="#1d1d1d" stroke-width="3"/><path d="M400 470c40-50 110-70 170-40" fill="none" stroke="#1d1d1d" stroke-width="3"/>
<path d="M160 180l140-55 140 55v290H160z" fill="#fff" stroke="#1d1d1d" stroke-width="5"/><path d="M300 125l140 55-140 40-140-40z" fill="#fff" stroke="#1d1d1d" stroke-width="5"/>
<path d="M160 230l140 40 140-40v34l-140 40-140-40z" fill="#fff" stroke="#1d1d1d" stroke-width="4"/><path d="M335 330h55v140h-55z" fill="#fff" stroke="#1d1d1d" stroke-width="4"/><path d="M362 330v140" stroke="#1d1d1d" stroke-width="3"/>
<g fill="#fff" stroke="#1d1d1d" stroke-width="3"><path d="M60 120l8 16 18 3-13 12 3 18-16-9-16 9 3-18-13-12 18-3z"/><path d="M520 90l8 16 18 3-13 12 3 18-16-9-16 9 3-18-13-12 18-3z"/><path d="M470 40a40 40 0 1 0 30 70 34 34 0 1 1-30-70z"/></g>
<g fill="#fff" stroke="#1d1d1d" stroke-width="3"><circle cx="80" cy="455" r="14"/><circle cx="115" cy="458" r="14"/><circle cx="500" cy="455" r="14"/><circle cx="535" cy="458" r="14"/></g></svg>'''
page(f'''<div class="hdr">{LG}<span>Name: ____________________</span></div><h1 class="t">Die Kaaba in Mekka</h1><p class="lead">Male die Kaaba aus. Sie ist schwarz mit einem goldenen Band. Wer hat sie gebaut? Der Prophet Ibrahim und sein Sohn Ismail.</p>{kaaba}''')
# mascots coloring
page(f'''<div class="hdr">{LG}<span>Name: ____________________</span></div><h1 class="t">Qalam und Fuffl</h1><p class="lead">Male deine zwei Lernfreunde aus!</p><div class="duo"><div>{color_me(qalam)}<b>Qalam, die Schreibfeder</b></div><div>{color_me(fox)}<b>Fuffl, der Fuchs</b></div></div>''')
# certificate
page(f'''<div class="cert">{LG}<div class="cq">{color_me(qalam)}</div><h1>Urkunde</h1><p class="big">für</p><p class="nmline">______________________________</p>
<p class="big">Du kennst jetzt alle <b>28 Buchstaben</b><br>des arabischen Alphabets!</p><div class="arline ar">ا ب ت ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ ف ق ك ل م ن ه و ي</div>
<div class="stars big">{stars(5)}</div><p>Datum: ______________ &nbsp;&nbsp;&nbsp; Lehrer/in: ______________________</p><p class="mash">مَا شَاءَ ٱللَّه</p></div>''',"certp")

F=W+'/f2'
css=f'''
@font-face{{font-family:Naskh;src:url(file://{W}/naskh.ttf)}}
@font-face{{font-family:Baloo2;font-weight:800;src:url(file://{F}/fontsource-baloo-2-5.2.5/files/baloo-2-latin-800-normal.woff2)}}
@font-face{{font-family:Nunito;font-weight:400;src:url(file://{F}/fontsource-nunito-sans-5.2.5/files/nunito-sans-latin-400-normal.woff2)}}
@font-face{{font-family:Nunito;font-weight:700;src:url(file://{F}/fontsource-nunito-sans-5.2.5/files/nunito-sans-latin-700-normal.woff2)}}
@font-face{{font-family:Nunito;font-weight:800;src:url(file://{F}/fontsource-nunito-sans-5.2.5/files/nunito-sans-latin-800-normal.woff2)}}
@page{{size:A4;margin:0}}
*{{box-sizing:border-box}}
body{{margin:0;font-family:Nunito,sans-serif;color:#1d1d1d}}
.page{{width:210mm;height:297mm;padding:12mm 14mm 17mm;position:relative;page-break-after:always;overflow:hidden;display:flex;flex-direction:column;gap:3.2mm}}
.foot{{position:absolute;bottom:6mm;left:0;right:0;text-align:center;font-size:8pt;color:#888}}
h1,h2,h3{{font-family:Baloo2,sans-serif;margin:0;line-height:1.1}}
.ar{{font-family:Naskh,serif;direction:rtl}}
.lg{{height:9mm;width:auto}} .cover .lg{{height:18mm}} .cert .lg{{height:16mm}}
.hdr{{display:flex;align-items:center;gap:4mm;justify-content:space-between;font-size:10.5pt;font-weight:700;color:#444;border-bottom:1.5px solid #ddd;padding-bottom:2mm}}
.num{{background:#13877c;color:#fff;border-radius:99px;padding:0 3mm}}
.top{{display:grid;grid-template-columns:105mm 1fr;gap:6mm;align-items:center}}
.big .olet{{width:100%;height:76mm}}
.info h1{{font-size:40pt;color:#13877c}}
.snd{{font-size:15pt;margin:1mm 0 3mm}}
.tag{{display:inline-block;border:1.5px solid #1d1d1d;border-radius:99px;padding:.5mm 3mm;font-size:10pt;font-weight:700;margin:0 0 2mm}}
.tag.hv{{border-color:#2d63c8;color:#2d63c8}}
.lbl{{font-family:Baloo2;font-size:15pt;margin:2mm 0 1mm}}
.stars{{display:flex;gap:2mm}} .st{{width:10mm;height:10mm}} .stars.big .st{{width:16mm;height:16mm}}
h3{{font-size:15pt;display:flex;align-items:baseline;gap:3mm}} h3 small{{font-family:Nunito;font-size:10pt;color:#666;font-weight:700}}
.row.trace{{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm;direction:rtl}}
.tr{{width:100%;height:32mm;border:1.5px dashed #c9c9c9;border-radius:4mm}}
.lines{{display:grid;gap:5mm}} .lines div{{height:17mm;border-bottom:2px solid #1d1d1d;background:linear-gradient(transparent 49%,#d8d8d8 50%,transparent 51%);}}
.forms{{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm;direction:rtl}}
.fm{{border:1.5px solid #ddd;border-radius:4mm;text-align:center;padding:0 0 1.5mm}}
.fm .ar{{font-size:34pt;line-height:1.5;display:block}} .fm small{{font-weight:700;color:#666;direction:ltr}}
.word{{display:grid;grid-template-columns:1fr 70mm;gap:4mm;flex:1;min-height:0;max-height:62mm}}
.wl{{display:flex;flex-direction:column;justify-content:center;gap:2mm;font-size:12pt}} .wl .w{{font-size:46pt;line-height:1.4}}
.draw{{border:2px solid #1d1d1d;border-radius:5mm;padding:2mm 3mm}} .draw small{{font-weight:700;color:#666}}
.t{{font-size:30pt;color:#13877c;margin-top:2mm}} .lead{{font-size:13pt;margin:0}}
.legend{{display:flex;gap:6mm;font-size:13pt;font-weight:700;align-items:center;flex-wrap:wrap}} .legend span{{display:flex;gap:2mm;align-items:center}}
.sw{{display:inline-block;width:8mm;height:8mm;border:1.5px solid #1d1d1d;border-radius:2mm}} .sw.r{{background:#ef4a4a}} .sw.b{{background:#3d74e0}} .sw.g{{background:#2bb673}} .sw.y{{background:#ffd34d}}
.legend .ar{{font-size:18pt}}
.grid6{{display:grid;grid-template-columns:repeat(6,1fr);gap:3mm;direction:rtl}} .grid7{{display:grid;grid-template-columns:repeat(7,1fr);gap:3mm;direction:rtl}}
.cell{{border:2px solid #1d1d1d;border-radius:4mm;height:30mm;display:grid;place-items:center}} .cell .ar{{font-size:36pt;line-height:1}}
.grid7 .cell{{height:26mm}}
.match{{display:grid;gap:7mm;margin-top:6mm}} .mrow{{display:grid;grid-template-columns:40mm 6mm 1fr 6mm 30mm;align-items:center;font-size:18pt;font-weight:800;font-family:Baloo2}}
.mrow .dot{{width:5mm;height:5mm;border-radius:50%;background:#1d1d1d}} .mlet{{font-size:40pt;text-align:center;line-height:1}}
.scene{{width:100%;flex:1;min-height:0}}
.duo{{display:grid;grid-template-columns:1fr 1fr;gap:8mm;flex:1;align-items:center;text-align:center}} .duo svg{{width:100%;height:150mm}} .duo b{{font-family:Baloo2;font-size:16pt}}
.cm path,.cm circle,.cm ellipse,.cm rect{{stroke:#1d1d1d!important;stroke-width:2.4}} .cm .eye{{fill:#1d1d1d!important}}
.cover{{display:flex;flex-direction:column;align-items:center;text-align:center;gap:4mm;height:100%;justify-content:center}}
.cover h1{{font-size:54pt;color:#13877c}} .cover h2{{font-size:20pt;color:#444}} .cvq svg{{width:60mm;height:auto}}
.arbig{{font-family:Naskh;font-size:60pt;line-height:1.4}} .nm{{font-size:14pt;font-weight:700}}
.how{{text-align:left;border:2px solid #1d1d1d;border-radius:6mm;padding:4mm 8mm;font-size:12.5pt}} .how ol{{margin:1mm 0 0;padding-left:6mm}}
.note{{font-size:11pt;color:#555;max-width:140mm}}
.cert{{border:4mm double #13877c;border-radius:8mm;height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:4mm;padding:10mm}}
.cert h1{{font-size:60pt;color:#13877c}} .cert .big{{font-size:18pt;margin:0}} .nmline{{font-size:22pt;margin:0}} .cq svg{{width:42mm;height:auto}}
.arline{{font-size:22pt;line-height:1.6;max-width:160mm}} .mash{{font-family:Naskh;font-size:30pt;margin:0}}
'''
open('sheets.html','w').write('<!doctype html><html lang="de"><head><meta charset="utf-8"><style>'+css+'</style></head><body>'+"".join(pages)+'</body></html>')
print(len(pages))
