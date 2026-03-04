string_original = input()
english = "eyopaxcETOPAHXCBM"
russian = "еуорахсЕТОРАНХСВМ"
string_new = ""
for ch in string_original:
    if ch in english:
        index = english.find(ch)
        string_new = string_new + russian[index]
    else:
        string_new += ch

old_sum = 0
for ch in string_new:
    amount = ord(ch) * 3
    old_sum += amount

new_sum = 0
for ch in string_original:
    amount = ord(ch) * 3
    new_sum += amount

print("Старая стоимость:", str(new_sum) + "🐝")
print("Новая стоимость:", str(old_sum) + "🐝")
