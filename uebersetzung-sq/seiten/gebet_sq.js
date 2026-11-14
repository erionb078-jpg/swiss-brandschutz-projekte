(function(){
const $=id=>document.getElementById(id);
const reduce=matchMedia("(prefers-reduced-motion: reduce)").matches;

/* ---------- Texte ---------- */
const TX={
 bism:{ar:["بِسْمِ اللَّهِ"],tr:"Bismil-lah",de:"Në emër të Allahut."},
 schahada:{ar:["أَشْهَدُ أَنْ لَا إِلَٰهَ إِلَّا اللَّهُ وَحْدَهُ لَا شَرِيكَ لَهُ","وَأَشْهَدُ أَنَّ مُحَمَّدًا عَبْدُهُ وَرَسُولُهُ"],tr:"Esh-hedu en la ilahe il-lallahu vahdehu la sherike leh, ve esh-hedu enne Muhammeden abduhu ve resuluh.",de:"Dëshmoj se nuk ka zot tjetër përveç Allahut, Një i Vetëm e pa shok, dhe dëshmoj se Muhammedi është robi dhe i dërguari i Tij."},
 takbir:{ar:["اللَّهُ أَكْبَرُ"],tr:"Allahu ekber",de:"Allahu është më i Madhi."},
 thana:{ar:["سُبْحَانَكَ اللَّهُمَّ وَبِحَمْدِكَ، وَتَبَارَكَ اسْمُكَ،","وَتَعَالَى جَدُّكَ، وَلَا إِلَٰهَ غَيْرُكَ"],tr:"Subhaneke Allahumme ve bihamdike, ve tebarekesmuke, ve teala xhedduke, ve la ilahe gajruk.",de:"I lartësuar je Ti, o Allah, dhe falënderimi është për Ty. I bekuar është emri Yt, e lartë është madhëria Jote dhe nuk ka zot tjetër përveç Teje."},
 auudhu:{ar:["أَعُوذُ بِاللَّهِ مِنَ الشَّيْطَانِ الرَّجِيمِ","بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"],tr:"Eudhu bil-lahi mine-sh-shejtani-r-raxhim. Bismil-lahi-r-rahmani-r-rahim.",de:"Kërkoj mbrojtje te Allahu nga shejtani i mallkuar. Në emër të Allahut, të Gjithëmëshirshmit, Mëshirëplotit."},
 fatiha:{ar:["الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ (٢) الرَّحْمَٰنِ الرَّحِيمِ (٣) مَالِكِ يَوْمِ الدِّينِ (٤)","إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ (٥) اهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ (٦)","صِرَاطَ الَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ الْمَغْضُوبِ عَلَيْهِمْ وَلَا الضَّالِّينَ (٧) آمِين"],tr:"Elhamdu lil-lahi rabbil alemin. Er-rahmani-r-rahim. Maliki jeumid-din. Ijjake na'budu ve ijjake neste'in. Ihdinas-siratal mustekim. Siratal-ledhine en'amte alejhim, gajril magdubi alejhim ve led-dal-lin. Amin.",de:"Falënderimi i takon Allahut, Zotit të botëve, të Gjithëmëshirshmit, Mëshirëplotit, Sunduesit të Ditës së Gjykimit. Vetëm Ty të adhurojmë dhe vetëm prej Teje ndihmë kërkojmë. Udhëzona në rrugën e drejtë, në rrugën e atyre që i ke begatuar, jo të atyre që kanë merituar zemërimin, as të atyre që kanë humbur. Amin."},
 fatiha_b:{ar:["بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ (١)"],tr:"Bismil-lahi-r-rahmani-r-rahim. ",de:"Në emër të Allahut, të Gjithëmëshirshmit, Mëshirëplotit. "},
 kauthar:{ar:["إِنَّا أَعْطَيْنَاكَ الْكَوْثَرَ (١) فَصَلِّ لِرَبِّكَ وَانْحَرْ (٢)","إِنَّ شَانِئَكَ هُوَ الْأَبْتَرُ (٣)"],tr:"Inna a'tajnakel keuther. Fesal-li li rabbike venhar. Inne shani'eke huvel ebter.",de:"Ne të kemi dhënë ty bollëkun. Prandaj fal namaz për Zotin tënd dhe ther kurban. Me të vërtetë, urrejtësi yt është ai që është i këputur."},
 ichlas:{ar:["بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ","قُلْ هُوَ اللَّهُ أَحَدٌ (١) اللَّهُ الصَّمَدُ (٢) لَمْ يَلِدْ وَلَمْ يُولَدْ (٣)","وَلَمْ يَكُنْ لَهُ كُفُوًا أَحَدٌ (٤)"],tr:"Bismil-lahi-r-rahmani-r-rahim. Kul huvallahu ehad. Allahus-samed. Lem jelid ve lem juled. Ve lem jekun lehu kufuven ehad.",de:"Thuaj: Ai është Allahu, Një i Vetëm. Allahu është Ai të cilit të gjithë i drejtohen. As nuk ka lindur kë, as nuk është i lindur. Dhe askush nuk është i barabartë me Të."},
 ruku:{ar:["سُبْحَانَ رَبِّيَ الْعَظِيمِ"],tr:"Subhane rabbijel adhim",de:"I lartësuar qoftë Zoti im, i Madhi."},
 qauma:{ar:["سَمِعَ اللَّهُ لِمَنْ حَمِدَهُ","رَبَّنَا لَكَ الْحَمْدُ"],tr:"Semi'allahu limen hamideh. Rabbena lekel hamd.",de:"Allahu e dëgjon atë që e lavdëron. Zoti ynë, Ty të takon lavdërimi."},
 sudschud:{ar:["سُبْحَانَ رَبِّيَ الْأَعْلَى"],tr:"Subhane rabbijel a'la",de:"I lartësuar qoftë Zoti im, Më i Larti."},
 jalsa:{ar:["رَبِّ اغْفِرْ لِي"],tr:"Rabbigfir li",de:"Zoti im, më fal."},
 tahiyyat:{ar:["التَّحِيَّاتُ لِلَّهِ وَالصَّلَوَاتُ وَالطَّيِّبَاتُ،","السَّلَامُ عَلَيْكَ أَيُّهَا النَّبِيُّ وَرَحْمَةُ اللَّهِ وَبَرَكَاتُهُ،","السَّلَامُ عَلَيْنَا وَعَلَى عِبَادِ اللَّهِ الصَّالِحِينَ،","أَشْهَدُ أَنْ لَا إِلَٰهَ إِلَّا اللَّهُ وَأَشْهَدُ أَنَّ مُحَمَّدًا عَبْدُهُ وَرَسُولُهُ"],tr:"Et-tehijjatu lil-lahi ves-salavatu vet-tajjibat. Es-selamu alejke ejjuhen-nebijju ve rahmetullahi ve berekatuh. Es-selamu alejna ve ala ibadil-lahis-salihin. Esh-hedu en la ilahe il-lallah, ve esh-hedu enne Muhammeden abduhu ve resuluh.",de:"Të gjitha përshëndetjet, lutjet dhe fjalët e mira i takojnë Allahut. Paqja qoftë mbi ty, o Pejgamber, dhe mëshira e Allahut dhe bekimet e Tij. Paqja qoftë mbi ne dhe mbi robërit e mirë të Allahut. Dëshmoj se nuk ka zot tjetër përveç Allahut dhe dëshmoj se Muhammedi është robi dhe i dërguari i Tij."},
 salawat:{ar:["اللَّهُمَّ صَلِّ عَلَى مُحَمَّدٍ وَعَلَى آلِ مُحَمَّدٍ، كَمَا صَلَّيْتَ عَلَى إِبْرَاهِيمَ وَعَلَى آلِ إِبْرَاهِيمَ، إِنَّكَ حَمِيدٌ مَجِيدٌ","اللَّهُمَّ بَارِكْ عَلَى مُحَمَّدٍ وَعَلَى آلِ مُحَمَّدٍ، كَمَا بَارَكْتَ عَلَى إِبْرَاهِيمَ وَعَلَى آلِ إِبْرَاهِيمَ، إِنَّكَ حَمِيدٌ مَجِيدٌ"],tr:"Allahumme sal-li ala Muhammedin ve ala ali Muhammed, kema sal-lejte ala Ibrahime ve ala ali Ibrahim, inneke hamidun mexhid. Allahumme barik ala Muhammedin ve ala ali Muhammed, kema barekte ala Ibrahime ve ala ali Ibrahim, inneke hamidun mexhid.",de:"O Allah, lavdëroje Muhammedin dhe familjen e Muhammedit, ashtu siç e lavdërove Ibrahimin dhe familjen e Ibrahimit. Ti je i Lavdishëm, i Madhëruar. O Allah, bekoje Muhammedin dhe familjen e Muhammedit, ashtu siç e bekove Ibrahimin dhe familjen e Ibrahimit. Ti je i Lavdishëm, i Madhëruar."},
 dua:{ar:["رَبَّنَا آتِنَا فِي الدُّنْيَا حَسَنَةً وَفِي الْآخِرَةِ حَسَنَةً","وَقِنَا عَذَابَ النَّارِ"],tr:"Rabbena atina fid-dunja haseneten ve fil-ahireti haseneten ve kina adhaben-nar.",de:"Zoti ynë, na jep të mira në këtë botë dhe të mira në botën tjetër, dhe na ruaj nga dënimi i zjarrit."},
 salam:{ar:["السَّلَامُ عَلَيْكُمْ وَرَحْمَةُ اللَّهِ"],tr:"Es-selamu alejkum ve rahmetullah",de:"Paqja dhe mëshira e Allahut qofshin mbi ju."}
};

function sayOf(k){const ks=k.split("+").map(x=>TX[x]);return{ar:[].concat(...ks.map(x=>x.ar)),tr:ks.map(x=>x.tr.trim()).join(" "),de:ks.map(x=>x.de.trim()).join(" ")}}
/* ---------- Schritte ---------- */
const WUDU=[
 {t:"Nijeti dhe Bismil-lah",a:"heart",say:"bism",d:"Bëje në zemër nijetin për të marrë abdes për hir të Allahut. Pastaj thuaj „Bismil-lah“.",h:"Nijeti bëhet në zemër. Nuk ke nevojë ta thuash me zë."},
 {t:"Larja e duarve",img:"01-haende",o:"62% 55%",n:3,d:"Laji të dyja duart deri te nyjat, edhe mes gishtave. Fillo me dorën e djathtë.",h:"Lëviz unazat që uji të arrijë edhe poshtë tyre."},
 {t:"Shpëlarja e gojës",img:"02-mund",o:"52% 30%",n:3,d:"Merr ujë në gojë me dorën e djathtë, shpëlaje mirë dhe nxirre ujin."},
 {t:"Pastrimi i hundës",img:"03-nase",o:"53% 28%",n:3,d:"Me dorën e djathtë tërhiq lehtë ujë në hundë dhe nxirre me dorën e majtë."},
 {t:"Larja e fytyrës",img:"04-gesicht",o:"52% 28%",n:3,d:"Laje gjithë fytyrën: nga rrënja e flokëve deri nën mjekër dhe nga njëri vesh te tjetri.",h:"Nëse ke mjekër të dendur, kaloji gishtat e lagur nëpër të."},
 {t:"Larja e krahut të djathtë",img:"05-arm-rechts",o:"58% 42%",n:3,d:"Laje krahun e djathtë nga majat e gishtave deri te bërryli, duke e përfshirë bërrylin."},
 {t:"Larja e krahut të majtë",img:"06-arm-links",o:"55% 45%",n:3,d:"Tani laje njësoj krahun e majtë, duke e përfshirë bërrylin."},
 {t:"Mes'hi i kokës",img:"07-kopf",o:"45% 18%",n:1,d:"Kaloji duart e lagura një herë mbi kokë, nga balli prapa.",h:"Koka nuk lahet, vetëm fërkohet me duar të lagura. Kjo quhet mes'h."},
 {t:"Pastrimi i veshëve",img:"08-ohren",o:"48% 22%",n:1,d:"Pastroje me gishtat tregues të lagur pjesën e brendshme të veshëve dhe me gishtat e mëdhenj pjesën e pasme."},
 {t:"Larja e këmbës së djathtë",img:"09-fuss-rechts",o:"60% 70%",n:3,d:"Laje këmbën e djathtë deri te nyjat, duke i përfshirë ato, edhe mes gishtave."},
 {t:"Larja e këmbës së majtë",img:"10-fuss-links",o:"60% 70%",n:3,d:"Tani laje njësoj këmbën e majtë, deri te nyjat dhe mes gishtave."},
 {t:"Dëshmia pas abdesit",a:"heart",say:"schahada",d:"Gati! Pas abdesit thuaj shehadetin. Tani je gati për namaz."}
];
const CDN=n=>`https://cdn.islamic.network/quran/audio/128/ar.alafasy/${n}.mp3`;
const R=(a,b)=>Array.from({length:b-a+1},(_,i)=>CDN(a+i));
const GEBET=[
 {r:1,t:"Nijeti",p:"down",heart:1,d:"Qëndro në sexhade, me fytyrë nga kibla, drejtimi i Qabes në Mekë. Bëje në zemër nijetin: po fal 2 rekate farz të namazit të sabahut.",h:"Shikimi të qëndrojë në vendin ku vjen balli gjatë sexhdes."},
 {r:1,t:"Tekbiri hyrës",p:"takbir",say:"takbir",d:"Ngriji duart deri te veshët, me pëllëmbët nga kibla, dhe thuaj „Allahu ekber“. Me këtë fillon namazi.",h:"Gratë i ngrenë duart deri te supet."},
 {r:1,t:"Kijami dhe Subhaneke",p:"stand",say:"thana",d:"Vëre dorën e djathtë mbi të majtën, poshtë kërthizës, dhe lexo me zë të ulët Subhaneken.",h:"Gratë i vënë duart mbi gjoks."},
 {r:1,t:"Eudhu dhe Besmele",p:"stand",say:"auudhu",d:"Thuaj me zë të ulët Eudhu-në dhe pastaj Besmelen."},
 {r:1,t:"El-Fatiha",p:"stand",say:"fatiha",au:R(2,7),d:"Lexo Fatihanë. Në fund thuaj „Amin“.",h:"Në namazin e sabahut imami e lexon Fatihanë dhe suren me zë. Kur fal vetëm, mund t'i lexosh me zë ose me zë të ulët."},
 {r:1,t:"Sure e shkurtër: El-Kevther",p:"stand",say:"kauthar",au:R(6205,6207),d:"Pas Fatihasë lexo një sure të shkurtër ose të paktën tri ajete të shkurtra, këtu El-Kevtherin."},
 {r:1,t:"Rukuja",p:"ruku",n:3,say:"ruku",d:"Thuaj „Allahu ekber“ dhe përkulu: shpina drejt, duart mbi gjunjë, shikimi te këmbët. Pastaj thuaj tri herë:"},
 {r:1,t:"Ngritja nga rukuja",p:"itidal",say:"qauma",d:"Ngrihu dhe gjatë ngritjes thuaj fjalinë e parë. Kur të qëndrosh drejt, thuaj të dytën."},
 {r:1,t:"Sexhdja e parë",p:"sujud",n:3,say:"sudschud",d:"Thuaj „Allahu ekber“ dhe bjer në sexhde: fillimisht gjunjët, pastaj duart, pastaj hunda dhe balli. Thuaj tri herë:",h:"Shtatë gjymtyrë prekin tokën: balli me hundën, të dyja duart, të dy gjunjët dhe gishtat e të dyja këmbëve."},
 {r:1,t:"Ulja mes dy sexhdeve",p:"sit",say:"jalsa",d:"Ngrihu me „Allahu ekber“ dhe ulu qetë derisa trupi të qetësohet. Duart i ke mbi kofshë."},
 {r:1,t:"Sexhdja e dytë",p:"sujud",n:3,say:"sudschud",d:"Bjer përsëri në sexhde me „Allahu ekber“ dhe thuaj tri herë:",h:"Me këtë përfundon rekati i parë."},
 {r:2,t:"Ngritja: Besmele dhe Fatiha",p:"stand",say:"fatiha_b+fatiha",au:R(1,7),d:"Ngrihu me „Allahu ekber“ dhe vendosi përsëri duart. Lexo Besmelen dhe Fatihanë.",h:"Subhaneken dhe Eudhu-në i thua vetëm në rekatin e parë."},
 {r:2,t:"Sure e shkurtër: El-Ihlas",p:"stand",say:"ichlas",au:R(6222,6225),d:"Pas Fatihasë lexo përsëri një sure të shkurtër, këtu El-Ihlasin."},
 {r:2,t:"Rukuja",p:"ruku",n:3,say:"ruku",d:"Thuaj „Allahu ekber“, përkulu dhe thuaj tri herë:"},
 {r:2,t:"Ngritja nga rukuja",p:"itidal",say:"qauma",d:"Ngrihu dhe thuaj fjalinë e parë, në këmbë të dytën."},
 {r:2,t:"Sexhdja e parë",p:"sujud",n:3,say:"sudschud",d:"Bjer në sexhde me „Allahu ekber“ dhe thuaj tri herë:"},
 {r:2,t:"Ulja mes dy sexhdeve",p:"sit",say:"jalsa",d:"Ulu shkurt dhe qetë me „Allahu ekber“."},
 {r:2,t:"Sexhdja e dytë",p:"sujud",n:3,say:"sudschud",d:"Bjer përsëri në sexhde me „Allahu ekber“ dhe thuaj tri herë:",h:"Pas saj nuk ngrihesh, por mbetesh ulur."},
 {r:3,t:"Ulja: Et-Tehijjatu",p:"sit",finger:1,say:"tahiyyat",d:"Pas sexhdes së dytë ulu, me duart mbi kofshë, dhe lexo Et-Tehijjatun.",h:"Te „la ilahe“ ngre gishtin tregues të djathtë, te „il-lallah“ e ul përsëri."},
 {r:3,t:"Salavatet për Pejgamberin ﷺ",p:"sit",say:"salawat",d:"Ulur, lexo salavatet për Pejgamberin ﷺ."},
 {r:3,t:"Duaja",p:"sit",say:"dua",d:"Lute Allahun për të mira, për shembull me këtë dua nga Kurani."},
 {r:3,t:"Selami nga e djathta",p:"sit",turn:1,say:"salam",d:"Ktheje kokën nga e djathta dhe jep selam.",h:"Figura të shikon ty: e djathta e saj për ty është majtas."},
 {r:3,t:"Selami nga e majta",p:"sit",turn:-1,say:"salam",d:"Ktheje kokën nga e majta dhe jep selam përsëri. Namazi yt përfundoi. MashaAllah!"}
];
const RNAME={1:"Rekati 1",2:"Rekati 2",3:"Përfundimi"};
const COURSES={wudu:{steps:WUDU,title:"Abdesi: të gjithë hapat",scene:"wudu"},gebet:{steps:GEBET,title:"Namazi i sabahut: të gjithë hapat",scene:"gebet"}};

/* ---------- Gebets-Figur: Bilder je Haltung, weich überblendet ---------- */
const POSE={"stand_down": {"x": 111.5, "y": 24.0, "w": 77.0, "h": 228.0, "mx": 150.0, "my": 58.2}, "takbir": {"x": 108.3, "y": 24.0, "w": 83.5, "h": 228.0, "mx": 150.0, "my": 58.2}, "stand_fold": {"x": 113.9, "y": 24.0, "w": 72.3, "h": 228.0, "mx": 150.0, "my": 58.2}, "ruku": {"x": 86.6, "y": 100.1, "w": 126.8, "h": 151.9, "mx": 203.2, "my": 130.5}, "itidal": {"x": 121.5, "y": 24.2, "w": 57.1, "h": 227.8, "mx": 156.8, "my": 53.8}, "sujud": {"x": 79.9, "y": 169.8, "w": 140.2, "h": 82.2, "mx": 210.3, "my": 229.0}, "sit": {"x": 102.6, "y": 73.8, "w": 94.7, "h": 178.2, "mx": 150.0, "my": 107.6}, "salam_r": {"x": 102.2, "y": 74.2, "w": 95.6, "h": 177.8, "mx": 147.1, "my": 108.0}, "salam_l": {"x": 101.3, "y": 73.8, "w": 97.3, "h": 178.2, "mx": 152.9, "my": 107.6}};
const ALIAS={down:"stand_down",stand:"stand_fold",takbir:"takbir",ruku:"ruku",itidal:"itidal",sujud:"sujud",sit:"sit"};
function buildGebet(){
  let s=`<rect x="26" y="250" width="248" height="10" rx="5" fill="var(--mat)"/><rect x="26" y="258" width="248" height="4" rx="2" fill="var(--mat-2)"/>`;
  for(let i=0;i<9;i++)s+=`<line x1="${30+i*30}" y1="262" x2="${30+i*30}" y2="270" stroke="var(--mat-2)" stroke-width="2" stroke-linecap="round"/>`;
  for(const n in POSE){const q=POSE[n];s+=`<image class="pz" data-p="${n}" href="${n}.webp" x="${q.x}" y="${q.y}" width="${q.w}" height="${q.h}" opacity="0"/>`}
  s+=`<g id="ov"></g>`;$("svg").innerHTML=s;
}
let curPose=null;
function poseTo(name,o,dur){
  o=o||{};let n=ALIAS[name]||name;if(o.turn>0)n="salam_r";if(o.turn<0)n="salam_l";
  if(!$("svg").querySelector(".pz"))buildGebet();
  $("svg").querySelectorAll(".pz").forEach(im=>im.setAttribute("opacity",im.dataset.p===n?"1":"0"));
  curPose=n;const q=POSE[n];let s="";
  if(o.heart)s+=`<circle class="glow" cx="${q.x+q.w*.5}" cy="${q.y+q.h*.3}" r="16" fill="var(--teal)" opacity=".6"/><path d="M${q.x+q.w*.5} ${q.y+q.h*.3+7}l-8-8a5 5 0 0 1 8-6a5 5 0 0 1 8 6z" fill="#fff"/>`;
  if(o.talk&&!o.turn){const cx=q.mx+16,cy=q.my;for(let i=1;i<=2;i++){const r=4+i*6;s+=`<path class="glow" style="animation-delay:${i*.3}s" d="M${cx+r*.5} ${cy-r} Q${cx+r*1.1} ${cy} ${cx+r*.5} ${cy+r}" fill="none" stroke="var(--teal)" stroke-width="3" stroke-linecap="round"/>`}}
  if(o.finger){const fx=q.x+q.w*.3,fy=q.y+q.h*.8;s+=`<circle class="glow" cx="${fx}" cy="${fy}" r="13" fill="none" stroke="var(--teal)" stroke-width="3"/><path class="pulse" d="M${fx} ${fy-6}v-22" stroke="var(--teal)" stroke-width="3" stroke-linecap="round"/><path d="M${fx-6} ${fy-24}l6-8 6 8" fill="none" stroke="var(--teal)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>`}
  if(o.turn){const x=q.mx,y=q.y-12,t=o.turn;s+=`<g class="arrowR"><path d="M${x-22} ${y}q22-14 44 0" fill="none" stroke="var(--teal)" stroke-width="3.5" stroke-linecap="round"/><path d="${t>0?`M${x-22} ${y}l9-1-4-8`:`M${x+22} ${y}l-9-1 4-8`}" fill="none" stroke="var(--teal)" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></g><text x="${x}" y="${y-14}" text-anchor="middle" font-family="Lexend,system-ui,sans-serif" font-weight="700" font-size="14" fill="var(--teal)">${t>0?"djathtas":"majtas"}</text>`}
  $("ov").innerHTML=s;
}

/* ---------- Waschungs-Figur (Bild, Vorderansicht, Koordinaten in Bildpixeln 1024×1536) ---------- */
const FULL=[-256,0,1536,1536];
const AREA={
 heart:{vb:[110,0,800,800],hl:`<circle cx="500" cy="470" r="70" fill="var(--teal)"/><path d="M500 505l-34-34a20 20 0 0 1 34-28a20 20 0 0 1 34 28z" fill="#fff"/>`,drops:[]},
 hands:{vb:[150,500,700,700],hl:`<circle cx="300" cy="850" r="78"/><circle cx="705" cy="850" r="78"/>`,drops:[[300,740],[705,740]]},
 mouth:{vb:[330,20,360,360],hl:`<ellipse cx="510" cy="203" rx="36" ry="20"/>`,drops:[[510,120]]},
 nose:{vb:[330,20,360,360],hl:`<ellipse cx="510" cy="176" rx="22" ry="28"/>`,drops:[[510,95]]},
 face:{vb:[300,-20,420,420],hl:`<ellipse cx="510" cy="168" rx="84" ry="100"/>`,drops:[[460,40],[510,30],[560,40]]},
 arms:{vb:[40,240,940,940],hl:`<path d="M335 335 L292 565 L300 850 M688 335 L728 565 L705 850" stroke="var(--teal)" stroke-opacity=".42" stroke-width="100" stroke-linecap="round" stroke-linejoin="round" fill="none"/>`,drops:[[300,420],[720,420],[290,640],[730,640]]},
 head:{vb:[300,-60,420,420],hl:`<path d="M412 135C410 20 610 20 608 135C560 92 460 92 412 135Z"/>`,drops:[[510,-10]]},
 ears:{vb:[300,-20,420,420],hl:`<ellipse cx="420" cy="168" rx="24" ry="36"/><ellipse cx="600" cy="168" rx="24" ry="36"/>`,drops:[[420,70],[600,70]]},
 feet:{vb:[170,1100,660,660],hl:`<ellipse cx="380" cy="1478" rx="90" ry="55"/><ellipse cx="612" cy="1478" rx="90" ry="55"/>`,drops:[[380,1350],[612,1350]]}
};
let vbCur=FULL.slice(),vbAnim=null;
function setVB(v){$("svg").setAttribute("viewBox",v.map(n=>n.toFixed(1)).join(" "))}
function vbTo(t,dur){const f=vbCur.slice();if(vbAnim)cancelAnimationFrame(vbAnim);
  if(reduce||!dur){vbCur=t.slice();setVB(vbCur);return}
  const t0=performance.now();const st=now=>{let k=Math.min(1,(now-t0)/dur);k=k<.5?2*k*k:1-Math.pow(-2*k+2,2)/2;vbCur=f.map((x,i)=>x+(t[i]-x)*k);setVB(vbCur);if(k<1)vbAnim=requestAnimationFrame(st)};vbAnim=requestAnimationFrame(st)}
const DROP=(x,y,k,f)=>`<g transform="translate(${x} ${y}) scale(${f})"><path class="drop" style="animation-delay:${k*.35}s" d="M0 -9q7 9 0 13q-7-4 0-13z" fill="var(--water)" stroke="#fff" stroke-width=".8"/></g>`;
function drawWudu(a,first){
  const A=AREA[a];const f=A.vb[2]/300*1.4;
  let s=`<image href="figur.webp" x="0" y="0" width="1024" height="1536"/>`;
  if(a==="heart")s+=`<g class="glow">${A.hl}</g>`;
  else{s+=`<g class="glow" fill="var(--teal)" fill-opacity=".38" stroke="var(--teal)" stroke-width="${f*2.2}" stroke-dasharray="${f*6} ${f*4}">${A.hl}</g>`;A.drops.forEach((d,i)=>{s+=DROP(d[0],d[1],i,f)+DROP(d[0]+f*7,d[1]-f*12,i+1.5,f)})}
  $("svg").innerHTML=s;vbTo(A.vb,first?0:800);
}

/* ---------- Ablauf ---------- */
let course="wudu",idx=0,auto=false,autoT=null,seqT=null,cntT=null;
function buildPhotos(){const ph=$("photos");if(course!=="wudu"){ph.innerHTML="";ph.hidden=true;return}
  ph.innerHTML=WUDU.filter(w=>w.img).map((w,k)=>`<img src="wudu/${w.img}.webp" alt="" data-img="${w.img}" style="transform-origin:${w.o}" ${k>1?'loading="lazy"':''} width="1200" height="800">`).join("")}
function setCourse(c,keep){
  course=COURSES[c]?c:"wudu";
  ["wudu","gebet"].forEach(k=>$("tab-"+k).setAttribute("aria-current",String(k===course)));
  $("allTitle").textContent=COURSES[course].title;$("stage").classList.toggle("wide",course==="wudu");$("sound").hidden=course!=="gebet";buildPhotos();
  
  const L=$("list");L.innerHTML="";
  let lastR=null;
  COURSES[course].steps.forEach((s,i)=>{if(s.r&&s.r!==lastR){lastR=s.r;const h=document.createElement("li");h.className="grp";h.textContent=RNAME[s.r];L.appendChild(h)}const li=document.createElement("li");
    li.innerHTML=`<button type="button" id="st-${course}-${i}"><span class="n">${i+1}</span><span><b>${s.t}</b>${s.n?`<small>${s.n}×</small>`:""}</span></button>`;
    li.firstChild.addEventListener("click",()=>{show(i);document.getElementById("stage").scrollIntoView({behavior:reduce?"auto":"smooth",block:"center"})});L.appendChild(li)});
  if(course==="gebet"){if(vbAnim)cancelAnimationFrame(vbAnim);setVB([0,0,300,300]);buildGebet()}else{vbCur=FULL.slice();setVB(vbCur)}
  show(keep?idx:0,true);
}
function show(i,first){if(course!=="wudu")$("svg").style.visibility="visible";
  const S=COURSES[course].steps;idx=Math.max(0,Math.min(S.length-1,i));const s=S[idx];
  $("stNo").textContent=(course==="wudu"?"Abdesi":"Namazi i sabahut"+(s.r?" · "+RNAME[s.r]:""))+" · Hapi "+(idx+1)+" nga "+S.length;
  $("stTitle").textContent=s.t;$("stDo").textContent=s.d;
  const sy=s.say&&sayOf(s.say);$("stSay").hidden=!sy;
  if(sy){$("sAr").innerHTML=sy.ar.join("<br>");$("sTr").textContent=sy.tr;$("sDe").textContent=sy.de}
  $("stHint").hidden=!s.h;if(s.h)$("stHint").innerHTML="<b>Këshillë:</b>&nbsp;"+s.h;
  $("prev").disabled=idx===0;$("next").textContent=idx===S.length-1?(course==="wudu"?"Vazhdo te namazi →":"Nga fillimi ↺"):"Vazhdo →";
  $("pos").textContent=(idx+1)+" / "+S.length;$("bar").style.width=((idx+1)/S.length*100)+"%";
  document.querySelectorAll("#list button").forEach((b,k)=>b.setAttribute("aria-current",String(k===idx)));audioFor(s);
  clearInterval(seqT);clearInterval(cntT);
  if(course==="wudu"){const ph=$("photos");ph.hidden=!s.img;$("svg").style.visibility=s.img?"hidden":"visible";
    ph.querySelectorAll("img").forEach(im=>{const on=im.dataset.img===s.img;im.classList.remove("on");if(on){void im.offsetWidth;im.classList.add("on")}});
    if(!s.img)drawWudu(s.a,first)}
  else if(s.seq){let k=0;poseTo(s.seq[0],{},first?0:700);if(!reduce)seqT=setInterval(()=>{k=(k+1)%s.seq.length;poseTo(s.seq[k],{},700)},1500)}
  else poseTo(s.p,{heart:s.heart,finger:s.finger,turn:s.turn,talk:!!s.say},first?0:750);
  const C=$("count");C.innerHTML="";
  if(s.n){for(let k=0;k<s.n;k++)C.insertAdjacentHTML("beforeend",`<i>${k+1}</i>`);const I=[...C.children];let k=0;
    const tick=()=>{I.forEach((e,j)=>e.classList.toggle("on",j<=k));k=(k+1)%(s.n+1);if(k===0)k=0};
    if(reduce)I.forEach(e=>e.classList.add("on"));else{I.forEach(e=>e.classList.remove("on"));let n=0;cntT=setInterval(()=>{I.forEach((e,j)=>e.classList.toggle("on",j<n));n=n>=s.n?0:n+1},900)}}
  if(auto)schedule();
}
/* ---------- Ton ---------- */
const player=new Audio();player.preload="none";let plist=[],pi=0,soundOn=false,playing=false;
function setPlay(v){playing=v;const b=$("play");b.textContent=v?"❚❚ Ndalo":"▶ Dëgjo leximin";b.setAttribute("aria-pressed",String(v))}
function stopAudio(){player.pause();setPlay(false);$("aupos").textContent=""}
function playList(){if(!plist.length)return;pi=0;playOne()}
function playOne(){player.src=plist[pi];$("aupos").textContent=plist.length>1?"Ajeti "+(pi+1)+" nga "+plist.length:"";player.play().then(()=>setPlay(true)).catch(()=>{setPlay(false);$("aupos").textContent="Zëri nuk u nis. Shtyp „Dëgjo leximin“."})}
player.addEventListener("ended",()=>{if(pi<plist.length-1){pi++;playOne()}else{setPlay(false);$("aupos").textContent="";if(auto){clearTimeout(autoT);autoT=setTimeout(()=>{const S=COURSES[course].steps;if(idx<S.length-1)show(idx+1);else setAuto(false)},1200)}}});
player.addEventListener("error",()=>{setPlay(false);$("aupos").textContent="Incizimi nuk arrihet tani."});
function audioFor(s){stopAudio();plist=s.au||[];const has=plist.length>0;$("auRow").hidden=course!=="gebet"||!s.say;$("play").hidden=!has;$("aunote").hidden=has;
  if(has&&soundOn)playList()}
$("play").addEventListener("click",()=>{if(playing){stopAudio()}else playList()});
$("sound").addEventListener("click",()=>{soundOn=!soundOn;$("sound").setAttribute("aria-pressed",String(soundOn));$("sound").textContent=soundOn?"🔊 Zëri i ndezur":"🔈 Zëri i fikur";if(soundOn&&plist.length&&!playing)playList();if(!soundOn)stopAudio()});
function next(){const S=COURSES[course].steps;if(idx<S.length-1)show(idx+1);else if(course==="wudu"){location.hash="gebet"}else show(0)}
function schedule(){clearTimeout(autoT);const s=COURSES[course].steps[idx];if(soundOn&&s.au&&s.au.length)return;const sy=s.say&&sayOf(s.say);const ms=Math.min(16000,5000+(sy?sy.tr.length*45:0));
  autoT=setTimeout(()=>{const S=COURSES[course].steps;if(idx<S.length-1)show(idx+1);else setAuto(false)},ms)}
function setAuto(v){auto=v;$("auto").setAttribute("aria-pressed",String(v));$("auto").textContent=v?"❚❚ Pauzë":"▶ Automatikisht";clearTimeout(autoT);if(v)schedule()}
$("prev").addEventListener("click",()=>show(idx-1));
$("next").addEventListener("click",next);
$("auto").addEventListener("click",()=>setAuto(!auto));
document.addEventListener("keydown",e=>{if(e.target.closest("input,textarea,select"))return;if(e.key==="ArrowRight")next();if(e.key==="ArrowLeft")show(idx-1)});
function route(){const h=location.hash.slice(1);if(h==="wudu"||h==="gebet"){setCourse(h);if(h==="gebet"||h==="wudu"){}}else if(!h){setCourse(course,true)}}
addEventListener("hashchange",()=>{route();if(location.hash==="#gebet"||location.hash==="#wudu")$("stage").scrollIntoView({behavior:reduce?"auto":"smooth",block:"center"})});
route();if(!location.hash)setCourse("wudu");
})();
