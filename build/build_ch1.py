# -*- coding: utf-8 -*-
# Germany chances report (summer 2027 remainder + winter 2027/28) — v1, 28 Nov 2026
from build31 import CSS
from build_nl import T

EXTRA = '''
.ch{display:inline-block;padding:1px 6px;border-radius:8px;font-weight:700;font-size:8px;white-space:nowrap}
.c1{background:#d7f0dd;color:#145a2a}.c2{background:#fff1c2;color:#7a5a00}.c3{background:#ffe0cc;color:#8a3b00}.c0{background:#f6d3d8;color:#8a0018}
.urg{color:#b00020;font-weight:700}
'''
def C(n, t=None):
    lab = {1:'خوب', 2:'متوسط', 3:'کم', 0:'نمی‌شود'}[n]
    return '<span class="ch c%d">%s</span>' % (n, t or lab)

S = []; a = S.append
a('<h1>شانس پذیرش در آلمان — تابستان ۲۰۲۷ (باقی‌مانده) و زمستان ۲۰۲۷/۲۸</h1>')
a('<div class="sub">کسری جامعی · ۲۸ نوامبر ۲۰۲۶ (۷ آذر ۱۴۰۵) · ضمیمه‌ی راهنمای آلمان v32. '
  'اطلاعات از صفحه‌ی رسمی دانشگاه‌ها و پایگاه برنامه‌های بین‌المللی DAAD در همین روز (۲۰ تا ۲۳ نوامبر برای چند برنامه‌ی تابستان). '
  'صفحه‌های DAAD هنوز برچسب «۲۰۲۶/۲۷» دارند؛ تاریخ‌های زمستان معمولاً هر سال تکرار می‌شوند ولی ⚠ قبل از درخواست روی سایت خود دانشگاه چک کن. '
  'شانس‌ها تخمین من است، نه آمار رسمی (تقریباً هیچ دانشگاهی آمار قبولی منتشر نمی‌کند).</div>')

a('<div class="box warn"><b>چهار چیز که همه‌چیز را عوض می‌کند</b><ol>'
  '<li><b>GRE برای تو عملاً بسته است.</b> ETS از ۸ سپتامبر ۲۰۲۶ آزمون GRE و TOEFL را برای «ساکنان ایران» در ایران، در خانه و حتی در کشورهای دیگر متوقف کرده و تاریخ برگشتی اعلام نکرده. پس هر برنامه‌ای که GRE را <b>اجباری</b> می‌خواهد (TUM، KIT، RWTH، Bamberg، Bayreuth، Mannheim، Konstanz CIS، Saarland CS/DSAI/Cyber، Regensburg، HPI، Kassel، Kiel UAS …) از فهرست بیرون است.</li>'
  '<li><b>آیلتس تو ۲۷ مه ۲۰۲۷ دو ساله می‌شود</b> (آزمون ۲۷ مه ۲۰۲۵). بیشتر دانشگاه‌ها مدرک «حداکثر ۲ ساله» می‌خواهند و آزمون دوباره برای ساکن ایران سخت است (IELTS در ایران متوقف شده؛ فقط ارمنستان/ترکیه/قطر ⚠). پس <b>همه‌ی درخواست‌های زمستان را تا قبل از ۲۷ مه ۲۰۲۷ بفرست</b>، حتی برنامه‌هایی که مهلتشان ژوئن یا ژوئیه است.</li>'
  '<li><b>معدل آلمانی تو ۱٫۷۷ است</b> (فرمول باواریایی). این عدد درست کنار چند مرز است: Paderborn CS فقط با نمره‌ی «زیر ۱٫۸» GRE را معاف می‌کند؛ Trier DS حد ۱٫۷ دارد. اگر uni-assist کمی متفاوت حساب کند، ممکن است آن طرف مرز بیفتی.</li>'
  '<li><b>آزمون رسمی آلمانی در تهران هست.</b> مرکز ÖSD «اندیشه پارسیان» (osd@andisheparsian.com) برای <b>۱۰ دسامبر ۲۰۲۶</b> آزمون ZA1، ZA2 و ZB1 دارد. یک مدرک رسمی A1/A2 چند برنامه‌ی دیگر را برایت باز می‌کند (بخش ۵). ⚠ مهلت ثبت‌نام این نوبت احتمالاً گذشته؛ نوبت بعدی را بپرس.</li>'
  '</ol></div>')

a('<div class="box"><b>شانس را این‌طور سنجیدم:</b> '
  + C(1) + ' همه‌ی شرط‌های رسمی را داری و گزینش سخت نیست یا معیارها (معدل، درس‌های مرتبط، سابقه‌ی کار) به نفع توست. '
  + C(2) + ' شرط‌ها را داری ولی رتبه‌بندی/آزمون/مصاحبه هست، یا یک شرط مرزی است. '
  + C(3) + ' یک شرط مهم مرزی است (مثلاً ECTS جبر خطی، حد معدل) یا رقابت خیلی شدید است. '
  + C(0) + ' شرطی داری که نمی‌توانی برآورده کنی (GRE، آلمانی، شهریه‌ی بالا). '
  '<br><b>نقاط قوت تو:</b> معدل ۱٫۷۷؛ آیلتس ۷ (هیچ بخش زیر ۶)؛ حدود ۷۵ واحد درس کامپیوتر (سیستم‌عامل ۱۹٫۵، شبکه ۲۰، پایگاه داده، مهندسی نرم‌افزار، تست، روش‌های صوری ۲۰، نظریه‌ی زبان‌ها)؛ ۲۳ ماه کار فرانت‌اند؛ پروژه‌ی ML نمره‌ی ۲۰. '
  '<b>نقاط ضعف:</b> درس مستقل «جبر خطی» نداری (فقط نصف ریاضی ۲)؛ ریاضی کل حدود ۱۸ واحد؛ درس ML جدا نداری؛ برنامه‌نویسی پیشرفته ۱۱ و معماری کامپیوتر ۱۱٫۱۵؛ GRE نداری.</div>')

