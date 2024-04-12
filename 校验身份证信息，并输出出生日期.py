from datetime import datetime
s=input();
ident=list(s);
li=[1,0,'X',9,8,7,6,5,4,3,2];
key=True;
date_str='';
if(len(ident)==18):
    summ=ident[0]*7+ident[1]*9+ident[2]*10+ident[3]*5+ident[4]*8+ident[5]*4+ident[6]*2+ident[7]+ident[8]*6+ident[9]*3+ident[10]*7+ident[11]*9+ident[12]*10+ident[13]*5+ident[14]*8+ident[15]*4+ident[16]*2;
    a=int(summ)%11;
    if(int(ident[16])%2!=0):sax=1;
    else :sax=0;
    for i in range (6,14):
        date_str+=str(ident[i]);
    try:
        date=datetime.strptime(date_str,"%Y%m%d")
    except ValueError:
        key=False;
    if(int(li[a])==int(ident[17])):
        if(key==True):
            print('身份证号码校验为合法号码');
            print('出生：{}年{}月{}日'.format(date.year,date.month,date.day));
            if(sax==1):print('性别：男');
            else: print('性别：女');
        if(key==False):print('身份证校验错误');
    if(int(li[a])!=int(ident[17])):print('身份证校验错误');
if(len(ident)!=18):print('身份证校验错误');
