# -*- coding: utf-8 -*-
# Netherlands MSc guide for Kasra — v1 (23 Nov 2026)
from build31 import CSS, fa  # same look as the Germany guide

def T(head, rows, cls=None):
    h = ''.join('<th>%s</th>' % x for x in head)
    b = ''
    for i, r in enumerate(rows):
        c = (cls[i] if cls else '')
        if r and r[0] == '##':
            b += '<tr class="grp"><td colspan="%d">%s</td></tr>' % (len(head), r[1]); continue
        b += '<tr class="%s">%s</tr>' % (c, ''.join('<td>%s</td>' % x for x in r))
    return '<table class="big"><thead><tr>%s</tr></thead><tbody>%s</tbody></table>' % (h, b)

S = []
a = S.append

a('<h1>راهنمای ارشد هلند — نسخه‌ی ۱</h1>')
a('<div class="sub">کسری جامعی · به‌روزرسانی ۲۳ نوامبر ۲۰۲۶ (۲ آذر ۱۴۰۵) · هم‌قالب راهنمای آلمان (v31). '
  'همه‌ی مهلت‌ها و هزینه‌ها از صفحه‌های رسمی دانشگاه‌ها یا Study in NL (Nuffic) در همین روز خوانده شده؛ جایی که منبع رسمی چیزی نگفته یا منابع با هم نمی‌خوانند ⚠ گذاشته‌ام. '
  'ترم‌ها: <b>فوریه ۲۰۲۷</b> (معادل تابستان آلمان) و <b>سپتامبر ۲۰۲۷</b> (معادل زمستان).</div>')

a('<div class="box warn"><b>سه واقعیت مهم قبل از هر چیز</b><ol>'
  '<li><b>شهریه:</b> غیراروپایی‌ها در هلند «شهریه‌ی مؤسسه‌ای» می‌دهند: دانشگاه‌های پژوهشی (WO) حدود <b>€۱۹٬۵۰۰ تا €۳۴٬۰۰۰ در سال</b>، دانشگاه‌های کاربردی (HBO) حدود <b>€۱۰٬۵۰۰ تا €۱۴٬۰۰۰ در سال</b> (ارشد HBO معمولاً یک‌ساله است). سقفی که برای آلمان گفته بودی (~€۴٬۰۰۰ در ترم) را همه رد می‌کنند. مقایسه: در آلمان بیشتر برنامه‌هایت شهریه ندارند.</li>'
  '<li><b>تمکن مالی (IND):</b> سال ۲۰۲۶ برای دانشگاه/HBO <b>€۱٬۱۳۰٫۷۷ در ماه</b> (~€۱۳٬۵۶۹ در سال) — به سن ربطی ندارد؛ هر ۱ ژانویه عوض می‌شود. برای ورودی سپتامبر ۲۰۲۷ رقم ۲۰۲۷ ملاک است (هنوز منتشر نشده). معمولاً باید <b>شهریه‌ی سال اول + هزینه‌ی زندگی</b> را قبل از ویزا به حساب دانشگاه بریزی (مثلاً Radboud: €۱۳٬۸۰۰ زندگی، بعد از رسیدن برمی‌گردد).</li>'
  '<li><b>ایرانی‌ها مهلت زودتر دارند</b> در بعضی HBOها: Saxion (۱ آوریل ۲۰۲۷، پرداخت تا ۱ مه)، Hanze (۱ مه / فوریه: ۱ اکتبر). انتقال پول از ایران به حساب دانشگاه به‌خاطر تحریم سخت است؛ بیشتر دانشگاه‌ها <b>پرداخت از طرف شخص ثالث</b> (Third-party payer) خارج از ایران را قبول می‌کنند — زودتر هماهنگ کن.</li>'
  '</ol></div>')

