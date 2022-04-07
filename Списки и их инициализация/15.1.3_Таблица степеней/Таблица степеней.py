numbers = [3, 7, 5]
while True:
    numb = int(input('Введите число: '))
    numbers.append(numb)
    print('Текущий список чисел: ', numbers)

    for i in numbers:
        print(i ** 2, i ** 3, i ** 4)
    print()
