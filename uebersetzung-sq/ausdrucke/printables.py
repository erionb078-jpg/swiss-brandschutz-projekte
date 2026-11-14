import json,math,base64,re,os,random,html
SP='/tmp/claude-0/-home-claude/133ba4ae-4316-560e-9041-7dc80082bb1c/scratchpad'
W=SP+'/fontwork';F=W+'/f2'
G=json.load(open(W+'/glyphs.json'));STK=json.load(open(W+'/strokes.json'))
LOGO='data:image/png;base64,'+base64.b64encode(open(SP+'/logo/l-002.png','rb').read()).decode()
QALAM=open(SP+'/qalam.svg').read().replace('class="nuri"','class="mas"')
FOX=open(SP+'/fox.svg').read().replace('<svg','<svg class="mas"',1)
def colorme(svg):
    svg=re.sub(r'fill="(?!none)[^"]*"','fill="#fff"',svg);svg=re.sub(r'stroke="[^"]*"','stroke="#1d1d1d"',svg)
    return svg.replace('class="mas"','class="mas cm"')
# fixed palette for print (Qalam uses css vars)
def solid(svg):
    return (svg.replace('var(--muted)','#6e5966').replace('var(--teal)','#13877c').replace('var(--sun)','#f2b632')
            .replace('var(--coral)','#ee7a2b').replace('var(--line)','#e3d6dd'))
QALAM_C=solid(QALAM)
L=[("ا","Elif","ā","أسد","luan"),("ب","Ba","b","بيت","shtëpi"),("ت","Ta","t","تمر","hurma"),("ث","Tha","th","ثوب","rrobë"),("ج","Xhim","xh","جبل","mal"),("ح","Ḥa","ḥ","حليب","qumësht"),("خ","Kha","kh","خبز","bukë"),("د","Dal","d","دار","shtëpi"),("ذ","Dhal","dh","ذهب","ar"),("ر","Ra","r","رجل","burrë"),("ز","Zaj","z","زيت","vaj"),("س","Sin","s","سمك","peshk"),("ش","Shin","sh","شمس","diell"),("ص","Ṣad","ṣ","صبر","durim"),("ض","Ḍad","ḍ","ضوء","dritë"),("ط","Ṭa","ṭ","طير","zog"),("ظ","Ẓa","ẓ","ظل","hije"),("ع","ʿAjn","ʿ","عين","sy"),("غ","Gajn","gh","غيم","re"),("ف","Fa","f","فيل","elefant"),("ق","Qaf","q","قلم","laps"),("ك","Kef","k","كلب","qen"),("ل","Lam","l","لبن","qumësht"),("م","Mim","m","ماء","ujë"),("ن","Nun","n","نور","dritë"),("ه","He","h","هلال","hënë e re"),("و","Vav","w","ورد","trëndafila"),("ي","Ja","j","يد","dorë")]
HEAVY="خصضغطقظ"
def vb(i,pad=60,minh=760):
    x0,y0,x1,y1=G[i]['bb'];w=x1-x0+2*pad;h=max(y1-y0+2*pad,minh)
    return f"{x0-pad} {y0-pad-(h-(y1-y0+2*pad))/2} {w} {h}"
def outline(i,cls="ol",sw=14):
    return f'<svg class="{cls}" viewBox="{vb(i)}">'+"".join(f'<path d="{d}" fill="#fff" stroke="#1d1d1d" stroke-width="{sw}" stroke-linejoin="round"/>' for d in G[i]['p'])+'</svg>'
def solidletter(i,col,cls="sl"):
    return f'<svg class="{cls}" viewBox="{vb(i)}">'+"".join(f'<path d="{d}" fill="{col}"/>' for d in G[i]['p'])+'</svg>'
STAR='<svg class="st" viewBox="0 0 24 24"><path d="M12 2.8l2.8 5.8 6.3.9-4.6 4.4 1.1 6.3L12 17.2l-5.6 3 1.1-6.3L2.9 9.5l6.3-.9z" fill="FILL" stroke="#1d1d1d" stroke-width="1.1"/></svg>'
star=lambda f="#fff":STAR.replace("FILL",f)
SCI='<svg class="sci" viewBox="0 0 24 24" fill="none" stroke="#888" stroke-width="1.6"><circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M8.1 8.1L20 18M8.1 15.9L20 6"/></svg>'