# ---------------- Status ----------------
a('<h2>الف) وضعیت درخواست‌های فعلی‌ات در هلند</h2>')
a(T(['برنامه', 'ورودی', 'شماره‌ها', 'وضعیت', 'قدم بعدی'], [
  ['<b>Saxion — Master ICT: Software Engineering</b> (Deventer، HBO، ۱ سال)', 'سپتامبر ۲۰۲۷', 'Studielink 2607182 · دانشجویی 00614427',
   '✅ OSIRIS + Questionnaire ارسال شد (۱ نوامبر)؛ «Additional requirements (TVW)» در جریان؛ منتظر تصمیم',
   'مهلت ایرانی: درخواست ۱ آوریل ۲۰۲۷، پرداخت و مدارک ۱ مه ۲۰۲۷. شهریه <b>€۱۰٬۵۶۰ در سال</b> (صفحه‌ی برنامه؛ سال تحصیلی ذکر نشده ⚠). هزینه‌ی درخواست ندارد.'],
  ['<b>THUAS — Data Driven Business</b> (Den Haag، HBO، ۱ سال)', 'سپتامبر ۲۰۲۷', '27012972 (27012972@student.hhs.nl)',
   '✅ OSIRIS + مدارک ارسال شد (۱ نوامبر)؛ جواب ۲–۴ هفته',
   'شهریه‌ی ارشد تمام‌وقت انگلیسی: <b>€۱۴٬۰۰۰</b> (جدول ۲۰۲۶/۲۷؛ ۲۰۲۷/۲۸ هنوز اعلام نشده ⚠). برای سپتامبر IELTS ۶٫۵ کل / ۶٫۰ هر بخش ✔. اگر تا آخر نوامبر جواب نیامد، ایمیل بزن. ⚠ تمرکز این برنامه بیزینس/دیتا است، نه CS.'],
  ['<b>Fontys — Master Applied IT</b> (Eindhoven، HBO)', 'فوریه ۲۰۲۷ <b>و</b> سپتامبر ۲۰۲۷', '6293034',
   '🟡 در Studielink برای هر دو ورودی؛ «Language assessment required»؛ پورتفولیوی دور اول تا ۸ نوامبر/ایمیل ۱۳ نوامبر — ⚠ وضعیت ارسالش در فایل‌هایم ثبت نشده',
   'فوریه: دور دوم پورتفولیو <b>۸ دسامبر</b>، مصاحبه ۱۰–۲۰ دسامبر (جزئیات در بخش ب). سپتامبر: Studielink تا ۱ مه، پورتفولیو ۸ آوریل/۸ مه.'],
  ['TU/e — Computer Science and Engineering', 'فوریه ۲۰۲۷', 'case M26110569', '❌ رها شد (۷ نوامبر): ترجمه‌ی رسمی انگلیسی/هلندی مدرک نداشتی', 'برای سپتامبر ۲۰۲۷ فقط اگر ترجمه‌ی رسمی انگلیسی بگیری (بخش ج).'],
], ['done', 'done', 'sn', 'bad']))

# ---------------- Feb 2027 ----------------
a('<h2>ب) ورودی فوریه ۲۰۲۷ — هنوز چه می‌شود زد؟</h2>')
a('<div class="box">تقریباً همه‌ی مهلت‌های غیراروپایی فوریه گذشته‌اند، چون ویزا (MVV) حدود <b>۳ ماه</b> وقت می‌برد. '
  'تنها گزینه‌ی واقعی که پیدا کردم Fontys Applied IT است (که همین الان در آن ثبت‌نام داری). THUAS DDB هم ورودی فوریه دارد ولی مهلتش ⚠ نامطمئن است.</div>')
