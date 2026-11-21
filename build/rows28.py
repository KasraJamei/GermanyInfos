# -*- coding: utf-8 -*-
# v28 (21 Nov 2026): merges v26/v27 findings (20 Nov) + round-4 official checks (14 Nov) into rows25.
from rows25 import ROWS as R25
from rows20 import R
import copy
ROWS = copy.deepcopy(R25)
UA = 'uni-assist €75 (هر برنامه‌ی بعدی €30)'

def U(prefix, **kw):
    hits = [r for r in ROWS if r['p'].startswith(prefix)]
    assert len(hits) == 1, (prefix, len(hits), [h['p'] for h in hits])
    r = hits[0]
    r['v'] = kw.pop('v', '✅')
    r.update(kw)
    return r

def N(g, st, p, r, f, t, s, w, n, dl=None, dlw='', v='✅'):
    x = R(g, st, p + ' 🆕۲۸', r, f, t, s, w, n, None, dl, dlw)
    x['v'] = v
    ROWS.append(x)

PASS15 = '⏹ مهلت ۱۵ نوامبر گذشت'

# ---------- submitted ----------
U('Stuttgart — Computer Science', g='done', st='✔ ارسال شد · نوامبر ۲۰۲۶ (ورودی زمستان ۲۰۲۷/۲۸)',
  n='ترم زمستان؛ اگر مدرکی ناقص مانده، تا ۱۵ ژانویه ۲۰۲۷ در پورتال self-service آپلود کن')
U('Bochum — Computer Science', g='done', st='✔ ارسال شد ۲۰ نوامبر ۲۰۲۶ (ورودی زمستان ۲۰۲۷/۲۸)',
  n='فقط ورودی زمستان برای غیراروپایی؛ ≥۱۸۰ ECTS با ≥۵۰ هسته‌ی CS و ≥۱۸ ریاضی؛ C1؛ در پورتال مطمئن شو Submit شده')
U('Bonn — Cyber Security', st='❌ رد شد (Rejected / Excluded) ۸ نوامبر ۲۰۲۶', n='دلیل را در «View application details» ببین')
U('Bonn — Computer Science', st='✔ ارسال شد ۳۱ اکتبر ۲۰۲۶ · Received')

# ---------- 15 Nov passed ----------
for p in ('TU Ilmenau — RCSE', 'TU Ilmenau — Data Science', 'TU Ilmenau — Research in Media', 'Magdeburg — Digital Engineering'):
    U(p, g='passed', st=PASS15 + ' (زمستان می‌ماند)', v='✅')
U('Magdeburg — Data and Knowledge', g='passed', v='⚠', st=PASS15 + ' (⚠ یک منبع ۲۶ نوامبر)',
  n='منابع تناقض دارند (۱۵ یا ۲۶ نوامبر). اگر می‌خواهی، همین امروز در My assist مهلت را ببین؛ وگرنه زمستان (تا ۱۵ مه)')
for p in ('Deggendorf — Applied Computer Science', 'Deggendorf — AI &amp; Data Science', 'Deggendorf — Automotive Software'):
    U(p, g='passed', st=PASS15, v='✅', n='اگر €60 را پرداخت و «Bewerbung absenden» را نزده بودی، این ترم بسته است. زمستان: ۱۵ آوریل → ۱۵ مه')
U('Saarland — Cybersecurity', g='excl', st='❌ GRE (رسمی)', n='راهنمای رسمی ماسترهای انگلیسی Saarland (۹ نوامبر): مدرک غیر EHEA ⇒ GRE General یا GATE؛ IELTS ≥ 7.0؛ معدل ≥ ۳٫۰/۴ و ۱۰٪ برتر. مهلت ۱۵ نوامبر هم گذشت.')
U('Saarland — Data Science &amp; AI', g='excl', st='❌ GRE (رسمی)', n='همان راهنمای رسمی Saarland: GRE/GATE برای مدرک غیر EHEA')

# ---------- corrections from 14 Nov official checks ----------
U('Hannover — Computer Science', g='excl', st='❌ آلمانی C1 (رسمی)',
  n='صفحه‌ی رسمی LUH (۱۴ نوامبر): «International application: German C1» به‌علاوه‌ی English C1؛ VPD لازم. مهلت ۳۰ نوامبر')
U('TH OWL — Information Technology', g='open', st='🟢 الان باز (از ۱۷ نوامبر)', r='uni-assist (غیراروپایی) — نه KIS', f=UA,
  s='۱۷ نوامبر → <b>۱۵ ژانویه ۲۰۲۷</b>',
  n='❗ اصلاح: صفحه‌ی بین‌الملل TH OWL: مدرک غیراروپایی ⇒ درخواست از uni-assist (KIS فقط برای اروپایی‌ها). B2؛ شهریه ندارد؛ statement of purpose؛ کپی تأییدشده + ترجمه‌ی رسمی آپلود. ⚠ ECTS/معدل در صفحه نیامده')