CSS=f'''
@font-face{{font-family:Naskh;src:url(file://{W}/naskh.ttf)}}
@font-face{{font-family:Lexend;font-weight:700;src:url(file://{F}/fontsource-lexend-5.2.5/files/lexend-latin-700-normal.woff2)}}
@font-face{{font-family:Lexend;font-weight:800;src:url(file://{F}/fontsource-lexend-5.2.5/files/lexend-latin-800-normal.woff2)}}
@font-face{{font-family:Lexend;font-weight:500;src:url(file://{F}/fontsource-lexend-5.2.5/files/lexend-latin-500-normal.woff2)}}
@font-face{{font-family:Nunito;font-weight:400;src:url(file://{F}/fontsource-nunito-sans-5.2.5/files/nunito-sans-latin-400-normal.woff2)}}
@font-face{{font-family:Nunito;font-weight:700;src:url(file://{F}/fontsource-nunito-sans-5.2.5/files/nunito-sans-latin-700-normal.woff2)}}
@font-face{{font-family:Nunito;font-weight:800;src:url(file://{F}/fontsource-nunito-sans-5.2.5/files/nunito-sans-latin-800-normal.woff2)}}
:root{{--plum:#6b2150;--plum2:#4e1539;--red:#d6303a;--gold:#e8a821;--tint:#f6eff3;--tint2:#efe3ea;--ink:#2a1823;--muted:#6e5966;--line:#e3d6dd;--heavy:#2d63c8;--teal:#13877c;--fox:#ee7a2b}}
*{{box-sizing:border-box}} body{{margin:0;font-family:Nunito,sans-serif;color:var(--ink);-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.page{{position:relative;overflow:hidden;page-break-after:always;display:flex;flex-direction:column}}
h1,h2,h3{{font-family:Lexend,sans-serif;margin:0;line-height:1.1;letter-spacing:-.01em}}
.ar{{font-family:Naskh,serif;direction:rtl}}
.bar{{display:flex;align-items:center;gap:5mm;border-bottom:1.2mm solid var(--plum);padding-bottom:3mm;margin-bottom:4mm}}
.bar img{{height:11mm}} .bar .tt{{flex:1}} .bar h1{{font-size:20pt;color:var(--plum)}} .bar p{{margin:.5mm 0 0;font-size:10pt;color:var(--muted)}}
.bar .nm{{font-size:10pt;font-weight:700;color:var(--muted);text-align:right}}
.ft{{position:absolute;left:0;right:0;bottom:5mm;text-align:center;font-size:7.5pt;color:#9a8a93}}
.ft b{{color:var(--plum)}}
.cm path,.cm circle,.cm ellipse,.cm rect{{stroke:#1d1d1d!important;stroke-width:2.4}}
.st{{width:7mm;height:7mm}}
.cut{{border:.35mm dashed #a9a9a9}}
.sci{{width:5mm;height:5mm}}
'''
def bar(title,sub="",name=True,logo=True):
    return f'<div class="bar">{f"<img src={LOGO!r}>" if logo else ""}<div class="tt"><h1>{title}</h1>{f"<p>{sub}</p>" if sub else ""}</div>{"<div class=nm>Emri: ________________</div>" if name else ""}</div>'
FT='<div class="ft"><b>abrar</b> · Harf për Harf · falas për printim – jo për shitje</div>'
DOCS=[]
def doc(fname,size,w,h,pages,extra=""):
    body="".join(f'<section class="page" style="width:{w}mm;height:{h}mm;padding:{p.get("pad","12mm 13mm 14mm")}">{p["html"]}{"" if p.get("noft") else FT}</section>' for p in pages)
    DOCS.append((fname,f'<!doctype html><html lang="sq"><head><meta charset="utf-8"><style>@page{{size:{size};margin:0}}{CSS}{extra}</style></head><body>{body}</body></html>'))

# 1 ---------- Alphabet poster A3 ----------
cells=""
for i,(c,n,snd,w,mean) in enumerate(L):
    col="var(--heavy)" if c in HEAVY else "var(--plum)"
    cells+=f'<div class="pc"><span class="no">{i+1}</span>{solidletter(i,col)}<b>{n}</b><span class="snd">{html.escape(snd)}</span><span class="ex"><span class="ar">{w}</span> · {mean}</span></div>'
doc("Alphabet-Poster-A3.pdf","A3",297,420,[{"pad":"14mm 14mm 16mm","html":f'''
<div class="ph"><img src="{LOGO}"><div><h1>Alfabeti arab</h1><p class="ar arr">الحُرُوفُ العَرَبِيَّة</p></div><div class="phq">{QALAM_C}</div></div>
<div class="pg">{cells}</div>
<div class="pleg"><span><i style="background:var(--plum)"></i>shkronjë e lehtë – tingëllon e çelët</span><span><i style="background:var(--heavy)"></i>shkronjë e rëndë – tingëllon e errët: <span class="ar" style="font-size:16pt">خ ص ض غ ط ق ظ</span></span><span>Lexo nga e djathta në të majtë ←</span></div>'''}],
'''.ph{display:grid;grid-template-columns:auto 1fr auto;gap:8mm;align-items:center;border-bottom:1.6mm solid var(--plum);padding-bottom:5mm}
.ph img{height:18mm}.ph h1{font-size:32pt;color:var(--plum);white-space:nowrap}.arr{font-size:22pt;margin:0;color:var(--red);line-height:1.3}.phq svg{width:20mm;height:auto}
.pg{display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:repeat(7,1fr);gap:3.2mm;direction:rtl;margin-top:6mm;flex:1;min-height:0}
.pc{position:relative;min-height:0;overflow:hidden;border-radius:5mm;background:var(--tint);display:flex;flex-direction:column;align-items:center;justify-content:center;padding:1.5mm 2mm 2.5mm;direction:ltr}
.pc .sl{width:100%;height:21mm}.pc b{font-family:Lexend;font-size:15pt;color:var(--ink);line-height:1.1}.pc .snd{font-size:10pt;font-weight:800;color:var(--red)}
.pc .ex{font-size:9.5pt;color:var(--muted);font-weight:700}.pc .ex .ar{font-size:13pt;color:var(--ink)}
.pc .no{position:absolute;top:2mm;left:3mm;font-family:Lexend;font-size:8pt;color:#b39aa8}
.pleg{display:flex;gap:8mm;justify-content:center;flex-wrap:wrap;font-weight:700;font-size:11pt;margin:5mm 0 3mm;align-items:center}.pleg span{display:flex;gap:2mm;align-items:center}.pleg i{width:6mm;height:6mm;border-radius:2mm;display:inline-block}''')

