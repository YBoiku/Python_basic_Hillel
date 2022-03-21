input_case = input("Выбери тип операции:\n1: Сложение\n2: Вычитание\n3: Умножение\n4: Деление"
                   "\n5: Возведение в степень\n6: Квадратный корень из числа\nВыбор операции: ")
return_case = int(input_case)
if return_case == 1:
    value_1 = float(input("Первое слагаемое: "))
    value_2 = float(input("Второе слагаемое: "))
    addition = value_1 + value_2
    print(addition)
elif return_case == 2:
    value_1 = float(input("Первое уменьшимое: "))
    value_2 = float(input("Второе вычитаемое: "))
    subtraction = value_1 - value_2
    print(subtraction)
elif return_case == 3:
    value_1 = float(input("Первый множитель: "))
    value_2 = float(input("Второй множитель: "))
    multiplication = value_1 * value_2
    print(multiplication)
elif return_case == 4:
    value_1 = float(input("Первое делимое: "))
    value_2 = float(input("Второй делитель: "))
    if value_2 != 0.0:
        division = value_1 / value_2
        print(division)
    else:
        print("На ноль делить нельзя")
elif return_case == 5:
    value_1 = float(input("Первый основание: "))
    value_2 = float(input("Второй показатель степени: "))
    exponentiation = value_1 ** value_2
    print(exponentiation)
elif return_case == 6:
    value_1 = float(input("Число под корнем: "))
    square_root = value_1 * 0.5
    print(square_root)
else:
    print("Вы ограниченны вышеперечисленным списком операций")