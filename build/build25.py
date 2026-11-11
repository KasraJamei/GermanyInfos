# -*- coding: utf-8 -*-
import json, datetime as d, re
from rows25 import ROWS
CITY=json.load(open('../t0.json'))
L19=open('build19.py').read().split('\n')
CSS='\n'.join(L19[78:92]).replace('%%','%')   # style block lines 79-92 (1-based)
CITYBOX=L19[120]; CITYTAB=L19[121]
FA=str.maketrans('0123456789','۰۱۲۳۴۵۶۷۸۹')
def fa(s): return s.translate(FA)
def B(x): return '<bdi>%s</bdi>'%x
MON=['ژانویه','فوریه','مارس','آوریل','مه','ژوئن','ژوئیه','اوت','سپتامبر','اکتبر','نوامبر','دسامبر']
TODAY=d.date(2026,11,9)
def fdate(iso):
    x=d.date.fromisoformat(iso); return fa('%d %s %d'%(x.day,MON[x.month-1],x.year))
CLS={'done':'done','open':'opn','soon':'sn','winter':'lt','passed':'lt','excl':'bad'}
GT={'done':'✅ ارسال‌شده','open':'🟢 الان باز (ترم تابستان ۲۰۲۷، مگر خلافش نوشته شده)','soon':'🔵 به‌زودی باز می‌شود','winter':'⚪ فقط ورودی زمستان ۲۰۲۷/۲۸','passed':'⏹ مهلت تابستان ۲۰۲۷ گذشته (برای زمستان می‌ماند)','excl':'❌ مانع جدی یا نامناسب'}

# ---------- 1. submitted ----------
done=[r for r in ROWS if r['g']=='done']
srows=''.join('<tr class="ok"><td><b>%s</b></td><td>%s</td><td>%s</td><td>%s</td></tr>'%(B(r['p']),r['st'].replace('✔ ',''),r['r'],r['n']) for r in done)

# ---------- 2. calendar ----------
cal=[r for r in ROWS if r['dl'] and r['g'] in ('open','soon','winter','passed') and d.date.fromisoformat(r['dl'])>=TODAY]
cal.sort(key=lambda r:r['dl'])
def short(n):
    n=re.sub(r'^[✔↻ ]+','',n); return n
crows=''
for r in cal:
    days=(d.date.fromisoformat(r['dl'])-TODAY).days
    urg=' style="color:#b00020"' if days<=31 else ''
    crows+='<tr class="%s"><td class="dt"%s>%s<br><span>%s روز مانده</span></td><td><b>%s</b><br><small>%s</small></td><td>%s</td><td>%s</td><td>%s</td></tr>'%(
        CLS[r['g']],urg,fdate(r['dl']),fa(str(days)),B(r['p']),r['st'],r['dlw'],r['r'],short(r['n']))

# ---------- 3. comprehensive ----------
brows=''
for g in ('done','open','soon','winter','passed','excl'):
    rs=[r for r in ROWS if r['g']==g]
    brows+='<tr class="grp"><td colspan="12">%s — %s برنامه</td></tr>'%(GT[g],fa(str(len(rs))))
    for r in rs:
        c=CITY[r['c']] if r['c'] is not None else ['']*8+['—']*4
        brows+='<tr class="%s"><td>%s</td><td><b>%s</b></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'%(
            CLS[g],r.get('v','↻')+' '+r['st'],B(r['p']),r['r'],r['f'],r['t'],r['s'],r['w'],r['n'],c[8],c[9],c[10],c[11])