# 2 ---------- Lernplan A4 landscape ----------
PLAN=[("1","Alfabeti I","6–9","Alfabeti · Gjej shkronjën","Fletët për ngjyrosje 1–7","Viti i Elefantit"),
("2","Alfabeti II","6–9, ushtrimi 1","Si quhet? · Detektivi i pikave · Gjej çiftet","Fletët për ngjyrosje 8–14 · Memory","Fëmijëria në shkretëtirë"),
("3","Format e shkronjave","10–13, ushtrimi 2","Katër forma · Njih format","Fletët për ngjyrosje 15–21","El-Emin"),
("4","Të gjashtat & numrat","10–14, ushtrimi 3","Të gjashtat · Numrat","Fletët për ngjyrosje 22–28 · Fleta e numrave","Hatixheja"),
("5","Fetha","15–19","Fetha · Lexo fethën","Fleta e ngjyrave fetha/kesra/damma","Lexo! – Shpella Hira"),
("6","Ushtro fethën","20–23, ushtrimi 4–6","Lexo fethën (3 yje!)","Fleta e lidhjeve","I patundur në Mekë"),
("7","Kesra","24–30, ushtrimi 7–9","Kesra · Lexo kesrën","Bëj flamujt e shkronjave","Viti i Pikëllimit & Taifi"),
("8","Damma","31–37, ushtrimi 10–12","Damma · Lexo dammën · Përzierje zanoresh","Bëj shënuesit e librit","Udhëtimi i natës"),
("9","Sukuni","38–39","Sukuni · Lexo fjalë · Çifte rrokjesh","Bëj Qaben","Hixhreti"),
("10","Kalkale","40–42, ushtrimi 13–14","Testi i madh","Bëj xhaminë","Jeta në Medinë"),
("11","Shkronjat e rënda & të lehta","81–83, ushtrimi 24","E çelët & e errët · E rëndë apo e lehtë? · Dëgjo me vëmendje","Fleta e rëndë apo e lehtë","Bedri, Uhudi dhe Hendeku"),
("12","Ra & Lam · Përsëritje","82–85","Ra & Allah · Ushtro Ra & Lam","Certifikata 🎉","Kthimi në Mekë · Lamtumira · Çfarë ndodhi e para?")]
rows="".join(f'<tr><td class="wk">{w}</td><td><b>{t}</b></td><td>f. {p}</td><td>{g}</td><td>{m}</td><td>{s}</td><td class="ok"><span class="box"></span></td></tr>' for w,t,p,g,m,s in PLAN)
rows=rows.replace("🎉","")
doc("Lernplan-12-Wochen.pdf","A4 landscape",297,210,[
{"html":bar("Plani mësimor: mëso të lexosh në 12 javë","Libri · loja „Harf për Harf“ · fletët për ngjyrosje · „Sira me Fufflin“ – javë pas jave",True)+f'''
<table class="plan"><thead><tr><th>Java</th><th>Tema</th><th>Në libër</th><th>Harf për Harf</th><th>Ngjyros &amp; punë dore</th><th>Sira me Fufflin</th><th>U krye</th></tr></thead><tbody>{rows}</tbody></table>'''},
{"html":bar("Si ta përdorni planin mësimor","Një javë – pesë mësime të shkurtra",False)+f'''
<div class="wkgrid">
<div class="day"><b>E hënë</b><span>15 min.</span><p>Lexoni faqet e reja të librit bashkë me mësuesin ose prindërit.</p></div>
<div class="day"><b>E martë</b><span>10 min.</span><p>Luaj mësimin në „Harf për Harf“.</p></div>
<div class="day"><b>E mërkurë</b><span>15 min.</span><p>Zgjidh ushtrimet në libër – online ose në letër.</p></div>
<div class="day"><b>E enjte</b><span>15 min.</span><p>Ngjyros fletën, ndiqe me laps dhe shkruaj vetë.</p></div>
<div class="day"><b>E premte</b><span>10 min.</span><p>Një kuiz në „Harf për Harf“ dhe një stacion me Fufflin.</p></div>
<div class="day we"><b>Fundjava</b><span>e lirë</span><p>Punë dore, lojë memory – dhe ngjyros një yll në planin e yjeve!</p></div>
</div>
<div class="tips"><div class="tq">{QALAM_C}</div><ul>
<li><b>Më mirë shkurt dhe çdo ditë</b> se një herë gjatë. 10–15 minuta mjaftojnë.</li>
<li><b>Lexo me zë:</b> thuaje çdo rrokje me zë – kështu mëson edhe goja.</li>
<li><b>Mos shkruaj shkronja latine</b> pranë fjalëve arabe. Kjo e ngadalëson leximin.</li>
<li><b>Me mësues:</b> shqiptimin e saktë e mëson më së miri nga një mësues i kualifikuar.</li>
<li><b>Vazhdo:</b> pas javës 12 libri vazhdon me meddin, sheddenë, tenvinin dhe më shumë – me të njëjtin ritëm.</li></ul><div class="tf">{FOX}</div></div>'''}],
'''.plan{width:100%;border-collapse:separate;border-spacing:0;font-size:9.4pt}
.plan th{background:var(--plum);color:#fff;font-family:Lexend;font-weight:700;text-align:left;padding:2.4mm 2.4mm;font-size:9.5pt}
.plan th:first-child{border-radius:3mm 0 0 0}.plan th:last-child{border-radius:0 3mm 0 0;text-align:center}
.plan td{padding:1.4mm 2.4mm;border-bottom:.3mm solid var(--line);vertical-align:middle}
.plan tr:nth-child(even) td{background:var(--tint)}
.plan .wk{font-family:Lexend;font-weight:800;font-size:15pt;color:var(--red);text-align:center;width:14mm}
.plan .ok{text-align:center}.box{display:inline-block;width:6mm;height:6mm;border:.5mm solid var(--plum);border-radius:1.5mm}
.wkgrid{display:grid;grid-template-columns:repeat(6,1fr);gap:4mm;margin-top:2mm}
.day{background:var(--tint);border-radius:5mm;padding:4mm;display:flex;flex-direction:column;gap:1mm}.day b{font-family:Lexend;font-size:13pt;color:var(--plum)}
.day span{font-weight:800;color:var(--red);font-size:10pt}.day p{margin:0;font-size:10.5pt}.day.we{background:#fdf3dc}
.tips{display:grid;grid-template-columns:34mm 1fr 34mm;gap:6mm;align-items:center;margin-top:8mm}.tips svg{width:100%;height:auto}
.tips ul{margin:0;padding-left:5mm;font-size:12pt;display:grid;gap:2.2mm}.tips b{color:var(--plum)}''')

