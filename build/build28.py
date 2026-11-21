# -*- coding: utf-8 -*-
import datetime as d, re
from rows28 import ROWS
FA = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
def fa(s): return s.translate(FA)
def B(x): return '<bdi>%s</bdi>' % x
MON = ['ژانویه','فوریه','مارس','آوریل','مه','ژوئن','ژوئیه','اوت','سپتامبر','اکتبر','نوامبر','دسامبر']
TODAY = d.date(2026, 11, 21)
def fdate(iso):
    x = d.date.fromisoformat(iso); return fa('%d %s %d' % (x.day, MON[x.month-1], x.year))
CLS = {'done':'done','open':'opn','soon':'sn','winter':'lt','passed':'lt','excl':'bad'}
GT = {'done':'✅ ارسال‌شده','open':'🟢 الان باز (ترم تابستان ۲۰۲۷، مگر خلافش نوشته شده)','soon':'🔵 به‌زودی باز می‌شود','winter':'⚪ فقط ورودی زمستان ۲۰۲۷/۲۸','passed':'⏹ مهلت تابستان ۲۰۲۷ گذشته (برای زمستان می‌ماند)','excl':'❌ مانع جدی یا نامناسب'}

CSS = '''
@font-face{font-family:Vaz;src:url(Vazirmatn-Regular.ttf)}
@font-face{font-family:Vaz;font-weight:700;src:url(Vazirmatn-Bold.ttf)}
body{font-family:Vaz,sans-serif;font-size:10px;color:#1b2430;margin:0}
h1{font-size:19px;color:#0b3d6b;margin:0 0 4px}
h2{font-size:14px;color:#0b3d6b;border-bottom:2px solid #0b3d6b;padding-bottom:3px;margin:16px 0 6px;page-break-after:avoid}
h3{font-size:12px;margin:10px 0 4px;color:#0b3d6b}
.sub{color:#555;font-size:9px;margin-bottom:6px;line-height:1.6}
.box{background:#eef3f8;border-right:4px solid #0b3d6b;padding:6px 9px;margin:6px 0;line-height:1.7;font-size:9.5px}
.warn{background:#fdecee;border-right-color:#b00020}
.good{background:#e8f5ec;border-right-color:#1e7b3a}
table{border-collapse:collapse;width:100%;margin:4px 0 8px}
th{background:#0b3d6b;color:#fff;font-size:9px;padding:4px 5px;text-align:right}
td{border:1px solid #d5dbe3;padding:3px 5px;vertical-align:top;font-size:8.8px;line-height:1.5}
tr{page-break-inside:avoid} thead{display:table-header-group}
tr.done td{background:#eaf6ee} tr.opn td{background:#f2fbf4} tr.sn td{background:#eef5fd}
tr.lt td{background:#fafafa;color:#444} tr.bad td{background:#fdf0f1;color:#5a2a30}
tr.grp td{background:#0b3d6b!important;color:#fff!important;font-weight:700;font-size:9px}
td.dt{white-space:nowrap;font-weight:700} td.dt span{font-weight:400;font-size:8px;color:#666}
table.big td{font-size:8px} .red{color:#b00020;font-weight:700}
ul.chk{list-style:none;padding:0;margin:4px 0} ul.chk li{padding:3px 0;border-bottom:1px dotted #ccc;font-size:9.5px}
ol{margin:4px 0;padding-right:18px} ol li{margin:2px 0;font-size:9.5px;line-height:1.7}
'''

