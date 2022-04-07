# ## Задача 1. Генерация списка
# Дано целое число N. Напишите программу, которая
# формирует список из нечетных чисел от 1 до N.
#
# Пример 1
# ```
# Введите число: 1
#
# Список из нечётных чисел от 1 до N: [1]
# ```
#
# Пример 2
# ```
# Введите число: 14
#
# Список из нечётных чисел от 1 до N: [1, 3, 5, 7, 9, 11, 13]
# ```

n = int(input('Введите целое число N: '))
n_list = []

for i in range(1, n + 1, 2):
    n_list.append(i)

print('Список из нечётных чисел от 1 до N:', n_list)

