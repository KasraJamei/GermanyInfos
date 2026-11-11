# -*- coding: utf-8 -*-
from rows20 import ROWS as R20, R, UA
import copy
ROWS=copy.deepcopy(R20)
def find(s): return [r for r in ROWS if r['p'].startswith(s)][0]
# corrections verified 7 Nov 2026
m=find('Magdeburg'); m['s']='تا <b>۱۵ نوامبر ۲۰۲۶</b> ✔'; m['dl']='2026-11-15'; m['n']=m['n']+' ⚠ مهلت اصلاح شد (قبلاً ۲۶ نوامبر نوشته شده بود)'
h=find('HPI'); h['g']='excl'; h['st']='❌ GRE + VPD'; h['r']='مستقیم + uni-assist (VPD)'; h['f']='VPD €75'; h['n']='⚠ ۷ نوامبر: GRE و VPD لازم است؛ اصلاح‌شده'; h['dl']=None
a=find('Augsburg'); a['g']='excl'; a['st']='❌ آلمانی C1'; a['n']='⚠ ۷ نوامبر: گواهی آلمانی C1 لازم است؛ اصلاح‌شده'; a['dl']=None
b=find('Bochum'); b['g']='winter'; b['st']='⚪ فقط زمستان برای غیراروپایی'; b['n']='⚠ ۷ نوامبر: برای غیراروپایی فقط ورودی زمستان؛ '+b['n']
s=find('Stuttgart'); s['n']='⚠ ۷ نوامبر: ورودی تابستان گذشته؛ فقط زمستان. '+s['n']
f=find('FH Südwestfalen'); f['g']='winter'; f['st']='⚪ تابستان ۲۰۲۷ ندارد'; f['n']='⚠ ۷ نوامبر: ورودی تابستان ۲۰۲۷ ندارد؛ '+f['n']; f['dl']=None
d=find('Deggendorf'); d['n']=d['n']+' · ✏ ۷ نوامبر: فرم و مدارک آپلود شد؛ فقط پرداخت €60 و «Bewerbung absenden» مانده'
d['st']='🟡 پر شده، ارسال‌نشده (€60)'
u=find('Duisburg-Essen — Communications'); u['n']=u['n']+' · لینک: uni-due.de/international/international-admissions.php'
# new row
ai=R('open','🟢 الان باز','Aalen — Computer Science (کاربردی)',UA.split(' (')[0]+' (VPD لازم برای مدرک خارجی) + پورتال Aalen','VPD €75','⚠ بررسی شود','۱ اکتبر → <b>۱۵ دسامبر ۲۰۲۶</b> ⚠','—','⚠ ۷ نوامبر: صفحه‌ی Aalen برای مدرک خارجی VPD می‌خواهد (پس بدون هزینه نیست)؛ تاریخ را از سایت رسمی تأیید کن؛ پورتال: onlineportal.bewerbung.htw-aalen.de/bewerbung',None,'2026-12-15','تابستان')
ROWS.append(ai)
