from datetime import datetime
st=input();
n=int(input());
for i in range (0,n):
    print(st,end='');
print('',end='\n');
date=input();
date_obj = datetime.strptime(date, "%Y/%m/%d");
date_str = date_obj.strftime("%Y年%m月%d日");
print(date_str)
for i in range (0,n):
    print(st,end='');
