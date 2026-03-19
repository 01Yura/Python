dict1 = {'apple': 7, 'orange': 2, 'peach': 5}
dict2 = {'kiwi': 1, 'apple': 6, 'orange': 2}

dict3 = {}
for key in dict1:
    dict3[key] = dict1.get(key, 0) + dict2.get(key, 0)
for key in dict2:
    dict3[key] = dict1.get(key, 0) + dict2.get(key, 0)
print(dict3)