a(T(['برنامه', 'مهلت غیراروپایی', 'هزینه‌ی درخواست', 'شهریه‌ی غیراروپایی', 'شرط‌ها / تو', 'نظرم'], [
  ['##', '🟢 هنوز باز'],
  ['<b>Fontys — Applied IT</b> (HBO)', 'Studielink: <b>۱ دسامبر</b> · پورتفولیو دور ۲: <b>۸ دسامبر</b> · مصاحبه ۱۰–۲۰ دسامبر · فرم خوابگاه ۶ دسامبر',
   'ندارد', '⚠ اعلام نشده (Fontys فقط ماشین‌حساب شهریه دارد؛ HBO معمولاً €۱۰–۱۴ هزار)',
   'لیسانس IT ✔؛ پورتفولیو (انگیزه‌نامه، پروفایل شایستگی، CV، توصیه‌نامه)؛ مصاحبه. ⚠ قاعده‌ی کلی Fontys برای فوریه: پرداخت شهریه + مدارک ویزا تا ۶ دسامبر — Applied IT استثنا است و تاریخ دقیقش باید از admission@fontys.nl پرسیده شود.',
   '🟡 فقط اگر پول شهریه + تمکن (~€۲۵ هزار) را تا اوایل دسامبر جور می‌کنی. وگرنه همین برنامه را برای <b>سپتامبر</b> نگه دار.'],
  ['THUAS — Data Driven Business', '⚠ Study in NL: ۱۵ ژانویه ۲۰۲۷ برای شروع ۱ فوریه — در سایت THUAS پیدا نکردم؛ احتمالاً برای ویزا زودتر بسته شده',
   'ندارد', '€۱۴٬۰۰۰ (۲۰۲۶/۲۷)', 'IELTS فوریه: ۶٫۰ کل و هر بخش ✔', '🟡 الان برای سپتامبر درخواست داری. اگر فوریه می‌خواهی، از THUAS بپرس (درخواست فعلی را می‌شود جابه‌جا کرد یا نه).'],
  ['##', '⏹ مهلت فوریه گذشته'],
  ['University of Twente — CS', '۱ اکتبر ۲۰۲۶', '€۱۰۰', '€۱۳٬۰۲۰ برای نیم‌سال', '—', 'برای سپتامبر ۲۰۲۷ (بخش ج)'],
  ['Leiden — CS', '۱۵ اکتبر', '€۱۰۰', '€۲۳٬۳۰۰ (۲۰۲۷/۲۸)', '—', 'برای سپتامبر'],
  ['RUG Groningen (هیچ ارشد CS در فوریه نیست)', '۱۵ اکتبر', '€۱۰۰', '—', '—', '—'],
  ['Radboud / VU Amsterdam', '۱ نوامبر (VU: ویزا باید قبل از ۱ دسامبر شروع شده باشد)', '€۱۰۰ (Radboud فوریه: €۷۵)', '—', '—', 'برای سپتامبر'],
  ['HAN — Engineering Systems (Cyber-Physical / Automotive / Energy)', '۱ اکتبر (ضمانت مالی ۱ نوامبر)', 'ندارد', '€۱۰٬۹۴۰', '—', 'برای سپتامبر'],
  ['Fontys (همه‌ی برنامه‌ها به‌جز Applied IT)', '۱۵ نوامبر', 'ندارد', '—', '—', '—'],
  ['Saxion', 'فوریه فقط تبادل دانشجو (ایرانی: ۱ اکتبر)', '—', '—', '—', 'ارشدها فقط سپتامبر'],
  ['TU/e — CSE', 'رها شد', '—', '€۲۱٬۷۰۰', '—', '—'],
], ['grp', 'sn', 'sn', 'grp', 'lt', 'lt', 'lt', 'lt', 'lt', 'lt', 'lt', 'lt']))

# ---------------- Sept 2027 ----------------
a('<h2>ج) ورودی سپتامبر ۲۰۲۷ — گزینه‌ها</h2>')
a('<div class="box">شرط‌هایی که با تو چک کردم: معدل ۱۷٫۴۳/۲۰ ≈ ۸۷٪ · IELTS ۷٫۰ (Writing ۶٫۰ ⚠: هر برنامه‌ای که «حداقل ۶٫۵ در هر بخش» بخواهد ردت می‌کند) · بدون GRE · مدرک با <b>ترجمه‌ی رسمی آلمانی</b> (بعضی دانشگاه‌ها فقط ترجمه‌ی انگلیسی یا هلندی قبول می‌کنند — TU/e ترجمه‌ی آلمانی‌ات را نپذیرفت). '
  '<b>هزینه‌ی درخواست:</b> بیشتر دانشگاه‌های پژوهشی برای مدرک خارجی <b>€۱۰۰</b> می‌گیرند؛ HBOها (Saxion، THUAS، Fontys، Hanze، Windesheim، Avans، Inholland) معمولاً ندارند.</div>')
