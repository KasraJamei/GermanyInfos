# -*- coding: utf-8 -*-
# v29 (21 Nov 2026): German-language check for uni-assist picks + Computer Engineering / ECE / Embedded sweep (official pages)
from rows28 import ROWS as R28
from rows20 import R
import copy
ROWS = copy.deepcopy(R28)
UA = 'uni-assist €75 (هر برنامه‌ی بعدی €30)'

def U(prefix, **kw):
    hits = [r for r in ROWS if r['p'].startswith(prefix)]
    assert len(hits) == 1, (prefix, len(hits), [h['p'] for h in hits])
    r = hits[0]; r['v'] = kw.pop('v', '✅'); r.update(kw); return r

def N(g, st, p, r, f, t, s, w, n, dl=None, dlw='', v='✅'):
    x = R(g, st, p + ' 🆕۲۹', r, f, t, s, w, n, None, dl, dlw); x['v'] = v; ROWS.append(x)

# ---------- German check (official, 21 Nov) ----------
U('Rostock — Computer Science International', n='✔ uni-assist؛ ۱ اکتبر → ۳۰ نوامبر؛ آیلتس ۷ (TOEFL 94) زیر ۲ سال ✔؛ <b>آلمانی لازم نیست</b> (صفحه‌ی شرایط ورود)؛ معدل ≥۸۵٪ ✔ (~۸۷٪)؛ ≥۱۸ ریاضی، ≥۱۲ نظریه (تا ۹ جبرانی)؛ بدون محدودیت ظرفیت')
U('Passau — Computer Science',
  n='uni-assist (VPD معیار نیست)؛ ۱ نوامبر → ۱۵ دسامبر؛ ≥۱۱۰ ECTS کامپیوتر؛ معدل ≤۲٫۷ یا ۷۰٪ برتر ✔؛ IAU Tehran North در anabin H+ ✔ (به گفته‌ی خودت)؛ خلاصه‌ی پایان‌نامه/پروژه؛ انگلیسی B2؛ <b>آلمانی A1 لازم است ولی اگر نداری تا پایان سال اول</b> با یک دوره‌ی مقدماتی (گواهی دوره‌هایت تا B1 احتمالاً کافی است ⚠)')
U('Marburg — Computer Science',
  n='uni-assist (My assist)؛ ⚠ مهلت ۳۱ دسامبر (یک منبع ثانویه ۲۶ فوریه)؛ Eignungsfeststellung؛ ≥۹۰ CP CS+ریاضی (≥۱۲ ریاضی، ≥۷۲ CS، ≥۹ نظریه)؛ معدل ≤۳٫۲ ✔؛ <b>آلمانی لازم نیست</b> اگر انگلیسی C1 باشی (جدول Marburg: آیلتس ۷٫۰ = C1 ✔)؛ گزینه‌ی دیگر B1 انگلیسی + DSH-2')
U('Marburg — Data Science', n='uni-assist؛ مثل Marburg CS: آیلتس ۷ = C1 ✔ → آلمانی لازم نیست؛ دانش عمیق CS + ریاضی، به‌ویژه ML؛ ≥۱۴۴ ECTS')
U('TU Dortmund — Data Science',
  n='uni-assist از طریق International Office؛ ۱۵ نوامبر → ۱۵ ژانویه؛ GRE و VPD ندارد؛ <b>آلمانی لازم نیست</b>؛ انگلیسی B2 (آیلتس ۷ ✔). ≥۴۴ CP: <b>ریاضی ≥۱۶، CS ≥۸، آمار ≥۸</b> (اصلاح v28) — «بدون استثنا»؛ مدارک: فرم خوداظهاری (دو امضا)، <b>گزارش آماری (Statistical report)</b> طبق فایل تکلیف ترم تابستان ۲۰۲۷ ⚠، آزمون خودسنجی آنلاین (نمره اثری ندارد)، <b>module handbook</b> درس‌های پایه‌ی ریاضی')
U('TH OWL — Information Technology',
  n='uni-assist برای غیراروپایی؛ ۱۷ نوامبر → ۱۵ ژانویه؛ تدریس فقط انگلیسی؛ <b>آلمانی ذکر نشده</b>؛ B2؛ لیسانس برق/IT/CS/مکاترونیک ✔؛ ⚠ ECTS و معدل در صفحه نیامده؛ شهریه ندارد')
