# -*- coding: utf-8 -*-
# v30 (23 Nov 2026): full cross-check against the uni-assist member list (user, 23 Nov)
# + DAAD International Programmes scan (1,604 English-taught masters, 23 Nov) + official pages.
from rows29 import ROWS as R29
from rows20 import R
import copy
ROWS = copy.deepcopy(R29)
UA = 'uni-assist €75 (هر برنامه‌ی بعدی €30)'

def U(prefix, **kw):
    hits = [r for r in ROWS if r['p'].startswith(prefix)]
    assert len(hits) == 1, (prefix, len(hits), [h['p'] for h in hits])
    r = hits[0]; r['v'] = kw.pop('v', '✅'); r.update(kw); return r

def N(g, st, p, r, f, t, s, w, n, dl=None, dlw='', v='✅'):
    x = R(g, st, p + ' 🆕۳۰', r, f, t, s, w, n, None, dl, dlw); x['v'] = v; ROWS.append(x)

# ---------- corrections (official pages, 22–23 Nov) ----------
U('Paderborn — Computer Science', g='open', st='🟢 الان باز — تا ۳۰ نوامبر', dl='2026-11-30', dlw='تابستان', v='✅',
  n='<b>اصلاح v30:</b> صفحه‌ی رسمی دانشکده: GRE (Q≥۱۵۷، AW≥۴) یا dMAT-CS لازم است <b>مگر</b> معدل تبدیلی با فرمول باواریایی «واقعاً کمتر از ۱٫۸» باشد. معدل تو: ۱ + ۳×(۲۰−۱۷٫۴۳)/(۲۰−۱۰) = <b>۱٫۷۷ → معاف</b> ⚠ (اگر کمینه‌ی قبولی را ۱۲ بگیرند می‌شود ۱٫۹۶ و معاف نیستی). کردیت لازم (هر چهار حوزه، بدون جبران): مهندسی نرم‌افزار ≥۲۰، نظریه ≥۲۰، Computer Engineering ≥۱۵، ریاضی ≥۱۵ — با ریزنمراتت احتمالاً ✔. آیلتس ≥۶٫۵ ✔. شرط پایان‌نامه ندارد. uni-assist؛ <b>۳۰ نوامبر</b>')
U('Paderborn — Computer Engineering', g='open', st='🟢 الان باز — تا ۳۰ نوامبر (⚠ تز)', dl='2026-11-30', dlw='تابستان', v='⚠',
  r='uni-assist', f=UA, t='ندارد', s='تا <b>۳۰ نوامبر ۲۰۲۶</b> (مدارک تکمیلی تا ۱۵ ژانویه)', w='تا ۳۱ مه',
  n='<b>اصلاح v30:</b> صفحه‌ی مرکزی Paderborn معافیت GRE را تأیید می‌کند (معدل تبدیلی بهتر از ۱٫۸ → تو ۱٫۷۷ ✔⚠). ولی شرط لیسانس هنوز: ≥۱۵ ریاضی، ≥۳۰ CS، ≥۳۰ برق و <b>≥۱۲ CP پایان‌نامه‌ی مستقل</b> — تو «Software Project» ۳ واحدی داری → ریسک اصلی همین است؛ کمیته تصمیم می‌گیرد. آیلتس ≥۶٫۵ ✔. اگر فقط یکی از Paderborn را می‌زنی، <b>CS شانس بیشتری دارد</b>')
U('TH OWL — Information Technology', v='⚠',
  n='⚠ <b>دو صفحه‌ی رسمی TH OWL با هم نمی‌خوانند:</b> صفحه‌ی برنامه: غیراروپایی ۱۷ نوامبر → ۱۵ ژانویه از پورتال KIS؛ PDF «Hinweise Master IT»: غیراروپایی از <b>uni-assist</b>، تابستان ۱ اکتبر → <b>۱ دسامبر</b>. امن‌ترین کار: از uni-assist تا <b>۱ دسامبر</b> بفرست. شرط: لیسانس برق/IT/Informatik/مکاترونیک، ≥۱۸۰ ECTS، معدل ≤۲٫۵ ✔ (۱٫۷۷)؛ انگلیسی «خیلی خوب» (B2)؛ <b>Statement of purpose انگلیسی</b>؛ شهریه ندارد',
  s='⚠ ۱ دسامبر (PDF) یا ۱۵ ژانویه (صفحه‌ی برنامه)', dl='2026-12-01')