n_done=len(done)
html='''<!doctype html><html lang="fa" dir="rtl"><head><meta charset="utf-8"><style>'''+CSS.split('</style>')[0]+'''
tr.grp td{background:#0b3d6b!important;color:#fff!important;font-weight:700;font-size:9px!important}
table.cal td{font-size:9.5px;padding:4px 6px}
</style></head><body>
<h1>راهنمای ددلاین‌ها و وضعیت درخواست‌ها — آلمان (نسخه ۲۵)</h1>
<div class="sub">برای: کسری جامعی · به‌روزرسانی ۹ نوامبر ۲۰۲۶ (۱۸ آبان ۱۴۰۵) · نسخه ۲۵: کل لیست DAAD Study Guide (۲۸۷ برنامه‌ی انگلیسی، رشته‌های ریاضی/علوم طبیعی) غربال شد؛ ۹۱ برنامه‌ی کامپیوتری تازه از صفحه‌ی DAAD و در موارد مهم از سایت رسمی بررسی شد؛ ۱۵ دانشگاه لیست جدید هم از سایت رسمی چک شد. ردیف‌های تازه با 🆕۲۵ مشخص‌اند.</div>
<div class="box"><b>علامت‌ها:</b> ✅ = از صفحه‌ی رسمی دانشگاه (+ DAAD) تأیید شد (۷–۹ نوامبر) · ⚠ = منابع متناقض یا فقط DAAD؛ قبل از اقدام چک کن · ↻ = این دور دوباره چک نشد</div>


<h2>۰. مستقیم، بدون uni-assist و بدون VPD (به ترتیب مهلت)</h2>
<table><tr><th>برنامه</th><th>ترم</th><th>بازه</th><th>مسیر</th><th>هزینه‌ی درخواست</th><th>شهریه</th><th>مانع / نکته</th></tr>
<tr class="opn"><td><b><bdi>Saarland — Cybersecurity 🆕</bdi></b></td><td>تابستان ۲۰۲۷</td><td style="color:#b00020"><b>تا ۱۵ نوامبر</b></td><td>apply.cs.uni-saarland.de</td><td>ذکر نشده</td><td>ندارد</td><td>GRE نمی‌خواهد؛ C1 ✔؛ <b>۲ توصیه‌نامه‌ی استاد</b> + بیانیه</td></tr>
<tr class="opn"><td><b><bdi>Saarland — Data Science &amp; AI 🆕</bdi></b></td><td>تابستان ۲۰۲۷</td><td style="color:#b00020"><b>تا ۱۵ نوامبر</b></td><td>همان پورتال</td><td>ذکر نشده</td><td>ندارد</td><td>GRE نمی‌خواهد؛ ۲ توصیه‌نامه؛ ⚠ پیش‌زمینه‌ی ML/AI</td></tr>
<tr class="opn"><td><b><bdi>Hof — Software Eng. for Industrial Applications</bdi></b></td><td>تابستان ۲۰۲۷</td><td>۵ → ۳۰ نوامبر</td><td>Primuss</td><td>ذکر نشده</td><td>€3,300</td><td>۱ سال کار ✔</td></tr>
<tr class="opn"><td><b><bdi>Hildesheim — Future Analytics: AI &amp; Audio 🆕</bdi></b></td><td>تابستان ۲۰۲۷</td><td>تا ۱۵ دسامبر</td><td>ismll (همان پورتال قبلی‌ات)</td><td>ذکر نشده</td><td>ندارد</td><td>برنامه‌ی تازه؛ AI + صوت/موسیقی؛ ⚠ جزئیات بعداً</td></tr>
<tr class="sn"><td><b><bdi>TUHH — Computer Science</bdi></b></td><td>تابستان ۲۰۲۷</td><td>۱ دسامبر → ۱۵ ژانویه</td><td>TUNE</td><td>ندارد ✔</td><td>ندارد</td><td>precheck معدل</td></tr>
<tr class="opn"><td><b><bdi>Albstadt — Industrial AI</bdi></b></td><td>تابستان ۲۰۲۷</td><td>تا ۱۵ ژانویه</td><td>HISinOne</td><td>ذکر نشده</td><td>€1,500</td><td>در پورتال تأیید کن VPD نخواهد</td></tr>
<tr class="opn"><td><b><bdi>Saarland — Media Informatics 🆕</bdi></b></td><td>تابستان ۲۰۲۷</td><td>تا ۱۵ ژانویه</td><td>sim.uni-saarland.de</td><td>ذکر نشده</td><td>ندارد</td><td>C1 ✔؛ ۲ توصیه‌نامه</td></tr>
<tr class="opn"><td><b><bdi>Chemnitz — Web Engineering 🆕</bdi></b></td><td>تابستان ۲۰۲۷</td><td>تا ۱۵ ژانویه</td><td>EduApplication</td><td>⚠ ذکر نشده</td><td>ندارد</td><td>بدون گزینش؛ B2</td></tr>
<tr class="sn"><td><b><bdi>TH OWL — Information Technology 🆕</bdi></b></td><td>تابستان ۲۰۲۷</td><td>۱۷ نوامبر → ۱۵ ژانویه</td><td>KIS</td><td>ذکر نشده</td><td>ندارد</td><td>برق/IT/CS؛ ⚠ ECTS/معدل نامشخص</td></tr>
<tr class="sn"><td><b><bdi>Trier — Data Science (اصلاح)</bdi></b></td><td>تابستان ۲۰۲۷</td><td>۱۵ دسامبر → ۱۵ ژانویه</td><td>PORTA</td><td><b>€70</b></td><td>ندارد</td><td>معدل ≤۱٫۷ (۱٫۷۷→۱٫۷ مرزی ⚠)</td></tr>
<tr class="sn"><td><b><bdi>TU Darmstadt — CS / AI&amp;ML (اصلاح)</bdi></b></td><td>تابستان ۲۰۲۷</td><td>۱ دسامبر → ۱۵ ژانویه</td><td>پورتال + پست</td><td>ذکر نشده</td><td>ندارد</td><td>⚠ اگر مدارک کافی نباشد آزمون حضوری (مارس)</td></tr>
<tr class="sn"><td><b><bdi>Augsburg — Data Science 🆕</bdi></b></td><td>تابستان ۲۰۲۷</td><td>تا ۱ مارس (برای ویزا زودتر)</td><td>VIBS</td><td><b>ندارد ✔</b></td><td>ندارد</td><td>رسمی: بدون VPD، بدون آزمون؛ معدل ≤۲٫۷ ✔؛ ⚠ ۴ ECTS DS/ML</td></tr>
<tr class="sn"><td><b><bdi>Augsburg — Math &amp; CS 🆕</bdi></b></td><td>تابستان ۲۰۲۷</td><td>تا ۱ مارس</td><td>VIBS</td><td>ندارد ✔</td><td>ندارد</td><td>⚠ ۳۰ ECTS ریاضی اثبات‌محور</td></tr>
<tr class="lt"><td><b><bdi>Stuttgart — INFOTECH 🆕</bdi></b></td><td>زمستان ۲۰۲۷/۲۸</td><td><b>۱۵ نوامبر → ۱۵ ژانویه</b></td><td>C@MPUS</td><td>ذکر نشده</td><td>€1,500</td><td>همراه Stuttgart CS؛ C1 ✔؛ ≤۲٫۵ ✔</td></tr>
<tr class="lt"><td><b><bdi>Bochum — Computer Science</bdi></b></td><td>زمستان ۲۰۲۷/۲۸</td><td>تا ۱۵ دسامبر</td><td>apply.cs.rub.de</td><td>ذکر نشده</td><td>ندارد</td><td>C1</td></tr>
<tr class="lt"><td><b><bdi>TUHH — Data Science / ICS 🆕</bdi></b></td><td>زمستان ۲۰۲۷/۲۸</td><td>تا ۱ مارس</td><td>TUNE</td><td>ندارد ✔</td><td>ندارد</td><td>C1</td></tr>
<tr class="lt"><td><b><bdi>Hamburg — IAS / DSAI</bdi></b></td><td>زمستان ۲۰۲۷/۲۸</td><td>۱۵ فوریه → ۳۱ مارس</td><td>STiNE</td><td>ذکر نشده</td><td>ندارد</td><td></td></tr>
<tr class="lt"><td><b><bdi>Siegen — CS / HCI 🆕</bdi></b></td><td>زمستان ۲۰۲۷/۲۸</td><td>CS تا ۳۰ آوریل؛ HCI ۱–۳۰ آوریل</td><td>UNISONO</td><td>ندارد ✔</td><td>ندارد</td><td>صریحاً بدون هزینه</td></tr>
<tr class="lt"><td><b><bdi>RUB — Cognitive Science 🆕</bdi></b></td><td>زمستان ۲۰۲۷/۲۸</td><td>تا ۱۵ ژوئیه</td><td>hio</td><td>ذکر نشده</td><td>ندارد</td><td>CS در لیست رشته‌ها</td></tr>
</table>
<div class="box">❗ Aalen، Amberg-Weiden، THI، THWS، Heilbronn، HSBI و Coburg با اینکه پورتال خودشان را دارند، برای مدرک خارجی VPD از uni-assist می‌خواهند. Passau، Marburg، Ilmenau، Magdeburg، Weimar، Osnabrück و TU Dortmund فقط از uni-assist (€75) درخواست می‌گیرند.</div>

<h2>۱. ارسال‌شده‌ها (%s برنامه)</h2>
<table><tr><th>برنامه</th><th>تاریخ و شماره</th><th>مسیر</th><th>نکته / قدم بعدی</th></tr>%s</table>

<h2>۲. تقویم مهلت‌های پیش رو (به ترتیب تاریخ)</h2>
<div class="box">فقط برنامه‌هایی که مانع جدی ندارند. قرمز = کمتر از یک ماه مانده. برنامه‌های uni-assist زمان پردازش دارند؛ چند هفته زودتر بفرست.</div>
<table class="cal"><tr><th>مهلت</th><th>برنامه</th><th>ترم</th><th>مسیر</th><th>نکته</th></tr>%s</table>

<h2>۳. جدول جامع — همه‌ی برنامه‌ها</h2>
<div class="box">ستون «تابستان» = ورودی آوریل ۲۰۲۷، «زمستان» = ورودی اکتبر ۲۰۲۷. «باز → بسته». «—» یعنی هزینه‌ای روی سایت ذکر نشده. TU/e به راهنمای هلند منتقل شد.</div>
<table class="big"><tr><th>وضعیت</th><th>برنامه</th><th>مسیر</th><th>هزینه‌ی درخواست</th><th>شهریه / ترم</th><th>تابستان ۲۰۲۷</th><th>زمستان ۲۰۲۷/۲۸</th><th>نکته</th><th>شهر · جمعیت ≈</th><th>اتاق WG / کل ماهانه ≈</th><th>بازار کار IT</th><th>THE 2027 آلمان · جهان</th></tr>%s</table>

<h2>۴. چک‌لیست باز (به ترتیب فوریت)</h2>
<ul class="chk">
<li>✔ <b>ارسال شد (۱۰ برنامه):</b> Göttingen ×۲، Bonn ×۲ (❌ Cyber Security رد شد ۸ نوامبر؛ CS هنوز Received)، Hildesheim ×۲، Freiburg ×۲، Duisburg-Essen ×۲</li>
<li>☐ <b>تا ۱۵ نوامبر — Saarland Cybersecurity و/یا Data Science &amp; AI:</b> رایگان و مستقیم؛ فوراً از دو استاد توصیه‌نامه بخواه</li>
<li>☐ <b>تا ۱۵ نوامبر — Deggendorf:</b> پرداخت €60 + «Bewerbung absenden» (AI&amp;DS، Automotive SE هم همین حساب)</li>
<li>☐ <b>اگر uni-assist را باز کنی، تا ۱۵ نوامبر:</b> Ilmenau Data Science و Research in Media Eng.، Magdeburg DKE و Digital Engineering</li>
<li>☐ <b>تا ۳۰ نوامبر — Hof SEIA</b> (Primuss، رایگان)</li>
<li>☐ <b>۱ دسامبر:</b> Deggendorf HPC/QC؛ TUHH CS باز می‌شود؛ Darmstadt باز می‌شود (کپی پستی!)</li>
<li>☐ <b>تا ۱۵ دسامبر:</b> Hildesheim Future Analytics (رایگان)؛ Bochum CS (زمستان)؛ uni-assist: Passau CS و AI Engineering، Osnabrück Cognitive Science</li>
<li>☐ <b>تا ۳۱ دسامبر (uni-assist):</b> Marburg CS / Data Science / Business Informatics</li>
<li>☐ <b>تا ۱۵ ژانویه:</b> Trier (€70)، Chemnitz Web Eng.، Saarland Media Informatics، TH OWL IT، TUHH CS، Albstadt، Stuttgart CS + INFOTECH (زمستان)؛ uni-assist: Weimar HCI، TU Dortmund DS و A&amp;R؛ VPD: THI ×۴</li>
<li>☐ <b>تا ۱ مارس:</b> Augsburg Data Science و Math &amp; CS (رایگان، بدون VPD؛ برای ویزا هرچه زودتر)</li>
<li>☐ <b>Aalen ML&amp;DA:</b> پیش‌نویس ذخیره است؛ فقط با VPD</li>
<li>☐ <b>ریزنمرات را برای این‌ها چک کن:</b> Augsburg DS (۴ ECTS DS/ML)، Saarland DSAI (ML/AI)، Passau AIE (۳۵ ریاضی + ۴۰ CS)، Trier (معدل مرزی)</li>
<li>☐ آیلتس فعلی تا حدود ژوئن ۲۰۲۷ معتبر است</li>
</ul>

<h2>۵. شهرها: جمعیت، اجاره، هزینه‌ی ماهانه و بازار کار IT (بررسی ۲۶ اکتبر ۲۰۲۶)</h2>
%s
%s

<div class="sub" style="margin-top:10px">منابع اصلی (۹ نوامبر): لیست DAAD Study Guide (study-guide.com، ۲۸۷ برنامه، ۱۵ صفحه) و صفحه‌ی جزئیات هر برنامه؛ صفحه‌های رسمی Saarland (cysec، آیین‌نامه‌ی Cybersecurity، SIC، UMTL)، Augsburg (DS، Math&amp;CS)، Chemnitz (Web Eng + صفحه‌ی درخواست)، Hildesheim، TH OWL، Weimar HCI، Passau (AIE + درخواست بین‌المللی)، Marburg (مهلت‌ها)، TU Ilmenau (مهلت‌ها)، Stuttgart INFOTECH، HPI، TUM CSE، Tübingen MedInf، TU Dortmund، Trier، TU Darmstadt، Uni Köln، Würzburg، Regensburg، Halle، Koblenz، Lübeck، TH Köln، HS Bochum، HTWK. منابع v24 (۷ نوامبر): صفحه‌های رسمی Hof، TUHH (و راهنمای How-to-apply 2026)، UHH، Ulm، TU Ilmenau، Aalen (پورتال)، Deggendorf (DAAD)، Albstadt (آیین‌نامه + بروشور)، HFT، Heilbronn، TH Nürnberg، OVGU، Hannover (DAAD)، Rostock، TU Dresden، Fulda، Passau، Kiel (DAAD)، Marburg، Lübeck (آیین‌نامه)، BTU، Weimar، THI، OTH Amberg-Weiden، TU Dortmund، HSBI، Anhalt (DAAD)، Rhine-Waal (DAAD)، THWS، Reutlingen، Siegen، Stuttgart، Bochum، Hamburg IAS/DSAI، Konstanz. منابع قبلی: صفحه‌های رسمی Duisburg-Essen (ISE)، OVGU Magdeburg، TU Ilmenau، TU Dresden، Rostock، Paderborn، Regensburg، TUM، Lübeck، BTU، Bauhaus-Universität Weimar، Bamberg، Bayreuth، Augsburg، Siegen، Hamburg (IAS، DSAI)، TUHH، Bochum، Stuttgart، HTWG Konstanz، TU Chemnitz، Leipzig، TU Dortmund، Esslingen، Mannheim، LMU؛ صفحه‌های DAAD برای Hannover، Kiel، Fulda، Hof، Emden/Leer و Rhine-Waal.</div>
</body></html>'''%(fa(str(n_done)),srows,crows,brows,CITYBOX,CITYTAB)
open('g25.html','w').write(html)
print('ok',len(html),len(cal))
