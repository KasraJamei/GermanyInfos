# GermanyInfos — پرونده‌ی کامل اپلای ارشد کسری جامعی

> به‌روزرسانی: **۲۳ نوامبر ۲۰۲۶ (۲ آذر ۱۴۰۵)** · ریپوی **خصوصی** — شامل مدارک هویتی و اطلاعات تماس؛ عمومی نکن.

## از کجا شروع کنم؟
| می‌خواهم… | برو سراغ |
|---|---|
| بدانم الان چه بزنم و مهلت‌ها چیست | [`pdf/Germany_MSc_CS_Guide_Kasra_v31.pdf`](pdf/Germany_MSc_CS_Guide_Kasra_v31.pdf) (بخش الف/ب + چک‌لیست) |
| وضعیت درخواست‌هایی که زده‌ام + شماره‌ها | [`applications/STATUS.md`](applications/STATUS.md) |
| یک فرم جدید پر کنم (آدرس، معدل، تبدیل نمره، زبان، سابقه کار…) | [`profile/APPLICANT_PROFILE.md`](profile/APPLICANT_PROFILE.md) |
| جواب‌های آماده‌ی سؤال‌های تکراری، Comment، تقسیم درس‌ها به حوزه‌ها | [`profile/FORM_ANSWERS.md`](profile/FORM_ANSWERS.md) |
| فایل برای آپلود | [`documents/00_ready_to_upload/`](documents/00_ready_to_upload/) — فهرست کامل: [`documents/README.md`](documents/README.md) |
| لیست ۶۱ درس با واحد و نمره (برای فرم‌های Module) | [`data/modules_61_courses.csv`](data/modules_61_courses.csv) |

## خلاصه‌ی پروفایل
BSc Computer Engineering، IAU Tehran North (anabin **H+**) · معدل **17.43/20** (آلمانی **1.77**) · ۱۴۴ واحد · IELTS **7.0** (L8.5 R6.5 S7 W6) · آلمانی B1 (گواهی دوره) · بدون GRE · ~۲۳ ماه کار فرانت‌اند (Angular) · ۳ توصیه‌نامه · پروژه‌ی پایانی ML for Cyberattack Detection (۲۰/۲۰).

## وضعیت کلی (۲۳ نوامبر)
- **ارسال‌شده:** ۱۲ برنامه در آلمان (Göttingen ×۲، Bonn ×۲ [Cyber Security رد]، Hildesheim ×۲، Freiburg ×۲، UDE ×۲، Stuttgart CS، RUB CS) + Saxion و THUAS در هلند.
- **این هفته (۳۰ نوامبر):** uni-assist — Rostock CSI، Paderborn CS (+CE)، Marburg؛ Dresden پیشنهاد حذف. ۱ دسامبر TH OWL.
- **بعدی:** TU Darmstadt CS (پاکت کاغذی تا ۱۵ ژانویه برسد)، RUB EEIT، HS Bremen، Passau، TU Dortmund DS، Augsburg DS.

## ساختار ریپو
```
pdf/            راهنماها (آلمان v25…v30، کانادا، اروپا-علوم انسانی)
applications/   STATUS.md + records/ (اسکرین‌شات/PDF فرم‌های ارسال‌شده: Bonn، RPTU، THUAS…)
profile/        APPLICANT_PROFILE.md · FORM_ANSWERS.md
documents/      00_ready_to_upload … 09_letters_and_forms (مدارک)
data/           modules_61_courses.csv/.txt · Germany_uni_list.xlsx
research/       یادداشت‌های راستی‌آزمایی دورهای قبل (DAAD، رسمی)
build/          کد ساخت PDF راهنما (Python → HTML → Playwright → PDF، فونت Vazirmatn)
canada/         محاسبات و کد راهنمای کانادا
ALL-KNOWN-INFO-FULL.md   برون‌بری حافظه‌ی Claude (۱۱ نوامبر؛ قدیمی)
```

## تاریخچه‌ی راهنما
- **v31 (۲۳ نوامبر):** سبد نهایی uni-assist (€255)، مسیر TH OWL = uni-assist، TU Dortmund DS ذخیره برای بعد.
- **v30 (۲۳ نوامبر):** تطبیق کامل با فهرست اعضای uni-assist + مرور ۱۶۰۴ ارشد انگلیسی DAAD؛ ۲۲ برنامه‌ی تازه؛ اصلاح Paderborn CS/CE (معافیت GRE)، TH OWL، Dresden؛ TU Darmstadt به «می‌زنم».
- v29 (۲۱ نوامبر): شرط آلمانی برنامه‌های uni-assist + دور Computer Engineering/Embedded.
- v28 (۲۱ نوامبر)، v25–v27 (۱۱–۲۰ نوامبر): ادغام بررسی‌های رسمی.

## بازسازی PDF
```bash
cd build && python3 build31.py && node render31.js   # body PDF؛ سپس ۳ صفحه‌ی شهرها از v29 اضافه می‌شود
```