# ---------------- 1. Summer remainder ----------------
a('<h2>۱) تابستان ۲۰۲۷ — چیزهایی که هنوز می‌شود زد</h2>')
a('<p>فقط برنامه‌هایی که مهلتشان بعد از امروز است و هنوز نزده‌ای. سبد uni-assist (Rostock CSI، Paderborn CS و CE، Marburg، Passau، Kiel، TH OWL) و Darmstadt را جدا داری.</p>')
a(T(['مهلت', 'برنامه', 'شهر (ایالت)', 'مسیر / هزینه', 'شرط کلیدی در مقایسه با تو', 'شانس'], [
 ['<span class="urg">۳۰ نوامبر</span>', 'TU Dresden — Computer Science', 'Dresden (ساکسونی)', 'uni-assist + پورتال Eignungsfeststellung، بدون شهریه', 'ECTS در ۵ حوزه را داری؛ IELTS ۷ و هر بخش ≥۶ ✔؛ GRE «اکیداً توصیه» (نداری). ⚠ قبلاً به‌خاطر شک درباره‌ی شروع تابستان حذفش کردی؛ صفحه‌ی رسمی پنجره‌ی ۱ اکتبر–۳۰ نوامبر را برای «ترم تابستان بعدی» نشان می‌دهد. اگر هنوز پرداخت نکرده‌ای، نگه داشتنش فقط €۳۰ است.', C(2)],
 ['<span class="urg">۱ دسامبر</span>', 'TUHH — Computer Science (precheck)', 'Hamburg', 'TUNE، بدون شهریه', 'precheck معدل تا ۱ دسامبر، درخواست تا ۱۵ ژانویه', C(2)],
 ['<span class="urg">۵ دسامبر (VPD)</span>', 'THI — AI / AI Eng. Autonomous Systems / Cybersecurity', 'Ingolstadt (بایرن)', 'VPD + PRIMUSS، €۱٬۲۰۰ در ترم', 'VPD تا ۵ دسامبر باید برسد — عملاً دیر است', C(3)],
 ['۱۵ دسامبر', 'Passau — AI Engineering', 'Passau (بایرن)', 'uni-assist (+€۳۰)', 'مثل Passau CS: ≥۳۵ ECTS ریاضی + نظری (تو مرزی) و ≥۴۰ CS ✔؛ معدل ≤۲٫۷ ✔', C(2)],
 ['۱۵ دسامبر', 'Osnabrück — Cognitive Science', 'Osnabrück (نیدرزاکسن)', 'uni-assist (+€۳۰)', 'میان‌رشته‌ای؛ تناسب متوسط', C(2)],
 ['۱۵ دسامبر', 'THWS — Artificial Intelligence', 'Würzburg (بایرن)', 'VPD + پورتال THWS', 'VPD باید قبل از مهلت برسد — خیلی تنگ', C(3)],
 ['۳۱ دسامبر', 'Marburg — Data Science / Business Informatics', 'Marburg (هسن)', 'uni-assist (+€۳۰)', 'IELTS ۷ (C1) ✔؛ DS ریاضی/آمار قوی می‌خواهد', C(2)],
 ['۱۵ ژانویه', '<b>Chemnitz — Web Engineering</b>', 'Chemnitz (ساکسونی)', 'EduApplication، بدون شهریه', 'IELTS ۵٫۵؛ لیسانس CS؛ <b>بهترین تناسب با کار فرانت‌اند تو</b>. ⚠ مدارک باید تا مهلت برسد.', C(1)],
 ['۱۵ ژانویه', '<b>BTU — Artificial Intelligence</b>', 'Cottbus (براندنبورگ)', 'uni-assist (+€۳۰)، بدون شهریه', 'IELTS ۶؛ ECTS و معدل ذکر نشده', C(1)],
 ['۱۵ ژانویه', '<b>Weimar — CS for Digital Media / HCI / Digital Engineering</b>', 'Weimar (تورینگن)', 'uni-assist (+€۳۰ هر کدام)', 'IELTS ۶٫۵ ✔؛ لیسانس CS/CE قبول؛ HCI با سابقه‌ی UI تو جور است', C(1)],
 ['۱۵ ژانویه', 'Saarland — Media Informatics / Systems Engineering', 'Saarbrücken (زارلند)', 'مستقیم (SIM)', 'IELTS ۷ (C1) ✔؛ دو توصیه‌نامه', C(2)],
 ['۱۵ ژانویه', 'TU Darmstadt — CS', 'Darmstadt (هسن)', 'مستقیم + پاکت کاغذی', 'تصمیمش را گرفته‌ای؛ احتمال آزمون حضوری مارس', C(2)],
 ['۱۵ ژانویه', 'TU Dortmund — Data Science (💾 ذخیره)', 'Dortmund (NRW)', 'uni-assist (+€۳۰)', 'معدل ≤۲٫۷ ✔؛ <b>پذیرش فقط بر اساس گزارش ۱۰ صفحه‌ای یک پروژه‌ی آماری</b>', C(2)],
 ['۱۵ ژانویه', 'Anhalt — Electrical & Computer Eng.', 'Köthen (زاکسن-آنهالت)', 'uni-assist (+€۳۰)', 'کاربردی؛ تناسب CE خوب', C(1)],
 ['۱۵ ژانویه', 'HSBI — Data Science Research Master', 'Gütersloh/Bielefeld (NRW)', 'uni-assist یا HSBI', 'معدل ≤۲٫۵ ✔؛ IELTS ۵٫۵؛ ویدئوی ۲ دقیقه‌ای + مصاحبه', C(1)],
 ['۱۵ ژانویه', 'Trier — Data Science', 'Trier (راینلاند-فالتس)', 'مستقیم (PORTA)', '<b>حد معدل ۱٫۷</b>؛ ۱٫۸–۲٫۲ موردی؛ تو ۱٫۷۷ ⇒ بستگی به محاسبه دارد', C(3)],
 ['۱۵ ژانویه', 'RUB — EEIT Communication Systems', 'Bochum (NRW)', 'hio (همان حساب)', '۲۵ CP ریاضی و ۵۰ CP IT/برق — مرزی', C(3)],
 ['۱۵ ژانویه', 'Heilbronn SEM / Applied AI · Albstadt Industrial AI', 'بادن-وورتمبرگ', '€۱٬۵۰۰ در ترم', 'شرط‌ها را داری؛ فقط شهریه', C(2)],
 ['۱۵ ژانویه', 'Konstanz — COSIB', 'Konstanz (BW)', 'ZEuS، €۲٬۶۵۰ در ترم', 'شهریه بالا', C(3)],
 ['۱ مارس', 'Augsburg — Data Science / Math & CS', 'Augsburg (بایرن)', 'VIBS، بدون هزینه', '<b>جبر خطی ≥۵ ECTS</b> (تو کم)؛ پذیرش یک‌ترمه', C(3)],
], None))