# 3 ---------- Sternchen-Plan ----------
sc="".join(f'<div class="sc"><span class="ar">{c}</span><small>{n}</small>{star()}</div>' for c,n,*_ in L)
doc("Sternchen-Plan.pdf","A4",210,297,[{"html":bar("Plani im i yjeve","A di ta lexosh dhe ta shkruash një shkronjë? Atëherë ngjyros yllin e saj!")+f'''
<div class="sgrid">{sc}</div>
<div class="sfoot"><div class="sq">{colorme(QALAM)}</div><div><h2>I ke të 28 yjet?</h2><p>Atëherë merr certifikatën tënde! Tregoja planin mësuesit.</p><p class="ar" style="font-size:24pt;margin:0">مَا شَاءَ ٱللَّه</p></div><div class="sq">{colorme(FOX)}</div></div>'''}],
'''.sgrid{display:grid;grid-template-columns:repeat(7,1fr);gap:3mm;direction:rtl;margin-top:3mm}
.sc{border:.5mm solid var(--plum);border-radius:4mm;display:flex;flex-direction:column;align-items:center;padding:1mm 1mm 2mm;direction:ltr}
.sc .ar{font-size:30pt;line-height:1.35;color:var(--plum)}.sc small{font-weight:800;font-size:9pt;color:var(--muted)}.sc .st{width:13mm;height:13mm;margin-top:1mm}
.sfoot{display:grid;grid-template-columns:40mm 1fr 40mm;gap:6mm;align-items:center;margin-top:auto;margin-bottom:8mm;text-align:center}
.sfoot svg{width:100%;height:auto;max-height:46mm}.sfoot h2{font-size:20pt;color:var(--plum)}.sfoot p{margin:2mm 0}''')

# 4 ---------- Memory ----------
cards=[]
for c,n,snd,*_ in L:
    cards.append(f'<div class="mc cut"><span class="ar">{c}</span></div>')
    cards.append(f'<div class="mc cut nm"><b>{n}</b><small>Tingulli: {html.escape(snd)}</small></div>')
cards+= [f'<div class="mc cut jk">{QALAM_C}<small>Joker</small></div>']*2+[f'<div class="mc cut jk">{FOX}<small>Joker</small></div>']*2
pages=[]
for k in range(0,len(cards),20):
    pages.append({"html":bar("Memory me shkronja",f"Prej, ktheji përmbys, gjej çiftet: shkronja + emri · fleta {k//20+1} nga 3",False)+f'<div class="mg">{"".join(cards[k:k+20])}</div><div class="hint">{SCI} Prej përgjatë vijave me ndërprerje. Këshillë: printo në letër të trashë.</div>'})
back="".join(f'<div class="mc cut bk"><img src="{LOGO}"><span class="ar">حرف</span></div>' for _ in range(20))
pages.append({"html":bar("Ana e pasme e kartave (opsionale)","Printoje në anën e pasme të fletëve me karta ose ngjite",False)+f'<div class="mg">{back}</div>'})
doc("Memory-Karten.pdf","A4",210,297,pages,
'''.mg{display:grid;grid-template-columns:repeat(4,45mm);grid-auto-rows:46mm;gap:0;justify-content:center;margin-top:2mm}
.mc{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1mm;text-align:center}
.mc .ar{font-size:54pt;line-height:1.2;color:var(--plum)}.mc.nm b{font-family:Lexend;font-size:19pt;color:var(--ink)}.mc small{font-weight:800;color:var(--red);font-size:10pt}
.mc.jk svg{width:26mm;height:30mm}.mc.bk{background:var(--plum)}.mc.bk img{height:9mm;background:#fff;border-radius:2mm;padding:1mm 2mm}.mc.bk .ar{color:#f4d9e7;font-size:22pt}
.hint{display:flex;gap:2mm;align-items:center;justify-content:center;font-size:10pt;color:var(--muted);margin-top:3mm}''')