U('TU Dresden — Computer Science', v='⚠',
  n='uni-assist + پورتال Eignungsfeststellung (همان ایمیل)؛ هر دو تا <b>۳۰ نوامبر</b>. ⚠ صفحه‌ی «اطلاعات اضافی» Dresden: اگر برنامه‌ای در تابستان سمستر اول نداشته باشد، درخواست سمستر اول <b>رد می‌شود</b> — صفحات CS صریحاً شروع تابستان سمستر اول را نمی‌گویند (فقط پنجره‌ی ۱ اکتبر → ۳۰ نوامبر را). مدرک «first degree in computer science»؛ ۹۰ ECTS در حوزه‌های مشخص (≥۲۰ سیستم‌عامل/شبکه/پایگاه‌داده/امنیت، ≥۲۰ ریاضی، ≥۲۵ برنامه‌نویسی/SE/HCI، ≥۱۰ نظریه، ≥۵ معماری)؛ C1 ✔؛ مدارک آزمون صلاحیت: CV، motivation letter، module descriptions؛ GRE «به‌شدت توصیه» (صفحه‌ی SINS نامی از GRE نمی‌برد) → ریسک بالا')
U('FH Südwestfalen — Informatics and Business', v='✅',
  n='صفحه‌ی رسمی (۲۳ نوامبر): «تابستان ۲۰۲۷: ثبت‌نام ممکن نیست»؛ زمستان: غیراروپایی ۱ مارس → ۱ ژوئن از uni-assist + پرسش‌نامه؛ انگلیسی (آیلتس ۶٫۵ ✔)؛ ⚠ لیسانس ≥۲۱۰ ECTS و برای CS ≥۲۰ ECTS مدیریت بازرگانی (تو فقط کارآفرینی) → ضعیف')

U('TU Darmstadt — CS', st='🔵 پورتال از ۱ دسامبر — تصمیم گرفتی بزنی', r='مستقیم (پورتال آنلاین TU Darmstadt) + <b>ارسال کاغذی</b> به Zulassung International، Karolinenplatz 5, 64289 Darmstadt',
  n='✅ <b>تصمیم ۲۳ نوامبر: می‌زنی</b> (آشنایت در آلمان پاکت را تحویل می‌دهد). پنجره: <b>۱ دسامبر ۲۰۲۶ → ۱۵ ژانویه ۲۰۲۷ (cut-off)</b> — هم فرم آنلاین و هم پاکت کاغذی (فرم «Antrag auf Zulassung» امضاشده + مدارک) باید تا ۱۵ ژانویه <b>به دانشگاه برسد</b>؛ مهر پست کافی نیست، ایمیل/آپلود قبول نیست. ⚠ صفحه‌ی دانشکده می‌گوید «certified hard copies»، صفحه‌ی مرکزی بین‌الملل می‌گوید کپی ساده کافی است ولی ترجمه باید «certified» باشد (سفارت آلمان یا مترجم قسم‌خورده در آلمان) → با international.admission@zv.tu-darmstadt.de تأیید کن که ترجمه‌های رسمی ایرانی‌ات قبول است. شرط: ≥۶۰ ECTS هم‌تراز درس‌های هسته‌ی B.Sc. Informatik دارمشتات (چک‌لیست Academic Eligibility را خودت پر کن، نفرست)؛ معدل و سابقه‌ی کار اثری ندارند؛ آیلتس ≥۷ ✔. اگر مدارک صلاحیت را تأیید نکند: دعوت به آزمون ۹۰ دقیقه‌ای <b>حضوری</b> در دارمشتات، هفته‌ی اول مارس (بدون آزمون از راه دور) — معافیت فقط با GRE V≥۱۵۵/Q≥۱۶۵/AW≥۳٫۵ یا GATE ≥۷۵۰ تا ۲۰ فوریه. فقط یکی از CS / AI&amp;ML / IT Security در هر دوره. نتیجه دست‌کم ۸ هفته بعد از رسیدن مدارک')

# ---------- NEW — summer 2027 still possible ----------
N('open', '🟢 الان باز — تا ۳۰ نوامبر', 'Paderborn — Electrical Systems Engineering', 'uni-assist یا PAUL', '+€30', 'ندارد',
  'تا <b>۳۰ نوامبر ۲۰۲۶</b> (مهلت مرکزی ارشدهای انگلیسی)', 'تا ۳۱ مه',
  'تدریس کامل انگلیسی (کلاس آلمانی در دوره اجباری)؛ لیسانس برق «یا مرتبط» ⚠؛ معدل ≤۲٫۵ ✔ <b>یا</b> GRE (DAAD)؛ ⚠ صفحه‌ی درخواست دانشکده GRE را در فهرست مدارک آورده → قبل از پرداخت مطمئن شو؛ گرایش Signal &amp; Information Processing یا Electronics &amp; Devices؛ B2 (آیلتس ۶ ✔)', dl='2026-11-30', dlw='تابستان', v='⚠')
N('open', '🟢 الان باز — تا ۱ دسامبر', 'TH Augsburg — Interactive Media Systems (کاربردی)', 'uni-assist یا HISinOne', UA, 'ندارد (€۱۶۰ ترم)',
  '۱ نوامبر → <b>۱ دسامبر ۲۰۲۶</b>', '۲ مه → ۱۵ ژوئن',
  'MA؛ گرایش‌های انگلیسی: Mixed Reality، HCI Design، Game Development؛ <b>آزمون صلاحیت</b> (tha.de/en/ims)؛ آلمانی لازم نیست؛ انگلیسی با آزمون/مصاحبه؛ رشته‌ی لیسانس ذکر نشده ⚠ — بیشتر طراحی/رسانه تا مهندسی', dl='2026-12-01', dlw='تابستان', v='⚠')