# ---------- A. decision tables (curated, 21 Nov) ----------
UA_PICK = [
 ('1','Rostock — Computer Science International','<span class="red">۳۰ نوامبر</span>','€75','همه‌ی شرایط جور است: ≥۸۵٪ (تو ~۸۷٪)، ≥۱۸ ریاضی، ≥۱۲ نظریه، آیلتس ۷ زیر ۲ سال. <b>اول این را بزن.</b>'),
 ('2','Passau — Computer Science','۱۵ دسامبر','+€30','≥۱۱۰ ECTS کامپیوتر؛ ≤۲٫۷ ✔. ⚠ قبل از پرداخت: وضعیت H+ دانشگاهت در anabin؛ ⚠ آلمانی A1 را در صفحه چک کن. AI Engineering فقط اگر ریاضی/نظریه قوی است.'),
 ('3','Marburg — Computer Science (یا Data Science)','۳۱ دسامبر ⚠','+€30','≥۹۰ CP CS+ریاضی، ≤۳٫۲ ✔، C1 ✔. ⚠ مهلت را در My assist تأیید کن. فقط یکی از دو برنامه.'),
 ('4','TU Dortmund — Data Science','۱۵ ژانویه','+€30','بدون GRE و VPD؛ ≥۴۴ CP (۱۶ CS، ۸ ریاضی، ۸ آمار ⚠)؛ B2. module handbook آماده کن.'),
 ('5','TH OWL — Information Technology','۱۵ ژانویه','+€30','❗ برای غیراروپایی از uni-assist (نه KIS). شهریه ندارد؛ B2. ⚠ ECTS/معدل در صفحه نیامده.'),
 ('اختیاری','Weimar — CS for Digital Media / HCI · BTU — AI','۱۵ ژانویه','+€30 هرکدام','Weimar: گزارش پروژه به‌جای پایان‌نامه؛ HCI معدل ≤۲٫۰. BTU: ML، برنامه‌نویسی، ریاضی.'),
]
UA_NO = [
 ('TU Dresden CS','لیسانس «Computer Science» می‌خواهد و GRE «به‌شدت توصیه» → ریسک بالا'),
 ('Emden/Leer Industrial Informatics','۲۱۰ ECTS (یا ۳۰ ECTS تکمیلی)؛ تمرکز real-time/صنعتی'),
 ('Kiel (CAU) CS','مهلت متناقض و فقط لیسانس CS مشابه Kiel — اول ایمیل بزن'),
 ('Osnabrück Cognitive Science','لیسانس Cognitive Science یا «مشابه» — مهندسی کامپیوتر نامطمئن'),
 ('Paderborn CS','GRE/dMAT مگر معافیت (معدل تبدیلی <۱٫۸؛ تو ۱٫۷۷ مرزی) — اول ایمیل'),
 ('THI ×۴، Aalen، THWS، OTH-AW، HSBI، Heilbronn','VPD لازم (۴–۸ هفته) → تا مهلت عملاً نمی‌رسد'),
]
DIR_PICK = [
 ('1','Augsburg — Data Science','۱ مارس (هرچه زودتر)','ندارد','ندارد','بدون VPD، آزمون و هزینه؛ ≤۲٫۷ ✔. ⚠ ۴ ECTS DS/ML. تاریخ توصیه‌شده‌ی ویزا گذشته → همین هفته.'),
 ('2','Hildesheim — Future Analytics: AI & Audio','<span class="red">۱۵ دسامبر</span>','ذکر نشده','ندارد','همان پورتال ismll درخواست‌های قبلی‌ات؛ ۳۰ ظرفیت؛ B2.'),
 ('3','TUHH — Computer Science','۱ دسامبر → ۱۵ ژانویه','ندارد ✔','ندارد','۱ دسامبر precheck معدل را بزن، بعد درخواست.'),
 ('4','Saarland — Media Informatics','اوایل دسامبر → ۱۵ ژانویه','ذکر نشده','ندارد','پورتال SIM (جدا از CS)؛ ≤۲٫۳ ✔؛ C1 ✔؛ GRE در صفحه نیست ⚠ VPD را تأیید کن.'),
 ('5','Augsburg — Math & CS','۱ مارس','ندارد','ندارد','⚠ ۳۰ ریاضی اثبات‌محور + ۶۰ CS؛ پس از تاریخ توصیه‌شده پذیرش فقط برای یک ترم.'),
 ('با هزینه','Trier — Data Science','۱۵ دسامبر → ۱۵ ژانویه','€70','ندارد','⚠ معدل ≤۱٫۷ (۱٫۷۷→۱٫۷ مرزی).'),
 ('با هزینه','Chemnitz — Web Engineering','۱۵ ژانویه','≈ €49.95 ⚠','ندارد','EduApplication؛ بدون گزینش؛ B2؛ مدارک باید تا مهلت برسد.'),
 ('با هزینه','Deggendorf — HPC / Quantum Computing','<span class="red">۱ دسامبر</span>','€60 (یک‌بار)','€500 سرویس','اگر €60 را قبلاً پرداخت کرده‌ای، رایگان اضافه می‌شود؛ آزمون ارزیابی.'),
]
DIR_NO = [
 ('TU Darmstadt CS','کپی کاغذی باید تا ۱۵ ژانویه <b>برسد</b> + احتمال آزمون حضوری در دارمشتات (مارس)'),
 ('Hof SEIA','€3,300 شهریه/ترم + ۱ سال کار تمام‌وقت استخدامی بعد از لیسانس'),
 ('Albstadt Industrial AI · Konstanz COSIB','شهریه €1,500 / €2,650 (+ COSIB ۱ سال کار)'),
 ('Coburg Autonomous Driving','VPD/ZAB تا ۲ دسامبر نمی‌رسد'),
 ('Saarland Cybersecurity / DS&AI / CS','GRE (راهنمای رسمی)؛ مهلت هم گذشت'),
]
def tr(cells, cls=''):
    return '<tr class="%s">' % cls + ''.join('<td>%s</td>' % c for c in cells) + '</tr>'
