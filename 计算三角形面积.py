a,b,c=map(float,input().split(','));
p=(a+b+c)/2;
S=(p*(p-a)*(p-b)*(p-c))**(1/2);
print('{:.3f}'.format(S)); 
