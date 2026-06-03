N = int(input("Введите число N: "))

if N < 0:
    print("N не может быть отрицательным")
else:
    i = 1
    summa = 0
    while i <= N:
        summa = summa + i * i
        i = i + 1
    print(f"Сумма квадратов чисел от 1 до {N}: {summa}")