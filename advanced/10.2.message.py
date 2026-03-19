d = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " "
}


numbers = ""
message = input()
for ch in message:
    for key in d:
        if ch.upper() in d.get(key):
            numbers+=key*(d.get(key).index(ch.upper()) + 1)

print(numbers)