a(T(['برنامه', 'مهلت غیراروپایی', 'هزینه‌ی درخواست', 'شهریه‌ی سالانه (غیراروپایی)', 'شرط‌ها / تو', 'نظرم'], [
  ['##', 'دانشگاه‌های کاربردی (HBO) — ارزان‌تر، ۱ ساله، کاربردی'],
  ['<b>Saxion — ICT: Software Engineering</b> ✅ زده‌ای', '<b>ایرانی: ۱ آوریل ۲۰۲۷</b> (پرداخت/مدارک ۱ مه)', 'ندارد', '€۱۰٬۵۶۰',
   'لیسانس مرتبط با نرم‌افزار ✔؛ بدون پیش‌ارشد', '✅ بهترین تناسب در هلند با کار فرانت‌اندت'],
  ['<b>THUAS — Data Driven Business</b> ✅ زده‌ای', '⚠ در صفحه نیامده', 'ندارد', '€۱۴٬۰۰۰ (۲۰۲۶/۲۷)', 'لیسانس ✔؛ IELTS ۶٫۵/۶٫۰ ✔', '🟡 بیزینس/دیتا؛ گران‌ترین HBO لیست'],
  ['<b>Fontys — Applied IT</b> 🟡 ثبت‌نام داری', 'Studielink ۱ مه (ترجیحاً قبل از ۱ آوریل) · پورتفولیو ۸ آوریل یا ۸ مه · مصاحبه ۱۰–۲۰ آوریل/مه', 'ندارد', '⚠ اعلام نشده',
   'لیسانس IT ✔؛ پورتفولیو + مصاحبه', '✅ اگر فوریه نشد، برای سپتامبر حتماً کامل کن'],
  ['<b>HAN — Engineering Systems: Cyber-Physical Systems</b> 🆕 (Arnhem/Nijmegen)', '۱ مه ۲۰۲۷ (⚠ مهلت جدای ایرانی در صفحه نیامد)', 'ندارد', '<b>€۱۰٬۹۴۰</b> (۲۰۲۶/۲۷)',
   'لیسانس مهندسی ✔ (Computer Eng.)؛ میانگین ≥۷۰٪ ✔؛ IELTS ≥۶٫۰ هر بخش ✔؛ CV + انگیزه‌نامه', '✅ <b>پیشنهاد اضافه:</b> embedded/کنترل، به لیسانست نزدیک؛ ارزان‌ترین HBO. عضو NL Scholarship.'],
  ['Fontys — Data Driven Business (Eindhoven)', '۱ مه ۲۰۲۷', 'ندارد', '⚠ اعلام نشده', 'لیسانس ✔؛ جلسه‌ی intake', '🟡 مشابه THUAS DDB؛ لازم نیست هر دو را بزنی'],
  ['##', 'دانشگاه‌های پژوهشی (WO) — گران، ۲ ساله؛ فقط با بورسیه منطقی است'],
  ['<b>University of Twente — Computer Science</b>', '<b>۱ مه ۲۰۲۷</b> (درخواست کامل در Osiris)', '€۱۰۰', '<b>€۲۲٬۳۲۰</b>',
   'CS / Computer Eng. ✔؛ ≥۶۰ ECTS CS (OOP، ADS، DB ✔)، ≥۲۰ ریاضی ✔، <b>≥۱۵ ECTS پروژه/روش تحقیق ⚠</b>؛ معدل ≥۷۰٪ ✔؛ IELTS ۶٫۵ / ۶٫۰ ✔؛ بدون GRE',
   '✅ بهترین گزینه‌ی پژوهشی برایت (بدون GRE، شرط زبان جور). بورسیه UTS + NL Scholarship: حداقل ۲ ماه قبل از مهلت بورسیه درخواست بده'],
  ['<b>Radboud — Software Science / Computing Science</b> (Nijmegen)', '۱ آوریل ۲۰۲۷ · <b>با بورسیه: ۳۱ ژانویه</b>', '€۱۰۰', '<b>€۱۹٬۵۵۵</b> (Software Science، ۲۰۲۷/۲۸؛ ارزان‌ترین WO)',
   'لیسانس CS ✔؛ ⚠ معدل/IELTS دقیق در صفحه نیامد', '🟡 اگر یک WO برای بورسیه می‌زنی، این یا Twente'],
  ['Leiden — Computer Science', '۱ آوریل ۲۰۲۷', '€۱۰۰', '€۲۳٬۳۰۰', 'لیسانس CS/AI ✔؛ ⚠ جزئیات معدل/IELTS نیامد', '🟡 خوب ولی گران'],
  ['VU / UvA — Computer Science (joint)', '۱ آوریل ۲۰۲۷ · <b>برای بورسیه تا ۱ دسامبر ۲۰۲۶</b> (بورسیه ۱ فوریه)', '€۱۰۰ (تا ۴ برنامه)', '€۲۳٬۴۳۰ یا €۲۴٬۹۷۰ ⚠ (دو ستون بی‌عنوان در PDF رسمی)', '⚠ جزئیات نیامد', '🟡 آمستردام گران؛ فقط با بورسیه VUFP'],
  ['RUG Groningen — Computing Science', '۱ مه ۲۰۲۷', '€۱۰۰', '€۲۴٬۹۰۰', 'لیسانس CS (بررسی درس‌به‌درس)', '🟡'],
  ['Utrecht — Computing Science', '⚠ حدود ۱ آوریل (۲۰۲۶ همین بود)', '€۱۰۰ (۳ سال اعتبار)', '⚠ اعلام نشده؛ Utrecht گفته برای ورودی‌های جدید غیراروپایی از ۲۰۲۷/۲۸ <b>+€۳٬۰۰۰</b>', '⚠', '🟡'],
  ['Maastricht — Artificial Intelligence', '⚠ در صفحه نیامد', 'دارد ولی بعد از ثبت‌نام برمی‌گردد', '€۲۵٬۵۰۰', '⚠', '🟡'],
  ['TU/e — Computer Science and Engineering', '۱ مه ۲۰۲۷', '€۱۰۰ (فقط حواله‌ی بانکی)', '€۲۲٬۴۰۰', '⚠ <b>ترجمه‌ی رسمی انگلیسی/هلندی</b> لازم دارد (ترجمه‌ی آلمانی‌ات را نپذیرفت)', '❌ مگر ترجمه‌ی انگلیسی بگیری'],
  ['UvA — Software Engineering', '<b>۳۱ ژانویه ۲۰۲۷</b>', '€۱۰۰', '<b>€۳۴٬۲۰۰</b> (Study in NL)', '⚠', '❌ خیلی گران'],
  ['TU Delft — Computer Science', '۱۵ ژانویه ۲۰۲۷', '€۱۰۰', '⚠ اعلام نشده', '<b>GRE لازم</b> + IELTS ≥۷ و <b>≥۶٫۵ در هر بخش</b> (Writing تو ۶٫۰)', '❌ دو مانع قطعی'],
], ['grp', 'done', 'done', 'sn', 'opn', 'lt', 'grp', 'opn', 'opn', 'lt', 'lt', 'lt', 'lt', 'lt', 'bad', 'bad', 'bad']))