# ---------------- 2. Winter ----------------
a('<h2 class="pb">۲) زمستان ۲۰۲۷/۲۸ (شروع اکتبر ۲۰۲۷) — به ترتیب مهلت</h2>')
a('<p>برای غیراروپایی‌ها. ستون «مهلت» تاریخ دانشگاه است؛ <b>تاریخ عملی تو ۲۷ مه ۲۰۲۷ است</b> (انقضای آیلتس) مگر خلافش را از دانشگاه بگیری. همه بدون شهریه مگر نوشته شده باشد.</p>')
G = '##'
a(T(['مهلت (غیراروپایی)', 'برنامه', 'شهر (ایالت)', 'مسیر', 'شرط کلیدی در مقایسه با تو', 'شانس'], [
 [G, '<b>باز است یا تا ژانویه/فوریه بسته می‌شود</b>'],
 ['<span class="urg">۱۵ نوامبر ← ۱۵ ژانویه ۲۰۲۷</span>', '<b>Stuttgart — INFOTECH</b>', 'Stuttgart (BW)', 'C@MPUS (همان حساب CS)؛ €۱٬۵۰۰ در ترم', 'لیسانس CS/CE/برق/IT؛ گزینش موسسه‌ای. Stuttgart CS را قبلاً برای همین ترم زده‌ای', C(2)],
 ['<span class="urg">۱۵ ژانویه ۲۰۲۷</span>', 'Stuttgart — Electrical Engineering (EN)', 'Stuttgart (BW)', 'C@MPUS؛ €۱٬۵۰۰', 'لیسانس برق؛ تو CE ⇒ مرزی', C(3)],
 ['<span class="urg">۱۵ نوامبر ← ۱۵ فوریه ۲۰۲۷</span>', '<b>H-BRS — Autonomous Systems</b>', 'Sankt Augustin، کنار Bonn (NRW)', 'فقط uni-assist', 'از زمستان ۲۰۲۷ <b>حداقل معدل حذف شد</b>؛ لیسانس مهندسی با ≥۵۰٪ CS قبول (شاید تا ۱۲ ECTS تکلیف اضافه)؛ IELTS ۶٫۵ ✔؛ ظرفیت محدود', C(2)],
 ['۱۵ فوریه ۲۰۲۷', 'H-BRS — Game Technologies', 'Sankt Augustin (NRW)', 'uni-assist', 'تناسب متوسط', C(2)],
 [G, '<b>مارس ۲۰۲۷</b>'],
 ['۱ مارس', '<b>TUHH — Data Science</b> / <b>Information & Communication Systems</b>', 'Hamburg', 'TUNE', 'IELTS ۶٫۵ ✔؛ «عملکرد تحصیلی خیلی خوب»؛ DS ریاضی و CS قوی می‌خواهد', C(2)],
 ['۱ فوریه ← ۱۵ مارس', '<b>Bremen — AI & Intelligent Systems</b>', 'Bremen', 'MOIN', '۹۰ CP کامپیوتر ✔؛ رتبه: معدل ۵۰٪ + تخصص (AI/ML) ۴۰٪ + انگیزه‌نامه ۱۰٪', C(2)],
 ['۱ فوریه ← ۱۵ مارس', 'TU Braunschweig — Data Science', 'Braunschweig (نیدرزاکسن)', 'پورتال TU BS', '≥۲۵ ECTS ریاضی پایه (تو حدود ۳۰، مرزی)', C(2)],
 ['۱۵ مارس ⚠', 'Heidelberg — Data & Computer Science', 'Heidelberg (BW)', 'heiCO؛ €۱٬۵۰۰ در ترم', '<b>پذیرش محدود نیست</b>: هر کس شرط‌ها را داشته باشد قبول است (۳۲ CP CS با زیرحوزه‌ها ✔؛ IELTS ۶٫۵ ✔). ⚠ مهلت ترم اول را از سایت چک کن', C(1)],
 ['۱۵ فوریه ← ۳۱ مارس', 'Hamburg — Intelligent Adaptive Systems / Data Science & AI', 'Hamburg', 'STiNE', 'IAS: ≥۶۰ ECTS CS ✔؛ <b>فقط حدود ۵٪ برتر پذیرفته می‌شوند</b>', C(3)],
 ['۳۱ مارس', 'Nordhausen — CE for IoT Systems', 'Nordhausen (تورینگن)', 'uni-assist', 'کاربردی؛ تناسب مستقیم با CE', C(1)],
 ['۳۱ مارس', 'h_da — EEIT International', 'Darmstadt (هسن)', 'مستقیم', 'کاربردی؛ برق/IT', C(2)],
 ['۳۱ مارس (غیراروپایی)', 'Offenburg — Enterprise & IT Security', 'Offenburg (BW)', 'HISinOne؛ €۱٬۵۰۰', 'امنیت؛ تناسب متوسط', C(2)],
 ['۳۱ مارس', 'Wuppertal — Computer Simulation in Science', 'Wuppertal (NRW)', 'uni-assist', 'ریاضی/شبیه‌سازی سنگین', C(3)],
 [G, '<b>آوریل ۲۰۲۷</b>'],
 ['تا ۱۵ آوریل', 'Göttingen — Applied CS', 'Göttingen (نیدرزاکسن)', 'مستقیم', '≥۶۰ CS + ≥۱۵ ریاضی ✔؛ <b>آزمون آنلاین + مصاحبه</b> (تجربه‌ی اکتبر را داری)', C(2)],
 ['تا ۱۵ آوریل', 'Frankfurt UAS — Information Technology / HIS', 'Frankfurt (هسن)', 'uni-assist', 'کاربردی؛ IELTS ۵٫۵', C(2)],
 ['۱ ژانویه ← ۳۰ آوریل', '<b>Siegen — Computer Science</b> / HCI', 'Siegen (NRW)', 'UNISONO، <b>هیچ هزینه‌ای</b>', 'prerequisite sheet؛ آزمون آنلاین کوتاه + مصاحبه؛ تمرکز embedded / نرم‌افزار / visual computing', C(1)],
 ['۱۵ مارس ← ۳۰ آوریل', '<b>Oldenburg — Data Science & ML</b>', 'Oldenburg (نیدرزاکسن)', 'uni-assist', '۲۰ CP ریاضی (آمار ✔، آنالیز ✔) + ۱۰ CS ✔؛ رتبه: معدل + تجربه‌ی DS (پروژه‌ی ML تو)؛ IELTS ۵٫۵', C(1)],
 ['تا ۳۰ آوریل', 'RPTU — Computer Science', 'Kaiserslautern (RLP)', 'applymsc، €۶۰ یک‌باره', 'IELTS ۶٫۵ ✔؛ GRE توصیه (نداری)', C(2)],
 ['تا ۳۰ آوریل', 'Tübingen — Machine Learning', 'Tübingen (BW)', 'ALMA؛ €۱٬۵۰۰', '≥۲۷ ECTS ریاضی شامل <b>جبر خطی</b> و آنالیز و عددی/آمار (تو کم)؛ رقابتی', C(3)],
 [G, '<b>مه ۲۰۲۷ (همه را قبل از ۲۷ مه بفرست)</b>'],
 ['۱ آوریل ← ۳۱ مه', '<b>TU Dresden — Computer Science</b>', 'Dresden (ساکسونی)', 'uni-assist + پورتال Eignungsfeststellung', '۵ حوزه‌ی ECTS ✔؛ <b>IELTS ۷ و هر بخش ≥۶ — دقیقاً داری</b>؛ تصمیم فقط با مدارک (بدون آزمون)؛ GRE توصیه', C(2)],
 ['۱ آوریل ← ۳۱ مه', '<b>Rostock — CS International</b>', 'Rostock (مکلنبورگ)', 'uni-assist', '<b>≥۸۵٪ معدل</b> (تو ۸۷٪ ✔)؛ ۱۸ ریاضی + ۱۲ نظری ✔؛ IELTS ۷ ✔', C(1)],
 ['تا ۳۱ مه', '<b>Paderborn — Computer Science</b>', 'Paderborn (NRW)', 'uni-assist', '۲۰ SE + ۲۰ نظری + ۱۵ فنی + ۱۵ ریاضی ✔؛ <b>GRE فقط با نمره‌ی زیر ۱٫۸ معاف</b> (تو ۱٫۷۷)', C(2)],
 ['تا ۳۱ مه', 'Paderborn — Computer Engineering', 'Paderborn (NRW)', 'uni-assist', '≥۳۰ برق (تو مرزی)؛ معافیت GRE فقط «CGPA خیلی خوب» (عدد ندارد)', C(3)],
 ['۱ آوریل ← ۳۱ مه', '<b>Passau — CS / AI Engineering</b>', 'Passau (بایرن)', 'uni-assist یا مستقیم', 'معدل ≤۲٫۷ ✔؛ ≥۴۰ CS ✔؛ ≥۳۵ ریاضی+نظری (مرزی)؛ IELTS ۵٫۵؛ A1 آلمانی (B1 دوره داری)', C(1)],
 ['۱ مارس ← ۳۱ مه', 'UTN — AI & Robotics / Human & AI', 'Nürnberg (بایرن)', 'uni-assist یا UTN', '≥۲۴ CS ✔؛ <b>≥۱۸ آنالیز + جبر خطی</b> (مرزی)؛ فرایند ارزیابی صلاحیت', C(2)],
 ['۴ ژانویه ← ۱۵ مه', 'TU Dortmund — Data Science', 'Dortmund (NRW)', 'uni-assist', 'گزارش پروژه‌ی آماری تعیین‌کننده است', C(2)],
 ['۱۵ آوریل ← ۱۵ مه', 'Magdeburg — DKE / Visual Computing / Digital Engineering', 'Magdeburg (زاکسن-آنهالت)', 'uni-assist', 'IELTS ۷ ✔؛ VC: معدل ≤۲٫۵ + توصیه‌نامه + انگیزه‌نامه', C(2)],
 ['۱ آوریل ← ۱۵ مه', 'Ulm — Cognitive Systems', 'Ulm (BW)', 'پورتال Ulm؛ €۱٬۵۰۰', 'میان‌رشته‌ای', C(3)],
 ['اواسط آوریل ← پایان مه', 'FU Berlin — Data Science', 'Berlin', 'uni-assist', 'IELTS ۷ ✔؛ ریاضی/CS پایه ✔؛ برلین پرمتقاضی', C(2)],
 ['۱–۳۱ مه', 'Fulda — Data Science', 'Fulda (هسن)', 'uni-assist', '<b>آلمانی A2 رسمی لازم</b> (ÖSD)', C(3)],
 ['۱ مه ← ۱ ژوئن', '<b>TH Bingen — Computer Science</b>', 'Bingen (RLP)', 'uni-assist', 'کاربردی؛ نمره «gut» ✔؛ ۲۱۰ ECTS (لیسانس ۴ساله ✔)؛ IELTS ۶٫۵ ✔', C(1)],
 ['تا ۳۱ مه', 'Trier — Data Science', 'Trier (RLP)', 'PORTA', 'حد معدل ۱٫۷', C(3)],
 ['تا ۳۰ مه', 'Emden/Leer — Industrial Informatics', 'Emden (نیدرزاکسن)', 'uni-assist یا eCampus', 'کاربردی؛ سیستم‌های بی‌درنگ و برنامه‌نویسی صنعتی', C(2)],
 ['۱۵ آوریل ← ۳۱ مه', 'Freiburg — CS', 'Freiburg (BW)', 'HISinOne؛ €۱٬۵۰۰', 'IELTS ۷ ✔؛ نظریه‌ی قوی (نظریه‌ی زبان ۱۶٫۵، روش‌های صوری ۲۰ ✔)؛ تابستان را زده‌ای', C(2)],
 ['۱ آوریل ← ۳۱ مه', 'TU Dresden — Computational Modelling & Simulation', 'Dresden', '⚠', 'ریاضی سنگین', C(3)],
 [G, '<b>ژوئن–ژوئیه ۲۰۲۷ (مهلت دیر، ولی تو باید زودتر بفرستی)</b>'],
 ['تا ۱۵ ژوئن', '<b>Kiel — Computer Science</b>', 'Kiel (شلسویگ-هولشتاین)', 'uni-assist', 'لیسانس CS «قابل مقایسه»؛ اگر نیمه‌منطبق باشی آزمون آنلاین؛ IELTS ۵٫۵', C(2)],
 ['تا ۱۵ ژوئن', '<b>Koblenz — Web & Data Science</b>', 'Koblenz (RLP)', 'uni-assist', 'معدل ≤۲٫۵ ✔؛ IELTS ۵٫۵؛ تناسب خوب با وب', C(1)],
 ['۱ مارس ← ۱۵ ژوئن', 'FH Dortmund — Embedded Systems Eng.', 'Dortmund (NRW)', 'go-study-europe precheck', 'معدل ≤۲٫۵ ✔؛ IELTS ۶٫۵ ✔؛ پایان‌نامه ✔؛ تخصص embedded لازم', C(2)],
 ['۱ آوریل ← ۳۰ ژوئن', '<b>Hildesheim — Data Analytics / Software Eng.</b>', 'Hildesheim (نیدرزاکسن)', 'ismll', 'رتبه: معدل ۵۳٪ + درس‌های مرتبط ۳۵٪؛ IELTS ۶؛ تابستان را زده‌ای', C(1)],
 ['۱ مه ← ۳۰ ژوئن', 'Marburg — CS / Data Science', 'Marburg (هسن)', 'uni-assist یا مستقیم', 'IELTS ۷ ✔؛ دانش نظری؛ تابستان را زده‌ای', C(2)],
 ['۱ مارس ← ۱۵ ژوئیه', '<b>BTU — Artificial Intelligence</b> / Cyber Security', 'Cottbus (براندنبورگ)', 'uni-assist', 'IELTS ۶؛ شرط ECTS ذکر نشده', C(1)],
 ['۱ آوریل ← ۱۵ ژوئیه', '<b>Weimar — CSDM / HCI / Digital Eng.</b>', 'Weimar (تورینگن)', 'uni-assist', 'IELTS ۶٫۵ ✔', C(1)],
 ['تا ۱۵ ژوئیه', '<b>Chemnitz — Web Eng.</b> / Automotive SE', 'Chemnitz (ساکسونی)', 'EduApplication', 'IELTS ۵٫۵؛ تناسب عالی با وب', C(1)],
 ['۱ ژوئن ← ۱۵ ژوئیه', 'Bielefeld — Intelligent Interactive Systems', 'Bielefeld (NRW)', 'campus.uni-bielefeld', 'معدل ≤۲٫۷ ✔؛ ۳۰ CS + ۱۰ ریاضی ✔ + <b>۳۰ «روش‌های فنی سیستم‌های هوشمند»</b> (مرزی)', C(2)],
 ['۱ ژوئن ← ۱۵ ژوئیه', '<b>HSBI — Data Science Research Master</b>', 'Gütersloh (NRW)', 'uni-assist یا HSBI', 'معدل ≤۲٫۵ ✔؛ ویدئو + مصاحبه', C(1)],
 ['تا ۱۵ ژوئیه', 'Saarland — Media Informatics', 'Saarbrücken', 'مستقیم', 'IELTS ۷ ✔؛ ۲ توصیه‌نامه', C(2)],
 ['۱ ژوئن ← ۱۵ ژوئیه', 'TU Darmstadt — CS', 'Darmstadt (هسن)', 'مستقیم + پاکت', 'اگر تابستان نشد', C(2)],
 ['۱ مه ← ۱۵ ژوئیه', 'KU Eichstätt-Ingolstadt — Data Science', 'Ingolstadt (بایرن)', 'uni-assist یا KU', '<b>یک سال جبر خطی + یک سال آنالیز با اثبات</b>؛ GRE ریاضی توصیه', C(3)],
 ['تا ۳۱ ژوئیه', 'Duisburg-Essen — ESE / Communications Eng.', 'Duisburg (NRW)', 'پورتال UDE', 'تابستان را زده‌ای', C(2)],
 ['تا ۱ سپتامبر', 'Augsburg — Data Science / Math & CS', 'Augsburg (بایرن)', 'VIBS', 'جبر خطی ≥۵ ECTS (کم)', C(3)],
], None))

