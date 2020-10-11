"""
    1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
import argparse

# Добавляем описание для программы
parser = argparse.ArgumentParser(
    description="Расчитывает заработную плату сотрудника по формуле (выработка в часах * ставка в час) + премия")

# Задаем позиционные аргументы, их тип данных и описание к ним
parser.add_argument('pph', type=int, help='production per hours/выработка в часах у сотрудника')
parser.add_argument('rph', type=int, help='rate per hour/ставка в час у сотрудника')

# Задаем премию в виде опционального аргумента
parser.add_argument('--prize', type=int, help='prize/премия для сотрудника', default=0)

# Присваеваем args "список" полученных от пользователя аргументы
args = parser.parse_args()


# Создаем функцию для расчета зарабатной платы сотрудника
def payroll(pph, rph, prize): return (pph * rph) + prize


print(f"Указанная выроботка: {args.pph}\nУказанная ставка: {args.rph}\nУказанная премия: {args.prize}")

# Расчитываем заработную плату сотрудника
print("Заработная плата сотрудника составляет: ", payroll(args.pph, args.rph, args.prize))