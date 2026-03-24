# words = ["eat", "tea", "tan", "ate", "nat", "bat"]

# [
#     ["eat", "tea", "ate"],
#     ["tan", "nat"],
#     ["bat"]
# ]

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
sorted_words = ["".join(sorted(word)) for word in words]



unique_words = set(sorted_words)


common_list = []
for el in sorted(unique_words):
    li = []
    for i in range(len(sorted_words)):
        if el == sorted_words[i]:
            li.append(words[i])
    common_list.append(li)

print(common_list)


# Мое решение
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = {}

for word in words:
    key = "".join(sorted(word))
    groups.setdefault(key, []).append(word)

print(list(groups.values()))