# ---------------- Money ----------------
a('<h2>د) پول — سال اول در هلند (تخمینی)</h2>')
a(T(['مورد', 'HBO (مثلاً Saxion)', 'WO (مثلاً Twente)', 'منبع / نکته'], [
  ['شهریه‌ی سال اول (از قبل پرداخت)', '€۱۰٬۵۶۰', '€۲۲٬۳۲۰', 'صفحه‌ی برنامه‌ها'],
  ['تمکن زندگی (IND، ۱۲ ماه)', '~€۱۳٬۶۰۰ (رقم ۲۰۲۶؛ ۲۰۲۷ کمی بیشتر)', 'همان', 'IND: €۱٬۱۳۰٫۷۷ در ماه در ۲۰۲۶؛ ارشد HBO یک‌ساله ولی تمکن سالانه است'],
  ['هزینه‌ی IND (ویزا + اقامت)', '~€۲۵۴', '~€۲۵۴', 'Radboud (دانشگاه جمع می‌کند)'],
  ['هزینه‌ی درخواست', '۰', '€۱۰۰', '—'],
  ['بیمه‌ی شروع، تست سل، بلیط، ودیعه‌ی خانه', '~€۱٬۵۰۰–۳٬۰۰۰', 'همان', 'تخمین؛ خانه در هلند کمیاب و گران است (€۵۰۰–۹۰۰ اتاق)'],
  ['<b>جمع چیزی که باید قبل از ویزا داشته باشی</b>', '<b>~€۲۵٬۰۰۰–۲۷٬۰۰۰</b>', '<b>~€۳۷٬۰۰۰–۳۹٬۰۰۰</b>', 'در آلمان (بدون شهریه): ~€۱۵–۱۸ هزار'],
], ['', '', '', '', '', 'opn']))
a('<div class="box good"><b>بورسیه‌ها (همه نسبی؛ زود اقدام کن):</b><ul class="chk">'
  '<li>• <b>NL Scholarship</b> (اسم جدید Holland Scholarship): <b>€۵٬۰۰۰</b> یک‌بار در سال اول؛ غیراروپایی بدون مدرک هلندی ✔. برای ۲۰۲۷/۲۸ شرکت‌کننده‌ها: Twente، TU/e، Radboud، RUG، Utrecht، VU، Maastricht، Wageningen + ۲۳ HBO از جمله <b>Fontys، HAN، Saxion</b>. مهلت را هر دانشگاه جدا تعیین می‌کند ⚠.</li>'
  '<li>• بورسیه‌ی خود دانشگاه‌ها (UTS در Twente، Radboud Scholarship با مهلت درخواست ۳۱ ژانویه، VUFP در VU با مهلت ۱ فوریه و درخواست برنامه تا ۱ دسامبر ۲۰۲۶): معمولاً فقط بعد از پذیرش مشروط قابل درخواست‌اند → <b>برای بورسیه باید دسامبر/ژانویه اپلای کنی</b>، نه آوریل.</li></ul></div>')

