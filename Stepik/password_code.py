lenght=int(input('Enter your Wi-FI password lenght: '))
print('What symbols do you use in this password?')
digits=input('Do you use digits?   y/n  ')
upper_case=input('Do you use uppercase letters?   y/n  ')
lower_case=input('Do you use lowercase letters?   y/n  ')
spec_symb=input('Do you use special symbols like  @&*+-$  and others?   y/n  ')
k=0
if digits=='y':
      k=k+10
if upper_case=='y':
      k=k+26
if lower_case=='y':
      k=k+26
if spec_symb=='y':
      k=k+31
pass_comb=lenght**k
print('Amount combinations of your password: ', pass_comb)
vga_speed_per_sec=200000
minutes=pass_comb/vga_speed_per_sec/60
hours=minutes/60
days=hours/24
months=days/30.5
years=months/12
century=years/100
print('Using Video Card that costs around 100$ your password can be hacked in:' )
if pass_comb>10**20: 
    print("Several millions years")
elif pass_comb>10**13: 
    print(round(years,1), 'years')
elif pass_comb>10**12:
    print(round(months,1), 'months')
elif pass_comb>10**10:
    print(round(days,1), 'days')
elif pass_comb>10**9:
    print(round(hours,1), 'hours')
elif pass_comb<=10**9:    
    print(round(minutes,1), 'minutes')