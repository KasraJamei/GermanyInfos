# -*- coding: utf-8 -*-
# v25: + 15 named universities (official, 8 Nov) + DAAD Study Guide list (287 programmes, English, fos 1-226) triaged; new candidates checked on DAAD + official sites 9 Nov 2026
from rows24 import ROWS as R24
from rows20 import R
import copy
ROWS = copy.deepcopy(R24)
UA = 'uni-assist €75 (هر برنامه‌ی بعدی €30)'
VPD = 'VPD از uni-assist (€75، تا ۸ هفته)'

def U(prefix, **kw):
    hits = [r for r in ROWS if r['p'].startswith(prefix)]
    assert len(hits) == 1, (prefix, len(hits))
    r = hits[0]
    r['v'] = kw.pop('v', '✅')
    r.update(kw)
    return r

def N(g, st, p, r, f, t, s, w, n, c=None, dl=None, dlw='', v='✅'):
    x = R(g, st, p + ' 🆕۲۵', r, f, t, s, w, n, c, dl, dlw)
    x['v'] = v
    ROWS.append(x)

# ---------- corrections to existing rows ----------
U('Trier', g='soon', st='🔵 از ۱۵ دسامبر', r='مستقیم (PORTA) — بدون uni-assist', f='€70 (از ۱۰ اکتبر ۲۰۲۶)', t='ندارد',
  s='۱۵ دسامبر ۲۰۲۶ → <b>۱۵ ژانویه ۲۰۲۷</b>', w='۴ → ۳۱ مه ۲۰۲۷',
  n='اصلاح v24: غیراروپایی تابستان هم دارد. معدل ≤۱٫۷ (رقم دوم حذف می‌شود → ۱٫۷۷ = ۱٫۷ ✔ مرزی ⚠)؛ مهندسی کامپیوتر موردی (~۹۰٪ قبول)؛ آیلتس ۶٫۵؛ انگیزه‌نامه یک صفحه',
  dl='2027-01-15', dlw='تابستان')
U('TU Darmstadt', g='soon', v='⚠', st='🔵 از ۱ دسامبر', r='مستقیم + کپی برابر اصل پستی (باید تا مهلت برسد)', f='ذکر نشده', t='ندارد',
  s='۱ دسامبر → <b>۱۵ ژانویه ۲۰۲۷</b>', w='۱ ژوئن → ۱۵ ژوئیه',
  n='اصلاح v24: آزمون حضوری فقط اگر مدارک ۶۰ ECTS هم‌تراز را نشان ندهد؛ وگرنه بدون آزمون. GRE (V155/Q165) جایگزین آزمون. آیلتس ۷ ✔. همین روال برای AI &amp; Machine Learning',
  dl='2027-01-15', dlw='تابستان')
U('HPI Potsdam', st='❌ GRE + VPD', n='صفحه‌ی درخواست رسمی (۹ نوامبر): GRE General و VPD برای مدرک خارج از EU لازم است؛ GRE-Q = ۱۵٪ امتیاز')
U('Würzburg', g='excl', st='❌ پایان‌نامه‌ی ۱۰ ECTS', r='WueStudy + VPD', s='۳۱ اکتبر گذشت', w='اواخر ژانویه → ۱۵ مارس ۲۰۲۷',
  n='پایان‌نامه‌ی ۱۰ ECTS کامپیوتر لازم است؛ ≥۱۰۰ ECTS CS+ریاضی')
U('TH Köln', w='اوایل مارس → <b>۳۰ آوریل ۲۰۲۷</b> (uni-assist)',
  n='مهلت تابستان ۳۱ اکتبر گذشت. رتبه‌بندی: ۵۰٪ معدل، ۲۵٪ تناسب، ۲۵٪ مصاحبه؛ ≥۸۰ ECTS کامپیوتر؛ ویدیو؛ B2')
