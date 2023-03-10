"""
По данному натуральному числу N найдите сумму чисел
1 + 1/1! + 1/2! + 1/3! + 1/N!
Количество действий должно быть пропорционально N.
"""
n = int(input())

fac = 1
sum = 1.0  # float

for i in range(1, n + 1):  # Проходимся по всем значениям от 1 до n
    fac *= i
    sum += 1 / fac  # Находим сумму

print(sum)
