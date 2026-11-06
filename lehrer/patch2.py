P='/tmp/claude-0/-home-claude/133ba4ae-4316-560e-9041-7dc80082bb1c/scratchpad/abrar-website/index.html'
s=open(P,encoding='utf-8').read()
# alten Abschnitt + altes Script entfernen
a=s.index('<section class="block lehrer" id="unterricht">'); b=s.index('<section class="block games" id="spiele">')
s=s[:a]+'@@SEC@@'+s[b:]
ja=s.index("\n<script>\n(function(){\n  var seg=document.querySelectorAll('#split")
jb=s.index('})();\n</script>\n',ja)+len('})();\n</script>\n')
s=s[:ja]+'@@JS@@'+s[jb:]

SUREN=[("الفاتحة","Al-Fatiha",1),("الناس","An-Nas",114),("الفلق","Al-Falaq",113),("الإخلاص","Al-Ichlas",112),("المسد","Al-Masad",111),("النصر","An-Nasr",110),("الكافرون","Al-Kafirun",109),("الكوثر","Al-Kauthar",108),("الماعون","Al-Maun",107),("قريش","Quraisch",106),("الفيل","Al-Fil",105),("الهمزة","Al-Humaza",104),("العصر","Al-Asr",103),("التكاثر","At-Takathur",102),("القارعة","Al-Qaria",101),("العاديات","Al-Adiyat",100),("الزلزلة","Az-Zalzala",99),("البينة","Al-Bayyina",98),("القدر","Al-Qadr",97),("العلق","Al-Alaq",96)]
opts=''.join(f'<option value="{t}">{n}. {t}</option>' for a_,t,n in SUREN)

CSS=r'''
/* ---------- Erweiterung: Familie, Lesetest, Suren, Gutschein ---------- */
.pers{margin-top:2px}
.pers .seg{grid-template-columns:repeat(3,1fr)}
.pers .seg button{display:flex;flex-direction:column;align-items:center;gap:1px;line-height:1.2}
.pers .seg button small{font-family:var(--f-body);font-weight:700;font-size:12px;opacity:.8}
.offer .price .per{display:block;width:100%;font-size:14px;font-weight:700;color:var(--muted)}
.more{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:28px}
.mini{display:flex;flex-direction:column;gap:12px;border:2px solid var(--line);border-radius:24px;padding:24px;background:var(--bg);min-width:0}
.mini .tag{align-self:flex-start;font-family:var(--f-display);font-weight:800;font-size:12px;letter-spacing:.08em;text-transform:uppercase;border-radius:999px;padding:4px 11px;background:var(--teal-soft);color:var(--teal)}
.mini.gift .tag{background:var(--fox-soft);color:var(--fox)}
.mini h3{font-family:var(--f-display);font-size:21px;line-height:1.25;margin:0;text-wrap:balance}
.mini p{margin:0;color:var(--muted)}
.mini .go{margin-top:auto;font-family:var(--f-display);font-weight:800;color:var(--plum);text-decoration:none;display:inline-flex;align-items:center;gap:6px}
.mini .go:hover{text-decoration:underline}
.mini .vis{border-radius:16px;background:var(--tint);padding:14px;display:flex;align-items:center;gap:14px;min-height:96px}
.clock{position:relative;width:64px;height:64px;flex:none;border-radius:50%;background:conic-gradient(var(--teal) 0 60deg,var(--teal-soft) 60deg 360deg);display:grid;place-items:center}
.clock::after{content:"";position:absolute;inset:9px;border-radius:50%;background:var(--bg)}
.clock b{position:relative;z-index:1;font-family:var(--f-display);font-size:15px;color:var(--teal)}
.vis .lines{display:grid;gap:7px;flex:1}
.vis .lines i{display:block;height:8px;border-radius:4px;background:var(--line)}
.vis .lines i:nth-child(2){width:80%}.vis .lines i:nth-child(3){width:60%;background:var(--teal)}
.surchips{display:flex;flex-wrap:wrap;gap:6px;direction:rtl}
.surchips span{font-family:var(--f-ar);font-size:15px;line-height:1.2;padding:5px 9px;border-radius:10px;background:var(--bg);border:2px solid var(--line)}
.surchips span.ok{border-color:var(--teal);color:var(--teal)}
.voucher{position:relative;flex:1;border:2px dashed var(--fox);border-radius:14px;padding:12px 14px;background:var(--bg);display:grid;gap:2px}
.voucher::before,.voucher::after{content:"";position:absolute;top:50%;width:14px;height:14px;border-radius:50%;background:var(--tint);transform:translateY(-50%)}
.voucher::before{left:-9px}.voucher::after{right:-9px}
.voucher small{font-weight:800;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--fox)}
.voucher b{font-family:var(--f-display);font-size:17px}
.voucher span{font-size:13px;color:var(--muted)}
.voucher .ar{position:absolute;right:14px;top:8px;font-size:20px;color:var(--fox)}
form.rf fieldset.five{grid-template-columns:repeat(3,1fr)}
@media (max-width:960px){.more{grid-template-columns:1fr 1fr}.more .mini:last-child{grid-column:1/-1}}
@media (max-width:640px){.more{grid-template-columns:1fr}form.rf fieldset.five{grid-template-columns:1fr 1fr}}
'''
s=s.replace('</style>',CSS+'</style>',1)

