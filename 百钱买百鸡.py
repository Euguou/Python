for i in range(1,100):#i为公鸡
    for j in range (1,100):#j为母鸡
        a=100-i-j;#a为小鸡
        mon=(i*5)+(j*3)+(a/3)
        if(mon==100):
            print(i,j,a);
            continue;
