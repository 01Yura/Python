string = input().lower()
words = string.split()

print("Общее количество артиклей:", words.count("a") + words.count("an") + words.count("the"))