U('Regensburg', n='هر سه برنامه‌ی انگلیسی (CS، Data Science، Human-Centred AI، و Media Informatics) GRE Q≥۱۶۴ برای ایران + VPD')
U('Saarland — CS', n='GRE/GATE لازم (DAAD + سایت). ⚠ Cybersecurity، Data Science &amp; AI و Media Informatics در همین دانشگاه GRE نمی‌خواهند — پایین را ببین')
U('Lübeck', n='پاره‌وقت/آنلاین. برنامه‌ی دیگر Lübeck: Robotics &amp; Autonomous Systems (پایین)')

# ---------- new: SUMMER 2027 ----------
N('open', '🟢 باز — فوری', 'Saarland — Cybersecurity', 'مستقیم (apply.cs.uni-saarland.de)', 'ذکر نشده', 'ندارد (~€300)',
  'تا <b>۱۵ نوامبر ۲۰۲۶</b>', 'زودهنگام ۱۵ نوامبر / عادی ۱۵ مه',
  'آیین‌نامه §۳۲ و صفحه‌ی رسمی: GRE ذکر نشده ✔ (برخلاف Saarland CS)؛ C1 (آیلتس ۷ ✔، MOI قبول نیست)؛ ۲ توصیه‌نامه‌ی استاد + بیانیه؛ شایستگی ریاضی/نظری/عملی؛ ⚠ FAQ پورتال قابل‌خواندن نبود', 59, '2026-11-15', 'تابستان')
N('open', '🟢 باز — فوری', 'Saarland — Data Science &amp; AI', 'مستقیم (apply.cs.uni-saarland.de)', 'ذکر نشده', 'ندارد (~€394)',
  'تا <b>۱۵ نوامبر ۲۰۲۶</b>', 'زودهنگام ۱۵ نوامبر / عادی ۱۵ مه',
  'صفحه‌ی رسمی: GRE ذکر نشده؛ C1؛ دوسیه + ۲ «expert opinion» (توصیه‌نامه)؛ شایستگی ریاضی، نظری، عملی + ML/AI/داده‌کاوی ⚠', 59, '2026-11-15', 'تابستان')
N('open', '🟢 باز — فوری (uni-assist)', 'TU Ilmenau — Data Science', 'uni-assist + پورتال Ilmenau', UA, 'ندارد (~€320)',
  '۱ اوت → <b>۱۵ نوامبر ۲۰۲۶</b>', 'باز ⚠',
  'NC-free؛ امتیازی (لیسانس CS = ۲۰ امتیاز، معدل ≤۲٫۰ = ۵)؛ C1 آیلتس ۷ ✔؛ مهلت از صفحه‌ی رسمی مهلت‌های Ilmenau', 15, '2026-11-15', 'تابستان')
N('open', '🟢 باز — فوری (uni-assist)', 'TU Ilmenau — Research in Media Engineering', 'uni-assist + پورتال Ilmenau', UA, 'ندارد',
  '۱ اوت → <b>۱۵ نوامبر ۲۰۲۶</b>', 'باز ⚠',
  'لیسانس مهندسی/علوم کامپیوتر ۱۸۰ ✔؛ C1 ✔؛ ریاضی/برق/DSP توصیه‌شده ⚠؛ نیمی آلمانی ولی کامل با انگلیسی ممکن', 15, '2026-11-15', 'تابستان')
N('open', '🟢 باز — فوری (uni-assist)', 'Magdeburg — Digital Engineering', 'uni-assist', UA, 'ندارد (~€311)',
  '۱۵ اکتبر → <b>۱۵ نوامبر ۲۰۲۶</b>', '۱۵ آوریل → ۱۵ مه ۲۰۲۷',
  'لیسانس مهندسی یا کامپیوتر ✔؛ C1 (آیلتس ۷ ✔)', 14, '2026-11-15', 'تابستان', v='⚠')