# ---------------- Rules ----------------
a('<h2>ه) نکته‌های ویژه‌ی ایرانی‌ها و روند ویزا</h2>')
a('<ol>'
  '<li><b>روند:</b> پذیرش → دانشگاه برایت MVV + اقامت را از IND درخواست می‌کند (تو مستقیم به IND نمی‌روی) → پرداخت شهریه + تمکن به حساب دانشگاه → جواب IND چند هفته → وقت سفارت هلند برای برچسب MVV (⚠ اینکه در تهران صادر می‌شود یا کشور همسایه را قبل از اقدام بپرس). دانشگاه‌ها توصیه می‌کنند <b>~۳ ماه قبل از شروع</b> اقدام کنی.</li>'
  '<li><b>امنیت دانش:</b> طبق گزارش ۳ نوامبر ۲۰۲۶ (Delta، TU Delft) غربالگری اجباری دانشجویان ارشد <b>هنوز اجرا نشده</b> و وزیر حتی در فکر حذف دانشجوها از آن است. ولی محدودیت‌های تحریمی برای رشته‌های هسته‌ای/موشکی از قبل وجود دارد — برای CS، نرم‌افزار و دیتا معمولاً مشکلی نیست.</li>'
  '<li><b>ترجمه:</b> برای Saxion و THUAS با ترجمه‌ی آلمانی درخواست دادی و تا الان ایرادی نگرفته‌اند؛ TU/e انگلیسی/هلندی خواست. اگر می‌خواهی WO بزنی، <b>ترجمه‌ی رسمی انگلیسی</b> مدرک و ریزنمره را همین آذر سفارش بده.</li>'
  '<li><b>IELTS:</b> حدود ژوئن ۲۰۲۷ دو ساله می‌شود. Twente می‌گوید مدرک باید تا یک ماه بعد از درخواست معتبر باشد → برای سپتامبر ۲۰۲۷ قبل از مه درخواست بده.</li>'
  '<li><b>پول:</b> انتقال از ایران تقریباً غیرممکن است؛ یک نفر در خارج (آلمان/ترکیه/امارات) به‌عنوان Third-party payer — از قبل با دانشگاه هماهنگ کن که قبولش دارند.</li>'
  '</ol>')

