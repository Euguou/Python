age,rate=map(float,input().split(','));
low=(220-age-rate)*0.6+rate;
high=(220-age-rate)*0.8+rate;
print('{}'.format(low)+'~'+'{}'.format(high));
