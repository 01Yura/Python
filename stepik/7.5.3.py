num=int(input())
mx=0
mn=9
while num!=0:
    last_digit=num%10
    num//=10
    if last_digit>mx:
        mx=last_digit
    if mn>=last_digit:
        mn=last_digit
print('Максимальная цифра равна', mx)
print('Минимальная цифра равна', mn)


x = input()
print('Максимальная цифра равна', max(x))
print('Минимальная цифра равна', min(x))

n = int(input())
max_digit = 0
min_digit = 9
while n > 0:
    cur_digit = n % 10
    max_digit = max(max_digit, cur_digit)
    min_digit = min(min_digit, cur_digit)
    n //= 10
print("Максимальная цифра равна", max_digit)
print("Минимальная цифра равна", min_digit)