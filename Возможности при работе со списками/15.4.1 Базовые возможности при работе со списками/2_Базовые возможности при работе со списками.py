print('Очки игроков')

# Условие задачи:
# scores - список очков
# Очки второго игрока += длина списка
# Добавляется новый игрок
# Очки третьего игрока += длина списка
# Выходные данные:
# scores
#


scores = [8, 5, 10, 7, 6]
scores[1] += len(scores)
scores.append(0)
scores[3] += len(scores)
scores.append(1)
print(scores)


b = len(scores) - 1

print(b)
print(scores[0])
print(scores[- 1])
