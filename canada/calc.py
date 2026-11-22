# CRS (single) + FSW 67 grid, official tables (canada.ca grid, IRPR s.78-83)
FL={10:34,9:31,8:23,7:17,6:9,5:6,4:6}
def fl(c): return FL[min(c,10)]
def sl(c): return 6 if c>=9 else 3 if c>=7 else 1 if c>=5 else 0
AGE={**{a:110 for a in range(20,30)},30:105,31:99,32:94,33:88,34:83,35:77}
EDU={'bach':120,'mast':135}
CWE={0:0,1:40,2:53,3:64,4:72,5:80}
def crs(age=27,edu='bach',clb=(10,8,9,7),fr=None,fw=1,cwe=0,hw=0,cstudy=0,pnp=False,offer=0):
    core=AGE[age]+EDU[edu]+sum(fl(c) for c in clb)
    if fr: core+=sum(sl(c) for c in fr)
    lmi=max(CWE[cwe]+hw, offer); core+=lmi
    all9=min(clb)>=9; all7=min(clb)>=7
    hi = edu=='mast'
    el = (50 if all9 else 25) if hi else (25 if all9 else 13)
    el = el if all7 else 0
    ec = 0
    if cwe>=1: ec = (50 if cwe>=2 else 25) if hi else (25 if cwe>=2 else 13)
    eg=min(50,el+ec)
    fwl=0
    if fw>=1 and all7: fwl = (50 if all9 else 25) if fw>=3 else (25 if all9 else 13)
    fwc=0
    if fw>=1 and cwe>=1: fwc = (50 if cwe>=2 else 25) if fw>=3 else (25 if cwe>=2 else 13)
    fg=min(50,fwl+fwc)
    tr=min(100,eg+fg)
    add=0
    if fr and min(fr)>=7: add+= 50 if min(clb)>=5 else 25
    add+= {0:0,2:15,3:30}[cstudy]
    if pnp: add+=600
    return core,tr,add,core+tr+add
def fsw(clb=(10,8,9,7),fr=None,edu='bach',yrs=1,age=27,adapt=0):
    lp=sum(6 if c>=9 else 5 if c==8 else 4 if c==7 else -99 for c in clb)
    if fr and min(fr)>=5: lp+=4
    ep={'bach':21,'mast':23}[edu]
    wp=15 if yrs>=6 else 13 if yrs>=4 else 11 if yrs>=2 else 9
    ap=12 if age<=35 else 0
    return lp,ep,wp,ap,min(adapt,10),lp+ep+wp+ap+min(adapt,10)
S={
 'S0 فعلی (اگر GT همان نمره‌ها شود)':dict(),
 'S1 GT با CLB9 در هر ۴ مهارت':dict(clb=(10,9,9,9)),
 'S2 S1 + ۳ سال سابقه خارجی':dict(clb=(10,9,9,9),fw=3),
 'S3 S0 + فرانسه NCLC7':dict(fr=(7,7,7,7)),
 'S4 S1 + فرانسه NCLC7':dict(clb=(10,9,9,9),fr=(7,7,7,7)),
 'S5 ارشد آلمان + CLB9 + ۳ سال':dict(edu='mast',clb=(10,9,9,9),fw=3),
 'S6 S1 + پیشنهاد کار 2x میانه':dict(clb=(10,9,9,9),offer=100),
 'S7 ارشد ۲ساله کانادا + ۱ سال کار کانادا':dict(edu='mast',clb=(10,9,9,9),fw=2,cwe=1,cstudy=2),
 'S8 S7 + کار پردرآمد 1.3x':dict(edu='mast',clb=(10,9,9,9),fw=2,cwe=1,cstudy=2,hw=20),
 'S9 S7 + کار پردرآمد 2x':dict(edu='mast',clb=(10,9,9,9),fw=2,cwe=1,cstudy=2,hw=70),
}
for k,v in S.items():
    for age in (27,30):
        print(k,'age',age,crs(age=age,**v))
print('FSW')
for k,v in {'now':dict(),'clb9':dict(clb=(10,9,9,9)),'clb9+2y':dict(clb=(10,9,9,9),yrs=2),'now+fr5':dict(fr=(5,5,5,5)),'mast+clb9':dict(edu='mast',clb=(10,9,9,9)),'mast+now':dict(edu='mast')}.items():
    print(k,fsw(**v))