N('open', '🟢 الان باز — تا ۱۵ دسامبر', 'OTH Regensburg — Electrical & Microsystems Engineering (کاربردی)', 'مستقیم (HISinOne) ⚠ VPD', 'ذکر نشده', '⚠ «متغیر» (بایرن)',
  '۱۵ نوامبر → <b>۱۵ دسامبر ۲۰۲۶</b>', '۱ مه → ۳۱ مه',
  'M.Eng. انگلیسی (یا آلمانی)؛ آلمانی لازم نیست؛ B2 (آیلتس ۶ ✔)؛ تمرکز: نیمه‌هادی، اپتوالکترونیک، میکروالکترونیک، سنسور (Infineon/Osram) → <b>تناسب با مهندسی کامپیوتر ضعیف</b>؛ شرایط رشته/معدل در برگه‌ی اطلاعات دانشگاه (DAAD)', dl='2026-12-15', dlw='تابستان', v='⚠')
N('open', '🟢 الان باز — تا ۱۵ دسامبر', 'Aalen — Advanced Systems Design (کاربردی)', 'پورتال Aalen (⚠ Aalen برای مدرک خارجی VPD می‌خواهد)', 'ذکر نشده', '€1,500 / ترم (غیراروپایی)',
  '۱ اکتبر → <b>۱۵ دسامبر ۲۰۲۶</b>', '۱۵ آوریل → ۱۵ ژوئن',
  'پژوهش‌محور؛ لیسانس الکترونیک/برق/اپتیک/مکاترونیک/<b>CS</b> ✔ با معدل بالای میانگین؛ گزینش با تهیه‌ی یک موضوع؛ B2؛ موضوع‌ها: IT security، ML، رباتیک صنعتی، IoT. ⚠ VPD تا ۱۵ دسامبر احتمالاً نمی‌رسد', dl='2026-12-15', dlw='تابستان', v='⚠')
N('open', '🟢 الان باز — تا ۱۵ ژانویه', 'RUB Bochum — Electrical Eng. & IT: Communication Systems', 'مستقیم (hio.ruhr-uni-bochum.de — همان حساب CS)', 'ندارد', 'ندارد (~€۳۸۰ ترم)',
  'اوایل دسامبر → <b>۱۵ ژانویه ۲۰۲۷</b> (غیراروپایی)', 'تا ۱۵ ژوئیه',
  '<b>کل برنامه انگلیسی</b>؛ آلمانی لازم نیست (برای این گرایش)؛ لیسانس برق یا «مشابه» ≥۱۸۰ ECTS با <b>≥۲۵ CP ریاضی</b> و <b>≥۵۰ CP IT/برق/الکترونیک</b> (کمبود تا ۲۵ CP با درس جبرانی)؛ B2 (آیلتس ۶ ✔، MOI قبول نیست)؛ درس‌ها: DSP، مخابرات سیار و بی‌سیم، بهینه‌سازی، <b>ML</b>. تناسب خوب با مهندسی کامپیوتر', dl='2027-01-15', dlw='تابستان', v='✅')
N('open', '🟢 الان باز — تا ۱۵ ژانویه', 'HS Bremen — Electronics Engineering (کاربردی)', 'مستقیم (فرم + مدارک) + VPD از uni-assist برای تبدیل معدل', 'ذکر نشده', 'ندارد (~€۴۴۰ ترم)',
  'نسخه‌ی ۳ترمه: ۱۵ دسامبر → <b>۱۵ ژانویه ۲۰۲۷</b> (نسخه‌ی ۴ترمه تا ۱۵ اکتبر — گذشت)', '۳ترمه: ۱ ژوئن → ۱۵ ژوئیه',
  'تمرکز «Intelligent Systems»: طراحی IC و سیستم، FPGA، ML، پیاده‌سازی سخت‌افزاری AI، DSP، مخابرات → <b>تناسب خوب با مهندسی کامپیوتر</b>؛ CS هم پذیرفته؛ معدل ≤۲٫۵ ✔؛ <b>C1</b> (آیلتس ۷ ✔)؛ ⚠ نسخه‌ی ۳ترمه ۲۱۰ ECTS می‌خواهد؛ <b>۲ توصیه‌نامه</b> با فرم مخصوص؛ ⚠ DAAD هم «آلمانی لازم نیست» و هم «آشنایی پایه با آلمانی» نوشته', dl='2027-01-15', dlw='تابستان', v='⚠')
