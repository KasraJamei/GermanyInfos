# -*- coding: utf-8 -*-
from rows21 import ROWS as R21, R, UA
import copy
ROWS=[r for r in copy.deepcopy(R21) if not r['p'].startswith('Aalen')]
def find(s): return [r for r in ROWS if r['p'].startswith(s)][0]
O='🟢 الان باز'; S='🔵 به‌زودی'
def add(g,p,r,f,t,s,n,dl,dlw='تابستان',st=None):
    ROWS.append(R(g,st or (O if g=='open' else S if g=='soon' else '⚪'),p+' 🆕',r,f,t,s,'—',n+' · ✔ ۷ نوامبر',None,dl,dlw))
# updates of existing rows from the 7 Nov list
find('Hof — Applied Research')['r']='مستقیم (Primuss، رایگان)'; find('Hof — Applied Research')['n']+=' · شانس کم–متوسط؛ ⚠ کار علمی مستقل، گواهی ۱۸ هفته کار، Anabin H+ (منبع غیررسمی می‌گوید uni-assist و ۱۵ ژانویه؛ از سایت Hof تأیید کن)'
find('OTH Amberg')['s']='۱ نوامبر → <b>۸ دسامبر ۲۰۲۶</b> ✔'; find('OTH Amberg')['dl']='2026-12-08'; find('OTH Amberg')['n']+=' · Primuss €50 + VPD؛ شانس متوسط–بالا؛ آزمون آنلاین ۲۰–۳۰ دسامبر'
t=find('THI Ingolstadt'); t['dl']='2027-01-15'; t['s']='۱۵ اکتبر → <b>۱۵ ژانویه ۲۰۲۷</b> ✔'; t['t']='€1,200'
hb=find('Hochschule Bielefeld'); hb['dl']='2027-01-15'; hb['s']='۱ دسامبر → <b>۱۵ ژانویه ۲۰۲۷</b> ✔'; hb['n']='✔ ۷ نوامبر: uni-assist؛ ۱۸۰ ECTS و معدل ۲٫۵ کافی؛ ویدیو + مصاحبه؛ شانس متوسط–بالا'
e=find('Emden'); e['g']='open'; e['st']=O; e['dl']='2026-12-01'; e['dlw']='تابستان'; e['s']='→ <b>۱ دسامبر ۲۰۲۶</b> ✔'; e['n']='✔ ۷ نوامبر: uni-assist؛ ۲۱۰ ECTS برق/کامپیوتر، سیستم‌های real-time؛ شانس متوسط'
hbrs=find('H-BRS'); hbrs['g']='passed'; hbrs['st']='⏹ مهلت گذشت'; hbrs['dl']=None; hbrs['n']+=' · ✔ ۷ نوامبر: مهلت متقاضی ویزا ۱۵ ژوئیه بود'
# new open rows
add('open','Aalen — Computer Science (کاربردی)','پورتال Aalen؛ ⚠ صفحه‌ی رسمی برای مدرک خارجی VPD می‌خواهد','⚠ رایگان در لیست؛ VPD €75 اگر خواستند','€1,500','۱ اکتبر → <b>۱۵ دسامبر ۲۰۲۶</b> ✔','مهندسی کامپیوتر صریحاً قبول؛ با کمتر از ۲۱۰ ECTS یک ترم اضافه؛ شانس بالا · onlineportal.bewerbung.htw-aalen.de/bewerbung','2026-12-15')
add('open','Aalen — ML &amp; Data Analytics (کاربردی)','پورتال Aalen (همان)','⚠ مثل بالا','€1,500','۱ اکتبر → <b>۱۵ دسامبر ۲۰۲۶</b> ✔','همان شرط‌ها؛ شانس متوسط–بالا','2026-12-15')
add('open','Deggendorf — AI &amp; Data Science (کاربردی)','Primuss (همان حساب)','€60 مشترک با Applied CS','€500 سرویس','→ <b>۱۵ نوامبر ۲۰۲۶</b>','⚠ ۹۰ واحد CS که ۱۸تایش AI/DS باشد؛ آزمون ورودی؛ شانس متوسط','2026-11-15')
add('open','Deggendorf — Automotive Software Eng. (کاربردی)','Primuss (همان حساب)','€60 مشترک','€500 سرویس','→ <b>۱۵ نوامبر ۲۰۲۶</b>','لیسانس CS/برق؛ آزمون + مصاحبه؛ شانس متوسط','2026-11-15')
add('open','Deggendorf — HPC / Quantum Computing (کاربردی)','Primuss (همان حساب)','€60 مشترک','€500 سرویس','→ <b>۱ دسامبر ۲۰۲۶</b>','آزمون ارزیابی؛ شانس متوسط','2026-12-01')
add('open','Hof — AI &amp; Robotics (کاربردی)','Primuss؛ ⚠ مدرک خارجی را باید uni-assist ≥۴ هفته قبل بررسی کند','رایگان','ندارد','۵ نوامبر → <b>۳۰ نوامبر ۲۰۲۶</b>','A1 رسمی، ۲۱۰ ECTS یا ماژول اضافه؛ شانس کم','2026-11-30')
add('open','Anhalt — Electrical &amp; Computer Eng. (کاربردی)','uni-assist',UA,'رایگان','→ <b>۱۵ ژانویه ۲۰۲۷</b>','IELTS 7 ✔ (C1)، ۱ سال کار ✔، انگیزه‌نامه؛ شانس بالا','2027-01-15')
add('open','THI — Sociotechnical Cybersecurity (کاربردی)','uni-assist (مدارک تا ۵ دسامبر)',UA,'€1,200','→ <b>۱۵ ژانویه ۲۰۲۷</b>','لیسانس CS، A1 تا پایان ترم اول، مصاحبه؛ شانس متوسط','2027-01-15')
add('open','THI — AI Eng. Autonomous Systems (کاربردی)','uni-assist',UA,'€1,200','→ <b>۱۵ ژانویه ۲۰۲۷</b>','۲۱۰ ECTS؛ شانس کم–متوسط','2027-01-15')
add('open','Heilbronn — Software Eng. (SEM) (کاربردی)','⚠ گواهی Studienkolleg Konstanz/uni-assist','⚠','€1,500','→ <b>۱۵ ژانویه ۲۰۲۷</b>','معدل ۲٫۵ ✔؛ شانس متوسط','2027-01-15')
add('open','Heilbronn — Applied AI (کاربردی)','⚠ مثل SEM','⚠','€1,500','→ <b>۱۵ ژانویه ۲۰۲۷</b>','⚠ ≥۵۰ ECTS ریاضی+CS+AI؛ شانس کم–متوسط','2027-01-15')
add('open','Albstadt — Industrial AI (کاربردی)','⚠ مسیر مشخص نیست','⚠','€1,500','۱ اکتبر → <b>۱۵ ژانویه ۲۰۲۷</b>','شرط خاصی اعلام نشده؛ شانس متوسط','2027-01-15')
add('open','HFT Stuttgart — Software Technology (کاربردی)','⚠','⚠','€1,500','→ <b>۱۵ ژانویه ۲۰۲۷</b> (فقط اگر جا بماند)','نمرات «خیلی بالاتر از متوسط»؛ شانس کم','2027-01-15')
add('open','Rhine-Waal — Usability Eng. (کاربردی)','uni-assist',UA,'⚠','→ <b>۱۵ ژانویه ۲۰۲۷</b>','IELTS 7 ✔، معدل ۲٫۰ ✔؛ ⚠ ۲۱۰ ECTS؛ شانس متوسط','2027-01-15')
add('open','THM — Business Informatics (Analytics) (کاربردی)','uni-assist',UA,'⚠','۱ اکتبر → <b>۱۵ ژانویه ۲۰۲۷</b>','⚠ Wirtschaftsinformatik؛ معدل ۲٫۰ ✔؛ آزمون؛ شانس کم','2027-01-15')
add('soon','TH Nürnberg — Intelligent Autonomous Systems (کاربردی)','⚠','⚠','⚠','۱۵ نوامبر → <b>۱۵ ژانویه ۲۰۲۷</b>','⚠ A1 رسمی، ۲۱۰ ECTS، کپی پایان‌نامه؛ شانس کم','2027-01-15')
# removed
for p,n in [('Kiel UAS — CS','برای مدرک خارج از اروپا GRE می‌خواهد'),('Stralsund — SSD','لیسانس مکانیک می‌خواهد'),('TH Augsburg — IMS','تدریس آلمانی است'),('Dortmund — Medical Informatics','گرایش سلامت و پایان‌نامه لازم است'),('Bremerhaven — ESD و THM CCCE','گواهی رسمی آلمانی A2/A1 لازم است'),('HTW Berlin','شهریه €4,400 بالای سقف'),('SRH / Fresenius / HDBW (خصوصی)','دانشگاه‌های خصوصی کنار گذاشته شدند')]:
    ROWS.append(R('excl','❌ حذف','%s 🆕'%p,'—','—','—','—','—',n+' · ✔ ۷ نوامبر',None))
u=find('Duisburg-Essen — Communications'); u['g']='done'; u['st']='✔ ارسال شد ۷ نوامبر ۲۰۲۶ · شماره ۷۱۳۵۱۵-۰۲ · Eingegangen'; u['p']='Duisburg-Essen — Communications Engineering (ISE)'; u['dl']=None
# keep done rows first
ROWS.sort(key=lambda r:0 if r['g']=='done' else 1)