# 5 ---------- Gebets-Tracker ----------
PR=[("Sabahu","الفجر"),("Dreka","الظهر"),("Ikindia","العصر"),("Akshami","المغرب"),("Jacia","العشاء")]
DAYS=["E hënë","E martë","E mërkurë","E enjte","E premte","E shtunë","E diel"]
SUN=['<circle cx="12" cy="12" r="5"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3"/>']
th="".join(f'<th><span class="ar">{a}</span><br>{d}</th>' for d,a in PR)
tr="".join(f'<tr><td class="dn">{d}</td>'+"".join('<td><span class="cir"></span></td>' for _ in PR)+'<td><span class="sm">'+star()+'</span></td></tr>' for d in DAYS)
doc("Gebets-Tracker.pdf","A4 landscape",297,210,[{"html":bar("Falem çdo ditë!","Ngjyros një rreth për çdo namaz. I ke të pesë? Atëherë ngjyros yllin!",True)+f'''
<div class="gt"><table class="tk"><thead><tr><th></th>{th}<th>Ylli</th></tr></thead><tbody>{tr}</tbody></table>
<div class="side"><div class="sf">{colorme(FOX)}</div><p><b>Fuffli e di:</b> pesë namazet ishin dhurata e udhëtimit të natës.</p><p class="cnt">Këtë javë i fala<br><span>____</span><br>nga 35 namaze!</p></div></div>'''}],
'''.gt{display:grid;grid-template-columns:1fr 62mm;gap:6mm;flex:1}
.tk{width:100%;border-collapse:separate;border-spacing:2mm}.tk th{font-family:Lexend;font-size:11pt;color:#fff;background:var(--plum);border-radius:3mm;padding:1.5mm}.tk th .ar{font-family:Naskh;font-size:15pt;color:#f6dbe9}
.tk th:first-child{background:none}.tk td{text-align:center;background:var(--tint);border-radius:3mm;height:16mm}.tk .dn{font-family:Lexend;font-weight:700;color:var(--plum);text-align:left;padding-left:3mm;background:none;font-size:12pt}
.cir{display:inline-block;width:11mm;height:11mm;border-radius:50%;border:.6mm solid var(--plum);background:#fff}.sm .st{width:11mm;height:11mm}
.side{background:#fdf3dc;border-radius:6mm;padding:5mm;display:flex;flex-direction:column;gap:3mm;text-align:center}.side .sf svg{width:42mm;height:auto}
.side p{margin:0;font-size:11pt}.side b{color:var(--plum)}.cnt{font-family:Lexend;font-size:13pt!important;color:var(--plum)}.cnt span{font-size:26pt}''')

# 6 ---------- Arabische Zahlen ----------
AD="٠١٢٣٤٥٦٧٨٩"
tbl="".join(f'<div class="zn"><span class="ar">{AD[i]}</span><b>{i}</b></div>' for i in range(10))
trc="".join(f'<div class="tz"><span class="ar g">{AD[i]}</span><span class="ar g">{AD[i]}</span><span class="ar g">{AD[i]}</span></div>' for i in range(1,10))
random.seed(3)
cnt=""
for n in [3,5,2,7,4,6]:
    cnt+=f'<div class="cr"><div class="obj">'+"".join(star("#fff") for _ in range(n))+'</div><span class="wb"></span></div>'
pairs=random.sample(range(10,100),6);rp=random.sample(pairs,6)
def ar_num(n):return "".join(AD[int(d)] for d in str(n))
mt="".join(f'<div class="mr"><span class="ar ml">{ar_num(a)}</span><span class="dt"></span><span></span><span class="dt"></span><b>{b}</b></div>' for a,b in zip(pairs,rp))
doc("Arabische-Zahlen.pdf","A4",210,297,[
{"html":bar("Numrat arabë","Kështu shkruhen numrat në Kuran – për shembull numrat e faqeve dhe të ajeteve")+f'''
<div class="zgrid">{tbl}</div><h3 class="h">1 · Ndiqi me laps dhe shkruaji numrat</h3><div class="tgrid">{trc}</div>
<div class="note">Kujdes: <span class="ar">٥</span> është <b>5</b> dhe <span class="ar">٠</span> është <b>0</b> – mos i ngatërro!</div>'''},
{"html":bar("Ushtro numrat","Numëro, shkruaj, lidh")+f'''
<h3 class="h">2 · Numëro yjet dhe shkruaj numrin arab në kuti</h3><div class="cgrid">{cnt}</div>
<h3 class="h">3 · Lidh numrin arab me numrin e saktë</h3><div class="match">{mt}</div>
<h3 class="h">4 · Vizato aq hurma sa thotë numri</h3><div class="dgrid"><div><span class="ar">٤</span></div><div><span class="ar">٨</span></div><div><span class="ar">٦</span></div></div>'''}],
'''.zgrid{display:grid;grid-template-columns:repeat(5,1fr);gap:3mm;direction:rtl}.zn{background:var(--tint);border-radius:4mm;text-align:center;padding:1mm 0 2mm}
.zn .ar{font-size:44pt;line-height:1.3;color:var(--plum);display:block}.zn b{font-family:Lexend;font-size:16pt;color:var(--red)}
.h{font-size:13pt;color:var(--plum);margin:6mm 0 3mm}.tgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:3mm}
.tz{border:.4mm solid var(--line);border-radius:3mm;display:flex;justify-content:space-around;padding:1mm 2mm;direction:rtl}.tz .g{font-size:34pt;line-height:1.3;color:#fff;-webkit-text-stroke:.5mm #9a9a9a}
.tz .g:first-child{color:#e6e6e6;-webkit-text-stroke:0}
.note{margin-top:5mm;background:#fdf3dc;border-radius:4mm;padding:3mm 5mm;font-size:12pt}.note .ar{font-size:18pt}
.cgrid{display:grid;grid-template-columns:1fr 1fr;gap:3mm}.cr{display:flex;align-items:center;gap:3mm;border:.4mm solid var(--line);border-radius:3mm;padding:2mm 3mm}
.obj{flex:1;display:flex;flex-wrap:wrap;gap:1mm}.obj .st{width:8mm;height:8mm}.wb{width:16mm;height:16mm;border:.6mm solid var(--plum);border-radius:3mm}
.match{display:grid;gap:3.5mm}.mr{display:grid;grid-template-columns:28mm 5mm 1fr 5mm 20mm;align-items:center}.ml{font-size:26pt;text-align:center;color:var(--plum)}
.mr b{font-family:Lexend;font-size:18pt}.dt{width:4mm;height:4mm;border-radius:50%;background:var(--ink)}
.dgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm}.dgrid div{border:.5mm solid var(--plum);border-radius:4mm;height:40mm;position:relative}
.dgrid .ar{position:absolute;top:1mm;right:3mm;font-size:24pt;color:var(--plum)}''')

