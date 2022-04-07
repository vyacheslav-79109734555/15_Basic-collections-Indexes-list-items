number_list = [1, 5, 2, -7, 6]
for _ in range(5):
    new_numb = int(input('Введите число: '))
    number_list.append(new_numb)
for number in number_list:
    print(number, '** 2 =', number ** 2)
