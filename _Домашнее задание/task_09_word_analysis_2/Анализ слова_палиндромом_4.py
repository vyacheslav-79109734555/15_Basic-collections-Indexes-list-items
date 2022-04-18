string = input('Введите текст: ').replace(' ', '').lower()
if string[0::] == string[::-1]:
    print('Да')
else:
    print('Нет')
