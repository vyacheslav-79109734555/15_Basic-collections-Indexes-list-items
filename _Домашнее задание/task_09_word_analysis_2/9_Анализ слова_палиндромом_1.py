text = list(input('Введите слово: '))
palindrome_list = list(reversed(text))
x = ''
for i in range(len(text)):
    if text[i] == palindrome_list[i]:
        x = ''
    else:
        x = 'не '

print(f'Слово: {text}, {x}является палиндромом')

print(f'\nпалиндромом: {palindrome_list}')
