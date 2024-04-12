n=int(input());
a=n%10;#个位
b=int(n/10%10);#十位
c=int(n/100);#百位
new=a*100+b*10+c;
print(new);