# 7 ---------- Stickerbogen ----------
IC=open(SP+'/sira/index.html').read()
icons={}
for k in ["kaaba","moon","palm","mosque","camel","lamp"]:
    m=re.search(k+r":`(<svg.*?</svg>)`",IC,flags=re.S);icons[k]=m.group(1).replace("var(--sand)","#e9cf98").replace("var(--sky-soft)","#dbe4f7").replace("var(--fox)","#ee7a2b").replace("var(--fox-soft)","#fde4d1").replace("var(--palm-soft)","#d3efe2").replace("var(--sky)","#3a5bb0").replace("var(--ink)","#1c2440")
st=[]
st.append(f'<div class="sk" style="background:#d9f0ec">{QALAM_C}</div>');st.append(f'<div class="sk" style="background:#fde8d8">{FOX}</div>')
for t,bg,fg in [("Super!","#6b2150","#fff"),("Lexove bukur!","#d6303a","#fff"),("Vazhdo kështu!","#13877c","#fff"),("Masha'Allah!","#e8a821","#2a1823")]:
    st.append(f'<div class="sk tx" style="background:{bg};color:{fg}">{star("#ffd34d")}<b>{t}</b></div>')
for t,bg in [("مَا شَاءَ ٱللَّه","#6b2150"),("أَحْسَنْتَ","#13877c"),("بَارَكَ ٱللَّهُ فِيكَ","#d6303a")]:
    st.append(f'<div class="sk tx" style="background:{bg};color:#fff"><b class="ar" style="font-size:17pt">{t}</b></div>')
for k in icons: st.append(f'<div class="sk ic">{icons[k]}</div>')
for c in ["ا","ب","ت","ج","ح","ع","ق","م","ن"]:
    i=[x[0] for x in L].index(c);st.append(f'<div class="sk lt" style="background:{random.choice(["#f6eff3","#d9f0ec","#fde8d8","#fdf3dc"])}">{solidletter(i,"#6b2150")}</div>')
st+= [f'<div class="sk tx" style="background:#fff;border:.6mm solid #e8a821">{star("#ffd34d")}</div>']*(30-len(st))
doc("Stickerbogen.pdf","A4",210,297,[{"html":bar("Fletë me ngjitëse","Printoje në letër ngjitëse (A4, vetëngjitëse) dhe preje – për fletore, planin e yjeve dhe punë të mira",False)+f'<div class="skg">{"".join(st[:30])}</div>'}],
'''.skg{display:grid;grid-template-columns:repeat(5,34mm);grid-auto-rows:34mm;gap:4mm;justify-content:center;margin-top:3mm}
.sk{border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;overflow:hidden;text-align:center;box-shadow:inset 0 0 0 .5mm rgba(0,0,0,.08)}
.sk svg.mas{width:24mm;height:26mm}.sk.tx b{font-family:Lexend;font-size:11.5pt;line-height:1.1;padding:0 2mm}.sk.tx .st{width:10mm;height:10mm}
.sk.ic svg{width:30mm;height:30mm;border-radius:50%}.sk.lt .sl{width:22mm;height:22mm}''')

# 8 ---------- Bastelbögen ----------
S=60 # cube side mm
def tab(x,y,w,h,side):
    # trapezoid glue tab outside edge; side in top,bottom,left,right
    t=8
    if side=="top":return f'<path d="M{x} {y} L{x+t} {y-t} L{x+w-t} {y-t} L{x+w} {y}" class="tb"/>'
    if side=="bottom":return f'<path d="M{x} {y+h} L{x+t} {y+h+t} L{x+w-t} {y+h+t} L{x+w} {y+h}" class="tb"/>'
    if side=="left":return f'<path d="M{x} {y} L{x-t} {y+t} L{x-t} {y+h-t} L{x} {y+h}" class="tb"/>'
    return f'<path d="M{x+w} {y} L{x+w+t} {y+t} L{x+w+t} {y+h-t} L{x+w} {y+h}" class="tb"/>'
def kface(x,y,door=False,stone=False,top=False):
    s=f'<rect x="{x}" y="{y}" width="{S}" height="{S}" fill="#1b1b1f" stroke="#555" stroke-width=".3"/>'
    if not top:
        s+=f'<rect x="{x}" y="{y+S*0.22}" width="{S}" height="{S*0.12}" fill="#d9a520"/>'
        for k in range(6):s+=f'<path d="M{x+3+k*9} {y+S*0.28}q2 -3 4 0t4 0" stroke="#7a5a10" stroke-width=".5" fill="none"/>'
    if door:s+=f'<rect x="{x+S*0.62}" y="{y+S*0.55}" width="{S*0.2}" height="{S*0.45}" fill="#d9a520"/><path d="M{x+S*0.72} {y+S*0.55}v{S*0.45}" stroke="#7a5a10" stroke-width=".5"/>'
    if stone:s+=f'<ellipse cx="{x+4}" cy="{y+S*0.82}" rx="3" ry="4" fill="#c0c0c0" stroke="#d9a520" stroke-width="1"/>'
    return s