N('open', '🟢 باز (VPD)', 'Coburg — Autonomous Driving (کاربردی)', 'Primuss + VPD برای Coburg', VPD, '€1,500 + €109',
  '۱۶ مه → <b>۲ دسامبر ۲۰۲۶</b>', '۳ دسامبر → ۱۵ مه ۲۰۲۷',
  'کامپیوتر/IT پذیرفته؛ ۱۸۰ ECTS بدون ترم عملی ✔ (کمبود تا یک سال)؛ B2؛ ⚠ VPD تا ۲ دسامبر به‌سختی می‌رسد', None, '2026-12-02', 'تابستان', v='⚠')
N('open', '🟢 باز (uni-assist)', 'Passau — AI Engineering', 'uni-assist', UA, 'ندارد (~€130)',
  '۱ نوامبر → <b>۱۵ دسامبر ۲۰۲۶</b>', '۱ آوریل → ۳۱ مه',
  '≥۳۵ ECTS ریاضی (با نظری) + ≥۴۰ CS؛ معدل ≤۲٫۷ ✔؛ دانشگاه H+ در anabin؛ خلاصه‌ی پایان‌نامه یا پروژه‌ی کارشناسی ✔؛ B2', 42, '2026-12-15', 'تابستان')
N('open', '🟢 باز (uni-assist)', 'Osnabrück — Cognitive Science', 'uni-assist', UA, 'ندارد (~€350)',
  'تا <b>۱۵ دسامبر ۲۰۲۶</b>', 'تا ۱۵ ژوئن ۲۰۲۷',
  'لیسانس کامپیوتر «ممکن است» پذیرفته شود ⚠؛ B2؛ برنامه‌ی میان‌رشته‌ای (AI/علوم شناختی)', None, '2026-12-15', 'تابستان', v='⚠')
N('open', '🟢 باز — مستقیم، بدون هزینه', 'Hildesheim — Future Analytics: AI &amp; Audio Worlds', 'مستقیم (ismll.uni-hildesheim.de/apply — همان پورتال DA/SE)', 'ذکر نشده', 'ندارد (~€470)',
  '۱۵ سپتامبر → <b>۱۵ دسامبر ۲۰۲۶</b> (DAAD)', 'فقط تابستان',
  'برنامه‌ی جدید از تابستان ۲۰۲۷؛ لیسانس CS/DS/AI ✔؛ ۳۰ ظرفیت؛ B2؛ تخصص صوت/موسیقی + AI؛ ⚠ صفحه‌ی رسمی: جزئیات بعداً', 4, '2026-12-15', 'تابستان', v='⚠')
N('open', '🟢 باز (uni-assist)', 'Marburg — Data Science', 'uni-assist', UA, 'ندارد (~€406)',
  '۱ نوامبر → <b>۳۱ دسامبر ۲۰۲۶</b>', '۱ مه → ۳۰ ژوئن',
  'C1 (آیلتس ۷ ✔)؛ دانش عمیق CS + ریاضی، به‌ویژه ML؛ ≥۱۴۴ ECTS', 44, '2026-12-31', 'تابستان')
N('open', '🟢 باز (uni-assist)', 'Marburg — Business Informatics', 'uni-assist', UA, 'ندارد',
  '۱ نوامبر → <b>۳۱ دسامبر ۲۰۲۶</b>', '۱ مه → ۳۰ ژوئن',
  'C1 ✔؛ ⚠ دانش مدیریت بازرگانی هم لازم است', 44, '2026-12-31', 'تابستان', v='⚠')
N('soon', '🔵 از ۲۶ نوامبر', 'Uni Konstanz — CS for Industry &amp; Business (COSIB)', 'مستقیم (ZEuS)', 'ذکر نشده', '€2,650',
  '۲۶ نوامبر → <b>۱۵ ژانویه ۲۰۲۷</b>', '۲۵ مارس → ۳۰ آوریل',
  'ارشد یک‌ساله‌ی آموزش مداوم (۶۰ ECTS) → احتمالاً ۲۴۰ ECTS لازم ⚠؛ ≥۱ سال کار ✔؛ سیستم امتیازی ۲۰ از ۳۵', 60, '2027-01-15', 'تابستان', v='⚠')
