def greet(*args):
    greeting = f"Hello, {args[0]}"
    if len(args) < 2:
        return greeting + "!"
    else:
        for i in range(1, len(args)):
            greeting = greeting + f" and {args[i]}"
    return greeting + "!"

greet("Goga", "Jack", "Pups")