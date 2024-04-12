n = int(input());
for i in range (1,1+n):
   for j in range(1,1+i):
        ans=i*j;
        ans=str(ans);
        ans=ans.ljust(3);
        if(i!=j) :
            print('{}*{}={}'.format(i,j,ans),end='');
        if(i==j) :
            print('{}*{}={}'.format(i,j,ans),end='\n');
