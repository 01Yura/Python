month = int(input())

if month == 2:
    print(28)
elif (month <= 7 and month % 2 != 0) or (month>7 and month % 2 == 0):
    print(31)
else:
    print(30)
