print('Замена символа')
# Слово
# Номер символа в слове
# Чем заменяем
# выходные данные:
# Новое слово

word = input('Введите слово: ')
replace_num = int(input('Номер символа для замены: '))
replace_sym = input('Чем заменяем: ')
new_word = ''
count = 0
for sym in word:
    count += 1
    if replace_num != count:
        new_word += sym
    else:
        new_word += replace_sym

print(new_word)
