def calculated():
    try:
        input_case = input("Выбери тип операции:\n1: Сложение\n2: Вычитание\n3: Умножение\n4: Деление"
                           "\n5: Возведение в степень\n6: Квадратный корень из числа\nВыбор операции: ")
        return_case = int(input_case)
        if return_case == 1:
            try:
                value_1 = float(input("Первое слагаемое: "))
                value_2 = float(input("Второе слагаемое: "))
                addition = value_1 + value_2
                print(addition)
            except ValueError:
                print("Необходимо ввести число")
        elif return_case == 2:
            try:
                value_1 = float(input("Первое уменьшаемое: "))
                value_2 = float(input("Второе вычитаемое: "))
                subtraction = value_1 - value_2
                print(subtraction)
            except ValueError:
                print("Необходимо ввести число")
        elif return_case == 3:
            try:
                value_1 = float(input("Первый множитель: "))
                value_2 = float(input("Второй множитель: "))
                multiplication = value_1 * value_2
                print(multiplication)
            except ValueError:
                print("Необходимо ввести число")
        elif return_case == 4:
            try:
                value_1 = float(input("Первое делимое: "))
                value_2 = float(input("Второй делитель: "))
                if value_2 != 0.0:
                    division = value_1 / value_2
                    print(division)
                else:
                    print("На ноль делить нельзя")
            except ValueError:
                print("Необходимо ввести число")
        elif return_case == 5:
            try:
                value_1 = float(input("Первый основание: "))
                value_2 = float(input("Второй показатель степени: "))
                exponentiation = value_1 ** value_2
                print(exponentiation)
            except ValueError:
                print("Необходимо ввести число")
        elif return_case == 6:
            try:
                value_1 = float(input("Число под корнем: "))
                square_root = value_1 ** 0.5
                print(square_root)
            except ValueError:
                print("Необходимо ввести число")
        else:
            print("Вы ограниченны вышеперечисленным списком операций")
    except ValueError:
        print("Необходимо ввести число из тех что перечисленны")


calculated()
while True:
    new_start = (input("еще раз? Да/Нет: ")).lower()
    if new_start == 'да':
        calculated()
    else:
        break
