for i in range(1000,10000):
    a=int(i%10);
    b=int(i/10%10);
    c=int(i/100%10);
    d=int(i/1000);
    n=(a**4)+(b**4)+(c**4)+(d**4);
    if(i==n):  
        print(i);
    i+=1;
