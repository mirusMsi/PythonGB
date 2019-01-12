
__author__ = 'Сергей Иванович Мирошкин (miroshkin.mirus@ya.ru)'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.


def task_1():
    while True:
        number = input('Enter some integer or "no" for exit: ')

        if number.lower() == 'no':
            break

        try:
            int(number)
            maximum = 0
            i = 0

            while i < len(number):
                check = int(number[i:(i + 1)])
                if maximum < check:
                    maximum = check
                i += 1

            print(maximum)

            break

        except ValueError:
            print('You entered not integer, please will try again.')


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.


def task_2():

    value_one = input('Enter some first value: ')
    value_two = input('Enter some second value: ')

    value_one, value_two = value_two, value_one

    print(value_one, value_two, sep='\n')


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4


def main():
    want = "yes"
    amount_tasks = 3
    welcome = f"Enter task's number which you want to check (integer from 1 to {amount_tasks} or 'no' for exit): "

    while True:
        task = input(welcome)

        if task.lower() == 'no':
            want = task.lower()
            break
        else:
            try:
                int(task)
                task = int(task)
                if 0 < task <= amount_tasks:
                    break
                else:
                    print('You entered incorrect number, please will try again.')
            except ValueError:
                print('You entered not integer, please will try again.')

    if want == 'yes':
        num = "task_" + f"{task}"
        fun = globals()[num]
        fun()


main()
