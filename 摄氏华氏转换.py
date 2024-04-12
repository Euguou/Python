s=input();
ls=list(s);T=''
for i in range (0,len(ls)-1):
    T+=str(ls[i]);
T=float(T);
if(ls[len(ls)-1]=='C' or ls[len(ls)-1]=='c'):
    F= T*1.8 + 32;
    print('摄氏温度{}C转为华氏温度为{:.2f}F'.format(T,F));
elif(ls[len(ls)-1]=='F' or ls[len(ls)-1]=='f'):
    C=(T-32)/ 1.8;
    print('华氏温度{}F转为摄氏温度为{:.2f}C'.format(T,C));
else :print('Data error!');
    
