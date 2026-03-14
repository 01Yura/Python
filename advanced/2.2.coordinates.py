n = int(input())
position = [0, 0, 0, 0]
for i in range(n):
    dot = input().split(" ")
    if int(dot[0]) > 0:
        if int(dot[1]) > 0:
            position[0] = position[0] + 1
        elif int(dot[1]) < 0:
            position[3] = position[3] + 1
    elif int(dot[0]) < 0:
        if int(dot[1]) > 0:
            position[1] = position[1] + 1
        elif int(dot[1]) < 0:
            position[2] = position[2] + 1

print(f"Первая четверть: {position[0]}")
print(f"Вторая четверть: {position[1]}")
print(f"Третья четверть: {position[2]}")
print(f"Четвертая четверть: {position[3]}")
