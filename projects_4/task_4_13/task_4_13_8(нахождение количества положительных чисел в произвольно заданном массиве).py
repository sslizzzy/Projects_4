user_input = input("Введите элементы массива через пробел: ")
A = list(map(float, user_input.split()))
n = len(A)

i = 0
count = 0
while i < n:
    if A[i] > 0:
        count = count + 1
    i = i + 1
print("Массив:", A)
print("Количество положительных чисел:", count)