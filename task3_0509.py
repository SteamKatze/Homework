try:
    # Користувач вводить перше число
    num1 = float(input("Введіть перше число: "))

    # Користувач вводить друге число
    num2 = float(input("Введіть друге число: "))

    # Користувач обирає математичну операцію
    operation = input("Виберіть операцію (+, -, *, /): ")

    # Обчислюємо, згідно обраної математичної операції
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        # Перевіряємо, чи друге число не дорівнює нулю при діленні
        if num2 == 0:
            raise ValueError("Ділення на нуль неможливе")
        result = num1 / num2
    else:
        raise ValueError("Введено неправильну операцію")

    # Виводимо результат
    print(f"Результат: {result}")

except ValueError as e:
    # Обробка помилок вводу або ділення на нуль
    print(f"Помилка: {e}")
except ZeroDivisionError:
    # Обробка помилки ділення на нуль
    print("Ділення на нуль неможливе")
except Exception as e:
    # Обробка інших невідомих помилок
    print(f"Сталася невідома помилка: {e}")
