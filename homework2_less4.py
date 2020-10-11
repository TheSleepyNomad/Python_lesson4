"""
    2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше
предыдущего элемента.
    Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор
    Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
    Результат: [12, 44, 4, 10, 78, 123].
"""
from random import randrange as rr

# В rand_list генерируется список случайной длины(от 1 до 20 элем.) и случайными элементам
rand_list = [rr(500) for _ in range(rr(1, 20))]
result = []
print(rand_list)

if len(rand_list) > 1:
    for val in range(1, len(rand_list)):
        if rand_list[val] > rand_list[val - 1]:
            result.append(rand_list[val])
else:
    result.append(rand_list[-1])

print(result)