U('Weimar — CS for Digital Media',
  n='uni-assist؛ تا ۱۵ ژانویه؛ <b>آلمانی رسمی لازم نیست</b> (فقط توصیه)؛ آیلتس ≥۶٫۵ و هر بخش ≥۶ ✔؛ لیسانس CS/مهندسی کامپیوتر ✔؛ ⚠ <b>آپلود پایان‌نامه‌ی لیسانس</b> لازم است — گزارش پروژه‌ی ML‌ات را به‌جایش بگذار؛ ارزیابی با نمره‌ی دروس هسته‌ی CS + کیفیت پایان‌نامه/گزارش')
U('Weimar — Human-Computer', n='uni-assist؛ تا ۱۵ ژانویه؛ تدریس انگلیسی؛ آلمانی ذکر نشده؛ B2 (آیلتس ۶٫۵، هیچ بخش زیر ۶ ✔)؛ لیسانس CS یا مرتبط با محتوای HCI کافی')
U('BTU Cottbus — Artificial', n='uni-assist؛ تا ۱۵ ژانویه؛ تدریس انگلیسی؛ آلمانی ذکر نشده؛ MOI قبول نیست (آیلتس ✔)؛ CS، ریاضی و «اخلاق» هم‌تراز لیسانس AI خود BTU')

# ---------- Computer Engineering / ECE / Embedded ----------
U('Paderborn — Computer Engineering', st='❌ GRE + تز ۱۲ CP', v='✅',
  n='صفحه‌ی رسمی: لیسانس باید ≥۱۵–۲۰ ریاضی، ۳۰ CS، ۳۰ برق و <b>۱۲ CP پایان‌نامه</b> داشته باشد (تو پایان‌نامه‌ی رسمی نداری)؛ GRE (Q≥۱۵۷، AW≥۳) برای غیر EU، معافیت فقط اگر معدل تبدیلی بهتر از ۱٫۸ (صفحه‌ی دانشکده اصلاً معافیت را ذکر نکرده)؛ uni-assist')
N('open', '🟢 الان باز — تا ۳۰ نوامبر', 'Rostock — Electrical Engineering (IT track)', 'uni-assist (همان دور Rostock CSI)', '+€30', 'ندارد',
  '۱ اکتبر → <b>۳۰ نوامبر ۲۰۲۶</b>', '۱ آوریل → ۳۱ مه',
  'تدریس انگلیسی؛ گرایش Information Technology شامل پردازش سیگنال، طراحی مدار، <b>سیستم‌های embedded و چندپردازنده‌ای</b>، مخابرات بی‌سیم؛ ≥۱۸۰ CP «در electrical engineering» ⚠ (مهندسی کامپیوتر را کمیته بررسی می‌کند)؛ معدل ≥۸۵٪ ✔؛ میدان‌ها و امواج ≥۳، ریاضی ≥۱۸، برنامه‌نویسی ≥۶؛ آیلتس ۷ زیر ۲ سال ✔؛ آلمانی برای ورود لازم نیست ولی کلاس آلمانی در دوره اجباری است',
  dl='2026-11-30', dlw='تابستان')
N('open', '🟢 الان باز — تا ۱۵ ژانویه (متقاضی ویزا)', 'Saarland — Systems Engineering (ICS, English)', 'مستقیم (پورتال SIM)', 'ذکر نشده', 'ندارد',
  'اواسط دسامبر → ۱ مارس؛ <b>با ویزا تا ۱۵ ژانویه</b>', 'تا ۱۵ ژوئیه (با ویزا)',
  'گرایش Information &amp; Communication Systems کاملاً انگلیسی؛ GRE ذکر نشده (دانشکده‌ی مهندسی، جدا از CS)؛ معدل ≤۲٫۵ ✔ یا ارجاع/مصاحبه؛ B2 (PDF قدیمی‌تر: آیلتس ≥۶٫۵، CGPA ≥۷۵٪، ۲ توصیه‌نامه از طریق سامانه ⚠)؛ لیسانس سیستم/برق/الکترونیک/مخابرات — ⚠ مهندسی کامپیوتر را با ics-info@uni-saarland.de چک کن',
  dl='2027-01-15', dlw='تابستان', v='⚠')
