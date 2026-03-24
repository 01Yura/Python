def mean(*args):
    li = []
    for el in args:
        if type(el) == type(1) or type(el) == type(0.5):
            li.append(el)
    if len(li) == 0:
        return 0
    else:
        return sum(li) / len(li)


print(mean(3, 2.5, 0.5, "srt"))
