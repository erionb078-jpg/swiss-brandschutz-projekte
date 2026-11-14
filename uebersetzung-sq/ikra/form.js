<script>
(function(){
  var $=function(i){return document.getElementById(i)};
  var MAIL='MAILADDR';
  var seg=document.querySelectorAll('#split .seg button'),res=$('splitRes');
  var info={30:['30 minuta','ideale për fëmijë 6–9 vjeç, mirë 2 herë në javë'],45:['45 minuta','për fëmijë 10–14 vjeç – më e zgjedhura'],60:['60 minuta','për të rinjtë dhe për texhvid ose bazat e fesë']};
  function setLen(m){
    seg.forEach(function(b){b.setAttribute('aria-pressed',String(b.dataset.min==m))});
    res.innerHTML=info[m][0]+'<small>'+info[m][1]+'</small>';$('r-len').value=String(m);
  }
  seg.forEach(function(b){b.addEventListener('click',function(){setLen(+b.dataset.min)})});
  setLen(45);

  function pick(v){
    var r=$('o-'+v);if(r)r.checked=true;
    var les=v==='mesim';
    ['fachWrap','lehrerWrap','lenWrap','oftWrap'].forEach(function(i){$(i).hidden=!les});
    $('sureWrap').hidden=v!=='sure';
  }
  document.querySelectorAll('input[name=angebot]').forEach(function(r){r.addEventListener('change',function(){pick(r.value)})});
  document.querySelectorAll('[data-pick]').forEach(function(a){a.addEventListener('click',function(){pick(a.dataset.pick)})});
  pick('mesim');
  try{var q=new URLSearchParams(location.search);var su=q.get('sure');if(su){pick('sure');$('r-sure').value=su}else if(q.get('angebot')){pick(q.get('angebot'))}}catch(e){}

  var st=$('rstatus');
  $('copyMail').addEventListener('click',function(){var b=this;function sel(){var r=document.createRange();r.selectNodeContents($('mailAddr'));var s=getSelection();s.removeAllRanges();s.addRange(r)}
    try{navigator.clipboard.writeText(MAIL).then(function(){b.textContent='U kopjua'},sel)}catch(e){sel()}});
  $('rf').addEventListener('submit',function(ev){
    ev.preventDefault();
    var f=ev.target,name=f.name.value.trim(),mail=f.email.value.trim(),v=f.angebot.value;
    if(!name||!/^\S+@\S+\.\S+$/.test(mail)){st.hidden=false;st.innerHTML='<b>Ju lutem shkruani emrin dhe një adresë e-maili të vlefshme.</b>Që të mund t\'ju përgjigjemi.';(name?f.email:f.name).focus();return}
    var zeit=f.zeit.value.trim(),alter=f.alter.value.trim();
    var T={
      mesim:['Kërkesë: Mësim me orë – '+f.fach.value,'mësim me orë te një hoxhë.\nLënda: '+f.fach.value+'\nHoxha: '+f.lehrer.value+'\nGjatësia e orës: '+f.laenge.value+' minuta\nSa shpesh: '+f.oft.value],
      lesetest:['Kërkesë: Testi falas i leximit','testin falas të leximit, për të ditur me çka të fillojmë.'],
      fatiha:['Kërkesë: Kontrolli falas i Fatihasë','ta lexojmë Fatihanë dhe ta kontrollojmë falas te hoxha.'],
      sure:['Kërkesë: Dëgjimi i sures ('+f.sure.value+')','ta lexojmë suren '+f.sure.value+' falas te hoxha dhe ai ta dëgjojë.']
    }[v];
    var body='Es-selamu alejkum,\n\ndëshirojmë '+T[1]+'\n\nPër: '+f.wer.value+(alter?'\nMosha: '+alter:'')+'\nKoha: '+(zeit||'fleksibël')+'\n\nEmri: '+name+'\nE-mail: '+mail+'\n';
    st.hidden=false;
    st.innerHTML='<b>Programi juaj i e-mailit hapet me mesazhin e gatshëm. Aty shtypni „Dërgo“.</b>Nëse nuk hapet asgjë, kopjoni tekstin dhe dërgojeni te '+MAIL+':<pre></pre>';
    st.querySelector('pre').textContent='Tema: '+T[0]+'\n\n'+body;
    window.location.href='mailto:'+MAIL+'?subject='+encodeURIComponent(T[0])+'&body='+encodeURIComponent(body);
  });
})();
</script>