# ---------------- 3. Best picks ----------------
a('<h2 class="pb">۳) بهترین گزینه‌ها بر اساس رشته</h2>')
a(T(['رشته', 'بهترین شانس', 'شانس متوسط', 'رویایی ولی سخت'], [
 ['<b>علوم کامپیوتر عمومی</b>', 'Rostock CSI · Passau CS · Siegen CS · TH Bingen CS · Heidelberg DCS (€۱٬۵۰۰)', 'TU Dresden CS · Paderborn CS · Kiel CS · Göttingen ACS · Darmstadt · Freiburg · RPTU · Bonn', 'Hamburg IAS (۵٪)'],
 ['<b>وب و مهندسی نرم‌افزار</b> (نزدیک‌ترین به کار تو)', 'Chemnitz Web Eng. · Koblenz Web & DS · Hildesheim SE · Weimar CSDM', 'Stuttgart INFOTECH · Emden Industrial Informatics · Chemnitz ASE', '—'],
 ['<b>داده و هوش مصنوعی</b>', 'Oldenburg DS&ML · BTU AI · HSBI DS · Hildesheim DA', 'Bremen AIIS · TUHH DS · TU Braunschweig DS · TU Dortmund DS · FU Berlin DS · UTN', 'Tübingen ML · KU Eichstätt DS · Trier DS · Augsburg DS'],
 ['<b>مهندسی کامپیوتر و embedded</b>', 'Nordhausen CE-IoT · Anhalt ECE', 'Paderborn CE · FH Dortmund ESE · TUHH ICS · H-BRS AS · Duisburg ESE', 'Saarland Embedded Systems (GRE/GATE در فهرست مدارک)'],
 ['<b>HCI و رسانه</b>', 'Weimar HCI · Siegen HCI', 'Saarland Media Informatics · Magdeburg Visual Computing', '—'],
], None))
a('<div class="box good"><b>بر اساس شهر و ایالت:</b> بیشترین گزینه‌های خوب در <b>شرق</b> (Chemnitz، Dresden، Weimar، Cottbus، Rostock، Magdeburg، Nordhausen، Köthen) است. رقابت آنجا کمتر است، بیشتر انگلیسی‌محور است و هزینه‌ی زندگی هم پایین‌تر است. '
  '<b>NRW</b> (Siegen، Paderborn، Bochum، Dortmund، Bielefeld، Gütersloh، Sankt Augustin) هم گزینه‌ی زیاد و بدون شهریه دارد. '
  '<b>بادن-وورتمبرگ</b> (Stuttgart، Heidelberg، Freiburg، Tübingen، Ulm، Heilbronn) برای غیراروپایی‌ها €۱٬۵۰۰ در ترم می‌گیرد. '
  '<b>بایرن</b> بیشتر VPD یا GRE یا شهریه دارد؛ استثناها Passau و UTN هستند.</div>')

