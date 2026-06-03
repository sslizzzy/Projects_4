user_input = input("Введите элементы массива через пробел: ")
A = list(map(float, user_input.split()))
n = len(A)

i = 0
summa = 0
while i < n:
    if i % 2 != 0:  
        summa = summa + A[i]
    i = i + 1
print("Массив:", A)
print("Индексы начинаются с 0")
print("Сумма элементов с нечётными индексами:", summa)