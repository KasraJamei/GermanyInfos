# -*- coding: utf-8 -*-
import json, datetime as d, re
from rows24 import ROWS
CITY=json.load(open('../t0.json'))
L19=open('build19.py').read().split('\n')
CSS='\n'.join(L19[78:92]).replace('%%','%')   # style block lines 79-92 (1-based)
CITYBOX=L19[120]; CITYTAB=L19[121]
FA=str.maketrans('0123456789','۰۱۲۳۴۵۶۷۸۹')
def fa(s): return s.translate(FA)
def B(x): return '<bdi>%s</bdi>'%x
MON=['ژانویه','فوریه','مارس','آوریل','مه','ژوئن','ژوئیه','اوت','سپتامبر','اکتبر','نوامبر','دسامبر']
TODAY=d.date(2026,11,7)
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
<h1>راهنمای ددلاین‌ها و وضعیت درخواست‌ها — آلمان (نسخه ۲۴)</h1>
<div class="sub">برای: کسری جامعی · به‌روزرسانی ۷ نوامبر ۲۰۲۶ (۱۶ آبان ۱۴۰۵) · نسخه ۲۴: همه‌ی برنامه‌های تابستان ۲۰۲۷ و برنامه‌های اصلی زمستان، یکی‌یکی از صفحه‌ی رسمی دانشگاه و DAAD (و در صورت لزوم پورتال درخواست) دوباره بررسی شدند. مسیر، هزینه‌ی درخواست، بازه‌ی زمانی و موانع اصلاح شد.</div>
<div class="box"><b>علامت‌ها:</b> ✅ = ۷ نوامبر از صفحه‌ی رسمی دانشگاه (+ DAAD یا پورتال) تأیید شد · ⚠ = منابع متناقض یا فقط منبع غیررسمی؛ قبل از اقدام چک کن · ↻ = این دور دوباره چک نشد (زمستان/حذف‌شده‌ها؛ قبل از باز شدن بازه‌شان چک می‌کنم). «شرق» = آلمان شرقی؛ «کاربردی» = Hochschule. uni-assist: €75 اولی، €30 بعدی. VPD = گواهی پیش‌بررسی uni-assist (تا ۸ هفته).</div>


