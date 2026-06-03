N = int(input("Сколько чисел вы хотите ввести? "))

if N <= 0:
    print("Количество чисел должно быть больше 0")
else:
    max_num = float(input("Введите число 1: "))
    i = 2
    while i <= N:
        num = float(input(f"Введите число {i}: "))
        if num > max_num:
            max_num = num
        i = i + 1
    print("Максимальное число:", max_num)