ox,oy=20,18
net=""
# cross: row1 top face at col1; row2 four sides; row3 bottom at col1
pos=[(1,0,"top"),(0,1,"s"),(1,1,"door"),(2,1,"s"),(3,1,"stone"),(1,2,"bottom")]
for cx,cy,kind in pos:
    x,y=ox+cx*S,oy+cy*S
    net+=kface(x,y,door=(kind=="door"),stone=(kind=="stone"),top=(kind in("top","bottom")))
net+=tab(ox,oy+S,S,S,"top")+tab(ox+2*S,oy+S,S,S,"top")+tab(ox+3*S,oy+S,S,S,"top")+tab(ox+3*S,oy+S,S,S,"right")
net+=tab(ox,oy+S,S,S,"bottom")+tab(ox+2*S,oy+S,S,S,"bottom")+tab(ox+3*S,oy+S,S,S,"bottom")
net+=f'<g stroke="#999" stroke-dasharray="1.5 1.5" stroke-width=".4" fill="none"><path d="M{ox+S} {oy+S}h{S}M{ox+S} {oy+2*S}h{S}M{ox+S} {oy+S}v{S}M{ox+2*S} {oy+S}v{S}M{ox+3*S} {oy+S}v{S}"/></g>'
kaaba_svg=f'<svg viewBox="0 0 290 225" class="netsvg"><style>.tb{{fill:#f3e7c9;stroke:#999;stroke-width:.4}}</style>{net}<text x="{ox+S*1.5}" y="{oy+S*0.55}" text-anchor="middle" font-size="5" fill="#d9a520" font-family="Nunito">sipër</text><text x="{ox+S*1.5}" y="{oy+S*2.55}" text-anchor="middle" font-size="5" fill="#d9a520" font-family="Nunito">poshtë</text></svg>'
howk='<ol><li>Preje – edhe pjesët e çelëta për ngjitje.</li><li>Palose në të gjitha vijat (palosja nga brenda).</li><li>Lyej pjesët me ngjitës dhe ngjite kubin.</li><li>Qabja jote është gati! Vendose në mes dhe vër rreth saj një rreth letre – metafin, ku haxhinjtë sillen rreth Qabes.</li></ol>'
# mosque: facade stand-up + minaret tube
moschee=f'''<svg viewBox="0 0 186 120" class="msvg"><g stroke="#1d1d1d" stroke-width=".7" fill="#fff">
<path d="M10 110V58h96v52z"/><path d="M28 58a30 30 0 0 1 60 0z"/><path d="M58 22v6"/><path d="M55 22a3 3 0 1 0 6 0 2.4 2.4 0 1 1-6 0z"/>
<path d="M46 110V86a12 12 0 0 1 24 0v24z"/><path d="M18 78a6 6 0 0 1 12 0v12H18zM86 78a6 6 0 0 1 12 0v12H86z"/>
<path d="M112 110V40h14v70z"/><path d="M110 40l9-14 9 14z"/><path d="M110 64h18M110 66h18"/><path d="M116 80a3 3 0 0 1 6 0v8h-6z"/>
<path d="M10 110h118v8H10z" fill="#f3e7c9"/></g>
<text x="69" y="117" text-anchor="middle" font-size="4" font-family="Nunito" fill="#777">palose mbrapa = këmbëza</text>
<g stroke="#1d1d1d" stroke-width=".7" fill="#fff"><path d="M140 20h40v90h-40z"/><path d="M180 20h6v90h-6z" fill="#f3e7c9"/>
<path d="M150 40a4 4 0 0 1 8 0v10h-8zM162 40a4 4 0 0 1 8 0v10h-8zM150 70a4 4 0 0 1 8 0v10h-8zM162 70a4 4 0 0 1 8 0v10h-8z"/><path d="M140 58h40M140 60h40"/></g>
<text x="160" y="15" text-anchor="middle" font-size="4.5" font-family="Nunito" fill="#555">Minareja: mbështille si tub</text></svg>'''
cone='<svg viewBox="0 0 80 100" class="cone"><path d="M40 6 L76 50 A44 44 0 0 1 4 50 Z" fill="#fff" stroke="#1d1d1d" stroke-width=".7"/><path d="M40 6L4 50" stroke="#999" stroke-dasharray="1.5 1.5" stroke-width=".5"/><text x="40" y="42" text-anchor="middle" font-size="4.5" font-family="Nunito" fill="#555">Maja: ngjite si kon</text></svg>'
# pennants
def pennant(i):
    c,n=L[i][0],L[i][1]
    return f'<div class="pen"><svg viewBox="0 0 60 78"><path d="M2 2h56L30 76z" fill="#fff" stroke="#1d1d1d" stroke-width=".6"/><path d="M2 8h56" stroke="#999" stroke-dasharray="1.5 1.5" stroke-width=".5"/></svg><div class="pl">{solidletter(i,"#fff","pls")}</div><small>{n}</small></div>'
pens="".join(pennant(i) for i in range(28))
pen_pages=[]
for k in range(0,28,6):
    pen_pages.append({"html":bar("Flamujt e shkronjave",f"Ngjyrosi flamujt, preji, palosi sipër dhe ngjiti në një spango · fleta {k//6+1} nga 5",False)+f'<div class="pg2">{"".join(pennant(i) for i in range(k,min(28,k+6)))}</div>'})
# stand-up figures
def standup(svg,name,col):
    return f'''<div class="su"><div class="sf cut"><div class="half">{svg}</div><div class="fold">✂ ---- palose këtu ---- ✂</div><div class="half flip">{svg}</div><div class="base" style="background:{col}">{name}</div></div></div>'''
