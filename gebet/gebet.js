(function(){
const $=id=>document.getElementById(id);
const reduce=matchMedia("(prefers-reduced-motion: reduce)").matches;

/* ---------- Texte ---------- */
const TX={
 bism:{ar:["بِسْمِ اللَّهِ"],tr:"Bismillah",de:"Im Namen Allahs."},
 schahada:{ar:["أَشْهَدُ أَنْ لَا إِلَٰهَ إِلَّا اللَّهُ وَحْدَهُ لَا شَرِيكَ لَهُ","وَأَشْهَدُ أَنَّ مُحَمَّدًا عَبْدُهُ وَرَسُولُهُ"],tr:"Asch-hadu an la ilaha illallahu wahdahu la scharika lah, wa asch-hadu anna Muhammadan abduhu wa rasuluh.",de:"Ich bezeuge, dass es keinen Gott gibt außer Allah, dem Einen ohne Partner, und ich bezeuge, dass Muhammad Sein Diener und Gesandter ist."},
 takbir:{ar:["اللَّهُ أَكْبَرُ"],tr:"Allahu akbar",de:"Allah ist größer."},
 thana:{ar:["سُبْحَانَكَ اللَّهُمَّ وَبِحَمْدِكَ، وَتَبَارَكَ اسْمُكَ،","وَتَعَالَى جَدُّكَ، وَلَا إِلَٰهَ غَيْرُكَ"],tr:"Subhanakallahumma wa bihamdika, wa tabarakasmuka, wa ta'ala dschadduka, wa la ilaha ghairuk.",de:"Gepriesen bist Du, o Allah, und Dir gebührt das Lob. Gesegnet ist Dein Name, erhaben ist Deine Herrlichkeit, und es gibt keinen Gott außer Dir."},
 auudhu:{ar:["أَعُوذُ بِاللَّهِ مِنَ الشَّيْطَانِ الرَّجِيمِ","بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"],tr:"A'udhu billahi minasch-schaitanir-radschim. Bismillahir-rahmanir-rahim.",de:"Ich suche Schutz bei Allah vor dem verfluchten Satan. Im Namen Allahs, des Allerbarmers, des Barmherzigen."},
 fatiha:{ar:["الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ (٢) الرَّحْمَٰنِ الرَّحِيمِ (٣) مَالِكِ يَوْمِ الدِّينِ (٤)","إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ (٥) اهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ (٦)","صِرَاطَ الَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ الْمَغْضُوبِ عَلَيْهِمْ وَلَا الضَّالِّينَ (٧) آمِين"],tr:"Al-hamdu lillahi rabbil-alamin. Ar-rahmanir-rahim. Maliki yaumid-din. Iyyaka na'budu wa iyyaka nasta'in. Ihdinas-siratal-mustaqim. Siratal-ladhina an'amta alaihim, ghairil-maghdubi alaihim wa lad-dallin. Amin.",de:"Alles Lob gehört Allah, dem Herrn der Welten, dem Allerbarmer, dem Barmherzigen, dem Herrscher am Tag des Gerichts. Dir allein dienen wir, und Dich allein bitten wir um Hilfe. Führe uns den geraden Weg, den Weg derer, denen Du Gnade erwiesen hast, nicht derer, die Deinen Zorn erregt haben, und nicht der Irregehenden. Amin."},
 fatiha_b:{ar:["بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ (١)"],tr:"Bismillahir-rahmanir-rahim. ",de:"Im Namen Allahs, des Allerbarmers, des Barmherzigen. "},
 kauthar:{ar:["إِنَّا أَعْطَيْنَاكَ الْكَوْثَرَ (١) فَصَلِّ لِرَبِّكَ وَانْحَرْ (٢)","إِنَّ شَانِئَكَ هُوَ الْأَبْتَرُ (٣)"],tr:"Inna a'tainakal-kauthar. Fa salli li rabbika wanhar. Inna schani'aka huwal-abtar.",de:"Wir haben dir die Fülle gegeben. So bete zu deinem Herrn und opfere. Wer dich hasst, der ist es, der abgeschnitten ist."},
 ichlas:{ar:["بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ","قُلْ هُوَ اللَّهُ أَحَدٌ (١) اللَّهُ الصَّمَدُ (٢) لَمْ يَلِدْ وَلَمْ يُولَدْ (٣)","وَلَمْ يَكُنْ لَهُ كُفُوًا أَحَدٌ (٤)"],tr:"Bismillahir-rahmanir-rahim. Qul huwallahu ahad. Allahus-samad. Lam yalid wa lam yulad. Wa lam yakun lahu kufuwan ahad.",de:"Sag: Er ist Allah, der Eine. Allah, der Ewige, auf den alle angewiesen sind. Er zeugt nicht und wurde nicht gezeugt. Und keiner ist Ihm gleich."},
 ruku:{ar:["سُبْحَانَ رَبِّيَ الْعَظِيمِ"],tr:"Subhana rabbiyal-azim",de:"Gepriesen ist mein Herr, der Gewaltige."},
 qauma:{ar:["سَمِعَ اللَّهُ لِمَنْ حَمِدَهُ","رَبَّنَا لَكَ الْحَمْدُ"],tr:"Sami'allahu liman hamidah. Rabbana lakal-hamd.",de:"Allah hört den, der Ihn lobt. Unser Herr, Dir gebührt das Lob."},
 sudschud:{ar:["سُبْحَانَ رَبِّيَ الْأَعْلَى"],tr:"Subhana rabbiyal-a'la",de:"Gepriesen ist mein Herr, der Höchste."},
 jalsa:{ar:["رَبِّ اغْفِرْ لِي"],tr:"Rabbighfir li",de:"Mein Herr, vergib mir."},
 tahiyyat:{ar:["التَّحِيَّاتُ لِلَّهِ وَالصَّلَوَاتُ وَالطَّيِّبَاتُ،","السَّلَامُ عَلَيْكَ أَيُّهَا النَّبِيُّ وَرَحْمَةُ اللَّهِ وَبَرَكَاتُهُ،","السَّلَامُ عَلَيْنَا وَعَلَى عِبَادِ اللَّهِ الصَّالِحِينَ،","أَشْهَدُ أَنْ لَا إِلَٰهَ إِلَّا اللَّهُ وَأَشْهَدُ أَنَّ مُحَمَّدًا عَبْدُهُ وَرَسُولُهُ"],tr:"At-tahiyyatu lillahi was-salawatu wat-tayyibat. As-salamu alaika ayyuhan-nabiyyu wa rahmatullahi wa barakatuh. As-salamu alaina wa ala ibadillahis-salihin. Asch-hadu an la ilaha illallah, wa asch-hadu anna Muhammadan abduhu wa rasuluh.",de:"Alle Grüße, Gebete und guten Worte gehören Allah. Friede sei mit dir, o Prophet, und die Barmherzigkeit Allahs und Sein Segen. Friede sei mit uns und mit den rechtschaffenen Dienern Allahs. Ich bezeuge, dass es keinen Gott gibt außer Allah, und ich bezeuge, dass Muhammad Sein Diener und Gesandter ist."},
 salawat:{ar:["اللَّهُمَّ صَلِّ عَلَى مُحَمَّدٍ وَعَلَى آلِ مُحَمَّدٍ، كَمَا صَلَّيْتَ عَلَى إِبْرَاهِيمَ وَعَلَى آلِ إِبْرَاهِيمَ، إِنَّكَ حَمِيدٌ مَجِيدٌ","اللَّهُمَّ بَارِكْ عَلَى مُحَمَّدٍ وَعَلَى آلِ مُحَمَّدٍ، كَمَا بَارَكْتَ عَلَى إِبْرَاهِيمَ وَعَلَى آلِ إِبْرَاهِيمَ، إِنَّكَ حَمِيدٌ مَجِيدٌ"],tr:"Allahumma salli ala Muhammadin wa ala ali Muhammad, kama sallaita ala Ibrahima wa ala ali Ibrahim, innaka hamidun madschid. Allahumma barik ala Muhammadin wa ala ali Muhammad, kama barakta ala Ibrahima wa ala ali Ibrahim, innaka hamidun madschid.",de:"O Allah, segne Muhammad und die Familie Muhammads, wie Du Ibrahim und die Familie Ibrahims gesegnet hast. Du bist der Lobenswerte, der Ruhmreiche. O Allah, gib Muhammad und der Familie Muhammads Segen, wie Du Ibrahim und der Familie Ibrahims Segen gegeben hast. Du bist der Lobenswerte, der Ruhmreiche."},
 dua:{ar:["رَبَّنَا آتِنَا فِي الدُّنْيَا حَسَنَةً وَفِي الْآخِرَةِ حَسَنَةً","وَقِنَا عَذَابَ النَّارِ"],tr:"Rabbana atina fid-dunya hasanatan wa fil-achirati hasanatan wa qina adhaban-nar.",de:"Unser Herr, gib uns Gutes in dieser Welt und Gutes im Jenseits, und bewahre uns vor der Strafe des Feuers."},
 salam:{ar:["السَّلَامُ عَلَيْكُمْ وَرَحْمَةُ اللَّهِ"],tr:"As-salamu alaikum wa rahmatullah",de:"Friede sei mit euch und die Barmherzigkeit Allahs."}
};

function sayOf(k){const ks=k.split("+").map(x=>TX[x]);return{ar:[].concat(...ks.map(x=>x.ar)),tr:ks.map(x=>x.tr.trim()).join(" "),de:ks.map(x=>x.de.trim()).join(" ")}}
/* ---------- Schritte ---------- */
const WUDU=[
 {t:"Absicht und Bismillah",a:"heart",say:"bism",d:"Fasse im Herzen die Absicht, die Gebetswaschung für Allah zu machen. Sprich dann „Bismillah“.",h:"Die Absicht ist im Herzen. Du musst sie nicht laut aussprechen."},
 {t:"Hände waschen",img:"01-haende",o:"62% 55%",n:3,d:"Wasche beide Hände bis zu den Handgelenken, auch zwischen den Fingern. Beginne mit der rechten Hand.",h:"Bewege Ringe, damit das Wasser auch darunter kommt."},
 {t:"Mund ausspülen",img:"02-mund",o:"52% 30%",n:3,d:"Nimm mit der rechten Hand Wasser in den Mund, spüle ihn gründlich aus und spucke das Wasser aus."},
 {t:"Nase reinigen",img:"03-nase",o:"53% 28%",n:3,d:"Zieh mit der rechten Hand Wasser leicht in die Nase und schnäuze es mit der linken Hand wieder aus."},
 {t:"Gesicht waschen",img:"04-gesicht",o:"52% 28%",n:3,d:"Wasche das ganze Gesicht: vom Haaransatz bis unter das Kinn und von einem Ohr bis zum anderen.",h:"Hast du einen dichten Bart, fahre mit nassen Fingern hindurch."},
 {t:"Rechten Arm waschen",img:"05-arm-rechts",o:"58% 42%",n:3,d:"Wasche den rechten Arm von den Fingerspitzen bis einschließlich Ellbogen."},
 {t:"Linken Arm waschen",img:"06-arm-links",o:"55% 45%",n:3,d:"Wasche jetzt genauso den linken Arm, bis einschließlich Ellbogen."},
 {t:"Kopf bestreichen",img:"07-kopf",o:"45% 18%",n:1,d:"Fahre mit den nassen Händen einmal über den Kopf, von der Stirn nach hinten.",h:"Der Kopf wird nicht gewaschen, nur mit nassen Händen bestrichen. Das heißt Masah."},
 {t:"Ohren reinigen",img:"08-ohren",o:"48% 22%",n:1,d:"Reinige mit den nassen Zeigefingern das Innere der Ohren und mit den Daumen die Rückseite."},
 {t:"Rechten Fuß waschen",img:"09-fuss-rechts",o:"60% 70%",n:3,d:"Wasche den rechten Fuß bis einschließlich Knöchel, auch zwischen den Zehen."},
 {t:"Linken Fuß waschen",img:"10-fuss-links",o:"60% 70%",n:3,d:"Wasche jetzt genauso den linken Fuß, bis einschließlich Knöchel und zwischen den Zehen."},
 {t:"Glaubensbekenntnis danach",a:"heart",say:"schahada",d:"Fertig! Sprich nach der Waschung das Glaubensbekenntnis. Jetzt bist du bereit für das Gebet."}
];
const CDN=n=>`https://cdn.islamic.network/quran/audio/128/ar.alafasy/${n}.mp3`;
const R=(a,b)=>Array.from({length:b-a+1},(_,i)=>CDN(a+i));
const GEBET=[
 {r:1,t:"Absicht",p:"down",heart:1,d:"Stell dich auf den Gebetsteppich, das Gesicht zur Qibla, der Richtung der Kaaba in Mekka. Fasse im Herzen die Absicht: Ich bete die 2 Rakat Fard des Morgengebets (Fadschr).",h:"Dein Blick ruht auf der Stelle, an die bei der Niederwerfung deine Stirn kommt."},
 {r:1,t:"Eröffnungs-Takbir",p:"takbir",say:"takbir",d:"Hebe die Hände bis zu den Ohren, die Handflächen zur Qibla, und sprich „Allahu akbar“. Damit beginnt dein Gebet.",h:"Frauen heben die Hände bis zu den Schultern."},
 {r:1,t:"Stehen und Lobpreis",p:"stand",say:"thana",d:"Lege die rechte Hand auf die linke, unterhalb des Bauchnabels, und sprich leise den Lobpreis.",h:"Frauen legen die Hände auf die Brust."},
 {r:1,t:"Schutz suchen und Basmala",p:"stand",say:"auudhu",d:"Sprich leise die Bitte um Schutz und danach die Basmala."},
 {r:1,t:"Al-Fatiha",p:"stand",say:"fatiha",au:R(2,7),d:"Lies die Fatiha. Am Ende sagst du „Amin“.",h:"Im Morgengebet liest der Imam die Fatiha und die Sure laut. Betest du allein, darfst du sie laut oder leise lesen."},
 {r:1,t:"Kurze Sure: Al-Kauthar",p:"stand",say:"kauthar",au:R(6205,6207),d:"Lies nach der Fatiha eine kurze Sure oder mindestens drei kurze Verse, hier Al-Kauthar."},
 {r:1,t:"Verbeugung (Ruku)",p:"ruku",n:3,say:"ruku",d:"Sprich „Allahu akbar“ und beuge dich: Rücken gerade, Hände auf den Knien, Blick auf die Füße. Sprich dann dreimal:"},
 {r:1,t:"Aufrichten",p:"itidal",say:"qauma",d:"Richte dich auf und sprich dabei den ersten Satz. Wenn du gerade stehst, sprich den zweiten."},
 {r:1,t:"Erste Niederwerfung",p:"sujud",n:3,say:"sudschud",d:"Sprich „Allahu akbar“ und geh nieder: zuerst die Knie, dann die Hände, dann Nase und Stirn. Sprich dreimal:",h:"Sieben Körperteile berühren den Boden: Stirn mit Nase, beide Hände, beide Knie und die Zehen beider Füße."},
 {r:1,t:"Sitzen zwischen den Niederwerfungen",p:"sit",say:"jalsa",d:"Richte dich mit „Allahu akbar“ auf und setz dich ruhig hin, bis der Körper zur Ruhe kommt. Die Hände liegen auf den Oberschenkeln."},
 {r:1,t:"Zweite Niederwerfung",p:"sujud",n:3,say:"sudschud",d:"Geh mit „Allahu akbar“ wieder nieder und sprich dreimal:",h:"Damit ist die erste Raka fertig."},
 {r:2,t:"Aufstehen: Basmala und Fatiha",p:"stand",say:"fatiha_b+fatiha",au:R(1,7),d:"Steh mit „Allahu akbar“ auf und leg die Hände wieder zusammen. Lies die Basmala und die Fatiha.",h:"Den Lobpreis und die Bitte um Schutz sprichst du nur in der ersten Raka."},
 {r:2,t:"Kurze Sure: Al-Ichlas",p:"stand",say:"ichlas",au:R(6222,6225),d:"Lies nach der Fatiha wieder eine kurze Sure, hier Al-Ichlas."},
 {r:2,t:"Verbeugung (Ruku)",p:"ruku",n:3,say:"ruku",d:"Sprich „Allahu akbar“, beuge dich und sprich dreimal:"},
 {r:2,t:"Aufrichten",p:"itidal",say:"qauma",d:"Richte dich auf und sprich dabei den ersten Satz, im Stehen den zweiten."},
 {r:2,t:"Erste Niederwerfung",p:"sujud",n:3,say:"sudschud",d:"Geh mit „Allahu akbar“ nieder und sprich dreimal:"},
 {r:2,t:"Sitzen zwischen den Niederwerfungen",p:"sit",say:"jalsa",d:"Setz dich mit „Allahu akbar“ kurz und ruhig hin."},
 {r:2,t:"Zweite Niederwerfung",p:"sujud",n:3,say:"sudschud",d:"Geh mit „Allahu akbar“ wieder nieder und sprich dreimal:",h:"Danach stehst du nicht auf, sondern bleibst sitzen."},
 {r:3,t:"Sitzen: At-Tahiyyat",p:"sit",finger:1,say:"tahiyyat",d:"Setz dich nach der zweiten Niederwerfung hin, die Hände auf den Oberschenkeln, und sprich At-Tahiyyat.",h:"Bei „la ilaha“ hebst du den rechten Zeigefinger, bei „illallah“ senkst du ihn wieder."},
 {r:3,t:"Segen für den Propheten ﷺ",p:"sit",say:"salawat",d:"Sprich im Sitzen den Segenswunsch für den Propheten ﷺ."},
 {r:3,t:"Bittgebet",p:"sit",say:"dua",d:"Bitte Allah um Gutes, zum Beispiel mit diesem Bittgebet aus dem Quran."},
 {r:3,t:"Salam nach rechts",p:"sit",turn:1,say:"salam",d:"Dreh den Kopf nach rechts und sprich den Friedensgruß.",h:"Die Figur schaut dich an: Ihre rechte Seite ist für dich links."},
 {r:3,t:"Salam nach links",p:"sit",turn:-1,say:"salam",d:"Dreh den Kopf nach links und sprich den Friedensgruß noch einmal. Dein Gebet ist fertig. Masha Allah!"}
];
const RNAME={1:"1. Raka",2:"2. Raka",3:"Abschluss"};
const COURSES={wudu:{steps:WUDU,title:"Die Gebetswaschung: alle Schritte",scene:"wudu"},gebet:{steps:GEBET,title:"Das Morgengebet: alle Schritte",scene:"gebet"}};

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
  if(o.turn){const x=q.mx,y=q.y-12,t=o.turn;s+=`<g class="arrowR"><path d="M${x-22} ${y}q22-14 44 0" fill="none" stroke="var(--teal)" stroke-width="3.5" stroke-linecap="round"/><path d="${t>0?`M${x-22} ${y}l9-1-4-8`:`M${x+22} ${y}l-9-1 4-8`}" fill="none" stroke="var(--teal)" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></g><text x="${x}" y="${y-14}" text-anchor="middle" font-family="Lexend,system-ui,sans-serif" font-weight="700" font-size="14" fill="var(--teal)">${t>0?"nach rechts":"nach links"}</text>`}
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
  $("stNo").textContent=(course==="wudu"?"Waschung":"Morgengebet"+(s.r?" · "+RNAME[s.r]:""))+" · Schritt "+(idx+1)+" von "+S.length;
  $("stTitle").textContent=s.t;$("stDo").textContent=s.d;
  const sy=s.say&&sayOf(s.say);$("stSay").hidden=!sy;
  if(sy){$("sAr").innerHTML=sy.ar.join("<br>");$("sTr").textContent=sy.tr;$("sDe").textContent=sy.de}
  $("stHint").hidden=!s.h;if(s.h)$("stHint").innerHTML="<b>Tipp:</b>&nbsp;"+s.h;
  $("prev").disabled=idx===0;$("next").textContent=idx===S.length-1?(course==="wudu"?"Weiter zum Gebet →":"Von vorn ↺"):"Weiter →";
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
function setPlay(v){playing=v;const b=$("play");b.textContent=v?"❚❚ Anhalten":"▶ Rezitation anhören";b.setAttribute("aria-pressed",String(v))}
function stopAudio(){player.pause();setPlay(false);$("aupos").textContent=""}
function playList(){if(!plist.length)return;pi=0;playOne()}
function playOne(){player.src=plist[pi];$("aupos").textContent=plist.length>1?"Vers "+(pi+1)+" von "+plist.length:"";player.play().then(()=>setPlay(true)).catch(()=>{setPlay(false);$("aupos").textContent="Ton konnte nicht starten. Tippe auf „Rezitation anhören“."})}
player.addEventListener("ended",()=>{if(pi<plist.length-1){pi++;playOne()}else{setPlay(false);$("aupos").textContent="";if(auto){clearTimeout(autoT);autoT=setTimeout(()=>{const S=COURSES[course].steps;if(idx<S.length-1)show(idx+1);else setAuto(false)},1200)}}});
player.addEventListener("error",()=>{setPlay(false);$("aupos").textContent="Die Aufnahme ist gerade nicht erreichbar."});
function audioFor(s){stopAudio();plist=s.au||[];const has=plist.length>0;$("auRow").hidden=course!=="gebet"||!s.say;$("play").hidden=!has;$("aunote").hidden=has;
  if(has&&soundOn)playList()}
$("play").addEventListener("click",()=>{if(playing){stopAudio()}else playList()});
$("sound").addEventListener("click",()=>{soundOn=!soundOn;$("sound").setAttribute("aria-pressed",String(soundOn));$("sound").textContent=soundOn?"🔊 Ton an":"🔈 Ton aus";if(soundOn&&plist.length&&!playing)playList();if(!soundOn)stopAudio()});
function next(){const S=COURSES[course].steps;if(idx<S.length-1)show(idx+1);else if(course==="wudu"){location.hash="gebet"}else show(0)}
function schedule(){clearTimeout(autoT);const s=COURSES[course].steps[idx];if(soundOn&&s.au&&s.au.length)return;const sy=s.say&&sayOf(s.say);const ms=Math.min(16000,5000+(sy?sy.tr.length*45:0));
  autoT=setTimeout(()=>{const S=COURSES[course].steps;if(idx<S.length-1)show(idx+1);else setAuto(false)},ms)}
function setAuto(v){auto=v;$("auto").setAttribute("aria-pressed",String(v));$("auto").textContent=v?"❚❚ Pause":"▶ Automatisch";clearTimeout(autoT);if(v)schedule()}
$("prev").addEventListener("click",()=>show(idx-1));
$("next").addEventListener("click",next);
$("auto").addEventListener("click",()=>setAuto(!auto));
document.addEventListener("keydown",e=>{if(e.target.closest("input,textarea,select"))return;if(e.key==="ArrowRight")next();if(e.key==="ArrowLeft")show(idx-1)});
function route(){const h=location.hash.slice(1);if(h==="wudu"||h==="gebet"){setCourse(h);if(h==="gebet"||h==="wudu"){}}else if(!h){setCourse(course,true)}}
addEventListener("hashchange",()=>{route();if(location.hash==="#gebet"||location.hash==="#wudu")$("stage").scrollIntoView({behavior:reduce?"auto":"smooth",block:"center"})});
route();if(!location.hash)setCourse("wudu");
})();
