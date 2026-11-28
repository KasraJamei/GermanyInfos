# -*- coding: utf-8 -*-
# Canada MSc chances (Fall 2027 / Winter 2028) — v1, 28 Nov 2026
from build31 import CSS
from build_nl import T
EXTRA = '''
.ch{display:inline-block;padding:1px 6px;border-radius:8px;font-weight:700;font-size:8px;white-space:nowrap}
.c1{background:#d7f0dd;color:#145a2a}.c2{background:#fff1c2;color:#7a5a00}.c3{background:#ffe0cc;color:#8a3b00}.c0{background:#f6d3d8;color:#8a0018}
.urg{color:#b00020;font-weight:700}
'''
def C(n, t=None):
    return '<span class="ch c%d">%s</span>' % (n, t or {1:'خوب',2:'متوسط',3:'کم',0:'نمی‌شود'}[n])
S = []; a = S.append
a('<h1>شانس پذیرش ارشد کانادا — پاییز ۲۰۲۷ و زمستان (ژانویه) ۲۰۲۸</h1>')
a('<div class="sub">کسری جامعی · ۲۸ نوامبر ۲۰۲۶ (۷ آذر ۱۴۰۵) · ضمیمه‌ی «راهنمای مهاجرت به کانادا» (نسخه‌ی ۲۵ نوامبر). '
  'شرط‌ها از صفحه‌ی رسمی دانشکده‌ها و دانشکده‌های تحصیلات تکمیلی (Graduate Studies) در همین روز خوانده شده. شانس‌ها تخمین من است؛ دانشگاه‌ها آمار قبولی منتشر نمی‌کنند (جز تورنتو: ۵ تا ۱۰٪). '
  'در کانادا «فال» = سپتامبر و «وینتر» = ژانویه است. ژانویه‌ی ۲۰۲۷ تقریباً همه‌جا بسته است، پس وینتر را برای ژانویه‌ی ۲۰۲۸ بررسی کردم.</div>')

a('<div class="box warn"><b>پنج چیز که شانس تو را در کانادا تعیین می‌کند</b><ol>'
  '<li><b>نمره‌ی نوشتن آیلتس (۶) بزرگ‌ترین مانع است.</b> خیلی از دانشگاه‌های بزرگ «هر بخش حداقل ۶٫۵» می‌خواهند: تورنتو، UBC ونکوور (CS: کل ۷ و هر بخش ۶٫۵)، آلبرتا، کلگری، ساسکاچوان. اتاوا هم نوشتن ۶٫۵ می‌خواهد. این‌ها برای تو بسته‌اند.</li>'
  '<li><b>تورنتو اصلاً دانشجوی خارجی برای MSc CS نمی‌گیرد.</b> صفحه‌ی رسمی: «International applicants are not considered for the MSc in Computer Science» (فقط MScAC یا دکتری مستقیم).</li>'
  '<li><b>آیلتس تو ۲۷ مه ۲۰۲۷ دو ساله می‌شود.</b> بیشتر دانشگاه‌ها می‌گویند نمره «حداکثر ۲ ساله» باشد (UVic، SFU؛ گوئلف: «در زمان پذیرش»). مهلت‌های پاییز ۲۰۲۷ قبل از آن است ✔. ولی مهلت‌های ژانویه‌ی ۲۰۲۸ بیشتر ژوئن تا اوت ۲۰۲۷ است، یعنی <b>بعد از انقضای آیلتس</b>. پس برای وینتر ۲۰۲۸ عملاً آزمون تازه لازم داری، و آیلتس در ایران متوقف است.</li>'
  '<li><b>بورسیه یعنی ویزا.</b> برای ویزای تحصیلی باید ۲۳٬۴۴۸ دلار هزینه‌ی زندگی + شهریه‌ی سال اول نشان بدهی. نرخ رد ویزای تحصیلی در ۲۰۲۵ حدود ۵۹٪ بوده. یک ارشد پژوهشی (thesis) با کمک‌هزینه هم پول را حل می‌کند، هم پرونده‌ی ویزا را قوی‌تر می‌کند. ارشدهای درسی (course-based) معمولاً پولی‌اند.</li>'
  '<li><b>در بیشتر ارشدهای پژوهشی، استاد راهنما تصمیم می‌گیرد.</b> گوئلف و UBC اوکاناگان بدون موافقت استاد پذیرش نمی‌دهند؛ ریجاینا برای مسیر thesis استاد را قبل از درخواست می‌خواهد. <b>از همین هفته به استادها ایمیل بزن.</b></li>'
  '</ol></div>')

