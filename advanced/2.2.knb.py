timur = input()
ruslan = input()

timur_list = ['каменьножницы', 'ножницыбумага', 'бумагакамень']

if timur + ruslan in timur_list:
    print("Тимур")
else:
    if timur == ruslan:
        print("ничья")
    else:
        print("Руслан")
