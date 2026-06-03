user_input = input("Введите элементы массива через пробел: ")
A = list(map(float, user_input.split()))
n = len(A)

if n == 0:
    print("Массив пуст")
else:
    i = 0
    summa = 0
    while i < n:
        summa = summa + A[i]
        i = i + 1
    sred = summa / n
    print("Массив:", A)
    print("Среднее арифметическое:", sred)