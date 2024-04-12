find=input();
s=input();
a=list(s);
key=True;
for i in range (0,len(a)):
    if(find==a[i]):
        print('index = {}'.format(i));
        key=False;
if(key==True): print("Not Found");