ua_t = ''.join(tr([a, '<b>%s</b>' % B(p), dl, cost, note], 'opn') for a, p, dl, cost, note in UA_PICK)
ua_no = ''.join(tr(['<b>%s</b>' % B(p), why], 'bad') for p, why in UA_NO)
dir_t = ''.join(tr([a, '<b>%s</b>' % B(p), dl, fee, tu, note], 'opn' if a.isdigit() else 'sn') for a, p, dl, fee, tu, note in DIR_PICK)
dir_no = ''.join(tr(['<b>%s</b>' % B(p), why], 'bad') for p, why in DIR_NO)

# ---------- B. submitted ----------
done = [r for r in ROWS if r['g'] == 'done']
srows = ''.join(tr(['<b>%s</b>' % B(r['p']), r['st'].replace('✔ ', ''), r['r'], r['n']], 'done' if '❌' not in r['st'] else 'bad') for r in done)

# ---------- C. calendar ----------
cal = [r for r in ROWS if r['dl'] and r['g'] in ('open','soon','winter') and d.date.fromisoformat(r['dl']) >= TODAY]
cal.sort(key=lambda r: r['dl'])
crows = ''
for r in cal:
    days = (d.date.fromisoformat(r['dl']) - TODAY).days
    urg = ' style="color:#b00020"' if days <= 31 else ''
    crows += '<tr class="%s"><td class="dt"%s>%s<br><span>%s روز مانده</span></td><td><b>%s</b><br><small>%s %s</small></td><td>%s</td><td>%s</td><td>%s</td></tr>' % (
        CLS[r['g']], urg, fdate(r['dl']), fa(str(days)), B(r['p']), r.get('v', ''), r['st'], r['dlw'], r['r'], re.sub(r'^[✔↻ ]+', '', r['n']))

# ---------- D. comprehensive ----------
brows = ''
for g in ('done','open','soon','winter','passed','excl'):
    rs = [r for r in ROWS if r['g'] == g]
    brows += '<tr class="grp"><td colspan="8">%s — %s برنامه</td></tr>' % (GT[g], fa(str(len(rs))))
    for r in rs:
        brows += tr([r.get('v', '↻') + ' ' + r['st'], '<b>%s</b>' % B(r['p']), r['r'], r['f'], r['t'], r['s'], r['w'], r['n']], CLS[g])

