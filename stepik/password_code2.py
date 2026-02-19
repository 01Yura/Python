import string
import math

def password_strength(password):
    length = len(password)
    possible_characters = 0
    
    # Check the character set used in the password
    if any(c.islower() for c in password):
        possible_characters += len(string.ascii_lowercase)
    if any(c.isupper() for c in password):
        possible_characters += len(string.ascii_uppercase)
    if any(c.isdigit() for c in password):
        possible_characters += len(string.digits)
    if any(c in string.punctuation for c in password):
        possible_characters += len(string.punctuation)
    
    # Total possible combinations
    total_combinations = possible_characters ** length
    
    # Assume a brute force attacker can test 1,000,000 passwords per second
    attempts_per_second = 1_000_000
    seconds_to_crack = total_combinations / attempts_per_second
    
    # Convert seconds to more understandable time units
    minutes_to_crack = seconds_to_crack / 60
    hours_to_crack = minutes_to_crack / 60
    days_to_crack = hours_to_crack / 24
    years_to_crack = days_to_crack / 365
    
    return total_combinations, seconds_to_crack, minutes_to_crack, hours_to_crack, days_to_crack, years_to_crack

def main():
    password = input("Введите пароль для проверки: ")
    total_combinations, seconds, minutes, hours, days, years = password_strength(password)
    
    print(f"Общее количество возможных комбинаций: {total_combinations}")
    print(f"Время для взлома пароля методом BruteForce:")
    print(f" - секунд: {seconds:.2f}")
    print(f" - минут: {minutes:.2f}")
    print(f" - часов: {hours:.2f}")
    print(f" - дней: {days:.2f}")
    print(f" - лет: {years:.2f}")

if __name__ == "__main__":
    main()
