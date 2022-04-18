def palindrome(s):
    wrong = [' ', '.', ',', '!', '?', ':', ';', '-']
    s = s.lower()
    for symbol in wrong:
        s = s.replace(symbol, '')
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True


print(palindrome(txt_str))
