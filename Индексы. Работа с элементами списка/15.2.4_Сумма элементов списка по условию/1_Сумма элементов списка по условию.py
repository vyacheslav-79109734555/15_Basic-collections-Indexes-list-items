print('Задача 2. СУММА ВСЕХ ЭЛЕМЕНТОВ В МАССИВЕ, КРАТНАЯ ДАННОМУ ЧИСЛУ K')


# Пользователь вводит список из N чисел и число K.
# Напишите код, выводящий на экран сумму элементов списка, которые кратны K.
#
# Пример:
# Кол-во чисел в списке: 7
# Введите 1 число: 15
# Введите 2 число: 16
# Введите 3 число: 10
# Введите 4 число: 9
# Введите 5 число: 6
# Введите 6 число: 7
# Введите 7 число: 17

# Введите делитель: 3
# Индекс числа 15: 0
# Индекс числа 16: 1
# Индекс числа 10: 2
# Индекс числа 9: 3
# Индекс числа 6: 4
# Индекс числа 7: 5
# Индекс числа 17: 6
# Сумма индексов: 30

def find_Sum(arr, n, k):
    sum = 0
    for i in range(n):
        if arr[i] % k == 0:
            sum += arr[i]
    return sum


arr = []
n = int(input('Кол-во чисел в списке: '))
for i in range(1, n + 1):
    print('Введите', i, 'число:', end=' ')
    numb = int(input())
    arr.append(numb)
print(arr)
k = int(input('Введите делитель: '))

N = (find_Sum(arr, n, k))
print('Сумма элементов списка: ', N)