<h2>۰. فقط بدون هزینه‌ی درخواست و بدون uni-assist (تأییدشده ۷ نوامبر)</h2>
<table><tr><th>برنامه</th><th>ترم</th><th>بازه</th><th>مسیر</th><th>شهریه</th><th>مانع / نکته</th></tr>
<tr class="opn"><td><b><bdi>Hof — Software Eng. for Industrial Applications</bdi></b></td><td>تابستان ۲۰۲۷</td><td>۵ → ۳۰ نوامبر</td><td>Primuss</td><td>€3,300</td><td>۱ سال کار ✔؛ هزینه‌ی درخواست ذکر نشده</td></tr>
<tr class="opn"><td><b><bdi>Albstadt — Industrial AI</bdi></b></td><td>تابستان ۲۰۲۷</td><td>۱ اکتبر → ۱۵ ژانویه</td><td>HISinOne</td><td>€1,500</td><td>در ۳ منبع هیچ VPD/هزینه‌ای ذکر نشده؛ در پورتال تأیید کن</td></tr>
<tr class="sn"><td><b><bdi>TUHH — Computer Science</bdi></b></td><td>تابستان ۲۰۲۷</td><td>۱ دسامبر → ۱۵ ژانویه</td><td>TUNE (بدون uni-assist)</td><td>ندارد</td><td>«TUHH هزینه‌ی درخواست نمی‌گیرد»؛ precheck معدل</td></tr>
<tr class="opn"><td><b><bdi>Hof — Applied Research in CS</bdi></b></td><td>تابستان ۲۰۲۷</td><td>۵ → ۳۰ نوامبر</td><td>Primuss</td><td>ندارد</td><td>❗ A1 رسمی لازم (نداری) + ۲۱۰ ECTS</td></tr>
<tr class="lt"><td><b><bdi>Bochum — Computer Science</bdi></b></td><td>زمستان ۲۰۲۷/۲۸</td><td>نوامبر → ۱۵ دسامبر ۲۰۲۶</td><td>apply.cs.rub.de</td><td>ندارد</td><td>هزینه ذکر نشده؛ C1</td></tr>
<tr class="lt"><td><b><bdi>Stuttgart — Computer Science (EN)</bdi></b></td><td>زمستان ۲۰۲۷/۲۸</td><td>تا ۱۵ ژانویه ۲۰۲۷</td><td>C@MPUS</td><td>€1,500</td><td>هزینه ذکر نشده</td></tr>
<tr class="lt"><td><b><bdi>Hamburg — IAS / DSAI</bdi></b></td><td>زمستان ۲۰۲۷/۲۸</td><td>۱۵ فوریه → ۳۱ مارس</td><td>STiNE</td><td>ندارد</td><td>هزینه ذکر نشده</td></tr>
<tr class="lt"><td><b><bdi>Siegen — Computer Science</bdi></b></td><td>زمستان ۲۰۲۷/۲۸</td><td>۱ ژانویه → ۳۰ آوریل</td><td>UNISONO</td><td>ندارد</td><td>✔ صریحاً بدون هزینه؛ آزمون + مصاحبه</td></tr>
</table>
<div class="box">❗ Aalen، Amberg-Weiden، THI، THWS، Heilbronn و HSBI با اینکه پورتال خودشان را دارند، برای مدرک خارجی VPD از uni-assist می‌خواهند؛ پس بدون هزینه نیستند.</div>

<h2>۱. ارسال‌شده‌ها (%s برنامه)</h2>
<table><tr><th>برنامه</th><th>تاریخ و شماره</th><th>مسیر</th><th>نکته / قدم بعدی</th></tr>%s</table>

<h2>۲. تقویم مهلت‌های پیش رو (به ترتیب تاریخ)</h2>
<div class="box">فقط برنامه‌هایی که مانع جدی ندارند. قرمز = کمتر از یک ماه مانده. برنامه‌های uni-assist زمان پردازش دارند؛ چند هفته زودتر بفرست.</div>
<table class="cal"><tr><th>مهلت</th><th>برنامه</th><th>ترم</th><th>مسیر</th><th>نکته</th></tr>%s</table>

<h2>۳. جدول جامع — همه‌ی برنامه‌ها</h2>
<div class="box">ستون «تابستان» = ورودی آوریل ۲۰۲۷، «زمستان» = ورودی اکتبر ۲۰۲۷. «باز → بسته». «—» یعنی هزینه‌ای روی سایت ذکر نشده. TU/e به راهنمای هلند منتقل شد.</div>
<table class="big"><tr><th>وضعیت</th><th>برنامه</th><th>مسیر</th><th>هزینه‌ی درخواست</th><th>شهریه / ترم</th><th>تابستان ۲۰۲۷</th><th>زمستان ۲۰۲۷/۲۸</th><th>نکته</th><th>شهر · جمعیت ≈</th><th>اتاق WG / کل ماهانه ≈</th><th>بازار کار IT</th><th>THE 2027 آلمان · جهان</th></tr>%s</table>

