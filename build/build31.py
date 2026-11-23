# -*- coding: utf-8 -*-
import datetime as d, re
from rows31 import ROWS, COVER
FA = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
def fa(s): return s.translate(FA)
def B(x): return '<bdi>%s</bdi>' % x
MON = ['ژانویه','فوریه','مارس','آوریل','مه','ژوئن','ژوئیه','اوت','سپتامبر','اکتبر','نوامبر','دسامبر']
TODAY = d.date(2026, 11, 23)
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
 ('2','Paderborn — Computer Science ✅ اصلاح v30','<span class="red">۳۰ نوامبر</span>','+€30','GRE لازم نیست اگر معدل تبدیلی (فرمول باواریایی) کمتر از ۱٫۸ باشد → تو <b>۱٫۷۷</b> ⚠. کردیت: SE ≥۲۰، نظریه ≥۲۰، CE ≥۱۵، ریاضی ≥۱۵ (احتمالاً ✔). شرط پایان‌نامه ندارد. <b>از Paderborn CE قوی‌تر است.</b>'),
 ('3','Paderborn — Computer Engineering (در سبدت)','<span class="red">۳۰ نوامبر</span>','+€30','معافیت GRE مثل CS ✔⚠؛ ولی <b>پایان‌نامه‌ی ≥۱۲ CP</b> می‌خواهد (تو Software Project ۳ واحدی) + ≥۳۰ CP برق → ریسک. اگر بودجه فقط برای یکی است، CS را نگه دار.'),
 ('3+','Paderborn — Electrical Systems Engineering 🆕','<span class="red">۳۰ نوامبر</span>','+€30','اختیاری. معدل ≤۲٫۵ ✔ یا GRE؛ ⚠ صفحه‌ی درخواست دانشکده GRE را در فهرست مدارک آورده؛ لیسانس «برق یا مرتبط» ⚠.'),
 ('3+','Rostock — Electrical Engineering (IT track)','<span class="red">۳۰ نوامبر</span>','+€30','اختیاری. ⚠ لیسانس «electrical engineering» — مهندسی کامپیوتر را کمیته بررسی می‌کند.'),
 ('4','TH OWL — Information Technology 🛒','<span class="red">۱ دسامبر</span> (امن)','+€30','✅ v31: مسیر قطعی = <b>uni-assist</b> (صفحه‌ی Master، International Office، FAQ رشته)؛ KIS فقط برای مدرک آلمان/EU. با بقیه‌ی سبد تا ۳۰ نوامبر. در uni-assist: Technische Hochschule Ostwestfalen-Lippe → Master → Information Technology (full-time) → Summer 2027. معدل ≤۲٫۵ ✔؛ انگیزه‌نامه‌ی انگلیسی. FH صنعتی، شانس بالا → گزینه‌ی مطمئن.'),
 ('اختیاری','TH Augsburg — Interactive Media Systems 🆕','<span class="red">۱ دسامبر</span>','+€30','MA؛ Mixed Reality / HCI / Game Dev؛ آزمون صلاحیت؛ بیشتر رسانه/طراحی.'),
 ('5','Passau — Computer Science','۱۵ دسامبر','+€30','≥۱۱۰ ECTS کامپیوتر؛ ≤۲٫۷ ✔؛ anabin H+ ✔؛ آلمانی A1 تا پایان سال اول.'),
 ('6','Marburg — Computer Science (در سبدت)','۳۱ دسامبر ⚠','+€30','فرم Self-Disclosure را پر کردی ✔؛ ⚠ پایان‌نامه ≥۱۰ CP (توضیح در Comment)؛ مهلت را در My assist تأیید کن.'),
 ('💾','TU Dortmund — Data Science — ذخیره برای بعد','۱۵ ژانویه','+€30','<b>تصمیم ۲۳ نوامبر: فعلاً نزن.</b> بعد از جواب Bonn (~۱۵ دسامبر): اگر قبول نشدی اضافه کن. ≥۴۴ CP (ریاضی ≥۱۶، CS ≥۸، آمار ≥۸ ⚠) + گزارش آماری + module handbook.'),
 ('8','Anhalt — Electrical &amp; Computer Eng.','۱۵ ژانویه','+€30','۱ سال کار مرتبط ✔، ≤۲٫۴ ✔.'),
 ('اختیاری','Weimar — CS for Digital Media / HCI · BTU — AI','۱۵ ژانویه','+€30 هرکدام','آلمانی لازم نیست؛ Weimar CS4DM پایان‌نامه/گزارش پروژه می‌خواهد.'),
]
UA_NO = [
 ('TU Dresden CS (در سبدت)','مدرک «computer science» + ۹۰ ECTS حوزه‌ای + GRE «توصیه‌شده» + پورتال آزمون صلاحیت جدا؛ ⚠ شروع تابستان سمستر اول در صفحات CS صریح نیست → پیشنهاد: حذف (−€30)'),
 ('Kiel CAU — EIE 🆕 · Regensburg HCAI 🆕 · Potsdam CS 🆕','GRE'),
 ('Hannover — EEIT Microelectronics / AI-Driven Mechatronics 🆕','کنترل ≥۱۰ ECTS / مکانیک ≥۱۵ ECTS لازم'),
 ('Emden/Leer Industrial Informatics · Business Informatics 🆕','۲۱۰ ECTS / €5,980'),
 ('Kiel CAU CS · Osnabrück Cognitive Science','فقط لیسانس CS مشابه / Cognitive Science — نامطمئن'),
 ('THI ×۴، Aalen، THWS، OTH-AW، HSBI، Heilbronn، THA EE 🆕','VPD لازم (۴–۸ هفته) → برای تابستان دیر؛ <b>برای زمستان VPD را از الان بگیر</b>'),
]
DIR_PICK = [
 ('1','RUB Bochum — EEIT: Communication Systems 🆕','۱۵ ژانویه','ندارد','ندارد','<b>همان پورتال hio که CS را زدی.</b> کاملاً انگلیسی؛ ≥۲۵ CP ریاضی + ≥۵۰ CP IT/برق (کمبود تا ۲۵ CP جبرانی)؛ B2 ✔؛ DSP، مخابرات، ML.'),
 ('2','TU Darmstadt — Computer Science ✅ تصمیم ۲۳ نوامبر','۱ دسامبر → <span class="red">۱۵ ژانویه (رسیدن پاکت)</span>','ذکر نشده','ندارد','فرم آنلاین + پاکت کاغذی (فرم امضاشده + کپی مدارک + ترجمه) به Karolinenplatz 5 — آشنایت تحویل بدهد. ≥۶۰ ECTS هم‌تراز هسته‌ی Informatik؛ ⚠ احتمال آزمون حضوری اوایل مارس؛ ⚠ نوع ترجمه را با دانشگاه چک کن.'),
 ('2+','HS Bremen — Electronics Engineering 🆕','۱۵ دسامبر → ۱۵ ژانویه','ذکر نشده','ندارد','FPGA، طراحی IC، ML سخت‌افزاری؛ C1 ✔؛ ≤۲٫۵ ✔؛ ⚠ ۲۱۰ ECTS برای نسخه‌ی ۳ترمه + VPD برای تبدیل معدل + ۲ توصیه‌نامه.'),
 ('3','Augsburg — Data Science','۱ مارس (هرچه زودتر)','ندارد','ندارد','بدون VPD، آزمون و هزینه؛ ≤۲٫۷ ✔. ⚠ ۴ ECTS DS/ML.'),
 ('4','Hildesheim — Future Analytics: AI &amp; Audio','<span class="red">۱۵ دسامبر</span>','ذکر نشده','ندارد','همان پورتال ismll؛ ۳۰ ظرفیت؛ B2.'),
 ('5','TUHH — Computer Science','۱ دسامبر → ۱۵ ژانویه','ندارد ✔','ندارد','۱ دسامبر precheck معدل، بعد درخواست.'),
 ('6','Saarland — Media Informatics · Systems Eng. (ICS)','تا ۱۵ ژانویه','ذکر نشده','ندارد','پورتال SIM؛ C1 ✔؛ GRE ذکر نشده ⚠.'),
 ('اختیاری','Kempten — Electrical Engineering 🆕','۱۵ نوامبر → ۱۵ ژانویه','ذکر نشده','€500','لیسانس برق/مخابرات/الکترونیک ⚠؛ B2؛ A1 در دوره.'),
 ('اختیاری','OTH Regensburg — Electrical &amp; Microsystems 🆕','۱۵ دسامبر','ذکر نشده','⚠ متغیر','نیمه‌هادی/میکروالکترونیک → تناسب ضعیف.'),
 ('اختیاری','Aalen — Advanced Systems Design 🆕','۱۵ دسامبر','ذکر نشده','€1,500','CS پذیرفته؛ ⚠ VPD Aalen.'),
 ('با هزینه','Trier — Data Science','۱۵ دسامبر → ۱۵ ژانویه','€70','ندارد','⚠ معدل ≤۱٫۷ (۱٫۷۷ مرزی).'),
 ('با هزینه','Chemnitz — Web Engineering','۱۵ ژانویه','≈ €49.95 ⚠','ندارد','EduApplication؛ بدون گزینش؛ B2؛ مدارک باید تا مهلت برسد.'),
]
DIR_NO = [
 ('HAW Hamburg — ICE 🆕 (تابستان)','VPD «۸ هفته قبل از پنجره» → برای تابستان دیر؛ زمستان (۱ ژوئن → ۱۵ ژوئیه) عالی'),
 ('Hof SEIA · Albstadt · Konstanz COSIB','شهریه/سابقه‌ی کار'),
 ('Coburg Autonomous Driving','VPD/ZAB تا ۲ دسامبر نمی‌رسد'),
 ('Saarland Cybersecurity / DS&amp;AI / CS','GRE / مهلت گذشت'),
 ('TH Rosenheim 🆕 · FU Berlin CS 🆕 · Goethe CS 🆕 · Uni Bremen CS/EEIT 🆕 · HAW Hamburg CS 🆕','آلمانی لازم'),
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

KL = {'in':('✅ در راهنما','done'),'new':('🆕 تازه/اصلاح','opn'),'none':('— ارشد انگلیسی مرتبط ندارد','lt'),'na':('⚪ مرتبط نیست','lt')}
cov_rows = ''.join(tr(['<b>%s</b>' % B(u), KL[k][0], c], KL[k][1]) for u, k, c in COVER)
COV_HTML = """
<h2 style="page-break-before:always">ت. تطبیق با فهرست اعضای uni-assist (فهرستی که ۲۳ نوامبر فرستادی)</h2>
<div class="box">عضو uni-assist بودن یعنی دانشگاه <b>برای بعضی</b> برنامه‌ها از uni-assist (درخواست یا VPD) استفاده می‌کند، نه همه. «ارشد انگلیسی مرتبط ندارد» = در پایگاه برنامه‌های بین‌المللی DAAD (۱۶۰۴ ارشد انگلیسی‌زبان، ۲۳ نوامبر) برنامه‌ی CS/IT/برق-کامپیوتر/داده/AI/Embedded برایش پیدا نشد؛ ممکن است برنامه‌ای باشد که در DAAD ثبت نشده. ✅ = در راهنما بود · 🆕 = این نسخه اضافه شد · ⚪ = مرتبط نیست (پزشکی، هنر، الهیات، خصوصی).</div>
<table><thead><tr><th>دانشگاه</th><th>وضعیت</th><th>برنامه‌های مرتبط (جزئیات در جدول جامع)</th></tr></thead>"""+cov_rows+"""</table>
<h2 style="page-break-before:always">۱."""
n_done = len(done)
html = '''<!doctype html><html lang="fa" dir="rtl"><head><meta charset="utf-8"><style>%s</style></head><body>
<h1>راهنمای ارشد آلمان — نسخه‌ی ۳۱</h1>
<div class="sub">برای: کسری جامعی · ۲۳ نوامبر ۲۰۲۶ (۲ آذر ۱۴۰۵) · جای همه‌ی نسخه‌های قبلی را می‌گیرد. <b>نسخه‌ی ۳۱ (۲۳ نوامبر):</b> سبد نهایی uni-assist (€255)؛ مسیر TH OWL قطعی شد (uni-assist)؛ TU Dortmund DS «ذخیره برای بعد»؛ Dresden حذف. <b>نسخه‌ی ۳۰:</b> تطبیق کامل با فهرست اعضای uni-assist که فرستادی (بخش «ت»)، مرور کل پایگاه برنامه‌های بین‌المللی DAAD (۱۶۰۴ ارشد انگلیسی، ۲۳ نوامبر) و چک صفحه‌های رسمی. ۲۲ ردیف تازه (🆕۳۰)، TU Darmstadt CS به «می‌زنم» منتقل شد، و ۵ اصلاح مهم: <b>Paderborn CS قابل‌درخواست شد</b> (معافیت GRE با معدل ۱٫۷۷)، Paderborn CE (معافیت GRE ✔ ولی شرط تز)، تناقض مهلت TH OWL، ابهام شروع تابستان Dresden، FH Südwestfalen.</div>
<div class="box"><b>علامت‌ها:</b> ✅ = از صفحه‌ی رسمی دانشگاه تأیید شد (۷ تا ۲۰ نوامبر) · ⚠ = منابع متناقض، فقط DAAD/منبع ثانویه، یا نکته‌ای که خودت باید چک کنی · ↻ = این دور دوباره چک نشد. هزینه‌ی uni-assist: €75 برای اولین برنامه در هر ترم و €30 برای هر برنامه‌ی بعدی. هیچ‌چیز تضمین پذیرش نیست.</div>

<h2>الف. الان چه بزنم؟ — uni-assist (به ترتیب اولویت)</h2>
<table><tr><th>#</th><th>برنامه</th><th>مهلت</th><th>هزینه</th><th>چرا / هشدار</th></tr>%s</table>
<div class="box good"><b>سبد نهایی (۲۳ نوامبر) — پرداخت و ارسال تا ۳۰ نوامبر:</b> Rostock CSI + Paderborn CS + Paderborn CE + Marburg CS + Passau CS + Kiel CS + TH OWL IT = €75 + ۶×€30 = <b>€255</b>؛ Dresden حذف. <b>💾 ذخیره:</b> TU Dortmund DS (+€30، تا ۱۵ ژانویه) — بعد از جواب Bonn تصمیم بگیر. بقیه‌ی uni-assistی‌ها (Paderborn ESE، Rostock EE، TH Augsburg IMS، BTU) نزن؛ Anhalt و Weimar فقط پشتیبان اختیاری. ⚠ اینکه برنامه‌ای که بعد از پرداخت اضافه می‌کنی هم €30 حساب شود را در My assist ببین. <b>آلمانی:</b> هیچ‌کدام از این‌ها برای ورود آلمانی نمی‌خواهند؛ فقط Passau آلمانی A1 را تا پایان سال اول می‌خواهد. مهلت یعنی «مدارک کامل + پرداخت» تا آن روز به uni-assist برسد؛ پردازش ۴ تا ۶ هفته طول می‌کشد، روز آخر نزن. هر مدرک را فقط یک بار در «My documents» آپلود کن و سؤال‌های اختصاصی هر دانشگاه را کامل جواب بده.</div>
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

<h2>۴. چک‌لیست باز (به ترتیب فوریت، ۲۳ نوامبر)</h2>
<ul class="chk">
<li>✔ <b>ارسال شد (۱۲):</b> Göttingen ×۲، Bonn ×۲ (❌ Cyber Security رد شد؛ CS هنوز Received)، Hildesheim ×۲، Freiburg ×۲، Duisburg-Essen ×۲، Stuttgart CS (زمستان)، RUB Bochum CS (زمستان)</li>
<li>✔ <b>uni-assist:</b> حساب ساخته شد، ۱۴ مدرک در My documents آپلود شد (۲۲ نوامبر)؛ سبد نهایی: Rostock CSI، Paderborn CS، Paderborn CE، Marburg CS، Passau CS، Kiel CS، TH OWL IT (€255)؛ Dresden حذف؛ فرم Self-Disclosure Marburg و فرم Self-indication Passau پر شد</li>
<li>☐ <b>تا ۳۰ نوامبر (uni-assist):</b> Dresden را حذف و TH OWL IT را اضافه کن؛ سؤال‌های Passau (لینک Drive پروژه + PDF Self-indication)؛ <b>پرداخت €255 و ارسال</b> (ترجیحاً ۲۸–۲۹ نوامبر)</li>
<li>☐ <b>تا ۱ دسامبر:</b> TUHH CS → precheck معدل (TH OWL با سبد ۳۰ نوامبر رفته)</li>
<li>☐ <b>~۱۵ دسامبر:</b> جواب Bonn CS → تصمیم درباره‌ی 💾 TU Dortmund DS</li>
<li>☐ <b>تا ۱۵ دسامبر:</b> Hildesheim Future Analytics (مستقیم)؛ اختیاری OTH Regensburg EMSE، Aalen ASD</li>
<li>☐ <b>TU Darmstadt CS:</b> از ۱ دسامبر فرم آنلاین → چاپ و امضای Antrag → ایمیل به international.admission@zv.tu-darmstadt.de درباره‌ی ترجمه‌ها → فرستادن مدارک برای آشنایت در آلمان تا اوایل ژانویه → تحویل پاکت به Karolinenplatz 5 <b>قبل از ۱۵ ژانویه</b></li>
<li>☐ <b>تا ۱۵ ژانویه:</b> <b>RUB EEIT Communication Systems</b> (مستقیم، همان حساب hio)؛ HS Bremen Electronics Eng.؛ 💾 TU Dortmund DS (فقط اگر Bonn نشد)، اختیاری Anhalt ECE (uni-assist)؛ TUHH CS، Saarland، Chemnitz Web Eng.، Kempten EE (مستقیم)؛ اختیاری Weimar/BTU؛ Stuttgart EE برای زمستان (C@MPUS)</li>
<li>☐ <b>تا ۱ مارس:</b> Augsburg DS و Math &amp; CS</li>
<li>☐ <b>برای زمستان ۲۰۲۷/۲۸ — VPD را از ژانویه تا آوریل بگیر:</b> HAW Hamburg ICE، TH Augsburg EE، THI، Aalen، Heilbronn (هر VPD برای همان دانشگاه/برنامه صادر می‌شود)</li>
<li>☐ <b>ریزنمرات را چک کن:</b> Paderborn CS (۲۰/۲۰/۱۵/۱۵)، RUB EEIT (۲۵ ریاضی، ۵۰ IT/برق)، Augsburg DS (۴ ECTS DS/ML)، TU Dortmund DS (۸ آمار)، Passau (۱۱۰ CS)</li>
<li>☐ آیلتس فعلی (خرداد ۱۴۰۴) تا حدود ژوئن ۲۰۲۷ برای Rostock معتبر است (حداکثر ۲ سال)</li>
</ul>

<div class="sub" style="margin-top:10px"><b>منابع این نسخه:</b> <b>v30 (۲۳ نوامبر):</b> فهرست اعضای uni-assist (از خودت)؛ پایگاه DAAD International Programmes (API، ۱۶۰۴ ارشد انگلیسی) و صفحات DAAD ۳۹۰۴، ۴۵۸۷، ۴۱۴۰، ۱۰۳۴۵، ۶۹۶۸، ۶۰۹۱، ۱۰۵۴۸، ۴۴۹۳، ۴۲۶۹، ۶۱۵۹، ۱۱۱۶۹، ۷۶۰۷، ۳۷۹۳، ۹۷۳۸، ۳۷۵۲، ۴۶۳۶، ۱۰۷۱۲، ۹۸۶۳، ۱۱۲۸۳، ۳۹۸۰، ۱۱۲۹۰، ۶۹۲۶، ۱۱۱۷۰؛ رسمی: cs.uni-paderborn.de (information for international students)، uni-paderborn.de (CE، deadlines)، ei.uni-paderborn.de (ESE application)، informatik.tu-darmstadt.de (Admissions &amp; Application Guide)، tu-darmstadt.de (CS، bewerbungsfristen، international application)، th-owl.de (IT + Hinweise Master IT PDF)، tu-dresden.de (admission، SINS، Zusatzinformationen)، uni-rostock.de/ief، fh-swf.de، fh-erfurt.de، ai.fh-erfurt.de، haw-hamburg.de (ICE، CS، Bewerbungsleitfaden Master)، h-da.de، etit.ruhr-uni-bochum.de، tha.de (FAQ Master EE)، msc-ee.hs-bremen.de، uni-bremen.de، uni-frankfurt.de، mi.fu-berlin.de، uni-potsdam.de و ZulO MSc CS (hpi.de)، uni-wuppertal.de؛ ثانویه: mygermanuniversity.com (Kiel EIE، Hamm-Lippstadt، FH SWF). بررسی رسمی ۱۴ نوامبر: uni-hildesheim.de و ismll.uni-hildesheim.de/apply، tu-chemnitz.de (Web Eng، bew_bamala، mb/am/aprocess)، uni-augsburg.de (DS، Math&amp;CS)، TUHH (Masterstudiengaenge_englisch، How-to-apply 2026)، th-owl.de (IT + international/bewerben)، informatik.tu-darmstadt.de و tu-darmstadt.de، uni-saarland.de (Media Informatics، uni-assist)، uni-trier.de (current application dates، evaluation fee، DS info)، hof-university.com (ARCS، CS، SEIA، Application Guide)، uni-rostock.de، tu-dresden.de (CS، CMS)، uni-hannover.de، hs-coburg.de (AD، VC&amp;AI، international applicants)، th-deg.de/en/apply، hs-emden-leer.de. به‌روزرسانی ۲۰ نوامبر (v26/v27): uni-kassel.de، uni-passau.de، uni-marburg.de، international.tu-dortmund.de، statistik.tu-dortmund.de، etit.tu-dortmund.de، uol.de، uni-rostock.de، informatik.rub.de، uni-paderborn.de، haw-kiel.de، DAAD، uni-assist.de؛ ثانویه: mygermanuniversity.com، collegedunia.com. منابع قبلی: نسخه‌ی ۲۵ (پوشه‌ی research در گیت‌هاب).</div>
</body></html>''' % (CSS, ua_t, ua_no, dir_t, dir_no, fa(str(n_done)), srows, crows, brows)
html=re.sub(r'(<table[^>]*>)(<tr><th>.*?</th></tr>)', r'\1<thead>\2</thead>', html)
html=html.replace('<h2>۲.','<h2 style="page-break-before:always">۲.').replace('<h2>۳.','<h2 style="page-break-before:always">۳.').replace('<h2>۱.','''<h2>پ. Computer Engineering / برق-کامپیوتر / Embedded (بررسی رسمی ۲۱ نوامبر)</h2>
<table><thead><tr><th>برنامه</th><th>ورودی / مهلت</th><th>مسیر</th><th>حکم</th></tr></thead>
<tr class="opn"><td><b><bdi>Rostock — Electrical Engineering (IT track)</bdi></b></td><td>تابستان ۲۰۲۷ · <span class="red">۳۰ نوامبر</span></td><td>uni-assist</td><td>✅ بزن (کنار Rostock CSI) — ⚠ لیسانس برق</td></tr>
<tr class="opn"><td><b><bdi>Saarland — Systems Engineering (ICS)</bdi></b></td><td>تابستان ۲۰۲۷ · ۱۵ ژانویه</td><td>مستقیم (SIM)</td><td>✅ بزن — ⚠ تطابق مهندسی کامپیوتر</td></tr>
<tr class="opn"><td><b><bdi>Anhalt — Electrical &amp; Computer Eng.</bdi></b></td><td>تابستان ۲۰۲۷ · ۱۵ ژانویه</td><td>uni-assist</td><td>✅ ممکن (۱ سال کار مرتبط ✔، ≤۲٫۴ ✔)</td></tr>
<tr class="opn"><td><b><bdi>Deggendorf — Electrical Eng. &amp; IT (EN)</bdi></b></td><td>تابستان ۲۰۲۷ · ۱ دسامبر</td><td>Primuss (€60)</td><td>⚠ شرایط را چک کن</td></tr>
<tr class="lt"><td><b><bdi>RPTU — Embedded Computing Systems / Automation &amp; Control</bdi></b></td><td>زمستان · <b>الان باز تا ۳۰ آوریل</b></td><td>مستقیم</td><td>✅ بزن (CGPA ≥۳٫۵/۴ ⚠)</td></tr>
<tr class="lt"><td><b><bdi>Stuttgart INFOTECH · TU Ilmenau RCSE · Nordhausen CE for IoT</bdi></b></td><td>زمستان</td><td>C@MPUS · uni-assist</td><td>در جدول جامع</td></tr>
<tr class="lt"><td><b><bdi>Kassel ECE · FAU CME · TU Darmstadt iCE · RWU EEES</bdi></b></td><td>زمستان (آوریل–ژوئیه)</td><td>مختلف</td><td>بعداً</td></tr>
<tr class="lt"><td><b><bdi>Bremen CIT / CMM</bdi></b></td><td>فقط آوریل؛ ۲۰۲۷ گذشت</td><td>مستقیم</td><td>آوریل ۲۰۲۸</td></tr>
<tr class="opn"><td><b><bdi>Paderborn — Computer Engineering</bdi></b></td><td>تابستان ۲۰۲۷ · <span class="red">۳۰ نوامبر</span></td><td>uni-assist</td><td>⚠ اصلاح v30: معافیت GRE با معدل ۱٫۷۷ ✔؛ ریسک: تز ۱۲ CP</td></tr>
<tr class="opn"><td><b><bdi>Paderborn — Electrical Systems Engineering 🆕</bdi></b></td><td>تابستان ۲۰۲۷ · <span class="red">۳۰ نوامبر</span></td><td>uni-assist / PAUL</td><td>⚠ ≤۲٫۵ ✔ یا GRE؛ لیسانس برق یا مرتبط</td></tr>
<tr class="opn"><td><b><bdi>RUB Bochum — EEIT: Communication Systems 🆕</bdi></b></td><td>تابستان ۲۰۲۷ · ۱۵ ژانویه</td><td>مستقیم (hio)</td><td>✅ بزن — ۲۵ CP ریاضی + ۵۰ CP IT/برق</td></tr>
<tr class="opn"><td><b><bdi>HS Bremen — Electronics Engineering 🆕</bdi></b></td><td>تابستان ۲۰۲۷ · ۱۵ ژانویه</td><td>مستقیم + VPD</td><td>⚠ ۲۱۰ ECTS + ۲ توصیه‌نامه؛ تناسب خوب</td></tr>
<tr class="opn"><td><b><bdi>Kempten EE · OTH Regensburg EMSE 🆕</bdi></b></td><td>تابستان · ۱۵ ژانویه / ۱۵ دسامبر</td><td>مستقیم</td><td>⚠ لیسانس برق/الکترونیک</td></tr>
<tr class="lt"><td><b><bdi>TH Augsburg EE · HAW Hamburg ICE · h_da EEIT · Frankfurt UAS IT · Magdeburg EEIT · Chemnitz ES/ICS/ARC · Stuttgart EE · BHT ICE 🆕</bdi></b></td><td>زمستان ۲۰۲۷/۲۸</td><td>مختلف (چند تا VPD)</td><td>در جدول جامع</td></tr>
<tr class="bad"><td><b><bdi>UDE Computer Engineering · RPTU ECE · Ulm CCE · Hannover CE · Frankfurt UAS GCS</bdi></b></td><td>—</td><td>—</td><td>❌ آلمانی لازم</td></tr>
<tr class="bad"><td><b><bdi>RWTH CE · Saarland Embedded Systems</bdi></b></td><td>—</td><td>—</td><td>❌ GRE</td></tr>
<tr class="bad"><td><b><bdi>Siegen Electrical Engineering</bdi></b></td><td>—</td><td>—</td><td>❌ غیراروپایی فقط زمستان + لیسانس برق</td></tr>
</table>

''' + COV_HTML)
open('g31.html', 'w').write(html)
print('ok', len(cal), n_done)