# bookmarks
bm=[]
bm.append(f'<div class="bm cut" style="background:#f6eff3"><img src="{LOGO}"><div class="ar bal">'+"<br>".join(" ".join(x[0] for x in L[k:k+4]) for k in range(0,28,4))+'</div><small>Alfabeti</small></div>')
bm.append(f'<div class="bm cut" style="background:#d9f0ec"><div class="bq">{QALAM_C}</div><div class="ar big">اقْرَأْ</div><b>Lexo!</b><small>Fjala e parë e Kuranit</small></div>')
bm.append(f'<div class="bm cut"><div class="bq">{colorme(FOX)}</div><b style="color:#1d1d1d">Ngjyrosmë!</b><div class="ar big" style="color:#fff;-webkit-text-stroke:.5mm #1d1d1d">حَرْف</div><small>Name: ________</small></div>')
bm.append(f'<div class="bm cut" style="background:#fdf3dc"><b>Këtu ndalova:</b><div class="lines">'+"".join('<span>Faqja ____</span>' for _ in range(8))+f'</div><img src="{LOGO}"></div>')
doc("Bastelboegen.pdf","A4",210,297,[
{"html":bar("Fletë pune: Qabja","Një kub për ta prerë, palosur dhe ngjitur",False)+f'<div class="netwrap">{kaaba_svg}</div><div class="how">{howk}</div><div class="hint">{SCI} Këshillë: printo në letër të trashë (160–200 g). Gërshërët dhe ngjitësin përdori me një të rritur.</div>'},
{"html":bar("Fletë pune: Xhamia","Një xhami që qëndron në këmbë dhe një minare për ta mbështjellë – ngjyros, prej, vendos!",False)+f'<div class="mwrap">{moschee}</div><div class="cwrap">{cone}<div class="how"><ol><li>Ngjyros gjithçka me ngjyra.</li><li>Prej xhaminë dhe palose mbrapa shiritin e çelët poshtë – dhe ajo qëndron në këmbë.</li><li>Prej minaren, mbështille si tub dhe ngjite me pjesën e çelët.</li><li>Prej majën, ngjite si kon dhe vendose sipër minares.</li></ol></div></div>'},
*pen_pages,
{"html":bar("Figura në këmbë: Kalemi & Fuffli","Ngjyrosi, preji, palosi në mes dhe ngjit këmbëzën – kështu qëndrojnë në tavolinën tënde",False)+f'<div class="sug">{standup(colorme(QALAM),"Qalam","#13877c")}{standup(colorme(FOX),"Fuffl","#ee7a2b")}</div>'},
{"html":bar("Shënues libri","Katër shënues libri për t'i prerë – për librin tënd Abrar",False)+f'<div class="bmg">{"".join(bm)}</div><div class="hint">{SCI} Prej përgjatë vijave me ndërprerje. Me film ngjitës bëhen më të fortë.</div>'}],
'''.netwrap{display:flex;justify-content:center}.netsvg{width:186mm;height:auto}
.how{font-size:12pt;background:var(--tint);border-radius:5mm;padding:3mm 6mm}.how ol{margin:0;padding-left:6mm;display:grid;gap:1.5mm}
.hint{display:flex;gap:2mm;align-items:center;justify-content:center;font-size:10pt;color:var(--muted);margin-top:4mm}
.mwrap{display:flex;justify-content:center}.msvg{width:186mm;height:auto}.cwrap{display:grid;grid-template-columns:70mm 1fr;gap:6mm;align-items:center;margin-top:3mm}.cone{width:70mm}
.pg2{display:grid;grid-template-columns:repeat(3,1fr);gap:8mm 6mm;margin-top:6mm;direction:rtl}
.pen{position:relative;direction:ltr}.pen>svg{width:100%;height:auto;display:block}
.pen .pl{position:absolute;left:0;right:0;top:19%;display:flex;justify-content:center}.pen .pl svg.pls{width:38mm;height:38mm}.pls path{stroke:#1d1d1d;stroke-width:10}
.pen small{position:absolute;left:0;right:0;top:9%;text-align:center;font-family:Lexend;font-weight:700;font-size:13pt}
.sug{display:grid;grid-template-columns:1fr 1fr;gap:10mm;margin-top:4mm;flex:1}
.sf{display:flex;flex-direction:column;align-items:center;height:240mm;padding:3mm}.half{flex:1;display:flex;align-items:center;justify-content:center}.half svg{height:95mm;width:auto}
.half.flip{transform:rotate(180deg)}.fold{font-size:8pt;color:#999;letter-spacing:1px}.base{width:100%;text-align:center;color:#fff;font-family:Lexend;font-weight:800;padding:2mm;border-radius:2mm}
.bmg{display:grid;grid-template-columns:repeat(4,44mm);gap:4mm;justify-content:center;margin-top:2mm}
.bm{height:215mm;border-radius:3mm;display:flex;flex-direction:column;align-items:center;justify-content:space-between;padding:6mm 3mm;text-align:center}
.bm img{height:9mm;background:#fff;border-radius:2mm;padding:1mm 2mm}.bal{font-size:20pt;line-height:1.75;color:var(--plum)}.bm small{font-weight:800;color:var(--muted);font-size:9pt}
.bq svg{width:30mm;height:auto}.bm .big{font-size:40pt;color:var(--plum);line-height:1.4}.bm b{font-family:Lexend;color:var(--plum);font-size:13pt}
.lines{display:grid;gap:5mm;font-weight:700;color:var(--muted)}''')

os.makedirs(SP+'/sq/print/printhtml',exist_ok=True)
for fn,h in DOCS:
    open(SP+'/sq/print/printhtml/'+fn.replace('.pdf','.html'),'w').write(h)
print([d[0] for d in DOCS])
