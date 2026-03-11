# объявление функции
def math_round_to_int(num):
    nums = str(num).split(".")
    if int(nums[1][0]) >= 5:
        return int(num + 1)
    else:
        return int(num)


# считываем данные
num = float(input())

# вызываем функцию
print(math_round_to_int(num))