# ---------------- 4. Closed ----------------
a('<h2>۴) برنامه‌هایی که فعلاً برایت بسته‌اند</h2>')
a(T(['دلیل', 'برنامه‌ها'], [
 ['<b>GRE اجباری</b> (برای ساکن ایران در دسترس نیست)', 'TUM (همه)، KIT CS، RWTH (SSE، DS، CE، HCIS)، Bamberg ISSS، Bayreuth CS، Mannheim DS، Konstanz CIS، Saarland CS / DSAI / Cybersecurity، Regensburg (CS، DS، HCAI، MI)، HPI Potsdam، Potsdam CS، Kassel CS، Kiel UAS، TU Dortmund Automation & Robotics، FAU AI، Neu-Ulm AIDA، Bonn Mobile Robotics، Kiel CAU EE'],
 ['<b>GRE یا TestAS</b>', 'Rhine-Waal Information Eng. & CS (TestAS ≥۱۰۰ — ⚠ دسترسی TestAS برای ایران را از g.a.s.t. بپرس)'],
 ['<b>آلمانی C1/B2</b>', 'Hannover CS/CE، Augsburg CS، Hamburg Informatik، Leipzig DS، HTWG Konstanz، FU Berlin CS، Goethe Frankfurt، Uni Bremen CS، HAW Hamburg CS، Duisburg-Essen CE، Ulm CCE، RPTU ECE، Frankfurt UAS General CS، Coburg VCAI، Hof CS'],
 ['<b>شهریه‌ی بالا</b>', 'HTW Berlin، Emden Business Informatics/BIDA (€۵٬۹۸۰)، TU Braunschweig CoDaS (€۸٬۰۰۰)، دانشگاه‌های خصوصی'],
 ['<b>رشته‌ی لیسانس دیگر</b>', 'Mannheim/HU/Hohenheim Business، Stralsund، Hannover Mechatronics'],
], None))