N('soon', '🔵 از ۱۷ نوامبر', 'TH OWL — Information Technology (Lemgo, کاربردی)', 'مستقیم (پورتال KIS)', 'ذکر نشده', 'ندارد',
  '۱۷ نوامبر → <b>۱۵ ژانویه ۲۰۲۷</b>', '۱ آوریل → ۱ ژوئن',
  'لیسانس برق/IT/کامپیوتر/مکاترونیک ✔؛ B2؛ uni-assist ذکر نشده؛ ⚠ ECTS و معدل در صفحه نیامده', None, '2027-01-15', 'تابستان', v='⚠')
N('open', '🟢 باز — مستقیم', 'Chemnitz — Web Engineering', 'مستقیم (EduApplication — نه uni-assist)', '⚠ ذکر نشده', 'ندارد (~€340)',
  'تا <b>۱۵ ژانویه ۲۰۲۷</b> (مدارک باید برسد)', 'تا ۱۵ ژوئیه',
  'بدون گزینش (NC-free)؛ لیسانس CS/کامپیوتر کاربردی ✔؛ B2 (آیلتس ۵٫۵)؛ آلمانی A1/A2 به‌عنوان درس داخل برنامه، نه شرط ورود', 57, '2027-01-15', 'تابستان')
N('open', '🟢 باز — مستقیم، بدون هزینه', 'Saarland — Media Informatics', 'مستقیم (sim.uni-saarland.de/bewerbung)', 'ذکر نشده', 'ندارد',
  'تا <b>۱۵ ژانویه ۲۰۲۷</b>', 'تا ۱۵ ژوئیه',
  'C1 اجباری (آیلتس ۷ ✔)؛ آلمانی لازم نیست؛ ۲ توصیه‌نامه؛ لیسانس CS ✔؛ GRE ذکر نشده', 59, '2027-01-15', 'تابستان')
N('open', '🟢 باز (uni-assist)', 'Weimar — Human-Computer Interaction (شرق)', 'uni-assist', UA, 'ندارد (~€340)',
  '۱ نوامبر → <b>۱۵ ژانویه ۲۰۲۷</b>', '۱ آوریل → ۱۵ ژوئیه',
  'معدل ≤۲٫۰ = «شانس خیلی خوب» ✔؛ انگیزه‌نامه ۲–۴ صفحه؛ آیلتس ۶٫۵ ✔', 47, '2027-01-15', 'تابستان')
N('open', '🟢 باز (uni-assist)', 'TU Dortmund — Automation &amp; Robotics', 'uni-assist', UA, 'ندارد (~€320)',
  '۱ نوامبر → <b>۱۵ ژانویه ۲۰۲۷</b> (⚠ برخی برنامه‌ها ۱۵ دسامبر)', '۱ ژانویه → ۱۵ مه',
  'C1 (آیلتس ۷ ✔)؛ ریاضی + «computer systems» از ریزنمرات ⚠', 38, '2027-01-15', 'تابستان', v='⚠')
N('open', '🟢 باز (VPD)', 'THI — Intelligent Aerial Systems (کاربردی)', 'VPD + PRIMUSS', 'VPD €75', '€1,200 + €82',
  '۱۵ اکتبر → <b>۱۵ ژانویه ۲۰۲۷</b>', '۱ آوریل → ۱۵ ژوئیه',
  '۱۸۰ ECTS CS ✔؛ B2؛ A1 تا پایان ترم اول (نه شرط ورود)', 30, '2027-01-15', 'تابستان')
N('open', '🟢 باز (uni-assist یا مستقیم)', 'THI — User Experience Design (کاربردی)', 'uni-assist یا مستقیم THI', 'فقط هزینه‌ی uni-assist', '€1,200 + €82',
  '۱۵ اکتبر → <b>۱۵ ژانویه ۲۰۲۷</b>', '۱ آوریل → ۱۵ ژوئیه',
  '۲۱۰ یا ۱۸۰ + جبران؛ مهارت برنامه‌نویسی + طراحی + تجربه‌ی کار؛ آزمون ارزیابی', 30, '2027-01-15', 'تابستان', v='⚠')
