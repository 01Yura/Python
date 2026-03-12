import random


def is_valid(n):
    if n.isdigit() and 1 <= int(n) <= 100:
        return True
    else:
        return False


flag = True
while flag:
    num = random.randint(1, 100)
    counter = 0
    print('Добро пожаловать в числовую угадайку.')
    print('Я загадал число от 1 до 100, попробуйте угадать')
    print()
    n = input('Введите целое число от 1 до 100: ')
    while True:
        if not is_valid(n):
            n = input('А может быть все-таки введем целое число от 1 до 100? ')
            continue
        else:
            n = int(n)

        if n < num:
            counter += 1
            print('Ваше число меньше загаданного, попробуйте еще разок')
            n = input()
            continue
        elif n > num:
            counter += 1
            print('Ваше число больше загаданного, попробуйте еще разок')
            n = input()
            continue
        else:
            print(f'Вы угадали, поздравляем! Это было число {n}.')
            print(f'Количество попыток: {counter}')
            print('Спасибо, что играли в числовую угадайку. Если хотите сыграть еще раз? Введите - да: ')
            flag = input().lower()
            print()
            if flag == "да":
                flag = True
            else:
                flag = False

            break
