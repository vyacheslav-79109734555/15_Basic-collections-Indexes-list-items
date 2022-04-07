# Задача 7. Контейнеры.
# Контейнеры на складе лежат в ряд в порядке не возрастания своей массы (в килограммах).
# На склад привезли ещё один контейнер, который также нужно положить на определённое место.
#
# Напишите программу, которая получает на вход невозрастающую последовательность натуральных
# чисел, означающих массу каждого контейнера в ряду.
# После этого вводится число X – масса нового контейнера.
# Программа выводит номер, под которым будет лежать новый контейнер.
# Если в ряде есть контейнеры с одинаковой массой, таким же, как у нового, то его нужно положить после них.
# Обеспечьте контроль ввода: все числа целые и не превышают 200.
#
# #### Пример:
# ```
# Кол-во контейнеров: 8
# Введите вес контейнера: 165
# Введите вес контейнера: 163
# Введите вес контейнера: 160
# Введите вес контейнера: 160
# Введите вес контейнера: 157
# Введите вес контейнера: 157
# Введите вес контейнера: 155
# Введите вес контейнера: 154
# Введите вес нового контейнера: 162
# Номер, куда встанет новый контейнер: 3
# ```


my_arr = []
a = int(input('Кол-во контейнеров: '))


def input_control(a):
    for i in range(a):
        n = input('Введите вес контейнера: ')
        if len(n) > 0 and n.isdigit() > 0 and int(n) < 200:
            my_arr.append(n)
        else:
            print('ошибка')

    return my_arr


input_control(a)

if len(my_arr) < a:
    a = a - len(my_arr)
    input_control(a)

print('список контейнеров:', my_arr)

y = int(input('Введите вес нового контейнера: '))
x = 1
for i in range(len(my_arr)):
    if int(my_arr[i]) >= y and i < len(my_arr):
        x += 1

print('Номер, куда встанет новый контейнер: ', x)
my_arr.insert(x - 1, str(y))

print('новый список контейнеров:', my_arr)
