s=input();
ls=list(s);
L=0; D=[];key=True;
for i in range(0,len(ls)):
    if(ls[i]=='L'): L+=1;
    D.append('1')
    if(ls[i]=='D'): D[i]=0;
for i in range(0,len(ls)-2):
    if(D[i]==0 and D[i+1]==0 and D[i+2]==0): key=False;
if(key==True and L<=1):print('YES');
else :print('NO')