# ---------------- 5. ÖSD ----------------
a('<h2>۵) اگر مدرک رسمی آلمانی (ÖSD) بگیری، این‌ها باز می‌شوند</h2>')
a('<div class="box">تو دوره‌ی B1 را گذرانده‌ای ولی «گواهی دوره» را بیشتر دانشگاه‌ها قبول نمی‌کنند؛ آزمون رسمی (Goethe، telc، ÖSD) می‌خواهند. ÖSD در تهران برگزار می‌شود. پیشنهاد: <b>ZA2 یا ZB1</b> در اولین نوبت ممکن.</div>')
a(T(['سطح لازم', 'برنامه', 'مهلت زمستان', 'شرط‌های دیگر'], [
 ['A1 رسمی', 'Fulda — Global Software Development', '⚠ (تابستان: ۱ دسامبر)', 'معدل ≤۲٫۵ ✔؛ ۱۸۰ ECTS ⇒ +۳۰ ECTS'],
 ['A1 رسمی', 'Hof — Applied Research in CS', '۱۵ آوریل ← ۳۱ مه', '≥۲۱۰ ECTS ✔؛ ≤۲٫۵ ✔؛ کارآموزی ۱۸ هفته (⚠ تو ۱ واحد)'],
 ['A1 رسمی', 'Chemnitz — Embedded Systems / ICS / Automation, Robotics & Control', 'تا ۱۵ ژوئیه', 'تناسب CE خوب'],
 ['A2 رسمی', 'Fulda — Data Science', '۱–۳۱ مه', 'B2 انگلیسی ✔'],
 ['A2 رسمی', 'TH Rosenheim — Engineering Sciences (EEIT)', '⚠', '—'],
 ['A1/A2 رسمی', 'Bremerhaven — Embedded Systems Design', 'فقط تابستان (۳۱ دسامبر)', '—'],
], None))

