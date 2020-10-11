"""
    7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1!
и до n!.
"""
from itertools import count as ct
from functools import reduce


def fact(n):
    fact = n + 1
    n = 0
    for num in ct():
        n += 1
        fact_list = [num for num in range(1, n+1)]
        fact_num = reduce(lambda x, y: x * y, fact_list)
        if n == fact:
            break
        yield f"Факториал {n}! равен {fact_num}"


try:
    user_fact = int(input("Введите факториал числа: "))
    for _ in fact(user_fact):
        print(_)

except ValueError:
    print("Вводите только цифры")

