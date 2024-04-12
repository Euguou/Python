from queue import Queue;
n=int(input());
prime=Queue();
key=True;
factor = [];
for i in range (2,n-1):
    if(n%i==0):
        factor.append(i);
if len(factor) == 0:
    print(n);
for i in range (0,len(factor)):
    for j in range(2,factor[i]-1):
        if(factor[i]%j==0):
            key=False;
            break;
    if(key==True): print(factor[i]);
