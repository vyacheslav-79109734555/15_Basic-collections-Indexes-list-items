# топот
# я иду с мечем судия
# Делу - тело, лету - лед
# А за работу дадут? - Оба раза!

def palindrome(s):
    s_palin = ''
    for i in range(len(s) - 1, -1, -1):
        s_palin += s[i]
    return s == s_palin


# ********************************
txt_str = input('Введите строку: ')
txt_set = palindrome(txt_str)
print('txt_set', txt_set)


# TODO ******************************** хорошее решение
def palindrome(s):
    wrong = [' ', '.', ',', '!', '?', ':', ';', '-']
    s = s.lower()
    for symbol in wrong:
        s = s.replace(symbol, '')
    return s == s[:: -1]


print(palindrome(txt_str))

