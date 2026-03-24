def info_kwargs(**kwargs):
    sorted_dict = sorted(kwargs.items())
    for key, value in sorted_dict:
        print(f"{key}: {value}")


info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')