a('<div class="box"><b>پروفایل تو از دید کانادا:</b> معدل ۱۷٫۴۳ از ۲۰ (حدود ۸۷٪؛ در مقیاس ۴ تقریباً ۳٫۶ تا ۳٫۷ ⚠ بسته به ارزیابی) — بالای حد B+ و «۷۸٪» بیشتر دانشگاه‌ها. آیلتس آکادمیک ۷ (L8.5 R6.5 <b>W6</b> S7). بدون GRE (برای ساکن ایران متوقف). '
  'برای ارشد پژوهشی نقطه‌ضعف: مقاله یا تجربه‌ی پژوهشی رسمی نداری؛ پروژه‌ی پایانی‌ات مرور مقایسه‌ای است. برای ویندزور: چهار درس کامپیوتری زیر ۷۰٪ داری (برنامه‌نویسی پیشرفته ۱۱، معماری ۱۱٫۱۵، طراحی زبان ۱۲، مدار منطقی ۱۳٫۲۵)؛ آنجا «۵ درس یا بیشتر زیر ۷۰٪» شانس را خیلی کم می‌کند. '
  '<br>' + C(1) + ' شرط‌ها را داری و رقابت معقول است · ' + C(2) + ' شرط‌ها را داری ولی استاد/رقابت تعیین می‌کند · ' + C(3) + ' خیلی رقابتی یا یک شرط مرزی · ' + C(0) + ' شرطی که نمی‌توانی برآورده کنی</div>')

