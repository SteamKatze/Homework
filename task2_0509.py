try:
    # Користувач вводить перше число
    number1 = float(input("Введіть перше число: "))

    # Користувач вводить друге число
    number2 = float(input("Введіть друге число: "))

    if number1 == number2:
        print("Числа рівні.")
    else:
        # Сортуємо числа у порядку зростання
        sorted_numbers = [number1, number2]
        sorted_numbers.sort()

        print(f"Числа у порядку зростання: {sorted_numbers[0]}, {sorted_numbers[1]}")

except ValueError:
    print("Введено некоректні дані. Будь ласка, введіть число.")