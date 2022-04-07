# Задача 6. Анализ слова
# Мы пишем программу-анализатор слов, чтобы потом, возможно, использовать
# её для тренировки нейросети, которая будет генерировать нужный нам текст.
#
# Пользователь вводит слово. Напишите программу, которая считает количество
# уникальных букв в слове. Уникальные буквы это те, которые встречаются всего один раз.
#
# #### Пример 1:
# ```
# Введите слово: привет
# Кол-во уникальных букв: 6
# ```
# #### Пример 2:
# ```
# Введите слово: лава
# Кол-во уникальных букв: 2
# ```

text = list(input('Введите слово: '))
count = 0
for sym in text:
    x = 0
    for i in text:
        if sym == i:
            x += 1
    if x < 2:
        count += 1
# print(text)
print('Кол-во уникальных букв:', count)

