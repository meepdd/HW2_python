"""
Определите среднее арифметическое элементов последовательности,
завершающейся числом 0.
Число 0 в последовательность не входит.
Числа, следующие за нулем, считывать не нужно.
"""

count = 0
total = 0

while True:  # Цикл до тех пор, пока мы не встретим ноль
    numb = int(input())
    if numb == 0:
        break
    count += 1  # Добавить число к текущему итогу
    total += numb  # Увеличиваем счет

if count > 0:  # Если мы встретили хотя бы одно число
    mean = total / count
    print(mean)
else:
    print("None")