N('open', '🟢 الان باز — تا ۱۵ ژانویه', 'Kempten — Electrical Engineering (کاربردی)', 'مستقیم (meincampus.hs-kempten.de)', 'ذکر نشده', '€500 / ترم (غیراروپایی)',
  '۱۵ نوامبر → <b>۱۵ ژانویه ۲۰۲۷</b>', '۲۷ آوریل → ۱۵ ژوئیه',
  'M.Eng. انگلیسی، کاربردی؛ لیسانس برق/مخابرات/الکترونیک ⚠ (مهندسی کامپیوتر نام برده نشده)؛ B2 (آیلتس ۵٫۵ ✔)؛ آلمانی A1 در ترم ۱ یا ۲ در خود دانشگاه', dl='2027-01-15', dlw='تابستان', v='⚠')
N('open', '🟡 فقط اگر VPD همین هفته', 'HAW Hamburg — Information & Communications Engineering (کاربردی)', 'مستقیم (myHAW) + <b>VPD از uni-assist</b>', 'ذکر نشده', 'ندارد (€۳۹۷ ترم)',
  '۱ دسامبر → <b>۱۵ ژانویه ۲۰۲۷</b>', '۱ ژوئن → ۱۵ ژوئیه',
  'انگلیسی؛ B2 ✔؛ لیسانس برق/Information Engineering/CS سیستم‌های فنی یا مشابه؛ با ۱۸۰ ECTS باید ۳۰ کردیت اضافه بگذرانی مگر ≥۶ ماه کار بعد از لیسانس. ⚠ راهنمای HAW: VPD «دست‌کم ۸ هفته قبل از شروع پنجره» → برای تابستان دیر است؛ <b>برای زمستان ۲۰۲۷/۲۸ عالی</b> (VPD را تا آوریل بگیر)', dl='2027-01-15', dlw='تابستان', v='⚠')
N('open', '🟡 VPD تا ۱۵ دسامبر نمی‌رسد', 'TH Augsburg — Electrical Engineering (کاربردی)', 'HISinOne + <b>VPD مخصوص THA</b> از uni-assist (۴–۶ هفته)', 'ذکر نشده', 'ندارد (€۱۶۴ ترم)',
  '۱۵ نوامبر → ۱۵ دسامبر ۲۰۲۶', '<b>۲ مه → ۱۵ ژوئیه ۲۰۲۷</b>',
  'فقط انگلیسی؛ آلمانی لازم نیست؛ لیسانس برق، مکاترونیک یا <b>Computer Engineering</b> ✔؛ معدل ≤۲٫۶۹ ✔؛ ۲۱۰ ECTS (با ۱۸۰ پذیرش مشروط + جبران در سال اول)؛ B2 (آیلتس ۶٫۵ ✔)؛ motivation letter. <b>برای زمستان VPD را از الان سفارش بده</b>', v='✅')

# ---------- NEW — winter 2027/28 ----------
N('winter', '⚪ زمستان — الان باز (تا ۱۵ ژانویه)', 'Stuttgart — Electrical Engineering (MSc, English)', 'مستقیم (C@MPUS — همان حساب CS)', 'ذکر نشده', '€1,500 / ترم (BW، غیراروپایی)',
  '—', '<b>۱۵ نوامبر ۲۰۲۶ → ۱۵ ژانویه ۲۰۲۷</b>',
  'کاملاً انگلیسی؛ آلمانی لازم نیست؛ لیسانس برق و IT «یا مرتبط» ⚠؛ C1 (آیلتس ۷ ✔). ورودی تابستان هم دارد (۱۵ مه → ۱۵ ژوئیه برای تابستان ۲۰۲۸)', dl='2027-01-15', dlw='زمستان', v='⚠')
N('winter', '⚪ فقط زمستان', 'h_da Darmstadt — EEIT International (کاربردی)', 'مستقیم (mse-application-hda.de)', 'ذکر نشده', 'ندارد (~€۳۸۳ ترم)',
  'برای مدرک خارجی ذکر نشده', '<b>تا ۳۱ مارس ۲۰۲۷</b>',
  'انگلیسی؛ ۴ ترم (۲ ترم دانشگاه + ۲ ترم پروژه در صنعت)؛ گرایش <b>Embedded Systems &amp; Microelectronics</b>، Communications، Automation؛ لیسانس برق/الکترونیک/IT/<b>CS</b> ✔؛ «نمرات عالی» و تجربه‌ی IT اولویت دارد؛ B2 (آیلتس ۶٫۵ ✔)؛ کلاس آلمانی اجباری در دوره', dl='2027-03-31', dlw='زمستان')
N('winter', '⚪ فقط زمستان', 'Frankfurt UAS — Information Technology (کاربردی)', 'uni-assist', UA, 'ندارد (~€۳۸۰ ترم)', '—', '<b>تا ۱۵ آوریل ۲۰۲۷</b>',
  'همه‌ی درس‌ها انگلیسی؛ آلمانی لازم نیست؛ لیسانس برق و IT با تمرکز ICT «یا مشابه» ⚠؛ معدل ≤۲٫۰ ✔ (۱٫۷۷)؛ ≥۱۸۰ ECTS؛ B2؛ ظرفیت محدود', dl='2027-04-15', dlw='زمستان', v='⚠')