a('<h2>۱) پاییز ۲۰۲۷ (سپتامبر) — به ترتیب مهلت</h2>')
G = '##'
a(T(['مهلت', 'دانشگاه — برنامه', 'شهر (استان)', 'آیلتس لازم', 'شرط و پول', 'شانس'], [
 [G, '<b>همین هفته (۱ دسامبر ۲۰۲۶)</b>'],
 ['<span class="urg">۱ دسامبر</span>', '<b>Waterloo — MMath CS (thesis)</b>', 'Waterloo (انتاریو)', '۶٫۵ (نوشتن ۶، صحبت ۶٫۵) ✔', 'حداقل ۷۸٪ ✔؛ ورودی سپتامبر، ژانویه و مه؛ کمک‌هزینه دارد (مبلغ در صفحه نیامده). از معتبرترین‌ها و بسیار رقابتی', C(3)],
 ['<span class="urg">۱ دسامبر</span>', '<b>York — MSc Computer Science</b>', 'Toronto (انتاریو)', '۷ کل ✔ (حد بخش‌ها ذکر نشده)', 'B+ در دو سال آخر ✔ + یک درس نظری سال آخر ✔؛ <b>کمک‌هزینه‌ی سالانه‌ی دانشجوی خارجی ۴۷٬۴۳۷ دلار</b> (گرایش AI بدون کمک‌هزینه)', C(2)],
 ['<span class="urg">۱ دسامبر</span>', 'Memorial — MSc CS', 'St. John\'s (نیوفاندلند)', '⚠ در صفحه نیامد', 'حداقل ۷۵٪ ✔ در CS یا CE؛ GRE برای خارجی‌ها «اکیداً توصیه»؛ کمک‌هزینه‌ی مسیر thesis ۲۰٬۰۰۰ دلار', C(2)],
 ['<span class="urg">۱ دسامبر</span>', 'Toronto — MScAC (حرفه‌ای)', 'Toronto', '۷ و هر بخش ۶٫۵ ❌', 'MSc CS برای خارجی‌ها بسته', C(0)],
 [G, '<b>دسامبر–ژانویه</b>'],
 ['۱۵ دسامبر', '<b>UVic — MSc Computer Science</b>', 'Victoria (بریتیش کلمبیا)', '۶٫۵ و هیچ بخش زیر ۶ ✔', 'برای درخواست استاد لازم نیست ولی استادها تصمیم می‌گیرند؛ لیسانس CE قبول؛ ورودی سپتامبر/ژانویه/مه', C(2)],
 ['۱۵ دسامبر ⚠', 'McGill — MSc CS (thesis)', 'Montreal (کبک)', '۶٫۵ کل ✔', 'CGPA ≥۳٫۲ ✔؛ GRE اختیاری؛ «مهلت‌های دانشکده خیلی زودتر از مهلت پیش‌فرض» ⚠؛ کبک: CAQ لازم؛ بسیار رقابتی', C(3)],
 ['۱۵ دسامبر', 'UBC Vancouver — MSc CS', 'Vancouver (BC)', '۷ و هر بخش ۶٫۵ ❌ (ELLT: ۸ و هر بخش ۷)', 'بورسیه‌ی کامل؛ ولی شرط زبان را نداری', C(0)],
 ['۱۵ دسامبر', 'USask — MSc CS', 'Saskatoon', '۷ و هیچ بخش زیر ۶٫۵ ❌', 'کمک‌هزینه ۱۸ هزار + شهریه', C(0)],
 ['⚠ (ببین)', 'UBC Okanagan — MSc CS', 'Kelowna (BC)', '۶٫۵ و هیچ بخش زیر ۶ ✔', 'بدون موافقت استاد پذیرش نمی‌دهد', C(2)],
 ['۱۵ ژانویه', '<b>Queen\'s — MSc Computing</b>', 'Kingston (انتاریو)', '۷ کل ✔', 'خارجی‌ها رتبه‌ی «A» (first class) لازم — ۸۷٪ تو احتمالاً ✔ ⚠؛ ۱۵ ژانویه برای در نظر گرفتن کمک‌هزینه؛ تماس با استاد توصیه شده', C(2)],
 ['۱۹ ژانویه', '<b>SFU — MSc Computing Science (thesis)</b>', 'Burnaby/Vancouver (BC)', '۶٫۵ و هر بخش ≥۶ ✔ (قاعده‌ی دانشگاه؛ ⚠ دانشکده ممکن است بالاتر بخواهد)', 'CGPA ≥۳٫۰ از ۴٫۳۳ ✔؛ رقابتی', C(2)],
 ['۱۹ ژانویه', 'SFU — Professional Master\'s (Big Data / Visual Computing / Cybersecurity)', 'Burnaby (BC)', 'همان', 'درسی و پولی (شهریه در صفحه نیامد ⚠)؛ شانس پذیرش بهتر، ولی پول ویزا بیشتر', C(2)],
 [G, '<b>فوریه–آوریل ۲۰۲۷</b>'],
 ['۱۵ فوریه', '<b>Regina — MSc CS: Data Science</b> (thesis/project هم هست)', 'Regina (ساسکاچوان)', '۶٫۵ ✔ (حد بخش‌ها ذکر نشده)', 'میانگین ≥۷۰٪ و CS ≥۷۵٪ ✔؛ برای گرایش Data Science استاد از قبل لازم نیست؛ مسیر thesis استاد قبل از درخواست', C(1)],
 ['۲۸ فوریه (ویزا)', 'UNB — Master of Computer Science', 'Fredericton (نیوبرانزویک)', '⚠ در صفحه نیامد', 'معمولاً B+ و ۲۰٪ برتر کلاس؛ کمک‌هزینه تضمینی نیست؛ پیش‌مهلت ۵ ژانویه', C(2)],
 ['۲۸ فوریه', 'McMaster — MASc / MEng Computing & Software', 'Hamilton (انتاریو)', '⚠ (لیسانسش ۶٫۵ و هر بخش ۶)', 'MASc حداقل B+ ✔؛ MEng حداقل B- (پولی)', C(2)],
 ['۱ مارس', '<b>Concordia — MCompSc (thesis)</b> / MApCompSc (درسی)', 'Montreal (کبک)', 'دانشکده‌ی مهندسی و CS: ۶٫۵ کل ✔', 'thesis: «رتبه‌ی خیلی بالا»، کمک‌هزینه معمولاً هست؛ MApComp درسی و co-op، پولی (شهریه‌ی کبک برای خارجی بالا ⚠)', C(2)],
 ['۱ مارس', '<b>Guelph — MSc Computer Science</b>', 'Guelph (انتاریو)', '⚠ (آزمون حداکثر ۲ ساله «در زمان پذیرش»)', 'میانگین ۷۵٪ دو سال آخر ✔؛ <b>پیدا کردن استاد اجباری</b>؛ کمک‌هزینه‌ی حداقل ۲۰٬۰۰۰ دلار در سال (۲ سال)', C(2)],
 ['۱ مارس', 'Calgary — MSc CS', 'Calgary (آلبرتا)', '۷ و هر بخش ۶٫۵ ❌', 'GRE هم «انتظار می‌رود»', C(0)],
 ['۱ آوریل', '<b>Dalhousie — MCS (thesis)</b> / MACS (درسی)', 'Halifax (نوا اسکوشیا)', '۷ کل ✔', 'MCS: معدل بالای ۳٫۴ ✔ + طرح پژوهشی؛ MACS: حداقل ۳٫۰، پولی، ورودی سپتامبر/ژانویه/مه', C(2)],
 ['۱۵ آوریل', 'Windsor — MSc CS / Master of Applied Computing (درسی)', 'Windsor (انتاریو)', '۶٫۵، هیچ بخش زیر ۶ و حداکثر یک بخش ۶ ✔ (دقیقاً تو)', 'MAC: ۷۰٪ (یا ۷۷٪ سه سال آخر) ✔، ودیعه ۴٬۰۰۰ دلار، پولی؛ ⚠ قاعده‌ی «۵ درس CS زیر ۷۰٪» — تو ۴ تا', C(2)],
 ['⚠', 'Western — MSc CS', 'London (انتاریو)', '۶٫۵ و هیچ بخش زیر ۶ ✔', 'حداقل ۷۵٪، عملاً ۷۸٪؛ بیشتر پذیرفته‌شده‌ها بالای ۸۲٪ ✔', C(2)],
 ['⚠', 'Carleton — MCS', 'Ottawa (انتاریو)', '۶٫۵ و هر بخش ≥۶ ✔ (⚠ برنامه ممکن است بالاتر بخواهد)', 'مسیر درسی بدون استاد هم دارد؛ «بسته‌های کمک‌هزینه‌ی سخاوتمندانه»', C(2)],
 ['⚠', 'TMU — MSc Computer Science', 'Toronto', '۷ کل ✔', 'حداقل B (۳٫۰) ✔', C(2)],
 ['⚠', 'Lakehead — MSc CS (course / project / thesis / AI)', 'Thunder Bay (انتاریو) — شهر RCIP', '⚠', 'حداقل B ✔؛ هزینه‌ی درخواست ۱۲۵؛ ⚠ مهلت بین‌المللی پاییز ۲۰۲۷ روشن نیست', C(2)],
 ['⚠', 'Laurentian — MSc Computational Sciences', 'Sudbury (انتاریو) — شهر RCIP', '۶٫۵ و هیچ بخش زیر ۶ ✔', 'B (۷۰٪) ✔؛ مسیر درسی یا thesis', C(1)],
 ['—', 'uOttawa — MCS', 'Ottawa', '۶٫۵ و نوشتن ۶٫۵ ❌', '', C(0)],
 ['—', 'Alberta — MSc CS', 'Edmonton', 'هر بخش ۶٫۵ ❌', 'کمک‌هزینه ۳۰٬۸۰۰', C(0)],
], None))