# ---------------- Checklist ----------------
a('<h2>و) چک‌لیست هلند</h2>')
a('<ul class="chk">'
  '<li>☐ <b>همین هفته:</b> وضعیت پورتفولیوی Fontys Applied IT را چک کن (ایمیل ۱۳ نوامبر رفته یا نه)؛ تصمیم: فوریه (دور ۲، ۸ دسامبر) یا فقط سپتامبر</li>'
  '<li>☐ <b>تا ۱ دسامبر:</b> اگر فوریه‌ی Fontys را می‌خواهی، Studielink را برای فوریه نگه دار و از admission@fontys.nl مهلت پرداخت/ویزای Applied IT را بپرس</li>'
  '<li>☐ <b>تا ۸ دسامبر:</b> پورتفولیوی دور ۲ Fontys (فقط اگر فوریه)</li>'
  '<li>☐ <b>آخر نوامبر:</b> اگر THUAS جواب نداده، ایمیل پیگیری؛ Saxion: TVW را دنبال کن</li>'
  '<li>☐ <b>دسامبر:</b> تصمیم درباره‌ی WO: اگر Twente یا Radboud با بورسیه، ترجمه‌ی رسمی انگلیسی + درخواست تا ژانویه (Radboud با بورسیه ۳۱ ژانویه)</li>'
  '<li>☐ <b>تا ۱ آوریل ۲۰۲۷:</b> Saxion (مهلت ایرانی) — اگر پذیرش آمد، پرداخت و مدارک تا ۱ مه</li>'
  '<li>☐ <b>تا ۱ مه ۲۰۲۷:</b> HAN CPS (اختیاری، پیشنهادی) · Fontys Applied IT سپتامبر · Twente CS (اگر می‌زنی)</li>'
  '<li>☐ <b>ژانویه ۲۰۲۷:</b> رقم جدید تمکن IND را چک کن</li>'
  '</ul>')
a('<div class="box"><b>جمع‌بندی:</b> با شهریه‌ی هلند، آلمان برای تو اولویت اول می‌ماند. در هلند <b>Saxion + Fontys Applied IT</b> (و اختیاری <b>HAN CPS</b>) را نگه دار — همه بدون هزینه‌ی درخواست. THUAS را که زده‌ای ادامه بده. WOها فقط اگر برای بورسیه وقت می‌گذاری (Twente بهترین تناسب).</div>')