N('winter', '⚪ فقط زمستان', 'Magdeburg — Electrical Engineering & IT (شرق)', 'uni-assist', UA, 'ندارد (€۳۱۱ ترم)', '—', '<b>تا ۱۵ ژوئیه ۲۰۲۷</b>',
  'فقط انگلیسی؛ آلمانی لازم نیست؛ لیسانس برق/IT «یا مرتبط»؛ معدل ≤۲٫۰ ✔؛ B2 (آیلتس ۶٫۵ ✔)؛ حوزه‌ها: Automation، ICT، Power &amp; Energy (گرایش Image Processing هم دارد)', dl='2027-07-15', dlw='زمستان', v='⚠')
N('winter', '⚪ فقط زمستان', 'FH Erfurt — Software Engineering (شرق، کاربردی)', 'uni-assist', UA, 'ندارد', '—', '۱۵ مه → ۱۵ سپتامبر ۲۰۲۷ (DAAD) ⚠',
  'انگلیسی، برنامه‌ی تازه (از زمستان ۲۰۲۶/۲۷)؛ لیسانس نرم‌افزاری یا نزدیک ✔؛ معمولاً ۲۱۰ ECTS (با ۱۸۰ مشروط)؛ B2؛ آلمانی لازم نیست؛ تجربه‌ی کاری نرم‌افزار امتیاز دارد', dl='2027-09-15', dlw='زمستان', v='⚠')
N('winter', '⚪ فقط زمستان', 'Chemnitz — Embedded Systems (شرق)', 'uni-assist', UA, 'ندارد (€۳۴۰ ترم)', '—', '<b>تا ۱۵ ژوئیه ۲۰۲۷</b>',
  'تدریس ۱۰۰٪ انگلیسی؛ معماری دیجیتال، پردازش سیگنال، بینایی ماشین، سیستم‌های بی‌درنگ → تناسب خوب؛ ⚠ <b>آلمانی A1 با مدرک رسمی</b> (Goethe/telc/ÖSD) — گواهی دوره‌های انجمن اتریش احتمالاً کافی نیست؛ B2؛ معادل‌بودن لیسانس را کمیته تعیین می‌کند', dl='2027-07-15', dlw='زمستان', v='⚠')
N('winter', '⚪ فقط زمستان', 'Chemnitz — Information & Communication Systems (شرق)', 'EduApplication', 'ذکر نشده', 'ندارد', '—', '<b>تا ۱۵ ژوئیه ۲۰۲۷</b>',
  '۱۰۰٪ انگلیسی؛ گرایش Information Processing یا Communication Systems؛ ⚠ آلمانی A1 رسمی؛ B2', dl='2027-07-15', dlw='زمستان', v='⚠')
N('winter', '⚪ فقط زمستان', 'Chemnitz — Automation, Robotics & Control (شرق)', 'uni-assist', UA, 'ندارد', '—', 'تا ۱۵ ژوئیه ۲۰۲۷',
  '۱۰۰٪ انگلیسی؛ ⚠ آلمانی A1 رسمی؛ لیسانس برق/Digital Engineering یا معادل؛ کنترل‌محور → تناسب متوسط', v='⚠')
N('winter', '⚪ فقط زمستان', 'BHT Berlin — Information & Communications Engineering (کاربردی)', '⚠', 'ذکر نشده', 'ندارد', '—', '⚠ اعلام نشده',
  'M.Eng. انگلیسی، ۳ ترم؛ برای فارغ‌التحصیلان برق و <b>Technical Computer Science</b>؛ B2؛ ظرفیت محدود (DAAD)', v='⚠')
N('passed', '⏹ فقط ورودی تابستان — ۳۰ سپتامبر گذشت', 'Ulm — Communication & Information Technology', 'پورتال Ulm', 'ذکر نشده', '€1,500 / ترم (BW)',
  'فقط تابستان؛ ۱۵ اوت → ۳۰ سپتامبر (برای تابستان ۲۰۲۸)', 'ورودی زمستان ندارد',
  '۱۰۰٪ انگلیسی؛ گرایش Intelligent Systems (ML، الگو، امنیت) و Communications؛ معدل ≤۲٫۰ ✔؛ C1 ✔؛ لیسانس برق/مخابرات/الکترونیک یا مرتبط با ۶ از ۸ موضوع پایه', v='✅')

