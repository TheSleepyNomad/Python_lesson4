"""
    6. Реализовать два небольших скрипта:
    а) итератор, генерирующий целые числа, начиная с указанного,
    б) итератор, повторяющий элементы некоторого списка, определенного заранее.
    Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не
должен быть бесконечным. Необходимо предусмотреть условие его завершения.
"""
from itertools import cycle, count
from random import randrange as rr


print("а) итератор, генерирующий целые числа, начиная с указанного")
stop_number = 0
try:
    for numb in count(int(input("Введите целое число, с которого нужно начать генерацию чисел: "))):
        if stop_number > 10:
            break
        stop_number += 1
        print(numb, end=" ")
except ValueError:
    print("Введите цифру!!!")

print("\nб) итератор, повторяющий элементы некоторого списка, определенного заранее.")
stop_number = 0
for numb in cycle([rr(50) for x in range(rr(1, 20))]):
    if stop_number > 20:
        break
    stop_number += 1
    print(numb, end=" ")