# ---------------- 6. Plan ----------------
a('<h2 class="pb">۶) برنامه‌ی زمانی پیشنهادی</h2>')
a('<ol class="big">'
  '<li><b>تا ۳۰ نوامبر:</b> سبد uni-assist را پرداخت و ارسال کن. اگر هنوز پرداخت نکرده‌ای، درباره‌ی نگه داشتن TU Dresden تصمیم بگیر (+€۳۰ و پورتال Eignungsfeststellung تا همان روز).</li>'
  '<li><b>۱ دسامبر:</b> precheck TUHH؛ باز شدن پورتال Darmstadt.</li>'
  '<li><b>دسامبر:</b> از مرکز ÖSD تهران نوبت بعدی ZA2/ZB1 را بپرس و ثبت‌نام کن.</li>'
  '<li><b>تا ۱۵ دسامبر:</b> (اختیاری، €۳۰ هر کدام) Passau AIE در uni-assist.</li>'
  '<li><b>تا ۱۵ ژانویه:</b> تابستان: Chemnitz Web Eng.، BTU AI، Weimar CSDM/HCI، Anhalt ECE، HSBI DS، Darmstadt. <b>زمستان: Stuttgart INFOTECH</b> (همان حساب C@MPUS).</li>'
  '<li><b>تا ۱۵ فوریه:</b> H-BRS Autonomous Systems (uni-assist، زمستان).</li>'
  '<li><b>تا ۱ مارس:</b> TUHH DS و ICS. <b>تا ۱۵ مارس:</b> Bremen AIIS، TU Braunschweig DS، Heidelberg DCS. <b>تا ۳۱ مارس:</b> Nordhausen، Hamburg (اختیاری).</li>'
  '<li><b>۱ تا ۳۰ آوریل:</b> Siegen CS، Oldenburg DS&ML، RPTU CS، Göttingen ACS. <b>همان اول آوریل</b> که uni-assist برای زمستان باز شد: TU Dresden CS، Rostock CSI، Paderborn CS، Passau CS، Magdeburg، Kiel، Koblenz، BTU، Weimar، Chemnitz و TH Bingen را یکجا بفرست.</li>'
  '<li><b>قبل از ۲۷ مه ۲۰۲۷:</b> همه‌ی درخواست‌های زمستان ارسال شده باشد (انقضای آیلتس).</li>'
  '<li><b>بعد از جواب‌های تابستان (فوریه–مارس):</b> اگر پذیرش تابستان گرفتی، بخش زمستان را کوچک کن.</li>'
  '</ol>')

