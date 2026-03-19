text = 'bridge snake island game glory eye arrogant car nature game glory game'
li = text.split()
d = {}

for word in li:
    d[word] = d.get(word, 0) + 1

li_max = list()
max_value = max(d.values())
for key, value in d.items():
    if max_value == value:
        li_max.append(key)

li_max.sort()
print(li_max[0])