# ---------- NEW — excluded ----------
for p, why in (
    ('Hannover — EEIT: Microelectronics track', '≥۱۰ ECTS کنترل (درس کنترل نداری) + C1 + مهلت ۳۰ نوامبر'),
    ('Hannover — AI-Driven Mechatronics & Robotics', '≥۱۵ ECTS مکانیک فنی + ۲۰ ECTS برق/درایو لازم'),
    ('Kiel (CAU) — Electrical & Information Engineering', 'GRE Quant ≥ صدک ۶۴ برای غیراروپایی (منبع ثانویه ⚠)؛ مهلت تابستان ۲۵ سپتامبر گذشت'),
    ('Regensburg — Human-Centred AI', 'GRE برای مدرک کشورهای خارج از کنوانسیون لیسبون (ایران) + VPD + ≥۱۸ CP پردازش زبان'),
    ('Potsdam — Computer Science (Digital Engineering Faculty)', 'آیین‌نامه‌ی پذیرش ۲۰۲۵: GRE General برای متقاضی خارجی'),
    ('Magdeburg — AI & Engineering for Medical Applications', '€4,165/ترم + ۱ سال کار + آلمانی A2 + آناتومی'),
    ('Emden/Leer — Business Informatics', '€5,980/ترم + ۱ سال کار بعد از لیسانس'),
    ('TH Rosenheim — Engineering Sciences (EEIT)', 'آلمانی A2 با مدرک رسمی'),
    ('FU Berlin — Computer Science', 'تدریس عمدتاً آلمانی'),
    ('Goethe Frankfurt — Computer Science', 'تدریس آلمانی'),
    ('Uni Bremen — Computer Science / EEIT', 'آلمانی (EEIT: آلمانی C1)'),
    ('HAW Hamburg — Computer Science', 'تدریس آلمانی؛ آلمانی C1')):
    N('excl', '❌ ' + why.split('؛')[0].split(' + ')[0], p, '—', '—', '—', '—', '—', why)

