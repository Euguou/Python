def delete_extra_zero(n):
    if isinstance(n, int):    
        return n
    if isinstance(n, float):     
        n = str(n).rstrip('0') 
        n = int(n.rstrip('.')) if n.endswith('.') else float(n)  
        return n
a=float(input());b=float(input());c=float(input());
S=a+b+c;
average=S/3;
print('三数之和为{}'.format(delete_extra_zero(S)));
print('三数均值为{}'.format(average));
