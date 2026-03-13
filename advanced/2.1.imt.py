mass = float(input())
height = float(input())

imt = mass/height**2

if imt < 18.5:
    print("Недостаточная масса")
elif imt <= 25:
    print("Оптимальная масса")
else:
    print("Избыточная масса")
