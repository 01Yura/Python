list_of_words = input().split()
s = ""
for element in list_of_words:
    s = s + element[0] + ". "
s = s[:len(s) -1]
