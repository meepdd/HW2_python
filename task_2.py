"""
Проверьте, есть ли среди данных N чисел нули.
Выведите YES, если среди введенных чисел есть хотя бы один нуль,
или NO в противном случае.
"""

N = int(input())

found_zero = False  # по умолчанию

# Вводим числа N
for i in range(N):
    num = int(input())
    if num == 0:  # если хотя бы одно число 0
        found_zero = True  # меняем на True

if found_zero:
    print("YES")
else:
    print("NO")
