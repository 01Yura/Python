tuples = [(46, 82), (75,), (3, -4, -10)]
end_list = []
for t in tuples:
    li = list(t)
    li[-1] = 100
    end_list.append(tuple(li))

print(end_list)


