print('Замена символа')
# Слово
# Номер символа в слове
# Чем заменяем
# выходные данные:
# Новое слово

word = input('Введите слово: ')
replace_num = int(input('Номер символа для замены: '))
replace_sym = input('Чем заменяем: ')

sym_list = []
for sym in word:
    sym_list.append(sym)
sym_list[replace_num - 1] = replace_sym

for i in sym_list:
    print(i, end='')