a('<h2 class="pb">۲) زمستان (ژانویه)</h2>')
a('<div class="box yel"><b>ژانویه‌ی ۲۰۲۷ (۵ هفته‌ی دیگر):</b> عملاً بسته. Algoma (Sault Ste. Marie، ارشد یک‌ساله) مهلتش <b>۱ دسامبر ۲۰۲۶</b> است (آیلتس ۶٫۵ و هیچ بخش زیر ۶ ✔، هزینه‌ی درخواست ۱۲۵). ولی ⚠ پردیسش مشخص نیست (Sault Ste. Marie یا Brampton) و ویزای کانادا در ۵ هفته تقریباً نمی‌رسد.</div>')
a(T(['مهلت ژانویه ۲۰۲۸', 'برنامه', 'با آیلتس فعلی (تا ۲۷ مه ۲۰۲۷)؟', 'شانس'], [
 ['۱ آوریل ۲۰۲۷', 'Memorial — MSc CS', '✔ قبل از انقضا', C(2)],
 ['۳۱ مه ۲۰۲۷ (پیش‌مهلت کمک‌هزینه)', 'UNB — MCS', '⚠ اگر تا ۲۷ مه بفرستی', C(2)],
 ['۱ ژوئن ۲۰۲۷', 'Waterloo — MMath CS', '❌ بعد از انقضا (مگر قبل از ۲۷ مه بفرستی و دانشگاه «زمان درخواست» را ملاک بگیرد)', C(3)],
 ['۱۵ ژوئن ۲۰۲۷', 'UVic — MSc CS / Regina — HCC', '⚠ مثل بالا', C(2)],
 ['۱ ژوئیه ۲۰۲۷', 'Concordia — MCompSc', '❌ احتمالاً آزمون تازه لازم', C(2)],
 ['۱ اوت ۲۰۲۷', 'Guelph — MSc CS · Dalhousie — MCS / MACS', '❌ گوئلف صریحاً می‌گوید «در زمان پذیرش» حداکثر ۲ ساله', C(2)],
 ['۱۵ اوت ۲۰۲۷', 'Windsor — MSc CS', '❌', C(2)],
], None))

