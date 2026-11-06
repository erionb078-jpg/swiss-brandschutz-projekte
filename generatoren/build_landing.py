import base64,shutil,os,re
D='abrar-website'
shutil.rmtree(D,ignore_errors=True);os.makedirs(D+'/buch')
shutil.copytree('abrar-online-buch/pages',D+'/buch/pages')
shutil.copytree('abrar-online-buch/spiel',D+'/spiel')
shutil.copytree('abrar-online-buch/sira',D+'/sira')
shutil.copy([os.path.join('/mnt/user-data/attachments/133ba4ae-4316-560e-9041-7dc80082bb1c',f) for f in os.listdir('/mnt/user-data/attachments/133ba4ae-4316-560e-9041-7dc80082bb1c') if f.endswith('.pdf')][0],D+'/buch/Abrar_Quran_Reading_2026.pdf')
# book: fix links + home link on title
b=open('abrar-online-buch/index.html').read()
b=b.replace('href="spiel/index.html"','href="../spiel/index.html"').replace('href="sira/index.html"','href="../sira/index.html"')
a='<div class="brand"><b>Das Abrar Online Buch</b>'
assert b.count(a)==1
b=b.replace(a,'<a class="brand" href="../index.html" style="text-decoration:none;color:inherit" title="Zur Startseite"><b>Das Abrar Online Buch</b>')
b=b.replace('<span class="sub">Quran Reading · Step by Step</span></div>','<span class="sub">← Startseite · Quran Reading</span></a>',1)
open(D+'/buch/index.html','w').write(b)
# games: back link to start page
HOME='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/></svg>'
for f,old in [(D+'/spiel/index.html','Zum Buch</a>'),(D+'/sira/index.html','Buch</a>')]:
    s=open(f).read()
    m=re.search(r'<a class="chip" href="\.\./index\.html"[^>]*>.*?'+re.escape(old),s,flags=re.S)
    assert m,f
    rep=re.sub(r'<svg.*?</svg>',HOME,m.group(0),count=1,flags=re.S).replace(old,'Start</a>').replace('Zurück zum Buch','Zur Startseite')
    s=s[:m.start()]+rep+s[m.end():]
    open(f,'w').write(s)