U('Chemnitz — Web Engineering', v='⚠', f='≈ €49.95 (EduApplication) ⚠',
  n='پایلوت EduApplication (نه uni-assist)؛ غیراروپایی تا ۱۵ ژانویه، مدارک باید تا مهلت برسد؛ بدون گزینش؛ B2 (آیلتس ۵٫۵)؛ ⚠ هزینه‌ی €49.95 روی صفحه‌ی Advanced Manufacturing همین سامانه آمده، صفحه‌ی Web Eng مبلغ نمی‌گوید')
U('Saarland — Media Informatics', v='⚠', st='🟢 از اوایل دسامبر (پورتال SIM)',
  n='پورتال sim.uni-saarland.de (جدا از پورتال CS)؛ اوایل دسامبر → ۱۵ ژانویه؛ معدل ≤۲٫۳ ✔ یا توصیه‌نامه/مصاحبه؛ C1 (آیلتس ۷ ✔، MOI قبول نیست)؛ GRE در صفحه نیامده؛ ⚠ VPD برای ماستر را تأیید کن')
U('TU Darmstadt — CS', v='✅', st='🔵 از ۱ دسامبر',
  n='❗ کپی برابر اصل کاغذی باید تا ۱۵ ژانویه <b>برسد</b> (مهر پست کافی نیست). اگر مدارک صلاحیت را تأیید نکند: آزمون ۹۰ دقیقه‌ای حضوری در دارمشتات (هفته‌ی اول مارس). GRE V155/Q165/AW3.5 یا GATE 750 معاف می‌کند. آیلتس ۷ ✔. فقط یکی از CS / AI&amp;ML / IT Security در هر دوره')
U('Hildesheim — Future Analytics', v='✅',
  n='پورتال ismll: «International: Dec. 15, 2026» ✔؛ حداکثر ۳۰ ظرفیت؛ گزینش با معدل + توانایی‌های مرتبط؛ B2 (آیلتس ≥۵٫۵)؛ هزینه ذکر نشده؛ برنامه‌ی تازه — جزئیات بیشتر بعداً')
U('Augsburg — Data Science', v='✅', st='🟢 VIBS باز — بفرست',
  n='رسمی: VPD لازم نیست، هزینه ندارد، آزمون/مصاحبه ندارد؛ معدل ≤۲٫۷۰ ✔؛ B2؛ حداقل ECTS: حساب ۵، جبرخطی ۵، زبان برنامه‌نویسی ۴، برنامه‌نویسی عملی ۴، الگوریتم/عددی ۵، گسسته/پایگاه‌داده ۵، <b>DS/ML ۴ ⚠</b>. تاریخ توصیه‌شده برای غیراروپایی (۱ نوامبر) گذشته → هرچه زودتر. ⚠ اگر IAU در anabin کامل H+ نباشد، ارزیابی ZAB لازم می‌شود')
U('Augsburg — Mathematics', v='✅', st='🟢 VIBS باز',
  n='کامل انگلیسی ممکن؛ ۶۰ ریاضی + ۳۰ CS یا ۳۰ ریاضی + ۶۰ CS؛ ≤۲٫۷۰؛ B2؛ بدون VPD و هزینه. بعد از تاریخ توصیه‌شده (۱ نوامبر/۱ دسامبر) پذیرش فقط برای یک ترم معتبر است')
U('TUHH — Computer Science', v='✅',
  n='۱ دسامبر → ۱۵ ژانویه؛ precheck معدل لازم؛ آیلتس ۶٫۵ ✔؛ هزینه ندارد، uni-assist ندارد (راهنمای How-to-apply 2026)')
U('TUHH — Data Science', v='⚠', n='فقط زمستان. ⚠ PDF برنامه‌های انگلیسی TUHH «۱۵ ژانویه → ۱ مارس» نوشته؛ راهنمای عمومی برای زمستان ۲۰۲۶ «۱ دسامبر → ۱ فوریه» بود — قبل از اقدام چک کن')
U('TUHH — Information', v='⚠', n='مثل TUHH Data Science: تاریخ زمستان در دو منبع رسمی متفاوت است ⚠')
U('Trier — Data Science', v='✅',
  n='غیراروپایی تابستان ۱۵ دسامبر ۲۰۲۶ → ۱۵ ژانویه ۲۰۲۷ ✔؛ PORTA از اواسط دسامبر؛ €70 یک‌بار؛ انگیزه‌نامه؛ بعد از مهلت چیزی اضافه نمی‌شود. ⚠ معدل ≤۱٫۷ (۱٫۷۷→۱٫۷ مرزی)')
