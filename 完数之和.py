summ=0
n=int(input());
for j in range(1,n):
    ans=0;
    for i in range(1,j):
        if(j%i==0):
            ans+=i;
    if(ans==j):
        summ+=j;
    else :continue;
print(summ);
