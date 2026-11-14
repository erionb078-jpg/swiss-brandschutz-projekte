const {chromium}=require('playwright');const fs=require('fs');const D=process.argv[2];(async()=>{const b=await chromium.launch();const p=await b.newPage();
for(const f of fs.readdirSync(D+'/printhtml')){await p.goto('file://'+D+'/printhtml/'+f);await p.waitForTimeout(900);
await p.pdf({path:D+'/out/downloads/'+f.replace('.html','.pdf'),printBackground:true,preferCSSPageSize:true});}
await p.goto('file://'+D+'/sheets.html');await p.waitForTimeout(1500);
await p.pdf({path:D+'/out/uebungsblaetter/Harf-Uebungsblaetter.pdf',format:'A4',printBackground:true,preferCSSPageSize:true});
await b.close();})();