# ---------------- 7. Uncertainties ----------------
a('<h2>۷) چیزهایی که هنوز مطمئن نیستیم</h2><ul>'
  '<li>⚠ تاریخ‌های زمستان ۲۰۲۷/۲۸ بیشتر از صفحه‌هایی است که برچسب ۲۰۲۶/۲۷ دارند یا قاعده‌ی تکراری می‌گویند. هر دانشگاه ممکن است تغییر دهد.</li>'
  '<li>⚠ اینکه هر دانشگاه آیلتس را «حداکثر ۲ ساله در زمان درخواست» یا «در زمان ثبت‌نام» می‌خواهد، در بیشتر صفحه‌ها نیامده. برای مهلت‌های بعد از ۲۷ مه از خود دانشگاه بپرس.</li>'
  '<li>⚠ تبدیل ۱۴۴ واحد ایران به ECTS را هر دانشگاه خودش حساب می‌کند (معمولاً لیسانس ۴ساله ≈ ۲۴۰ ECTS). شرط‌های مرزی من (ریاضی، جبر خطی، برق) با فرض «۱ واحد ≈ ۱٫۵ تا ۱٫۷ ECTS» است.</li>'
  '<li>⚠ شرکت در آزمون IELTS خارج از ایران برای ساکن ایران: منابع با هم نمی‌خوانند (بعضی می‌گویند British Council فقط مقیم قانونی خارج را می‌پذیرد، بعضی ارمنستان/ترکیه با IDP را ممکن می‌دانند).</li>'
  '<li>⚠ دسترسی TestAS (g.a.s.t.) برای ساکن ایران بررسی نشد؛ dMAT فعلاً فقط برای هند است.</li>'
  '<li>⚠ مهلت ترم اول Heidelberg DCS، Marburg، TH OWL، Frankfurt UAS HIS و BTU Cyber Security در صفحه‌ها نیامد.</li>'
  '</ul>')

# ---------------- Sources ----------------
a('<h2>منابع</h2><ol style="font-size:8.5px;line-height:1.7">'
  '<li>ETS — Iran testing update (ets.org/iran-testing-update.html)؛ RFE/RL (rferl.org/a/iran-english-test-abroad-sanctions/33893817.html)؛ bandladder.com (وضعیت IELTS در ایران، ۲۵ اکتبر ۲۰۲۶)</li>'
  '<li>ÖSD — Exam centres (osd.at/en/exam-centres)؛ ÖKF Teheran (bmeia.gv.at/kf-teheran)</li>'
  '<li>DAAD International Programmes — جست‌وجو و صفحه‌های جزئیات: 4591, 9040, 3747, 4700, 7606, 3736, 10354, 7618, 6148, 9042, 4238, 4092, 5616, 5625, 7784, 4429, 8951, 4634, 9906, 9646, 9894, 4384, 6937, 4655, 8322, 4785, 3923, 7670, 4775, 4513, 8324, 9725, 3632, 3629, 7066, 5351, 3799, 3903, 10360, 8265, 5561, 8353, 5634, 8953</li>'
  '<li>Siegen (uni-siegen.de/node/6003)؛ Hamburg IAS (master-intelligent-adaptive-systems.com)؛ Uni Hamburg CampusCenter (fristen-termine)؛ Bremen AIIS (صفحه‌ی برنامه + خلاصه‌ی شرایط ۰۷/۲۰۲۳)؛ Heidelberg (informatik.uni-heidelberg.de/studium/master/dacs/application، mathinf.uni-heidelberg.de)</li>'
  '<li>Passau (uni-passau.de/en/msc-computer-science)؛ Stuttgart INFOTECH (uni-stuttgart.de)؛ TU Braunschweig DS (tu-braunschweig.de/en/data-science/prospectivestudents)؛ TU Dresden CS admission (tu-dresden.de/ing/informatik/.../m-sc-computer-science/admission)</li>'
  '<li>Fintiba — dMAT (fintiba.com/germany/visa/dmat-exam)؛ راهنمای آلمان v32 (بررسی‌های ۷ تا ۲۳ نوامبر ۲۰۲۶)</li>'
  '</ol>')

html = '<!doctype html><html lang="fa" dir="rtl"><head><meta charset="utf-8"><style>' + CSS + EXTRA + '</style></head><body>' + ''.join(S) + '</body></html>'
open('ch1.html', 'w').write(html); print('ok')
