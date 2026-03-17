tuples = [(1, 2), (), (3,), ()]
print([t for t in tuples if len(t) != 0])