U('Hof — Software Eng.', v='✅', t='€3,300',
  n='❗ شهریه €3,300 در ترم (Graduate School). ≥۱ سال کار <b>تمام‌وقت و استخدامی</b> بعد از لیسانس (فریلنس/پاره‌وقت قبول نیست؛ Arbeitszeugnis با تاریخ‌ها)؛ آیلتس ۶٫۵ ✔؛ هزینه‌ی درخواست ندارد؛ مهلت ۳۰ نوامبر')
U('Hof — Applied Research', g='excl', st='❌ A1 رسمی',
  n='رسمی (۱۴ نوامبر): آلمانی A1 «با مدرک آزمون رسمی»؛ ≥۲۱۰ ECTS؛ ≤۲٫۵؛ کارآموزی ۱۸ هفته؛ کار علمی + مرور ادبیات؛ آزمون شفاهی')
U('Coburg — Autonomous Driving', g='excl', st='❌ VPD/ZAB تا ۲ دسامبر نمی‌رسد',
  n='غیراروپایی تابستان «May 16 → December 2»؛ VPD (۴–۶ هفته) یا ارزیابی ZAB لازم؛ €1,500/ترم؛ B2. برای زمستان زودتر اقدام کن')
U('Rostock — Computer Science International', v='✅', st='🟢 الان باز — تا ۳۰ نوامبر',
  n='✔ uni-assist؛ ۱ اکتبر → ۳۰ نوامبر؛ آیلتس ۷ (TOEFL 94) زیر ۲ سال ✔؛ معدل ≥۸۵٪ ✔ (~۸۷٪)؛ ≥۱۸ ریاضی، ≥۱۲ نظریه (تا ۹ جبرانی)؛ بدون محدودیت ظرفیت')
U('TU Dresden — Computer Science', v='⚠',
  n='uni-assist + پورتال آزمون صلاحیت (همان ایمیل)؛ تا ۳۰ نوامبر؛ ⚠ مدرک «in Computer Science» می‌خواهد (تو مهندسی کامپیوتر)؛ ۹۰ ECTS در ۶ حوزه؛ آیلتس ۷ و هیچ بخش زیر ۶ ✔؛ GRE «به‌شدت توصیه‌شده» → ریسک بالا')
U('Emden/Leer — Industrial Informatics', v='✅', r='uni-assist',
  n='uni-assist؛ غیراروپایی تا ۳۰ نوامبر؛ ۲۱۰ ECTS یا ۱۸۰ + برنامه‌ی تکمیلی ۳۰ ECTS؛ پایه‌ی سیستم‌های real-time و SE؛ ظرفیت محدود')
U('Deggendorf — HPC', v='✅', st='🟢 الان باز — تا ۱ دسامبر',
  n='Primuss؛ €60 یک‌بار (اگر قبلاً پرداخت کرده‌ای، تکرار نمی‌شود)؛ لیسانس CS/فیزیک/مهندسی ✔؛ آزمون ارزیابی؛ €500 هزینه‌ی سرویس هر ترم برای غیراروپایی')
U('TU Dortmund — Automation', g='excl', st='❌ GRE (رسمی)',
  n='v26 (۲۰ نوامبر): صفحه‌ی رسمی ETIT برای لیسانس غیر EU، GRE می‌خواهد (V≥۱۵۰، AW≥۳، Q≥۱۶۰؛ حداکثر ۱ سال قدمت)')
U('TU Dortmund — Data Science', g='open', st='🟢 الان باز (از ۱۵ نوامبر)', r='International Office → uni-assist؛ VPD لازم نیست',
  n='GRE ذکر نشده؛ ≥۴۴ CP (≥۱۶ CS، ≥۸ ریاضی، ≥۸ آمار ⚠ ریزنمرات)؛ B2؛ فرم خوداظهاری + آزمون خودسنجی؛ module handbook آماده کن')
U('Paderborn — Computer Science', st='❌ GRE/dMAT (مگر معافیت)', v='⚠',
  n='GRE (Q≥۱۵۷، AW≥۴) یا dMAT-CS (≥۵۰٪)؛ معافیت فقط اگر معدل تبدیل‌شده «کمتر از ۱٫۸» باشد — ۱٫۷۷ تو خیلی مرزی است. قبل از پرداخت به study-advice ایمیل بزن؛ مهلت ۳۰ نوامبر (مدارک تکمیلی تا ۱۵ ژانویه)')
