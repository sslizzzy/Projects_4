user_input = input("Введите элементы массива через пробел: ")
A = list(map(float, user_input.split()))
n = len(A)

i = 0
summa = 0
count = 0

while i < n:
    if i % 2 == 0:  
        summa = summa + A[i]
        count = count + 1
    i = i + 1

if count == 0:
    print("Нет элементов с чётными индексами")
else:
    sred = summa / count
    print("Массив:", A)
    print("Индексы начинаются с 0")
    print("Среднее арифметическое элементов с чётными индексами:", sred)