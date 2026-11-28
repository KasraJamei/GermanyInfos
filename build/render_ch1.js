const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+process.cwd()+'/ch1.html');await p.waitForTimeout(800);
await p.pdf({path:'Germany_Chances_Summer_Winter_2027_Kasra_v1.pdf',format:'A4',landscape:true,printBackground:true,margin:{top:'10mm',bottom:'10mm',left:'9mm',right:'9mm'}});
await b.close();})();
