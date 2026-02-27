num = int(input())
cnt = 0
total = 0
flag = True
last_2_digits = num % 100
if last_2_digits == 11:
    print("0" + "/" + "0")
    flag = False

while flag:
    total += 1
    if len(str(num)) > 7:
        cnt += 1
    num = int(input())
    last_2_digits = num % 100
    if last_2_digits == 11 and len(str(num)) > 7:
        total += 1
        cnt += 1
        break
    elif last_2_digits == 11:
        total += 1
        break

print(cnt, '/', total, sep='')
