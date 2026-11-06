import os,subprocess
from playwright.sync_api import sync_playwright
OUT='/home/claude/en'
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page()
    for f in sorted(os.listdir('/tmp/sp/printhtml')):
        pg.goto('file:///tmp/sp/printhtml/'+f);pg.wait_for_timeout(900)
        pg.pdf(path=OUT+'/downloads/'+f.replace('.html','.pdf'),print_background=True,prefer_css_page_size=True)
    pg.goto('file:///tmp/sp/sheets.html');pg.wait_for_timeout(1500)
    pg.pdf(path=OUT+'/uebungsblaetter/Harf-Uebungsblaetter.pdf',format='A4',print_background=True,prefer_css_page_size=True)
    b.close()
