import json
S='/tmp/claude-0/-home-claude/133ba4ae-4316-560e-9041-7dc80082bb1c/scratchpad'
LOGO=open(f'{S}/lehrer/logo.txt').read()
ST=[
 ("Stufe 1","Die Grundlage fürs Gebet",[(1,"الفاتحة","Al-Fatiha","Die Eröffnende",7),(114,"الناس","An-Nas","Die Menschen",6),(113,"الفلق","Al-Falaq","Das Morgengrauen",5),(112,"الإخلاص","Al-Ichlas","Die Aufrichtigkeit",4)]),
 ("Stufe 2","Kurz und oft gehört",[(111,"المسد","Al-Masad","Die Palmfaser",5),(110,"النصر","An-Nasr","Die Hilfe",3),(109,"الكافرون","Al-Kafirun","Die Ungläubigen",6),(108,"الكوثر","Al-Kauthar","Die Fülle",3)]),
 ("Stufe 3","Fünf kleine Schritte",[(107,"الماعون","Al-Maun","Die Hilfeleistung",7),(106,"قريش","Quraisch","Quraisch",4),(105,"الفيل","Al-Fil","Der Elefant",5),(104,"الهمزة","Al-Humaza","Der Stichler",9),(103,"العصر","Al-Asr","Die Zeit",3)]),
 ("Stufe 4","Etwas längere Suren",[(102,"التكاثر","At-Takathur","Die Vermehrung",8),(101,"القارعة","Al-Qaria","Das Pochende",11),(100,"العاديات","Al-Adiyat","Die Rennenden",11),(99,"الزلزلة","Az-Zalzala","Das Beben",8)]),
 ("Stufe 5","Der Weg zum Juz Amma",[(98,"البينة","Al-Bayyina","Der klare Beweis",8),(97,"القدر","Al-Qadr","Die Bestimmung",5),(96,"العلق","Al-Alaq","Das Anhängsel",19)]),
]
total=sum(len(x[2]) for x in ST)
html=f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#6b2150">
<title>Kurze Suren lernen – Abrar</title>
<meta name="description" content="{total} kurze Suren in 5 Stufen: abhaken, kostenlos beim Lehrer abhören lassen und für jede Stufe eine Urkunde erstellen.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lexend:wght@500;600;700;800&family=Nunito+Sans:wght@400;600;700;800&family=Noto+Naskh+Arabic:wght@500;700&family=Amiri+Quran&display=swap">
<style>
:root{{
  --bg:#ffffff; --tint:#f6eff3; --tint-2:#efe3ea; --ink:#2a1823; --muted:#6e5966; --line:#e8d9e1;
  --plum:#6b2150; --plum-2:#4e1539; --red:#d6303a; --teal:#13877c; --teal-2:#0d5f57; --teal-soft:#d9f0ec; --gold:#e8a821; --on-plum:#ffffff;
  --f-display:"Lexend",system-ui,-apple-system,"Segoe UI",sans-serif;
  --f-body:"Nunito Sans",system-ui,-apple-system,"Segoe UI",sans-serif;
  --f-ar:"Noto Naskh Arabic","Geeza Pro","Traditional Arabic",serif;
}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{
  --bg:#17101a; --tint:#21162a; --tint-2:#2b1d35; --ink:#f3e9ef; --muted:#bba7b3; --line:#3a2a40;
  --plum:#e7a2c9; --plum-2:#c97aa8; --red:#ff6b6b; --teal:#4fc4b5; --teal-2:#2f8f84; --teal-soft:#14393a; --gold:#ffcf5c; --on-plum:#2a1823; color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#17101a; --tint:#21162a; --tint-2:#2b1d35; --ink:#f3e9ef; --muted:#bba7b3; --line:#3a2a40;
  --plum:#e7a2c9; --plum-2:#c97aa8; --red:#ff6b6b; --teal:#4fc4b5; --teal-2:#2f8f84; --teal-soft:#14393a; --gold:#ffcf5c; --on-plum:#2a1823; color-scheme:dark}}
*{{box-sizing:border-box}}
html{{scroll-behavior:smooth}}
body{{margin:0;background:var(--bg);color:var(--ink);font-family:var(--f-body);font-size:17px;line-height:1.6;-webkit-font-smoothing:antialiased;overflow-x:hidden}}
h1,h2,h3{{font-family:var(--f-display);line-height:1.15;text-wrap:balance}}
.ar{{font-family:var(--f-ar);direction:rtl;unicode-bidi:isolate}}
.wrap{{max-width:1040px;margin:0 auto;padding-left:max(20px,env(safe-area-inset-left,0px));padding-right:max(20px,env(safe-area-inset-right,0px))}}
header{{position:sticky;top:0;z-index:20;background:color-mix(in srgb,var(--bg) 92%,transparent);backdrop-filter:blur(10px);border-bottom:1px solid var(--line);padding-top:env(safe-area-inset-top,0px)}}
header .wrap{{display:flex;align-items:center;justify-content:space-between;gap:14px;height:64px}}
.logo{{height:40px;width:auto;background:#fff;border-radius:10px;padding:4px 8px;box-shadow:0 0 0 1px var(--line)}}
.back{{font-family:var(--f-display);font-weight:700;color:var(--plum);text-decoration:none;font-size:15px}}
.back:hover{{text-decoration:underline}}
.hero{{background:radial-gradient(110% 90% at 90% 0%,var(--teal-soft),transparent 60%),var(--tint)}}
.hero .wrap{{display:grid;grid-template-columns:1.3fr .7fr;gap:36px;align-items:center;padding-block:52px 56px}}
.kicker{{font-weight:800;font-size:13px;letter-spacing:.09em;text-transform:uppercase;color:var(--teal)}}
.hero h1{{font-size:clamp(34px,5vw,54px);margin:8px 0 14px}}
.hero p{{color:var(--muted);max-width:36em;margin:0 0 12px}}
.ring{{justify-self:center;position:relative;width:min(220px,60vw);aspect-ratio:1;max-width:100%}}
.ring svg{{width:100%;height:100%;transform:rotate(-90deg)}}
.ring .in{{position:absolute;inset:0;display:grid;place-content:center;text-align:center}}
.ring b{{font-family:var(--f-display);font-size:clamp(40px,7vw,56px);line-height:1;font-variant-numeric:tabular-nums}}
.ring span{{color:var(--muted);font-weight:700;font-size:14px}}
.how{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:22px}}
.how div{{background:var(--bg);border:2px solid var(--line);border-radius:18px;padding:14px 16px}}
.how b{{display:block;font-family:var(--f-display);font-size:16px}}
.how span{{color:var(--muted);font-size:15px}}
main{{padding-block:24px 64px}}
.stage{{margin-top:40px}}
.shead{{display:flex;align-items:flex-end;justify-content:space-between;gap:12px;flex-wrap:wrap;border-bottom:2px solid var(--line);padding-bottom:12px;margin-bottom:16px}}
.shead h2{{margin:0;font-size:clamp(24px,3vw,30px)}}
.shead h2 small{{display:block;font-family:var(--f-body);font-size:15px;font-weight:700;color:var(--muted);margin-top:2px}}
.sbar{{display:flex;align-items:center;gap:10px;font-weight:800;font-size:14px;color:var(--muted);font-variant-numeric:tabular-nums}}
.sbar i{{display:block;width:120px;height:10px;border-radius:5px;background:var(--line);overflow:hidden}}
.sbar i u{{display:block;height:100%;width:0;background:var(--teal);transition:width .4s}}
.list{{display:grid;gap:10px}}
.row{{display:grid;grid-template-columns:auto 1fr auto auto;align-items:center;gap:16px;border:2px solid var(--line);border-radius:20px;padding:12px 14px 12px 12px;background:var(--bg);transition:border-color .2s,background .2s}}
.row.done{{border-color:var(--teal);background:color-mix(in srgb,var(--teal-soft) 55%,var(--bg))}}
.num{{width:46px;height:46px;border-radius:14px;display:grid;place-items:center;background:var(--tint);font-family:var(--f-display);font-weight:800;font-size:15px;color:var(--plum);font-variant-numeric:tabular-nums}}
.row.done .num{{background:var(--teal);color:#fff}}
.nm{{min-width:0;display:flex;align-items:center;gap:14px;flex-wrap:wrap}}
.nm .ar{{font-size:26px;line-height:1.3;font-weight:700}}
.nm .lt b{{display:block;font-family:var(--f-display);font-size:17px}}
.nm .lt span{{color:var(--muted);font-size:15px}}
.check{{position:relative;display:inline-flex;align-items:center;gap:8px;cursor:pointer;font-weight:800;font-size:15px;white-space:nowrap;user-select:none}}
.check input{{position:absolute;opacity:0;pointer-events:none}}
.check .box{{width:28px;height:28px;border-radius:9px;border:2px solid var(--line);display:grid;place-items:center;background:var(--bg);transition:background .2s,border-color .2s}}
.check .box svg{{width:16px;height:16px;opacity:0;color:#fff}}
.check input:checked+.box{{background:var(--teal);border-color:var(--teal)}}
.check input:checked+.box svg{{opacity:1}}
.check input:focus-visible+.box{{outline:2px solid var(--plum);outline-offset:2px}}
.listen{{font-family:var(--f-display);font-weight:700;font-size:14px;color:var(--plum);text-decoration:none;border:2px solid var(--line);border-radius:12px;padding:8px 12px;white-space:nowrap}}
.listen:hover{{border-color:var(--plum)}}
.award{{margin-top:14px;display:flex;align-items:center;justify-content:space-between;gap:14px;flex-wrap:wrap;border-radius:18px;padding:14px 18px;background:var(--teal-soft)}}
.award p{{margin:0;font-weight:800}}
.award a{{font-family:var(--f-display);font-weight:700;text-decoration:none;background:var(--teal);color:#fff;border-radius:12px;padding:9px 14px;box-shadow:0 3px 0 var(--teal-2)}}
.tip{{margin-top:44px;border:2px dashed var(--line);border-radius:22px;padding:20px 22px;display:grid;gap:6px}}
.tip b{{font-family:var(--f-display)}}
.tip p{{margin:0;color:var(--muted)}}
.cta{{margin-top:28px;border-radius:26px;padding:28px;background:var(--plum);color:var(--on-plum);display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap}}
.cta h3{{margin:0 0 6px;font-size:clamp(22px,3vw,28px)}}
.cta p{{margin:0;opacity:.9;max-width:34em}}
.cta a{{font-family:var(--f-display);font-weight:800;text-decoration:none;background:var(--bg);color:var(--plum);border-radius:14px;padding:12px 20px;white-space:nowrap}}
.row{{grid-template-columns:auto 1fr auto auto}}
.practice{{font-family:var(--f-display);font-weight:700;font-size:14px;color:#fff;background:var(--teal);border:0;border-radius:12px;padding:9px 13px;cursor:pointer;white-space:nowrap;box-shadow:0 3px 0 var(--teal-2)}}
.practice[aria-expanded="true"]{{background:var(--plum);box-shadow:0 3px 0 var(--plum-2)}}
.practice:focus-visible{{outline:2px solid var(--plum);outline-offset:2px}}
.prac{{border:2px solid var(--teal);border-radius:22px;padding:18px;background:var(--bg);display:grid;gap:14px;margin:-2px 0 6px}}
.ptop{{display:flex;flex-wrap:wrap;gap:14px 22px;align-items:flex-end;justify-content:space-between}}
.opt{{display:grid;gap:6px}}
.opt>span{{font-size:13px;font-weight:800;color:var(--muted)}}
.segs{{display:flex;gap:4px;background:var(--tint);border-radius:12px;padding:4px;flex-wrap:wrap}}
.segs button{{font:inherit;font-family:var(--f-display);font-weight:700;font-size:14px;border:0;border-radius:9px;padding:7px 11px;background:transparent;color:var(--ink);cursor:pointer}}
.segs button[aria-pressed="true"]{{background:var(--teal);color:#fff}}
.segs button:focus-visible{{outline:2px solid var(--plum)}}
.pbtns{{display:flex;gap:8px;flex-wrap:wrap}}
.pbtns button{{font:inherit;font-family:var(--f-display);font-weight:700;font-size:15px;border-radius:12px;padding:10px 16px;cursor:pointer;border:2px solid var(--line);background:var(--bg);color:var(--plum)}}
.pbtns button.go{{background:var(--teal);color:#fff;border-color:var(--teal);box-shadow:0 3px 0 var(--teal-2)}}
.pstat{{display:flex;align-items:center;gap:10px;min-height:32px;font-weight:800;color:var(--teal);font-variant-numeric:tabular-nums}}
.you{{background:var(--plum);color:#fff;border-radius:999px;padding:4px 12px;font-family:var(--f-display);animation:you 1s ease-in-out infinite}}
@keyframes you{{0%,100%{{transform:scale(1)}}50%{{transform:scale(1.07)}}}}
.qtext{{direction:rtl;border-radius:18px;background:var(--tint);padding:14px 16px;display:grid;gap:4px;max-height:420px;overflow:auto}}
.qtext .bsm{{text-align:center;font-family:"Amiri Quran",var(--f-ar);font-size:24px;line-height:2;color:var(--muted)}}
.ay{{font:inherit;text-align:right;direction:rtl;font-family:"Amiri Quran",var(--f-ar);font-size:clamp(23px,3vw,29px);line-height:2.1;color:var(--ink);background:transparent;border:0;border-radius:12px;padding:2px 10px;cursor:pointer}}
.ay:hover{{background:var(--bg)}}
.ay.on{{background:var(--teal-soft);box-shadow:inset -4px 0 0 var(--teal)}}
.ay i{{font-style:normal;display:inline-grid;place-items:center;min-width:30px;height:30px;margin-inline-start:8px;border-radius:50%;border:2px solid var(--teal);color:var(--teal);font-family:var(--f-ar);font-size:15px;line-height:1;vertical-align:middle}}
.pfoot{{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap;border-top:2px solid var(--line);padding-top:12px}}
.pfoot p{{margin:0;color:var(--muted);font-size:13px;max-width:42em}}
.pfoot a{{font-family:var(--f-display);font-weight:800;text-decoration:none;background:var(--plum);color:var(--on-plum);border-radius:12px;padding:10px 16px;white-space:nowrap}}
.loadmsg{{color:var(--muted);font-weight:700;padding:8px}}
@media (max-width:760px){{.row{{grid-template-columns:auto 1fr auto}}.row .practice{{grid-column:2/-1;justify-self:start}}}}
@media (prefers-reduced-motion:reduce){{.you{{animation:none}}}}
footer{{border-top:1px solid var(--line);padding-block:24px 36px;color:var(--muted);font-size:14px}}
@media (max-width:760px){{
  .hero .wrap{{grid-template-columns:1fr;padding-block:36px 40px}}
  .ring{{width:170px}}
  .how{{grid-template-columns:1fr}}
  .row{{grid-template-columns:auto 1fr auto;row-gap:10px}}
  
  .check .lbl{{display:none}}
}}
@media (prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}.sbar i u{{transition:none}}}}
</style>
</head>
<body>
<header><div class="wrap">
  <a href="../index.html" aria-label="Abrar – Startseite"><img class="logo" src="{LOGO}" alt="Abrar Institute"></a>
  <a class="back" href="../index.html#unterricht">← Lernen mit Lehrer</a>
</div></header>

<section class="hero"><div class="wrap">
  <div>
    <span class="kicker">Kostenlos · für jedes Alter</span>
    <h1>Kurze Suren lernen</h1>
    <p>{total} kurze Suren in 5 Stufen, von der Fatiha bis Al-Alaq. Hör jede Sure von Scheich al-Minshawi, sprich Vers für Vers nach und hake ab, was du auswendig kannst. Danach trägst du sie kostenlos unserem Lehrer vor.</p>
    <div class="how">
      <div><b>1. Anhören und nachsprechen</b><span>Der Scheich liest vor, du sprichst nach.</span></div>
      <div><b>2. Abhören lassen</b><span>Kostenlos beim Lehrer, online.</span></div>
      <div><b>3. Urkunde holen</b><span>Für jede geschaffte Stufe.</span></div>
    </div>
  </div>
  <div class="ring" role="img" aria-label="Fortschritt">
    <svg viewBox="0 0 120 120" aria-hidden="true"><circle cx="60" cy="60" r="52" fill="none" stroke="var(--line)" stroke-width="12"/><circle id="arc" cx="60" cy="60" r="52" fill="none" stroke="var(--teal)" stroke-width="12" stroke-linecap="round" stroke-dasharray="326.7" stroke-dashoffset="326.7" style="transition:stroke-dashoffset .5s"/></svg>
    <div class="in"><b id="cnt">0</b><span>von {total} Suren</span></div>
  </div>
</div></section>

<main><div class="wrap" id="stages"></div>
<div class="wrap">
  <div class="tip"><b>Tipp vom Lehrer</b><p>Lerne jeden Tag ein kleines Stück und wiederhole es im Gebet. Was du im Gebet sprichst, vergisst du nicht so schnell.</p></div>
  <div class="cta"><div><h3>Fertig mit einer Sure?</h3><p>Trag sie unserem zertifizierten Lehrer vor. Er hört zu, korrigiert und sagt dir, ob alles sitzt. Das ist kostenlos.</p></div><a href="../index.html?angebot=sure#anfrage">Termin zum Abhören anfragen</a></div>
</div></main>

<footer><div class="wrap">„Quran lesen lernen – Schritt für Schritt“ · Abrar · <a href="../index.html" style="color:inherit">Zur Startseite</a></div></footer>

<script>
const ST={json.dumps(ST,ensure_ascii=False)};
const KEY="suren-v1";let done={{}};
try{{done=JSON.parse(localStorage.getItem(KEY)||"{{}}")||{{}}}}catch(e){{done={{}}}}
const save=()=>{{try{{localStorage.setItem(KEY,JSON.stringify(done))}}catch(e){{}}}};
const TOTAL=ST.reduce((a,s)=>a+s[2].length,0);
const tick='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>';
const root=document.getElementById("stages");
ST.forEach((st,si)=>{{
  const sec=document.createElement("section");sec.className="stage";sec.id="stufe-"+(si+1);
  sec.innerHTML=`<div class="shead"><h2>${{st[0]}}<small>${{st[1]}} · ${{st[2].length}} Suren</small></h2><div class="sbar"><i><u></u></i><span class="sc">0/${{st[2].length}}</span></div></div><div class="list"></div><div class="award" hidden><p>Stufe ${{si+1}} geschafft. Masha Allah!</p><a href="../urkunde/index.html#suren-${{si+1}}">Urkunde erstellen</a></div>`;
  const list=sec.querySelector(".list");
  st[2].forEach(([n,ar,lt,de,v])=>{{
    const r=document.createElement("div");r.className="row";r.dataset.n=n;
    r.innerHTML=`<span class="num" title="Sure ${{n}}">${{n}}</span>
      <div class="nm"><span class="ar" lang="ar">${{ar}}</span><span class="lt"><b>${{lt}}</b><span>${{de}} · ${{v}} Verse</span></span></div>
      <label class="check" for="s-${{n}}"><input type="checkbox" id="s-${{n}}"><span class="box">${{tick}}</span><span class="lbl">Kann ich</span></label>
      <button type="button" class="practice" aria-expanded="false" aria-controls="p-${{n}}">▶ Anhören &amp; üben</button>`;
    const cb=r.querySelector("input");cb.checked=!!done[n];
    cb.addEventListener("change",()=>{{if(cb.checked)done[n]=1;else delete done[n];save();upd()}});
    list.appendChild(r);
    const pn=document.createElement("div");pn.className="prac";pn.id="p-"+n;pn.hidden=true;list.appendChild(pn);
    r.querySelector(".practice").addEventListener("click",()=>togglePractice(n,lt,r));
  }});
  root.appendChild(sec);
}});

/* ---------- Üben mit Scheich al-Minshawi ---------- */
const G1={{1:1,114:6231,113:6226,112:6222,111:6217,110:6214,109:6208,108:6205,107:6198,106:6194,105:6189,104:6180,103:6177,102:6169,101:6158,100:6147,99:6139,98:6131,97:6126,96:6107}};
const VERSES={{}};ST.forEach(s=>s[2].forEach(x=>VERSES[x[0]]=x[4]));
const AU=g=>`https://cdn.islamic.network/quran/audio/128/ar.minshawi/${{g}}.mp3`;
const AR="٠١٢٣٤٥٦٧٨٩",an=k=>String(k).replace(/\d/g,d=>AR[d]);
const TXT={{}};
const audio=new Audio();audio.preload="auto";
let P=null; // aktuelle Übung
function opts(){{let s={{rep:3,echo:1,bism:1,loop:0}};try{{Object.assign(s,JSON.parse(localStorage.getItem("suren-opt")||"{{}}"))}}catch(e){{}}return s}}
function saveOpts(o){{try{{localStorage.setItem("suren-opt",JSON.stringify(o))}}catch(e){{}}}}
async function getText(n){{
  if(TXT[n])return TXT[n];
  const r=await fetch(`https://api.alquran.cloud/v1/surah/${{n}}/quran-uthmani`);if(!r.ok)throw new Error("http");
  const j=await r.json();let ay=j.data.ayahs.map(a=>a.text.trim());
  if(n!==1){{const w=ay[0].split(/\s+/);if(w.length>4&&w[0].replace(/[ً-ْٰۡؐ-ؚ]/g,"").startsWith("بسم"))ay[0]=w.slice(4).join(" ")}}
  return TXT[n]=ay;
}}
function seg(name,vals,cur,lab){{return `<div class="opt"><span>${{lab}}</span><div class="segs" role="group" aria-label="${{lab}}">${{vals.map(v=>`<button type="button" data-o="${{name}}" data-v="${{v[0]}}" aria-pressed="${{String(v[0]==cur)}}">${{v[1]}}</button>`).join("")}}</div></div>`}}
function closePractice(){{if(!P)return;stopP();P.panel.hidden=true;P.panel.innerHTML="";P.btn.setAttribute("aria-expanded","false");P.btn.textContent="▶ Anhören & üben";P=null}}
async function togglePractice(n,lt,row){{
  const panel=document.getElementById("p-"+n),btn=row.querySelector(".practice");
  if(P&&P.n===n){{closePractice();return}}
  closePractice();
  const o=opts();P={{n,lt,panel,btn,o,i:0,r:0,timer:null,on:false,intro:false}};
  btn.setAttribute("aria-expanded","true");btn.textContent="Schließen";panel.hidden=false;
  panel.innerHTML=`<div class="ptop">
      ${{seg("rep",[[1,"1×"],[3,"3×"],[5,"5×"],[10,"10×"]],o.rep,"Jeden Vers wiederholen")}}
      ${{seg("echo",[[1,"An"],[0,"Aus"]],o.echo,"Pause zum Nachsprechen")}}
      ${{seg("loop",[[0,"1×"],[1,"Endlos"]],o.loop,"Ganze Sure")}}
      <div class="pbtns"><button type="button" class="go" data-a="play">▶ Start</button><button type="button" data-a="stop">⏹ Stopp</button></div>
    </div>
    <div class="pstat" aria-live="polite"></div>
    <div class="qtext"><div class="loadmsg">Sure wird geladen …</div></div>
    <div class="pfoot"><p>Rezitation: Scheich Muhammad Siddiq al-Minshawi (Murattal), abgespielt über das offene Audio-Angebot von Islamic Network. Quran-Text: alquran.cloud. Tippe auf einen Vers, um dort zu beginnen.</p>
    <a href="../index.html?sure=${{encodeURIComponent(lt)}}#anfrage">Sitzt die Sure? Beim Lehrer abhören lassen</a></div>`;
  panel.querySelectorAll("[data-o]").forEach(b=>b.addEventListener("click",()=>{{const k=b.dataset.o;P.o[k]=+b.dataset.v;saveOpts(P.o);
    panel.querySelectorAll(`[data-o="${{k}}"]`).forEach(x=>x.setAttribute("aria-pressed",String(x===b)))}}));
  panel.querySelector('[data-a="play"]').addEventListener("click",()=>{{P.on?pauseP():startP(P.i)}});
  panel.querySelector('[data-a="stop"]').addEventListener("click",()=>{{stopP();P.i=0;mark(-1)}});
  try{{
    const ay=await getText(n);if(!P||P.n!==n)return;
    const box=panel.querySelector(".qtext");
    box.innerHTML=(n!==1?`<div class="bsm" lang="ar">بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ</div>`:"")+ay.map((t,k)=>`<button type="button" class="ay" lang="ar" data-k="${{k}}">${{t}} <i>${{an(k+1)}}</i></button>`).join("");
    box.querySelectorAll(".ay").forEach(b=>b.addEventListener("click",()=>startP(+b.dataset.k,true)));
  }}catch(e){{const box=panel.querySelector(".qtext");box.innerHTML=`<div class="loadmsg">Der Text konnte gerade nicht geladen werden. Die Rezitation funktioniert trotzdem: tippe auf Start.</div>`}}
  panel.scrollIntoView({{behavior:matchMedia("(prefers-reduced-motion: reduce)").matches?"auto":"smooth",block:"nearest"}});
}}
function stat(h){{if(P)P.panel.querySelector(".pstat").innerHTML=h}}
function mark(k){{if(!P)return;P.panel.querySelectorAll(".ay").forEach(b=>b.classList.toggle("on",+b.dataset.k===k));const c=P.panel.querySelector(`.ay[data-k="${{k}}"]`);if(c&&k>=0)c.scrollIntoView({{block:"nearest"}})}}
function setBtn(){{if(P)P.panel.querySelector('[data-a="play"]').textContent=P.on?"❚❚ Pause":"▶ Weiter"}}
function playSrc(src,after){{clearTimeout(P.timer);audio.src=src;audio.onended=after;audio.play().catch(()=>{{P.on=false;setBtn();stat("Der Ton konnte nicht starten. Tippe noch einmal auf Start.")}})}}
function startP(k,fromClick){{
  if(!P)return;P.on=true;setBtn();
  if(fromClick||k===0&&P.r===0&&!P.started){{P.i=k;P.r=0}}
  const nV=VERSES[P.n];
  if(!P.started&&P.n!==1&&P.n!==9&&P.i===0){{P.started=true;stat("Basmala");mark(-1);playSrc(AU(1),()=>verse());return}}
  P.started=true;verse();
}}
function verse(){{
  if(!P||!P.on)return;const nV=VERSES[P.n];
  mark(P.i);stat(`Vers ${{P.i+1}} von ${{nV}} · ${{P.r+1}}. Mal von ${{P.o.rep}}`);
  playSrc(AU(G1[P.n]+P.i),()=>{{
    if(!P||!P.on)return;
    const go=()=>{{if(!P||!P.on)return;
      if(P.r+1<P.o.rep){{P.r++}}else{{P.r=0;P.i++}}
      if(P.i>=nV){{if(P.o.loop){{P.i=0}}else{{P.on=false;P.i=0;P.started=false;setBtn();P.panel.querySelector('[data-a="play"]').textContent="▶ Nochmal";mark(-1);stat("Geschafft! Kannst du die Sure schon allein? Dann hake sie oben ab.");return}}}}
      verse()}};
    if(P.o.echo){{const ms=Math.max(1500,(audio.duration||3)*1000*1.1);stat(`<span class="you">Jetzt du!</span> Sprich Vers ${{P.i+1}} nach`);P.timer=setTimeout(go,ms)}}else go();
  }});
}}
function pauseP(){{if(!P)return;P.on=false;audio.pause();clearTimeout(P.timer);setBtn();stat("Pausiert")}}
function stopP(){{if(!P)return;P.on=false;P.started=false;P.r=0;audio.pause();clearTimeout(P.timer);setBtn();if(P.panel.querySelector('[data-a="play"]'))P.panel.querySelector('[data-a="play"]').textContent="▶ Start";stat("")}}
function upd(){{
  let all=0;
  document.querySelectorAll(".stage").forEach((sec,si)=>{{
    const rows=[...sec.querySelectorAll(".row")];let c=0;
    rows.forEach(r=>{{const ok=!!done[r.dataset.n];r.classList.toggle("done",ok);if(ok)c++}});
    all+=c;sec.querySelector(".sc").textContent=c+"/"+rows.length;
    sec.querySelector(".sbar u").style.width=(c/rows.length*100)+"%";
    sec.querySelector(".award").hidden=c<rows.length;
  }});
  document.getElementById("cnt").textContent=all;
  document.getElementById("arc").style.strokeDashoffset=326.7*(1-all/TOTAL);
}}
upd();
</script>
</body>
</html>'''
open(f'{S}/abrar-website/suren/index.html','w',encoding='utf-8').write(html)
print('ok',len(html))
