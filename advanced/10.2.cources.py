courses = [
    {
        "course_number": "CS101",
        "room_number": 3004,
        "teacher": "Хайнс",
        "time": "8:00"
    },
    {
        "course_number": "CS102",
        "room_number": 4501,
        "teacher": "Альварадо",
        "time": "9:00"
    },
    {
        "course_number": "CS103",
        "room_number": 6755,
        "teacher": "Рич",
        "time": "10:00"
    },
    {
        "course_number": "NT110",
        "room_number": 1244,
        "teacher": "Берк",
        "time": "11:00"
    },
    {
        "course_number": "CM241",
        "room_number": 1411,
        "teacher": "Ли",
        "time": "13:00"
    }
]

number = input()
for d in courses:
    if d.get("course_number") == number:
        print(f"{number}: {d.get("room_number")}, {d.get("teacher")}, {d.get("time")}")

my_dict = {
    'CS101': ('3004', 'Хайнс', '8:00'),
    'CS102': ('4501', 'Альварадо', '9:00'),
    'CS103': ('6755', 'Рич', '10:00'),
    'NT110': ('1244', 'Берк', '11:00'),
    'CM241': ('1411', 'Ли', '13:00'),
}

course_number = input()
audience, teacher, time = my_dict[course_number]
print(f'{course_number}: {audience}, {teacher}, {time}')