n = int(input());
ans=0;i=1;
while i<=n:
    a = i%10;
    if(a==3):
        ans+=i;
    i+=1;
print(ans);