N('soon', '🔵 VIBS باز است — مستقیم، بدون هزینه', 'Augsburg — Data Science', 'مستقیم (VIBS) — بدون VPD', 'ندارد ✔ (رسمی)', 'ندارد (~€177)',
  'مهلت <b>۱ مارس ۲۰۲۷</b> (توصیه برای ویزا: ۱ نوامبر/۱ دسامبر)', 'تا ۱ سپتامبر (توصیه ۱ مه)',
  'رسمی: VPD لازم نیست، هزینه ندارد، GRE بی‌اثر، بدون آزمون/مصاحبه؛ معدل ≤۲٫۷۰ ✔؛ حداقل ECTS: حسابان ۵، جبرخطی ۵، برنامه‌نویسی ۴+۴، الگوریتم ۵، گسسته/پایگاه‌داده ۵، <b>DS/ML ۴ ⚠</b>؛ B2', 73, '2027-03-01', 'تابستان')
N('soon', '🔵 VIBS باز است — مستقیم، بدون هزینه', 'Augsburg — Mathematics &amp; Computer Science', 'مستقیم (VIBS) — بدون VPD', 'ندارد ✔', 'ندارد',
  'مهلت <b>۱ مارس ۲۰۲۷</b> (توصیه ۱ نوامبر/۱ دسامبر)', 'تا ۱ سپتامبر',
  '۶۰ ECTS CS + ۳۰ ریاضی اثبات‌محور ⚠ (یا برعکس)؛ معدل ≤۲٫۷۰ ✔؛ بر اساس مدارک', 73, '2027-03-01', 'تابستان', v='⚠')

