def delete_extra_zero(n):
    if isinstance(n, int):    
        return n
    if isinstance(n, float):     
        n = str(n).rstrip('0') 
        n = int(n.rstrip('.')) if n.endswith('.') else float(n)  
        return n
a=int(input());b=int(input());
ch=a-(b-2*a)/2;rabbit=(b-2*a)/2;
print('{},{}'.format(delete_extra_zero(ch),delete_extra_zero(rabbit)));
