print('Подсчет слов')
#
# Входные данные:
# Три слова
# Текст (вводиться по словам, в конце "end"
# Выходные данные:
# Кол-во каждого из трех слов в тексте
#
words_list = []
counts = [0, 0, 0]

for i in range(3):
    print('Введите', i + 1, 'слово:', end=' ')
    word = input()
    words_list.append(word)

text = input('Слово из текста: ')

while text != 'end':
    for index in range(3):
        if words_list[index] == text:
            counts[index] += 1
    text = input('Слово из текста: ')

print('\nПодсчет слов в тексте')
for i in range(3):
    print(words_list[i], ':', counts[i])