# ---------- new: WINTER 2027/28 ----------
W = [
 ('TUHH — Data Science', 'مستقیم (TUNE)', 'ندارد ✔ (TUHH)', 'ندارد', 'تا <b>۱ مارس ۲۰۲۷</b>', 'C1 (آیلتس ۶٫۵ ✔)؛ لیسانس DS یا CS+ریاضی قوی', 54, '2027-03-01', '✅'),
 ('TUHH — Information &amp; Communication Systems', 'مستقیم (TUNE)', 'ندارد ✔', 'ندارد', 'تا <b>۱ مارس ۲۰۲۷</b>', 'C1؛ سابقه‌ی «خیلی خوب»؛ PDF شرایط تخصصی', 54, '2027-03-01', '✅'),
 ('Stuttgart — INFOTECH', 'مستقیم (C@MPUS)', 'ذکر نشده', '€1,500', '<b>۱۵ نوامبر ۲۰۲۶ → ۱۵ ژانویه ۲۰۲۷</b>', 'رسمی: پنجره‌ی زمستان همین حالا؛ C1 آیلتس ۷ ✔؛ CS/برق/IT؛ معدل ≤۲٫۵ ✔', 51, '2027-01-15', '✅'),
 ('Siegen — Human-Computer Interaction', 'مستقیم (UNISONO)', 'ندارد ✔', 'ندارد', '۱ → <b>۳۰ آوریل ۲۰۲۷</b> (تابستان: اکتبر گذشت)', 'معدل ≤۲٫۵ ✔؛ آیلتس ۶٫۵ ✔', 74, '2027-04-30', '✅'),
 ('Oldenburg — Data Science &amp; ML', 'uni-assist', UA, 'ندارد', '۱۵ مارس → <b>۳۰ آوریل ۲۰۲۷</b>', '۲۰ ریاضی + ۱۰ CS؛ بدون GRE؛ رتبه‌بندی با معدل', 10, '2027-04-30', '✅'),
 ('Oldenburg — Digitalised Energy Systems', 'uni-assist', UA, 'ندارد', '۱۵ مارس → <b>۱۵ ژوئن ۲۰۲۷</b>', 'لیسانس CS ✔؛ ۵ OOP + ۵ پردازش اطلاعات + ۱۰ ریاضی', 10, '2027-06-15', '✅'),
 ('Magdeburg — Visual Computing', 'uni-assist', UA, 'ندارد', '۱۵ آوریل → <b>۱۵ مه ۲۰۲۷</b>', 'معدل ≤۲٫۵ ✔؛ توصیه‌نامه + انگیزه‌نامه؛ GRE اختیاری', 14, '2027-05-15', '✅'),
 ('Ulm — Cognitive Systems', '⚠ پورتال Ulm', '⚠', '€1,500', '۱ آوریل → <b>۱۵ مه ۲۰۲۷</b>', 'معدل ≤۲٫۵ ✔؛ CS پذیرفته؛ B2', 12, '2027-05-15', '⚠'),
 ('UTN Nuremberg — Human &amp; AI', 'uni-assist یا UTN', 'ذکر نشده', 'ندارد', '۱ مارس → <b>۳۱ مه ۲۰۲۷</b>', 'C1 (آیلتس ۶٫۵)', 66, '2027-05-31', '⚠'),
 ('KU Eichstätt-Ingolstadt — Data Science', 'uni-assist یا KU', 'ذکر نشده', 'ندارد', '۱ مه → <b>۱۵ ژوئیه ۲۰۲۷</b>', 'ریاضی سنگین؛ GRE Math «به‌شدت توصیه» (نه اجباری)', None, '2027-07-15', '⚠'),
 ('Nordhausen — CE for IoT Systems (کاربردی)', 'uni-assist', UA, 'ندارد', 'پنجره‌ی ۱ نوامبر → <b>۳۱ مارس ۲۰۲۷</b> ⚠', 'ورودی تابستان ۲۱۰ ECTS می‌خواهد ❌ → فقط زمستان با ۱۸۰ ✔؛ معدل ≤۲٫۵ ✔', None, '2027-03-31', '⚠'),
 ('H-BRS — Game Technologies (کاربردی)', 'uni-assist (متقاضی ویزا)', UA, 'ندارد', '۱۵ نوامبر ۲۰۲۶ → <b>۱۵ فوریه ۲۰۲۷</b>', '≥۶۵٪ کامپیوتر در لیسانس ۴ ساله ✔؛ انگیزه‌نامه + CV؛ در حال اعتبارسنجی', 71, '2027-02-15', '⚠'),
 ('Lübeck — Robotics &amp; Autonomous Systems', 'uni-assist', UA, 'ندارد', '۱۵ فوریه → <b>۱ آوریل ۲۰۲۷</b> (تابستان گذشت)', 'معدل ≤۲٫۷ ✔؛ ≥۳۲ ریاضی + ≥۲۸ فنی/کامپیوتر؛ «رشته‌ی مرتبط» ⚠؛ تز لازم نیست', 45, '2027-04-01', '✅'),
 ('TH Köln — Automation &amp; IT', 'uni-assist', UA, 'ندارد', '۱ مارس → <b>۳۰ آوریل ۲۰۲۷</b>', 'معدل ≤۲٫۵ ✔؛ انگیزه‌نامه ۲ صفحه', 26, '2027-04-30', '✅'),
 ('Koblenz — Web &amp; Data Science', 'uni-assist', UA, 'ندارد', 'تا <b>۱۵ ژوئن ۲۰۲۷</b>', 'معدل ≤۲٫۵ ✔؛ آیلتس ۵٫۵؛ تز لازم نیست', None, '2027-06-15', '✅'),
 ('Anhalt — Media Engineering', 'uni-assist', UA, 'ندارد', '۱۵ مارس → <b>۱۵ ژوئیه ۲۰۲۷</b>', 'مسیر ۴ ترمی (۱۸۰ ECTS هر رشته) فقط زمستان؛ مسیر تابستان ۲۱۰ می‌خواهد', None, '2027-07-15', '✅'),
 ('RUB Bochum — Cognitive Science', 'مستقیم (hio)', 'ذکر نشده', 'ندارد', 'تا <b>۱۵ ژوئیه ۲۰۲۷</b>', 'CS در لیست رشته‌ها ✔؛ B2', 49, '2027-07-15', '✅'),
 ('RPTU — Cognitive Science', 'مستقیم', '€60 ارزیابی مدرک خارجی', 'ندارد', '۱ مارس → <b>۳۰ آوریل ۲۰۲۷</b>', 'CS در لیست ✔؛ B2', 8, '2027-04-30', '✅'),
 ('TU Dresden — Computational Modelling &amp; Simulation', '⚠', '⚠', 'ندارد', '۱ آوریل → <b>۳۱ مه ۲۰۲۷</b>', 'CS ✔؛ ریاضی (حسابان، جبرخطی، احتمال)', 18, '2027-05-31', '⚠'),
 ('FAU — International Information Systems', 'مستقیم (campo)', '€100', 'شهریه‌ی غیراروپایی ⚠', '۱۵ آوریل → <b>۳۱ مه ۲۰۲۷</b>', 'C1 آیلتس ۷ ✔؛ CS پذیرفته؛ ترم خارج معاف (تحصیل در ایران)', 65, '2027-05-31', '⚠'),
 ('Saarland — Language Science &amp; Technology', 'مستقیم', 'ذکر نشده', 'ندارد', 'تا <b>۱۵ فوریه ۲۰۲۷</b>', 'زبان‌شناسی رایانشی؛ CS پذیرفته', 59, '2027-02-15', '✅'),
 ('Deggendorf — Digital Health', 'مستقیم', '€60', '€500', '۱۵ آوریل → <b>۱۵ ژوئیه ۲۰۲۷</b>', 'CS ✔؛ C1؛ فرایند ارزیابی', 27, '2027-07-15', '✅'),
 ('Deggendorf — Life Science Informatics', 'مستقیم', '€60', '€500', '۱۵ آوریل → <b>۱۵ ژوئن ۲۰۲۷</b>', 'لیسانس Informatics ✔؛ آزمون ارزیابی؛ C1', 27, '2027-06-15', '✅'),
 ('Bayreuth — Philosophy &amp; CS', 'uni-assist (روال ویژه، پولی)', UA, 'ندارد', '۱ مارس → <b>۱۵ ژوئیه ۲۰۲۷</b>', 'CS ✔؛ A1 تا پایان سال اول؛ مقاله‌ی ۵۰۰ کلمه‌ای', 41, '2027-07-15', '✅'),
 ('Bonn-Rhein-Sieg / Ilmenau / Bremen — دیگر', '—', '—', '—', '—', 'Ilmenau CSP (DSP/مخابرات ⚠)، Bremen MIS (۱۲ CP بازرگانی ⚠)، FU Computational Sciences، FAU Computational Engineering (€100 + شهریه)، Augsburg SE Elite (معدل عالی)، Erfurt SE (طراحی برای ۲۱۰)، Saarland Graduate School — همه ضعیف', None, None, '⚠'),
]
for p, r, f, t, w, n, c, dl, v in W:
    N('winter', '⚪ فقط زمستان', p, r, f, t, 'ندارد', w, n, c, dl, 'زمستان', v=v)

