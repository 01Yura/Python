class Cat:
    """Класс, описывающий кошку"""
    night_vision = True
    paws_count = 4

cat = Cat()
cat2 = Cat()

cat.breed = 'Британский'
cat.name = 'Кемаль'
cat.age = 1

cat2.color = "Синий"

print(cat.breed, cat.name)        # обращение к атрибутам
print(cat2.color)

cat.age += 2                      # изменение значения атрибута
print(cat.age)

print(dir(cat))
print(dir(cat2))
print("------------")
Cat.paws_count = 90
print(cat.paws_count)
cat.paws_count = 1
print(cat.paws_count)
print(Cat.paws_count)
print(cat.__dict__)
print(Cat.__dict__)
print(Cat.__doc__)
print(cat.__class__)