a('<h2>۳) بر اساس شهر و نوع برنامه</h2>')
a(T(['دسته', 'بهترین گزینه‌ها برای تو', 'نکته'], [
 ['<b>پژوهشی با کمک‌هزینه</b> (بهترین برای ویزا)', 'York (۴۷٬۴۳۷ دلار) · Guelph (۲۰ هزار) · Memorial (۲۰ هزار) · Queen\'s · UVic · Dalhousie MCS · Concordia MCompSc · Regina · Western · Carleton', 'باید استاد هم‌رشته پیدا کنی؛ ایمیل با CV و یک پاراگراف درباره‌ی علاقه‌ی پژوهشی (وب، ML برای امنیت، HCI)'],
 ['<b>درسی (پولی)</b>', 'SFU Professional Master\'s · Dalhousie MACS · Windsor MAC · Concordia MApCompSc · McMaster MEng · Lakehead course-based · Laurentian course', 'پذیرش راحت‌تر، ولی شهریه + ۲۳٬۴۴۸ دلار پول نشان‌دادنی؛ ویزا سخت‌تر'],
 ['<b>انتاریو</b>', 'York، Waterloo، Queen\'s، Guelph، Western، Carleton، TMU، McMaster، Windsor، Lakehead، Laurentian، Algoma', 'بیشترین تعداد برنامه'],
 ['<b>بریتیش کلمبیا</b>', 'UVic، SFU، UBC Okanagan', 'UBC ونکوور به‌خاطر شرط نوشتن بسته'],
 ['<b>آتلانتیک</b>', 'Memorial، Dalhousie، UNB', 'رقابت کمتر (تأیید رسمی نشده)؛ مسیرهای اقامت آتلانتیک'],
 ['<b>پریری</b>', 'Regina', 'Saskatoon، Calgary، Edmonton به‌خاطر شرط زبان بسته'],
 ['<b>کبک</b>', 'Concordia، McGill', 'CAQ لازم؛ اقامت کبک فرانسوی می‌خواهد'],
 ['<b>شهرهای RCIP</b> (بخش ۸ب راهنمای کانادا)', 'Lakehead (Thunder Bay)، Laurentian (Sudbury)، Algoma (Sault Ste. Marie)', 'بعد از ارشد، راه دوم اقامت دائم بدون قرعه'],
], None))

a('<h2>۴) کارهای این هفته و ماه‌های بعد</h2><ol class="big">'
  '<li><b>تا ۱ دسامبر (۳ روز):</b> اگر می‌خواهی، <b>York</b> (کمک‌هزینه‌ی ۴۷ هزار) و Memorial. Waterloo فقط اگر هزینه‌ی درخواست برایت مهم نیست. هزینه‌ی درخواست هر کدام حدود ۱۰۰ تا ۱۵۰ دلار است ⚠؛ پرداخت با کارت خارجی لازم است.</li>'
  '<li><b>همین هفته:</b> برای هر دانشگاه پژوهشی ۲ تا ۳ استاد هم‌رشته پیدا کن و ایمیل بزن (Guelph، UBCO، Regina و Queen\'s به آن وابسته‌اند).</li>'
  '<li><b>تا ۱۵ دسامبر:</b> UVic (و McGill اگر مهلت دانشکده‌اش را تأیید کردی).</li>'
  '<li><b>تا ۱۵–۱۹ ژانویه:</b> Queen\'s و SFU.</li>'
  '<li><b>تا ۱۵ فوریه – ۱ مارس:</b> Regina، UNB، McMaster، Concordia، Guelph.</li>'
  '<li><b>تا ۱ آوریل:</b> Dalhousie؛ <b>۱۵ آوریل:</b> Windsor.</li>'
  '<li><b>ارزیابی مدرک:</b> بعضی دانشگاه‌ها WES یا ارزیابی خودشان را می‌خواهند؛ WES برای مدارک ایران در ۲۰۲۶ مشکل داشته (راهنمای کانادا، بخش ۱۱).</li>'
  '<li><b>آلمان را کنار نگذار.</b> کانادا با نرخ رد ویزای بالا و هزینه‌ی سنگین، فقط با کمک‌هزینه منطقی است.</li>'
  '</ol>')