n_done = len(done)
html = '''<!doctype html><html lang="fa" dir="rtl"><head><meta charset="utf-8"><style>%s</style></head><body>
<h1>راهنمای ارشد آلمان — نسخه‌ی ۲۸ (یکپارچه)</h1>
<div class="sub">برای: کسری جامعی · ۲۱ نوامبر ۲۰۲۶ (۳۰ آبان ۱۴۰۵) · این نسخه جای نسخه‌های ۲۵، ۲۶ و ۲۷ را می‌گیرد: یافته‌های بررسی رسمی ۱۴ نوامبر و به‌روزرسانی ۲۰ نوامبر در خود جدول‌ها ادغام شد و تناقض‌ها برداشته شد. ردیف‌های تازه: 🆕۲۸.</div>
<div class="box"><b>علامت‌ها:</b> ✅ = از صفحه‌ی رسمی دانشگاه تأیید شد (۷ تا ۲۰ نوامبر) · ⚠ = منابع متناقض، فقط DAAD/منبع ثانویه، یا نکته‌ای که خودت باید چک کنی · ↻ = این دور دوباره چک نشد. هزینه‌ی uni-assist: €75 برای اولین برنامه در هر ترم و €30 برای هر برنامه‌ی بعدی. هیچ‌چیز تضمین پذیرش نیست.</div>

<h2>الف. الان چه بزنم؟ — uni-assist (به ترتیب اولویت)</h2>
<table><tr><th>#</th><th>برنامه</th><th>مهلت</th><th>هزینه</th><th>چرا / هشدار</th></tr>%s</table>
<div class="box good">جمع چهار برنامه‌ی اول: €75 + ۳×€30 = <b>€165</b>. مهلت یعنی «مدارک کامل + پرداخت» تا آن روز به uni-assist برسد؛ پردازش ۴ تا ۶ هفته طول می‌کشد، روز آخر نزن. هر مدرک را فقط یک بار در «My documents» آپلود کن و سؤال‌های اختصاصی هر دانشگاه را کامل جواب بده.</div>
<h3>uni-assist — فعلاً نزن</h3>
<table><tr><th>برنامه</th><th>دلیل</th></tr>%s</table>

<h2>ب. الان چه بزنم؟ — مستقیم، بدون uni-assist</h2>
<table><tr><th>#</th><th>برنامه</th><th>مهلت</th><th>هزینه‌ی درخواست</th><th>شهریه</th><th>نکته</th></tr>%s</table>
<h3>مستقیم — فعلاً نزن</h3>
<table><tr><th>برنامه</th><th>دلیل</th></tr>%s</table>
<div class="box">ورودی زمستان ۲۰۲۷/۲۸ (مستقیم و بدون هزینه): Siegen CS و HCI (UNISONO، تا ۳۰ آوریل)، TUHH Data Science و ICS (TUNE، ⚠ تاریخ)، Hamburg IAS و DSAI (STiNE، ۱۵ فوریه → ۳۱ مارس)، Stuttgart INFOTECH (C@MPUS تا ۱۵ ژانویه، €1,500 شهریه). بخش ج را ببین.</div>

<h2>۱. ارسال‌شده‌ها (%s برنامه)</h2>
<table><tr><th>برنامه</th><th>تاریخ و شماره</th><th>مسیر</th><th>نکته / قدم بعدی</th></tr>%s</table>

<h2>۲. تقویم مهلت‌های پیش رو (از ۲۱ نوامبر، به ترتیب تاریخ)</h2>
<div class="box">فقط برنامه‌هایی که مانع جدی ندارند. قرمز = کمتر از یک ماه مانده.</div>
<table><tr><th>مهلت</th><th>برنامه</th><th>ترم</th><th>مسیر</th><th>نکته</th></tr>%s</table>

<h2>۳. جدول جامع — همه‌ی برنامه‌ها</h2>
<div class="box">«تابستان» = ورودی آوریل ۲۰۲۷، «زمستان» = ورودی اکتبر ۲۰۲۷؛ «باز → بسته». «ذکر نشده» = هزینه‌ای در صفحه‌ی رسمی پیدا نشد. اطلاعات شهرها (اجاره، هزینه، بازار کار) در بخش ۵ آخر فایل است.</div>
<table class="big"><tr><th>وضعیت</th><th>برنامه</th><th>مسیر</th><th>هزینه‌ی درخواست</th><th>شهریه / ترم</th><th>تابستان ۲۰۲۷</th><th>زمستان ۲۰۲۷/۲۸</th><th>نکته</th></tr>%s</table>

<h2>۴. چک‌لیست باز (به ترتیب فوریت)</h2>
<ul class="chk">
<li>✔ <b>ارسال شد (۱۲):</b> Göttingen ×۲، Bonn ×۲ (❌ Cyber Security رد شد ۸ نوامبر؛ CS هنوز Received)، Hildesheim ×۲، Freiburg ×۲، Duisburg-Essen ×۲، Stuttgart CS (زمستان)، RUB Bochum CS (زمستان، ۲۰ نوامبر)</li>
<li>☐ <b>همین هفته:</b> حساب uni-assist → Rostock CSI (تا ۳۰ نوامبر)؛ Augsburg Data Science (VIBS)</li>
<li>☐ <b>تا ۱ دسامبر:</b> Deggendorf HPC/QC (€60) — اگر می‌خواهی</li>
<li>☐ <b>۱ دسامبر:</b> TUHH CS → precheck معدل؛ پورتال SIM برای Saarland Media Informatics باز می‌شود</li>
<li>☐ <b>تا ۱۵ دسامبر:</b> Hildesheim Future Analytics (مستقیم)؛ Passau CS (uni-assist — اول anabin)</li>
<li>☐ <b>تا ۳۱ دسامبر:</b> Marburg CS یا DS (uni-assist — مهلت را تأیید کن)</li>
<li>☐ <b>تا ۱۵ ژانویه:</b> TU Dortmund DS و TH OWL IT (uni-assist)؛ TUHH CS، Saarland Media Informatics، Trier (€70)، Chemnitz Web Eng. (مستقیم)؛ اختیاری Weimar/BTU</li>
<li>☐ <b>تا ۱ مارس:</b> Augsburg Math &amp; CS (اگر می‌خواهی)</li>
<li>☐ <b>ریزنمرات را چک کن:</b> Augsburg DS (۴ ECTS DS/ML)، TU Dortmund DS (۸ آمار)، Passau (۱۱۰ CS)، Marburg (۹ نظریه)، Trier (معدل مرزی)</li>
<li>☐ <b>anabin:</b> وضعیت Islamic Azad University – Tehran North (برای Passau و Augsburg)</li>
<li>☐ آیلتس فعلی (خرداد ۱۴۰۴) تا حدود ژوئن ۲۰۲۷ برای Rostock معتبر است (حداکثر ۲ سال)</li>
</ul>

<div class="sub" style="margin-top:10px"><b>منابع این نسخه:</b> بررسی رسمی ۱۴ نوامبر: uni-hildesheim.de و ismll.uni-hildesheim.de/apply، tu-chemnitz.de (Web Eng، bew_bamala، mb/am/aprocess)، uni-augsburg.de (DS، Math&amp;CS)، TUHH (Masterstudiengaenge_englisch، How-to-apply 2026)، th-owl.de (IT + international/bewerben)، informatik.tu-darmstadt.de و tu-darmstadt.de، uni-saarland.de (Media Informatics، uni-assist)، uni-trier.de (current application dates، evaluation fee، DS info)، hof-university.com (ARCS، CS، SEIA، Application Guide)، uni-rostock.de، tu-dresden.de (CS، CMS)، uni-hannover.de، hs-coburg.de (AD، VC&amp;AI، international applicants)، th-deg.de/en/apply، hs-emden-leer.de. به‌روزرسانی ۲۰ نوامبر (v26/v27): uni-kassel.de، uni-passau.de، uni-marburg.de، international.tu-dortmund.de، statistik.tu-dortmund.de، etit.tu-dortmund.de، uol.de، uni-rostock.de، informatik.rub.de، uni-paderborn.de، haw-kiel.de، DAAD، uni-assist.de؛ ثانویه: mygermanuniversity.com، collegedunia.com. منابع قبلی: نسخه‌ی ۲۵ (پوشه‌ی research در گیت‌هاب).</div>
</body></html>''' % (CSS, ua_t, ua_no, dir_t, dir_no, fa(str(n_done)), srows, crows, brows)
html=re.sub(r'(<table[^>]*>)(<tr><th>.*?</th></tr>)', r'\1<thead>\2</thead>', html)
html=html.replace('<h2>۲.','<h2 style="page-break-before:always">۲.').replace('<h2>۳.','<h2 style="page-break-before:always">۳.').replace('<h2>۱.','<h2 style="page-break-before:always">۱.')
open('g28.html', 'w').write(html)
print('ok', len(cal), n_done)
