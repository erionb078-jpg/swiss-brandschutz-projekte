import re,sys
P='/tmp/claude-0/-home-claude/133ba4ae-4316-560e-9041-7dc80082bb1c/scratchpad/abrar-website/index.html'
s=open(P,encoding='utf-8').read()
assert 'id="unterricht"' not in s

CSS=r'''
/* ---------- Unterricht mit Lehrer ---------- */
.annc{display:flex;justify-content:center;padding:12px max(20px,env(safe-area-inset-right,0px)) 12px max(20px,env(safe-area-inset-left,0px));background:var(--teal-soft)}
.annc a{display:inline-flex;align-items:center;gap:10px;flex-wrap:wrap;justify-content:center;text-align:center;color:var(--ink);text-decoration:none;font-weight:700}
.annc .pill{background:var(--teal);color:#fff;border-radius:999px;padding:3px 10px;font-size:12px;letter-spacing:.06em;text-transform:uppercase;font-family:var(--f-display)}
.annc a span.go{color:var(--teal);font-family:var(--f-display)}
.annc a:hover span.go{text-decoration:underline}
.lehrer{background:linear-gradient(var(--tint),var(--bg))}
.lehrer .trust{display:flex;flex-wrap:wrap;gap:10px;margin-top:18px}
.lehrer .trust span{display:inline-flex;align-items:center;gap:8px;border:2px solid var(--line);background:var(--bg);border-radius:999px;padding:7px 14px;font-weight:700;font-size:14px}
.lehrer .trust svg{width:18px;height:18px;flex:none;color:var(--teal)}
.offers{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:36px;align-items:stretch}
.offer{position:relative;display:flex;flex-direction:column;gap:16px;border-radius:28px;padding:30px;min-width:0;background:var(--bg);border:2px solid var(--line)}
.offer.fat{border-color:var(--teal);box-shadow:0 10px 0 var(--teal-soft)}
.offer.pack{border-color:var(--plum);box-shadow:0 10px 0 var(--tint-2)}
.offer .badge{align-self:flex-start;font-family:var(--f-display);font-weight:800;font-size:12px;letter-spacing:.08em;text-transform:uppercase;border-radius:999px;padding:5px 12px}
.offer.fat .badge{background:var(--teal);color:#fff}
.offer.pack .badge{background:var(--plum);color:var(--bg)}
.offer h3{font-family:var(--f-display);font-size:clamp(22px,2.6vw,28px);line-height:1.2;margin:0;text-wrap:balance}
.offer p{margin:0;color:var(--muted)}
.offer .price{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}
.offer .price b{font-family:var(--f-display);font-weight:800;font-size:clamp(40px,5vw,54px);line-height:1;font-variant-numeric:tabular-nums}
.offer.fat .price b{color:var(--teal)}
.offer.pack .price b{color:var(--plum)}
.offer .price span{color:var(--muted);font-weight:700}
.fatbox{border-radius:20px;background:var(--teal-soft);padding:18px 16px 16px;text-align:center}
.fatbox .bism{font-size:clamp(24px,3.2vw,32px);line-height:1.7;color:var(--ink);margin:0}
.ayat{display:flex;justify-content:center;gap:8px;margin-top:10px;flex-wrap:wrap}
.ayat i{font-style:normal;width:34px;height:34px;border-radius:50%;display:grid;place-items:center;font-family:var(--f-ar);font-size:17px;background:var(--bg);color:var(--teal);border:2px solid var(--teal);animation:ayah 7s infinite;animation-delay:calc(var(--k)*1s)}
@keyframes ayah{0%,8%{background:var(--teal);color:#fff}14%,100%{background:var(--bg);color:var(--teal)}}
.fatbox small{display:block;margin-top:10px;color:var(--muted);font-weight:700}
.howto{list-style:none;margin:0;padding:0;display:grid;gap:10px;counter-reset:h}
.howto li{display:grid;grid-template-columns:30px 1fr;gap:12px;align-items:start}
.howto li::before{counter-increment:h;content:counter(h);width:30px;height:30px;border-radius:10px;display:grid;place-items:center;font-family:var(--f-display);font-weight:800;background:var(--teal-soft);color:var(--teal)}
.offer.pack .howto li::before{content:"✓";background:var(--tint-2);color:var(--plum)}
.howto b{display:block}
.howto span{color:var(--muted);font-size:15px}
.split{border-radius:20px;background:var(--tint);padding:18px}
.split .lbl{display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap;font-weight:800;font-size:14px;margin-bottom:10px}
.split .lbl span{color:var(--muted);font-weight:700}
.seg{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;background:var(--bg);border:2px solid var(--line);border-radius:14px;padding:4px}
.seg button{font:inherit;font-family:var(--f-display);font-weight:700;font-size:15px;border:0;border-radius:10px;padding:9px 6px;background:transparent;color:var(--ink);cursor:pointer}
.seg button[aria-pressed="true"]{background:var(--plum);color:var(--bg)}
.seg button:focus-visible{outline:2px solid var(--plum);outline-offset:2px}
.blocks{display:flex;flex-wrap:wrap;gap:5px;margin:14px 0 10px}
.blocks i{height:16px;border-radius:5px;background:var(--plum);opacity:.85;transition:width .3s}
.split .res{font-family:var(--f-display);font-weight:800;font-size:18px}
.split .res small{display:block;font-family:var(--f-body);font-weight:700;font-size:14px;color:var(--muted);margin-top:2px}
.offer .btn{align-self:flex-start;margin-top:auto}
.offer.fat .btn.pri{background:var(--teal);box-shadow:0 4px 0 #0d5f57;color:#fff}
/* Anfrage */
.req{margin-top:48px;display:grid;grid-template-columns:.8fr 1.2fr;gap:32px;border:2px solid var(--line);border-radius:28px;padding:32px;background:var(--bg)}
.req h3{font-family:var(--f-display);font-size:clamp(22px,2.6vw,28px);margin:0 0 10px}
.req .side p{color:var(--muted);margin:0 0 14px}
.req .mail{display:flex;align-items:center;gap:8px;flex-wrap:wrap;font-weight:800}
.req .mail code{font-family:var(--f-body);font-size:16px;background:var(--tint);border-radius:10px;padding:6px 10px;user-select:all}
.req .mail button{font:inherit;font-size:14px;font-weight:700;border:2px solid var(--line);border-radius:10px;background:var(--bg);color:var(--plum);padding:5px 10px;cursor:pointer}
form.rf{display:grid;grid-template-columns:1fr 1fr;gap:14px;min-width:0}
form.rf .full{grid-column:1/-1}
form.rf fieldset{border:0;margin:0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:10px}
form.rf legend{font-weight:800;font-size:14px;margin-bottom:8px;padding:0}
.opt{position:relative;display:block;cursor:pointer}
.opt input{position:absolute;opacity:0;pointer-events:none}
.opt span{display:flex;flex-direction:column;gap:2px;border:2px solid var(--line);border-radius:16px;padding:12px 14px;font-weight:800;transition:border-color .15s,background .15s}
.opt span small{font-weight:700;color:var(--muted)}
.opt input:checked+span{border-color:var(--plum);background:var(--tint)}
.opt input:focus-visible+span{outline:2px solid var(--plum);outline-offset:2px}
form.rf label.f{display:grid;gap:6px;font-weight:800;font-size:14px;min-width:0}
form.rf input[type=text],form.rf input[type=email],form.rf input[type=tel],form.rf select,form.rf textarea{font:inherit;font-weight:400;font-size:16px;color:var(--ink);background:var(--bg);border:2px solid var(--line);border-radius:12px;padding:11px 12px;width:100%;min-width:0}
form.rf textarea{min-height:92px;resize:vertical}
form.rf input:focus,form.rf select:focus,form.rf textarea:focus{outline:none;border-color:var(--plum)}
form.rf .note{font-size:13px;color:var(--muted);margin:0}
form.rf .send{display:flex;align-items:center;gap:14px;flex-wrap:wrap}
form.rf .send .btn{border:0;cursor:pointer}
.rstatus{grid-column:1/-1;border-radius:16px;background:var(--teal-soft);padding:14px 16px;margin:0}
.rstatus b{display:block;margin-bottom:4px}
.rstatus pre{white-space:pre-wrap;font-family:var(--f-body);font-size:14px;margin:8px 0 0;background:var(--bg);border-radius:10px;padding:10px;max-height:180px;overflow:auto}
@media (max-width:860px){.offers,.req{grid-template-columns:1fr}.req{padding:22px}}
@media (max-width:520px){form.rf,form.rf fieldset{grid-template-columns:1fr}.offer{padding:22px}}
@media (prefers-reduced-motion:reduce){.ayat i{animation:none}.blocks i{transition:none}}
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
      <div class="price"><b>149 €</b><span>einmalig, für alle Kapitel</span></div>
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
        <li><div><b>Einzelunterricht online</b><span>Nur du und der Lehrer, per Video.</span></div></li>
        <li><div><b>Stunden frei einteilen</b><span>Kurze Einheiten für Kinder, längere für Erwachsene.</span></div></li>
        <li><div><b>Urkunde zum Abschluss</b><span>Wenn du das Buch geschafft hast.</span></div></li>
      </ul>
      <a class="btn pri" href="#anfrage" data-pick="buch">Lehrer für das Buch buchen</a>
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
      <fieldset class="full">
        <legend>Was möchtest du?</legend>
        <label class="opt"><input type="radio" name="angebot" id="o-fatiha" value="fatiha" checked><span>Fatiha-Check<small>kostenlos</small></span></label>
        <label class="opt"><input type="radio" name="angebot" id="o-buch" value="buch"><span>Das ganze Buch<small>149 €</small></span></label>
      </fieldset>
      <label class="f" for="r-name">Name<input type="text" id="r-name" name="name" autocomplete="name" required></label>
      <label class="f" for="r-mail">E-Mail<input type="email" id="r-mail" name="email" autocomplete="email" required></label>
      <label class="f" for="r-wer">Für wen?<select id="r-wer" name="wer"><option>Für mich</option><option>Für mein Kind</option><option>Für mehrere Personen</option></select></label>
      <label class="f" for="r-len" id="lenWrap" hidden>Einheiten<select id="r-len" name="laenge"><option value="30">18 × 30 Minuten</option><option value="45" selected>12 × 45 Minuten</option><option value="60">9 × 60 Minuten</option></select></label>
      <label class="f full" for="r-zeit">Wann hast du Zeit?<textarea id="r-zeit" name="zeit" placeholder="z. B. Montag und Mittwoch ab 18 Uhr, Samstag vormittags"></textarea></label>
      <div class="full send">
        <button class="btn pri" type="submit">Anfrage senden</button>
        <p class="note">Wir nutzen deine Angaben nur, um dir Termine vorzuschlagen.</p>
      </div>
      <p class="rstatus" id="rstatus" role="status" hidden></p>
    </form>
  </div>
</div></section>
'''
anchor='<section class="block games" id="spiele">'
assert anchor in s
s=s.replace(anchor,SEC+anchor,1)

