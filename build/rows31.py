# -*- coding: utf-8 -*-
# v31 (23 Nov 2026): final uni-assist cart; TH OWL route confirmed (uni-assist); TU Dortmund DS saved for later.
from rows30 import ROWS, COVER
def P(prefix):
    h = [r for r in ROWS if r['p'].startswith(prefix)]; assert len(h) == 1, prefix; return h[0]
r = P('TH OWL — Information Technology'); r['v'] = '✅'; r['st'] = '🛒 در سبد uni-assist (۲۳ نوامبر)'
r['n'] = '<b>اصلاح v31 — مسیر قطعی شد: uni-assist</b> (نه KIS). صفحه‌ی «Application for a Master’s Degree Program»، صفحه‌ی International Office و FAQ uni-assist خود رشته (MIT) همه می‌گویند غیراروپایی با مدرک خارجی از uni-assist؛ KIS فقط برای مدرک آلمان/اتحادیه‌ی اروپا. VPD لازم نیست؛ uni-assist مدارک را مستقیم به TH OWL می‌فرستد. مهلت‌ها متناقض (Hinweise PDF: ۱ دسامبر؛ صفحه‌ی برنامه: ۱۵ ژانویه؛ FAQ ۲۰۲۳: ۲۵ ژانویه) → با بقیه‌ی سبد تا ۳۰ نوامبر بفرست. شرط: ≥۱۸۰ ECTS، معدل ≤۲٫۵ ✔ (۱٫۷۷)، انگلیسی خیلی خوب ✔؛ <b>انگیزه‌نامه‌ی انگلیسی</b>. محتوا: Algorithms، Industrial SE، AI، IT Security، سیستم‌های real-time؛ FH، Lemgo، رنگ صنعتی/اتوماسیون → گزینه‌ی مطمئن.'
r = P('TU Dortmund — Data Science'); r['st'] = '💾 ذخیره برای بعد — فعلاً نزن'
r['n'] = '<b>تصمیم ۲۳ نوامبر: ذخیره.</b> بعد از جواب Bonn CS (~۱۵ دسامبر) تصمیم بگیر؛ اگر Bonn قبول نشد، تا <b>۱۵ ژانویه</b> با +€30 به uni-assist اضافه کن. ' + r['n']
r = P('TU Dresden — Computer Science'); r['g'] = 'excl'; r['st'] = '❌ از سبد حذف شد (۲۳ نوامبر)'
for k in ('Rostock — Computer Science Int', 'Passau — Computer', 'Kiel — Computer', 'Marburg — Computer'):
    r = P(k); r['st'] = '🛒 در سبد uni-assist (۲۳ نوامبر)'