# ---------------- Sources ----------------
src = [
 ('IND — Fees and required amounts 2026', 'https://ind.nl/en/news/fees-and-required-amounts-for-2026-known'),
 ('IND — Income requirements study', 'https://ind.nl/en/Pages/income-requirements-study.aspx'),
 ('Fontys — Applied IT application & admission', 'https://www.fontys.nl/en/Programmes/Applied-IT-master-full-time-and-part-time/Application-admission.htm'),
 ('Fontys — Deadlines non-EEA', 'https://www.fontys.nl/en/Study-at-Fontys/Practical-information/Application-deadlines/Deadlines-for-applicants-with-a-non-EEA-nationality.htm'),
 ('Fontys — Data Driven Business admission', 'https://www.fontys.nl/en/Programmes/Data-Driven-Business-master-full-time/Application-admission.htm'),
 ('Saxion — Deadlines (incl. Iranian nationals)', 'https://www.saxion.edu/studying-in-the-netherlands/application/deadlines'),
 ('Saxion — Master ICT Software Engineering', 'https://www.saxion.edu/programmes/master/ict-software-engineering'),
 ('THUAS — Data Driven Business', 'https://www.thuas.com/programmes/masters/data-driven-business'),
 ('THUAS — Tuition fees', 'https://www.thuas.com/study-choice/applications-finances-and-moving-here/tuition-fees'),
 ('Study in NL — THUAS DDB', 'https://www.studyinnl.org/dutch-education/studies/data-driven-business-58046-the-hague-university-of-applied-sciences'),
 ('HAN — February start', 'https://www.hanuniversity.com/en/study-and-living/studying-at-han/february-start/'),
 ('HAN — ES Cyber-Physical Systems admission & finances', 'https://www.hanuniversity.com/en/programs/master/engineering-systems-cyber-physical-systems/fulltime/admission-finances/'),
 ('Hanze — Application and enrolment', 'https://www.hanze.nl/en/studychoice/application-and-entry-requirements/application-and-enrolment'),
 ('UT — CS factsheet', 'https://www.utwente.nl/en/education/master/programmes/computer-science/masters-structure/factsheet/'),
 ('UT — CS admission (international)', 'https://www.utwente.nl/en/education/master/programmes/computer-science/admission/admission-international/'),
 ('UT — CS tuition fees', 'https://www.utwente.nl/en/education/master/programmes/computer-science/admission/tuitionfees'),
 ('UT — Master deadlines', 'https://utwente.nl/en/education/master/how-to-apply/master-deadlines'),
 ('Radboud — Deadlines masters', 'https://www.ru.nl/en/education/application-and-admission/application-procedure-masters/deadlines'),
 ('Radboud — Software Science tuition', 'https://www.ru.nl/en/education/masters/software-science/tuition'),
 ('Radboud — Visa costs and financial means', 'https://www.ru.nl/en/students/international-students/visa-and-residence-permit/application-procedure/costs'),
 ('Leiden — CS deadlines', 'https://www.universiteitleiden.nl/en/education/study-programmes/master/computer-science/admission-and-application/application-deadlines'),
 ('Leiden — CS tuition', 'https://www.universiteitleiden.nl/en/education/study-programmes/master/computer-science/admission-and-application/tuition-fees'),
 ('VU — Apply for a master', 'https://vu.nl/en/education/more-about/apply-masters-programme'),
 ('VU — Institutional fees 2027-28 (PDF)', 'https://assets-eu-01.kc-usercontent.com:443/ff31ad68-341e-015e-fb52-24df7a00ecea/202e5844-17c3-4e46-80a2-b3371ee5bc04/2027_Instellingscollegegelden_Master_EN.pdf'),
 ('RUG — Master deadlines', 'https://www.rug.nl/education/application-enrolment-tuition-fees/admission/procedures/application-informatie/application-deadlines/master-application-deadlines'),
 ('RUG — Computing Science', 'https://www.rug.nl/masters/computing-science/'),
 ('Utrecht — Non-EEA fee increase 2027-28', 'https://www.uu.nl/en/organisation/university-college-utrecht/increase-of-tuition-fees-for-non-eea-students-from-2027-28'),
 ('Maastricht — AI tuition', 'https://www.maastrichtuniversity.nl/education/master/programmes/artificial-intelligence/tuition-fees'),
 ('TU/e — Tuition fee', 'https://www.tue.nl/en/education/become-a-tue-student/tuition-fees-and-other-study-costs/tuition-fee'),
 ('UvA — Software Engineering admission', 'https://www.uva.nl/en/programmes/masters/software-engineering/application-and-admission/application-and-admission.html'),
 ('Study in NL — UvA Software Engineering', 'https://www.studyinnl.org/dutch-education/studies/software-engineering-1124-university-of-amsterdam'),
 ('TU Delft — CS non-EU admission (GRE)', 'https://tudelft.nl/onderwijs/opleidingen/masters/cs/msc-computer-science/admission-and-application/non-eu-efta-applicants-with-an-international-bachelor-degree'),
 ('TU Delft — Admission requirements (IELTS)', 'https://www.tudelft.nl/en/education/admission-and-application/msc-international-diploma/admission-requirements'),
 ('Study in NL — NL Scholarship', 'https://studyinnl.org/finances/nl-scholarship'),
 ('DegreeStep — NL application fees', 'https://degreestep.com/guides/netherlands-universities-no-application-fee/'),
 ('Delta (TU Delft) — Knowledge security plans, 3 Nov 2026', 'https://delta.tudelft.nl/en/article/knowledge-security-plans-no-screening-for-students-fewer-subject-areas-designated-as-sensitive'),
]
a('<h2>منابع</h2><ol style="direction:ltr;text-align:left;font-size:8px">' + ''.join('<li>%s — <a href="%s">%s</a></li>' % (t, u, u) for t, u in src) + '</ol>')

html = '<!doctype html><html lang="fa" dir="rtl"><head><meta charset="utf-8"><style>%s a{color:#0b5bd3;word-break:break-all}</style></head><body>%s</body></html>' % (CSS, ''.join(S))
open('nl1.html', 'w').write(html)
print('ok', len(html))
