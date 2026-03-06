n = int(input())
previous_book = input()
flag = "YES"
for i in range(n - 1):
    book = input()

    index_previous_book = previous_book.find(" ")
    index_book = book.find(" ")
    author_previous_book = previous_book[:index_previous_book]
    author_book = book[:index_book]
    if author_previous_book < author_book:
        previous_book = book
        continue
    elif author_previous_book == author_book:
        title_previous_book = previous_book[index_previous_book + 2:]
        title_book = book[index_book + 2:]
        if title_previous_book < title_book:
            previous_book = book
            continue

    flag = "NO"

print(flag)
