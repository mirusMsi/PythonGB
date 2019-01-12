
__author__ = 'Сергей Иванович Мирошкин (miroshkin.mirus@ya.ru)'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.


def task_1():

    answer = []

    while True:
        number = input('Enter some integer or "no" for exit: ')

        if number.lower() == 'no':
            break

        try:
            int(number)
            length = len(number)

            for i in range(length):
                answer.append(int(number[i:(i + 1)]))

            for i in range(length):
                print(answer[i])

            break

        except ValueError:
            print('You entered not integer, please will try again.')

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!


def task_2():

    value_one = input('Enter some first value: ')
    value_two = input('Enter some second value: ')

    buffer = value_one
    value_one = value_two
    value_two = buffer

    print(value_one, value_two, sep='\n')


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"


def task_3():

    while True:
        age = input('Enter your age (it should be integer) or "no" for exit: ')

        if age.lower() == 'no':
            break

        try:
            int(age)
            if int(age) < 18:
                print('Извините, пользование данным ресурсом только с 18 лет')
            else:
                print('Доступ разрешен.')
            break
        except ValueError:
            print('You entered not integer, please will try again.')


def head():
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


head()
