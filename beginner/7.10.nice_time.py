from math import pow

n = int(input())

for i in range(0, 1440):
    hours = i // 60
    minutes = i % 60
    if pow(hours, n) == minutes:
        if len(str(hours)) == 1:
            hours = "0" + str(hours)
        if len(str(minutes)) == 1:
            minutes = "0" + str(minutes)
        print(hours, ":", minutes, sep="")