# ---------- new: excluded (with reason) ----------
X = [
 ('Bonn — Artificial Intelligence', '❌ پایان‌نامه ۱۲ ECTS', 'فقط زمستان؛ C1؛ ۱۸ ریاضی/۱۴ نظری/۲۰ برنامه‌نویسی'),
 ('Bonn — Mobile Robotics', '❌ پایان‌نامه ≥۱۰', 'معدل ≤۲٫۰؛ GRE برای غیراروپایی درخواست می‌شود'),
 ('TUM — CSE / DEA / Games / Info Eng / IS', '❌ GRE Q≥۱۶۴ برای ایران', 'همه‌ی برنامه‌های CIT در TUM؛ €6,000 شهریه'),
 ('RWTH — Computer Engineering / HCIS', '❌ GRE', 'GRE General برای غیراروپایی'),
 ('Saarland — Embedded Systems / Visual Computing', '❌ GRE/GATE', ''),
 ('Kiel UAS — Data Science', '❌ GRE ≥۶۵٪', 'برای مدرک خارج از بولونیا'),
 ('Neu-Ulm — AI &amp; Health Informatics', '❌ GRE + A2', ''),
 ('Paderborn — Computer Engineering', '❌ GRE + تز ۱۲ CP', ''),
 ('Passau — Information Systems', '❌ GMAT', ''),
 ('Regensburg — Media Informatics', '❌ GRE + VPD', ''),
 ('Uni Köln — Information Systems', '❌ آلمانی C1', 'Uni Köln ماستر انگلیسی CS ندارد (Informatik آلمانی)'),
 ('Halle (MLU) — Informatik / Economics DS', '❌ آلمانی / ۶۰ ECTS اقتصاد', 'تنها برنامه‌ی انگلیسی: Economics Data Science &amp; Policy'),
 ('Fulda — Data Science', '❌ A2 رسمی', 'فقط زمستان، uni-assist ۱–۳۱ مه'),
 ('Tübingen — CS / Medical Informatics', '❌ آلمانی C1', 'برای لیسانس CS در Medical Informatics (Variant C) هم C1 آلمانی'),
 ('TU Braunschweig — CSE', '❌ A2 آلمانی', ''),
 ('Chemnitz — Data Science', '❌ آلمانی C1', ''),
 ('Koblenz — E-Government', '❌ پایان‌نامه‌ی کارشناسی', 'معدل ≤۲٫۵'),
 ('FH Dortmund — Embedded Systems Eng.', '❌ پایان‌نامه', ''),
 ('Deggendorf — Robotics / Mechatronic &amp; CPS / AI Smart Sensors / Applied AI Production', '❌ ۲۱۰ ECTS در مکاترونیک/صنایع', ''),
 ('RUB — Computational Engineering', '❌ لیسانس CS پذیرفته نمی‌شود', ''),
 ('Hof — AI-Driven Supply Chain', '❌ A1 رسمی + بازرگانی ۲۱۰', ''),
 ('Hochschule Bochum', '❌ ماستر انگلیسی کامپیوتر ندارد', 'فقط مکاترونیک/مکانیک/ژئوترمال'),
 ('HTWK Leipzig', '❌ ماستر انگلیسی ندارد', 'آلمانی لازم'),
 ('Osnabrück Cognitive Computing / Münster DS / THI Automotive AI / RPTU DISC', '❌ پاره‌وقت/پولی', ''),
 ('NIT/TUHH BA&amp;AI · CoDaS · RWTH DDS/AHI · Emden BIDA · FH Wedel', '❌ شهریه‌ی بالا (€5,980–€8,000)', ''),
 ('SRH · Fresenius · HDBW · ISM · Frankfurt School · KLU · Hertie · DIU', '❌ خصوصی و گران', ''),
 ('Ulm — Mathematical Data Science · Bayreuth Scientific Computing · Darmstadt Cognitive Science', '❌ پیش‌نیاز ریاضی/رشته', '۵۰ ریاضی / ۱۶ عددی / ۸۰ CP علوم شناختی'),
]
for p, st, n in X:
    N('excl', st, p, '—', '—', '—', '—', '—', n, None, None, '', v='✅')
U('Bonn — Cyber', st='❌ رد شد (Rejected / Excluded) ۸ نوامبر ۲۰۲۶', n='دلیل را در «View application details» ببین')
U('Bonn — Computer', st='✔ ارسال شد ۳۱ اکتبر · هنوز Received (۸ نوامبر)')