# Nav-Link
s=s.replace('<nav aria-label="Hauptmenü"><a href="#buch">Das Buch</a>','<nav aria-label="Hauptmenü"><a href="#buch">Das Buch</a><a href="#unterricht">Mit Lehrer</a>',1)
# Ankündigung unter den Fakten
fe='<div class="facts"><div class="wrap">'
i=s.index(fe); j=s.index('</div></div>',i)+len('</div></div>')
s=s[:j]+'\n<div class="annc"><a href="#unterricht"><span class="pill">Neu</span>Kostenloser Fatiha-Check mit unserem Lehrer <span class="go">Termin anfragen →</span></a></div>\n'+s[j:]

JS=r'''
<script>
(function(){
  var seg=document.querySelectorAll('#split .seg button'),blocks=document.getElementById('blocks'),res=document.getElementById('splitRes'),len=document.getElementById('r-len');
  var info={30:['18 Termine à 30 Minuten','ideal für Kinder: zweimal pro Woche, in 9 Wochen durch das Buch'],45:['12 Termine à 45 Minuten','z. B. einmal pro Woche: in 12 Wochen durch das Buch'],60:['9 Termine à 60 Minuten','für Erwachsene: einmal pro Woche, in 9 Wochen durch das Buch']};
  function set(m){
    seg.forEach(function(b){b.setAttribute('aria-pressed',String(b.dataset.min==m))});
    var n=540/m;blocks.innerHTML='';
    for(var k=0;k<n;k++){var e=document.createElement('i');e.style.width=(m*0.55)+'px';blocks.appendChild(e)}
    res.innerHTML=info[m][0]+'<small>'+info[m][1]+'</small>';
    if(len)len.value=String(m);
  }
  seg.forEach(function(b){b.addEventListener('click',function(){set(+b.dataset.min)})});
  set(45);
  var lenWrap=document.getElementById('lenWrap');
  function pick(v){var r=document.getElementById(v==='buch'?'o-buch':'o-fatiha');if(r){r.checked=true}lenWrap.hidden=v!=='buch'}
  document.querySelectorAll('input[name=angebot]').forEach(function(r){r.addEventListener('change',function(){pick(r.value)})});
  document.querySelectorAll('[data-pick]').forEach(function(a){a.addEventListener('click',function(){pick(a.dataset.pick);if(a.dataset.pick==='buch'&&len){len.value=document.querySelector('#split .seg button[aria-pressed=true]').dataset.min}})});
  var addr='info@abrarlearning.com',st=document.getElementById('rstatus');
  document.getElementById('copyMail').addEventListener('click',function(){var b=this;try{navigator.clipboard.writeText(addr).then(function(){b.textContent='Kopiert'},function(){sel()})}catch(e){sel()}
    function sel(){var r=document.createRange();r.selectNodeContents(document.getElementById('mailAddr'));var s=getSelection();s.removeAllRanges();s.addRange(r)}});
  document.getElementById('rf').addEventListener('submit',function(ev){
    ev.preventDefault();
    var f=ev.target,name=f.name.value.trim(),mail=f.email.value.trim();
    if(!name||!/^\S+@\S+\.\S+$/.test(mail)){st.hidden=false;st.innerHTML='<b>Bitte Name und eine gültige E-Mail-Adresse eintragen.</b>Dann können wir dir antworten.';(name?f.email:f.name).focus();return}
    var buch=f.angebot.value==='buch',m=f.laenge.value;
    var subj=buch?'Anfrage: Mit Lehrer durch das ganze Buch (149 €)':'Anfrage: Kostenloser Fatiha-Check';
    var body='Assalamu alaikum,\n\nich möchte '+(buch?'mit einem Lehrer das ganze Buch „Quran lesen lernen – Schritt für Schritt“ durchgehen (149 €).\nEinteilung: '+(540/m)+' × '+m+' Minuten':'meine Fatiha beim kostenlosen Fatiha-Check rezitieren und überprüfen lassen.')+
      '\nFür: '+f.wer.value+'\nZeit: '+(f.zeit.value.trim()||'flexibel')+'\n\nName: '+name+'\nE-Mail: '+mail+'\n';
    var href='mailto:'+addr+'?subject='+encodeURIComponent(subj)+'&body='+encodeURIComponent(body);
    st.hidden=false;
    st.innerHTML='<b>Dein E-Mail-Programm öffnet sich mit der fertigen Nachricht. Bitte dort auf Senden tippen.</b>Falls sich nichts öffnet, kopiere den Text und schick ihn an '+addr+':<pre></pre>';
    st.querySelector('pre').textContent='Betreff: '+subj+'\n\n'+body;
    window.location.href=href;
  });
})();
</script>
'''
s=s.replace('</body>',JS+'</body>',1) if '</body>' in s else s+JS
open(P,'w',encoding='utf-8').write(s)
print('ok',len(s))
