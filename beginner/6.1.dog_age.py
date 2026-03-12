dog_age = int(input())

human_age = 0
if dog_age <= 2:
    human_age = dog_age * 10.5
if dog_age > 2:
    human_age = 2 * 10.5 + (dog_age - 2) * 4
print(human_age)
