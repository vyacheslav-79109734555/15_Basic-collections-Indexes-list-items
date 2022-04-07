print('Задача 3. Меняет местами наибольший и наименьший элементы в списке')


# В собачьих бегах участвует N собак, у каждой из них есть определённое количество очков за сезон.
# На огромном табло выводятся очки каждой собаки.
# Однако при выводе был обнаружен баг: собаки с наибольшим
# и наименьшим количеством очков поменялись местами!
# Нужно это исправить.
# Дан список очков из N собак.
# Напишите программу, которая меняет местами наибольший и наименьший элементы в списке.

def large(arr):
    max_ = arr[0]
    for ele in arr:
        if ele > max_:
            max_ = ele

    return max_


def small(arr):
    min_ = arr[0]
    for ele in arr:
        if ele < min_:
            min_ = ele

    return min_


arr = []
n = int(input('Введите количество участников: '))
for i in range(1, n + 1):
    print('Введите количество очков за сезон', i, 'участника:', end=' ')
    num = int(input())
    arr.append(num)
print(arr)

result_max = large(arr)
result_min = small(arr)
arr[0] = result_max
arr[-1] = result_min

print(arr)
