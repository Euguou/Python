from queue import Queue 
n=int(input());
q=Queue();
def num(a):
    for i in range (2,a):
        key=True;
        for j in range(1,i):
            if(j==1):continue;
            if(i%j==0):
                key=False;
                break;
        if(key==True):q.put(i);
num(n);
ans=0;
for i in range (0,q.qsize()):
    ans+=q.get();
print(ans);



    