# ---------- coverage of the uni-assist member list (user's list, 23 Nov) ----------
# k: 'in' = already in guide, 'new' = new v30 rows, 'none' = no relevant English master found, 'na' = not relevant type
COVER = [
 ('Bauhaus-Universität Weimar','in','CS for Digital Media، HCI، Digital Engineering'),
 ('Bergische Universität Wuppertal','in','Computer Simulation in Science (زمستان)؛ Smart Materials (مرتبط نیست)'),
 ('Berliner Hochschule für Technik (BHT)','new','Data Science (زمستان)؛ 🆕 Information &amp; Communications Eng.'),
 ('BSP Business and Law School','na','خصوصی، مدیریت/حقوق'),
 ('BTU Cottbus-Senftenberg','in','AI (باز)، Cyber Security (زمستان)'),
 ('Carl von Ossietzky Universität Oldenburg','in','CS، DS &amp; ML، Digitalised Energy Systems (همه زمستان)'),
 ('Charité Universitätsmedizin Berlin','na','پزشکی'),
 ('Christian-Albrechts-Universität zu Kiel','new','CS (باز تا ۱۵ دسامبر)؛ 🆕 EIE ❌ GRE'),
 ('Europa-Universität Viadrina','none','حقوق/اقتصاد'),
 ('Ev. Hochschule Bochum · EH Berlin · EVHN Nürnberg','na','الهیات/علوم اجتماعی'),
 ('Fachhochschule Aachen','none','در پایگاه DAAD ارشد انگلیسی مرتبط ندارد'),
 ('Fachhochschule Dortmund','in','Digital Transformation (زمستان)؛ ESE و Medical Informatics ❌'),
 ('Fachhochschule Erfurt','new','🆕 Software Engineering (زمستان)'),
 ('Fachhochschule Potsdam','none','طراحی/علوم اجتماعی'),
 ('Fachhochschule Südwestfalen','in','Informatics &amp; Business (تابستان ۲۰۲۷ ندارد)؛ IMIS ❌'),
 ('Fachhochschule Wedel','na','خصوصی (IT Engineering €3,230)'),
 ('FH Westküste','none','ارشد انگلیسی مرتبط ندارد'),
 ('Frankfurt University of Applied Sciences','new','High Integrity Systems (زمستان)؛ 🆕 Information Technology (زمستان)؛ GCS ❌ آلمانی'),
 ('Freie Universität Berlin','new','Data Science (زمستان)؛ 🆕 CS ❌ آلمانی'),
 ('Goethe-Universität Frankfurt','new','🆕 CS ❌ آلمانی'),
 ('HAW Kiel','in','CS / DS ❌ (GRE)'),
 ('Heinrich-Heine-Universität Düsseldorf','in','AI &amp; Data Science (زمستان)'),
 ('HMU Erfurt · HMU Potsdam','na','پزشکی'),
 ('Hochschule 21','na','خصوصی/دوگانه'),
 ('Hochschule Aalen','new','ML &amp; DA (باز، VPD)، CS (زمستان)؛ 🆕 Advanced Systems Design (€1,500)'),
 ('Hochschule Anhalt','in','Electrical &amp; Computer Eng. (باز)، Media Engineering (زمستان)'),
 ('Hochschule Ansbach','none','ارشد انگلیسی مرتبط ندارد'),
 ('Hochschule Bielefeld (HSBI)','in','Data Science Research Master (VPD)'),
 ('Hochschule Bochum','in','❌ (Mechatronics — مرتبط نیست)'),
 ('Hochschule Bremen','new','🆕 Electronics Engineering (باز تا ۱۵ ژانویه)'),
 ('Hochschule Coburg','in','Autonomous Driving، VC&amp;AI ❌ (VPD/Primuss)'),
 ('Hochschule Darmstadt (h_da)','new','🆕 EEIT International (زمستان)'),
 ('HBK Saar · Muthesius · UdK Berlin','na','هنر'),
 ('Hochschule Düsseldorf','none','ارشد انگلیسی مرتبط ندارد'),
 ('Hochschule Emden/Leer','new','Industrial Informatics، BI&amp;DA ❌؛ 🆕 Business Informatics ❌ (€5,980)'),
 ('Hochschule Flensburg','none','ارشد انگلیسی مرتبط ندارد'),
 ('Hochschule Fulda','in','Global Software Development ❌، Data Science (زمستان)'),
 ('HAW Hamburg','new','🆕 Information &amp; Communications Eng. (VPD)؛ CS ❌ آلمانی'),
 ('Hochschule für Nachhaltige Entwicklung Eberswalde','none','Forest IT (مرتبط نیست)'),
 ('HTW Berlin','in','❌ (Project Mgmt &amp; DS / IT Business)'),
 ('HTW Dresden','none','ارشد انگلیسی مرتبط ندارد'),
 ('HWR Berlin','none','BI &amp; Process Mgmt (مدیریتی)'),
 ('Hochschule Hamm-Lippstadt','none','فقط ارشدهای مدیریتی/توسعه‌ی محصول انگلیسی'),
 ('Hochschule Hannover','none','ارشد انگلیسی مرتبط ندارد'),
 ('Hochschule Harz','none','ارشد انگلیسی مرتبط ندارد'),
 ('Hochschule Heilbronn','in','Software Eng. (SEM)، Applied AI (VPD/Studienkolleg)'),
 ('Hochschule Hof','in','ARCS ❌، SEIA ❌، AI &amp; Robotics ❌، CS ❌'),
 ('Hochschule Kaiserslautern','none','فقط Mechanical/Mechatronics'),
 ('Hochschule Kempten','new','🆕 Electrical Engineering (باز تا ۱۵ ژانویه، €500)'),
 ('Hochschule Koblenz','none','ارشد انگلیسی مرتبط ندارد'),
 ('Hochschule Landshut','none','ارشد انگلیسی مرتبط ندارد'),
 ('Hochschule Magdeburg-Stendal','none','ارشد انگلیسی مرتبط ندارد'),
 ('Hochschule Mainz','in','Applied Computer Science (زمستان)'),
 ('Hochschule Merseburg','none','ارشد انگلیسی مرتبط ندارد'),
 ('Hochschule München (HM)','none','ارشد انگلیسی مرتبط ندارد'),
 ('Hochschule Neu-Ulm','in','AI &amp; DA، AI &amp; Health ❌ (GRE)'),
 ('Hochschule Neubrandenburg','none','ارشد انگلیسی مرتبط ندارد'),
 ('Hochschule Niederrhein','none','ارشد انگلیسی مرتبط ندارد'),
 ('Hochschule Nordhausen','in','CE for IoT Systems (زمستان)'),
 ('Hochschule Osnabrück','none','ارشد انگلیسی مرتبط ندارد'),
 ('Hochschule RheinMain','none','Biomedical Eng.، Aviation (مرتبط نیست)'),
 ('Hochschule Ruhr West','none','ارشد انگلیسی مرتبط ندارد'),
 ('Hochschule Stralsund','in','❌'),
 ('Hochschule Weihenstephan-Triesdorf','none','کشاورزی/محیط زیست'),
 ('Hochschule Wismar','none','ارشد انگلیسی مرتبط ندارد'),
 ('Hochschule Worms','none','مدیریت/گردشگری'),
 ('Hochschule Zittau/Görlitz','none','ارشد انگلیسی مرتبط ندارد'),
 ('HTWK Leipzig','in','❌'),
 ('HS Rhein-Waal','in','Usability Eng. (باز)، Information Eng. &amp; CS ❌'),
 ('htw saar','none','ارشد انگلیسی مرتبط ندارد'),
 ('IPU Berlin · SDI München · INU · IST · NORDAKADEMIE · Rheinische HS Köln','na','خصوصی/غیرمرتبط'),
 ('Jade Hochschule','none','ارشد انگلیسی مرتبط ندارد'),
 ('Hochschule Trier · Umwelt-Campus Birkenfeld','none','ارشد انگلیسی مرتبط ندارد (Uni Trier جداست)'),
 ('Julius-Maximilians-Universität Würzburg','in','CS ❌ (VPD)'),
 ('Justus-Liebig-Universität Gießen','none','Agrobioinformatics (مرتبط نیست)'),
 ('Katholische HS Mainz · KSH München','na','الهیات/علوم اجتماعی'),
 ('Leibniz Universität Hannover','new','CS ❌ (VPD)، CE ❌ آلمانی؛ 🆕 EEIT Microelectronics ❌، AI-Driven Mechatronics ❌'),
 ('Ludwig-Maximilians-Universität München','in','Statistics &amp; DS ❌'),
 ('Martin-Luther-Universität Halle-Wittenberg','in','❌'),
 ('Medical School Berlin · MHH · Med. Uni Lausitz · MSH Hamburg','na','پزشکی'),
 ('OTH Amberg-Weiden','in','AI for Industrial Applications (VPD)'),
 ('OTH Regensburg','new','🆕 Electrical &amp; Microsystems Eng. (باز تا ۱۵ دسامبر)'),
 ('Ostfalia Hochschule','none','Automotive Service Tech. (مرتبط نیست)'),
 ('Otto-von-Guericke-Universität Magdeburg','new','DKE، Digital Eng. (تابستان گذشت)، Visual Computing؛ 🆕 EEIT (زمستان)، AI Medical ❌'),
 ('Philipps-Universität Marburg','in','CS، Data Science، Business Informatics'),
 ('RPTU Kaiserslautern-Landau','in','CS، ESY، A&amp;C، Cognitive Science'),
 ('TH Aschaffenburg','none','ارشد انگلیسی مرتبط ندارد'),
 ('TH Augsburg','new','🆕 Interactive Media Systems (باز تا ۱ دسامبر)، 🆕 Electrical Engineering (VPD)؛ IMS(Mech.) ❌'),
 ('TH Bingen','in','CS (زمستان)'),
 ('TH Brandenburg','none','ارشد انگلیسی مرتبط ندارد'),
 ('TH Ingolstadt','in','AI، AI Eng. Aut. Systems، Aerial، UX، Cybersecurity (VPD)'),
 ('TH Köln','in','Digital Sciences، Automation &amp; IT'),
 ('TH Lübeck','none','Biomedical Eng. (مرتبط نیست)'),
 ('TH Mittelhessen (THM)','in','Business Informatics (Analytics)'),
 ('TH Ostwestfalen-Lippe','in','Information Technology — ⚠ مهلت متناقض (۱ دسامبر / ۱۵ ژانویه)'),
 ('TH Rosenheim','new','🆕 Engineering Sciences ❌ (A2)'),
 ('TH Würzburg-Schweinfurt','in','AI (VPD)'),
 ('TU Bergakademie Freiberg','none','فقط مواد/شیمی'),
 ('TU Berlin','in','CS (VPD)'),
 ('TU Chemnitz','new','Web Eng.، Automotive SE؛ 🆕 Embedded Systems، ICS، ARC (زمستان، A1 رسمی)'),
 ('TU Dortmund','in','Data Science، Automation &amp; Robotics، Informatik'),
 ('TU Dresden','in','CS (⚠ تابستان)، CMS'),
 ('TU Ilmenau','in','RCSE، DS، RME (تابستان گذشت)'),
 ('TU München','in','❌ (GRE/شهریه €6,000)'),
 ('Universität Augsburg','in','Data Science، Math &amp; CS، SE'),
 ('Universität Bayreuth','in','CS ❌ (VPD)، Philosophy &amp; CS'),
 ('Universität Bielefeld','in','Intelligent Interactive Systems'),
 ('Universität Bremen','new','CIT/CMM، AI &amp; IS، Digital Media؛ 🆕 CS / EEIT ❌ آلمانی'),
 ('Universität des Saarlandes','in','Media Informatics، Systems Eng.، …'),
 ('Universität Duisburg-Essen','in','ESE و CommEng ✅ ارسال‌شده'),
 ('Universität Greifswald','in','Data Science (زمستان)'),
 ('Universität Kassel','in','CS ❌، Electrical Communication Eng.'),
 ('Universität Koblenz','in','Web &amp; Data Science'),
 ('Universität Leipzig','in','Data Science ❌'),
 ('Universität Osnabrück','in','Cognitive Science'),
 ('Universität Paderborn','new','CS ✅ اصلاح، CE ⚠ اصلاح؛ 🆕 Electrical Systems Eng.'),
 ('Universität Passau','in','CS، AI Engineering'),
 ('Universität Potsdam','new','Data Science؛ 🆕 CS ❌ GRE'),
 ('Universität Regensburg','new','CS، Media Informatics ❌؛ 🆕 Human-Centred AI ❌ GRE'),
 ('Universität Rostock','in','CSI، Electrical Engineering'),
 ('Universität Ulm','new','Cognitive Systems؛ 🆕 CIT (فقط تابستان؛ ۲۰۲۸)'),
 ('Universität zu Köln (+ VPD)','in','Information Systems ❌'),
 ('Universität zu Lübeck','in','AI ❌، Robotics (زمستان)'),
 ('Westsächsische Hochschule Zwickau','none','ارشد انگلیسی مرتبط ندارد'),
]
