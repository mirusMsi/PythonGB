
__author__ = 'Сергей Иванович Мирошкин (miroshkin.mirus@ya.ru)'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.


def task_first():
    number = str(input('Enter some integer:\n'))
    answer = []
    length = len(number)

    for i in range(length):
        answer.append(int(number[i:(i + 1)]))

    for i in range(length):
        print(answer[i])


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

value_one = input('Enter some first value:\n')
value_two = input('Enter some second value:\n')

buffer = value_one
value_one = value_two
value_two = buffer

print(value_one, "\n", value_two)


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

def main():
    task = 0

    while True:
        task = input("Enter task's number which you want to check (integer from one to three or 'no' for exit): ")
        if isinstance(task, int):
            if 0 < task < 4:
                break
            else:
                print('You entered incorrect number, please will try again.')
        else:
            print('You entered not integer, please will try again.')

    if task == 1:
        task_first()
    elif task == 2:

main()