ICON_CERT='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="9" r="5"/><path d="M9 13.5 7.5 21l4.5-2.5 4.5 2.5L15 13.5"/></svg>'
ICON_VID='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="6" width="13" height="12" rx="3"/><path d="m16 10 5-3v10l-5-3"/></svg>'
ICON_CAL='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="16" rx="3"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>'

SEC=f'''<section class="block lehrer" id="unterricht"><div class="wrap">
  <span class="kicker">Lernen mit Lehrer</span>
  <h2>Lies nicht allein: ein Lehrer hört dir zu</h2>
  <p class="intro">Das Buch sagt es selbst: Die Erklärungen helfen, aber lesen lernt man mit einem Lehrer. Bei uns liest du mit einem zertifizierten Lehrer mit Abschluss, im Einzelunterricht und online.</p>
  <div class="trust">
    <span>{ICON_CERT}Zertifizierter Lehrer mit Abschluss</span>
    <span>{ICON_VID}Einzelunterricht online</span>
    <span>{ICON_CAL}Termine nach Absprache</span>
  </div>

  <div class="offers">
    <article class="offer fat" aria-labelledby="fat-h">
      <span class="badge">Kostenlos für alle</span>
      <h3 id="fat-h">Fatiha-Check: Rezitiere deine Fatiha und lass sie prüfen</h3>
      <div class="fatbox">
        <p class="bism ar" lang="ar">بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ</p>
        <div class="ayat" aria-hidden="true"><i style="--k:0">١</i><i style="--k:1">٢</i><i style="--k:2">٣</i><i style="--k:3">٤</i><i style="--k:4">٥</i><i style="--k:5">٦</i><i style="--k:6">٧</i></div>
        <small>Sura al-Fatiha · 7 Verse · in jeder Gebetseinheit</small>
      </div>
      <p>Die Fatiha ist eine Säule des Gebets. Du sprichst sie in jeder Gebetseinheit, deshalb soll sie richtig sitzen. Buch dir einen freien Termin, trag sie unserem Lehrer vor und erfahre, ob alles in Ordnung ist.</p>
      <ol class="howto">
        <li><div><b>Termin anfragen</b><span>Nimm den nächsten freien Termin beim Lehrer.</span></div></li>
        <li><div><b>Fatiha rezitieren</b><span>Du liest sie dem Lehrer online vor, so wie du sie im Gebet sprichst.</span></div></li>
        <li><div><b>Rückmeldung bekommen</b><span>Der Lehrer sagt dir, was schon richtig ist und was du verbessern kannst.</span></div></li>
      </ol>
      <div class="price"><b>0 €</b><span>für jeden, jedes Alter</span></div>
      <a class="btn pri" href="#anfrage" data-pick="fatiha">Kostenlosen Termin anfragen</a>
    </article>

    <article class="offer pack" aria-labelledby="pack-h">
      <span class="badge">Das ganze Buch</span>
      <h3 id="pack-h">Mit Lehrer durch das ganze Buch</h3>
      <p>Ein zertifizierter Lehrer geht das komplette Buch mit dir durch: vom Alphabet über Harakat, Madd und Tanwin bis zu den Pausenzeichen. Mit Übungen, Hausaufgaben und Korrektur.</p>
      <div class="split pers" id="pers">
        <div class="lbl">Wie viele lernen mit?<span>Geschwister und Familie lernen zusammen</span></div>
        <div class="seg" role="group" aria-label="Anzahl der Personen">
          <button type="button" data-p="1" aria-pressed="true">1 Person<small>149 €</small></button>
          <button type="button" data-p="2" aria-pressed="false">2 Personen<small>259 €</small></button>
          <button type="button" data-p="3" aria-pressed="false">3 Personen<small>349 €</small></button>
        </div>
      </div>
      <div class="price"><b id="packPrice">149 €</b><span id="packSub">einmalig, für alle Kapitel</span></div>
      <div class="split" id="split">
        <div class="lbl">Teile deine 9 Stunden auf<span id="splitHint">so wie es dir passt</span></div>
        <div class="seg" role="group" aria-label="Länge einer Unterrichtseinheit">
          <button type="button" data-min="30" aria-pressed="false">30 Min.</button>
          <button type="button" data-min="45" aria-pressed="true">45 Min.</button>
          <button type="button" data-min="60" aria-pressed="false">60 Min.</button>
        </div>
        <div class="blocks" id="blocks" aria-hidden="true"></div>
        <div class="res" id="splitRes" aria-live="polite">12 Termine à 45 Minuten<small>z. B. einmal pro Woche: in 12 Wochen durch das Buch</small></div>
      </div>
      <ul class="howto">
        <li><div><b>Einzel- oder Familienunterricht online</b><span>Nur ihr und der Lehrer, per Video.</span></div></li>
        <li><div><b>Stunden frei einteilen</b><span>Kurze Einheiten für Kinder, längere für Erwachsene.</span></div></li>
        <li><div><b>Urkunde zum Abschluss</b><span>Für jeden, der das Buch geschafft hat.</span></div></li>
      </ul>
      <a class="btn pri" href="#anfrage" data-pick="buch">Lehrer für das Buch buchen</a>
    </article>
  </div>

  <div class="more">
    <article class="mini" aria-labelledby="lt-h">
      <span class="tag">Kostenlos · 10 Minuten</span>
      <div class="vis" aria-hidden="true"><span class="clock"><b>10′</b></span><span class="lines"><i></i><i></i><i></i></span></div>
      <h3 id="lt-h">Lesetest: Wo stehst du gerade?</h3>
      <p>Du liest dem Lehrer ein paar Zeilen vor. Danach weißt du, mit welchem Kapitel im Buch du am besten startest.</p>
      <a class="go" href="#anfrage" data-pick="lesetest">Lesetest anfragen →</a>
    </article>
    <article class="mini" aria-labelledby="su-h">
      <span class="tag">Kostenlos · 20 Suren</span>
      <div class="vis" aria-hidden="true"><div class="surchips"><span class="ok">الفاتحة</span><span class="ok">الناس</span><span class="ok">الفلق</span><span>الإخلاص</span><span>المسد</span><span>النصر</span></div></div>
      <h3 id="su-h">Kurze Suren lernen und abhören lassen</h3>
      <p>20 kurze Suren in 5 Stufen zum Abhaken. Jede Sure kannst du kostenlos beim Lehrer vortragen, und für jede Stufe gibt es eine Urkunde.</p>
      <a class="go" href="suren/index.html">Zu den kurzen Suren →</a>
    </article>
    <article class="mini gift" aria-labelledby="gs-h">
      <span class="tag">Zum Verschenken</span>
      <div class="vis" aria-hidden="true"><div class="voucher"><span class="ar">هَدِيَّة</span><small>Gutschein</small><b>Quran lesen lernen</b><span>9 Stunden mit Lehrer · für Yusuf</span></div></div>
      <h3 id="gs-h">Das Lehrer-Paket als Gutschein</h3>
      <p>Ein Geschenk mit Bedeutung, zum Beispiel zu Eid, zum Geburtstag oder für die ganze Familie. Wir schicken dir den Gutschein mit dem Namen der beschenkten Person.</p>
      <a class="go" href="#anfrage" data-pick="gutschein">Gutschein anfragen →</a>
    </article>
  </div>

  <div class="req" id="anfrage">
    <div class="side">
      <h3>Termin anfragen</h3>
      <p>Schreib uns, was du möchtest und wann du Zeit hast. Wir melden uns mit Terminvorschlägen.</p>
      <p>Beim Absenden öffnet sich dein E-Mail-Programm mit der fertigen Nachricht. Du kannst uns auch direkt schreiben:</p>
      <div class="mail"><code id="mailAddr">info@abrarlearning.com</code><button type="button" id="copyMail">Kopieren</button></div>
    </div>
    <form class="rf" id="rf" novalidate>
      <fieldset class="full five">
        <legend>Was möchtest du?</legend>
        <label class="opt"><input type="radio" name="angebot" id="o-fatiha" value="fatiha" checked><span>Fatiha-Check<small>kostenlos</small></span></label>
        <label class="opt"><input type="radio" name="angebot" id="o-lesetest" value="lesetest"><span>Lesetest<small>kostenlos</small></span></label>
        <label class="opt"><input type="radio" name="angebot" id="o-sure" value="sure"><span>Sure abhören<small>kostenlos</small></span></label>
        <label class="opt"><input type="radio" name="angebot" id="o-buch" value="buch"><span>Das ganze Buch<small>ab 149 €</small></span></label>
        <label class="opt"><input type="radio" name="angebot" id="o-gutschein" value="gutschein"><span>Gutschein<small>ab 149 €</small></span></label>
      </fieldset>
      <label class="f" for="r-name">Name<input type="text" id="r-name" name="name" autocomplete="name" required></label>
      <label class="f" for="r-mail">E-Mail<input type="email" id="r-mail" name="email" autocomplete="email" required></label>
      <label class="f" for="r-wer" id="werWrap">Für wen?<select id="r-wer" name="wer"><option>Für mich</option><option>Für mein Kind</option><option>Für mehrere Personen</option></select></label>
      <label class="f" for="r-sure" id="sureWrap" hidden>Welche Sure?<select id="r-sure" name="sure">{opts}</select></label>
      <label class="f" for="r-for" id="giftWrap" hidden>Name der beschenkten Person<input type="text" id="r-for" name="beschenkt"></label>
      <label class="f" for="r-pers" id="persWrap" hidden>Personen<select id="r-pers" name="personen"><option value="1">1 Person · 149 €</option><option value="2">2 Personen · 259 €</option><option value="3">3 Personen · 349 €</option></select></label>
      <label class="f" for="r-len" id="lenWrap" hidden>Einheiten<select id="r-len" name="laenge"><option value="30">18 × 30 Minuten</option><option value="45" selected>12 × 45 Minuten</option><option value="60">9 × 60 Minuten</option></select></label>
      <label class="f full" for="r-zeit" id="zeitLbl">Wann hast du Zeit?<textarea id="r-zeit" name="zeit" placeholder="z. B. Montag und Mittwoch ab 18 Uhr, Samstag vormittags"></textarea></label>
      <div class="full send">
        <button class="btn pri" type="submit">Anfrage senden</button>
        <p class="note">Wir nutzen deine Angaben nur, um dir Termine vorzuschlagen.</p>
      </div>
      <p class="rstatus" id="rstatus" role="status" hidden></p>
    </form>
  </div>
</div></section>
'''
JS=r'''
<script>
(function(){
  var $=function(i){return document.getElementById(i)};
  var PRICE={1:149,2:259,3:349};
  var seg=document.querySelectorAll('#split .seg button'),blocks=$('blocks'),res=$('splitRes');
  var info={30:['18 Termine à 30 Minuten','ideal für Kinder: zweimal pro Woche, in 9 Wochen durch das Buch'],45:['12 Termine à 45 Minuten','z. B. einmal pro Woche: in 12 Wochen durch das Buch'],60:['9 Termine à 60 Minuten','für Erwachsene: einmal pro Woche, in 9 Wochen durch das Buch']};
  function setLen(m){
    seg.forEach(function(b){b.setAttribute('aria-pressed',String(b.dataset.min==m))});
    var n=540/m;blocks.innerHTML='';
    for(var k=0;k<n;k++){var e=document.createElement('i');e.style.width=(m*0.55)+'px';blocks.appendChild(e)}
    res.innerHTML=info[m][0]+'<small>'+info[m][1]+'</small>';$('r-len').value=String(m);
  }
  seg.forEach(function(b){b.addEventListener('click',function(){setLen(+b.dataset.min)})});
  var pseg=document.querySelectorAll('#pers .seg button');
  function setPers(p){
    pseg.forEach(function(b){b.setAttribute('aria-pressed',String(b.dataset.p==p))});
    $('packPrice').textContent=PRICE[p]+' €';
    $('packSub').innerHTML=p==1?'einmalig, für alle Kapitel':'zusammen, für alle Kapitel <span class="per">das sind '+Math.round(PRICE[p]/p)+' € pro Person</span>';
    $('r-pers').value=String(p);
  }
  pseg.forEach(function(b){b.addEventListener('click',function(){setPers(+b.dataset.p)})});
  setLen(45);setPers(1);

  function pick(v){
    var r=$('o-'+v);if(r)r.checked=true;
    var paid=v==='buch'||v==='gutschein';
    $('lenWrap').hidden=!paid;$('persWrap').hidden=!paid;
    $('sureWrap').hidden=v!=='sure';$('giftWrap').hidden=v!=='gutschein';
    $('werWrap').hidden=v==='gutschein';
    $('zeitLbl').firstChild.nodeValue=v==='gutschein'?'Nachricht (z. B. Anlass, gewünschtes Datum)':'Wann hast du Zeit?';
  }
  document.querySelectorAll('input[name=angebot]').forEach(function(r){r.addEventListener('change',function(){pick(r.value)})});
  document.querySelectorAll('[data-pick]').forEach(function(a){a.addEventListener('click',function(){pick(a.dataset.pick)})});
  try{var q=new URLSearchParams(location.search);var su=q.get('sure');if(su){pick('sure');$('r-sure').value=su}else if(q.get('angebot')){pick(q.get('angebot'))}}catch(e){}

  var addr='info@abrarlearning.com',st=$('rstatus');
  $('copyMail').addEventListener('click',function(){var b=this;function sel(){var r=document.createRange();r.selectNodeContents($('mailAddr'));var s=getSelection();s.removeAllRanges();s.addRange(r)}
    try{navigator.clipboard.writeText(addr).then(function(){b.textContent='Kopiert'},sel)}catch(e){sel()}});
  $('rf').addEventListener('submit',function(ev){
    ev.preventDefault();
    var f=ev.target,name=f.name.value.trim(),mail=f.email.value.trim(),v=f.angebot.value;
    if(!name||!/^\S+@\S+\.\S+$/.test(mail)){st.hidden=false;st.innerHTML='<b>Bitte Name und eine gültige E-Mail-Adresse eintragen.</b>Dann können wir dir antworten.';(name?f.email:f.name).focus();return}
    var m=f.laenge.value,p=+f.personen.value,pack=(540/m)+' × '+m+' Minuten, '+p+(p>1?' Personen':' Person')+' ('+PRICE[p]+' €)';
    var zeit=f.zeit.value.trim();
    var T={
      fatiha:['Anfrage: Kostenloser Fatiha-Check','meine Fatiha beim kostenlosen Fatiha-Check rezitieren und überprüfen lassen.'],
      lesetest:['Anfrage: Kostenloser Lesetest','einen kostenlosen Lesetest machen, um zu wissen, mit welchem Kapitel ich starten soll.'],
      sure:['Anfrage: Sure abhören lassen ('+f.sure.value+')','die Sure '+f.sure.value+' kostenlos beim Lehrer vortragen und abhören lassen.'],
      buch:['Anfrage: Mit Lehrer durch das ganze Buch ('+PRICE[p]+' €)','mit einem Lehrer das ganze Buch „Quran lesen lernen – Schritt für Schritt“ durchgehen.\nPaket: '+pack],
      gutschein:['Anfrage: Gutschein Lehrer-Paket ('+PRICE[p]+' €)','das Lehrer-Paket als Gutschein verschenken.\nFür: '+(f.beschenkt.value.trim()||'(Name folgt)')+'\nPaket: '+pack]
    }[v];
    var body='Assalamu alaikum,\n\nich möchte '+T[1]+'\n'+(v!=='gutschein'?'Für: '+f.wer.value+'\nZeit: '+(zeit||'flexibel'):'Nachricht: '+(zeit||'-'))+'\n\nName: '+name+'\nE-Mail: '+mail+'\n';
    st.hidden=false;
    st.innerHTML='<b>Dein E-Mail-Programm öffnet sich mit der fertigen Nachricht. Bitte dort auf Senden tippen.</b>Falls sich nichts öffnet, kopiere den Text und schick ihn an '+addr+':<pre></pre>';
    st.querySelector('pre').textContent='Betreff: '+T[0]+'\n\n'+body;
    window.location.href='mailto:'+addr+'?subject='+encodeURIComponent(T[0])+'&body='+encodeURIComponent(body);
  });
})();
</script>
'''
s=s.replace('@@SEC@@',SEC).replace('@@JS@@',JS)
s=s.replace('<span class="pill">Neu</span>Kostenloser Fatiha-Check mit unserem Lehrer','<span class="pill">Neu</span>Kostenlos: Fatiha-Check, Lesetest und kurze Suren abhören')
# Footer-Link
s=s.replace('<li><a href="buch/index.html">Buch online lesen</a></li>','<li><a href="buch/index.html">Buch online lesen</a></li><li><a href="#unterricht">Lernen mit Lehrer</a></li><li><a href="suren/index.html">Kurze Suren lernen</a></li>',1)
open(P,'w',encoding='utf-8').write(s)
print('ok')
