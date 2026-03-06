a, b, c, d = input(), input(), input(), input()

max_string = max(a, b, c, d)
min_string = min(a, b, c, d)

last_max_char = max_string[-1]
last_min_char = min_string[-1]

last_max_char_index = ord(last_max_char)
last_min_char_index = ord(last_min_char)

print((last_max_char_index * last_min_char_index) ** 2)
