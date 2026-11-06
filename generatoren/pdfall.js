const {chromium}=require('playwright');const fs=require('fs');(async()=>{const b=await chromium.launch();const p=await b.newPage();
for(const f of fs.readdirSync('printhtml')){await p.goto('file://'+process.cwd()+'/printhtml/'+f);await p.waitForTimeout(900);
await p.pdf({path:'downloads/'+f.replace('.html','.pdf'),printBackground:true,preferCSSPageSize:true});}
await b.close();})();
