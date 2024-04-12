s=input();
ls=list(s);
num='';
n=str(ls[len(ls)-1]);
for i in range(0,len(ls)-1):
    num+=str(ls[i]);
num=int(num);
print(num);
if(num>0 and num<=17):
    if(n=='A' or n=='F' or n=='a' or n=='f'):print('窗口');
    elif(n=='B' or n=='b'):print('中间');
    elif(n=='C' or n=='D' or n=='c' or n=='d'):print('过道');
    else :print('输入错误');
else:print('输入错误');