U('Passau — Computer Science', v='✅',
  n='uni-assist (VPD معیار نیست)؛ ۱ نوامبر → ۱۵ دسامبر؛ ≥۱۱۰ ECTS کامپیوتر؛ معدل ≤۲٫۷ یا ۷۰٪ برتر ✔؛ <b>IAU باید در anabin H+ باشد ⚠</b>؛ خلاصه‌ی پایان‌نامه/پروژه؛ B2؛ ⚠ v26 آلمانی A1 هم نوشته — در صفحه چک کن')
U('Kiel — Computer Science', v='⚠',
  n='uni-assist؛ شهریه ندارد؛ ⚠ مهلت متناقض (۱۵ دسامبر یا ۱۵ ژانویه) — در My assist ببین؛ فقط لیسانس CS مشابه Kiel، مهندسی کامپیوتر ممکن است قبول نشود → قبل از پرداخت ایمیل بزن')
U('Marburg — Computer Science', v='⚠',
  n='uni-assist (My assist)؛ ⚠ مهلت ۳۱ دسامبر (یک منبع ثانویه ۲۶ فوریه)؛ Eignungsfeststellung؛ ≥۹۰ CP CS+ریاضی (≥۱۲ ریاضی، ≥۷۲ CS، ≥۹ نظریه)؛ معدل ≤۳٫۲ ✔؛ C1 (آیلتس ۷) یا DSH-2 + B1')
U('Oldenburg — CS', n='مهلت تابستان ۳۱ اکتبر گذشت. زمستان: غیراروپایی تا ۳۰ آوریل ۲۰۲۷ (توصیه ۱۵ ژانویه)؛ VPD جای درخواست را نمی‌گیرد؛ B2')
U('Aalen — ML', v='⚠', st='⚠ پیش‌نویس ذخیره شد — VPD لازم',
  n='فیلد «Certificate of recognition (VPD by Uni Assist)» اجباری است؛ VPD ۴–۸ هفته ← تا ۱۵ دسامبر عملاً نمی‌رسد')
for p in ('THI Ingolstadt — Artificial', 'THI — Sociotechnical', 'THI — AI Eng.', 'THI — Intelligent Aerial'):
    U(p, v='⚠', st='⚠ VPD تا ۵ دسامبر — عملاً دیر')
U('OTH Amberg', v='⚠', st='⚠ VPD لازم — عملاً دیر')

# ---------- new rows ----------
N('excl', '❌ GRE اجباری', 'Kassel — Computer Science', 'uni-assist', UA, 'ندارد', 'تا ۱۵ ژانویه', '۱ مارس → ۱۵ ژوئیه',
  'v26: برای لیسانس خارج از اتحادیه‌ی اروپا GRE (Q≥۱۶۰، V≥۱۵۵، AW≥۳٫۵)؛ معافیت ذکر نشده')
N('excl', '❌ GRE (مدرک غیربولونیا)', 'HAW Kiel — Computer Science / Data Science', 'uni-assist', UA, 'ندارد', '—', '—',
  'v26: برای مدرک خارج از منطقه‌ی بولونیا GRE لازم است (با Uni Kiel/CAU اشتباه نشود)')
N('excl', '❌ تدریس آلمانی', 'Hof — Computer Science (M.Sc.)', 'Primuss', '—', 'ندارد', '—', '—', 'عمدتاً آلمانی؛ آلمانی B2')
N('excl', '❌ آلمانی B2', 'Coburg — Visual Computing & AI', 'Primuss', '—', '—', '—', '—', 'تدریس آلمانی و انگلیسی؛ B2 آلمانی')
N('soon', '🔵 هنوز تاریخ ندارد', 'TU Dortmund — Informatik / Angewandte Informatik', 'uni-assist', UA, 'ندارد', '⚠ اعلام نشده', '⚠', 'v26: قرار است از تابستان ۲۰۲۷ انگلیسی شوند؛ مهلت هنوز اعلام نشده — صبر کن', v='⚠')
N('open', '🟢 الان باز — تا ۱ دسامبر', 'Deggendorf — Electrical Eng. & IT (EN)', 'مستقیم (Primuss، همان حساب)', '€60 (یک‌بار)', '€500 سرویس', '۱۵ اکتبر → <b>۱ دسامبر</b>', '—',
  'از جدول رسمی th-deg.de/en/apply (۱۴ نوامبر)؛ ⚠ شرایط ورود و تطابق با لیسانس مهندسی کامپیوتر را در صفحه‌ی برنامه چک کن', dl='2026-12-01', dlw='تابستان', v='⚠')
U('Augsburg — Data Science', g='open')
U('Augsburg — Mathematics', g='open')
U('Emden/Leer — Industrial Informatics', f=UA)
U('THWS Würzburg', v='⚠', st='⚠ VPD لازم — تا ۱۵ دسامبر عملاً دیر')
U('Hochschule Bielefeld', v='⚠', st='⚠ VPD لازم — تا ۱۵ ژانویه تنگ')
