def hide_card(s: str):
    if " " in s:
        s = s.replace(" ", "")
    l = list(s)
    for i in range(0,12):
        l[i] = "*"
    new_s = "".join(l)
    return new_s


print(hide_card("1234567890123456"))