N('winter', '⚪ زمستان — الان باز (تا ۳۰ آوریل)', 'RPTU — Embedded Computing Systems (ESY) / Automation & Control', 'مستقیم (applymsc.eit.rptu.de)', 'هزینه‌ی ارزیابی RPTU (⚠ مبلغ؛ CS: €60)', 'ندارد',
  'تابستان: ۱ مه → ۳۱ اکتبر (گذشت)', '<b>۱ نوامبر ۲۰۲۶ → ۳۰ آوریل ۲۰۲۷</b>',
  'تدریس انگلیسی؛ آلمانی لازم نیست؛ GRE ذکر نشده؛ لیسانس برق یا <b>مهندسی کامپیوتر</b> ✔؛ CGPA ≥۳٫۵/۴ ⚠ (۸۷٪ مرزی)؛ آیلتس ۶٫۰ ✔؛ محدودیت ظرفیت ندارد. همان RPTU که پرونده‌ی CS‌ات آنجا نیمه‌کاره است',
  dl='2027-04-30', dlw='زمستان')
N('winter', '⚪ فقط زمستان', 'Kassel — Electrical Communication Engineering', 'uni-assist', UA, 'ندارد (~€392 ترم)', '—', 'تا ۱۵ ژوئیه ⚠',
  'لیسانس برق/مخابرات/مرتبط؛ معدل «خوب»؛ B2؛ GRE در صفحه‌ی ECE ذکر نشده (برخلاف Kassel CS)', v='⚠')
N('winter', '⚪ فقط زمستان', 'FAU — Communications & Multimedia Engineering', 'مستقیم (campo)', '€100 غیراروپایی', '⚠ شهریه‌ی غیراروپایی از تابستان ۲۰۲۷', '—', 'فوریه → ۱۵ ژوئیه (ترجیحاً تا ۱۵ آوریل)',
  'GRE اختیاری؛ آیلتس ۶٫۰؛ لیسانس مهندسی + نمره‌ی «خوب» در ریاضی مهندسی، سیگنال و سیستم، مخابرات دیجیتال، DSP؛ آزمون صلاحیت (QFV)')
N('winter', '⚪ فقط زمستان', 'TU Darmstadt — Information & Communication Engineering (iCE)', 'مستقیم', 'ذکر نشده', 'ندارد', '—', '⚠ تاریخ در صفحه نیست',
  'لیسانس برق/CS/مخابرات؛ آیلتس ۷ ✔؛ آزمون ارزیابی آنلاین', v='⚠')
N('winter', '⚪ فقط زمستان', 'RWU Ravensburg-Weingarten — Electrical Eng. & Embedded Systems', 'پورتال RWU + مدارک پستی', 'ذکر نشده', '⚠ شهریه‌ی غیراروپایی (BW)', '—', 'تا ۱۵ آوریل',
  'تدریس انگلیسی؛ ≤۲٫۵ و ۲۱۰ ECTS (با ۱۸۰ باید ۳۰ ECTS جبران کنی)؛ آیلتس ۶٫۰؛ مدارک کاغذی باید برسد', v='✅')
N('passed', '⏹ تابستان ۲۰۲۷ گذشت (۱۵ اکتبر)', 'Bremen — Communication & IT (CIT) / CMM', 'مستقیم', 'ذکر نشده', 'ندارد', 'فقط آوریل؛ مهلت ۱۵ اکتبر ۲۰۲۶ گذشت', 'ورودی زمستان ندارد',
  'بعدی: آوریل ۲۰۲۸ (پورتال از اوت ۲۰۲۷)؛ GRE و آلمانی لازم نیست؛ آیلتس ۷ ✔؛ معدل/تناسب ≤۲٫۳ + آزمون آنلاین ≥۵۰٪')
for p, why in (('Duisburg-Essen — Computer Engineering (ISE)', '۵۰٪ آلمانی؛ آلمانی B2 لازم (مثل ESE که درخواست دادی)'),
               ('RPTU — Electrical & Computer Engineering', 'زبان دوره آلمانی؛ «Deutsche Sprachkenntnisse sind erforderlich»'),
               ('Ulm — Communications & Computer Engineering', 'تدریس آلمانی؛ آلمانی C1'),
               ('Hannover — Computer Engineering', 'International application: German C1 + VPD'),
               ('Frankfurt UAS — General Computer Science', '۵۰٪ آلمانی؛ «excellent German» اجباری'),
               ('Siegen — Electrical Engineering', 'غیراروپایی فقط زمستان (۱–۳۰ آوریل) و «معمولاً فقط لیسانس برق»')):
    N('excl', '❌ ' + why.split('؛')[0], p, '—', '—', '—', '—', '—', why)
