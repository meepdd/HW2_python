"""
Подсчитайте кол-во натуральных делителей числа х
(включая 1 и само число)
"""
x = int(input())
count = 0

for i in range(1, x + 1):  # Проходимся по всем значениям от 1 до n
    if x % i == 0:  #Если делится без остатка, то увеличиваем счетчик
        count += 1

print(count)