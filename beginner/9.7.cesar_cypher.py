shift = int(input())
message = input()
decoded_message = ""

for ch in message:
    if ord(ch) - shift < 97:
        new_letter = chr(ord(ch) + 26 - shift)
    else:
        new_letter = chr(ord(ch) - shift)
    decoded_message = decoded_message + new_letter
print(decoded_message)
