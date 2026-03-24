import timeit

def comp():
    return [x * x for x in range(1000000)]

def loop():
    result = []
    for x in range(1000000):
        result.append(x * x)
    return result

print("comprehension:", timeit.timeit(comp, number=10))
print("loop:", timeit.timeit(loop, number=10))

# comprehension: 9.7595524999997
# loop: 10.159445500001311