a('<h2>۵) چیزهایی که هنوز مطمئن نیستیم</h2><ul>'
  '<li>⚠ شرط آیلتس Memorial، UNB، McMaster (تحصیلات تکمیلی)، Lakehead و Guelph در صفحه‌هایی که خواندم نیامد.</li>'
  '<li>⚠ SFU و Carleton قاعده‌ی کلی دانشگاه (۶٫۵/۶) را دارند؛ ممکن است دانشکده‌ی CS بالاتر بخواهد.</li>'
  '<li>⚠ تبدیل معدل ۱۷٫۴۳/۲۰ به مقیاس ۴ (حدود ۳٫۶–۳٫۷) را هر دانشگاه خودش انجام می‌دهد.</li>'
  '<li>⚠ مهلت دانشکده‌ی CS در McGill، Western، Carleton، TMU و Lakehead (پاییز ۲۰۲۷، بین‌المللی) در صفحه‌ها نبود.</li>'
  '<li>⚠ اینکه دانشگاه‌ها آیلتس را «۲ سال تا زمان درخواست» یا «تا زمان پذیرش/شروع» می‌خواهند؛ برای ژانویه‌ی ۲۰۲۸ مهم است.</li>'
  '<li>⚠ شهریه‌ی دقیق برنامه‌های درسی (SFU، Dalhousie MACS، Windsor MAC، Concordia MApComp، McMaster MEng).</li>'
  '</ul>')

a('<h2>منابع</h2><ol style="font-size:8.5px;line-height:1.7">'
  '<li>Toronto: web.cs.toronto.edu/graduate/msc؛ sgs.utoronto.ca (English proficiency)</li>'
  '<li>UBC: cs.ubc.ca/students/grad/admissions و english-proficiency-requirement؛ okanagan.calendar.ubc.ca (masters degrees، computer science admission)</li>'
  '<li>Waterloo: uwaterloo.ca/graduate-studies-postdoctoral-affairs/node/1470 (MMath CS thesis)</li>'
  '<li>McGill: mcgill.ca/gradapplicants/programs/computer-science؛ cs.mcgill.ca/graduate/future/mscadmission</li>'
  '<li>SFU: sfu.ca/fas/study/future-graduates/apply/computing-science.html؛ sfu.ca/gradstudies/apply/applying/requirements.html</li>'
  '<li>Calgary: grad.ucalgary.ca (CS MSc thesis)؛ calendar.ucalgary.ca (ELP)</li>'
  '<li>York: yorku.ca/gradstudies … Electrical_Engineering_Computer_Science_MSc_Aug_2026.pdf</li>'
  '<li>Western: csd.uwo.ca/graduate/future/admission.html · Carleton: carleton.ca/scs (masters program)، calendar.carleton.ca، graduate.carleton.ca (ESL)</li>'
  '<li>Concordia: concordia.ca/academics/graduate/computer-science-mcompsc.html؛ concordia.ca/gradstudies (English language proficiency)</li>'
  '<li>Queen\'s: cs.queensu.ca/apply/graduate.php؛ queensu.ca/grad-postdoc/grad-studies/apply · McMaster: eng.mcmaster.ca (CAS Graduate Information، نوامبر ۲۰۲۵)</li>'
  '<li>Windsor: uwindsor.ca/graduate-studies/494 و /305 · Guelph: uoguelph.ca/programs/msc-computer-science · TMU: torontomu.ca/graduate/future-students/apply/requirements</li>'
  '<li>Dalhousie: dal.ca (CS admissions، MACS admissions، FGS English requirements) · UNB: unb.ca/fredericton/cs/grad/admissionrequirements.html · Memorial: mun.ca/become/graduate (Computer Science)</li>'
  '<li>USask: grad.usask.ca/programs/computer-science.php · Manitoba: umanitoba.ca/graduate-studies (CS MSc) · Regina: uregina.ca/science/computer-science/graduate-programs/application-process.html</li>'
  '<li>UVic: uvic.ca/graduate (CS MSc، language proficiency) · Laurentian: laurentian.ca (language requirements) · Lakehead: lakeheadu.ca (MSc CS) · uOttawa: ouinfo.ca/universities/ottawa/language-requirements ⚠ (صفحه‌ی ثانویه)</li>'
  '</ol>')

html = '<!doctype html><html lang="fa" dir="rtl"><head><meta charset="utf-8"><style>' + CSS + EXTRA + '</style></head><body>' + ''.join(S) + '</body></html>'
open('ca1.html', 'w').write(html); print('ok')
