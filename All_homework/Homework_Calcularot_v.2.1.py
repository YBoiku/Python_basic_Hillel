while True:
    input_case = input("Выбери тип операции:\n1: Сложение\n2: Вычитание\n3: Умножение\n4: Деление"
                       "\n5: Возведение в степень\n6: Квадратный корень из числа\nВыбор операции: ")
    if input_case in "123456":
        try:
            if input_case == "1":
                value_1 = float(input("Первое слагаемое: "))
                value_2 = float(input("Второе слагаемое: "))
                result = value_1 + value_2
            elif input_case == "2":
                value_1 = float(input("Первое уменьшаемое: "))
                value_2 = float(input("Второе вычитаемое: "))
                result = value_1 - value_2
            elif input_case == "3":
                value_1 = float(input("Первый множитель: "))
                value_2 = float(input("Второй множитель: "))
                result = value_1 * value_2
            elif input_case == "4":
                value_1 = float(input("Первое делимое: "))
                value_2 = float(input("Второй делитель: "))
                result = value_1 / value_2
            elif input_case == "5":
                value_1 = float(input("Первый основание: "))
                value_2 = float(input("Второй показатель степени: "))
                result = value_1 ** value_2
            elif input_case == "6":
                value_1 = float(input("Число под корнем: "))
                result = value_1 ** 0.5
            else:
                result = "Необходимо выбрать одну из перечисленных возможностей"
            print(result)
        except ValueError:
            print("Необходимо ввести число")
        except ZeroDivisionError:
            print("Нельзя делить на ноль")
    else:
        print("Необходимо выбрать одну из перечисленных возможностей")

    new_start = input("Хотите посчитать еще раз? Любая кнопка/N: ").lower()
    if new_start == "n":
        break