<h2>۴. چک‌لیست باز</h2>
<ul class="chk">
<li>✔ <b>ارسال شد (۱۰ برنامه):</b> Göttingen Applied CS و ADS، Bonn CS و Cyber Security، Hildesheim SE و DA، Freiburg CS و ESE، Duisburg-Essen ESE و Communications Engineering</li>
<li>☐ <b>Deggendorf:</b> پرداخت €60 + «Bewerbung absenden» تا <b>۱۵ نوامبر</b>؛ در همان حساب AI&amp;DS و Automotive SE (۱۵ نوامبر) و HPC/QC (۱ دسامبر)</li>
<li>☐ <b>Hof SEIA:</b> بدون هزینه‌ی درخواست، ۵ → ۳۰ نوامبر (شهریه €3,300)</li>
<li>☐ <b>Albstadt Industrial AI:</b> ۱ اکتبر → ۱۵ ژانویه؛ اول در پورتال چک کن VPD نخواهد</li>
<li>☐ <b>TUHH CS:</b> ۱ دسامبر → ۱۵ ژانویه؛ precheck؛ module manual آماده کن</li>
<li>☐ <b>Bochum (زمستان):</b> تا ۱۵ دسامبر؛ انگیزه‌نامه + ایمیل دو استاد</li>
<li>☐ <b>Stuttgart (زمستان):</b> تا ۱۵ ژانویه</li>
<li>☐ <b>Aalen ML&amp;DA:</b> پیش‌نویس ذخیره است؛ فقط اگر uni-assist را باز کنی</li>
<li>☐ <b>اگر uni-assist را باز کنی:</b> ۱۵ نوامبر Ilmenau و Magdeburg؛ ۳۰ نوامبر Rostock، Dresden؛ Emden ۳۰ نوامبر؛ ۱۵ دسامبر Passau، Kiel؛ ۳۱ دسامبر Marburg؛ ۱۵ ژانویه Anhalt، HSBI، BTU، Weimar، Dortmund، THI Cybersecurity، Rhine-Waal. VPD برای Amberg-Weiden/THI/HSBI/Aalen زمان‌بر است</li>
<li>☐ <b>TU/e (هلند):</b> ترجمه‌ی رسمی انگلیسی ندارد → فعلاً کنار گذاشته شد</li>
<li>☐ آیلتس فعلی تا حدود ژوئن ۲۰۲۷ معتبر است (برخی برنامه‌ها حداکثر ۲ سال قبول دارند)</li>
</ul>

<h2>۵. شهرها: جمعیت، اجاره، هزینه‌ی ماهانه و بازار کار IT (بررسی ۲۶ اکتبر ۲۰۲۶)</h2>
%s
%s

<div class="sub" style="margin-top:10px">منابع اصلی این نسخه (۷ نوامبر): صفحه‌های رسمی Hof، TUHH (و راهنمای How-to-apply 2026)، UHH، Ulm، TU Ilmenau، Aalen (پورتال)، Deggendorf (DAAD)، Albstadt (آیین‌نامه + بروشور)، HFT، Heilbronn، TH Nürnberg، OVGU، Hannover (DAAD)، Rostock، TU Dresden، Fulda، Passau، Kiel (DAAD)، Marburg، Lübeck (آیین‌نامه)، BTU، Weimar، THI، OTH Amberg-Weiden، TU Dortmund، HSBI، Anhalt (DAAD)، Rhine-Waal (DAAD)، THWS، Reutlingen، Siegen، Stuttgart، Bochum، Hamburg IAS/DSAI، Konstanz. منابع قبلی: صفحه‌های رسمی Duisburg-Essen (ISE)، OVGU Magdeburg، TU Ilmenau، TU Dresden، Rostock، Paderborn، Regensburg، TUM، Lübeck، BTU، Bauhaus-Universität Weimar، Bamberg، Bayreuth، Augsburg، Siegen، Hamburg (IAS، DSAI)، TUHH، Bochum، Stuttgart، HTWG Konstanz، TU Chemnitz، Leipzig، TU Dortmund، Esslingen، Mannheim، LMU؛ صفحه‌های DAAD برای Hannover، Kiel، Fulda، Hof، Emden/Leer و Rhine-Waal.</div>
</body></html>'''%(fa(str(n_done)),srows,crows,brows,CITYBOX,CITYTAB)
open('g24.html','w').write(html)
print('ok',len(html),len(cal))
