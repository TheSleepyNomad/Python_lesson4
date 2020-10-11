"""
    4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
обязательно использовать генератор.
"""

from random import randrange as rr
# Создаем список чисел с помощью генератора
rand_list = [rr(30) for _ in range(rr(1, 30))]
# Создаем новый список чисел элементы которого соответствуют требованию, а именно не имеют повторений в rand_list
result = [i for i in rand_list if rand_list.count(i) == 1]
# Выводим изначальный и новый список чисел
print(rand_list)
print(result)